"""Tests for PDF loading helpers."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from langchain_core.documents import Document

from src.helper import PDFLoadError, load_pdf_documents


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


if __name__ == "__main__":
    unittest.main()
