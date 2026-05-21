---
title: Agent Scratchpad
aliases:
  - Agent Scratchpad
  - agent working memory
  - agent notepad
  - intermediate reasoning buffer
type: permanent-note
status: enriched
confidence: high
tags:
  - permanent-note
  - v6-llm-elaborated
  - prompt-engineering

domain: prompt-engineering
subdomains:
  - agent-frameworks
  - working-memory

created: 2026-05-20
updated: '2026-05-20'
source-type: report-extraction
source-reports:
  - agent-scratchpad-synthetic-seed-2026-05-20
evidence-quality: high
extraction-method: pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)
complexity-level: advanced-practitioner
depth-level: enhanced
parent-concept: Agentic Frameworks
related:
  - '[[Working Memory]]'
  - '[[Chain-of-Thought Prompting]]'
prerequisites:
  - '[[Working Memory]]'
specializes:
  - '[[]]'
broader:
  - '[[]]'
see-also:
  - '[[]]'
contrasts-with:
  - '[[]]'
contradicts:
  - '[[]]'
applies-to:
  - '[[Chain-of-Thought Prompting]]'
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
  last-enhanced: '2026-05-20'
---


# Agent Scratchpad

> [!definition] **Agent Scratchpad**
> Agent Scratchpad is a specialized section within an agent's context window designed to capture intermediate reasoning steps, tool outputs, partial conclusions, and working hypotheses during multi-step task execution. Unlike general working memory or other forms of persistent storage that do not accumulate evidence and planning state across sequences of actions, the Agent Scratchpad serves as an explicit working memory space tailored for large language models within agentic frameworks.

> [!attention] **Boundary**
> It should not be confused with general working memory or other forms of persistent storage that do not accumulate evidence and planning state across sequences of actions. It is specifically designed for the context of large language models and agentic frameworks.

## Core Explanation

Agent Scratchpad functions as a dedicated workspace where an agent can record its thought processes and findings during complex tasks. This externalization allows the reasoning process to be auditable, ensuring that each step is transparent and traceable. Without such a designated space, agents would need to recompute intermediate conclusions at every stage of task execution, leading to redundant computation and potential loss of critical insights.

The concept of Agent Scratchpad draws from cognitive science principles, particularly the notion of working memory as an active workspace for processing information. By externalizing this process into the context window, it mimics human problem-solving strategies where intermediate results are stored temporarily before synthesis into a final answer. This approach not only enhances efficiency but also ensures that key findings remain accessible throughout the task.

In practice, Agent Scratchpad accumulates evidence and planning states across multiple actions, allowing for iterative refinement of hypotheses and conclusions. This accumulation is crucial in long-running agentic tasks where early insights can inform later steps, preventing the need to rediscover information already processed. However, this reliance on a finite context window introduces challenges in managing capacity and content over time.

<!-- enhancement-pass:1 (2026-05-20) -->
The Agent Scratchpad's role in agentic frameworks is further enriched by its ability to facilitate reflective thinking, a process that involves stepping back from immediate problem-solving tasks to review and refine one’s approach. This reflective aspect allows agents to not only solve problems but also learn from the solutions they generate, potentially improving their performance on future similar tasks.

## Practical Implications

> [!example] **Application 1 — Instructional design**
> In instructional design for agentic frameworks, the Agent Scratchpad can significantly enhance task efficiency by reducing redundant computation. By allowing agents to store and reference intermediate findings, designers can create more streamlined workflows that minimize unnecessary recalculations. This not only speeds up task completion but also ensures that critical insights are retained throughout complex processes.

> [!example] **Application 2 — Long-running tasks**
> For long-running agentic tasks, the Agent Scratchpad plays a crucial role in maintaining continuity and preventing loss of key intermediate findings. As tasks progress, early important conclusions can be pushed out of effective attention range due to the finite context window. Effective management strategies such as compression or summarization are essential to prevent the scratchpad from becoming overcrowded and losing its utility.

## Key Distinctions

> [!key-distinction] **Agent Scratchpad vs general working memory**
> While both Agent Scratchpad and general working memory serve as temporary storage for processing information, they differ in their specific functions. General working memory is a broader concept that encompasses various forms of short-term cognitive processes without the explicit accumulation of evidence across sequences of actions. In contrast, the Agent Scratchpad is specifically designed to capture and retain intermediate reasoning steps and findings within large language models.

<!-- enhancement-pass:1 (2026-05-20) -->

> [!key-distinction] **Reflective vs Reactive Thinking**
> Reflective thinking involves deliberate review and analysis of past actions or decisions, whereas reactive thinking is characterized by immediate responses to stimuli without prior deliberation. The Agent Scratchpad supports reflective thinking by enabling agents to revisit and refine their reasoning steps, enhancing learning and adaptability over time.

## Common Misconceptions

<!-- enhancement-pass:1 (2026-05-20) -->

> [!warning] **Misconception** — People think that Agent Scratchpad is just another form of general working memory.
>
> While both serve as temporary storage for information processing, the Agent Scratchpad specifically accumulates evidence and planning states across sequences of actions. This accumulation allows agents to build upon previous insights without needing to rediscover them, a feature not inherent in general working memory.

## Open Questions

> [!open-question] **Question**
> How can Agent Scratchpad capacity be managed effectively?
>
> *What would resolve it:* Research into effective strategies for managing the finite capacity of Agent Scratchpad, such as compression techniques or structured note-taking methods, would resolve this question.

> [!open-question] **Question**
> What are the most effective summarization strategies for Agent Scratchpad content?
>
> *What would resolve it:* Experimental studies comparing different summarization approaches and their impact on task efficiency and information retention in agentic frameworks could provide insights into optimal practices.

<!-- enhancement-pass:1 (2026-05-20) -->

> [!open-question] **Question**
> How does the capacity management of Agent Scratchpad affect long-term learning outcomes?
>
> *What would resolve it:* Research into how different strategies for managing scratchpad capacity impact an agent's ability to retain and apply learned information over time would provide valuable insights.

## Synthesis

Agent Scratchpad is a critical component in enhancing the reasoning processes of large language models within agentic frameworks. By providing an explicit working memory space, it supports efficient multi-step task execution while maintaining transparency and audibility throughout the process. This capability not only improves task efficiency but also ensures that key intermediate findings are preserved, making it indispensable for complex problem-solving tasks.

<!-- enhancement-pass:1 (2026-05-20) -->
In summary, the Agent Scratchpad not only serves as a critical tool for enhancing task efficiency in agentic frameworks but also plays a pivotal role in fostering reflective thinking and learning. By supporting iterative refinement of reasoning processes, it enables agents to adapt and improve over time.

## Connections & Context

**Falls under:** [[Agentic Frameworks]]

**Prerequisites:** [[Working Memory]]

**Applies to:** [[Chain-of-Thought Prompting]]

**Source:** [[agent-scratchpad-synthetic-seed-2026-05-20]]

<!-- enhancement-pass:1 (2026-05-20) -->

### Why these connections matter

> [!connection] **[[Working Memory]]** — *prerequisites*
> The concept of Working Memory provides the foundational cognitive architecture that underpins the functionality of Agent Scratchpad. Just as working memory temporarily holds and manipulates information for tasks, the Agent Scratchpad extends this principle to large language models, ensuring that intermediate reasoning steps are accessible and usable across multiple actions.

> [!connection] **[[Chain-of-Thought Prompting]]** — *applies-to*
> Agent Scratchpad enhances Chain-of-Thought Prompting by providing a structured space for agents to articulate their thought processes. This not only aids in generating coherent and logical responses but also allows users to understand the reasoning behind an agent's conclusions, thereby improving transparency and trust.
