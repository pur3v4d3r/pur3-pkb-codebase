---
title: Checklist_Workflow_(R.A.C.L.-M.)
aliases:
  - Fallback Workflow
  - Manual RACL Procedure Checklist
  - RACL-M Checklist
tags:
  - pkb
  - workflow
status: seedling 🌱
created: 2025-10-10T04:04:26.262Z
updated: 2025-10-10T04:06:30.912Z
source: "[[📙🧠report_r.a.g.-augmented-curation-loop-(r.a.c.l.)]]"
related:
  - "[[🚀proj-prompt-engineering-note]]"
  - "[[checklist_sop_(r.a.c.l)]]"
  - "[[📙🧠report_r.a.g.-augmented-curation-loop-(r.a.c.l.)]]"
  - "[[sop_prompting_inside-pkb_manually_(r.a.c.l.)]]"
date created: 2025-10-10T00:04:26.000-04:00
date modified: 2025-10-10T00:07:42.941-04:00
---

# Checklist_Workflow_(R.A.C.L.-M.)

## ✅ RACL-M Workflow Checklist: Manual Fallback Procedure

> [!the-purpose]
> - This checklist outlines the mandatory, step-by-step procedure to replicate the RACL's intellectual and data-rigor mandates without relying on automated tools, ensuring full compatibility with the Dataview schema.

### I. System & Data Initialization (Preconditions & Phase 1)

| **Step** | **Action / Mandate**                                                                                                                                   | **Compliance Check**                                               |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| **P-1**  | **Folder Check:** Verify the existence of the three required lifecycle folders.                                                                        | `_RACL_Staging/`, `03_Zettels/`, `99_Archive/` must be accessible. |
| **P-2**  | **Formulate Query:** Articulate the precise **Initial Research Query**.                                                                                | Query is clear, focused, and recorded.                             |
| **P-3**  | **Manual RAG Search:** Perform a deep associative search (e.g., Graph/Core Search) to identify at least  conceptually aligned source notes.            | At least five relevant vault notes are identified for context.     |
| **1.1**  | **Note Creation:** Create the `RACL Staging Note` in **`_RACL_Staging/`** and apply the `RACL-M Staging Template`.                                     | New note exists in staging folder.                                 |
| **1.2**  | **Log Sources (YAML):** Manually input the **`user_query`** and the **`rag_source`** links (`[[Note X]]`) for the selected notes into the frontmatter. | YAML contains the query and a list of explicit note links.         |

---

### II. Master Prompt & LLM Execution (Phase 2)

| **Step** | **Action / Mandate**                                                                                                                     | **Compliance Check**                                                                                             |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **2.1**  | **Extract Context:** Copy the raw text content of the manually logged `rag_source` notes.                                                | Full content of all notes is in a temporary buffer.                                                              |
| **2.2**  | **Assemble Prompt:** Construct the full **Master Prompt Template** by manually pasting the content into the **Section B (RAG Context)**. | Prompt includes the full 'Senior Academic Research Analyst' persona and the explicit output mandate (Section D). |
| **2.3**  | **Execute LLM:** Paste and execute the complete, assembled Master Prompt into the chosen LLM interface.                                  | LLM processing initiated; output is pending.                                                                     |

---

### III. Critical Analysis & Data Parsing (Phase 3 & 4)

|**Step**|**Action / Mandate**|**Compliance Check**|
|---|---|---|
|**3.1**|**CoT Validation:** Critically review the LLM's output, verifying the presence and intellectual coherence of the **RACL Reasoning Trace (C.1-C.3)**.|CoT is present and logical (no incoherence/rejection).|
|**3.2**|**Schema Validation:** Confirm the output contains a **single, clean YAML code block** (` ```yaml... ``` `).|Single, parsable YAML block is confirmed.|
|**3.3**|**Score Parsing (Temporary):** Copy the LLM's YAML block and **paste it temporarily** into the body of the `RACL Staging Note`.|YAML block inserted _immediately following_ the frontmatter.|
|**3.4**|**Update Frontmatter (Scores):** Manually extract `critique.score`, `critique.novelty`, and `critique.decomposability` and insert them into the **primary YAML frontmatter header**.|Nested `critique` fields in the header are updated with numerical/boolean data.|
|**3.5**|**Update Frontmatter (RAG Audit):** Manually extract the LLM's reported **`rag_source_used`** links and append them to the `rag_source` list in the frontmatter.|The `rag_source` list in the header now reflects LLM's utilized context.|
|**3.6**|**Clean-up:** **Delete** the temporary YAML code block from the note's body.|Only the frontmatter remains in the body, ensuring a clean audit.|
|**3.7**|**Update Status:** Manually update the frontmatter field: **`status: "Scored: Phase 4"`**.|Status field reflects successful scoring compliance.|

---

### IV. Zettel Creation & Synthesis (Phase 5, 6, 7 & 8)

| **Step** | **Action / Mandate**                                                                                                                                          | **Compliance Check**                                                          |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **4.1**  | **Extract Zettels:** Locate the **`zettel_decomposition`** list from the LLM's initial output.                                                                | All proposed Zettel items are identified.                                     |
| **4.2**  | **Create Atomic Notes:** For each Zettel item: manually create a new note in **`03_Zettels/`**, using the exact content of the `title:` and `content:         | ` fields.                                                                     |
| **4.3**  | **Enforce Lineage:** In the frontmatter of _each new Zettel_, manually add the mandatory link back to the source: `source: "[[Title of RACL Staging Note]]"`. | Every Zettel contains an auditable lineage link back to the parent RACL note. |
| **5.1**  | **Synthesis Review (P6):** Review all new Zettels and manually create **internal links (`[[]]`)** to MOCs, established concepts, or other notes.              | New Zettels are semantically embedded into the vault's network.               |
| **5.2**  | **Human Audit (P7):** Verify the `critique.score` against the rigor threshold. Plan for re-evaluation if the score is low.                                    | Intellectual quality assurance checkpoint completed.                          |
| **5.3**  | **Loop Closure (P8):** Manually update the `RACL Staging Note` status to **`status: "Archived"`**.                                                            | Status updated to final state.                                                |
| **5.4**  | **Archive:** Manually **move** the `RACL Staging Note` from **`_RACL_Staging/`** to **`99_Archive/`**.                                                        | Vault hygiene is achieved; the process is complete.                           |
