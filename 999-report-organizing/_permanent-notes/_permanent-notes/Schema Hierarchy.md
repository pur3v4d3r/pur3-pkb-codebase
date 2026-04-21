---
title: "Schema Hierarchy"
aliases: []
type: permanent-note
status: evergreen
confidence: high
domain: cognitive-psychology
subdomains: []
tags: [permanent-note, cognitive-psychology]
created: '2026-04-21'
updated: '2026-04-21'
complexity: intermediate
importance: medium
review-frequency: quarterly
mastery-stage: seedling
provenance:
  source-type: report-extraction
  pipeline-version: "3.0.0"
  source-reports: [schema-and-how-they-work-deep-dive-2026-04-08, schema-and-how-they-work-deep-dive-2026-04-08_report]
  extraction-method: pkb-extractor-v1 → pipeline-v3
---

# Schema Hierarchy

> [!definition] Schema Hierarchy
> A schema hierarchy is the nested organization of schemas whereby higher-level schemas embed lower-level sub-schemas as components. The PHYSICIAN-VISIT schema embeds an EXAMINATION sub-schema, which itself embeds DIAGNOSTIC-REASONING sub-schemas. The RESTAURANT schema embeds ORDER-TAKING, FOOD-DELIVERY, and PAYMENT sub-schemas.
>
> **Properties of hierarchical embedding:**
> - A sub-schema can appear in multiple parent schemas (PAYMENT appears in both RESTAURANT and RETAIL-PURCHASE)
> - Higher-level schemas provide the *context* (instantiating values) that fill the slots in sub-schemas
> - Schema failure can occur at any level — the high-level schema can be correct while a sub-schema mis-activates
> - Schema automation occurs at the sub-schema level first, then propagates upward (early expertise is bottom-up sub-schema automation; expert fluency is top-level schema driving)

## Core Explanation

> [!evidence] Schema Hierarchy
> A schema hierarchy is the nested organization of schemas whereby higher-level schemas embed lower-level sub-schemas as components. The PHYSICIAN-VISIT schema embeds an EXAMINATION sub-schema, which itself embeds DIAGNOSTIC-REASONING sub-schemas. The RESTAURANT schema embeds ORDER-TAKING, FOOD-DELIVERY, and PAYMENT sub-schemas.
>
> **Properties of hierarchical embedding:**
> - A sub-schema can appear in multiple parent schemas (PAYMENT appears in both RESTAURANT and RETAIL-PURCHASE)
> - Higher-level schemas provide the *context* (instantiating values) that fill the slots in sub-schemas
> - Schema failure can occur at any level — the high-level schema can be correct while a sub-schema mis-activates
> - Schema automation occurs at the sub-schema level first, then propagates upward (early expertise is bottom-up sub-schema automation; expert fluency is top-level schema driving)
> *— [[schema-and-how-they-work-deep-dive-2026-04-08_report]]*

> [!evidence] Schema Hierarchy
> The multi-level nested organization of schemas whereby higher-level schemas embed lower-level sub-schemas as components. Sub-schemas can be shared across multiple parent schemas. Automation proceeds from lower-level sub-schemas upward. Schema failure can occur at any hierarchical level: the macro-level schema can be correctly activated while a sub-schema misfires, or a sub-schema gap can prevent a macro-level schema from being successfully instantiated.
> *— [[schema-and-how-they-work-deep-dive-2026-04-08_report]]*

> [!evidence] Schema Hierarchy
> A schema hierarchy is the nested organization of schemas whereby higher-level schemas embed lower-level sub-schemas as components. The PHYSICIAN-VISIT schema embeds an EXAMINATION sub-schema, which itself embeds DIAGNOSTIC-REASONING sub-schemas. The RESTAURANT schema embeds ORDER-TAKING, FOOD-DELIVERY, and PAYMENT sub-schemas.
>
> **Properties of hierarchical embedding:**
> - A sub-schema can appear in multiple parent schemas (PAYMENT appears in both RESTAURANT and RETAIL-PURCHASE)
> - Higher-level schemas provide the *context* (instantiating values) that fill the slots in sub-schemas
> - Schema failure can occur at any level — the high-level schema can be correct while a sub-schema mis-activates
> - Schema automation occurs at the sub-schema level first, then propagates upward (early expertise is bottom-up sub-schema automation; expert fluency is top-level schema driving)
> *— [[schema-and-how-they-work-deep-dive-2026-04-08]]*

> [!evidence] Schema Hierarchy
> The multi-level nested organization of schemas whereby higher-level schemas embed lower-level sub-schemas as components. Sub-schemas can be shared across multiple parent schemas. Automation proceeds from lower-level sub-schemas upward. Schema failure can occur at any hierarchical level: the macro-level schema can be correctly activated while a sub-schema misfires, or a sub-schema gap can prevent a macro-level schema from being successfully instantiated.
> *— [[schema-and-how-they-work-deep-dive-2026-04-08]]*

## Connections

**Related:** [[AI-Tutoring-Systems]] · [[Accretion,-Tuning,-Restructuring]] · [[Anchoring-Bias]] · [[Assimilation,-Accommodation,-and-Equilibration]] · [[Assimilation-Accommodation]] · [[Attractor-Networks-Hopfield]] · [[Bartlett's-Reconstructive-Memory-Experiments]] · [[Comprehension-Schema-Theory]] · [[Constraint-Satisfaction]] · [[Cultural-Psychology]] · [[Cultural-Transmission]] · [[David-Rumelhart]] · [[Default-Values-Schemas]] · [[Free-Energy-Principle]] · [[Hippocampal-Neocortical-Transfer]] · [[Inference-Generation]] · [[Knowledge-Neurons]] · [[Markus-Kitayama-Self-Construal]] · [[Meme-Theory]] · [[PKM-Personal-Knowledge-Management]] · [[Piaget-Equilibration]] · [[Predictive-Processing-Framework]] · [[Prototype-Theory]] · [[Schema-Automation-and-Fluency-Development]] · [[Schema-Change-Modes]] · [[Schema-Construction-Problem-—-Original-Analytical-Insight]] · [[Schema-Intrusion-Errors]] · [[Schema-Theory-Bartlett,-Rumelhart]] · [[Scripts-Schank-Abelson]] · [[Semantic-Memory-Categorical-Organization]] · [[Skill-Acquisition-Three-Stage-Model]] · [[Sleep-Memory-Consolidation]] · [[Symbolic-AI-Representations]] · [[Top-Down-Bottom-Up-Processing]] · [[Transformer-Architecture-Attention-Mechanism]] · [[Trauma-Memory]] · [[Von-Restorff-Isolation-Effect]] · [[active-inference]] · [[assimilation]] · [[assimilation-and-accommodation]] · [[bartlett]] · [[bottom-up-processing]] · [[cognitive-load-theory]] · [[conceptual-change-theory-and-schema-restructuring]] · [[confirmation-bias]] · [[declarative-schemas]] · [[elaborative-inference]] · [[embodied-cognition]] · [[episodic-memory]] · [[equilibration]] · [[expert-blind-spot]] · [[expert-blindness]] · [[expertise]] · [[germane-cognitive-load]] · [[hippocampus]] · [[knowledge-representation]] · [[long-term-memory]] · [[mental-models]] · [[parallel-distributed-processing]] · [[pragmatic-reasoning-schemas]] · [[prediction-error]] · [[predictive-processing]] · [[priming]] · [[prior-knowledge-activation]] · [[procedural-schemas]] · [[reconstructive-memory]] · [[schema-accommodation]] · [[schema-attractor]] · [[schema-crystallization-event]] · [[schema-hierarchy]] · [[schema-theory]] · [[schema-theory-and-learning]] · [[semantic-memory]] · [[spaced-repetition]] · [[spreading-activation]] · [[synaptic-consolidation]] · [[tacit-knowledge]] · [[transfer-of-learning]] · [[working-memory]]

```dataview
LIST FROM [[Schema Hierarchy]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[schema-and-how-they-work-deep-dive-2026-04-08]] · [[schema-and-how-they-work-deep-dive-2026-04-08_report]]
