"""Hosted embedding adapters for deployment runtimes."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Sequence

from src.config import (
    DEFAULT_HUGGINGFACE_EMBEDDING_MODEL,
    DEFAULT_HUGGINGFACE_INFERENCE_PROVIDER,
    DEFAULT_HUGGINGFACE_TIMEOUT_SECONDS,
)
from src.helper_constants import EXPECTED_EMBEDDING_DIMENSION


class RemoteEmbeddingError(RuntimeError):
    """Raised when hosted embedding inference fails safely."""


def _as_plain_data(value: Any) -> Any:
    if hasattr(value, "tolist"):
        return value.tolist()
    return value


def _is_number_sequence(value: Any) -> bool:
    return isinstance(value, Sequence) and not isinstance(value, (str, bytes)) and all(
        isinstance(item, (int, float)) for item in value
    )


def _mean_pool(vectors: Sequence[Sequence[float]]) -> list[float]:
    if not vectors:
        raise RemoteEmbeddingError("Hugging Face returned an empty embedding.")
    width = len(vectors[0])
    if width == 0 or any(len(vector) != width for vector in vectors):
        raise RemoteEmbeddingError("Hugging Face returned malformed embedding data.")
    return [
        sum(float(vector[index]) for vector in vectors) / len(vectors)
        for index in range(width)
    ]


def _coerce_vector(value: Any) -> list[float]:
    value = _as_plain_data(value)
    if _is_number_sequence(value):
        return [float(item) for item in value]
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        if len(value) == 1 and _is_number_sequence(value[0]):
            return [float(item) for item in value[0]]
        if all(_is_number_sequence(item) for item in value):
            return _mean_pool(value)
    raise RemoteEmbeddingError("Hugging Face returned malformed embedding data.")


def _coerce_vectors(value: Any, expected_count: int) -> list[list[float]]:
    value = _as_plain_data(value)
    if expected_count == 1:
        return [_coerce_vector(value)]
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        raise RemoteEmbeddingError("Hugging Face returned malformed embedding data.")
    vectors = [_coerce_vector(item) for item in value]
    if len(vectors) != expected_count:
        raise RemoteEmbeddingError(
            "Hugging Face returned an unexpected number of embeddings: "
            f"expected {expected_count}, got {len(vectors)}."
        )
    return vectors


def _validate_dimension(vector: list[float]) -> list[float]:
    if len(vector) != EXPECTED_EMBEDDING_DIMENSION:
        raise RemoteEmbeddingError(
            f"Expected embedding dimension {EXPECTED_EMBEDDING_DIMENSION}, "
            f"got {len(vector)}."
        )
    return vector


@dataclass
class HuggingFaceAPIEmbeddings:
    """LangChain-compatible embeddings using hosted Hugging Face inference."""

    api_key: str = field(repr=False)
    model: str = DEFAULT_HUGGINGFACE_EMBEDDING_MODEL
    provider: str = DEFAULT_HUGGINGFACE_INFERENCE_PROVIDER
    timeout_seconds: int = DEFAULT_HUGGINGFACE_TIMEOUT_SECONDS
    client_factory: Callable[..., Any] | None = field(default=None, repr=False)
    _client: Any | None = field(default=None, init=False, repr=False)

    def _get_client(self) -> Any:
        if self._client is None:
            factory = self.client_factory
            if factory is None:
                from huggingface_hub import InferenceClient

                factory = InferenceClient
            self._client = factory(
                provider=self.provider,
                api_key=self.api_key,
                timeout=self.timeout_seconds,
            )
        return self._client

    def _feature_extraction(self, text: str | list[str]) -> Any:
        try:
            return self._get_client().feature_extraction(
                text,
                model=self.model,
                normalize=True,
                truncate=True,
            )
        except Exception as exc:
            raise RemoteEmbeddingError(
                _sanitize_remote_error(str(exc), self.api_key)
            ) from exc

    def embed_query(self, text: str) -> list[float]:
        """Embed one query string."""
        return _validate_dimension(_coerce_vector(self._feature_extraction(text)))

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed documents when a vector store calls the standard interface."""
        if not texts:
            return []
        vectors = _coerce_vectors(self._feature_extraction(texts), len(texts))
        return [_validate_dimension(vector) for vector in vectors]


def _sanitize_remote_error(message: str, api_key: str) -> str:
    sanitized = message.replace(api_key, "[redacted]") if api_key else message
    if api_key:
        return sanitized.replace("Bearer " + api_key, "Bearer [redacted]")
    return sanitized
