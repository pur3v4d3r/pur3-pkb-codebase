---
title: "Technical Detail: SDT Formalization of Monitoring"
aliases: []
type: permanent-note
status: evergreen
confidence: high
domain: unknown
subdomains: []
tags: [permanent-note, unknown]
created: '2026-04-21'
updated: '2026-04-21'
complexity: intermediate
importance: medium
review-frequency: quarterly
mastery-stage: seedling
provenance:
  source-type: report-extraction
  pipeline-version: "3.0.0"
  source-reports: [metacognitive-monitoring-accuracy-calibration-deep-dive-2026-04-12, metacognitive-monitoring-accuracy-calibration-deep-dive-2026-04-12_report]
  extraction-method: pkb-extractor-v1 → pipeline-v3
---

# Technical Detail: SDT Formalization of Monitoring

> [!definition] Technical Detail: SDT Formalization of Monitoring
> *Definition pending — derived from 2 source report(s).*

## Core Explanation

> [!evidence] Technical Detail: SDT Formalization of Monitoring
> In the SDT framework, each item generates an internal signal strength (e.g., retrieval fluency). Learned items produce a signal distribution with mean $\mu_L$ and variance $\sigma^2$, while not-learned items produce a distribution with mean $\mu_{NL}$ and variance $\sigma^2$. Monitoring accuracy corresponds to the discriminability parameter $d' = \frac{\mu_L - \mu_{NL}}{\sigma}$.
>
> The learner sets a criterion $c$ on the signal dimension: items above criterion receive "learned" judgments, items below receive "not learned." Calibration is then the joint product of discriminability ($d'$) and criterion placement.
>
> **What this buys:** The SDT framework separates monitoring accuracy into two independent components — sensitivity (the ability to discriminate learned from unlearned items, captured by $d'$) and response bias (the tendency to over- or under-report learning, captured by $c$). This separation is theoretically critical because interventions that improve monitoring sensitivity are fundamentally different from interventions that shift response bias.
>
> **Precision:** This is a schematic framework — the specific signal distributions, the dimensionality of the signal space, and the decision rule are all active areas of investigation.
> **Dependencies:** Assumes familiarity with basic SDT; see [[Signal-Detection|signal detection theory]] for foundations.
> *— [[metacognitive-monitoring-accuracy-calibration-deep-dive-2026-04-12_report]]*

> [!evidence] Technical Detail: SDT Formalization of Monitoring
> In the SDT framework, each item generates an internal signal strength (e.g., retrieval fluency). Learned items produce a signal distribution with mean $\mu_L$ and variance $\sigma^2$, while not-learned items produce a distribution with mean $\mu_{NL}$ and variance $\sigma^2$. Monitoring accuracy corresponds to the discriminability parameter $d' = \frac{\mu_L - \mu_{NL}}{\sigma}$.
>
> The learner sets a criterion $c$ on the signal dimension: items above criterion receive "learned" judgments, items below receive "not learned." Calibration is then the joint product of discriminability ($d'$) and criterion placement.
>
> **What this buys:** The SDT framework separates monitoring accuracy into two independent components — sensitivity (the ability to discriminate learned from unlearned items, captured by $d'$) and response bias (the tendency to over- or under-report learning, captured by $c$). This separation is theoretically critical because interventions that improve monitoring sensitivity are fundamentally different from interventions that shift response bias.
>
> **Precision:** This is a schematic framework — the specific signal distributions, the dimensionality of the signal space, and the decision rule are all active areas of investigation.
> **Dependencies:** Assumes familiarity with basic SDT; see [[Signal-Detection|signal detection theory]] for foundations.
> *— [[metacognitive-monitoring-accuracy-calibration-deep-dive-2026-04-12]]*

## Connections

**Related:** [[Algorithmic-Metacognition-—-When-Spaced-Repetition-Systems-Do-Metacognitive-Work]] · [[Cognitive-Reflection-Test-and-Rationality-Quotient]] · [[Computational-Modeling-of-Metacognitive-Control-uses-cognitive-architectures-lik]] · [[Desirable-Difficulties]] · [[Metacognitive-Feelings-Affect,-Fluency,-and-Learning-Judgments]] · [[Metacognitive-Monitoring-Accuracy-and-Calibration]] · [[Metacognitive-Transfer-—-Does-PKB-Monitoring-Skill-Generalize-Across-Domains]] · [[Monitoring-Regulation-Decoupling]] · [[Nelson-Narens-Model]] · [[Self-Regulated-Learning-as-a-Resource-Allocation-Problem-Under-Uncertainty]] · [[Signal-Detection]] · [[bayesian-inference]] · [[calibration]] · [[cognitive-architecture]] · [[cognitive-biases]] · [[cognitive-forcing-functions]] · [[cognitive-load-theory]] · [[cognitive-psychology-foundations]] · [[comprehension-monitoring]] · [[conditional-metacognitive-knowledge]] · [[critical-thinking-as-metacognitively-regulated-reasoning]] · [[declarative-memory]] · [[declarative-metacognitive-knowledge]] · [[deep-processing]] · [[deliberate-practice]] · [[desirable-difficulties]] · [[dunning-kruger-effect]] · [[epistemic-calibration]] · [[feeling-of-knowing]] · [[intellectual-humility]] · [[judgment-of-learning]] · [[metacognition]] · [[metacognition-foundational-report]] · [[metacognitive-accuracy]] · [[metacognitive-awareness]] · [[metacognitive-calibration]] · [[metacognitive-calibration-training]] · [[metacognitive-experience]] · [[metacognitive-judgments]] · [[metacognitive-knowledge]] · [[metacognitive-monitoring]] · [[metacognitive-regulation]] · [[metacognitive-scaffolding-as-externalized-prefrontal-function]] · [[metacognitive-self-regulation]] · [[metacognitive-strategies]] · [[monitoring-control-coupling]] · [[monitoring-gap]] · [[monitoring-regulation-decoupling]] · [[nelson-narens-model]] · [[prefrontal-cortex]] · [[procedural-metacognitive-knowledge]] · [[pseudometacognition]] · [[regulation-of-cognition]] · [[self-monitoring]] · [[self-regulated-learning]] · [[working-memory-capacity]]

```dataview
LIST FROM [[Technical Detail SDT Formalization of Monitoring]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[metacognitive-monitoring-accuracy-calibration-deep-dive-2026-04-12]] · [[metacognitive-monitoring-accuracy-calibration-deep-dive-2026-04-12_report]]
