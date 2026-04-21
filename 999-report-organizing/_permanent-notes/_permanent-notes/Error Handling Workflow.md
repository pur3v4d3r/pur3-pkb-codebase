---
title: "Error Handling Workflow"
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

# Error Handling Workflow

> [!definition] Error Handling Workflow
> *Definition pending — derived from 2 source report(s).*

## Examples

> [!example] Error Handling Workflow
> **Scenario**: Backend engineer agent fails during database migration
>
> ```yaml
> # backend-engineer agent system prompt includes:
>
> ## Error Handling Protocol
>
> If you encounter an error:
> 1. **Classify severity**:
>    - Critical: Data loss risk, security vulnerability
>    - High: Feature broken, tests failing
>    - Medium: Partial functionality, warnings
>    - Low: Style issues, minor inconsistencies
>
> 2. **For Critical/High errors**:
>    - STOP immediately
>    - Document error in state file with severity
>    - Set status: BLOCKED
>    - DO NOT proceed or attempt fixes blindly
>    - Example:
>      ```markdown
>      Status: BLOCKED
>      Error: Database migration failed - constraint violation
>      Severity: Critical
>      Details: Column 'user_id' has null values but NOT NULL constraint added
>      Rollback: Migration rolled back automatically
>      Required action: Manual data cleanup or migration modification needed
>      ```
>
> 3. **For Medium errors**:
>    - Attempt automatic fix (1 retry)
>    - If retry fails, document and set status: NEEDS_REVIEW
>    - Continue with non-dependent tasks
>
> 4. **For Low errors**:
>    - Fix automatically
>    - Note in completion message
>    - Do not block progress
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!example] Error Handling Workflow
> **Scenario**: Backend engineer agent fails during database migration
>
> ```yaml
> # backend-engineer agent system prompt includes:
>
> ## Error Handling Protocol
>
> If you encounter an error:
> 1. **Classify severity**:
>    - Critical: Data loss risk, security vulnerability
>    - High: Feature broken, tests failing
>    - Medium: Partial functionality, warnings
>    - Low: Style issues, minor inconsistencies
>
> 2. **For Critical/High errors**:
>    - STOP immediately
>    - Document error in state file with severity
>    - Set status: BLOCKED
>    - DO NOT proceed or attempt fixes blindly
>    - Example:
>      ```markdown
>      Status: BLOCKED
>      Error: Database migration failed - constraint violation
>      Severity: Critical
>      Details: Column 'user_id' has null values but NOT NULL constraint added
>      Rollback: Migration rolled back automatically
>      Required action: Manual data cleanup or migration modification needed
>      ```
>
> 3. **For Medium errors**:
>    - Attempt automatic fix (1 retry)
>    - If retry fails, document and set status: NEEDS_REVIEW
>    - Continue with non-dependent tasks
>
> 4. **For Low errors**:
>    - Fix automatically
>    - Note in completion message
>    - Do not block progress
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Error Handling Workflow]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
