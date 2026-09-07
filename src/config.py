"""Configuration loading and validation for the medical chatbot."""

from __future__ import annotations

import os
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"
ENV_EXAMPLE_PATH = PROJECT_ROOT / ".env.example"

DEFAULT_PINECONE_INDEX_NAME = "medical-bot"
DEFAULT_PINECONE_CLOUD = "aws"
DEFAULT_PINECONE_REGION = "us-east-1"
DEFAULT_PINECONE_NAMESPACE = "medical-chatbot-v1"
DEFAULT_OPENROUTER_MODEL = "openrouter/free"
DEFAULT_FLASK_HOST = "127.0.0.1"
DEFAULT_FLASK_PORT = 8080
DEFAULT_FLASK_DEBUG = False
DEFAULT_DATA_DIR = "data"
DEFAULT_EMBEDDINGS_PROVIDER = "local"
REMOTE_EMBEDDINGS_PROVIDER = "huggingface_api"
DEFAULT_HUGGINGFACE_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_HUGGINGFACE_INFERENCE_PROVIDER = "hf-inference"
DEFAULT_HUGGINGFACE_TIMEOUT_SECONDS = 15

REQUIRED_ENV_VARS = (
    "PINECONE_API_KEY",
    "PINECONE_INDEX_NAME",
    "PINECONE_CLOUD",
    "PINECONE_REGION",
    "PINECONE_NAMESPACE",
    "OPENROUTER_API_KEY",
    "OPENROUTER_MODEL",
    "FLASK_HOST",
    "FLASK_PORT",
    "FLASK_DEBUG",
    "DATA_DIR",
)
DEPLOYMENT_ENV_VARS = (
    "EMBEDDINGS_PROVIDER",
    "HF_TOKEN",
    "HUGGINGFACE_EMBEDDING_MODEL",
    "HUGGINGFACE_INFERENCE_PROVIDER",
    "HUGGINGFACE_TIMEOUT_SECONDS",
)


class ConfigurationError(ValueError):
    """Raised when required configuration is missing or invalid."""


def is_vercel_environment(environ: Mapping[str, str | None] | None = None) -> bool:
    """Return whether settings are being loaded inside Vercel."""
    mapping = environ if environ is not None else os.environ
    return mapping.get("VERCEL") == "1"


def ensure_env_file(
    env_path: Path = ENV_PATH,
    example_path: Path = ENV_EXAMPLE_PATH,
) -> bool:
    """Create `.env` from `.env.example` when `.env` is absent."""
    if env_path.exists():
        return False
    if not example_path.exists():
        raise ConfigurationError(
            f"Cannot create {env_path.name}: missing template {example_path.name}."
        )
    shutil.copyfile(example_path, env_path)
    return True


def parse_bool(value: object, *, default: bool = DEFAULT_FLASK_DEBUG) -> bool:
    """Parse environment-style boolean values."""
    if value is None:
        return default
    if isinstance(value, bool):
        return value

    normalized = str(value).strip().lower()
    if normalized in {"1", "true", "t", "yes", "y", "on"}:
        return True
    if normalized in {"0", "false", "f", "no", "n", "off"}:
        return False
    raise ConfigurationError(
        "Invalid FLASK_DEBUG value. Expected one of: true, false, 1, 0, yes, no, on, off."
    )


def _get(mapping: Mapping[str, str | None], key: str, default: str) -> str:
    value = mapping.get(key)
    if value is None or value == "":
        return default
    return value


def _get_int(mapping: Mapping[str, str | None], key: str, default: int) -> int:
    raw_value = mapping.get(key)
    if raw_value is None or raw_value == "":
        return default
    try:
        return int(raw_value)
    except ValueError as exc:
        raise ConfigurationError(f"Invalid {key} value. Expected an integer.") from exc


def _normalize_embeddings_provider(value: str) -> str:
    provider = value.strip().lower()
    if provider in {"local", "huggingface_api"}:
        return provider
    if provider in {"hf_api", "huggingface", "huggingface-inference"}:
        return REMOTE_EMBEDDINGS_PROVIDER
    raise ConfigurationError(
        "Invalid EMBEDDINGS_PROVIDER value. Expected local or huggingface_api."
    )


def _default_embeddings_provider(mapping: Mapping[str, str | None]) -> str:
    if is_vercel_environment(mapping):
        return REMOTE_EMBEDDINGS_PROVIDER
    return DEFAULT_EMBEDDINGS_PROVIDER


@dataclass(frozen=True)
class Settings:
    """Runtime settings loaded from environment variables."""

    pinecone_api_key: str = ""
    pinecone_index_name: str = DEFAULT_PINECONE_INDEX_NAME
    pinecone_cloud: str = DEFAULT_PINECONE_CLOUD
    pinecone_region: str = DEFAULT_PINECONE_REGION
    pinecone_namespace: str = DEFAULT_PINECONE_NAMESPACE
    openrouter_api_key: str = ""
    openrouter_model: str = DEFAULT_OPENROUTER_MODEL
    flask_host: str = DEFAULT_FLASK_HOST
    flask_port: int = DEFAULT_FLASK_PORT
    flask_debug: bool = DEFAULT_FLASK_DEBUG
    data_dir: str = DEFAULT_DATA_DIR
    embeddings_provider: str = DEFAULT_EMBEDDINGS_PROVIDER
    hf_token: str = ""
    huggingface_embedding_model: str = DEFAULT_HUGGINGFACE_EMBEDDING_MODEL
    huggingface_inference_provider: str = DEFAULT_HUGGINGFACE_INFERENCE_PROVIDER
    huggingface_timeout_seconds: int = DEFAULT_HUGGINGFACE_TIMEOUT_SECONDS

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, str | None]) -> "Settings":
        """Build settings from an environment-style mapping."""
        embeddings_provider = _normalize_embeddings_provider(
            _get(mapping, "EMBEDDINGS_PROVIDER", _default_embeddings_provider(mapping))
        )
        flask_debug = (
            DEFAULT_FLASK_DEBUG
            if is_vercel_environment(mapping)
            else parse_bool(mapping.get("FLASK_DEBUG"), default=DEFAULT_FLASK_DEBUG)
        )
        return cls(
            pinecone_api_key=mapping.get("PINECONE_API_KEY") or "",
            pinecone_index_name=_get(
                mapping, "PINECONE_INDEX_NAME", DEFAULT_PINECONE_INDEX_NAME
            ),
            pinecone_cloud=_get(mapping, "PINECONE_CLOUD", DEFAULT_PINECONE_CLOUD),
            pinecone_region=_get(mapping, "PINECONE_REGION", DEFAULT_PINECONE_REGION),
            pinecone_namespace=_get(
                mapping, "PINECONE_NAMESPACE", DEFAULT_PINECONE_NAMESPACE
            ),
            openrouter_api_key=mapping.get("OPENROUTER_API_KEY") or "",
            openrouter_model=_get(
                mapping, "OPENROUTER_MODEL", DEFAULT_OPENROUTER_MODEL
            ),
            flask_host=_get(mapping, "FLASK_HOST", DEFAULT_FLASK_HOST),
            flask_port=_get_int(mapping, "FLASK_PORT", DEFAULT_FLASK_PORT),
            flask_debug=flask_debug,
            data_dir=_get(mapping, "DATA_DIR", DEFAULT_DATA_DIR),
            embeddings_provider=embeddings_provider,
            hf_token=mapping.get("HF_TOKEN") or "",
            huggingface_embedding_model=_get(
                mapping,
                "HUGGINGFACE_EMBEDDING_MODEL",
                DEFAULT_HUGGINGFACE_EMBEDDING_MODEL,
            ),
            huggingface_inference_provider=_get(
                mapping,
                "HUGGINGFACE_INFERENCE_PROVIDER",
                DEFAULT_HUGGINGFACE_INFERENCE_PROVIDER,
            ),
            huggingface_timeout_seconds=_get_int(
                mapping,
                "HUGGINGFACE_TIMEOUT_SECONDS",
                DEFAULT_HUGGINGFACE_TIMEOUT_SECONDS,
            ),
        )

    def validate_for_indexing(self) -> None:
        """Validate settings needed to build or update the vector index."""
        self._require("PINECONE_API_KEY", self.pinecone_api_key)

    def validate_for_runtime(self) -> None:
        """Validate settings needed to run the chatbot application."""
        self._require("PINECONE_API_KEY", self.pinecone_api_key)
        self._require("OPENROUTER_API_KEY", self.openrouter_api_key)
        if self.uses_remote_embeddings:
            self._require("HF_TOKEN", self.hf_token)
            self._validate_remote_embedding_model()

    @property
    def uses_remote_embeddings(self) -> bool:
        """Return whether runtime query embeddings use hosted inference."""
        return self.embeddings_provider == REMOTE_EMBEDDINGS_PROVIDER

    def missing_runtime_secret_names(self) -> list[str]:
        """Return missing runtime secrets without exposing values."""
        missing = []
        if not self.pinecone_api_key.strip():
            missing.append("PINECONE_API_KEY")
        if not self.openrouter_api_key.strip():
            missing.append("OPENROUTER_API_KEY")
        if self.uses_remote_embeddings and not self.hf_token.strip():
            missing.append("HF_TOKEN")
        return missing

    @staticmethod
    def _require(env_var: str, value: str) -> None:
        if not value.strip():
            raise ConfigurationError(
                f"Missing required environment variable: {env_var}. "
                f"Set {env_var} in .env locally or as a Vercel environment variable."
            )

    def _validate_remote_embedding_model(self) -> None:
        model = self.huggingface_embedding_model.strip()
        provider = self.huggingface_inference_provider.strip()
        if not model:
            raise ConfigurationError(
                "Missing required environment variable: HUGGINGFACE_EMBEDDING_MODEL. "
                f"Set HUGGINGFACE_EMBEDDING_MODEL={DEFAULT_HUGGINGFACE_EMBEDDING_MODEL}."
            )
        if model.lower() == provider.lower():
            raise ConfigurationError(
                "Invalid HUGGINGFACE_EMBEDDING_MODEL value. "
                f"Set HUGGINGFACE_EMBEDDING_MODEL={DEFAULT_HUGGINGFACE_EMBEDDING_MODEL} "
                f"and HUGGINGFACE_INFERENCE_PROVIDER={DEFAULT_HUGGINGFACE_INFERENCE_PROVIDER}."
            )


def load_settings(
    *,
    env_path: Path = ENV_PATH,
    example_path: Path = ENV_EXAMPLE_PATH,
    environ: Mapping[str, str | None] | None = None,
    override: bool = False,
    create_env_file: bool = True,
) -> Settings:
    """Load settings from `.env` and environment variables."""
    if environ is not None:
        return Settings.from_mapping(environ)

    if create_env_file and not is_vercel_environment():
        ensure_env_file(env_path=env_path, example_path=example_path)

    load_dotenv(dotenv_path=env_path, override=override)
    return Settings.from_mapping(os.environ)
