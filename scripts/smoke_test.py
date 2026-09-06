"""Small read-only smoke diagnostics for project phases."""

from __future__ import annotations

import argparse
import contextlib
import io
import logging
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.rag import retrieval_previews


def build_parser() -> argparse.ArgumentParser:
    """Build the smoke-test command parser."""
    parser = argparse.ArgumentParser(description="Medical chatbot smoke diagnostics.")
    parser.add_argument(
        "query",
        help="Query string for retrieving the top three indexed documents.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run retrieval diagnostics."""
    args = build_parser().parse_args(argv)
    logging.disable(logging.WARNING)
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
            io.StringIO()
        ):
            previews = retrieval_previews(args.query)
    finally:
        logging.disable(logging.NOTSET)
    for item in previews:
        print(f"{item.rank}\t{item.source}\t{item.page}\t{item.preview}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
