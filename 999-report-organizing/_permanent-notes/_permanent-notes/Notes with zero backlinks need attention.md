---
title: "Notes with zero backlinks need attention"
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

# Notes with zero backlinks need attention

> [!definition] Notes with zero backlinks need attention
> *Definition pending — derived from 1 source report(s).*

## Practical Implications

> [!warning] Notes with zero backlinks need attention
> These permanent notes are not linked to from anywhere else in the vault. Consider adding connections.
> *— [[PKB-Dashboard]]*

## Connections

```dataview
LIST FROM [[Notes with zero backlinks need attention]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[PKB-Dashboard]]
