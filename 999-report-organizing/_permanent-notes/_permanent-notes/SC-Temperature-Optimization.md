---
title: "SC-Temperature-Optimization"
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
  source-reports: [claudes-extended-thinking_report, report-claudes-extended-thinking-acrchitecture_report]
  extraction-method: pkb-extractor-v1 → pipeline-v3
---

# SC-Temperature-Optimization

> [!definition] SC-Temperature-Optimization
> The critical parameter choice where too-low temperature (e.g., 0.3) produces near-identical samples (defeating the purpose), while too-high temperature (e.g., 1.0) increases random variation but may introduce errors—optimal range typically 0.6-0.8 for self-consistency applications.

## Core Explanation

> [!evidence] SC-Temperature-Optimization
> The critical parameter choice where too-low temperature (e.g., 0.3) produces near-identical samples (defeating the purpose), while too-high temperature (e.g., 1.0) increases random variation but may introduce errors—optimal range typically 0.6-0.8 for self-consistency applications.
> *— [[claudes-extended-thinking_report]]*

> [!evidence] SC-Temperature-Optimization
> The critical parameter choice where too-low temperature (e.g., 0.3) produces near-identical samples (defeating the purpose), while too-high temperature (e.g., 1.0) increases random variation but may introduce errors—optimal range typically 0.6-0.8 for self-consistency applications.
> *— [[report-claudes-extended-thinking-acrchitecture_report]]*

## Connections

**Related:** [[Chain-of-Thought]] · [[Chain-of-Thought-Prompting]] · [[Chain-of-Verification]] · [[Cognitive Science Foundations of LLM Reasoning Techniques]] · [[Dhuliawala et al. 2023]] · [[Evaluation Methodologies for LLM Reasoning Quality]] · [[Multi-Agent Architectures and Agentic Workflows]] · [[Prompt Engineering Taxonomy and Pattern Library]] · [[Reflexion]] · [[Safety and Alignment Considerations in Advanced Reasoning Systems]] · [[Self-Consistency]] · [[Shinn et al. 2023]] · [[Token Economics and Cost Optimization for Production LLM Systems]] · [[Tree-of-Thoughts]] · [[Wang-et-al.-2022]] · [[Wei-et-al.-2022]] · [[Yao et al. 2023]]

```dataview
LIST FROM [[SC-Temperature-Optimization]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[claudes-extended-thinking_report]] · [[report-claudes-extended-thinking-acrchitecture_report]]
