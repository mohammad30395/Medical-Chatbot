"""Tests for hosted embedding adapters."""

import unittest

from src.helper_constants import EXPECTED_EMBEDDING_DIMENSION
from src.remote_embeddings import HuggingFaceAPIEmbeddings, RemoteEmbeddingError


class FakeInferenceClient:
    response = None
    error: Exception | None = None
    calls: list[dict[str, object]] = []

    def __init__(self, **kwargs: object) -> None:
        self.kwargs = kwargs

    def feature_extraction(self, text: str | list[str], **kwargs: object) -> object:
        if self.error is not None:
            raise self.error
        self.calls.append({"text": text, **kwargs})
        return self.response


class RemoteEmbeddingTests(unittest.TestCase):
    def setUp(self) -> None:
        FakeInferenceClient.response = [0.1] * EXPECTED_EMBEDDING_DIMENSION
        FakeInferenceClient.error = None
        FakeInferenceClient.calls = []

    def _embeddings(self) -> HuggingFaceAPIEmbeddings:
        return HuggingFaceAPIEmbeddings(
            api_key="hf_test_secret",
            client_factory=FakeInferenceClient,
        )

    def test_embed_query_returns_384_dimensions(self) -> None:
        vector = self._embeddings().embed_query("medical query")

        self.assertEqual(len(vector), EXPECTED_EMBEDDING_DIMENSION)
        self.assertEqual(
            FakeInferenceClient.calls[0]["model"],
            "sentence-transformers/all-MiniLM-L6-v2",
        )
        self.assertTrue(FakeInferenceClient.calls[0]["normalize"])
        self.assertTrue(FakeInferenceClient.calls[0]["truncate"])

    def test_embed_documents_handles_batch_vectors(self) -> None:
        FakeInferenceClient.response = [
            [0.1] * EXPECTED_EMBEDDING_DIMENSION,
            [0.2] * EXPECTED_EMBEDDING_DIMENSION,
        ]

        vectors = self._embeddings().embed_documents(["one", "two"])

        self.assertEqual(len(vectors), 2)
        self.assertEqual(len(vectors[0]), EXPECTED_EMBEDDING_DIMENSION)
        self.assertEqual(FakeInferenceClient.calls[0]["text"], ["one", "two"])

    def test_embed_documents_empty_input_returns_empty_list(self) -> None:
        self.assertEqual(self._embeddings().embed_documents([]), [])
        self.assertEqual(FakeInferenceClient.calls, [])

    def test_malformed_dimension_raises_clear_error(self) -> None:
        FakeInferenceClient.response = [0.1] * 128

        with self.assertRaisesRegex(RemoteEmbeddingError, "Expected embedding dimension"):
            self._embeddings().embed_query("medical query")

    def test_remote_error_redacts_token(self) -> None:
        FakeInferenceClient.error = RuntimeError("failed with hf_test_secret")

        with self.assertRaises(RemoteEmbeddingError) as context:
            self._embeddings().embed_query("medical query")

        message = str(context.exception)
        self.assertIn("[redacted]", message)
        self.assertNotIn("hf_test_secret", message)


if __name__ == "__main__":
    unittest.main()
