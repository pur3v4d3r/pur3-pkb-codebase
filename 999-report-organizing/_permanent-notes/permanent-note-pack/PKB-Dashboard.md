---
title: "PKB Dashboard"
aliases:
  - Knowledge Base Dashboard
  - Permanent Notes Overview
type: dashboard
status: evergreen
tags:
  - dashboard
  - meta
  - dataview
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# PKB Dashboard

> [!info] **Knowledge Base Overview**
> This dashboard provides a live overview of your Permanent Notes knowledge base using Dataview queries. All tables and lists update automatically as you add, edit, or link notes.

---

## Vault Statistics

> [!summary] **Quick Stats**
> - Total permanent notes: `$= dv.pages('"03-notes/01_permanent-notes"').where(p => p.type === "permanent-note").length`
> - Evergreen notes: `$= dv.pages('"03-notes/01_permanent-notes"').where(p => p.status === "evergreen").length`
> - Notes needing review: `$= dv.pages('"03-notes/01_permanent-notes"').where(p => p.status === "needs review" || p.status === "draft").length`
> - High confidence: `$= dv.pages('"03-notes/01_permanent-notes"').where(p => p.confidence === "high").length`
> - Domains covered: `$= dv.pages('"03-notes/01_permanent-notes"').where(p => p.domain).map(p => p.domain).distinct().length`

---

## Recently Updated Notes

```dataview
TABLE updated AS "Last Updated", domain AS "Domain", confidence AS "Confidence", mastery-stage AS "Mastery"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note"
SORT updated DESC
LIMIT 15
```

---

## Notes by Domain

```dataview
TABLE WITHOUT ID 
  key AS "Domain",
  length(rows) AS "Note Count",
  round(length(filter(rows, (r) => r.confidence = "high")) / length(rows) * 100) + "%" AS "High Confidence"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND domain
GROUP BY domain
SORT length(rows) DESC
```

---

## Notes by Mastery Stage

### Seedlings (New, Underdeveloped)

```dataview
LIST
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND mastery-stage = "seedling"
SORT created DESC
```

### Budding (Growing, Partially Developed)

```dataview
LIST
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND mastery-stage = "budding"
SORT updated DESC
```

### Evergreen (Mature, Well-Developed)

```dataview
LIST
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND mastery-stage = "evergreen"
SORT title ASC
```

---

## Notes by Complexity Level

```dataview
TABLE WITHOUT ID
  key AS "Complexity",
  length(rows) AS "Count"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND complexity-level
GROUP BY complexity-level
SORT key ASC
```

---

## Orphan Notes (No Incoming Links)

> [!warning] **Notes with zero backlinks need attention**
> These permanent notes are not linked to from anywhere else in the vault. Consider adding connections.

```dataview
TABLE domain AS "Domain", created AS "Created"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND length(file.inlinks) = 0
SORT created DESC
```

---

## Most Connected Notes (Knowledge Hubs)

```dataview
TABLE length(file.inlinks) AS "Backlinks", length(file.outlinks) AS "Outlinks", domain AS "Domain"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note"
SORT length(file.inlinks) + length(file.outlinks) DESC
LIMIT 15
```

---

## Ghost Links (Referenced But Not Created)

> [!tip] **Expansion Opportunities**
> These wiki-links appear in your notes but don't have corresponding files yet. Each is a candidate for a new permanent note.

```dataviewjs
// Find all outgoing links from permanent notes that point to non-existent files
const pages = dv.pages('"03-notes/01_permanent-notes"')
  .where(p => p.type === "permanent-note");

const brokenLinks = new Set();

for (const page of pages) {
  const outlinks = page.file.outlinks;
  for (const link of outlinks) {
    const target = dv.page(link.path);
    if (!target) {
      brokenLinks.add(link.path);
    }
  }
}

if (brokenLinks.size > 0) {
  const sorted = [...brokenLinks].sort();
  dv.list(sorted.map(l => `[[${l}]]`));
} else {
  dv.paragraph("*All wiki-links are populated. Great work!*");
}
```

---

## Notes by Source Report

```dataview
TABLE WITHOUT ID
  key AS "Source Report",
  length(rows) AS "Notes Generated",
  min(rows.created) AS "First Created"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND source-reports
FLATTEN source-reports AS sr
GROUP BY sr
SORT length(rows) DESC
```

---

## Notes Due for Review

> [!warning] **Review Schedule**
> Notes flagged for periodic review based on their `review-frequency` setting.

```dataviewjs
const today = dv.date("today");
const pages = dv.pages('"03-notes/01_permanent-notes"')
  .where(p => p.type === "permanent-note" && p.updated && p["review-frequency"]);

const dueForReview = [];

for (const p of pages) {
  const updated = dv.date(p.updated);
  if (!updated) continue;
  
  const freq = p["review-frequency"];
  let daysThreshold;
  
  if (freq === "monthly") daysThreshold = 30;
  else if (freq === "quarterly") daysThreshold = 90;
  else if (freq === "biannual") daysThreshold = 180;
  else if (freq === "annual") daysThreshold = 365;
  else daysThreshold = 90; // default to quarterly
  
  const daysSinceUpdate = Math.floor((today - updated) / (1000 * 60 * 60 * 24));
  
  if (daysSinceUpdate >= daysThreshold) {
    dueForReview.push({
      link: p.file.link,
      domain: p.domain || "—",
      lastUpdated: p.updated,
      daysSince: daysSinceUpdate,
      frequency: freq
    });
  }
}

if (dueForReview.length > 0) {
  dv.table(
    ["Note", "Domain", "Last Updated", "Days Overdue", "Frequency"],
    dueForReview
      .sort((a, b) => b.daysSince - a.daysSince)
      .map(r => [r.link, r.domain, r.lastUpdated, r.daysSince, r.frequency])
  );
} else {
  dv.paragraph("*All notes are up to date with their review schedules.*");
}
```

---

## Confidence Distribution

```dataviewjs
const pages = dv.pages('"03-notes/01_permanent-notes"')
  .where(p => p.type === "permanent-note" && p.confidence);

const counts = {};
for (const p of pages) {
  const c = p.confidence;
  counts[c] = (counts[c] || 0) + 1;
}

const order = ["high", "medium", "low"];
dv.table(
  ["Confidence", "Count", "Percentage"],
  order
    .filter(c => counts[c])
    .map(c => [
      c.charAt(0).toUpperCase() + c.slice(1),
      counts[c],
      Math.round(counts[c] / pages.length * 100) + "%"
    ])
);
```

---

## High-Importance Notes

```dataview
TABLE domain AS "Domain", confidence AS "Confidence", mastery-stage AS "Mastery"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND importance = "critical"
SORT domain ASC
```

---

## Tag Cloud (Top Domains)

```dataviewjs
const pages = dv.pages('"03-notes/01_permanent-notes"')
  .where(p => p.type === "permanent-note" && p.tags);

const tagCounts = {};
for (const p of pages) {
  for (const tag of p.tags) {
    if (tag === "permanent-note" || tag === "evergreen") continue;
    tagCounts[tag] = (tagCounts[tag] || 0) + 1;
  }
}

const sorted = Object.entries(tagCounts)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 25);

dv.table(
  ["Tag", "Usage Count"],
  sorted.map(([tag, count]) => [`#${tag}`, count])
);
```

---

*Dashboard auto-updates via Dataview. Last manual review: `= this.updated`*
