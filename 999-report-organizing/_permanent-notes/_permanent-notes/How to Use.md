---
title: "How to Use"
aliases: []
type: permanent-note
status: evergreen
confidence: medium
domain: uncategorized
subdomains: []
tags: [permanent-note, uncategorized]
created: '2026-04-21'
updated: '2026-04-21'
complexity: intermediate
importance: medium
review-frequency: quarterly
mastery-stage: seedling
provenance:
  source-type: report-extraction
  pipeline-version: "3.0.0"
  source-reports: [Dataview-Query-Reference]
  extraction-method: pkb-extractor-v1 → pipeline-v3
---

# How to Use

> [!definition] How to Use
> *Definition pending — derived from 1 source report(s).*

## Core Explanation

> [!evidence] How to Use
> Copy any query below into a note. Wrap it in a fenced code block with `dataview` or `dataviewjs` as the language. Queries update live as your vault changes.
> *— [[Dataview-Query-Reference]]*

## Connections

**Related:** [[metacognition]]

```dataview
LIST FROM [[How to Use]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[Dataview-Query-Reference]]
