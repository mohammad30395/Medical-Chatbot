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
