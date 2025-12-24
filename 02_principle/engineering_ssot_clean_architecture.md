## Context Configuration (Mode Switching)
**CASE 1: Engineering Mode (Target: Apps, APIs, Packages)**
- **Constraints:**
    - **Physical Layout:** Strict separation of `src/` (Core Logic) vs `scripts/` (Utilities).
    - **Architecture:** Clean Architecture + SSOT.
    - **Typing:** 100% Strict (`TypeAlias`, `Protocol`).

**CASE 2: Hacking Mode (Target: Scripts, Prototypes)**
- **Constraints:**
    - **Structure:** Single file (`main.py`) or flat structure allowed.
    - **Metadata:** PEP 723 (Inline Metadata) preferred.
    - **Entry Point:** `if __name__ == "__main__":` REQUIRED.

## Architectural Axioms (The "What")
1. **Interface-Agnostic Design [CRITICAL]:**
    - **Philosophy:** Treat Web APIs as just one of many interfaces (Universal Interface).
    - **Rule:** Business Logic MUST NOT import from Interface layers.
    - **Test:** Logic must be executable purely via Python shell without HTTP context.

2. **Dependency Injection (DI):**
    - **Rule:** Minimize direct object instantiation.
    - **Method:** Inject dependencies explicitly via **Constructors** (`__init__`).

3. **Logical Cohesion over Abstraction:**
    - **Context:** Especially for CPU-bound/Computational logic (e.g., NumPy).
    - **Constraint:** Do **NOT** over-engineer with complex Interfaces (`Protocol`).
    - **Action:** **Centralize** computational logic into specific modules/functions.

4. **Pipeline & SoC:**
    - **SSOT:** Logic/Config definitions MUST exist in exactly one place.
    - **Pipeline Design:** Break complex logic into stages. Use **Generators (`yield`)** for streaming/memory efficiency.

## Operational Standards (The "How")
1. **Defensive Programming (Fail Fast):**
    - **Structure:** Define a **Domain-Specific Base Exception** (Inherit from `Exception`).
    - **Action:** Raise specific errors immediately. Never use silent `pass`.
    - **Invariants:** Use `assert` liberally for internal state checks.

2. **Observability (Logging Strategy):**
    - **Tool Selection:**
        - **IF (Complex/Production):** Use `structlog` (JSON structure).
        - **ELSE (Simple/Script):** Use `loguru` (DX/Simplicity).
    - **Rule:** Treat logs as **Event Data**, not strings.
    - **Context:** MUST inject **Contextual Identifiers** (e.g., Correlation IDs).

3. **Performance & Concurrency:**
    - **Asyncio First:** Default to async loops. Match Sync/Async drivers carefully.
    - **Optimization:** Profile first, then Optimize (e.g., Port to Rust/C). No premature optimization.

4. **Pythonic Orthodoxy:**
    - **Style:** Follow **PEP 20** (Zen of Python).
    - **Flow:** Prefer EAFP (`try-except`) over LBYL (`if-else`).
    - **Duck Typing:** Prefer **Structural Subtyping** (`Protocol`) over Nominal Inheritance. Focus on what an object *does* (behavior), not what it *is*.
    - **Idioms:** Use Context Managers (`with`) for resource safety

## Refactoring Protocol
- **Trigger:** Violation of Interface Agnosticism OR SSOT.
- **Safety Net:** IF (Tests == Missing) -> Write tests first -> THEN refactor.
- **Action:** Aggressively decouple Logic from Interface if mixed.
- **Boy Scout Rule:** Commit_Quality > Checkout_Quality.