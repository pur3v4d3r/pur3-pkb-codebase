---
title: "Model Selection Decision Tree"
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

# Model Selection Decision Tree

> [!definition] Model Selection Decision Tree
> ```
> Is this task complex reasoning or novel problem-solving?
> ├─ YES → Use Opus 4 (deepest reasoning)
> └─ NO → Is routine/repetitive work with clear patterns?
>     ├─ YES → Use Haiku 4.5 (3x cost savings, 2x speed)
>     └─ NO → Use Sonnet 4.5 (balanced default)
>
> Special cases:
> - Orchestrator/coordinator: Sonnet 4.5 (needs maximum context understanding)
> - Quality validation: Opus 4 (critical quality gate)
> - Worker agents: Haiku 4.5 (volume tasks)
> ```

## Core Explanation

> [!evidence] Model Selection Decision Tree
> ```
> Is this task complex reasoning or novel problem-solving?
> ├─ YES → Use Opus 4 (deepest reasoning)
> └─ NO → Is routine/repetitive work with clear patterns?
>     ├─ YES → Use Haiku 4.5 (3x cost savings, 2x speed)
>     └─ NO → Use Sonnet 4.5 (balanced default)
>
> Special cases:
> - Orchestrator/coordinator: Sonnet 4.5 (needs maximum context understanding)
> - Quality validation: Opus 4 (critical quality gate)
> - Worker agents: Haiku 4.5 (volume tasks)
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Model Selection Decision Tree
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Model Selection Decision Tree
> ```
> Is this task complex reasoning or novel problem-solving?
> ├─ YES → Use Opus 4 (deepest reasoning)
> └─ NO → Is routine/repetitive work with clear patterns?
>     ├─ YES → Use Haiku 4.5 (3x cost savings, 2x speed)
>     └─ NO → Use Sonnet 4.5 (balanced default)
>
> Special cases:
> - Orchestrator/coordinator: Sonnet 4.5 (needs maximum context understanding)
> - Quality validation: Opus 4 (critical quality gate)
> - Worker agents: Haiku 4.5 (volume tasks)
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Model Selection Decision Tree]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
