---
title: Flow-Diagram_Agentic-Breakdown__(C.A.w.)
aliases:
  - "Process Flow Diagram: AMP-F Agentic Breakdown"
  - Agentic Workflow Flowchart
  - AMP-F Agent Breakdown
  - Gemini 2.5 CAG Process
tags:
  - prompt-engineering
  - project/prompt_engineering
  - type/reference
status: 🪴 seedling
created: 2025-10-09T05:52:17.780Z
updated: 2025-10-09T06:05:13.859Z
source: "[Gemini-2.5-Flash]"
related:
  - "[[🚀proj-prompt-engineering-note]]"
  - "[[report_the-cognitive-augmentation-workflow_(c.a.w.)]]"
date created: 2025-10-09T01:52:17.000-04:00
date modified: 2025-10-10T00:20:00.218-04:00
---
``
# Process Flow Diagram: AMP-F Agentic Breakdown

> [!the-purpose]
> This reference note clarifies the roles and sequence of the **Generative Execution (Phase II)**—the technical engine of the workflow. It explains _who_ (which agent) does _what_ and _when_.

## **The Agentic Meta-Prompting Framework (AMP-F) Flow**

1. **System Role (The Constraint Setter)**
    - **Action:** Establishes non-negotiable global constraints (Persona, Tone, Citation Style, Mandatory Output Formatting).
    - **Goal:** Define the operating environment and scholarly non-negotiables.

2. **Conductor LLM (The Architect/Orchestrator)**
    - **Action:** Receives the complex task, decomposes it, and employs the **Tree-of-Thoughts (ToT)** strategy.
    - **Goal:** Plan the reasoning path, oversee the process, and maintain the final coherent structure.

3. **Expert LLM (The Specialized Researcher) - RAG Enabled**
    - **Action:** Executes highly specific, singular tasks delegated by the Conductor, primarily **Retrieval Augmented Generation (RAG)** lookups.
    - **Goal:** Access the external, verified knowledge base to ensure factual grounding and mitigate hallucination.

4. **Expert LLM (The Specialized Researcher) - Contradiction**
    - **Action:** Executes singular tasks like drafting an opposing viewpoint or counter-argument.
    - **Goal:** Proactively inject conceptual nuance and challenge the primary narrative.

5. **Conductor LLM (Synthesis and Formatting)**
    - **Action:** Synthesizes the outputs from the Expert Agents and applies the mandated final structure (Markdown + YAML Front Matter).
    - **Goal:** Ensure the output is immediately ready for Phase III Validation.
