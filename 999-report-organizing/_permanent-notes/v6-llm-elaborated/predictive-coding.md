---
title: "Predictive Coding"
aliases:
  - "Predictive Coding"
  - "predictive coding theory"
type: permanent-note
status: enriched
confidence: high

tags:
  - permanent-note
  - v6-llm-elaborated
  - neuroscience

domain: neuroscience
subdomains:
  - cognitive-science
  - computational-neuroscience

created: 2026-04-27
updated: 2026-04-27

source-type: report-extraction
source-reports:
  - "predictive-coding-synthetic-seed-2026-04-27"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "Bayesian Brain Hypothesis"

related:
  - "[[predictive-processing]]"
  - "[[free-energy-principle]]"
  - "[[attention-and-cognitive-control]]"
  - "[[bayesian-reasoning]]"
prerequisites:
  - "[[]]"
specializes:
  - "[[]]"
broader:
  - "[[]]"
see-also:
  - "[[predictive-processing]]"
contrasts-with:
  - "[[free-energy-principle]]"
contradicts:
  - "[[]]"
applies-to:
  - "[[attention-and-cognitive-control]]"
formalizes:
  - "[[bayesian-reasoning]]"
instance-of:
  - "[[]]"
supports:
  - "[[]]"
refines:
  - "[[]]"

review-frequency: quarterly
mastery-stage: budding
importance: medium

provenance:
  pipeline-version: "v6.0.0"
  outline-contract: "v6-outline-v1"
  elaborate-contract: "v6-elaborate-v1"
  passes: 2
---

# Predictive Coding

> [!definition] **Predictive Coding**
> Predictive Coding is a neurocomputational framework proposing that the brain continuously generates top-down predictions about sensory input while propagating only prediction errors—unexplained residuals—up the cortical hierarchy, thereby organizing perception and learning around minimizing surprise rather than passively registering stimuli. It falls under the Bayesian Brain Hypothesis as a specific implementation of probabilistic inference, though it remains a computational model rather than a confirmed neural mechanism. Crucially, it should not be conflated with the broader Free Energy Principle, which encompasses additional theoretical claims beyond predictive error minimization.

> [!attention] **Boundary**
> Predictive Coding is a computational framework, not a specific neural mechanism. It should not be conflated with the Free Energy Principle, which is a broader theoretical framework. The proposed neural implementation (e.g., superficial vs deep pyramidal cells) remains under empirical investigation and is not established fact.

## Core Explanation

Predictive Coding fundamentally reorients our understanding of perception by inverting the classical bottom-up model. Instead of the brain passively receiving sensory data and constructing percepts from the ground up, it actively generates predictions about incoming stimuli based on prior experience. These predictions flow downward through cortical layers, while only the discrepancies between expected and actual input—prediction errors—propagate upward for further processing. This framework posits that the brain's primary function is not to represent the world directly but to minimize the surprise associated with sensory input, creating a dynamic loop where perception is an active inference process rather than a passive registration of external events.

The theoretical roots of Predictive Coding lie in Bayesian inference, where the brain treats perception as a process of updating probabilistic beliefs. By prioritizing prediction error minimization, the framework elegantly explains phenomena like perceptual illusions: when top-down predictions conflict with sensory input (e.g., the Kanizsa triangle illusion), the brain resolves the discrepancy by generating a percept that aligns with its expectations rather than the raw visual data. This also accounts for attentional mechanisms, as the brain selectively amplifies sensory channels that reduce prediction errors, effectively prioritizing information that confirms or updates its models of the world.

Empirically, Predictive Coding gains traction through its explanatory power for behavioral and neural phenomena without requiring specific neural implementations. For instance, it accounts for the brain's efficiency in processing complex scenes by focusing resources on unexpected elements rather than redundant information. This aligns with observations that cortical activity correlates more strongly with prediction errors than with raw sensory input, suggesting a computational economy where the brain avoids redundant processing of predictable stimuli. The framework thus provides a unifying lens for understanding how the brain optimizes information processing under constraints of limited neural resources.

Critically, Predictive Coding operates as a high-level computational abstraction, not a detailed account of neural wiring. It describes *what* the brain does (minimize prediction errors) without specifying *how* neurons implement this process. This distinction is vital: while the framework predicts that superficial and deep pyramidal cells might handle predictions and errors respectively, this remains a hypothesis under empirical scrutiny rather than established fact. The framework's strength lies in its generality, allowing it to guide experiments without prematurely committing to specific neural architectures.

## Practical Implications

> [!example] **Application 1 — Visual Illusions**
> In visual illusions like the Kanizsa triangle, Predictive Coding explains why observers perceive a complete triangle where none exists. The brain's top-down predictions about shape and continuity override the incomplete sensory input, generating a percept that minimizes prediction error. Without this framework, such illusions would appear as mere sensory misrepresentations. However, Predictive Coding reveals them as evidence of the brain actively constructing reality based on prior expectations, with the illusion persisting because the prediction error is resolved by the brain's model rather than the physical stimulus.

> [!example] **Application 2 — Attentional Focus**
> Predictive Coding clarifies how attention enhances perception: by amplifying sensory channels that reduce prediction errors, the brain prioritizes information that confirms or updates its models. For example, in a crowded room, attention to a voice minimizes prediction errors for auditory input by filtering out irrelevant noise. Without this mechanism, attention would merely increase sensory gain indiscriminately, failing to explain why we selectively notice unexpected or meaningful stimuli. The framework thus shows attention as a tool for error minimization, not just signal amplification.

> [!example] **Application 3 — Cortical Resource Allocation**
> The brain's energetic efficiency in processing sensory input is explained by Predictive Coding: predictable stimuli generate minimal prediction errors, requiring less neural activity. For instance, familiar faces are processed with less cortical activation than novel ones because the brain's predictions align closely with input. Ignoring this framework would lead to the misconception that all sensory processing consumes equal energy. Instead, Predictive Coding reveals that the brain conserves resources by focusing neural activity on unexpected events, optimizing both speed and metabolic cost.

## Key Distinctions

> [!key-distinction] **Computational Framework vs. Neural Mechanism**
> Predictive Coding is a computational model describing *what* the brain does (minimize prediction errors), not a description of *how* neurons achieve this. It should not be mistaken for a specific neural mechanism, such as the proposed role of superficial vs. deep pyramidal cells. The distinction matters because conflating the two risks treating theoretical predictions as anatomical facts; empirical evidence supports the computational role of prediction errors but not the neural implementation, which remains under investigation.

> [!key-distinction] **Predictive Coding vs. Free Energy Principle**
> Predictive Coding is a specific computational framework within the broader Free Energy Principle (FEP), which posits that biological systems minimize free energy to maintain homeostasis. While Predictive Coding focuses on sensory prediction errors, FEP extends to all adaptive behavior, including action and emotion. Confusing them would misrepresent Predictive Coding as a comprehensive theory of life rather than a targeted model of perception. The key is recognizing that Predictive Coding is a subset of FEP's principles, not an equivalent framework.

## Open Questions

> [!open-question] **Question**
> What is the neural circuitry implementing prediction-error signaling in the cortex?
>
> *What would resolve it:* Empirical validation through high-resolution neural recordings during predictive tasks would identify whether superficial and deep pyramidal cells indeed encode predictions and errors, respectively. Resolving this would confirm or refute the proposed microcircuitry, distinguishing computational predictions from biological reality.

## Synthesis

Predictive Coding bridges abstract computational theory with concrete neuroscience by framing perception as an active inference process. It extends the Bayesian Brain Hypothesis into a testable model, explaining how the brain's efficiency, attention, and even illusions emerge from error minimization. This synthesis positions Predictive Coding as a cornerstone for understanding cognition, offering a unified language for phenomena ranging from sensory processing to decision-making. Its significance lies in demonstrating that the brain is not a passive receiver but an active predictor, reshaping how we model both healthy and pathological brain function.

By connecting to related concepts like Bayesian Reasoning and Predictive Processing, Predictive Coding reveals a broader paradigm shift in neuroscience. It moves beyond isolated neural mechanisms to emphasize the brain's role as a probabilistic inference engine, where learning and perception are two sides of the same error-minimization coin. This perspective not only clarifies existing phenomena but also guides future research into neural coding, artificial intelligence, and clinical applications for disorders involving prediction errors, such as schizophrenia or autism.

## Evidence

The strongest evidence for Predictive Coding lies in its ability to explain diverse phenomena through a single computational lens. Behavioral studies show that perceptual illusions arise when prediction errors are resolved by top-down expectations rather than sensory input, while neural data reveal that cortical activity correlates more strongly with prediction errors than with raw stimuli. Attentional experiments further demonstrate that selective focus reduces prediction errors for relevant inputs, aligning with the framework's predictions. Crucially, this evidence remains computational and behavioral, avoiding premature claims about neural implementation, which underscores Predictive Coding's role as a framework rather than a neuroanatomical fact.

## Connections & Context

**Falls under:** [[Bayesian Brain Hypothesis]]

**Sibling concepts:** [[predictive-processing]]

**Contrasts with:** [[free-energy-principle]]

**Applies to:** [[attention-and-cognitive-control]]

**Formalizes:** [[bayesian-reasoning]]

**Source:** [[predictive-coding-synthetic-seed-2026-04-27]]
