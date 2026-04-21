---
title: "Markdown State Protocol"
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

# Markdown State Protocol

> [!definition] Markdown State Protocol
> *Definition pending — derived from 2 source report(s).*

## Examples

> [!example] Markdown State Protocol
> **MULTI_AGENT_PLAN.md**:
> ```markdown
> # Project: User Dashboard
> **Created**: 2026-01-06  
> **Last Updated**: 2026-01-06 15:45
>
> ## Active Features
>
> ### Feature: Analytics Widget
> - **Slug**: analytics-widget
> - **Status**: IN_PROGRESS
> - **Assigned To**: frontend-specialist
> - **Started**: 2026-01-06 15:30
> - **Progress**: 60%
> - **Blockers**: None
> - **Next Check**: 2026-01-06 16:00
>
> ### Feature: Export Functionality  
> - **Slug**: export-csv
> - **Status**: READY_FOR_BUILD
> - **Assigned To**: backend-engineer
> - **Dependencies**: analytics-widget (data schema)
> - **Waiting Since**: 2026-01-06 15:45
> - **Expected Start**: 2026-01-06 16:00
>
> ## Completed Features
>
> ### Feature: User Authentication
> - **Completed**: 2026-01-06 14:20
> - **Implemented By**: backend-engineer
> - **Reviewed By**: security-auditor
> - **Tests**: ✅ All passing
> - **Deployed**: ✅ Production
>
> ---
>
> ## Status Definitions
> - **PLANNING**: Requirements being gathered
> - **READY_FOR_ARCH**: Ready for architecture review
> - **READY_FOR_BUILD**: Design approved, ready for implementation
> - **IN_PROGRESS**: Active implementation
> - **READY_FOR_REVIEW**: Implementation complete, needs review
> - **BLOCKED**: Waiting on dependency or decision
> - **DONE**: Complete and verified
>
> ---
>
> ## Agent Communication Log
>
> **2026-01-06 15:45 - frontend-specialist → backend-engineer**:
> Analytics widget needs these API endpoints:
> - GET /api/analytics/summary?range={7d,30d,90d}
> - GET /api/analytics/metrics?metric={users,sessions,conversions}
>
> Response format:
> ```json
> {
>   "data": [...],
>   "meta": { "range": "7d", "total": 1234 }
> }
> ```
>
> **2026-01-06 15:50 - backend-engineer → frontend-specialist**:
> Acknowledged. Will prioritize these endpoints after export-csv is unblocked.
> ETA: 2026-01-06 16:30
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!example] Markdown State Protocol
> **MULTI_AGENT_PLAN.md**:
> ```markdown
> # Project: User Dashboard
> **Created**: 2026-01-06  
> **Last Updated**: 2026-01-06 15:45
>
> ## Active Features
>
> ### Feature: Analytics Widget
> - **Slug**: analytics-widget
> - **Status**: IN_PROGRESS
> - **Assigned To**: frontend-specialist
> - **Started**: 2026-01-06 15:30
> - **Progress**: 60%
> - **Blockers**: None
> - **Next Check**: 2026-01-06 16:00
>
> ### Feature: Export Functionality  
> - **Slug**: export-csv
> - **Status**: READY_FOR_BUILD
> - **Assigned To**: backend-engineer
> - **Dependencies**: analytics-widget (data schema)
> - **Waiting Since**: 2026-01-06 15:45
> - **Expected Start**: 2026-01-06 16:00
>
> ## Completed Features
>
> ### Feature: User Authentication
> - **Completed**: 2026-01-06 14:20
> - **Implemented By**: backend-engineer
> - **Reviewed By**: security-auditor
> - **Tests**: ✅ All passing
> - **Deployed**: ✅ Production
>
> ---
>
> ## Status Definitions
> - **PLANNING**: Requirements being gathered
> - **READY_FOR_ARCH**: Ready for architecture review
> - **READY_FOR_BUILD**: Design approved, ready for implementation
> - **IN_PROGRESS**: Active implementation
> - **READY_FOR_REVIEW**: Implementation complete, needs review
> - **BLOCKED**: Waiting on dependency or decision
> - **DONE**: Complete and verified
>
> ---
>
> ## Agent Communication Log
>
> **2026-01-06 15:45 - frontend-specialist → backend-engineer**:
> Analytics widget needs these API endpoints:
> - GET /api/analytics/summary?range={7d,30d,90d}
> - GET /api/analytics/metrics?metric={users,sessions,conversions}
>
> Response format:
> ```json
> {
>   "data": [...],
>   "meta": { "range": "7d", "total": 1234 }
> }
> ```
>
> **2026-01-06 15:50 - backend-engineer → frontend-specialist**:
> Acknowledged. Will prioritize these endpoints after export-csv is unblocked.
> ETA: 2026-01-06 16:30
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Markdown State Protocol]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
