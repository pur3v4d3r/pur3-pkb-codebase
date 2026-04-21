---
title: "Hook Configuration Architecture"
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

# Hook Configuration Architecture

> [!definition] Hook Configuration Architecture
> *Definition pending — derived from 2 source report(s).*

## Methodology & Sources

> [!methodology-and-sources] Hook Configuration Architecture
> Hooks are defined in `settings.json` at user or project scope:
>
> ```json
> {
>   "hooks": {
>     "SubagentStop": {
>       "command": "python .claude/scripts/handle_agent_completion.py",
>       "runIn": "project",
>       "env": {
>         "QUEUE_FILE": ".queue/features.md"
>       }
>     },
>     "Stop": {
>       "command": "bash .claude/scripts/print_next_action.sh",
>       "runIn": "project"  
>     },
>     "ToolStart": {
>       "command": "echo 'Tool started: ${TOOL_NAME}'",
>       "runIn": "user"
>     }
>   }
> }
> ```
>
> **Hook script responsibilities**:
> - Read current agent's output/status
> - Update shared state files
> - Determine next agent in pipeline
> - Print next action to stdout (appears in Claude conversation)
> - Log execution for audit trail
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!methodology-and-sources] Hook Configuration Architecture
> Hooks are defined in `settings.json` at user or project scope:
>
> ```json
> {
>   "hooks": {
>     "SubagentStop": {
>       "command": "python .claude/scripts/handle_agent_completion.py",
>       "runIn": "project",
>       "env": {
>         "QUEUE_FILE": ".queue/features.md"
>       }
>     },
>     "Stop": {
>       "command": "bash .claude/scripts/print_next_action.sh",
>       "runIn": "project"  
>     },
>     "ToolStart": {
>       "command": "echo 'Tool started: ${TOOL_NAME}'",
>       "runIn": "user"
>     }
>   }
> }
> ```
>
> **Hook script responsibilities**:
> - Read current agent's output/status
> - Update shared state files
> - Determine next agent in pipeline
> - Print next action to stdout (appears in Claude conversation)
> - Log execution for audit trail
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Hook Configuration Architecture]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
