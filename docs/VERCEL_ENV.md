# Vercel Environment Variables

Configure these in Vercel Project -> Settings -> Environment Variables. Do not put secret values in source code, commits, browser JavaScript, or this document. Redeploy after changing any Vercel environment variable.

The deployed app reads server-side variables from `os.environ`. A physical `.env` file is only for local development and is not required in Vercel.

## Required Runtime Variables

| Variable name | Secret | Recommended scopes | Purpose |
| --- | --- | --- | --- |
| `PINECONE_API_KEY` | Yes | Preview, Production | Authenticates server-side Pinecone index queries. |
| `PINECONE_INDEX_NAME` | No | Preview, Production | Selects the already-created Pinecone index. |
| `PINECONE_NAMESPACE` | No | Preview, Production | Selects the namespace containing indexed document chunks. |
| `OPENROUTER_API_KEY` | Yes | Preview, Production | Authenticates server-side OpenRouter chat requests. |
| `OPENROUTER_MODEL` | No | Preview, Production | Selects the OpenRouter chat model route. |
| `EMBEDDINGS_PROVIDER` | No | Preview, Production | Selects hosted query embeddings for the Vercel runtime. |
| `HF_TOKEN` | Yes | Preview, Production | Authenticates server-side Hugging Face hosted embedding requests. |
| `HUGGINGFACE_EMBEDDING_MODEL` | No | Preview, Production | Selects the same embedding model family used when indexing Pinecone. |
| `HUGGINGFACE_INFERENCE_PROVIDER` | No | Preview, Production | Selects the hosted Hugging Face inference backend. |
| `HUGGINGFACE_TIMEOUT_SECONDS` | No | Preview, Production | Sets the hosted embedding request timeout. |

## Optional Runtime Variables

| Variable name | Secret | Recommended scopes | Purpose |
| --- | --- | --- | --- |
| `PINECONE_CLOUD` | No | Development, Preview, Production | Used by local index creation/check commands, not normal Vercel request handling. |
| `PINECONE_REGION` | No | Development, Preview, Production | Used by local index creation/check commands, not normal Vercel request handling. |
| `DATA_DIR` | No | Development | Used by local PDF loading and indexing commands. The normal Vercel app queries Pinecone and does not need the source PDF. |
| `FLASK_HOST` | No | Development | Used only by local `python app.py`; Vercel does not use it to bind the server. |
| `FLASK_PORT` | No | Development | Used only by local `python app.py`; Vercel assigns the serverless runtime port. |
| `FLASK_DEBUG` | No | Development | Used only for local development. The app forces debug off inside Vercel. |

## Browser Secret Boundary

The browser loads `templates/chat.html` and `static/style.css`, then calls the Flask `/get` route with a JSON message. Browser JavaScript never reads Vercel environment variables and never calls Pinecone, Hugging Face, or OpenRouter directly.

## Deployment Notes

Do not run `store_index.py` during a Vercel build, import, startup, or request. Indexing remains an explicit local command. The deployed app should query the already-indexed Pinecone namespace.

Use Vercel's encrypted environment variable UI for secrets. Only variable names are safe to inspect in logs or CLI output.
