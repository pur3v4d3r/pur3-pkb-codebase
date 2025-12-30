---
title: SOP_Prompting_Inside-PKB_Manually_(R.A.C.L.)
aliases:
  - RACL-M SOP
  - Manual RACL Procedure
  - Offline Knowledge Curation
tags:
  - workflow
  - pkb
status: seedling 🌱
created: 2025-10-10T03:35:24.393Z
updated: 2025-10-10T03:50:28.198Z
source: "[[📙🧠report_r.a.g.-augmented-curation-loop-(r.a.c.l.)]]"
related:
  - "[[🚀proj-prompt-engineering-note]]"
  - "[[📙🧠report_r.a.g.-augmented-curation-loop-(r.a.c.l.)]]"
  - "[[checklist_sop_(r.a.c.l)]]"
  - "[[checklist_workflow_(r.a.c.l.-m.)]]"
---



## Manual Standard Operating Procedure (SOP): The RACL-M

> [!the-purpose]
> - This SOP, the **RAG-Augmented Curation Loop - Manual (RACL-M)**, is designed to replicate the intellectual and data rigor of the RACL without reliance on QuickAdd, Templater, or the Smart Chat command structure. Its primary goal is to ensure that even under system failure, the output assets are fully compatible with the automated RACL's Dataview schema for eventual auditing and indexing.

### Preconditions and System Readiness (Manual Check)

  * **Required Folders:** Ensure the following folders exist and are accessible: `_RACL_Staging`, `03_Zettels`, and `99_Archive`.
  * **Tools:** Access to a text editor (Obsidian is preferred for linking, but a plain editor suffices for initial drafting) and a functional LLM (Web access, API-only, or local executable).
  * **Templates:** A simplified `RACL-M Staging Template` must exist to initialize the YAML frontmatter.

### Phase 1: Manual Contextual Grounding (RAG-M Mandate)

**Intellectual Mandate:** Fulfill the **Retrieve/Refine** phase by manually grounding the LLM's analysis within the existing knowledge corpus.

1.  **Formulate Query:** Articulate the precise, high-level **Initial Research Query** (e.g., "How does Foucault's concept of 'Discipline' intersect with modern data privacy frameworks?").
2.  **Manual Associative Search:** Perform a deep semantic search across your vault using Obsidian's core search, the Graph View, or manual browsing of MOCs.
      * **Goal:** Identify $\text{N} \ge 5$ of the most relevant, conceptually aligned notes that directly address or contextualize the query.
3.  **Log RAG Sources:** Create a new note in the `_RACL_Staging` folder named using the query title.
4.  **Initialize YAML (Template):** Apply the `RACL-M Staging Template` and manually input the captured information:

<!-- end list -->

```yaml
---
user_query: "[The full text of the Initial Research Query]"
review_date: "[2025-11-21 or Today's Date]"
status: "Draft: Phase 2"
critique:
  score: 0.0 # Placeholder
  novelty: 0 # Placeholder
  decomposability: false # Placeholder
rag_source: # Manual input of the selected links
  - "[[Link to Note 1]]"
  - "[[Link to Note 2]]"
  - "[[...]]"
---
```

### Phase 2: Master Prompt Construction and LLM Input

**Intellectual Mandate:** Prepare the LLM with the full intellectual burden of the RACL architecture.

1.  **Extract Context:** Copy the raw text content of the identified `rag_source` notes into a temporary text buffer.
2.  **Assemble Master Prompt:** Construct the full **Master Prompt Template** for the LLM.
      * **Section A (System Instruction):** The full 'Senior Academic Research Analyst' persona.
      * **Section B (RAG Context):** Paste the content of the copied `rag_source` notes here.
      * **Section D (Structured Output Mandate):** Include the full, blank YAML schema, exactly as specified in the RACL reference, using the literal block style (`|`) for Zettel content.
3.  **Execute LLM:** Paste the complete, assembled Master Prompt into the LLM interface (e.g., ChatGPT, Claude, etc.) and execute.

### Phase 3: Critical Analysis and Decomposition (Manual Parsing)

**Intellectual Mandate:** Fulfill the **Examine/Evaluate (E)** and **Fragment/Formulate (F)** phases and manually validate the structured output.

1.  **Output Review:** Critically review the LLM's output against the Master Prompt.
      * **Validation Check 1 (CoT):** Verify the presence and intellectual coherence of the **RACL Reasoning Trace (C.1-C.3)**. *If the CoT is absent or incoherent, reject the output and re-run Phase 2.*
      * **Validation Check 2 (Schema):** Confirm the output contains a *single, clean* YAML code block (` ```yaml... ``` `).
2.  **Manual Score Parsing (Phase 4):**
      * Copy the YAML code block from the LLM's response.
      * Paste the copied block *immediately following* the existing YAML frontmatter in the `RACL Staging Note`. This is a temporary insertion.
      * **Update Frontmatter:** Manually extract the nested scores from the temporary block and update the primary frontmatter fields:
          * Extract `critique.score`, `critique.novelty`, and `critique.decomposability` and insert them into the existing YAML header.
          * **Crucially:** Extract and confirm the `rag_source_used` links reported by the LLM and add them to the `rag_source` list in the frontmatter.
      * Delete the temporary YAML code block from the body of the note.
3.  **Update Status:** Change the frontmatter status: `status: "Scored: Phase 4"`.

### Phase 4: Zettel Deconstruction and Linking (Manual Zettelizer)

**Intellectual Mandate:** Fulfill the **Establish/Embed** phase by creating atomic notes and guaranteeing intellectual lineage.

1.  **Extract Zettel Decomposition:** Go back to the LLM's output and locate the `zettel_decomposition` list.
2.  **Create Atomic Notes:** For each item (`- id: Zettel X...`) in the list:
      * Manually create a **New Note** in the `03_Zettels` folder.
      * Title the new note with the exact content of the `title:` field.
      * Paste the content of the `content: |` field into the body of the new note.
      * **Enforce Lineage Linkage:** In the new Zettel's frontmatter, manually add the link back to the source:

<!-- end list -->

```yaml
---
source: "[[Title of RACL Staging Note]]"
---
```

### Phase 5: Contextual Review, Synthesis, and Archival (Closure)

**Intellectual Mandate:** Replicate the human intervention and vault hygiene phases.

1.  **Contextual Review (Phase 6):**
      * Review the newly created Zettels in `03_Zettels`.
      * Manually create **internal links** (`[[]]`) from the new Zettels to existing notes, MOCs, or other relevant conceptual territories. This is the synthesis step.
2.  **Audit and Indexing (Phase 7):**
      * As a human audit, verify that the `critique.score` in the RACL Staging Note's frontmatter is acceptable (e.g., $\ge 0.7$). If not, plan for re-evaluation.
3.  **Loop Closure (Phase 8):**
      * In the `RACL Staging Note`, update the frontmatter: `status: "Archived"`.
      * Move the `RACL Staging Note` from `_RACL_Staging/` to the final `99_Archive/` folder.

This RACL-M SOP ensures that even when the automation is broken, the core **intellectual rigor** and the **integrity of the structured metadata** are preserved. When your systems are back online, all manually processed notes will seamlessly integrate with your existing Dataview audit and indexing queries.