"""Project scaffolding template for an empty medical chatbot project.

Run this script from the root of a new empty project to create the same
Phase 02 skeleton. It is intentionally not used to overwrite this repository.
"""

from pathlib import Path


ENV_EXAMPLE_LINES = (
    ("PINECONE_API_KEY", ""),
    ("PINECONE_INDEX_NAME", "medical-bot"),
    ("PINECONE_CLOUD", "aws"),
    ("PINECONE_REGION", "us-east-1"),
    ("PINECONE_NAMESPACE", "medical-chatbot-v1"),
    ("OPENROUTER_API_KEY", ""),
    ("OPENROUTER_MODEL", "openrouter/free"),
    ("FLASK_HOST", "127.0.0.1"),
    ("FLASK_PORT", "8080"),
    ("FLASK_DEBUG", "false"),
    ("DATA_DIR", "data"),
)


PROJECT_FILES = {
    "app.py": '''"""Application entry point placeholder for the medical chatbot."""\n''',
    "store_index.py": '''"""Index creation entry point placeholder for the medical chatbot."""\n''',
    "setup.py": '''"""Packaging configuration for editable installs."""\n\nfrom setuptools import find_packages, setup\n\n\nsetup(\n    name="medical-chatbot",\n    version="0.1.0",\n    packages=find_packages(include=["src", "src.*"]),\n    python_requires=">=3.10,<3.13",\n)\n''',
    "requirements.txt": "# Dependencies will be added in a later phase.\n",
    ".env.example": "\n".join(f"{key}={value}" for key, value in ENV_EXAMPLE_LINES) + "\n",
    "README.md": "# Medical Chatbot\n\nPhase 02 status: scaffold placeholder only.\n",
    "data/.gitkeep": "",
    "research/trials.ipynb": '{\n "cells": [],\n "metadata": {},\n "nbformat": 4,\n "nbformat_minor": 5\n}\n',
    "src/__init__.py": '''"""Medical chatbot source package."""\n''',
    "src/config.py": '''"""Configuration placeholders for the medical chatbot."""\n\nREQUIRED_ENV_VARS = (\n    "PINECONE_API_KEY",\n    "PINECONE_INDEX_NAME",\n    "PINECONE_CLOUD",\n    "PINECONE_REGION",\n    "PINECONE_NAMESPACE",\n    "OPENROUTER_API_KEY",\n    "OPENROUTER_MODEL",\n    "FLASK_HOST",\n    "FLASK_PORT",\n    "FLASK_DEBUG",\n    "DATA_DIR",\n)\n''',
}


def create_project(root: Path) -> None:
    """Create scaffold files without overwriting existing files."""
    for relative_path, content in PROJECT_FILES.items():
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            continue
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    create_project(Path.cwd())
