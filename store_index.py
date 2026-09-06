"""Index management entry point for the medical chatbot."""

from __future__ import annotations

import argparse
import sys

from src.config import ConfigurationError
from src.indexing import IndexingError, ingest_documents
from src.pinecone_index import PineconeIndexError, check_pinecone_index


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(description="Medical chatbot index utilities.")
    parser.add_argument(
        "--check-index",
        action="store_true",
        help="Validate Pinecone authentication and index configuration.",
    )
    parser.add_argument(
        "--ingest",
        action="store_true",
        help="Load PDFs, split chunks, embed locally, and upsert into Pinecone.",
    )
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Clear only the configured Pinecone namespace before ingestion.",
    )
    parser.add_argument(
        "--yes-rebuild-namespace",
        action="store_true",
        help="Required confirmation for --rebuild namespace clearing.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run index utility commands."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.check_index and args.ingest:
        parser.error("Choose only one command: --check-index or --ingest.")

    if not args.check_index and not args.ingest:
        parser.print_help()
        return 0

    if args.check_index:
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

    try:
        result = ingest_documents(
            rebuild=args.rebuild,
            confirm_rebuild=args.yes_rebuild_namespace,
        )
    except (ConfigurationError, FileNotFoundError, IndexingError, PineconeIndexError) as exc:
        print(f"Indexing failed: {exc}", file=sys.stderr)
        return 1

    print("Indexing completed")
    print(f"index: {result.index_name}")
    print(f"namespace: {result.namespace}")
    print(f"pdfs: {result.pdf_count}")
    print(f"pages/documents: {result.page_count}")
    print(f"expected chunks: {result.chunk_count}")
    print(f"ids upserted: {result.upserted_count}")
    if result.stats_vector_count is not None:
        print(f"namespace vector count: {result.stats_vector_count}")
    else:
        print("namespace vector count: unavailable")
    print(f"similarity matches: {result.similarity_match_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
