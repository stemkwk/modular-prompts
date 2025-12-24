## Project Structure & Layout (Context-Dependent: Type B)
**Type B: The "Swiss Army Knife" (Script/Automation)**
* **Use when:** Cron jobs, file manipulation, "throwaway" tasks (Hacking Mode).
* **Structure:** Keep it flat. `main.py`, `config.py`, `utils.py`.
* **Metadata:** Use **PEP 723** (`# /// script ...`) for dependency management.