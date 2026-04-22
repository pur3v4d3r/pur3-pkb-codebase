---
title: JSON-RPC
aliases:
- JSON-RPC
type: permanent-note
status: enriched
confidence: low
tags:
- permanent-note
- seedling
- concept-stub
- other
domain: other
created: 2026-04-22
updated: '2026-04-22'
source-type: stub-generation
extraction-method: generate-stubs-v1 (auto-generated from wiki-link audit)
referenced-by-count: 134
see-also:
- '[[A-Debugging-Workflow-in-Practice|A Debugging Workflow in Practice]]'
- '[[A-Working-settings.json-for-Python-Development|A Working settings.json for Python
  Development]]'
- '[[AI-Agent-Development-and-Prompt-Engineering|AI Agent Development and Prompt Engineering]]'
- '[[AI-Assistance-vs.-Learning-Depth|AI Assistance vs. Learning Depth]]'
- '[[Abstract]]'
- '[[Annotation-Confidence-25|Annotation Confidence 25]]'
- '[[Annotation-Confidence-35|Annotation Confidence 35]]'
- '[[Annotation-Confidence-45|Annotation Confidence 45]]'
- '[[Annotation-Confidence-45-for-the-risks;-35-for-the-mitigations|Annotation Confidence
  45 for the risks; 35 for the mitigations]]'
- '[[Annotation-Coverage-Gap-—-Terminal-Proficiency-and-Command-Line-Development|Annotation
  Coverage Gap — Terminal Proficiency and Command-Line Development]]'
review-frequency: quarterly
mastery-stage: budding
importance: high
maturity: budding
provenance:
  enrichment-method: enrich_stubs-v1
  enrichment-model: qwen2.5:7b-instruct-q5_K_M
parent-moc:
- '[[software-engineering-and-development-moc]]'
---

# JSON-RPC

> [!definition] JSON-RPC
> - **Key-Term**: [[JSON-RPC]]
> - **Definition**: JSON-RPC is a remote procedure call protocol that uses JSON to encode its requests, notifications, and responses.
> - **Domain**: other
> - **Status**: 🌱 budding | Confidence: speculative

## Core Explanation

> [!analytical-insight] Core Explanation
> JSON-RPC allows clients to request procedures from servers in a simple and lightweight manner using HTTP or TCP/IP. It defines four message types: calls (requests), results (responses), errors, and notifications.

> [!analytical-insight] Explanation 2
> In practice, JSON-RPC is used for inter-process communication where the client sends a JSON-encoded request to the server, which processes it and returns a JSON-encoded response or error message.

> [!analytical-insight] Explanation 3
> Key nuances include its simplicity and ease of use, making it suitable for web applications and microservices. Sub-variants like JSON-RPC 2.0 introduce features such as batch requests and notifications.

## Practical Implications

> [!example] Application
> Concrete application in web development where client-side JavaScript can call server-side procedures seamlessly.

> [!example] Application
> Use in API design, particularly for lightweight services that need to be easily integrated with web applications.

## Connections

**Related:** [[HTTP]] · [[REST]] · [[RPC]]

**See Also (existing):**
- [[A-Debugging-Workflow-in-Practice|A Debugging Workflow in Practice]]
- [[A-Working-settings.json-for-Python-Development|A Working settings.json for Python Development]]
- [[AI-Agent-Development-and-Prompt-Engineering|AI Agent Development and Prompt Engineering]]
- [[AI-Assistance-vs.-Learning-Depth|AI Assistance vs. Learning Depth]]
- [[Abstract]]
- [[Annotation-Confidence-25|Annotation Confidence 25]]
- [[Annotation-Confidence-35|Annotation Confidence 35]]
- [[Annotation-Confidence-45|Annotation Confidence 45]]

```dataview
LIST FROM [[JSON-RPC]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** *(auto-enriched from domain knowledge)*