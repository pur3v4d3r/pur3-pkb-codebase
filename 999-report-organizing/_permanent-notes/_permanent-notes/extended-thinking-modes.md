---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Extended Thinking Modes"
aliases:
  - "Extended Thinking Modes"
  - "Extended-Thinking-Modes"
  - "ETM"
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

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-04-21
updated: 2026-04-21

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "claudes-extended-thinking"
evidence-quality: medium
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"
pipeline-version: "2.1.0"
extraction-date: "2026-04-21"

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
  - "[[chain-of-thought|Chain-of-Thought]]"
  - "[[tree-of-thoughts|Tree-of-Thoughts]]"
  - "[[self-consistency|Self-Consistency]]"
  - "[[reflexion|Reflexion]]"
  - "[[chain-of-thought|Chain-of-Thought]]"
  - "[[chain-of-thought-prompting|Chain-of-Thought-Prompting]]"
  - "[[wei-et-al.-2022|Wei-et-al.-2022]]"
  - "[[tree-of-thoughts|Tree-of-Thoughts]]"
  - "[[yao-et-al.-2023|Yao et al. 2023]]"
  - "[[self-consistency|Self-Consistency]]"
  - "[[wang-et-al.-2022|Wang-et-al.-2022]]"
  - "[[reflexion|Reflexion]]"
  - "[[shinn-et-al.-2023|Shinn et al. 2023]]"
  - "[[chain-of-verification|Chain-of-Verification]]"
  - "[[dhuliawala-et-al.-2023|Dhuliawala et al. 2023]]"
  - "[[prompt-engineering-taxonomy-and-pattern-library|Prompt Engineering Taxonomy and Pattern Library]]"
  - "[[Token Economics and Cost Optimization for Production LLM Systems]]"
  - "[[cognitive-science-foundations-of-llm-reasoning-techniques|Cognitive Science Foundations of LLM Reasoning Techniques]]"
  - "[[multi-agent-architectures-and-agentic-workflows|Multi-Agent Architectures and Agentic Workflows]]"
  - "[[evaluation-methodologies-for-llm-reasoning-quality|Evaluation Methodologies for LLM Reasoning Quality]]"

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

# Extended Thinking Modes

> [!definition] **Extended Thinking Modes** *(from [[claudes-extended-thinking]])*
> Claude supports multiple thinking modes controlled via the `<thinking_mode>` parameter:
> 
> - **`enabled`**: Thinking blocks generated when the model determines they would improve response quality
> - **`disabled`**: No thinking blocks generated (standard response mode)  
> - **`auto`**: Model autonomously decides when to use thinking based on task complexity
> - **`interleaved`**: Thinking can be interspersed with tool use and response generation for complex multi-step workflows

## Core Explanation

> [!analytical-insight] Key Insight *(from [[claudes-extended-thinking]])*
> Reflexion within extended thinking enables a form of "fast meta-learning"—not learning new knowledge, but learning better problem-solving strategies for the specific task at hand through rapid iteration cycles. This parallels human expert problem-solving more closely than direct answer generation.

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction** *(from [[claudes-extended-thinking]])*
> While ToT enables superior reasoning quality, it comes with significant token costs. A ToT exploration with branching factor 4 and depth 3 generates 64 leaf nodes in complete exploration. Strategic pruning (discarding low-scoring branches early) is essential for practical deployment. The academic paper generator template in the user's original request demonstrates sophisticated pruning strategies using threshold-based and relative scoring approaches.

> [!warning] **Key Distinction** *(from [[claudes-extended-thinking]])*
> [**Deliberation-Effectiveness-Tradeoff**:: The empirically observed phenomenon where moderate deliberation improves outcomes, but excessive deliberation can degrade performance through overthinking, anxiety effects, or analysis paralysis—suggesting optimal thinking depth is task-dependent with diminishing returns.]

## Concrete Examples

> [!example] **Practical Manifestation: Error Correction Without Visible Revisions** *(from [[claudes-extended-thinking]])*
> Consider a mathematical problem where Claude's initial approach in a thinking block proves incorrect:
> 
> ```xml
> 
> 
> The solution uses formula Y because [explanation]...
> ```
> 
> The user sees only the correct approach—never knowing that an initial error was caught and corrected during thinking. This creates response quality that would be impossible with visible reasoning chains.

## Connections & Context

**Related concepts:**
[[chain-of-thought|Chain-of-Thought]] · [[tree-of-thoughts|Tree-of-Thoughts]] · [[self-consistency|Self-Consistency]] · [[reflexion|Reflexion]] · [[chain-of-thought|Chain-of-Thought]] · [[chain-of-thought-prompting|Chain-of-Thought-Prompting]] · [[wei-et-al.-2022|Wei-et-al.-2022]] · [[tree-of-thoughts|Tree-of-Thoughts]] · [[yao-et-al.-2023|Yao et al. 2023]] · [[self-consistency|Self-Consistency]] · [[wang-et-al.-2022|Wang-et-al.-2022]] · [[reflexion|Reflexion]] · [[shinn-et-al.-2023|Shinn et al. 2023]] · [[chain-of-verification|Chain-of-Verification]] · [[dhuliawala-et-al.-2023|Dhuliawala et al. 2023]] · [[prompt-engineering-taxonomy-and-pattern-library|Prompt Engineering Taxonomy and Pattern Library]] · [[Token Economics and Cost Optimization for Production LLM Systems]] · [[cognitive-science-foundations-of-llm-reasoning-techniques|Cognitive Science Foundations of LLM Reasoning Techniques]] · [[multi-agent-architectures-and-agentic-workflows|Multi-Agent Architectures and Agentic Workflows]] · [[evaluation-methodologies-for-llm-reasoning-quality|Evaluation Methodologies for LLM Reasoning Quality]] · [[safety-and-alignment-considerations-in-advanced-reasoning-systems|Safety and Alignment Considerations in Advanced Reasoning Systems]]

---

## Source Attribution

**Extracted from:** [[claudes-extended-thinking]]
