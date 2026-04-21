---
title: "State Management Approaches"
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

# State Management Approaches

> [!definition] State Management Approaches
> **1. Shared Markdown Files** (simplest):
> - Single truth source: MULTI_AGENT_PLAN.md
> - Agents read → execute → write updates
> - Human-readable state (can inspect/debug)
> - Version controlled (git tracks state changes)
>
> **2. JSON State Files** (structured):
> - .claude/state/features.json
> - Machine-readable for automation
> - Schema validation possible
> - Harder for humans to edit
>
> **3. File System State** (implicit):
> - Presence of files indicates status
> - docs/requirements/X.md exists → requirements complete
> - docs/architecture/ADR-X.md exists → design complete
> - src/features/X/ exists → implementation started
>
> **4. Git Branches** (advanced):
> - Each agent works in separate branch
> - Main agent merges when complete
> - Conflicts resolved explicitly
> - Full audit trail

## Core Explanation

> [!evidence] State Management Approaches
> **1. Shared Markdown Files** (simplest):
> - Single truth source: MULTI_AGENT_PLAN.md
> - Agents read → execute → write updates
> - Human-readable state (can inspect/debug)
> - Version controlled (git tracks state changes)
>
> **2. JSON State Files** (structured):
> - .claude/state/features.json
> - Machine-readable for automation
> - Schema validation possible
> - Harder for humans to edit
>
> **3. File System State** (implicit):
> - Presence of files indicates status
> - docs/requirements/X.md exists → requirements complete
> - docs/architecture/ADR-X.md exists → design complete
> - src/features/X/ exists → implementation started
>
> **4. Git Branches** (advanced):
> - Each agent works in separate branch
> - Main agent merges when complete
> - Conflicts resolved explicitly
> - Full audit trail
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] State Management Approaches
> **1. Shared Markdown Files** (simplest):
> - Single truth source: MULTI_AGENT_PLAN.md
> - Agents read → execute → write updates
> - Human-readable state (can inspect/debug)
> - Version controlled (git tracks state changes)
>
> **2. JSON State Files** (structured):
> - .claude/state/features.json
> - Machine-readable for automation
> - Schema validation possible
> - Harder for humans to edit
>
> **3. File System State** (implicit):
> - Presence of files indicates status
> - docs/requirements/X.md exists → requirements complete
> - docs/architecture/ADR-X.md exists → design complete
> - src/features/X/ exists → implementation started
>
> **4. Git Branches** (advanced):
> - Each agent works in separate branch
> - Main agent merges when complete
> - Conflicts resolved explicitly
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] State Management Approaches
> **1. Shared Markdown Files** (simplest):
> - Single truth source: MULTI_AGENT_PLAN.md
> - Agents read → execute → write updates
> - Human-readable state (can inspect/debug)
> - Version controlled (git tracks state changes)
>
> **2. JSON State Files** (structured):
> - .claude/state/features.json
> - Machine-readable for automation
> - Schema validation possible
> - Harder for humans to edit
>
> **3. File System State** (implicit):
> - Presence of files indicates status
> - docs/requirements/X.md exists → requirements complete
> - docs/architecture/ADR-X.md exists → design complete
> - src/features/X/ exists → implementation started
>
> **4. Git Branches** (advanced):
> - Each agent works in separate branch
> - Main agent merges when complete
> - Conflicts resolved explicitly
> - Full audit trail
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[State Management Approaches]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
