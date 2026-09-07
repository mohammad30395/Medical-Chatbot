"""Flask backend for the medical chatbot."""

from __future__ import annotations

from typing import Any

from flask import Flask, jsonify, render_template, request

from src.config import ConfigurationError, Settings, load_settings
from src.pinecone_index import PineconeIndexError
from src.rag import (
    LLMError,
    MAX_QUESTION_CHARS,
    QUESTION_TOO_LONG_MESSAGE,
    answer_question,
)


app = Flask(__name__)

RUNTIME_SECRET_VARS = ("PINECONE_API_KEY", "OPENROUTER_API_KEY")


def _normalize_message(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.split())


def _request_message() -> str:
    form_message = request.form.get("msg")
    if form_message is not None:
        return _normalize_message(form_message)

    json_body = request.get_json(silent=True)
    if isinstance(json_body, dict):
        return _normalize_message(json_body.get("message"))
    return ""


def _missing_runtime_variables(settings: Settings) -> list[str]:
    missing = []
    if not settings.pinecone_api_key.strip():
        missing.append("PINECONE_API_KEY")
    if not settings.openrouter_api_key.strip():
        missing.append("OPENROUTER_API_KEY")
    return missing


def _runtime_configuration_status() -> dict[str, Any]:
    try:
        settings = load_settings(create_env_file=False)
    except ConfigurationError as exc:
        return {
            "runtime_configuration_present": False,
            "missing": list(RUNTIME_SECRET_VARS),
            "configuration_error": str(exc),
        }

    missing = _missing_runtime_variables(settings)
    return {
        "runtime_configuration_present": not missing,
        "missing": missing,
    }


def _json_error(message: str, status_code: int):
    response = jsonify({"error": message})
    response.status_code = status_code
    return response


def _llm_error_message(exc: LLMError) -> str:
    message = str(exc).lower()
    if "authentication" in message:
        return "The language model configuration is not ready."
    if "rate limit" in message or "quota" in message:
        return "The language model is temporarily unavailable because of rate limits or quota."
    if "model unavailable" in message or "not found" in message:
        return "The configured language model is currently unavailable."
    if "timeout" in message or "network" in message or "connection" in message:
        return "The language model request timed out or the network is unavailable."
    return "The language model request failed."


def _looks_like_runtime_connectivity_failure(exc: Exception) -> bool:
    message = str(exc).lower()
    markers = (
        "pinecone",
        "timeout",
        "timed out",
        "network",
        "connection",
        "connectionerror",
        "readtimeout",
    )
    return any(marker in message for marker in markers)


@app.get("/")
def index():
    """Render the chat page."""
    return render_template("chat.html", max_question_chars=MAX_QUESTION_CHARS)


@app.post("/get")
def get_answer():
    """Answer a user message from form data or JSON."""
    message = _request_message()
    if not message:
        return _json_error("Message is required.", 400)
    if len(message) > MAX_QUESTION_CHARS:
        return _json_error(QUESTION_TOO_LONG_MESSAGE, 400)

    try:
        result = answer_question(message)
    except ConfigurationError as exc:
        return _json_error(str(exc), 503)
    except ValueError as exc:
        return _json_error(str(exc), 400)
    except PineconeIndexError:
        return _json_error("The medical knowledge index is unavailable.", 503)
    except LLMError as exc:
        return _json_error(_llm_error_message(exc), 503)
    except Exception as exc:
        if _looks_like_runtime_connectivity_failure(exc):
            return _json_error("A required runtime service is unavailable.", 503)
        return _json_error("An unexpected server error occurred.", 500)

    answer = str(result.get("answer", "")).strip()
    return jsonify({"answer": answer})


@app.get("/health")
def health():
    """Report lightweight application health without contacting external services."""
    return jsonify({"status": "ok", **_runtime_configuration_status()})


def main() -> None:
    """Run the development server using configured Flask settings."""
    settings = load_settings()
    app.run(
        host=settings.flask_host,
        port=settings.flask_port,
        debug=settings.flask_debug,
    )


if __name__ == "__main__":
    main()
