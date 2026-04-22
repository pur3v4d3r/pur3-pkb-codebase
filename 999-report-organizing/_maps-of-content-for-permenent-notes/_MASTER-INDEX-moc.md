---
title: Permanent Notes Master Index MOC
aliases:
  - Master MOC
  - Top-Level Index
  - Vault Map
created: 2026-04-22
modified: 2026-04-22
status: evergreen
type: moc
tags:
  - master-index
  - moc
  - knowledge-hub
child-mocs:
  - "[[cognitive-science-moc]]"
  - "[[metacognition-moc]]"
  - "[[self-regulated-learning-moc]]"
  - "[[motivation-theory-moc]]"
  - "[[learning-strategies-and-practice-moc]]"
  - "[[adult-and-self-directed-learning-moc]]"
  - "[[pkm-and-knowledge-systems-moc]]"
  - "[[software-engineering-and-development-moc]]"
  - "[[clinical-reasoning-and-practice-moc]]"
  - "[[social-cultural-and-eudaimonic-psychology-moc]]"
  - "[[researchers-and-theorists-moc]]"
---

# Permanent Notes Master Index MOC

> [!abstract] Purpose
> Top-level navigation entry point into the ~896-note permanent-notes corpus. Each link below opens a Tier-1 Map-of-Content covering one major domain of the vault.

> [!important] Navigation Strategy
> Start at the MOC closest to your inquiry → follow hub anchors → drill into atomic notes → use the auto-indexed Dataview block at the bottom of each MOC for exhaustive listings.

---

## 🗺️ Tier-1 Maps of Content

### 🧠 [[cognitive-science-moc]]
Memory systems, attention, executive function, cognitive architecture, dual-process reasoning, schema theory, and the cognitive science of reading. **Anchor hubs**: [[working-memory]], [[long-term-memory]], [[information-processing-theory]], [[Cognitive-Load-Theory]], [[dual-process-theory]].

### 🤔 [[metacognition-moc]]
Cognition about cognition. Flavell's taxonomy, the Nelson–Narens monitoring–control architecture, calibration research, metacognitive feelings, and applied metacognition. **Anchor hubs**: [[metacognitive-monitoring]], [[metacognitive-control]], [[metacognitive-knowledge]], [[Flavell's-Metacognitive-Framework]], [[Nelson-and-Narens]].

### 🎯 [[self-regulated-learning-moc]]
The cyclical self-regulation of learning. Zimmerman, Winne–Hadwin, Pintrich, and Boekaerts models. Forethought / performance / self-reflection phases. Volition and the action-phase tradition. **Anchor hubs**: [[self-regulated-learning]], [[forethought-phase]], [[Zimmerman's-Cyclical-Model-of-Self-Regulated-Learning]], [[barry-zimmerman]].

### 🌱 [[motivation-theory-moc]]
SDT, SCT, AGT, EVT, mindset, attribution, interest, control-value. Spans the corpus's largest theoretical sub-cluster. **Anchor hubs**: [[self-determination-theory]], [[self-efficacy]], [[growth-mindset]], [[achievement-goal-theory]], [[albert-bandura]].

### 📚 [[learning-strategies-and-practice-moc]]
Evidence-based strategies, deliberate practice, cognitive-load-aware instructional design, transfer, and the desirable-difficulty literature. **Anchor hubs**: [[transfer-of-learning]], [[deliberate-practice]], [[spaced-repetition]], [[Active-Recall]], [[Cognitive-Load-Theory]], [[Desirable-Difficulty]].

### 🎓 [[adult-and-self-directed-learning-moc]]
Andragogy, heutagogy, the Knowles–Tough–Garrison–Brookfield SDL traditions, transformative learning (Mezirow), competency-based and workplace learning, communities of practice, and the cross-cultural dimension of adult learning. **Anchor hubs**: [[self-directed-learning]], [[andragogy]], [[heutagogy]], [[malcolm-knowles]], [[communities-of-practice]], [[Transformative-Learning]].

### 📚 [[pkm-and-knowledge-systems-moc]]
Personal Knowledge Management theory, Zettelkasten, Evergreen Notes, Obsidian-specific architecture, and AI-assisted knowledge work. **Anchor hubs**: [[personal-knowledge-management]], [[Zettelkasten-Method]], [[Evergreen-Notes]], [[obsidian-pkb-architecture]].

### 💻 [[software-engineering-and-development-moc]]
Programming, Python ecosystem, Git, dev tooling, software architecture, API design, debugging, and developer cognition — captured at the intersection of software practice and cognitive science. **Anchor hubs**: [[Python]], [[software-engineering-workflows]], [[Software-Architecture]], [[API-Fundamentals]], [[Error-Handling-as-Cognitive-Engineering]].

### 🩺 [[clinical-reasoning-and-practice-moc]]
Diagnostic reasoning, evidence-based medicine, clinical heuristics, CBT, motivational interviewing, recognition-primed decision making, and the cognitive psychology of expert clinical judgment. **Anchor hubs**: [[Clinical-Reasoning]], [[Evidence-Based-Medicine]], [[diagnostic-error-cognitive-causes]], [[recognition-primed-decision-making]], [[cognitive-behavioral-therapy]].

### 🌟 [[social-cultural-and-eudaimonic-psychology-moc]]
Social psychology (identity, perception, prejudice), cross-cultural psychology (WEIRD-sample critique, cultural variation in needs), humanistic and positive psychology (eudaimonia, flourishing, well-being), and bridging social-cognitive constructs. **Anchor hubs**: [[social-cognition]], [[Social-Identity-Theory]], [[eudaimonia]], [[Flourishing]], [[WEIRD-Sample-Bias]], [[humanistic-psychology]].

### 👥 [[researchers-and-theorists-moc]]
Person-note attribution index spanning all domains. Use as the canonical link target when citing researchers in concept-notes. **Anchor people**: [[albert-bandura]], [[john-flavell]], [[barry-zimmerman]], [[anders-ericsson]], [[daniel-kahneman]], [[john-sweller]].

---

## 🛠️ Vault Operations

### Workflow Documents
- [[_MOC-DEVELOPMENT-WORKFLOW-v1.0.0]] — How this MOC system was built and how to extend it

### Generated Audit Artifacts
- `_inventory.json` — Full 896-note manifest (filename, frontmatter, links)
- `_clusters.json` — Cluster discovery output (machine-readable)
- `_clusters-report.md` — Cluster discovery report (human-readable)

### Helper Scripts (`99-scripts/moc-builder/`)
- `moc_inventory.py` — Phase 1: catalog all notes
- `moc_cluster.py` — Phase 2: discover thematic clusters via 4 signals
- `moc_backlink.py` — Phase 5: idempotently populate `parent-moc` frontmatter

---

## 📊 Vault-Wide Statistics

```dataview
TABLE WITHOUT ID
  "Total permanent notes" AS Metric,
  length(rows) AS Value
FROM "999-report-organizing/_permanent-notes/llm-generated-permanent-notes"
GROUP BY true
```

```dataview
TABLE WITHOUT ID
  domain AS "Domain",
  length(rows) AS "Notes"
FROM "999-report-organizing/_permanent-notes/llm-generated-permanent-notes"
GROUP BY domain
SORT length(rows) DESC
```

```dataview
TABLE WITHOUT ID
  status AS "Status",
  length(rows) AS "Notes"
FROM "999-report-organizing/_permanent-notes/llm-generated-permanent-notes"
GROUP BY status
SORT length(rows) DESC
```

## 🔗 Top 30 Hub Notes (by referenced-by-count)

```dataview
TABLE
  domain,
  referenced-by-count AS "Refs"
FROM "999-report-organizing/_permanent-notes/llm-generated-permanent-notes"
SORT referenced-by-count DESC
LIMIT 30
```

## 🚧 Notes Without a Parent MOC (Orphans)

```dataview
TABLE referenced-by-count AS "Refs"
FROM "999-report-organizing/_permanent-notes/llm-generated-permanent-notes"
WHERE !parent-moc OR length(parent-moc) = 0
SORT referenced-by-count DESC
LIMIT 50
```

---

# 🔗 Related Topics for PKB Expansion

## 🎯 Core Extensions

1. **Tier-2 sub-MOCs** — Connection: each Tier-1 MOC will eventually spawn 2–4 Tier-2 children · Depth Potential: SDT alone warrants its own MOC; same for CLT, attribution theory · Knowledge Graph Role: refinement of current hierarchy · Priority: High
2. **Domain-field re-tagging campaign** — Connection: 381 notes carry `domain: other` · Depth Potential: enables sharper Dataview queries · Knowledge Graph Role: data-quality investment · Priority: High

## 🌐 Cross-Domain Connections

3. **Ghost-note backlog** — Connection: many `see-also` links point to non-existent notes (e.g. `[[Activating-Prior-Knowledge]]`) · Depth Potential: each ghost is a future atomic note · Knowledge Graph Role: corpus growth driver · Priority: Medium
4. **Reconciliation with `07-mocs/`** — Connection: legacy MOCs at `D:/10_pur3v4d3r's-vault/07-mocs/` use the same naming convention · Depth Potential: deduplicate or merge · Knowledge Graph Role: vault hygiene · Priority: Low

## 📚 Foundational Prerequisites

- **[[_MOC-DEVELOPMENT-WORKFLOW-v1.0.0]]** — Methodology behind this index

## 🛠️ Practical Applications

- Use the orphan-detection Dataview query above to identify notes that fell through the regex-based MOC membership rules and need explicit `parent-moc` assignment.
