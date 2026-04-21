---
title: "Path Format"
aliases: []
type: permanent-note
status: evergreen
confidence: high
domain: unknown
subdomains: []
tags: [permanent-note, unknown]
created: '2026-04-21'
updated: '2026-04-21'
complexity: intermediate
importance: medium
review-frequency: quarterly
mastery-stage: seedling
provenance:
  source-type: report-extraction
  pipeline-version: "3.0.0"
  source-reports: [Meta-Bind-Button-Setup-Guide_report]
  extraction-method: pkb-extractor-v1 → pipeline-v3
---

# Path Format

> [!definition] Path Format
> *Definition pending — derived from 1 source report(s).*

## Practical Implications

> [!warning] Path Format
> - Use **forward slashes** `/` only (not backslashes)
> - Paths are **relative to vault root** (no leading slash)
> - Do NOT include the `.md` extension in `fileName`
> - The `templateFile` path MUST include `.md`
> *— [[Meta-Bind-Button-Setup-Guide_report]]*

## Connections

**Related:** [[SRL-Dashboard-MOC]] · [[SRL-System-Setup-Guide]] · [[SRL-Reading-Session-Template]] · [[SRL-Monthly-Review-Template]] · [[Next-Note]] · [[Note-Name]] · [[SRL-Calibration-Log]] · [[SRL-Dashboard-MOC]] · [[SRL-Living-Learning-Agenda]] · [[SRL-Monthly-Review-Template]] · [[SRL-Quick-Reference-Cards]] · [[SRL-Reading-Session-Template]] · [[SRL-System-Setup-Guide]] · [[target-note]] · [[SRL-Living-Learning-Agenda]] · [[SRL-Calibration-Log]] · [[SRL-Quick-Reference-Cards]] · [[Note-Name]] · [[Next-Note]] · [[target-note]] · [[SRL-Dashboard-MOC]] · [[SRL-System-Setup-Guide]] · [[SRL-Reading-Session-Template]] · [[SRL-Monthly-Review-Template]] · [[SRL-Living-Learning-Agenda]] · [[SRL-Calibration-Log]] · [[SRL-Quick-Reference-Cards]] · [[Next-Note]] · [[Note-Name]] · [[SRL-Calibration-Log]] · [[SRL-Dashboard-MOC]] · [[SRL-Living-Learning-Agenda]] · [[SRL-Monthly-Review-Template]] · [[SRL-Quick-Reference-Cards]] · [[SRL-Reading-Session-Template]] · [[SRL-System-Setup-Guide]] · [[target-note]]

```dataview
LIST FROM [[Path Format]]
WHERE file.path != this.file.path
SORT file.mtime DESC
LIMIT 10
```

---

**Sources:** [[Meta-Bind-Button-Setup-Guide_report]]
