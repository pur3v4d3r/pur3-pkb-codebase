---
title: "Active Inference"
aliases:
  - "Active Inference"
  - "Friston active inference"
  - "action-as-inference"
type: permanent-note
status: enriched
confidence: medium

tags:
  - permanent-note
  - v6-llm-elaborated
  - cognitive-science

domain: cognitive-science
subdomains:
  - computational-neuroscience
  - predictive-processing

created: 2026-04-26
updated: 2026-04-26

source-type: report-extraction
source-reports:
  - "active-inference-synthetic-seed-2026-04-26"
evidence-quality: medium
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "Predictive Processing"

related:
  - "[[Free Energy Principle]]"
  - "[[Predictive Coding]]"
  - "[[Bayesian Brain]]"
prerequisites:
  - "[[]]"
specializes:
  - "[[]]"
broader:
  - "[[Free Energy Principle]]"
see-also:
  - "[[Predictive Coding]]"
contrasts-with:
  - "[[Bayesian Brain]]"
contradicts:
  - "[[]]"
applies-to:
  - "[[]]"
formalizes:
  - "[[]]"
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

# Active Inference

> [!definition] **Active Inference**
> Active Inference is a theoretical framework developed by Karl Friston that unifies perception and action under the principle of minimizing variational free energy, falling under [[Predictive Processing]]. It extends the Free Energy Principle by integrating motor commands as proprioceptive predictions whose prediction errors are minimized through the spinal reflex arc, thus reframing action as the resolution of self-fulfilling predictions rather than a separate output of a motor controller.

> [!attention] **Boundary**
> This concept excludes specific implementations or applications of Active Inference, focusing on its core principles and mechanisms.

## Core Explanation

At its core, Active Inference posits that organisms minimize long-term variational free energy by either updating their internal generative model to match sensory input (perception) or acting on the world to make sensory input match the model (action). This unification dissolves the traditional distinction between perception and action, treating both as forms of inference. By minimizing prediction errors, Active Inference provides a coherent framework for understanding how organisms interact with their environment.

In practice, this means that when an organism encounters unexpected sensory input, it updates its generative model to better predict future inputs. Conversely, if the current state of the world does not align with the internal model, the organism takes action to reduce prediction errors. This process is continuous and recursive, allowing for real-time adaptation and learning. The theoretical roots of Active Inference lie in Bayesian principles, where prior beliefs are updated based on sensory evidence, leading to a dynamic balance between prediction and correction.

The conceptual nuances of Active Inference highlight its generative nature, emphasizing the role of internal models in predicting future states. Unlike other predictive processing frameworks like Free Energy Principle or Bayesian Brain, which focus more on perception, Active Inference places equal emphasis on action as a means to resolve prediction errors. This dual focus makes it particularly powerful for understanding complex cognitive processes such as decision-making and learning.

Empirically, Active Inference has been applied in various domains of cognitive science, including neuroscience and artificial intelligence. For instance, it can be used to model how humans make decisions under uncertainty by continuously updating their internal models based on sensory feedback and taking actions that reduce prediction errors.

## Mechanism

The mechanism of Active Inference involves the continuous minimization of variational free energy through two primary processes: perception and action. Perception updates the generative model to better predict future inputs, while action adjusts the environment to make sensory input more consistent with the internal model. This process is facilitated by the spinal reflex arc, which translates motor commands into proprioceptive predictions that minimize prediction errors.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design, Active Inference can guide the creation of adaptive learning environments. By understanding how learners update their internal models based on feedback and take actions to reduce prediction errors, educators can design interactive materials that continuously adjust to meet students' needs, thereby enhancing learning outcomes.

> [!example] **Application 2 — Neuroscience**
> In neuroscience, Active Inference provides a framework for understanding how the brain processes sensory information and generates motor commands. By modeling the brain as an active inference system, researchers can better explain phenomena such as attentional shifts and decision-making under uncertainty.

> [!example] **Application 3 — Artificial Intelligence**
> In AI, Active Inference offers a principled approach to developing autonomous agents that can learn and adapt in complex environments. By minimizing prediction errors through both perception and action, these agents can make informed decisions based on their internal models of the world.

## Key Distinctions

> [!key-distinction] **Unified Perception and Action vs Separate Control**
> Active Inference differs from other predictive processing frameworks like Free Energy Principle or Bayesian Brain by unifying perception and action under a single principle. Unlike these frameworks, which often treat perception as the primary process for updating internal models, Active Inference emphasizes that both perception and action are forms of inference aimed at minimizing prediction errors.

## Key Figures

- **Karl Friston** — Karl Friston is the primary developer of Active Inference. He introduced this framework as an extension of the Free Energy Principle, emphasizing the unification of perception and action under a single principle of minimizing variational free energy.

## Open Questions

> [!open-question] **Question**
> How can Active Inference be empirically validated?
>
> *What would resolve it:* Empirical validation would require controlled experiments that test specific predictions derived from the Active Inference framework, such as how organisms update their internal models and take actions to reduce prediction errors.

> [!open-question] **Question**
> What are the limitations and potential biases in using generative models?
>
> *What would resolve it:* Addressing these concerns would involve developing methods for independently constraining priors in generative models, ensuring that they do not lead to unfalsifiable predictions. This could be achieved through cross-validation with independent datasets or by incorporating empirical constraints.

## Synthesis

Active Inference holds significant value in cognitive science as it provides a unified framework for understanding perception and action. By integrating these processes, Active Inference offers new insights into complex cognitive phenomena such as decision-making, learning, and attention. Its potential impact extends beyond cognitive science to fields like neuroscience and artificial intelligence, where it can guide the development of adaptive systems that learn from their environment in real-time.

The framework's generative nature and emphasis on minimizing prediction errors make it particularly relevant for understanding how organisms interact with their environments. By continuously updating internal models based on sensory feedback and taking actions to reduce prediction errors, Active Inference provides a coherent explanation for a wide range of cognitive processes.

## Connections & Context

**Falls under:** [[Predictive Processing]]

**Generalizes to:** [[Free Energy Principle]]

**Sibling concepts:** [[Predictive Coding]]

**Contrasts with:** [[Bayesian Brain]]

**Source:** [[active-inference-synthetic-seed-2026-04-26]]
