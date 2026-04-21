---
title: "Optimized Agent Fleet"
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

# Optimized Agent Fleet

> [!definition] Optimized Agent Fleet
> *Definition pending — derived from 2 source report(s).*

## Examples

> [!example] Optimized Agent Fleet
> **Coordinator** (Sonnet 4.5):
> ```yaml
> name: project-orchestrator
> model: sonnet
> # Needs: Complex task analysis, delegation decisions, synthesis
> ```
>
> **Worker Agents** (Haiku 4.5):
> ```yaml
> name: test-generator
> model: haiku
> # Clear patterns: input → test cases → output
>
> name: documentation-writer  
> model: haiku
> # Routine work: code → docstrings, well-defined task
>
> name: code-formatter
> model: haiku
> # Mechanical task: code → formatted code
> ```
>
> **Quality Gates** (Opus 4):
> ```yaml
> name: architecture-reviewer
> model: opus
> # Critical decisions: design validation, long-term impact
>
> name: security-auditor
> model: opus  
> # High stakes: security vulnerabilities must not be missed
> ```
>
> **Cost impact**: Majority of invocations use Haiku (70%), some Sonnet (25%), rare Opus (5%) = ~60-70% overall cost reduction vs. all-Sonnet fleet.
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!example] Optimized Agent Fleet
> **Coordinator** (Sonnet 4.5):
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!example] Optimized Agent Fleet
> **Coordinator** (Sonnet 4.5):
> ```yaml
> name: project-orchestrator
> model: sonnet
> # Needs: Complex task analysis, delegation decisions, synthesis
> ```
>
> **Worker Agents** (Haiku 4.5):
> ```yaml
> name: test-generator
> model: haiku
> # Clear patterns: input → test cases → output
>
> name: documentation-writer  
> model: haiku
> # Routine work: code → docstrings, well-defined task
>
> name: code-formatter
> model: haiku
> # Mechanical task: code → formatted code
> ```
>
> **Quality Gates** (Opus 4):
> ```yaml
> name: architecture-reviewer
> model: opus
> # Critical decisions: design validation, long-term impact
>
> name: security-auditor
> model: opus  
> # High stakes: security vulnerabilities must not be missed
> ```
>
> **Cost impact**: Majority of invocations use Haiku (70%), some Sonnet (25%), rare Opus (5%) = ~60-70% overall cost reduction vs. all-Sonnet fleet.
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Optimized Agent Fleet]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
