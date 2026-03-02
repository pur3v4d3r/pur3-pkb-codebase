---
type: dashboard
id: aoel-dashboard
status: active
version: 1.0.0
created: 2026-03-02
modified: 2026-03-02

series: "The Architecture of the Examined Life"
purpose: "Progress tracking, statistics, and quick navigation hub"
accessibility: functional-overview

tags:
  - "#examined-life"
  - "#dashboard"
  - "#dataview"
  - "#progress-tracking"
  - "#navigation"
---

# 📊 Dashboard: The Architecture of the Examined Life PKB

> **Purpose:** Real-time overview of the complete PKB—track completion, explore statistics, and navigate quickly to any note.

---

## 🎯 Quick Links

### Primary Navigation
- [[index-the-architecture-of-the-examined-life|🏛️ Index — Start Here]]
- [[glossary-examined-life-key-terms|📖 Glossary — All Key Terms]]
- [[developmental-staging-of-the-examined-life|🌱 Developmental Staging]]
- [[methodology-research-methods-and-standards|🔬 Methodology]]

### Jump to Tier
- [[report-01-the-inquiry-engine|⚡ Tier 1: Epistemic Foundation (Reports 01-08)]]
- [[report-09-the-embodied-thinker|🌍 Tier 2: Practical Integration (Reports 09-12)]]
- [[report-13-the-predictive-mind|🔬 Tier 3: Unification (Reports 13-15)]]

---

## 📈 Build Progress Overview

### Phase Completion Status

| Phase | Description | Status | Notes | Target |
|-------|-------------|--------|-------|--------|
| **Phase 1** | Structural Foundation | ✅ **Complete** | 5 of 5 | 5 |
| **Phase 2** | Tier 1 Reports | ✅ **Complete** | 8 of 8 | 8 |
| **Phase 3** | Tier 2 Reports | ✅ **Complete** | 4 of 4 | 4 |
| **Phase 4** | Tier 3 Reports | ✅ **Complete** | 3 of 3 | 3 |
| **Phase 5** | Reference Library | 🔄 **In Progress** | 0 of 50-70 | 50-70 |

**Overall Progress:** 20 / 75-110 notes (18-27%)

---

## 📚 All Reports by Tier

### Tier 1: Epistemic Architecture (Reports 01-08)

```dataview
TABLE WITHOUT ID
  file.link as "Report",
  status as "Status",
  word-count as "Words"
FROM "the-architecture-of-the-examined-life/01-reports/tier-1-epistemic"
SORT file.name ASC
```

### Tier 2: Practical Integration (Reports 09-12)

```dataview
TABLE WITHOUT ID
  file.link as "Report",
  status as "Status",
  word-count as "Words"
FROM "the-architecture-of-the-examined-life/01-reports/tier-2-practical"
SORT file.name ASC
```

### Tier 3: Unification & Synthesis (Reports 13-15)

```dataview
TABLE WITHOUT ID
  file.link as "Report",
  status as "Status",
  word-count as "Words"
FROM "the-architecture-of-the-examined-life/01-reports/tier-3-integrative"
SORT file.name ASC
```

---

## 📖 Reference Library Status

### Priority 1: Foundational Sources (8 Expected)

**Expected Sources:**
- [ ] John Dewey — *How We Think*
- [ ] Daniel Kahneman — *Thinking, Fast and Slow*
- [ ] Antonio Damasio — *Descartes' Error*
- [ ] Lisa Feldman Barrett — *How Emotions Are Made*
- [ ] Andy Clark — *Surfing Uncertainty*
- [ ] Lev Vygotsky — *Mind in Society*
- [ ] Aristotle — *Nicomachean Ethics*
- [ ] Deci & Ryan — Self-Determination Theory Research

```dataview
TABLE WITHOUT ID
  file.link as "Reference",
  author as "Author",
  accessibility-rating as "Accessibility"
FROM "the-architecture-of-the-examined-life/02-reference-library"
WHERE priority = 1
SORT author ASC
```

### All Reference Notes

```dataview
TABLE WITHOUT ID
  file.link as "Reference",
  author as "Author",
  priority as "Priority",
  cited-in as "Cited In"
FROM "the-architecture-of-the-examined-life/02-reference-library"
SORT priority ASC, author ASC
```

**Current Count:** 0 reference notes (Target: 30-50)

---

## 🌐 Connection Notes

**Purpose:** Bridge to familiar external frameworks

**Expected Connections:**
- [ ] Mindfulness & Contemplative Practice
- [ ] Cognitive Behavioral Therapy (CBT)
- [ ] Growth Mindset (Dweck)
- [ ] Emotional Intelligence
- [ ] Digital Literacy & Information Hygiene

```dataview
TABLE WITHOUT ID
  file.link as "Connection",
  framework as "External Framework",
  target-reports as "Connects To"
FROM "the-architecture-of-the-examined-life/04-connections"
SORT file.name ASC
```

**Current Count:** 0 connection notes (Target: 10-15)

---

## 🔬 Expansion Topics

**Purpose:** Future research directions and open questions

```dataview
TABLE WITHOUT ID
  file.link as "Topic",
  originating-reports as "Raised In",
  priority as "Priority"
FROM "the-architecture-of-the-examined-life/05-expansion-topics"
SORT priority DESC, file.name ASC
```

**Current Count:** 0 expansion notes (Target: 15-25)

---

## 📊 PKB Statistics

### Note Count by Type

```dataview
TABLE WITHOUT ID
  type as "Note Type",
  length(rows) as "Count"
FROM "the-architecture-of-the-examined-life"
WHERE type != null
GROUP BY type
SORT length(rows) DESC
```

### Terms in Glossary

**Total Glossary Entries:** 40+ core terms (growing to 100-150)

**Coverage:**
- ✅ Tier 1 core concepts captured
- ✅ Tier 2 core concepts captured  
- ✅ Tier 3 core concepts captured
- 🔄 Comprehensive expansion ongoing

---

## 🔗 Knowledge Graph Metrics

### Most Connected Notes (Hubs)

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  length(file.outlinks) as "Outlinks",
  length(file.inlinks) as "Inlinks",
  (length(file.outlinks) + length(file.inlinks)) as "Total Links"
FROM "the-architecture-of-the-examined-life"
WHERE file.name != "dashboard-examined-life-pkb"
SORT (length(file.outlinks) + length(file.inlinks)) DESC
LIMIT 10
```

### Recent Updates

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  file.mtime as "Last Modified"
FROM "the-architecture-of-the-examined-life"
SORT file.mtime DESC
LIMIT 10
```

---

## ✅ Quality Gates Status

### Phase 1: Structural Foundation ✅

- [x] All 5 structural notes exist
- [x] All folder structure created
- [x] Navigation links functional
- [x] Index welcoming and accessible
- [x] Methodology explains approach
- [x] Staging provides developmental roadmap
- [x] Glossary has 40+ initial terms
- [x] Dashboard operational

**Status: COMPLETE** — Ready for Phase 5

### Phase 2: Tier 1 Reports ✅

- [x] All 8 Tier 1 reports complete
- [x] Sequential navigation works (01→08)
- [x] All reports link to Index
- [x] Content quality validated
- [x] Accessibility confirmed

**Status: COMPLETE**

### Phase 3: Tier 2 Reports ✅

- [x] All 4 Tier 2 reports complete
- [x] Retroactive enrichment sections present
- [x] Bidirectional linking to Tier 1
- [x] Accessibility maintained

**Status: COMPLETE**

### Phase 4: Tier 3 Reports ✅

- [x] All 3 Tier 3 reports complete
- [x] Report 13 demonstrates master homology
- [x] Report 14 provides existential grounding
- [x] Report 15 integrates full framework
- [x] Developmental staging integrated

**Status: COMPLETE**

### Phase 5: Reference Library & Connections 🔄

**In Progress — Current Priorities:**
- [ ] Generate Priority 1 Reference Notes (8 foundational sources)
- [ ] Create 3-5 most accessible Connection Notes
- [ ] Extract first wave of Expansion Topics (5-10 high-priority)

**Status: ACTIVE WORK PHASE**

---

## 🎯 Next Session Goals

### Immediate Priorities:

1. **Reference Notes (Priority 1 — Foundational Sources):**
   - [ ] ref-dewey-how-we-think.md
   - [ ] ref-kahneman-thinking-fast-and-slow.md
   - [ ] ref-damasio-descartes-error.md
   - [ ] ref-barrett-how-emotions-are-made.md
   - [ ] ref-clark-surfing-uncertainty.md
   - [ ] ref-vygotsky-mind-in-society.md
   - [ ] ref-aristotle-nicomachean-ethics.md
   - [ ] ref-deci-ryan-self-determination-theory.md

2. **Connection Notes (Most Accessible First):**
   - [ ] connection-mindfulness-contemplative-practice.md
   - [ ] connection-cognitive-behavioral-therapy.md
   - [ ] connection-growth-mindset.md

3. **Glossary Expansion:**
   - [ ] Add remaining 60-85 terms from report deep-dive
   - [ ] Ensure every report's key concepts represented

---

## 🔧 Maintenance Tasks

**Periodic Reviews:**
- [ ] Validate all wiki-links resolve (no broken links)
- [ ] Check for orphan notes (every note linked from at least one other)
- [ ] Verify glossary bidirectional linking complete
- [ ] Update this dashboard as progress advances

**Quality Assurance:**
- [ ] Sample accessibility checks (Can Mom understand "Big Idea" sections?)
- [ ] Link density verification (20-40 per report)
- [ ] Metadata completeness audit

---

## 🗂️ File Structure Overview

```
the-architecture-of-the-examined-life/
├── 00-navigation/
│   └── index-the-architecture-of-the-examined-life.md ✅
├── 01-reports/
│   ├── tier-1-epistemic/ (8 reports) ✅
│   ├── tier-2-practical/ (4 reports) ✅
│   └── tier-3-integrative/ (3 reports) ✅
├── 02-reference-library/ (0/30-50 notes) 🔄
├── 03-glossary-and-staging/
│   ├── glossary-examined-life-key-terms.md ✅
│   ├── developmental-staging-of-the-examined-life.md ✅
│   └── methodology-research-methods-and-standards.md ✅
├── 04-connections/ (0/10-15 notes) 🔄
└── 05-expansion-topics/ (0/15-25 notes) 🔄
```

---

## 📞 Support Resources

**Master Planning Documents:**
- `MASTER-PLAN-PKB-BUILD-EXECUTION.md` — Complete operational blueprint
- `examined-life-pkb-planning.md` — Detailed content extraction guide
- Source material: `the-architecture-of-the-examined-life.md` (150,000 words)

**Session Tracking:**
- See bottom of `MASTER-PLAN-PKB-BUILD-EXECUTION.md` for session logs

---

*Dashboard last updated: March 2, 2026*
*Auto-refreshes with every Dataview query execution*
