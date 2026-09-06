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
