---
title: "Extended Thinking Modes"
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
  source-reports: [claudes-extended-thinking, claudes-extended-thinking_report, report-claudes-extended-thinking-acrchitecture, report-claudes-extended-thinking-acrchitecture_report]
  extraction-method: pkb-extractor-v1 → pipeline-v3
---

# Extended Thinking Modes

> [!definition] Extended Thinking Modes
> Claude supports multiple thinking modes controlled via the `<thinking_mode>` parameter:
>
> - **`enabled`**: Thinking blocks generated when the model determines they would improve response quality
> - **`disabled`**: No thinking blocks generated (standard response mode)  
> - **`auto`**: Model autonomously decides when to use thinking based on task complexity
> - **`interleaved`**: Thinking can be interspersed with tool use and response generation for complex multi-step workflows

## Core Explanation

> [!evidence] Extended Thinking Modes
> Claude supports multiple thinking modes controlled via the `<thinking_mode>` parameter:
>
> - **`enabled`**: Thinking blocks generated when the model determines they would improve response quality
> - **`disabled`**: No thinking blocks generated (standard response mode)  
> - **`auto`**: Model autonomously decides when to use thinking based on task complexity
> - **`interleaved`**: Thinking can be interspersed with tool use and response generation for complex multi-step workflows
> *— [[claudes-extended-thinking_report]]*

> [!evidence] Extended Thinking Modes
> Claude supports multiple thinking modes controlled via the `<thinking_mode>` parameter:
>
> - **`enabled`**: Thinking blocks generated when the model determines they would improve response quality
> - **`disabled`**: No thinking blocks generated (standard response mode)  
> - **`auto`**: Model autonomously decides when to use thinking based on task complexity
> - **`interleaved`**: Thinking can be interspersed with tool use and response generation for complex multi-step workflows
> *— [[claudes-extended-thinking]]*

> [!evidence] Extended Thinking Modes
> Claude supports multiple thinking modes controlled via the `<thinking_mode>` parameter:
>
> - **`enabled`**: Thinking blocks generated when the model determines they would improve response quality
> - **`disabled`**: No thinking blocks generated (standard response mode)  
> - **`auto`**: Model autonomously decides when to use thinking based on task complexity
> - **`interleaved`**: Thinking can be interspersed with tool use and response generation for complex multi-step workflows
> *— [[report-claudes-extended-thinking-acrchitecture_report]]*

> [!evidence] Extended Thinking Modes
> Claude supports multiple thinking modes controlled via the `<thinking_mode>` parameter:
>
> - **`enabled`**: Thinking blocks generated when the model determines they would improve response quality
> - **`disabled`**: No thinking blocks generated (standard response mode)  
> - **`auto`**: Model autonomously decides when to use thinking based on task complexity
> - **`interleaved`**: Thinking can be interspersed with tool use and response generation for complex multi-step workflows
> *— [[report-claudes-extended-thinking-acrchitecture]]*

## Connections

**Related:** [[Chain-of-Thought]] · [[Chain-of-Thought-Prompting]] · [[Chain-of-Verification]] · [[Cognitive Science Foundations of LLM Reasoning Techniques]] · [[Dhuliawala et al. 2023]] · [[Evaluation Methodologies for LLM Reasoning Quality]] · [[Multi-Agent Architectures and Agentic Workflows]] · [[Prompt Engineering Taxonomy and Pattern Library]] · [[Reflexion]] · [[Safety and Alignment Considerations in Advanced Reasoning Systems]] · [[Self-Consistency]] · [[Shinn et al. 2023]] · [[Token Economics and Cost Optimization for Production LLM Systems]] · [[Tree-of-Thoughts]] · [[Wang-et-al.-2022]] · [[Wei-et-al.-2022]] · [[Yao et al. 2023]]

```dataview
LIST FROM [[Extended Thinking Modes]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[claudes-extended-thinking]] · [[claudes-extended-thinking_report]] · [[report-claudes-extended-thinking-acrchitecture]] · [[report-claudes-extended-thinking-acrchitecture_report]]
