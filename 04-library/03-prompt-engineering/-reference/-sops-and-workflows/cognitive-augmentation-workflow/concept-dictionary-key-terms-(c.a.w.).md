---
title: Concept-Dictionary_Key Terms_(C.A.W.)
aliases:
  - "Concept Dictionary: Key Terms for Cognitive Augmentation"
  - CAG Key Terms
  - Cognitive Augmentation Glossary
  - Workflow Terminology Reference
tags:
  - prompt-engineering
  - type/reference
  - pkm
status: 🪴 seedling
created: 2025-10-09T05:56:45.273Z
updated: 2025-10-09T05:58:14.714Z
source: "[Gemini-2.5-Flash]"
related:
  - "[[🚀proj-prompt-engineering-note]]"
  - "[[report_the-cognitive-augmentation-workflow_(c.a.w.)]]"
date created: 2025-10-09T01:56:45.000-04:00
date modified: 2025-10-10T00:20:31.103-04:00
---

# Concept Dictionary: Key Terms for Cognitive Augmentation

> [!the-purpose]
> This note defines the specialized vocabulary introduced by the workflow. It ensures that you and your system have a consistent, rigorous understanding of the _why_ behind the critical components.

|Concept Name|Definition & Purpose (The WHY)|Key Metadata Link|
|---|---|---|
|**Semantic Density (SD)**|The quantitative metric for **evidential depth** and reliability. It is a confidence score grounded in semantic analysis, overcoming the limits of simple coherence scores. **WHY:** It acts as the primary Personal Knowledge Base Gatekeeper for rigor.|`semantic_density`|
|**Agentic Meta-Prompting Framework (AMP-F)**|A layered, structured prompting system using **System, Conductor, and Expert roles**. **WHY:** It enforces complex scholarly constraints and transitions generation from a monolithic prompt to a controlled, multi-agent process.|`ai_source_model`, `data_provenance_method`|
|**Tree-of-Thoughts (ToT)**|A reasoning strategy that forces the LLM to generate, evaluate, and search multiple _branching_ thoughts. **WHY:** It guarantees exploration, proactively generates counter-arguments, and mitigates biases by preventing linear reinforcement.|(Linked to AMP-F process)|
|**Metadata Trust Ledger**|The collective set of prescriptive YAML fields that actively encodes the provenance, quality, and reliability of the generated note. **WHY:** It transforms the Personal Knowledge Base from a passive file organizer into an active **Risk-Management Tool**.|All Phase I Metadata|
|**Contradiction Management System (CMS)**|The architectural necessity to _allow_ for, generate, and explicitly label notes that capture opposing or conflicting arguments. **WHY:** True intellectual depth requires **dialectic reasoning**—the ability to understand and reconcile competing theories, not just eliminate them.|`is_contradictory`|
|**Citation Rigor Protocol**|The mandatory, three-step verification process (LLM-based, automated, **human audit**) for all cited claims. **WHY:** It directly combats the single greatest threat to scholarly utility: citation hallucination.|`citation_check_status`|
