---
title: Table_Smart-Connections-Integration-Matrix_(C.O.D.E.-Framework)
aliases:
  - "Smart Connections Integration Matrix: C.O.D.E. Framework"
  - CODE Framework Integration
  - PKM Integration Table
  - Smart Connections Matrix
tags:
  - pkb/plugin/smart-connections
status: seedling 🌱
created: 2025-10-10T07:15:59.625Z
updated: 2025-10-10T07:16:53.914Z
source: "[[📙🧠Report_Prompting_Inside-the-PKB]]"
related:
  - "[[📙🧠Report_Prompting_Inside-the-PKB]]"
  - "[[🚀proj-prompt-engineering-note]]"
date created: 2025-10-10T03:15:59.000-04:00
date modified: 2025-10-10T03:17:17.922-04:00
---

# Smart Connections Integration Matrix: C.O.D.E. Framework

| **PKM Stage (CODE)** | **Primary Goal**                                 | **Smart Connections (SC) Integration Point**                                            | **Local LLM Action/Task**                                                                                         |
| -------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **C**apture          | Rapid, reliable note entry.13                    | SC auto-indexes new note upon saving (passive operation).1                              | N/A (Focus is on recording data).                                                                                 |
| **O**rganize         | Structural linking, classification (PARA/MOC).14 | SC Connections Pane surfaces semantic neighbors to inform manual linking decisions.4    | Draft MOC outlines or suggest PARA classification links based on retrieved context clusters.                      |
| **D**istill          | Synthesis, critical reflection, summarization.   | SC Search View performs highly specific RAG retrieval (Context Assembly).8              | Abstractive summarization and conceptual comparison of multiple retrieved notes.2                                 |
| **E**xpress          | Output generation (reports, drafts, papers).     | SC provides on-demand contextual support during writing/drafting using the Search View. | Context-Constrained Knowledge Synthesis (CCKS) to generate structured paragraphs based ONLY on vault knowledge.15 |
