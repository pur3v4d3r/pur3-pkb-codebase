---
title: Single-Responsibility-Principle
aliases:
  - Single-Responsibility-Principle
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
referenced-by-count: 82
see-also:
  - '[[Bridging-to-Prior-Knowledge|Bridging to Prior Knowledge]]'
  - '[[Checklist-PKM-System-Design-Audit-Seven-Problem-Framework|Checklist PKM System Design Audit (Seven-Problem Framework)]]'
  - '[[Clinical-Decision-Support-Systems|Clinical Decision Support Systems]]'
  - '[[Cognitive-Load-Theory-Sweller,-1988;-Sweller-et-al.,-2011|Cognitive Load Theory (Sweller, 1988; Sweller et al., 2011)]]'
  - '[[Cognitive-Offloading-vs.-Cognitive-Engagement|Cognitive Offloading vs. Cognitive Engagement]]'
  - '[[Desirable-Difficulties-Bjork-&-Bjork,-1992;-2011|Desirable Difficulties (Bjork & Bjork, 1992; 2011)]]'
  - '[[Directions-for-Future-Investigation|Directions for Future Investigation]]'
  - '[[Dual-Process-Theory-and-its-Implications-for-Knowledge-Management-Decision-Makin|Dual-Process Theory and its Implications for Knowledge Management Decision-Making]]'
  - '[[Emergent-Organization-vs.-Imposed-Organization|Emergent Organization vs. Imposed Organization]]'
  - '[[Encoding-Depth-Craik-&-Lockhart,-1972|Encoding Depth (Craik & Lockhart, 1972)]]'

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: budding
importance: high
maturity: budding
provenance:
  enrichment-method: enrich_stubs-v1
  enrichment-model: qwen2.5:7b-instruct-q5_K_M
---

# Single-Responsibility-Principle

> [!definition] Single-Responsibility-Principle
> - **Key-Term**: [[Single-Responsibility-Principle]]
> - **Definition**: The Single-Responsibility Principle (SRP) is a design principle stating that a class should have one, and only one, reason to change, which means it should encapsulate only one responsibility or feature.
> - **Domain**: other
> - **Status**: 🌱 budding | Confidence: speculative

## Core Explanation

> [!analytical-insight] Core Explanation
> The SRP encourages developers to break down large classes into smaller, more manageable ones by focusing on a single aspect of functionality. This leads to code that is easier to understand, test, and maintain.

> [!analytical-insight] Explanation 2
> By adhering to the SRP, each class becomes responsible for only one part of the system's behavior, making it simpler to modify or extend without affecting other parts of the application.

> [!analytical-insight] Explanation 3
> Key nuances include distinguishing between responsibilities based on changes in requirements rather than just functionality. Sub-variants like the Interface Segregation Principle (ISP) further refine this concept by suggesting that no client should be forced to depend on methods it does not use.

## Practical Implications

> [!example] Application
> Improves code modularity and maintainability, making it easier to update or fix parts of the system without impacting others.

> [!example] Application
> Facilitates better testing as each class has a single responsibility, which can be tested independently.

## Connections

**Related:** [[Design-Patterns]] · [[Modularity]] · [[Test-Driven-Development]]

**See Also (existing):**
- [[Bridging-to-Prior-Knowledge|Bridging to Prior Knowledge]]
- [[Checklist-PKM-System-Design-Audit-Seven-Problem-Framework|Checklist PKM System Design Audit (Seven-Problem Framework)]]
- [[Clinical-Decision-Support-Systems|Clinical Decision Support Systems]]
- [[Cognitive-Load-Theory-Sweller,-1988;-Sweller-et-al.,-2011|Cognitive Load Theory (Sweller, 1988; Sweller et al., 2011)]]
- [[Cognitive-Offloading-vs.-Cognitive-Engagement|Cognitive Offloading vs. Cognitive Engagement]]
- [[Desirable-Difficulties-Bjork-&-Bjork,-1992;-2011|Desirable Difficulties (Bjork & Bjork, 1992; 2011)]]
- [[Directions-for-Future-Investigation|Directions for Future Investigation]]
- [[Dual-Process-Theory-and-its-Implications-for-Knowledge-Management-Decision-Makin|Dual-Process Theory and its Implications for Knowledge Management Decision-Making]]

```dataview
LIST FROM [[Single-Responsibility-Principle]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** *(auto-enriched from domain knowledge)*