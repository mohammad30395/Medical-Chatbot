"""Tests for safe Pinecone index management."""

import contextlib
import io
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from src.config import Settings
from src.pinecone_index import (
    PINECONE_INDEX_DIMENSION,
    PINECONE_INDEX_METRIC,
    PINECONE_VECTOR_TYPE,
    PineconeIndexError,
    check_pinecone_index,
    ensure_pinecone_index,
)
from store_index import main


class FakeIndexList:
    def __init__(self, names: list[str]) -> None:
        self._names = names

    def names(self) -> list[str]:
        return self._names


class FakePineconeClient:
    def __init__(
        self,
        *,
        names: list[str] | None = None,
        dimension: int = PINECONE_INDEX_DIMENSION,
        metric: str = PINECONE_INDEX_METRIC,
        vector_type: str = PINECONE_VECTOR_TYPE,
        ready: bool = True,
    ) -> None:
        self.names = names or []
        self.dimension = dimension
        self.metric = metric
        self.vector_type = vector_type
        self.ready = ready
        self.created_with: dict[str, object] | None = None
        self.index_requested: str | None = None

    def list_indexes(self) -> FakeIndexList:
        return FakeIndexList(self.names)

    def create_index(self, **kwargs: object) -> None:
        self.created_with = kwargs
        self.names.append(str(kwargs["name"]))

    def describe_index(self, name: str) -> SimpleNamespace:
        return SimpleNamespace(
            name=name,
            dimension=self.dimension,
            metric=self.metric,
            vector_type=self.vector_type,
            status={"ready": self.ready},
            host=f"{name}.example.pinecone.io",
        )

    def Index(self, name: str) -> SimpleNamespace:
        self.index_requested = name
        return SimpleNamespace(name=name)


class PineconeIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.settings = Settings(
            pinecone_api_key="test-key",
            pinecone_index_name="medical-bot",
            pinecone_cloud="aws",
            pinecone_region="us-east-1",
        )

    @patch("src.pinecone_index.time.sleep", lambda _: None)
    def test_existing_matching_index_returns_index_connection(self) -> None:
        client = FakePineconeClient(names=["medical-bot"])

        index = ensure_pinecone_index(self.settings, pinecone_client=client)

        self.assertEqual(index.name, "medical-bot")
        self.assertIsNone(client.created_with)

    @patch("src.pinecone_index.time.sleep", lambda _: None)
    def test_missing_index_is_created_with_project_contract(self) -> None:
        client = FakePineconeClient()

        ensure_pinecone_index(self.settings, pinecone_client=client)

        self.assertIsNotNone(client.created_with)
        assert client.created_with is not None
        self.assertEqual(client.created_with["name"], "medical-bot")
        self.assertEqual(client.created_with["dimension"], PINECONE_INDEX_DIMENSION)
        self.assertEqual(client.created_with["metric"], PINECONE_INDEX_METRIC)
        self.assertEqual(client.created_with["vector_type"], PINECONE_VECTOR_TYPE)

    def test_existing_mismatched_index_stops_without_delete(self) -> None:
        client = FakePineconeClient(names=["medical-bot"], dimension=1536)

        with self.assertRaisesRegex(PineconeIndexError, "will not delete"):
            ensure_pinecone_index(self.settings, pinecone_client=client)

        self.assertIsNone(client.created_with)

    def test_existing_mismatched_vector_type_stops_without_delete(self) -> None:
        client = FakePineconeClient(names=["medical-bot"], vector_type="sparse")

        with self.assertRaisesRegex(PineconeIndexError, "vector_type is sparse"):
            ensure_pinecone_index(self.settings, pinecone_client=client)

        self.assertIsNone(client.created_with)

    @patch("src.pinecone_index.time.sleep", lambda _: None)
    def test_check_reports_verified_index_contract(self) -> None:
        client = FakePineconeClient(names=["medical-bot"])

        result = check_pinecone_index(self.settings, pinecone_client=client)

        self.assertEqual(result.index_name, "medical-bot")
        self.assertEqual(result.dimension, 384)
        self.assertEqual(result.metric, "cosine")
        self.assertEqual(result.vector_type, "dense")
        self.assertTrue(result.ready)

    @patch("store_index.check_pinecone_index")
    def test_check_index_cli_returns_success_without_printing_secrets(self, mock_check) -> None:
        mock_check.return_value = SimpleNamespace(
            index_name="medical-bot",
            dimension=384,
            metric="cosine",
            vector_type="dense",
            ready=True,
        )
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            exit_code = main(["--check-index"])

        self.assertEqual(exit_code, 0)
        self.assertNotIn("test-key", output.getvalue())


if __name__ == "__main__":
    unittest.main()
