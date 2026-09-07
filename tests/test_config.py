"""Tests for configuration loading and validation."""

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.config import (
    DEFAULT_DATA_DIR,
    DEFAULT_FLASK_DEBUG,
    DEFAULT_FLASK_HOST,
    DEFAULT_FLASK_PORT,
    DEFAULT_HUGGINGFACE_EMBEDDING_MODEL,
    DEFAULT_HUGGINGFACE_INFERENCE_PROVIDER,
    DEFAULT_HUGGINGFACE_TIMEOUT_SECONDS,
    DEFAULT_OPENROUTER_MODEL,
    DEFAULT_PINECONE_CLOUD,
    DEFAULT_PINECONE_INDEX_NAME,
    DEFAULT_PINECONE_NAMESPACE,
    DEFAULT_PINECONE_REGION,
    REMOTE_EMBEDDINGS_PROVIDER,
    ConfigurationError,
    Settings,
    is_vercel_environment,
    load_settings,
    parse_bool,
)


class SettingsTests(unittest.TestCase):
    def test_defaults_load_correctly(self) -> None:
        settings = load_settings(environ={})

        self.assertEqual(settings.pinecone_index_name, DEFAULT_PINECONE_INDEX_NAME)
        self.assertEqual(settings.pinecone_cloud, DEFAULT_PINECONE_CLOUD)
        self.assertEqual(settings.pinecone_region, DEFAULT_PINECONE_REGION)
        self.assertEqual(settings.pinecone_namespace, DEFAULT_PINECONE_NAMESPACE)
        self.assertEqual(settings.openrouter_model, DEFAULT_OPENROUTER_MODEL)
        self.assertEqual(settings.flask_host, DEFAULT_FLASK_HOST)
        self.assertEqual(settings.flask_port, DEFAULT_FLASK_PORT)
        self.assertEqual(settings.flask_debug, DEFAULT_FLASK_DEBUG)
        self.assertEqual(settings.data_dir, DEFAULT_DATA_DIR)
        self.assertEqual(settings.embeddings_provider, "local")
        self.assertEqual(settings.hf_token, "")
        self.assertEqual(
            settings.huggingface_embedding_model,
            DEFAULT_HUGGINGFACE_EMBEDDING_MODEL,
        )
        self.assertEqual(
            settings.huggingface_inference_provider,
            DEFAULT_HUGGINGFACE_INFERENCE_PROVIDER,
        )
        self.assertEqual(
            settings.huggingface_timeout_seconds,
            DEFAULT_HUGGINGFACE_TIMEOUT_SECONDS,
        )

    def test_boolean_parsing_works(self) -> None:
        for value in ("true", "True", "1", "yes", "on", True):
            with self.subTest(value=value):
                self.assertTrue(parse_bool(value))

        for value in ("false", "False", "0", "no", "off", False):
            with self.subTest(value=value):
                self.assertFalse(parse_bool(value))

    def test_missing_secret_validation_raises_clear_error(self) -> None:
        settings = Settings()

        with self.assertRaisesRegex(
            ConfigurationError,
            "Missing required environment variable: PINECONE_API_KEY",
        ):
            settings.validate_for_indexing()

        with self.assertRaisesRegex(
            ConfigurationError,
            "Missing required environment variable: OPENROUTER_API_KEY",
        ):
            Settings(pinecone_api_key="present").validate_for_runtime()

    def test_model_and_index_constants_match_project_contract(self) -> None:
        settings = load_settings(environ={})

        self.assertEqual(settings.pinecone_index_name, "medical-bot")
        self.assertEqual(settings.pinecone_cloud, "aws")
        self.assertEqual(settings.pinecone_region, "us-east-1")
        self.assertEqual(settings.pinecone_namespace, "medical-chatbot-v1")
        self.assertEqual(settings.openrouter_model, "openrouter/free")
        self.assertEqual(settings.flask_host, "127.0.0.1")
        self.assertEqual(settings.flask_port, 8080)
        self.assertFalse(settings.flask_debug)
        self.assertEqual(settings.data_dir, "data")
        self.assertEqual(settings.embeddings_provider, "local")
        self.assertEqual(
            settings.huggingface_embedding_model,
            "sentence-transformers/all-MiniLM-L6-v2",
        )

    def test_remote_embedding_runtime_validation_requires_hf_token(self) -> None:
        settings = Settings(
            pinecone_api_key="present",
            openrouter_api_key="present",
            embeddings_provider=REMOTE_EMBEDDINGS_PROVIDER,
            hf_token="",
        )

        with self.assertRaisesRegex(ConfigurationError, "HF_TOKEN"):
            settings.validate_for_runtime()

    def test_remote_embedding_runtime_validation_accepts_hf_token(self) -> None:
        settings = Settings(
            pinecone_api_key="present",
            openrouter_api_key="present",
            embeddings_provider=REMOTE_EMBEDDINGS_PROVIDER,
            hf_token="present",
        )

        settings.validate_for_runtime()
        self.assertEqual(settings.missing_runtime_secret_names(), [])

    def test_remote_embedding_runtime_validation_rejects_provider_as_model(self) -> None:
        settings = Settings(
            pinecone_api_key="present",
            openrouter_api_key="present",
            embeddings_provider=REMOTE_EMBEDDINGS_PROVIDER,
            hf_token="present",
            huggingface_embedding_model="hf-inference",
            huggingface_inference_provider="hf-inference",
        )

        with self.assertRaisesRegex(ConfigurationError, "HUGGINGFACE_EMBEDDING_MODEL"):
            settings.validate_for_runtime()

    def test_embedding_provider_aliases_and_invalid_values(self) -> None:
        settings = load_settings(environ={"EMBEDDINGS_PROVIDER": "hf_api"})

        self.assertEqual(settings.embeddings_provider, REMOTE_EMBEDDINGS_PROVIDER)

        with self.assertRaisesRegex(ConfigurationError, "EMBEDDINGS_PROVIDER"):
            load_settings(environ={"EMBEDDINGS_PROVIDER": "unknown"})

    def test_missing_env_file_is_created_from_example(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            env_path = root / ".env"
            example_path = root / ".env.example"
            env_lines = (
                ("PINECONE_API_KEY", ""),
                ("PINECONE_INDEX_NAME", "medical-bot"),
                ("OPENROUTER_API_KEY", ""),
                ("FLASK_DEBUG", "true"),
            )
            example_path.write_text(
                "\n".join(f"{key}={value}" for key, value in env_lines) + "\n",
                encoding="utf-8",
            )

            with patch.dict(os.environ, {}, clear=True):
                settings = load_settings(
                    env_path=env_path,
                    example_path=example_path,
                    override=True,
                )

            self.assertTrue(env_path.exists())
            self.assertEqual(settings.pinecone_index_name, "medical-bot")
            self.assertTrue(settings.flask_debug)

    def test_vercel_environment_does_not_create_env_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            env_path = root / ".env"
            example_path = root / ".env.example"
            example_path.write_text(
                "PINECONE_API_KEY=\nOPENROUTER_API_KEY=\n",
                encoding="utf-8",
            )
            environ = {
                "VERCEL": "1",
                "PINECONE_API_KEY": "pinecone-secret",
                "OPENROUTER_API_KEY": "openrouter-secret",
            }

            with patch.dict(os.environ, environ, clear=True):
                settings = load_settings(
                    env_path=env_path,
                    example_path=example_path,
                    override=True,
                )

            self.assertTrue(is_vercel_environment(environ))
            self.assertFalse(env_path.exists())
            self.assertEqual(settings.pinecone_index_name, "medical-bot")
            self.assertEqual(settings.openrouter_model, "openrouter/free")


if __name__ == "__main__":
    unittest.main()
