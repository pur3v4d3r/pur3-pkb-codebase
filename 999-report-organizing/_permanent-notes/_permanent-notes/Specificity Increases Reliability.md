---
title: "Specificity Increases Reliability"
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

# Specificity Increases Reliability

> [!definition] Specificity Increases Reliability
> *Definition pending — derived from 2 source report(s).*

## Core Explanation

> [!evidence] Specificity Increases Reliability
> [**Prompt-Specificity-Principle**:: Vague instructions like "be thorough" or "follow best practices" lead to inconsistent agent behavior; specific, actionable steps with concrete examples produce deterministic, reliable outputs that can be evaluated and improved iteratively.]^verified-stable
>
> **Vague (❌)**:
> ```markdown
> You are a code reviewer. Review code for quality and best practices.
> Provide helpful feedback.
> ```
>
> **Specific (✅)**:
> ```markdown
> You are a code reviewer. Execute this exact workflow:
> 1. Run `git diff --staged` to see changes
> 2. For each modified function:
>    - Check cyclomatic complexity (flag if >10)
>    - Verify all parameters have type hints (Python) or TypeScript types
>    - Ensure docstrings exist for functions >5 lines
> 3. Check for:
>    - Hardcoded credentials (search for "password", "api_key" patterns)
>    - TODO/FIXME comments in production code
>    - Console.log/print statements (should use logger)
> 4. Generate report with line-specific findings in this format:
>    [file:line] [severity] [issue] - [specific fix]
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Specificity Increases Reliability
> [**Prompt-Specificity-Principle**:: Vague instructions like "be thorough" or "follow best practices" lead to inconsistent agent behavior; specific, actionable steps with concrete examples produce deterministic, reliable outputs that can be evaluated and improved iteratively.]^verified-stable
>
> **Vague (❌)**:
> ```markdown
> You are a code reviewer. Review code for quality and best practices.
> Provide helpful feedback.
> ```
>
> **Specific (✅)**:
> ```markdown
> You are a code reviewer. Execute this exact workflow:
> 1. Run `git diff --staged` to see changes
> 2. For each modified function:
>    - Check cyclomatic complexity (flag if >10)
>    - Verify all parameters have type hints (Python) or TypeScript types
>    - Ensure docstrings exist for functions >5 lines
> 3. Check for:
>    - Hardcoded credentials (search for "password", "api_key" patterns)
>    - TODO/FIXME comments in production code
>    - Console.log/print statements (should use logger)
> 4. Generate report with line-specific findings in this format:
>    [file:line] [severity] [issue] - [specific fix]
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Specificity Increases Reliability]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
