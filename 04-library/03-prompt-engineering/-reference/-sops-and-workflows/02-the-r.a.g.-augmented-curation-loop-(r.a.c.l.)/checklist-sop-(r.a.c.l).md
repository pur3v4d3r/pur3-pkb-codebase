---
title: Checklist_SOP_(R.A.C.L)
aliases:
  - RACL Workflow Checklist
  - Automated RACL Steps
  - 8-Phase RACL Sequence
tags:
  - workflow
  - pkb
status: seedling 🌱
created: 2025-10-10T04:01:25.971Z
updated: 2025-10-10T04:02:06.471Z
source: "[[📙🧠report_r.a.g.-augmented-curation-loop-(r.a.c.l.)]]"
related:
  - "[[🚀proj-prompt-engineering-note]]"
  - "[[📙🧠report_r.a.g.-augmented-curation-loop-(r.a.c.l.)]]"
  - "[[checklist_workflow_(r.a.c.l.-m.)]]"
  - "[[checklist_sop_(r.a.c.l)]]"
  - "[[sop_prompting_inside-pkb_manually_(r.a.c.l.)]]"
---


## ✅ RACL Workflow Checklist: The 8-Phase Sequence

> [!the-purpose]
> - This checklist outlines the primary actions within the RACL's single, uninterrupted sequence, orchestrated by the QuickAdd Macro.

|Phase|**Action / Mandate**|**Tool / Mechanism**|**Compliance Check**|
|---|---|---|---|
|**P1**|**Semantic Retrieval (RAG Mandate):** Prompt user for **Initial Research Query**. Invoke **Smart Chat** to perform semantic search, retrieving top _N_ relevant vault notes to ground the LLM's context.|QuickAdd Macro ![](data:,) Smart Connections|Context is injected into Master Prompt (Section B).|
|**P2**|**Input Formatting & Initialization:** Create temporary **`RACL Staging Note`** in the `_RACL_Staging/` folder. Initialize YAML frontmatter with placeholders (e.g., `user_query`, `review_date`, `status: "Draft: Phase 2"`).|Templater Script ![](data:,) Dedicated Folder Structure|YAML frontmatter is created with all required fields (including nested placeholders).|
|**P3**|**Critical Analysis (LLM Execution):** Execute Smart Chat with the **Master Prompt Template**. LLM **must** generate a visible **Chain-of-Thought (CoT)** reasoning trace, followed immediately and exclusively by a single, parsable YAML code block.|QuickAdd Macro ![](data:,) LLM/Smart Chat ![](data:,) Master Prompt|Output is a single ` ```yaml... ``` ` block containing **CoT** trace.|
|**P4**|**Structured Metadata Scoring:** Execute `RACL_ScoreParser.js`. Script **must** parse the LLM's YAML output, extracting nested keys (e.g., `critique.score`, `rag_source`), and injecting them directly into the note's YAML frontmatter.|Templater User Script (`RACL_ScoreParser.js`) ![](data:,) Obsidian API|`status` field is updated to **`Scored: Phase 4`**.|
|**P5**|**Zettel Deconstruction:** Execute `RACL_Zettelizer.js`. Script **must** iterate through the `zettel_decomposition` list from the LLM's output. For each item, use `tp.file.create_new` to materialize a new atomic note in the **`03_Zettels`** folder. **Crucially**, each new Zettel must automatically include a link back to the parent `RACL Staging Note` (e.g., `source: [[parent note]]`).|Templater User Script (`RACL_Zettelizer.js`) ![](data:,) `tp.file.create_new`|All Zettels are created and contain an explicit link to the staging note in their frontmatter.|
|**P6**|**Contextual Review (Human Intervention):** Researcher reviews Zettels and scores. Primary task is **Establish/Embed**, manually applying contextual links (`[[]]`) to MOCs and related concepts, integrating the new knowledge into the semantic network.|Human / Dataview (Dynamic MOCs)|New Zettels are linked to the existing vault structure.|
|**P7**|**Auditing and Indexing:** Run **Dataview Audit Queries** (e.g., **Rigor Audit: Low Score Flag**, **Zettelization Failure Log**) to identify outputs requiring re-evaluation.|Dataview Queries ![](data:,) Audit Dashboards|All RACL notes meet or are flagged for not meeting the required intellectual rigor thresholds (e.g., `critique.score > 0.7`).|
|**P8**|**Loop Closure and Archival:** Researcher manually updates the note's `status` to **`Archived`**. Execute the final QuickAdd Macro/Obsidian command to move the file from `_RACL_Staging/` to the permanent **`99_Archive/`** folder.|Manual Update ![](data:,) QuickAdd Macro ![](data:,) Obsidian Command|Vault hygiene is maintained; note is removed from staging and moved to archive.|

---

## ⚙️ Architectural Layer Mandates

### 1. **Structured Automation Layer (QuickAdd Orchestrator)**

|**Mandate**|**Technical Requirement**|
|---|---|
|**Uninterrupted Sequence**|The QuickAdd Macro must be configured as a comprehensive **Macro Choice**, chaining the execution of all steps (**P2, P3, P4, P5**) sequentially to enforce the methodology.|
|**Enforced Input**|The macro must prompt the user for the query and use that value to parameterize the **Staging Note title** and the **Master Prompt execution**.|
|**LLM Constraint**|The macro step for **P3** must be configured as an **AI Assistant Command** (Smart Chat) that runs the Master Prompt on the _active file_ and _waits for output_.|
|**Completion Notification**|The final macro step must be an **Obsidian Command** to notify the user of RACL completion, guiding them toward the **Phase 6** review.|

### 2. **Templater Scripting Logic (Data Integrity and Creation)**

|**Script**|**Mandate**|
|---|---|
|**`RACL_ScoreParser.js` (P4)**|**Must** reliably locate and parse the text between the **` ```yaml... ``` `** delimiters. **Must** extract complex nested keys (e.g., `critique.score`, `rag_source_used`). **Must** use the Templater API environment to execute file updates, injecting scores into the note's frontmatter.|
|**`RACL_Zettelizer.js` (P5)**|**Must** extract the `zettel_decomposition` list from the parsed YAML. **Must** use the `tp.file.create_new` function to create new files in **`03_Zettels`**. **Must** ensure the Zettel content is extracted correctly from the LLM’s use of the **YAML literal block style (`|

### 3. **Master Prompt Template (LLM Governance)**

| **Mandate**           | **Technical Requirement**                                                                                                                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Role Assignment**   | Explicitly assign the LLM the persona of a **'Senior Academic Research Analyst specializing in PKM Decomposition'**.                                                                                                  |
| **Output Mandate**    | **Crucial:** The LLM **MUST NOT** include any introductory or explanatory text outside of the Reasoning Trace and the YAML block.                                                                                     |
| **CoT Enforcement**   | **Must** demand a sequential, multi-step **Chain-of-Thought (CoT)** section (C.1, C.2, C.3) **before** the structured output block.                                                                                   |
| **Schema Strictness** | Output **MUST** be delivered in a single, dedicated, parsable YAML code block (` ```yaml... ``` `) with the required **nested structure** (`critique: { score: ..., novelty: ... }`) and the `rag_source_used` links. |