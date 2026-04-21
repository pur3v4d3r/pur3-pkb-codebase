---
title: "Complete Project Structure"
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

# Complete Project Structure

> [!definition] Complete Project Structure
> ```
> project-root/
> ├── .claude/
> │   ├── agents/                     # Project-specific agents
> │   │   ├── domain-expert.md       # Understands business logic
> │   │   ├── integration-tester.md  # Tests external API integrations
> │   │   └── architect.md           # System design specialist
> │   ├── commands/                   # Custom slash commands  
> │   │   ├── /review.md             # Comprehensive code review workflow
> │   │   ├── /deploy.md             # Deployment checklist execution
> │   │   └── /research.md           # Multi-agent research coordination
> │   ├── scripts/                    # Hook scripts and automation
> │   │   ├── handle_agent_completion.py
> │   │   ├── queue_next_agent.sh
> │   │   └── print_next_action.sh
> │   └── state/                      # Shared state files
> │       ├── MULTI_AGENT_PLAN.md    # Coordination hub
> │       └── features/               # Per-feature work areas
> │           ├── auth-system.md
> │           └── payment-gateway.md
> ├── CLAUDE.md                       # Project context
> ├── CLAUDE.local.md                 # Personal overrides (gitignored)
> └── .mcp.json                       # MCP server configuration
>
> ~/.claude/                           # User-level (global)
> ├── agents/
> │   ├── code-reviewer.md            # Personal code review preferences
> │   ├── security-auditor.md         # Global security standards
> │   └── documentation-writer.md     # Consistent doc style
> ├── commands/
> │   └── /daily-standup.md           # Personal workflow automation
> └── settings.json                   # Global configuration
> ```

## Core Explanation

> [!evidence] Complete Project Structure
> ```
> project-root/
> ├── .claude/
> │   ├── agents/                     # Project-specific agents
> │   │   ├── domain-expert.md       # Understands business logic
> │   │   ├── integration-tester.md  # Tests external API integrations
> │   │   └── architect.md           # System design specialist
> │   ├── commands/                   # Custom slash commands  
> │   │   ├── /review.md             # Comprehensive code review workflow
> │   │   ├── /deploy.md             # Deployment checklist execution
> │   │   └── /research.md           # Multi-agent research coordination
> │   ├── scripts/                    # Hook scripts and automation
> │   │   ├── handle_agent_completion.py
> │   │   ├── queue_next_agent.sh
> │   │   └── print_next_action.sh
> │   └── state/                      # Shared state files
> │       ├── MULTI_AGENT_PLAN.md    # Coordination hub
> │       └── features/               # Per-feature work areas
> │           ├── auth-system.md
> │           └── payment-gateway.md
> ├── CLAUDE.md                       # Project context
> ├── CLAUDE.local.md                 # Personal overrides (gitignored)
> └── .mcp.json                       # MCP server configuration
>
> ~/.claude/                           # User-level (global)
> ├── agents/
> │   ├── code-reviewer.md            # Personal code review preferences
> │   ├── security-auditor.md         # Global security standards
> │   └── documentation-writer.md     # Consistent doc style
> ├── commands/
> │   └── /daily-standup.md           # Personal workflow automation
> └── settings.json                   # Global configuration
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Complete Project Structure
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!evidence] Complete Project Structure
> ```
> project-root/
> ├── .claude/
> │   ├── agents/                     # Project-specific agents
> │   │   ├── domain-expert.md       # Understands business logic
> │   │   ├── integration-tester.md  # Tests external API integrations
> │   │   └── architect.md           # System design specialist
> │   ├── commands/                   # Custom slash commands  
> │   │   ├── /review.md             # Comprehensive code review workflow
> │   │   ├── /deploy.md             # Deployment checklist execution
> │   │   └── /research.md           # Multi-agent research coordination
> │   ├── scripts/                    # Hook scripts and automation
> │   │   ├── handle_agent_completion.py
> │   │   ├── queue_next_agent.sh
> │   │   └── print_next_action.sh
> │   └── state/                      # Shared state files
> │       ├── MULTI_AGENT_PLAN.md    # Coordination hub
> │       └── features/               # Per-feature work areas
> │           ├── auth-system.md
> │           └── payment-gateway.md
> ├── CLAUDE.md                       # Project context
> ├── CLAUDE.local.md                 # Personal overrides (gitignored)
> └── .mcp.json                       # MCP server configuration
>
> ~/.claude/                           # User-level (global)
> ├── agents/
> │   ├── code-reviewer.md            # Personal code review preferences
> │   ├── security-auditor.md         # Global security standards
> │   └── documentation-writer.md     # Consistent doc style
> ├── commands/
> │   └── /daily-standup.md           # Personal workflow automation
> └── settings.json                   # Global configuration
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Complete Project Structure]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
