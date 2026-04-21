---
title: "Task Decomposition Example"
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

# Task Decomposition Example

> [!definition] Task Decomposition Example
> *Definition pending — derived from 2 source report(s).*

## Examples

> [!example] Task Decomposition Example
> **User request**: "Refactor the authentication module for better security"
>
> **Main agent analysis**:
> ```
> Task: Authentication refactoring + security improvement
>
> Decomposition:
> ├─ Subtask 1: Security audit (identify vulnerabilities)
> │  └─ Agent: security-auditor (read-only, Opus for thorough review)
> │  └─ Reason: Must happen first to know what to fix
> │
> ├─ Subtask 2: Code refactoring (implement fixes)
> │  └─ Agent: backend-engineer (write access, Haiku for routine refactoring)
> │  └─ Reason: Depends on security audit findings
> │
> ├─ Subtask 3: Test generation (ensure no regressions)
> │  └─ Agent: test-engineer (write tests/**, Haiku for clear patterns)
> │  └─ Reason: Can happen parallel to refactoring (independent files)
> │
> └─ Subtask 4: Final review (validate improvements)
>    └─ Agent: code-quality-reviewer (read-only, Sonnet for synthesis)
>    └─ Reason: After implementation complete
>
> Execution plan:
> 1. security-auditor (sequential, required first)
> 2. backend-engineer + test-engineer (parallel, independent)
> 3. code-quality-reviewer (sequential, requires 2 complete)
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!example] Task Decomposition Example
> **User request**: "Refactor the authentication module for better security"
>
> **Main agent analysis**:
> ```
> Task: Authentication refactoring + security improvement
>
> Decomposition:
> ├─ Subtask 1: Security audit (identify vulnerabilities)
> │  └─ Agent: security-auditor (read-only, Opus for thorough review)
> │  └─ Reason: Must happen first to know what to fix
> │
> ├─ Subtask 2: Code refactoring (implement fixes)
> │  └─ Agent: backend-engineer (write access, Haiku for routine refactoring)
> │  └─ Reason: Depends on security audit findings
> │
> ├─ Subtask 3: Test generation (ensure no regressions)
> │  └─ Agent: test-engineer (write tests/**, Haiku for clear patterns)
> │  └─ Reason: Can happen parallel to refactoring (independent files)
> │
> └─ Subtask 4: Final review (validate improvements)
>    └─ Agent: code-quality-reviewer (read-only, Sonnet for synthesis)
>    └─ Reason: After implementation complete
>
> Execution plan:
> 1. security-auditor (sequential, required first)
> 2. backend-engineer + test-engineer (parallel, independent)
> 3. code-quality-reviewer (sequential, requires 2 complete)
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Task Decomposition Example]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
