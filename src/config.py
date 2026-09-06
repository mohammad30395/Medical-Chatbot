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


class ConfigurationError(ValueError):
    """Raised when required configuration is missing or invalid."""


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

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, str | None]) -> "Settings":
        """Build settings from an environment-style mapping."""
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
            flask_debug=parse_bool(
                mapping.get("FLASK_DEBUG"), default=DEFAULT_FLASK_DEBUG
            ),
            data_dir=_get(mapping, "DATA_DIR", DEFAULT_DATA_DIR),
        )

    def validate_for_indexing(self) -> None:
        """Validate settings needed to build or update the vector index."""
        self._require("PINECONE_API_KEY", self.pinecone_api_key)

    def validate_for_runtime(self) -> None:
        """Validate settings needed to run the chatbot application."""
        self._require("PINECONE_API_KEY", self.pinecone_api_key)
        self._require("OPENROUTER_API_KEY", self.openrouter_api_key)

    @staticmethod
    def _require(env_var: str, value: str) -> None:
        if not value.strip():
            raise ConfigurationError(
                f"Missing required environment variable: {env_var}. "
                f"Set {env_var} in .env."
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

    if create_env_file:
        ensure_env_file(env_path=env_path, example_path=example_path)

    load_dotenv(dotenv_path=env_path, override=override)
    return Settings.from_mapping(os.environ)
