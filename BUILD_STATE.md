# Build State

## Phase 01 - Device and Repository Audit

Status: PASS
Audit timestamp: 2026-09-06 15:26:15 +06

## Project Root

- Project root: `/Users/macbook/Desktop/Fahmid/Target/7.AI App/4.Date.31.08.2026/Medical-Chatbot`
- Current working directory: `/Users/macbook/Desktop/Fahmid/Target/7.AI App/4.Date.31.08.2026/Medical-Chatbot`
- Folder writable: yes
- VS Code/Codex writable folder status: operating in a writable project folder

## Repository Facts

- Git repository: yes
- Git branch: `main`
- Git remote: `origin https://github.com/mohammad30395/Medical-Chatbot.git`
- Existing files before Phase 01 changes:
  - `.gitattributes`
- Existing directories before Phase 01 changes:
  - `.`
  - `.git`
- Recursive inspection depth: files to max depth 4, directories to max depth 3
- Conflicting files found: none
- `data/` directory present: no
- Existing `.gitignore`: no
- Existing `BUILD_STATE.md`: no

## Environment Facts

- OS: macOS 26.6.2
- OS build: 25G83
- Shell: `/bin/zsh`
- Shell version: zsh 5.9 (arm64-apple-darwin25.0)
- CPU architecture: arm64
- Python installed: yes
- Available Python executables and versions:
  - `python3`: Python 3.9.6
  - `python3.10`: Python 3.10.21
  - `python3.11`: Python 3.11.15
  - `python3.12`: Python 3.12.13
- Python 3.10 available: yes
- Python 3.10 executable path: `/opt/homebrew/opt/python@3.10/bin/python3.10`
- Python 3.10 platform: macosx-26-arm64
- Python `venv` module: available
- pip versions checked:
  - `pip3`: pip 21.2.4 for Python 3.9
  - `pip3.10`: pip 26.2.1 for Python 3.10
  - `pip3.11`: pip 26.1.2 for Python 3.11
  - `python3.12 -m pip`: pip 26.2.1 for Python 3.12
- Chosen pip for future phases: `python3.10 -m pip` / `pip3.10`
- Git version: git version 2.50.1 (Apple Git-155)
- Conda installed: no executable found (`conda`, `mamba`, and `micromamba` not found)
- Active virtual environment: none detected
- Active Conda environment: none detected
- Existing virtual environment in project: none detected
- Secret scan: no secret-shaped values found in workspace files outside `.git`

## Environment Strategy

- Chosen Python executable: `/opt/homebrew/opt/python@3.10/bin/python3.10`
- Chosen virtual environment path: `/Users/macbook/Desktop/Fahmid/Target/7.AI App/4.Date.31.08.2026/Medical-Chatbot/.venv`
- Strategy: use standard Python `venv` in `.venv` with Python 3.10 in a later phase.
- Rationale: the tutorial used Python 3.10, and Python 3.10.21 is installed locally. No Conda workflow exists in this repository.
- Dependency action in Phase 01: none. No packages were installed or changed.

## Blockers

- No Phase 01 blockers.
- Future content prerequisite: no `data/` directory or medical source PDFs are present yet. Later phases must use only real files that exist in `data/` and must not fabricate medical source content.

## Commands Run

- `pwd`
- `ls -la`
- `find . -maxdepth 4 -type f -not -path './.git/*' | sort`
- `find . -maxdepth 3 -type d -not -path './.git/*' | sort`
- `test -f BUILD_STATE.md && sed -n '1,240p' BUILD_STATE.md || true`
- `test -f .gitignore && sed -n '1,200p' .gitignore || true`
- `sw_vers`
- `uname -m`
- `echo $SHELL`
- `zsh --version`
- `git --version`
- `git rev-parse --is-inside-work-tree`
- `test -w . && printf 'writable\n' || printf 'not writable\n'`
- `sed -n '1,120p' .gitattributes`
- `for exe in python python2 python3 python3.9 python3.10 python3.11 python3.12 python3.13; do if command -v $exe >/dev/null 2>&1; then printf '%s: ' $exe; $exe --version; fi; done`
- `for exe in pip pip3 pip3.10 pip3.11 pip3.12 pip3.13; do if command -v $exe >/dev/null 2>&1; then printf '%s: ' $exe; $exe --version; fi; done`
- `find . -maxdepth 3 \( -name 'pyvenv.cfg' -o -name 'conda-meta' \) -print`
- `find . -maxdepth 2 -type d \( -name '.venv' -o -name 'venv' -o -name 'env' -o -name '.env' -o -name 'conda' -o -name '.conda' \) -print`
- `git status --short`
- `git branch --show-current`
- `git remote -v`
- `whence -p -a python python2 python3 python3.9 python3.10 python3.11 python3.12 python3.13 pip pip3 pip3.10 pip3.11 pip3.12 pip3.13 conda mamba micromamba`
- `python3.10 -m pip --version`
- `python3.10 -c 'import sys; print(sys.executable)'`
- `python3.10 -c 'import sysconfig; print(sysconfig.get_platform())'`
- `python3.10 -c 'import venv; print("venv module available")'`
- `printenv CONDA_PREFIX VIRTUAL_ENV PYENV_VERSION`
- `find . -maxdepth 4 -type f -not -path './.git/*' \( -name '.env' -o -name '*.pem' -o -name '*.key' -o -name '*secret*' -o -name '*credential*' \) -print`
- `rg -n --hidden --glob '!.git/**' '(OPENAI_API_KEY|OPENROUTER_API_KEY|PINECONE_API_KEY|api[_-]?key|secret|token|password|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `python3.12 -m pip --version`
- `python3.11 -m pip --version`
- `test -d data && find data -maxdepth 3 -type f | sort || true`
- `sed -n '1,260p' BUILD_STATE.md`
- `sed -n '1,120p' .gitignore`
- `git status --short`
- `find . -maxdepth 4 -type f -not -path './.git/*' \( -name '.env' -o -name '*.pem' -o -name '*.key' -o -name '*credential*' \) -print`
- `rg -n --hidden --glob '!.git/**' --glob '!BUILD_STATE.md' --glob '!.gitignore' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=|PINECONE_API_KEY\s*=|OPENAI_API_KEY\s*=|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `test -f BUILD_STATE.md && test -f .gitignore && printf 'planning files present\n'`

## Tests and Acceptance Checks

- Python strategy explicit: yes
- Python 3.10 availability verified: yes
- No packages installed: yes
- No application source files created: yes
- No `.env` created: yes
- No Pinecone or OpenRouter initialization: yes
- No secrets found in repository workspace files outside `.git`: yes
- `BUILD_STATE.md` exists and contains verified facts: yes
- `.gitignore` skeleton created because none existed: yes
- Final Git status after Phase 01 changes: `.gitignore` and `BUILD_STATE.md` are untracked
- Final planning file presence check: pass

## Files Changed In Phase 01

- `BUILD_STATE.md`
- `.gitignore`

## Next Expected Phase

- Phase 02, only when explicitly requested.

---

## Phase 02 - Project Scaffold

Status: PASS
Completion timestamp: 2026-09-06 18:49:58 +06

## Scope

- Built the requested project skeleton only.
- Did not implement RAG logic.
- Did not install dependencies.
- Did not create `.env`.
- Did not add real secrets.
- Did not initialize Pinecone or OpenRouter.
- Did not use `template.py` to overwrite this repository.

## Files Changed In Phase 02

- `.gitignore`
- `.env.example`
- `README.md`
- `app.py`
- `data/.gitkeep`
- `requirements.txt`
- `research/trials.ipynb`
- `setup.py`
- `src/__init__.py`
- `src/config.py`
- `store_index.py`
- `template.py`
- `BUILD_STATE.md`

## Scaffold Created

- `app.py`
- `store_index.py`
- `template.py`
- `setup.py`
- `requirements.txt`
- `.env.example`
- `README.md`
- `data/.gitkeep`
- `research/trials.ipynb`
- `src/__init__.py`
- `src/config.py`

## Dependency State

- Installed environment inspected before creating `requirements.txt`.
- Python checked: Python 3.10.21
- pip checked: pip 26.2.1 for Python 3.10
- Installed packages checked:
  - pip 26.2.1
  - setuptools 84.0.0
  - wheel 0.48.0
- `requirements.txt` intentionally contains only a placeholder comment. Dependencies will be added in a later phase.
- Dependency installation action: none.

## Environment File State

- `.env.example` contains only the requested variable names and non-secret default values.
- API key variables in `.env.example` are blank:
  - `PINECONE_API_KEY=`
  - `OPENROUTER_API_KEY=`
- `.env` file exists: no.

## Commands Run In Phase 02

- `pwd`
- `find . -maxdepth 4 -type f -not -path './.git/*' | sort`
- `find . -maxdepth 4 -type d -not -path './.git/*' | sort`
- `sed -n '1,260p' BUILD_STATE.md`
- `sed -n '1,200p' .gitignore`
- `git status --short`
- `python3.10 --version`
- `python3.10 -m pip --version`
- `python3.10 -m pip list --format=columns`
- `find . -maxdepth 4 -type f -not -path './.git/*' \( -name '.env' -o -name '*.pem' -o -name '*.key' -o -name '*credential*' \) -print`
- `rg -n --hidden --glob '!.git/**' --glob '!BUILD_STATE.md' --glob '!.gitignore' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=|PINECONE_API_KEY\s*=|OPENAI_API_KEY\s*=|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `mkdir -p data research src`
- `python3.10 -m py_compile app.py store_index.py template.py setup.py src/__init__.py src/config.py`
- `python3.10 -m json.tool research/trials.ipynb >/dev/null`
- `python3.10 -c 'from setuptools import find_packages; print(find_packages(include=["src", "src.*"])); import src.config; print(src.config.REQUIRED_ENV_VARS[0])'`
- `test ! -f .env && printf 'no .env file\n'`
- `rg -n '^(.env|.venv/|venv/|__pycache__/|\*\.pyc|.pytest_cache/|.DS_Store|data/\*\.pdf|data/\*\.PDF)$' .gitignore`
- `rg -n --hidden --glob '!.git/**' --glob '!BUILD_STATE.md' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=\s*[^[:space:]]+|PINECONE_API_KEY\s*=\s*[^[:space:]]+|OPENAI_API_KEY\s*=\s*[^[:space:]]+|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `find . -type d -name '__pycache__' -print`
- `find . -type f -name '*.pyc' -print`
- `rm -r __pycache__ src/__pycache__`
- `python3.10 - <<'PY' ... compile scaffold Python files ... PY`
- `python3.10 - <<'PY' ... validate .env.example exact contents ... PY`
- `python3.10 - <<'PY' ... verify .env.example API key values are blank ... PY`
- `python3.10 - <<'PY' ... verify required scaffold files are present ... PY`
- `python3.10 - <<'PY' ... verify editable-install package discovery and src.config import ... PY`
- `rm -r src/__pycache__`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `sed -n '1,360p' BUILD_STATE.md`
- `find . -maxdepth 4 -type f -not -path './.git/*' | sort`
- `find . -maxdepth 4 -type d -not -path './.git/*' | sort`
- `find . -type d -name '__pycache__' -print`
- `find . -type f -name '*.pyc' -print`
- `rg -n --hidden --glob '!.git/**' --glob '!BUILD_STATE.md' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=\s*[^[:space:]]+|PINECONE_API_KEY\s*=\s*[^[:space:]]+|OPENAI_API_KEY\s*=\s*[^[:space:]]+|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `git status --short`

## Tests and Acceptance Checks

- Directory scaffold present: pass.
- Final scaffold directories present: `.`, `.git`, `data`, `research`, `src`.
- Existing non-scaffold planning/repo files preserved: `.gitattributes`, `.gitignore`, `BUILD_STATE.md`.
- Python placeholder syntax validation: pass.
- Minimal notebook JSON validation: pass.
- Editable-install package discovery using `find_packages(include=["src", "src.*"])`: pass, discovered `['src']`.
- `src.config` import check: pass.
- `.gitignore` includes required protections: pass.
- `.env.example` exact requested contents: pass.
- `.env.example` API key values blank: pass.
- Secret-shaped value scan outside `.git` and excluding `BUILD_STATE.md`: pass.
- `.env` absent: pass.
- Python bytecode caches removed after validation: pass.

## Unresolved Issues

- No Phase 02 blockers.
- Future content prerequisite remains: no medical source PDFs exist in `data/`. Later phases must use only actual files placed there by the user.

## Next Expected Phase

- Phase 03, only when explicitly requested.

---

## Phase 03 - Python Environment and Dependencies

Status: PASS
Completion timestamp: 2026-09-06 19:03:44 +06

## Scope

- Created the project isolated Python environment at `.venv`.
- Installed only the packages needed for the requested Phase 03 dependency/import surface.
- Updated `requirements.txt` from the Phase 02 placeholder to top-level dependency names.
- Added `requirements.lock.txt` from `.venv/bin/python -m pip freeze`.
- Did not implement application logic.
- Did not create `.env`.
- Did not request or use an OpenAI API key.
- Did not call OpenAI, OpenRouter, or Pinecone services.

## Python Environment

- Environment path: `/Users/macbook/Desktop/Fahmid/Target/7.AI App/4.Date.31.08.2026/Medical-Chatbot/.venv`
- Python executable: `.venv/bin/python`
- Python version: Python 3.10.21
- pip version: pip 26.2.1
- Initial `.venv` package set before dependency install:
  - pip 26.2.1
  - setuptools 84.0.0
- Dependency consistency check after install: pass (`pip check` reported no broken requirements).

## Top-Level Dependencies Installed

- `flask`
- `python-dotenv`
- `pypdf`
- `sentence-transformers`
- `langchain`
- `langchain-core`
- `langchain-classic`
- `langchain-community`
- `langchain-text-splitters`
- `langchain-huggingface`
- `langchain-pinecone`
- `langchain-openrouter`

Note: `langchain-openrouter` was added because Phase 03 explicitly required probing `langchain_openrouter` and importing `ChatOpenRouter`.

## Locked Versions

Verified in `requirements.lock.txt`:

- Flask 3.1.3
- python-dotenv 1.2.3
- pypdf 6.17.0
- sentence-transformers 6.0.1
- langchain 1.4.0
- langchain-core 1.6.2
- langchain-classic 1.0.8
- langchain-community 0.4.2
- langchain-text-splitters 1.1.2
- langchain-huggingface 1.2.2
- langchain-pinecone 0.2.13
- langchain-openrouter 0.2.8
- pinecone 7.3.0

## Import Paths Verified

- `PyPDFLoader`: `from langchain_community.document_loaders import PyPDFLoader`
- `RecursiveCharacterTextSplitter`: `from langchain_text_splitters import RecursiveCharacterTextSplitter`
- `HuggingFaceEmbeddings`: `from langchain_huggingface import HuggingFaceEmbeddings`
- `PineconeVectorStore`: `from langchain_pinecone import PineconeVectorStore`
- `ChatOpenRouter`: `from langchain_openrouter import ChatOpenRouter`
- `create_retrieval_chain`: `from langchain_classic.chains import create_retrieval_chain`
- `create_stuff_documents_chain`: `from langchain_classic.chains.combine_documents import create_stuff_documents_chain`

## API Relocation Notes

- `from langchain.chains import create_retrieval_chain` failed because `langchain.chains` is not present in installed `langchain==1.4.0`.
- Current working path for retrieval chain helper in this environment: `langchain_classic.chains`.
- Current working path for stuff documents helper in this environment: `langchain_classic.chains.combine_documents`.
- Official references checked:
  - `https://reference.langchain.com/python/langchain-classic/chains/retrieval/create_retrieval_chain`
  - `https://reference.langchain.com/python/langchain-classic/chains/combine_documents/stuff/create_stuff_documents_chain`
  - `https://reference.langchain.com/python/langchain-openrouter/chat_models/ChatOpenRouter`
  - `https://reference.langchain.com/python/langchain-community/document_loaders/pdf/PyPDFLoader`
  - `https://reference.langchain.com/python/langchain-huggingface/embeddings/huggingface/HuggingFaceEmbeddings`
  - `https://reference.langchain.com/python/langchain-pinecone/vectorstores/PineconeVectorStore`

## Warnings

- Importing `PyPDFLoader` from `langchain_community.document_loaders` emitted a deprecation/maintenance warning that `langchain-community` is being sunset. The import still succeeds, and Phase 03 explicitly required `langchain-community`.
- `openai==3.8.0` was installed as a transitive dependency of LangChain integrations, but no OpenAI API was called and no OpenAI API key was requested.

## Files Changed In Phase 03

- `requirements.txt`
- `requirements.lock.txt`
- `BUILD_STATE.md`

## Commands Run In Phase 03

- `pwd`
- `find . -maxdepth 4 -type f -not -path './.git/*' | sort`
- `find . -maxdepth 4 -type d -not -path './.git/*' | sort`
- `sed -n '1,420p' BUILD_STATE.md`
- `sed -n '1,220p' requirements.txt`
- `sed -n '1,220p' .gitignore`
- `git status --short`
- `python3.10 --version`
- `python3.10 -m pip --version`
- `python3.10 -m pip list --format=columns`
- `find . -maxdepth 4 -type f -not -path './.git/*' \( -name '.env' -o -name '*.pem' -o -name '*.key' -o -name '*credential*' \) -print`
- `rg -n --hidden --glob '!.git/**' --glob '!BUILD_STATE.md' --glob '!.gitignore' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=|PINECONE_API_KEY\s*=|OPENAI_API_KEY\s*=|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `python3.10 -m venv .venv`
- `.venv/bin/python --version`
- `.venv/bin/python -m pip --version`
- `.venv/bin/python -m pip list --format=columns`
- `.venv/bin/python -m pip install -r requirements.txt`
- `.venv/bin/python - <<'PY' ... required module import probes ... PY`
- `.venv/bin/python - <<'PY' ... initial symbol import probes using langchain.chains ... PY`
- `rg -n "def create_retrieval_chain|create_retrieval_chain" .venv/lib/python3.10/site-packages/langchain*`
- `rg -n "def create_stuff_documents_chain|create_stuff_documents_chain" .venv/lib/python3.10/site-packages/langchain*`
- `.venv/bin/python - <<'PY' ... print langchain and langchain_classic versions/files ... PY`
- `find .venv/lib/python3.10/site-packages/langchain_classic/chains -maxdepth 3 -type f | sort | sed -n '1,160p'`
- `.venv/bin/python - <<'PY' ... symbol import probes using langchain_classic paths ... PY`
- `.venv/bin/python -m pip check`
- `.venv/bin/python -m pip list --format=columns`
- `.venv/bin/python -m pip freeze > requirements.lock.txt`
- `sed -n '1,180p' requirements.lock.txt`
- `for pkg in Flask python-dotenv pypdf sentence-transformers langchain langchain-core langchain-classic langchain-community langchain-text-splitters langchain-huggingface langchain-pinecone langchain-openrouter pinecone; do rg -n "^${pkg}==" requirements.lock.txt || exit 1; done`
- `env -u OPENAI_API_KEY -u OPENROUTER_API_KEY -u PINECONE_API_KEY .venv/bin/python - <<'PY' ... final module and symbol import probe ... PY`
- `find . -path './.venv' -prune -o -type d -name '__pycache__' -print`
- `find . -path './.venv' -prune -o -type f -name '*.pyc' -print`
- `test ! -f .env && printf 'no .env file\n'`
- `git status --short --untracked-files=all`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=\s*[^[:space:]]+|PINECONE_API_KEY\s*=\s*[^[:space:]]+|OPENAI_API_KEY\s*=\s*[^[:space:]]+|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `git ls-files | sort`
- `git diff -- requirements.txt .gitignore BUILD_STATE.md | sed -n '1,260p'`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `tail -n 190 BUILD_STATE.md`
- `wc -l requirements.lock.txt`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -type d -name '__pycache__' -print`
- `find . -path './.venv' -prune -o -type f -name '*.pyc' -print`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=\s*[^[:space:]]+|PINECONE_API_KEY\s*=\s*[^[:space:]]+|OPENAI_API_KEY\s*=\s*[^[:space:]]+|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `test -d .venv && test -x .venv/bin/python && test -f requirements.lock.txt && printf 'phase 03 artifacts present\n'`

## Tests and Acceptance Checks

- `.venv` created with Python 3.10.21: pass.
- Dependencies installed from `requirements.txt`: pass.
- Required module imports in a clean Python process: pass.
  - `flask`
  - `dotenv`
  - `pypdf`
  - `sentence_transformers`
  - `langchain`
  - `langchain_classic`
  - `langchain_huggingface`
  - `langchain_pinecone`
  - `langchain_openrouter`
  - `pinecone`
- Required symbol imports in a clean Python process: pass.
  - `PyPDFLoader`
  - `RecursiveCharacterTextSplitter`
  - `HuggingFaceEmbeddings`
  - `PineconeVectorStore`
  - `ChatOpenRouter`
  - `create_retrieval_chain`
  - `create_stuff_documents_chain`
- Final import probe with `OPENAI_API_KEY`, `OPENROUTER_API_KEY`, and `PINECONE_API_KEY` unset: pass.
- `pip check`: pass.
- `requirements.lock.txt` created by `pip freeze`: pass.
- Exact locked versions present for required packages: pass.
- No `.env` file exists: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, and excluding `BUILD_STATE.md`: pass.
- Source tree bytecode/cache artifact check outside `.venv`: pass.
- Final Phase 03 artifact presence check: pass.
- Final Git status after Phase 03 changes: `BUILD_STATE.md` modified, `requirements.txt` modified, `requirements.lock.txt` untracked.

## Unresolved Issues

- No Phase 03 blockers.
- `langchain-community` emitted a maintenance warning during import. No code changes were made beyond dependency setup in this phase.

## Next Expected Phase

- Phase 04, only when explicitly requested.

---

## Phase 04 - Configuration and Secrets

Status: PASS
Completion timestamp: 2026-09-06 20:21:19 +06

## Scope

- Implemented `src/config.py` configuration loading and validation.
- Added configuration unit tests in `tests/test_config.py`.
- Loaded `.env` using `python-dotenv`.
- Added a frozen `Settings` dataclass.
- Added separate validation methods:
  - `validate_for_indexing()`
  - `validate_for_runtime()`
- Added clear missing-secret errors naming the missing environment variable.
- Did not install or change dependencies.
- Did not call Pinecone or OpenRouter.
- Did not call or configure paid OpenAI API usage.
- Did not print secret values.

## `.env` Handling

- `.env` existed before Phase 04 implementation.
- `.env` was not copied from `.env.example` because it already existed.
- Masked key status check showed:
  - `PINECONE_API_KEY`: set
  - `OPENROUTER_API_KEY`: set
- Secret values were not printed.
- `.env` remains ignored by Git.

## Configuration Contract

Defaults implemented:

- `PINECONE_INDEX_NAME`: `medical-bot`
- `PINECONE_CLOUD`: `aws`
- `PINECONE_REGION`: `us-east-1`
- `PINECONE_NAMESPACE`: `medical-chatbot-v1`
- `OPENROUTER_MODEL`: `openrouter/free`
- `FLASK_HOST`: `127.0.0.1`
- `FLASK_PORT`: `8080`
- `FLASK_DEBUG`: `false`
- `DATA_DIR`: `data`

## Files Changed In Phase 04

- `src/config.py`
- `tests/test_config.py`
- `BUILD_STATE.md`

## Commands Run In Phase 04

- `pwd`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `find . -maxdepth 4 -type d -not -path './.git/*' -not -path './.venv/*' | sort`
- `tail -n 240 BUILD_STATE.md`
- `sed -n '1,220p' src/config.py`
- `sed -n '1,220p' .env.example`
- `git status --short --untracked-files=all`
- `.venv/bin/python -m pip list --format=columns`
- `if test -f .env; then printf '.env exists\n'; else printf '.env missing\n'; fi`
- `.venv/bin/python - <<'PY' ... masked .env key status check ... PY`
- `test -f tests/test_config.py && sed -n '1,260p' tests/test_config.py || true`
- `mkdir -p tests`
- `.venv/bin/python - <<'PY' ... compile src/config.py and tests/test_config.py ... PY`
- `.venv/bin/python -m unittest tests.test_config -v`
- `.venv/bin/python - <<'PY' ... load settings from .env with masked secret status ... PY`
- `.venv/bin/python - <<'PY' ... missing validation error probe ... PY`
- `.venv/bin/python - <<'PY' ... masked .env key status check for API keys ... PY`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=\s*[^[:space:]]+|PINECONE_API_KEY\s*=\s*[^[:space:]]+|OPENAI_API_KEY\s*=\s*[^[:space:]]+|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `.venv/bin/python -m unittest tests.test_config -v`
- `.venv/bin/python - <<'PY' ... validation error probe for indexing and runtime secrets ... PY`
- `find . -path './.venv' -prune -o -type d -name '__pycache__' -print`
- `find . -path './.venv' -prune -o -type f -name '*.pyc' -print`
- `rm -r tests/__pycache__ src/__pycache__`
- `find . -maxdepth 4 -type f -not -path './.git/*' -not -path './.venv/*' | sort`
- `find . -maxdepth 4 -type d -not -path './.git/*' -not -path './.venv/*' | sort`
- `find . -path './.venv' -prune -o -type d -name '__pycache__' -print`
- `find . -path './.venv' -prune -o -type f -name '*.pyc' -print`
- `.venv/bin/python - <<'PY' ... final masked .env API key status check ... PY`
- `git status --short --untracked-files=all`
- `git diff -- src/config.py tests/test_config.py BUILD_STATE.md | sed -n '1,360p'`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests and Acceptance Checks

- Dependency environment inspected before implementation: pass.
- Dependency changes made: none.
- `src/config.py` syntax validation: pass.
- `tests/test_config.py` syntax validation: pass.
- Unit tests: pass, 5 tests.
  - defaults load correctly
  - boolean parsing works
  - missing `.env` file is created from `.env.example`
  - missing secret validation raises clear errors
  - model/index constants match the project contract
- `load_settings()` loads existing `.env` with `python-dotenv`: pass.
- `validate_for_indexing()` missing secret error names `PINECONE_API_KEY`: pass.
- `validate_for_runtime()` missing secret error names `OPENROUTER_API_KEY` when Pinecone key is present: pass.
- Existing `.env` API key status check: both required API key fields are set.
- No Pinecone/OpenRouter external connectivity calls made: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, and excluding `BUILD_STATE.md`: pass.
- Source tree bytecode/cache artifact check outside `.venv`: pass.

## Unresolved Issues

- No Phase 04 blockers.
- External connectivity remains intentionally untested because this phase forbids Pinecone/OpenRouter calls.

## Next Expected Phase

- Phase 05, only when explicitly requested.

---

## Phase 05 - PDF Loading

Status: PASS
Completion timestamp: 2026-09-06 20:30:28 +06

## Scope

- Implemented only the PDF loading layer in `src/helper.py`.
- Added helper-level unit tests in `tests/test_helper.py`.
- Did not split PDF text.
- Did not embed PDF text.
- Did not send PDF content to OpenRouter.
- Did not modify Pinecone, vector store, RAG, or application runtime code.
- Did not create, download, or fabricate any medical PDF.
- Did not install or change dependencies.
- Did not print `.env` secrets.

## PDF Loading Behavior

- Function implemented: `load_pdf_documents(data_dir: str | Path) -> list[Document]`
- Data directory is resolved to an absolute path.
- PDF discovery is case-insensitive using `.pdf` suffix matching.
- Missing/no-PDF state raises `FileNotFoundError` with instruction to place a legally obtained PDF in `data/`.
- PDFs are loaded with current LangChain `PyPDFLoader` import path:
  - `from langchain_community.document_loaders import PyPDFLoader`
- Returned objects are LangChain `Document` instances from `langchain_core.documents`.
- `source` metadata is ensured on each returned document.
- `page` metadata from the loader is preserved when present.
- Loader/PDF errors are wrapped as `PDFLoadError` with the source filename while preserving the original exception as `__cause__`.

## Real Data PDF Smoke Check

- Real PDF files found in `data/`: 0
- Read-only real-PDF smoke check: skipped because no PDF exists in `data/`.
- No medical content was printed.

## Files Changed In Phase 05

- `src/helper.py`
- `tests/test_helper.py`
- `BUILD_STATE.md`

## Commands Run In Phase 05

- `pwd`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `find . -maxdepth 4 -type d -not -path './.git/*' -not -path './.venv/*' | sort`
- `tail -n 260 BUILD_STATE.md`
- `sed -n '1,260p' src/config.py`
- `test -f src/helper.py && sed -n '1,260p' src/helper.py || true`
- `find data -maxdepth 2 -type f | sort`
- `git status --short --untracked-files=all`
- `.venv/bin/python - <<'PY' ... compile src/helper.py and tests/test_helper.py ... PY`
- `.venv/bin/python -m unittest tests.test_helper -v`
- `.venv/bin/python -m unittest discover -s tests -v`
- `.venv/bin/python - <<'PY' ... import src.helper load_pdf_documents and PDFLoadError ... PY`
- `find data -type f \( -iname '*.pdf' \) | sort`
- `.venv/bin/python - <<'PY' ... call load_pdf_documents('data') and print FileNotFoundError only ... PY`
- `find . -path './.venv' -prune -o -type d -name '__pycache__' -print`
- `find . -path './.venv' -prune -o -type f -name '*.pyc' -print`
- `git status --short --untracked-files=all`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=\s*[^[:space:]]+|PINECONE_API_KEY\s*=\s*[^[:space:]]+|OPENAI_API_KEY\s*=\s*[^[:space:]]+|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `rm -r tests/__pycache__ src/__pycache__`
- `find . -path './.venv' -prune -o -type d -name '__pycache__' -print`
- `find . -path './.venv' -prune -o -type f -name '*.pyc' -print`
- `find data -type f \( -iname '*.pdf' \) | sort`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Dependency environment changes made: none.
- `src/helper.py` syntax validation: pass.
- `tests/test_helper.py` syntax validation: pass.
- Helper unit tests: pass, 3 tests.
  - no PDF raises a clear `FileNotFoundError`
  - `.PDF` uppercase suffix is discovered case-insensitively
  - metadata is preserved
  - malformed/loader errors include source filename and preserve original exception
- Full test discovery: pass, 8 tests.
- Helper import probe: pass.
- Actual `data/` no-PDF probe: pass, clear error produced.
- Real PDF smoke check: skipped, no real PDF present.
- No OpenRouter calls made: pass.
- No Pinecone/RAG modifications made: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, and excluding `BUILD_STATE.md`: pass.
- Source tree bytecode/cache artifact check outside `.venv`: pass.

## Unresolved Issues

- No Phase 05 code blockers.
- `data/` contains no real medical PDF. Before any final integration check or real indexing run, manually place at least one legally obtained medical PDF in `data/`.

## Next Expected Phase

- Phase 06, only when explicitly requested.

---

## Phase 06 - Chunking and Local Embeddings

Status: PASS
Completion timestamp: 2026-09-06 21:29:20 +06

## Scope

- Implemented document chunking in `src/helper.py`.
- Implemented local CPU Hugging Face embeddings in `src/helper.py`.
- Implemented embedding dimension verification in `src/helper.py`.
- Added/updated helper-level tests in `tests/test_helper.py`.
- Did not call Pinecone.
- Did not call OpenRouter.
- Did not index anything.
- Did not send PDF content to any model API.
- Did not install or change dependencies.
- Did not print `.env` secrets.

## Chunking Behavior

- Function implemented: `split_documents(documents)`.
- Text splitter: `RecursiveCharacterTextSplitter`.
- `chunk_size`: 500.
- `chunk_overlap`: 20.
- Empty input returns `[]`.
- Original document metadata is preserved by the splitter.
- `chunk_index` metadata is added per `(source, page)` group where practical.

## Embedding Behavior

- Function implemented: `get_embeddings()`.
- Tutorial-compatible alias implemented: `download_hugging_face_embeddings()`.
- Embedding class: `langchain_huggingface.HuggingFaceEmbeddings`.
- Model: `sentence-transformers/all-MiniLM-L6-v2`.
- Local execution target: CPU via `model_kwargs={"device": "cpu"}`.
- Encode configuration: `encode_kwargs={"normalize_embeddings": True}`.
- Hugging Face API credentials are not required by code.
- Function implemented: `verify_embedding_dimension(embeddings)`.
- Dimension probe uses one short harmless string.
- Expected dimension: 384.
- Actual dimension from local smoke probe: 384.

## Real Smoke Test

- Real PDFs found in `data/`: 1.
- PDF basename observed: `Medical_book.pdf`.
- License/legal provenance was not verified by code; user is responsible for ensuring the file was legally obtained.
- Loaded pages/documents: 637.
- Chunks produced: 5860.
- First document metadata keys:
  - `creationdate`
  - `creator`
  - `moddate`
  - `page`
  - `page_label`
  - `producer`
  - `source`
  - `total_pages`
- Embedded one short probe only.
- No page text was printed.
- No indexing was performed.

## Warnings

- First local embedding probe emitted a Hugging Face warning about unauthenticated requests and optional `HF_TOKEN` for higher rate limits. No Hugging Face token was required.
- PDF smoke loading emitted many `fontTools` warnings from PDF parsing. The smoke check was rerun with PDF parser warnings suppressed to capture clean count-only output. No dependency was added for `fontTools` in this phase.

## Files Changed In Phase 06

- `src/helper.py`
- `tests/test_helper.py`
- `BUILD_STATE.md`

## Commands Run In Phase 06

- `pwd`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `find . -maxdepth 4 -type d -not -path './.git/*' -not -path './.venv/*' | sort`
- `tail -n 260 BUILD_STATE.md`
- `sed -n '1,260p' src/helper.py`
- `sed -n '1,320p' tests/test_helper.py`
- `find data -maxdepth 2 -type f | sort`
- `git status --short --untracked-files=all`
- `.venv/bin/python - <<'PY' ... inspect HuggingFaceEmbeddings signature ... PY`
- `find data -type f \( -iname '*.pdf' \) -print | wc -l`
- `find data -type f \( -iname '*.pdf' \) -exec basename {} \; | sort`
- `.venv/bin/python -m pip list --format=columns | rg '^(sentence-transformers|langchain-huggingface|langchain-text-splitters|langchain-core)\s+'`
- `.venv/bin/python - <<'PY' ... compile src/helper.py and tests/test_helper.py ... PY`
- `.venv/bin/python -m unittest tests.test_helper -v`
- `.venv/bin/python -m unittest discover -s tests -v`
- `.venv/bin/python - <<'PY' ... import Phase 06 helper functions/constants ... PY`
- `.venv/bin/python - <<'PY' ... get_embeddings and verify_embedding_dimension smoke probe ... PY`
- `.venv/bin/python - <<'PY' ... real PDF load/split smoke check ... PY`
- `.venv/bin/python - <<'PY' ... real PDF load/split smoke check with pypdf warnings suppressed ... PY`
- `.venv/bin/python -m pip check`
- `find . -path './.venv' -prune -o -type d -name '__pycache__' -print`
- `find . -path './.venv' -prune -o -type f -name '*.pyc' -print`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=\s*[^[:space:]]+|PINECONE_API_KEY\s*=\s*[^[:space:]]+|OPENAI_API_KEY\s*=\s*[^[:space:]]+|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `git status --short --untracked-files=all`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `rm -r tests/__pycache__ src/__pycache__`
- `tail -n 180 BUILD_STATE.md`
- `find . -path './.venv' -prune -o -type d -name '__pycache__' -print`
- `find . -path './.venv' -prune -o -type f -name '*.pyc' -print`
- `find data -type f \( -iname '*.pdf' \) -exec basename {} \; | sort`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=\s*[^[:space:]]+|PINECONE_API_KEY\s*=\s*[^[:space:]]+|OPENAI_API_KEY\s*=\s*[^[:space:]]+|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `git status --short --untracked-files=all`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Dependency environment inspected before implementation: pass.
- Dependency changes made: none.
- `src/helper.py` syntax validation: pass.
- `tests/test_helper.py` syntax validation: pass.
- Helper unit tests: pass, 8 tests.
  - chunk size setting is 500
  - chunk overlap setting is 20
  - metadata survives splitting
  - empty input returns `[]`
  - embedding dimension check returns 384 with a fake embedding object
  - dimension mismatch raises a clear error
  - existing PDF loader tests remain passing
- Full test discovery: pass, 13 tests.
- Helper import probe: pass.
- Local embedding dimension smoke check: pass, dimension 384.
- Real PDF smoke check: pass.
- `pip check`: pass.
- No Pinecone calls made: pass.
- No OpenRouter calls made: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, and excluding `BUILD_STATE.md`: pass.
- Source tree bytecode/cache artifacts removed outside `.venv`: pass.
- Final Git status after Phase 06 changes: `BUILD_STATE.md`, `src/helper.py`, and `tests/test_helper.py` modified.

## Unresolved Issues

- No Phase 06 code blockers.
- Local Hugging Face model artifacts may now exist in the user's Hugging Face cache outside the repository after the first model load.
- The existing `data/Medical_book.pdf` was used only for read-only smoke checks. Its legal provenance was not verified by code.

## Next Expected Phase

- Phase 07, only when explicitly requested.

---

## Phase 07 - Pinecone Index Setup

Status: PASS
Completion timestamp: 2026-09-06 21:54:04 +06

## Scope

- Implemented safe Pinecone index management in `src/pinecone_index.py`.
- Updated `store_index.py` only enough to support `--check-index`.
- Added Pinecone index-management unit tests in `tests/test_pinecone_index.py`.
- Used the current `pinecone` Python SDK (`pinecone==7.3.0`), not `pinecone-client`.
- Did not upload document chunks.
- Did not modify RAG application logic.
- Did not call OpenRouter.
- Did not print the Pinecone API key.
- Did not install or change dependencies.

## Pinecone Index Contract

- Index name source: `PINECONE_INDEX_NAME`, default `medical-bot`.
- Actual configured index checked: `medical-bot`.
- Vector type: dense.
- Dimension: 384.
- Metric: cosine.
- Deployment type: serverless.
- Configured cloud: `aws`.
- Configured region: `us-east-1`.
- Namespace remains separate from index configuration: `PINECONE_NAMESPACE=medical-chatbot-v1`.

## Implemented Functions

- `create_pinecone_client(settings=None)`: initializes Pinecone with `PINECONE_API_KEY`.
- `ensure_pinecone_index(settings=None, pinecone_client=None, wait=True)`: lists indexes, creates missing index with the project contract, validates existing indexes, waits for readiness, and returns a Pinecone `Index` connection.
- `wait_for_index_ready(pinecone_client, index_name, ...)`: polls until ready.
- `check_pinecone_index(settings=None, pinecone_client=None)`: reusable connectivity/contract check returning a safe summary object.

## Safety Behavior

- Existing indexes are inspected before use.
- If an existing index has a different dimension, metric, or vector type, the code raises `PineconeIndexError`.
- The code does not delete or recreate incompatible existing indexes automatically.
- Safe recovery options in the error message:
  - change `PINECONE_INDEX_NAME` in `.env` to a new empty index name, or
  - manually delete/recreate the existing index in Pinecone after confirming no needed data will be lost.
- Region/create failures are wrapped with the configured cloud/region and Pinecone response while redacting the API key if it appears in the message.

## Real Connectivity Check

- Command run: `.venv/bin/python store_index.py --check-index`.
- Authentication: pass.
- Target index exists: pass.
- Dimension: 384.
- Metric: cosine.
- Vector type: dense.
- Ready: True.
- No chunks uploaded.

## Files Changed In Phase 07

- `src/pinecone_index.py`
- `store_index.py`
- `tests/test_pinecone_index.py`
- `BUILD_STATE.md`

## Commands Run In Phase 07

- `pwd`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `find . -maxdepth 4 -type d -not -path './.git/*' -not -path './.venv/*' | sort`
- `tail -n 280 BUILD_STATE.md`
- `sed -n '1,260p' src/config.py`
- `sed -n '1,260p' store_index.py`
- `sed -n '1,360p' tests/test_helper.py`
- `git status --short --untracked-files=all`
- `.venv/bin/python - <<'PY' ... inspect Pinecone SDK signatures ... PY`
- `.venv/bin/python - <<'PY' ... masked Pinecone .env status check ... PY`
- `.venv/bin/python -m pip list --format=columns | rg '^(pinecone|langchain-pinecone)\s+'`
- `test -f tests/test_pinecone_index.py && sed -n '1,360p' tests/test_pinecone_index.py || true`
- `.venv/bin/python - <<'PY' ... compile src/pinecone_index.py, store_index.py, tests/test_pinecone_index.py ... PY`
- `.venv/bin/python -m unittest tests.test_pinecone_index -v`
- `.venv/bin/python -m unittest discover -s tests -v`
- `.venv/bin/python - <<'PY' ... import Pinecone index helpers/constants ... PY`
- `.venv/bin/python store_index.py --help`
- `.venv/bin/python store_index.py --check-index`
- `.venv/bin/python - <<'PY' ... describe Pinecone index contract fields ... PY`
- `.venv/bin/python -m unittest tests.test_pinecone_index -v`
- `.venv/bin/python -m unittest discover -s tests -v`
- `.venv/bin/python store_index.py --check-index`
- `.venv/bin/python - <<'PY' ... compile Phase 07 Python files ... PY`
- `.venv/bin/python -m pip check`
- `find . -path './.venv' -prune -o -type d -name '__pycache__' -print`
- `find . -path './.venv' -prune -o -type f -name '*.pyc' -print`
- `git status --short --untracked-files=all`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=\s*[^[:space:]]+|PINECONE_API_KEY\s*=\s*[^[:space:]]+|OPENAI_API_KEY\s*=\s*[^[:space:]]+|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `find data -type f \( -iname '*.pdf' \) -exec basename {} \; | sort`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `rm -r __pycache__ tests/__pycache__ src/__pycache__`
- `tail -n 190 BUILD_STATE.md`
- `find . -path './.venv' -prune -o -type d -name '__pycache__' -print`
- `find . -path './.venv' -prune -o -type f -name '*.pyc' -print`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' '(sk-[A-Za-z0-9_-]{20,}|OPENROUTER_API_KEY\s*=\s*[^[:space:]]+|PINECONE_API_KEY\s*=\s*[^[:space:]]+|OPENAI_API_KEY\s*=\s*[^[:space:]]+|BEGIN (RSA|OPENSSH|PRIVATE) KEY)' .`
- `git status --short --untracked-files=all`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Dependency environment inspected before implementation: pass.
- Dependency changes made: none.
- Pinecone SDK signature inspection: pass.
- `src/pinecone_index.py` syntax validation: pass.
- `store_index.py` syntax validation: pass.
- `tests/test_pinecone_index.py` syntax validation: pass.
- Pinecone unit tests: pass, 6 tests.
  - existing matching index returns an index connection
  - missing index is created with dimension 384, metric cosine, vector type dense
  - existing mismatched dimension stops without delete
  - existing mismatched vector type stops without delete
  - check reports verified index contract
  - `--check-index` CLI succeeds without printing fake secrets
- Full test discovery: pass, 19 tests.
- `store_index.py --help`: pass.
- Real `store_index.py --check-index`: pass.
- Real connectivity confirmed:
  - authentication works
  - target index exists
  - dimension is 384
  - metric is cosine
  - vector type is dense
  - index is ready
- `pip check`: pass.
- No Pinecone uploads performed: pass.
- No OpenRouter calls made: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, and excluding `BUILD_STATE.md`: pass.
- Source tree bytecode/cache artifacts removed outside `.venv`: pass.
- Final Git status after Phase 07 changes: `BUILD_STATE.md` modified, `store_index.py` modified, `src/pinecone_index.py` untracked, `tests/test_pinecone_index.py` untracked.

## Unresolved Issues

- No Phase 07 blockers.
- `data/Medical_book.pdf` remains present and ignored by Git; legal provenance remains the user's responsibility.

## Next Expected Phase

- Phase 08, only when explicitly requested.

---

## Phase 08 - Indexing Pipeline

Status: PASS
Completion timestamp: 2026-09-06 22:27:55 +06

## Scope

- Implemented the explicit ingestion command in `store_index.py`.
- Added reusable ingestion helpers in `src/indexing.py`.
- Added helper-level indexing tests in `tests/test_indexing.py`.
- Used existing PDF files from `data/`; no PDF content was invented or fabricated.
- Used local `sentence-transformers/all-MiniLM-L6-v2` embeddings through `langchain_huggingface.HuggingFaceEmbeddings`.
- Upserted chunks into the configured Pinecone index and namespace.
- Did not build the LLM chain.
- Did not call OpenRouter.
- Did not install or change dependencies.

## Indexing Flow Implemented

- Data source: PDFs in configured `DATA_DIR`, currently `data`.
- PDF loader: `load_pdf_documents`.
- Chunking: `split_documents` with chunk size 500 and overlap 20.
- Embeddings: local CPU all-MiniLM-L6-v2, expected dimension 384.
- Vector store: `langchain_pinecone.PineconeVectorStore`.
- Pinecone index: `medical-bot`.
- Pinecone namespace: `medical-chatbot-v1`.
- Verification query: one similarity search using a harmless short probe.

## Idempotency and Rebuild Safety

- Vector IDs are deterministic SHA-256 IDs based on source, page, chunk index, and chunk-content hash.
- Re-running `store_index.py --ingest` reuses/updates the same IDs instead of creating duplicates.
- The namespace vector count remained 5860 after two ingestion runs.
- `--rebuild` refuses to clear data unless paired with `--yes-rebuild-namespace`.
- Rebuild clearing is limited to the configured namespace only.
- `--rebuild` without confirmation was tested and failed before clearing anything.

## Real Indexing Result

- Real command run: `.venv/bin/python store_index.py --ingest`.
- PDFs found: 1.
- Pages/documents loaded: 637.
- Expected chunks: 5860.
- IDs upserted: 5860.
- Namespace vector count after indexing: 5860.
- Similarity matches returned: 1.
- Idempotency rerun result: namespace vector count remained 5860.
- Direct post-guard namespace count check: 5860.

## Files Changed In Phase 08

- `src/indexing.py`
- `store_index.py`
- `tests/test_indexing.py`
- `BUILD_STATE.md`

## Commands Run In Phase 08

- `pwd && rg --files -g '!*requirements.lock.txt' | sort | sed -n '1,200p'`
- `sed -n '1,260p' BUILD_STATE.md`
- `git status --short`
- `find . -type d -name '__pycache__' -o -type f -name '*.pyc'`
- `sed -n '1,260p' src/indexing.py`
- `sed -n '1,260p' store_index.py`
- `sed -n '1,260p' tests/test_indexing.py`
- `.venv/bin/python -m py_compile src/indexing.py store_index.py tests/test_indexing.py`
- `.venv/bin/python -m unittest discover -s tests -v`
- `.venv/bin/python store_index.py --check-index`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `.venv/bin/python store_index.py --ingest`
- `.venv/bin/python store_index.py --ingest`
- `.venv/bin/python store_index.py --ingest --rebuild`
- `.venv/bin/python -m pip check`
- `sed -n '1,120p' .gitignore`
- `.venv/bin/python - <<'PY' ... direct namespace vector count check ... PY`
- `find data -maxdepth 2 -type f | sort`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `tail -n 220 BUILD_STATE.md`
- `git diff -- store_index.py src/indexing.py tests/test_indexing.py`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `tail -n 180 BUILD_STATE.md`
- `git status --short --untracked-files=all`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `git diff --check`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Dependency changes made: none.
- `src/indexing.py` syntax validation: pass.
- `store_index.py` syntax validation: pass.
- `tests/test_indexing.py` syntax validation: pass.
- Full test discovery: pass, 28 tests.
- New indexing tests cover:
  - deterministic vector IDs are stable and content-sensitive
  - namespace clearing requires explicit confirmation
  - namespace clearing targets only the configured namespace
  - Pinecone metadata sanitizing preserves supported values
  - ingestion uses deterministic IDs and the configured namespace
  - ID collisions fail clearly
  - upsert ID count mismatch fails clearly
  - `--ingest` CLI success path does not print fake secrets
  - `--rebuild --yes-rebuild-namespace` CLI passes explicit confirmation flags
- Real Pinecone index check: pass.
- Real ingestion: pass.
- Idempotency verification: pass.
- Rebuild guard without confirmation: pass.
- `pip check`: pass.
- `.gitignore` still protects `.env`, virtual environments, caches, and PDFs: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, and excluding `BUILD_STATE.md`: pass.
- Source tree bytecode/cache artifacts removed outside `.venv`: pass.
- `git diff --check`: pass.
- No OpenRouter calls made: pass.

## Unresolved Issues

- No Phase 08 code blockers.
- `data/Medical_book.pdf` is present and ignored by Git. Its legal provenance remains the user's responsibility.
- Hugging Face emitted an unauthenticated-request warning during model loading; the local embedding run still completed successfully.

## Next Expected Phase

- Phase 09, only when explicitly requested.

---

## Phase 09 - Retriever

Status: PASS
Completion timestamp: 2026-09-06 23:55:16 +06

## Scope

- Implemented only the retrieval layer in `src/rag.py`.
- Added a read-only retrieval diagnostic CLI in `scripts/smoke_test.py`.
- Added retriever unit and integration tests in `tests/test_rag.py`.
- Reused `get_embeddings()` from `src/helper.py`.
- Connected to the existing Pinecone index through `PineconeVectorStore`.
- Used the configured Pinecone namespace.
- Did not initialize any LLM.
- Did not call OpenRouter.
- Did not install or change dependencies.
- Did not upload, delete, or rebuild Pinecone data.

## Retriever Contract

- `get_vector_store()` returns a `langchain_pinecone.PineconeVectorStore` connected to the configured Pinecone index and namespace.
- `get_retriever()` returns a vector-store retriever.
- Tutorial retrieval setting preserved: `search_kwargs={"k": 3}`.
- Diagnostic previews are capped at 160 characters.
- Diagnostic output prints only rank, source, page, and short preview rows during a successful run.

## Real Retrieval Smoke Result

- Command run: `.venv/bin/python scripts/smoke_test.py "What is diabetes?"`
- Documents returned: 3.
- Output fields: rank, source, page, preview.
- Preview length limit: 160 characters.
- No full medical page text printed.

## Files Changed In Phase 09

- `src/rag.py`
- `scripts/smoke_test.py`
- `tests/test_rag.py`
- `BUILD_STATE.md`

## Commands Run In Phase 09

- `pwd && rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 240 BUILD_STATE.md`
- `sed -n '1,260p' src/config.py`
- `sed -n '1,300p' src/helper.py`
- `sed -n '1,320p' src/pinecone_index.py`
- `sed -n '1,320p' tests/test_pinecone_index.py`
- `sed -n '1,220p' .gitignore && sed -n '1,220p' setup.py`
- `git status --short --untracked-files=all`
- `.venv/bin/python - <<'PY' ... inspect PineconeVectorStore signatures ... PY`
- `.venv/bin/python -m pip list --format=columns | rg '^(langchain-pinecone|langchain-core|langchain-huggingface|pinecone|sentence-transformers)\s+'`
- `test -f src/rag.py && sed -n '1,260p' src/rag.py || true && test -d scripts && find scripts -maxdepth 2 -type f | sort || true`
- `find data -maxdepth 2 -type f | sort`
- `.venv/bin/python -m py_compile src/rag.py scripts/smoke_test.py tests/test_rag.py`
- `.venv/bin/python -m unittest tests.test_rag -v`
- `.venv/bin/python scripts/smoke_test.py --help`
- `.venv/bin/python -m unittest discover -s tests -v`
- `.venv/bin/python scripts/smoke_test.py "What is diabetes?"`
- `.venv/bin/python -m pip check`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `git diff --check`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `tail -n 170 BUILD_STATE.md`
- `git status --short --untracked-files=all`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `git diff --check`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Dependency environment inspected before implementation: pass.
- Dependency changes made: none.
- `src/rag.py` syntax validation: pass.
- `scripts/smoke_test.py` syntax validation: pass.
- `tests/test_rag.py` syntax validation: pass.
- Retriever unit tests: pass, 5 tests.
  - vector store uses configured namespace
  - retriever preserves `search_kwargs={"k": 3}`
  - diagnostic previews preserve metadata and cap text length
  - diagnostic printing emits compact rows
  - smoke script suppresses library output during successful retrieval
- Retriever integration test: pass, 1 test.
  - live Pinecone retriever returned 1-3 documents for a normal medical query
- Full test discovery: pass, 34 tests.
- Smoke diagnostic command: pass, returned 3 compact rows.
- `pip check`: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, outside `.env`, and excluding `BUILD_STATE.md`: pass.
- Source tree bytecode/cache artifacts removed outside `.venv`: pass.
- `git diff --check`: pass.
- No OpenRouter calls made: pass.
- No LLM initialized: pass.

## Unresolved Issues

- No Phase 09 code blockers.
- The existing local PDF in `data/` remains ignored by Git, and legal provenance remains the user's responsibility.
- The test suite may still show a Hugging Face unauthenticated-request warning during the live integration test, but retrieval passes without requiring a Hugging Face token.

## Next Expected Phase

- Phase 10, only when explicitly requested.

---

## Phase 10 - OpenRouter LLM

Status: PASS
Completion timestamp: 2026-09-07 00:07:12 +06
Resolution timestamp: 2026-09-07 01:17:25 +06

## Scope

- Implemented only the OpenRouter LLM client in `src/rag.py`.
- Added `get_llm()`.
- Added `smoke_test_llm()` for a single tiny non-medical OpenRouter invocation.
- Added LLM client and error-sanitization tests in `tests/test_rag.py`.
- Did not initialize `ChatOpenAI`.
- Did not use `OPENAI_API_KEY`.
- Did not hard-code an individual free model in source code.
- Kept the model configurable through `OPENROUTER_MODEL`.
- Did not connect the LLM to retrieved medical context.
- Did not build the LLM chain.
- Did not install or change dependencies.

## LLM Client Contract

- Provider class: `langchain_openrouter.ChatOpenRouter`.
- API key source: `OPENROUTER_API_KEY`.
- Model source: `OPENROUTER_MODEL`.
- Default model remains configured in `src/config.py` as `openrouter/free`.
- Temperature: 0.
- Timeout: 15 seconds, passed to the installed `langchain_openrouter` package as `15000` milliseconds.
- Automatic retries: 0, adjusted after the first smoke attempt showed the provider client entering retry/backoff after a timeout.
- Max output tokens: 64, added because the installed OpenRouter SDK default requested up to 65536 tokens for this model/account.

## Error Handling

- Added `LLMError` for OpenRouter setup/invocation failures.
- User-facing errors are classified as:
  - authentication failure
  - model unavailable
  - rate limit / quota exceeded
  - timeout / network failure
  - generic OpenRouter request failure
- Error messages redact configured API key values, bearer tokens, API-key fields, and common key-shaped strings.

## Real OpenRouter Smoke Result

- Command run once: `.venv/bin/python - <<'PY' ... smoke_test_llm() ... PY`
- Prompt: `Reply with exactly: OK`.
- Result: BLOCKED.
- Observed failure: request timed out in the OpenRouter client and entered internal retry/backoff before completion.
- Action taken: interrupted the hung smoke process and changed client configuration to `max_retries=0` and `timeout=15`.
- No second real OpenRouter invocation was made, to avoid creating a retry loop or wasting free quota.

## OpenRouter Smoke Retry

- Retry timestamp: 2026-09-07 00:17:33 +06.
- Command run once after user requested retry: `.venv/bin/python - <<'PY' ... smoke_test_llm() with local process alarm ... PY`
- Prompt: `Reply with exactly: OK`.
- Result: BLOCKED.
- Observed failure: `OpenRouter timeout or network failure: local one-shot smoke timeout`.
- No key values were printed.
- No additional retry loop was started.

## OpenRouter Smoke Retry 2

- Retry timestamp: 2026-09-07 00:26:31 +06.
- Masked configuration check: `OPENROUTER_API_KEY` present.
- Configured model at retry time: `openai/gpt-oss-20b:free`.
- Command run once after user requested retry: `.venv/bin/python - <<'PY' ... child smoke_test_llm() with parent process timeout ... PY`
- Prompt: `Reply with exactly: OK`.
- Result: BLOCKED.
- Observed failure: `OpenRouter smoke failed: local parent timeout after one invocation`.
- No key values were printed.
- No additional retry loop was started.

## OpenRouter Smoke Retry 3

- Retry timestamp: 2026-09-07 00:29:49 +06.
- Masked configuration check: `OPENROUTER_API_KEY` present.
- Configured model at retry time: `openai/gpt-oss-120b:free`.
- Command run once after user requested retry: `.venv/bin/python - <<'PY' ... child smoke_test_llm() with parent process timeout ... PY`
- Prompt: `Reply with exactly: OK`.
- Result: BLOCKED.
- Observed failure: `OpenRouter smoke failed: local parent timeout after one invocation`.
- No key values were printed.
- No additional retry loop was started.

## OpenRouter Smoke Retry 4

- Retry timestamp: 2026-09-07 00:34:04 +06.
- Masked configuration check: `OPENROUTER_API_KEY` present.
- Configured model at retry time: `google/gemini-2.0-flash-001`.
- Command run once after user requested retry: `.venv/bin/python - <<'PY' ... child smoke_test_llm() with parent process timeout ... PY`
- Prompt: `Reply with exactly: OK`.
- Result: BLOCKED.
- Observed failure: `OpenRouter smoke failed: local parent timeout after one invocation`.
- No key values were printed.
- No additional retry loop was started.

## OpenRouter Smoke Retry 5

- Retry timestamp: 2026-09-07 00:38:07 +06.
- Masked configuration check: `OPENROUTER_API_KEY` present.
- Configured model at retry time: `anthropic/claude-3.5-sonnet`.
- Command run once after user requested retry: `.venv/bin/python - <<'PY' ... child smoke_test_llm() with parent process timeout ... PY`
- Prompt: `Reply with exactly: OK`.
- Result: BLOCKED.
- Observed failure: `OpenRouter smoke failed: local parent timeout after one invocation`.
- No key values were printed.
- No additional retry loop was started.

## OpenRouter Smoke Retry 6

- Retry timestamp: 2026-09-07 01:10:08 +06.
- Masked configuration check: `OPENROUTER_API_KEY` present.
- Configured model at retry time: `openai/gpt-chat-latest`.
- Command run once after user requested retry: `.venv/bin/python - <<'PY' ... child smoke_test_llm() with parent process timeout ... PY`
- Prompt: `Reply with exactly: OK`.
- Result: BLOCKED.
- Observed failure: `OpenRouter smoke failed: local parent timeout after one invocation`.
- No key values were printed.
- No additional retry loop was started.

## Root Cause and Resolution

- New evidence from user: direct curl from the same Mac/project terminal succeeded with `OPENROUTER_MODEL=openai/gpt-chat-latest` and returned `OK`.
- Python `.env` loading was verified: `OPENROUTER_API_KEY` was present and `OPENROUTER_MODEL` was `openai/gpt-chat-latest`.
- Proxy environment was inspected: no `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, or `NO_PROXY` settings were present.
- Installed `langchain_openrouter` source was inspected.
- Root cause 1: `ChatOpenRouter.timeout` maps to the OpenRouter SDK `timeout_ms`, so the previous `timeout=15` was interpreted as 15 milliseconds, not 15 seconds.
- Root cause 2: after testing with an explicit 15000 ms timeout, the request reached OpenRouter but failed because the SDK/provider path requested up to 65536 tokens by default; OpenRouter reported the account/model could only afford 119 tokens for that request.
- Code change: `get_llm()` now passes `timeout=LLM_TIMEOUT_SECONDS * 1000` and `max_tokens=64`.
- Real application-level smoke after the fix used `openai/gpt-chat-latest`, completed successfully, returned a non-empty response, and the response preview was `OK`.
- No API key values were printed.
- No retry loop was introduced.

## Files Changed In Phase 10

- `src/rag.py`
- `tests/test_rag.py`
- `BUILD_STATE.md`

## Commands Run In Phase 10

- `pwd && rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 260 BUILD_STATE.md`
- `sed -n '1,320p' src/rag.py`
- `sed -n '1,260p' src/config.py`
- `.venv/bin/python - <<'PY' ... inspect ChatOpenRouter signatures ... PY`
- `.venv/bin/python - <<'PY' ... locate langchain_openrouter package ... PY`
- `.venv/bin/python -m pip list --format=columns | rg '^(langchain-openrouter|langchain-core|openai|httpx|pydantic)\s+'`
- `sed -n '1,160p' .env.example && sed -n '1,260p' tests/test_rag.py`
- `.venv/bin/python -m py_compile src/rag.py tests/test_rag.py`
- `.venv/bin/python -m unittest tests.test_rag -v`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' 'ChatOpenAI|OPENAI_API_KEY' .`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' 'sk-or-v1-|sk-[A-Za-z0-9_-]{20,}' src tests scripts .env.example README.md setup.py store_index.py app.py template.py`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' 'ChatOpenAI|OPENAI_API_KEY' src tests scripts app.py store_index.py template.py setup.py README.md .env.example`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `.venv/bin/python - <<'PY' ... smoke_test_llm() one-shot OpenRouter smoke ... PY`
- `.venv/bin/python -m unittest discover -s tests -v`
- `.venv/bin/python - <<'PY' ... instantiate get_llm without invoking ... PY`
- `.venv/bin/python -m pip check`
- `git diff -- src/rag.py tests/test_rag.py`
- `git diff --check`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `git status --short --untracked-files=all`
- `.venv/bin/python - <<'PY' ... retry smoke_test_llm() once with local process alarm ... PY`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `.venv/bin/python - <<'PY' ... masked OpenRouter key/model configuration check ... PY`
- `.venv/bin/python - <<'PY' ... retry smoke_test_llm() once in child process with parent timeout ... PY`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `sed -n '1,260p' /Users/macbook/.codex/attachments/46b09151-85c0-4dc8-a039-933f1eb00fde/pasted-text.txt`
- `sed -n '261,520p' /Users/macbook/.codex/attachments/46b09151-85c0-4dc8-a039-933f1eb00fde/pasted-text.txt`
- `.venv/bin/python - <<'PY' ... inspect ChatOpenRouter implementation, validators, timeout mapping, and SDK constructor ... PY`
- `.venv/bin/python - <<'PY' ... inspect proxy environment variables without values ... PY`
- `.venv/bin/python - <<'PY' ... verify Python load_settings sees masked OpenRouter configuration ... PY`
- `.venv/bin/python - <<'PY' ... minimal ChatOpenRouter diagnostic with timeout=15000 and max_retries=0 ... PY`
- `.venv/bin/python -m py_compile src/rag.py tests/test_rag.py`
- `.venv/bin/python -m unittest tests.test_rag -v`
- `.venv/bin/python -m unittest discover -v`
- `.venv/bin/python -m unittest discover -s tests -v`
- `.venv/bin/python -m pip check`
- `.venv/bin/python - <<'PY' ... real smoke_test_llm() after fix ... PY`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' 'ChatOpenAI|OPENAI_API_KEY' src tests scripts app.py store_index.py template.py setup.py README.md .env.example`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `git diff --check`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `.venv/bin/python - <<'PY' ... masked OpenRouter key/model configuration check ... PY`
- `.venv/bin/python - <<'PY' ... retry smoke_test_llm() once in child process with parent timeout ... PY`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `.venv/bin/python - <<'PY' ... masked OpenRouter key/model configuration check ... PY`
- `.venv/bin/python - <<'PY' ... retry smoke_test_llm() once in child process with parent timeout ... PY`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `.venv/bin/python - <<'PY' ... masked OpenRouter key/model configuration check ... PY`
- `.venv/bin/python - <<'PY' ... retry smoke_test_llm() once in child process with parent timeout ... PY`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `.venv/bin/python - <<'PY' ... masked OpenRouter key/model configuration check ... PY`
- `.venv/bin/python - <<'PY' ... retry smoke_test_llm() once in child process with parent timeout ... PY`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Dependency environment inspected before implementation: pass.
- Dependency changes made: none.
- `ChatOpenRouter` installed API inspected: pass.
- `src/rag.py` syntax validation: pass.
- `tests/test_rag.py` syntax validation: pass.
- Retriever and LLM focused tests: pass, 12 tests.
- Full test discovery: pass, 40 tests.
- `get_llm()` instantiation with configured `.env`: pass.
- LLM smoke helper invokes exactly once in unit tests: pass.
- User-facing error sanitization tests: pass.
- `ChatOpenAI` / `OPENAI_API_KEY` scoped source scan: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, outside `.env`, and excluding `BUILD_STATE.md`: pass.
- `pip check`: pass.
- Source tree bytecode/cache artifacts removed outside `.venv`: pass.
- `git diff --check`: pass.
- Real OpenRouter one-shot smoke test: blocked by timeout.
- Real OpenRouter one-shot smoke retry: blocked by local timeout/network failure.
- Real OpenRouter one-shot smoke retry 2: blocked by parent timeout.
- Real OpenRouter one-shot smoke retry 3: blocked by parent timeout.
- Real OpenRouter one-shot smoke retry 4: blocked by parent timeout.
- Real OpenRouter one-shot smoke retry 5: blocked by parent timeout.
- Real OpenRouter one-shot smoke retry 6: blocked by parent timeout.
- Minimal `ChatOpenRouter` diagnostic with `timeout=15000` and no `max_tokens`: reached OpenRouter and failed with a quota/token-limit response, confirming the earlier timeout diagnosis exposed a separate default-token issue.
- `python -m unittest discover -v`: ran 0 tests due this repository's discovery layout.
- `python -m unittest discover -s tests -v`: pass, 40 tests.
- Real application-level OpenRouter smoke after fix: pass.
- Successful smoke model: `openai/gpt-chat-latest`.
- Successful smoke response was non-empty: yes.
- Successful smoke response preview: `OK`.

## Unresolved Issues

- No Phase 10 code blockers found.

## Next Expected Phase

- Phase 11, only when explicitly requested.

---

## Phase 11 - RAG Chain

Status: PASS
Completion timestamp: 2026-09-07 01:23:50 +06

## Scope

- Implemented `src/prompt.py`.
- Finished the core tutorial-style RAG chain in `src/rag.py`.
- Added unit tests for the prompt and RAG chain behavior in `tests/test_rag.py`.
- Used `ChatPromptTemplate` from `langchain_core.prompts`.
- Used `create_retrieval_chain` from `langchain_classic.chains`.
- Used `create_stuff_documents_chain` from `langchain_classic.chains.combine_documents`.
- Did not add application UI or Flask routes.
- Did not change dependencies.
- Did not upload, delete, or rebuild Pinecone data.

## Prompt Contract

- System role: educational medical-information assistant.
- Factual medical claims must use only supplied retrieved context.
- Unsupported-context fallback is exactly: `I don't know based on the provided medical source.`
- Prompt instructs the model not to invent diagnoses, treatments, drug doses, contraindications, or facts absent from context.
- Prompt instructs the model not to claim to replace a clinician.
- Prompt instructs urgent professional/emergency help for possible emergencies.
- Prompt keeps answers concise and readable.
- System message includes `{context}`.
- Human message uses `{input}`.

## RAG Chain Contract

- `get_rag_chain()` builds:
  - `question_answer_chain = create_stuff_documents_chain(llm, prompt)`
  - `rag_chain = create_retrieval_chain(retriever, question_answer_chain)`
- `answer_question(question)` rejects empty or whitespace-only input.
- `answer_question(question)` invokes the chain with `{"input": question}`.
- `answer_question(question)` extracts final answer text robustly from common returned structures.
- `answer_question(question)` returns a Flask-suitable dictionary:
  - `answer`
  - `sources`
- Returned `sources` contain only metadata such as source and page.
- Full retrieved context is not returned by `answer_question()`.

## Real End-to-End RAG Query

- Command run once after unit tests passed: `.venv/bin/python - <<'PY' ... answer_question('What is diabetes mellitus?') ... PY`
- Query: `What is diabetes mellitus?`
- Result: PASS.
- Answer non-empty: yes.
- Source metadata count: 3.
- Full retrieved context printed: no.
- OpenRouter model used from `.env`: `openai/gpt-chat-latest`.

## Files Changed In Phase 11

- `src/prompt.py`
- `src/rag.py`
- `tests/test_rag.py`
- `BUILD_STATE.md`

## Commands Run In Phase 11

- `pwd && rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 300 BUILD_STATE.md`
- `sed -n '1,260p' src/rag.py`
- `sed -n '1,320p' tests/test_rag.py`
- `.venv/bin/python - <<'PY' ... inspect ChatPromptTemplate and chain factory signatures ... PY`
- `.venv/bin/python - <<'PY' ... inspect create_retrieval_chain and create_stuff_documents_chain source ... PY`
- `test -f src/prompt.py && sed -n '1,220p' src/prompt.py || true`
- `git status --short --untracked-files=all`
- `.venv/bin/python -m py_compile src/prompt.py src/rag.py tests/test_rag.py`
- `.venv/bin/python -m unittest tests.test_rag -v`
- `.venv/bin/python -m unittest discover -s tests -v`
- `.venv/bin/python -m unittest discover -v`
- `.venv/bin/python - <<'PY' ... real answer_question RAG query ... PY`
- `.venv/bin/python -m pip check`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' 'ChatOpenAI|OPENAI_API_KEY' src tests scripts app.py store_index.py template.py setup.py README.md .env.example`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `git diff --check`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `git diff -- src/rag.py src/prompt.py tests/test_rag.py`
- `tail -n 220 BUILD_STATE.md`
- `git status --short --untracked-files=all`
- `git diff --check`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `git diff --stat`
- `tail -n 90 BUILD_STATE.md`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Dependency environment inspected before implementation: pass.
- Dependency changes made: none.
- Installed chain factory signatures inspected: pass.
- `src/prompt.py` syntax validation: pass.
- `src/rag.py` syntax validation: pass.
- `tests/test_rag.py` syntax validation: pass.
- Focused RAG tests: pass, 17 tests.
- Full suite with repository test path: pass, 45 tests.
- `python -m unittest discover -v`: ran 0 tests due this repository's discovery layout.
- `answer_question()` empty input rejection: pass.
- `answer_question()` invokes with `{"input": question}`: pass.
- `answer_question()` does not return full context: pass.
- Unsupported-context behavior covered by prompt-level validation and deterministic fake chain: pass.
- Real end-to-end RAG query after tests: pass.
- `pip check`: pass.
- `ChatOpenAI` / `OPENAI_API_KEY` scoped source scan: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, outside `.env`, and excluding `BUILD_STATE.md`: pass.
- Source tree bytecode/cache artifacts removed outside `.venv`: pass.
- `git diff --check`: pass.

## Unresolved Issues

- No Phase 11 code blockers found.
- The real RAG query emitted the existing Hugging Face unauthenticated-request warning during embedding model load; retrieval and answer generation completed successfully.
- The existing local PDF in `data/` remains ignored by Git, and legal provenance remains the user's responsibility.

## Next Expected Phase

- Phase 12, only when explicitly requested.

---

## Phase 12 - Flask Backend

Status: PASS
Completion timestamp: 2026-09-07 01:33:39 +06

## Scope

- Replaced the Phase 02 `app.py` placeholder with the Flask backend.
- Added `app = Flask(__name__)`.
- Added GET `/` to render `templates/chat.html`.
- Added POST `/get` for tutorial-compatible `msg` form data and JSON `message`.
- Added whitespace normalization and HTTP 400 rejection for empty input.
- Added lazy call to `src.rag.answer_question()` only inside POST `/get`.
- Added lightweight GET `/health` without Pinecone or OpenRouter calls.
- Added Flask test-client tests.
- Added the minimal `templates/chat.html` needed by the backend route.
- Did not change frontend appearance beyond the minimal renderable template needed for GET `/`.
- Did not change dependencies.
- Did not call OpenRouter in Phase 12 tests.
- Did not upload, delete, rebuild, or query Pinecone from the Flask route tests.

## Backend Contract

- Successful POST `/get` returns JSON shaped as `{"answer": "..."}`.
- Missing or empty input maps to HTTP 400.
- Missing runtime configuration maps to HTTP 503.
- OpenRouter model unavailable, rate-limit/quota, auth, timeout, and network errors map to HTTP 503 with friendly messages.
- Pinecone index failures map to HTTP 503.
- Generic unexpected exceptions map to HTTP 500 with a generic message.
- Stack traces and raw exception details are not exposed by handled route errors.
- `/health` returns `status`, `runtime_configuration_present`, and missing variable names only.
- `/health` never returns secret values.
- Startup host, port, and debug mode come from `Settings`.
- Default host remains `127.0.0.1`.
- Default port remains `8080`.

## Files Changed In Phase 12

- `app.py`
- `templates/chat.html`
- `tests/test_app.py`
- `BUILD_STATE.md`

## Commands Run In Phase 12

- `pwd && rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 180 BUILD_STATE.md`
- `sed -n '1,280p' app.py`
- `sed -n '1,320p' src/config.py`
- `sed -n '1,360p' src/rag.py`
- `sed -n '1,260p' tests/test_config.py`
- `sed -n '1,260p' tests/test_rag.py`
- `find templates -maxdepth 3 -type f -print 2>/dev/null || true`
- `sed -n '261,560p' tests/test_rag.py`
- `sed -n '1,260p' src/pinecone_index.py`
- `sed -n '1,260p' tests/test_pinecone_index.py`
- `find . -maxdepth 3 -type f \( -name '*app*' -o -path './templates/*' \) -print`
- `.venv/bin/python -m py_compile app.py tests/test_app.py`
- `.venv/bin/python -m unittest tests.test_app -v`
- `.venv/bin/python -m unittest discover -s tests -v`
- `.venv/bin/python - <<'PY' ... list Flask routes ... PY`
- `.venv/bin/python -m pip check`
- `git diff -- app.py templates/chat.html tests/test_app.py`
- `sed -n '1,240p' tests/test_app.py`
- `sed -n '1,220p' templates/chat.html`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `git diff --stat`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `git diff --check`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' 'ChatOpenAI|OPENAI_API_KEY' app.py src tests scripts store_index.py template.py setup.py README.md .env.example`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `tail -n 120 BUILD_STATE.md`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Dependency environment inspected: pass.
- Dependency changes made: none.
- `app.py` syntax validation: pass.
- `tests/test_app.py` syntax validation: pass.
- Focused Flask backend tests: pass, 9 tests.
- Full suite with repository test path: pass, 54 tests.
- GET `/` returns 200: pass.
- POST `/get` empty returns 400: pass.
- POST `/get` with mocked `answer_question()` returns 200 JSON: pass.
- POST `/get` accepts form field `msg`: pass.
- GET `/health` returns 200 without exposing secrets: pass.
- Flask route import/listing completed without external API calls: pass.
- `pip check`: pass.
- `ChatOpenAI` / `OPENAI_API_KEY` scoped source scan: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, outside `.env`, and excluding `BUILD_STATE.md`: pass.
- Source tree bytecode/cache artifacts removed outside `.venv`: pass.
- `git diff --check`: pass.

## Unresolved Issues

- No Phase 12 code blockers found.
- Full test discovery still emits the existing Hugging Face unauthenticated-request warning from the prior retriever integration test when credentials and index are available.

## Next Expected Phase

- Phase 13, only when explicitly requested.

---

## Phase 13 - Frontend

Status: PASS
Completion timestamp: 2026-09-07 01:40:37 +06

## Scope

- Implemented `templates/chat.html` as a responsive single-page chat UI.
- Added `static/style.css`.
- Preserved the existing Phase 12 Flask backend behavior.
- Did not add authentication, accounts, history databases, or extra features.
- Did not change dependencies.
- Did not call OpenRouter from browser JavaScript.
- Did not call Pinecone from browser JavaScript.
- Did not expose API keys in browser JavaScript.
- Did not use external CDN dependencies.

## Frontend Contract

- Header text: `Medical Knowledge Assistant`.
- Visible subtitle: `Answers are grounded in the uploaded medical source.`
- Includes chat transcript area.
- Includes user and assistant message bubbles.
- Includes textarea input and send button.
- Enter submits.
- Shift+Enter can insert a newline.
- Loading/typing state is shown while a request is pending.
- Duplicate submissions are disabled while a request is pending.
- Browser sends `POST /get` with JSON shaped as `{ "message": userText }`.
- Browser reads JSON shaped as `{ "answer": "..." }`.
- HTTP failures show friendly error messages.
- User and assistant content is rendered with `textContent`, not raw HTML insertion.
- Focus returns to the input after a response or handled failure.
- Includes disclaimer: `Educational information only. Not a substitute for professional medical advice.`
- Input and send button include accessible labels.
- Styling is kept in `static/style.css`.

## Files Changed In Phase 13

- `templates/chat.html`
- `static/style.css`
- `tests/test_app.py`
- `BUILD_STATE.md`

## Commands Run In Phase 13

- `pwd && rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 180 BUILD_STATE.md`
- `sed -n '1,240p' templates/chat.html`
- `sed -n '1,220p' app.py`
- `.venv/bin/python -m py_compile app.py tests/test_app.py`
- `.venv/bin/python -m unittest tests.test_app -v`
- `.venv/bin/python -m unittest discover -s tests -v`
- `.venv/bin/python - <<'PY' ... print configured Flask host/port/debug ... PY`
- `lsof -nP -iTCP:8080 -sTCP:LISTEN || true`
- `.venv/bin/python app.py`
- `curl -sS -o /tmp/medical_chatbot_home.html -w '%{http_code}\n' http://127.0.0.1:8080/`
- `curl -sS -o /tmp/medical_chatbot_style.css -w '%{http_code}\n' http://127.0.0.1:8080/static/style.css`
- `curl -sS http://127.0.0.1:8080/health`
- `rg -n 'OpenRouter|openrouter|Pinecone|pinecone|OPENROUTER|PINECONE|innerHTML|insertAdjacentHTML|outerHTML' templates static || true`
- `rg -n 'https?://|cdn|api\.openrouter|pinecone\.io' templates static || true`
- `git diff -- templates/chat.html static/style.css tests/test_app.py app.py`
- `git status --short --untracked-files=all`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `git diff --check`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' 'ChatOpenAI|OPENAI_API_KEY' app.py src tests scripts store_index.py template.py setup.py README.md .env.example templates static`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `tail -n 130 BUILD_STATE.md`
- `curl -sS -o /tmp/medical_chatbot_home_final.html -w '%{http_code}\n' http://127.0.0.1:8080/`
- `rg -n 'Completion timestamp' BUILD_STATE.md`
- `sed -n '1588,1710p' BUILD_STATE.md`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Dependency environment inspected: pass.
- Dependency changes made: none.
- `app.py` syntax validation: pass.
- `tests/test_app.py` syntax validation: pass.
- Focused Flask/frontend tests: pass, 11 tests.
- Full suite with repository test path: pass, 56 tests.
- GET `/` renders the Phase 13 frontend: pass.
- Static stylesheet served from `/static/style.css`: pass.
- Manual local GET `/`: pass, HTTP 200.
- Manual local GET `/static/style.css`: pass, HTTP 200.
- Manual local GET `/health`: pass, HTTP 200 and no secret values.
- Browser-side direct OpenRouter/Pinecone reference scan: pass.
- Browser-side raw HTML insertion scan: pass.
- External URL/CDN scan for `templates/` and `static/`: pass.
- `ChatOpenAI` / `OPENAI_API_KEY` scoped source scan: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, outside `.env`, and excluding `BUILD_STATE.md`: pass.
- Source tree bytecode/cache artifacts removed outside `.venv`: pass.
- `git diff --check`: pass.

## Unresolved Issues

- No Phase 13 code blockers found.
- Full test discovery still emits the existing Hugging Face unauthenticated-request warning from the prior retriever integration test when credentials and index are available.
- The Flask development server is running locally at `http://127.0.0.1:8080`.

## Next Expected Phase

- Phase 14, only when explicitly requested.

---

## Phase 14 - Medical Safety and RAG Hardening

Status: PASS
Completion timestamp: 2026-09-07 01:48:24 +06

## Scope

- Reviewed the browser to Flask to RAG request path.
- Hardened the RAG system prompt against retrieved-document prompt injection.
- Added explicit prompt priority wording: system rules outrank user text and retrieved context.
- Added explicit wording that retrieved PDF text is data, not instructions.
- Added backend and RAG input length limits.
- Added emergency-like input handling that returns a short urgent-care recommendation without invoking retrieval or the LLM.
- Preserved the educational disclaimer in the UI.
- Preserved top-k retrieval behavior from the tutorial.
- Did not add a moderation API or paid service.
- Did not change dependencies.
- Did not call OpenRouter as part of Phase 14 tests.
- Did not upload, delete, rebuild, or index Pinecone data.

## Safety Contract

- Retrieved PDF text is treated as untrusted data, not executable instructions.
- Prompt tells the model to ignore role changes, policy changes, tool requests, or override attempts in retrieved context.
- Insufficient-context behavior remains exactly: `I don't know based on the provided medical source.`
- Prompt continues to prohibit fabricated diagnoses, treatments, drug doses, contraindications, and unsupported certainty.
- Emergency-like user statements return: `If this may be an emergency, seek urgent professional or emergency help now.`
- One request is limited to 2000 normalized characters.
- The Flask route rejects overlong requests before calling RAG.
- No default application logging of full medical user queries was added.
- The browser still sends only the user's current question to `/get`.
- The LLM context remains limited to retrieved chunks supplied by the retriever chain, not the whole PDF.

## Files Changed In Phase 14

- `app.py`
- `src/prompt.py`
- `src/rag.py`
- `templates/chat.html`
- `tests/test_app.py`
- `tests/test_rag.py`
- `BUILD_STATE.md`

## Commands Run In Phase 14

- `pwd && rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 180 BUILD_STATE.md`
- `sed -n '1,260p' src/prompt.py`
- `sed -n '1,280p' src/rag.py`
- `sed -n '1,260p' app.py`
- `sed -n '1,260p' templates/chat.html`
- `sed -n '1,320p' tests/test_app.py`
- `sed -n '1,360p' tests/test_rag.py`
- `git diff -- app.py src/prompt.py src/rag.py templates/chat.html`
- `.venv/bin/python -m py_compile app.py src/prompt.py src/rag.py tests/test_app.py tests/test_rag.py`
- `.venv/bin/python -m unittest tests.test_rag tests.test_app -v`
- `.venv/bin/python -m unittest discover -s tests -v`
- `lsof -nP -iTCP:8080 -sTCP:LISTEN || true`
- `.venv/bin/python - <<'PY' ... print configured Flask host/port/debug ... PY`
- `rg -n 'logger\.|logging\.|print\(|console\.log|console\.error|console\.warn' app.py src templates static || true`
- `rg -n 'innerHTML|insertAdjacentHTML|outerHTML|OpenRouter|openrouter|Pinecone|pinecone|OPENROUTER|PINECONE|api\.openrouter|pinecone\.io|https?://|cdn' templates static || true`
- `.venv/bin/python app.py`
- `curl -sS -o /tmp/medical_chatbot_phase14_home.html -w '%{http_code}\n' http://127.0.0.1:8080/`
- `curl -sS -o /tmp/medical_chatbot_phase14_style.css -w '%{http_code}\n' http://127.0.0.1:8080/static/style.css`
- `curl -sS http://127.0.0.1:8080/health`
- `curl -sS -X POST -H 'Content-Type: application/json' -d '{"message":"   "}' -o /tmp/medical_chatbot_phase14_empty.json -w '%{http_code}\n' http://127.0.0.1:8080/get`
- `.venv/bin/python -m pip check`
- `git diff --check`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' 'ChatOpenAI|OPENAI_API_KEY' app.py src tests scripts store_index.py template.py setup.py README.md .env.example templates static`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `git diff --stat`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `tail -n 150 BUILD_STATE.md`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Dependency environment inspected: pass.
- Dependency changes made: none.
- `app.py` syntax validation: pass.
- `src/prompt.py` syntax validation: pass.
- `src/rag.py` syntax validation: pass.
- `tests/test_app.py` syntax validation: pass.
- `tests/test_rag.py` syntax validation: pass.
- Focused RAG and Flask tests: pass, 35 tests.
- Full suite with repository test path: pass, 63 tests.
- Prompt-injection phrase inside a fake retrieved document is treated as content, not instruction: pass.
- Empty input rejection: pass.
- Overlong input rejection: pass.
- Insufficient-context behavior: pass.
- No secret leakage in wrapped RAG errors: pass.
- Emergency-like input returns a short urgent-care response without calling the chain: pass.
- UI educational disclaimer remains visible: pass.
- Browser-side raw HTML insertion scan: pass.
- Browser-side direct OpenRouter/Pinecone reference scan: pass.
- Manual local GET `/`: pass, HTTP 200.
- Manual local GET `/static/style.css`: pass, HTTP 200.
- Manual local GET `/health`: pass, HTTP 200 and no secret values.
- Manual local empty POST `/get`: pass, HTTP 400.
- `pip check`: pass.
- `ChatOpenAI` / `OPENAI_API_KEY` scoped source scan: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, outside `.env`, and excluding `BUILD_STATE.md`: pass.
- `git diff --check`: pass.

## Unresolved Issues

- No Phase 14 code blockers found.
- Full test discovery still emits the existing Hugging Face unauthenticated-request warning from the prior retriever integration test when credentials and index are available.
- The Flask development server is running locally at `http://127.0.0.1:8080`.

## Next Expected Phase

- Phase 15, only when explicitly requested.
