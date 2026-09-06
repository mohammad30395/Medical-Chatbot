"""PDF loading helpers for the medical chatbot."""

from __future__ import annotations

from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


CHUNK_SIZE = 500
CHUNK_OVERLAP = 20
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EXPECTED_EMBEDDING_DIMENSION = 384


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
        path
        for path in data_dir.rglob("*")
        if path.is_file() and path.suffix.lower() == ".pdf"
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


def split_documents(documents: list[Document]) -> list[Document]:
    """Split documents into retrieval-sized chunks while preserving metadata."""
    if not documents:
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    chunks = splitter.split_documents(documents)

    chunk_counts: dict[tuple[str, object], int] = {}
    for chunk in chunks:
        source = str(chunk.metadata.get("source", ""))
        page = chunk.metadata.get("page")
        key = (source, page)
        chunk_index = chunk_counts.get(key, 0)
        chunk.metadata["chunk_index"] = chunk_index
        chunk_counts[key] = chunk_index + 1

    return chunks


def get_embeddings() -> HuggingFaceEmbeddings:
    """Create local CPU Hugging Face embeddings for retrieval."""
    return HuggingFaceEmbeddings(
        model=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
        show_progress=False,
    )


def download_hugging_face_embeddings() -> HuggingFaceEmbeddings:
    """Tutorial-compatible alias for creating Hugging Face embeddings."""
    return get_embeddings()


def verify_embedding_dimension(embeddings: HuggingFaceEmbeddings) -> int:
    """Verify the embedding model returns the expected vector dimension."""
    vector = embeddings.embed_query("health information retrieval test")
    dimension = len(vector)
    if dimension != EXPECTED_EMBEDDING_DIMENSION:
        raise ValueError(
            f"Expected embedding dimension {EXPECTED_EMBEDDING_DIMENSION}, "
            f"got {dimension}."
        )
    return dimension
