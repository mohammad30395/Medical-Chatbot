# Medical Knowledge Assistant

A Flask-based medical knowledge chatbot that answers questions from uploaded PDF source material using retrieval augmented generation (RAG).

This project is built for educational and portfolio use. It is not a clinical tool, does not provide medical diagnosis, and should not be used as a replacement for professional medical advice.

## What This App Does

- Loads one or more medical PDF files from `data/`
- Splits PDF pages into retrieval-friendly text chunks
- Creates local embeddings with `sentence-transformers/all-MiniLM-L6-v2`
- Stores vectors in a Pinecone index
- Retrieves the most relevant source chunks for each user question
- Sends the retrieved context to an OpenRouter chat model
- Serves a simple Flask chat interface in the browser

## Tech Stack

| Area | Technology |
| --- | --- |
| Backend | Flask |
| RAG orchestration | LangChain |
| PDF loading | PyPDF / LangChain document loaders |
| Embeddings | Hugging Face sentence transformers |
| Vector database | Pinecone |
| LLM provider | OpenRouter |
| Testing | Pytest |
| Deployment target | Vercel |

## How It Works

```text
Medical PDFs
    -> PDF loader
    -> text splitter
    -> local embedding model
    -> Pinecone vector index
    -> similarity retrieval
    -> OpenRouter chat model
    -> Flask chat UI
```

The local indexing flow uses `sentence-transformers/all-MiniLM-L6-v2`, which produces `384`-dimension embeddings. The Pinecone index must therefore use:

- dimension: `384`
- metric: `cosine`
- vector type: dense

## Project Structure

```text
.
|-- app.py                    # Flask application entrypoint
|-- store_index.py            # Pinecone index check and PDF ingestion commands
|-- requirements.txt          # Local development dependencies
|-- requirements-vercel.txt   # Smaller Vercel deployment dependencies
|-- requirements.lock.txt     # Verified dependency lock snapshot
|-- setup.py                  # Editable package metadata
|-- vercel.json               # Vercel configuration
|-- api/
|   `-- index.py              # Vercel serverless entrypoint
|-- data/
|   `-- .gitkeep              # Put local PDF files here
|-- scripts/
|   |-- check_env.py          # Local setup checker
|   `-- smoke_test.py         # Runtime smoke checks
|-- src/
|   |-- config.py             # Environment loading and validation
|   |-- helper.py             # PDF loading, splitting, and embeddings
|   |-- indexing.py           # Document ingestion pipeline
|   |-- pinecone_index.py     # Pinecone index management
|   |-- prompt.py             # Medical QA prompt
|   |-- rag.py                # Retrieval and answer generation
|   `-- remote_embeddings.py  # Hosted Hugging Face embeddings for deployment
|-- static/
|   `-- style.css             # Local Flask CSS
|-- public/
|   `-- static/style.css      # Static assets for Vercel
|-- templates/
|   `-- chat.html             # Chat interface
`-- tests/                    # Unit and integration tests
```

## Requirements

Before running the app, make sure you have:

- Python `3.10` to `3.12`
- A Pinecone account and API key
- An OpenRouter account and API key
- At least one legally obtained medical PDF
- Internet access for dependency installation, Pinecone, OpenRouter, and the first embedding model download

The project metadata in `setup.py` declares `python_requires=">=3.10,<3.13"`.

## Environment Variables

Create a local `.env` file from the example:

```bash
cp .env.example .env
```

Then fill in your own values.

```env
PINECONE_API_KEY=
PINECONE_INDEX_NAME=medical-bot
PINECONE_CLOUD=aws
PINECONE_REGION=us-east-1
PINECONE_NAMESPACE=medical-chatbot-v1

OPENROUTER_API_KEY=
OPENROUTER_MODEL=openrouter/free

FLASK_HOST=127.0.0.1
FLASK_PORT=8080
FLASK_DEBUG=false
DATA_DIR=data

EMBEDDINGS_PROVIDER=local
HF_TOKEN=
HUGGINGFACE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
HUGGINGFACE_INFERENCE_PROVIDER=hf-inference
HUGGINGFACE_TIMEOUT_SECONDS=15
```

### Important Secrets

Never commit `.env`, `.env.local`, API keys, tokens, or private PDFs. They are intentionally ignored by Git.

## Local Setup

Create and activate a virtual environment:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

If your machine uses another compatible Python version, use that executable instead:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Add Medical PDFs

Place one or more legally obtained medical PDF files inside `data/`.

Example:

```text
data/Medical_book.pdf
```

PDF files are ignored by Git through `.gitignore`, so they will not appear after cloning the repository. Each developer must provide their own local PDF source files.

## Check Your Setup

Run the setup checker:

```bash
python scripts/check_env.py
```

To also verify Pinecone connectivity and index configuration:

```bash
python scripts/check_env.py --check-pinecone
```

The checker validates required files, `.env` variable names, configured secret presence, Python runtime, and whether PDF files exist in `data/`. It does not print secret values.

## Prepare Pinecone

Check or create the Pinecone index:

```bash
python store_index.py --check-index
```

This command verifies that the configured index uses the correct vector settings for the local embedding model.

## Index The PDFs

After adding PDFs to `data/`, ingest them into Pinecone:

```bash
python store_index.py --ingest
```

This command:

- loads PDF files from `data/`
- splits pages into `500` character chunks with `20` character overlap
- embeds chunks locally
- upserts vectors into the configured Pinecone namespace
- verifies that similarity search returns indexed content

To rebuild only the configured namespace:

```bash
python store_index.py --ingest --rebuild --yes-rebuild-namespace
```

## Run The App

Start the Flask development server:

```bash
python app.py
```

Open the local app:

```text
http://127.0.0.1:8080
```

The host, port, and debug mode are controlled by `FLASK_HOST`, `FLASK_PORT`, and `FLASK_DEBUG` in `.env`.

## Health Check

With the app running, visit:

```text
http://127.0.0.1:8080/health
```

The health endpoint reports lightweight runtime status without contacting Pinecone or OpenRouter and without exposing secrets.

## Tests

Run the default offline test suite:

```bash
pytest -q
```

Integration tests are opt-in because they may call Pinecone and OpenRouter:

```bash
RUN_INTEGRATION_TESTS=1 pytest -q -m integration
```

Run integration tests only after `.env` is configured and PDF data has been indexed.

## Vercel Deployment Notes

For Vercel, PDF ingestion still happens locally before deployment. The deployed app queries the already-populated Pinecone namespace.

Vercel uses `requirements-vercel.txt`, which avoids installing the heavier local `torch` and `sentence-transformers` stack. For hosted query embeddings on Vercel, configure:

```env
EMBEDDINGS_PROVIDER=huggingface_api
HF_TOKEN=your_hugging_face_token
```

Also set the required Pinecone and OpenRouter environment variables in the Vercel project settings.

## Common Commands

```bash
source .venv/bin/activate
python scripts/check_env.py
python store_index.py --check-index
python store_index.py --ingest
python app.py
pytest -q
```

## Troubleshooting

### No PDF files found

Add at least one `.pdf` file inside `data/`, then rerun:

```bash
python store_index.py --ingest
```

### Pinecone dimension mismatch

This project requires dimension `384` and metric `cosine`. If an existing Pinecone index has different settings, create a new index name or manually recreate the old index after confirming you no longer need its data.

### OpenRouter authentication failed

Check that `OPENROUTER_API_KEY` is set correctly in `.env`. Do not paste the key into source code, frontend JavaScript, logs, or issue reports.

### OpenRouter model unavailable or rate-limited

Free OpenRouter models can change or become rate-limited. Update `OPENROUTER_MODEL` in `.env` to a currently available model for your account.

### First embedding run is slow

The first local indexing run may download `sentence-transformers/all-MiniLM-L6-v2`. Later runs should be faster after the model is cached.

## Git-Ignored Local Files

The following files and folders are expected to exist locally but should not be committed:

- `.env`
- `.env.local`
- `.venv/`
- `.vercel/`
- `data/*.pdf`
- Python cache folders such as `__pycache__/` and `.pytest_cache/`

## Security

- Keep API keys server-side only
- Never expose secrets in HTML, browser JavaScript, screenshots, commits, or logs
- Commit `.env.example`, not `.env`
- Use only legally obtained source PDFs

## Medical Disclaimer

This app provides educational information grounded in uploaded source documents. It does not diagnose, treat, or replace professional medical advice. If a situation may be urgent or life-threatening, contact local emergency services or a qualified medical professional immediately.

## License

See p[LICENSE](LICENSE) for license information.
