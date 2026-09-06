"""PDF loading helpers for the medical chatbot."""

from __future__ import annotations

from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader


class PDFLoadError(RuntimeError):
    """Raised when a PDF cannot be loaded."""


def _resolve_data_dir(data_dir: str | Path) -> Path:
    path = Path(data_dir).expanduser()
    if not path.is_absolute():
        path = Path.cwd() / path
    return path.resolve()


def _find_pdf_files(data_dir: Path) -> list[Path]:
    if not data_dir.exists() or not data_dir.is_dir():
        return []
    return sorted(
        path for path in data_dir.rglob("*") if path.is_file() and path.suffix.lower() == ".pdf"
    )


def load_pdf_documents(data_dir: str | Path) -> list[Document]:
    """Load all PDFs from a data directory as LangChain documents."""
    resolved_data_dir = _resolve_data_dir(data_dir)
    pdf_files = _find_pdf_files(resolved_data_dir)
    if not pdf_files:
        raise FileNotFoundError(
            f"No PDF files found in {resolved_data_dir}. "
            "Place at least one legally obtained PDF in data/."
        )

    documents: list[Document] = []
    for pdf_file in pdf_files:
        try:
            loaded_documents = PyPDFLoader(str(pdf_file)).load()
        except Exception as exc:
            raise PDFLoadError(f"Failed to load PDF '{pdf_file.name}'.") from exc

        for document in loaded_documents:
            document.metadata.setdefault("source", str(pdf_file))
            documents.append(document)

    return documents
