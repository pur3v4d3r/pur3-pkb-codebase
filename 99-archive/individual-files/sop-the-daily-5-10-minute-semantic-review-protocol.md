---
title: SOP_The Daily 5-10 Minute Semantic Review Protocol
aliases:
  - AI-Assisted Linking Routine
  - Daily Semantic Review
  - Semantic Review Protocol
tags:
  - type/report/psychology
  - pkm
  - pkb/plugin/smart-connections
status: seedling 🌱
created: 2025-10-10T07:10:17.230Z
updated: 2025-10-10T07:12:06.321Z
source: "[[📙🧠Report_Prompting_Inside-the-PKB]]"
related:
  - "[[📙🧠Report_Prompting_Inside-the-PKB]]"
  - "[[🚀proj-prompt-engineering-note]]"
date created: 2025-10-10T03:10:17.000-04:00
date modified: 2025-10-10T03:13:53.663-04:00
---

# SOP_The Daily 5-10 Minute Semantic Review Protocol

> [!the-mission]
> The core objective of the daily protocol is to leverage semantic search to proactively identify latent connections and potential note redundancies.

**Pre-Condition:** The user must ensure that the Smart Connections configuration is set to Profile A (High Precision Threshold, Low Retrieval Count ![](data:,)) for focused results.

**Step 1: Capture and Passive Indexing.** The routine begins with the capture of information, whether writing a new permanent note or processing items from the 'Inbox' folder.13 Upon saving, the Smart Connections plugin automatically indexes this new material using the local AI.1

**Step 2: Proactive Linking and Distillation.** The user opens the Connections pane for the newest note. Because the similarity threshold is high (0.96+), the system displays only the most highly relevant semantic neighbors. This shifts the daily task from the stressful, time-consuming hunt for links 5 to a quick, guided validation. The consistency enforced by this automation reinforces the Zettelkasten principle of interconnectedness without high cognitive overhead, fulfilling the goal of making PKM easier to maintain.4

- **Action A (Refinement):** If a highly relevant connection is identified but lacks an explicit link, the user creates a formal link (`[]`) within the note text, formalizing the relationship identified by the AI.
    
- **Action B (Consolidation):** If a connection exhibits extreme similarity (scores near 1.0), it suggests semantic overlap or redundancy. The user should consolidate the new material into the older, more established note, thereby strengthening the knowledge base and improving fidelity.
    
