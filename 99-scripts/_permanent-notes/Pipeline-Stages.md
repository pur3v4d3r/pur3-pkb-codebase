---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Pipeline Stages"
aliases:
  - "Pipeline Stages"
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
updated: 2026-03-19

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "multi-agent-systems-with-claude-code"
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

# Pipeline Stages

> [!definition] **Pipeline Stages**
> The canonical three-stage pattern:
> 
> **Stage 1: Requirements/Planning** (PM agent)
> - Input: User request, problem statement
> - Process: Clarifying questions, acceptance criteria definition
> - Output: Specification document, status set to READY_FOR_ARCH
> - Hand off: Architect agent triggered
> 
> **Stage 2: Architecture/Design** (Architect agent)  
> - Input: Specification from PM stage
> - Process: Design review, constraint validation, ADR creation
> - Output: Architecture document, status set to READY_FOR_BUILD
> - Handoff: Implementer agent triggered
> 
> **Stage 3: Implementation** (Implementer agent)
> - Input: Architecture from previous stage
> - Process: Code generation, test creation, documentation updates
> - Output: Working implementation, status set to DONE
> - Handoff: Human review or deployment pipeline

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
