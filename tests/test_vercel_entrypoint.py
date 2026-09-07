"""Tests for the Vercel Flask entrypoint."""

from __future__ import annotations

import importlib
import sys
from unittest.mock import patch

from flask import Flask


def test_api_index_exposes_existing_flask_app() -> None:
    import app as local_app_module
    from api.index import app

    assert isinstance(app, Flask)
    assert app is local_app_module.app


def test_api_index_routes_render_with_flask_test_client() -> None:
    from api.index import app

    app.config.update(TESTING=True)
    client = app.test_client()

    home = client.get("/")
    health = client.get("/health")

    assert home.status_code == 200
    assert "Medical Knowledge Assistant" in home.get_data(as_text=True)
    assert health.status_code == 200
    assert "PINECONE_API_KEY" not in health.get_data(as_text=True)
    assert "OPENROUTER_API_KEY" not in health.get_data(as_text=True)


def test_api_index_post_get_uses_single_authoritative_route_with_mocked_rag() -> None:
    from api.index import app

    app.config.update(TESTING=True)
    client = app.test_client()

    with patch("app.answer_question", return_value={"answer": "Vercel answer."}) as mock_answer:
        response = client.post("/get", json={"message": " What is diabetes? "})

    assert response.status_code == 200
    assert response.get_json() == {"answer": "Vercel answer."}
    mock_answer.assert_called_once_with("What is diabetes?")


def test_importing_api_index_does_not_start_server_or_import_index_cli() -> None:
    sys.modules.pop("api.index", None)
    sys.modules.pop("store_index", None)

    with patch("flask.Flask.run") as mock_run:
        module = importlib.import_module("api.index")

    assert isinstance(module.app, Flask)
    mock_run.assert_not_called()
    assert "store_index" not in sys.modules
