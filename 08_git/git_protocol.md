## Version Control Protocol

### 1. Commit Standards
- **Convention:** **Conventional Commits** v1.0.0.
- **Language:** **English ONLY**. (Imperative mood: "Add" not "Added").
- **Format:** `type(scope): subject`
    - **Types:**
        - `feat`: New feature.
        - `fix`: Bug fix.
        - `refactor`: Code change that neither fixes a bug nor adds a feature.
        - `chore`: Build process, dependency updates.
        - `docs`: Documentation only changes.
        - `test`: Adding missing tests.
    - **Example:** `feat(auth): implement JWT refresh token logic`

### 2. Pull Request (PR) Rules
- **Title:** Matches the Commit Subject (e.g., `feat(user): ...`).
- **Description Body:**
    - **Summary:** What changed?
    - **Impact:** Breaking changes? (Yes/No)
    - **Testing:** How can the reviewer verify this? (Step-by-step).

### 3. Branching Strategy
- **Main/Master:** Production-ready code.
- **Feature Branch:** `feat/{ticket-id}-{short-desc}`
- **Fix Branch:** `fix/{ticket-id}-{short-desc}`