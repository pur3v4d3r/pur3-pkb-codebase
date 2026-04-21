---
title: "Tool Access Patterns"
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

# Tool Access Patterns

> [!definition] Tool Access Patterns
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

> [!evidence] Tool Access Patterns
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
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Tool Access Patterns
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
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Tool Access Patterns]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
