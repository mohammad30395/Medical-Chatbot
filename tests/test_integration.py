"""Opt-in integration tests for external services."""

from __future__ import annotations

import os

import pytest
from langchain_core.documents import Document

from src.config import load_settings
from src.pinecone_index import (
    PINECONE_INDEX_DIMENSION,
    PINECONE_INDEX_METRIC,
    check_pinecone_index,
)
from src.rag import RETRIEVER_SEARCH_KWARGS, get_retriever, smoke_test_llm


pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(
        os.getenv("RUN_INTEGRATION_TESTS") != "1",
        reason="Set RUN_INTEGRATION_TESTS=1 to run external integration tests.",
    ),
]


def test_pinecone_connectivity_index_contract_and_top_k_retrieval() -> None:
    settings = load_settings(create_env_file=False)
    settings.validate_for_indexing()

    index_check = check_pinecone_index(settings)

    assert index_check.index_name == settings.pinecone_index_name
    assert index_check.dimension == PINECONE_INDEX_DIMENSION
    assert index_check.metric == PINECONE_INDEX_METRIC
    assert index_check.ready

    documents = get_retriever(settings=settings).invoke("What is diabetes?")

    assert 1 <= len(documents) <= RETRIEVER_SEARCH_KWARGS["k"]
    assert all(isinstance(document, Document) for document in documents)


def test_openrouter_generation_request_once() -> None:
    settings = load_settings(create_env_file=False)
    settings.validate_for_runtime()

    response = smoke_test_llm(settings=settings)

    assert response.strip()
