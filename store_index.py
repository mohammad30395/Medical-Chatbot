"""Index management entry point for the medical chatbot."""

from __future__ import annotations

import argparse
import sys

from src.config import ConfigurationError
from src.pinecone_index import PineconeIndexError, check_pinecone_index


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(description="Medical chatbot index utilities.")
    parser.add_argument(
        "--check-index",
        action="store_true",
        help="Validate Pinecone authentication and index configuration.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run index utility commands."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.check_index:
        parser.print_help()
        return 0

    try:
        result = check_pinecone_index()
    except (ConfigurationError, PineconeIndexError) as exc:
        print(f"Pinecone index check failed: {exc}", file=sys.stderr)
        return 1

    print("Pinecone index check passed")
    print(f"index: {result.index_name}")
    print(f"dimension: {result.dimension}")
    print(f"metric: {result.metric}")
    if result.vector_type is not None:
        print(f"vector_type: {result.vector_type}")
    print(f"ready: {result.ready}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
