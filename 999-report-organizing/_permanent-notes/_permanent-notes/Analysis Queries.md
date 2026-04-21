---
title: "Analysis Queries"
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

# Analysis Queries

> [!definition] Analysis Queries
> *Definition pending — derived from 2 source report(s).*

## Methodology & Sources

> [!methodology-and-sources] Analysis Queries
> **Query patterns for debugging**:
>
> ```python
> # Find all failed agent invocations
> def find_failures(session_id):
>     log_file = f'.claude/logs/executions/session_{session_id}.jsonl'
>     failures = []
>
>     with open(log_file) as f:
>         for line in f:
>             entry = json.loads(line)
>             if entry['event'] == 'agent_completed' and entry['status'] == 'failure':
>                 failures.append(entry)
>
>     return failures
>
> # Analyze agent performance  
> def agent_performance_report():
>     metrics = {}
>
>     for log_file in Path('.claude/logs/executions').glob('*.jsonl'):
>         with open(log_file) as f:
>             for line in f:
>                 entry = json.loads(line)
>                 if entry['event'] == 'agent_completed':
>                     agent = entry['agent_name']
>                     if agent not in metrics:
>                         metrics[agent] = {
>                             'invocations': 0,
>                             'successes': 0,
>                             'failures': 0,
>                             'total_duration': 0,
>                             'total_tokens': 0
>                         }
>
>                     metrics[agent]['invocations'] += 1
>                     if entry['status'] == 'success':
>                         metrics[agent]['successes'] += 1
>                     else:
>                         metrics[agent]['failures'] += 1
>
>                     m = entry['metrics']
>                     metrics[agent]['total_duration'] += m['duration_seconds']
>                     metrics[agent]['total_tokens'] += m['tokens_used']
>
>     # Calculate averages
>     for agent, data in metrics.items():
>         n = data['invocations']
>         data['avg_duration'] = data['total_duration'] / n
>         data['avg_tokens'] = data['total_tokens'] / n
>         data['success_rate'] = data['successes'] / n * 100
>
>     return metrics
>
> # Find coordination bottlenecks
> def find_bottlenecks(session_id):
>     """Identify agents that cause long wait times"""
>     log_file = f'.claude/logs/executions/session_{session_id}.jsonl'
>     events = []
>
>     with open(log_file) as f:
>         for line in f:
>             events.append(json.loads(line))
>
>     # Sort by timestamp
>     events.sort(key=lambda e: e['timestamp'])
>
>     # Find gaps
>     gaps = []
>     for i in range(len(events) - 1):
>         current = datetime.fromisoformat(events[i]['timestamp'])
>         next_event = datetime.fromisoformat(events[i+1]['timestamp'])
>         gap = (next_event - current).total_seconds()
>
>         if gap > 30:  # More than 30 second gap
>             gaps.append({
>                 'after_agent': events[i]['agent_name'],
>                 'before_agent': events[i+1]['agent_name'],
>                 'gap_seconds': gap
>             })
>
>     return sorted(gaps, key=lambda g: g['gap_seconds'], reverse=True)
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!methodology-and-sources] Analysis Queries
> **Query patterns for debugging**:
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!methodology-and-sources] Analysis Queries
> **Query patterns for debugging**:
>
> ```python
> # Find all failed agent invocations
> def find_failures(session_id):
>     log_file = f'.claude/logs/executions/session_{session_id}.jsonl'
>     failures = []
>
>     with open(log_file) as f:
>         for line in f:
>             entry = json.loads(line)
>             if entry['event'] == 'agent_completed' and entry['status'] == 'failure':
>                 failures.append(entry)
>
>     return failures
>
> # Analyze agent performance  
> def agent_performance_report():
>     metrics = {}
>
>     for log_file in Path('.claude/logs/executions').glob('*.jsonl'):
>         with open(log_file) as f:
>             for line in f:
>                 entry = json.loads(line)
>                 if entry['event'] == 'agent_completed':
>                     agent = entry['agent_name']
>                     if agent not in metrics:
>                         metrics[agent] = {
>                             'invocations': 0,
>                             'successes': 0,
>                             'failures': 0,
>                             'total_duration': 0,
>                             'total_tokens': 0
>                         }
>
>                     metrics[agent]['invocations'] += 1
>                     if entry['status'] == 'success':
>                         metrics[agent]['successes'] += 1
>                     else:
>                         metrics[agent]['failures'] += 1
>
>                     m = entry['metrics']
>                     metrics[agent]['total_duration'] += m['duration_seconds']
>                     metrics[agent]['total_tokens'] += m['tokens_used']
>
>     # Calculate averages
>     for agent, data in metrics.items():
>         n = data['invocations']
>         data['avg_duration'] = data['total_duration'] / n
>         data['avg_tokens'] = data['total_tokens'] / n
>         data['success_rate'] = data['successes'] / n * 100
>
>     return metrics
>
> # Find coordination bottlenecks
> def find_bottlenecks(session_id):
>     """Identify agents that cause long wait times"""
>     log_file = f'.claude/logs/executions/session_{session_id}.jsonl'
>     events = []
>
>     with open(log_file) as f:
>         for line in f:
>             events.append(json.loads(line))
>
>     # Sort by timestamp
>     events.sort(key=lambda e: e['timestamp'])
>
>     # Find gaps
>     gaps = []
>     for i in range(len(events) - 1):
>         current = datetime.fromisoformat(events[i]['timestamp'])
>         next_event = datetime.fromisoformat(events[i+1]['timestamp'])
>         gap = (next_event - current).total_seconds()
>
>         if gap > 30:  # More than 30 second gap
>             gaps.append({
>                 'after_agent': events[i]['agent_name'],
>                 'before_agent': events[i+1]['agent_name'],
>                 'gap_seconds': gap
>             })
>
>     return sorted(gaps, key=lambda g: g['gap_seconds'], reverse=True)
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Analysis Queries]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
