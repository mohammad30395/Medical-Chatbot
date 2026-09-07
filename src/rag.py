"""Retrieval helpers for the medical chatbot."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain_core.runnables import RunnablePassthrough
from langchain_openrouter import ChatOpenRouter
from langchain_pinecone import PineconeVectorStore

from src.config import ConfigurationError, Settings, load_settings
from src.helper import get_embeddings
from src.pinecone_index import ensure_pinecone_index
from src.prompt import MEDICAL_QA_PROMPT
from src.remote_embeddings import RemoteEmbeddingError


RETRIEVER_SEARCH_KWARGS = {"k": 3}
PREVIEW_MAX_CHARS = 160
LLM_TEMPERATURE = 0
LLM_TIMEOUT_SECONDS = 15
LLM_MAX_RETRIES = 0
LLM_MAX_TOKENS = 48
LLM_SMOKE_PROMPT = "Reply with exactly: OK"
MAX_QUESTION_CHARS = 2000
MAX_CONTEXT_CHARS_PER_DOCUMENT = 300
EMERGENCY_RESPONSE = (
    "If this may be an emergency, seek urgent professional or emergency help now."
)
QUESTION_TOO_LONG_MESSAGE = (
    f"Question is too long. Limit is {MAX_QUESTION_CHARS} characters."
)
EMERGENCY_PATTERN = re.compile(
    r"\b("
    r"chest pain|can'?t breathe|cannot breathe|trouble breathing|"
    r"severe bleeding|stroke|heart attack|overdose|seizure|"
    r"suicidal|kill myself|self[- ]?harm"
    r")\b",
    flags=re.IGNORECASE,
)


class LLMError(RuntimeError):
    """Raised when OpenRouter LLM setup or invocation fails safely."""


@dataclass(frozen=True)
class RetrievalPreview:
    """Small, safe-to-print retrieval diagnostic row."""

    rank: int
    source: str
    page: object
    preview: str


def _redact_secret_values(message: str, settings: Settings) -> str:
    sanitized = message
    for secret in (
        settings.openrouter_api_key,
        settings.pinecone_api_key,
        settings.hf_token,
    ):
        if secret:
            sanitized = sanitized.replace(secret, "[redacted]")
    sanitized = re.sub(
        r"Bearer\s+[A-Za-z0-9._~+/=-]+",
        "Bearer [redacted]",
        sanitized,
        flags=re.IGNORECASE,
    )
    sanitized = re.sub(
        r"(api[-_]?key['\"]?\s*[:=]\s*['\"]?)[^'\"\s,}]+",
        r"\1[redacted]",
        sanitized,
        flags=re.IGNORECASE,
    )
    sanitized = re.sub(r"sk-or-v1-[A-Za-z0-9_-]+", "[redacted]", sanitized)
    sanitized = re.sub(r"sk-[A-Za-z0-9_-]{20,}", "[redacted]", sanitized)
    return sanitized


def _classify_llm_error(message: str) -> str:
    lowered = message.lower()
    if any(
        text in lowered
        for text in ("401", "403", "unauthorized", "forbidden", "auth")
    ):
        return "OpenRouter authentication failed"
    if any(text in lowered for text in ("404", "not found", "model", "unavailable")):
        return "OpenRouter model unavailable"
    if any(
        text in lowered
        for text in (
            "429",
            "rate limit",
            "quota",
            "insufficient credits",
            "more credits",
            "fewer max_tokens",
            "can only afford",
        )
    ):
        return "OpenRouter rate limit or quota exceeded"
    if any(
        text in lowered
        for text in ("timeout", "timed out", "network", "connection")
    ):
        return "OpenRouter timeout or network failure"
    return "OpenRouter request failed"


def _to_llm_error(exc: Exception, settings: Settings) -> LLMError:
    sanitized = _redact_secret_values(str(exc), settings)
    return LLMError(f"{_classify_llm_error(sanitized)}: {sanitized}")


def _require_openrouter_api_key(settings: Settings) -> None:
    if not settings.openrouter_api_key.strip():
        raise ConfigurationError(
            "Missing required environment variable: OPENROUTER_API_KEY. "
            "Set OPENROUTER_API_KEY in .env."
        )


def get_llm(*, settings: Settings | None = None) -> ChatOpenRouter:
    """Create the configured OpenRouter chat model client."""
    resolved_settings = settings or load_settings()
    _require_openrouter_api_key(resolved_settings)
    try:
        return ChatOpenRouter(
            api_key=resolved_settings.openrouter_api_key,
            model=resolved_settings.openrouter_model,
            temperature=LLM_TEMPERATURE,
            timeout=LLM_TIMEOUT_SECONDS * 1000,
            max_retries=LLM_MAX_RETRIES,
            max_tokens=LLM_MAX_TOKENS,
        )
    except Exception as exc:
        raise _to_llm_error(exc, resolved_settings) from exc


def smoke_test_llm(*, settings: Settings | None = None) -> str:
    """Invoke OpenRouter exactly once with a tiny non-medical prompt."""
    resolved_settings = settings or load_settings()
    _require_openrouter_api_key(resolved_settings)
    llm = get_llm(settings=resolved_settings)
    try:
        response = llm.invoke(LLM_SMOKE_PROMPT)
    except Exception as exc:
        raise _to_llm_error(exc, resolved_settings) from exc

    content = str(getattr(response, "content", "")).strip()
    if not content:
        raise LLMError("OpenRouter returned an empty response.")
    return content


def get_rag_chain(
    *,
    settings: Settings | None = None,
    llm: Any | None = None,
    retriever: Any | None = None,
    prompt: Any = MEDICAL_QA_PROMPT,
) -> Any:
    """Build the tutorial-style retrieval augmented generation chain."""
    resolved_llm = llm or get_llm(settings=settings)
    resolved_retriever = retriever or get_retriever(settings=settings)
    question_answer_chain = create_stuff_documents_chain(resolved_llm, prompt)
    limited_question_answer_chain = RunnablePassthrough.assign(
        context=lambda inputs: limit_documents_for_llm(inputs.get("context", [])),
    ) | question_answer_chain
    return create_retrieval_chain(resolved_retriever, limited_question_answer_chain)


def limit_documents_for_llm(
    documents: list[Document],
    *,
    max_chars_per_document: int = MAX_CONTEXT_CHARS_PER_DOCUMENT,
) -> list[Document]:
    """Limit retrieved chunk text before it is sent to the LLM."""
    limited_documents: list[Document] = []
    for document in documents:
        page_content = re.sub(r"\s+", " ", document.page_content).strip()
        if len(page_content) > max_chars_per_document:
            page_content = page_content[: max_chars_per_document - 3].rstrip() + "..."
        limited_documents.append(
            Document(
                page_content=page_content,
                metadata=dict(document.metadata),
            )
        )
    return limited_documents


def _extract_answer(chain_result: Any) -> str:
    if isinstance(chain_result, str):
        return chain_result.strip()

    if isinstance(chain_result, dict):
        for key in ("answer", "output_text", "result"):
            value = chain_result.get(key)
            if value is None:
                continue
            content = getattr(value, "content", value)
            text = str(content).strip()
            if text:
                return text

    content = getattr(chain_result, "content", None)
    if content is not None:
        text = str(content).strip()
        if text:
            return text

    raise LLMError("RAG chain returned no answer text.")


def _extract_source_metadata(chain_result: Any) -> list[dict[str, object]]:
    if not isinstance(chain_result, dict):
        return []

    documents = chain_result.get("context") or chain_result.get("source_documents") or []
    sources: list[dict[str, object]] = []
    seen: set[tuple[str, str]] = set()
    for document in documents:
        metadata = getattr(document, "metadata", {}) or {}
        source = str(metadata.get("source", "unknown"))
        page = metadata.get("page", "unknown")
        key = (source, str(page))
        if key in seen:
            continue
        seen.add(key)
        sources.append({"source": source, "page": page})
    return sources


def normalize_question(question: str) -> str:
    """Normalize and validate a user question before retrieval or LLM use."""
    normalized_question = " ".join(question.split())
    if not normalized_question:
        raise ValueError("Question must not be empty.")
    if len(normalized_question) > MAX_QUESTION_CHARS:
        raise ValueError(QUESTION_TOO_LONG_MESSAGE)
    return normalized_question


def is_emergency_like(question: str) -> bool:
    """Detect simple emergency-like statements for a short safety response."""
    return bool(EMERGENCY_PATTERN.search(question))


def answer_question(
    question: str,
    *,
    rag_chain: Any | None = None,
    settings: Settings | None = None,
) -> dict[str, object]:
    """Answer a user question with the configured RAG chain."""
    normalized_question = normalize_question(question)
    if is_emergency_like(normalized_question):
        return {"answer": EMERGENCY_RESPONSE, "sources": []}

    resolved_settings = settings
    chain = rag_chain or get_rag_chain(settings=resolved_settings)
    try:
        chain_result = chain.invoke({"input": normalized_question})
    except RemoteEmbeddingError:
        raise
    except LLMError:
        raise
    except Exception as exc:
        resolved_settings = resolved_settings or load_settings()
        raise _to_llm_error(exc, resolved_settings) from exc

    answer = _extract_answer(chain_result)
    return {
        "answer": answer,
        "sources": _extract_source_metadata(chain_result),
    }


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
    embedding_model = embeddings or get_embeddings(settings=resolved_settings)
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
