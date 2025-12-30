---
title: 📊 Table_R.A.C.L.-Phase-Alignment-with-(SOP_Prompt-Engineering-and-Curation)
aliases:
  - RACL SOP Mapping
  - RACL vs Reference SOP
  - Phase Alignment Table
tags:
  - workflow
  - pkb
  - prompt-engineering
status: 🌱 seedling
created: 2025-10-10T01:38:18.910Z
updated: 2025-10-10T01:42:19.760Z
source: "[[📙🧠report_r.a.g.-augmented-curation-loop-(r.a.c.l.)]]"
related:
  - "[[🚀proj-prompt-engineering-note]]"
  - "[[📙🧠report_r.a.g.-augmented-curation-loop-(r.a.c.l.)]]"
---


> [!the-purpose]
> The 8-Phase RACL workflow is structurally designed to incorporate the full intellectual rigor of the four core phases of the REFERENCE SOP (Retrieve/Refine, Examine/Evaluate, Fragment/Formulate, Establish/Embed). This alignment ensures that automation enhances, rather than diminishes, the scholarly quality of the curation process.

**📊 Table: RACL Phase Alignment with REFERENCE SOP**

|**REFERENCE SOP Phase**|**Intellectual Mandate**|**RACL Phase Alignment**|**Automation Mechanism**|
|---|---|---|---|
|**R**etrieve/Refine|Grounding the context|Phase 1: Semantic Retrieval (RAG)|Smart Connections|
|**E**xamine/Evaluate|Critical analysis and scoring|Phase 3: Critical Analysis (CoT)|Master Prompt Template (CoT block) 5|
|**F**ragment/Formulate|Decomposing into atomic units|Phase 5: Zettel Deconstruction|Templater Script (`tp.file.create_new`) 7|
|**E**stablish/Embed|Synthesis, linking, and archival|Phase 6, 7, 8: Review, Indexing, Closure|Dataview & QuickAdd Macro|
