---
title: "The MULTI_AGENT_PLAN.md Pattern"
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

# The MULTI_AGENT_PLAN.md Pattern

> [!definition] The MULTI_AGENT_PLAN.md Pattern
> A structured markdown file acting as the coordination hub:
>
> ```markdown
> # Multi-Agent Development Plan
>
> ## Task: Implement User Authentication
> - **Assigned To**: builder
> - **Status**: In Progress  
> - **Dependencies**: None
> - **Notes**: Using JWT tokens, coordinate with validator for test cases
> - **Last Updated**: 2026-01-06 14:32 by architect
>
> ## Task: Write Integration Tests
> - **Assigned To**: validator
> - **Status**: Pending
> - **Dependencies**: Waiting for builder to complete auth module
> - **Notes**: Need to verify token expiration, refresh flow
> - **Last Updated**: 2026-01-06 14:35 by validator
>
> ## Task: Security Audit
> - **Assigned To**: security-auditor
> - **Status**: Blocked
> - **Dependencies**: Integration tests must pass
> - **Notes**: Check for injection vulnerabilities, rate limiting
> - **Last Updated**: 2026-01-06 14:30 by project-manager
>
> ---
>
> ## Messages Between Agents
>
> ### Architect → Builder (14:32)
> The authentication flow should follow this pattern:
> 1. User submits credentials
> 2. Server validates against database
> 3. Generate JWT with user roles
> 4. Return token + refresh token
>
> **Important**: Include rate limiting on login endpoint (max 5 attempts/minute)
>
> ### Builder → Validator (14:40)
> Auth module completed. Key endpoints:
> - POST /auth/login
> - POST /auth/refresh
> - POST /auth/logout
>
> Test focus: Token expiration (15 min), refresh mechanism, logout invalidation
> ```

## Core Explanation

> [!evidence] The MULTI_AGENT_PLAN.md Pattern
> A structured markdown file acting as the coordination hub:
>
> ```markdown
> # Multi-Agent Development Plan
>
> ## Task: Implement User Authentication
> - **Assigned To**: builder
> - **Status**: In Progress  
> - **Dependencies**: None
> - **Notes**: Using JWT tokens, coordinate with validator for test cases
> - **Last Updated**: 2026-01-06 14:32 by architect
>
> ## Task: Write Integration Tests
> - **Assigned To**: validator
> - **Status**: Pending
> - **Dependencies**: Waiting for builder to complete auth module
> - **Notes**: Need to verify token expiration, refresh flow
> - **Last Updated**: 2026-01-06 14:35 by validator
>
> ## Task: Security Audit
> - **Assigned To**: security-auditor
> - **Status**: Blocked
> - **Dependencies**: Integration tests must pass
> - **Notes**: Check for injection vulnerabilities, rate limiting
> - **Last Updated**: 2026-01-06 14:30 by project-manager
>
> ---
>
> ## Messages Between Agents
>
> ### Architect → Builder (14:32)
> The authentication flow should follow this pattern:
> 1. User submits credentials
> 2. Server validates against database
> 3. Generate JWT with user roles
> 4. Return token + refresh token
>
> **Important**: Include rate limiting on login endpoint (max 5 attempts/minute)
>
> ### Builder → Validator (14:40)
> Auth module completed. Key endpoints:
> - POST /auth/login
> - POST /auth/refresh
> - POST /auth/logout
>
> Test focus: Token expiration (15 min), refresh mechanism, logout invalidation
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] The MULTI_AGENT_PLAN.md Pattern
> A structured markdown file acting as the coordination hub:
>
> ```markdown
> # Multi-Agent Development Plan
>
> ## Task: Implement User Authentication
> - **Assigned To**: builder
> - **Status**: In Progress  
> - **Dependencies**: None
> - **Notes**: Using JWT tokens, coordinate with validator for test cases
> - **Last Updated**: 2026-01-06 14:32 by architect
>
> ## Task: Write Integration Tests
> - **Assigned To**: validator
> - **Status**: Pending
> - **Dependencies**: Waiting for builder to complete auth module
> - **Notes**: Need to verify token expiration, refresh flow
> - **Last Updated**: 2026-01-06 14:35 by validator
>
> ## Task: Security Audit
> - **Assigned To**: security-auditor
> - **Status**: Blocked
> - **Dependencies**: Integration tests must pass
> - **Notes**: Check for injection vulnerabilities, rate limiting
> - **Last Updated**: 2026-01-06 14:30 by project-manager
>
> ---
>
> ## Messages Between Agents
>
> ### Architect → Builder (14:32)
> The authentication flow should follow this pattern:
> 1. User submits credentials
> 2. Server validates against database
> 3. Generate JWT with user roles
> 4. Return token + refresh token
>
> **Important**: Include rate limiting on login endpoint (max 5 attempts/minute)
>
> ### Builder → Validator (14:40)
> Auth module completed. Key endpoints:
> - POST /auth/login
> - POST /auth/refresh
> - POST /auth/logout
>
> Test focus: Token expiration (15 min), refresh mechanism, logout invalidation
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[The MULTI_AGENT_PLAN.md Pattern]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
