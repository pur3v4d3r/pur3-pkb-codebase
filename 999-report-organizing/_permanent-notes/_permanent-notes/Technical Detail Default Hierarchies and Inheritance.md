---
title: "Technical Detail: Default Hierarchies and Inheritance"
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

# Technical Detail: Default Hierarchies and Inheritance

> [!definition] Technical Detail: Default Hierarchies and Inheritance
> *Definition pending — derived from 2 source report(s).*

## Core Explanation

> [!evidence] Technical Detail: Default Hierarchies and Inheritance
> Default value assignment operates through a **default hierarchy** with inheritance. Consider the BIRD schema:
> - BIRD has default: LOCOMOTION = FLIES
> - ROBIN inherits from BIRD, so ROBIN also defaults: LOCOMOTION = FLIES
> - PENGUIN overrides the BIRD default: LOCOMOTION = SWIMS (not flies)
>
> This inheritance structure — with override capability at the more specific level — is what makes schemas flexible. You don't have to store the full specification for every instance; instead, you store the prototype (the generic schema) and inherit from it, noting only the deviations. This is computationally efficient: the representation space required is proportional to how much each instance deviates from the prototype, not to the total number of features.
>
> **The default-override distinction matters for memory:** When you experience a PENGUIN, you activate BIRD (inheriting most defaults), but override the LOCOMOTION default. At recall, there's a systematic tendency to "forget" the override and remember the default — to "remember" the penguin flew, reverting to the inherited default rather than the stored override. This is one mechanism behind the [[reconstructive-memory]] phenomenon documented by Bartlett.
> *— [[schema-and-how-they-work-deep-dive-2026-04-08_report]]*

> [!evidence] Technical Detail: Default Hierarchies and Inheritance
> Default value assignment operates through a **default hierarchy** with inheritance. Consider the BIRD schema:
> - BIRD has default: LOCOMOTION = FLIES
> - ROBIN inherits from BIRD, so ROBIN also defaults: LOCOMOTION = FLIES
> - PENGUIN overrides the BIRD default: LOCOMOTION = SWIMS (not flies)
>
> This inheritance structure — with override capability at the more specific level — is what makes schemas flexible. You don't have to store the full specification for every instance; instead, you store the prototype (the generic schema) and inherit from it, noting only the deviations. This is computationally efficient: the representation space required is proportional to how much each instance deviates from the prototype, not to the total number of features.
>
> **The default-override distinction matters for memory:** When you experience a PENGUIN, you activate BIRD (inheriting most defaults), but override the LOCOMOTION default. At recall, there's a systematic tendency to "forget" the override and remember the default — to "remember" the penguin flew, reverting to the inherited default rather than the stored override. This is one mechanism behind the [[reconstructive-memory]] phenomenon documented by Bartlett.
> *— [[schema-and-how-they-work-deep-dive-2026-04-08]]*

## Connections

**Related:** [[AI-Tutoring-Systems]] · [[Accretion,-Tuning,-Restructuring]] · [[Anchoring-Bias]] · [[Assimilation,-Accommodation,-and-Equilibration]] · [[Assimilation-Accommodation]] · [[Attractor-Networks-Hopfield]] · [[Bartlett's-Reconstructive-Memory-Experiments]] · [[Comprehension-Schema-Theory]] · [[Constraint-Satisfaction]] · [[Cultural-Psychology]] · [[Cultural-Transmission]] · [[David-Rumelhart]] · [[Default-Values-Schemas]] · [[Free-Energy-Principle]] · [[Hippocampal-Neocortical-Transfer]] · [[Inference-Generation]] · [[Knowledge-Neurons]] · [[Markus-Kitayama-Self-Construal]] · [[Meme-Theory]] · [[PKM-Personal-Knowledge-Management]] · [[Piaget-Equilibration]] · [[Predictive-Processing-Framework]] · [[Prototype-Theory]] · [[Schema-Automation-and-Fluency-Development]] · [[Schema-Change-Modes]] · [[Schema-Construction-Problem-—-Original-Analytical-Insight]] · [[Schema-Intrusion-Errors]] · [[Schema-Theory-Bartlett,-Rumelhart]] · [[Scripts-Schank-Abelson]] · [[Semantic-Memory-Categorical-Organization]] · [[Skill-Acquisition-Three-Stage-Model]] · [[Sleep-Memory-Consolidation]] · [[Symbolic-AI-Representations]] · [[Top-Down-Bottom-Up-Processing]] · [[Transformer-Architecture-Attention-Mechanism]] · [[Trauma-Memory]] · [[Von-Restorff-Isolation-Effect]] · [[active-inference]] · [[assimilation]] · [[assimilation-and-accommodation]] · [[bartlett]] · [[bottom-up-processing]] · [[cognitive-load-theory]] · [[conceptual-change-theory-and-schema-restructuring]] · [[confirmation-bias]] · [[declarative-schemas]] · [[elaborative-inference]] · [[embodied-cognition]] · [[episodic-memory]] · [[equilibration]] · [[expert-blind-spot]] · [[expert-blindness]] · [[expertise]] · [[germane-cognitive-load]] · [[hippocampus]] · [[knowledge-representation]] · [[long-term-memory]] · [[mental-models]] · [[parallel-distributed-processing]] · [[pragmatic-reasoning-schemas]] · [[prediction-error]] · [[predictive-processing]] · [[priming]] · [[prior-knowledge-activation]] · [[procedural-schemas]] · [[reconstructive-memory]] · [[schema-accommodation]] · [[schema-attractor]] · [[schema-crystallization-event]] · [[schema-hierarchy]] · [[schema-theory]] · [[schema-theory-and-learning]] · [[semantic-memory]] · [[spaced-repetition]] · [[spreading-activation]] · [[synaptic-consolidation]] · [[tacit-knowledge]] · [[transfer-of-learning]] · [[working-memory]]

```dataview
LIST FROM [[Technical Detail Default Hierarchies and Inheritance]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[schema-and-how-they-work-deep-dive-2026-04-08]] · [[schema-and-how-they-work-deep-dive-2026-04-08_report]]
