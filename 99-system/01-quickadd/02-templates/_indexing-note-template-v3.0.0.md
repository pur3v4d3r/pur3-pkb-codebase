# Folder: [<% await tp.system.prompt("file-name") %>]
### 📁<% tp.file.title %>'s <small>Index Note</small>
## Overview
```dataview
TABLE status AS "Status/Note", rating AS "LLM-Output-Rating", file.ctime AS "Date Created"
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
SORT file.name ASC
```

```dataview
TABLE 
    regexreplace(file.name, "^cog-psy-report_", "") AS "Note Title", 
    status AS "Status/Note", 
    rating AS "LLM-Output-Rating", 
    (date(today) - file.mtime) AS "Days Ago"
FROM ""
WHERE 
    file.folder = this.file.folder 
    AND file.name != this.file.name
SORT file.name ASC
```
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
## Notes by FROM Specification
```
LIST 
FROM 
WHERE file.folder = this.file.folder
SORT file.name ASC
LIMIT 20
```
##### **Cheat-Sheet for Queries**
```
dataview
```

| *Tags*                | *Type Property* | *Status*   |
| --------------------- | --------------- | ---------- |
| `#pkm`                | `reference`     | `read`     |
| `#pkb`                | `concept`       | `not-read` |
| `#cognitive-science`  | `permwnent`     |            |
| `#prompt-engineering` |                 |            |
| `#learning-theory`    |                 |            |
| `#type/reference`     |                 |            |








