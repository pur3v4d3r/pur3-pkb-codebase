---
title: "Review Queries Library"
aliases:
  - "DQL Snippets"
  - "Review Query Cookbook"
  - "Dataview Cookbook"
type: reference
status: evergreen
tags:
  - reference
  - dataview-query
  - dataviewjs
  - pkb-meta
  - review-workflow
created: 2026-04-25
updated: 2026-04-25
related:
  - "[[Review-Dashboard]]"
---

# 📚 Review Queries Library

> [!abstract] Why this exists
> The [[Review-Dashboard]] is the day-to-day console. **This** is the cookbook — every snippet here is **standalone**, depends on no helper module, and can be copy-pasted into any note (a domain MOC, a project page, an inbox file). When you want a focused review filter inside a specific context, grab the right block from below.

> [!helpful-tip] How to choose between DQL and DataviewJS
> - **DQL** (` ```dataview `) — short, declarative, fast to write. Use for simple filters and tables. **Limitation**: hyphenated frontmatter keys (`last-reviewed`, `review-frequency`, `evidence-quality`, `parent-concept`) cannot be referenced directly in DQL `WHERE` clauses (the hyphen is parsed as subtraction). Use DataviewJS for those.
> - **DataviewJS** (` ```dataviewjs `) — full JavaScript. Use whenever you need computed fields, hyphenated keys, custom math, multi-field aggregation, or conditional badges.

> [!important] Folder path
> Every snippet below points at `"999-report-organizing/_permanent-notes/v6-llm-elaborated"`. Adjust the `FROM "..."` (DQL) or `FOLDER` constant (DataviewJS) at the top of each block to target a different folder. See **Section 3** for alternative source patterns.

---

## Section 1 — Pure DQL Queries

### 1.1 — Notes Not Edited in Last 30 Days

DQL has no clean way to read `last-reviewed` (hyphenated key). This query uses `file.mtime` as the practical proxy. For true `last-reviewed` logic, see snippet 2.1.

```dataview
TABLE WITHOUT ID
    file.link                            AS "Note",
    dateformat(file.mtime, "yyyy-MM-dd") AS "Last edit",
    default(status, "—")                 AS "Status",
    default(domain, "—")                 AS "Domain"
FROM "999-report-organizing/_permanent-notes/v6-llm-elaborated"
WHERE type = "permanent-note"
  AND file.mtime < date(today) - dur(30 days)
SORT file.mtime ASC
```

### 1.2 — Tagged `#needs-review`

```dataview
TABLE WITHOUT ID
    file.link                            AS "Note",
    default(status, "—")                 AS "Status",
    default(importance, "—")             AS "Importance",
    dateformat(file.mtime, "yyyy-MM-dd") AS "Last edit"
FROM "999-report-organizing/_permanent-notes/v6-llm-elaborated" AND #needs-review
WHERE type = "permanent-note"
SORT file.mtime ASC
```

### 1.3 — High-Centrality Notes (≥ N inlinks)

Pure DQL only sees Obsidian's resolved inlinks (it can't aggregate the 12 frontmatter relational fields in a single expression — see DataviewJS section 2.3 for true density).

```dataview
TABLE WITHOUT ID
    file.link              AS "Note",
    length(file.inlinks)   AS "Inlinks",
    length(file.outlinks)  AS "Outlinks",
    default(status, "—")   AS "Status"
FROM "999-report-organizing/_permanent-notes/v6-llm-elaborated"
WHERE type = "permanent-note"
  AND length(file.inlinks) >= 5
SORT length(file.inlinks) DESC
```

### 1.4 — By Status (Evergreen, Enriched, Budding, etc.)

```dataview
TABLE WITHOUT ID
    file.link                            AS "Note",
    default(domain, "—")                 AS "Domain",
    default(confidence, "—")             AS "Confidence",
    dateformat(file.mtime, "yyyy-MM-dd") AS "Last edit"
FROM "999-report-organizing/_permanent-notes/v6-llm-elaborated"
WHERE type = "permanent-note" AND status = "enriched"
SORT file.mtime ASC
```

Replace `"enriched"` with `"evergreen"`, `"budding"`, `"seedling"`, `"wilting"`, `"archived"` as needed.

### 1.5 — Stale Content (Not Updated in 6+ Months)

```dataview
TABLE WITHOUT ID
    file.link                            AS "Note",
    dateformat(file.mtime, "yyyy-MM-dd") AS "Last edit",
    default(confidence, "—")             AS "Confidence",
    default(status, "—")                 AS "Status"
FROM "999-report-organizing/_permanent-notes/v6-llm-elaborated"
WHERE type = "permanent-note"
  AND file.mtime < date(today) - dur(180 days)
SORT file.mtime ASC
```

### 1.6 — Notes in a Specific Domain

```dataview
TABLE WITHOUT ID
    file.link                            AS "Note",
    default(status, "—")                 AS "Status",
    default(confidence, "—")             AS "Confidence",
    dateformat(file.mtime, "yyyy-MM-dd") AS "Last edit"
FROM "999-report-organizing/_permanent-notes/v6-llm-elaborated"
WHERE type = "permanent-note" AND domain = "cognitive-psychology"
SORT file.mtime ASC
```

### 1.7 — Notes Linked to a Specific Concept

The `FROM [[note]]` clause selects every note that has any link **to** that target. Replace `[[working-memory]]` with the target concept.

```dataview
TABLE WITHOUT ID
    file.link            AS "Note",
    default(status, "—") AS "Status",
    default(domain, "—") AS "Domain"
FROM [[working-memory]]
WHERE type = "permanent-note"
SORT file.mtime DESC
```

### 1.8 — Notes That Specialize / Contrast With Another

```dataview
TABLE WITHOUT ID
    file.link                                          AS "Note",
    contains(specializes,    [[cognitive-load-theory]]) AS "Specializes target?",
    contains(contrasts-with, [[behaviorism]])           AS "Contrasts target?"
FROM "999-report-organizing/_permanent-notes/v6-llm-elaborated"
WHERE type = "permanent-note"
  AND (contains(specializes,    [[cognitive-load-theory]])
    OR contains(contrasts-with, [[behaviorism]]))
SORT file.name ASC
```

### 1.9 — Combined: Stale AND High-Confidence

The most concerning quadrant — trusted but unverified.

```dataview
TABLE WITHOUT ID
    file.link                            AS "Note",
    confidence                           AS "Confidence",
    dateformat(file.mtime, "yyyy-MM-dd") AS "Last edit"
FROM "999-report-organizing/_permanent-notes/v6-llm-elaborated"
WHERE type = "permanent-note"
  AND confidence = "high"
  AND file.mtime < date(today) - dur(180 days)
SORT file.mtime ASC
```

### 1.10 — Group by Status (Counts)

```dataview
TABLE WITHOUT ID
    rows.file.link AS "Notes"
FROM "999-report-organizing/_permanent-notes/v6-llm-elaborated"
WHERE type = "permanent-note"
GROUP BY default(status, "(unspecified)") AS "Status"
SORT length(rows) DESC
```

### 1.11 — Notes by Source Report

Useful for tracing which notes came from which extraction batch.

```dataview
TABLE WITHOUT ID
    rows.file.link AS "Notes"
FROM "999-report-organizing/_permanent-notes/v6-llm-elaborated"
WHERE type = "permanent-note" AND source-reports
FLATTEN source-reports AS report
GROUP BY report AS "Source Report"
SORT length(rows) DESC
LIMIT 20
```

### 1.12 — Notes With No Outbound Relations

A first-pass orphan check using DQL only.

```dataview
TABLE WITHOUT ID
    file.link            AS "Note",
    default(status, "—") AS "Status",
    default(domain, "—") AS "Domain"
FROM "999-report-organizing/_permanent-notes/v6-llm-elaborated"
WHERE type = "permanent-note"
  AND length(file.outlinks) = 0
  AND length(file.inlinks)  = 0
SORT file.ctime ASC
```

---

## Section 2 — DataviewJS Snippets (Standalone)

These blocks are **fully self-contained** — no helper module required. Each one is around 30-60 lines and can be pasted into any note.

### 2.1 — Days Since Review (with `last-reviewed` → `updated` → `mtime` fallback)

```dataviewjs
const FOLDER = '"999-report-organizing/_permanent-notes/v6-llm-elaborated"';

const toDate = (v) => {
    if (v == null) return null;
    if (typeof v === "object" && typeof v.isValid === "boolean") return v.isValid ? v : null;
    try { const d = dv.date(v); return (d && d.isValid) ? d : null; } catch (e) { return null; }
};

const lastTouched = (p) =>
    toDate(p["last-reviewed"]) || toDate(p.updated) || toDate(p.file.mtime);

const daysSinceReview = (p) => {
    const d = lastTouched(p);
    if (!d) return Infinity;
    return Math.floor(dv.date("now").diff(d, "days").days);
};

const ageBadge = (d) => {
    if (d === Infinity) return "—";
    if (d < 7)   return `🟢 ${d}d`;
    if (d < 30)  return `🟡 ${d}d`;
    if (d < 90)  return `🟠 ${d}d`;
    if (d < 180) return `🔴 ${d}d`;
    return `🟣 ${d}d`;
};

const rows = dv.pages(FOLDER)
    .where(p => p.type === "permanent-note")
    .map(p => ({ link: p.file.link, days: daysSinceReview(p) }))
    .sort(r => r.days, "desc")
    .slice(0, 20);

dv.table(
    ["Note", "Age", "Days"],
    rows.map(r => [r.link, ageBadge(r.days), r.days === Infinity ? "—" : r.days])
);
```

### 2.2 — Overdue Based on `review-frequency`

```dataviewjs
const FOLDER = '"999-report-organizing/_permanent-notes/v6-llm-elaborated"';

const FREQ_DAYS = {
    daily: 1, weekly: 7, biweekly: 14, monthly: 30,
    quarterly: 90, biannual: 180, yearly: 365, annual: 365
};

const toDate = (v) => {
    if (v == null) return null;
    if (typeof v === "object" && typeof v.isValid === "boolean") return v.isValid ? v : null;
    try { const d = dv.date(v); return (d && d.isValid) ? d : null; } catch (e) { return null; }
};

const lastTouched = (p) =>
    toDate(p["last-reviewed"]) || toDate(p.updated) || toDate(p.file.mtime);

const daysSince = (d) => {
    if (!d) return Infinity;
    return Math.floor(dv.date("now").diff(d, "days").days);
};

const overdue = dv.pages(FOLDER)
    .where(p => p.type === "permanent-note")
    .map(p => {
        const window = FREQ_DAYS[(p["review-frequency"] || "quarterly").toLowerCase()] ?? 90;
        const days   = daysSince(lastTouched(p));
        return { link: p.file.link, days, window, ratio: days / window };
    })
    .where(r => r.ratio > 1)
    .sort(r => r.ratio, "desc");

dv.table(
    ["Note", "Days since", "Window (d)", "Overdue ×"],
    overdue.slice(0, 30).map(r => [
        r.link,
        r.days === Infinity ? "🆕 never" : r.days,
        r.window,
        r.ratio === Infinity ? "🆕 never" : `${r.ratio.toFixed(1)}×`
    ])
);
```

### 2.3 — True Relational Density (all 12 fields + inlinks)

```dataviewjs
const FOLDER = '"999-report-organizing/_permanent-notes/v6-llm-elaborated"';

const RELATIONAL_FIELDS = [
    "related", "prerequisites", "specializes", "broader", "see-also",
    "contrasts-with", "contradicts", "applies-to", "formalizes",
    "instance-of", "supports", "refines"
];

const isLiveLink = (v) =>
    v && typeof v === "object" && v.path && String(v.path).trim().length > 0;

const outboundCount = (p) => {
    let n = 0;
    for (const f of RELATIONAL_FIELDS) {
        const v = p[f];
        if (!v) continue;
        const arr = Array.isArray(v) ? v : [v];
        n += arr.filter(isLiveLink).length;
    }
    return n;
};

const ranked = dv.pages(FOLDER)
    .where(p => p.type === "permanent-note")
    .map(p => {
        const inb = (p.file.inlinks?.length) || 0;
        const out = outboundCount(p);
        return { link: p.file.link, inb, out, total: inb + out };
    })
    .sort(r => r.total, "desc")
    .slice(0, 20);

dv.table(
    ["Note", "Inlinks", "Outbound (frontmatter)", "Total density"],
    ranked.map(r => [r.link, r.inb, r.out, r.total])
);
```

### 2.4 — Notes Linked to a Set of Key Concepts

```dataviewjs
const FOLDER = '"999-report-organizing/_permanent-notes/v6-llm-elaborated"';

// ─── Edit this list ─────────────────────────────────────────────────────
const KEY_CONCEPTS = ["working-memory", "schema-theory", "self-directed-learning"];
// ────────────────────────────────────────────────────────────────────────

const RELATIONAL_FIELDS = [
    "related", "prerequisites", "specializes", "broader", "see-also",
    "contrasts-with", "contradicts", "applies-to", "formalizes",
    "instance-of", "supports", "refines"
];

const matches = (p) => {
    for (const f of RELATIONAL_FIELDS) {
        const v = p[f];
        if (!v) continue;
        const arr = Array.isArray(v) ? v : [v];
        for (const link of arr) {
            if (link && link.path) {
                const name = link.path.split("/").pop().replace(/\.md$/, "");
                if (KEY_CONCEPTS.includes(name)) return true;
            }
        }
    }
    return false;
};

const focused = dv.pages(FOLDER)
    .where(p => p.type === "permanent-note" && matches(p))
    .sort(p => p.file.name);

dv.paragraph(`**${focused.length}** notes linked to: ${KEY_CONCEPTS.map(c => `\`${c}\``).join(", ")}`);
dv.table(
    ["Note", "Status", "Domain"],
    focused.map(p => [p.file.link, p.status || "—", p.domain || "—"])
);
```

### 2.5 — Confidence × Staleness Matrix

```dataviewjs
const FOLDER = '"999-report-organizing/_permanent-notes/v6-llm-elaborated"';

const daysSince = (p) => {
    try { return Math.floor(dv.date("now").diff(p.file.mtime, "days").days); }
    catch (e) { return Infinity; }
};

const matrix = {
    high:   { fresh: 0, aging: 0, stale: 0 },
    medium: { fresh: 0, aging: 0, stale: 0 },
    low:    { fresh: 0, aging: 0, stale: 0 }
};

for (const p of dv.pages(FOLDER).where(p => p.type === "permanent-note")) {
    const conf = (p.confidence || "medium").toString().toLowerCase();
    const d    = daysSince(p);
    const age  = d < 30 ? "fresh" : d < 180 ? "aging" : "stale";
    if (matrix[conf]) matrix[conf][age] += 1;
}

dv.table(
    ["Confidence ↓ / Age →", "Fresh (<30d)", "Aging (30-180d)", "Stale (>180d)"],
    [
        ["high",   matrix.high.fresh,   matrix.high.aging,   `⚠️ ${matrix.high.stale}`],
        ["medium", matrix.medium.fresh, matrix.medium.aging, matrix.medium.stale],
        ["low",    matrix.low.fresh,    matrix.low.aging,    matrix.low.stale]
    ]
);
```

### 2.6 — Group by Domain with Counts

```dataviewjs
const FOLDER = '"999-report-organizing/_permanent-notes/v6-llm-elaborated"';

const grouped = {};
for (const p of dv.pages(FOLDER).where(p => p.type === "permanent-note")) {
    const d = p.domain || "(unspecified)";
    if (!grouped[d]) grouped[d] = [];
    grouped[d].push(p);
}

const sorted = Object.entries(grouped).sort((a, b) => b[1].length - a[1].length);

for (const [domain, pages] of sorted) {
    dv.header(4, `${domain} (${pages.length})`);
    dv.list(pages.sort(p => p.file.name).map(p => p.file.link));
}
```

### 2.7 — Quick "Review This One" Logger Helper

Add this at the top of any focused review session note. It surfaces the single highest-priority note matching a filter:

```dataviewjs
const FOLDER = '"999-report-organizing/_permanent-notes/v6-llm-elaborated"';

const FREQ_DAYS = { daily: 1, weekly: 7, monthly: 30, quarterly: 90, yearly: 365 };

const toDate = (v) => {
    if (v == null) return null;
    if (typeof v === "object" && typeof v.isValid === "boolean") return v.isValid ? v : null;
    try { const d = dv.date(v); return (d && d.isValid) ? d : null; } catch (e) { return null; }
};

const lastTouched = (p) =>
    toDate(p["last-reviewed"]) || toDate(p.updated) || toDate(p.file.mtime);

const daysSince = (d) => {
    if (!d) return Infinity;
    return Math.floor(dv.date("now").diff(d, "days").days);
};

const candidate = dv.pages(FOLDER)
    .where(p => p.type === "permanent-note")
    .map(p => {
        const window = FREQ_DAYS[(p["review-frequency"] || "quarterly").toLowerCase()] ?? 90;
        return { p, ratio: daysSince(lastTouched(p)) / window };
    })
    .sort(r => r.ratio, "desc")
    .first();

if (candidate) {
    dv.header(3, "🎯 Next note to review");
    dv.paragraph(`**${candidate.p.file.link}** — ${candidate.ratio === Infinity ? "🆕 never reviewed" : candidate.ratio.toFixed(1) + "× overdue"}`);
    dv.paragraph(`*Domain: ${candidate.p.domain || "—"} • Status: ${candidate.p.status || "—"}*`);
} else {
    dv.paragraph("_No candidates._");
}
```

### 2.8 — Notes by Subdomain (Flatten Tags-Like Field)

```dataviewjs
const FOLDER = '"999-report-organizing/_permanent-notes/v6-llm-elaborated"';

const grouped = {};
for (const p of dv.pages(FOLDER).where(p => p.type === "permanent-note")) {
    const subs = Array.isArray(p.subdomains) ? p.subdomains : (p.subdomains ? [p.subdomains] : []);
    for (const s of subs) {
        if (!grouped[s]) grouped[s] = [];
        grouped[s].push(p);
    }
}

const sorted = Object.entries(grouped).sort((a, b) => b[1].length - a[1].length);
dv.table(
    ["Subdomain", "Note count", "Sample"],
    sorted.map(([sub, pages]) => [
        sub,
        pages.length,
        pages.slice(0, 3).map(p => p.file.link).join(", ") + (pages.length > 3 ? "…" : "")
    ])
);
```

### 2.9 — Outbound-Field Coverage Audit

How well-populated is each relational field across the vault? Empty columns = unused relation types.

```dataviewjs
const FOLDER = '"999-report-organizing/_permanent-notes/v6-llm-elaborated"';

const RELATIONAL_FIELDS = [
    "related", "prerequisites", "specializes", "broader", "see-also",
    "contrasts-with", "contradicts", "applies-to", "formalizes",
    "instance-of", "supports", "refines"
];

const isLiveLink = (v) => v && typeof v === "object" && v.path;

const counts = {};
for (const f of RELATIONAL_FIELDS) counts[f] = { withField: 0, totalLinks: 0 };

const notes = dv.pages(FOLDER).where(p => p.type === "permanent-note");

for (const p of notes) {
    for (const f of RELATIONAL_FIELDS) {
        const v = p[f];
        if (!v) continue;
        const arr = Array.isArray(v) ? v : [v];
        const live = arr.filter(isLiveLink).length;
        if (live > 0) {
            counts[f].withField += 1;
            counts[f].totalLinks += live;
        }
    }
}

const total = notes.length || 1;
dv.table(
    ["Field", "Notes using it", "% of vault", "Total links", "Avg per user"],
    RELATIONAL_FIELDS.map(f => [
        f,
        counts[f].withField,
        `${(counts[f].withField / total * 100).toFixed(0)}%`,
        counts[f].totalLinks,
        counts[f].withField ? (counts[f].totalLinks / counts[f].withField).toFixed(1) : "—"
    ])
);
```

### 2.10 — Find Broken / Unresolved Wiki-Links in Frontmatter

Surfaces links pointing at notes that don't exist in the vault. Common after renames.

```dataviewjs
const FOLDER = '"999-report-organizing/_permanent-notes/v6-llm-elaborated"';

const RELATIONAL_FIELDS = [
    "related", "prerequisites", "specializes", "broader", "see-also",
    "contrasts-with", "contradicts", "applies-to", "formalizes",
    "instance-of", "supports", "refines"
];

const broken = [];
for (const p of dv.pages(FOLDER).where(p => p.type === "permanent-note")) {
    for (const f of RELATIONAL_FIELDS) {
        const v = p[f];
        if (!v) continue;
        const arr = Array.isArray(v) ? v : [v];
        for (const link of arr) {
            if (link && link.path) {
                const target = dv.page(link.path);
                if (!target) broken.push({ src: p.file.link, field: f, target: link.path });
            }
        }
    }
}

if (broken.length === 0) {
    dv.paragraph("✨ All frontmatter relational links resolve.");
} else {
    dv.paragraph(`**${broken.length}** broken frontmatter links.`);
    dv.table(
        ["Source", "Field", "Missing target"],
        broken.slice(0, 50).map(r => [r.src, r.field, `\`${r.target}\``])
    );
}
```

---

## Section 3 — Source Patterns (Folder Filter Recipes)

Every snippet above filters with a specific folder string — adjust to your needs. Common alternatives:

| Pattern | Meaning |
|---------|---------|
| `dv.pages('"999-report-organizing/_permanent-notes/v6-llm-elaborated"')` | One specific folder (the vault default) |
| `dv.pages('"999-report-organizing/_permanent-notes"')` | All permanent-note subfolders combined |
| `dv.pages('#permanent-note')` | All tagged notes (any folder) |
| `dv.pages().where(p => p.type === "permanent-note")` | All notes with the type, vault-wide (slow on large vaults) |
| `dv.pages('"Folder" and -"Folder/Archive"')` | Folder minus subfolder |
| `dv.pages('"Folder" or #permanent-note')` | Union: folder OR tagged |

DQL equivalents:

```text
FROM "999-report-organizing/_permanent-notes/v6-llm-elaborated"
FROM #permanent-note
FROM "999-report-organizing/_permanent-notes" AND -"999-report-organizing/_permanent-notes/v4-llm-condensed"
```

---

## 🔗 Related

- **[[Review-Dashboard]]** — the live console that combines every snippet here into one view
- **[[99-scripts/dv-review-helpers.js]]** — the helper module the dashboard depends on (DataviewJS only)
