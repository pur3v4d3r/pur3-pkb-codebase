<%*
// ═══════════════════════════════════════════════════════════════════════════
// SRL MONTHLY PRACTICE REVIEW TEMPLATE v1.0
// Meta-reflection across sessions for long-term SRL development tracking
// ═══════════════════════════════════════════════════════════════════════════

const reviewMonth = await tp.system.prompt("📅 Which month/year is this review for? (e.g., March 2026)");
const reviewDate = tp.date.now("YYYY-MM-DD");
_%>
---
type: srl-monthly-review
status: active
date: <% reviewDate %>
review-period: "<% reviewMonth %>"
created: <% reviewDate %>
tags:
  - srl-system
  - monthly-review
  - meta-reflection
  - metacognitive-calibration
  - srl-development
aliases:
  - "SRL Monthly Review <% reviewMonth %>"
---

# 📊 SRL Monthly Practice Review — <% reviewMonth %>

> [!abstract] Purpose
> This review examines patterns across the month's reading sessions to assess long-term [[metacognitive-calibration|metacognitive calibration]] development, [[Attribution (Heider, 1958)|attribution pattern]] health, strategy effectiveness, and overall SRL growth. This is the meta-level awareness that [[barry-zimmerman|Zimmerman]] calls "self-regulatory self-efficacy" — confidence in your ability to regulate your own learning. See [[metacognitive-regulation]] and [[deliberate-practice]].

---

## 📈 Quantitative Summary

### Session Data (Auto-Populated via Dataview)

```dataviewjs
const reviewPeriod = dv.current()["review-period"];
// Adjust the date filter below to match your review period
const sessions = dv.pages('#srl-session')
    .where(s => s["reflection-completed"] === true);

if (sessions.length === 0) {
    dv.paragraph("*No completed sessions found. Adjust the filter or complete sessions first.*");
} else {
    const avgEfficacyPre = sessions
        .where(s => s["self-efficacy-pre"] > 0)
        .map(s => s["self-efficacy-pre"]).values;
    const avgProcessIntegrity = sessions
        .where(s => s["process-integrity-rating"] > 0)
        .map(s => s["process-integrity-rating"]).values;
    
    const mean = arr => arr.length > 0 
        ? (arr.reduce((a, b) => a + b, 0) / arr.length).toFixed(1) 
        : "—";
    
    const controllable = sessions
        .where(s => s["attribution-controllable"] === true).length;
    const defensive = sessions
        .where(s => s["defensive-inference-detected"] === true).length;
    
    dv.table(["Metric", "Value"], [
        ["Sessions completed", sessions.length],
        ["Average self-efficacy (pre)", mean(avgEfficacyPre)],
        ["Average process integrity", mean(avgProcessIntegrity)],
        ["Controllable attributions", `${controllable}/${sessions.length}`],
        ["Defensive inferences detected", `${defensive}/${sessions.length}`],
    ]);
}
```

### Manual Data (Fill In)

| Metric | Value |
|--------|-------|
| Sessions completed this month | |
| Average Forethought quality (1–10) | |
| Average Self-Reflection quality (1–10) | |
| Average Comprehension Achievement (1–10) | |
| New permanent notes created | |
| New wiki-links established | |

---

## 📉 Trend Analysis

### Comprehension Trend

**First week vs. last week of the month:**
`INPUT[inlineSelect(option(Improving), option(Flat), option(Variable), option(Declining)):comprehension-trend]`

**Evidence for this assessment:**
> 

### Process Goal Completion Trend

`INPUT[inlineSelect(option(Improving), option(Flat), option(Variable), option(Declining)):process-goal-trend]`

**Most consistently met process goal:**
> 

**Most consistently missed process goal:**
> 

### Self-Efficacy Trend

`INPUT[inlineSelect(option(Increasing), option(Stable), option(Decreasing)):efficacy-trend]`

**If decreasing — controllable attribution:**
> 

---

## 🔬 Attribution Pattern Review

> [!important] This is the most critical section of the monthly review.
> Attribution patterns are the primary diagnostic for SRL cycle health. See [[Attribution (Heider, 1958)]] and [[attribution-retraining]].

**Most common attribution for comprehension difficulties this month:**
> 

**Is this attribution consistently:**
- [ ] Specific (names a mechanism, not a global trait)?
- [ ] Unstable (implies things could be different)?
- [ ] Controllable (within my influence)?

**If any box is unchecked:**
> What is the most accurate controllable reframe? *(Use [[SRL-Quick-Reference-Cards]] Card 2)*

**Attribution evolution since last review:**
> *(Are attributions becoming more specific and controllable over time? This IS the development.)*

---

## 🛠️ Strategy Effectiveness Review

**Strategy that produced best comprehension outcomes:**
> **Which:** 
> **Evidence:** 

**Strategy that consistently underperformed:**
> **Which:** 
> **Attribution:** *(Why didn't it work? Strategy-level explanation.)*

**Strategy to introduce or intensify next month:**
> 

**Strategy to reduce or retire:**
> 

---

## 🔗 PKB Growth Review

**Highest-quality connection made this month:**
> [[]] ↔ [[]] — 

**Most significant gap identified:**
> 

**Knowledge graph development assessment:**
> *(Is the knowledge graph becoming denser and more interconnected? Are new domains being opened?)*

---

## 🧭 Calibration Assessment

> [!tip] This is the Calibration Engine's output check.
> See [[metacognitive-calibration]] and [[SRL-Calibration-Log]].

**Distance between pre-session predictions and actual outcomes has been:**
`INPUT[inlineSelect(option(Decreasing — calibration improving), option(Stable), option(Increasing — calibration degrading)):calibration-trend]`

**The most common direction of miscalibration:**
`INPUT[inlineSelect(option(Overconfident — fluency illusion), option(Underconfident — anxiety-driven), option(Well-calibrated)):miscalibration-direction]`

**If overconfident:** Review [[the-fluency-illusion]] and consider adding more demanding generativity tests to Cold Reconstruction.

**If underconfident:** Review [[self-efficacy]] sources and ensure mastery experiences are being recognized in Self-Reaction zones.

---

## 💪 Self-Efficacy Assessment

**Current self-efficacy for complex PKB reading (1–10):** ___

**Compared to last month:**
`INPUT[inlineSelect(option(Higher), option(Same), option(Lower)):efficacy-comparison]`

**If lower — controllable attribution and planned response:**
> 

**Mastery experience from this month I can draw on:**
> *(Name a specific session where you achieved genuine comprehension — this is the raw material of [[self-efficacy|self-efficacy]].)*

---

## 🎯 Goals for Next Month

### Forethought Development
**One specific Forethought improvement:**
> 

### Self-Reflection Development
**One specific Self-Reflection improvement:**
> 

### Strategy Development
**One new strategy to systematically trial:**
> 

### System Development
**One improvement to the SRL system itself:**
> *(Template modification? New tracking metric? Dataview query? Plugin integration?)*

---

## 💬 Meta-Reflection *(Mastery Grammar)*

> [!quote] Close with [[achievement-goal-theory|mastery-framed]] reflection. See [[mastery-goal-orientation]].

**What has my SRL practice taught me about how I learn?**
> 

**What is one thing I can do now that I genuinely could not do at the start of this month?**
> 

**What question about my own learning am I now more precisely able to ask?**
> 

---

## ✅ Action Items

- [ ] Update [[SRL-Living-Learning-Agenda]] with next month's goals
- [ ] Review [[SRL-Calibration-Log]] for trend confirmation
- [ ] Implement strategy changes identified above
- [ ] Schedule next monthly review: ___
- [ ] Consider scaffold fading: any zones that can be simplified? See [[Scaffolded Fading]]

---

> [!connections-and-links]
> **PKB Connections:**
> - [[Zimmerman's-Cyclical-SRL-Model]] — This review evaluates the cycle's long-term health
> - [[metacognitive-calibration]] — Calibration trend is the primary developmental indicator
> - [[deliberate-practice]] — The monthly review IS the deliberate practice feedback mechanism
> - [[self-efficacy]] — Self-efficacy trajectory reveals motivational system health
> - [[Attribution (Heider, 1958)]] — Attribution pattern review is the most critical diagnostic
> - [[Scaffolded Fading]] — Monthly review is where scaffold reduction decisions are made
