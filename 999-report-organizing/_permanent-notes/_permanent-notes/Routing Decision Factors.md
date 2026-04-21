---
title: "Routing Decision Factors"
aliases: []
type: permanent-note
status: evergreen
confidence: high
domain: unknown
subdomains: []
tags: [permanent-note, unknown]
created: '2026-04-21'
updated: '2026-04-21'
complexity: intermediate
importance: medium
review-frequency: quarterly
mastery-stage: seedling
provenance:
  source-type: report-extraction
  pipeline-version: "3.0.0"
  source-reports: [multi-agent-systems-with-claude-code, multi-agent-systems-with-claude-code_report]
  extraction-method: pkb-extractor-v1 → pipeline-v3
---

# Routing Decision Factors

> [!definition] Routing Decision Factors
> The main agent considers:
>
> **1. Task complexity**:
> - Simple (single agent)
> - Moderate (2-3 agents sequentially)  
> - Complex (5+ agents, potentially parallel)
>
> **2. Domain matching**:
> - Keywords in user query vs. agent descriptions
> - Trigger phrase alignment
> - Explicit user requests ("use X agent")
>
> **3. Dependency analysis**:
> - Sequential: B depends on A's output
> - Parallel: A and B are independent
> - Conditional: C only needed if A finds issues
>
> **4. Resource constraints**:
> - Token budget (prefer Haiku agents for volume)
> - Time sensitivity (prefer parallel for speed)
> - Quality requirements (prefer Opus for critical tasks)

## Core Explanation

> [!evidence] Routing Decision Factors
> The main agent considers:
>
> **1. Task complexity**:
> - Simple (single agent)
> - Moderate (2-3 agents sequentially)  
> - Complex (5+ agents, potentially parallel)
>
> **2. Domain matching**:
> - Keywords in user query vs. agent descriptions
> - Trigger phrase alignment
> - Explicit user requests ("use X agent")
>
> **3. Dependency analysis**:
> - Sequential: B depends on A's output
> - Parallel: A and B are independent
> - Conditional: C only needed if A finds issues
>
> **4. Resource constraints**:
> - Token budget (prefer Haiku agents for volume)
> - Time sensitivity (prefer parallel for speed)
> - Quality requirements (prefer Opus for critical tasks)
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Routing Decision Factors
> The main agent considers:
>
> **1. Task complexity**:
> - Simple (single agent)
> - Moderate (2-3 agents sequentially)  
> - Complex (5+ agents, potentially parallel)
>
> **2. Domain matching**:
> - Keywords in user query vs. agent descriptions
> - Trigger phrase alignment
> - Explicit user requests ("use X agent")
>
> **3. Dependency analysis**:
> - Sequential: B depends on A's output
> - Parallel: A and B are independent
> - Conditional: C only needed if A finds issues
>
> **4. Resource constraints**:
> - Token budget (prefer Haiku agents for volume)
> - Time sensitivity (prefer parallel for speed)
> - Quality requirements (prefer Opus for critical tasks)
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Routing Decision Factors
> The main agent considers:
>
> **1. Task complexity**:
> - Simple (single agent)
> - Moderate (2-3 agents sequentially)  
> - Complex (5+ agents, potentially parallel)
>
> **2. Domain matching**:
> - Keywords in user query vs. agent descriptions
> - Trigger phrase alignment
> - Explicit user requests ("use X agent")
>
> **3. Dependency analysis**:
> - Sequential: B depends on A's output
> - Parallel: A and B are independent
> - Conditional: C only needed if A finds issues
>
> **4. Resource constraints**:
> - Token budget (prefer Haiku agents for volume)
> - Time sensitivity (prefer parallel for speed)
> - Quality requirements (prefer Opus for critical tasks)
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Routing Decision Factors]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
