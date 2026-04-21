---
title: "Multiple VSCode Terminals Pattern"
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

# Multiple VSCode Terminals Pattern

> [!definition] Multiple VSCode Terminals Pattern
> *Definition pending — derived from 2 source report(s).*

## Examples

> [!example] Multiple VSCode Terminals Pattern
> **Simple but powerful**: Run separate Claude Code instances in multiple terminals:
>
> ```
> Terminal 1 (architect):
> $ cd /project
> $ claude
> > I'm the architect agent. I'll read MULTI_AGENT_PLAN.md,
>   design the solution, then update my task status.
>
> Terminal 2 (builder):  
> $ cd /project
> $ claude
> > I'm the builder agent. Waiting for architect to set
>   status READY_FOR_BUILD, then I'll implement.
>
> Terminal 3 (validator):
> $ cd /project
> $ claude  
> > I'm the validator agent. Monitoring for status READY_FOR_TEST,
>   then I'll run integration tests.
> ```
>
> **Coordination**: Agents coordinate through the shared markdown file, no complex frameworks needed.
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!example] Multiple VSCode Terminals Pattern
> **Simple but powerful**: Run separate Claude Code instances in multiple terminals:
>
> ```
> Terminal 1 (architect):
> $ cd /project
> $ claude
> > I'm the architect agent. I'll read MULTI_AGENT_PLAN.md,
>   design the solution, then update my task status.
>
> Terminal 2 (builder):  
> $ cd /project
> $ claude
> > I'm the builder agent. Waiting for architect to set
>   status READY_FOR_BUILD, then I'll implement.
>
> Terminal 3 (validator):
> $ cd /project
> $ claude  
> > I'm the validator agent. Monitoring for status READY_FOR_TEST,
>   then I'll run integration tests.
> ```
>
> **Coordination**: Agents coordinate through the shared markdown file, no complex frameworks needed.
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Multiple VSCode Terminals Pattern]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
