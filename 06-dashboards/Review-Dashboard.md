---
title: "Review Dashboard"
aliases:
  - "Review Hub"
  - "Permanent Notes Review"
  - "PKB Review Console"
type: dashboard
status: evergreen
cssclasses:
  - review-dashboard
tags:
  - dashboard
  - pkb-meta
  - review-workflow
created: 2026-04-25
updated: 2026-04-25
review-frequency: weekly
importance: high
related:
  - "[[Review Queries Library]]"
  - "[[Review System README]]"
---

# 🧠 Review Dashboard

> [!abstract] What this is
> A live, multi-criteria triage console for your permanent notes. Every section below is generated at view-time from the current state of your vault. Sorted by an overdue-aware priority score, surfaced by tag, status, staleness, centrality, and theme — so you always know **what to review next** without guessing.

> [!helpful-tip] How to use it
> 1. Open this note in **Reading View** (the queries don't render in Source Mode).
> 2. Start with the **🔥 Critical Attention Queue** at the top — it blends every signal into one ranked list.
> 3. Click any note → review it → log the review by adding `last-reviewed: 2026-04-25` to its frontmatter (or run the `Log Review` Templater command if installed).
> 4. Re-open this dashboard. Notes you reviewed drop down the queue. The system gets sharper as you adopt the `last-reviewed` field.

> [!attention] Schema fallback chain
> If a note has no `last-reviewed`, the system uses `updated`, then `file.mtime`. So this works on your existing vault **right now**, before you change anything. See [[Review System README]] for migration guidance.

---

## 📊 Vault Pulse

```dataviewjs
const code = await dv.io.load("scripts/dv-review-helpers.js");
const REVIEW = (new Function("dv", code + "\nreturn REVIEW;"))(dv);

const notes = dv.pages('"PermanentNotes"').where(p => p.type === "permanent-note");
// If your permanent notes live elsewhere, change the folder path above,
// or use:  dv.pages().where(p => p.type === "permanent-note")

const total      = notes.length;
const overdue    = notes.where(p => REVIEW.isOverdue(p)).length;
const flagged    = notes.where(p => (p.file.tags || []).includes("#needs-review")).length;
const hubs       = notes.where(p => REVIEW.isHub(p, 8)).length;
const orphans    = notes.where(p => REVIEW.isOrphan(p)).length;
const evergreen  = notes.where(p => REVIEW.statusBucket(p) === "evergreen").length;
const neverRev   = notes.where(p => !p["last-reviewed"]).length;

dv.table(
    ["Metric", "Count", "% of vault"],
    [
        ["📚 Total permanent notes",  total,                                       "100%"],
        ["⚠️ Overdue for review",     overdue,    `${(overdue   / total * 100).toFixed(0)}%`],
        ["🏷️ Tagged #needs-review",   flagged,    `${(flagged   / total * 100).toFixed(0)}%`],
        ["🌟 Hubs (≥8 connections)",  hubs,       `${(hubs      / total * 100).toFixed(0)}%`],
        ["🔌 Orphans (no links)",     orphans,    `${(orphans   / total * 100).toFixed(0)}%`],
        ["✅ Evergreen status",        evergreen,  `${(evergreen / total * 100).toFixed(0)}%`],
        ["❓ Never reviewed",          neverRev,   `${(neverRev  / total * 100).toFixed(0)}%`]
    ]
);
```

---

## 🔥 Critical Attention Queue

> [!key-claim] Top 15, blended priority
> Composite score combines overdue ratio (×5), centrality (log-scaled), declared importance, mastery stage, and the `#needs-review` tag (×3). Notes with explicit user signals always rise above heuristic-only candidates.

```dataviewjs
const code = await dv.io.load("scripts/dv-review-helpers.js");
const REVIEW = (new Function("dv", code + "\nreturn REVIEW;"))(dv);

const ranked = dv.pages('"PermanentNotes"')
    .where(p => p.type === "permanent-note")
    .map(p => ({
        link:     p.file.link,
        priority: REVIEW.priorityScore(p),
        ratio:    REVIEW.overdueRatio(p),
        days:     REVIEW.daysSinceReview(p),
        density:  REVIEW.relationalDensity(p),
        status:   REVIEW.statusBucket(p),
        importance: p.importance || "—"
    }))
    .sort(r => r.priority, "desc")
    .slice(0, 15);

dv.table(
    ["Note", "Priority", "Overdue", "Last touched", "Density", "Status", "Importance"],
    ranked.map(r => [
        r.link,
        REVIEW.priorityBadge(r.priority) + ` (${r.priority.toFixed(1)})`,
        REVIEW.ratioBadge(r.ratio),
        REVIEW.ageBadge(r.days),
        r.density,
        r.status,
        r.importance
    ])
);
```

---

## 🚨 Overdue: Past Their Review Window

> [!definition] Overdue
> A note's review window equals its `review-frequency` field (`daily`, `weekly`, `monthly`, `quarterly`, `yearly`). Overdue = days-since-review > window. Notes with no frequency default to **quarterly (90 days)**.

```dataviewjs
const code = await dv.io.load("scripts/dv-review-helpers.js");
const REVIEW = (new Function("dv", code + "\nreturn REVIEW;"))(dv);

const overdue = dv.pages('"PermanentNotes"')
    .where(p => p.type === "permanent-note" && REVIEW.isOverdue(p))
    .map(p => ({
        link:      p.file.link,
        days:      REVIEW.daysSinceReview(p),
        window:    REVIEW.reviewWindow(p),
        ratio:     REVIEW.overdueRatio(p),
        frequency: p["review-frequency"] || "quarterly (default)",
        domain:    p.domain || "—"
    }))
    .sort(r => r.ratio, "desc");

if (overdue.length === 0) {
    dv.paragraph("✨ Nothing overdue. Either you're on top of things or your `review-frequency` defaults are too lenient.");
} else {
    dv.paragraph(`**${overdue.length} notes** past their review cadence.`);
    dv.table(
        ["Note", "Days since", "Window", "Overdue ×", "Frequency", "Domain"],
        overdue.slice(0, 30).map(r => [
            r.link,
            REVIEW.ageBadge(r.days),
            `${r.window}d`,
            REVIEW.ratioBadge(r.ratio),
            r.frequency,
            r.domain
        ])
    );
}
```

---

## 🏷️ Explicitly Flagged: `#needs-review`

> [!info] User-tagged review queue
> Notes you've marked for revisit. These bypass all heuristics — explicit user signals are sovereign.

```dataview
TABLE WITHOUT ID
    file.link        AS "Note",
    status           AS "Status",
    domain           AS "Domain",
    dateformat(file.mtime, "yyyy-MM-dd") AS "Last edit",
    default(importance, "—")             AS "Importance"
FROM #needs-review
WHERE type = "permanent-note"
SORT file.mtime ASC
```

---

## 📊 Stale Notes Radar (>180 days untouched)

> [!warning] Possibly outdated
> Notes whose underlying source material may have evolved while the note hasn't kept up. Especially worth checking on **enriched** notes derived from older reports — has the upstream understanding changed?

```dataviewjs
const code = await dv.io.load("scripts/dv-review-helpers.js");
const REVIEW = (new Function("dv", code + "\nreturn REVIEW;"))(dv);

const STALE_THRESHOLD = 180;

const stale = dv.pages('"PermanentNotes"')
    .where(p => p.type === "permanent-note" && REVIEW.daysSinceUpdate(p) > STALE_THRESHOLD)
    .map(p => ({
        link:       p.file.link,
        days:       REVIEW.daysSinceUpdate(p),
        confidence: p.confidence || "—",
        evidence:   p["evidence-quality"] || "—",
        sourceAge:  REVIEW.daysSinceCreation(p)
    }))
    .sort(r => r.days, "desc")
    .slice(0, 25);

if (stale.length === 0) {
    dv.paragraph(`✅ Nothing untouched longer than ${STALE_THRESHOLD} days.`);
} else {
    dv.table(
        ["Note", "Days since edit", "Age", "Confidence", "Evidence quality"],
        stale.map(r => [
            r.link,
            REVIEW.ageBadge(r.days),
            REVIEW.ageBadge(r.sourceAge),
            r.confidence,
            r.evidence
        ])
    );
}
```

---

## 🌟 Centrality Hubs (review these carefully — they propagate)

> [!important] Why hubs deserve careful review
> Errors or gaps in a hub propagate through every note that links to it. A 5-minute correction here saves 30 minutes of downstream confusion later. Hub = total relational density ≥ 8 (outbound relations across all 12 relational fields + Obsidian-resolved inlinks).

```dataviewjs
const code = await dv.io.load("scripts/dv-review-helpers.js");
const REVIEW = (new Function("dv", code + "\nreturn REVIEW;"))(dv);

const hubs = dv.pages('"PermanentNotes"')
    .where(p => p.type === "permanent-note")
    .map(p => {
        const out = REVIEW.outboundRelations(p);
        const inb = (p.file.inlinks?.length) || 0;
        return {
            link:       p.file.link,
            inbound:    inb,
            outbound:   out.total,
            total:      inb + out.total,
            days:       REVIEW.daysSinceReview(p),
            domain:     p.domain || "—",
            confidence: p.confidence || "—"
        };
    })
    .where(r => r.total >= 8)
    .sort(r => r.total, "desc")
    .slice(0, 20);

if (hubs.length === 0) {
    dv.paragraph("No hubs yet — your graph is still developing. Hubs typically emerge once a domain has ~15+ notes.");
} else {
    dv.table(
        ["Hub", "Inbound", "Outbound", "Total", "Last reviewed", "Domain", "Confidence"],
        hubs.map(r => [
            r.link, r.inbound, r.outbound, r.total,
            REVIEW.ageBadge(r.days), r.domain, r.confidence
        ])
    );
}
```

---

## 📦 Status Queues

> [!structure] Bucketed by lifecycle status
> Each row is a clickable count linking to the filtered view. Different statuses warrant different review modes:
> - **Seedling/Budding** → "is this still the best framing?"
> - **Enriched** → "has the underlying source been superseded?"
> - **Evergreen** → "any new connections to add?"
> - **Wilting** → "rescue, archive, or delete?"

```dataviewjs
const code = await dv.io.load("scripts/dv-review-helpers.js");
const REVIEW = (new Function("dv", code + "\nreturn REVIEW;"))(dv);

const notes = dv.pages('"PermanentNotes"').where(p => p.type === "permanent-note");

const buckets = {};
for (const p of notes) {
    const b = REVIEW.statusBucket(p);
    if (!buckets[b]) buckets[b] = [];
    buckets[b].push({
        link:    p.file.link,
        days:    REVIEW.daysSinceReview(p),
        overdue: REVIEW.isOverdue(p)
    });
}

const order = ["seedling", "budding", "enriched", "evergreen", "wilting", "archived"];
const rows = [];

for (const status of order) {
    if (!buckets[status]) continue;
    const arr = buckets[status];
    const overdueCount = arr.filter(x => x.overdue).length;
    const avgDays = Math.round(
        arr.reduce((s, x) => s + (x.days === Infinity ? 365 : x.days), 0) / arr.length
    );
    rows.push([
        status,
        arr.length,
        overdueCount,
        REVIEW.ageBadge(avgDays),
        `${(overdueCount / arr.length * 100).toFixed(0)}%`
    ]);
}

// Catch any unexpected statuses
for (const [status, arr] of Object.entries(buckets)) {
    if (order.includes(status)) continue;
    rows.push([status, arr.length, "—", "—", "—"]);
}

dv.table(
    ["Status", "Count", "Overdue", "Avg age", "% overdue"],
    rows
);
```

### Drill-down: Evergreen needing refresh

```dataviewjs
const code = await dv.io.load("scripts/dv-review-helpers.js");
const REVIEW = (new Function("dv", code + "\nreturn REVIEW;"))(dv);

const evergreen = dv.pages('"PermanentNotes"')
    .where(p => p.type === "permanent-note" && REVIEW.statusBucket(p) === "evergreen")
    .map(p => ({
        link:    p.file.link,
        days:    REVIEW.daysSinceReview(p),
        density: REVIEW.relationalDensity(p)
    }))
    .sort(r => r.days, "desc")
    .slice(0, 10);

if (evergreen.length === 0) {
    dv.paragraph("_No evergreen notes yet — they emerge from sustained refinement of budding/enriched notes._");
} else {
    dv.table(
        ["Evergreen note", "Days since review", "Density"],
        evergreen.map(r => [r.link, REVIEW.ageBadge(r.days), r.density])
    );
}
```

---

## 🎯 Theme Focus — Filter by Domain

> [!example] Adjust the theme variable below
> Change `THEME` to any value present in your `domain` or `parent-concept` frontmatter (e.g., `"cognitive-psychology"`, `"philosophy"`, `"educational-psychology"`). The block returns priority-sorted notes within that theme so you can do focused review sessions.

```dataviewjs
const code = await dv.io.load("scripts/dv-review-helpers.js");
const REVIEW = (new Function("dv", code + "\nreturn REVIEW;"))(dv);

// ─── EDIT THIS LINE TO CHANGE THE THEME ─────────────────────────────────
const THEME = "cognitive-psychology";
// ────────────────────────────────────────────────────────────────────────

const focus = dv.pages('"PermanentNotes"')
    .where(p => 
        p.type === "permanent-note" && (
            p.domain === THEME ||
            (p.subdomains && p.subdomains.includes(THEME)) ||
            p["parent-concept"] === THEME
        )
    )
    .map(p => ({
        link:     p.file.link,
        priority: REVIEW.priorityScore(p),
        days:     REVIEW.daysSinceReview(p),
        status:   REVIEW.statusBucket(p),
        density:  REVIEW.relationalDensity(p)
    }))
    .sort(r => r.priority, "desc");

dv.header(4, `Theme: ${THEME} — ${focus.length} notes`);

if (focus.length === 0) {
    dv.paragraph(`_No notes match domain/subdomain/parent-concept = "${THEME}". Try a different theme._`);
} else {
    dv.table(
        ["Note", "Priority", "Last reviewed", "Status", "Density"],
        focus.slice(0, 20).map(r => [
            r.link,
            REVIEW.priorityBadge(r.priority),
            REVIEW.ageBadge(r.days),
            r.status,
            r.density
        ])
    );
}
```

### All available themes (for the variable above)

```dataviewjs
const counts = {};
const notes = dv.pages('"PermanentNotes"').where(p => p.type === "permanent-note");

for (const p of notes) {
    if (p.domain) counts[p.domain] = (counts[p.domain] || 0) + 1;
    if (p["parent-concept"]) counts[p["parent-concept"]] = (counts[p["parent-concept"]] || 0) + 1;
    if (Array.isArray(p.subdomains)) {
        for (const s of p.subdomains) counts[s] = (counts[s] || 0) + 1;
    }
}

const sorted = Object.entries(counts).sort((a, b) => b[1] - a[1]);
dv.table(
    ["Theme", "Notes"],
    sorted.map(([theme, n]) => [`\`${theme}\``, n])
);
```

---

## 📈 Review Velocity

> [!info] Are you actually reviewing?
> Counts notes whose `last-reviewed` (or `updated` if `last-reviewed` is absent) falls within each window. Helps you spot whether the workflow is being used.

```dataviewjs
const code = await dv.io.load("scripts/dv-review-helpers.js");
const REVIEW = (new Function("dv", code + "\nreturn REVIEW;"))(dv);

const notes = dv.pages('"PermanentNotes"').where(p => p.type === "permanent-note");

const buckets = { d7: 0, d30: 0, d90: 0 };
for (const p of notes) {
    const d = REVIEW.daysSinceReview(p);
    if (d <= 7)  buckets.d7  += 1;
    if (d <= 30) buckets.d30 += 1;
    if (d <= 90) buckets.d90 += 1;
}

dv.table(
    ["Window", "Notes touched", "% of vault"],
    [
        ["Last 7 days",  buckets.d7,  `${(buckets.d7  / notes.length * 100).toFixed(0)}%`],
        ["Last 30 days", buckets.d30, `${(buckets.d30 / notes.length * 100).toFixed(0)}%`],
        ["Last 90 days", buckets.d90, `${(buckets.d90 / notes.length * 100).toFixed(0)}%`]
    ]
);
```

### Recently reviewed (last 30 days)

```dataviewjs
const code = await dv.io.load("scripts/dv-review-helpers.js");
const REVIEW = (new Function("dv", code + "\nreturn REVIEW;"))(dv);

const recent = dv.pages('"PermanentNotes"')
    .where(p => p.type === "permanent-note" && REVIEW.daysSinceReview(p) <= 30)
    .map(p => ({
        link:   p.file.link,
        days:   REVIEW.daysSinceReview(p),
        status: REVIEW.statusBucket(p)
    }))
    .sort(r => r.days, "asc")
    .slice(0, 15);

if (recent.length === 0) {
    dv.paragraph("_No reviews in the last 30 days. Time to start the workflow._");
} else {
    dv.table(
        ["Note", "Reviewed", "Status"],
        recent.map(r => [r.link, REVIEW.ageBadge(r.days), r.status])
    );
}
```

---

## 🔌 Orphans (Graph Health)

> [!caution] Disconnected notes weaken the graph
> Notes with zero inbound and zero outbound relations. Either they need to be linked into the broader knowledge structure, or they don't belong as permanent notes. Aim for **<5%** orphan ratio.

```dataviewjs
const code = await dv.io.load("scripts/dv-review-helpers.js");
const REVIEW = (new Function("dv", code + "\nreturn REVIEW;"))(dv);

const orphans = dv.pages('"PermanentNotes"')
    .where(p => p.type === "permanent-note" && REVIEW.isOrphan(p))
    .map(p => ({
        link:   p.file.link,
        days:   REVIEW.daysSinceCreation(p),
        domain: p.domain || "—",
        status: REVIEW.statusBucket(p)
    }))
    .sort(r => r.days, "desc");

if (orphans.length === 0) {
    dv.paragraph("✨ Zero orphans. Your graph is fully connected.");
} else {
    dv.paragraph(`**${orphans.length} orphaned notes.** Either link them in or reconsider whether they should be permanent notes.`);
    dv.table(
        ["Orphan", "Age", "Domain", "Status"],
        orphans.slice(0, 25).map(r => [
            r.link,
            REVIEW.ageBadge(r.days),
            r.domain,
            r.status
        ])
    );
}
```

---

## 🔗 Related Topics for PKB Expansion

### 🎯 Core Extensions

1. **[[Review Queries Library]]**
   - **Connection**: Standalone DQL/DataviewJS snippets you can paste into any note for ad-hoc review filters without depending on the helper module
   - **Depth Potential**: Query patterns for every relational field, copy-paste-ready
   - **Knowledge Graph Role**: Reference companion to this dashboard
   - **Priority**: High — needed when you want quick filters in context-specific notes (e.g., a domain MOC)

2. **[[Review System README]]**
   - **Connection**: Setup, schema migration, troubleshooting, the `last-reviewed` adoption strategy
   - **Depth Potential**: Full operational documentation
   - **Knowledge Graph Role**: System documentation hub
   - **Priority**: High — read once, then reference as needed

### 🌐 Cross-Domain Connections

3. **[[Spaced Repetition]]**
   - **Connection**: Review-frequency math is a coarse-grained spaced repetition scheme. The same priority-score architecture extends to a true SM-2 / Anki-style scheduler
   - **Depth Potential**: Implement an actual SRS algorithm with success/failure feedback adjusting the next-review interval
   - **Knowledge Graph Role**: Bridge between PKB methodology and learning science
   - **Priority**: Medium

4. **[[Knowledge Graph Health Metrics]]**
   - **Connection**: Orphan ratio, hub identification, connectivity coefficient — extends the graph-health portion of this dashboard into a dedicated audit
   - **Depth Potential**: Full vault audit framework with trend tracking
   - **Knowledge Graph Role**: Bridge to AUDIT mode of the PKB Specialist Agent
   - **Priority**: Medium

### 📚 Foundational Prerequisites

- **[[Dataview Plugin]]** — DQL syntax and the `dv` API are assumed knowledge
- **[[Permanent Note Schema]]** — the frontmatter contract this dashboard reads from

### 🛠️ Practical Applications

- **[[Weekly Review Ritual]]** — sit-down workflow that consumes this dashboard's output
- **[[Note Pruning Sessions]]** — using the orphan list to triage what to delete vs. integrate
