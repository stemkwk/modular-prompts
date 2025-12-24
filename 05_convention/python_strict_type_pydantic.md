## Code Style & Syntax Rules

### 1. Formatting & Typing Standards
- **Tooling Enforcement:** Strict adherence to `Ruff` (Linting) & `Pyright` (Typing).
- **Indentation:** 2-space.
- **Import Strategy:** Group strictly by **[Standard Lib] > [Third Party] > [Local Modules]**.
- **Type Hints:**
    - **Mode:** 100% Strict (Use `type` keyword (PEP 695) over `TypeAlias`, `Protocol`).
    - **Syntax:** Modern Union (`X | Y`). No string quotes.
    - **Imports:** `from __future__ import annotations` (MANDATORY at top).
    - **Circularity:** Use `if typing.TYPE_CHECKING:` to prevent runtime import costs.

### 2. Implementation Patterns
- **Filesystem [CRITICAL]:** STRICTLY use `pathlib.Path`. (**BAN:** `os.path`).
- **Resource Safety:** Context Managers (`with`) REQUIRED for file/network I/O.
- **Data Modeling:**
    - **Internal:** `@dataclass(frozen=True)` (Immutable).
    - **External (API):** `Pydantic` (`BaseModel`) v2.
    - **Rule:** Keep ORM models separate from Pydantic schemas.

### 3. Advanced Pythonic Patterns
- **Magic Methods (Dunder):**
    - **Rule:** Leverage Python's **Data Model** (`__init__`, `__str__`, `__call__`) instead of custom method names (e.g., avoid `to_string()`, `execute()`).
    - **Debugging:** Implement `__repr__` for all classes to ensure unambiguous debugging output.
    - **Containers:** Implement `__getitem__`, `__len__`, `__iter__` to make objects behave like native containers.
- **Decorators:**
    - **Strategy:** Leverage **Class-based** or **Parametrized** decorators for stateful logic.
    - **Metadata:** ALWAYS preserve metadata via `@functools.wraps`.
    - **Utils:** Use `contextlib.contextmanager` for simple resource management.
- **String Handling:**
    - **Simple:** Use `f-strings` (Default).
    - **Complex/Dynamic:** Use **Factory Pattern** or **Template Engine** (e.g., Jinja2). Avoid complex logic inside f-string braces.
- **Comprehensions:**
    - **Scope:** List/Dict/Set/Generator comprehensions allowed.
    - **Constraint:** Readability First. IF (Logic > 2 lines) -> Refactor to Loop or Helper Function.
    - **Syntactic Sugar:** Use Walrus Operator (`:=`) sparingly for concise assignments.

### 4. Control Flow & Optimization [CRITICAL]
- **Data Structure Selection:**
    - **Stop abusing `list`:** Use specialized containers.
    - **Lookup:** `set` (O(1)) > `list` (O(N)).
    - **Mapping:** `dict` (Hash Map) > `if-elif` chains.
    - **Queue/Count:** `collections.deque`, `collections.Counter` > Manual implementation.
- **Vectorization:**
    - **Rule:** For numerical/data processing, use `NumPy` or `Pandas`.
    - **Ban:** Explicit `for` loops for calculation (Use vectorized operations).
- **Branching:**
    - Prefer **Guard Clauses** (Early Return) over nested `if`.
    - Prefer **Dictionary Dispatch** over long switch/match chains.

### 5. Security & API Guidelines
- **Secrets:** NEVER hardcode. Use `.env` (via `pydantic-settings`).
- **Logs:** Mask PII/Sensitive data before logging.
- **i18n Readiness:** Ensure error messages and user-facing strings are **decoupled** for future Internationalization. Use placeholders or error codes, not raw strings.
- **API Errors:** Use standardized **Error Codes** (e.g., `AUTH_001`), not just HTTP Status.

### 6. Documentation Standards
- **Docstrings:** Google Style (English). Mandatory for **Public Interfaces**.
- **Comments:** No emojis. Technical and objective only.

### 7. Mode-Specific Exceptions [CRITICAL]
**IF (Mode == Hacking/Scripting):**
- **Relaxation:**
    - Explicit Type Hints (`Protocol`, `TypeAlias`) are **OPTIONAL**.
    - Dependency Injection is **NOT REQUIRED**.
    - Single file structure is **PREFERRED**.
    - `print()` is allowed (instead of `structlog`).