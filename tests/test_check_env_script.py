"""Tests for the local environment checker script."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from unittest.mock import patch


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CHECK_ENV_PATH = PROJECT_ROOT / "scripts" / "check_env.py"


def load_check_env_module():
    """Load the script module without requiring scripts to be a package."""
    spec = importlib.util.spec_from_file_location("check_env_script", CHECK_ENV_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_project_skeleton(root: Path, module) -> None:
    """Write only the files needed by the environment checker."""
    for relative_path in module.REQUIRED_PROJECT_FILES:
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("placeholder\n", encoding="utf-8")

    env_lines = [
        "PINECONE_API_KEY=test-pinecone-secret",
        "PINECONE_INDEX_NAME=medical-bot",
        "PINECONE_CLOUD=aws",
        "PINECONE_REGION=us-east-1",
        "PINECONE_NAMESPACE=medical-chatbot-v1",
        "OPENROUTER_API_KEY=test-openrouter-secret",
        "OPENROUTER_MODEL=openrouter/free",
        "FLASK_HOST=127.0.0.1",
        "FLASK_PORT=8080",
        "FLASK_DEBUG=false",
        "DATA_DIR=data",
    ]
    (root / ".env.example").write_text(
        "\n".join(line.split("=", 1)[0] + "=" for line in env_lines) + "\n",
        encoding="utf-8",
    )
    (root / ".env").write_text("\n".join(env_lines) + "\n", encoding="utf-8")
    data_dir = root / "data"
    data_dir.mkdir(exist_ok=True)
    (data_dir / "source.pdf").write_bytes(b"%PDF-1.4\n")


def test_run_checks_does_not_touch_pinecone_by_default(tmp_path):
    module = load_check_env_module()
    write_project_skeleton(tmp_path, module)

    with patch.object(module, "check_pinecone_connectivity") as mock_pinecone:
        results = module.run_checks(project_root=tmp_path)

    mock_pinecone.assert_not_called()
    assert all(result.passed for result in results)


def test_env_check_reports_secret_presence_without_values(tmp_path):
    module = load_check_env_module()
    write_project_skeleton(tmp_path, module)

    results = module.check_env_names(tmp_path)
    combined_details = "\n".join(result.detail for result in results)

    assert "test-pinecone-secret" not in combined_details
    assert "test-openrouter-secret" not in combined_details
    assert any(result.name == "PINECONE_API_KEY configured" for result in results)
    assert any(result.name == "OPENROUTER_API_KEY configured" for result in results)


def test_missing_pdf_is_reported_clearly(tmp_path):
    module = load_check_env_module()
    (tmp_path / "data").mkdir()

    results = module.check_local_inputs(tmp_path)
    pdf_result = next(result for result in results if result.name == "medical PDFs")

    assert not pdf_result.passed
    assert "legally obtained PDF" in pdf_result.detail


def test_pinecone_check_is_only_run_with_explicit_flag(tmp_path):
    module = load_check_env_module()
    write_project_skeleton(tmp_path, module)

    with patch.object(
        module,
        "check_pinecone_connectivity",
        return_value=[module.CheckResult("Pinecone connectivity", True, "authenticated")],
    ) as mock_pinecone:
        results = module.run_checks(project_root=tmp_path, check_pinecone=True)

    mock_pinecone.assert_called_once_with()
    assert any(result.name == "Pinecone connectivity" for result in results)
