---
title: "Team Coordination Pitfalls"
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

# Team Coordination Pitfalls

> [!definition] Team Coordination Pitfalls
> *Definition pending — derived from 2 source report(s).*

## Practical Implications

> [!warning] Team Coordination Pitfalls
> **⚠️ Agent divergence**: Team members modify agents locally without committing
> - **Symptom**: "It works on my machine" but not others'
> - **Solution**: Enforce `.claude/agents/` in git, personal mods in `~/.claude/`
>
> **⚠️ Status confusion**: Different status interpretations
> - **Symptom**: Work proceeds when blocked, or waits unnecessarily
> - **Solution**: Explicit status definitions in AGENT_CONVENTIONS.md
>
> **⚠️ Conflicting agent modifications**: Two devs update same agent
> - **Symptom**: Git merge conflicts in agent definitions
> - **Solution**: Treat agents like code - PR review required for changes
>
> **⚠️ No communication protocol**: Agents can't coordinate across developers
> - **Symptom**: Duplicate work, conflicting approaches
> - **Solution**: Shared state files, status updates, communication log in state
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!warning] Team Coordination Pitfalls
> **⚠️ Agent divergence**: Team members modify agents locally without committing
> - **Symptom**: "It works on my machine" but not others'
> - **Solution**: Enforce `.claude/agents/` in git, personal mods in `~/.claude/`
>
> **⚠️ Status confusion**: Different status interpretations
> - **Symptom**: Work proceeds when blocked, or waits unnecessarily
> - **Solution**: Explicit status definitions in AGENT_CONVENTIONS.md
>
> **⚠️ Conflicting agent modifications**: Two devs update same agent
> - **Symptom**: Git merge conflicts in agent definitions
> - **Solution**: Treat agents like code - PR review required for changes
>
> **⚠️ No communication protocol**: Agents can't coordinate across developers
> - **Symptom**: Duplicate work, conflicting approaches
> - **Solution**: Shared state files, status updates, communication log in state
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!warning] Team Coordination Pitfalls
> **⚠️ Agent divergence**: Team members modify agents locally without committing
> - **Symptom**: "It works on my machine" but not others'
> - **Solution**: Enforce `.claude/agents/` in git, personal mods in `~/.claude/`
>
> **⚠️ Status confusion**: Different status interpretations
> - **Symptom**: Work proceeds when blocked, or waits unnecessarily
> - **Solution**: Explicit status definitions in AGENT_CONVENTIONS.md
>
> **⚠️ Conflicting agent modifications**: Two devs update same agent
> - **Symptom**: Git merge conflicts in agent definitions
> - **Solution**: Treat agents like code - PR review required for changes
>
> **⚠️ No communication protocol**: Agents can't coordinate across developers
> - **Symptom**: Duplicate work, conflicting approaches
> - **Solution**: Shared state files, status updates, communication log in state
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Team Coordination Pitfalls]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
