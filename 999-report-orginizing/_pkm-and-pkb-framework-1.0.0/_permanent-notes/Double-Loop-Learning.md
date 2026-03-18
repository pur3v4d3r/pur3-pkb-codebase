---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Double-Loop Learning"
aliases:
  - "Double-Loop Learning"
type: permanent-note
status: evergreen
confidence: high

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  - permanent-note
  - evergreen
  - educational-psychology
  - pkm-framework
  - educational-psychology/self-regulated-learning
  - educational-psychology/feedback-in-learning
  - educational-psychology/formative-assessment
  - systems-theory/cybernetics

domain: educational-psychology
subdomains:
  - systems-theory
  - learning-analytics
  - instructional-design
  - cognitive-psychology
  - educational-philosophy

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
  - "26-feedback-loops-pkm-framework-2026-03-15"
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
  - "[[AI-Assisted Calibration Testing in PKB Systems]]"
  - "[[AI-Augmented Heutagogy: Affordances and Risks]]"
  - "[[Adaptive Learning Systems and PKB: Lessons from Intelligent Tutoring Systems]]"
  - "[[Andragogy]]"
  - "[[Argyris and Schön]]"
  - "[[Arnold and Pistilli]]"
  - "[[Autonomy Need]]"
  - "[[Barry Zimmerman]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  - "[[Report 04: Metacognitive Self-Regulation — The Engine of Effective PKM]]"
  - "[[Report 06: The Science of Remembering — Memory Systems, Retrieval Practice, and PKB Review Design]]"
  - "[[Report 08: Reflective Practice and Experiential Learning — Dewey, Kolb, and the Learning Cycle in PKM]]"
  - "[[Report 12: The Reflective PKB — Embedding Metacognitive Monitoring into Daily Practice]]"
  - "[[Report 18: Calibration and Epistemic Humility — Knowing What You Know and Don't Know]]"

enables:
  - "[[Report 27: The Complete PKM/PKB Design Framework — Synthesizing Principles Across All Reports]]"
  - "[[Report 29: Ethical PKM — Intellectual Honesty, Epistemic Responsibility, and Virtue in Knowledge Work]]"
  - "[[Report 30: Future of PKM — AI-Enhanced Knowledge Building, Emerging Research, and Open Questions]]"

expansion-topics:
  - topic: "[[AI-Assisted Calibration Testing in PKB Systems]]"
    description: "Explores how conversational AI systems can serve as dialogic testing partners — generating novel app"
    priority: medium
  - topic: "[[Obsidian Plugin Architecture for Feedback Systems]]"
    description: "A practical implementation report addressing the technical infrastructure required for PKB feedback "
    priority: medium
  - topic: "[[Defensive Reasoning and the PKB: When Personal Knowledge Systems Reinforce Bias]]"
    description: "Extends the Argyris and Schön double-loop learning analysis to examine how PKBs can become instrumen"
    priority: medium
  - topic: "[[Network Analysis Tools for PKB Structural Feedback]]"
    description: "Examines how graph-theoretic analysis of PKB network structure can generate macro-level feedback sig"
    priority: medium

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: seedling
importance: high
---

# Double-Loop Learning

> [!definition] **Double-Loop Learning**
> A learning process distinguished from [[Single-Loop Learning]] by its scope of correction. Single-loop learning corrects errors *within* an existing framework of assumptions — it adjusts behavior to better achieve existing goals. Double-loop learning questions and revises the framework itself — it asks whether the goals are correct, whether the assumptions underlying the strategy are valid, and whether the system's governing values are appropriate. In PKB terms: single-loop feedback says "this note format is not working; adjust the format." Double-loop feedback says "my entire approach to capturing information may be producing the wrong kind of knowledge; reconsider the approach."

*Source: (defined across 4 reports)*

## Core Explanation

> [!evidence] Supporting Evidence
> **The Feedback Timing Paradox (Kornell & Bjork, 2008; Karpicke & Roediger, 2008)**: Educational psychology presents a genuine paradox on the question of feedback timing. Immediate feedback research (summarized by Hattie & Timperley, 2007) shows that feedback close in time to the relevant behavior is processed more effectively — learners can connect the signal to the specific action that generated it. However, [[Desirable Difficulties]] research (Robert Bjork) demonstrates that delayed feedback…

> [!evidence] Supporting Evidence
> **What the Feedback Timing Literature Suggests for PKB Design**: The immediate-vs.-delayed tension actually resolves differently depending on the *purpose* of the feedback and the *phase* of learning. For error detection during initial learning, immediate feedback is superior — the learner needs to know quickly that their model is wrong before the incorrect representation consolidates. For retrieval practice during review, delayed or absent feedback during the retrieval attempt followed by…

> [!evidence] Supporting Evidence
> **What the Learning Analytics Literature Suggests for PKB**: The empirical record suggests that the instinct to build a comprehensive PKB analytics dashboard — a single view showing everything about one's knowledge system — is likely to produce a tool that is impressive but rarely consulted. More effective is feedback that is *contextual* (appearing at the point where it is actionable), *specific* (tied to a particular note, topic, or behavior rather than the system overall), and *goal-linked*…

> [!analytical-insight] Key Insight
> **The Write-Only Problem**: Most current PKBs are architecturally incapable of learning from themselves because they lack the four components that cybernetics, SRL, and learning analytics all identify as necessary for self-correcting feedback: (1) a representation of desired state (learning goals), (2) sensors that detect actual state (monitoring mechanisms), (3) a comparator that generates discrepancy signals (the gap between desired and actual), and (4) effectors that adjust system behavior…

> [!analytical-insight] Key Insight
> **Why Most PKB Feedback Fails: The Single-Timescale Trap**: The most common PKB feedback mechanisms — spaced repetition systems, periodic review workflows, usage statistics — predominantly operate at the meso-level. They generate signals about individual notes and short-term behavioral patterns, but they are largely blind to both the micro-level (the phenomenology of note-creation, where many of the most important calibration failures occur) and the macro-level (the structural evolution of the…

## Practical Implications

> [!example] **Application**
> **The Feedback Sandwich Workflow**: A concrete Obsidian implementation that addresses all three timescales within a single review session: (1) **Before opening the note**: generate a brief written recall attempt (what do I believe this note says? what is the core mechanism/claim?); (2) **Open the note and compare**: note any discrepancies between recall attempt and note content — these are calibration data; (3) **After reviewing the note**: write one application question (how would this concept…

> [!example] **Application**
> **The Epistemic Health Dashboard in Dataview**: A minimal Dataview implementation for systematic pattern detection:
> - Per-domain breakdown of `epistemic-status` tags (what fraction of notes in each domain are `tested` vs `superficial` vs `uncertain`?)
> - Isolation index: notes with zero outgoing links and zero incoming links, grouped by domain
> - Recency map: notes not revisited in the past 90 days, by domain and epistemic-status
> - Application gap: notes tagged with a concept-type that have no…

> [!warning] **Key Distinction**
> A well-designed PKB feedback system can produce a new and subtle form of the "productivity theater" problem: the learner spends significant effort maintaining the feedback architecture — tagging notes, running Dataview queries, consulting dashboards — and experiences this maintenance as meaningful engagement with their knowledge system, while the feedback signals themselves are never actually used to drive behavioral change. Feedback architecture that is visually impressive but operationally…

## Connections & Context

**Cross-report connections:**
- [[Zimmerman's Self-Regulated Learning Cycle]]

**Cross-report connections:**
- [[Donald Schön]]
- [[Reflective Practitioner]]

**Related concepts:**
[[AI-Assisted Calibration Testing in PKB Systems]] · [[AI-Augmented Heutagogy: Affordances and Risks]] · [[Adaptive Learning Systems and PKB: Lessons from Intelligent Tutoring Systems]] · [[Andragogy]] · [[Argyris and Schön]] · [[Arnold and Pistilli]] · [[Autonomy Need]] · [[Barry Zimmerman]] · [[Black and Wiliam]] · [[Canvas]] · [[Capability]] · [[Capability Development]] · [[Capability Documentation: A Theory and Practice of Capability Notes]] · [[Cognitive Apprenticeship]] · [[Cognitive Load Theory]]
