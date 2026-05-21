---
aliases:
  - "Folder Tree Snippet"
  - "Snippet"
tags:
  - "type/report"
  - "year/2025"
  - "type/tutorial"
  - "status/in-progress"
  - "pkb"
  - "obsidian"
  - "note-organization"
  - "cognitive-science/cognitive-load"
  - "cognitive-load-management"
  - "cognitive-resources"
  - "pkb/optimization"
  - "folder-strategy"
  - "cognitive-pkm"
source: "claude-sonnet-4.5"
id: "20251205200816"
created: "2025-12-05T20:08:16"
modified: "2025-12-05T20:08:16"
week: "[[2025-W49]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "reference"
maturity: "needs-review"
confidence: "speculative"
next-review: "2025-12-12"
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-05|Daily-Note]]"
---

> [!purpose] ### Overview
> - **Title**:: [[Snippet System: Folder Tree]]
> - **Prompt/Topic Used**:: 
> - **Status**:: 🌱 `= this.maturity` | Confidence: `= this.confidence`

> [! ] # :FasClipboardList:In-Note Metadata Panel
> 
> - **Note-Type**: `= this.type`
> - **Development Status**: `= this.maturity`
> - **Epistemic Confidence**: `= this.confidence`
> - **Next Review**: `= this.next-review`
> - **Review Count**: `= this.review-count`
> - **Created**: `= this.created`
> - **Last Modified**: `= this.modified`
> 
> > [!purpose] ### 📝Content Metrics
> > [**Word Count**:: `= this.file.size`]| [**Est. Read Time**:: `= round(this.file.size / 1300) + " min"`]
> > [**Depth Class**:: `= choice(this.file.size < 500, "🌱Stub", choice(this.file.size < 2000, "📄Note", "📜Essay"))`]
> ----
> > [!purpose] ### 🕰️Temporal Context
> > [**Created**:: `= this.file.ctime`] | [**Age**:: `= (date(today) - this.file.ctime).days + " days"`]
> > [**Last Touch**:: `= this.file.mtime`] | [**Staleness**:: `= choice((date(today) - this.file.mtime).days > 180, "🕸️Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂Cold", "🔥Fresh"))`]
> > [**Touch Frequency**:: `= choice((date(today) - this.file.mtime).days < 7, "🔥Active", choice((date(today) - this.file.mtime).days < 30, "👌Regular", "❄️Dormant"))`]
> ----
> > [!topic-idea] ### 🔗Network Connectivity
> > [**In-Links**:: `= length(this.file.inlinks)`] | [**Out-Links**:: `= length(this.file.outlinks)`]
> > [**Network Status**:: `= choice(length(this.file.inlinks) = 0, "🕸️Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱Node"))`]
> ```dataviewjs
> // SYSTEM: Semantic Bridge Engine
> // PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts)
> const current = dv.current();
> const myOutlinks = current.file.outlinks.map(l => l.path);
> 
> // 1. Filter the Vault
> const siblings = dv.pages()
>     .where(p => p.file.path !== current.file.path) // Exclude self
>     .where(p => !current.file.outlinks.map(l => l.path).includes(p.file.path)) // Exclude existing direct links
>     .map(p => {
>         // Find overlap between this page's links and the current page's links
>         const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
>         return { 
>             link: p.file.link, 
>             sharedCount: shared.length, 
>             sharedLinks: shared 
>         };
>     })
>     .where(p => p.sharedCount > 0) // Must share at least 1 connection
>     .sort(p => p.sharedCount, "desc") // Sort by strongest connection
>     .limit(5); // Only show top 5
> 
> // 2. Render the Bridge
> if (siblings.length > 0) {
>     dv.header(3, "Semantic Bridges (Missing Connections)");
>     dv.table(
>         ["Sibling Note", "Strength", "Shared Context"], 
>         siblings.map(s => [
>             s.link, 
>             "🔗" + s.sharedCount, 
>             s.sharedLinks.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
>         ])
>     );
> } else {
>     dv.paragraph("*No semantic siblings found. This note is unique in its connections.*");
> }
> ```
> ---
> ### Related Notes
> ```dataview
> TABLE type, maturity, confidence
> FROM  ""
> WHERE  type = "reference"
> SORT "maturity" DESC
> LIMIT 15
> ```
> ### Sources & References
> ```dataview
> TABLE 
>     source AS "Source Type",
>     file.ctime AS "Date Added"
> FROM ""
> WHERE source = "claude-sonnet-4.5"
> SORT file.ctime DESC
> LIMIT 10
> ```
> ### Backlinks & Connections
> ```dataview
> TABLE 
>     type AS "Type",
>     maturity AS "Maturity",
>     length(file.inlinks) AS "Its Backlinks",
>     dateformat(date(created), "MMM dd, yyyy") AS "Created"
> FROM [[#]]
> WHERE file.name != this.file.name
> SORT length(file.inlinks) DESC
> LIMIT 20
> ```
> ### 2025-12-05 - Initial Creation
> *Context*: `=this.title` **by**: `=this.source`
> *Maturity*: `= this.maturity`  
> *Confidence*: `= this.confidence`
> 
> ### Tags & Classification
> *Primary Tags*: `= this.tags`  
> *Type*: `= this.type`  
> *Source*: `= this.source`
---

# Snippet System: Folder Tree


> [! ] ### Claude Thinking
> pur3v4d3r: I'm looking around at my current theme in my PKB, and the major thing that stands out at me, is the file tree. What kinds of snippets (Simple to Advanced) are there for customizing the File tree/Folder Tree. Thinking from text changes, icons, colors, etc., matching to the current themes colors.
> GitHub Copilot: 
> The user is asking about customization options for the file tree/folder tree in Obsidian. They want to understand the range of possibilities from simple to advanced, including:
> - Text styling changes
> - Icons
> - Colors
> - Integration with their current theme
> This is a discovery/educational request rather than a specific implementation request. I should provide an overview of the customization spectrum with examples at different complexity levels, showing what's possible.
> Key areas to cover:
> 1. Simple text/color changes
> 2. Folder/file icons (Unicode/emoji)
> 3. Custom folder colors/highlighting
> 4. Advanced: Conditional styling based on folder names
> 5. Advanced: Hover effects, animations
> 6. Advanced: Integration with folder structure (indentation, nesting indicators)
> I should provide code examples at each level so they can see what's involved and choose their desired complexity level.

> [! ] # 📁 File Tree Customization Spectrum
> 
> The file explorer is one of the most customizable areas in Obsidian. Here's a breakdown from simple to advanced:

---

## 🟢 **LEVEL 1: Simple Color & Typography**

### Basic Folder/File Styling
```css
/* Change folder text color */
.nav-folder-title {
  color: #7800F4; /* Signature purple */
  font-weight: 600;
}

/* Change file text color */
.nav-file-title {
  color: #FFFFFF;
  font-size: 13px;
}

/* Highlight active file */
.nav-file-title.is-active {
  color: #FFC700; /* Signature gold */
  background-color: rgba(120, 0, 244, 0.15);
}
```

---

## 🟡 **LEVEL 2: Icons & Visual Indicators**

### Add Folder Icons (Unicode/Emoji)
```css
/* Add folder icon before folder names */
.nav-folder-title::before {
  content: "📁 ";
  margin-right: 4px;
}

/* Collapsed folder icon */
.nav-folder.is-collapsed .nav-folder-title::before {
  content: "📂 ";
}

/* Add file icon before files */
.nav-file-title::before {
  content: "📄 ";
  margin-right: 4px;
  opacity: 0.6;
}
```

### Different Icons for Different File Types
```css
/* Markdown files */
.nav-file-title[data-path$=".md"]::before {
  content: "📝 ";
}

/* Canvas files */
.nav-file-title[data-path$=".canvas"]::before {
  content: "🎨 ";
}

/* PDFs */
.nav-file-title[data-path$=".pdf"]::before {
  content: "📕 ";
}
```

---

## 🟠 **LEVEL 3: Conditional Folder Styling**

### Color-Code Folders by Name/Purpose
```css
/* Projects folder in purple */
.nav-folder-title[data-path*="02-projects"] {
  color: #7800F4;
  font-weight: 700;
}

.nav-folder-title[data-path*="02-projects"]::before {
  content: "🚀 ";
}

/* Daily notes in teal */
.nav-folder-title[data-path*="01_daily-notes"] {
  color: #72FFF1;
}

.nav-folder-title[data-path*="01_daily-notes"]::before {
  content: "📅 ";
}

/* Library in gold */
.nav-folder-title[data-path*="04-library"] {
  color: #FFC700;
}

.nav-folder-title[data-path*="04-library"]::before {
  content: "📚 ";
}

/* System folders dimmed */
.nav-folder-title[data-path*="99-system"] {
  opacity: 0.5;
  font-size: 11px;
}

.nav-folder-title[data-path*="99-system"]::before {
  content: "⚙️ ";
}
```

---

## 🔴 **LEVEL 4: Advanced Visual Hierarchy**

### Enhanced Nesting & Indentation
```css
/* Improved visual hierarchy for nested folders */
.nav-folder.mod-root > .nav-folder-children > .nav-folder {
  border-left: 2px solid rgba(120, 0, 244, 0.3);
  margin-left: 8px;
  padding-left: 12px;
}

/* Subtle background for folder groups */
.nav-folder-children {
  background: rgba(0, 0, 0, 0.1);
  border-radius: 4px;
  padding: 4px 0;
  margin: 2px 0;
}

/* Hover effects */
.nav-folder-title:hover {
  background: linear-gradient(90deg, 
    rgba(120, 0, 244, 0.2) 0%, 
    transparent 100%);
  border-left: 3px solid #7800F4;
  padding-left: 5px;
  transition: all 0.2s ease;
}

.nav-file-title:hover {
  background: rgba(114, 255, 241, 0.1);
  border-left: 2px solid #72FFF1;
  padding-left: 6px;
  transition: all 0.15s ease;
}
```

---

## 🟣 **LEVEL 5: Expert - Complete System**

### Comprehensive File Tree Theme
```css
/*
═══════════════════════════════════════════════════════════
 FILE TREE: Complete Customization System
 Purpose: Transform file explorer with signature palette
 Author: Pur3v4d3r
 Date: 2025-12-05
═══════════════════════════════════════════════════════════
*/

/* [FOUNDATION] Base Explorer Styling */
.nav-files-container {
  padding: 8px;
  background: rgba(120, 0, 244, 0.03);
}

/* [FOLDERS] Core Folder Styling */
.nav-folder-title {
  padding: 4px 8px;
  border-radius: 4px;
  font-weight: 600;
  transition: all 0.2s ease;
  position: relative;
}

.nav-folder-title::before {
  margin-right: 6px;
  font-size: 14px;
}

/* Folder States */
.nav-folder.is-collapsed .nav-folder-title::before {
  content: "▶️";
  font-size: 10px;
}

.nav-folder:not(.is-collapsed) .nav-folder-title::before {
  content: "🔽";
  font-size: 10px;
}

/* [FILES] Core File Styling */
.nav-file-title {
  padding: 3px 8px 3px 24px;
  border-radius: 3px;
  font-size: 12px;
  transition: all 0.15s ease;
}

/* Active File Highlight */
.nav-file-title.is-active {
  color: #FFC700;
  background: linear-gradient(90deg, 
    rgba(120, 0, 244, 0.3) 0%, 
    rgba(120, 0, 244, 0.1) 100%);
  border-left: 4px solid #FFC700;
  font-weight: 600;
}

/* [CONTEXT COLORS] Folder-Specific Styling */
.nav-folder-title[data-path*="00-inbox"] {
  color: #FF6B6B;
  background: rgba(255, 107, 107, 0.1);
}

.nav-folder-title[data-path*="01_daily-notes"] {
  color: #72FFF1;
  background: rgba(114, 255, 241, 0.1);
}

.nav-folder-title[data-path*="02-projects"] {
  color: #7800F4;
  background: rgba(120, 0, 244, 0.15);
}

.nav-folder-title[data-path*="03-notes"] {
  color: #FFC700;
  background: rgba(255, 199, 0, 0.1);
}

.nav-folder-title[data-path*="04-library"] {
  color: #4ECDC4;
  background: rgba(78, 205, 196, 0.1);
}

.nav-folder-title[data-path*="99-"] {
  opacity: 0.6;
  font-size: 11px;
  font-style: italic;
}

/* [INTERACTIONS] Hover & Focus States */
.nav-folder-title:hover,
.nav-file-title:hover {
  transform: translateX(3px);
  box-shadow: -3px 0 0 #7800F4;
}

/* [HIERARCHY] Nesting Indicators */
.nav-folder-children {
  position: relative;
}

.nav-folder-children::before {
  content: "";
  position: absolute;
  left: 8px;
  top: 0;
  bottom: 0;
  width: 1px;
  background: linear-gradient(180deg, 
    #7800F4 0%, 
    transparent 100%);
  opacity: 0.3;
}

/* [ACCESSIBILITY] Motion Sensitivity */
@media (prefers-reduced-motion: reduce) {
  .nav-folder-title,
  .nav-file-title {
    transition: none;
  }
  
  .nav-folder-title:hover,
  .nav-file-title:hover {
    transform: none;
  }
}
```

---

> [! ] ## 🎯 **Implementation Recommendation**
> 
> Based on your vault structure, I'd suggest:
> 
> **Quick Win (5 minutes)**: Start with Level 2-3 to add icons and color-code your main folders (00-inbox, 01_daily-notes, 02-projects, etc.)
> 
> **Full Treatment (15 minutes)**: Implement Level 5 for a complete cohesive system matching your signature palette.
> 
> Would you like me to generate a custom snippet specifically tailored to your folder structure (00-inbox, 01_daily-notes, 02-projects, etc.) with your signature colors?

