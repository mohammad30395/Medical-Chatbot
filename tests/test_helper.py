"""Tests for PDF loading helpers."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from langchain_core.documents import Document

from src.helper import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    EXPECTED_EMBEDDING_DIMENSION,
    PDFLoadError,
    get_embeddings,
    load_pdf_documents,
    split_documents,
    verify_embedding_dimension,
)
from src.config import Settings


class FakePyPDFLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load(self) -> list[Document]:
        return [
            Document(
                page_content="fixture page",
                metadata={"source": self.file_path, "page": 0},
            )
        ]


class FailingPyPDFLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load(self) -> list[Document]:
        raise ValueError("malformed fixture")


class FakeEmbeddings:
    def __init__(self, dimension: int) -> None:
        self.dimension = dimension

    def embed_query(self, text: str) -> list[float]:
        return [0.0] * self.dimension


class LoadPDFDocumentsTests(unittest.TestCase):
    def test_no_pdf_raises_clear_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            with self.assertRaisesRegex(
                FileNotFoundError,
                "Place at least one legally obtained PDF in data/",
            ):
                load_pdf_documents(temp_dir)

    def test_loads_pdf_case_insensitively_and_preserves_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_path = Path(temp_dir) / "fixture.PDF"
            pdf_path.write_bytes(b"not read because loader is monkeypatched")

            with patch("src.helper.PyPDFLoader", FakePyPDFLoader):
                documents = load_pdf_documents(temp_dir)

        self.assertEqual(len(documents), 1)
        self.assertIsInstance(documents[0], Document)
        self.assertEqual(documents[0].metadata["source"], str(pdf_path.resolve()))
        self.assertEqual(documents[0].metadata["page"], 0)

    def test_loader_errors_include_source_and_preserve_original_exception(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_path = Path(temp_dir) / "broken.pdf"
            pdf_path.write_bytes(b"not a valid pdf")

            with patch("src.helper.PyPDFLoader", FailingPyPDFLoader):
                with self.assertRaisesRegex(PDFLoadError, "broken.pdf") as context:
                    load_pdf_documents(temp_dir)

        self.assertIsInstance(context.exception.__cause__, ValueError)


class SplitDocumentsTests(unittest.TestCase):
    def test_chunk_settings_match_contract(self) -> None:
        self.assertEqual(CHUNK_SIZE, 500)
        self.assertEqual(CHUNK_OVERLAP, 20)

    def test_empty_input_behaves_predictably(self) -> None:
        self.assertEqual(split_documents([]), [])

    def test_metadata_survives_splitting_and_chunk_index_is_added(self) -> None:
        source = "fixture.pdf"
        document = Document(
            page_content=" ".join(f"token{i}" for i in range(160)),
            metadata={"source": source, "page": 2, "custom": "preserved"},
        )

        chunks = split_documents([document])

        self.assertGreater(len(chunks), 1)
        for index, chunk in enumerate(chunks):
            self.assertEqual(chunk.metadata["source"], source)
            self.assertEqual(chunk.metadata["page"], 2)
            self.assertEqual(chunk.metadata["custom"], "preserved")
            self.assertEqual(chunk.metadata["chunk_index"], index)


class EmbeddingTests(unittest.TestCase):
    def test_get_embeddings_uses_remote_provider_when_configured(self) -> None:
        settings = Settings(
            embeddings_provider="huggingface_api",
            hf_token="hf_test_token",
        )

        with patch("src.helper.HuggingFaceAPIEmbeddings") as mock_remote_embeddings:
            get_embeddings(settings=settings)

        mock_remote_embeddings.assert_called_once_with(
            api_key="hf_test_token",
            model="sentence-transformers/all-MiniLM-L6-v2",
            provider="hf-inference",
            timeout_seconds=15,
        )

    def test_get_embeddings_remote_provider_requires_token(self) -> None:
        settings = Settings(embeddings_provider="huggingface_api", hf_token="")

        with self.assertRaisesRegex(Exception, "HF_TOKEN"):
            get_embeddings(settings=settings)

    def test_embedding_dimension_check_returns_384(self) -> None:
        dimension = verify_embedding_dimension(
            FakeEmbeddings(EXPECTED_EMBEDDING_DIMENSION)
        )

        self.assertEqual(dimension, 384)

    def test_embedding_dimension_check_raises_clear_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "Expected embedding dimension 384"):
            verify_embedding_dimension(FakeEmbeddings(128))


if __name__ == "__main__":
    unittest.main()
