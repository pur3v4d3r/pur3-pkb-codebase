---
title: "Query Tips"
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

# Query Tips

> [!definition] Query Tips
> *Definition pending — derived from 1 source report(s).*

## Core Explanation

> [!evidence] Query Tips
> - Always use `"` around folder paths in `FROM` clauses
> - Use `contains()` for checking if a list contains a value
> - `file.inlinks` = pages linking TO this page, `file.outlinks` = pages this page links TO
> - `FLATTEN` turns array fields into individual rows for grouping
> - `date(today)` gives today's date, `dur(7 days)` gives a duration
> - Inline fields use `[key:: value]` syntax and are queryable like frontmatter
> *— [[Dataview-Query-Reference]]*

## Connections

**Related:** [[metacognition]]

```dataview
LIST FROM [[Query Tips]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[Dataview-Query-Reference]]
