---
title: "Critical Thinking Practice Dashboard"
aliases: [CT Dashboard, Critical Thinking Dashboard, Reasoning Practice Tracker]
tags:
  - critical-thinking
  - dashboard
  - deliberate-practice
  - dataview
  - metacognition
created: 2026-05-13
modified: 2026-05-13
type: dashboard
status: evergreen
related:
  - "[[Critical Thinking Practice MOC]]"
  - "[[Paul-Elder Framework]]"
  - "[[Deliberate Practice]]"
cssclasses:
  - dashboard
  - critical-thinking
---

# 🧠 Critical Thinking Practice Dashboard

> [!abstract] Purpose
> Live aggregation of every [[Deliberate Practice|deliberate-practice]] critical-thinking session in the vault. Tracks **volume**, **framework distribution**, **rigor trend**, **standards weaknesses**, and **bias frequency** — turning practice into measurable [[Self-Regulated Learning]].
>
> **Data source:** `03-notes/critical-thinking-practice/` — populated automatically by the [[_master-critical-thinking-deliberate-practice-v1.0.0|master template]] and companion framework templates.

---

## 📊 1 · Headline Metrics

```dataviewjs
const all = dv.pages('"03-notes/critical-thinking-practice"')
  .where(p => p.type === "critical-thinking-session");
const total       = all.length;
const last7  = all.where(p => p.file.cday >= dv.date("today") - dv.duration("7 days")).length;
const last30 = all.where(p => p.file.cday >= dv.date("today") - dv.duration("30 days")).length;
const complete    = all.where(p => p.status === "complete").length;
const inProgress  = all.where(p => p.status === "in-progress").length;
const needsReview = all.where(p => p.status === "needs-re-review").length;

dv.table(
  ["Metric", "Value"],
  [
    ["**Total sessions**", total],
    ["Sessions — last 7 days", last7],
    ["Sessions — last 30 days", last30],
    ["Status: complete", complete],
    ["Status: in-progress", inProgress],
    ["Status: needs re-review", needsReview]
  ]
);
```

---

## 📈 2 · Average Rigor Score (last 10 sessions)

```dataviewjs
const recent = dv.pages('"03-notes/critical-thinking-practice"')
  .where(p => p.type === "critical-thinking-session")
  .sort(p => p.file.cday, "desc")
  .limit(10);

const stds = ["clarity","accuracy","precision","relevance","depth","breadth","logic","significance","fairness"];
const rows = recent.map(p => {
  const vals = stds.map(s => Number(p["rating-" + s])).filter(v => !isNaN(v) && v > 0);
  const avg  = vals.length ? (vals.reduce((a,b)=>a+b,0) / vals.length).toFixed(2) : "—";
  return [p.file.link, p.framework ?? "—", avg, vals.length];
});
dv.table(["Session", "Framework", "Avg Rigor", "Stds Rated"], rows);
```

---

## 🎯 3 · Intellectual Standards — Where am I Weakest?

```dataviewjs
const sessions = dv.pages('"03-notes/critical-thinking-practice"')
  .where(p => p.type === "critical-thinking-session");
const stds = ["clarity","accuracy","precision","relevance","depth","breadth","logic","significance","fairness"];
const rows = stds.map(s => {
  const vals = sessions.map(p => Number(p["rating-" + s])).filter(v => !isNaN(v) && v > 0).values;
  if (vals.length === 0) return [s, "—", "—", "—"];
  const avg = vals.reduce((a,b)=>a+b,0) / vals.length;
  const min = Math.min(...vals);
  const max = Math.max(...vals);
  return [s, avg.toFixed(2), `${min}–${max}`, vals.length];
});
// sort ascending by average (weakest first)
rows.sort((a,b) => (a[1] === "—" ? 99 : Number(a[1])) - (b[1] === "—" ? 99 : Number(b[1])));
dv.table(["Standard (weakest first)", "Lifetime Avg", "Range", "n"], rows);
```

> [!helpful-tip] Action
> The top row is your **growth edge**. Pick a session next week that deliberately stresses this standard.

---

## 🧩 4 · Framework Distribution

```dataviewjs
const sessions = dv.pages('"03-notes/critical-thinking-practice"')
  .where(p => p.type === "critical-thinking-session");
const groups = {};
for (const s of sessions) {
  const f = s.framework ?? "unspecified";
  groups[f] = (groups[f] ?? 0) + 1;
}
const rows = Object.entries(groups).sort((a,b) => b[1] - a[1]);
dv.table(["Framework", "Sessions"], rows);
```

---

## 🗂 5 · Object-Type Distribution

```dataviewjs
const sessions = dv.pages('"03-notes/critical-thinking-practice"')
  .where(p => p.type === "critical-thinking-session");
const groups = {};
for (const s of sessions) {
  const t = s["object-type"] ?? "unspecified";
  groups[t] = (groups[t] ?? 0) + 1;
}
dv.table(["Object Type", "Sessions"], Object.entries(groups).sort((a,b)=>b[1]-a[1]));
```

---

## 🕒 6 · Recent Sessions (last 20)

```dataview
TABLE WITHOUT ID
  file.link AS "Session",
  framework AS "Framework",
  object-type AS "Object",
  question-type AS "Q-Type",
  stakes AS "Stakes",
  status AS "Status"
FROM "03-notes/critical-thinking-practice"
WHERE type = "critical-thinking-session"
SORT file.cday DESC
LIMIT 20
```

---

## 🔄 7 · Sessions Flagged for Re-Review

```dataview
LIST
FROM "03-notes/critical-thinking-practice"
WHERE type = "critical-thinking-session" AND status = "needs-re-review"
SORT file.mtime DESC
```

---

## 📝 8 · Metacognitive Reflections (rollup)

```dataview
TABLE WITHOUT ID
  file.link AS "Reflection",
  period AS "Period",
  weakest-standard AS "Weak Standard",
  strongest-virtue-exercised AS "Strong Virtue"
FROM "03-notes/critical-thinking-practice/_reflections"
WHERE type = "metacognitive-reflection"
SORT file.cday DESC
```

---

## 📐 9 · Calibration — Confidence Shift Analysis

> Does structured analysis actually move my confidence? If `confidence-pre ≈ confidence-post` consistently, the framework may be functioning as **post-hoc rationalization** rather than reasoning.

```dataviewjs
const sessions = dv.pages('"03-notes/critical-thinking-practice"')
  .where(p => p.type === "critical-thinking-session")
  .where(p => p["confidence-pre"] != null && p["confidence-post"] != null);

const rows = sessions.map(p => {
  const pre  = Number(p["confidence-pre"]);
  const post = Number(p["confidence-post"]);
  const delta = post - pre;
  const marker = delta === 0 ? "—" : (delta > 0 ? `▲ ${delta}` : `▼ ${delta}`);
  return [p.file.link, pre, post, marker];
});

if (rows.length === 0) {
  dv.paragraph("*No calibration data yet — fill `confidence-pre` and `confidence-post` in sessions.*");
} else {
  dv.table(["Session", "Pre", "Post", "Δ"], rows);
  const deltas = sessions.map(p => Number(p["confidence-post"]) - Number(p["confidence-pre"])).values;
  const movedCount = deltas.filter(d => d !== 0).length;
  const pct = ((movedCount / deltas.length) * 100).toFixed(0);
  dv.paragraph(`**Sessions where analysis moved my confidence:** ${movedCount} / ${deltas.length} (**${pct}%**)`);
}
```

---

## 🏷 10 · Bias Self-Reports (DataviewJS scan)

```dataviewjs
const biases = [
  "Confirmation Bias","Anchoring Bias","Availability Heuristic","Motivated Reasoning",
  "Sunk Cost Fallacy","Dunning-Kruger Effect","Bandwagon Effect","Halo Effect",
  "Fundamental Attribution Error","Hindsight Bias"
];
const sessions = dv.pages('"03-notes/critical-thinking-practice"')
  .where(p => p.type === "critical-thinking-session");
const counts = Object.fromEntries(biases.map(b => [b, 0]));
for (const s of sessions) {
  const content = await dv.io.load(s.file.path);
  for (const b of biases) {
    // count checked checkboxes referring to each bias
    const re = new RegExp(`- \\[x\\][^\\n]*${b}`, "i");
    if (re.test(content)) counts[b]++;
  }
}
const rows = Object.entries(counts).sort((a,b) => b[1] - a[1]);
dv.table(["Bias (most-reported first)", "Times Reported"], rows);
```

---

# 🔗 Related

- [[Critical Thinking Practice MOC]]
- [[Paul-Elder Framework]] · [[FRISCO Model]] · [[Toulmin Argument Model]] · [[SEE-I Method]]
- [[Metacognition]] · [[Deliberate Practice]] · [[Self-Regulated Learning]]
- [[Cognitive Biases]] · [[Intellectual Standards]] · [[Intellectual Virtues]]
