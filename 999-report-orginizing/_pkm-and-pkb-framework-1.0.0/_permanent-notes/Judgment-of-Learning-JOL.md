---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Judgment of Learning / JOL"
aliases:
  - "Judgment of Learning / JOL"
  - "JOLJ"
type: permanent-note
status: evergreen
confidence: high

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - evergreen
  - cognitive-psychology
  - pkm-framework
  - memory-science
  - retrieval-practice
  - spaced-repetition
  - active-recall

domain: cognitive-psychology
subdomains:
  - cognitive-psychology
  - educational-psychology
  - instructional-design
  - metacognition
  - memory-science

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-03-18
updated: 2026-03-18

# ═══════════════════════════════════════════════════════════════════════════
# SOURCE TRACKING
# ═══════════════════════════════════════════════════════════════════════════
source-type: report-extraction
source-reports:
  - "20-retrieval-enhanced-knowledge-networks-pkm-framework-2026-03-15"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → permanent-notes-generator-v1"

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
complexity-level: advanced-practitioner
depth-level: comprehensive

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  - "[[]]"

related:
  - "[[]]"

broader:
  - "[[]]"

narrower:
  - "[[]]"

see-also:
  - "[[Anderson et al. (1994)]]"
  - "[[Anki and Spaced Repetition in Obsidian — Practical Integration Patterns]]"
  - "[[Cognitive Psychology]]"
  - "[[David Rumelhart]]"
  - "[[Desirable Difficulties]]"
  - "[[Educational Psychology]]"
  - "[[Elaborative Interrogation]]"
  - "[[Elaborative Retrieval]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  - "[[]]"

enables:
  - "[[]]"

expansion-topics:
  - topic: "[[]]"
    description: ""
    priority: medium

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: high
---

# Judgment of Learning / JOL

> [!definition] **Judgment of Learning / JOL**
> A metacognitive estimate of how well information has been learned and how readily it will be recalled in the future. JOLs based on reading are systematically overconfident; JOLs based on retrieval attempts are significantly better calibrated. A well-designed PKB review system generates retrieval-based JOLs to correct the fluency-illusion bias.

*Source: Nelson & Narens, 1990*

## Core Explanation

> [!evidence] Supporting Evidence
> **Untitled**: **Evidence Base: Testing Effect**
> 
> The systematic reviews are unambiguous. Dunlosky et al.'s (2013) analysis of ten major learning strategies, published in *Psychological Science in the Public Interest*, rated practice testing as having "high utility" — one of only two strategies to achieve this rating (the other being distributed practice/spaced repetition). The review examined evidence across multiple age groups, content domains (from foreign language vocabulary to science…

> [!evidence] Supporting Evidence
> **Untitled**: **What the Testing Effect Evidence Suggests for PKB Design**
> 
> The evidence does not merely suggest that testing *helps* — it suggests something stronger: that the dominant review practice in most PKBs (re-reading notes, browsing linked notes, passive review) is, by the best available evidence, a *systematically inferior* strategy for building durable, retrievable knowledge. The effect size of d = 0.50 is not a marginal improvement; it represents a difference between remembering…

> [!evidence] Supporting Evidence
> **Untitled**: **Evidence Base: Spacing Effect and Spaced Repetition Systems**
> 
> Cepeda et al.'s (2006) landmark meta-analysis of 254 studies and nearly 14,000 participants found that spaced practice produced superior long-term retention across virtually all conditions studied, with optimal spacing gaps depending on the desired retention interval. Their key finding was that the ratio of study gap to test gap should be approximately 10-20% — so for material you want to retain for one month,…

> [!analytical-insight] Key Insight
> **Untitled**: **Both Mechanisms Point to the Same PKB Design Principle**
> 
> The elaborative retrieval account and the encoding variability account, despite their different theoretical commitments, converge on a single PKB design implication: retrieval practice should be *generative* and *context-varied*. If elaborative retrieval is the mechanism, then PKB retrieval practice should prompt the learner to generate connections, not merely recall facts — "What does this connect to?", "What would I…

> [!analytical-insight] Key Insight
> **Untitled**: **Spaced Retrieval Enriches Network Topology, Not Just Node Strength**
> 
> The standard account of spacing effects focuses on *node strength* (how well a specific item is retained). But the network model predicts a second benefit that is less commonly articulated: *topology enrichment*. When activation must travel further to reach a target (because it has begun to fade), it traverses more diverse pathways in search of activation routes, strengthening a wider variety of connections in…

## Practical Implications

> [!example] **Application**
> **Retrieval-First Note Design in Obsidian**: Implement retrieval-first design through a two-part note structure:
> 
> **Part 1: The Recall Header (3–5 lines)** — A question, a cloze-deletion prompt, or a key claim that can be recalled without reading the note. Example: "What is the central mechanism of the Testing Effect? (Hint: think about *reconstruction* vs. recognition)." This is placed at the very top of the note, before any content.
> 
> **Part 2: The Knowledge Body** — The full note content,…

> [!example] **Application**
> **The Random Walk Review Pattern in Obsidian**: Implement three complementary random-sampling review methods:
> 
> **Method A: The Daily Random Pull** — Use Obsidian's Dataview plugin to generate a view of 5 notes that were created more than 30 days ago and have not been reviewed in the past 7 days, ordered randomly. Review each using the Retrieval-First protocol.
> 
> **Method B: Peripheral Node Review** — Periodically use graph analysis (Obsidian Graph View filtered for notes with 0-2 incoming links)…

## Connections & Context

**Cross-report connections:**
- [[wiki-links]]

**Related concepts:**
[[Anderson et al. (1994)]] · [[Anki and Spaced Repetition in Obsidian — Practical Integration Patterns]] · [[Cognitive Psychology]] · [[David Rumelhart]] · [[Desirable Difficulties]] · [[Educational Psychology]] · [[Elaborative Interrogation]] · [[Elaborative Retrieval]] · [[Fluency Illusion]] · [[Instructional Design]] · [[Interleaving in Knowledge Review — The Case for Anti-Topic-Clustering]] · [[Knowledge Graph Analytics for PKB Health Assessment]] · [[Koriat and Bjork (2005)]] · [[Memory Reconsolidation]] · [[Metacognition]]
