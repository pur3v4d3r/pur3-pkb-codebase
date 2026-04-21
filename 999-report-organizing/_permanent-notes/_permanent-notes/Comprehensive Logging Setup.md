---
title: "Comprehensive Logging Setup"
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

# Comprehensive Logging Setup

> [!definition] Comprehensive Logging Setup
> *Definition pending — derived from 2 source report(s).*

## Examples

> [!example] Comprehensive Logging Setup
> **Hook script for trace logging**:
>
> `.claude/scripts/log_agent_execution.py`:
> ```python
> import json
> import time
> from datetime import datetime
> from pathlib import Path
>
> class AgentExecutionLogger:
>     def __init__(self):
>         self.log_dir = Path('.claude/logs/executions')
>         self.log_dir.mkdir(parents=True, exist_ok=True)
>         self.session_id = datetime.now().strftime('%Y%m%d_%H%M%S')
>
>     def log_invocation(self, agent_name, trigger, context):
>         """Log when agent is invoked"""
>         log_entry = {
>             'timestamp': datetime.now().isoformat(),
>             'session_id': self.session_id,
>             'event': 'agent_invoked',
>             'agent_name': agent_name,
>             'trigger': trigger,  # 'automatic' or 'explicit'
>             'context': {
>                 'user_query': context.get('query'),
>                 'keywords_matched': context.get('keywords'),
>                 'confidence_score': context.get('confidence'),
>                 'parent_agent': context.get('parent')
>             }
>         }
>         self._write_log(log_entry)
>
>     def log_completion(self, agent_name, status, metrics):
>         """Log when agent completes"""
>         log_entry = {
>             'timestamp': datetime.now().isoformat(),
>             'session_id': self.session_id,
>             'event': 'agent_completed',
>             'agent_name': agent_name,
>             'status': status,  # 'success', 'failure', 'timeout'
>             'metrics': {
>                 'duration_seconds': metrics.get('duration'),
>                 'tokens_used': metrics.get('tokens'),
>                 'tools_invoked': metrics.get('tools'),
>                 'retry_count': metrics.get('retries', 0)
>             },
>             'output_summary': metrics.get('output_summary')
>         }
>         self._write_log(log_entry)
>
>     def log_error(self, agent_name, error_type, error_details):
>         """Log agent errors"""
>         log_entry = {
>             'timestamp': datetime.now().isoformat(),
>             'session_id': self.session_id,
>             'event': 'agent_error',
>             'agent_name': agent_name,
>             'error': {
>                 'type': error_type,
>                 'message': str(error_details),
>                 'severity': self._classify_severity(error_type)
>             }
>         }
>         self._write_log(log_entry)
>
>     def _write_log(self, entry):
>         log_file = self.log_dir / f'session_{self.session_id}.jsonl'
>         with open(log_file, 'a') as f:
>             f.write(json.dumps(entry) + '\n')
>
>     def _classify_severity(self, error_type):
>         severity_map = {
>             'ToolPermissionDenied': 'high',
>             'TokenLimitExceeded': 'medium',
>             'InvalidOutputFormat': 'low'
>         }
>         return severity_map.get(error_type, 'medium')
> ```
> *— [[multi-agent-systems-with-claude-code_report]]*

> [!example] Comprehensive Logging Setup
> **Hook script for trace logging**:
>
> `.claude/scripts/log_agent_execution.py`:
> ```python
> import json
> import time
> from datetime import datetime
> from pathlib import Path
>
> class AgentExecutionLogger:
>     def __init__(self):
>         self.log_dir = Path('.claude/logs/executions')
>         self.log_dir.mkdir(parents=True, exist_ok=True)
>         self.session_id = datetime.now().strftime('%Y%m%d_%H%M%S')
>
>     def log_invocation(self, agent_name, trigger, context):
>         """Log when agent is invoked"""
>         log_entry = {
>             'timestamp': datetime.now().isoformat(),
>             'session_id': self.session_id,
>             'event': 'agent_invoked',
>             'agent_name': agent_name,
>             'trigger': trigger,  # 'automatic' or 'explicit'
>             'context': {
>                 'user_query': context.get('query'),
>                 'keywords_matched': context.get('keywords'),
>                 'confidence_score': context.get('confidence'),
>                 'parent_agent': context.get('parent')
>             }
>         }
>         self._write_log(log_entry)
>
>     def log_completion(self, agent_name, status, metrics):
>         """Log when agent completes"""
>         log_entry = {
>             'timestamp': datetime.now().isoformat(),
>             'session_id': self.session_id,
>             'event': 'agent_completed',
>             'agent_name': agent_name,
>             'status': status,  # 'success', 'failure', 'timeout'
>             'metrics': {
>                 'duration_seconds': metrics.get('duration'),
>                 'tokens_used': metrics.get('tokens'),
>                 'tools_invoked': metrics.get('tools'),
>                 'retry_count': metrics.get('retries', 0)
>             },
>             'output_summary': metrics.get('output_summary')
>         }
>         self._write_log(log_entry)
>
>     def log_error(self, agent_name, error_type, error_details):
>         """Log agent errors"""
>         log_entry = {
>             'timestamp': datetime.now().isoformat(),
>             'session_id': self.session_id,
>             'event': 'agent_error',
>             'agent_name': agent_name,
>             'error': {
>                 'type': error_type,
>                 'message': str(error_details),
>                 'severity': self._classify_severity(error_type)
>             }
>         }
>         self._write_log(log_entry)
>
>     def _write_log(self, entry):
>         log_file = self.log_dir / f'session_{self.session_id}.jsonl'
>         with open(log_file, 'a') as f:
>             f.write(json.dumps(entry) + '\n')
>
>     def _classify_severity(self, error_type):
>         severity_map = {
>             'ToolPermissionDenied': 'high',
>             'TokenLimitExceeded': 'medium',
>             'InvalidOutputFormat': 'low'
>         }
>         return severity_map.get(error_type, 'medium')
> ```
> *— [[multi-agent-systems-with-claude-code]]*

## Connections

**Related:** [[Agent-Definition-File-Format]] · [[Agent-Observability-and-Debugging-Toolkit]] · [[Agentic-Workflow-Design-Patterns]] · [[Claude-Code-MCP-Server-Integration]] · [[Context-Isolation-Architecture]] · [[Conway's-Law]] · [[Description-Field-Optimization]] · [[DevOps-Practices]] · [[Distributed-Systems-Design]] · [[Enterprise-Multi-Agent-Governance]] · [[Enterprise-Software-Architecture]] · [[Error-Handling-in-Multi-Agent-Systems]] · [[Hook-Based-Automation]] · [[Knowledge-Work-Automation]] · [[Main-Agent-as-Coordinator]] · [[Model-Selection-Economics]] · [[Multi-Agent-AI-Systems]] · [[Multi-Agent-PKM-Automation]] · [[PKM-Systems]] · [[Production-Agent-Prompt-Library]] · [[Security-Governance]] · [[Sequential-Pipeline-Pattern]] · [[Shared-State-Coordination]] · [[Software-Engineering-Workflows]] · [[Team-Collaboration-Patterns]] · [[Tool-Restriction-Strategies]] · [[agent-file-format-specification]] · [[agent-prompt-engineering]] · [[agile-standups]] · [[bounded-contexts]] · [[circuit-breaker-pattern]] · [[claude-code-basics]] · [[claude-opus-4]] · [[claude-sonnet-4]] · [[claude.md-files]] · [[cognitive-load]] · [[coordination-pattern-library]] · [[custom-commands]] · [[event-driven-architecture]] · [[expertise-theory]] · [[hooks-system]] · [[mapreduce]] · [[mcp-servers]] · [[message-queues]] · [[microservices-architecture]] · [[output-styles]] · [[principle-of-least-privilege]] · [[prompt-engineering-fundamentals]] · [[skills]] · [[skills-system]] · [[state-management-protocols]] · [[tool-permission-grammar]] · [[working-memory]] · [[yaml-syntax]]

```dataview
LIST FROM [[Comprehensive Logging Setup]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[multi-agent-systems-with-claude-code]] · [[multi-agent-systems-with-claude-code_report]]
