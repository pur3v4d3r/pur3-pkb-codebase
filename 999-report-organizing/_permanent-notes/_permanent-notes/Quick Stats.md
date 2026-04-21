---
title: "Quick Stats"
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
  source-reports: [PKB-Dashboard]
  extraction-method: pkb-extractor-v1 → pipeline-v3
---

# Quick Stats

> [!definition] Quick Stats
> *Definition pending — derived from 1 source report(s).*

## Core Explanation

> [!evidence] Quick Stats
> - Total permanent notes: `$= dv.pages('"03-notes/01_permanent-notes"').where(p => p.type === "permanent-note").length`
> - Evergreen notes: `$= dv.pages('"03-notes/01_permanent-notes"').where(p => p.status === "evergreen").length`
> - Notes needing review: `$= dv.pages('"03-notes/01_permanent-notes"').where(p => p.status === "needs review" || p.status === "draft").length`
> - High confidence: `$= dv.pages('"03-notes/01_permanent-notes"').where(p => p.confidence === "high").length`
> - Domains covered: `$= dv.pages('"03-notes/01_permanent-notes"').where(p => p.domain).map(p => p.domain).distinct().length`
> *— [[PKB-Dashboard]]*

## Connections

```dataview
LIST FROM [[Quick Stats]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[PKB-Dashboard]]
