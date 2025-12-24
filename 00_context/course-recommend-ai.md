## Project Context Specification (Static)

### 1. Identity & Scope
- **Project Name:** course-recommend-ai
- **Type:** Data Pipeline & Backend for Intelligent RAG Service
- **Core Objective:**
    - **Mission:** Personalize university course recommendation based on academic history & future goals.
    - **Key Value:**
        - **Hybrid RAG:** VectorDB (Semantic) + GraphDB (Reasoning) + RDB (Hard Filtering).
        - **SSOT Architecture:** File-based Data Lake (`data/`) as the Single Source of Truth.
        - **Efficiency:** "Group by Stage" organization & Streaming processing.

### 2. Functional Requirements (The "What")
- **Must-Have Features:**
    1. **Crawling Pipeline:** Strategy-based fetching of raw syllabus data (HTML or PDF).
    2. **Parse & Enrich Pipeline:** Extract structure from HTML or PDF & Enrich metadata using LLMs.
    3. **Personalization Engine:** Match courses via "Hard Constraints" (Time, Credits) & "Soft Preferences" (Goals).
- **Target Audience:** University students (Starting with Korea Univ).

### 3. Technical Constraints (Immutable)
- **Quality Policy:** Quality & Architecture > Speed. (SoC, Strict Typing, Maintainability).
- **Infrastructure:**
    - **Runtime:** Python 3.12+ (Hatch/uv).
    - **Orchestration:** Prefect (Flows/Tasks).
    - **Storage:** Local JSON Data Lake (Primary) -> Sync to RDB/VDB/GDB (Secondary).
- **Architectural Axioms:**
    - **Path Partitioning:** `data/universities/[stage]/[univ]/[year]/[semester]/...`
    - **Streaming:** Strictly use `ijson` and Generators for large datasets.
    - **Polymorphism:** Use Discriminated Unions for User Goals (`AcademicJourney`).
    - **DI:** Fetcher/Saver must be injected into Strategies.