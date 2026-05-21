# [cosmology-reports-index]
# Index

## Overview

### Files in this Folder

```dataview
TABLE file.ctime AS "Date Created", file.mtime AS "Last Modified"
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
SORT file.name ASC
```

## Performance Metrics

### Folder Activity Metrics (Count & Rate)

```dataview
TABLE WITHOUT ID
  length(rows) AS "Total Notes in Folder",
  length(filter(rows, (r) => date(r.file.ctime) >= date(today) - dur(7 days))) AS "New Notes (Last 7 Days)",
  length(filter(rows, (r) => date(r.file.mtime) >= date(today) - dur(7 days))) AS "Modified Notes (Last 7 Days)"
FLATTEN file.mtime as modified
WHERE file.folder = this.file.folder AND file.name != this.file.name
GROUP BY "Folder Metrics"
```
## Recent Changes

### Recent Changes (Detailed Modification Log)

```dataview
TABLE
  file.mtime AS "Last Modified Date",
  (date(today) - file.mtime) AS "Days Ago"
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
SORT file.mtime DESC
LIMIT 15
```
## Linking Metrics

### Links to this Folder's Notes

```dataview
LIST
FROM [[]]
WHERE contains(file.outlinks, this.file.folder)
  AND file.folder != this.file.folder
SORT file.name ASC
```

### Orphaned Notes in this folder with no Links

```dataview
TABLE WITHOUT ID
  file.link AS "Orphaned Note",
  length(file.outlinks) AS "Links Out"
FROM ""
WHERE file.folder = this.file.folder
  AND length(file.inlinks) = 0
  AND file.name != this.file.name
SORT file.name ASC
```

## Notes by Tag Specification

### Notes by Specific Tag

```
LIST 
FROM "type = [🧬concept]"
WHERE file.folder = this.file.folder
SORT file.name ASC
```

Note:
- You need to fill out the correct Tags you want to be dispayed in this section.
- Refer to Tag Taxonomy here: [[reference-taxonomy-pur3v4d3r-tags_202511190109]]
dataview