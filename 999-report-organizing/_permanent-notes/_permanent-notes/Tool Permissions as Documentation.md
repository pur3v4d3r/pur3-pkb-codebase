---
title: "Tool Permissions as Documentation"
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

# Tool Permissions as Documentation

> [!definition] Tool Permissions as Documentation
> *Definition pending — derived from 2 source report(s).*

## Core Explanation

> [!evidence] Tool Permissions as Documentation
> Tool restrictions serve as **implicit documentation** of agent responsibilities:
>
> ```yaml
> # This agent's tools tell you its role without reading the prompt
> name: database-migration-specialist
> tools: Read(migrations/**), Write(migrations/**), Bash(alembic), Bash(psql)
> ```
>
> You can immediately understand: This agent works exclusively with database migrations, can read/write migration files, and can run database tooling. It cannot touch application code or infrastructure.
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Tool Permissions as Documentation
> Tool restrictions serve as **implicit documentation** of agent responsibilities:
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Tool Permissions as Documentation
> Tool restrictions serve as **implicit documentation** of agent responsibilities:
>
> ```yaml
> # This agent's tools tell you its role without reading the prompt
> name: database-migration-specialist
> tools: Read(migrations/**), Write(migrations/**), Bash(alembic), Bash(psql)
> ```
>
> You can immediately understand: This agent works exclusively with database migrations, can read/write migration files, and can run database tooling. It cannot touch application code or infrastructure.
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Tool Permissions as Documentation]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
