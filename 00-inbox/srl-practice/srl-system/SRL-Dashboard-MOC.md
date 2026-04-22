---
# ═══════════════════════════════════════════════════════════════════════════
# SRL SYSTEM DASHBOARD — MAP OF CONTENT
# Central navigation hub for the SRL Reading System
# ═══════════════════════════════════════════════════════════════════════════
type: moc
status: evergreen
created: "{{date}}"
updated: "{{date}}"
tags:
  - moc
  - srl-system
  - dashboard
  - navigation
  - dataview
  - meta-bind
aliases:
  - "SRL Dashboard"
  - "SRL System Hub"
  - "Self-Regulated Learning Dashboard"
---

# 🧠 SRL Reading System Dashboard

> [!abstract] System Overview
> This is the central hub for your **Self-Regulated Learning Reading System** — an Obsidian-native implementation of [[Zimmerman's-Cyclical-SRL-Model|Zimmerman's Cyclical SRL Model]] designed for reading complex academic texts within your PKB. The system integrates [[forethought-phase|Forethought]], [[self-reflection-phase|Self-Reflection]], [[metacognitive-calibration|calibration tracking]], and [[achievement-goal-theory|mastery-oriented]] motivational design.

---

## ⚡ Quick Actions

> [!tip] Use these to launch system components quickly.

`BUTTON[new-srl-session]` `BUTTON[open-learning-agenda]` `BUTTON[open-calibration-log]` `BUTTON[open-reference-cards]` `BUTTON[new-monthly-review]` `BUTTON[new-framework-activation]`

```meta-bind-button
label: "📖 New Reading Session"
id: new-srl-session
style: primary
actions:
  - type: templaterCreateNote
    templateFile: "99-system/01-quickadd/02-templates/SRL-Reading-Session-Template.md"
    folderPath: "999-report-orginizing/srl-practice/srl-sessions"
    fileName: ""
```

```meta-bind-button
label: "📋 Learning Agenda"
id: open-learning-agenda
style: default
actions:
  - type: open
    link: "[[SRL-Living-Learning-Agenda]]"
```

```meta-bind-button
label: "📊 Calibration Log"
id: open-calibration-log
style: default
actions:
  - type: open
    link: "[[SRL-Calibration-Log]]"
```

```meta-bind-button
label: "🃏 Reference Cards"
id: open-reference-cards
style: default
actions:
  - type: open
    link: "[[SRL-Quick-Reference-Cards]]"
```

```meta-bind-button
label: "📈 Monthly Review"
id: new-monthly-review
style: default
actions:
  - type: templaterCreateNote
    templateFile: "99-system/01-quickadd/02-templates/SRL-Monthly-Review-Template.md"
    folderPath: "999-report-orginizing/srl-practice/srl-reviews"
    fileName: ""
```

```meta-bind-button
label: "🧬 Framework Activation"
id: new-framework-activation
style: default
actions:
  - type: templaterCreateNote
    templateFile: "99-system/01-quickadd/02-templates/SRL-Framework-Activation-Template.md"
    folderPath: "999-report-orginizing/srl-practice/srl-sessions"
    fileName: ""
```

---

## 📊 System Metrics

### Session Overview

```dataviewjs
const sessions = dv.pages('#srl-session');
const completed = sessions.where(s => s["reflection-completed"] === true);
const thisMonth = completed.where(s => {
    const d = s.date;
    const now = new Date();
    return d && new Date(d).getMonth() === now.getMonth() 
        && new Date(d).getFullYear() === now.getFullYear();
});

dv.table(["Metric", "All Time", "This Month"], [
    ["Total Sessions", sessions.length, thisMonth.length],
    ["Completed (with Reflection)", completed.length, thisMonth.length],
    ["Forethought Only", sessions.where(s => s["forethought-completed"] && !s["reflection-completed"]).length, "—"],
]);
```

### Recent Sessions

```dataview
TABLE WITHOUT ID
  file.link AS "Session",
  text-title AS "Text",
  schema-level AS "Schema",
  comprehension-level AS "Comprehension",
  self-efficacy-pre AS "Efficacy",
  date AS "Date"
FROM #srl-session
SORT date DESC
LIMIT 5
```

### Attribution Health

```dataviewjs
const sessions = dv.pages('#srl-session')
    .where(s => s["reflection-completed"] === true);

if (sessions.length === 0) {
    dv.paragraph("*No completed sessions yet.*");
} else {
    const controllable = sessions
        .where(s => s["attribution-controllable"] === true).length;
    const defensive = sessions
        .where(s => s["defensive-inference-detected"] === true).length;
    const total = sessions.length;
    
    const healthScore = ((controllable / total) * 100).toFixed(0);
    const status = healthScore >= 80 ? "🟢 Healthy" : 
                   healthScore >= 60 ? "🟡 Monitor" : "🔴 Needs Attention";
    
    dv.table(["Metric", "Value", "Status"], [
        ["Controllable Attribution Rate", `${healthScore}%`, status],
        ["Defensive Inferences", `${defensive}/${total}`, defensive === 0 ? "🟢" : "🟡"],
    ]);
}
```

---

## 🗺️ System Components

### Core Workflow Documents

| Component | Purpose | Frequency |
|-----------|---------|-----------|
| [[SRL-Reading-Session-Template]] | Master session template (Forethought + Self-Reflection) | Every reading session |
| [[SRL-Living-Learning-Agenda]] | Forward-planning handoff node | Update after every session, consult before every session |
| [[SRL-Calibration-Log]] | Long-term calibration tracking | Update after every session, review monthly |
| [[SRL-Quick-Reference-Cards]] | Goal language, attribution retraining, mastery grammar | Reference during sessions as needed |
| [[SRL-Monthly-Review-Template]] | Periodic meta-reflection | Monthly |
| [[SRL-Framework-Activation-Template]] | Specialized Forethought for new frameworks | When reading introduces a new framework |

### Session Workflow

```
┌──────────────────────────────────────────────────────┐
│  1. Consult [[SRL-Living-Learning-Agenda]]           │
│     ↓                                                │
│  2. Create new session from [[SRL-Reading-Session-   │
│     Template]] (or [[SRL-Framework-Activation-       │
│     Template]] for new frameworks)                   │
│     ↓                                                │
│  3. Complete FORETHOUGHT zones (5-10 min)            │
│     ↓                                                │
│  4. READ with process goals active                   │
│     ↓                                                │
│  5. Complete SELF-REFLECTION zones (10-15 min)       │
│     ↓                                                │
│  6. Update [[SRL-Living-Learning-Agenda]]            │
│  7. Update [[SRL-Calibration-Log]]                   │
│  8. Create PKB notes as flagged                      │
└──────────────────────────────────────────────────────┘
          ↑                                    │
          └────────── FEEDBACK LOOP ───────────┘
```

---

## 📚 Theoretical Foundation

### Core Frameworks

| Framework | Role in System | Key Note |
|-----------|---------------|----------|
| [[Zimmerman's-Cyclical-SRL-Model]] | Primary structural architecture | The three-phase cycle |
| [[achievement-goal-theory]] | Goal language and motivational framing | Mastery vs. performance orientation |
| [[self-determination-theory]] | Autonomy-supportive design | Protecting intrinsic motivation |
| [[Attribution (Heider, 1958)]] | Causal attribution in Self-Reflection | Adaptive vs. defensive inferences |
| [[self-efficacy]] | Motivational substrate | Calibrated confidence, not elevation |
| [[metacognitive-calibration]] | Long-term developmental output | The Calibration Engine |
| [[formative-assessment]] | Self-evaluation design | Descriptive, not evaluative |
| [[deliberate-practice]] | Practice architecture | Feedback-driven skill development |

### Key Concepts

- [[forethought-phase]] — Task Analysis + Motivational Beliefs
- [[self-reflection-phase]] — Self-Judgment + Self-Reaction
- [[performance-phase]] — Monitoring + Strategy deployment
- [[adaptive-inference]] — The cycle's primary output
- [[defensive-inference]] — The cycle's primary failure mode
- [[the-fluency-illusion]] — Why Cold Reconstruction matters
- [[mastery-oriented-response-pattern]] — The target response to difficulty
- [[metacognitive-monitoring]] — Monitoring accuracy as quality control
- [[attribution-retraining]] — Shifting maladaptive attributions
- [[growth-mindset]] — Incremental theory supporting adaptive attributions
- [[autonomy-support]] — Language design for motivation protection
- [[prior-knowledge-activation]] — Schema activation before reading
- [[Elaborative Interrogation]] — Deep processing strategy
- [[Desirable Difficulties (Robert Bjork, 1994)]] — The mechanism behind Cold Reconstruction
- [[testing-effect-retrieval-practice-effect]] — Why production > recognition

---

## 🔧 System Maintenance

### Overdue Reviews

```dataview
LIST
FROM #srl-session
WHERE reflection-completed = false AND forethought-completed = true
SORT date DESC
```

### Monthly Review Schedule

```dataview
TABLE WITHOUT ID
  file.link AS "Review",
  review-period AS "Period",
  date AS "Date"
FROM #monthly-review
SORT date DESC
LIMIT 6
```

### System Health Checklist

- [ ] All recent sessions have completed Self-Reflection phases
- [ ] [[SRL-Living-Learning-Agenda]] updated within the last week
- [ ] [[SRL-Calibration-Log]] reviewed within the last month
- [ ] No persistent defensive inference patterns (check Attribution Health above)
- [ ] Process goals evolving in sophistication (check [[SRL-Living-Learning-Agenda]] Progressive Goal Log)
- [ ] Monthly review completed for current month

---

## 📖 Implementation Guide

### For New Users

1. **Read** [[SRL-Quick-Reference-Cards]] Card 5 (Early Implementation Survival Guide)
2. **Start small** — Use only Zones 1 and 3 of Forethought, and Zone 1 of Self-Reflection
3. **Use process-satisfaction standards** — Success = protocol execution, not comprehension
4. **Expect the implementation dip** — First 5-10 sessions will feel harder, not easier
5. **Add zones progressively** over 4-6 weeks as each becomes fluent

### Scaffold Fading Schedule

| Weeks | Forethought Zones | Self-Reflection Zones |
|-------|-------------------|----------------------|
| 1-2 | Zone 1 (Prior Knowledge) + Zone 3 (Goals) | Zone 1 (Cold Reconstruction) |
| 3-4 | Add Zone 2 (Task Characterization) + Zone 4 (Self-Efficacy) | Add Zone 2 (Process Audit) |
| 5-6 | Add Zone 5 (Motivational Priming) | Add Zone 3 (Attribution) |
| 7-8 | Full Forethought Protocol | Add Zone 4 (Adaptive Inference) + Zone 5 (PKB Integration) |
| 9+ | Full system with Zone 6 (Handoff) | Full system including Handoff |

### Folder Structure

```
Your Vault/
├── 99-system/01-quickadd/02-templates/
│   ├── SRL-Reading-Session-Template.md
│   ├── SRL-Monthly-Review-Template.md
│   └── SRL-Framework-Activation-Template.md
├── 999-report-orginizing/srl-practice/srl-system/
│   ├── SRL-Dashboard-MOC.md          ← You are here
│   ├── SRL-Living-Learning-Agenda.md
│   ├── SRL-Calibration-Log.md
│   └── SRL-Quick-Reference-Cards.md
├── 999-report-orginizing/srl-practice/srl-sessions/
│   ├── 2026-03-25-1054-srl-session.md
│   └── ...
└── 999-report-orginizing/srl-practice/srl-reviews/
    ├── SRL-Monthly-Review-March-2026.md
    └── ...
```

---

> [!connections-and-links]
> **This MOC connects to:**
> - [[Zimmerman's-Cyclical-SRL-Model]] — The theoretical architecture this system implements
> - [[practical-philosophy-moc]] — Broader philosophical practice context
> - [[metacognition]] — The cognitive science foundation
> - [[self-regulated-learning]] — The research domain
> - [[PKB]] — The knowledge management system this integrates with
> - [[obsidian]] — The platform this system runs on
