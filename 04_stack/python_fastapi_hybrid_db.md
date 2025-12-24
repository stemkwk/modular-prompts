## Preferred Tech Stack (Context-Aware Selection)

### 1. Core Foundation & DX
- **Runtime & Build:**
    - App: `Docker`, `uv` (Package Manager).
    - Script: `uv run`.
    - Build Backend: `Hatch`.
- **Task Runner Strategy (Hybrid):**
    - **Logic (SSOT):** `Hatch Scripts` in `pyproject.toml`. All flags/options defined here.
    - **Facade (DX):** `Makefile`. Wraps hatch commands for simple typing (e.g., `make test`).
- **Standard Libs:** `pathlib` (Filesystem), `zoneinfo` (Time), `json`, `yaml`.

### 2. Quality Assurance
- **Static Analysis:** `Ruff` (Lint/Format), `Pyright` (Strict Typing).
- **Testing:**
    - Runner: `Pytest` + `pytest-asyncio`.
    - Data Factory: **Polyfactory** (Dynamic fixtures > Hardcoded Dicts).
    - **Infrastructure:** **Testcontainers** (Real Postgres > SQLite) to ensure 100% compatibility.
    - **Mocking Strategy:**
        - **Unit:** Use `pytest-mock` (`mocker` fixture).
        - **Integration (FastAPI):** Use `app.dependency_overrides`.
        - **Constraint:** Avoid patching internal implementation details (Mock Interfaces, not Implementation).
    - Coverage: `coverage.py`.
- **Observability:**
    - Engineering: `structlog` (Structured).
    - Simplicity: `loguru`.

### 3. Interface Frameworks
- **Web API:** `FastAPI` (Standard, Pydantic v2).
- **CLI Tool:** `Typer` + `rich` (UI).
- **GUI & Desktop (Select by Context):**
    - **Internal Tools:** `PySide6` (Qt) - Native Performance.
    - **Consumer Apps:** `Tauri` OR `Web Frontend` (React/Vue).
- **Background Tasks:** `Celery` (Distributed) OR `asyncio` loops (Simple).

### 4. Data & Storage (Select ONLY if required)
- **RDBMS:** PostgreSQL + SQLAlchemy 2.0+ (Async) + Alembic.
- **Specialized DB:**
    - Vector: `pgvector`.
    - Graph: `Memgraph`.
- **Cache:** Redis (via `redis-py` async).
- **Object Storage:** MinIO (S3 Compatible).

### 5. Domain Utilities & Modeling
- **Data Validation:** `Pydantic` (Core Data Model - v2+).
- **Configuration:** `pydantic-settings` (Env Management).
- **Computation:** `NumPy`, `Polars` (Performance), `OpenCV`.
- **Network:** `httpx` (Async Client).
- **Auth:** `PyJWT` (Token), `pwdlib` (Modern Hashing) OR `bcrypt`.