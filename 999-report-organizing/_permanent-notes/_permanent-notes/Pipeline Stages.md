---
title: "Pipeline Stages"
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

# Pipeline Stages

> [!definition] Pipeline Stages
> The canonical three-stage pattern:
>
> **Stage 1: Requirements/Planning** (PM agent)
> - Input: User request, problem statement
> - Process: Clarifying questions, acceptance criteria definition
> - Output: Specification document, status set to READY_FOR_ARCH
> - Hand off: Architect agent triggered
>
> **Stage 2: Architecture/Design** (Architect agent)  
> - Input: Specification from PM stage
> - Process: Design review, constraint validation, ADR creation
> - Output: Architecture document, status set to READY_FOR_BUILD
> - Handoff: Implementer agent triggered
>
> **Stage 3: Implementation** (Implementer agent)
> - Input: Architecture from previous stage
> - Process: Code generation, test creation, documentation updates
> - Output: Working implementation, status set to DONE
> - Handoff: Human review or deployment pipeline

## Core Explanation

> [!evidence] Pipeline Stages
> The canonical three-stage pattern:
>
> **Stage 1: Requirements/Planning** (PM agent)
> - Input: User request, problem statement
> - Process: Clarifying questions, acceptance criteria definition
> - Output: Specification document, status set to READY_FOR_ARCH
> - Hand off: Architect agent triggered
>
> **Stage 2: Architecture/Design** (Architect agent)  
> - Input: Specification from PM stage
> - Process: Design review, constraint validation, ADR creation
> - Output: Architecture document, status set to READY_FOR_BUILD
> - Handoff: Implementer agent triggered
>
> **Stage 3: Implementation** (Implementer agent)
> - Input: Architecture from previous stage
> - Process: Code generation, test creation, documentation updates
> - Output: Working implementation, status set to DONE
> - Handoff: Human review or deployment pipeline
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Pipeline Stages
> The canonical three-stage pattern:
>
> **Stage 1: Requirements/Planning** (PM agent)
> - Input: User request, problem statement
> - Process: Clarifying questions, acceptance criteria definition
> - Output: Specification document, status set to READY_FOR_ARCH
> - Hand off: Architect agent triggered
>
> **Stage 2: Architecture/Design** (Architect agent)  
> - Input: Specification from PM stage
> - Process: Design review, constraint validation, ADR creation
> - Output: Architecture document, status set to READY_FOR_BUILD
> - Handoff: Implementer agent triggered
>
> **Stage 3: Implementation** (Implementer agent)
> - Input: Architecture from previous stage
> - Process: Code generation, test creation, documentation updates
> - Output: Working implementation, status set to DONE
> - Handoff: Human review or deployment pipeline
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Pipeline Stages]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
