---
title: Base-Rate Neglect
aliases:
  - Base-Rate Neglect
  - Base Rate Neglect
  - base-rate fallacy
  - neglect of base rates
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - cognitive-psychology

domain: cognitive-psychology
subdomains:
  - judgment
  - heuristics-and-biases

created: 2026-04-25
updated: '2026-05-23'
source-type: report-extraction
source-reports:
  - base-rate-neglect-synthetic-seed-2026-04-25
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: enhanced
parent-concept: Cognitive Architecture
related:
  - '[[representativeness-heuristic]]'
  - "[[Prosecutor's Fallacy]]"
  - '[[bayesian-reasoning]]'
prerequisites:
  - '[[]]'
specializes:
  - '[[]]'
broader:
  - '[[]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[representativeness-heuristic]]'
  - "[[Prosecutor's Fallacy]]"
contradicts:
  - '[[]]'
applies-to:
  - '[[bayesian-reasoning]]'
formalizes:
  - '[[]]'
instance-of:
  - '[[]]'
supports:
  - '[[]]'
refines:
  - '[[]]'

review-frequency: quarterly
mastery-stage: budding
importance: medium
provenance:
  pipeline-version: v6.0.0
  outline-contract: v6-outline-v1
  elaborate-contract: v6-elaborate-v1
  passes: 2
  enhancement-passes: 1
  enhancement-model: qwen3:30b
  enhancement-method: enhance_notes-v1
  last-enhanced: '2026-04-27'
  diagram-passes: 1
  diagram-model: qwen2.5:14b-instruct-q5_K_M
  last-diagrammed: '2026-05-23'
---

## 📊 Visual Overview

<!-- diagram-pass:1 (2026-05-23) -->

> [!abstract] **Diagram 1 — Base-Rate Neglect Process Flow**
> *Follow the flow from base rate to specific case information.*
>
> ```mermaid
> graph TD
>   A[Receive Base Rate]
>   B[Receive Specific Case Info]
>   C{Use Base Rate}
>   D{Use Specific Case Info}
>   E[Underweight Base Rate]
>   F[Over-rely on Specific Case]
>   G[Error in Judgment]
>   A -->|Base Rate| C
>   B -->|Specific Case Info| D
>   C -->|No| E
>   D -->|Yes| F
>   E --> G
>   F --> G
> ```


> [!abstract] **Diagram 2 — Representativeness Heuristic vs Base-Rate Neglect**
> *Compare the two biases in their decision-making processes.*
>
> ```mermaid
> graph TD
>   A[Base Rate]
>   B{Use}
>   C[Specific Case Info]
>   D{Use}
>   E[Error: Underweighting Base Rate]
>   F[Representativeness Heuristic]
>   G[Prototype/Stereotype]
>   H{Match}
>   I[Error: Over-relying on Specifics]
>   A -->|Base-Rate Neglect| B
>   C -->|Base-Rate Neglect| D
>   B -->|No| E
>   D -->|Yes| E
>   F -->|Representativeness Heuristic| H
>   G -->|Prototype/Stereotype| H
>   H -->|Match| I
> ```


> [!abstract] **Diagram 3 — Base-Rate Neglect in Decision-Making**
> *Identify the steps leading to judgment errors.*
>
> ```mermaid
> graph TD
>   A[Receive Information]
>   B{Focus on Specifics}
>   C[Underweight Base Rate]
>   D[Error in Judgment]
>   E[Bayesian Normativity]
>   F[Correct Posterior Probability]
>   G[Spontaneous Deployment Failure]
>   A -->|Base-Rate Neglect| B
>   B -->|Yes| C
>   C --> D
>   A -->|Bayesian Reasoning| E
>   E --> F
>   F --> G
> ```

# Base-Rate Neglect

> [!definition] **Base-Rate Neglect**
> Base-Rate Neglect refers to the tendency of individuals to ignore general statistical information (base rates) when making judgments about specific cases, even when this information is highly relevant. It falls under [[cognitive-architecture]], as it highlights a dissociation between intuitive judgment and Bayesian normativity.

> [!attention] **Boundary**
> This concept excludes biases that are specifically related to overconfidence or confirmation bias and focuses on the underweighting of base rates in judgment processes.

## Core Explanation

Base-Rate Neglect occurs when people over-rely on specific case details rather than considering the broader statistical context. This bias can be observed in various scenarios, such as legal judgments where judges might focus too much on individual evidence while ignoring the overall probability of guilt or innocence.

The core mechanism behind Base-Rate Neglect is rooted in how our minds process information. When faced with a specific case, people tend to engage in heuristics that simplify decision-making but often at the expense of accurate Bayesian reasoning. This underweighting of base rates can lead to significant errors in judgment, as demonstrated by participants who can compute correct posterior probabilities when asked separately.

Theoretical roots of Base-Rate Neglect are found in cognitive psychology and the heuristics-and-biases literature. It is often contrasted with Bayesian reasoning, which emphasizes the importance of integrating base rates into judgments. The key claim about Base-Rate Neglect is that it reliably produces biases even when individuals can compute correct posterior probabilities, indicating a failure in spontaneous deployment rather than underlying capacity.

Empirical evidence supporting Base-Rate Neglect comes from numerous studies where participants are asked to estimate the probability of an event based on base rates and specific case information. These studies consistently show that people tend to over-rely on the latter, even when it is less diagnostic.

## Mechanism

The cognitive processes involved in Base-Rate Neglect can be understood through a step-by-step analysis. Initially, individuals receive both base rate and specific case information. However, due to the ease of processing specific details, these are often given more weight than the broader statistical context. This underweighting is further exacerbated by the representativeness heuristic, which leads people to focus on how well the specific case matches their preconceived notions.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design, Base-Rate Neglect can lead to ineffective learning materials. For instance, if a course focuses too much on individual examples without providing relevant statistical information, learners might fail to generalize the material effectively.

> [!example] **Application 2 — Medical diagnoses**
> Base-Rate Neglect is particularly problematic in medical settings where doctors might over-rely on patient symptoms and ignore the prevalence of certain conditions. This can lead to misdiagnoses and inappropriate treatment plans.

> [!example] **Application 3 — Legal judgments**
> In legal contexts, Base-Rate Neglect can result in unfair verdicts. Judges might focus too much on specific evidence from a case while ignoring the broader statistical likelihood of guilt or innocence, leading to biased decisions.

<!-- enhancement-pass:1 (2026-04-27) -->

> [!example] **Application 4 — Investment decision-making**
> In financial contexts, base-rate neglect leads investors to overestimate the likelihood of success for individual stocks based on recent performance while ignoring market-wide failure rates. For instance, during market bubbles, investors may disregard historical data showing 70% of new tech ventures fail, instead focusing on isolated success stories. This contributes to systemic overvaluation and increased market volatility, as seen in the dot-com bubble where base-rate awareness could have mitigated speculative excess.

## Key Distinctions

> [!key-distinction] **Base-Rate Neglect vs Representativeness Heuristic**
> While both biases involve over-reliance on specific case information, Base-Rate Neglect specifically refers to the underweighting of base rates. The representativeness heuristic, in contrast, involves judging probabilities based on how well a particular instance matches a prototype or stereotype.

<!-- enhancement-pass:1 (2026-04-27) -->

> [!key-distinction] **Base-Rate Neglect vs. Base-Rate Fallacy**
> While often conflated, base-rate neglect describes the cognitive tendency to ignore statistical information, whereas the base-rate fallacy specifically refers to the erroneous application of base rates in probabilistic reasoning (e.g., misapplying Bayes' theorem). The fallacy occurs when base rates are considered but incorrectly weighted, whereas neglect involves their complete omission from the judgment process. This distinction clarifies why some errors stem from computational errors rather than information underweighting.

## Key Figures

- **Amos Tversky** — Tversky was one of the key figures who documented Base-Rate Neglect through empirical studies and highlighted its implications for decision-making.
- **Daniel Kahneman** — Kahneman, along with Tversky, contributed significantly to the understanding of cognitive biases like Base-Rate Neglect by integrating psychological insights into broader theories of judgment and decision-making.

<!-- enhancement-pass:1 (2026-04-27) -->
- **Gerd Gigerenzer** — Gigerenzer's work demonstrated that base-rate neglect diminishes when information is presented as natural frequencies rather than probabilities, challenging the notion that the bias is an immutable cognitive flaw. His research provided practical interventions for reducing the bias in medical and legal contexts, emphasizing the role of information format in cognitive processing.

## Open Questions

> [!open-question] **Question**
> How does Base-Rate Neglect vary across different cognitive formats?
>
> *What would resolve it:* Further research is needed to explore how the format in which base rates are presented (e.g., probability vs. natural frequency) affects the likelihood of Base-Rate Neglect.

> [!open-question] **Question**
> Can interventions be designed to mitigate the effects of Base-Rate Neglect?
>
> *What would resolve it:* Experimental studies could test various educational and cognitive strategies aimed at improving individuals' ability to integrate base rates into their judgments.

<!-- enhancement-pass:1 (2026-04-27) -->

> [!open-question] **Question**
> How do cultural differences in statistical literacy affect base-rate neglect across societies?
>
> *What would resolve it:* Cross-cultural studies comparing East Asian and Western populations could resolve this, as collectivist cultures may exhibit different base-rate processing patterns due to varying emphasis on group statistics versus individual cases.

## Synthesis

Base-Rate Neglect is a critical concept in understanding human judgment processes, particularly within the broader field of [[cognitive-architecture]]. By highlighting the dissociation between intuitive reasoning and Bayesian normativity, it underscores the importance of integrating statistical information into decision-making. This concept has significant implications across various domains, including legal judgments, medical diagnoses, and instructional design. Addressing Base-Rate Neglect can lead to more accurate and fair outcomes in these areas, making it a vital area of study for cognitive psychologists and practitioners alike.

The contrast with Bayesian reasoning further emphasizes the need for interventions that help individuals better integrate base rates into their decision-making processes. By understanding and addressing Base-Rate Neglect, we can improve our overall judgment accuracy and reduce biases in critical fields such as medicine and law.

## Evidence

Empirical evidence supporting Base-Rate Neglect comes from numerous studies where participants are asked to estimate the probability of an event based on base rates and specific case information. These studies consistently show that people tend to over-rely on the latter, even when it is less diagnostic.

<!-- enhancement-pass:1 (2026-04-27) -->
Gigerenzer's research demonstrates that presenting base rates as natural frequencies (e.g., '10 out of 100 people') rather than probabilities (e.g., '10%') significantly reduces base-rate neglect. This effect, observed across diverse populations including medical professionals and laypeople, suggests the bias is not inherent to human cognition but stems from how information is encoded. Meta-analyses confirm this framing effect accounts for up to 50% reduction in neglect across studies, highlighting the malleability of the bias through presentation design.

## Connections & Context

**Falls under:** [[cognitive-architecture]]

**Contrasts with:** [[representativeness-heuristic]] · [[Prosecutor's Fallacy]]

**Applies to:** [[bayesian-reasoning]]

**Source:** [[base-rate-neglect-synthetic-seed-2026-04-25]]
