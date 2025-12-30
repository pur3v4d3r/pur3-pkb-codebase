---
type: prompt-component
id: "20251212205052"
status: active
version: 1.0.0
rating: "0.0"
source: pur3v4d3r
title: Generate Components for Dataview, Dataviewjs, Etc.
description: This instruction tells the LLM to generate various examples of Dataview, can be run multiple time to achieve various results.
key-takeaway: Works and has provided excellent resources.
last-used: "[[2025-12-12]]"
tags:
  - year/2025
  - llm-capability/generation
  - prompt-workflow/deployment
  - prompt-pattern
  - prompt-engineering/anatomy
aliases:
  - Prompt-Engineering
  - Prompt Component
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
link-related:
  - "[[2025-12-12|Daily Note]]"
  - "[[2025-W50|Weekly Review]]"
---

> [!in-note-metadata]
> ### Prompt Component Metadata
> 
> *Prompt-Component-ID*:: `=this.id`
> *Prompt-Component-Version*:: `=this.version`
> *Prompt-Component-Description*:: `=this.description`
> 
> > [!review] 🕰️Temporal Context
> > **Created**:: `= this.file.ctime` | **Age**:: `= (date(today) - this.file.ctime).days + " days"`
> > **Last Touch**:: `= this.file.mtime` | **Staleness**:: `= choice((date(today) - this.file.mtime).days > 180, "🕸️ Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂 Cold", "🔥 Fresh"))`
> 
> > [!review] 📝Content Metrics
> > **Word Count**:: `= this.file.size` B | **Est. Read Time**:: `= round(this.file.size / 1300) + " min"`
> > **Depth Class**:: `= choice(this.file.size < 500, "🌱 Stub", choice(this.file.size < 2000, "📄 Note", "📜 Essay"))`
>
> >[!review] 🛠️ Metadata Health Check
> > **Missing Fields**:: `$= const fields = ["status", "type", "tags"]; const missing = fields.filter(f => !dv.current()[f]); missing.length > 0 ? "⚠️ Missing: " + missing.join(", ") : "✅ All Systems Go"`

> [!purpose] 🔗Network Connectivity
> **In-Links**:: `= length(this.file.inlinks)` | **Out-Links**:: `= length(this.file.outlinks)`
> **Network Status**:: `= choice(length(this.file.inlinks) = 0, "🕸️ Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱 Node"))`
> 
> > [!review] 📂Folder Context
> > **Location**:: `= this.file.folder`
> > **Neighbors**:: `$= dv.pages('"' + dv.current().file.folder + '"').length - 1` other notes here.
>```dataviewjs
>// 🧠 SYSTEM: Semantic Bridge Engine
>// PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts)
>const current = dv.current();
>const myOutlinks = current.file.outlinks.map(l => l.path);
>
>// 1. Filter the Vault
>const siblings = dv.pages()
>    .where(p => p.file.path !== current.file.path) // Exclude self
>    .where(p => !current.file.outlinks.map(l => l.path).includes(p.file.path)) // Exclude existing direct links
>    .map(p => {
>        // Find overlap between this page's links and the current page's links
>        const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
>        return { 
>            link: p.file.link, 
>            sharedCount: shared.length, 
>            sharedLinks: shared 
>        };
>    })
>    .where(p => p.sharedCount > 0) // Must share at least 1 connection
>    .sort(p => p.sharedCount, "desc") // Sort by strongest connection
>    .limit(5); // Only show top 5
>
>// 2. Render the Bridge
>if (siblings.length > 0) {
>    dv.header(4, "🌉 Semantic Bridges (Missing Connections)");
>    dv.table(
>        ["Sibling Note", "Strength", "Shared Context"], 
>        siblings.map(s => [
>            s.link, 
>            "🔗 " + s.sharedCount, 
>            s.sharedLinks.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
>        ])
>    );
>} else {
>    dv.paragraph("*No semantic siblings found. This note is unique in its connections.*");
>}
>```
>
>#### Related Notes
>```dataview
>TABLE rating, title, status, version, source
>FROM  ""
>WHERE  type = "prompt-component"
>SORT "maturity" DESC
>LIMIT 15
>```

[Initial Creation: [[2025-12-12|Friday, December 12th, 2025]]]

---

# prompt-component-instruction-generate-dataview-inline-queries-reference-v1.0.0-2025121220

`````prompt-component
----
Prompt-Component-ID: "2025121220"
Prompt-Component-Version: 1.0.0
----

<goal>
Comprehensive Resource that contains a collection of Dataview Queries, Dataview Inline Queries and Advanced Dataviejs Queries. Specifically, for use within an "indexing note", for me to use around my PKB.
</goal>
<task>
I need a comprehensive resource that covers all available "Dataview Queries", "Dataview Inline Queries" and "Advanced Dataviejs Queries" pertaining to Index Note Dashboards.
This reference isn't about these types of queries, it's a comprehensive resource/compendium that encompasses all known queries of this type that you find while conducting your tree of thoughts search.
I require you to cover as many areas as you can. My main purpose is to amass a collection of these, to pull from, as a resource to build various index notes/dashboards, that display information pertaining to the folder the notes are contained and links between the notes in the folder, among other novel uses.
Side Note: I'm also very interested to know what novel/advanced use cases there are.
</task>
<exemplar>
```dataview
TABLE file.ctime AS "Date Created", file.mtime AS "Last Modified"
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
SORT file.name ASC
```
```dataview
TABLE WITHOUT ID
  length(rows) AS "Total Notes in Folder",
  length(filter(rows, (r) => date(r.file.ctime) >= date(today) - dur(7 days))) AS "New Notes (Last 7 Days)",
  length(filter(rows, (r) => date(r.file.mtime) >= date(today) - dur(7 days))) AS "Modified Notes (Last 7 Days)"
FLATTEN file.mtime as modified
WHERE file.folder = this.file.folder AND file.name != this.file.name
GROUP BY "Folder Metrics"
```
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
</exemplar>

`````
