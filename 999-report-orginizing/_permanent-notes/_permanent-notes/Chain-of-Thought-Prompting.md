---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Chain-of-Thought Prompting"
aliases:
  - "Chain-of-Thought Prompting"
type: permanent-note
status: evergreen
confidence: medium

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - evergreen
  - other
  - type/report
  - source/claude-sonnet
  - maturity/seedling
  - confidence/speculative
  - status/not-read

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-03-27
updated: 2026-03-27

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "prompt-report-chain-of-thought-logic-2025122305"
evidence-quality: medium
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"
pipeline-version: "2.1.0"
extraction-date: "2026-03-27"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: intermediate
depth-level: comprehensive

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  []

related:
  []

broader:
  []

narrower:
  []

see-also:
  - "[[Chanin-Of-Thought|**Chanin Of Thought**]]"
  - "[[Transformer-Architecture|Transformer Architecture]]"
  - "[[Few-Shot-Learning|Few-Shot Learning]]"
  - "[[Emergent-Abilities|Emergent Abilities]]"
  - "[[Self-Consistency]]"
  - "[[Tree-of-Thoughts|Tree of Thoughts]]"
  - "[[Logical-Reasoning|Logical Reasoning]]"
  - "[[Working-Memory|Working Memory]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  []

enables:
  []

expansion-topics:
  []

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: medium
---

# Chain-of-Thought Prompting

> [!definition] **Chain-of-Thought Prompting**
> [**Chain-of-Thought-Prompting**:: A prompting methodology that elicits intermediate reasoning steps from language models by providing few-shot exemplars demonstrating explicit step-by-step problem decomposition, enabling the model to generate similar reasoning traces before producing final answers.]^verified

## Core Explanation

> [!evidence] Supporting Evidence
> [**CoT-Emergence-Threshold**:: Wei et al. (2022) demonstrated that CoT prompting shows negligible improvements for models below ~100B parameters (including GPT-3 175B with standard prompting), but achieves dramatic gains above this threshold—PaLM 540B with CoT attained 58% on GSM8K math problems, surpassing fine-tuned models and representing ~40% absolute improvement over standard prompting.]^verified

> [!evidence] Supporting Evidence
> [**GSM8K-Results**:: Wei et al. (2022) demonstrated that PaLM-540B with CoT achieved 58% accuracy on GSM8K, representing a 40+ percentage point improvement over the same model with standard prompting (17%). Follow-up work by Wang et al. (2022) using Self-Consistency on top of CoT pushed accuracy to 74%, establishing new state-of-the-art and surpassing fine-tuned GPT-3 with verification.]^verified

> [!evidence] Supporting Evidence
> **Primary Sources:**
> 
> Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems, 35*, 24824-24837. arXiv:2201.11903
> 
> Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., & Zhou, D. (2022). Self-consistency improves chain of thought reasoning in language models. *arXiv preprint arXiv:2203.11171*
> 
> Yao, S., Yu, D., Zhao, J., Shafran,…

> [!analytical-insight] Key Insight
> [**CoT-Computational-Mechanism**:: Chain-of-Thought prompting enables transformers to solve problems requiring serial computation by converting depth-limited parallel processing into iterative sequential processing, where each intermediate token serves as a computational "thinking step" that refines hidden representations and accumulates reasoning progress.]^verified

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction**
> <span style='color: #FF00DC;'>⚠️ Critical Limitation:</span> The discontinuous emergence of CoT capabilities creates <span style='color: #FF00DC;'>prediction challenges</span> for AI safety research. If reasoning abilities manifest suddenly above parameter thresholds, <span style='color: #FF00DC;'>smaller-scale testing may fail to reveal behaviors</span> that emerge in production systems. This "capability overhang" means model evaluations performed at 10B parameters cannot reliably predict…

## Connections & Context

**Cross-report connections:**
- [[Cognitive-Load-Theory|Cognitive Load Theory]]
- [[Attention-Mechanism|Attention Mechanism]]
- [[Circuit-Complexity-Theory|Circuit Complexity Theory]]
- [[Mechanistic-Interpretability|Mechanistic Interpretability]]
- [[Prompt-Engineering|Prompt Engineering]]
- [[Few-Shot-Learning|Few-Shot Learning]]
- [[Ensemble-Methods|Ensemble Methods]]
- [[AI-Safety|AI Safety]]
- [[Transformer-Architecture|Transformer Architecture]]
- [[Emergent-Abilities-in-LLMs|Emergent Abilities in LLMs]]

**Related concepts:**
[[Chanin-Of-Thought|**Chanin Of Thought**]] · [[Transformer-Architecture|Transformer Architecture]] · [[Few-Shot-Learning|Few-Shot Learning]] · [[Emergent-Abilities|Emergent Abilities]] · [[Self-Consistency]] · [[Tree-of-Thoughts|Tree of Thoughts]] · [[Logical-Reasoning|Logical Reasoning]] · [[Working-Memory|Working Memory]] · [[Jason-Wei|Jason Wei]] · [[Google-Research|Google Research]] · [[Transformer-Architecture|Transformer Architecture]] · [[Working-Memory|Working Memory]] · [[Cognitive-Load-Theory|Cognitive Load Theory]] · [[Few-Shot-Learning|Few-Shot Learning]] · [[GPT-3]]

## References

- **📚 References & Resources**: **Primary Sources:**

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems, 35*, 24824-24837. arXiv:2201.11903

Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., & Zhou, D. (2022). Self-consistency improves chain of thought reasoning in language models. *arXiv preprint arXiv:2203.11171*

Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., & Narasimhan, K. (2023). Tree of thoughts: Deliberate problem solving with large language models. *arXiv preprint arXiv:2305.10601*

Wang, B., Min, S., Deng, X., Shen, J., Wu, Y., Zettlemoyer, L., & Sun, H. (2023). Towards understanding chain-of-thought prompting: An empirical study of what matters. *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics*, 2717-2739. https://doi.org/10.18653/v1/2023.acl-long.153

Feng, G., Zhang, B., Gu, Y., Ye, H., He, D., & Wang, L. (2024). Chain of thought empowers transformers to solve inherently serial problems. *arXiv preprint arXiv:2402.12875*

**Logical Fallacy Research:**

Walker, P. B., et al. (2025). Addressing logical fallacies in scientific reasoning from large language models: Towards a dual-inference training framework. *arXiv preprint arXiv:2512.04228*

Li, Y., et al. (2024). Reason from fallacy: Enhancing large language models' logical reasoning through logical fallacy understanding. *arXiv preprint arXiv:2404.04293*

**Empirical Evaluation:**

Meincke, L., Mollick, E. R., Mollick, L., & Shapiro, D. (2025). Prompting science report 2: The decreasing value of chain of thought in prompting. *The Wharton School Research Paper*. SSRN: https://ssrn.com/abstract=5285532

Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). Large language models are zero-shot reasoners. *arXiv preprint arXiv:2205.11916*

**Further Reading:**

Google Research Blog: "Language Models Perform Reasoning via Chain of Thought" (https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought/)

IBM Research: "What is Chain of Thought Prompting?" (https://www.ibm.com/think/topics/chain-of-thoughts)

Prompt Engineering Guide: Chain-of-Thought section (https://www.promptingguide.ai/techniques/cot)

## Methodology Notes

> [!methodology-and-sources] **Self-Consistency Algorithm**
> **Step 1:** Generate $K$ independent reasoning chains for the same problem using <span style='color: #72FFF1;'>temperature sampling</span> (typically $T = 0.7$)
> 
> **Step 2:** Extract final answers from each chain (parsing the conclusion after reasoning steps)
> 
> **Step 3:** Compute answer frequency distribution and select <span style='color: #27FF00;'>majority vote</span> as final output
> 
> **Rationale:** <span style='color: #FFC700;'>Incorrect reasoning paths</span> typically diverge toward different wrong answers, while <span style='color: #27FF00;'>correct reasoning</span>, though expressed…

---

## Source Attribution

**Extracted from:** [[prompt-report-chain-of-thought-logic-2025122305]]
