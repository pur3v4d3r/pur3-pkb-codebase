---
title: "Routing Algorithm"
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

# Routing Algorithm

> [!definition] Routing Algorithm
> *Definition pending — derived from 2 source report(s).*

## Methodology & Sources

> [!methodology-and-sources] Routing Algorithm
> Simplified pseudocode for main agent routing logic:
>
> ```python
> def route_task(user_query):
>     # 1. Parse user query
>     intent = extract_intent(user_query)
>     keywords = extract_keywords(user_query)
>     explicit_agent = check_explicit_invocation(user_query)
>
>     if explicit_agent:
>         return [explicit_agent]  # User specified agent
>
>     # 2. Score all agents against query
>     agent_scores = []
>     for agent in available_agents:
>         score = match_score(
>             agent.description,
>             keywords,
>             intent
>         )
>         agent_scores.append((agent, score))
>
>     # 3. Select best matches above threshold
>     candidates = [
>         agent for agent, score in agent_scores
>         if score > CONFIDENCE_THRESHOLD
>     ]
>
>     # 4. Determine execution strategy
>     if len(candidates) == 1:
>         return sequential([candidates[0]])
>
>     dependencies = analyze_dependencies(candidates)
>     if has_dependencies(dependencies):
>         return sequential(order_by_dependencies(candidates))
>     else:
>         return parallel(candidates)
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!methodology-and-sources] Routing Algorithm
> Simplified pseudocode for main agent routing logic:
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!methodology-and-sources] Routing Algorithm
> Simplified pseudocode for main agent routing logic:
>
> ```python
> def route_task(user_query):
>     # 1. Parse user query
>     intent = extract_intent(user_query)
>     keywords = extract_keywords(user_query)
>     explicit_agent = check_explicit_invocation(user_query)
>
>     if explicit_agent:
>         return [explicit_agent]  # User specified agent
>
>     # 2. Score all agents against query
>     agent_scores = []
>     for agent in available_agents:
>         score = match_score(
>             agent.description,
>             keywords,
>             intent
>         )
>         agent_scores.append((agent, score))
>
>     # 3. Select best matches above threshold
>     candidates = [
>         agent for agent, score in agent_scores
>         if score > CONFIDENCE_THRESHOLD
>     ]
>
>     # 4. Determine execution strategy
>     if len(candidates) == 1:
>         return sequential([candidates[0]])
>
>     dependencies = analyze_dependencies(candidates)
>     if has_dependencies(dependencies):
>         return sequential(order_by_dependencies(candidates))
>     else:
>         return parallel(candidates)
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Routing Algorithm]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
