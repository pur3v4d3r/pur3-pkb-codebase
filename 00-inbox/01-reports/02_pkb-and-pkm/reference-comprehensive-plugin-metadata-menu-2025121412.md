---
aliases:
  - Metadata Menu
  - metadata menu
tags:
  - type/report
  - year/2025
  - type/analysis
  - status/in-progress
  - pkb
  - pkm
  - metadata-systems
  - cognitive-science/metacognition
  - cognitive-load-management
  - cognitive-resources
  - pkb/optimization
  - cognitive-pkm
source: claude-sonnet-4.5
id: "20251214122932"
created: 2025-12-14T12:29:32
modified: 2025-12-14T12:29:32
week: "[[2025-W50]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: reference
maturity: seedling
confidence: speculative
next-review: 2025-12-21
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-14|Daily-Note]]"
---

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Comprehensive Reference: Metadata Menu]]
> - **MOC**: `=this.link-up`

```dataviewjs
// SYSTEM: Enhanced Semantic Bridge Engine v2.0
// PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts) with advanced analytics

const current = dv.current();
const myOutlinks = current.file.outlinks?.map(l => l.path) || [];

// Performance optimization: Create Set for faster lookups
const myOutlinkSet = new Set(myOutlinks);
const currentPath = current.file.path;

// Advanced sibling analysis with metadata
let siblings = [];

try {
  siblings = dv.pages()
    .where(p => {
      // Safety checks
      if (!p.file?.path || p.file.path === currentPath) return false;
      // Exclude already linked notes
      if (current.file.outlinks?.some(l => l.path === p.file.path)) return false;
      return true;
    })
    .map(p => {
      try {
        // Calculate shared connections
        const shared = p.file.outlinks?.filter(l => myOutlinkSet.has(l.path)) || [];
        const sharedCount = shared.length;
        
        // Calculate similarity score (0-100%)
        const totalConnections = myOutlinks.length + (p.file.outlinks?.length || 0);
        const similarityScore = totalConnections > 0 ? Math.round((sharedCount * 2 / totalConnections) * 100) : 0;
        
        return { 
          link: p.file.link, 
          sharedCount, 
          sharedLinks: shared,
          similarityScore,
          maturity: p.maturity || "unset",
          type: p.type || "unknown",
          lastModified: p.file.mtime
        };
      } catch (e) {
        console.warn("Error processing page:", p.file?.path, e);
        return null;
      }
    })
    .where(p => p && p.sharedCount > 0)
    .sort(p => p.similarityScore, "desc")
    .limit(8);
    
  // Ensure siblings is an array
  if (!Array.isArray(siblings)) {
    siblings = [];
  }
} catch (e) {
  console.error("Error building siblings:", e);
  siblings = [];
}

// Render enhanced semantic bridges
if (siblings.length > 0) {
  dv.header(3, "🔗 Semantic Bridges (Missing Connections)");
  
  // Add summary statistics with error handling
  try {
    const totalSharedConnections = siblings.reduce((sum, s) => sum + (s.sharedCount || 0), 0);
    const avgSimilarity = siblings.length > 0 ? 
      Math.round(siblings.reduce((sum, s) => sum + (s.similarityScore || 0), 0) / siblings.length) : 0;
    
    dv.paragraph(`**Found ${siblings.length} semantic siblings** • Total shared: ${totalSharedConnections} connections • Avg. similarity: ${avgSimilarity}%`);
  } catch (e) {
    console.warn("Error calculating sibling statistics:", e);
    dv.paragraph(`**Found ${siblings.length} semantic siblings**`);
  }
  
  dv.table(
    ["Note", "Similarity", "Strength", "Maturity", "Type", "Shared Context"], 
    siblings.map(s => [
      s.link, 
      `📊${s.similarityScore || 0}%`,
      "🔗" + (s.sharedCount || 0), 
      s.maturity === "evergreen" ? "🌳" + s.maturity : 
      s.maturity === "budding" ? "🌿" + s.maturity :
      s.maturity === "developing" ? "🌱" + s.maturity :
      s.maturity === "seedling" ? "大豆" + s.maturity : "❓unset",
      s.type || "unknown",
      s.sharedLinks?.slice(0, 2).map(l => l.displayName || l.path).join(", ") + ((s.sharedLinks?.length || 0) > 2 ? "…" : "") || ""
    ])
  );
} else {
  dv.paragraph("*No semantic siblings found. This note is unique in its connections.*");
}

// DOMAIN COVERAGE: Advanced domain analysis
const myTags = current.tags || [];
const primaryDomain = myTags.find(t => typeof t === "string" && t.includes("/"))?.split("/")[0] 
                   || myTags.find(t => typeof t === "string");

if (primaryDomain) {
  let domainNotes = [];
  try {
    domainNotes = dv.pages()
      .where(p => 
        p.tags && 
        Array.isArray(p.tags) && 
        p.tags.some(t => 
          typeof t === "string" && 
          (t.startsWith(primaryDomain) || t === primaryDomain)
        )
      );
  } catch (e) {
    console.warn("Error filtering domain notes:", e);
    domainNotes = [];
  }
   
  const maturityDistribution = {
    evergreen: domainNotes.filter(p => p.maturity === "evergreen").length,
    budding: domainNotes.filter(p => p.maturity === "budding").length,
    developing: domainNotes.filter(p => p.maturity === "developing").length,
    seedling: domainNotes.filter(p => p.maturity === "seedling").length,
    unset: domainNotes.filter(p => !p.maturity).length
  };

  // Advanced domain health metrics
  const totalNotes = domainNotes.length;
  const matureNotes = maturityDistribution.evergreen + maturityDistribution.budding;
  const coverage = totalNotes > 0 ? Math.round((matureNotes / totalNotes) * 100) : 0;
  
  // Domain activity score (based on recent modifications)
  const recentNotes = domainNotes.filter(p => {
    try {
      const daysOld = (new Date() - new Date(p.file.mtime)) / (1000 * 60 * 60 * 24);
      return daysOld < 30;
    } catch (e) {
      return false;
    }
  }).length;
  const activityScore = totalNotes > 0 ? Math.round((recentNotes / totalNotes) * 100) : 0;

  dv.header(3, `📂 Domain Analysis: ${primaryDomain}`);
  dv.paragraph(`**Total notes**: ${totalNotes} | **Recent activity**: ${activityScore}% (30d)`);
  dv.paragraph(`**Maturity breakdown**: 🌳${maturityDistribution.evergreen} | 🌿${maturityDistribution.budding} | 🌱${maturityDistribution.developing} | 🌰${maturityDistribution.seedling} | ❓${maturityDistribution.unset}`);
  dv.paragraph(`**Domain health**: ${coverage}% mature (evergreen + budding)`);
  
  // Domain health indicator
  const healthIndicator = coverage >= 80 ? "🟢 Excellent" : 
                         coverage >= 60 ? "🟡 Good" : 
                         coverage >= 40 ? "🟠 Fair" : "🔴 Poor";
  dv.paragraph(`**Health status**: ${healthIndicator}`);
}

// NETWORK INTELLIGENCE: Advanced connectivity analysis
const inlinks = current.file.inlinks || [];
const outlinks = current.file.outlinks || [];

dv.header(3, "🕸️ Network Intelligence");
const networkMetrics = [
  ["**Metric**", "**Value**", "**Insight**"],
  ["In-links", inlinks.length, inlinks.length > 10 ? "⚡ Hub" : inlinks.length > 0 ? "🌱 Node" : "🕸️ Orphan"],
  ["Out-links", outlinks.length, outlinks.length > 15 ? "🗺️ Explorer" : outlinks.length > 5 ? "🧭 Navigator" : "🎯 Focused"],
  ["Link Ratio", outlinks.length > 0 ? (inlinks.length / outlinks.length).toFixed(1) : "∞", 
   outlinks.length > 0 && inlinks.length / outlinks.length > 2 ? "📈 High authority" : "📊 Balanced"]
];

dv.table(networkMetrics[0], networkMetrics.slice(1));

// TEMPORAL ANALYSIS: Content aging and review patterns
dv.header(3, "⏰ Temporal Intelligence");
try {
  const created = current.file.ctime;
  const modified = current.file.mtime;
  const ageDays = Math.floor((new Date() - new Date(created)) / (1000 * 60 * 60 * 24));
  const stalenessDays = Math.floor((new Date() - new Date(modified)) / (1000 * 60 * 60 * 24));

  const reviewInsights = [];
  if (current["review-count"] > 5) reviewInsights.push("🔁 Well-reviewed");
  if (stalenessDays > 180) reviewInsights.push("⏰ Needs refresh");
  if (ageDays < 30) reviewInsights.push("🆕 New content");

  dv.paragraph(`**Age**: ${ageDays} days | **Staleness**: ${stalenessDays} days`);
  dv.paragraph(`**Review status**: ${current["review-count"] || 0} reviews | ${reviewInsights.join(" • ") || "📝 Standard"}`);
} catch (e) {
  console.warn("Error in temporal analysis:", e);
  dv.paragraph("*Temporal analysis unavailable*");
}
```
> [!abstract] ### 🏷️ Tag Intelligence
> **Tag Count**: `= length(this.tags)` | **Unique Domains**: `= length(filter(this.tags, (t) => contains(t, "/")))` hierarchical tags
> **Tag Density**: `= choice(length(this.tags) < 3, "⚠️Sparse", choice(length(this.tags) > 10, "📚Rich", "✅Balanced"))`
> > 
> > ---
> 
> ```dataviewjs
> // TAG CO-OCCURRENCE: Find notes sharing the most tags with this note
> const current = dv.current();
> 
> // Safely get tags from current note
> let myTags = [];
> if (current.tags) {
>     if (Array.isArray(current.tags)) {
>         myTags = current.tags;
>     } else if (typeof current.tags === 'string') {
>         myTags = [current.tags];
>     }
> }
> 
> if (myTags.length > 0) {
>     const tagSiblings = dv.pages()
>         .where(p => p.file.path !== current.file.path)
>         .where(p => {
>             // Safely check if page has tags
>             if (!p.tags) return false;
>             // Convert tags to array if needed
>             let pageTags = [];
>             if (Array.isArray(p.tags)) {
>                 pageTags = p.tags;
>             } else if (typeof p.tags === 'string') {
>                 pageTags = [p.tags];
>             }
>             return pageTags.length > 0;
>         })
>         .map(p => {
>             // Safely convert page tags to array
>             let pageTags = [];
>             if (p.tags) {
>                 if (Array.isArray(p.tags)) {
>                     pageTags = p.tags;
>                 } else if (typeof p.tags === 'string') {
>                     pageTags = [p.tags];
>                 }
>             }
>             
>             // Find shared tags
>             const sharedTags = pageTags.filter(t => {
>                 if (typeof t === 'string') {
>                     return myTags.includes(t);
>                 } else if (t && typeof t === 'object' && t.path) {
>                     // Handle tag objects
>                     return myTags.some(myTag => {
>                         if (typeof myTag === 'string') {
>                             return myTag === t.path;
>                         }
>                         return false;
>                     });
>                 }
>                 return false;
>             });
>             
>             return {
>                 link: p.file.link,
>                 sharedCount: sharedTags.length,
>                 sharedTags: sharedTags,
>                 totalTags: pageTags.length
>             };
>         })
>         .where(p => p.sharedCount >= 2) // At least 2 shared tags
>         .sort(p => p.sharedCount, "desc")
>         .limit(5);
> 
>     if (tagSiblings.length > 0) {
>         dv.header(5, "🏷️ Tag Siblings (Shared Taxonomy)");
>         dv.table(
>             ["Note", "Overlap", "Shared Tags"],
>             tagSiblings.map(s => {
>                 // Safely extract tag names for display
>                 let displayTags = s.sharedTags.map(t => {
>                     if (typeof t === 'string') {
>                         return t;
>                     } else if (t && typeof t === 'object' && t.path) {
>                         return t.path;
>                     }
>                     return String(t);
>                 });
>                 
>                 return [
>                     s.link,
>                     s.sharedCount + "/" + s.totalTags,
>                     displayTags.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
>                 ];
>             })
>         );
>     } else {
>         dv.paragraph("*No tag siblings with 2+ shared tags found.*");
>     }
> } else {
>     dv.paragraph("*No tags on this note to analyze.*");
> }
> ```

---

##### Comprehensive Reference: Metadata Menu

> [! ] ### Claude Thinking
> The user is requesting a comprehensive reference note on the Obsidian plugin "Metadata Menu" with specific focus on:
> 1. Setup configuration for their metadata system
> 2. Skillful operation and usage
> **Request Classification:**
> - Type: comprehensive_note
> - Scope: reference
> - Research Required: YES - This is a specific technical plugin that requires current documentation and best practices
> **Research Trigger Criteria Assessment:**
> ✓ Topic involves a specific software tool that may have updates post-January 2025
> ✓ User needs accurate technical documentation
> ✓ Complex synthesis requires authoritative sources for proper implementation guidance
> **Initial Scope Mapping:**
> The topic "Metadata Menu Plugin for Obsidian" encompasses these major domains:
> - Primary domain: Obsidian plugin ecosystem, metadata management
> - Adjacent domains: Dataview integration, YAML frontmatter, properties system, workflow automation
> - Depth requirement: High complexity - requires technical setup instructions, configuration patterns, advanced features
> **Systematic Web Research Phase:**
> I need to execute multiple searches to gather comprehensive information:
> 1. **QUERY RATIONALE**: Search for official Metadata Menu documentation
>    **EXPECTED INSIGHT**: Core functionality, installation, basic configuration
> 2. **QUERY RATIONALE**: Search for Metadata Menu advanced features and configuration
>    **EXPECTED INSIGHT**: Field types, presets, file classes, advanced workflows
> 3. **QUERY RATIONALE**: Search for Metadata Menu integration with Dataview
>    **EXPECTED INSIGHT**: How these systems work together for querying
> 4. **QUERY RATIONALE**: Search for Metadata Menu best practices and examples
>    **EXPECTED INSIGHT**: Real-world usage patterns, optimization strategies
> 5. **QUERY RATIONALE**: Search for Metadata Menu recent updates or changes
>    **EXPECTED INSIGHT**: Current version features, any breaking changes
> **Structural Planning:**
> STRUCTURAL REASONING:
> ├── Core Concept Architecture
> │   ├── Why this structure? Plugin documentation requires: conceptual foundation → installation → configuration → usage → advanced features
> │   └── Information flow logic: Build from understanding what it does → how to set it up → how to use it → how to master it
> ├── Hierarchy Decisions
> │   ├── Primary sections: 
> │   │   1. Overview & Concepts (what it is, why use it)
> │   │   2. Installation & Initial Setup
> │   │   3. Metadata System Architecture (field types, file classes, presets)
> │   │   4. Configuration Patterns (YAML settings, UI configuration)
> │   │   5. Operational Usage (day-to-day workflows)
> │   │   6. Advanced Features (automation, integration, power user techniques)
> │   │   7. Troubleshooting & Optimization
> │   └── Subsection depth: 3-4 levels deep where needed for technical specifications
> └── Cross-referencing Strategy
>     └── Internal link opportunities: 
>         - [[Dataview]], [[YAML]], [[Obsidian Properties]]
>         - [[Templater]], [[QuickAdd]] (for workflow integration)
>         - [[Personal Knowledge Management]], [[Zettelkasten]]
>         - [[Inline Fields]], [[Metadata Schema]]
> Now I'll execute the research phase.
> Now I have sufficient research to create a comprehensive reference note. Let me proceed with the response following the structure outlined in the thinking phase.

---
tags: #obsidian #metadata-management #plugin #dataview-integration #pkm #reference-note
aliases: [Metadata Menu Plugin, MM Plugin, Obsidian Metadata Manager, FileClass System]
---

> [!comprehensive-reference] 📚 Comprehensive Reference
> - **Generated**: 2024-12-14
> - **Version**: 1.0
> - **Type**: Reference Documentation

> [!abstract]
> **Executive Overview**
> <span style='color: #FFC700;'>**Metadata Menu**</span> is a powerful [[Obsidian]] [[Community Plugin]] designed for <span style='color: #27FF00;'>data quality enthusiasts who need systematic, typed metadata management across their vault</span>. Unlike Obsidian's native [[Properties]] system, Metadata Menu provides comprehensive field typing, validation, autocompletion, contextual editing via multiple access points, and seamless integration with [[Dataview]] for creating editable database-style tables. The plugin bridges the gap between flexible inline [[Dataview Syntax|field notation]] (`field:: value`) and structured [[YAML Frontmatter]] properties, enabling users to transform their [[Personal Knowledge Base|PKB]] into a <span style='background-color: #72FFF140; color: #72FFF1;'>queryable, maintainable database with enforced data schemas</span>.

> [!how-to-use-this]
> **Navigation Guide**
> This reference note is organized into 9 major sections covering installation, configuration, field architecture, fileClass systems, operational workflows, [[DataviewJS]] integration, API usage, and advanced optimization strategies. Use the table of contents below for quick navigation to specific topics, or search for technical terms using [[Wiki-Links]]. Code examples are provided throughout with actual syntax you can copy directly into your vault.

## 📑 Table of Contents

1. [[#🎯 Core Concepts & Architecture]]
2. [[#⚙️ Installation & Initial Setup]]
3. [[#🏗️ Field Types & Definitions]]
4. [[#📁 FileClass System Architecture]]
5. [[#🎮 Operational Controls & Access Points]]
6. [[#🔗 Dataview Integration & Editable Tables]]
7. [[#🛠️ API Usage & Programmatic Control]]
8. [[#🚀 Advanced Features & Workflows]]
9. [[#🔧 Troubleshooting & Optimization]]

---

## 1️⃣ Core Concepts & Architecture

> [!definition]
> - **Metadata-Menu**:: <span style='color: #27FF00;'>An Obsidian community plugin that adds typed field definitions, validation, autocompletion, and contextual editing capabilities to both YAML frontmatter properties and Dataview-style inline fields</span>
> - **Field-Definition**:: <span style='color: #27FF00;'>A configuration specifying a field's name, type (Input, Boolean, Number, Select, Date, etc.), validation rules, and display options—enabling consistent data entry across files</span>
> - **FileClass**:: <span style='color: #27FF00;'>A special note that acts as a metadata schema template, defining field configurations applicable to groups of files based on frontmatter attributes, tags, paths, or Dataview queries</span>

### Foundational Understanding

<span style='color: #FFC700;'>**Metadata Menu**</span> operates on the principle that [[Personal Knowledge Management]] systems benefit from <span style='color: #27FF00;'>structured, validated metadata rather than freeform text fields</span>. The plugin recognizes that while [[Obsidian]] allows arbitrary [[YAML]] properties and [[Dataview]] enables `field:: value` notation anywhere in notes, neither system enforces types, validates input, or provides sophisticated editing interfaces.

[**Core-Philosophy**:: Metadata Menu treats your vault as a distributed database where each note is a record, fields are columns with schemas, and fileClasses are table definitions—enabling database-style operations while preserving Markdown flexibility.]

The plugin introduces three fundamental concepts that work in concert:

**1. Field Definitions** specify <span style='color: #72FFF1;'>data types</span> (18 available types from simple Input to complex Object Lists), <span style='color: #72FFF1;'>validation rules</span> (min/max for numbers, allowed values for Select fields), and <span style='color: #72FFF1;'>display preferences</span> (array vs. indented list format). These can be defined globally (applying vault-wide) or contextually (through [[#📁 FileClass System Architecture|fileClasses]]).

**2. FileClasses** act as <span style='background-color: #FFC70040; color: #FFC700;'>metadata schemas or templates</span> that automatically apply field definitions to files matching specific criteria. Think of them as "note types" or "document classes"—you might have a `meeting` fileClass with fields for `attendees`, `agenda`, `action-items`, and a `book` fileClass with `author`, `genre`, `rating`, `read-date`.

**3. Control Mechanisms** provide multiple access points for editing metadata: [[#🎮 Operational Controls & Access Points|autocompletion]] during typing, [[Context Menu]] options when right-clicking, dedicated [[Command Palette]] commands, a <span style='color: #72FFF1;'>Metadata Menu button</span> that appears in various UI locations, and most powerfully, <span style='color: #72FFF1;'>inline controls within Dataview tables</span> via the [[#🔗 Dataview Integration & Editable Tables|fieldModifier API]].

> [!key-claim]
> **Central Principle**
> Metadata Menu transforms Obsidian from a flexible but unstructured note-taking app into a <span style='color: #27FF00;'>type-safe, schema-aware knowledge database</span> while maintaining full Markdown compatibility. Every field can be edited through multiple interfaces, validated against defined constraints, and queried programmatically through Dataview—creating a best-of-both-worlds system that combines database rigor with Markdown flexibility.

### Metadata Menu vs. Native Properties

| Feature | Obsidian Properties | Metadata Menu |
|---------|---------------------|---------------|
| **Field Types** | Limited (text, date, number, checkbox, list, alias, tags) | 18+ types including Select, Multi, Cycle, File, Object, Lookup, Formula, Canvas-aware |
| **Validation** | Minimal (type-based only) | <span style='color: #72FFF1;'>Comprehensive: min/max ranges, allowed values, Dataview queries for suggestions</span> |
| **Inline Fields** | ❌ No support | ✅ Full support for `field:: value` anywhere in note |
| **Contextual Schemas** | ❌ Global only | ✅ FileClass-based schemas with inheritance |
| **Editing Interfaces** | Properties panel only | <span style='color: #27FF00;'>Context menus, command palette, modal dialogs, Dataview table controls</span> |
| **Autocompletion** | Basic | <span style='color: #72FFF1;'>Advanced with preset suggestions based on field type</span> |
| **Dataview Integration** | Read-only | <span style='background-color: #27FF0040; color: #27FF00;'>Bi-directional: query AND edit within tables</span> |

> [!important]
> **Compatibility Note**
> Metadata Menu works alongside Obsidian's native Properties system (introduced in v1.4). The plugin reads and writes standard YAML frontmatter, so properties created with Metadata Menu are fully compatible with Obsidian's Properties panel and vice versa. However, Metadata Menu's advanced features (type validation, fileClass schemas, inline field support) only work when fields are defined within the plugin's settings.

### Metadata Location Support

Metadata Menu manages fields in two locations:

**Frontmatter (YAML) Properties:**
```yaml
---
status: in-progress
priority: 3
due-date: 2024-12-20
tags: [project, work]
fileClass: meeting-note
---
```

**Inline Fields (Dataview Syntax):**
```markdown
This project is currently [status:: in-progress] and has a 
priority:: 3 rating.

The deadline is (due-date:: 2024-12-20).
```

<span style='color: #FF00DC;'>⚠️ **Critical Distinction**</span>: Inline fields offer flexibility for context-specific metadata (e.g., marking a specific paragraph's timestamp), while frontmatter works better for document-level properties. Metadata Menu treats both equally, but <span style='color: #72FFF1;'>Dataview queries perform faster on frontmatter fields</span> due to caching.

---

## 2️⃣ Installation & Initial Setup

> [!methodology-and-sources]
> **Installation Process**
> Metadata Menu is installed like any [[Community Plugin]]. The setup phase focuses on configuring global settings, establishing your fileClass folder structure, and defining your first field schemas.

### Step 1: Plugin Installation

1. Open Obsidian Settings → **Community Plugins**
2. Ensure "Restricted Mode" is **OFF**
3. Click **Browse** and search for "Metadata Menu"
4. Click **Install** then **Enable**
5. <span style='color: #27FF00;'>✓ Verified:</span> Plugin button appears in left ribbon (customizable icon)

### Step 2: Essential Plugin Configuration

Navigate to Settings → Metadata Menu to configure core behaviors:

**Global Settings Section:**

| Setting | Recommended Value | Purpose |
|---------|------------------|---------|
| **Class Files Path** | `99_system/fileclasses/` | <span style='color: #72FFF1;'>Folder where fileClass definition notes are stored</span> |
| **FileClass Attribute Name** | `fileClass` (default) | Frontmatter key used to assign files to classes |
| **Show Metadata Menu Button** | ✅ Enable in: File Explorer, Tab Headers, Backlinks | Provides quick access to field modal |
| **Context Menu Display** | "Field Options" (modal) | <span style='color: #9E6CD3;'>Reduces menu clutter by grouping options</span> |
| **Frontmatter Display** | Arrays (not indented lists) | Better compatibility with Obsidian Properties |
| **Field Autocompletion** | ✅ Enabled globally | Triggers suggestions when typing `:` after field names |
| **First Day of Week** | Monday (adjust to preference) | Affects Date field picker |

> [!helpful-tip]
> **Folder Exclusions**
> Use the "Exclude folders from indexing" setting to prevent Metadata Menu from processing template folders, archive folders, or attachment directories. This significantly improves performance in large vaults. Use regex patterns like `^(templates|archive|attachments)/` to exclude multiple paths.

**Preset Fields Settings:**

This is where you define <span style='color: #FFC700;'>global field definitions</span> that apply vault-wide (unless overridden by fileClass-specific definitions).

**Example: Creating a Global "Priority" Field**

1. Click **"Add New"** in Preset Fields Settings
2. Configure:
   - **Field Name**: `priority`
   - **Field Type**: `Number`
   - **Min Value**: `0`
   - **Max Value**: `10`
   - **Step**: `1`
   - **Command**: ✅ Enabled (allows hotkey assignment)
3. Click **Save**

<span style='color: #27FF00;'>✓ Result:</span> The `priority` field is now available in every note via autocompletion, context menu, and can be inserted via Command Palette.

### Step 3: FileClass Folder Structure

[**FileClass-Folder-Organization**:: Best practice is to create a dedicated folder outside your main content areas to store fileClass definition notes, preventing them from appearing in general searches while remaining accessible for schema management.]

**Recommended Structure:**
```
99_system/
└── fileclasses/
    ├── _core/           # Base classes
    │   ├── note.md
    │   └── document.md
    ├── content/         # Content-type classes  
    │   ├── article.md
    │   ├── book.md
    │   └── video.md
    ├── workflow/        # Process-oriented classes
    │   ├── meeting.md
    │   ├── project.md
    │   └── task.md
    └── reference/       # Reference material classes
        ├── person.md
        └── company.md
```

<span style='color: #FF00DC;'>⚠️ **Trailing Slash Requirement**</span>: When specifying the Class Files Path in settings, you <span style='color: #FF00DC;'>**MUST**</span> include the trailing slash: `99_system/fileclasses/` (not `99_system/fileclasses`). Omitting it will cause fileClass detection to fail silently.

### Step 4: Enabling Dataview Integration

For [[#🔗 Dataview Integration & Editable Tables|editable Dataview tables]], you must enable JavaScript execution:

1. Install the **Dataview** plugin (if not already installed)
2. Open Dataview settings
3. Enable **"Enable JavaScript Queries"**
4. Enable **"Enable Inline JavaScript Queries"**

<span style='color: #27FF00;'>✓ Prerequisite Complete:</span> You can now use `fieldModifier` API in DataviewJS blocks.

---

## 3️⃣ Field Types & Definitions

> [!definition]
> - **Field-Type**:: <span style='color: #27FF00;'>The data structure and validation rules applied to a metadata field—determines what values are allowed, how they're displayed, and what editing controls are available</span>
> - **Preset-Field**:: <span style='color: #27FF00;'>A global field definition configured in plugin settings, available in all notes regardless of fileClass assignment</span>
> - **Nested-Field**:: <span style='color: #27FF00;'>A field that exists as a child of an Object or ObjectList parent, enabling hierarchical data structures within metadata</span>

### Complete Field Type Taxonomy

Metadata Menu supports <span style='color: #72FFF1;'>18 distinct field types</span>, each with specific use cases and configuration options:

#### Basic Input Types

| Type | Description | Use Case | Validation Options |
|------|-------------|----------|-------------------|
| **Input** | <span style='color: #72FFF1;'>Free text (default type)</span> | General text, notes, descriptions | Template patterns with `{placeholder}` |
| **Boolean** | True/false/null | Checkboxes, flags, completion status | None |
| **Number** | Integer or float | Ratings, counts, scores, quantities | <span style='color: #72FFF1;'>Min, Max, Step (increment)</span> |
| **Date** | Calendar date | Deadlines, creation dates, events | <span style='color: #72FFF1;'>Insert as link vs. plain text, shift intervals</span> |

**Input Field Templates:**

<span style='color: #FFC700;'>Input fields</span> support template patterns where text in `{curly braces}` becomes an input prompt or dropdown:

```yaml
# Field definition with template:
`template: "Project: {project_name} - Status: {active|pending|completed}"`

# Creates modal with:
# - Text input for "project_name"  
# - Dropdown for Status with 3 options
```

#### Selection & Enumeration Types

| Type       | Description                                                              | Behavior                         | Configuration                                 |
| ---------- | ------------------------------------------------------------------------ | -------------------------------- | --------------------------------------------- |
| **Select** | <span style='color: #72FFF1;'>Single choice from predefined list</span>  | Dropdown suggester               | Define values list in settings                |
| **Multi**  | <span style='color: #72FFF1;'>Multiple choices from list</span>          | Checkbox selection modal         | Values list + display format (array/indented) |
| **Cycle**  | <span style='color: #72FFF1;'>Rotates through values sequentially</span> | Each edit advances to next value | Ordered values list (loops back to first)     |

**Example Select Field Configuration:**
```yaml
# In fileClass or Preset Fields:
Field Name: status
Type: Select
Values: 
  - not-started
  - in-progress
  - blocked
  - completed
  - archived
```

> [!helpful-tip]
> **Cycle Fields for Status Workflows**
> Use <span style='color: #72FFF1;'>Cycle fields</span> for linear progressions like `draft → review → final` or `todo → doing → done`. Each click advances to the next stage. Perfect for [[Kanban]]-style workflows or [[GTD]] status tracking.

#### File & Link Types

| Type | Description | Linking Behavior | Query Support |
|------|-------------|-----------------|---------------|
| **File** | <span style='color: #72FFF1;'>Single file link from vault</span> | Creates `[[wikilink]]` | <span style='color: #27FF00;'>✅ Dataview query filters available files</span> |
| **MultiFile** | <span style='color: #72FFF1;'>Multiple file links</span> | Array of `[[links]]` | <span style='color: #27FF00;'>✅ Dataview query filters suggestions</span> |
| **Media** | <span style='color: #72FFF1;'>Image or video file</span> | Displays preview inline | File type restrictions |
| **MultiMedia** | <span style='color: #72FFF1;'>Multiple media files</span> | Gallery-style display | File type restrictions |

**Advanced File Field with Dataview Query:**

<span style='color: #FFC700;'>File and MultiFile</span> fields can restrict suggestions to files matching a [[Dataview]] query:

```javascript
// In field settings → Dataview Query:
dv.pages('"reference/people"').where(p => p.role === "engineer")

// Only suggests files from reference/people folder where role = engineer
// Enables "typed" links that enforce schema relationships
```

[**Dataview-Query-Filtering**:: File-type fields support embedding dv.pages() queries that dynamically filter which files appear in the suggestion dropdown, enabling schema-enforced relationships like "only link to Person notes" or "only link to active Projects".]

#### Computational & Dynamic Types

| Type | Description | Update Behavior | Typical Use |
|------|-------------|----------------|-------------|
| **Lookup** | <span style='color: #72FFF1;'>Queries vault and aggregates results</span> | Auto or manual | <span style='color: #27FF00;'>Count related notes, sum values, collect links</span> |
| **Formula** | <span style='color: #72FFF1;'>JavaScript calculation</span> | Auto or manual | Computed fields based on other metadata |
| **Canvas** | <span style='color: #72FFF1;'>Tracks connections in Canvas</span> | Auto-updates on canvas changes | <span style='color: #27FF00;'>Visual relationship mapping</span> |
| **Canvas Group** | <span style='color: #72FFF1;'>Canvas group membership</span> | Auto-updates | Group-based categorization |
| **Canvas Group Link** | <span style='color: #72FFF1;'>Files linked to canvas groups</span> | Auto-updates | Combined canvas + link tracking |

**Lookup Field Example:**

<span style='background-color: #72FFF140; color: #72FFF1;'>Lookup fields</span> enable advanced aggregations without writing Dataview queries:

```yaml
# Lookup field configuration:
Field Name: total-project-tasks
Type: Lookup
Query: dv.pages('#task').where(p => p.project === current.file.name)
Output: Count All

# Result: Automatically counts all task notes linked to this project
# Updates when tasks are added/removed (if auto-update enabled)
```

> [!warning]
> **Performance Impact of Auto-Update**
> Lookup and Formula fields with <span style='color: #FF00DC;'>auto-update enabled</span> can significantly slow Obsidian if you have many such fields across hundreds of notes. For large vaults (>1000 notes), prefer <span style='color: #27FF00;'>manual update</span> triggered via Command Palette: `Metadata Menu: Update lookup fields`.

#### Structural Types (Nesting & Hierarchies)

| Type | Description | Nesting Capability | Use Case |
|------|-------------|-------------------|----------|
| **Object** | <span style='color: #72FFF1;'>Container for child fields</span> | <span style='color: #27FF00;'>✅ Infinite depth supported</span> | Group related fields (e.g., Contact Info) |
| **ObjectList** | <span style='color: #72FFF1;'>Array of Objects (repeater)</span> | <span style='color: #27FF00;'>✅ Nested Objects allowed</span> | Multiple instances (e.g., list of employees) |

**Object and ObjectList Field Hierarchy:**

These enable <span style='background-color: #FFC70040; color: #FFC700;'>complex, nested data structures</span> within frontmatter:

```yaml
---
# ObjectList example: Multiple employees
Employees:
  - Name: John Doe         # Input field (child of Employees)
    Role: CFO              # Select field (child of Employees)
    Contact Info:          # Object field (child of Employees)
      email: john@acme.co  # Input field (child of Contact Info)
      phone: 555-0101      # Input field (child of Contact Info)
  - Name: Jane Smith
    Role: CEO
    Contact Info:
      email: jane@acme.co
      phone: 555-0102
---
```

[**Object-Nesting**:: Object and ObjectList fields support infinite depth nesting—you can have ObjectLists containing Objects that themselves contain ObjectLists, enabling arbitrarily complex data hierarchies while maintaining full Metadata Menu editing capabilities at every level.]

> [!key-claim]
> **Nesting Limitations**
> While Object/ObjectList support infinite depth, <span style='color: #FF00DC;'>Lookup, Formula, Canvas, Canvas Group, and Canvas Group Link fields CANNOT be nested</span>. They must exist at the root level or directly under a single Object parent (not within ObjectLists).

#### Specialized Types

| Type | Description | Availability | Notes |
|------|-------------|--------------|-------|
| **JSON** | <span style='color: #72FFF1;'>Free-form JSON data</span> | Frontmatter + inline | <span style='color: #9E6CD3;'>Serialized for inline fields</span> |
| **YAML** | <span style='color: #72FFF1;'>Free-form YAML data</span> | Frontmatter only | Raw YAML block |

---

### Field Definition Workflow

**Creating a Field Definition (Preset or FileClass):**

1. Navigate to Settings → Metadata Menu → Preset Fields Settings **OR** open a fileClass note and click the button → Fields tab
2. Click **"+ Add New"**
3. Configure field properties:

| Property | Purpose | Required |
|----------|---------|----------|
| **Field Name** | <span style='color: #72FFF1;'>Identifier (case-sensitive)</span> | ✅ Yes |
| **Type** | Select from 18 types | ✅ Yes |
| **Parent** | For nesting under Object/ObjectList | Optional |
| **Values** | For Select/Multi/Cycle types | Type-dependent |
| **Min/Max/Step** | For Number type | Type-dependent |
| **Dataview Query** | For File/Lookup types | Optional |
| **Command Palette** | Enable hotkey assignment | Optional |
| **Icon** | Lucide icon name for button | Optional |

4. Click **Save**

> [!methodology-and-sources]
> **Field Name Uniqueness**
> Field names must be <span style='color: #FF00DC;'>unique per level within a fileClass or Preset Fields</span>. You can have a `status` field at root level AND a `status` field nested under an Object, but not two `status` fields at the same nesting level.

---

## 4️⃣ FileClass System Architecture

> [!definition]
> - **FileClass**:: <span style='color: #27FF00;'>A special note stored in the designated fileClass folder that defines a metadata schema (field types, validation rules) applicable to files matching specific mapping criteria</span>
> - **FileClass-Mapping**:: <span style='color: #27FF00;'>The process by which Metadata Menu determines which fileClass(es) apply to a given file, based on frontmatter values, tags, paths, bookmark groups, or Dataview queries</span>
> - **FileClass-Inheritance**:: <span style='color: #27FF00;'>A mechanism allowing one fileClass to extend another, inheriting its field definitions while adding or overriding specific fields</span>

### FileClass Fundamentals

A <span style='color: #FFC700;'>fileClass</span> is fundamentally a <span style='color: #27FF00;'>note that acts as a schema definition</span>. The frontmatter of this note contains the fileClass configuration and field definitions, while the note body can contain documentation about the class (ignored by the plugin).

**Anatomy of a FileClass Note:**

```yaml
---
# 99_system/fileclasses/meeting.md
# FileClass configuration (frontmatter)

# Optional: Inherit from another fileClass
extends: note

# Optional: Map by tag names
mapWithTag: true
tagNames: [meeting, standup]

# Optional: Map by folder path
path: [meetings/, work/meetings/]

# Optional: Map by bookmark group
bookmarkGroups: [Work Meetings, Team Standups]

# Optional: Custom button icon
icon: users

# Field definitions for this class
id: fileClass-meeting-v1

# Individual fields defined in UI, stored here
---

# Meeting Note Documentation

This fileClass is used for all meeting notes. It provides structured fields for:
- Attendees tracking
- Agenda items
- Action items with assignments
- Follow-up dates

## Usage
Assign to a note by adding `fileClass: meeting` to frontmatter.
```

### FileClass Mapping Methods

Files are associated with fileClasses through <span style='color: #72FFF1;'>seven mapping methods</span> (in priority order):

**Priority Order (highest to lowest):**

1. <span style='color: #FFC700;'>**Frontmatter Declaration**</span> (highest priority)
2. <span style='color: #72FFF1;'>**Tag Match**</span>
3. <span style='color: #72FFF1;'>**Path Match**</span>
4. <span style='color: #72FFF1;'>**Bookmark Group Match**</span>
5. <span style='color: #72FFF1;'>**FileClass Query Match**</span>
6. <span style='color: #9E6CD3;'>**Global FileClass**</span>
7. <span style='color: #9E6CD3;'>**Preset Fields**</span> (lowest priority)

#### Method 1: Frontmatter Declaration

**Most Explicit Method:**

```yaml
---
fileClass: meeting
---
```

For multiple fileClasses:
```yaml
---
fileClass: 
  - meeting
  - project-related
---
```

For nested fileClasses (stored in subfolders):
```yaml
---
fileClass: work/meeting-note
---
# Maps to: 99_system/fileclasses/work/meeting-note.md
```

#### Method 2: Tag-Based Mapping

**Enable in fileClass frontmatter:**

```yaml
---
# In fileClass note
mapWithTag: true
tagNames: [meeting, standup, retrospective]
---
```

**Effect:** Any note containing `#meeting`, `#standup`, or `#retrospective` automatically inherits this fileClass's fields.

<span style='color: #27FF00;'>✓ Use Case:</span> Perfect for tagging-first workflows where tags define note types.

#### Method 3: Path-Based Mapping

**Automatic folder-based schema application:**

```yaml
---
# In fileClass note  
path: 
  - meetings/
  - work/meetings/
  - team/standups/
---
```

[**Path-Mapping-Behavior**:: All notes within the specified folders (and subfolders) automatically inherit this fileClass. Supports relative paths from vault root and partial path matching.]

<span style='color: #FF00DC;'>⚠️ **Trailing Slashes**</span>: Always include trailing slashes for folder paths to distinguish them from file name patterns.

#### Method 4: Bookmark Group Mapping

**Integrate with Obsidian's Bookmarks:**

```yaml
---
# In fileClass note
bookmarkGroups: 
  - Active Projects
  - Client Work
---
```

<span style='color: #27FF00;'>✓ Use Case:</span> Useful for curated collections where bookmarking implies membership in a semantic category.

#### Method 5: FileClass Query (Dataview-Based)

**Dynamic, query-driven mapping:**

Configured in **Plugin Settings** → FileClass Settings → Query Based FileClass Settings:

```javascript
// Query that returns files to map to "meeting" fileClass:
dv.pages('"work"').where(p => p.type === "meeting" || p.tags.includes("standup"))

// Associate with fileClass: meeting
```

<span style='background-color: #72FFF140; color: #72FFF1;'>Most powerful mapping method</span>—enables complex logic combining folder location, metadata values, and tag conditions. Recalculates automatically when files change.

#### Method 6: Global FileClass

**Vault-Wide Default Schema:**

Set in **Plugin Settings** → FileClass Settings → Global FileClass:

```
Global FileClass: _base-note
```

<span style='color: #9E6CD3;'>Every note in the vault</span> (that doesn't match a higher-priority mapping) inherits fields from this fileClass. Use for universal metadata like `created-date`, `modified-date`, `status`.

#### Method 7: Preset Fields (Fallback)

If no fileClass mappings apply, fields defined in **Preset Fields Settings** are available. These act as the ultimate fallback schema.

> [!key-claim]
> **Mapping Priority Logic**
> When multiple fileClasses map to the same file, <span style='color: #FF00DC;'>field definitions from higher-priority mappings override lower-priority ones</span>. If `meeting` fileClass (frontmatter) and `work-note` fileClass (tag) both define a `status` field with different types, the `meeting` definition wins. Fields unique to each class are merged—the file gets ALL fields from ALL mapped classes.

---

### FileClass Inheritance

<span style='color: #FFC700;'>FileClasses can extend other fileClasses</span>, inheriting all field definitions and settings:

**Example: Inheritance Hierarchy**

```yaml
# Base class: 99_system/fileclasses/note.md
---
# Fields: title, created, modified, status
---
```

```yaml
# Derived class: 99_system/fileclasses/meeting.md
---
extends: note
# Inherits: title, created, modified, status
# Adds: attendees, agenda, action-items
---
```

```yaml
# Further derived: 99_system/fileclasses/standup.md
---
extends: meeting  
# Inherits: title, created, modified, status, attendees, agenda, action-items
# Adds: blockers, sprint-goal
---
```

[**FileClass-Inheritance-Rules**:: Child fileClasses inherit ALL fields from parent classes. If a child redefines a field (same name), the child's definition overrides the parent's. The extends chain can be arbitrarily deep, enabling hierarchical schema taxonomies.]

**Excluding Parent Fields:**

```yaml
---
extends: note
excludedFields: [status, modified]  
# Inherits all fields from 'note' EXCEPT status and modified
---
```

---

### FileClass Management Interface

When viewing a fileClass note, a <span style='color: #72FFF1;'>special button appears</span> (customizable icon) that opens the **FileClass View**—a three-tab interface:

#### Tab 1: FileClass Table View

- <span style='color: #27FF00;'>Database-style table</span> showing all files mapped to this class
- Columns = Fields defined in fileClass
- <span style='color: #72FFF1;'>Editable cells</span>: Click to modify metadata directly
- <span style='color: #72FFF1;'>Filtering</span>: Type in column headers to filter rows
- <span style='color: #72FFF1;'>Sorting</span>: Click column headers (multi-column sorting supported)
- <span style='color: #72FFF1;'>Saved Views</span>: Store custom filter/sort configurations

**Bulk Operations:**
- Checkbox column for selecting multiple files
- Modify field values across selected files simultaneously
- Export view to CSV

#### Tab 2: FileClass Fields View

- <span style='color: #27FF00;'>Field definition editor</span> (same interface as Preset Fields)
- Add, edit, delete, reorder fields
- Configure field types, validation, options
- Changes apply to all files mapped to this fileClass

#### Tab 3: FileClass Settings View

Configure fileClass-specific behaviors:

| Setting | Options | Effect |
|---------|---------|--------|
| **Button Icon** | Lucide icon name | Customizes fileClass button appearance |
| **Max Table Rows** | Number (default 50) | Pagination in table view |
| **Extends** | FileClass name | Inheritance parent |
| **Excluded Fields** | Field names array | Exclude inherited fields |
| **Map With Tag** | Boolean | Enable tag-based mapping |
| **Tag Names** | Array of tags | Tags that trigger mapping |
| **Path** | Array of paths | Folders that trigger mapping |
| **Bookmark Groups** | Array of group names | Bookmark groups that trigger mapping |

---

### FileClass Best Practices

> [!methodology-and-sources]
> **FileClass Design Patterns**
> 1. **Inheritance Hierarchy**: Create a base `note` fileClass with universal fields, then derive specific classes
> 2. **Mapping Strategy**: Use frontmatter for explicit assignment, tags for workflows, paths for organizational structures
> 3. **Field Granularity**: Prefer specific fileClasses with focused field sets over one mega-class with dozens of optional fields
> 4. **Naming Convention**: Use descriptive, hyphenated names: `project-note`, `meeting-standup`, `person-contact`

**Example: Three-Tier Inheritance**

```
_base-note (Global FileClass)
├── created-date
├── modified-date  
└── status

content-note (extends: _base-note)
├── (inherited fields)
├── author
├── tags
└── summary

└── book-note (extends: content-note)
    ├── (inherited fields)
    ├── isbn
    ├── pages
    ├── rating
    └── read-date
```

---

## 5️⃣ Operational Controls & Access Points

> [!definition]
> - **Field-Control**:: <span style='color: #27FF00;'>An interactive UI element that allows viewing and modifying a metadata field's value, with behavior determined by the field type</span>
> - **Metadata-Menu-Button**:: <span style='color: #27FF00;'>A clickable icon that appears in various Obsidian interfaces (file explorer, tab headers, etc.) providing access to a note's full metadata modal</span>
> - **Field-Modal**:: <span style='color: #27FF00;'>A popup dialog displaying all defined fields for a note, organized by fileClass, with inline editing controls</span>

### Five Primary Control Mechanisms

Metadata Menu provides <span style='color: #FFC700;'>five complementary access points</span> for metadata editing:

#### 1. Autocompletion (During Typing)

**Frontmatter Autocompletion:**

```yaml
---
status:   # Type ":" to trigger suggester
```

**Inline Field Autocompletion:**

```markdown
This task is status::   # Type "::" to trigger suggester
[priority:: ]           # Bracketed inline field
(due-date:: )           # Parenthesized inline field
```

[**Autocompletion-Trigger**:: Metadata Menu's autocompletion activates when typing the field delimiter (: in frontmatter, :: for inline fields) and presents a filtered list of available fields based on current fileClass mappings plus global preset fields.]

<span style='color: #72FFF1;'>Field Type Behaviors:</span>
- **Select/Multi**: Dropdown with defined values
- **File/MultiFile**: File suggester (filtered by Dataview query if configured)
- **Date**: Calendar picker + natural language input
- **Number**: Numeric input with increment/decrement buttons
- **Boolean**: Checkbox toggle

> [!helpful-tip]
> **Disable Autocompletion Per-Field**
> If autocompletion interferes with your writing flow for certain fields, you can disable it globally (Plugin Settings → toggle off) or exclude specific fields (Settings → Excluded Fields from Context Menus).

---

#### 2. Context Menu (Right-Click)

**Multiple Context Entry Points:**

| Location | Access Method | Available Options |
|----------|--------------|-------------------|
| **Live Preview** | Right-click in editor | Add field at cursor, Manage field at cursor |
| **Link** | Right-click on `[[wikilink]]` | Modify linked note's metadata |
| **File Explorer** | Right-click on file | Access target file's metadata |
| **Tab Header** | Right-click on tab | Access open file's metadata |
| **Backlinks Pane** | Right-click on backlink | Access linked note's metadata |

**Context Menu Structure:**

```
📋 Metadata Menu
├── ➕ Add field at section
│   ├── Add on top of file
│   ├── Add at cursor position  
│   └── Add at bottom of file
├── 🔧 Manage field at cursor (if cursor on field)
├── 📝 Insert missing fields (bulk)
│   ├── All fileClasses
│   └── Per fileClass...
└── 🔗 FileClass: [name] (if mapped)
    ├── Open fileClass view
    └── Insert fileClass fields
```

> [!key-claim]
> **Contextual Metadata Editing**
> The context menu's power lies in <span style='color: #27FF00;'>editing ANY note's metadata without opening it</span>. Right-click a link in your current note → modify the linked note's fields → changes saved immediately. Essential for curating metadata across vault-wide collections.

---

#### 3. Command Palette

**Available Commands:**

| Command | Hotkey Assignable | Function |
|---------|------------------|----------|
| `Metadata Menu: Add field at cursor` | ✅ Yes | Insert field at current position |
| `Metadata Menu: Manage field at cursor` | ✅ Yes | Edit field under cursor |
| `Metadata Menu: Open note fields modal` | ✅ Yes | Full metadata modal |
| `Metadata Menu: Insert field [FIELD_NAME]` | ✅ Yes (per field) | <span style='color: #72FFF1;'>Insert specific field directly</span> |
| `Metadata Menu: Update lookup fields` | ✅ Yes | Refresh all non-auto Lookup fields |
| `Metadata Menu: Index metadata fields` | ❌ No | Force re-index (troubleshooting) |
| `Metadata Menu: Open fileClass view` | ✅ Yes | Access fileClass table/settings |

> [!helpful-tip]
> **Per-Field Command Hotkeys**
> Enable "Command Palette" in a field's definition settings to create a dedicated command for inserting that field. Assign hotkeys for frequently-used fields like `priority`, `status`, or `due-date` for keyboard-driven workflows.

**Example Hotkey Setup:**

```
Ctrl+Shift+P  →  Insert priority field
Ctrl+Shift+S  →  Insert status field  
Ctrl+Shift+D  →  Insert due-date field
```

---

#### 4. Metadata Menu Button

A <span style='color: #72FFF1;'>clickable button icon</span> appears in multiple locations (configurable):

**Button Locations:**
- 📂 **File Explorer**: Next to each file name
- 📑 **Tab Headers**: In tab bar for open files
- 🔗 **Backlinks Pane**: Next to each backlink
- 🔍 **Search Results**: Next to matching files
- ⭐ **Starred/Bookmarks**: Next to bookmarked items

**Button Action:** Opens the <span style='color: #FFC700;'>Note Fields Modal</span>—a comprehensive dialog displaying:

```
┌─────────────────────────────────────┐
│  📝 Note Title                      │
├─────────────────────────────────────┤
│  FileClass: meeting                 │ ← Click to change
├─────────────────────────────────────┤
│  📋 Existing Fields                 │
│  ├ status: in-progress              │ ← Click to edit
│  ├ priority: 3                      │
│  └ due-date: 2024-12-20             │
├─────────────────────────────────────┤
│  ➕ Missing Fields                  │ ← Click to insert
│  ├ attendees (not set)              │
│  └ action-items (not set)           │
├─────────────────────────────────────┤
│  🔧 Bulk Actions                    │
│  └ Insert all missing fields        │
└─────────────────────────────────────┘
```

[**Note-Fields-Modal**:: The centralized metadata management interface that displays all fields defined by a note's fileClass(es) plus global preset fields, organized into existing (with current values) and missing (available for insertion) sections, with inline editing controls for each field type.]

**Customization:**

```yaml
# In fileClass frontmatter
icon: calendar  # Use different icon per fileClass
```

Icon names from <span style='color: #72FFF1;'>https://lucide.dev</span> library.

---

#### 5. Dataview Table Controls (Advanced)

Covered comprehensively in [[#🔗 Dataview Integration & Editable Tables]].

**Preview:**

<span style='background-color: #72FFF140; color: #72FFF1;'>The most powerful control mechanism</span>—enables editing metadata directly within Dataview query results, transforming read-only tables into interactive databases.

```dataviewj
const {fieldModifier: f} = MetadataMenu.api;

dv.table(["File", "Status", "Priority"],
  dv.pages("#project").map(p => [
    p.file.link,
    f(dv, p, "status"),      // ← Editable dropdown
    f(dv, p, "priority")     // ← Editable number field
  ])
);
```

---

### Field Editing Behaviors by Type

Different field types produce different editing interfaces:

| Field Type | Control Appearance | Interaction |
|------------|-------------------|-------------|
| **Input** | Text input box | Type freely |
| **Boolean** | Checkbox | Click to toggle |
| **Number** | Number input with +/- buttons | Type or click increment |
| **Select** | Dropdown menu | Click to select |
| **Multi** | Checkbox list modal | Select multiple, confirm |
| **Cycle** | Button with current value | <span style='color: #72FFF1;'>Click to advance to next</span> |
| **Date** | Calendar picker + text input | Choose date or type natural language |
| **File** | File suggester modal | Search and select from vault |
| **MultiFile** | File suggester (multi-select) | Search, select multiple, confirm |
| **Lookup** | <span style='color: #9E6CD3;'>Display only + Update button</span> | Click "Update" if not auto-updating |
| **Formula** | <span style='color: #9E6CD3;'>Display only + Update button</span> | Click "Update" if not auto-updating |

> [!warning]
> **Lookup and Formula Field Manual Updates**
> If auto-update is disabled for <span style='color: #FF00DC;'>Lookup or Formula fields</span>, you MUST manually trigger updates via:
> 1. Command Palette: `Metadata Menu: Update lookup fields`
> 2. Click "Update" button in Note Fields Modal
> 3. Right-click field → "Update lookup field"
> 
> Otherwise, values remain stale even if underlying data changes.

---

## 6️⃣ Dataview Integration & Editable Tables

> [!definition]
> - **FieldModifier-API**:: <span style='color: #27FF00;'>A JavaScript function provided by Metadata Menu that wraps field values with interactive editing controls when embedded in DataviewJS table cells</span>
> - **Editable-Dataview-Table**:: <span style='color: #27FF00;'>A Dataview table created with DataviewJS that uses the fieldModifier API to render field values as interactive UI controls rather than static text</span>

### Core Concept: From Read-Only to Interactive

<span style='color: #FFC700;'>Standard Dataview tables</span> display metadata but cannot modify it:

```datavie
TABLE status, priority, due-date
FROM #project
SORT priority DESC
```

<span style='color: #27FF00;'>Result:</span> Static table—click cells does nothing.

<span style='color: #FFC700;'>Metadata Menu-enhanced DataviewJS tables</span> make fields editable:

```dataviewj
const {fieldModifier: f} = MetadataMenu.api;

dv.table(["File", "Status", "Priority", "Due Date"],
  await Promise.all(
    dv.pages("#project")
      .sort(p => p.priority, 'desc')
      .map(async p => [
        p.file.link,
        await f(dv, p, "status"),
        await f(dv, p, "priority"),
        await f(dv, p, "due-date")
      ])
  )
);
```

<span style='color: #27FF00;'>Result:</span> <span style='background-color: #27FF0040; color: #27FF00;'>Fully interactive table</span> with dropdowns, number spinners, date pickers—click to edit, changes save to frontmatter instantly.

---

### FieldModifier API Syntax

[**FieldModifier-Function-Signature**:: `fieldModifier(dv, page, fieldName, options?)` where dv is the Dataview API instance, page is the current page object being processed, fieldName is the string identifier of the field to render, and options is an optional configuration object controlling display behavior.]

**Function Signature:**

```javascript
fieldModifier(
  dv,           // Dataview API instance
  page,         // Dataview page object (e.g., p in .map(p => ...))
  fieldName,    // String: name of field to make editable
  options       // Optional: { attr?, options? }
)
```

**Options Object Structure:**

```javascript
{
  attr: {
    // Dataview attributes as data tags (rarely needed)
  },
  options: {
    alwaysOn: boolean,      // true = control always visible
                            // false (default) = click to show
    showAddField: boolean   // true = show "+" if field missing
                            // false (default) = show null
  }
}
```

---

### Basic Editable Table Pattern

**Template Structure:**

```dataviewj
// 1. Import fieldModifier API
const {fieldModifier: f} = MetadataMenu.api;

// 2. Define table configuration
const tableHeadings = ["Name", "Field1", "Field2"];
const fileQuery = '#tag-or-folder';
const limit = 20;
const sortField = 'field1';

// 3. Build table with editable fields
dv.table(
  tableHeadings,
  await Promise.all(
    dv.pages(fileQuery)
      .limit(limit)
      .sort(p => p[sortField], 'desc')
      .map(async p => [
        p.file.link,                    // File link (not editable)
        await f(dv, p, "field1"),       // Editable field
        await f(dv, p, "field2")        // Editable field
      ])
  )
);
```

> [!important]
> **Async/Await Requirement**
> The `fieldModifier` function is <span style='color: #FF00DC;'>asynchronous</span>, requiring:
> 1. `await` before each `f()` call
> 2. `async` in the `.map(async p => ...)` function
> 3. `await Promise.all()` wrapping the entire pages array
> 
> Forgetting these will cause the table to render `[object Promise]` instead of controls.

---

### Advanced Table Examples

#### Example 1: Project Dashboard with Filtering

```dataviewj
const {fieldModifier: f} = MetadataMenu.api;

// Configuration
const statusFilter = "read";  // Only show active projects
const sortBy = "rating";
const sortOrder = "desc";

dv.table(
  ["Project", "Status", "Priority", "Due Date", "Owner"],
  await Promise.all(
    dv.pages('"04-library"')
      .where(p => p.status === statusFilter)
      .sort(p => p[sortBy], sortOrder)
      .map(async p => [
        p.file.link,
        await f(dv, p, "status"),
        await f(dv, p, "rating", {options: {alwaysOn: true}}),
        await f(dv, p, "created"),
        await f(dv, p, "source")
      ])
  )
);
```

<span style='color: #72FFF1;'>Key Features:</span>
- Filters to only active projects
- Priority control always visible (no click required)
- Sorts by priority descending

#### Example 2: Reading List with Completion Tracking

```dataviewj
const {fieldModifier: f} = MetadataMenu.api;

dv.table(
  ["📚 Book", "Author", "✅ Finished", "⭐ Rating", "📅 Completed"],
  await Promise.all(
    dv.pages('"04-library"')
      .sort(p => p.finished ? p["completed-date"] : "9999", 'desc')
      .map(async p => [
        p.file.link,
        p.author,
        await f(dv, p, "finished"),        // Boolean checkbox
        await f(dv, p, "rating"),          // Number 1-5
        await f(dv, p, "completed-date")   // Date picker
      ])
  )
);
```

<span style='color: #27FF00;'>✓ Workflow:</span> Check "Finished" box → Rating field appears → Set date → Book moves to top of completed section.

#### Example 3: Task Board with Cycle Status

```dataviewj
const {fieldModifier: f} = MetadataMenu.api;

dv.table(
  ["Task", "Status", "Priority", "Assigned To"],
  await Promise.all(
    dv.pages('#task')
      .where(p => p.status !== "done")
      .sort(p => p.priority, 'desc')
      .map(async p => [
        p.file.link,
        await f(dv, p, "status"),         // Cycle: todo→doing→review→done
        await f(dv, p, "priority"),        
        await f(dv, p, "assigned-to")      // File field (links to person notes)
      ])
  )
);
```

<span style='color: #72FFF1;'>Status is a Cycle field</span>: Click to advance `todo` → `doing` → `review` → `done`. Completed tasks disappear from table.

---

### Integrating with FileClass Table Views

FileClass notes have a built-in table view, but you can also <span style='color: #FFC700;'>create custom Dataview tables</span> that combine multiple fileClasses or add additional filters:

```dataviewj
const {fieldModifier: f} = MetadataMenu.api;

// Show all content notes (books, articles, videos) in one table
dv.table(
  ["Content", "Type", "Status", "Rating", "Created"],
  await Promise.all(
    dv.pages('')
      .where(p => ["book", "article", "video"].includes(p.fileClass))
      .sort(p => p.created, 'desc')
      .map(async p => [
        p.file.link,
        p.fileClass,                          // Show which type it is
        await f(dv, p, "status"),             
        await f(dv, p, "rating"),
        p.created
      ])
  )
);
```

---

### Troubleshooting Editable Tables

**Problem: Controls Don't Appear**

<span style='color: #FF00DC;'>Symptoms:</span> Table renders but cells show plain text instead of interactive controls.

**Checklist:**
1. ✅ Dataview plugin JavaScript queries enabled?
   - Settings → Dataview → Enable JavaScript Queries
2. ✅ Using `dataviewjs` block (not `dataview`)?
   ```dataviewjs  // ← Correct
   ```
3. ✅ Imported `fieldModifier` correctly?
   ```javascript
   const {fieldModifier: f} = MetadataMenu.api;  // ✅ Correct
   // NOT: this.app.plugins.plugins["metadata-menu"].api  ❌
   ```
4. ✅ Using `await` and `async` properly?
   ```javascript
   await Promise.all(
     pages.map(async p => [
       await f(dv, p, "field")  // ← All three required
     ])
   )
   ```
5. ✅ Field definitions exist in Metadata Menu?
   - Check Settings → Metadata Menu → Preset Fields or fileClass fields

**Problem: Table Shows `[object Promise]`**

<span style='color: #FF00DC;'>Cause:</span> Missing `await` or `async` keywords.

**Solution:**
```javascript
// ❌ WRONG:
.map(p => [f(dv, p, "field")])

// ✅ CORRECT:  
.map(async p => [await f(dv, p, "field")])
```

**Problem: Changes Don't Save**

<span style='color: #FF00DC;'>Symptoms:</span> Edit field in table, but value reverts when table refreshes.

**Causes & Fixes:**
1. Field not indexed by Metadata Menu
   - Verify field definition exists
   - Check file isn't excluded from indexing (Settings → Excluded folders)
2. Frontmatter syntax error preventing parse
   - Open note, check YAML is valid
3. Lookup/Formula field being manually edited
   - <span style='color: #FF00DC;'>These are computed fields—changes get overwritten</span>

---

### Performance Optimization for Large Tables

**For vaults with 1000+ notes:**

```dataviewj
const {fieldModifier: f} = MetadataMenu.api;

// Limit results to improve render time
const LIMIT = 50;  // Only show top 50 results

dv.table(["File", "Priority"],
  await Promise.all(
    dv.pages("#project")
      .sort(p => p.priority, 'desc')
      .limit(LIMIT)  // ← Critical for performance
      .map(async p => [
        p.file.link,
        await f(dv, p, "priority", {options: {alwaysOn: false}})
        // alwaysOn: false = controls hidden until clicked
      ])
  )
);
```

[**Table-Rendering-Performance**:: DataviewJS tables with fieldModifier controls render more slowly than standard Dataview tables because each cell requires additional DOM manipulation. For large result sets (100+ rows), use .limit() to paginate and set alwaysOn: false to defer control rendering until user interaction.]

---

## 7️⃣ API Usage & Programmatic Control

> [!definition]
> - **Metadata-Menu-API**:: <span style='color: #27FF00;'>A JavaScript interface exposed by the plugin at `MetadataMenu.api` or `app.plugins.plugins["metadata-menu"].api`, providing functions for reading and writing metadata programmatically</span>

### Accessing the API

**Two Access Patterns:**

```javascript
// Pattern 1: Direct from global (recommended in DataviewJS)
const api = MetadataMenu.api;

// Pattern 2: Via plugin manager (use in external scripts)
const api = app.plugins.plugins["metadata-menu"].api;
```

### Available API Methods

| Method | Signature | Purpose |
|--------|-----------|---------|
| **fieldModifier** | `fieldModifier(dv, page, fieldName, options?)` | <span style='color: #72FFF1;'>Render editable control in Dataview table</span> |
| **postValues** | `postValues(fileOrPath, indexedPath, values)` | <span style='color: #72FFF1;'>Write values to nested fields programmatically</span> |
| **insertField** | `insertField(file, fieldName, location?)` | Insert field at specified location |
| **getField** | `getField(file, fieldName)` | Read field value |
| **updateLookupFields** | `updateLookupFields(file?)` | <span style='color: #72FFF1;'>Refresh Lookup fields in file or vault-wide</span> |

> [!warning]
> **API Stability**
> The Metadata Menu API is <span style='color: #FF00DC;'>not officially versioned or documented as stable</span>. Method signatures may change between plugin updates. Always test API-dependent code after updating Metadata Menu.

### Programmatic Field Insertion

**Use Case:** Templater or QuickAdd scripts that auto-populate metadata

```javascript
// In Templater template:
<%*
const api = app.plugins.plugins["metadata-menu"].api;

// Insert multiple fields at top of file
api.insertField(tp.file.path(true), "status", "top");
api.insertField(tp.file.path(true), "priority", "top");
api.insertField(tp.file.path(true), "created-date", "top");
%>
```

### Reading Field Values Programmatically

```javascript
const api = MetadataMenu.api;
const file = app.workspace.getActiveFile();

const status = api.getField(file, "status");
const priority = api.getField(file, "priority");

console.log(`Current status: ${status}, Priority: ${priority}`);
```

### Bulk Updating Lookup Fields

```javascript
const api = MetadataMenu.api;

// Update all Lookup fields in entire vault
api.updateLookupFields();

// Update Lookup fields in specific file
const file = app.workspace.getActiveFile();
api.updateLookupFields(file);
```

> [!helpful-tip]
> **Scheduled Lookup Updates**
> Combine with [[QuickAdd]] macros or [[Templater]] daily note templates to automatically refresh Lookup fields on a schedule. Example: Update project statistics every morning when opening daily note.

---

## 8️⃣ Advanced Features & Workflows

### Workflow 1: Project Management System

**FileClass Structure:**

```yaml
# 99_system/fileclasses/project.md
---
extends: note
mapWithTag: true
tagNames: [project]
---

# Fields (configured in UI):
- status: Select (planning|active|blocked|completed|archived)
- priority: Number (1-10)
- start-date: Date  
- due-date: Date
- owner: File (links to person note)
- budget: Number
- actual-spend: Number
- completion-percentage: Number (0-100)
- tasks: Lookup (counts #task notes where project = this file)
- blockers: Multi (list of blocker reasons)
```

**Dashboard Query:**

```dataviewj
const {fieldModifier: f} = MetadataMenu.api;

dv.header(2, "🚀 Active Projects");
dv.table(
  ["Project", "Status", "Priority", "Progress", "Tasks", "Due"],
  await Promise.all(
    dv.pages('#project')
      .where(p => p.status === "active")
      .sort(p => p.priority, 'desc')
      .map(async p => [
        p.file.link,
        await f(dv, p, "status"),
        await f(dv, p, "priority", {options: {alwaysOn: true}}),
        await f(dv, p, "completion-percentage"),
        await f(dv, p, "tasks"),  // Lookup field (read-only)
        await f(dv, p, "due-date")
      ])
  )
);
```

---

### Workflow 2: Reading Tracker with Statistics

**FileClasses:**

```yaml
# book.md
---
extends: content-note
mapWithTag: true
tagNames: [book]
---
Fields: title, author, genre, rating (1-5), finished (Boolean), 
        started-date, completed-date, page-count, notes
```

```yaml  
# reading-statistics.md (MOC note)
---
fileClass: dashboard
---
```

**Statistics Dashboard:**

```dataviewj
const {fieldModifier: f} = MetadataMenu.api;

const books = dv.pages('#book');
const finished = books.where(p => p.finished === true);
const inProgress = books.where(p => p.finished !== true && p["started-date"]);

dv.header(2, "📚 Reading Statistics");
dv.paragraph(`
- **Total Books**: ${books.length}
- **Finished**: ${finished.length}  
- **In Progress**: ${inProgress.length}
- **Average Rating**: ${finished.array().map(p => p.rating).reduce((a,b) => a+b, 0) / finished.length}
`);

dv.header(3, "Currently Reading");
dv.table(["Book", "Author", "Started", "Finished?"],
  await Promise.all(
    inProgress.sort(p => p["started-date"], 'desc')
      .map(async p => [
        p.file.link,
        p.author,
        p["started-date"],
        await f(dv, p, "finished")
      ])
  )
);
```

---

### Workflow 3: Meeting Notes with Action Items

**FileClass:**

```yaml
# meeting.md
---
mapWithTag: true
tagNames: [meeting]
---
Fields:
- meeting-type: Select (standup|planning|retrospective|client)
- date: Date
- attendees: MultiFile (links to person notes)
- agenda: Input (template)
- decisions: Input (multiline)
- action-items: ObjectList
  - task: Input
  - owner: File (person note)
  - due-date: Date
  - status: Cycle (todo|doing|done)
```

**All Action Items Dashboard:**

```dataviewj
const {fieldModifier: f} = MetadataMenu.api;

const meetings = dv.pages('#meeting');
let allActions = [];

// Extract all action items from all meetings
for (let meeting of meetings) {
  if (meeting["action-items"]) {
    for (let action of meeting["action-items"]) {
      allActions.push({
        meeting: meeting.file.link,
        task: action.task,
        owner: action.owner,
        dueDate: action["due-date"],
        status: action.status
      });
    }
  }
}

// Filter to open actions only
const openActions = allActions.filter(a => a.status !== "done");

dv.header(2, "✅ Open Action Items");
dv.table(
  ["Task", "Meeting", "Owner", "Due", "Status"],
  openActions
    .sort((a, b) => a.dueDate - b.dueDate)
    .map(action => [
      action.task,
      action.meeting,
      action.owner,
      action.dueDate,
      action.status
    ])
);
```

> [!key-claim]
> **ObjectList Power**
> <span style='background-color: #FFC70040; color: #FFC700;'>ObjectList fields enable repeating substructures</span> like multiple employees per company, multiple action items per meeting, or multiple checkpoints per project—each with their own typed fields. This transforms frontmatter into a lightweight relational database.

---

### Workflow 4: Zettelkasten with Automatic Backlink Counts

**Global FileClass for All Notes:**

```yaml
# _base-note.md (set as Global FileClass in settings)
---
---
Fields:
- created: Date (auto-set via Templater)
- modified: Date (auto-set via Templater)  
- status: Cycle (fleeting|literature|permanent|archived)
- connections: Lookup
  Query: dv.pages().where(p => p.file.outlinks.includes(current.file.link))
  Output: Count All
```

**Result:** Every note automatically tracks how many OTHER notes link to it via the `connections` Lookup field.

**Most Connected Notes Query:**

```dataview
TABLE connections as "Backlinks", status
FROM ""
WHERE connections > 5
SORT connections DESC
LIMIT 20
```

---

### Workflow 5: Date Shifting for Spaced Repetition

Metadata Menu supports <span style='color: #72FFF1;'>time-shifting Date fields</span>—advancing dates by predefined intervals:

**Configuration:**

```yaml
# In field settings:
Field Name: next-review
Type: Date
Shift Intervals: 1 day, 3 days, 1 week, 2 weeks, 1 month, 3 months

# Optional: Link to Cycle field
Cycle Field: review-stage
Cycle Values: [new, learning, young, mature, mastered]
```

**Behavior:**
1. Click "Shift" button on `next-review` field
2. Date advances by current interval (e.g., +1 week)
3. If linked to `review-stage` Cycle field, that advances too
4. Interval increases (next shift will be +2 weeks)

<span style='color: #27FF00;'>✓ Use Case:</span> [[Spaced Repetition]] for [[Zettelkasten]] notes, vocabulary learning, concept reviews.

---

## 9️⃣ Troubleshooting & Optimization

### Index Status & Force Re-indexing

Metadata Menu maintains an <span style='color: #72FFF1;'>internal index</span> of all field values, updated automatically when files change.

**Index Status Indicator:**

- Located in <span style='color: #72FFF1;'>status bar</span> (bottom of Obsidian)
- 🔄 **Rotating icon**: Indexing in progress
- ⚠️ **Warning icon**: Formulas/Lookups out of date
- ✅ **Check icon**: Index up to date

**Force Re-index (Troubleshooting):**

If metadata appears inconsistent:
1. Command Palette → `Metadata Menu: Index metadata fields`
2. Wait for status bar icon to show ✅

> [!warning]
> **Large Vault Re-indexing**
> For vaults with 5000+ notes, re-indexing can take 30-60 seconds and temporarily freeze Obsidian. Avoid re-indexing unless absolutely necessary.

---

### Performance Optimization Strategies

#### Strategy 1: Exclude Folders from Indexing

**Settings → Metadata Menu → Exclude folders:**

```regex
^(templates|archive|attachments|daily-notes)/
```

<span style='color: #27FF00;'>Effect:</span> Metadata Menu ignores these folders entirely, reducing index size and update frequency.

#### Strategy 2: Disable Auto-Update for Lookups

For <span style='color: #FF00DC;'>Lookup fields</span> that don't need real-time accuracy:

```yaml
# In Lookup field settings:
Auto-update: ❌ Disabled
```

<span style='color: #27FF00;'>Update manually:</span> Command Palette → `Metadata Menu: Update lookup fields`

#### Strategy 3: Limit Dataview Table Results

```dataviewj
const LIMIT = 30;  // Max rows to render

dv.table(...,
  await Promise.all(
    dv.pages(...)
      .limit(LIMIT)  // ← Essential for 1000+ note vaults
      .map(...)
  )
);
```

#### Strategy 4: Use Frontmatter Over Inline Fields

<span style='color: #72FFF1;'>Dataview queries on frontmatter fields are 10-100x faster</span> than inline field queries due to caching.

**Recommended:**
```yaml
---
status: active
priority: 5
---
```

**Avoid for frequently-queried fields:**
```markdown
The status:: active project has priority:: 5.
```

---

### Common Issues & Solutions

#### Issue: FileClass Not Applying

**Symptoms:** Fields defined in fileClass don't appear in note's metadata modal.

**Checklist:**
1. ✅ FileClass folder path correct with trailing slash?
   - Settings → Class Files Path: `99_system/fileclasses/`
2. ✅ FileClass mapping configured?
   - Check frontmatter `fileClass: name` OR
   - Tag match enabled + correct tag present OR
   - Path match includes this file's folder
3. ✅ FileClass note exists in correct location?
   - Verify file exists at: `99_system/fileclasses/[name].md`
4. ✅ Field definitions saved in fileClass?
   - Open fileClass → Click button → Fields tab → Verify fields exist

#### Issue: Autocompletion Not Triggering

**Symptoms:** Typing `:` or `::` doesn't show field suggestions.

**Fixes:**
1. Enable globally: Settings → Metadata Menu → Field Autocompletion ✅
2. Check field not excluded: Settings → Excluded fields from context menus
3. Verify field definition exists in Preset Fields or applicable fileClass

#### Issue: Context Menu Missing Options

**Symptoms:** Right-click doesn't show "Metadata Menu" submenu.

**Cause:** Plugin setting restricts display.

**Fix:** Settings → Metadata Menu → Context Menu Display → Change to "Show all options"

#### Issue: Frontmatter Formatting Breaks

**Symptoms:** YAML becomes malformed after editing via Metadata Menu.

**Common Causes:**
1. <span style='color: #FF00DC;'>Multi/MultiFile fields</span> with indented list display enabled
2. Special characters in field values (unescaped quotes)
3. Concurrent edits (Metadata Menu + manual typing simultaneously)

**Solutions:**
- Use array format for Multi fields: Settings → Frontmatter Display → Arrays
- Avoid manual frontmatter edits while Metadata Menu modal is open
- Use Input field template validation for special characters

---

### Debugging with Browser Console

<span style='color: #72FFF1;'>Advanced troubleshooting</span> via Developer Console:

1. `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Opt+I` (Mac)
2. Console tab
3. Type commands:

```javascript
// Check if Metadata Menu is loaded
app.plugins.plugins["metadata-menu"]

// View plugin API methods
MetadataMenu.api

// Get field value from active file
const file = app.workspace.getActiveFile();
MetadataMenu.api.getField(file, "status");

// Check fileClass mappings for current file
app.plugins.plugins["metadata-menu"].fieldIndex
```

---

## 📊 Metadata & Attribution

> [!methodology-and-sources]
> **Research Methodology**
> - **Primary Sources**: 
>   - Official Metadata Menu documentation: https://mdelobelle.github.io/metadatamenu/
>   - GitHub repository: https://github.com/mdelobelle/metadatamenu
>   - Obsidian community forum discussions and troubleshooting threads
> - **Research Queries**: 
>   - "Metadata Menu Obsidian plugin documentation"
>   - "Metadata Menu fileClass configuration setup"
>   - "Metadata Menu field types complete list options"
>   - "Metadata Menu Obsidian best practices workflow examples"
>   - "Metadata Menu API methods dataviewjs integration"
> - **Synthesis Approach**: Comprehensive web search followed by documentation review, cross-referenced with community usage examples and official release notes to ensure accuracy and completeness
> - **Confidence Level**: 
>   - **High** for core functionality, field types, fileClass system architecture
>   - **High** for Dataview integration and fieldModifier API usage
>   - **Medium** for undocumented API methods (subject to change without notice)

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12-14 | Initial comprehensive compilation covering all plugin features through v0.8.10 |

---

# 🔗 Related Topics for PKB Expansion

1. **[[Dataview Query Language - Advanced Patterns]]**
   - *Connection*: Metadata Menu's Lookup fields and File field queries rely heavily on Dataview's `dv.pages()` syntax
   - *Depth Potential*: Deep dive into DQL filtering, function chaining, and performance optimization strategies
   - *Knowledge Graph Role*: Bridges data querying and metadata management, enabling sophisticated vault-wide data analysis

2. **[[Obsidian Plugin Development - Creating Custom Metadata Processors]]**
   - *Connection*: Understanding Metadata Menu's architecture reveals patterns for building custom metadata-aware plugins
   - *Depth Potential*: Explore plugin API, metadata indexing strategies, and UI component integration
   - *Knowledge Graph Role*: Advances technical understanding of Obsidian's extensibility, enabling custom tool creation

3. **[[Personal Knowledge Management Schemas - Design Patterns]]**
   - *Connection*: FileClass system exemplifies schema-driven PKM; exploring broader schema design patterns enhances metadata strategy
   - *Depth Potential*: Examine taxonomies, ontologies, controlled vocabularies, and their application to knowledge work
   - *Knowledge Graph Role*: Theoretical foundation for practical metadata implementation across knowledge management systems

4. **[[Templater & QuickAdd Integration - Advanced Metadata Automation]]**
   - *Connection*: Metadata Menu's API enables programmatic field insertion/manipulation within template workflows
   - *Depth Potential*: Build automated note creation systems that populate fileClass assignments and field values based on context
   - *Knowledge Graph Role*: Synthesis of metadata management, templating, and workflow automation for maximum productivity
- 

---

### 📖 Extracted Definitions
```dataviewjs
const currentFile = dv.current().file;
const content = await dv.io.load(currentFile.path);
const bracketedFieldRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;

let definitions = [];
let match;

while ((match = bracketedFieldRegex.exec(content)) !== null) {
    definitions.push({
        key: match[1].trim(),
        value: match[2].trim()
    });
}

// Group by first letter
const grouped = {};
definitions.forEach(d => {
    const firstLetter = d.key[0].toUpperCase();
    if (!grouped[firstLetter]) grouped[firstLetter] = [];
    grouped[firstLetter].push(d);
});

// Display grouped results
const sortedLetters = Object.keys(grouped).sort();

for (let letter of sortedLetters) {
    dv.header(4, `${letter}`);
    dv.table(
        ["Term", "Definition"],
        grouped[letter].map(d => [`**${d.key}**`, d.value])
    );
}
```
---
