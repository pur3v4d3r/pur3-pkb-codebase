---
tags: #pkm #obsidian #reference-note #quick-reference
aliases: [Note Types QRC, Note Classification Guide]
---

# 📝 Quick Reference: Note Type Specifications

## Note Type Comparison Matrix

| Type | Length | Wiki-Links | Callouts | Metadata? | Purpose |
|------|--------|------------|----------|-----------|---------|
| **Simple Query** | 300-600 | 3-6 | 2-3 | ❌ NO | Quick answer |
| **Atomic** | 300-800 | 5-8 | 2-4 | ✅ YES | Single concept |
| **Reference** | 1500-4000+ | 20-40 | 12-15 | ✅ YES | Comprehensive resource |
| **MOC** | Variable | 30-100+ | 5-8 | ✅ YES | Navigation hub |
| **Synthesis** | 800-1500 | 15-30 | 10-12 | ✅ YES | Cross-domain integration |
| **Technical** | Variable | 15-40 | 15-20 | ✅ YES | Implementation guide |

## ATOMIC NOTES

**Purpose:** Thoroughly explain ONE concept

**Structure:**
````markdown
---
tags: #domain #concept #atomic-note
aliases: [Alt Name, Abbrev]
status: budding
type: atomic
---

# [Concept Name]

> [!definition] [Concept]
> Clear, precise definition

## Core Explanation
[What it is, why it matters, how it works]

## Key Distinctions
[What it's NOT, boundary clarification]

> [!example] Concrete Illustration
> [Specific example]

## Connections
[Relationships to related concepts]

## Applications
[Where/how this applies in practice]

## 🔗 Related Topics for PKB Expansion
[4 extension topics]
````

**Target Specs:**
- Length: 300-800 words
- Wiki-Links: 5-8 highly relevant
- Callouts: 2-4 semantic
- Focus: Clarity, precision, foundation

---

## REFERENCE NOTES

**Purpose:** Exhaustive coverage as permanent knowledge artifact

**Structure:**
````markdown
---
tags: #domain #framework #reference-note #subdomain
aliases: [Full Name, Abbrev, Search Terms]
status: evergreen
type: reference
---

# [Topic Name]

> [!abstract] Overview
> Executive summary

## Theoretical Foundations
[Academic frameworks, principles, history]

> [!definition] Key Term
> [Definition]

## Core Concepts
[Detailed explanation]

> [!key-claim] Central Proposition
> [Claim with support]

> [!evidence] Supporting Research
> [Empirical evidence]

## Practical Applications
[Real-world use cases]

> [!example] Application Scenario
> [Concrete demonstration]

## Advanced Topics
[Sophisticated extensions]

## Critical Analysis
[Limitations, competing views]

## References
[Citations]

## 🔗 Related Topics for PKB Expansion
[4-6 extension topics]
````

**Target Specs:**
- Length: 1500-4000+ words (no upper limit)
- Wiki-Links: 20-40 for knowledge graph
- Callouts: 12-15 for organization
- Focus: Depth, comprehensiveness, scholarly rigor

---

## MAPS OF CONTENT (MOCs)

**Purpose:** Curated navigation hub for knowledge domain

**Structure:**
````markdown
---
tags: #domain #moc
aliases: [Domain Map, Domain Index]
status: evergreen
type: moc
---

# [Domain] Map of Content

> [!abstract] Domain Overview
> Scope and organization

## Dashboard Metrics
**Total Notes:** [Dataview count]
**Maturity:** [Distribution]

## Core Concepts (🌳 Evergreen)
- [[Concept 1]] - Brief description
- [[Concept 2]] - Brief description

## Developing Notes (🌿 Budding)
- [[Topic 1]] - Status and needs

## Emerging Ideas (🌱 Seedling)
- [[New Concept]] - Initial thoughts

## Requires Attention (🍂 Wilting)
- [[Outdated Note]] - Why needs review

## Semantic Bridges
**To [[Other Domain MOC]]:**
- [[Bridge Concept]] - How domains connect

## Related MOCs
- [[Adjacent Domain MOC]]
- [[Parent Domain MOC]]
````

**Target Specs:**
- Length: Variable (structure-dependent)
- Wiki-Links: 30-100+ (primary feature)
- Callouts: 5-8 for categorization
- Focus: Organization, navigation, domain overview

---

## SYNTHESIS NOTES

**Purpose:** Cross-domain analysis revealing emergent insights

**Structure:**
````markdown
---
tags: #domain1 #domain2 #synthesis-note
aliases: [Synthesis Name]
status: budding
type: synthesis
---

# [Title]: [Concept A] + [Concept B]

> [!abstract] Synthesis Overview
> What's being integrated, why it matters

## Component Concepts

### [[Concept A]]
[Brief summary]

### [[Concept B]]
[Brief summary]

## Integration Analysis
[How concepts relate and combine]

> [!key-claim] Emergent Insight
> [Novel understanding from synthesis]

## Practical Implications
[What this means for application]

> [!example] Integrated Application
> [Synthesis in practice]

## Connection Map
[Relationship diagram]

## 🔗 Related Topics for PKB Expansion
[4 topics continuing synthesis]
````

**Target Specs:**
- Length: 800-1500 words
- Wiki-Links: 15-30 showing relationships
- Callouts: 10-12 highlighting connections
- Focus: Integration, emergent insights, cross-domain

---

## TECHNICAL GUIDES

**Purpose:** Implementation documentation with code/configuration

**Structure:**
````markdown
---
tags: #technical-guide #tool-name #implementation
aliases: [Guide Name, Implementation]
status: evergreen
type: reference
---

# [Technical Topic]

> [!abstract] Overview
> What this guide covers

## Prerequisites
- [[Requirement 1]]
- [[Requirement 2]]

## Installation/Setup

> [!methodology-and-sources] Process
> Step-by-step procedure
```language
code block with implementation
```

> [!what-this-does] Function
> What this code accomplishes

## Configuration

> [!helpful-tip] Best Practice
> Optimization advice

## Troubleshooting

> [!warning] Common Issue
> Problem and solution

## Examples

> [!example] Use Case
> Practical demonstration

## 🔗 Related Topics for PKB Expansion
[4 related technical topics]
````

**Target Specs:**
- Length: Variable (function-dependent)
- Wiki-Links: 15-40 for concepts
- Callouts: 15-20 (heavy documentation)
- Focus: Implementation, examples, troubleshooting

---

## Decision Tree: What Type to Create?
````
What's the user request?

Single concept needing explanation?
└─ → ATOMIC NOTE

Comprehensive coverage of topic?
└─ → REFERENCE NOTE

Navigation/organization of domain?
└─ → MOC

Connecting multiple concepts?
└─ → SYNTHESIS NOTE

Code/implementation guide?
└─ → TECHNICAL GUIDE

Quick answer to question?
└─ → SIMPLE QUERY RESPONSE (no metadata)
````

## Quick Self-Check by Type

**For Atomic:**
- [ ] Single concept only?
- [ ] Fully explained (not superficial)?
- [ ] Clear distinctions drawn?
- [ ] Example included?

**For Reference:**
- [ ] Comprehensive coverage?
- [ ] Multiple sources integrated?
- [ ] Theoretical + practical?
- [ ] 1500+ words of substance?

**For MOC:**
- [ ] Organized link collection?
- [ ] Clear categorization?
- [ ] Navigation-focused?
- [ ] 20+ curated links?

**For Synthesis:**
- [ ] Multiple concepts integrated?
- [ ] Emergent insights present?
- [ ] Cross-domain connections?
- [ ] Novel understanding created?