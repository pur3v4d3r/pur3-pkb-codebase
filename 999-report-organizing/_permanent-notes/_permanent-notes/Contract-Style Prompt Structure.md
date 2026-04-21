---
title: "Contract-Style Prompt Structure"
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

# Contract-Style Prompt Structure

> [!definition] Contract-Style Prompt Structure
> The optimal system prompt follows a contract format:
>
> ```markdown
> # [Agent Name] - [One-line role description]
>
> ## Role
> You are [specific expertise/domain specialist].
> [1-2 sentences defining core responsibility]
>
> ## When Invoked
> [Specific trigger conditions]
> [What situations require this agent]
>
> ## Success Criteria
> This invocation succeeds when:
> - [Measurable outcome 1]
> - [Measurable outcome 2]
> - [Measurable outcome 3]
>
> ## Workflow
> 1. [First step - be specific]
> 2. [Second step with tool usage if applicable]
> 3. [Analysis or processing step]
> 4. [Output generation step]
> 5. [Validation or review step]
>
> ## Key Practices
> - [Best practice 1 with rationale]
> - [Best practice 2 with examples]
> - [Best practice 3 with constraints]
>
> ## Constraints
> - [What NOT to do]
> - [Boundary conditions]
> - [Error handling requirements]
>
> ## Output Format
> [Structured output specification]
> ```

## Core Explanation

> [!evidence] Contract-Style Prompt Structure
> The optimal system prompt follows a contract format:
>
> ```markdown
> # [Agent Name] - [One-line role description]
>
> ## Role
> You are [specific expertise/domain specialist].
> [1-2 sentences defining core responsibility]
>
> ## When Invoked
> [Specific trigger conditions]
> [What situations require this agent]
>
> ## Success Criteria
> This invocation succeeds when:
> - [Measurable outcome 1]
> - [Measurable outcome 2]
> - [Measurable outcome 3]
>
> ## Workflow
> 1. [First step - be specific]
> 2. [Second step with tool usage if applicable]
> 3. [Analysis or processing step]
> 4. [Output generation step]
> 5. [Validation or review step]
>
> ## Key Practices
> - [Best practice 1 with rationale]
> - [Best practice 2 with examples]
> - [Best practice 3 with constraints]
>
> ## Constraints
> - [What NOT to do]
> - [Boundary conditions]
> - [Error handling requirements]
>
> ## Output Format
> [Structured output specification]
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Contract-Style Prompt Structure
> The optimal system prompt follows a contract format:
>
> ```markdown
> # [Agent Name] - [One-line role description]
>
> ## Role
> You are [specific expertise/domain specialist].
> [1-2 sentences defining core responsibility]
>
> ## When Invoked
> [Specific trigger conditions]
> [What situations require this agent]
>
> ## Success Criteria
> This invocation succeeds when:
> - [Measurable outcome 1]
> - [Measurable outcome 2]
> - [Measurable outcome 3]
>
> ## Workflow
> 1. [First step - be specific]
> 2. [Second step with tool usage if applicable]
> 3. [Analysis or processing step]
> 4. [Output generation step]
> 5. [Validation or review step]
>
> ## Key Practices
> - [Best practice 1 with rationale]
> - [Best practice 2 with examples]
> - [Best practice 3 with constraints]
>
> ## Constraints
> - [What NOT to do]
> - [Boundary conditions]
> - [Error handling requirements]
>
> ## Output Format
> [Structured output specification]
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Contract-Style Prompt Structure]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
