"""PDF loading helpers for the medical chatbot."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from langchain_core.documents import Document

from src.config import ConfigurationError, Settings, load_settings
from src.helper_constants import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    EMBEDDING_MODEL,
    EXPECTED_EMBEDDING_DIMENSION,
)
from src.remote_embeddings import HuggingFaceAPIEmbeddings


PyPDFLoader: Any | None = None
RecursiveCharacterTextSplitter: Any | None = None
HuggingFaceEmbeddings: Any | None = None


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


def _get_pdf_loader_class() -> Any:
    global PyPDFLoader
    if PyPDFLoader is None:
        from langchain_community.document_loaders import PyPDFLoader as loader_class

        PyPDFLoader = loader_class
    return PyPDFLoader


def _get_text_splitter_class() -> Any:
    global RecursiveCharacterTextSplitter
    if RecursiveCharacterTextSplitter is None:
        from langchain_text_splitters import (
            RecursiveCharacterTextSplitter as splitter_class,
        )

        RecursiveCharacterTextSplitter = splitter_class
    return RecursiveCharacterTextSplitter


def _get_huggingface_embeddings_class() -> Any:
    global HuggingFaceEmbeddings
    if HuggingFaceEmbeddings is None:
        from langchain_huggingface import HuggingFaceEmbeddings as embeddings_class

        HuggingFaceEmbeddings = embeddings_class
    return HuggingFaceEmbeddings


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
            loaded_documents = _get_pdf_loader_class()(str(pdf_file)).load()
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

    splitter = _get_text_splitter_class()(
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


def _get_local_embeddings() -> Any:
    """Create local CPU Hugging Face embeddings for retrieval."""
    return _get_huggingface_embeddings_class()(
        model=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
        show_progress=False,
    )


def _get_remote_embeddings(settings: Settings) -> HuggingFaceAPIEmbeddings:
    if not settings.hf_token.strip():
        raise ConfigurationError(
            "Missing required environment variable: HF_TOKEN. "
            "Set HF_TOKEN in .env locally or as a Vercel environment variable."
        )
    return HuggingFaceAPIEmbeddings(
        api_key=settings.hf_token,
        model=settings.huggingface_embedding_model,
        provider=settings.huggingface_inference_provider,
        timeout_seconds=settings.huggingface_timeout_seconds,
    )


def get_embeddings(
    *,
    settings: Settings | None = None,
    provider: str | None = None,
) -> Any:
    """Create embeddings for the selected runtime strategy."""
    selected_provider = provider
    resolved_settings = settings
    if selected_provider is None:
        selected_provider = (
            resolved_settings.embeddings_provider
            if resolved_settings is not None
            else "local"
        )

    if selected_provider == "local":
        return _get_local_embeddings()
    if selected_provider == "huggingface_api":
        resolved_settings = resolved_settings or load_settings()
        return _get_remote_embeddings(resolved_settings)
    raise ConfigurationError(
        "Invalid EMBEDDINGS_PROVIDER value. Expected local or huggingface_api."
    )


def download_hugging_face_embeddings() -> Any:
    """Tutorial-compatible alias for creating Hugging Face embeddings."""
    return get_embeddings()


def verify_embedding_dimension(embeddings: Any) -> int:
    """Verify the embedding model returns the expected vector dimension."""
    vector = embeddings.embed_query("health information retrieval test")
    dimension = len(vector)
    if dimension != EXPECTED_EMBEDDING_DIMENSION:
        raise ValueError(
            f"Expected embedding dimension {EXPECTED_EMBEDDING_DIMENSION}, "
            f"got {dimension}."
        )
    return dimension
