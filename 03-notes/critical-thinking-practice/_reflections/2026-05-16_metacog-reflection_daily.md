---
title: "Critical Thinking Practice — Dashboard & Index"
aliases:
  - "CT Practice Dashboard"
  - "Critical Thinking Index"
  - "Deliberate Practice Dashboard"
tags:
  - dashboard
  - critical-thinking
  - deliberate-practice
  - meta-knowledge
  - cognitive-self-development
cssclasses:
  - wide-page
  - dashboard
created: 2025-05-16
status: live-dashboard
type: dashboard
companion-to:
  - "[[critical-thinking-deliberate-practice-template]]"
  - "[[paul-elder-framework-reference]]"
  - "[[critical-thinking-frameworks-master-reference]]"
---

# 🧠 Critical Thinking Practice — Dashboard

> [!abstract] Dashboard Purpose
> This dashboard is the **meta-view** over your [[Deliberate Practice]] sessions. Where each individual session captures one act of reasoning, this dashboard surfaces patterns invisible at the session level: which **Elements** you consistently underweight, which **Standards** you systematically skip, which **Intellectual Traits** are persistent strengths or weaknesses, and how your **Developmental Stage** is trending over time.
> 
> The triangulation principle applies here too: aggregate metrics expose what single-session introspection cannot. The patterns are diagnostic — they tell you what to work on next.

> [!key-claim] How to Use This Dashboard
> 1. **Weekly:** Open this file. Review the "Recent Sessions" and "Due for Review" panels. Complete any reviews that have come due.
> 2. **Monthly:** Examine the "Persistent Weaknesses" patterns. Adjust your next sessions' difficulty and trait-focus to target the weakest dimensions.
> 3. **Quarterly:** Audit the "Developmental Stage Progression" — has the trendline moved? If not, what would need to change in your practice approach?

---

## 📑 Dashboard Navigation

1. [[#🔥 Active Work — Sessions Due for Review]]
2. [[#📋 All Recent Practice Sessions]]
3. [[#📊 Aggregate Score Trends]]
4. [[#🎯 Persistent Weakness Patterns]]
5. [[#🌟 Trait Development Trajectory]]
6. [[#🏛️ Framework Usage Distribution]]
7. [[#🧭 Domain & Difficulty Patterns]]
8. [[#📈 Developmental Stage Tracking]]
9. [[#🪞 Metacognitive Patterns]]
10. [[#🎓 Practice Discipline Metrics]]
11. [[#📚 Reference & Resource Links]]

---

# 🔥 Active Work — Sessions Due for Review

> [!warning] Spaced Review Is Where Insight Consolidates
> Per [[Spaced Repetition]] principles, deliberate practice sessions need scheduled re-engagement to translate momentary insight into durable cognitive change. The first three days are the highest-leverage interval; the 30- and 90-day reviews verify whether the action items actually shaped behavior.

### 📅 Reviews Due Today or Overdue

```dataview
TABLE
  primary-framework AS "Framework",
  difficulty AS "Diff",
  date-practiced AS "Originally Practiced",
  review-due AS "Review Due",
  (date(today) - review-due).days AS "Days Overdue"
FROM #critical-thinking-practice
WHERE review-due <= date(today) AND status != "archived"
SORT review-due ASC
```

### 🔜 Upcoming Reviews (Next 7 Days)

```dataview
TABLE
  primary-framework AS "Framework",
  date-practiced AS "Practiced",
  review-due AS "Due",
  (review-due - date(today)).days AS "Days Until Due"
FROM #critical-thinking-practice
WHERE review-due > date(today) AND review-due <= date(today) + dur(7 days)
SORT review-due ASC
```

---

# 📋 All Recent Practice Sessions

### Latest 20 Sessions — At a Glance

```dataview
TABLE
  primary-framework AS "Framework",
  session-type AS "Type",
  difficulty AS "Diff",
  stakes AS "Stakes",
  overall-score AS "Overall",
  developmental-stage AS "Stage"
FROM #critical-thinking-practice
SORT date-practiced DESC
LIMIT 20
```

### Sessions by Domain

```dataview
TABLE
  domain AS "Domain",
  length(rows) AS "Sessions",
  round(average(rows.difficulty), 1) AS "Avg Difficulty",
  round(average(rows.overall-score), 2) AS "Avg Score"
FROM #critical-thinking-practice
WHERE domain
GROUP BY domain
SORT length(rows) DESC
```

### Currently In-Progress (Not Yet Completed)

```dataview
TABLE
  primary-framework AS "Framework",
  date-practiced AS "Started",
  difficulty AS "Diff"
FROM #critical-thinking-practice
WHERE status = "in-progress"
SORT date-practiced DESC
```

---

# 📊 Aggregate Score Trends

> [!definition] Score Interpretation
> All scores use the Paul-Elder rubric scale: **1 = Beginning**, **2 = Developing**, **3 = Competent**, **4 = Advanced**. A composite score of **3+ across all rubrics** represents competent practicing-level critical thinking. The goal is not perfect scores but **identifying the lowest-scoring dimension** as your next development target.

### Average Scores by Rubric (Last 10 Sessions)

```dataview
TABLE WITHOUT ID
  "Elements" AS "Rubric",
  round(average(elements-score), 2) AS "Avg Score"
FROM #critical-thinking-practice
WHERE elements-score
LIMIT 10
```

```dataview
TABLE WITHOUT ID
  "Standards" AS "Rubric",
  round(average(standards-score), 2) AS "Avg Score"
FROM #critical-thinking-practice
WHERE standards-score
LIMIT 10
```

```dataview
TABLE WITHOUT ID
  "Traits" AS "Rubric",
  round(average(traits-score), 2) AS "Avg Score"
FROM #critical-thinking-practice
WHERE traits-score
LIMIT 10
```

```dataview
TABLE WITHOUT ID
  "Integration" AS "Rubric",
  round(average(integration-score), 2) AS "Avg Score"
FROM #critical-thinking-practice
WHERE integration-score
LIMIT 10
```

### Overall Score Trajectory (All Sessions, Chronological)

```dataview
TABLE
  date-practiced AS "Date",
  overall-score AS "Overall",
  elements-score AS "Elements",
  standards-score AS "Standards",
  traits-score AS "Traits",
  integration-score AS "Integration"
FROM #critical-thinking-practice
WHERE overall-score
SORT date-practiced ASC
```

---

# 🎯 Persistent Weakness Patterns

> [!key-claim] The Diagnostic Pattern
> If the same Element or Standard appears repeatedly in the "weakest" slot across many sessions, that is your **primary development site**. Random variation produces different weaknesses each session; systematic deficit produces the same one repeatedly. The frequency table below diagnoses which it is.

### Element That Most Frequently Scored Lowest

```dataview
TABLE
  weakest-element AS "Element",
  length(rows) AS "Times Identified",
  round(length(rows) * 100 / length(this.file.outlinks), 1) AS "% of Sessions"
FROM #critical-thinking-practice
WHERE weakest-element
GROUP BY weakest-element
SORT length(rows) DESC
```

### Standard That Most Frequently Scored Lowest

```dataview
TABLE
  weakest-standard AS "Standard",
  length(rows) AS "Times Identified"
FROM #critical-thinking-practice
WHERE weakest-standard
GROUP BY weakest-standard
SORT length(rows) DESC
```

### Element Scores Across Recent Sessions

```dataview
TABLE
  purpose-score AS "P",
  question-score AS "Q",
  information-score AS "I",
  inference-score AS "Inf",
  concepts-score AS "C",
  assumptions-score AS "A",
  implications-score AS "Imp",
  pov-score AS "PoV"
FROM #critical-thinking-practice
WHERE purpose-score
SORT date-practiced DESC
LIMIT 15
```

### Most-Detected Fallacies

```dataview
TABLE
  most-damaging-fallacy AS "Most Damaging Fallacy",
  length(rows) AS "Times Identified"
FROM #critical-thinking-practice
WHERE most-damaging-fallacy
GROUP BY most-damaging-fallacy
SORT length(rows) DESC
```

### Active Bias Patterns

```dataview
TABLE
  active-bias AS "Most Active Bias",
  length(rows) AS "Sessions"
FROM #critical-thinking-practice
WHERE active-bias
GROUP BY active-bias
SORT length(rows) DESC
```

---

# 🌟 Trait Development Trajectory

> [!definition] Trait-Skill Asymmetry
> Per [[CCTDI]] research cited in the master reference: "Disposition predicts skill deployment better than skill predicts disposition use." A person with strong skills but weak dispositions reasons well only when prompted; strong dispositions drive lifelong skill development. **Trait scores deserve at least as much attention as skill scores.**

### Trait Focus Distribution Across Sessions

```dataview
TABLE
  target-trait AS "Target Trait",
  length(rows) AS "Sessions Focused",
  round(average(rows.traits-score), 2) AS "Avg Traits Score When Focused"
FROM #critical-thinking-practice
WHERE target-trait
GROUP BY target-trait
SORT length(rows) DESC
```

### Most Frequently Strongest Trait

```dataview
TABLE
  trait-strongest AS "Strongest Trait",
  length(rows) AS "Times Strongest"
FROM #critical-thinking-practice
WHERE trait-strongest
GROUP BY trait-strongest
SORT length(rows) DESC
```

### Most Frequently Weakest Trait (Development Target)

```dataview
TABLE
  trait-weakest AS "Weakest Trait",
  length(rows) AS "Times Weakest"
FROM #critical-thinking-practice
WHERE trait-weakest
GROUP BY trait-weakest
SORT length(rows) DESC
```

### Intellectual Vices Detected

```dataview
TABLE
  vice-detected AS "Vice",
  length(rows) AS "Times Detected"
FROM #critical-thinking-practice
WHERE vice-detected
GROUP BY vice-detected
SORT length(rows) DESC
```

---

# 🏛️ Framework Usage Distribution

> [!example] Practice Discipline Diagnostic
> If you only ever use one framework, you're not triangulating — you're worshipping. If you never use a particular framework, you're missing what it would reveal. Healthy practice cycles through frameworks.

### Sessions by Primary Framework

```dataview
TABLE
  primary-framework AS "Framework",
  length(rows) AS "Sessions",
  round(length(rows) * 100 / length(this.file.outlinks), 1) AS "% of Practice",
  round(average(rows.overall-score), 2) AS "Avg Score"
FROM #critical-thinking-practice
WHERE primary-framework
GROUP BY primary-framework
SORT length(rows) DESC
```

### Framework Coverage Recommendation

> [!warning] Triangulation Check
> If any framework shows < 10% usage, consider deliberately selecting it for your next practice session. The frameworks you avoid most often are usually those that would reveal what you most want to ignore.

---

# 🧭 Domain & Difficulty Patterns

### Practice Across Domains

```dataview
TABLE
  domain AS "Domain",
  length(rows) AS "Sessions",
  round(average(rows.difficulty), 1) AS "Avg Difficulty",
  round(average(rows.overall-score), 2) AS "Avg Score"
FROM #critical-thinking-practice
WHERE domain
GROUP BY domain
SORT length(rows) DESC
```

### Difficulty Distribution

```dataview
TABLE
  difficulty AS "Difficulty Level",
  length(rows) AS "Sessions",
  round(average(rows.overall-score), 2) AS "Avg Score"
FROM #critical-thinking-practice
WHERE difficulty
GROUP BY difficulty
SORT difficulty ASC
```

> [!key-claim] The Deliberate Practice Zone
> Per [[Deliberate Practice]] research, the productive zone is **difficulty 3–4** — challenging enough to require genuine effort, not so hard that resolution becomes impossible. If your difficulty distribution skews toward 1–2, you're rehearsing competence rather than building it. If it skews toward 5, you're flailing rather than progressing.

### Stakes Distribution

```dataview
TABLE
  stakes AS "Stakes",
  length(rows) AS "Sessions",
  round(average(rows.overall-score), 2) AS "Avg Score"
FROM #critical-thinking-practice
WHERE stakes
GROUP BY stakes
SORT length(rows) DESC
```

---

# 📈 Developmental Stage Tracking

> [!key-claim] Stage Movement Requires Months
> Per the Paul-Elder reference: "Each stage transition typically requires months of consistent effort. Most adults plateau at Stage 2 or 3 without intentional intervention." If your stage estimates haven't moved in 90 days of practice, that is a diagnostic finding — adjust your practice approach.

### Estimated Stage Progression

```dataview
TABLE
  date-practiced AS "Date",
  developmental-stage AS "Stage",
  overall-score AS "Score",
  primary-framework AS "Framework"
FROM #critical-thinking-practice
WHERE developmental-stage
SORT date-practiced ASC
```

### Stage Distribution

```dataview
TABLE
  developmental-stage AS "Stage Estimate",
  length(rows) AS "Sessions"
FROM #critical-thinking-practice
WHERE developmental-stage
GROUP BY developmental-stage
SORT developmental-stage ASC
```

---

# 🪞 Metacognitive Patterns

> [!definition] Metacognitive Pattern Detection
> The metacognitive fields captured in each session — verdict shifts, confidence deltas, closing insights — reveal the *quality* of your self-regulation over time. A practitioner whose verdicts never shift may be using analysis to confirm pre-existing views; one whose confidence never calibrates may be incapable of holding views provisionally.

### Verdict Shifts Across Sessions

```dataview
TABLE
  verdict-shifted AS "Shifted?",
  length(rows) AS "Count"
FROM #critical-thinking-practice
WHERE verdict-shifted
GROUP BY verdict-shifted
```

> [!warning] Shift Pattern Diagnostic
> If `verdict-shifted = false` in > 80% of sessions, ask: am I practicing critical thinking, or am I practicing rationalization? Genuine inquiry produces verdict updates regularly. Pure confirmation of existing views suggests motivated reasoning.

### Confidence Calibration Patterns

```dataview
TABLE
  date-practiced AS "Date",
  initial-confidence AS "Initial",
  final-confidence AS "Final",
  emotional-charge AS "Emotion"
FROM #critical-thinking-practice
WHERE initial-confidence
SORT date-practiced DESC
LIMIT 15
```

### Recent Closing Insights

```dataview
TABLE
  closing-insight AS "What I Learned About Myself as a Thinker"
FROM #critical-thinking-practice
WHERE closing-insight
SORT date-practiced DESC
LIMIT 10
```

### Load-Bearing Assumptions Surfaced

```dataview
TABLE
  date-practiced AS "Date",
  load-bearing-assumption AS "Load-Bearing Assumption"
FROM #critical-thinking-practice
WHERE load-bearing-assumption
SORT date-practiced DESC
LIMIT 15
```

---

# 🎓 Practice Discipline Metrics

### Session Frequency

```dataview
TABLE WITHOUT ID
  dateformat(date-practiced, "yyyy-MM") AS "Month",
  length(rows) AS "Sessions"
FROM #critical-thinking-practice
WHERE date-practiced
GROUP BY dateformat(date-practiced, "yyyy-MM")
SORT key DESC
LIMIT 12
```

### Average Session Duration

```dataview
TABLE WITHOUT ID
  "All Sessions" AS "Cohort",
  round(average(duration-minutes), 0) AS "Avg Minutes",
  round(min(duration-minutes), 0) AS "Min",
  round(max(duration-minutes), 0) AS "Max"
FROM #critical-thinking-practice
WHERE duration-minutes > 0
```

### Reviews Completed

```dataview
TABLE
  date-practiced AS "Practiced",
  review-count AS "Reviews Done",
  review-due AS "Next Due"
FROM #critical-thinking-practice
WHERE review-count > 0
SORT review-count DESC
LIMIT 20
```

### Discipline Self-Audit Questions

> [!example] Weekly Self-Audit
> - How many sessions did I complete this week? **Target:** 3–5
> - What was my average difficulty? **Target:** 3.0+
> - Did I do any reviews of past sessions? **Target:** All reviews due
> - Did I cycle through frameworks, or stay in my comfort zone?
> - Did my verdict shift in at least one session?

---

# 🔧 Quick Actions

### Start a New Practice Session

> [!example] Workflow
> 1. Trigger Templater with the `critical-thinking-deliberate-practice-template`
> 2. Answer the setup prompts
> 3. Work through the framework sections that apply
> 4. Always complete the metacognitive reflection and rubrics
> 5. Set review reminders

### Choose Today's Focus

> **If today is a low-energy day:** Use FRISCO (Ennis) — rapid, six-step audit
> **If today is a moderate day:** Use Browne-Keeley 10-Question Sweep
> **If today is a high-focus day:** Use Paul-Elder Full Analysis
> **If today is a triangulation day:** Use Multi-Framework Triangulation on a high-stakes subject

### Targeted Practice by Weakness

Based on the patterns surfaced above, target the following in your next session:

- **Weakest Element overall:** *(see Persistent Weakness Patterns section)*
- **Weakest Standard overall:** *(see Persistent Weakness Patterns section)*
- **Weakest Trait overall:** *(see Trait Development Trajectory section)*
- **Underused Framework:** *(see Framework Usage Distribution section)*

---

# 📚 Reference & Resource Links

### Core References
- [[paul-elder-framework-reference]] — Full Paul-Elder framework treatment
- [[critical-thinking-frameworks-master-reference]] — Multi-framework synthesis
- [[critical-thinking-deliberate-practice-template]] — Session template

### Foundational Concepts
- [[Critical Thinking]] · [[Deliberate Practice]] · [[Metacognition]] · [[Self-Regulated Learning]]
- [[Elements of Thought]] · [[Intellectual Standards]] · [[Intellectual Virtues]]
- [[Dual Process Theory]] · [[System 1 and System 2]]
- [[Spaced Repetition]] · [[Schema Theory]] · [[Cognitive Load Theory]]

### Framework References
- [[Paul-Elder Framework]] · [[Ennis Streamlined Conception]] · [[FRISCO Model]]
- [[Toulmin Argument Model]] · [[Browne-Keeley 10 Questions]] · [[SEE-I Method]]
- [[Delphi Consensus]] · [[Halpern Critical Thinking]] · [[Watson-Glaser]]
- [[Bloom's Taxonomy]] · [[SOLO Taxonomy]] · [[Webb's Depth of Knowledge]]
- [[CCTDI]] · [[Habits of Mind]] · [[Reflective Judgment Model]]

### Trait Development
- [[Intellectual Humility]] · [[Intellectual Courage]] · [[Intellectual Empathy]]
- [[Intellectual Autonomy]] · [[Intellectual Integrity]] · [[Intellectual Perseverance]]
- [[Confidence in Reason]]

### Cognitive Pitfalls
- [[Cognitive Bias]] · [[Confirmation Bias]] · [[Motivated Reasoning]]
- [[Fallacies]] · [[Heuristics and Biases]]

---

> [!quote] Closing Reminder
> "Critical thinking is the art of analyzing and evaluating thinking with a view to improving it." — Richard Paul & Linda Elder
> 
> The dashboard above is *not* a measure of your worth as a thinker. It is a diagnostic instrument for finding where the next development is. The metric that matters is whether the patterns it surfaces inform what you do next.

---

*Dashboard version: 1.0.0 · Companion to: [[critical-thinking-deliberate-practice-template]]*
*Last refresh: queries are live — refresh by reopening this note*
