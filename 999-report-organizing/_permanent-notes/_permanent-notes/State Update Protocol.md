---
title: "State Update Protocol"
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

# State Update Protocol

> [!definition] State Update Protocol
> *Definition pending — derived from 2 source report(s).*

## Methodology & Sources

> [!methodology-and-sources] State Update Protocol
> **Atomic state updates**:
>
> ```python
> # Agent state update script
> import fcntl  # File locking for atomic operations
> from pathlib import Path
>
> def update_agent_status(feature_slug, new_status, agent_name, notes):
>     state_file = Path('.claude/state/MULTI_AGENT_PLAN.md')
>
>     # 1. Acquire lock (prevents concurrent writes)
>     with open(state_file, 'r+') as f:
>         fcntl.flock(f.fileno(), fcntl.LOCK_EX)
>
>         # 2. Read current state
>         content = f.read()
>
>         # 3. Update status for this feature
>         updated = update_feature_status(
>             content,
>             feature_slug,
>             new_status,
>             agent_name,
>             notes
>         )
>
>         # 4. Write back atomically
>         f.seek(0)
>         f.write(updated)
>         f.truncate()
>
>         # 5. Release lock automatically on context exit
>
>     # 6. Log the update
>     log_state_change(feature_slug, new_status, agent_name)
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!methodology-and-sources] State Update Protocol
> **Atomic state updates**:
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!methodology-and-sources] State Update Protocol
> **Atomic state updates**:
>
> ```python
> # Agent state update script
> import fcntl  # File locking for atomic operations
> from pathlib import Path
>
> def update_agent_status(feature_slug, new_status, agent_name, notes):
>     state_file = Path('.claude/state/MULTI_AGENT_PLAN.md')
>
>     # 1. Acquire lock (prevents concurrent writes)
>     with open(state_file, 'r+') as f:
>         fcntl.flock(f.fileno(), fcntl.LOCK_EX)
>
>         # 2. Read current state
>         content = f.read()
>
>         # 3. Update status for this feature
>         updated = update_feature_status(
>             content,
>             feature_slug,
>             new_status,
>             agent_name,
>             notes
>         )
>
>         # 4. Write back atomically
>         f.seek(0)
>         f.write(updated)
>         f.truncate()
>
>         # 5. Release lock automatically on context exit
>
>     # 6. Log the update
>     log_state_change(feature_slug, new_status, agent_name)
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[State Update Protocol]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
