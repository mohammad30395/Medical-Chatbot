"""Tests for the Pinecone ingestion pipeline."""

import contextlib
import io
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from langchain_core.documents import Document

from src.config import Settings
from src.indexing import (
    IndexingError,
    clear_namespace,
    deterministic_vector_id,
    deterministic_vector_ids,
    ingest_documents,
    sanitize_metadata,
)


class FakeEmbeddings:
    def embed_query(self, text: str) -> list[float]:
        return [0.0] * 384


class FakeIndex:
    def __init__(self) -> None:
        self.deleted_namespace: str | None = None

    def delete(self, *, delete_all: bool, namespace: str) -> None:
        if delete_all:
            self.deleted_namespace = namespace

    def describe_index_stats(self) -> dict[str, object]:
        return {"namespaces": {"medical-chatbot-v1": {"vector_count": 2}}}


class FakeVectorStore:
    instances: list["FakeVectorStore"] = []
    returned_ids: list[str] | None = None

    def __init__(self, *, index: FakeIndex, embedding: FakeEmbeddings, namespace: str) -> None:
        self.index = index
        self.embedding = embedding
        self.namespace = namespace
        self.added_ids: list[str] = []
        FakeVectorStore.instances.append(self)

    def add_documents(
        self,
        documents: list[Document],
        *,
        ids: list[str],
        namespace: str,
    ) -> list[str]:
        self.documents = documents
        self.added_ids = ids
        self.add_namespace = namespace
        return self.returned_ids if self.returned_ids is not None else ids

    def similarity_search(
        self,
        query: str,
        *,
        k: int,
        namespace: str,
    ) -> list[Document]:
        self.query = query
        self.query_k = k
        self.query_namespace = namespace
        return [Document(page_content="match", metadata={"source": "fixture.pdf"})]


class IndexingTests(unittest.TestCase):
    def setUp(self) -> None:
        FakeVectorStore.instances = []
        FakeVectorStore.returned_ids = None
        self.settings = Settings(
            pinecone_api_key="test-key",
            pinecone_index_name="medical-bot",
            pinecone_namespace="medical-chatbot-v1",
            data_dir="data",
        )

    def test_deterministic_vector_ids_are_stable_and_content_sensitive(self) -> None:
        document = Document(
            page_content="same content",
            metadata={"source": "fixture.pdf", "page": 1, "chunk_index": 0},
        )
        same = Document(
            page_content="same content",
            metadata={"source": "fixture.pdf", "page": 1, "chunk_index": 0},
        )
        changed = Document(
            page_content="changed content",
            metadata={"source": "fixture.pdf", "page": 1, "chunk_index": 0},
        )

        self.assertEqual(deterministic_vector_id(document), deterministic_vector_id(same))
        self.assertNotEqual(
            deterministic_vector_id(document),
            deterministic_vector_id(changed),
        )

    def test_clear_namespace_requires_confirmation(self) -> None:
        index = FakeIndex()

        with self.assertRaisesRegex(IndexingError, "--yes-rebuild-namespace"):
            clear_namespace(index, "medical-chatbot-v1", confirmed=False)

        self.assertIsNone(index.deleted_namespace)

    def test_clear_namespace_deletes_only_configured_namespace_when_confirmed(self) -> None:
        index = FakeIndex()

        clear_namespace(index, "medical-chatbot-v1", confirmed=True)

        self.assertEqual(index.deleted_namespace, "medical-chatbot-v1")

    def test_sanitize_metadata_keeps_supported_values_only(self) -> None:
        document = Document(
            page_content="text",
            metadata={
                "source": "fixture.pdf",
                "page": 0,
                "tags": ["a", "b"],
                "unsupported": {"nested": "dict"},
            },
        )

        sanitized = sanitize_metadata([document])[0]

        self.assertEqual(sanitized.metadata["source"], "fixture.pdf")
        self.assertEqual(sanitized.metadata["page"], 0)
        self.assertEqual(sanitized.metadata["tags"], ["a", "b"])
        self.assertNotIn("unsupported", sanitized.metadata)

    @patch("src.indexing.PineconeVectorStore", FakeVectorStore)
    @patch("src.indexing.get_embeddings", return_value=FakeEmbeddings())
    @patch("src.indexing.ensure_pinecone_index", return_value=FakeIndex())
    @patch("src.indexing.count_pdfs", return_value=1)
    @patch("src.indexing.split_documents")
    @patch("src.indexing.load_pdf_documents")
    def test_ingest_documents_upserts_with_deterministic_ids_and_namespace(
        self,
        mock_load_pdf_documents,
        mock_split_documents,
        mock_count_pdfs,
        mock_ensure_pinecone_index,
        mock_get_embeddings,
    ) -> None:
        pages = [
            Document(
                page_content="page text",
                metadata={"source": "fixture.pdf", "page": 0},
            )
        ]
        chunks = [
            Document(
                page_content="chunk one",
                metadata={"source": "fixture.pdf", "page": 0, "chunk_index": 0},
            ),
            Document(
                page_content="chunk two",
                metadata={"source": "fixture.pdf", "page": 0, "chunk_index": 1},
            ),
        ]
        mock_load_pdf_documents.return_value = pages
        mock_split_documents.return_value = chunks

        result = ingest_documents(settings=self.settings)

        expected_ids = deterministic_vector_ids(chunks)
        vector_store = FakeVectorStore.instances[0]
        self.assertEqual(vector_store.added_ids, expected_ids)
        self.assertEqual(vector_store.add_namespace, "medical-chatbot-v1")
        self.assertEqual(vector_store.query_namespace, "medical-chatbot-v1")
        self.assertEqual(result.chunk_count, 2)
        self.assertEqual(result.upserted_count, 2)
        self.assertEqual(result.stats_vector_count, 2)
        self.assertEqual(result.similarity_match_count, 1)

    @patch("src.indexing.PineconeVectorStore", FakeVectorStore)
    @patch("src.indexing.get_embeddings", return_value=FakeEmbeddings())
    @patch("src.indexing.ensure_pinecone_index", return_value=FakeIndex())
    @patch("src.indexing.split_documents")
    @patch("src.indexing.load_pdf_documents")
    def test_ingest_documents_detects_id_collisions(
        self,
        mock_load_pdf_documents,
        mock_split_documents,
        mock_ensure_pinecone_index,
        mock_get_embeddings,
    ) -> None:
        mock_load_pdf_documents.return_value = [
            Document(page_content="page", metadata={"source": "fixture.pdf"})
        ]
        mock_split_documents.return_value = [
            Document(page_content="same", metadata={"source": "fixture.pdf", "chunk_index": 0}),
            Document(page_content="same", metadata={"source": "fixture.pdf", "chunk_index": 0}),
        ]

        with self.assertRaisesRegex(IndexingError, "collision"):
            ingest_documents(settings=self.settings)

    @patch("src.indexing.PineconeVectorStore", FakeVectorStore)
    @patch("src.indexing.get_embeddings", return_value=FakeEmbeddings())
    @patch("src.indexing.ensure_pinecone_index", return_value=FakeIndex())
    @patch("src.indexing.split_documents")
    @patch("src.indexing.load_pdf_documents")
    def test_ingest_documents_detects_upsert_count_mismatch(
        self,
        mock_load_pdf_documents,
        mock_split_documents,
        mock_ensure_pinecone_index,
        mock_get_embeddings,
    ) -> None:
        mock_load_pdf_documents.return_value = [
            Document(page_content="page", metadata={"source": "fixture.pdf"})
        ]
        mock_split_documents.return_value = [
            Document(page_content="chunk one", metadata={"source": "fixture.pdf", "chunk_index": 0}),
            Document(page_content="chunk two", metadata={"source": "fixture.pdf", "chunk_index": 1}),
        ]
        FakeVectorStore.returned_ids = ["only-one-id"]

        with self.assertRaisesRegex(IndexingError, "unexpected ID count"):
            ingest_documents(settings=self.settings)


class StoreIndexIngestCLITests(unittest.TestCase):
    @patch("store_index.ingest_documents")
    def test_ingest_cli_returns_success(self, mock_ingest_documents) -> None:
        mock_ingest_documents.return_value = SimpleNamespace(
            index_name="medical-bot",
            namespace="medical-chatbot-v1",
            pdf_count=1,
            page_count=2,
            chunk_count=3,
            upserted_count=3,
            stats_vector_count=3,
            similarity_match_count=1,
        )

        from store_index import main

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(main(["--ingest"]), 0)
        self.assertNotIn("test-key", output.getvalue())

    @patch("store_index.ingest_documents")
    def test_rebuild_cli_passes_confirmation_flags(self, mock_ingest_documents) -> None:
        mock_ingest_documents.return_value = SimpleNamespace(
            index_name="medical-bot",
            namespace="medical-chatbot-v1",
            pdf_count=1,
            page_count=2,
            chunk_count=3,
            upserted_count=3,
            stats_vector_count=None,
            similarity_match_count=1,
        )

        from store_index import main

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(
                main(["--ingest", "--rebuild", "--yes-rebuild-namespace"]),
                0,
            )
        mock_ingest_documents.assert_called_once_with(
            rebuild=True,
            confirm_rebuild=True,
        )


if __name__ == "__main__":
    unittest.main()
