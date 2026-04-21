---
title: "How Auto-Delegation Works"
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

# How Auto-Delegation Works

> [!definition] How Auto-Delegation Works
> *Definition pending — derived from 2 source report(s).*

## Methodology & Sources

> [!methodology-and-sources] How Auto-Delegation Works
> 1. **User query analysis**: Extract intent, domain, task type
> 2. **Agent description scan**: Compare query against all agent descriptions
> 3. **Relevance scoring**: Match keywords, trigger phrases, domain alignment
> 4. **Confidence threshold**: Only auto-invoke if match confidence is high
> 5. **Execution**: Invoke agent with query context
> 6. **Result synthesis**: Integrate agent output into response
>
> **Optimization**: Include terms like "use PROACTIVELY", "MUST BE USED", "automatically invoke when" in descriptions to boost auto-activation likelihood. This is effectively **Tool SEO** for agents.
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!methodology-and-sources] How Auto-Delegation Works
> 1. **User query analysis**: Extract intent, domain, task type
> 2. **Agent description scan**: Compare query against all agent descriptions
> 3. **Relevance scoring**: Match keywords, trigger phrases, domain alignment
> 4. **Confidence threshold**: Only auto-invoke if match confidence is high
> 5. **Execution**: Invoke agent with query context
> 6. **Result synthesis**: Integrate agent output into response
>
> **Optimization**: Include terms like "use PROACTIVELY", "MUST BE USED", "automatically invoke when" in descriptions to boost auto-activation likelihood. This is effectively **Tool SEO** for agents.
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[How Auto-Delegation Works]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
