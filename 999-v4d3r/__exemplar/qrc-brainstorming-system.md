---
tags: #quick-reference #brainstorming #reasoning-techniques #one-pager
type: quick-reference
technique: Advanced Brainstorming System
category: integrated-frameworks
version: 2.0.0
---




# 🎯 Advanced Brainstorming System - Quick Reference

## One-Line Summary

Six-phase reasoning framework integrating ToT (exploration) + SC (validation) + CoVe (verification) + Self-Refine (critique) for systematic idea generation.

---

## Framework Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: Problem Architecture                                  │
│  └─ Decompose → Classify → Map Stakeholders                     │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 2: Multi-Path Exploration (Tree of Thoughts)             │
│  ├─ A: First Principles (challenge assumptions)                 │
│  ├─ B: Cross-Domain Analogy (transfer solutions)                │
│  ├─ C: Contrarian (invert conventional wisdom)                  │
│  └─ D: Future-Backwards (work from ideal state)                 │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 3: Deep Evaluation                                       │
│  └─ Score → Synthesize → Build Portfolio                        │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 4: Chain of Verification                                 │
│  └─ Extract Claims → Verify Independently → Revise              │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 5: Meta-Reasoning                                        │
│  └─ Reflect → Detect Blind Spots → Devil's Advocate             │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 6: Structured Output                                     │
│  └─ Summary → Ranked Recommendations → Next Steps               │
└─────────────────────────────────────────────────────────────────┘
```

---

## Technique Integration Map

| Technique | Research | Phase Used | Function |
|-----------|----------|------------|----------|
| **Tree of Thoughts** | Yao 2023 | Phase 2 | Multi-path exploration |
| **Self-Consistency** | Wang 2022 | Phase 3 | Convergence validation |
| **Chain of Verification** | Dhuliawala 2023 | Phase 4 | Hallucination reduction |
| **Self-Refine** | Madaan 2023 | Phase 5 | Iterative improvement |
| **Skeleton of Thoughts** | Ning 2023 | Phase 6 | Structured output |

---

## The Four Approaches (Phase 2)

### A: First Principles
```
"If we had to solve this with no existing infrastructure, 
 what would we build from scratch?"
```
- Challenge assumptions
- Find ground truths
- Rebuild upward

### B: Cross-Domain Analogy
```
"What other fields faced this problem? How did they solve it?"
```
- Biological systems (immune, evolution)
- Physical systems (thermodynamics, networks)
- Social systems (markets, governance)
- Engineering systems (software, logistics)

### C: Contrarian Inversion
```
"What if conventional wisdom is wrong? What would the opposite look like?"
```
- Identify orthodoxy
- Invert the goal
- Find successful contrarians

### D: Future-Backwards
```
"What does success look like in 3-5 years? Work backwards from there."
```
- Envision ideal state
- Map milestones
- Compress timeline

---

## Problem Type → Approach Weighting

| Problem Type | First Principles | Analogy | Contrarian | Future-Backwards |
|--------------|------------------|---------|------------|------------------|
| **TECHNICAL** | 35% | 30% | 15% | 20% |
| **STRATEGIC** | 20% | 20% | 30% | 30% |
| **CREATIVE** | 15% | 35% | 35% | 15% |
| **OPERATIONAL** | 40% | 25% | 10% | 25% |

---

## Chain of Verification Protocol

```
1. EXTRACT claims from recommendations
   "Market size is $10B" → Market Claim
   "Can be built in 6 months" → Feasibility Claim

2. VERIFY independently (don't look at original idea!)
   "What is the market size for X?"
   → Answer without reference to original

3. CLASSIFY result
   VERIFIED | PARTIALLY VERIFIED | UNVERIFIED | UNKNOWN

4. REVISE recommendations
   - Adjust confidence based on verification
   - Flag unverified claims
   - Remove ideas with unverified critical claims
```

---

## Quality Checkpoints

**Before Finalizing Output:**

- [ ] All 4 approaches produced 3+ ideas
- [ ] Ideas range from practical to visionary
- [ ] Key claims verified or flagged
- [ ] Top recommendations received devil's advocate
- [ ] Recommendations align with constraints
- [ ] Confidence matches verification status
- [ ] Next steps are specific + time-bound

---

## Confidence Calibration

| Level | Probability | Indicators |
|-------|-------------|------------|
| **Very High** | >90% | Multiple verified sources, strong precedent |
| **High** | 70-90% | Good evidence, manageable uncertainty |
| **Medium** | 50-70% | Mixed evidence, some unverified claims |
| **Low** | 30-50% | Limited evidence, significant unknowns |
| **Very Low** | <30% | Speculative, novel territory |

---

## Output Structure Template

```
## Executive Summary
- Challenge: [one sentence]
- Key Insight: [discovery]
- Top Recommendation: [headline + confidence]

## Recommendation 1 ⭐ [Confidence]
- Concept: [2-3 sentences]
- Scores: Novelty | Impact | Feasibility | Scalability
- Implementation: Phase 1 → 2 → 3
- Risks: [Risk] → [Mitigation]
- Verification: [status]

## Next Steps
- Immediate: [actions]
- Experiments: [validation tests]

## Blind Spots
- [acknowledged limitations]
```

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| **Mode Collapse** | All ideas similar | Increase temperature, force different approaches |
| **Verification Skip** | High confidence on unverified claims | Mandate Phase 4 execution |
| **Shallow Contrarian** | "Do the opposite" without depth | Require evidence/precedent |
| **Missing Constraints** | Ideas violate stated constraints | Add constraint check |
| **Premature Convergence** | Jump to recommendations too fast | Enforce 3-5 ideas per approach |

---

## Token Budget

| Version | Tokens | Use Case |
|---------|--------|----------|
| **Full** | ~4,500 | Complex challenges, high stakes |
| **Streamlined** | ~1,800 | Quick iteration, smaller contexts |
| **Minimal** | ~800 | Rapid ideation, familiar domains |

---

## Research References

- **ToT**: Yao et al. 2023 - "Tree of Thoughts: Deliberate Problem Solving"
- **SC**: Wang et al. 2022 - "Self-Consistency Improves Chain of Thought"
- **CoVe**: Dhuliawala et al. 2023 - "Chain-of-Verification Reduces Hallucination"
- **Self-Refine**: Madaan et al. 2023 - "Self-Refine: Iterative Refinement"
- **SoT**: Ning et al. 2023 - "Skeleton-of-Thought: Parallel Decoding"

---

**Related**: [[01-reasoning-techniques-guide]], [[04-quality-assurance-guide]], [[06-integration-patterns-guide]]
