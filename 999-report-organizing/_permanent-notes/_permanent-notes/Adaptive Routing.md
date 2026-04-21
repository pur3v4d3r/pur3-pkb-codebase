---
title: "Adaptive Routing"
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

# Adaptive Routing

> [!definition] Adaptive Routing
> *Definition pending — derived from 2 source report(s).*

## Core Explanation

> [!evidence] Adaptive Routing
> [**Adaptive-Routing-Behavior**:: The main agent learns from context and conversation history which agents are most effective for different task types; this creates implicit routing optimization where successful agent selections become more likely to be repeated for similar future tasks within the same conversation.]^verified-stable
>
> **Example**:
> ```
> Message 1: "Review this code for security"
> Main Agent → security-auditor (finds vulnerabilities)
>
> Message 10: "Review that other module too"
> Main Agent → security-auditor (remembers previous success)
>
> Message 20: "And the API endpoints?"  
> Main Agent → security-auditor (pattern reinforced)
> ```
>
> The conversation context teaches the main agent that "review" in this project context means "security review", not general code review.
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Adaptive Routing
> [**Adaptive-Routing-Behavior**:: The main agent learns from context and conversation history which agents are most effective for different task types; this creates implicit routing optimization where successful agent selections become more likely to be repeated for similar future tasks within the same conversation.]^verified-stable
>
> **Example**:
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Adaptive Routing
> [**Adaptive-Routing-Behavior**:: The main agent learns from context and conversation history which agents are most effective for different task types; this creates implicit routing optimization where successful agent selections become more likely to be repeated for similar future tasks within the same conversation.]^verified-stable
>
> **Example**:
> ```
> Message 1: "Review this code for security"
> Main Agent → security-auditor (finds vulnerabilities)
>
> Message 10: "Review that other module too"
> Main Agent → security-auditor (remembers previous success)
>
> Message 20: "And the API endpoints?"  
> Main Agent → security-auditor (pattern reinforced)
> ```
>
> The conversation context teaches the main agent that "review" in this project context means "security review", not general code review.
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Adaptive Routing]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
