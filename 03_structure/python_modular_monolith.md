## Project Topology (Context: Robust Engineering)

### Directory Map
Root/
├── .devcontainer/            # [Optional] Development Environment (Standard)
│   ├── devcontainer.json     # Settings & Extensions
│   ├── Dockerfile            # Dev Environment Image
│   └── post-create.sh        # Setup Hook (uv sync, pre-commit)
├── src/                      # Source Code (Core Logic)
│   ├── config/               # Shared Kernel (SSOT)
│   ├── infra/       # Global Adapters (DB, Redis, 3rd Party)
│   ├── utils/                # Global Pure Helpers
│   ├── interfaces/           # Entry Points (Adapters)
│   │   ├── api/              # FastAPI/Web Routes
│   │   ├── cli/              # Typer/Click Commands
│   │   ├── gui/              # PySide6/Tauri Adapters
│   │   └── tasks/            # Celery/Async Workers
│   └── {domain_module}/      # Feature Module (Vertical Slice)
│       ├── services/         # Business Logic & Orchestration
│       ├── entities/         # Pure Domain Models (Data Classes)
│       ├── schemas/          # DTOs/Validation (Pydantic)
│       ├── ports/            # Abstract Interfaces (Protocols)
│       ├── infra/            # Concrete Implementations (Repositories)
│       ├── exceptions/       # Domain Specific Errors
│       └── utils/            # Domain-Specific Helpers
├── tests/                    # Verification (MUST be at Root)
│   ├── unit/
│   └── integration/
├── scripts/                  # Runnable Utilities (One-off)
├── .gitignore                # Version Control Exclusion
├── README.md                 # Project Documentation
├── .env.example              # Config Template
├── pyproject.toml            # Dependencies
├── uv.lock                   # Lock file
└── Makefile                  # [Optional] Task Runner Facade

### Structural Constraints
1.  **Dev Environment:**
    - **Standard:** Use `.devcontainer` for team consistency.
    - **Local/Simple:** `uv` venv is acceptable if Docker is overkill.

2.  **Module Strategy (Feature Slices):**
    - **Default (Structured):** Prioritize **Folders** (as shown above) for maintainability.
    - **Exception (Flattened):** ONLY for trivial CRUD domains, merging files is allowed (e.g., `services.py`, `models.py`).
    - **Rule:** Domain `utils` MUST be pure functions. Domain `exceptions` MUST inherit from App Base Exception.

3.  **Root Mandates:**
    - `README.md` and `.gitignore` are **REQUIRED**.
    - `tests/` must reside at **ROOT**, not inside `src/`.