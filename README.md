# Medical Knowledge Assistant

## Project Overview

This is a local Flask medical-information chatbot that answers questions using retrieval augmented generation over PDF content placed in `data/`. It is an educational project, not a clinical tool.

The app loads legally obtained medical PDFs, splits them into small chunks, embeds those chunks locally with `sentence-transformers/all-MiniLM-L6-v2`, stores vectors in Pinecone, retrieves the top 3 matching chunks, and sends only those retrieved chunks to an OpenRouter chat model.

For Vercel deployment, local PDF indexing still happens before deployment. The deployed app queries the already-indexed Pinecone namespace and uses hosted Hugging Face feature extraction for query embeddings so Vercel does not need to install or download the local `torch`/`sentence-transformers` model stack.

## Architecture Diagram

```text
PDF -> loader -> 500/20 chunks -> all-MiniLM-L6-v2 -> Pinecone -> top-3 retriever -> OpenRouter -> Flask UI
```

## Folder Structure

```text
.
├── app.py
├── store_index.py
├── template.py
├── setup.py
├── requirements.txt
├── requirements-vercel.txt
├── requirements.lock.txt
├── vercel.json
├── pytest.ini
├── BUILD_STATE.md
├── README.md
├── data/
│   ├── .gitkeep
│   └── Medical_book.pdf
├── research/
│   └── trials.ipynb
├── scripts/
│   ├── check_env.py
│   └── smoke_test.py
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── helper.py
│   ├── indexing.py
│   ├── pinecone_index.py
│   ├── prompt.py
│   ├── remote_embeddings.py
│   └── rag.py
├── public/
│   └── static/
│       └── style.css
├── static/
│   └── style.css
├── templates/
│   └── chat.html
└── tests/
```

## Prerequisites

- Detected OS: macOS 26.6.2 on arm64.
- Shell: zsh.
- Python: project virtual environment uses Python 3.10.21.
- A Pinecone account and `PINECONE_API_KEY`.
- An OpenRouter account and `OPENROUTER_API_KEY`.
- At least one legally obtained medical PDF in `data/`.
- Internet access for Pinecone, OpenRouter, dependency installation, and the first local sentence-transformer model download.
- Local disk space for the Python environment and the cached embedding model.

## Python Environment Setup For macOS

Use the existing `.venv` if it is already present:

```bash
source .venv/bin/activate
python --version
```

To recreate the environment on macOS with Python 3.10:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

If `python3.10` is not installed, install Python 3.10 first or create the environment with another compatible Python only after confirming package compatibility.

## Install Commands

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
```

`requirements.lock.txt` records the exact versions installed in the verified local environment.

## Convenience Commands

Verify local files, expected environment variable names, Python version, and PDF presence without printing secret values:

```bash
python scripts/check_env.py
```

Optionally include a Pinecone index check:

```bash
python scripts/check_env.py --check-pinecone
```

Other common local commands:

```bash
python store_index.py --check-index
python store_index.py --ingest
python app.py
pytest -q
```

## Create `.env`

Create `.env` from the example file:

```bash
cp .env.example .env
```

Then fill in only your own secret values. Do not commit `.env`.

## Required Environment Variables

| Variable | Purpose | Default or required value |
| --- | --- | --- |
| `PINECONE_API_KEY` | Pinecone authentication | Required secret |
| `PINECONE_INDEX_NAME` | Pinecone index name | `medical-bot` |
| `PINECONE_CLOUD` | Pinecone serverless cloud | `aws` |
| `PINECONE_REGION` | Pinecone serverless region | `us-east-1` |
| `PINECONE_NAMESPACE` | Namespace for this project's vectors | `medical-chatbot-v1` |
| `OPENROUTER_API_KEY` | OpenRouter authentication | Required secret |
| `OPENROUTER_MODEL` | OpenRouter model selector | `openrouter/free` |
| `FLASK_HOST` | Flask bind host | `127.0.0.1` |
| `FLASK_PORT` | Flask port | `8080` |
| `FLASK_DEBUG` | Flask debug mode | `false` |
| `DATA_DIR` | PDF input directory | `data` |
| `EMBEDDINGS_PROVIDER` | Query embedding provider | `local`; use `huggingface_api` on Vercel |
| `HF_TOKEN` | Hugging Face hosted inference token | Required only when `EMBEDDINGS_PROVIDER=huggingface_api` |
| `HUGGINGFACE_EMBEDDING_MODEL` | Hosted query embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| `HUGGINGFACE_INFERENCE_PROVIDER` | Hugging Face inference provider | `hf-inference` |
| `HUGGINGFACE_TIMEOUT_SECONDS` | Hosted embedding timeout | `15` |

## Place The Medical PDF

Place one or more legally obtained medical PDFs inside `data/`, for example:

```text
data/Medical_book.pdf
```

The loader searches for `.pdf` files case-insensitively. It raises a clear error if no PDF exists. PDF files under `data/` are ignored by Git through `.gitignore`.

Do not ask the project to fabricate medical source content. The app should answer only from files that actually exist in `data/`.

## Check Or Create The Pinecone Index

Run:

```bash
python store_index.py --check-index
```

This command authenticates with Pinecone, checks whether the configured index exists, creates it if missing, and verifies the index contract:

- name from `PINECONE_INDEX_NAME`, normally `medical-bot`
- dense vectors
- dimension `384`
- metric `cosine`
- serverless cloud and region from `.env`

If an existing index has the wrong dimension or metric, the command stops instead of deleting it. Safe recovery options are to use a new index name or manually delete and recreate the old index after confirming you no longer need its data.

## Run Indexing

Run:

```bash
python store_index.py --ingest
```

The ingestion command loads PDFs from `data/`, splits documents into 500-character chunks with 20-character overlap, embeds chunks locally, and upserts deterministic vector IDs into the configured Pinecone namespace.

To deliberately clear only the configured namespace before ingestion:

```bash
python store_index.py --ingest --rebuild --yes-rebuild-namespace
```

## Run The Flask App

Run:

```bash
python app.py
```

The app reads `FLASK_HOST`, `FLASK_PORT`, and `FLASK_DEBUG` from settings. Heavy RAG components are initialized lazily so importing the app for tests does not call Pinecone or OpenRouter.

## Local URL

The normal local URL is:

```text
http://127.0.0.1:8080
```

## Run Offline Tests

Run:

```bash
pytest -q
```

Default tests are unit tests and must not call Pinecone or OpenRouter. In the verified environment, this command passed with skipped integration tests.

## Run Opt-In Integration Tests

Integration tests are marked with `@pytest.mark.integration` and are skipped unless explicitly enabled:

```bash
RUN_INTEGRATION_TESTS=1 pytest -q -m integration
```

Run these only when valid `.env` keys and indexed data are available. These tests can call Pinecone and can make at most one OpenRouter generation request.

## Troubleshooting

Missing PDF: place at least one legally obtained `.pdf` file inside `data/`, then rerun indexing.

Pinecone dimension mismatch: the project requires dimension `384` and metric `cosine`. Do not reuse an incompatible index. Use a new index name or manually recreate the index.

OpenRouter invalid key: verify `OPENROUTER_API_KEY` in `.env`. Do not paste the key into source code, logs, issues, or browser JavaScript.

OpenRouter free rate limit: free models are rate-limited and may reject requests. Wait, choose another available model in `OPENROUTER_MODEL`, or use an account/model with enough quota.

OpenRouter free model unavailable: `openrouter/free` is configurable because the free catalog can change. Set `OPENROUTER_MODEL` to an available OpenRouter model without changing source code.

Sentence-transformer first-download delay: the first call to local embeddings may download `sentence-transformers/all-MiniLM-L6-v2` and can take time depending on internet speed and disk performance.

Vercel hosted embedding setup: set `EMBEDDINGS_PROVIDER=huggingface_api` and configure `HF_TOKEN` in Vercel project environment variables. Do not expose this token to browser JavaScript.

Vercel dependency size: Vercel installs from `requirements-vercel.txt` through `vercel.json`, avoiding the local `torch` and `sentence-transformers` packages in the deployed runtime.

## Security

Never commit `.env`. Commit only `.env.example`.

Never expose API keys in frontend JavaScript or HTML. The browser calls only the Flask backend, and the backend reads secrets from server-side environment variables.

The health endpoint reports whether runtime configuration is present without returning secret values.

## Medical-Use Disclaimer

Educational information only. Not a substitute for professional medical advice.

If a user describes a possible emergency, the app should give a short urgent-care recommendation instead of trying to manage the emergency through the chatbot.

## Cost Note

This project does not require the paid OpenAI API and does not use `OPENAI_API_KEY`.

Embeddings run locally with `sentence-transformers/all-MiniLM-L6-v2` for local development and indexing. Vercel query embeddings use Hugging Face hosted inference when `EMBEDDINGS_PROVIDER=huggingface_api`. OpenRouter is used for the chat model through `ChatOpenRouter`; free OpenRouter models are rate-limited, not unlimited. Pinecone Starter limits can change, including supported cloud/region options and usage quotas.

## Why ChatOpenRouter Instead Of ChatOpenAI

The project contract uses OpenRouter as the generation provider, so `src/rag.py` imports `ChatOpenRouter` from `langchain_openrouter`. It does not instantiate `ChatOpenAI` and does not read `OPENAI_API_KEY`. Keeping `OPENROUTER_MODEL` configurable lets the app adapt when OpenRouter's free model catalog changes.

