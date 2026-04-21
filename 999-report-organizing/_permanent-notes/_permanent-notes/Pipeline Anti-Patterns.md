---
title: "Pipeline Anti-Patterns"
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

# Pipeline Anti-Patterns

> [!definition] Pipeline Anti-Patterns
> *Definition pending — derived from 2 source report(s).*

## Practical Implications

> [!warning] Pipeline Anti-Patterns
> **❌ Skipping stages**: Don't jump from requirements directly to implementation
> - Causes architectural inconsistencies
> - Leads to rework when design flaws discovered late
>
> **❌ Parallel execution of sequential stages**: Don't run architect and implementer simultaneously
> - Creates merge conflicts
> - Implementation may not match final architecture
>
> **❌ No status tracking**: Don't rely on memory for handoffs
> - Human forgets which stage is complete
> - Multiple developers can't coordinate
>
> **✅ Solution**: Always use explicit status markers and shared state files
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!warning] Pipeline Anti-Patterns
> **❌ Skipping stages**: Don't jump from requirements directly to implementation
> - Causes architectural inconsistencies
> - Leads to rework when design flaws discovered late
>
> **❌ Parallel execution of sequential stages**: Don't run architect and implementer simultaneously
> - Creates merge conflicts
> - Implementation may not match final architecture
>
> **❌ No status tracking**: Don't rely on memory for handoffs
> - Human forgets which stage is complete
> - Multiple developers can't coordinate
>
> **✅ Solution**: Always use explicit status markers and shared state files
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Pipeline Anti-Patterns]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
