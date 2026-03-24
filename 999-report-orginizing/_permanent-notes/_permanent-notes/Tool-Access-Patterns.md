---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Tool Access Patterns"
aliases:
  - "Tool Access Patterns"
  - "TAP"
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
created: 2026-03-24
updated: 2026-03-24

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

# Tool Access Patterns

> [!definition] **Tool Access Patterns**
> **Full tool access** (omit `tools` field):
> - Agent inherits all tools from main thread
> - Use for: General-purpose agents, orchestrators, implementation agents
> - Risk: Can perform destructive operations
> 
> **Read-only access** (`tools: Read, Grep, Glob`):
> - Agent can analyze but not modify
> - Use for: Code reviewers, analyzers, documentation generators
> - Safety: Cannot accidentally break anything
> 
> **Restricted write** (`tools: Read, Write(src/**), Bash(npm test)`):
> - Agent can modify specific directories, run specific commands
> - Use for: Feature developers limited to their module
> - Balance: Productive but constrained
> 
> **No file access** (`tools: Bash(echo *)`):
> - Agent can only run whitelisted commands
> - Use for: Specialized utilities, formatters
> - Maximum safety: Isolated execution

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




## Methodology Notes

> [!methodology-and-sources] **Frontmatter Field Semantics**
> **`name`** (required): Identifier for explicit invocation ("Use the code-reviewer agent..."). Should be hyphenated lowercase.
> 
> **`description`** (required): [**Description-Field-Purpose**:: Natural language explanation of when this agent should be invoked; Claude analyzes this field during automatic delegation to match agent capabilities with task requirements.]^verified-stable This is the most critical field for automatic routing. Include terms like "use PROACTIVELY" or "MUST BE USED" to boost auto-activation.
> 
> **`tools`** (optional): [**Tool-Restriction-Pattern**:: Comma-separated list of…

---

## Source Attribution

**Extracted from:** [[multi-agent-systems-with-claude-code]]
