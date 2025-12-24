# modular-prompts

> **"Prompt as Code."**
> Stop copy-pasting massive text blocks. Build your perfect System Prompt by assembling modular components.

## Why Modular?
Instead of maintaining a single, monolithic text file, this repository treats prompts as **components**. This approach brings software engineering best practices to prompt engineering:

* **Composable:** Mix and match modules (Identity, Tech Stack, Rules) like LEGO blocks.
* **Maintainable:** Update your coding standards in one file, and it applies everywhere.
* **Context-Aware:** Easily switch between "Engineering Mode" and "Scripting Mode".

## Structure
- `01_identity/`: **Who** the AI acts as (e.g., Principal Architect).
- `02_philosophy/`: **Core values** and mindset.
- `03_structure/`: Project **directory structures**.
- `04_stack/`: Preferred **technology stacks**.
- `05_convention/`: **Coding conventions** and rules.
- `06_interaction/`: **Response protocols** and behavior.

## Usage
1. Choose your modules.
2. Combine them in order (01 → 06).
3. Paste into **ChatGPT Custom Instructions** or **Claude Projects**.