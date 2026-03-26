---
# ═══════════════════════════════════════════════════════════════════════════
# SRL CALIBRATION LOG
# Tracks comprehension prediction accuracy and attribution patterns
# ═══════════════════════════════════════════════════════════════════════════
type: srl-calibration-log
status: evergreen
created: "{{date}}"
updated: "{{date}}"
tags:
  - srl-system
  - calibration-log
  - metacognitive-calibration
  - dashboard
  - dataview
aliases:
  - "SRL Calibration Log"
  - "Calibration Tracking"
---

# 📊 SRL Calibration Log

> [!abstract] Purpose
> This log tracks your [[Metacognitive-Calibration|metacognitive calibration]] — the accuracy of your comprehension predictions — across reading sessions. It is the instrument through which the [[Calibration-Engine|Calibration Engine]] produces its primary output: an increasingly accurate self-model. Review this log monthly or after every 10 sessions. See [[Zimmerman's-Cyclical-SRL-Model]], [[Metacognitive-Monitoring]], and [[Metacognitive-Accuracy]].

---

## 🔄 Active Session Tracking

### Recent Sessions (Last 10)

```dataview
TABLE WITHOUT ID
  file.link AS "Session",
  text-title AS "Text",
  self-efficacy-pre AS "Efficacy Pre",
  comprehension-level AS "Comprehension",
  prediction-accuracy AS "Prediction",
  attribution-type AS "Attribution",
  attribution-controllable AS "Controllable?",
  date AS "Date"
FROM #srl-session
SORT date DESC
LIMIT 10
```

### Session Count & Averages

```dataviewjs
const sessions = dv.pages('#srl-session');
const completed = sessions.where(s => s["reflection-completed"] === true);

if (completed.length === 0) {
    dv.paragraph("*No completed sessions yet. Complete your first SRL Reading Session to begin tracking.*");
} else {
    const avgEfficacyPre = completed
        .where(s => s["self-efficacy-pre"] > 0)
        .map(s => s["self-efficacy-pre"])
        .values;
    
    const avgEfficacyPost = completed
        .where(s => s["self-efficacy-post"] > 0)
        .map(s => s["self-efficacy-post"])
        .values;
    
    const avgProcessIntegrity = completed
        .where(s => s["process-integrity-rating"] > 0)
        .map(s => s["process-integrity-rating"])
        .values;
    
    const defensiveCount = completed
        .where(s => s["defensive-inference-detected"] === true)
        .length;
    
    const controllableCount = completed
        .where(s => s["attribution-controllable"] === true)
        .length;
    
    const mean = arr => arr.length > 0 
        ? (arr.reduce((a, b) => a + b, 0) / arr.length).toFixed(1) 
        : "—";
    
    dv.table(
        ["Metric", "Value"],
        [
            ["Total Completed Sessions", completed.length],
            ["Avg Self-Efficacy (Pre)", mean(avgEfficacyPre)],
            ["Avg Self-Efficacy (Post)", mean(avgEfficacyPost)],
            ["Avg Process Integrity", mean(avgProcessIntegrity)],
            ["Controllable Attributions", `${controllableCount}/${completed.length} (${((controllableCount/completed.length)*100).toFixed(0)}%)`],
            ["Defensive Inferences Detected", `${defensiveCount}/${completed.length}`],
        ]
    );
}
```

---

## 📈 Calibration Analysis

### Prediction Accuracy Distribution

```dataview
TABLE WITHOUT ID
  prediction-accuracy AS "Prediction Accuracy",
  length(rows) AS "Count"
FROM #srl-session
WHERE reflection-completed = true
GROUP BY prediction-accuracy
```

### Attribution Pattern Analysis

```dataview
TABLE WITHOUT ID
  attribution-type AS "Attribution Type",
  length(rows) AS "Count",
  min(rows.date) AS "First Seen",
  max(rows.date) AS "Last Seen"
FROM #srl-session
WHERE reflection-completed = true AND attribution-type != ""
GROUP BY attribution-type
SORT length(rows) DESC
```

### Comprehension Level Trend

```dataview
TABLE WITHOUT ID
  date AS "Date",
  text-title AS "Text",
  comprehension-level AS "Comprehension",
  self-efficacy-pre AS "Predicted",
  process-integrity-rating AS "Process Quality"
FROM #srl-session
WHERE reflection-completed = true
SORT date ASC
```

---

## 🎯 Calibration Delta Tracking

> [!info] About Calibration Delta
> The calibration delta measures the gap between your predicted confidence (self-efficacy pre-session) and your actual comprehension outcome. **Decreasing delta = improving calibration.** This is the core output of the [[Calibration-Engine]]. See [[Metacognitive-Calibration]].

```dataviewjs
const sessions = dv.pages('#srl-session')
    .where(s => s["reflection-completed"] === true && s["calibration-delta"] !== 0);

if (sessions.length < 3) {
    dv.paragraph("*Need at least 3 completed sessions with calibration data to show trends. Keep going!*");
} else {
    dv.table(
        ["Date", "Text", "Predicted", "Actual", "Delta", "Direction"],
        sessions.sort(s => s.date, 'asc').map(s => [
            s.date,
            s["text-title"],
            s["self-efficacy-pre"],
            s["comprehension-level"],
            s["calibration-delta"],
            s["calibration-delta"] > 0 ? "⬆️ Overconfident" : 
            s["calibration-delta"] < 0 ? "⬇️ Underconfident" : "✅ Calibrated"
        ])
    );
}
```

---

## 🔍 Pattern Recognition Prompts

> [!reflection] Monthly Review Prompts
> Use these when reviewing the log (monthly or every 10 sessions). See [[Metacognitive-Regulation]].

### Comprehension Prediction Accuracy
> "My comprehension prediction accuracy over the past sessions shows: ___"
> *(Look at the Prediction Accuracy Distribution above)*

### Attribution Patterns
> "The attribution pattern I most commonly generate is: ___"
> "Is this pattern consistently controllable and strategy-based? ___"
> *(If not — see [[Attribution-Retraining]] and the [[SRL-Quick-Reference-Cards]])*

### Adaptive Inference Quality
> "The adaptive inferences I generate most frequently concern: ___"
> "Am I actually implementing these inferences in subsequent Forethought sessions? ___"

### Calibration Trajectory
> "The distance between my pre-session predictions and actual outcomes has been: [decreasing / stable / increasing]"
> **Decreasing distance = improving [[Metacognitive-Calibration|calibration]]** — this is the primary developmental indicator.

### Strategy Effectiveness
> "The strategy that produced the best comprehension outcomes: ___"
> "The strategy I should trial or intensify: ___"

---

## 🏷️ Schema Level Distribution

```dataview
TABLE WITHOUT ID
  schema-level AS "Schema Level",
  length(rows) AS "Sessions",
  round(length(filter(rows, (r) => r.comprehension-level = "Full")) / length(rows) * 100) AS "% Full Comprehension"
FROM #srl-session
WHERE reflection-completed = true
GROUP BY schema-level
```

---

## ⚠️ Diagnostic Flags

### Sessions with Defensive Inferences

```dataview
TABLE WITHOUT ID
  file.link AS "Session",
  text-title AS "Text",
  date AS "Date",
  attribution-type AS "Attribution"
FROM #srl-session
WHERE defensive-inference-detected = true
SORT date DESC
```

### Sessions Where Prediction Was Significantly Off

```dataview
TABLE WITHOUT ID
  file.link AS "Session",
  text-title AS "Text",
  self-efficacy-pre AS "Predicted",
  comprehension-level AS "Actual",
  calibration-delta AS "Delta"
FROM #srl-session
WHERE reflection-completed = true AND (calibration-delta > 3 OR calibration-delta < -3)
SORT date DESC
```

---

## 📝 Manual Log Entries

> Use this section if you need to log sessions that don't have full template notes, or for special observations about your calibration trajectory.

| Date | Text | Criterion | Efficacy Pre | Actual Comprehension | Prediction Accuracy | Attribution | Adaptive Inference |
|------|------|-----------|-------------|---------------------|--------------------|--------------|--------------------|
| | | | | | | | |

---

> [!connections-and-links]
> **PKB Connections:**
> - [[Zimmerman's-Cyclical-SRL-Model]] — This log is a direct implementation of the Calibration Engine synthesis
> - [[Metacognitive-Calibration]] — Calibration is the emergent output tracked by this log
> - [[Metacognitive-Monitoring]] — Monitoring accuracy is what the prediction-outcome comparison measures
> - [[Attribution-Theory]] — Attribution patterns tracked here reveal the quality of the Self-Reflection Phase
> - [[Self-Efficacy]] — Self-efficacy is a dynamic output of the cycle, not a stable input — this log reveals its trajectory
> - [[The-Fluency-Illusion]] — Overconfident predictions are the primary signature of fluency illusion effects
> - [[Deliberate-Practice]] — The log enables the feedback quality that distinguishes deliberate practice from mere repetition
