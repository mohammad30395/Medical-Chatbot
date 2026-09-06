"""Document ingestion pipeline for Pinecone."""

from __future__ import annotations

import hashlib
import logging
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore

from src.config import Settings, load_settings
from src.helper import (
    EXPECTED_EMBEDDING_DIMENSION,
    get_embeddings,
    load_pdf_documents,
    split_documents,
    verify_embedding_dimension,
)
from src.pinecone_index import ensure_pinecone_index


SIMILARITY_PROBE = "general health information"
DEFAULT_STATS_TIMEOUT_SECONDS = 60
DEFAULT_STATS_POLL_INTERVAL_SECONDS = 5


class IndexingError(RuntimeError):
    """Raised when document ingestion cannot complete safely."""


@dataclass(frozen=True)
class IndexingResult:
    """Summary of a completed ingestion run."""

    pdf_count: int
    page_count: int
    chunk_count: int
    upserted_count: int
    namespace: str
    index_name: str
    stats_vector_count: int | None
    similarity_match_count: int


def _source_for_id(document: Document) -> str:
    source = document.metadata.get("source", "")
    try:
        return str(Path(str(source)).resolve())
    except OSError:
        return str(source)


def deterministic_vector_id(document: Document) -> str:
    """Create a stable vector ID from source, page, chunk index, and content."""
    source = _source_for_id(document)
    page = document.metadata.get("page", "")
    chunk_index = document.metadata.get("chunk_index", "")
    content_hash = hashlib.sha256(document.page_content.encode("utf-8")).hexdigest()
    stable_key = f"{source}|{page}|{chunk_index}|{content_hash}"
    return hashlib.sha256(stable_key.encode("utf-8")).hexdigest()


def deterministic_vector_ids(documents: Iterable[Document]) -> list[str]:
    """Create deterministic vector IDs for a sequence of documents."""
    return [deterministic_vector_id(document) for document in documents]


def _metadata_value_supported(value: Any) -> bool:
    if isinstance(value, (str, int, float, bool)):
        return True
    if isinstance(value, list):
        return all(isinstance(item, (str, int, float, bool)) for item in value)
    return False


def sanitize_metadata(documents: list[Document]) -> list[Document]:
    """Return copies with Pinecone-compatible metadata values."""
    sanitized_documents: list[Document] = []
    for document in documents:
        metadata = {
            key: value
            for key, value in document.metadata.items()
            if _metadata_value_supported(value)
        }
        sanitized_documents.append(
            Document(page_content=document.page_content, metadata=metadata)
        )
    return sanitized_documents


def count_pdfs(data_dir: str | Path) -> int:
    """Count PDF files case-insensitively in a data directory."""
    root = Path(data_dir).expanduser()
    if not root.is_absolute():
        root = Path.cwd() / root
    if not root.exists() or not root.is_dir():
        return 0
    return sum(
        1
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() == ".pdf"
    )


def clear_namespace(index: Any, namespace: str, *, confirmed: bool) -> None:
    """Clear only the configured namespace when explicitly confirmed."""
    if not confirmed:
        raise IndexingError(
            "Refusing to rebuild without explicit confirmation. Rerun with "
            "--rebuild --yes-rebuild-namespace to clear only the configured "
            f"namespace '{namespace}'."
        )
    index.delete(delete_all=True, namespace=namespace)


def _get_stats_vector_count(index: Any, namespace: str) -> int | None:
    try:
        stats = index.describe_index_stats()
    except Exception:
        return None

    namespaces = getattr(stats, "namespaces", None)
    if namespaces is None and isinstance(stats, dict):
        namespaces = stats.get("namespaces")
    if not namespaces:
        return None

    namespace_stats = namespaces.get(namespace)
    if namespace_stats is None:
        return 0

    if isinstance(namespace_stats, dict):
        vector_count = namespace_stats.get("vector_count")
    else:
        vector_count = getattr(namespace_stats, "vector_count", None)
    return int(vector_count) if vector_count is not None else None


def wait_for_namespace_count(
    index: Any,
    namespace: str,
    expected_count: int,
    *,
    timeout_seconds: int = DEFAULT_STATS_TIMEOUT_SECONDS,
    poll_interval_seconds: int = DEFAULT_STATS_POLL_INTERVAL_SECONDS,
) -> int | None:
    """Poll stats until namespace count reaches the expected chunk count."""
    deadline = time.monotonic() + timeout_seconds
    last_count: int | None = None

    while time.monotonic() <= deadline:
        last_count = _get_stats_vector_count(index, namespace)
        if last_count is None or last_count >= expected_count:
            return last_count
        time.sleep(poll_interval_seconds)

    return last_count


def ingest_documents(
    *,
    settings: Settings | None = None,
    rebuild: bool = False,
    confirm_rebuild: bool = False,
) -> IndexingResult:
    """Load PDFs, split chunks, embed locally, and upsert to Pinecone."""
    resolved_settings = settings or load_settings()
    resolved_settings.validate_for_indexing()
    namespace = resolved_settings.pinecone_namespace

    logging.getLogger("pypdf").setLevel(logging.ERROR)

    index = ensure_pinecone_index(resolved_settings)
    if rebuild:
        clear_namespace(index, namespace, confirmed=confirm_rebuild)

    documents = load_pdf_documents(resolved_settings.data_dir)
    chunks = split_documents(documents)
    if not chunks:
        raise IndexingError("No document chunks were produced from the PDF inputs.")

    ids = deterministic_vector_ids(chunks)
    if len(ids) != len(set(ids)):
        raise IndexingError("Deterministic vector ID collision detected.")

    embeddings = get_embeddings()
    verify_embedding_dimension(embeddings)

    sanitized_chunks = sanitize_metadata(chunks)
    vector_store = PineconeVectorStore(
        index=index,
        embedding=embeddings,
        namespace=namespace,
    )
    upserted_ids = vector_store.add_documents(
        sanitized_chunks,
        ids=ids,
        namespace=namespace,
    )
    if len(upserted_ids) != len(ids):
        raise IndexingError(
            "Pinecone upsert returned an unexpected ID count: "
            f"expected {len(ids)}, got {len(upserted_ids)}."
        )

    stats_vector_count = wait_for_namespace_count(index, namespace, len(chunks))
    matches = vector_store.similarity_search(
        SIMILARITY_PROBE,
        k=1,
        namespace=namespace,
    )
    if not matches:
        raise IndexingError("Similarity query returned no documents after indexing.")

    return IndexingResult(
        pdf_count=count_pdfs(resolved_settings.data_dir),
        page_count=len(documents),
        chunk_count=len(chunks),
        upserted_count=len(upserted_ids),
        namespace=namespace,
        index_name=resolved_settings.pinecone_index_name,
        stats_vector_count=stats_vector_count,
        similarity_match_count=len(matches),
    )
