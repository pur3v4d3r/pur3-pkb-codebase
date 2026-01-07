---
type: prompt-component
id: "20251203190518"
status: active
version: 1.0.0
rating: "10.0"
source: pur3v4d3r
title: Meta Bind Buttons Reference
description: Comprehensive Reference that contains a taxonomy of Meta Bind Buttons for me to use around my PKB.
key-takeaway: Has Exemplar
last-used: "[[2025-12-03]]"
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
  - "[[2025-12-03|Daily Note]]"
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

[Initial Creation: [[2025-12-03|Wednesday, December 3rd, 2025]]]

---

# prompt-component-instruction-generate-meta-bind-buttons-reference-v1.0.0-2025120319

`````prompt-component
----
Prompt-Component-ID: "2025120319"
Prompt-Component-Version: 1.0.0
----

<goal>
Comprehensive Reference that contains a taxonomy of Meta Bind Buttons for me to use around my PKB.
</goal>

<task>
I need a comprehensive resource that covers all available Meta Bind Buttons.
This reference isnt about Meta Bind Buttons, its a comprehensive resource/compendium that encompasses all known Meta Bind Buttons that you find while conducting your tree of thoughts search.
I need you to cover as many different areas as you can. My main purpose is to amass a collection of these, to pull from, as a resource to build various interactive panels and mini interactive dashboards.
Side Note: Im also very interested to know what novel/advanced use cases there are.
</task>

<exemplar>
Note: This is an exemplar of how you should handle the structure of buttons in this reference.

----

## Note Maturity

```
## 🌱 Development Status

**Current Maturity**: `VIEW[{maturity}]`

`BUTTON[maturity-seedling]`
`BUTTON[maturity-budding]`
`BUTTON[maturity-developing]`
`BUTTON[maturity-evergreen]`

```

### Maturity Seedling

```
# Button Template: maturity-seedling
id: maturity-seedling
label: 🌱 Seedling
style: default
action:
  type: updateMetadata
  bindTarget: maturity
  evaluate: false
  value: seedling
  
  label: Seedling
icon: sprout
style: default
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: maturity-seedling
hidden: false
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: seedling
```

> [! ] ### Metadata
> - **Function/Purpose**: {{PROVIDE THE BUTTONS FUNCTION}}
> - **Use Cases**: {{PROVIDE EXAMPLE USE CASES}}

> [! ] ### Button Example
`VIEW[{maturity}]`

```meta-bind-button
label: Seedling-A
icon: sprout
style: default
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: maturity-seedling
hidden: false
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: seedling-a
```

```meta-bind-button
label: Seedling-B
icon: sprout
style: default
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: maturity-seedling
hidden: false
actions:
  - type: updateMetadata
    bindTarget: maturity
    evaluate: false
    value: seedling-b
```

----
</exemplar>

`````
