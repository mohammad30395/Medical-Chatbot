"""Tests for the Flask backend."""

import unittest
from unittest.mock import patch

from src.config import ConfigurationError, Settings
from src.pinecone_index import PineconeIndexError
from src.rag import LLMError
from src.remote_embeddings import RemoteEmbeddingError

from app import app
from src.rag import MAX_QUESTION_CHARS, QUESTION_TOO_LONG_MESSAGE


class FlaskBackendTests(unittest.TestCase):
    def setUp(self) -> None:
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_get_index_returns_200(self) -> None:
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_get_index_renders_phase_13_frontend(self) -> None:
        response = self.client.get("/")
        body = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Medical Knowledge Assistant", body)
        self.assertIn("Answers are grounded in the uploaded medical source.", body)
        self.assertIn("Educational information only.", body)
        self.assertIn("/get", body)
        self.assertIn("fetch", body)
        self.assertIn("textContent", body)
        self.assertIn(f'maxlength="{MAX_QUESTION_CHARS}"', body)
        self.assertNotIn("OPENROUTER_API_KEY", body)
        self.assertNotIn("PINECONE_API_KEY", body)

    def test_static_style_returns_200(self) -> None:
        response = self.client.get("/static/style.css")
        try:
            self.assertEqual(response.status_code, 200)
            self.assertIn("chat-shell", response.get_data(as_text=True))
        finally:
            response.close()

    def test_post_get_empty_returns_400(self) -> None:
        response = self.client.post("/get", json={"message": "   "})

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    @patch("app.answer_question")
    def test_post_get_overlong_returns_400_without_rag_call(
        self,
        mock_answer_question,
    ) -> None:
        response = self.client.post(
            "/get",
            json={"message": "x" * (MAX_QUESTION_CHARS + 1)},
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], QUESTION_TOO_LONG_MESSAGE)
        mock_answer_question.assert_not_called()

    @patch("app.answer_question", return_value={"answer": "A concise answer."})
    def test_post_get_with_mocked_answer_returns_json(self, mock_answer_question) -> None:
        response = self.client.post("/get", json={"message": " What is diabetes? "})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"answer": "A concise answer."})
        mock_answer_question.assert_called_once_with("What is diabetes?")

    @patch("app.answer_question", return_value={"answer": "Form answer."})
    def test_post_get_accepts_tutorial_msg_form_field(self, mock_answer_question) -> None:
        response = self.client.post("/get", data={"msg": " Hello   there "})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"answer": "Form answer."})
        mock_answer_question.assert_called_once_with("Hello there")

    @patch(
        "app.answer_question",
        side_effect=ConfigurationError(
            "Missing required environment variable: OPENROUTER_API_KEY. "
            "Set OPENROUTER_API_KEY in .env."
        ),
    )
    def test_post_get_missing_configuration_returns_503(
        self,
        mock_answer_question,
    ) -> None:
        response = self.client.post("/get", json={"message": "hello"})

        self.assertEqual(response.status_code, 503)
        self.assertIn("OPENROUTER_API_KEY", response.get_json()["error"])
        mock_answer_question.assert_called_once_with("hello")

    @patch(
        "app.answer_question",
        side_effect=LLMError("OpenRouter rate limit or quota exceeded: sanitized"),
    )
    def test_post_get_llm_rate_limit_returns_503(self, mock_answer_question) -> None:
        response = self.client.post("/get", json={"message": "hello"})

        self.assertEqual(response.status_code, 503)
        self.assertIn("rate limits", response.get_json()["error"])
        mock_answer_question.assert_called_once_with("hello")

    @patch(
        "app.answer_question",
        side_effect=LLMError("RAG chain returned no answer text."),
    )
    def test_post_get_llm_empty_answer_returns_clear_503(
        self,
        mock_answer_question,
    ) -> None:
        response = self.client.post("/get", json={"message": "hello"})

        self.assertEqual(response.status_code, 503)
        self.assertIn("empty response", response.get_json()["error"])
        mock_answer_question.assert_called_once_with("hello")

    @patch("app.answer_question", side_effect=PineconeIndexError("Pinecone unavailable"))
    def test_post_get_pinecone_failure_returns_503(self, mock_answer_question) -> None:
        response = self.client.post("/get", json={"message": "hello"})

        self.assertEqual(response.status_code, 503)
        self.assertIn("knowledge index", response.get_json()["error"])
        mock_answer_question.assert_called_once_with("hello")

    @patch(
        "app.answer_question",
        side_effect=RemoteEmbeddingError("Hugging Face unavailable"),
    )
    def test_post_get_remote_embedding_failure_returns_503(
        self,
        mock_answer_question,
    ) -> None:
        response = self.client.post("/get", json={"message": "hello"})

        self.assertEqual(response.status_code, 503)
        self.assertIn("embedding service", response.get_json()["error"])
        mock_answer_question.assert_called_once_with("hello")

    @patch("app.answer_question", side_effect=RuntimeError("raw failure"))
    def test_post_get_unexpected_failure_returns_generic_500(self, mock_answer_question) -> None:
        response = self.client.post("/get", json={"message": "hello"})

        self.assertEqual(response.status_code, 500)
        self.assertEqual(
            response.get_json()["error"],
            "An unexpected server error occurred.",
        )
        self.assertNotIn("raw failure", response.get_data(as_text=True))
        mock_answer_question.assert_called_once_with("hello")

    @patch(
        "app.load_settings",
        return_value=Settings(
            pinecone_api_key="pinecone-secret",
            openrouter_api_key="openrouter-secret",
        ),
    )
    def test_health_returns_200_without_exposing_secrets(self, mock_load_settings) -> None:
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertEqual(payload["status"], "ok")
        self.assertTrue(payload["runtime_configuration_present"])
        self.assertEqual(payload["missing"], [])
        self.assertNotIn("pinecone-secret", response.get_data(as_text=True))
        self.assertNotIn("openrouter-secret", response.get_data(as_text=True))
        mock_load_settings.assert_called_once_with(create_env_file=False)

    @patch(
        "app.load_settings",
        return_value=Settings(
            pinecone_api_key="pinecone-secret",
            openrouter_api_key="openrouter-secret",
            embeddings_provider="huggingface_api",
            hf_token="",
        ),
    )
    def test_health_reports_missing_hf_token_for_remote_embeddings(
        self,
        mock_load_settings,
    ) -> None:
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertFalse(payload["runtime_configuration_present"])
        self.assertEqual(payload["missing"], ["HF_TOKEN"])
        self.assertNotIn("pinecone-secret", response.get_data(as_text=True))
        self.assertNotIn("openrouter-secret", response.get_data(as_text=True))
        mock_load_settings.assert_called_once_with(create_env_file=False)

    @patch(
        "app.load_settings",
        return_value=Settings(
            pinecone_api_key="pinecone-secret",
            openrouter_api_key="openrouter-secret",
            embeddings_provider="huggingface_api",
            hf_token="hf-secret",
            huggingface_embedding_model="hf-inference",
            huggingface_inference_provider="hf-inference",
        ),
    )
    def test_health_reports_invalid_remote_embedding_model(
        self,
        mock_load_settings,
    ) -> None:
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertFalse(payload["runtime_configuration_present"])
        self.assertIn("HUGGINGFACE_EMBEDDING_MODEL", payload["configuration_error"])
        self.assertNotIn("hf-secret", response.get_data(as_text=True))
        mock_load_settings.assert_called_once_with(create_env_file=False)


if __name__ == "__main__":
    unittest.main()
