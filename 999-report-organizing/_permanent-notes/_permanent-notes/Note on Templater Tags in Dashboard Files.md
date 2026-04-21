---
title: "Note on Templater Tags in Dashboard Files"
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
  source-reports: [PKB-System-Setup-Guide]
  extraction-method: pkb-extractor-v1 → pipeline-v3
---

# Note on Templater Tags in Dashboard Files

> [!definition] Note on Templater Tags in Dashboard Files
> *Definition pending — derived from 1 source report(s).*

## Core Explanation

> [!evidence] Note on Templater Tags in Dashboard Files
> The dashboard files use `<% tp.date.now("YYYY-MM-DD") %>` for the created/updated dates. When you first open them, run Templater to resolve these. Alternatively, replace them with a static date before placing in your vault.
> *— [[PKB-System-Setup-Guide]]*

## Connections

```dataview
LIST FROM [[Note on Templater Tags in Dashboard Files]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[PKB-System-Setup-Guide]]
