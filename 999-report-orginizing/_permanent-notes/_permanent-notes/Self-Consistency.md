---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Self-Consistency"
aliases:
  - "Self-Consistency"
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
  - confidence/provisional
  - status/not-read

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-03-19
updated: 2026-03-19

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "prompt-report-self-consistency-complexity-based-consistency-202512250916"
evidence-quality: medium
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: intermediate
depth-level: comprehensive

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  - "[[]]"

related:
  - "[[]]"

broader:
  - "[[]]"

narrower:
  - "[[]]"

see-also:
  - "[[Self-Consistency-&-Complexity-Based-Consistency|**Self-Consistency & Complexity-Based Consistency**]]"
  - "[[Chain-of-Thought-Prompting|Chain-of-Thought Prompting]]"
  - "[[Ensemble-Methods|Ensemble Methods]]"
  - "[[Reasoning-Verification|Reasoning Verification]]"
  - "[[Majority-Voting|Majority Voting]]"
  - "[[Cognitive-Diversity|Cognitive Diversity]]"
  - "[[Chain-of-Thought-Prompting|Chain-of-Thought Prompting]]"
  - "[[Temperature-Sampling|Temperature Sampling]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  - "[[]]"

enables:
  - "[[]]"

expansion-topics:
  - topic: "[[]]"
    description: ""
    priority: medium

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: medium
---

# Self-Consistency

> [!definition] **Self-Consistency**
> [**Self-Consistency**:: A prompting reliability technique that generates multiple independent [[Chain-of-Thought]] reasoning paths for a single query through high-temperature sampling, then aggregates final answers via [[Majority Voting]] to select the most statistically consistent conclusion, thereby mitigating the stochasticity and potential errors inherent in single-sample LLM generation.]^established

## Core Explanation

> [!evidence] Supporting Evidence
> [**Self-Consistency-Performance-Gains**:: Wang et al. (2022) demonstrated that Self-Consistency with 40 sampled reasoning chains improved accuracy on [[GSM8K]] math word problems from 56.5% (greedy decoding) to 74.4%, on [[MATH]] from 25.7% to 36.8%, and on [[StrategyQA]] commonsense reasoning from 72.5% to 79.2%, representing relative error reductions of 40-44% across reasoning domains.]^verified
> 
> These gains prove particularly significant for problems requiring multi-step inference where…

> [!evidence] Supporting Evidence
> **Wang et al. (2022) - Original Self-Consistency Paper**
> 
> [**GSM8K-Improvement**:: On the [[GSM8K]] grade school math dataset, Self-Consistency (40 samples) improved [[PaLM-540B]] accuracy from 56.5% (greedy) to 74.4%, and [[GPT-3]] davinci-002 from 46.8% to 61.2%, representing absolute gains of 17.9 and 14.4 percentage points respectively.]^verified
> 
> [**MATH-Improvement**:: On the competition-level [[MATH]] dataset, improvements were even more dramatic: PaLM-540B rose from 25.7% to 36.8%…

> [!evidence] Supporting Evidence
> **Kojima et al. (2023)** validated Self-Consistency across diverse model families:
> 
> - **[[GPT-4]]**: 8-12% accuracy improvement on multi-step reasoning tasks
> - **[[Claude-2]]**: 6-10% improvement on [[MMLU]] reasoning subtasks  
> - **[[Llama-2-70B]]**: 4-7% improvement on [[BIG-Bench]] hard reasoning problems
> 
> The technique's effectiveness proved model-agnostic, working across different architectures, training paradigms, and scale points, though larger models generally exhibited more substantial…

> [!analytical-insight] Key Insight
> [**Error-Independence-Assumption**:: Self-Consistency's effectiveness relies on the critical assumption that reasoning errors across independently sampled chains are largely uncorrelated—that is, different reasoning paths fail in different ways rather than systematically reproducing identical mistakes.]^established
> 
> This assumption holds remarkably well in practice for [[Chain-of-Thought]] reasoning, where the model's vast parameter space and high-dimensional reasoning trajectories create…

> [!analytical-insight] Key Insight
> [**Length-Accuracy-Correlation**:: In mathematical reasoning tasks, empirical studies show positive correlation (Pearson $r \approx 0.3-0.5$) between reasoning chain token length and answer correctness, with the relationship strongest for complex multi-step problems requiring elaborate intermediate calculations rather than simple one-step inferences.]^provisional
> 
> This correlation exhibits domain dependence: strong for mathematical problem solving and logical reasoning, moderate for commonsense…

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction**
> [**Self-Consistency-Cost-Multiplier**:: Standard Self-Consistency with $N=40$ samples imposes a 40× increase in inference cost compared to single-chain generation, making the technique economically prohibitive for high-volume production deployments without cost mitigation strategies like early stopping, adaptive sampling, or model distillation.]^established
> 
> This cost barrier explains why [[Self-Consistency]] sees primary adoption in high-stakes reasoning applications (medical diagnosis…

## Connections & Context

**Cross-report connections:**
- [[Chain-of-Thought-Prompting|Chain-of-Thought Prompting]]
- [[Self-Consistency]]
- [[Chain-of-Thought]]
- [[Few-Shot-Learning|Few-Shot Learning]]
- [[Self-Refine]]
- [[Self-Refine]]
- [[Least-to-Most-Prompting|Least-to-Most Prompting]]
- [[Least-to-Most]]
- [[Retrieval-Augmented-Generation|Retrieval-Augmented Generation]]

**Related concepts:**
[[Self-Consistency-&-Complexity-Based-Consistency|**Self-Consistency & Complexity-Based Consistency**]] · [[Chain-of-Thought-Prompting|Chain-of-Thought Prompting]] · [[Ensemble-Methods|Ensemble Methods]] · [[Reasoning-Verification|Reasoning Verification]] · [[Majority-Voting|Majority Voting]] · [[Cognitive-Diversity|Cognitive Diversity]] · [[Chain-of-Thought-Prompting|Chain-of-Thought Prompting]] · [[Temperature-Sampling|Temperature Sampling]] · [[Ensemble-Learning|Ensemble Learning]] · [[Bayesian-Reasoning|Bayesian Reasoning]] · [[Complex-Reasoning-Tasks|Complex Reasoning Tasks]] · [[Math-Word-Problems|Math Word Problems]] · [[Commonsense-Reasoning|Commonsense Reasoning]] · [[Multi-Step-Inference|Multi-Step Inference]] · [[Prompt-Reliability-Engineering|Prompt Reliability Engineering]]
