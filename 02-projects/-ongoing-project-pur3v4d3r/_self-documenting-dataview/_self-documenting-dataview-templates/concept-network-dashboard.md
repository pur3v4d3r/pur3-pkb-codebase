---
tags: #dashboard
---

# 🌐 Concept Network Dashboard

## 📊 Most Referenced Concepts

```dataview
TABLE 
  length(file.inlinks) as "References",
  concept-type as "Type",
  status as "Status"
WHERE concept-type
SORT length(file.inlinks) DESC
LIMIT 15
```

## 🆕 Recently Updated Concepts

```dataview
TABLE 
  concept-type as "Type",
  length(file.inlinks) as "Uses",
  file.mtime as "Updated"
WHERE concept-type
SORT file.mtime DESC
LIMIT 10
```

## 🔥 Active Concept Applications

```dataview
TABLE 
  file.folder as "Location",
  concepts as "Concepts Applied",
  status as "Status"
WHERE concepts
WHERE status = "active" OR status = "planning"
SORT file.mtime DESC
LIMIT 20
```

## 📈 Concept Usage by Folder

```dataviewjs
const conceptNotes = dv.pages().where(p => p.concepts).array()

const folderStats = {}
conceptNotes.forEach(note => {
  const folder = note.file.folder
  if (!folderStats[folder]) folderStats[folder] = 0
  folderStats[folder]++
})

const sorted = Object.entries(folderStats)
  .sort((a, b) => b[1] - a[1])
  .map(([folder, count]) => [folder, count])

dv.table(["Folder", "Notes Using Concepts"], sorted)
```

## 🕸️ Orphaned Concepts

```dataview
TABLE concept-type, created
WHERE concept-type
WHERE length(file.inlinks) = 0
SORT created DESC
```