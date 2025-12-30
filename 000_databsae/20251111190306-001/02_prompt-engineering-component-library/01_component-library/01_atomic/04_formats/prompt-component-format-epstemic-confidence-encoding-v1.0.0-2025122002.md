---
type: "prompt-component"
id: "20251220024707"
status: "active"
version: "1.0.0"
rating: "0.0"
source: "claude-opus"
title: "Epstemic Confidence Encoding"
description: "Encode ^verified types that tell the confidence level of the materials accuracy."
key-takeaway: "Tested"
last-used: "[[2025-12-20]]"
tags:
  - "year/2025"
  - "llm-capability/generation"
  - "prompt-workflow/deployment"
  - "prompt-pattern"
  - "prompt-engineering/anatomy"
aliases:
  - prompt-component-format-epstemic-confidence-encoding-v1.0.0-2025122002
  - "Prompt-Engineering"
  - "Prompt Component"
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
link-related:
  - "[[2025-12-20|Daily Note]]"
  - "[[2025-W51|Weekly Review]]"
---




[Initial Creation: [[2025-12-20|Saturday, December 20th, 2025]]]

---

# prompt-component-format-epstemic-confidence-encoding-v1.0.0-2025122002

`````prompt-component
----
Prompt-Component-ID: "2025122002"
Prompt-Component-Version: 1.0.0
----

<epistemic_confidence_encoding>
## 🎯 Epistemic Status Encoding Protocol
When generating knowledge claims, explicitly encode confidence levels using inline markers.
<confidence_taxonomy>
### Primary Confidence Levels

| Marker | Definition | Typical Source | Visual |
|--------|------------|----------------|--------|
| `^verified` | Multiple independent replications; scientific consensus | Meta-analyses, systematic reviews | 🟢 |
| `^established` | Widely accepted in field; standard textbook content | Authoritative texts, review papers | 🔵 |
| `^provisional` | Single study, recent finding, limited replication | Primary research, recent publications | 🟡 |
| `^speculative` | Theoretical inference, hypothesized relationship | Personal synthesis, theoretical papers | 🟠 |
| `^contested` | Active scholarly debate; conflicting evidence | Debate literature, response papers | 🔴 |
### Secondary Modifiers (Optional)

| Modifier | Meaning | Use Case |
|----------|---------|----------|
| `-stable` | Unlikely to change significantly | Well-established principles |
| `-volatile` | Field actively evolving; may shift | Cutting-edge domains |
| `-consensus` | Represents field agreement | Distinguishing from personal view |
| `-personal` | Personal synthesis, not field consensus | Original analysis |
</confidence_taxonomy>
<syntax_specification>
### Syntax Patterns
**Basic Format:**
```markdown
[**Field-Name**:: claim content]^confidence-level
```
**With Secondary Modifier:**
```markdown
[**Field-Name**:: claim content]^confidence-level-modifier
```
**Examples:**
```markdown
[**Spacing-Effect**:: distributed practice produces superior retention to massed practice]^verified-stable
[**Desirable-Difficulties**:: conditions that slow initial learning but enhance long-term retention]^established-consensus
[**AI-Consciousness**:: large language models may develop emergent self-models]^speculative-personal
[**Retrieval-Practice-Mechanisms**:: testing effect operates via elaborative retrieval processes]^provisional-volatile
[**Learning-Styles-Validity**:: matching instruction to preferences improves outcomes]^contested-active
```
</syntax_specification>
<generation_heuristics>
### When to Apply Each Level
**^verified**: Apply when:
- Multiple meta-analyses converge
- Effect replicated across labs, populations, contexts
- No serious methodological challenges remain
- Would be surprising if overturned
**^established**: Apply when:
- Appears in authoritative textbooks
- Cited without hedging in review papers
- Taught as standard curriculum content
- Limited ongoing debate
**^provisional**: Apply when:
- Based on single study or limited samples
- Published within last 2-3 years without replication
- Methodology sound but awaiting confirmation
- From reputable source but not yet consensus
**^speculative**: Apply when:
- Personal theoretical inference
- Extrapolating from adjacent domains
- "If X is true, then Y should follow" reasoning
- No direct empirical test yet
**^contested**: Apply when:
- Prominent researchers disagree
- Response/rebuttal papers exist
- Replication attempts show mixed results
- Active debate in journals
</generation_heuristics>
<integration_notes>
### Dataview Query Compatibility
These markers enable queries like:
```dataview
TABLE file.name as "Note", confidence
FROM "permanent-notes"
WHERE contains(file.content, "^speculative")
SORT file.mtime DESC
```
### Output Requirements
- Every substantive claim in reference notes SHOULD have confidence encoding
- Definitions from authoritative sources: `^established` minimum
- Personal syntheses: `^speculative-personal` or `^provisional-personal`
- Density: 40-60% of inline fields should carry confidence markers
</integration_notes>
</epistemic_confidence_encoding>

`````
