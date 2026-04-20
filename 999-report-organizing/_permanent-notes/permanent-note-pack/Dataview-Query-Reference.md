---
title: "Dataview Query Reference"
aliases:
  - DQL Reference
  - PKB Queries
type: reference
status: evergreen
tags:
  - reference
  - dataview
  - meta
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# Dataview Query Reference for PKB

> [!info] **How to Use**
> Copy any query below into a note. Wrap it in a fenced code block with `dataview` or `dataviewjs` as the language. Queries update live as your vault changes.

---

## Basic Queries

### List All Permanent Notes

```
dataview
LIST
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note"
SORT title ASC
```

### Table of Notes with Key Metadata

```
dataview
TABLE domain AS "Domain", confidence AS "Confidence", mastery-stage AS "Mastery", importance AS "Importance"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note"
SORT domain ASC, title ASC
```

### Notes Created This Week

```
dataview
TABLE created AS "Created", domain AS "Domain"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND created >= date(today) - dur(7 days)
SORT created DESC
```

### Notes Created This Month

```
dataview
TABLE created AS "Created", domain AS "Domain", confidence AS "Confidence"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND created >= date(today) - dur(30 days)
SORT created DESC
```

---

## Filtering Queries

### Notes by Specific Domain

```
dataview
LIST
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND domain = "cognitive-psychology"
SORT title ASC
```

### High-Confidence Notes Only

```
dataview
TABLE domain AS "Domain", complexity-level AS "Complexity"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND confidence = "high"
SORT domain ASC
```

### Notes by Complexity Level

```
dataview
TABLE domain AS "Domain", confidence AS "Confidence"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND complexity-level = "advanced-practitioner"
SORT title ASC
```

### Critical Importance Notes

```
dataview
TABLE domain AS "Domain", mastery-stage AS "Mastery", confidence AS "Confidence"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND importance = "critical"
SORT domain ASC
```

### Notes from a Specific Source Report

```
dataview
LIST
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND contains(source-reports, "Your Report Title Here")
SORT title ASC
```

### Seedling Notes (Needing Development)

```
dataview
TABLE domain AS "Domain", created AS "Created", confidence AS "Confidence"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND mastery-stage = "seedling"
SORT created ASC
```

---

## Relationship & Connection Queries

### Notes That Link to a Specific Note

> Replace "Metacognition" with any note name to find what links to it.

```
dataview
LIST
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND contains(file.outlinks, [[metacognition]])
SORT title ASC
```

### Orphan Notes (No Incoming Links)

```
dataview
TABLE domain AS "Domain", created AS "Created"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND length(file.inlinks) = 0
SORT created DESC
```

### Most Connected Notes

```
dataview
TABLE length(file.inlinks) AS "Backlinks", length(file.outlinks) AS "Outlinks", 
  length(file.inlinks) + length(file.outlinks) AS "Total"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note"
SORT length(file.inlinks) + length(file.outlinks) DESC
LIMIT 20
```

### Notes with Fewest Outgoing Links

> These notes may need more connections added.

```
dataview
TABLE length(file.outlinks) AS "Outlinks", domain AS "Domain"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note"
SORT length(file.outlinks) ASC
LIMIT 15
```

---

## Grouping Queries

### Notes Grouped by Domain

```
dataview
TABLE WITHOUT ID key AS "Domain", length(rows) AS "Count"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND domain
GROUP BY domain
SORT length(rows) DESC
```

### Notes Grouped by Mastery Stage

```
dataview
TABLE WITHOUT ID key AS "Mastery Stage", length(rows) AS "Count"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND mastery-stage
GROUP BY mastery-stage
SORT key ASC
```

### Notes Grouped by Source Report

```
dataview
TABLE WITHOUT ID key AS "Source Report", length(rows) AS "Notes"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND source-reports
FLATTEN source-reports AS sr
GROUP BY sr
SORT length(rows) DESC
```

### Notes Grouped by Confidence Level

```
dataview
TABLE WITHOUT ID key AS "Confidence", length(rows) AS "Count"
FROM "03-notes/01_permanent-notes"
WHERE type = "permanent-note" AND confidence
GROUP BY confidence
SORT key ASC
```

---

## DataviewJS Advanced Queries

### Ghost Links Finder

> Finds all wiki-links in permanent notes that point to non-existent files.

```
dataviewjs
const pages = dv.pages('"03-notes/01_permanent-notes"')
  .where(p => p.type === "permanent-note");

const ghost = new Set();

for (const page of pages) {
  for (const link of page.file.outlinks) {
    if (!dv.page(link.path)) {
      ghost.add(link.path);
    }
  }
}

if (ghost.size > 0) {
  dv.header(3, `${ghost.size} Ghost Links Found`);
  dv.list([...ghost].sort().map(l => `[[${l}]]`));
} else {
  dv.paragraph("*All wiki-links resolve to existing notes.*");
}
```

### Review Schedule Checker

> Shows notes overdue for review based on their review-frequency setting.

```
dataviewjs
const today = dv.date("today");
const pages = dv.pages('"03-notes/01_permanent-notes"')
  .where(p => p.type === "permanent-note" && p.updated && p["review-frequency"]);

const due = [];

for (const p of pages) {
  const updated = dv.date(p.updated);
  if (!updated) continue;
  
  const freq = p["review-frequency"];
  let days;
  if (freq === "monthly") days = 30;
  else if (freq === "quarterly") days = 90;
  else if (freq === "biannual") days = 180;
  else if (freq === "annual") days = 365;
  else days = 90;
  
  const elapsed = Math.floor((today - updated) / 86400000);
  if (elapsed >= days) {
    due.push([p.file.link, p.domain || "—", p.updated, elapsed + " days", freq]);
  }
}

if (due.length > 0) {
  due.sort((a, b) => parseInt(b[3]) - parseInt(a[3]));
  dv.table(["Note", "Domain", "Last Updated", "Overdue By", "Frequency"], due);
} else {
  dv.paragraph("*All notes are current with their review schedule.*");
}
```

### Domain Coverage Heatmap (Text-Based)

```
dataviewjs
const pages = dv.pages('"03-notes/01_permanent-notes"')
  .where(p => p.type === "permanent-note" && p.domain);

const counts = {};
for (const p of pages) {
  counts[p.domain] = (counts[p.domain] || 0) + 1;
}

const max = Math.max(...Object.values(counts));
const sorted = Object.entries(counts).sort((a, b) => b[1] - a[1]);

const rows = sorted.map(([domain, count]) => {
  const bar = "█".repeat(Math.ceil(count / max * 20));
  return [domain, count, bar];
});

dv.table(["Domain", "Notes", "Coverage"], rows);
```

### Expansion Topics Aggregator

> Collects all expansion-topics from permanent notes into one list.

```
dataviewjs
const pages = dv.pages('"03-notes/01_permanent-notes"')
  .where(p => p.type === "permanent-note" && p["expansion-topics"]);

const topics = [];

for (const p of pages) {
  const et = p["expansion-topics"];
  if (!et) continue;
  
  const items = Array.isArray(et) ? et : [et];
  for (const item of items) {
    if (item && item.topic) {
      topics.push([
        item.topic,
        item.priority || "—",
        item.description || "—",
        p.file.link
      ]);
    }
  }
}

if (topics.length > 0) {
  // Sort by priority
  const order = { "high": 0, "medium": 1, "low": 2, "—": 3 };
  topics.sort((a, b) => (order[a[1]] || 3) - (order[b[1]] || 3));
  dv.table(["Topic", "Priority", "Description", "Source Note"], topics);
} else {
  dv.paragraph("*No expansion topics found.*");
}
```

---

## Inline Query Examples

> Use these inline queries anywhere in a note. They render as a single value.

**Count of all permanent notes:**
`` `= length(filter(file.tasks, (t) => !t.completed))` ``
Actually use: `` `$= dv.pages('"03-notes/01_permanent-notes"').where(p => p.type === "permanent-note").length` ``

**Current note's domain:**
`` `= this.domain` ``

**Current note's creation date:**
`` `= this.created` ``

**Current note's backlink count:**
`` `= length(this.file.inlinks)` ``

**Current note's outlink count:**
`` `= length(this.file.outlinks)` ``

---

> [!tip] **Query Tips**
> - Always use `"` around folder paths in `FROM` clauses
> - Use `contains()` for checking if a list contains a value
> - `file.inlinks` = pages linking TO this page, `file.outlinks` = pages this page links TO
> - `FLATTEN` turns array fields into individual rows for grouping
> - `date(today)` gives today's date, `dur(7 days)` gives a duration
> - Inline fields use `[key:: value]` syntax and are queryable like frontmatter

---

*Reference last updated: `= this.updated`*
