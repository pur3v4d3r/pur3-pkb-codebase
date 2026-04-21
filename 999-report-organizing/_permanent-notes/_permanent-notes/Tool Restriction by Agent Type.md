---
title: "Tool Restriction by Agent Type"
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

# Tool Restriction by Agent Type

> [!definition] Tool Restriction by Agent Type
> *Definition pending — derived from 2 source report(s).*

## Examples

> [!example] Tool Restriction by Agent Type
> **Documentation Writer** (read + limited write):
> ```yaml
> tools: Read, Write(docs/**), Write(README.md), Glob
> ```
> Can read entire codebase for understanding, but only write to documentation directories.
>
> **Security Auditor** (read-only + scanning):
> ```yaml
> tools: Read, Grep, Glob, Bash(npm audit), Bash(pip check)
> ```
> Can analyze everything, run security scanners, but cannot modify code or configuration.
>
> **Test Generator** (read + test write + test execution):
> ```yaml  
> tools: Read, Write(tests/**), Bash(npm test), Bash(pytest)
> ```
> Can read source code, write test files, run tests, but cannot modify source code.
>
> **Frontend Developer** (scoped read/write):
> ```yaml
> tools: Read, Write(src/components/**), Write(src/styles/**), Bash(npm run dev)
> ```
> Limited to frontend directories, cannot touch backend or infrastructure.
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!example] Tool Restriction by Agent Type
> **Documentation Writer** (read + limited write):
> ```yaml
> tools: Read, Write(docs/**), Write(README.md), Glob
> ```
> Can read entire codebase for understanding, but only write to documentation directories.
>
> **Security Auditor** (read-only + scanning):
> ```yaml
> tools: Read, Grep, Glob, Bash(npm audit), Bash(pip check)
> ```
> Can analyze everything, run security scanners, but cannot modify code or configuration.
>
> **Test Generator** (read + test write + test execution):
> ```yaml  
> tools: Read, Write(tests/**), Bash(npm test), Bash(pytest)
> ```
> Can read source code, write test files, run tests, but cannot modify source code.
>
> **Frontend Developer** (scoped read/write):
> ```yaml
> tools: Read, Write(src/components/**), Write(src/styles/**), Bash(npm run dev)
> ```
> Limited to frontend directories, cannot touch backend or infrastructure.
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Tool Restriction by Agent Type]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
