---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Extended Thinking Modes"
aliases:
  - "Extended Thinking Modes"
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
  - #
  - p
  - r
  - o
  - m
  - t
  - -
  - e
  - n

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-04-01
updated: 2026-04-18

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "claudes-extended-thinking"
  - "report-claudes-extended-thinking-acrchitecture.md"
evidence-quality: medium
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"
pipeline-version: "2.1.0"
extraction-date: "2026-04-01"

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
  - "[[Chain-of-Thought|Chain of Thought]]"
  - "[[Tree-of-Thoughts|Tree of Thoughts]]"
  - "[[Self-Consistency]]"
  - "[[Reflexion]]"
  - "[[Chain-of-Thought-Prompting|Chain of Thought Prompting]]"
  - "[[Wei-et-al.-2022|Wei et al. 2022]]"
  - "[[Yao-et-al.-2023|Yao et al. 2023]]"
  - "[[Wang-et-al.-2022|Wang et al. 2022]]"
  - "[[Shinn-et-al.-2023|Shinn et al. 2023]]"
  - "[[Chain-of-Verification|Chain of Verification]]"
  - "[[Dhuliawala-et-al.-2023|Dhuliawala et al. 2023]]"
  - "[[Prompt-Engineering-Taxonomy-and-Pattern-Library|Prompt Engineering Taxonomy and Pattern Library]]"
  - "[[Token-Economics-and-Cost-Optimization-for-Production-LLM-Systems|Token Economics and Cost Optimization for Production LLM Systems]]"
  - "[[Cognitive-Science-Foundations-of-LLM-Reasoning-Techniques|Cognitive Science Foundations of LLM Reasoning Techniques]]"
  - "[[Multi-Agent-Architectures-and-Agentic-Workflows|Multi-Agent Architectures and Agentic Workflows]]"
  - "[[Evaluation-Methodologies-for-LLM-Reasoning-Quality|Evaluation Methodologies for LLM Reasoning Quality]]"

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
[[Chain-of-Thought|Chain of Thought]] · [[Tree-of-Thoughts|Tree of Thoughts]] · [[Self-Consistency]] · [[Reflexion]] · [[Chain-of-Thought|Chain of Thought]] · [[Chain-of-Thought-Prompting|Chain of Thought Prompting]] · [[Wei-et-al.-2022|Wei et al. 2022]] · [[Tree-of-Thoughts|Tree of Thoughts]] · [[Yao-et-al.-2023|Yao et al. 2023]] · [[Self-Consistency]] · [[Wang-et-al.-2022|Wang et al. 2022]] · [[Reflexion]] · [[Shinn-et-al.-2023|Shinn et al. 2023]] · [[Chain-of-Verification|Chain of Verification]] · [[Dhuliawala-et-al.-2023|Dhuliawala et al. 2023]] · [[Prompt-Engineering-Taxonomy-and-Pattern-Library|Prompt Engineering Taxonomy and Pattern Library]] · [[Token-Economics-and-Cost-Optimization-for-Production-LLM-Systems|Token Economics and Cost Optimization for Production LLM Systems]] · [[Cognitive-Science-Foundations-of-LLM-Reasoning-Techniques|Cognitive Science Foundations of LLM Reasoning Techniques]] · [[Multi-Agent-Architectures-and-Agentic-Workflows|Multi-Agent Architectures and Agentic Workflows]] · [[Evaluation-Methodologies-for-LLM-Reasoning-Quality|Evaluation Methodologies for LLM Reasoning Quality]] · [[Safety-and-Alignment-Considerations-in-Advanced-Reasoning-Systems|Safety and Alignment Considerations in Advanced Reasoning Systems]]

---

**Related concepts** *(from claudes-extended-thinking.md, report-claudes-extended-thinking-acrchitecture.md)*:
[[Chain-of-Thought|Chain of Thought]] * [[Tree-of-Thoughts|Tree of Thoughts]] * [[Chain-of-Thought-Prompting|Chain of Thought Prompting]] * [[Wei-et-al.-2022|Wei et al. 2022]] * [[Yao-et-al.-2023|Yao et al. 2023]] * [[Wang-et-al.-2022|Wang et al. 2022]] * [[Shinn-et-al.-2023|Shinn et al. 2023]] * [[Chain-of-Verification|Chain of Verification]] * [[Dhuliawala-et-al.-2023|Dhuliawala et al. 2023]] * [[Prompt-Engineering-Taxonomy-and-Pattern-Library|Prompt Engineering Taxonomy and Pattern Library]] * [[Token-Economics-and-Cost-Optimization-for-Production-LLM-Systems|Token Economics and Cost Optimization for Production LLM Systems]] * [[Cognitive-Science-Foundations-of-LLM-Reasoning-Techniques|Cognitive Science Foundations of LLM Reasoning Techniques]] * [[Multi-Agent-Architectures-and-Agentic-Workflows|Multi-Agent Architectures and Agentic Workflows]] * [[Evaluation-Methodologies-for-LLM-Reasoning-Quality|Evaluation Methodologies for LLM Reasoning Quality]] * [[Safety-and-Alignment-Considerations-in-Advanced-Reasoning-Systems|Safety and Alignment Considerations in Advanced Reasoning Systems]]

**Related concepts** *(from [[claudes-extended-thinking]], [[report-claudes-extended-thinking-acrchitecture]])*:
[[Chain-of-Thought|Chain of Thought]] * [[Tree-of-Thoughts|Tree of Thoughts]] * [[Chain-of-Thought-Prompting|Chain of Thought Prompting]] * [[Wei-et-al.-2022|Wei et al. 2022]] * [[Yao-et-al.-2023|Yao et al. 2023]] * [[Wang-et-al.-2022|Wang et al. 2022]] * [[Shinn-et-al.-2023|Shinn et al. 2023]] * [[Chain-of-Verification|Chain of Verification]] * [[Dhuliawala-et-al.-2023|Dhuliawala et al. 2023]] * [[Prompt-Engineering-Taxonomy-and-Pattern-Library|Prompt Engineering Taxonomy and Pattern Library]] * [[Token-Economics-and-Cost-Optimization-for-Production-LLM-Systems|Token Economics and Cost Optimization for Production LLM Systems]] * [[Cognitive-Science-Foundations-of-LLM-Reasoning-Techniques|Cognitive Science Foundations of LLM Reasoning Techniques]] * [[Multi-Agent-Architectures-and-Agentic-Workflows|Multi-Agent Architectures and Agentic Workflows]] * [[Evaluation-Methodologies-for-LLM-Reasoning-Quality|Evaluation Methodologies for LLM Reasoning Quality]] * [[Safety-and-Alignment-Considerations-in-Advanced-Reasoning-Systems|Safety and Alignment Considerations in Advanced Reasoning Systems]]

**Related concepts** *(from [[claudes-extended-thinking]], [[report-claudes-extended-thinking-acrchitecture]])*:
[[Chain-of-Thought|Chain of Thought]] * [[Tree-of-Thoughts|Tree of Thoughts]] * [[Chain-of-Thought-Prompting|Chain of Thought Prompting]] * [[Wei-et-al.-2022|Wei et al. 2022]] * [[Yao-et-al.-2023|Yao et al. 2023]] * [[Wang-et-al.-2022|Wang et al. 2022]] * [[Shinn-et-al.-2023|Shinn et al. 2023]] * [[Chain-of-Verification|Chain of Verification]] * [[Dhuliawala-et-al.-2023|Dhuliawala et al. 2023]] * [[Prompt-Engineering-Taxonomy-and-Pattern-Library|Prompt Engineering Taxonomy and Pattern Library]] * [[Token-Economics-and-Cost-Optimization-for-Production-LLM-Systems|Token Economics and Cost Optimization for Production LLM Systems]] * [[Cognitive-Science-Foundations-of-LLM-Reasoning-Techniques|Cognitive Science Foundations of LLM Reasoning Techniques]] * [[Multi-Agent-Architectures-and-Agentic-Workflows|Multi-Agent Architectures and Agentic Workflows]] * [[Evaluation-Methodologies-for-LLM-Reasoning-Quality|Evaluation Methodologies for LLM Reasoning Quality]] * [[Safety-and-Alignment-Considerations-in-Advanced-Reasoning-Systems|Safety and Alignment Considerations in Advanced Reasoning Systems]]




## Source Attribution

**Extracted from:** [[claudes-extended-thinking]]
