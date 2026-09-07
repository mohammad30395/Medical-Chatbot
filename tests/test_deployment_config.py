"""Tests for Vercel deployment configuration files."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_vercel_requirements_exclude_local_embedding_stack() -> None:
    requirements = (
        PROJECT_ROOT / "requirements-vercel.txt"
    ).read_text(encoding="utf-8").splitlines()
    normalized = {line.strip().lower() for line in requirements if line.strip()}

    assert "sentence-transformers" not in normalized
    assert "torch" not in normalized
    assert "transformers" not in normalized
    assert "huggingface-hub" in normalized
    assert "langchain-text-splitters" in normalized
    assert "langchain-openrouter" in normalized
    assert "langchain-pinecone" in normalized


def test_vercel_config_uses_slim_install_command() -> None:
    config = (PROJECT_ROOT / "vercel.json").read_text(encoding="utf-8")

    assert "requirements-vercel.txt" in config
    assert "store_index.py" not in config


def test_vercel_env_document_lists_names_without_values() -> None:
    document = (PROJECT_ROOT / "docs" / "VERCEL_ENV.md").read_text(encoding="utf-8")
    required_names = {
        "PINECONE_API_KEY",
        "PINECONE_INDEX_NAME",
        "PINECONE_NAMESPACE",
        "OPENROUTER_API_KEY",
        "OPENROUTER_MODEL",
        "EMBEDDINGS_PROVIDER",
        "HF_TOKEN",
        "HUGGINGFACE_EMBEDDING_MODEL",
        "HUGGINGFACE_INFERENCE_PROVIDER",
        "HUGGINGFACE_TIMEOUT_SECONDS",
    }

    for name in required_names:
        assert f"`{name}`" in document

    assert "medical-bot" not in document
    assert "medical-chatbot-v1" not in document
    assert "openrouter/free" not in document
    assert "sentence-transformers/all-MiniLM-L6-v2" not in document
    assert "hf-inference" not in document
