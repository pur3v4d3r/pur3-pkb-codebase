---
type: "prompt-component"
id: "20251202202226"
status: "active"
version: "1.0.0"
rating: "0.0"
source: "pur3v4d3r"
title: "Comprehensive Reference on Stoic Key Terms"
description: "A Comprehensive Reference Note on the various “Stoic/Stoicism Key Terms/Keywords/Definitions” found in the literature/teachings.  I'm currently studying and implementing Stoicism into my daily life. So, my purpose for this is to have a key reference to use for this goal, and to have a resource of these for using around my PKB, so it needs to be both informationally designed and visual appealing."
key-takeaway: "Has an Exemplar"
last-used: "[[2025-12-02]]"
tags:
  - "year/2025"
  - "llm-capability/generation"
  - "prompt-workflow/deployment"
  - "prompt-pattern"
  - "prompt-engineering/anatomy"
aliases:
  - "Prompt-Engineering"
  - "Prompt Component"
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
link-related:
  - "[[2025-12-02|Daily Note]]"
  - "[[2025-W49|Weekly Review]]"
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

[Initial Creation: [[2025-12-02|Tuesday, December 2nd, 2025]]]

---

# prompt-component-instruction-generate-reference-on-stoic-key-terms-v1.0.0-2025120220

```prompt-component
----
Prompt-Component-ID: "2025120220"
Prompt-Component-Version: 1.0.0
----

- I need a Comprehensive Reference Note on the various “Stoic/Stoicism Key Terms/Keywords/Definitions” found in the literature/teachings.

I'm currently studying and implementing Stoicism into my daily life. So, my purpose for this is to have a key reference to use for this goal, and to have a resource of these for using around my PKB, so it needs to be both informationally designed and visual appealing.

Exemplar
- This is something along the Lines of what I had in mind for the Callout “Stoic/Stoicism Key Terms/Keywords/Definitions”
> [!definition]
> - [**Key-Term**:: [[{{KEY TERM/KEYWORD GOES HERE}}]]]
> - [**Definition**:: {{DEFINITON OF THE KEY TERMS/KEYWORDS GOES HERE}}]
> - {{ADD IN ADDITIONAL METADATA ABOUT THIS KEY TERM HERE}}
> - {{NOTE: USE AS MANY UN-ORDERED BULLETS AS NEEDED I LIKE METADATA}}
> - {{JUST MAKE SURE DATAVIEW IS ABLE TO PARSE THE INFORMATION}}

```

