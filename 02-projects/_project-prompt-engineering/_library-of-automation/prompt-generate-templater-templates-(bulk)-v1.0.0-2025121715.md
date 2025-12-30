---
type: "prompt"
id: "20251217150502"
status: "active"
version: "1.0.0"
rating: "0.0"
source: "claude-sonnet-4.5"
title: "Generate Templater Templates in Bulk"
description: "To generate useful templater logic in a way that I can build a sizable collection of useful template syntax."
key-takeaway: "Tested Works great."
last-used: "[[2025-12-17]]"
tags:
  - "year/2025"
  - "prompt-engineering"
  - "llm-capability/generation"
  - "prompt-workflow/deployment"
aliases:
  - "Prompt"
  - "Prompt-Engineering"
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
link-related:
  - "[[2025-12-17|Daily Note]]"
  - "[[2025-W51|Weekly Review]]"
---

```dataviewjs
// SYSTEM: Enhanced Semantic Bridge Engine v2.0
// PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts) with advanced analytics

const current = dv.current();
const myOutlinks = current.file.outlinks?.map(l => l.path) || [];

// Performance optimization: Create Set for faster lookups
const myOutlinkSet = new Set(myOutlinks);
const currentPath = current.file.path;

// Function to remove Asian characters (Chinese, Japanese, Korean)
function removeAsianChars(text) {
    if (!text) return "";
    return text.toString().replace(/[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf\uac00-\ud7a3]/g, "");
}

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
 dv.header(3, removeAsianChars("🔗 Semantic Bridges (Missing Connections)"));
  
 // Add summary statistics with error handling
 try {
  const totalSharedConnections = siblings.reduce((sum, s) => sum + (s.sharedCount || 0), 0);
  const avgSimilarity = siblings.length > 0 ? 
   Math.round(siblings.reduce((sum, s) => sum + (s.similarityScore || 0), 0) / siblings.length) : 0;
   
  dv.paragraph(removeAsianChars(`**Found ${siblings.length} semantic siblings** • Total shared: ${totalSharedConnections} connections • Avg. similarity: ${avgSimilarity}%`));
 } catch (e) {
  console.warn("Error calculating sibling statistics:", e);
  dv.paragraph(removeAsianChars(`**Found ${siblings.length} semantic siblings**`));
 }
  
 dv.table(
  [removeAsianChars("Note"), removeAsianChars("Similarity"), removeAsianChars("Strength"), removeAsianChars("Maturity"), removeAsianChars("Type"), removeAsianChars("Shared Context")], 
  siblings.map(s => [
   s.link, 
   removeAsianChars(`📊${s.similarityScore || 0}%`),
   removeAsianChars(`🔗${s.sharedCount || 0}`), 
   removeAsianChars(s.maturity === "evergreen" ? "🌳evergreen" : 
   s.maturity === "budding" ? "🌿budding" :
   s.maturity === "developing" ? "🪴developing" :
   s.maturity === "seedling" ? "🌱seedling" : "❓unset"),
   removeAsianChars(s.type || "unknown"),
   removeAsianChars(s.sharedLinks?.slice(0, 2).map(l => l.displayName || l.path).join(", ") + ((s.sharedLinks?.length || 0) > 2 ? "…" : "") || "")
  ])
 );
} else {
 dv.paragraph(removeAsianChars("*No semantic siblings found. This note is unique in its connections.*"));
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

 dv.header(3, removeAsianChars(`📂 Domain Analysis: ${primaryDomain}`));
 dv.paragraph(removeAsianChars(`**Total notes**: ${totalNotes} | **Recent activity**: ${activityScore}% (30d)`));
 dv.paragraph(removeAsianChars(`**Maturity breakdown**: 🌳${maturityDistribution.evergreen} | 🌿${maturityDistribution.budding} | 🌱${maturityDistribution.developing} | 🌰${maturityDistribution.seedling} | ❓${maturityDistribution.unset}`));
 dv.paragraph(removeAsianChars(`**Domain health**: ${coverage}% mature (evergreen + budding)`));
  
 // Domain health indicator
 const healthIndicator = coverage >= 80 ? removeAsianChars("🟢 Excellent") : 
             coverage >= 60 ? removeAsianChars("🟡 Good") : 
             coverage >= 40 ? removeAsianChars("🟠 Fair") : removeAsianChars("🔴 Poor");
 dv.paragraph(removeAsianChars(`**Health status**: ${healthIndicator}`));
}

// NETWORK INTELLIGENCE: Advanced connectivity analysis
const inlinks = current.file.inlinks || [];
const outlinks = current.file.outlinks || [];

dv.header(3, removeAsianChars("🕸️ Network Intelligence"));
const networkMetrics = [
 [removeAsianChars("**Metric**"), removeAsianChars("**Value**"), removeAsianChars("**Insight**")],
 [removeAsianChars("In-links"), removeAsianChars(inlinks.length.toString()), removeAsianChars(inlinks.length > 10 ? "⚡ Hub" : inlinks.length > 0 ? "🌱 Node" : "🕸️ Orphan")],
 [removeAsianChars("Out-links"), removeAsianChars(outlinks.length.toString()), removeAsianChars(outlinks.length > 15 ? "🗺️ Explorer" : outlinks.length > 5 ? "🧭 Navigator" : "🎯 Focused")],
 [removeAsianChars("Link Ratio"), removeAsianChars(outlinks.length > 0 ? (inlinks.length / outlinks.length).toFixed(1) : "∞"), 
  removeAsianChars(outlinks.length > 0 && inlinks.length / outlinks.length > 2 ? "📈 High authority" : "📊 Balanced")]
];

dv.table(networkMetrics[0], networkMetrics.slice(1));

// TEMPORAL ANALYSIS: Content aging and review patterns
dv.header(3, removeAsianChars("⏰ Temporal Intelligence"));
try {
 const created = current.file.ctime;
 const modified = current.file.mtime;
 const ageDays = Math.floor((new Date() - new Date(created)) / (1000 * 60 * 60 * 24));
 const stalenessDays = Math.floor((new Date() - new Date(modified)) / (1000 * 60 * 60 * 24));

 const reviewInsights = [];
 if (current["review-count"] > 5) reviewInsights.push(removeAsianChars("🔁 Well-reviewed"));
 if (stalenessDays > 180) reviewInsights.push(removeAsianChars("⏰ Needs refresh"));
 if (ageDays < 30) reviewInsights.push(removeAsianChars("🆕 New content"));

 dv.paragraph(removeAsianChars(`**Age**: ${ageDays} days | **Staleness**: ${stalenessDays} days`));
 dv.paragraph(removeAsianChars(`**Review status**: ${current["review-count"] || 0} reviews | ${reviewInsights.join(" • ") || "📝 Standard"}`));
} catch (e) {
 console.warn("Error in temporal analysis:", e);
 dv.paragraph(removeAsianChars("*Temporal analysis unavailable*"));
}
```

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
>WHERE  type = "prompt"
>SORT "maturity" DESC
>LIMIT 15
>```

[Initial Creation: [[2025-12-17|Wednesday, December 17th, 2025]]]

---
### 📊 Key Differences from Dataview Prompt

|Aspect|Dataview Prompt|Templater Prompt|
|---|---|---|
|**Core Syntax**|DQL + DataviewJS|Templater delimiters (`<%` `%>`)|
|**Complexity Tiers**|DQL → DataviewJS → Charts/JS Engine|Basic → Intermediate → Advanced → Synergy|
|**Primary Use Cases**|Queries, data aggregation, visualization|Templates, automation, file generation|
|**Integration Focus**|Charts plugin, JS Engine|QuickAdd, Meta Bind, Tasks, Dataview|
|**Output Type**|Dynamic queries that update|Static/dynamic file generation|
|**Key Functions**|`LIST`, `TABLE`, `dv.pages()`|`tp.date.*`, `tp.file.*`, `tp.system.*`|
|**Documentation Depth**|Advanced+Synergy only|Advanced+Synergy only (parallel structure)|

>[! ] Usage Instructions
> **To use this prompt effectively:**
> 1. **Copy the entire prompt** from the markdown block above
> 2. **Replace `[INSERT THEME HERE]`** with your desired theme:
>     - Examples: "Daily Note Workflows", "Project Initialization", "Literature Note Capture", "MOC Generation", "Meeting Notes", "Spaced Repetition Review"
> 3. **Paste into Claude** (or your LLM of choice)
> 4. **Receive ~10-15 template examples** across all complexity tiers
> 5. **Copy output** and save as reference note in your PKB
> 6. **Repeat with new themes** in fresh contexts for unlimited template ideas
> **Suggested Theme Categories:**
> - 📝 **Capture**: Inbox processing, quick entry, fleeting notes
> - 🎯 **Projects**: Initialization, status updates, completion workflows
> - 📚 **Knowledge**: Permanent notes, literature notes, concept definitions
> - 🔄 **Review**: Daily/weekly/monthly reviews, retrospectives, habit tracking
> - 🗺️ **Navigation**: MOC generation, dashboard creation, index building
> - 🤖 **AI Integration**: Prompt templates, AI-assisted content generation
> - 🔗 **Linking**: Automated cross-referencing, semantic connection building
> - 📊 **Metadata**: Automated frontmatter, tag generation, classification
> This prompt will generate **immediately usable, production-ready Templater templates** with the same educational depth and progressive complexity structure as your Dataview query prompt.# 📊 Key Differences from Dataview Prompt

|Aspect|Dataview Prompt|Templater Prompt|
|---|---|---|
|**Core Syntax**|DQL + DataviewJS|Templater delimiters (`<%` `%>`)|
|**Complexity Tiers**|DQL → DataviewJS → Charts/JS Engine|Basic → Intermediate → Advanced → Synergy|
|**Primary Use Cases**|Queries, data aggregation, visualization|Templates, automation, file generation|
|**Integration Focus**|Charts plugin, JS Engine|QuickAdd, Meta Bind, Tasks, Dataview|
|**Output Type**|Dynamic queries that update|Static/dynamic file generation|
|**Key Functions**|`LIST`, `TABLE`, `dv.pages()`|`tp.date.*`, `tp.file.*`, `tp.system.*`|
|**Documentation Depth**|Advanced+Synergy only|Advanced+Synergy only (parallel structure)|

---
# 🎯 Usage Instructions
**To use this prompt effectively:**
1. **Copy the entire prompt** from the markdown block above
2. **Replace `[INSERT THEME HERE]`** with your desired theme:
    - Examples: "Daily Note Workflows", "Project Initialization", "Literature Note Capture", "MOC Generation", "Meeting Notes", "Spaced Repetition Review"
3. **Paste into Claude** (or your LLM of choice)
4. **Receive ~10-15 template examples** across all complexity tiers
5. **Copy output** and save as reference note in your PKB
6. **Repeat with new themes** in fresh contexts for unlimited template ideas
**Suggested Theme Categories:**
- 📝 **Capture**: Inbox processing, quick entry, fleeting notes
- 🎯 **Projects**: Initialization, status updates, completion workflows
- 📚 **Knowledge**: Permanent notes, literature notes, concept definitions
- 🔄 **Review**: Daily/weekly/monthly reviews, retrospectives, habit tracking
- 🗺️ **Navigation**: MOC generation, dashboard creation, index building
- 🤖 **AI Integration**: Prompt templates, AI-assisted content generation
- 🔗 **Linking**: Automated cross-referencing, semantic connection building
- 📊 **Metadata**: Automated frontmatter, tag generation, classification
This prompt will generate **immediately usable, production-ready Templater templates** with the same educational depth and progressive complexity structure as your Dataview query prompt.
# prompt-generate-templater-templates-(bulk)-v1.0.0-2025121715

`````prompt
----
Prompt-ID: "2025121715"
Prompt-Version: 1.0.0
----

You are a world-class Obsidian PKB Architect and Templater plugin expert. You have a deep understanding of the Templater plugin's complete API, including all internal functions (tp.date, tp.file, tp.frontmatter, tp.system, tp.config, tp.web) and advanced features like user scripts, dynamic commands, and plugin integrations.
Your task is to generate a comprehensive collection of Templater templates to be used as inspiration and educational examples for a user building their own PKB. You must generate a wide variety of templates, ranging from simple to highly advanced.
The examples must be centered around the theme of: **[INSERT THEME HERE]**
**CRITICAL FORMATTING RULE:** All code blocks you generate MUST use plain Markdown backticks (```) with **NO language identifier** (do NOT use ```templater or ```javascript). This is to ensure the code is stored as inert text and does not auto-execute within an Obsidian note.
You must follow this structure precisely:

---
## Basic Templates
*Provide 3-4 examples of fundamental Templater templates. These should demonstrate:
- Simple variable insertion (`<% tp.file.title %>`)
- Date/time formatting (`<% tp.date.now("YYYY-MM-DD") %>`)
- Basic frontmatter generation
- File path/name operations
Enclose each template in a plain code block with a brief description above it.*

---
## Intermediate Templates
*Provide 3-4 examples of more complex Templater templates. These should include:
- Conditional logic (`<% if %>`, `<% else %>`)
- Loops and iteration (`<% for %>`)
- Dynamic content generation based on context
- User input prompts (`<% tp.system.prompt() %>`)
- File manipulation operations
- Multi-line template variables
For each template, provide a 1-2 sentence description. Enclose templates in plain code blocks.*

---
## Advanced Templates
*Provide 2-3 examples of sophisticated Templater templates demonstrating expert-level capabilities.*
**For each Advanced Template, you MUST provide:**
1. **Description** - Exactly what the template does and how it works
2. **Top Use Cases** - 2-3 specific scenarios where this template shines
3. **Implementation Tips** - Critical details for successful deployment
4. **Customization Options** - 2-3 ways users can adapt the template to their needs
*After the documentation, provide the complete, functional Templater code in a plain code block.*
These advanced templates should demonstrate:
- User script integration
- Complex automation workflows
- Multi-file operations (creation, modification, organization)
- Advanced string manipulation and parsing
- System command execution
- Web API integration (`tp.web.daily_quote()` or custom requests)

---
## Synergy Templates (Plugin Integration)
*Provide 2-3 examples of Templater templates that integrate with other Obsidian plugins (QuickAdd, Dataview, Meta Bind, Tasks, etc.) to create powerful combined workflows.*
**For each Synergy Template, you MUST provide:**
1. **Description** - What the template does and which plugins it integrates with
2. **Top Use Cases** - 2-3 specific scenarios for this integration pattern
3. **Implementation Tips** - Prerequisites, setup steps, and critical details
4. **Customization Options** - 2-3 ways to extend or modify the integration
*After the documentation, provide the complete, functional template code in a plain code block.*
These synergy templates should demonstrate integration patterns like:
- Templater + QuickAdd (capture workflows)
- Templater + Dataview (dynamic content generation from queries)
- Templater + Meta Bind (interactive button workflows)
- Templater + Tasks (automated task management)
- Templater + Custom user scripts (extending functionality)

---
## Context: Your PKB Metadata & Structure
This is my metadata quick reference and folder structure for you to use when populating the templates.
### Available Options for Metadata Fields
#### type
- analysis
- claude-project
- cog-sci-report
- concept
- cosmo-report
- dashboard
- definition
- edu-report
- experiment
- framework
- gemini-gem
- guide
- literature
- mental-model
- moc
- pattern
- permanent-note
- pkb-report
- principle
- prompt
- prompt-report
- reference
- report
- review
- theory
- tutorial
#### source
- claude-opus-4.1
- claude-sonnet-4.5
- gemini-flash-2.5
- gemini-flash-3.0
- gemini-pro-2.5
- gemini-pro-3.0
#### maturity
- needs-review
- seedling
- developing
- budding
- evergreen
#### confidence
- speculative
- provisional
- moderate
- established
- high
#### status
- active
- archived
- deprecated
#### priority
- low
- medium
- high
- urgent
#### link-up (MOCs)
- `[[artificial-intelligence-moc]]`
- `[[cognitive-science-moc]]`
- `[[cosmology-moc]]`
- `[[educational-psychology-moc]]`
- `[[learning-theory-moc]]`
- `[[neuroscience-moc]]`
- `[[pkb-&-pkm-moc]]`
- `[[practical-philosophy-moc]]`
- `[[prompt-engineering-moc]]`
#### Tags
#pkm
#pkb 
#prompt-engineering
#cognitive-science
#cosmology
#type/report
#type/reference
#type/permanent
#status/complete
#status/in-progress
#status/not-read
#status/read
#status/seedling
#status/budding
#status/developing
#status/evergreen
#status/needs-review
#year/2025
#cognitive-pkm
#cognitive-enhancement
#cognitive-training
#dataview
#templater
#automation
### Folder Hierarchy
#### Level 0: Core Infrastructure
- 00-inbox/ → Ingestion & triage zone
- 00-meta/ → System memory & configuration
- 000_database/ → [Database storage]
#### Level 1: Temporal Organization
- 01-daily-notes/ → Atomic daily entries (time-indexed)
#### Level 2-7: Content Layers
- 02-projects/ → Active project documentation
- 03-notes/ → Core knowledge atoms
- 04-library/ → Reference materials & resources
- 05-tasks-&-reviews/ → GTD & reflection systems
- 06-dashboards/ → Overview & summary pages
- 07-mocs/ → Maps of Content (graph hubs)
#### Level 99: System Management
- 99-archive/ → Deprecated/completed content
- 99-system/ → System configuration files

---
## Template Generation Guidelines
**When generating templates, ensure:**
1. All Templater syntax uses correct delimiters: `<%` and `%>`
2. Multi-line template commands use `<%*` and `%>` for proper execution
3. Variables are properly accessed (e.g., `tp.file.title`, `tp.date.now()`)
4. User prompts provide clear guidance on expected input
5. Error handling is included for complex operations
6. Comments explain non-obvious logic
7. Templates are immediately usable (no placeholders requiring additional setup unless noted)
**For themes involving:**
- **Capture workflows** → Focus on inbox processing, quick entry, metadata automation
- **Project management** → Emphasize project initialization, status tracking, file organization
- **Knowledge management** → Highlight note creation, linking automation, MOC generation
- **Review systems** → Feature periodic review templates, progress tracking, reflection prompts
- **Content generation** → Showcase dynamic content creation, AI integration, multi-file workflows

---
## Output Format Reminder
Each template code block should:
- Use plain backticks (```) with NO language identifier
- Be complete and functional (ready to copy into Obsidian)
- Include inline comments for complex logic
- Follow best practices for Templater syntax
- Be tested conceptually for logical correctness
Provide comprehensive, production-ready templates that demonstrate the full power of Templater while remaining accessible and well-documented.

`````
