---
title: "Coordinator IS the Main Agent"
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

# Coordinator IS the Main Agent

> [!definition] Coordinator IS the Main Agent
> *Definition pending — derived from 2 source report(s).*

## Core Explanation

> [!evidence] Coordinator IS the Main Agent
> [**Coordinator-Architecture**:: The "coordinator agent" is not a separate agent file but rather the main Claude instance (general-purpose agent) that the user interacts with directly; it analyzes tasks, delegates to specialized subagents, aggregates results, and maintains high-level conversation continuity.]^verified-stable
>
> **This is a critical architectural insight**: You don't create a separate "coordinator.md" file. Instead, you influence the main agent's coordination behavior through:
> 1. Agent descriptions (what each agent does)
> 2. Output styles (workflow mode selection)
> 3. CLAUDE.md instructions (delegation patterns)
> 4. Custom commands (orchestration templates)
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Coordinator IS the Main Agent
> [**Coordinator-Architecture**:: The "coordinator agent" is not a separate agent file but rather the main Claude instance (general-purpose agent) that the user interacts with directly; it analyzes tasks, delegates to specialized subagents, aggregates results, and maintains high-level conversation continuity.]^verified-stable
>
> **This is a critical architectural insight**: You don't create a separate "coordinator.md" file. Instead, you influence the main agent's coordination behavior through:
> 1. Agent descriptions (what each agent does)
> 2. Output styles (workflow mode selection)
> 3. CLAUDE.md instructions (delegation patterns)
> 4. Custom commands (orchestration templates)
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Coordinator IS the Main Agent]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
