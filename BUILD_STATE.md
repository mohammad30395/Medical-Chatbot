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

---

## Phase 15 - Test Suite

Status: PASS
Completion timestamp: 2026-09-07 11:32:02 +06

## Scope

- Audited tests under `tests/`.
- Added pytest as the project test runner dependency.
- Added `pytest.ini`.
- Ensured default `pytest -q` does not call Pinecone or OpenRouter.
- Marked integration tests with `pytest.mark.integration`.
- Added automatic integration skips unless `RUN_INTEGRATION_TESTS=1`.
- Added opt-in integration coverage for Pinecone index checks, top-k retrieval, and one OpenRouter smoke generation.
- Preserved existing unittest-compatible tests.
- Did not run quota-consuming OpenRouter integration tests automatically.
- Did not change application behavior outside test-runner integration boundaries.

## Unit Coverage Verified

- Configuration defaults and secret validation: covered.
- PDF loader no-file behavior: covered.
- Chunk size 500 and overlap 20: covered.
- Metadata preservation: covered.
- Embedding dimension verification logic with mocked embeddings: covered.
- Retriever `k=3`: covered.
- System prompt context grounding and unknown-answer rule: covered.
- `answer_question()` input validation: covered.
- Flask GET `/`: covered.
- Flask POST `/get` success with mocked RAG: covered.
- Flask invalid input: covered.
- Health endpoint: covered.
- Secret-safe errors: covered.

## Integration Test Contract

- Integration tests are marked with `@pytest.mark.integration`.
- Integration tests skip unless `RUN_INTEGRATION_TESTS=1`.
- When enabled, integration tests verify:
  - Pinecone connectivity.
  - Pinecone index dimension and metric.
  - Top-k retrieval.
  - At most one OpenRouter generation request through `smoke_test_llm()`.

## Files Changed In Phase 15

- `pytest.ini`
- `requirements.txt`
- `requirements.lock.txt`
- `tests/test_rag.py`
- `tests/test_integration.py`
- `BUILD_STATE.md`

## Commands Run In Phase 15

- `pwd && rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 180 BUILD_STATE.md`
- `.venv/bin/python -m pip show pytest pytest-mock 2>/dev/null || true`
- `.venv/bin/python -m pip list --format=columns | sed -n '1,220p'`
- `sed -n '1,240p' requirements.txt`
- `sed -n '1,280p' tests/test_helper.py`
- `sed -n '1,320p' tests/test_indexing.py`
- `sed -n '1,260p' requirements.lock.txt`
- `lsof -nP -iTCP:8080 -sTCP:LISTEN || true`
- `sed -n '1,260p' setup.py`
- `find . -maxdepth 2 -type f \( -name 'pytest.ini' -o -name 'pyproject.toml' -o -name 'setup.cfg' -o -name 'tox.ini' \) -print`
- `.venv/bin/python -m pip install pytest`
- `.venv/bin/python - <<'PY' ... import pytest and print version ... PY`
- `.venv/bin/python -m pip freeze`
- `.venv/bin/python -m pip freeze > requirements.lock.txt`
- `env | rg '^RUN_INTEGRATION_TESTS=' || true`
- `.venv/bin/python -m py_compile tests/test_integration.py tests/test_rag.py`
- `.venv/bin/pytest -q`
- `sed -n '1,220p' pytest.ini`
- `sed -n '1,260p' tests/test_integration.py`
- `rg -n 'RUN_INTEGRATION_TESTS|pytest.mark.integration|smoke_test_llm|check_pinecone_index|get_retriever' tests`
- `.venv/bin/pytest -q --collect-only`
- `.venv/bin/python -m pip check`
- `.venv/bin/python - <<'PY' ... import pytest and print version ... PY`
- `git diff --check`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' 'ChatOpenAI|OPENAI_API_KEY' app.py src tests scripts store_index.py template.py setup.py README.md .env.example templates static pytest.ini requirements.txt`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `git diff -- pytest.ini requirements.txt requirements.lock.txt tests/test_rag.py tests/test_integration.py tests/test_app.py`
- `git status --short --untracked-files=all`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `.venv/bin/python - <<'PY' ... non-secret configuration presence check ... PY`
- `rg -n 'vector_count|indexed data|indexed|upsert|namespace.*vector|5860' BUILD_STATE.md | tail -n 20`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `git diff --check`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' 'ChatOpenAI|OPENAI_API_KEY' app.py src tests scripts store_index.py template.py setup.py README.md .env.example templates static pytest.ini requirements.txt`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `tail -n 130 BUILD_STATE.md`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Dependency environment inspected before adding pytest: pass.
- Dependency changed: added `pytest`.
- Post-dependency import check: pass, pytest 9.1.1.
- `requirements.lock.txt` refreshed with exact installed versions: pass.
- `tests/test_integration.py` syntax validation: pass.
- `tests/test_rag.py` syntax validation: pass.
- Default `pytest -q`: pass.
- Default `pytest -q` result: 62 passed, 3 skipped, 15 subtests passed.
- Default `pytest -q` did not call Pinecone or OpenRouter: pass, integration tests skipped.
- Pytest collection: pass, 65 tests collected.
- Integration tests are clearly marked: pass.
- Integration tests skip unless `RUN_INTEGRATION_TESTS=1`: pass.
- `pip check`: pass.
- `ChatOpenAI` / `OPENAI_API_KEY` scoped source scan: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, outside `.env`, and excluding `BUILD_STATE.md`: pass.
- Source tree bytecode/cache artifacts removed outside `.venv`: pass.
- `git diff --check`: pass.

## Unresolved Issues

- Opt-in integration suite was not run because it can consume OpenRouter quota.
- Non-secret config presence check shows Pinecone and OpenRouter key fields are populated.
- Earlier build-state records show namespace vector count of 5860, so indexed data appears to exist.
- Default pytest emits the existing `langchain-community` deprecation warning from the PDF loader import. The installed loader path still resolves through `langchain_community` in this environment.

## Next Expected Phase

- Phase 16, only when explicitly requested.

---

## Phase 16 - End-to-End Local Smoke Test

Status: BLOCKED
Completion timestamp: 2026-09-07 11:43:51 +06

## Scope

- Performed controlled end-to-end preflight.
- Ran ordered compile and default pytest checks.
- Started Flask locally on configured host/port.
- Verified GET `/health`.
- Verified GET `/`.
- Sent one realistic medical question to POST `/get`.
- Reproduced the failure once directly to identify root cause.
- Stopped the Flask process cleanly.
- Made the smallest local fix for the identified root cause.
- Reran only affected RAG tests, then default pytest.
- Did not exceed two OpenRouter requests.
- Did not run the out-of-source/nonsense POST after quota was consumed.
- Did not retry OpenRouter automatically.

## Preflight Results

- Virtual environment confirmed active: pass.
- `.env` exists: pass, values not printed.
- Medical PDF exists: pass, `data/Medical_book.pdf`.
- OpenRouter model setting is non-empty: pass, value not printed.
- Pinecone key field present: pass, value not printed.
- OpenRouter key field present: pass, value not printed.
- Pinecone index name: `medical-bot`.
- Pinecone index ready: pass.
- Pinecone index dimension: 384.
- Pinecone index metric: cosine.
- Configured namespace present: pass.
- Configured namespace vector count: 5860.

## Smoke Path Results

- Step 1, `python -m compileall` on project source: pass.
- Step 2, default `pytest -q`: pass, 62 passed, 3 skipped, 1 warning, 15 subtests passed.
- Step 3, Flask local start: pass, `http://127.0.0.1:8080`.
- Step 4, GET `/health`: pass, HTTP 200, no secret values.
- Step 5, GET `/`: pass, HTTP 200, HTML loaded.
- Step 6, POST realistic medical question to `/get`: failed with HTTP 503.
- Reproduction, direct `answer_question('What is diabetes mellitus?')`: failed with sanitized `LLMError`.
- Root cause: selected OpenRouter model rejected the RAG prompt because prompt token count was 594 and the model limit was 552.
- Smallest fix made: cap retrieved document text sent into the LLM context to 300 characters per document while preserving retrieval `k=3` and metadata.
- Affected tests after fix: pass.
- Default `pytest -q` after fix: pass, 63 passed, 3 skipped, 1 warning, 15 subtests passed.
- Local context-cap probe after fix: pass, capped length 300 and metadata preserved.
- Step 7, POST out-of-source/nonsense question: not run because the two allowed OpenRouter requests were already consumed.
- Step 8, Flask process stopped cleanly: pass.

## Files Changed In Phase 16

- `src/rag.py`
- `tests/test_rag.py`
- `BUILD_STATE.md`

## Commands Run In Phase 16

- `pwd && rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 180 BUILD_STATE.md`
- `sed -n '1,220p' pytest.ini`
- `git status --short --untracked-files=all`
- `.venv/bin/python - <<'PY' ... confirm virtualenv and .env existence without values ... PY`
- `find data -maxdepth 2 -type f \( -iname '*.pdf' -o -name '.gitkeep' \) -print | sort`
- `.venv/bin/python - <<'PY' ... confirm non-secret config presence ... PY`
- `lsof -nP -iTCP:8080 -sTCP:LISTEN || true`
- `.venv/bin/python - <<'PY' ... Pinecone index and namespace stats check ... PY`
- `.venv/bin/python - <<'PY' ... reproduce namespace stats with object/dict-safe access ... PY`
- `.venv/bin/python -m compileall app.py src tests scripts store_index.py template.py`
- `.venv/bin/pytest -q`
- `.venv/bin/python app.py`
- `curl -sS -o /tmp/medical_chatbot_phase16_health.json -w '%{http_code}\n' http://127.0.0.1:8080/health`
- `curl -sS -o /tmp/medical_chatbot_phase16_home.html -w '%{http_code}\n' http://127.0.0.1:8080/`
- `.venv/bin/python - <<'PY' ... inspect saved /health and / HTML responses ... PY`
- `curl -sS --max-time 120 -X POST -H 'Content-Type: application/json' -d '{"message":"What is diabetes mellitus?"}' -o /tmp/medical_chatbot_phase16_answer_medical.json -w '%{http_code}\n' http://127.0.0.1:8080/get`
- `.venv/bin/python - <<'PY' ... inspect sanitized /get failure response ... PY`
- `.venv/bin/python - <<'PY' ... direct answer_question reproduction ... PY`
- `.venv/bin/python -m py_compile src/rag.py tests/test_rag.py`
- `.venv/bin/pytest -q tests/test_rag.py -k 'get_rag_chain or limit_documents_for_llm or prompt_injection'`
- `.venv/bin/pytest -q`
- `.venv/bin/python -m compileall app.py src tests scripts store_index.py template.py`
- `.venv/bin/python - <<'PY' ... local context-cap probe ... PY`
- `lsof -nP -iTCP:8080 -sTCP:LISTEN || true`
- `.venv/bin/python -m pip check`
- `git diff --stat`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `git diff --check`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' 'ChatOpenAI|OPENAI_API_KEY' app.py src tests scripts store_index.py template.py setup.py README.md .env.example templates static pytest.ini requirements.txt`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `tail -n 150 BUILD_STATE.md`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Dependency environment inspected: pass.
- Dependency changes made: none.
- Preflight virtual environment check: pass.
- Preflight `.env` existence check: pass, values not printed.
- Preflight medical PDF check: pass.
- Preflight Pinecone index contract: pass.
- Preflight namespace vector count: pass, 5860.
- Preflight OpenRouter model non-empty check: pass, value not printed.
- `compileall` before smoke path: pass.
- Default `pytest -q` before smoke path: pass, 62 passed, 3 skipped.
- Flask startup: pass.
- GET `/health`: pass.
- GET `/`: pass.
- POST realistic medical question: blocked by OpenRouter prompt token limit response.
- Failure reproduced once: pass.
- Root cause identified: prompt token count exceeded the selected model's 552-token limit.
- Smallest local fix made: pass.
- Affected tests after fix: pass, 3 passed.
- Default `pytest -q` after fix: pass, 63 passed, 3 skipped.
- `pip check`: pass.
- `ChatOpenAI` / `OPENAI_API_KEY` scoped source scan: pass.
- Secret-shaped value scan outside `.git`, outside `.venv`, outside `.env`, and excluding `BUILD_STATE.md`: pass.
- Source tree bytecode/cache artifacts removed outside `.venv`: pass.
- `git diff --check`: pass.
- Flask process stopped cleanly: pass.

## Unresolved Issues

- Phase 16 end-to-end smoke remains blocked because the two allowed OpenRouter requests were consumed before the final smoke path could be rerun.
- The context-cap fix has unit coverage but has not been verified with another live OpenRouter `/get` request due the explicit quota limit.
- The out-of-source/nonsense POST was not run for the same quota reason.
- Default pytest still emits the existing `langchain-community` deprecation warning from the PDF loader import.

## Next Expected Phase

- Retry Phase 16 final smoke only after explicit user approval for another controlled run with up to two OpenRouter requests.

---

## Phase 16 - Controlled End-to-End Local Smoke Test Retry

Status: PASS
Completion timestamp: 2026-09-07 11:58:52 +06

## Scope

- Treated the pasted Phase 16 prompt as approval to retry the controlled smoke test.
- Re-inspected repository structure, `BUILD_STATE.md`, source files, tests, and configuration files.
- Confirmed preflight requirements without printing secret values.
- Ran the smoke path in the required order.
- Used exactly two OpenRouter-backed POST `/get` requests:
  - one realistic medical question.
  - one out-of-source/nonsense question.
- Did not run automatic retries.
- Did not modify code during this retry.
- Verified the previous context-cap fix against live `/get` behavior.
- Stopped Flask cleanly.

## Preflight Results

- Python version: 3.10.21.
- Virtual environment confirmed active: pass.
- `.env` exists: pass, values not printed.
- Required environment variables present and non-empty: pass.
- `OPENROUTER_MODEL` present and non-empty: pass, value not printed.
- Medical PDF exists in `data/`: pass, `data/Medical_book.pdf`.
- Flask host: `127.0.0.1`.
- Flask port: 8080.
- Required imports available: pass.
- Pinecone index name: `medical-bot`.
- Pinecone index ready: pass.
- Pinecone index dimension: 384.
- Pinecone index metric: cosine.
- Configured namespace present: pass.
- Configured namespace vector count: 5860.
- Configured port was free before Flask startup: pass.

## Token Safety Check

- Retrieved documents before OpenRouter call: 3.
- Limited documents before OpenRouter call: 3.
- Max context characters per document: 300.
- Limited context characters: 903.
- Estimated prompt tokens using `cl100k_base`: 370.
- Estimated prompt tokens below previously observed 552-token limit: pass.
- Retriever `k=3` preserved: pass.
- Metadata limiting behavior preserved by existing tests: pass.

## Smoke Path Results

- Step 1, `python -m compileall` on project source: pass.
- Step 2, default `pytest -q`: pass, 63 passed, 3 skipped, 1 warning, 15 subtests passed.
- Step 3, Flask local start: pass, `http://127.0.0.1:8080`.
- Step 4, GET `/health`: pass, HTTP 200, healthy status, no secret values.
- Step 5, GET `/`: pass, HTTP 200, HTML loaded and header present.
- Step 6, realistic medical POST `/get`: pass, HTTP 200.
- Realistic medical response generated: pass.
- Realistic medical response grounded indicator: answer mentions diabetes and does not dump raw context.
- Step 7, out-of-source/nonsense POST `/get`: pass, HTTP 200.
- Out-of-source fallback response: `I don't know based on the provided medical source.`
- No fabricated nonsense answer: pass.
- Step 8, Flask stopped cleanly: pass.

## Files Changed In Phase 16 Retry

- `BUILD_STATE.md`

## Commands Run In Phase 16 Retry

- `sed -n '1,260p' /Users/macbook/.codex/attachments/db51f7e1-3643-4316-bfcb-8e9d5c38d8c4/pasted-text.txt`
- `pwd && rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 180 BUILD_STATE.md`
- `sed -n '1,260p' app.py`
- `sed -n '1,320p' src/rag.py`
- `sed -n '1,120p' src/prompt.py && sed -n '1,220p' src/config.py`
- `sed -n '1,260p' tests/test_integration.py && sed -n '1,460p' tests/test_rag.py`
- `.venv/bin/python - <<'PY' ... preflight virtualenv/config check without secret values ... PY`
- `find data -maxdepth 2 -type f \( -iname '*.pdf' -o -name '.gitkeep' \) -print | sort`
- `lsof -nP -iTCP:8080 -sTCP:LISTEN || true`
- `.venv/bin/python - <<'PY' ... import availability check ... PY`
- `.venv/bin/python - <<'PY' ... Pinecone index contract and namespace vector count ... PY`
- `.venv/bin/python - <<'PY' ... token safety check before OpenRouter ... PY`
- `.venv/bin/python -m compileall app.py src tests scripts store_index.py template.py`
- `.venv/bin/pytest -q`
- `.venv/bin/python app.py`
- `curl -sS -o /tmp/medical_chatbot_phase16_retry_health.json -w '%{http_code}\n' http://127.0.0.1:8080/health`
- `curl -sS -o /tmp/medical_chatbot_phase16_retry_home.html -w '%{http_code}\n' http://127.0.0.1:8080/`
- `.venv/bin/python - <<'PY' ... inspect /health and / saved responses ... PY`
- `curl -sS --max-time 120 -X POST -H 'Content-Type: application/json' -d '{"message":"What is diabetes mellitus?"}' -o /tmp/medical_chatbot_phase16_retry_medical.json -w '%{http_code}\n' http://127.0.0.1:8080/get`
- `.venv/bin/python - <<'PY' ... inspect realistic medical answer safely ... PY`
- `curl -sS --max-time 120 -X POST -H 'Content-Type: application/json' -d '{"message":"What color is the launch code for the imaginary planet Zorblox?"}' -o /tmp/medical_chatbot_phase16_retry_nonsense.json -w '%{http_code}\n' http://127.0.0.1:8080/get`
- `.venv/bin/python - <<'PY' ... verify grounded fallback response ... PY`
- `lsof -nP -iTCP:8080 -sTCP:LISTEN || true`
- `.venv/bin/python -m pip check`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `git diff --stat`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' \) -delete`
- `git diff --check`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' 'ChatOpenAI|OPENAI_API_KEY' app.py src tests scripts store_index.py template.py setup.py README.md .env.example templates static pytest.ini requirements.txt`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!BUILD_STATE.md' --glob '!requirements.lock.txt' ...`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type f -name '*.pyc' \) -print`
- `tail -n 170 BUILD_STATE.md`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, files, tests, and config inspected first: pass.
- Virtual environment confirmed: pass.
- `.env` exists and was not printed: pass.
- Required env vars present: pass.
- Medical PDF exists: pass.
- Pinecone index `medical-bot` ready, 384d, cosine: pass.
- Namespace contains vectors: pass, 5860.
- OpenRouter model value non-empty: pass.
- Token safety check before OpenRouter: pass.
- `compileall`: pass.
- Default `pytest -q`: pass, 63 passed, 3 skipped.
- Flask startup on configured host/port: pass.
- GET `/health`: pass.
- GET `/`: pass.
- Realistic POST `/get`: pass, HTTP 200, non-empty answer.
- Out-of-source POST `/get`: pass, HTTP 200, grounded fallback returned.
- OpenRouter request count: exactly 2.
- No automatic retries: pass.
- Flask stopped cleanly: pass.
- `pip check`: pass.

## Unresolved Issues

- Default pytest still emits the existing `langchain-community` deprecation warning from the PDF loader import.
- The source tree still contains uncommitted Phase 16 hardening changes from the prior blocked attempt in `src/rag.py` and `tests/test_rag.py`.

## Next Expected Phase

- Phase 17, only when explicitly requested.

---

## Phase 17 - Documentation

Status: PASS
Completion timestamp: 2026-09-07 12:09:41 +06

## Scope

- Re-inspected repository files, `BUILD_STATE.md`, runtime entry points, indexing commands, configuration, helper constants, and test configuration before editing.
- Replaced the placeholder `README.md` with documentation based only on verified project behavior.
- Documented the required architecture path: PDF loader, 500/20 chunking, local `all-MiniLM-L6-v2` embeddings, Pinecone, top-3 retriever, OpenRouter, and Flask UI.
- Documented macOS/zsh environment setup for the detected machine.
- Documented `.env` creation, required environment variables, PDF placement, Pinecone index checks, indexing, Flask startup, offline tests, opt-in integration tests, troubleshooting, security, medical-use disclaimer, cost notes, and why `ChatOpenRouter` is used instead of `ChatOpenAI`.
- Did not change application source code.
- Did not print `.env` values.
- Did not call Pinecone or OpenRouter.

## Verified Facts

- Detected OS: macOS 26.6.2.
- CPU architecture: arm64.
- Shell: zsh.
- Project Python: `.venv/bin/python`, Python 3.10.21.
- Existing `.env`: present, values not printed.
- Existing `BUILD_STATE.md`: present.
- Real PDF in `data/`: `data/Medical_book.pdf`.
- Pinecone index behavior documented from `store_index.py`, `src/indexing.py`, and `src/pinecone_index.py`.
- Chunking constants documented from `src/helper.py`: chunk size 500, overlap 20, expected embedding dimension 384.
- Retriever setting documented from `src/rag.py`: top 3 documents.
- OpenRouter client documented from `src/rag.py`: `ChatOpenRouter`, no `ChatOpenAI`.
- Offline pytest configuration documented from `pytest.ini`: integration marker exists and default tests skip external service calls.

## Files Changed In Phase 17

- `README.md`
- `BUILD_STATE.md`

## Commands Run In Phase 17

- `pwd && rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 220 BUILD_STATE.md`
- `sed -n '1,260p' README.md`
- `sed -n '1,260p' store_index.py`
- `sed -n '1,260p' requirements.txt`
- `sed -n '1,220p' .env.example`
- `sw_vers; uname -m; .venv/bin/python --version`
- `rg -n 'CHUNK_SIZE|CHUNK_OVERLAP|EXPECTED_EMBEDDING_DIMENSION|HUGGINGFACE_EMBEDDING_MODEL|PINECONE_INDEX_DIMENSION|PINECONE_INDEX_METRIC|RETRIEVER_SEARCH_KWARGS|MAX_CONTEXT_CHARS|OPENROUTER|FLASK_HOST|FLASK_PORT' src`
- `sed -n '1,180p' src/helper.py`
- `sed -n '1,220p' src/config.py`
- `sed -n '1,260p' store_index.py`
- `sed -n '1,260p' src/indexing.py`
- `sed -n '1,220p' .gitignore; sed -n '1,120p' pytest.ini`
- `find . -maxdepth 3 -not -path './.git/*' -not -path './.venv/*' -not -path './__pycache__/*' -not -path './.pytest_cache/*' | sort`
- `sed -n '1,260p' app.py`
- `sed -n '1,220p' src/rag.py`
- `tail -n 180 BUILD_STATE.md`
- `git status --short`
- `sed -n '1,160p' src/prompt.py`
- `sed -n '1,280p' README.md`
- `rg -n 'Project Overview|Architecture Diagram|Folder Structure|Prerequisites|Python Environment Setup|Install Commands|Create `.env`|Required Environment Variables|Place The Medical PDF|Check Or Create The Pinecone Index|Run Indexing|Run The Flask App|Local URL|Run Offline Tests|Run Opt-In Integration Tests|Troubleshooting|Security|Medical-Use Disclaimer|Cost Note|Why ChatOpenRouter' README.md`
- `git diff --check`
- `.venv/bin/pytest -q`
- `test -f .env && printf '.env exists\n' || printf '.env missing\n'; test -f BUILD_STATE.md && printf 'BUILD_STATE.md exists\n' || printf 'BUILD_STATE.md missing\n'`
- `rg -n --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!.env' --glob '!requirements.lock.txt' --glob '!BUILD_STATE.md' '(sk-or-v1-[A-Za-z0-9_-]+|sk-[A-Za-z0-9_-]{20,}|[A-Za-z0-9_]{20,}\.[A-Za-z0-9_=-]{20,}\.[A-Za-z0-9_=-]{20,})' .`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `git status --short --untracked-files=all`

## Tests and Acceptance Checks

- Existing repository, `BUILD_STATE.md`, and files inspected first: pass.
- Work limited to Phase 17 documentation: pass.
- README includes all requested sections: pass.
- README documents `ChatOpenRouter` instead of `ChatOpenAI`: pass.
- README does not claim the app is production-ready: pass.
- `.env` exists and values were not printed: pass.
- Secret-shaped value scan outside `.git`, `.venv`, `.env`, `requirements.lock.txt`, and `BUILD_STATE.md`: pass, no matches.
- `git diff --check`: pass.
- Default `pytest -q`: pass, 63 passed, 3 skipped, 1 warning, 15 subtests passed.

## Unresolved Issues

- Default pytest still emits the existing `langchain-community` deprecation warning from the PDF loader import.
- Legal provenance of `data/Medical_book.pdf` remains the user's responsibility.

## Next Expected Phase

- Phase 18, only when explicitly requested.

---

## Phase 18 - Final Audit

Status: PASS
Completion timestamp: 2026-09-07 12:17:14 +06

## Scope

- Performed final repository audit only.
- Did not add new features.
- Did not deploy anything.
- Did not push to GitHub.
- Did not stage or commit files.
- Did not print `.env` values.
- Did not call Pinecone or OpenRouter.

## Audit Results

| Requirement | Result | Evidence |
| --- | --- | --- |
| Git repository exists | PASS | `git rev-parse --is-inside-work-tree` returned true. |
| `git status` checked | PASS | Checked before and during audit. |
| Accidental `.env` tracking | PASS | `.env` is ignored and not tracked. |
| API-key-looking strings in tracked files | PASS | Tracked-file secret-shaped scan found no values. |
| `data/*.pdf` tracking | PASS | `data/Medical_book.pdf` exists but is ignored and not tracked. |
| Pycache and pytest cache cleanup | PASS | Removed `__pycache__`, `*.pyc`, and `.pytest_cache` outside `.venv`. |
| Model cache files in repo | PASS | No model cache directory found outside `.venv`. |
| Large generated artifacts | PASS | Only large repo-tree file found was ignored source data PDF `data/Medical_book.pdf` at 15M. |
| Stale imports | PASS with limitation | `compileall`, import sanity, and tests passed; `ruff` was not installed, so no unused-import linter was run. |
| Unused `ChatOpenAI` source usage | PASS | No `ChatOpenAI` import or instantiation in app source. |
| `OPENAI_API_KEY` source usage | PASS | No runtime use; references are documentation, tests, or audit history only. |
| Obsolete `pinecone-client` dependency | PASS | No `pinecone-client` in requirements, lock file, setup, source, or tests. |
| Chunk size constant | PASS | `CHUNK_SIZE = 500`. |
| Chunk overlap constant | PASS | `CHUNK_OVERLAP = 20`. |
| Embedding model constant | PASS | `sentence-transformers/all-MiniLM-L6-v2`. |
| Embedding/index dimension | PASS | 384. |
| Pinecone index name | PASS | Default `medical-bot`. |
| Pinecone metric | PASS | `cosine`. |
| Retriever top-k | PASS | `RETRIEVER_SEARCH_KWARGS = {"k": 3}`. |
| Flask routes | PASS | `/`, `/get`, and `/health` exist. |
| OpenRouter variables | PASS | `.env.example` and config use `OPENROUTER_API_KEY` and `OPENROUTER_MODEL`. |
| `ChatOpenRouter` usage | PASS | `src/rag.py` imports `ChatOpenRouter` from `langchain_openrouter`. |
| Default `pytest -q` offline | PASS | `pytest -q` passed with integration tests skipped. |
| `requirements.lock.txt` exists | PASS | File exists and is tracked. |
| README commands match code | PASS | README commands match `store_index.py --help`, app entry point, and pytest configuration. |
| `BUILD_STATE.md` has all phases | PASS | Phases 01 through 17 were present before this Phase 18 entry; Phase 18 is now recorded. |

## Architecture Requirement Report

| Architecture Requirement | PASS/FAIL |
| --- | --- |
| PDF input from `data/` only | PASS |
| PDF loader layer present | PASS |
| 500/20 document chunks | PASS |
| Local `all-MiniLM-L6-v2` embeddings | PASS |
| 384-dimensional vectors | PASS |
| Pinecone index `medical-bot` | PASS |
| Pinecone cosine metric | PASS |
| Namespace-separated indexing | PASS |
| Deterministic vector IDs for idempotent ingestion | PASS |
| Top-3 retriever | PASS |
| OpenRouter LLM through `ChatOpenRouter` | PASS |
| No `ChatOpenAI` runtime client | PASS |
| Flask UI and `/get` backend route | PASS |
| Default offline test suite | PASS |
| Secret-safe frontend | PASS |
| Educational medical disclaimer | PASS |

## Remaining Manual Steps

- Keep `.env` local and fill it only with your own Pinecone and OpenRouter keys.
- Keep using only legally obtained PDFs in `data/`.
- Re-index after changing PDFs or after clearing the configured namespace.
- Run integration tests only when you intentionally want to spend external service quota.

## Known Free-Tier Limitations

- OpenRouter free models are rate-limited and availability can change.
- The configured `openrouter/free` model selector may choose a model with small context or parameter limits.
- Pinecone Starter limits can change, including region availability and vector/storage quotas.
- The first local sentence-transformer embedding call can download model files and may be slow.

## Safe To Commit

- No files were staged automatically.
- Safe commit candidates after this audit: `BUILD_STATE.md` only.

## Exact App Start Command

```bash
source .venv/bin/activate
python app.py
```

## Exact PDF Re-Index Command

```bash
source .venv/bin/activate
python store_index.py --ingest
```

## Commands Run In Phase 18

- `pwd; git status --short --untracked-files=all`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `rg -n '^## Phase|^# |Status:|Next Expected Phase|Unresolved Issues' BUILD_STATE.md`
- `test -f BUILD_STATE.md && printf 'BUILD_STATE.md exists\n'; test -f requirements.lock.txt && printf 'requirements.lock.txt exists\n'; test -f .env && printf '.env exists\n'; test -f .env.example && printf '.env.example exists\n'`
- `git rev-parse --is-inside-work-tree; git status --short --untracked-files=all; git ls-files .env .env.example 'data/*.pdf' 'data/*.PDF' requirements.txt requirements.lock.txt`
- `rg -n 'ChatOpenAI|OPENAI_API_KEY|pinecone-client|PINECONE_INDEX_NAME|medical-bot|cosine|CHUNK_SIZE = 500|CHUNK_OVERLAP = 20|all-MiniLM-L6-v2|EXPECTED_EMBEDDING_DIMENSION = 384|RETRIEVER_SEARCH_KWARGS = \{"k": 3\}|@app\.(get|post)\("/(get)?"' app.py src tests requirements.txt requirements.lock.txt README.md .env.example store_index.py setup.py pytest.ini`
- `find . -path './.git' -prune -o -path './.venv' -prune -o \( -type d -name '__pycache__' -o -type d -name '.pytest_cache' -o -type d -name 'models' -o -type d -name '.cache' -o -type f -size +10M \) -print | sort`
- `sed -n '1,260p' README.md; .venv/bin/python store_index.py --help`
- `.venv/bin/python -m compileall app.py src tests scripts store_index.py template.py`
- `.venv/bin/pytest -q`
- `.venv/bin/python - <<'PY' ... import sanity check ... PY`
- `.venv/bin/python -m pip check; .venv/bin/python -m pip freeze | rg -i '^(pinecone|pinecone-client|langchain|flask|python-dotenv|pypdf|sentence-transformers|openrouter)'`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} +`
- `.venv/bin/python - <<'PY' ... tracked secret-shaped scan without values ... PY`
- `printf 'tracked env/pdf files:\n'; git ls-files .env '.env*' 'data/*.pdf' 'data/*.PDF'; printf '\nOpenAI/OpenRouter/Pinecone dependency refs:\n'; rg -n 'ChatOpenAI|OPENAI_API_KEY|pinecone-client|from langchain_openrouter import ChatOpenRouter|OPENROUTER_API_KEY|OPENROUTER_MODEL' $(git ls-files ':!:requirements.lock.txt')`
- `.venv/bin/python - <<'PY' ... constants and routes check ... PY`
- `git ls-files -ci --exclude-standard; git ls-files -oi --exclude-standard | sort | sed -n '1,120p'`
- `git diff -- README.md BUILD_STATE.md | sed -n '1,220p'; git diff --name-only`
- `git log --oneline -5 -- README.md BUILD_STATE.md 2>/dev/null || true`
- `git status --short --untracked-files=all --ignored=matching | sed -n '1,160p'`
- `rg -n '^pinecone-client\b|pinecone-client' requirements.txt requirements.lock.txt setup.py .env.example README.md src tests || true`
- `rg -n 'RUN_INTEGRATION_TESTS|pytestmark|pytest.mark.integration|skip' tests/test_integration.py pytest.ini`
- `git diff --stat; git status --short --untracked-files=all`
- `ls -lh data/*.pdf 2>/dev/null || true; git ls-files 'data/*.pdf' 'data/*.PDF'`
- `date '+%Y-%m-%d %H:%M:%S %Z'; git diff --name-only; git diff --cached --name-only`

## Tests and Acceptance Checks

- `python -m compileall`: pass.
- `pytest -q`: pass, 63 passed, 3 skipped, 1 warning, 15 subtests passed.
- Dependency sanity: pass, `pip check` reported no broken requirements.
- Import sanity: pass for Flask, dotenv, pypdf, sentence-transformers, LangChain packages, OpenRouter, Pinecone, app modules, and required symbols.
- Secret scan: pass, tracked-file scan found no secret-shaped values.
- Cache cleanup: pass, cache files removed outside `.venv`; later import checks recreated no persistent tracked cache files.
- Git staging: pass, no files staged automatically.

## Unresolved Issues

- The default test suite still emits the existing `langchain-community` deprecation warning from the PyPDFLoader import.
- `ruff` is not installed, so unused-import linting was not run.
- Legal provenance of `data/Medical_book.pdf` remains the user's responsibility.

## Next Expected Phase

- No next build phase specified. Await explicit user direction.

---

## Deployment Phase 19 - Vercel Deployment Preparation

Status: PASS
Completion timestamp: 2026-09-07 15:31:52 +06

## Scope

- Prepared the existing Flask medical RAG app for Vercel deployment without changing local `python app.py` behavior.
- Preserved OpenRouter and Pinecone providers.
- Did not run `store_index.py`.
- Did not rebuild embeddings.
- Did not upload or modify the source medical PDF.
- Did not delete or recreate the Pinecone index.
- Did not add `vercel.json` because Vercel's current Flask/Python docs support root `app.py` with a top-level `app`.
- Did not print or expose API keys.
- Did not stage or commit files.

## Verified Vercel Behavior

- Vercel docs checked on 2026-09-07.
- Vercel Flask docs state that Vercel looks for a `Flask` instance named `app` at supported entrypoints.
- Vercel Python runtime docs state supported entrypoint files include root `app.py`, and the top-level name should be `app` for Flask.
- Vercel docs state Flask static assets should use `public/**` instead of relying on Flask's `app.static_folder`.
- Vercel docs state Flask apps deploy as a single Vercel Function with standard bundle size limits.

## Deployment Readiness

- Root `app.py` import: pass, top-level `app` is a Flask instance.
- Local app import did not call Pinecone or OpenRouter: pass.
- Simulated Vercel import with placeholder environment variables: pass.
- Simulated Vercel `/health`: pass, HTTP 200 and secret-safe output.
- Simulated Vercel `/`: pass, HTTP 200.
- Local `/static/style.css`: pass, HTTP 200.
- Vercel public stylesheet mirror: pass, `public/static/style.css` matches `static/style.css`.
- No `vercel.json`: pass, not required by verified Vercel entrypoint rules.
- `.vercelignore`: pass, excludes `.env`, `.env.*`, `.venv/`, caches, tests, research, and `data/*.pdf`.
- `load_settings()` on Vercel: pass, reads platform environment variables and does not create `.env`.

## Files Changed In Deployment Phase 19

- `.vercelignore`
- `public/static/style.css`
- `src/config.py`
- `tests/test_config.py`
- `BUILD_STATE.md`

## Commands Run In Deployment Phase 19

- `pwd; git status --short --untracked-files=all`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 220 BUILD_STATE.md`
- `sed -n '1,220p' app.py; sed -n '1,240p' src/config.py; sed -n '1,220p' requirements.txt`
- Official Vercel docs lookup for Flask/Python runtime behavior.
- `sed -n '1,260p' templates/chat.html; sed -n '1,260p' static/style.css`
- `test -f vercel.json && sed -n '1,200p' vercel.json || printf 'vercel.json missing\n'; test -f .vercelignore && sed -n '1,200p' .vercelignore || printf '.vercelignore missing\n'; test -d public && find public -maxdepth 3 -type f -print | sort || printf 'public missing\n'`
- `.venv/bin/python - <<'PY' ... Flask import and routes check ... PY`
- `rg -n 'store_index|ingest|Pinecone|OpenRouter|OPENROUTER_API_KEY|PINECONE_API_KEY|static/style.css|url_for' app.py templates static README.md .env.example src scripts tests setup.py requirements.txt`
- `wc -l static/style.css; sed -n '1,320p' static/style.css`
- `git ls-files .env 'data/*.pdf' 'data/*.PDF' static/style.css templates/chat.html app.py requirements.txt; git check-ignore .env data/Medical_book.pdf .venv .pytest_cache __pycache__ 2>/dev/null || true`
- `rg -n '^Flask==|^flask$|^sentence-transformers$|^langchain|^pinecone|^python-dotenv$|^pypdf$|^pytest$|^langchain-openrouter$|^langchain-pinecone$' requirements.txt requirements.lock.txt`
- `mkdir -p public/static && cp static/style.css public/static/style.css && cmp -s static/style.css public/static/style.css && printf 'public static CSS mirror matches\n'`
- `.venv/bin/pytest -q tests/test_config.py tests/test_app.py tests/test_check_env_script.py`
- `.venv/bin/python - <<'PY' ... verify Vercel settings do not create .env ... PY`
- `VERCEL=1 PINECONE_API_KEY=placeholder-pinecone OPENROUTER_API_KEY=placeholder-openrouter .venv/bin/python - <<'PY' ... Vercel import, /health, /, and /static/style.css check ... PY`
- `cmp -s static/style.css public/static/style.css && printf 'public static CSS mirror matches\n'; test ! -f vercel.json && printf 'vercel.json not needed\n'`
- `.venv/bin/python -m compileall app.py src tests scripts store_index.py template.py`
- `.venv/bin/pytest -q`
- `.venv/bin/python - <<'PY' ... dependency/import sanity check ... PY`
- `.venv/bin/python -m pip check`
- `lsof -nP -iTCP:8080 -sTCP:LISTEN || true`
- `.venv/bin/python app.py`
- `curl -sS -o /tmp/medical_chatbot_vercel_prep_health.json -w '%{http_code}\n' http://127.0.0.1:8080/health`
- `curl -sS -o /tmp/medical_chatbot_vercel_prep_home.html -w '%{http_code}\n' http://127.0.0.1:8080/`
- `curl -sS -o /tmp/medical_chatbot_vercel_prep_style.css -w '%{http_code}\n' http://127.0.0.1:8080/static/style.css`
- `.venv/bin/python - <<'PY' ... inspect saved route responses for secret-safe expected markers ... PY`
- `du -sh .venv/lib/python3.10/site-packages/torch .venv/lib/python3.10/site-packages/transformers .venv/lib/python3.10/site-packages/sentence_transformers 2>/dev/null || true; find .venv/lib/python3.10/site-packages -maxdepth 1 -name 'nvidia*' -exec du -sh {} + 2>/dev/null || true`
- `sed -n '1,220p' .vercelignore; test ! -f vercel.json && printf 'vercel.json absent\n'; cmp -s static/style.css public/static/style.css && printf 'public static CSS mirror matches\n'`
- `git ls-files .env '.env*' 'data/*.pdf' 'data/*.PDF' public/static/style.css .vercelignore; git check-ignore .env data/Medical_book.pdf .venv .pytest_cache __pycache__ 2>/dev/null || true`
- `.venv/bin/python - <<'PY' ... secret-shaped scan for tracked and untracked non-ignored files ... PY`
- `date '+%Y-%m-%d %H:%M:%S %Z'; git status --short --untracked-files=all; git diff --cached --name-only; lsof -nP -iTCP:8080 -sTCP:LISTEN || true`

## Tests and Acceptance Checks

- Repository, `BUILD_STATE.md`, `app.py`, requirements, entrypoint, and environment handling inspected first: pass.
- Flask import by Vercel-compatible entrypoint: pass.
- Required dependencies exist in `requirements.txt`: pass.
- No `vercel.json` added: pass, verified not needed for root `app.py`.
- Vercel static asset mirror added: pass.
- `.vercelignore` protects `.env` and `data/*.pdf`: pass.
- Vercel runtime env loading does not create `.env`: pass.
- `python -m compileall`: pass.
- `pytest -q`: pass, 68 passed, 3 skipped, 1 warning, 16 subtests passed.
- Dependency/import sanity: pass.
- `pip check`: pass.
- Local Flask startup: pass.
- GET `/health`: pass, HTTP 200.
- GET `/`: pass, HTTP 200.
- GET `/static/style.css`: pass, HTTP 200.
- OpenRouter calls: none in deployment-prep tests.
- Pinecone calls: none in deployment-prep tests.
- Git staging: pass, no files staged.

## Deployment URLs

- None. No deployment was performed in this phase.

## Blockers and Risks

- Manual Vercel environment variable configuration is required before deployment can run.
- Vercel standard Flask function bundle limit is documented as 500MB. Local installed package footprint measured about 544M for `torch`, 56M for `transformers`, and 4.8M for `sentence_transformers`, before any Hugging Face model cache. The actual Vercel build may require Large Functions/Fluid compute capacity, a dependency strategy change, or a later architecture change if the build exceeds platform limits.
- Source medical PDFs should stay out of Vercel. The deployed app is expected to query the already-indexed Pinecone namespace.
- OpenRouter free models remain rate-limited and availability can change.

## Vercel Action Required

- In the Vercel project dashboard, set these server-side Environment Variables for the target deployment environments without exposing them to browser JavaScript:
  - `PINECONE_API_KEY`
  - `PINECONE_INDEX_NAME=medical-bot`
  - `PINECONE_CLOUD=aws`
  - `PINECONE_REGION=us-east-1`
  - `PINECONE_NAMESPACE=medical-chatbot-v1`
  - `OPENROUTER_API_KEY`
  - `OPENROUTER_MODEL=openrouter/free` or another valid OpenRouter model ID
  - `FLASK_HOST=127.0.0.1`
  - `FLASK_PORT=8080`
  - `FLASK_DEBUG=false`
  - `DATA_DIR=data`
- Verify the Vercel build output for Python function bundle size. If it exceeds the standard limit, enable the appropriate Vercel capacity option or request a later deployment phase to move query embeddings away from local PyTorch.

## Next Expected Phase

- Vercel deployment attempt, only when explicitly requested.

---

## Post-Phase Fix - OpenRouter Model Configuration Retry

Status: PASS
Completion timestamp: 2026-09-07 14:54:50 +06

## Issue

- User still saw the browser message: `The language model is temporarily unavailable because of rate limits or quota.`
- Sanitized environment inspection showed `OPENROUTER_MODEL` was set to placeholder text: `some-available-openrouter-model`.
- That placeholder is not a usable OpenRouter model ID.

## Fix

- Updated only the non-secret `.env` model setting back to the project default: `OPENROUTER_MODEL=openrouter/free`.
- Did not change API keys.
- Did not print API keys.
- Did not change source code in this retry.

## Verification

- Fresh Flask `test_client` POST `/get` with `What is diabetes mellitus?`: pass, HTTP 200 with a non-empty answer.
- Verified active settings without printing secrets:
  - `OPENROUTER_API_KEY`: present.
  - `PINECONE_API_KEY`: present.
  - `OPENROUTER_MODEL`: `openrouter/free`.
  - `LLM_MAX_TOKENS`: 48.
- Port 8080 check after verification: no Flask process was listening.
- `git diff --check`: pass.

## Files Changed

- `.env` was updated locally and remains ignored by Git.
- `BUILD_STATE.md`

## Commands Run

- `pwd; git status --short --untracked-files=all`
- `rg -n 'LLM_MAX_TOKENS|OPENROUTER_MODEL|DEFAULT_OPENROUTER_MODEL|_classify_llm_error|more credits|fewer max_tokens|can only afford' src tests .env.example`
- `tail -n 120 BUILD_STATE.md`
- `.venv/bin/python - <<'PY' ... sanitized OpenRouter/Pinecone key presence and model check ... PY`
- `.venv/bin/python - <<'PY' ... update OPENROUTER_MODEL in .env without printing secrets ... PY`
- `.venv/bin/python - <<'PY' ... fresh Flask test_client POST /get verification ... PY`
- `lsof -nP -iTCP:8080 -sTCP:LISTEN || true`
- `git diff --check`
- `git status --short --untracked-files=all`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests and Acceptance Checks

- Repository, `BUILD_STATE.md`, and files inspected first: pass.
- `.env` key values were not printed: pass.
- OpenRouter model corrected from placeholder to project default: pass.
- Fresh `/get` backend path: pass, HTTP 200 with non-empty answer.
- Port 8080 free after check: pass.
- Git staging: pass, no files staged.

## Unresolved Issues

- OpenRouter free models remain rate-limited and availability can change.
- If browser testing still shows an old response, start Flask again after this `.env` correction.

## Next Expected Phase

- No next build phase specified. Await explicit user direction.

---

## Post-Phase Fix - OpenRouter Token Cap

Status: PASS
Completion timestamp: 2026-09-07 13:27:11 +06

## Issue

- Browser requests to `/get` returned: `The language model request failed.`
- A sanitized backend smoke check showed OpenRouter rejected the request because `max_tokens=64` was higher than the available allowance for the configured account/model.
- The backend had not classified OpenRouter's `requires more credits, or fewer max_tokens` wording as a quota/rate-limit condition, so the browser received the generic LLM failure message.

## Fix

- Lowered `LLM_MAX_TOKENS` in `src/rag.py` from 64 to 48.
- Updated OpenRouter error classification to treat `more credits`, `fewer max_tokens`, and `can only afford` as quota/rate-limit failures.
- Added a unit test covering the observed OpenRouter error wording.
- Did not change retrieval, embeddings, Pinecone, PDF loading, indexing, or UI architecture.
- Did not print API keys.

## Files Changed

- `src/rag.py`
- `tests/test_rag.py`
- `BUILD_STATE.md`

## Commands Run

- `pwd; git status --short --untracked-files=all`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 220 BUILD_STATE.md`
- `sed -n '1,380p' src/rag.py; sed -n '1,150p' src/prompt.py; sed -n '1,180p' app.py`
- `.venv/bin/python scripts/check_env.py`
- `.venv/bin/python - <<'PY' ... sanitized settings status without secret values ... PY`
- `lsof -nP -iTCP:8080 -sTCP:LISTEN || true`
- `.venv/bin/python - <<'PY' ... sanitized OpenRouter smoke_test_llm diagnostic ... PY`
- `rg -n 'LLM_MAX_TOKENS|rate limit|quota|_classify_llm_error|_llm_error_message|get_llm|smoke_test_llm' tests src app.py`
- `sed -n '150,260p' tests/test_rag.py; sed -n '70,120p' tests/test_app.py`
- `sed -n '1,260p' tests/test_integration.py`
- `git diff -- src/rag.py tests/test_rag.py app.py | sed -n '1,240p'`
- `.venv/bin/pytest -q tests/test_rag.py tests/test_app.py`
- `.venv/bin/python -m compileall src/rag.py tests/test_rag.py app.py`
- `.venv/bin/python - <<'PY' ... smoke_test_llm with LLM_MAX_TOKENS check ... PY`
- `.venv/bin/python - <<'PY' ... Flask test_client POST /get live verification ... PY`
- `.venv/bin/pytest -q`
- `.venv/bin/python -m compileall app.py src tests scripts store_index.py template.py`
- `.venv/bin/python -m pip check`
- `git diff -- src/rag.py tests/test_rag.py | sed -n '1,220p'`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `lsof -nP -iTCP:8080 -sTCP:LISTEN || true`
- `git status --short --untracked-files=all`
- `find . -path './.venv' -prune -o -path './.git' -prune -o \( -type d -name '__pycache__' -o -type d -name '.pytest_cache' -o -type f -name '*.pyc' \) -print | sort`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} +`

## Tests and Acceptance Checks

- Environment checker: pass.
- Sanitized settings check: pass, required keys present without printing values.
- OpenRouter smoke after fix: pass, non-empty response.
- Fresh Flask `test_client` POST `/get` after fix: pass, HTTP 200 with non-empty answer.
- Targeted tests: pass, 35 passed, 1 skipped, 1 warning, 4 subtests passed.
- Full offline `pytest -q`: pass, 67 passed, 3 skipped, 1 warning, 16 subtests passed.
- `compileall`: pass.
- `pip check`: pass.
- Cache cleanup outside `.venv`: pass.

## Unresolved Issues

- The existing Flask process on port 8080 was still running with old code during the fix. Restart Flask before testing in the browser.
- Default pytest still emits the existing `langchain-community` deprecation warning from the PyPDFLoader import.
- If the OpenRouter account/model allowance drops below 48 output tokens, requests may still fail with a quota/rate-limit message. In that case, add credits, choose a model with available free quota, or lower the cap again.

## Next Expected Phase

- No next build phase specified. Await explicit user direction.

---

## Optional Phase 19 - Local Convenience Commands

Status: PASS
Completion timestamp: 2026-09-07 12:31:59 +06

## Scope

- Added a cross-platform Python environment checker at `scripts/check_env.py`.
- Kept core architecture unchanged.
- Did not add desktop installers, Docker, cloud deployment, background services, or new app features.
- Did not change dependencies.
- Did not call OpenRouter.
- Did not call Pinecone by default; Pinecone validation is available only with explicit `--check-pinecone`.
- Did not print `.env` secret values.
- Staged nothing.

## Convenience Commands

- Environment verification: `python scripts/check_env.py`
- Optional Pinecone verification: `python scripts/check_env.py --check-pinecone`
- Index check: `python store_index.py --check-index`
- Safe indexing: `python store_index.py --ingest`
- Flask startup: `python app.py`
- Offline tests: `pytest -q`

## Files Changed In Optional Phase 19

- `scripts/check_env.py`
- `tests/test_check_env_script.py`
- `README.md`
- `BUILD_STATE.md`

## Commands Run In Optional Phase 19

- `pwd; git status --short --untracked-files=all`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `tail -n 180 BUILD_STATE.md`
- `sed -n '1,280p' README.md; sed -n '1,220p' store_index.py; sed -n '1,260p' app.py`
- `sed -n '1,260p' tests/test_config.py; sed -n '1,220p' tests/test_app.py`
- `sed -n '1,220p' setup.py; sed -n '1,180p' .env.example; sed -n '1,140p' .gitignore`
- `sed -n '1,260p' scripts/smoke_test.py`
- `git status --short --untracked-files=all; git diff --name-only`
- `.venv/bin/python scripts/check_env.py`
- `.venv/bin/pytest -q tests/test_check_env_script.py`
- `.venv/bin/python -m compileall scripts/check_env.py tests/test_check_env_script.py`
- `rg -n 'Convenience Commands|scripts/check_env.py|--check-pinecone|store_index.py --ingest|pytest -q' README.md scripts/check_env.py tests/test_check_env_script.py`
- `.venv/bin/pytest -q tests/test_check_env_script.py`
- `.venv/bin/python -m compileall app.py src tests scripts store_index.py template.py`
- `.venv/bin/python scripts/check_env.py`
- `.venv/bin/python - <<'PY' ... phase 19 import sanity check ... PY`
- `.venv/bin/pytest -q`
- `git diff --check`
- `.venv/bin/python - <<'PY' ... secret-shaped scan for tracked and untracked non-ignored files ... PY`
- `git status --short --untracked-files=all; git diff --name-only; git diff --cached --name-only`
- `.venv/bin/python -m pip check`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} + && find . -path './.git' -prune -o -path './.venv' -prune -o \( -type d -name '__pycache__' -o -type d -name '.pytest_cache' -o -type f -name '*.pyc' \) -print | sort`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `git status --short --untracked-files=all`

## Tests and Acceptance Checks

- Repository, `BUILD_STATE.md`, and existing files inspected first: pass.
- Work limited to Optional Phase 19 convenience commands: pass.
- `scripts/check_env.py` verifies required files and environment variable names: pass.
- `scripts/check_env.py` does not print secret values: pass.
- `scripts/check_env.py` does not call OpenRouter: pass.
- `scripts/check_env.py` does not call Pinecone unless `--check-pinecone` is passed: pass.
- README updated with convenience commands: pass.
- Targeted checker tests: pass, 4 passed.
- `python -m compileall`: pass.
- Default `pytest -q`: pass, 67 passed, 3 skipped, 1 warning, 15 subtests passed.
- Dependency sanity: pass, `pip check` reported no broken requirements.
- Import sanity: pass.
- Secret-shaped scan for tracked and untracked non-ignored files: pass.
- `git diff --check`: pass.
- Cache cleanup outside `.venv`: pass.
- Git staging: pass, no files staged.

## Unresolved Issues

- Default pytest still emits the existing `langchain-community` deprecation warning from the PyPDFLoader import.
- Legal provenance of `data/Medical_book.pdf` remains the user's responsibility.

## Next Expected Phase

- No next build phase specified. Await explicit user direction.

---

## Deployment Phase 20 - Vercel Compatibility Audit

Status: BLOCKED for standard Vercel deployment; audit completed.
Completion timestamp: 2026-09-07 16:38:59 +06

## Scope

- Audited Vercel compatibility for the existing Flask medical RAG app.
- Did not deploy.
- Did not run `store_index.py`.
- Did not rebuild embeddings.
- Did not upload or inspect full PDF content.
- Did not call OpenRouter.
- Did not call Pinecone.
- Did not change application architecture.
- Did not add `vercel.json`.
- Did not add `api/index.py`.
- Did not print API key values.

## Repository And Entrypoint Findings

- `app.py` defines a top-level Flask object: `app = Flask(__name__)`.
- Flask routes remain `/`, `/get`, `/health`, and `/static/<path:filename>`.
- Heavy runtime components are initialized lazily enough that importing `app.py` does not call OpenRouter or Pinecone.
- `store_index.py` is a manual CLI entrypoint only and is not imported by `app.py`.
- `.env` is ignored and `.vercelignore` exists.
- `public/static/style.css` exists and matches `static/style.css`, which aligns with Vercel static asset guidance while keeping local Flask behavior.
- `vercel.json` is currently absent. No audit-only evidence requires adding it yet.

## Verified Vercel Assumptions

- Vercel's Python runtime supports WSGI/ASGI applications and detects Flask from supported dependencies and entrypoints.
- Vercel supports top-level `app` in root `app.py`; this repository already matches that pattern.
- `api/index.py` can expose a top-level `app` for file-based Python functions, but Vercel's framework preset takes precedence for detected Flask projects, so adding `api/index.py` is not required for this repository at this phase.
- Current Vercel Python versions are 3.12 by default, with 3.13 and 3.14 also available.
- A Python 3.12 Linux dry-run dependency resolution succeeded from `requirements.txt`.
- The repository's `setup.py` declares `python_requires=">=3.10,<3.13"`, so Python 3.12 is compatible but Python 3.13/3.14 should not be selected without a later compatibility pass.
- Vercel's standard Python function bundle size limit is 500 MB uncompressed. Large Functions can support larger Python bundles only when enabled and eligible.

## Evidence

- Local Flask import sanity:
  - app type: Flask.
  - routes: `/`, `/get`, `/health`, `/static/<path:filename>`.
  - local defaults: host `127.0.0.1`, port `8080`, debug `False`.
- Runtime constants:
  - embedding model: `sentence-transformers/all-MiniLM-L6-v2`.
  - embedding dimension: `384`.
  - retriever k: `3`.
  - LLM max tokens: `48`.
  - per-document context cap: `300` characters.
- Installed package footprint:
  - local `torch`: 544 MB.
  - local `transformers`: 56 MB.
  - local `sentence_transformers`: 4.8 MB.
- Lockfile contains `sentence-transformers==6.0.1`, `torch==2.14.0`, `pinecone==7.3.0`, and `langchain-openrouter==0.2.8`.
- Lockfile does not contain obsolete `pinecone-client`.

## Compatibility Table

| Component | Current behavior | Vercel risk | Required change | Can remain unchanged |
| --- | --- | --- | --- | --- |
| Flask entrypoint | Root `app.py` exports `app` | Low | None for framework-preset deployment | Yes |
| `api/index.py` | Not present | Low | Not required unless a later phase chooses file-based routing | Yes |
| `vercel.json` | Not present | Medium if function config/exclusions become necessary | Add later only if configuring function exclusions, duration, memory, or routing | Yes for audit |
| Python version | Local venv is Python 3.10; `setup.py` allows `<3.13` | Medium | Use Vercel Python 3.12, not 3.13/3.14 without retesting | Local remains unchanged |
| Runtime dependencies | `requirements.txt` includes Flask, LangChain, Pinecone, OpenRouter, sentence-transformers | High because embedding dependencies are large | Strategy B should remove local embedding stack from Vercel runtime or isolate it outside request runtime | Core local requirements remain unchanged until deployment adaptation |
| sentence-transformers / torch | Query embeddings run locally on CPU | High; `torch` alone measured 544 MB locally, above standard 500 MB Python function limit | Move query embeddings out of Vercel runtime for standard deployment, or explicitly opt into Large Functions with known cold-start risk | Local behavior remains unchanged |
| Model download | First query can trigger local Hugging Face model download/cache | High; cold start and non-persistent cache risk | Do not rely on model download at serverless request time | Local behavior remains unchanged |
| Hugging Face cache | Local disk cache expected | High; serverless filesystem/cache persistence is not guaranteed as an app contract | Use external embedding path for deployed query embeddings | Local cache remains unchanged |
| Cold start latency | Imports include LangChain and local embedding libraries | Medium to high | Keep deployment runtime lighter in Strategy B | Local imports remain unchanged |
| Request duration | Retrieval, local embedding, Pinecone, OpenRouter all in one request | Medium | Remove local embedding compute from Vercel request path or configure function limits if intentionally using Strategy A | Flask route contract remains unchanged |
| Memory usage | Local embedding stack loads model/runtime in process | High on Hobby 2 GB if multiple cold starts/concurrency occur | Strategy B preferred | Local behavior remains unchanged |
| OpenRouter | Called only from `/get` through `ChatOpenRouter` | Medium due free route quota/model availability | Configure Vercel env vars; keep one LLM request per user request | Provider remains OpenRouter |
| Pinecone | Queried at runtime, indexing is manual | Medium due network latency/errors | Configure Vercel env vars; keep index pre-built | Pinecone remains vector store |
| `store_index.py` | Manual CLI only | Low | Do not run during Vercel build/import/startup/request | Yes |
| Local PDF/filesystem | PDF is used for indexing, not runtime RAG after Pinecone indexing | Low if not uploaded | Do not upload `data/*.pdf`; rely on existing Pinecone namespace | Yes |
| `.env` vs Vercel env vars | Local uses `.env`; Vercel should use project env vars | Medium | Set Vercel env vars manually; keep `.env` ignored | Local `.env` remains unchanged |
| Hard-coded localhost | Default config uses `127.0.0.1`; browser fetch uses relative `/get` | Low | No change for deployed request flow | Yes |
| Flask debug | Default `False` | Low | Ensure Vercel `FLASK_DEBUG=false` or unset | Yes |
| Long-lived process assumptions | Lazy globals may persist but are not required for correctness | Medium | Avoid relying on persistent model cache or process memory in Strategy B | Local behavior remains unchanged |

## Selected Deployment Strategy

- Selected Strategy B: Flask UI/RAG orchestration on Vercel, but query embeddings moved out of the Vercel runtime.
- Strategy A, full Flask RAG on Vercel with local query embeddings, is impractical for standard Vercel because the measured local `torch` package alone exceeds the 500 MB standard Python function limit before the rest of the app or model cache is counted.
- Strategy A might be explored only with explicit Large Functions configuration and acceptance of cold-start/model-cache risk, but it is not the safest default deployment path.
- Strategy B is not implemented in this phase.

## External Sources Checked

- Vercel Python Runtime: https://vercel.com/docs/functions/runtimes/python
- Vercel Python `/api` directory behavior: https://vercel.com/docs/functions/runtimes/python/api-directory
- Vercel Flask guide: https://vercel.com/docs/frameworks/backend/flask
- Vercel Functions limits: https://vercel.com/docs/functions/limitations

## Files Changed In Phase 20

- `BUILD_STATE.md`

## Commands Run In Phase 20

- `git status --short --untracked-files=all`
- `tail -n 220 BUILD_STATE.md`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `sed -n '1,260p' app.py`
- `sed -n '1,320p' src/config.py`
- `sed -n '1,360p' src/rag.py`
- `sed -n '1,280p' src/helper.py`
- `sed -n '1,360p' store_index.py`
- `sed -n '1,280p' src/pinecone_index.py`
- `sed -n '1,180p' requirements.txt && sed -n '1,260p' setup.py && test -f vercel.json && sed -n '1,160p' vercel.json || true`
- `du -sh .venv/lib/python3.10/site-packages/torch .venv/lib/python3.10/site-packages/transformers .venv/lib/python3.10/site-packages/sentence_transformers .venv/lib/python3.10/site-packages/langchain* 2>/dev/null || true`
- `.venv/bin/python -m compileall app.py src tests scripts store_index.py template.py`
- `.venv/bin/pytest -q`
- `.venv/bin/python - <<'PY' ... Flask/import/runtime constant sanity check ... PY`
- `.venv/bin/python - <<'PY' ... lockfile package check ... PY`
- `.venv/bin/python -m pip install --dry-run --only-binary=:all: --platform manylinux2014_x86_64 --python-version 3.12 --implementation cp --abi cp312 --target /tmp/medical_chatbot_py312_resolve_phase20 -r requirements.txt --report /tmp/medical_chatbot_py312_phase20_report.json`
- `.venv/bin/python - <<'PY' ... broad secret scan, produced false positives for variable names and dummy fixtures ... PY`
- `git diff --check`
- `git check-ignore .env data/Medical_book.pdf .venv .pytest_cache __pycache__ .vercelignore || true`
- `nl -ba tests/test_rag.py | sed -n '188,198p'`
- `.venv/bin/python - <<'PY' ... refined secret-shaped scan excluding .env, PDFs, and explicit dummy fixture tokens ... PY`
- `rg -n 'ChatOpenAI|OPENAI_API_KEY|pinecone-client|localhost|127\\.0\\.0\\.1|store_index' app.py src tests requirements.txt requirements.lock.txt README.md templates static public .gitignore .vercelignore || true`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} + && find . -path './.git' -prune -o -path './.venv' -prune -o \( -type d -name '__pycache__' -o -type d -name '.pytest_cache' -o -type f -name '*.pyc' \) -print | sort`
- `.venv/bin/python -m pip check`
- `test -f vercel.json && echo 'vercel_json: present' || echo 'vercel_json: absent'; test -f .vercelignore && echo 'vercelignore: present' || echo 'vercelignore: absent'; test -f public/static/style.css && echo 'public_static_css: present' || echo 'public_static_css: absent'; cmp -s static/style.css public/static/style.css && echo 'static_copy_matches: yes' || echo 'static_copy_matches: no'`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `git diff --name-only && git diff --cached --name-only`
- `tail -n 40 BUILD_STATE.md`

## Tests And Audit Results

- `python -m compileall`: pass.
- Default offline `pytest -q`: pass, 68 passed, 3 skipped, 1 warning, 16 subtests passed.
- Flask import/startup suitability check: pass, top-level Flask app imports without external service calls.
- Python 3.12 Linux dependency dry-run: pass, dependency resolution succeeds.
- Dependency sanity: pass, `pip check` reported no broken requirements.
- `git diff --check`: pass.
- Refined secret-shaped scan: pass.
- `.env`, `data/Medical_book.pdf`, `.venv`, `.pytest_cache`, and `__pycache__` are ignored: pass.
- Static copy for Vercel public serving: pass.
- `vercel.json` necessity: not required in this phase.

## Blockers

- Standard Vercel deployment of Strategy A is blocked by package size and serverless model-cache/cold-start risk from local query embeddings.
- Strategy B requires a later phase to move query embeddings out of the Vercel runtime while preserving local behavior.
- Vercel project environment variables must be configured manually before any real deployment can answer questions.

## Next Expected Phase

- Deployment phase to implement Strategy B or an explicitly approved Large Functions Strategy A experiment.

---

## Deployment Phase 21 - Strategy B Implementation

Status: PASS
Completion timestamp: 2026-09-07 17:03:57 +06

## Scope

- Implemented Strategy B for Vercel compatibility.
- Preserved local `python app.py` behavior by keeping local embeddings as the default provider.
- Added hosted Hugging Face feature-extraction query embeddings for deployment only when `EMBEDDINGS_PROVIDER=huggingface_api`.
- Kept Pinecone as the vector store and OpenRouter as the generation provider.
- Did not run `store_index.py`.
- Did not upload or inspect PDF content.
- Did not recreate, delete, or mutate the Pinecone index.
- Did not call OpenRouter.
- Did not call Pinecone.
- Did not call Hugging Face hosted inference.
- Did not print API key values.
- Did not stage or commit files.

## Implementation

- Added `src/remote_embeddings.py` with a LangChain-compatible `HuggingFaceAPIEmbeddings` adapter using `huggingface_hub.InferenceClient.feature_extraction`.
- Added `src/helper_constants.py` so the remote adapter can share the 384-dimensional embedding contract without importing local-only embedding code.
- Updated `src/helper.py` so `PyPDFLoader`, `RecursiveCharacterTextSplitter`, and `HuggingFaceEmbeddings` are imported lazily.
- Updated `src/helper.py` so `get_embeddings()` defaults to local embeddings, while `get_embeddings(settings=...)` can select hosted Hugging Face embeddings.
- Updated `src/rag.py` so runtime vector-store creation passes settings into `get_embeddings()`.
- Updated `app.py` so `/health` reports missing `HF_TOKEN` only when remote embeddings are selected, and `/get` maps hosted embedding failures to a 503 response.
- Added `requirements-vercel.txt` without `torch`, `sentence-transformers`, `transformers`, or `langchain-huggingface`.
- Added `vercel.json` so Vercel installs `requirements-vercel.txt`.
- Updated `.env.example` with deployment embedding variable names only.
- Updated README deployment notes for Strategy B.
- Updated `scripts/check_env.py` to verify Strategy B deployment files and `.env.example` deployment variable names.

## Deployment Environment Contract

- Local default: `EMBEDDINGS_PROVIDER=local`.
- Vercel deployment: set `EMBEDDINGS_PROVIDER=huggingface_api`.
- Vercel deployment requires `HF_TOKEN` as a server-side environment variable.
- `HUGGINGFACE_EMBEDDING_MODEL` remains `sentence-transformers/all-MiniLM-L6-v2` to match the already-indexed 384-dimensional Pinecone vectors.
- `HUGGINGFACE_INFERENCE_PROVIDER` defaults to `hf-inference`.
- `HUGGINGFACE_TIMEOUT_SECONDS` defaults to `15`.

## Files Changed In Deployment Phase 21

- `.env.example`
- `README.md`
- `app.py`
- `requirements.txt`
- `requirements-vercel.txt`
- `scripts/check_env.py`
- `src/config.py`
- `src/helper.py`
- `src/helper_constants.py`
- `src/rag.py`
- `src/remote_embeddings.py`
- `tests/test_app.py`
- `tests/test_check_env_script.py`
- `tests/test_config.py`
- `tests/test_deployment_config.py`
- `tests/test_helper.py`
- `tests/test_rag.py`
- `tests/test_remote_embeddings.py`
- `vercel.json`

## Commands Run In Deployment Phase 21

- `git status --short --untracked-files=all`
- `tail -n 220 BUILD_STATE.md`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `sed -n '1,260p' requirements.txt && printf '\n--- lock key deps ---\n' && rg -n '^(sentence-transformers|torch|transformers|huggingface-hub|requests|httpx|flask|langchain|langchain-core|langchain-openrouter|langchain-pinecone|pinecone)==' requirements.lock.txt`
- `.venv/bin/python - <<'PY' ... inspect `huggingface_hub.InferenceClient` signatures ... PY`
- `sed -n '1,460p' tests/test_helper.py`
- `sed -n '1,460p' tests/test_rag.py`
- `sed -n '1,260p' tests/test_config.py && sed -n '1,240p' tests/test_app.py`
- `sed -n '1,320p' tests/test_check_env_script.py && sed -n '1,320p' scripts/check_env.py`
- `sed -n '1,380p' src/indexing.py`
- `sed -n '1,180p' .env.example`
- `sed -n '1,220p' .gitignore && sed -n '1,160p' .vercelignore`
- `.venv/bin/pytest -q tests/test_config.py tests/test_helper.py tests/test_remote_embeddings.py tests/test_rag.py tests/test_app.py tests/test_check_env_script.py tests/test_deployment_config.py`
- `.venv/bin/python -m compileall app.py src tests scripts store_index.py template.py`
- `.venv/bin/python - <<'PY' ... local and remote embedding import sanity check ... PY`
- `VERCEL=1 EMBEDDINGS_PROVIDER=huggingface_api PINECONE_API_KEY=placeholder-pinecone OPENROUTER_API_KEY=placeholder-openrouter HF_TOKEN=placeholder-hf .venv/bin/python - <<'PY' ... blocked-heavy-import Vercel import check ... PY`
- `.venv/bin/python -m pip install --dry-run --only-binary=:all: --platform manylinux2014_x86_64 --python-version 3.12 --implementation cp --abi cp312 --target /tmp/medical_chatbot_vercel_strategy_b -r requirements-vercel.txt --report /tmp/medical_chatbot_vercel_strategy_b_report.json`
- `.venv/bin/pytest -q tests/test_deployment_config.py tests/test_remote_embeddings.py tests/test_helper.py tests/test_rag.py tests/test_app.py`
- `.venv/bin/pytest -q tests/test_app.py tests/test_rag.py tests/test_helper.py tests/test_remote_embeddings.py tests/test_config.py tests/test_deployment_config.py`
- `.venv/bin/python scripts/check_env.py`
- `.venv/bin/pytest -q`
- `.venv/bin/python -m pip check`
- `.venv/bin/python - <<'PY' ... direct dependency/import sanity check ... PY`
- `.venv/bin/python - <<'PY' ... secret-shaped scan excluding .env and PDFs ... PY`
- `git diff --check`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} + && find . -path './.git' -prune -o -path './.venv' -prune -o \( -type d -name '__pycache__' -o -type d -name '.pytest_cache' -o -type f -name '*.pyc' \) -print | sort`
- `git status --short --untracked-files=all`
- `git diff --name-only && git diff --cached --name-only`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests And Verification

- Targeted Strategy B tests: pass, 64 passed, 1 skipped, 16 subtests passed.
- Full default offline `pytest -q`: pass, 83 passed, 3 skipped, 16 subtests passed.
- `python -m compileall`: pass.
- `scripts/check_env.py`: pass.
- Dependency sanity: pass, `pip check` reported no broken requirements.
- Import sanity: pass.
- Vercel-style app import with heavy local embedding/PDF packages blocked: pass.
- Vercel Python 3.12 slim dependency dry-run: pass.
- Vercel slim dependency dry-run confirmed no `torch`, `sentence-transformers`, `transformers`, or `langchain-huggingface`.
- Refined secret-shaped scan: pass.
- `git diff --check`: pass.
- Cache cleanup outside `.venv`: pass.

## Deployment Readiness

- Strategy B code-level implementation is ready for Vercel configuration.
- No deployment was performed.
- No live hosted embedding smoke test was run because it would require a real `HF_TOKEN` and an external request.

## Vercel Action Required

- Add server-side Vercel environment variables:
  - `PINECONE_API_KEY`
  - `PINECONE_INDEX_NAME=medical-bot`
  - `PINECONE_NAMESPACE=medical-chatbot-v1`
  - `OPENROUTER_API_KEY`
  - `OPENROUTER_MODEL=openrouter/free`
  - `EMBEDDINGS_PROVIDER=huggingface_api`
  - `HF_TOKEN`
  - `HUGGINGFACE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2`
  - `HUGGINGFACE_INFERENCE_PROVIDER=hf-inference`
  - `HUGGINGFACE_TIMEOUT_SECONDS=15`
- Do not upload `data/*.pdf` to Vercel.
- Do not run `store_index.py` during Vercel build or startup.

## Unresolved Issues

- A real Vercel deployment and one live hosted embedding query have not been run in this phase.
- Hugging Face hosted inference can be rate-limited or unavailable depending on account/provider status.
- OpenRouter free model availability and quota remain external limitations.

## Next Expected Phase

- Vercel environment configuration and a controlled deployment smoke test with at most one hosted embedding call and one OpenRouter call.

---

## Deployment Phase 21 - Vercel Flask Entry Point

Status: PASS
Completion timestamp: 2026-09-07 17:22:58 +06

## Scope

- Added the smallest `api/index.py` entrypoint requested for Vercel.
- Preserved local `python app.py` behavior.
- Imported the existing Flask `app` instead of duplicating routes or RAG logic.
- Kept one authoritative route set in root `app.py`.
- Did not run `store_index.py`.
- Did not rebuild embeddings.
- Did not upload or inspect PDF content.
- Did not recreate, delete, or mutate the Pinecone index.
- Did not call OpenRouter.
- Did not call Pinecone.
- Did not call Hugging Face hosted inference.
- Did not print API key values.
- Did not stage or commit files.

## Implementation

- Created `api/__init__.py`.
- Created `api/index.py`.
- `api/index.py` inserts the project root into `sys.path` when needed, then imports `app` from root `app.py`.
- `api/index.py` exposes top-level `app` through `__all__ = ["app"]`.
- Added `tests/test_vercel_entrypoint.py`.
- Updated `scripts/check_env.py` so `api/__init__.py` and `api/index.py` are expected project files.
- Did not add another `vercel.json`; the existing Strategy B `vercel.json` remains for the slim Vercel install command.

## Verified Vercel Entry Point Behavior

- `from api.index import app` succeeds.
- Imported object is the same Flask instance as `app.app`.
- `GET /` returns 200 through `api.index.app.test_client()`.
- `GET /health` returns 200 through `api.index.app.test_client()` and does not expose secret values.
- `POST /get` returns 200 JSON through `api.index.app.test_client()` when RAG is mocked.
- Importing `api.index` does not call `Flask.run`.
- Importing `api.index` does not import `store_index.py`.
- Vercel-style import with local heavy embedding/PDF packages blocked succeeds for `/` and `/health`.

## Vercel Sources Checked

- Vercel Python `/api` directory docs: https://vercel.com/docs/functions/runtimes/python/api-directory
- Vercel Python runtime docs: https://vercel.com/docs/functions/runtimes/python

## Files Changed In Deployment Phase 21 Entry Point

- `api/__init__.py`
- `api/index.py`
- `scripts/check_env.py`
- `tests/test_vercel_entrypoint.py`
- `BUILD_STATE.md`

## Commands Run In Deployment Phase 21 Entry Point

- `git status --short --untracked-files=all`
- `tail -n 180 BUILD_STATE.md`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `sed -n '1,260p' app.py && sed -n '1,220p' vercel.json 2>/dev/null || true`
- Official Vercel docs lookup for Python `/api` entrypoint behavior.
- `.venv/bin/pytest -q tests/test_vercel_entrypoint.py tests/test_app.py tests/test_check_env_script.py`
- `.venv/bin/python - <<'PY' ... direct `from api.index import app` route check ... PY`
- `VERCEL=1 EMBEDDINGS_PROVIDER=huggingface_api PINECONE_API_KEY=placeholder-pinecone OPENROUTER_API_KEY=placeholder-openrouter HF_TOKEN=placeholder-hf .venv/bin/python - <<'PY' ... blocked-heavy-import `api.index` check ... PY`
- `.venv/bin/pytest -q`
- `.venv/bin/python -m compileall app.py api src tests scripts store_index.py template.py`
- `.venv/bin/python scripts/check_env.py`
- `.venv/bin/python -m pip check`
- `.venv/bin/pytest -q tests/test_vercel_entrypoint.py`
- `.venv/bin/python - <<'PY' ... final `api.index` import, route, health, and `store_index` import check ... PY`
- `.venv/bin/python - <<'PY' ... secret-shaped scan excluding .env and PDFs ... PY`
- `git diff --check`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} + && find . -path './.git' -prune -o -path './.venv' -prune -o \( -type d -name '__pycache__' -o -type d -name '.pytest_cache' -o -type f -name '*.pyc' \) -print | sort`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests And Verification

- New Vercel entrypoint tests: pass, 4 passed.
- Targeted Flask/checker tests with entrypoint tests: pass, 22 passed.
- Full default offline `pytest -q`: pass, 87 passed, 3 skipped, 16 subtests passed.
- `python -m compileall`: pass.
- `scripts/check_env.py`: pass.
- Dependency sanity: pass, `pip check` reported no broken requirements.
- Final `api.index` import check: pass.
- Final Vercel-style import with local heavy packages blocked: pass.
- Refined secret-shaped scan: pass.
- `git diff --check`: pass.
- Cache cleanup outside `.venv`: pass.

## Deployment Readiness

- Code-level Vercel Flask entrypoint is ready.
- No deployment was performed.
- Runtime answering on Vercel still requires Vercel environment variables from the Strategy B phase.

## Vercel Action Required

- Configure the required server-side Vercel environment variables before deployment.
- Keep `EMBEDDINGS_PROVIDER=huggingface_api` on Vercel.
- Keep `HF_TOKEN` server-side only.
- Do not upload `data/*.pdf` to Vercel.
- Do not run `store_index.py` during Vercel build, import, startup, or request handling.

## Unresolved Issues

- No live Vercel deployment smoke test was run.
- No live hosted embedding query was run.
- OpenRouter and Hugging Face hosted inference remain external quota/rate-limit dependencies.

## Next Expected Phase

- Vercel environment configuration and controlled deployment smoke test.

---

## Deployment Phase 22 - Vercel Runtime Dependency And Embedding Audit

Status: BLOCKED FOR STRATEGY A
Completion timestamp: 2026-09-07 17:40:42 +06

## Scope

- Audited runtime dependency separation and Strategy A viability.
- Did not deploy.
- Did not modify application architecture.
- Did not run `store_index.py`.
- Did not rebuild embeddings.
- Did not upload or inspect PDF content.
- Did not call OpenRouter.
- Did not call Pinecone.
- Did not call Hugging Face hosted inference.
- Did not print API key values.
- Did not stage or commit files.

## Dependency Separation

Runtime dependencies needed by the deployed Flask request path:

- `flask`
- `python-dotenv`
- `langchain-core`
- `langchain-classic`
- `langchain-text-splitters`
- `langchain-pinecone`
- `langchain-openrouter`
- `pinecone`
- Strategy A only: `langchain-huggingface`, `sentence-transformers`, and transitive `torch`/`transformers`
- Strategy B only: `huggingface-hub`

Indexing/development-only dependencies:

- `pypdf`
- `langchain-community`
- `langchain-huggingface` when used for local indexing/development
- `sentence-transformers` when used for local indexing/development
- `pytest`
- notebook/research dependencies if added later

Deployment request path assessment:

- `pypdf`: not required by `/`, `/health`, `/get`, or `api/index.py`.
- Jupyter: not present in current dependency manifests and not required at runtime.
- `pytest`: not required at runtime.
- `store_index.py` and indexing utilities: not required at runtime and must not run during Vercel build/import/startup/request handling.
- Query embedding is required at runtime and must use the same embedding space as the existing Pinecone index: `sentence-transformers/all-MiniLM-L6-v2`, dimension `384`.

## Strategy A Attempt

Strategy A tested: local Hugging Face query embeddings on Vercel, with no PDF loading, no indexing, lazy model initialization, and warm-instance reuse where possible.

Minimal Strategy A runtime requirement set tested in `/tmp/medical_chatbot_strategy_a_requirements.txt`:

- `flask`
- `python-dotenv`
- `langchain-core`
- `langchain-classic`
- `langchain-text-splitters`
- `langchain-pinecone`
- `langchain-openrouter`
- `pinecone`
- `langchain-huggingface`
- `sentence-transformers`

Python 3.12/Linux dependency resolution for this minimal Strategy A set succeeded, but the package payload is too large for standard Vercel.

Measured package/build-size evidence:

- Python 3.12/Linux minimal Strategy A wheel download count: 97 files.
- Minimal Strategy A wheel directory size: 848 MB compressed wheel files.
- `torch-2.6.0-cp312-cp312-manylinux1_x86_64.whl`: 731 MB on disk here; pip reported 766.6 MB during download.
- `transformers-5.16.1`: 12 MB wheel.
- `scipy-1.16.3`: 34 MB wheel.
- `numpy-2.2.6`: 16 MB wheel.
- Current local Python 3.10 installed footprint also shows the problem: `torch` alone is 526 MB, plus `transformers` 52 MB and `sentence_transformers` 2.9 MB.

Verified Vercel limitation:

- Current Vercel Python runtime docs state standard Python bundle size is 500 MB uncompressed.
- Current Vercel function limits docs state Python function size is 500 MB uncompressed, with Large Functions up to 5 GB only in beta/Fluid Compute.
- The compressed Strategy A wheel payload already exceeds 500 MB before installation expansion, bytecode, app code, or model cache.

Model download/cache behavior:

- With an empty Hugging Face cache and offline mode enabled, `get_embeddings(provider="local")` failed with an `OSError` containing offline/cache wording.
- This confirms the local embedding path requires a cached model or internet/model download behavior when cache is absent.
- That download/cache behavior is not acceptable as a standard Vercel request-time assumption.

## Decision

- Strategy A is not viable for standard Vercel.
- No Strategy A runtime dependency file was created.
- No lazy local embedding initialization test was added because Strategy A is blocked by measured package size before runtime behavior can be accepted.
- Existing Strategy B files from the previous deployment phase remain the recommended path.
- Do not silently replace the embedding model. The existing Pinecone vectors require the same `sentence-transformers/all-MiniLM-L6-v2` 384-dimensional embedding space.

## Python Compatibility

- Current Vercel Python docs list 3.12 as the default runtime, with 3.13 and 3.14 also available.
- Minimal Strategy A dependencies resolve for Python 3.12/Linux, but size blocks standard deployment.
- The repository's `setup.py` remains `python_requires=">=3.10,<3.13"`, so Python 3.12 is still the compatible Vercel target.

## Sources Checked

- Vercel Python Runtime: https://vercel.com/docs/functions/runtimes/python
- Vercel Function Limits: https://vercel.com/docs/functions/limitations

## Files Changed In Deployment Phase 22

- `BUILD_STATE.md`

## Commands Run In Deployment Phase 22

- `git status --short --untracked-files=all`
- `tail -n 220 BUILD_STATE.md`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `sed -n '1,260p' requirements.txt && printf '\n--- requirements-vercel ---\n' && sed -n '1,220p' requirements-vercel.txt && printf '\n--- lock selected ---\n' && rg -n '^(Flask|flask|python-dotenv|pypdf|pytest|jupyter|sentence-transformers|torch|transformers|huggingface-hub|langchain|langchain-core|langchain-classic|langchain-community|langchain-text-splitters|langchain-huggingface|langchain-pinecone|langchain-openrouter|pinecone)==' requirements.lock.txt`
- Official Vercel docs lookup for Python runtime, Python versions, bundle size, memory, and duration limits.
- `sed -n '1,260p' src/helper.py && sed -n '1,320p' src/rag.py && sed -n '1,260p' src/remote_embeddings.py`
- `printf '%s\n' ... > /tmp/medical_chatbot_strategy_a_requirements.txt`
- `printf '%s\n' ... > /tmp/medical_chatbot_strategy_b_requirements.txt`
- `du -sh .venv/lib/python3.10/site-packages/torch .venv/lib/python3.10/site-packages/transformers .venv/lib/python3.10/site-packages/sentence_transformers .venv/lib/python3.10/site-packages/langchain_huggingface 2>/dev/null || true`
- `rg -n 'pypdf|PyPDFLoader|Jupyter|pytest|store_index|load_pdf_documents|split_documents|get_embeddings|HuggingFaceEmbeddings|sentence-transformers|torch|transformers|langchain_community|langchain_huggingface' app.py api src scripts tests requirements.txt requirements-vercel.txt vercel.json README.md`
- `mkdir -p /tmp/medical_chatbot_strategy_a_wheels_1704 && .venv/bin/python -m pip download --only-binary=:all: --platform manylinux2014_x86_64 --python-version 3.12 --implementation cp --abi cp312 --dest /tmp/medical_chatbot_strategy_a_wheels_1704 -r /tmp/medical_chatbot_strategy_a_requirements.txt`
- `du -sh /tmp/medical_chatbot_strategy_a_wheels_1704 && du -sh /tmp/medical_chatbot_strategy_a_wheels_1704/torch-*.whl /tmp/medical_chatbot_strategy_a_wheels_1704/transformers-*.whl /tmp/medical_chatbot_strategy_a_wheels_1704/sentence_transformers-*.whl /tmp/medical_chatbot_strategy_a_wheels_1704/scipy-*.whl /tmp/medical_chatbot_strategy_a_wheels_1704/numpy-*.whl 2>/dev/null || true && find /tmp/medical_chatbot_strategy_a_wheels_1704 -type f | wc -l`
- `mkdir -p /tmp/medical_chatbot_empty_hf_cache_1704 /tmp/medical_chatbot_empty_st_cache_1704 && HF_HOME=/tmp/medical_chatbot_empty_hf_cache_1704 SENTENCE_TRANSFORMERS_HOME=/tmp/medical_chatbot_empty_st_cache_1704 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 .venv/bin/python - <<'PY' ... local embedding empty-cache check ... PY`
- `.venv/bin/python -m pip install --dry-run --only-binary=:all: --platform manylinux2014_x86_64 --python-version 3.12 --implementation cp --abi cp312 --target /tmp/medical_chatbot_strategy_a_dryrun -r /tmp/medical_chatbot_strategy_a_requirements.txt --report /tmp/medical_chatbot_strategy_a_report.json`
- `.venv/bin/pytest -q`
- `.venv/bin/python -m compileall app.py api src tests scripts store_index.py template.py`
- `.venv/bin/python -m pip check`
- `VERCEL=1 EMBEDDINGS_PROVIDER=huggingface_api PINECONE_API_KEY=placeholder-pinecone OPENROUTER_API_KEY=placeholder-openrouter HF_TOKEN=placeholder-hf .venv/bin/python - <<'PY' ... api.index import check ... PY`
- `git diff --check`
- `.venv/bin/python - <<'PY' ... secret-shaped scan excluding .env and PDFs ... PY`
- `.venv/bin/python - <<'PY' ... cleanup temporary audit artifacts ... PY`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests And Verification

- Full default offline `pytest -q`: pass, 87 passed, 3 skipped, 16 subtests passed.
- `python -m compileall`: pass.
- Dependency sanity: pass, `pip check` reported no broken requirements.
- `api.index` import check: pass.
- `git diff --check`: pass.
- Refined secret-shaped scan: pass.
- Temporary wheel/cache audit artifacts cleaned from `/tmp`.

## Blockers

- Strategy A is blocked for standard Vercel because the minimal local-embedding runtime exceeds Vercel's 500 MB Python function size limit before installation expansion and model cache.
- Local query embeddings would also require a pre-existing model cache or request-time model download when cache is absent.

## Next Expected Phase

- Proceed to Optional Prompt 28 only after explicit user approval, or continue with a controlled Strategy B Vercel deployment smoke test if the user chooses that path.

---

## Deployment Phase 23 - Controlled Strategy B Vercel Deployment Smoke Test

Status: BLOCKED
Completion timestamp: 2026-09-07 17:55:41 +06

## Scope

- Began controlled Strategy B Vercel deployment smoke-test preflight after user approval.
- Did not deploy because the repository is not linked to a Vercel project.
- Did not run `store_index.py`.
- Did not rebuild embeddings.
- Did not upload or inspect PDF content.
- Did not recreate, delete, or mutate the Pinecone index.
- Did not call OpenRouter.
- Did not call Pinecone.
- Did not call Hugging Face hosted inference.
- Did not print API key values.
- Did not stage or commit files.

## Preflight Findings

- Vercel CLI is installed at `/opt/homebrew/bin/vercel`.
- Vercel CLI version is `58.0.0`.
- Vercel CLI authentication works for the current user.
- `.vercel/project.json` is absent, so this local repository is not linked to a Vercel project.
- `vercel env ls` cannot run until the codebase is linked.
- `.env`, `data/Medical_book.pdf`, `.venv`, `.pytest_cache`, and `__pycache__` remain ignored.

## Deployment Smoke Test Status

- Deployment was not attempted.
- No deployment URL was created.
- No hosted embedding request was made.
- No OpenRouter request was made.
- No Pinecone request was made.

## Files Changed In Deployment Phase 23

- `BUILD_STATE.md`

## Commands Run In Deployment Phase 23

- `git status --short --untracked-files=all`
- `tail -n 180 BUILD_STATE.md`
- `rg --files --hidden -g '!.git/**' -g '!.venv/**' | sort`
- `sed -n '1,220p' vercel.json && sed -n '1,160p' requirements-vercel.txt && sed -n '1,120p' api/index.py`
- `command -v vercel || true`
- `vercel --version 2>/dev/null || true`
- `test -d .vercel && find .vercel -maxdepth 2 -type f -print | sort || true`
- `git check-ignore .env data/Medical_book.pdf .vercel .venv .pytest_cache __pycache__ 2>/dev/null || true`
- `vercel whoami`
- `vercel env ls 2>&1 | sed -E 's/(token=|Bearer )[A-Za-z0-9._~+\/-]+/\1[redacted]/g'`
- `.venv/bin/python -m compileall app.py api src tests scripts store_index.py template.py`
- `.venv/bin/pytest -q`
- `VERCEL=1 EMBEDDINGS_PROVIDER=huggingface_api PINECONE_API_KEY=placeholder-pinecone OPENROUTER_API_KEY=placeholder-openrouter HF_TOKEN=placeholder-hf .venv/bin/python - <<'PY' ... api.index import and route check ... PY`
- `date '+%Y-%m-%d %H:%M:%S %Z'`
- `.venv/bin/python - <<'PY' ... secret-shaped scan excluding .env and PDFs ... PY`
- `git diff --check`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} + && find . -path './.git' -prune -o -path './.venv' -prune -o \( -type d -name '__pycache__' -o -type d -name '.pytest_cache' -o -type f -name '*.pyc' \) -print | sort`
- `git status --short --untracked-files=all`

## Tests And Verification

- `python -m compileall`: pass.
- Full default offline `pytest -q`: pass, 87 passed, 3 skipped, 16 subtests passed.
- Vercel-style `api.index` import and route check: pass, `/` and `/health` returned 200 with placeholder secrets not exposed.
- Refined secret-shaped scan: pass.
- `git diff --check`: pass.
- Cache cleanup outside `.venv`: pass.

## Blockers

- The local repository is not linked to a Vercel project. Vercel CLI returned: codebase is not linked; pass a project name or run `vercel link`.
- Vercel environment variables cannot be listed or verified until the project is linked.
- Controlled deployment smoke test cannot continue safely until project linking is completed.

## Vercel Action Required

- Link this folder to the intended Vercel project by running one of these commands locally:
  - Interactive: `vercel link`
  - Non-interactive if you know the IDs: `vercel link --yes --team <team-id> --project <project-id>`
- After linking, configure the required server-side environment variables in Vercel before deployment:
  - `PINECONE_API_KEY`
  - `PINECONE_INDEX_NAME=medical-bot`
  - `PINECONE_NAMESPACE=medical-chatbot-v1`
  - `OPENROUTER_API_KEY`
  - `OPENROUTER_MODEL=openrouter/free`
  - `EMBEDDINGS_PROVIDER=huggingface_api`
  - `HF_TOKEN`
  - `HUGGINGFACE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2`
  - `HUGGINGFACE_INFERENCE_PROVIDER=hf-inference`
  - `HUGGINGFACE_TIMEOUT_SECONDS=15`

## Next Expected Phase

- Resume the controlled Strategy B Vercel deployment smoke test after the repository is linked to the intended Vercel project and server-side Vercel environment variables are configured.

---

## Deployment Phase 23 Retry - Controlled Strategy B Vercel Deployment Smoke Test

Status: BLOCKED
Completion timestamp: 2026-09-07 18:11:57 +06

## Scope

- Retried the controlled Strategy B smoke test after the user reported the repository was already deployed on Vercel.
- Did not run `store_index.py`.
- Did not rebuild embeddings.
- Did not upload or inspect PDF content.
- Did not recreate, delete, or mutate the Pinecone index.
- Did not call OpenRouter.
- Did not call Pinecone.
- Did not call Hugging Face hosted inference.
- Did not print API key values.
- Did not stage or commit files.

## Deployment Found

- Vercel CLI authentication works.
- Project discovered by name: `medical-chatbot`.
- Production alias: `https://medical-chatbot-nine-topaz.vercel.app`
- Direct deployment URL: `https://medical-chatbot-1nv7zdhpk.vercel.app`
- Deployment status: Ready.
- Vercel build output reports Python function size: 50.45 MB.
- Local `.vercel/project.json` is still absent, so this folder is not linked locally even though the Vercel project exists remotely.

## Vercel Smoke Checks

- `GET /health`: HTTP 200, valid JSON, status `ok`, no secret-looking values exposed.
- `GET /`: HTTP 200, chat title and disclaimer present, no secret-looking values exposed.
- `GET /static/style.css`: HTTP 200.
- Deployed `/get` was intentionally not called because production is missing the Strategy B remote embedding environment variables, so the request path would not be configured correctly and could waste quota or return a predictable runtime failure.

## Vercel Environment Audit

Configured in Vercel production:

- `PINECONE_API_KEY`
- `PINECONE_INDEX_NAME`
- `PINECONE_CLOUD`
- `PINECONE_REGION`
- `PINECONE_NAMESPACE`
- `OPENROUTER_API_KEY`
- `OPENROUTER_MODEL`
- `FLASK_HOST`
- `FLASK_PORT`
- `FLASK_DEBUG`
- `DATA_DIR`

Missing for Strategy B on Vercel:

- `EMBEDDINGS_PROVIDER=huggingface_api`
- `HF_TOKEN`
- `HUGGINGFACE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2`
- `HUGGINGFACE_INFERENCE_PROVIDER=hf-inference`
- `HUGGINGFACE_TIMEOUT_SECONDS=15`

## Files Changed In Deployment Phase 23 Retry

- `BUILD_STATE.md`

## Commands Run In Deployment Phase 23 Retry

- `git status --short --untracked-files=all`
- `tail -n 180 BUILD_STATE.md`
- `find . -maxdepth 3 -type f | sort | sed 's#^./##' | head -n 240`
- `vercel env ls production --project medical-chatbot --no-color`
- `vercel inspect medical-chatbot-nine-topaz.vercel.app --no-color`
- `test -f .vercel/project.json && sed -n '1,120p' .vercel/project.json || true`
- `curl -sS -D /tmp/medical_chatbot_vercel_health_headers.txt -o /tmp/medical_chatbot_vercel_health.json https://medical-chatbot-nine-topaz.vercel.app/health`
- `curl -sS -D /tmp/medical_chatbot_vercel_home_headers.txt -o /tmp/medical_chatbot_vercel_home.html https://medical-chatbot-nine-topaz.vercel.app/`
- `curl -sS -D /tmp/medical_chatbot_vercel_static_headers.txt -o /tmp/medical_chatbot_vercel_style.css https://medical-chatbot-nine-topaz.vercel.app/static/style.css`
- `.venv/bin/python -m compileall app.py api src tests scripts store_index.py template.py`
- `.venv/bin/pytest -q`
- `.venv/bin/python -m pip check`
- `VERCEL=1 EMBEDDINGS_PROVIDER=huggingface_api PINECONE_API_KEY=placeholder-pinecone OPENROUTER_API_KEY=placeholder-openrouter HF_TOKEN=placeholder-hf .venv/bin/python - <<'PY' ... api.index import and route check ... PY`
- `git diff --check`
- `.venv/bin/python - <<'PY' ... secret-shaped scan excluding .env and PDFs ... PY`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} +`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests And Verification

- `python -m compileall`: pass.
- Full default offline `pytest -q`: pass, 87 passed, 3 skipped, 16 subtests passed.
- `pip check`: pass, no broken requirements.
- Vercel-style `api.index` import and route check: pass, `/` and `/health` returned 200 with placeholder values not exposed.
- `git diff --check`: pass.
- Refined secret-shaped scan: pass.
- Cache cleanup outside `.venv`: pass.

## Blockers

- Vercel production is missing the Strategy B remote embedding variables. The deployed app is using the slim Vercel bundle, so the chat request path must use Hugging Face hosted embeddings instead of local `sentence-transformers`.
- `HF_TOKEN` is required for hosted Hugging Face embedding calls and cannot be created safely by code.
- After adding Vercel environment variables, a new production redeploy is required for the deployment to pick them up.

## Vercel Action Required

- In Vercel project `medical-chatbot`, add these production environment variables:
  - `EMBEDDINGS_PROVIDER=huggingface_api`
  - `HF_TOKEN=<your Hugging Face token>`
  - `HUGGINGFACE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2`
  - `HUGGINGFACE_INFERENCE_PROVIDER=hf-inference`
  - `HUGGINGFACE_TIMEOUT_SECONDS=15`
- Redeploy the production deployment after adding those variables.

## Next Expected Phase

- Resume the controlled Strategy B deployed `/get` smoke test after Vercel production has the Strategy B embedding variables and the app has been redeployed.

---

## Deployment Phase 23 Retry 2 - Strategy B Hosted Embedding Smoke Test

Status: BLOCKED
Completion timestamp: 2026-09-07 18:27:11 +06

## Scope

- Resumed after the user reported Vercel environment setup was done.
- Verified the deployed production alias again.
- Made exactly one deployed `/get` request.
- Did not run `store_index.py`.
- Did not rebuild embeddings.
- Did not upload or inspect PDF content.
- Did not recreate, delete, or mutate the Pinecone index.
- Did not make repeated OpenRouter requests.
- Did not print API key values.
- Did not stage or commit files.

## Deployment Findings

- Production alias: `https://medical-chatbot-nine-topaz.vercel.app`
- Direct deployment URL after redeploy: `https://medical-chatbot-a6x9v8aln.vercel.app`
- Deployment status: Ready.
- Vercel build output reports Python function size: 50.45 MB.
- Strategy B environment variable names are now present in Vercel production for:
  - `EMBEDDINGS_PROVIDER`
  - `HF_TOKEN`
  - `HUGGINGFACE_EMBEDDING_MODEL`
  - `HUGGINGFACE_TIMEOUT_SECONDS`
- `HUGGINGFACE_INFERENCE_PROVIDER` was not listed, so the app default of `hf-inference` is used unless it is later configured explicitly.

## Deployed Smoke Result

- `GET /health`: HTTP 200, valid JSON, no secret-looking values exposed.
- `POST /get`: HTTP 503, sanitized JSON error: `The query embedding service is unavailable.`
- Vercel logs showed Hugging Face requests ending with `GET https://huggingface.co/api/models/hf-inference` and HTTP 404.
- Evidence indicates the hosted embedding path is receiving `hf-inference` as a model ID, or the Hugging Face client is not being initialized with the model strongly enough for the deployed runtime.

## Local Fix Implemented

- Updated the hosted Hugging Face embedding adapter to pass `model=` at `InferenceClient` construction time and use the official `token=` argument.
- Kept the per-call model argument so current `huggingface_hub` behavior remains explicit.
- Added runtime validation so `HUGGINGFACE_EMBEDDING_MODEL=hf-inference` is rejected with a clear configuration error. The correct model value is `sentence-transformers/all-MiniLM-L6-v2`; `hf-inference` belongs in `HUGGINGFACE_INFERENCE_PROVIDER`.
- Updated `/health` to run non-network runtime validation and report invalid configuration without exposing secret values.

## Files Changed In Deployment Phase 23 Retry 2

- `BUILD_STATE.md`
- `app.py`
- `src/config.py`
- `src/remote_embeddings.py`
- `tests/test_app.py`
- `tests/test_config.py`
- `tests/test_remote_embeddings.py`

## Commands Run In Deployment Phase 23 Retry 2

- `git status --short --untracked-files=all`
- `tail -n 220 BUILD_STATE.md`
- `find . -maxdepth 3 -type f | sort | sed 's#^./##' | head -n 240`
- `vercel env ls production --project medical-chatbot --no-color`
- `vercel inspect medical-chatbot-nine-topaz.vercel.app --no-color`
- `curl -sS -D /tmp/medical_chatbot_vercel_get_headers.txt -o /tmp/medical_chatbot_vercel_get.json -X POST https://medical-chatbot-nine-topaz.vercel.app/get -H 'Content-Type: application/json' --data '{"message":"What are common symptoms of dengue?"}'`
- `curl -sS -D /tmp/medical_chatbot_vercel_health2_headers.txt -o /tmp/medical_chatbot_vercel_health2.json https://medical-chatbot-nine-topaz.vercel.app/health`
- `.venv/bin/python - <<'PY' ... sanitized deployed response inspection ... PY`
- `sed -n '1,260p' app.py && sed -n '1,360p' src/rag.py && sed -n '1,260p' src/remote_embeddings.py`
- `vercel logs medical-chatbot-nine-topaz.vercel.app --since 10m --no-color`
- `.venv/bin/python - <<'PY' ... huggingface_hub version and InferenceClient signature inspection ... PY`
- `.venv/bin/python - <<'PY' ... InferenceClient source inspection ... PY`
- `sed -n '1,260p' tests/test_remote_embeddings.py && sed -n '1,260p' tests/test_deployment_config.py && sed -n '1,220p' .env.example`
- `sed -n '1,260p' src/config.py && sed -n '1,180p' src/helper.py`
- `sed -n '1,260p' tests/test_config.py && sed -n '1,220p' tests/test_app.py`
- `rg -n "health|runtime_configuration|validate_for_runtime|HUGGINGFACE_EMBEDDING_MODEL|missing_runtime" tests src app.py`
- `.venv/bin/pytest -q tests/test_remote_embeddings.py tests/test_config.py tests/test_app.py`
- `.venv/bin/python -m compileall app.py api src tests scripts store_index.py template.py`
- `.venv/bin/pytest -q`
- `.venv/bin/python -m pip check`
- `VERCEL=1 EMBEDDINGS_PROVIDER=huggingface_api PINECONE_API_KEY=placeholder-pinecone OPENROUTER_API_KEY=placeholder-openrouter HF_TOKEN=placeholder-hf .venv/bin/python - <<'PY' ... api.index import and route check ... PY`
- `git diff --check`
- `.venv/bin/python - <<'PY' ... secret-shaped scan excluding .env and PDFs ... PY`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} +`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests And Verification

- Focused tests: pass, 30 passed, 12 subtests passed.
- `python -m compileall`: pass.
- Full default offline `pytest -q`: pass, 89 passed, 3 skipped, 16 subtests passed.
- `pip check`: pass, no broken requirements.
- Vercel-style `api.index` import and route check: pass, `/` and `/health` returned 200 with placeholder values not exposed.
- `git diff --check`: pass.
- Refined secret-shaped scan: pass.
- Cache cleanup outside `.venv`: pass.

## Blockers

- The deployed production app still returns HTTP 503 from `/get` until this local code fix is redeployed.
- Vercel encrypted environment values cannot be read safely. The log strongly suggests `HUGGINGFACE_EMBEDDING_MODEL` may be set to `hf-inference`; if so, it must be changed to `sentence-transformers/all-MiniLM-L6-v2`.

## Vercel Action Required

- Redeploy the project so Vercel runs the updated `src/remote_embeddings.py`, `src/config.py`, and `app.py`.
- In Vercel project `medical-chatbot`, verify without exposing values:
  - `EMBEDDINGS_PROVIDER` is `huggingface_api`
  - `HUGGINGFACE_EMBEDDING_MODEL` is `sentence-transformers/all-MiniLM-L6-v2`
  - `HUGGINGFACE_INFERENCE_PROVIDER` is either unset or `hf-inference`
  - `HF_TOKEN` is a valid Hugging Face token

## Next Expected Phase

- After redeploying this local fix and correcting any model/provider value mixup, resume with one deployed `/health` check and at most one deployed `/get` request.

---

## Deployment Phase 23 Retry 3 - Post-Redeploy Strategy B Health Check

Status: BLOCKED
Completion timestamp: 2026-09-07 18:32:50 +06

## Scope

- Resumed after the user reported the latest Vercel redeploy was done.
- Verified the production alias points to a newer Ready deployment.
- Checked Vercel production environment variable names without printing values.
- Ran `/health` only.
- Did not run deployed `/get` because `/health` reported invalid runtime configuration.
- Did not run `store_index.py`.
- Did not rebuild embeddings.
- Did not upload or inspect PDF content.
- Did not recreate, delete, or mutate the Pinecone index.
- Did not call OpenRouter.
- Did not call Pinecone.
- Did not call Hugging Face hosted inference.
- Did not stage or commit files.

## Deployment Findings

- Production alias: `https://medical-chatbot-nine-topaz.vercel.app`
- Direct deployment URL after latest redeploy: `https://medical-chatbot-nr6qhci4x.vercel.app`
- Deployment status: Ready.
- Vercel build output reports Python function size: 50.45 MB.
- Vercel production contains the Strategy B variable names:
  - `EMBEDDINGS_PROVIDER`
  - `HF_TOKEN`
  - `HUGGINGFACE_EMBEDDING_MODEL`
  - `HUGGINGFACE_TIMEOUT_SECONDS`

## Deployed Smoke Result

- `GET /health`: HTTP 200, valid JSON, no secret-looking values exposed.
- `/health` reported `runtime_configuration_present=false`.
- `/health` reported configuration error: `Invalid HUGGINGFACE_EMBEDDING_MODEL value. Set HUGGINGFACE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2 and HUGGINGFACE_INFERENCE_PROVIDER=hf-inference.`
- Deployed `/get` was intentionally not called because runtime configuration is known invalid.

## Files Changed In Deployment Phase 23 Retry 3

- `BUILD_STATE.md`

## Commands Run In Deployment Phase 23 Retry 3

- `git status --short --untracked-files=all`
- `tail -n 180 BUILD_STATE.md`
- `vercel inspect medical-chatbot-nine-topaz.vercel.app --no-color`
- `vercel env ls production --project medical-chatbot --no-color`
- `curl -sS -D /tmp/medical_chatbot_vercel_health3_headers.txt -o /tmp/medical_chatbot_vercel_health3.json https://medical-chatbot-nine-topaz.vercel.app/health`
- `.venv/bin/python -m compileall app.py api src tests scripts store_index.py template.py`
- `.venv/bin/pytest -q`
- `.venv/bin/python -m pip check`
- `git diff --check`
- `.venv/bin/python - <<'PY' ... secret-shaped scan excluding .env and PDFs ... PY`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} +`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests And Verification

- `python -m compileall`: pass.
- Full default offline `pytest -q`: pass, 89 passed, 3 skipped, 16 subtests passed.
- `pip check`: pass, no broken requirements.
- `git diff --check`: pass.
- Refined secret-shaped scan: pass.
- Cache cleanup outside `.venv`: pass.

## Blockers

- Vercel `HUGGINGFACE_EMBEDDING_MODEL` is set incorrectly. It appears to be set to the provider name `hf-inference`; it must be the embedding model ID `sentence-transformers/all-MiniLM-L6-v2`.
- Vercel encrypted environment values cannot be printed or verified directly by this audit, but the deployed app's own safe validation confirms the value is invalid.

## Vercel Action Required

- In Vercel project `medical-chatbot`, edit the Production environment variable:
  - `HUGGINGFACE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2`
- Optionally add or correct:
  - `HUGGINGFACE_INFERENCE_PROVIDER=hf-inference`
- Keep:
  - `EMBEDDINGS_PROVIDER=huggingface_api`
  - `HF_TOKEN=<your valid Hugging Face token>`
- Redeploy production after changing the environment variable.

## Next Expected Phase

- After correcting `HUGGINGFACE_EMBEDDING_MODEL` and redeploying, resume with one deployed `/health` check and at most one deployed `/get` request.

---

## Deployment Phase 23 Retry 4 - Strategy B Chat Smoke After Config Fix

Status: BLOCKED
Completion timestamp: 2026-09-07 19:05:23 +06

## Scope

- Resumed after the user reported `HUGGINGFACE_EMBEDDING_MODEL` was corrected and production redeployed.
- Verified the production alias points to a newer Ready deployment.
- Checked `/health` first.
- Made exactly one deployed `/get` request.
- Did not run `store_index.py`.
- Did not rebuild embeddings.
- Did not upload or inspect PDF content.
- Did not recreate, delete, or mutate the Pinecone index.
- Did not make repeated OpenRouter requests.
- Did not print API key values.
- Did not stage or commit files.

## Deployment Findings

- Production alias: `https://medical-chatbot-nine-topaz.vercel.app`
- Direct deployment URL after latest redeploy: `https://medical-chatbot-cs1cfdxx6.vercel.app`
- Deployment status: Ready.
- Vercel build output reports Python function size: 50.45 MB.
- Vercel production now contains `HUGGINGFACE_INFERENCE_PROVIDER`.
- Deployed `/health` returned HTTP 200 and `runtime_configuration_present=true`.

## Deployed Smoke Result

- `POST /get` returned HTTP 503 with sanitized JSON error: `The language model request failed.`
- Vercel logs showed:
  - Hugging Face hosted embedding request returned HTTP 200.
  - OpenRouter chat completion request returned HTTP 200.
- Since both upstream services returned HTTP 200, the remaining failure is in the answer extraction/empty-answer path after OpenRouter responds.
- A previous production request in Vercel logs returned HTTP 200 after the same Hugging Face and OpenRouter endpoints returned HTTP 200, so the current failure appears consistent with free-model variability or empty model output rather than a permanent connectivity/configuration failure.

## Local Fix Implemented

- Increased `LLM_MAX_TOKENS` from 48 to 192 to give `openrouter/free` routed models enough room to produce visible answer text.
- Added a clearer user-facing Flask error message when the RAG chain gets an empty/no-answer LLM response.
- Kept retry count at zero and did not add any automatic retry loop.
- Did not hard-code a specific OpenRouter model.

## Files Changed In Deployment Phase 23 Retry 4

- `BUILD_STATE.md`
- `app.py`
- `src/rag.py`
- `tests/test_app.py`

## Commands Run In Deployment Phase 23 Retry 4

- `git status --short --untracked-files=all`
- `tail -n 160 BUILD_STATE.md`
- `vercel inspect medical-chatbot-nine-topaz.vercel.app --no-color`
- `vercel env ls production --project medical-chatbot --no-color`
- `curl -sS -D /tmp/medical_chatbot_vercel_health4_headers.txt -o /tmp/medical_chatbot_vercel_health4.json https://medical-chatbot-nine-topaz.vercel.app/health`
- `curl -sS -D /tmp/medical_chatbot_vercel_get4_headers.txt -o /tmp/medical_chatbot_vercel_get4.json -X POST https://medical-chatbot-nine-topaz.vercel.app/get -H 'Content-Type: application/json' --data '{"message":"What are common symptoms of dengue?"}'`
- `vercel logs medical-chatbot-nine-topaz.vercel.app --since 15m --no-color`
- `sed -n '1,260p' src/rag.py && sed -n '1,220p' tests/test_rag.py`
- `sed -n '240,420p' src/rag.py && sed -n '1,220p' src/prompt.py`
- `sed -n '1,220p' tests/test_integration.py`
- `.venv/bin/pytest -q tests/test_app.py tests/test_rag.py`
- `.venv/bin/python -m compileall app.py api src tests scripts store_index.py template.py`
- `.venv/bin/pytest -q`
- `.venv/bin/python -m pip check`
- `VERCEL=1 EMBEDDINGS_PROVIDER=huggingface_api PINECONE_API_KEY=placeholder-pinecone OPENROUTER_API_KEY=placeholder-openrouter HF_TOKEN=placeholder-hf .venv/bin/python - <<'PY' ... api.index import and route check ... PY`
- `git diff --check`
- `.venv/bin/python - <<'PY' ... secret-shaped scan excluding .env and PDFs ... PY`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} +`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests And Verification

- Focused tests: pass, 40 passed, 1 skipped, 4 subtests passed.
- `python -m compileall`: pass.
- Full default offline `pytest -q`: pass, 90 passed, 3 skipped, 16 subtests passed.
- `pip check`: pass, no broken requirements.
- Vercel-style `api.index` import and route check: pass, `/` and `/health` returned 200 with placeholder values not exposed.
- `git diff --check`: pass.
- Refined secret-shaped scan: pass.
- Cache cleanup outside `.venv`: pass.

## Blockers

- The deployed production app still uses the previous `LLM_MAX_TOKENS=48` code until these local changes are redeployed.
- `openrouter/free` may route to models that produce empty output or behave inconsistently. The code now allows more output tokens, but if the issue continues after redeploy, choose a currently available specific free OpenRouter model in the Vercel `OPENROUTER_MODEL` variable instead of relying on `openrouter/free`.

## Vercel Action Required

- Redeploy the project so Vercel runs the updated `src/rag.py`, `app.py`, and `tests/test_app.py` changes.
- Keep these server-side env values:
  - `EMBEDDINGS_PROVIDER=huggingface_api`
  - `HUGGINGFACE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2`
  - `HUGGINGFACE_INFERENCE_PROVIDER=hf-inference`
  - `HF_TOKEN=<your valid Hugging Face token>`

## Next Expected Phase

- After redeploying this token-limit/error-message fix, resume with one deployed `/health` check and at most one deployed `/get` request.

---

## Deployment Phase 23 Retry 5 - Strategy B Deployed Chat Smoke

Status: BLOCKED
Completion timestamp: 2026-09-07 19:13:04 +06

## Scope

- Resumed after the user reported the latest redeploy was done.
- Verified the production alias points to a newer Ready deployment.
- Checked `/health` first.
- Made exactly one deployed `/get` request.
- Did not run `store_index.py`.
- Did not rebuild embeddings.
- Did not upload or inspect PDF content.
- Did not recreate, delete, or mutate the Pinecone index.
- Did not make repeated OpenRouter requests.
- Did not print API key values.
- Did not stage or commit files.

## Deployment Findings

- Production alias: `https://medical-chatbot-nine-topaz.vercel.app`
- Direct deployment URL after latest redeploy: `https://medical-chatbot-6olusr6ri.vercel.app`
- Deployment status: Ready.
- Vercel build output reports Python function size: 50.45 MB.
- Vercel production environment variable names include Strategy B variables:
  - `EMBEDDINGS_PROVIDER`
  - `HF_TOKEN`
  - `HUGGINGFACE_EMBEDDING_MODEL`
  - `HUGGINGFACE_INFERENCE_PROVIDER`
  - `HUGGINGFACE_TIMEOUT_SECONDS`
- Deployed `/health` returned HTTP 200 and `runtime_configuration_present=true`.

## Deployed Smoke Result

- `POST /get` returned HTTP 503 with sanitized JSON error: `The language model returned an empty response. Try again later or choose another OpenRouter model.`
- Vercel logs showed:
  - Hugging Face hosted embedding request returned HTTP 200.
  - OpenRouter chat completion request returned HTTP 200.
- This confirms Strategy B connectivity is working through Vercel, Hugging Face hosted embeddings, and OpenRouter transport.
- The remaining failure is the response content from the OpenRouter model selected by `openrouter/free`.
- Vercel logs also showed an earlier production `/get` request returning HTTP 200 with the same Hugging Face and OpenRouter services, so the failure is intermittent/model-route dependent rather than a deployment import/configuration failure.

## Files Changed In Deployment Phase 23 Retry 5

- `BUILD_STATE.md`

## Commands Run In Deployment Phase 23 Retry 5

- `git status --short --untracked-files=all`
- `tail -n 180 BUILD_STATE.md`
- `vercel inspect medical-chatbot-nine-topaz.vercel.app --no-color`
- `vercel env ls production --project medical-chatbot --no-color`
- `curl -sS -D /tmp/medical_chatbot_vercel_health5_headers.txt -o /tmp/medical_chatbot_vercel_health5.json https://medical-chatbot-nine-topaz.vercel.app/health`
- `curl -sS -D /tmp/medical_chatbot_vercel_get5_headers.txt -o /tmp/medical_chatbot_vercel_get5.json -X POST https://medical-chatbot-nine-topaz.vercel.app/get -H 'Content-Type: application/json' --data '{"message":"What are common symptoms of dengue?"}'`
- `vercel logs medical-chatbot-nine-topaz.vercel.app --since 8m --no-color`
- `.venv/bin/python -m compileall app.py api src tests scripts store_index.py template.py && .venv/bin/pytest -q`
- `git diff --check`
- `.venv/bin/python - <<'PY' ... secret-shaped scan excluding .env and PDFs ... PY`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} +`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests And Verification

- `python -m compileall`: pass.
- Full default offline `pytest -q`: pass, 90 passed, 3 skipped, 16 subtests passed.
- `git diff --check`: pass.
- Refined secret-shaped scan: pass.
- Cache cleanup outside `.venv`: pass.

## Blockers

- The configured Vercel `OPENROUTER_MODEL` value still appears to rely on `openrouter/free`, which can route to a model that returns empty content for this chain.
- The deployed app is connected to Hugging Face and OpenRouter successfully, but the selected OpenRouter free route did not return usable answer text on the controlled request.

## Vercel Action Required

- Change the server-side Vercel `OPENROUTER_MODEL` value from `openrouter/free` to a specific currently available free OpenRouter model that returns normal chat content.
- Redeploy production after changing `OPENROUTER_MODEL`.
- Do not use `OPENAI_API_KEY` or `ChatOpenAI`.

## Next Expected Phase

- After selecting a specific working free OpenRouter model and redeploying, resume with one deployed `/health` check and at most one deployed `/get` request.

---

## Deployment Phase 23 Retry 6 - Specific OpenRouter Model Smoke

Status: BLOCKED
Completion timestamp: 2026-09-07 20:06:35 +06

## Scope

- Resumed after the user reported changing the Vercel `OPENROUTER_MODEL` value and redeploying.
- Verified the production alias points to a newer Ready deployment.
- Checked `/health` first.
- Made exactly one deployed `/get` request.
- Did not run `store_index.py`.
- Did not rebuild embeddings.
- Did not upload or inspect PDF content.
- Did not recreate, delete, or mutate the Pinecone index.
- Did not make repeated OpenRouter requests.
- Did not print API key values.
- Did not stage or commit files.

## Deployment Findings

- Production alias: `https://medical-chatbot-nine-topaz.vercel.app`
- Direct deployment URL after latest redeploy: `https://medical-chatbot-jp6ni9l1x.vercel.app`
- Deployment status: Ready.
- Vercel build output reports Python function size: 50.45 MB.
- Deployed `/health` returned HTTP 200 and `runtime_configuration_present=true`.
- Vercel production environment variable names remain present for Strategy B and OpenRouter.

## Deployed Smoke Result

- `POST /get` returned HTTP 503 with sanitized JSON error: `The configured language model is currently unavailable.`
- Vercel logs showed:
  - Hugging Face hosted embedding request returned HTTP 200.
  - OpenRouter chat completion request returned HTTP 404.
- This confirms Pinecone/Hugging Face deployment wiring is still working, but the configured OpenRouter model ID is unavailable or invalid.

## Current Free Model Evidence

- Checked OpenRouter's current model listing on 2026-09-07.
- OpenRouter lists `inclusionai/ling-3.0-flash-sante:free` as a free text/chat model with a health/medicine focus.
- Source: `https://openrouter.ai/inclusionai/ling-3.0-flash-sante:free`

## Files Changed In Deployment Phase 23 Retry 6

- `BUILD_STATE.md`

## Commands Run In Deployment Phase 23 Retry 6

- `git status --short --untracked-files=all`
- `tail -n 160 BUILD_STATE.md`
- `vercel inspect medical-chatbot-nine-topaz.vercel.app --no-color`
- `curl -sS -D /tmp/medical_chatbot_vercel_health6_headers.txt -o /tmp/medical_chatbot_vercel_health6.json https://medical-chatbot-nine-topaz.vercel.app/health`
- `vercel env ls production --project medical-chatbot --no-color`
- `curl -sS -D /tmp/medical_chatbot_vercel_get6_headers.txt -o /tmp/medical_chatbot_vercel_get6.json -X POST https://medical-chatbot-nine-topaz.vercel.app/get -H 'Content-Type: application/json' --data '{"message":"What are common symptoms of dengue?"}'`
- `vercel logs medical-chatbot-nine-topaz.vercel.app --since 8m --no-color`
- `.venv/bin/python -m compileall app.py api src tests scripts store_index.py template.py && .venv/bin/pytest -q`
- OpenRouter current model lookup for a free chat model.
- `git diff --check`
- `.venv/bin/python - <<'PY' ... secret-shaped scan excluding .env and PDFs ... PY`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} +`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests And Verification

- `python -m compileall`: pass.
- Full default offline `pytest -q`: pass, 90 passed, 3 skipped, 16 subtests passed.
- `git diff --check`: pass.
- Refined secret-shaped scan: pass.
- Cache cleanup outside `.venv`: pass.

## Blockers

- The current Vercel `OPENROUTER_MODEL` value is not accepted by OpenRouter; the chat completion endpoint returns HTTP 404.
- The encrypted value cannot be printed or inspected safely from this audit.

## Vercel Action Required

- Change Vercel Production `OPENROUTER_MODEL` to a valid current free OpenRouter chat model.
- A currently verified candidate is:
  - `OPENROUTER_MODEL=inclusionai/ling-3.0-flash-sante:free`
- Redeploy production after changing the environment variable.

## Next Expected Phase

- After correcting `OPENROUTER_MODEL` and redeploying, resume with one deployed `/health` check and at most one deployed `/get` request.

---

## Deployment Phase 23 Retry 7 - OpenRouter Reasoning Output Compatibility

Status: BLOCKED
Completion timestamp: 2026-09-07 22:40:01 +06

## Scope

- Retried the deployed Strategy B smoke test after the user requested another attempt.
- Verified the production alias points to a newer Ready deployment.
- Checked `/health` first.
- Made exactly one deployed `/get` request.
- Inspected sanitized Vercel logs once.
- Did not run `store_index.py`.
- Did not rebuild embeddings.
- Did not upload or inspect PDF content.
- Did not recreate, delete, or mutate the Pinecone index.
- Did not make repeated OpenRouter requests.
- Did not print API key values.
- Did not stage or commit files.

## Deployment Findings

- Production alias: `https://medical-chatbot-nine-topaz.vercel.app`
- Direct deployment URL after latest redeploy: `https://medical-chatbot-fpixb5con.vercel.app`
- Deployment status: Ready.
- Vercel build output reports Python function size: 50.45 MB.
- Deployed `/health` returned HTTP 200 and `runtime_configuration_present=true`.
- Vercel production environment variable names remain present for Strategy B and OpenRouter.

## Deployed Smoke Result

- `POST /get` returned HTTP 503 with sanitized JSON error: `The language model returned an empty response. Try again later or choose another OpenRouter model.`
- Vercel logs showed:
  - Hugging Face hosted embedding request returned HTTP 200.
  - OpenRouter chat completion request returned HTTP 200.
- The configured model is now accepted by OpenRouter, but it can still produce no normal answer content for this LangChain response path.

## Local Fix Implemented

- Added `LLM_REASONING = {"effort": "none"}`.
- Passed `reasoning=dict(LLM_REASONING)` to `ChatOpenRouter`.
- This asks reasoning-capable OpenRouter models to return normal answer content instead of spending output on hidden/reasoning tokens.
- Kept `LLM_MAX_RETRIES=0`.
- Kept `OPENROUTER_MODEL` configurable and did not hard-code a specific model.

## Files Changed In Deployment Phase 23 Retry 7

- `BUILD_STATE.md`
- `src/rag.py`
- `tests/test_rag.py`

## Commands Run In Deployment Phase 23 Retry 7

- `git status --short --untracked-files=all`
- `tail -n 160 BUILD_STATE.md`
- `vercel inspect medical-chatbot-nine-topaz.vercel.app --no-color`
- `curl -sS -D /tmp/medical_chatbot_vercel_health7_headers.txt -o /tmp/medical_chatbot_vercel_health7.json https://medical-chatbot-nine-topaz.vercel.app/health`
- `vercel env ls production --project medical-chatbot --no-color`
- `curl -sS -D /tmp/medical_chatbot_vercel_get7_headers.txt -o /tmp/medical_chatbot_vercel_get7.json -X POST https://medical-chatbot-nine-topaz.vercel.app/get -H 'Content-Type: application/json' --data '{"message":"What are common symptoms of dengue?"}'`
- `vercel logs medical-chatbot-nine-topaz.vercel.app --since 8m --no-color`
- `.venv/bin/python -m compileall app.py api src tests scripts store_index.py template.py && .venv/bin/pytest -q`
- OpenRouter public models endpoint check without using an API key.
- `.venv/bin/python - <<'PY' ... ChatOpenRouter signature and source inspection ... PY`
- `.venv/bin/pytest -q tests/test_rag.py tests/test_app.py`
- `.venv/bin/python -m compileall app.py api src tests scripts store_index.py template.py`
- `.venv/bin/pytest -q`
- `.venv/bin/python -m pip check`
- `VERCEL=1 EMBEDDINGS_PROVIDER=huggingface_api PINECONE_API_KEY=placeholder-pinecone OPENROUTER_API_KEY=placeholder-openrouter HF_TOKEN=placeholder-hf .venv/bin/python - <<'PY' ... api.index import and route check ... PY`
- `git diff --check`
- `.venv/bin/python - <<'PY' ... secret-shaped scan excluding .env and PDFs ... PY`
- `find . -path './.venv' -prune -o -path './.git' -prune -o -depth \( -type f -name '*.pyc' -o -type d -name '__pycache__' -o -type d -name '.pytest_cache' \) -exec rm -rf {} +`
- `date '+%Y-%m-%d %H:%M:%S %Z'`

## Tests And Verification

- Focused tests: pass, 40 passed, 1 skipped, 4 subtests passed.
- `python -m compileall`: pass.
- Full default offline `pytest -q`: pass, 90 passed, 3 skipped, 16 subtests passed.
- `pip check`: pass, no broken requirements.
- Vercel-style `api.index` import and route check: pass, `/` and `/health` returned 200 with placeholder values not exposed.
- `git diff --check`: pass.
- Refined secret-shaped scan: pass.
- Cache cleanup outside `.venv`: pass.

## Blockers

- The deployed production app still uses the previous OpenRouter request parameters until this local reasoning compatibility fix is redeployed.

## Vercel Action Required

- Redeploy production so Vercel runs the updated `src/rag.py`.
- Keep `OPENROUTER_MODEL` set to a valid current free chat model.

## Next Expected Phase

- After redeploying this reasoning compatibility fix, resume with one deployed `/health` check and at most one deployed `/get` request.
