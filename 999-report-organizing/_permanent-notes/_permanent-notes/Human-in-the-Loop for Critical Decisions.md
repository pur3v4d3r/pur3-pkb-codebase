---
title: "Human-in-the-Loop for Critical Decisions"
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

# Human-in-the-Loop for Critical Decisions

> [!definition] Human-in-the-Loop for Critical Decisions
> *Definition pending — derived from 2 source report(s).*

## Core Explanation

> [!evidence] Human-in-the-Loop for Critical Decisions
> Some errors should **always** involve humans:
>
> **Automatic handling (no human needed)**:
> - Formatting errors (auto-fix with linters)
> - Test failures in feature branches (re-run or debug)
> - Resource temporarily unavailable (retry)
>
> **Human review required**:
> - Security vulnerabilities found (assess severity, plan fixes)
> - Database migration failures (risk of data loss)
> - Conflicting agent outputs (need human judgment)
> - Architecture decisions (long-term impact)
>
> **Hook implementation**:
> ```bash
> # .claude/scripts/notify_human.sh
>
> SEVERITY=$1
> MESSAGE=$2
>
> if [ "$SEVERITY" == "critical" ]; then
>     # Block further execution
>     echo "❌ CRITICAL ERROR - Human review required"
>     echo "$MESSAGE"
>     echo "To continue, resolve issue and run:"
>     echo "  ./claude continue-from-checkpoint"
>     exit 1
> fi
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Human-in-the-Loop for Critical Decisions
> Some errors should **always** involve humans:
>
> **Automatic handling (no human needed)**:
> - Formatting errors (auto-fix with linters)
> - Test failures in feature branches (re-run or debug)
> - Resource temporarily unavailable (retry)
>
> **Human review required**:
> - Security vulnerabilities found (assess severity, plan fixes)
> - Database migration failures (risk of data loss)
> - Conflicting agent outputs (need human judgment)
> - Architecture decisions (long-term impact)
>
> **Hook implementation**:
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Human-in-the-Loop for Critical Decisions
> Some errors should **always** involve humans:
>
> **Automatic handling (no human needed)**:
> - Formatting errors (auto-fix with linters)
> - Test failures in feature branches (re-run or debug)
> - Resource temporarily unavailable (retry)
>
> **Human review required**:
> - Security vulnerabilities found (assess severity, plan fixes)
> - Database migration failures (risk of data loss)
> - Conflicting agent outputs (need human judgment)
> - Architecture decisions (long-term impact)
>
> **Hook implementation**:
> ```bash
> # .claude/scripts/notify_human.sh
>
> SEVERITY=$1
> MESSAGE=$2
>
> if [ "$SEVERITY" == "critical" ]; then
>     # Block further execution
>     echo "❌ CRITICAL ERROR - Human review required"
>     echo "$MESSAGE"
>     echo "To continue, resolve issue and run:"
>     echo "  ./claude continue-from-checkpoint"
>     exit 1
> fi
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Human-in-the-Loop for Critical Decisions]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
