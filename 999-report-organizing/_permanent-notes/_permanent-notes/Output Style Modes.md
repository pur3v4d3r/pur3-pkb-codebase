---
title: "Output Style Modes"
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

# Output Style Modes

> [!definition] Output Style Modes
> Three primary workflow modes in Claude Code:
>
> **Research Mode** (`/output-style research`)
> - Focus: Deep exploration and understanding
> - Agent pattern: Single agent deep dives, sequential investigation
> - Tools: Heavy use of Explore, web search, documentation fetching
> - Output: Comprehensive analysis documents
>
> **Planning Mode** (`/output-style planning`)
> - Focus: Architecture and design
> - Agent pattern: Architect-focused, may invoke research agents
> - Tools: Codebase analysis, design document generation
> - Output: Architectural decision records (ADRs), design specs
>
> **Execution Mode** (`/output-style execution`)  
> - Focus: Implementation and delivery
> - Agent pattern: Multi-agent coordination (frontend + backend + testing)
> - Tools: Full tool access for code generation and testing
> - Output: Working code, tests, documentation

## Core Explanation

> [!evidence] Output Style Modes
> Three primary workflow modes in Claude Code:
>
> **Research Mode** (`/output-style research`)
> - Focus: Deep exploration and understanding
> - Agent pattern: Single agent deep dives, sequential investigation
> - Tools: Heavy use of Explore, web search, documentation fetching
> - Output: Comprehensive analysis documents
>
> **Planning Mode** (`/output-style planning`)
> - Focus: Architecture and design
> - Agent pattern: Architect-focused, may invoke research agents
> - Tools: Codebase analysis, design document generation
> - Output: Architectural decision records (ADRs), design specs
>
> **Execution Mode** (`/output-style execution`)  
> - Focus: Implementation and delivery
> - Agent pattern: Multi-agent coordination (frontend + backend + testing)
> - Tools: Full tool access for code generation and testing
> - Output: Working code, tests, documentation
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Output Style Modes
> Three primary workflow modes in Claude Code:
>
> **Research Mode** (`/output-style research`)
> - Focus: Deep exploration and understanding
> - Agent pattern: Single agent deep dives, sequential investigation
> - Tools: Heavy use of Explore, web search, documentation fetching
> - Output: Comprehensive analysis documents
>
> **Planning Mode** (`/output-style planning`)
> - Focus: Architecture and design
> - Agent pattern: Architect-focused, may invoke research agents
> - Tools: Codebase analysis, design document generation
> - Output: Architectural decision records (ADRs), design specs
>
> **Execution Mode** (`/output-style execution`)  
> - Focus: Implementation and delivery
> - Agent pattern: Multi-agent coordination (frontend + backend + testing)
> - Tools: Full tool access for code generation and testing
> - Output: Working code, tests, documentation
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Output Style Modes]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
