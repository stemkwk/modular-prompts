## Testing Strategy & Standards

### 1. Scope Definition
- **Unit Tests:**
    - **Target:** Domain Logic, Pure Utils, Transformations.
    - **Constraint:** **STRICTLY NO I/O** (No DB, No Network).
    - **Technique:** Use `unittest.mock` or `pytest-mock` for dependencies.
- **Integration Tests:**
    - **Target:** API Endpoints, Repository Layers, DB Queries.
    - **Constraint:** Use **REAL** dependencies (Docker/Testcontainers) where possible.
    - **Async:** Must be marked with `@pytest.mark.asyncio`.

### 2. Tooling & Patterns
- **Framework:** `pytest` (Primary runner).
- **Data Generation:**
    - **Rule:** Use **`polyfactory`** (Model Factories) > Hardcoded Dicts.
    - **Reason:** Ensures data stays synced with Pydantic models.
- **Coverage:** Aim for 80%+ on Domain Logic.

### 3. Implementation Rules
- **Location:** All tests MUST reside in `tests/` at the Project Root.
- **Naming:**
    - Files: `test_*.py`
    - Functions: `test_{function_name}_{condition}_{expected}`
    - Example: `test_create_user_duplicate_email_raises_error`
- **Anti-Patterns (BANNED):**
    - Testing built-in framework/library functionality.
    - Using `time.sleep` (Use polling/events instead).