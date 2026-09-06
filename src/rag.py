"""Retrieval helpers for the medical chatbot."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore

from src.config import Settings, load_settings
from src.helper import get_embeddings
from src.pinecone_index import ensure_pinecone_index


RETRIEVER_SEARCH_KWARGS = {"k": 3}
PREVIEW_MAX_CHARS = 160


@dataclass(frozen=True)
class RetrievalPreview:
    """Small, safe-to-print retrieval diagnostic row."""

    rank: int
    source: str
    page: object
    preview: str


def get_vector_store(
    *,
    settings: Settings | None = None,
    index: Any | None = None,
    embeddings: Any | None = None,
) -> PineconeVectorStore:
    """Connect to the configured Pinecone vector store namespace."""
    resolved_settings = settings or load_settings()
    resolved_settings.validate_for_indexing()
    pinecone_index = index or ensure_pinecone_index(resolved_settings)
    embedding_model = embeddings or get_embeddings()
    return PineconeVectorStore(
        index=pinecone_index,
        embedding=embedding_model,
        namespace=resolved_settings.pinecone_namespace,
    )


def get_retriever(
    *,
    vector_store: Any | None = None,
    settings: Settings | None = None,
) -> Any:
    """Create the tutorial-compatible retriever with k=3."""
    resolved_vector_store = vector_store or get_vector_store(settings=settings)
    return resolved_vector_store.as_retriever(
        search_kwargs=dict(RETRIEVER_SEARCH_KWARGS),
    )


def _short_preview(text: str, *, max_chars: int = PREVIEW_MAX_CHARS) -> str:
    normalized = re.sub(r"\s+", " ", text).strip()
    if len(normalized) <= max_chars:
        return normalized
    return normalized[: max_chars - 3].rstrip() + "..."


def retrieval_previews(
    query: str,
    *,
    retriever: Any | None = None,
) -> list[RetrievalPreview]:
    """Retrieve top documents and return compact metadata previews."""
    if not query.strip():
        raise ValueError("Query must not be empty.")

    resolved_retriever = retriever or get_retriever()
    documents: list[Document] = resolved_retriever.invoke(query)
    previews: list[RetrievalPreview] = []
    for rank, document in enumerate(documents[: RETRIEVER_SEARCH_KWARGS["k"]], start=1):
        previews.append(
            RetrievalPreview(
                rank=rank,
                source=str(document.metadata.get("source", "unknown")),
                page=document.metadata.get("page", "unknown"),
                preview=_short_preview(document.page_content),
            )
        )
    return previews


def print_retrieval_diagnostics(query: str) -> None:
    """Print rank, source, page, and a short preview for the top matches."""
    for item in retrieval_previews(query):
        print(f"{item.rank}\t{item.source}\t{item.page}\t{item.preview}")
