---
title: "Description Optimization Before/After"
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

# Description Optimization Before/After

> [!definition] Description Optimization Before/After
> *Definition pending — derived from 2 source report(s).*

## Examples

> [!example] Description Optimization Before/After
> **Before (❌ weak auto-activation)**:
> ```yaml
> name: api-agent
> description: Helps with API stuff
> ```
> - Too vague
> - No trigger keywords
> - No domain specificity
>
> **After (✅ strong auto-activation)**:
> ```yaml
> name: api-designer
> description: |
>   Use PROACTIVELY for REST API design tasks. Expert API architect specializing in:
>   - Endpoint design and RESTful principles
>   - Request/response schema definition (OpenAPI, JSON Schema)
>   - API versioning strategies
>   - Authentication/authorization patterns (OAuth, JWT)
>   - Rate limiting and pagination design
>
>   Automatically invoke when:
>   - User mentions "API", "endpoint", "REST", "GraphQL"
>   - Designing backend architecture
>   - Defining service interfaces
>   - Planning microservices communication
>
>   NOT for implementation (use backend-engineer) or frontend API consumption.
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!example] Description Optimization Before/After
> **Before (❌ weak auto-activation)**:
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!example] Description Optimization Before/After
> **Before (❌ weak auto-activation)**:
> ```yaml
> name: api-agent
> description: Helps with API stuff
> ```
> - Too vague
> - No trigger keywords
> - No domain specificity
>
> **After (✅ strong auto-activation)**:
> ```yaml
> name: api-designer
> description: |
>   Use PROACTIVELY for REST API design tasks. Expert API architect specializing in:
>   - Endpoint design and RESTful principles
>   - Request/response schema definition (OpenAPI, JSON Schema)
>   - API versioning strategies
>   - Authentication/authorization patterns (OAuth, JWT)
>   - Rate limiting and pagination design
>
>   Automatically invoke when:
>   - User mentions "API", "endpoint", "REST", "GraphQL"
>   - Designing backend architecture
>   - Defining service interfaces
>   - Planning microservices communication
>
>   NOT for implementation (use backend-engineer) or frontend API consumption.
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Description Optimization BeforeAfter]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
