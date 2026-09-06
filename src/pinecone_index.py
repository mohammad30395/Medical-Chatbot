"""Safe Pinecone index management for the medical chatbot."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any

from pinecone import Pinecone, ServerlessSpec

from src.config import Settings, load_settings


PINECONE_INDEX_DIMENSION = 384
PINECONE_INDEX_METRIC = "cosine"
PINECONE_VECTOR_TYPE = "dense"
DEFAULT_READY_TIMEOUT_SECONDS = 120
DEFAULT_POLL_INTERVAL_SECONDS = 5


class PineconeIndexError(RuntimeError):
    """Raised when Pinecone index setup or validation fails."""


@dataclass(frozen=True)
class PineconeIndexCheck:
    """Summary of a verified Pinecone index."""

    index_name: str
    dimension: int
    metric: str
    vector_type: str | None
    ready: bool
    host: str | None = None


def create_pinecone_client(settings: Settings | None = None) -> Pinecone:
    """Create an authenticated Pinecone client without exposing the API key."""
    resolved_settings = settings or load_settings()
    resolved_settings.validate_for_indexing()
    return Pinecone(api_key=resolved_settings.pinecone_api_key)


def _index_names(indexes: Any) -> list[str]:
    names = getattr(indexes, "names", None)
    if callable(names):
        return list(names())

    result: list[str] = []
    for index in indexes:
        if isinstance(index, dict):
            result.append(str(index["name"]))
        else:
            result.append(str(getattr(index, "name")))
    return result


def _get_value(obj: Any, key: str, default: Any = None) -> Any:
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _index_ready(index_description: Any) -> bool:
    status = _get_value(index_description, "status", {})
    return bool(_get_value(status, "ready", False))


def _index_host(index_description: Any) -> str | None:
    host = _get_value(index_description, "host")
    return str(host) if host else None


def _safe_exception_message(exc: Exception, settings: Settings) -> str:
    message = str(exc)
    if settings.pinecone_api_key:
        message = message.replace(settings.pinecone_api_key, "[redacted]")
    return message


def _validate_index_contract(index_description: Any, index_name: str) -> None:
    dimension = _get_value(index_description, "dimension")
    metric = _get_value(index_description, "metric")
    vector_type = _get_value(index_description, "vector_type")
    problems: list[str] = []

    if int(dimension) != PINECONE_INDEX_DIMENSION:
        problems.append(
            f"dimension is {dimension}, expected {PINECONE_INDEX_DIMENSION}"
        )
    if str(metric) != PINECONE_INDEX_METRIC:
        problems.append(f"metric is {metric}, expected {PINECONE_INDEX_METRIC}")
    if vector_type is not None and str(vector_type) != PINECONE_VECTOR_TYPE:
        problems.append(
            f"vector_type is {vector_type}, expected {PINECONE_VECTOR_TYPE}"
        )

    if problems:
        raise PineconeIndexError(
            f"Pinecone index '{index_name}' exists but has incompatible settings: "
            f"{'; '.join(problems)}. This code will not delete or recreate an "
            "existing index automatically. Safe recovery options: update "
            "PINECONE_INDEX_NAME in .env to a new empty index name, or manually "
            "delete/recreate the existing index in Pinecone after confirming no "
            "needed data will be lost."
        )


def wait_for_index_ready(
    pinecone_client: Any,
    index_name: str,
    *,
    timeout_seconds: int = DEFAULT_READY_TIMEOUT_SECONDS,
    poll_interval_seconds: int = DEFAULT_POLL_INTERVAL_SECONDS,
) -> Any:
    """Poll Pinecone until the index reports ready."""
    deadline = time.monotonic() + timeout_seconds
    last_description = None

    while time.monotonic() <= deadline:
        last_description = pinecone_client.describe_index(index_name)
        _validate_index_contract(last_description, index_name)
        if _index_ready(last_description):
            return last_description
        time.sleep(poll_interval_seconds)

    raise PineconeIndexError(
        f"Timed out waiting for Pinecone index '{index_name}' to become ready."
    )


def ensure_pinecone_index(
    settings: Settings | None = None,
    *,
    pinecone_client: Any | None = None,
    wait: bool = True,
) -> Any:
    """Ensure the configured Pinecone index exists and matches this project."""
    resolved_settings = settings or load_settings()
    resolved_settings.validate_for_indexing()
    client = pinecone_client or create_pinecone_client(resolved_settings)
    index_name = resolved_settings.pinecone_index_name

    try:
        existing_indexes = _index_names(client.list_indexes())
    except Exception as exc:
        raise PineconeIndexError(
            "Failed to list Pinecone indexes. Verify PINECONE_API_KEY in .env. "
            f"Pinecone response: {_safe_exception_message(exc, resolved_settings)}"
        ) from exc

    if index_name not in existing_indexes:
        try:
            client.create_index(
                name=index_name,
                dimension=PINECONE_INDEX_DIMENSION,
                metric=PINECONE_INDEX_METRIC,
                vector_type=PINECONE_VECTOR_TYPE,
                spec=ServerlessSpec(
                    cloud=resolved_settings.pinecone_cloud,
                    region=resolved_settings.pinecone_region,
                ),
            )
        except Exception as exc:
            raise PineconeIndexError(
                f"Failed to create Pinecone index '{index_name}' with serverless "
                f"cloud '{resolved_settings.pinecone_cloud}' and region "
                f"'{resolved_settings.pinecone_region}'. Use the Pinecone account "
                "response to set PINECONE_CLOUD/PINECONE_REGION in .env to a "
                "supported serverless deployment, then rerun the check. "
                f"Pinecone response: {_safe_exception_message(exc, resolved_settings)}"
            ) from exc

    description = wait_for_index_ready(client, index_name) if wait else client.describe_index(index_name)
    _validate_index_contract(description, index_name)
    return client.Index(index_name)


def check_pinecone_index(
    settings: Settings | None = None,
    *,
    pinecone_client: Any | None = None,
) -> PineconeIndexCheck:
    """Authenticate and verify the configured Pinecone index contract."""
    resolved_settings = settings or load_settings()
    client = pinecone_client or create_pinecone_client(resolved_settings)
    ensure_pinecone_index(
        resolved_settings,
        pinecone_client=client,
        wait=True,
    )
    description = client.describe_index(resolved_settings.pinecone_index_name)
    _validate_index_contract(description, resolved_settings.pinecone_index_name)

    return PineconeIndexCheck(
        index_name=resolved_settings.pinecone_index_name,
        dimension=int(_get_value(description, "dimension")),
        metric=str(_get_value(description, "metric")),
        vector_type=_get_value(description, "vector_type"),
        ready=_index_ready(description),
        host=_index_host(description),
    )
