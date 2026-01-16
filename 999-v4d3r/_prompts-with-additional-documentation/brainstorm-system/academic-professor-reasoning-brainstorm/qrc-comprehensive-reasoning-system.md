# Comprehensive Reasoning & Report System v2.0 — Quick Reference Card

> One-page reference for the multi-tier reasoning architecture

---

## Framework Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    REASONING TIER SELECTION                         │
├─────────────────────────────────────────────────────────────────────┤
│  Query Complexity?                                                  │
│  ├─ Single fact/definition ──────────────► TIER 1 (300-800 words)  │
│  ├─ Process/concept explanation ─────────► TIER 2 (1000-2500 words)│
│  └─ Multi-faceted/"comprehensive" ───────► TIER 3 (2500-5000+)     │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    FOUR-PHASE PROCESS                               │
├─────────────────────────────────────────────────────────────────────┤
│  1. EXPLORATION ──► 2. EVALUATION ──► 3. SYNTHESIS ──► 4. VERIFY   │
│     (decompose)       (score paths)    (build output)   (fact-check)│
└─────────────────────────────────────────────────────────────────────┘
```

---

## Tier Activation Rules

| Tier | Triggers | Components | Target |
|------|----------|------------|--------|
| **1** | Definition, single fact, basic | Linear CoT + basic check | 300-800 |
| **2** | Process, technical guide, how-to | Enhanced CoT + SC(3) + CoVe | 1000-2500 |
| **3** | Comprehensive, multi-faceted, theoretical | Full ToT + SC(5) + CoVe + Meta | 2500-5000+ |

---

## Chain of Density Layering

| Layer | Words | Content |
|-------|-------|---------|
| **1 — Foundation** | 100+ | Definition, significance, core mechanism |
| **2 — Enrichment** | 200+ | Evidence, distinctions, technical details |
| **3 — Integration** | 200+ | Connections, applications, limitations |
| **4 — Advanced** | 150+ | Frontiers, edge cases, open questions |

**Apply**: Layer 1-2 for Tier 1 | Layer 1-3 for Tier 2 | Layer 1-4 for Tier 3

---

## Verification Protocols

### Chain of Verification (CoVe)

```
1. EXTRACT claims from draft
2. GENERATE verification questions (specific, checkable)
3. ANSWER independently (don't look at draft!)
4. COMPARE and CORRECT
5. ASSIGN confidence markers
```

**Critical**: Step 3 must be independent to prevent confirmation bias

### Self-Consistency (SC)

```
For critical claim:
→ Path 1: First principles ─────► Conclusion
→ Path 2: Different method ─────► Conclusion  
→ Path 3: Alternative view ─────► Conclusion
→ VOTE: 3/3 agree = ^verified | 2/3 = ^established | diverge = ^contested
```

---

## Confidence Markers

| Marker | Probability | Indicators |
|--------|-------------|------------|
| **^verified** | >90% | Multiple sources, SC >80%, no counter-evidence |
| **^established** | 70-90% | Well-supported, broad consensus |
| **^provisional** | 50-70% | Supported but uncertain, may change |
| **^contested** | 30-50% | Expert disagreement, multiple interpretations |
| **^speculative** | <30% | Limited evidence, theoretical |

---

## Domain-Specific Emphasis

| Domain | Priority Focus |
|--------|----------------|
| **Scientific/Technical** | Evidence strength, replicability, precision |
| **Historical/Factual** | Dates, names, sequences, attributions |
| **Theoretical/Philosophical** | Logical consistency, counterarguments |
| **Methodological/Procedural** | Step accuracy, completeness, edge cases |

---

## Quality Checkpoint

### Pre-Generation
```
[ ] Tier selected appropriately
[ ] Subtopics identified with word budgets
[ ] Layers planned per concept
[ ] Claims flagged for verification
```

### Post-Generation
```
Score 1-10:
[ ] Depth (all layers present)
[ ] Accuracy (claims verified)
[ ] Clarity (examples, analogies)
[ ] Completeness (all aspects)
[ ] Structure (logical flow)
[ ] Utility (actionable)

COMPOSITE ≥ 8.0 → PASS
COMPOSITE < 8.0 → REVISE
```

---

## Tree of Thoughts (Tier 3)

### Dimensional Decomposition
```
Dimension 1: [Primary aspect] ─ Budget: [words]
Dimension 2: [Secondary aspect] ─ Budget: [words]
Dimension 3: [Additional aspect] ─ Budget: [words]
```

### Multi-Path Exploration (per dimension)
```
Path 1: [Approach] ─ Strengths: [X] ─ Score: [N/10]
Path 2: [Alternative] ─ Strengths: [Y] ─ Score: [N/10]
Path 3: [Third angle] ─ Strengths: [Z] ─ Score: [N/10]

SELECT: Primary = highest score
INTEGRATE: Supporting paths for nuance
```

### Path Scoring Criteria
- Explanatory power (1-10)
- Evidence strength (1-10)
- Pedagogical clarity (1-10)
- Completeness (1-10)
- **Overall** = Average

---

## Multi-Path Integration

```
CONVERGENT (paths agree):
→ High-confidence claims, multiple validation

COMPLEMENTARY (paths add different dimensions):
→ Path A contributes X understanding
→ Path B adds Y aspect
→ Combined reveals emergent Z

PRODUCTIVE TENSION (useful friction):
→ Disagreement enriches understanding
→ Note as ^contested with perspectives
```

---

## Research Integration

```
BEFORE SEARCHING:
- What can I answer from training?
- What specifically needs research?
- What's the search strategy?

MULTI-SOURCE RULE:
- Never single-source for important claims
- Synthesize 2-3 sources minimum
- Note consensus vs disagreement
```

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| **Shallow treatment** | <100 words per concept | Add missing layers |
| **Unverified claims** | No confidence markers | Run CoVe protocol |
| **Missing dimensions** | Incomplete coverage | Add ToT decomposition |
| **Confirmation bias** | Verification matches draft | Independent checking |
| **Low consensus** | SC paths diverge | Mark ^contested, note views |

---

## Output Templates

### Tier 3 (Comprehensive)
```
# [Topic]
> Overview (2-3 sentences)

## Foundational Understanding
[Core + context + mechanism]

## Detailed Exploration
### [Dimension 1] - [500-800 words]
### [Dimension 2] - [500-800 words]

## Integration & Synthesis
## Advanced Considerations
## Related Topics
```

### Tier 2 (Technical)
```
# [Title]
## Overview [definition, when, benefits]
## How It Works [mechanism, components]
## Implementation [steps, variations]
## Practical Considerations [pitfalls, troubleshooting]
## Examples
```

### Tier 1 (Quick)
```
# [Topic]
## Summary [direct answer]
## Key Points [3-5 bullets]
## Related [[links]]
```

---

## Research Foundation

| Technique | Source | Function |
|-----------|--------|----------|
| **Tree of Thoughts** | Yao et al. 2023 | Multi-path exploration |
| **Self-Consistency** | Wang et al. 2022 | Ensemble validation |
| **Chain of Verification** | Dhuliawala et al. 2023 | Hallucination reduction |
| **Self-Refine** | Madaan et al. 2023 | Iterative improvement |
| **Skeleton of Thoughts** | Ning et al. 2023 | Structural scaffolding |

---

## Performance Benchmarks

| Technique | Baseline | Enhanced | Improvement |
|-----------|----------|----------|-------------|
| ToT (Game of 24) | 7.3% | 74% | +67pp |
| Self-Consistency (GSM8K) | 46.9% | 74.4% | +27.5pp |
| CoVe (Biographies) | 45% halluc | 23% halluc | -49% relative |
| Combined ToT+SC | 74% | 85% | +11pp |

---

## Quick Decision Tree

```
START: What's the query?

├─ Single concept/definition?
│   └─► TIER 1: Linear CoT + basic verify
│
├─ Technical process/guide?
│   └─► TIER 2: Enhanced CoT + SC(3) + CoVe
│
├─ "Comprehensive/thorough" requested?
│   └─► TIER 3: Full ToT + SC(5) + CoVe + Meta
│
└─ Unsure?
    └─► Default TIER 2, escalate if complexity emerges
```

---

**Full Guide**: See comprehensive-reasoning-report-system-v2.md
**Clean Prompt**: See comprehensive-reasoning-prompt-clean.md
