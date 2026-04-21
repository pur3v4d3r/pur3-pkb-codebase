---
title: "Technical Detail: Prediction Error and Mode Selection"
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

# Technical Detail: Prediction Error and Mode Selection

> [!definition] Technical Detail: Prediction Error and Mode Selection
> *Definition pending — derived from 2 source report(s).*

## Core Explanation

> [!evidence] Technical Detail: Prediction Error and Mode Selection
> The activated schema generates predictions about what should be present, in what configuration, with what probability. Comparing these predictions to actual input generates a prediction error signal. The mode of schema change triggered depends on the *profile* of prediction errors:
>
> - **Small, distributed prediction errors** (the input matches the schema overall, with minor deviations): Trigger **accretion** — new data points are registered within the existing framework
> - **Consistent directional errors in specific slots** (the schema is systematically wrong about specific parameter values): Trigger **tuning** — the parameter values are updated toward the actual distribution
> - **Catastrophic failure** (the schema generates predictions that are comprehensively wrong, the input cannot be parsed by any available sub-schema): Trigger restructuring attempts — but ONLY IF the failure is recognized and salient enough to motivate repair
>
> **The detection threshold for restructuring:** The failure mode for conceptual change is that catastrophic schema failure is NOT recognized as requiring restructuring. The learner may:
> - Dismiss anomalous data as error ("the experiment must have been done wrong")
> - Apply non-central modifications that preserve the schema's core (adding epicycles — a tuning response to restructuring-level error)
> - Switch to task-performance mode without updating the schema (solving the problem correctly via procedure without understanding why — the "bright student" syndrome)
>
> **The role of metacognition:** Recognizing when prediction errors indicate genuine schema failure (vs. acceptable noise) is itself a metacognitive skill that varies across individuals and expertise levels. Less expert learners have less calibrated sense of when their schema is genuinely failing vs. when the task is just harder than expected.
> *— [[schema-and-how-they-work-deep-dive-2026-04-08_report]]*

> [!evidence] Technical Detail: Prediction Error and Mode Selection
> The activated schema generates predictions about what should be present, in what configuration, with what probability. Comparing these predictions to actual input generates a prediction error signal. The mode of schema change triggered depends on the *profile* of prediction errors:
>
> - **Small, distributed prediction errors** (the input matches the schema overall, with minor deviations): Trigger **accretion** — new data points are registered within the existing framework
> - **Consistent directional errors in specific slots** (the schema is systematically wrong about specific parameter values): Trigger **tuning** — the parameter values are updated toward the actual distribution
> - **Catastrophic failure** (the schema generates predictions that are comprehensively wrong, the input cannot be parsed by any available sub-schema): Trigger restructuring attempts — but ONLY IF the failure is recognized and salient enough to motivate repair
>
> **The detection threshold for restructuring:** The failure mode for conceptual change is that catastrophic schema failure is NOT recognized as requiring restructuring. The learner may:
> - Dismiss anomalous data as error ("the experiment must have been done wrong")
> - Apply non-central modifications that preserve the schema's core (adding epicycles — a tuning response to restructuring-level error)
> - Switch to task-performance mode without updating the schema (solving the problem correctly via procedure without understanding why — the "bright student" syndrome)
>
> **The role of metacognition:** Recognizing when prediction errors indicate genuine schema failure (vs. acceptable noise) is itself a metacognitive skill that varies across individuals and expertise levels. Less expert learners have less calibrated sense of when their schema is genuinely failing vs. when the task is just harder than expected.
> *— [[schema-and-how-they-work-deep-dive-2026-04-08]]*

## Connections

**Related:** [[AI-Tutoring-Systems]] · [[Accretion,-Tuning,-Restructuring]] · [[Anchoring-Bias]] · [[Assimilation,-Accommodation,-and-Equilibration]] · [[Assimilation-Accommodation]] · [[Attractor-Networks-Hopfield]] · [[Bartlett's-Reconstructive-Memory-Experiments]] · [[Comprehension-Schema-Theory]] · [[Constraint-Satisfaction]] · [[Cultural-Psychology]] · [[Cultural-Transmission]] · [[David-Rumelhart]] · [[Default-Values-Schemas]] · [[Free-Energy-Principle]] · [[Hippocampal-Neocortical-Transfer]] · [[Inference-Generation]] · [[Knowledge-Neurons]] · [[Markus-Kitayama-Self-Construal]] · [[Meme-Theory]] · [[PKM-Personal-Knowledge-Management]] · [[Piaget-Equilibration]] · [[Predictive-Processing-Framework]] · [[Prototype-Theory]] · [[Schema-Automation-and-Fluency-Development]] · [[Schema-Change-Modes]] · [[Schema-Construction-Problem-—-Original-Analytical-Insight]] · [[Schema-Intrusion-Errors]] · [[Schema-Theory-Bartlett,-Rumelhart]] · [[Scripts-Schank-Abelson]] · [[Semantic-Memory-Categorical-Organization]] · [[Skill-Acquisition-Three-Stage-Model]] · [[Sleep-Memory-Consolidation]] · [[Symbolic-AI-Representations]] · [[Top-Down-Bottom-Up-Processing]] · [[Transformer-Architecture-Attention-Mechanism]] · [[Trauma-Memory]] · [[Von-Restorff-Isolation-Effect]] · [[active-inference]] · [[assimilation]] · [[assimilation-and-accommodation]] · [[bartlett]] · [[bottom-up-processing]] · [[cognitive-load-theory]] · [[conceptual-change-theory-and-schema-restructuring]] · [[confirmation-bias]] · [[declarative-schemas]] · [[elaborative-inference]] · [[embodied-cognition]] · [[episodic-memory]] · [[equilibration]] · [[expert-blind-spot]] · [[expert-blindness]] · [[expertise]] · [[germane-cognitive-load]] · [[hippocampus]] · [[knowledge-representation]] · [[long-term-memory]] · [[mental-models]] · [[parallel-distributed-processing]] · [[pragmatic-reasoning-schemas]] · [[prediction-error]] · [[predictive-processing]] · [[priming]] · [[prior-knowledge-activation]] · [[procedural-schemas]] · [[reconstructive-memory]] · [[schema-accommodation]] · [[schema-attractor]] · [[schema-crystallization-event]] · [[schema-hierarchy]] · [[schema-theory]] · [[schema-theory-and-learning]] · [[semantic-memory]] · [[spaced-repetition]] · [[spreading-activation]] · [[synaptic-consolidation]] · [[tacit-knowledge]] · [[transfer-of-learning]] · [[working-memory]]

```dataview
LIST FROM [[Technical Detail Prediction Error and Mode Selection]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[schema-and-how-they-work-deep-dive-2026-04-08]] · [[schema-and-how-they-work-deep-dive-2026-04-08_report]]
