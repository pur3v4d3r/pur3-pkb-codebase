---
type: "prompt-component"
id: "20251202195311"
status: "active"
version: "1.0.0"
rating: "0.0"
source: "pur3v4d3r"
title: "Comprehensive Reference Note on Stoic Quote/Precepts"
description: "A comprehensive Reference Note on Stoic Quotes and Stoic Precepts. This is to be used as a foundational resource for quotes and precepts for use in my Daily Note, so I can practice Stoicism daily."
key-takeaway: "Has an Exemplar of how the quote/precept should look, using callouts."
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

# prompt-component-instruction-generate-reference-note-on-stoic-quote-v1.0.0-2025120219

```prompt-component
----
Prompt-Component-ID: "2025120219"
Prompt-Component-Version: 1.0.0
----

### Goal

I need A comprehensive Reference Note on Stoic Quotes and Stoic Precepts. This is to be used as a foundational resource for quotes and precepts for use in my Daily Note, so I can practice Stoicism daily.

### Exemplar
- This is how you should handle displaying the information for *each* Quote or Precept (Note: On citations you need to fill out all the required information, put n/a if not available.):

> [!stoic-quote] Stoic Quote
> "Remember that it is not only the desire of having, but also the desire of avoiding, that is subject to our will. Remember that you are a mortal, and one of the parts of a whole. Remember that the nature of the things which you desire is not your own, but foreign. Remember that as soon as an impression *[phantasia]* arises, say to it: 'You are just an impression and not at all the thing you claim to be.' Then examine it by those rules which you have, and first and chiefly, by this: whether it relates to the things which are in our power, or to those which are not; and, if it relates to anything not in our power, be prepared to say: 'It is nothing to me.'"
> 	—— Epictetus, 
> 	    Discourses [Book II, Chapter 18]

> [!citation]
> ### Quote Bibliographic Information
> - **Source Type**:: 
> - **Title**:: 
> - **Author(s)**:: 
> - **Year**:: 
> - **Publisher / Journal**:: 
> - **Volume / Issue**:: 
> - **Page(s)**:: 
> - **URL / DOI**::
> ### Citation Metadata
> - **Citation ID**:: {{ Format = 202512021807}}
> - **Date Created**:: {{ Format = 2025-12-02T18:07:09}}
> - **LLM Used**:: Claude Sonnet 4.5
> 	- **Agent Used**:: Claude Project -> Comprehensive Reference Note Generator

```

