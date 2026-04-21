---
title: "Cascading Failures"
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

# Cascading Failures

> [!definition] Cascading Failures
> *Definition pending — derived from 2 source report(s).*

## Practical Implications

> [!warning] Cascading Failures
> **Problem**: One agent failure causes chain reaction
>
> ```
> Agent A fails → outputs invalid data
>   → Agent B processes invalid data → produces bad output
>      → Agent C uses bad output → makes wrong decisions
>         → Entire pipeline corrupted
> ```
>
> **Solution**: Validate outputs at each stage
> ```yaml
> # In each agent system prompt
>
> ## Output Validation
> Before setting status to COMPLETE:
> 1. Validate your output meets success criteria:
>    - Required fields present
>    - Data types correct
>    - Constraints satisfied
>    - Tests pass (if applicable)
>
> 2. If validation fails:
>    - DO NOT mark complete
>    - Set status: VALIDATION_FAILED
>    - Document what failed
>    - Do not pass bad data to next agent
>
> 3. Only after validation succeeds:
>    - Set status: COMPLETE
>    - Write output to expected location
>    - Update state for next agent
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!warning] Cascading Failures
> **Problem**: One agent failure causes chain reaction
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!warning] Cascading Failures
> **Problem**: One agent failure causes chain reaction
>
> ```
> Agent A fails → outputs invalid data
>   → Agent B processes invalid data → produces bad output
>      → Agent C uses bad output → makes wrong decisions
>         → Entire pipeline corrupted
> ```
>
> **Solution**: Validate outputs at each stage
> ```yaml
> # In each agent system prompt
>
> ## Output Validation
> Before setting status to COMPLETE:
> 1. Validate your output meets success criteria:
>    - Required fields present
>    - Data types correct
>    - Constraints satisfied
>    - Tests pass (if applicable)
>
> 2. If validation fails:
>    - DO NOT mark complete
>    - Set status: VALIDATION_FAILED
>    - Document what failed
>    - Do not pass bad data to next agent
>
> 3. Only after validation succeeds:
>    - Set status: COMPLETE
>    - Write output to expected location
>    - Update state for next agent
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Cascading Failures]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
