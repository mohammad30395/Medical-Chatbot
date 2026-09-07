"""Read-only environment checks for the medical chatbot project."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import DEPLOYMENT_ENV_VARS, REQUIRED_ENV_VARS


REQUIRED_PROJECT_FILES = (
    "app.py",
    "api/__init__.py",
    "api/index.py",
    "store_index.py",
    "README.md",
    "requirements.txt",
    "requirements-vercel.txt",
    "requirements.lock.txt",
    ".env.example",
    "vercel.json",
    "src/config.py",
    "src/helper.py",
    "src/pinecone_index.py",
    "src/rag.py",
    "src/prompt.py",
    "templates/chat.html",
    "static/style.css",
    "public/static/style.css",
)
SECRET_ENV_VARS = {"PINECONE_API_KEY", "OPENROUTER_API_KEY"}


@dataclass(frozen=True)
class CheckResult:
    """Single environment check result."""

    name: str
    passed: bool
    detail: str


def _parse_env_keys(path: Path) -> dict[str, bool]:
    keys: dict[str, bool] = {}
    if not path.exists():
        return keys

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        keys[key.strip()] = bool(value.strip())
    return keys


def _pdf_count(data_dir: Path) -> int:
    if not data_dir.exists() or not data_dir.is_dir():
        return 0
    return sum(
        1 for path in data_dir.rglob("*") if path.is_file() and path.suffix.lower() == ".pdf"
    )


def check_required_files(project_root: Path = PROJECT_ROOT) -> list[CheckResult]:
    """Verify expected project files exist."""
    results: list[CheckResult] = []
    for relative_path in REQUIRED_PROJECT_FILES:
        path = project_root / relative_path
        results.append(
            CheckResult(
                name=f"file:{relative_path}",
                passed=path.exists(),
                detail="present" if path.exists() else "missing",
            )
        )
    return results


def check_env_names(project_root: Path = PROJECT_ROOT) -> list[CheckResult]:
    """Verify `.env.example` and `.env` contain the expected variable names."""
    example_path = project_root / ".env.example"
    env_path = project_root / ".env"
    example_keys = _parse_env_keys(example_path)
    env_keys = _parse_env_keys(env_path)

    results = [
        CheckResult(
            name=".env.example",
            passed=example_path.exists(),
            detail="present" if example_path.exists() else "missing",
        ),
        CheckResult(
            name=".env",
            passed=env_path.exists(),
            detail="present" if env_path.exists() else "missing; create it from .env.example",
        ),
    ]

    missing_example = [key for key in REQUIRED_ENV_VARS if key not in example_keys]
    missing_deployment_example = [
        key for key in DEPLOYMENT_ENV_VARS if key not in example_keys
    ]
    results.append(
        CheckResult(
            name=".env.example keys",
            passed=not missing_example,
            detail="all required names present"
            if not missing_example
            else "missing: " + ", ".join(missing_example),
        )
    )
    results.append(
        CheckResult(
            name=".env.example deployment keys",
            passed=not missing_deployment_example,
            detail="all deployment names present"
            if not missing_deployment_example
            else "missing: " + ", ".join(missing_deployment_example),
        )
    )

    if env_path.exists():
        missing_env = [key for key in REQUIRED_ENV_VARS if key not in env_keys]
        results.append(
            CheckResult(
                name=".env keys",
                passed=not missing_env,
                detail="all required names present"
                if not missing_env
                else "missing: " + ", ".join(missing_env),
            )
        )
        for key in sorted(SECRET_ENV_VARS):
            results.append(
                CheckResult(
                    name=f"{key} configured",
                    passed=env_keys.get(key, False),
                    detail="set" if env_keys.get(key, False) else "missing value",
                )
            )
    else:
        results.append(
            CheckResult(
                name=".env keys",
                passed=False,
                detail="not checked because .env is missing",
            )
        )

    return results


def check_local_inputs(project_root: Path = PROJECT_ROOT) -> list[CheckResult]:
    """Verify local input folders without reading or printing PDF content."""
    data_dir = project_root / "data"
    count = _pdf_count(data_dir)
    return [
        CheckResult(
            name="data directory",
            passed=data_dir.exists() and data_dir.is_dir(),
            detail="present" if data_dir.exists() and data_dir.is_dir() else "missing",
        ),
        CheckResult(
            name="medical PDFs",
            passed=count > 0,
            detail=f"{count} PDF file(s) found"
            if count
            else "none found; place a legally obtained PDF in data/",
        ),
    ]


def check_python_runtime() -> list[CheckResult]:
    """Verify the current Python runtime."""
    version = sys.version_info
    version_text = f"{version.major}.{version.minor}.{version.micro}"
    return [
        CheckResult(
            name="Python version",
            passed=(version.major, version.minor) >= (3, 10),
            detail=version_text,
        ),
        CheckResult(
            name="virtual environment",
            passed=bool(getattr(sys, "base_prefix", sys.prefix) != sys.prefix),
            detail="active" if getattr(sys, "base_prefix", sys.prefix) != sys.prefix else "not active",
        ),
    ]


def check_pinecone_connectivity() -> list[CheckResult]:
    """Optionally verify Pinecone without printing secrets."""
    try:
        from src.pinecone_index import check_pinecone_index

        result = check_pinecone_index()
    except Exception as exc:
        return [
            CheckResult(
                name="Pinecone connectivity",
                passed=False,
                detail=f"failed: {exc}",
            )
        ]

    return [
        CheckResult(
            name="Pinecone connectivity",
            passed=True,
            detail="authenticated",
        ),
        CheckResult(
            name="Pinecone index",
            passed=result.ready and result.dimension == 384 and result.metric == "cosine",
            detail=(
                f"{result.index_name}: ready={result.ready}, "
                f"dimension={result.dimension}, metric={result.metric}"
            ),
        ),
    ]


def run_checks(
    *,
    project_root: Path = PROJECT_ROOT,
    check_pinecone: bool = False,
) -> list[CheckResult]:
    """Run all default checks, with Pinecone behind an explicit flag."""
    results = []
    results.extend(check_python_runtime())
    results.extend(check_required_files(project_root))
    results.extend(check_env_names(project_root))
    results.extend(check_local_inputs(project_root))
    if check_pinecone:
        results.extend(check_pinecone_connectivity())
    return results


def build_parser() -> argparse.ArgumentParser:
    """Build the environment-check parser."""
    parser = argparse.ArgumentParser(
        description="Verify local Medical Chatbot environment without printing secrets."
    )
    parser.add_argument(
        "--check-pinecone",
        action="store_true",
        help="Also authenticate with Pinecone and validate the configured index.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run environment checks from the command line."""
    args = build_parser().parse_args(argv)
    results = run_checks(check_pinecone=args.check_pinecone)

    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"{status}\t{result.name}\t{result.detail}")

    return 0 if all(result.passed for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
