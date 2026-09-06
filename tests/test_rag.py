"""Tests for retriever construction and diagnostics."""

import contextlib
import io
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from langchain_core.documents import Document

from src.config import ConfigurationError, Settings, load_settings
from src.rag import (
    LLM_MAX_RETRIES,
    LLM_MAX_TOKENS,
    LLM_SMOKE_PROMPT,
    LLM_TEMPERATURE,
    LLM_TIMEOUT_SECONDS,
    LLMError,
    PREVIEW_MAX_CHARS,
    RETRIEVER_SEARCH_KWARGS,
    get_llm,
    get_retriever,
    get_vector_store,
    print_retrieval_diagnostics,
    retrieval_previews,
    smoke_test_llm,
)


class FakeVectorStore:
    instances: list["FakeVectorStore"] = []

    def __init__(self, *, index: object, embedding: object, namespace: str) -> None:
        self.index = index
        self.embedding = embedding
        self.namespace = namespace
        self.retriever_kwargs: dict[str, object] | None = None
        FakeVectorStore.instances.append(self)

    def as_retriever(self, **kwargs: object) -> SimpleNamespace:
        self.retriever_kwargs = kwargs
        return SimpleNamespace(search_kwargs=kwargs.get("search_kwargs"))


class FakeRetriever:
    def invoke(self, query: str) -> list[Document]:
        return [
            Document(
                page_content=" ".join(["medical"] * 60),
                metadata={"source": "fixture.pdf", "page": 4},
            ),
            Document(
                page_content="short preview",
                metadata={"source": "other.pdf", "page": 9},
            ),
        ]


class FakeChatOpenRouter:
    instances: list["FakeChatOpenRouter"] = []
    response_content = "OK"
    invoke_error: Exception | None = None

    def __init__(self, **kwargs: object) -> None:
        self.kwargs = kwargs
        self.invocations: list[str] = []
        FakeChatOpenRouter.instances.append(self)

    def invoke(self, prompt: str) -> SimpleNamespace:
        self.invocations.append(prompt)
        if self.invoke_error is not None:
            raise self.invoke_error
        return SimpleNamespace(content=self.response_content)


class RagUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        FakeVectorStore.instances = []
        FakeChatOpenRouter.instances = []
        FakeChatOpenRouter.response_content = "OK"
        FakeChatOpenRouter.invoke_error = None
        self.settings = Settings(
            pinecone_api_key="test-key",
            pinecone_index_name="medical-bot",
            pinecone_namespace="medical-chatbot-v1",
            openrouter_api_key="dummy-openrouter-key",
            openrouter_model="openrouter/free",
        )

    @patch("src.rag.PineconeVectorStore", FakeVectorStore)
    @patch("src.rag.get_embeddings", return_value=SimpleNamespace(name="embeddings"))
    @patch("src.rag.ensure_pinecone_index", return_value=SimpleNamespace(name="index"))
    def test_get_vector_store_uses_configured_namespace(
        self,
        mock_ensure_pinecone_index,
        mock_get_embeddings,
    ) -> None:
        vector_store = get_vector_store(settings=self.settings)

        self.assertIs(vector_store, FakeVectorStore.instances[0])
        self.assertEqual(vector_store.namespace, "medical-chatbot-v1")
        mock_ensure_pinecone_index.assert_called_once_with(self.settings)
        mock_get_embeddings.assert_called_once_with()

    def test_get_retriever_preserves_tutorial_k_setting(self) -> None:
        vector_store = FakeVectorStore(index=object(), embedding=object(), namespace="ns")

        retriever = get_retriever(vector_store=vector_store)

        self.assertEqual(RETRIEVER_SEARCH_KWARGS, {"k": 3})
        self.assertEqual(retriever.search_kwargs, {"k": 3})
        self.assertEqual(vector_store.retriever_kwargs, {"search_kwargs": {"k": 3}})

    def test_retrieval_previews_are_short_and_metadata_only(self) -> None:
        previews = retrieval_previews("normal medical query", retriever=FakeRetriever())

        self.assertEqual(len(previews), 2)
        self.assertEqual(previews[0].rank, 1)
        self.assertEqual(previews[0].source, "fixture.pdf")
        self.assertEqual(previews[0].page, 4)
        self.assertLessEqual(len(previews[0].preview), PREVIEW_MAX_CHARS)

    def test_print_retrieval_diagnostics_prints_compact_rows(self) -> None:
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            with patch("src.rag.retrieval_previews") as mock_previews:
                mock_previews.return_value = [
                    SimpleNamespace(
                        rank=1,
                        source="fixture.pdf",
                        page=0,
                        preview="short preview",
                    )
                ]
                print_retrieval_diagnostics("query")

        self.assertEqual(output.getvalue(), "1\tfixture.pdf\t0\tshort preview\n")
        self.assertNotIn("test-key", output.getvalue())

    @patch("src.rag.ChatOpenRouter", FakeChatOpenRouter)
    def test_get_llm_uses_openrouter_settings(self) -> None:
        llm = get_llm(settings=self.settings)

        self.assertIs(llm, FakeChatOpenRouter.instances[0])
        self.assertEqual(llm.kwargs["api_key"], "dummy-openrouter-key")
        self.assertEqual(llm.kwargs["model"], "openrouter/free")
        self.assertEqual(llm.kwargs["temperature"], LLM_TEMPERATURE)
        self.assertEqual(llm.kwargs["timeout"], LLM_TIMEOUT_SECONDS * 1000)
        self.assertEqual(llm.kwargs["max_retries"], LLM_MAX_RETRIES)
        self.assertEqual(llm.kwargs["max_tokens"], LLM_MAX_TOKENS)
        self.assertNotIn("OPENAI" + "_API_KEY", llm.kwargs)

    def test_get_llm_missing_openrouter_key_raises_clear_error(self) -> None:
        settings = Settings(openrouter_api_key="")

        with self.assertRaisesRegex(ConfigurationError, "OPENROUTER_API_KEY"):
            get_llm(settings=settings)

    @patch("src.rag.ChatOpenRouter", FakeChatOpenRouter)
    def test_smoke_test_llm_invokes_exactly_once(self) -> None:
        response = smoke_test_llm(settings=self.settings)

        self.assertEqual(response, "OK")
        self.assertEqual(FakeChatOpenRouter.instances[0].invocations, [LLM_SMOKE_PROMPT])

    @patch("src.rag.ChatOpenRouter", FakeChatOpenRouter)
    def test_smoke_test_llm_sanitizes_secret_bearing_errors(self) -> None:
        FakeChatOpenRouter.invoke_error = RuntimeError(
            "401 unauthorized Authorization: Bearer dummy-openrouter-key"
        )

        with self.assertRaises(LLMError) as context:
            smoke_test_llm(settings=self.settings)

        message = str(context.exception)
        self.assertIn("OpenRouter authentication failed", message)
        self.assertIn("[redacted]", message)
        self.assertNotIn("dummy-openrouter-key", message)

    @patch("src.rag.ChatOpenRouter", FakeChatOpenRouter)
    def test_smoke_test_llm_classifies_user_facing_errors(self) -> None:
        cases = (
            ("404 model unavailable", "OpenRouter model unavailable"),
            ("429 quota exceeded", "OpenRouter rate limit or quota exceeded"),
            ("ReadTimeout network failure", "OpenRouter timeout or network failure"),
        )

        for raw_error, expected in cases:
            with self.subTest(raw_error=raw_error):
                FakeChatOpenRouter.instances = []
                FakeChatOpenRouter.invoke_error = RuntimeError(raw_error)

                with self.assertRaises(LLMError) as context:
                    smoke_test_llm(settings=self.settings)

                self.assertIn(expected, str(context.exception))

    @patch("src.rag.ChatOpenRouter", FakeChatOpenRouter)
    def test_smoke_test_llm_empty_response_raises_clear_error(self) -> None:
        FakeChatOpenRouter.response_content = ""

        with self.assertRaisesRegex(LLMError, "empty response"):
            smoke_test_llm(settings=self.settings)


class SmokeScriptTests(unittest.TestCase):
    @patch("scripts.smoke_test.retrieval_previews")
    def test_smoke_script_suppresses_library_output(self, mock_previews) -> None:
        def fake_previews(query: str) -> list[SimpleNamespace]:
            print("library stdout")
            print("library warning", file=sys.stderr)
            return [
                SimpleNamespace(
                    rank=1,
                    source="fixture.pdf",
                    page=0,
                    preview=query,
                )
            ]

        mock_previews.side_effect = fake_previews

        from scripts.smoke_test import main

        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            self.assertEqual(main(["short preview"]), 0)

        self.assertEqual(stdout.getvalue(), "1\tfixture.pdf\t0\tshort preview\n")
        self.assertEqual(stderr.getvalue(), "")


class RagIntegrationTests(unittest.TestCase):
    def test_retriever_returns_one_to_three_documents_when_pinecone_available(self) -> None:
        try:
            settings = load_settings(create_env_file=False)
            settings.validate_for_indexing()
        except ConfigurationError as exc:
            self.skipTest(f"Pinecone configuration unavailable: {exc}")

        try:
            documents = get_retriever(settings=settings).invoke("What is diabetes?")
        except Exception as exc:
            self.skipTest(f"Pinecone retrieval unavailable: {exc}")

        self.assertGreaterEqual(len(documents), 1)
        self.assertLessEqual(len(documents), 3)
        self.assertTrue(all(isinstance(document, Document) for document in documents))


if __name__ == "__main__":
    unittest.main()
