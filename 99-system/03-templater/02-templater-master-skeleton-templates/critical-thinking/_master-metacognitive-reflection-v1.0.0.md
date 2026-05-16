---
title: "Metacognitive Reflection — daily 2026-05-16"
aliases: []
tags:
  - critical-thinking
  - metacognition
  - reflection
  - deliberate-practice
  - self-regulated-learning
created: 2026-05-16
modified: 2026-05-16
type: metacognitive-reflection
period: daily
status: in-progress
period-start: 
period-end: 2026-05-16
sessions-reviewed: 
weakest-standard: 
strongest-virtue-exercised: 
related: []
---

# Metacognitive Reflection — daily

> [!abstract] Purpose
> This is **second-order practice**: not reasoning *about a topic*, but reasoning *about my reasoning*. Following [[Flavell]]'s [[Metacognition]] framework — monitoring **what I know**, **how I think**, and **how to regulate** the process.

---

## 📅 Period Reviewed

**From:** `INPUT[date:period-start]` **to:** 2026-05-16
**Sessions reviewed:** `INPUT[number:sessions-reviewed]`

---

## 📊 1 · Sessions in this Period (auto-pulled)

```dataview
TABLE WITHOUT ID
  file.link AS "Session",
  framework AS "Framework",
  object-type AS "Object",
  overall-rigor-score AS "Rigor",
  status AS "Status"
FROM "03-notes/critical-thinking-practice"
WHERE type = "critical-thinking-session"
  AND file.cday >= date(this.period-start)
  AND file.cday <= date(this.period-end)
SORT file.cday DESC
```

---

## 🧠 2 · Metacognitive Knowledge — What I Notice About *Myself* as a Thinker

> [!definition] [[Metacognitive Knowledge]]
> Awareness of *person* variables (my cognitive tendencies), *task* variables (what this kind of thinking demands), and *strategy* variables (which tools work for me).

### Person Knowledge — *What do I now know about how I think?*
- Recurring blind spots I've identified: 
- Cognitive strengths I leveraged: 
- Emotional patterns that affected my reasoning: 

### Task Knowledge — *What did I learn about the demands of critical thinking?*
- Which types of questions/objects are hardest for me? 
- Which frameworks fit which problems best (in my experience)?

### Strategy Knowledge — *Which strategies actually worked?*
- Most useful framework this period: 
- Most useful single technique (steelmanning, SEE-I, surfacing assumptions, etc.): 
- Strategies I tried that didn't help: 

---

## 👁 3 · Metacognitive Monitoring — What Happened *During* My Thinking

> *In-the-moment awareness of my reasoning as it unfolded.*

- Sessions where I caught myself in a [[Cognitive Biases|bias]] **mid-analysis**: 
- Sessions where I caught the bias only **in retrospect**: 
- Sessions where I likely missed biases entirely: 

**Most common bias I committed this period:**
> 

---

## ⚙ 4 · Metacognitive Regulation — How I Steered My Thinking

> *Planning · Monitoring · Evaluating — the [[Self-Regulated Learning|SRL]] triad applied to CT.*

### Planning
- Did I pick the right framework for each session's needs? 
- Did I allocate enough time, or did I rush?

### Monitoring
- Where did I notice my reasoning weakening and **adjust course**?
- Where did I notice but **fail to adjust**?

### Evaluating
- Are my self-ratings on the [[Intellectual Standards]] calibrated, or am I being too generous / too harsh? *(Compare to past sessions — am I always rating the same way?)*

---

## 📉 5 · Standards Performance Trend (auto)

```dataviewjs
const sessions = dv.pages('"03-notes/critical-thinking-practice"')
  .where(p => p.type === "critical-thinking-session")
  .where(p => p.file.cday >= dv.current()["period-start"]);
const stds = ["clarity","accuracy","precision","relevance","depth","breadth","logic","significance","fairness"];
const rows = stds.map(s => {
  const vals = sessions.map(p => Number(p["rating-" + s])).filter(v => !isNaN(v) && v > 0).values;
  if (vals.length === 0) return [s, "—", "—"];
  const avg = (vals.reduce((a,b)=>a+b,0) / vals.length).toFixed(2);
  return [s, avg, vals.length];
});
dv.table(["Standard", "Avg Score", "n"], rows);
```

**Weakest standard this period:** `INPUT[inlineSelect(option(clarity), option(accuracy), option(precision), option(relevance), option(depth), option(breadth), option(logic), option(significance), option(fairness)):weakest-standard]`

**Concrete plan to strengthen it next period:**
> 

---

## 🌱 6 · Intellectual Virtues Inventory

> [!definition] [[Intellectual Virtues]]
> Stable dispositions of mind that critical thinkers develop over time. Practice without virtue cultivation produces technique without character.

| Virtue | Exercised this period? | Evidence |
|---|---|---|
| [[Intellectual Humility]] — knowing the limits of my knowledge | `INPUT[toggle:v-humility]` | |
| [[Intellectual Courage]] — facing ideas I'd rather avoid | `INPUT[toggle:v-courage]` | |
| [[Intellectual Empathy]] — genuinely entering opposing views | `INPUT[toggle:v-empathy]` | |
| [[Intellectual Autonomy]] — thinking for myself | `INPUT[toggle:v-autonomy]` | |
| [[Intellectual Integrity]] — applying same standards to self and others | `INPUT[toggle:v-integrity]` | |
| [[Intellectual Perseverance]] — pushing through difficulty | `INPUT[toggle:v-perseverance]` | |
| [[Confidence in Reason]] — trusting the process | `INPUT[toggle:v-confidence]` | |
| [[Fairmindedness]] — treating views by their merit, not source | `INPUT[toggle:v-fairmindedness]` | |

**Strongest virtue this period:** `INPUT[inlineSelect(option(humility), option(courage), option(empathy), option(autonomy), option(integrity), option(perseverance), option(confidence), option(fairmindedness)):strongest-virtue-exercised]`

**Virtue most needing cultivation:**
> 

---

## 🎯 7 · Concrete Commitments for Next Period

> [!important] Make them specific, observable, time-bound.

1. 
2. 
3. 

---

## 💡 8 · Key Insight from This Reflection

> *One sentence — the single most important thing I want to remember.*

> 

---

# 🔗 Related

- [[Metacognition]] · [[Metacognitive Monitoring]] · [[Metacognitive Knowledge]]
- [[Self-Regulated Learning]]
- [[Deliberate Practice]]
- [[Intellectual Virtues]]
- [[Critical Thinking Practice MOC]]
