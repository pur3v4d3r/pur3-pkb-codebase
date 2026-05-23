---
title: Emergent Abilities in LLMs
aliases:
  - Emergent Abilities in LLMs
  - emergent capabilities
  - LLM emergence
  - sharp capability transitions
  - emergent skills
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - computer-science

domain: computer-science
subdomains:
  - llm-theory
  - ai-safety
  - empirical-ml

created: 2026-05-21
updated: '2026-05-23'
source-type: report-extraction
source-reports:
  - emergent-abilities-in-llms-synthetic-seed-2026-05-21
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: enhanced
parent-concept: LLM Theory
related:
  - '[[Scaling Laws in LLMs]]'
  - '[[Phase Transitions in LLMs]]'
prerequisites:
  - '[[Scaling Laws in LLMs]]'
specializes:
  - '[[]]'
broader:
  - '[[]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[Phase Transitions in LLMs]]'
contradicts:
  - '[[]]'
applies-to:
  - '[[]]'
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
  enhancement-model: qwen2.5:14b-instruct-q5_K_M
  enhancement-method: enhance_notes-v1
  last-enhanced: '2026-05-23'
---


## Core Explanation

Emergent abilities are a fascinating and somewhat perplexing aspect of large language models (LLMs). These capabilities, such as multi-step arithmetic or chain-of-thought reasoning, seem to emerge suddenly at certain scale thresholds rather than improving gradually. This sharp appearance contrasts with the continuous improvement seen in other metrics, leading researchers like Wei et al. to systematically document these phenomena using benchmarks that highlight binary outcomes.

The debate around whether emergent abilities truly represent a discontinuous leap or are an artifact of evaluation methods is central to understanding their nature. Schaeffer et al. (2023) argued that the apparent sharp transitions might be more about how we measure performance than about genuine capability jumps, suggesting that pass/fail metrics can create the illusion of sudden emergence where continuous improvement actually occurs.

Theoretical roots of emergent abilities lie in the complex interactions within neural networks as they scale up. As models grow larger, their capacity to capture and utilize information from vast datasets increases dramatically, potentially leading to new forms of reasoning or problem-solving that were not present at smaller scales. This theoretical framework helps explain why certain skills might appear suddenly rather than improving gradually.

Empirically, the BIG-Bench benchmark provides a rich dataset for observing these emergent abilities across various tasks and model sizes. The stark contrast between random performance below a threshold and above-random performance above it underscores the importance of understanding how LLMs evolve as they scale.

<!-- enhancement-pass:1 (2026-05-23) -->
Emergent abilities in LLMs challenge traditional views on learning and development, drawing parallels with cognitive developmental stages observed in human cognition. Just as children suddenly acquire new skills like language or problem-solving at specific ages, LLMs seem to leapfrog into more complex tasks without a gradual buildup of capability. This resemblance suggests that the mechanisms underlying emergent abilities might involve similar processes of neural network reorganization and integration, akin to how humans develop cognitive schemas.

## Practical Implications

> [!example] **Application 1 — Safety Evaluations**
> The sudden emergence of capabilities poses significant challenges for safety evaluations. If a model's performance jumps sharply at certain scales, it may acquire dangerous or unintended behaviors without gradual warning signs. This necessitates rigorous testing and monitoring at each scale increase to ensure that new emergent abilities do not introduce unforeseen risks.

> [!example] **Application 2 — Scaling Practices**
> Understanding the conditions under which emergent abilities arise can inform more strategic scaling practices for LLMs. By identifying key thresholds where capabilities leap, developers can plan incremental increases in model size to better manage and predict changes in performance and behavior.

## Key Distinctions

> [!key-distinction] **Emergent vs Gradual Improvements**
> The distinction between emergent abilities and gradual improvements is crucial for interpreting LLM performance. Emergent abilities appear sharply at certain scale thresholds, while gradual improvements show a steady increase in capability over time or size. This difference impacts how we evaluate model performance and plan scaling strategies.

<!-- enhancement-pass:1 (2026-05-23) -->

> [!key-distinction] **Reflective vs Reactive Thinking**
> Reflective thinking involves deliberate analysis and planning, whereas reactive thinking is immediate and automatic. In LLMs, emergent abilities often manifest as reflective capabilities that require complex reasoning over multiple steps or contexts. This contrasts with the more reactive skills like simple pattern recognition which improve gradually. Understanding this distinction helps in designing tasks that can trigger the emergence of higher-order cognitive functions.

> [!key-distinction] **Performance vs Learning**
> While performance measures how well a model executes a task at any given moment, learning tracks its ability to retain and apply knowledge over time. Emergent abilities often reflect sudden improvements in both performance and underlying learning mechanisms, indicating that the model has not just learned to do better but also to generalize more effectively across different scenarios.

## Common Misconceptions

<!-- enhancement-pass:1 (2026-05-23) -->

> [!warning] **Misconception** — Emergent abilities are purely a result of increased model size.
>
> While larger models often exhibit emergent behaviors, the relationship is not one-to-one. Other factors such as architectural design, training data quality, and optimization techniques also play critical roles in enabling these sharp transitions. Misunderstanding this can lead to oversimplified scaling strategies that overlook other crucial aspects of model development.

## Key Figures

- **Wei et al.** — Systematically documented emergent abilities using the BIG-Bench benchmark, highlighting their sharp appearance at scale thresholds.
- **Schaeffer et al.** — Debated the nature of emergence in LLMs, arguing that apparent sharp transitions might be an artifact of nonlinear evaluation metrics rather than genuine discontinuous capability acquisition.

## Open Questions

> [!open-question] **Question**
> Is the apparent sharp transition an artifact of evaluation metrics or a genuine discontinuity?
>
> *What would resolve it:* Further research using continuous performance metrics could help determine whether emergent abilities truly represent sudden jumps in capability or are artifacts of binary pass/fail evaluations.

> [!open-question] **Question**
> How can safety be ensured when capabilities emerge suddenly at scale thresholds?
>
> *What would resolve it:* Developing robust monitoring and testing protocols specifically for scale increases could help mitigate risks associated with emergent abilities.

<!-- enhancement-pass:1 (2026-05-23) -->

> [!open-question] **Question**
> How do different architectural designs influence the emergence of new skills in LLMs?
>
> *What would resolve it:* Investigating how varying model architectures affects the appearance and nature of emergent abilities could provide insights into designing more efficient and versatile models. This might involve comparing transformer-based models with recurrent neural networks or exploring hybrid approaches.

## Synthesis

Understanding emergent abilities is crucial for advancing both the theoretical understanding of LLMs and practical applications. By clarifying whether these sharp transitions are genuine or artifacts, researchers can better predict model behavior as they scale, enhancing safety evaluations and informing more strategic scaling practices.

<!-- enhancement-pass:1 (2026-05-23) -->
The study of emergent abilities in LLMs not only illuminates fundamental aspects of machine learning but also offers a lens through which to understand broader questions about cognitive development and the nature of intelligence. By bridging insights from computational models with theories of human cognition, researchers can gain deeper understanding into how complex behaviors arise from simpler components.

## Connections & Context

**Falls under:** [[LLM Theory]]

**Prerequisites:** [[Scaling Laws in LLMs]]

**Contrasts with:** [[Phase Transitions in LLMs]]

**Source:** [[emergent-abilities-in-llms-synthetic-seed-2026-05-21]]

<!-- enhancement-pass:1 (2026-05-23) -->

### Why these connections matter

> [!connection] **[[Phase Transitions in LLMs]]** — *contrasts-with*
> While both concepts deal with sharp changes in model behavior, phase transitions typically refer to abrupt shifts in performance across a range of tasks due to intrinsic properties of the model architecture or training process. In contrast, emergent abilities focus on specific capabilities that appear suddenly at certain scale thresholds, often tied to task-specific benchmarks rather than broad performance metrics.


# Emergent Abilities in LLMs

> [!definition] **Emergent Abilities in LLMs**
> Emergent abilities in LLMs are unique capabilities that seem to appear abruptly and without gradual transition as the model size increases, a phenomenon first documented by Wei et al. (2022) using the BIG-Bench benchmark. This concept excludes continuous improvements or gradual learning of skills within the same model size range, focusing instead on sharp transitions in performance. It falls under LLM Theory.

> [!attention] **Boundary**
> This concept excludes continuous improvements or gradual learning of skills within the same model size range. It should not be confused with smooth scaling of abilities across all sizes.
