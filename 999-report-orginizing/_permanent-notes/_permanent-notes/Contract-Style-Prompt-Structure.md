---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Contract-Style Prompt Structure"
aliases:
  - "Contract-Style Prompt Structure"
  - "CPS"
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
  - claude-code
  - multi-agent-systems
  - ai-orchestration
  - agentic-architecture
  - prompt-engineering

domain: other
subdomains:
  - 

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-03-19
updated: 2026-03-20

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "multi-agent-systems-with-claude-code"
  - "multi-agent-systems-with-claude-code.md"
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
  - "[[Claude-Opus-4|Claude Opus 4]]"
  - "[[Claude-Sonnet-4|Claude Sonnet 4]]"
  - "[[Skills]]"
  - "[[Microservices-Architecture|Microservices Architecture]]"
  - "[[Bounded-Contexts|Bounded Contexts]]"
  - "[[Message-Queues|Message Queues]]"
  - "[[MapReduce]]"
  - "[[Event-Driven-Architecture|Event-Driven Architecture]]"
  - "[[Claude-Opus-4|Claude Opus 4]]"
  - "[[Claude-Sonnet-4|Claude Sonnet 4]]"
  - "[[Skills|Skills]]"
  - "[[Microservices-Architecture|Microservices Architecture]]"
  - "[[Bounded-Contexts|Bounded Contexts]]"
  - "[[Message-Queues|Message Queues]]"
  - "[[MapReduce|MapReduce]]"
  - "[[Event-Driven-Architecture|Event-Driven Architecture]]"

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

# Contract-Style Prompt Structure

> [!definition] **Contract-Style Prompt Structure**
> The optimal system prompt follows a contract format:
> 
> ```markdown
> # [Agent Name] - [One-line role description]
> 
> ## Role
> You are [specific expertise/domain specialist].
> [1-2 sentences defining core responsibility]
> 
> ## When Invoked
> [Specific trigger conditions]
> [What situations require this agent]
> 
> ## Success Criteria
> This invocation succeeds when:
> - [Measurable outcome 1]
> - [Measurable outcome 2]
> - [Measurable outcome 3]
> 
> ## Workflow
> 1. [First step - be specific]
> 2. [Second step with tool usage if applicable]
> 3. [Analysis or processing step]
> 4. [Output generation step]
> 5. [Validation or review step]
> 
> ## Key Practices
> - [Best practice 1 with rationale]
> - [Best practice 2 with examples]
> - [Best practice 3 with constraints]
> 
> ## Constraints
> - [What NOT to do]
> - [Boundary conditions]
> - [Error handling requirements]
> 
> ## Output Format
> [Structured output specification]
> ```

## Core Explanation

> [!analytical-insight] Key Insight
> [**Context-Isolation-Benefit**:: Each subagent maintains a separate conversation history and context window from the main agent and other subagents, preventing the "context pollution" that degrades performance in long conversations where unrelated information competes for attention and reduces focus on the current subtask.]^verified-stable
> 
> This isolation enables:
> - **Focus**: Subagents see only information relevant to their specialized task
> - **Scale**: Main conversation doesn't bloat with…

> [!analytical-insight] Key Insight
> [**Agent-Scope-Precedence**:: When agent names conflict between user-level and project-level definitions, project-level agents take precedence, allowing projects to override global agent behavior with domain-specific expertise while maintaining consistent agent names across the team.]^verified-stable

## Practical Implications

> [!example] **Application**
> *Describe how this concept applies in practice.*

> [!warning] **Key Distinction**
> **Problem**: If agents could spawn other agents recursively, you'd encounter:
> - **Infinite loops**: Agent A calls Agent B calls Agent A...
> - **Context explosion**: Each level creates new context windows
> - **Cost multipliers**: Exponential token consumption
> - **Debugging nightmares**: Non-deterministic execution trees
> 
> **Solution**: All delegation goes through the main agent, creating a **star topology** instead of a mesh network.

## Connections & Context

**Cross-report connections:**
- [[Claude-Code-Basics|Claude Code Basics]]
- [[CLAUDE.md-Files|CLAUDE.md Files]]
- [[Prompt-Engineering-Fundamentals|Prompt Engineering Fundamentals]]
- [[YAML-Syntax|YAML Syntax]]
- [[MCP-Servers|MCP Servers]]
- [[Custom-Commands|Custom Commands]]
- [[Skills-System|Skills System]]
- [[Output-Styles|Output Styles]]
- [[Hooks-System|Hooks System]]
- [[Agent-File-Format-Specification|Agent File Format Specification]]

**Related concepts:**
[[Claude-Opus-4|Claude Opus 4]] · [[Claude-Sonnet-4|Claude Sonnet 4]] · [[Skills]] · [[Microservices-Architecture|Microservices Architecture]] · [[Bounded-Contexts|Bounded Contexts]] · [[Message-Queues|Message Queues]] · [[MapReduce]] · [[Event-Driven-Architecture|Event-Driven Architecture]] · [[Circuit-Breaker-Pattern|Circuit Breaker Pattern]] · [[Conway's-Law|Conway's Law]] · [[Agile-Standups|Agile Standups]] · [[Principle-of-Least-Privilege|Principle of Least Privilege]] · [[Cognitive-Load|Cognitive Load]] · [[Expertise-Theory|Expertise Theory]] · [[Working-Memory|Working Memory]]

**Related concepts** *(from multi-agent-systems-with-claude-code.md)*:
[[Claude-Opus-4|Claude Opus 4]] * [[Claude-Sonnet-4|Claude Sonnet 4]] * [[Microservices-Architecture|Microservices Architecture]] * [[Bounded-Contexts|Bounded Contexts]] * [[Message-Queues|Message Queues]] * [[Event-Driven-Architecture|Event-Driven Architecture]] * [[Circuit-Breaker-Pattern|Circuit Breaker Pattern]] * [[Conway's-Law|Conway's Law]] * [[Agile-Standups|Agile Standups]] * [[Principle-of-Least-Privilege|Principle of Least Privilege]] * [[Cognitive-Load|Cognitive Load]] * [[Expertise-Theory|Expertise Theory]] * [[Working-Memory|Working Memory]] * [[Claude-Code-Basics|Claude Code Basics]] * [[CLAUDE.md-Files|CLAUDE.md Files]]

**Cross-report connections** *(from multi-agent-systems-with-claude-code.md)*:
- [[Claude-Code-Basics|Claude Code Basics]]
- [[CLAUDE.md-Files|CLAUDE.md Files]]
- [[Prompt-Engineering-Fundamentals|Prompt Engineering Fundamentals]]
- [[YAML-Syntax|YAML Syntax]]
- [[MCP-Servers|MCP Servers]]

**Cross-report connections** *(from multi-agent-systems-with-claude-code.md)*:
- [[Claude-Code-Basics|Claude Code Basics]]
- [[CLAUDE.md-Files|CLAUDE.md Files]]
- [[Prompt-Engineering-Fundamentals|Prompt Engineering Fundamentals]]
- [[YAML-Syntax|YAML Syntax]]
- [[MCP-Servers|MCP Servers]]



