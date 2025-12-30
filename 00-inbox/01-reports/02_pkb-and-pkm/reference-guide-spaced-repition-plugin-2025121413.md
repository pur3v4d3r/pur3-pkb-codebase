---
aliases:
  - "Obsidian SR"
  - "Spaced Repetition Plugin Guide"
tags:
  - "type/report"
  - "year/2025"
  - "type/analysis"
  - "status/in-progress"
  - "pkb"
  - "knowledge-workflow"
  - "review-system"
  - "self-improvement/skill-development"
  - "metacognitive-pkm"
  - "cognitive-resources"
  - "obsidian/plugins"
  - "spaced-repetition"
  - "cognitive-pkm"
source: "claude-sonnet-4.5"
id: "20251214132001"
created: "2025-12-14T13:20:01"
modified: "2025-12-14T13:20:01"
week: "[[2025-W50]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "reference"
maturity: "needs-review"
confidence: "speculative"
next-review: "2025-12-21"
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-14|Daily-Note]]"
---

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Introduction to Spaced Repetition in Obsidian]]
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

##### Introduction to Spaced Repetition in Obsidian

> [! ] ### Claude Thinking
> The user is requesting a comprehensive reference note on the "Spaced Repetition" plugin for Obsidian. This is clearly a request for a **Reference Note** type, which means:
> - Metadata header REQUIRED (tags + aliases)
> - Exhaustive coverage (1500-4000+ words)
> - 15-40 wiki-links
> - 8-15 callouts
> - Expansion section with 4 topics
> - Heavy use of inline fields for key information
> - Semantic color coding for visual hierarchy
> 
> I need to activate web_search to gather current, accurate information about the Spaced Repetition plugin since:
> 1. This is a technical tool that may have updates since January 2025
> 2. The user needs comprehensive, accurate operational guidance
> 3. Plugin features, syntax, and best practices need verification
> 4. I want to provide the most current installation and configuration details
> 
> Research areas needed:
> - Plugin overview and core functionality
> - Installation and setup procedures
> - Card creation syntax (single-line, multi-line, cloze deletions)
> - Scheduling algorithms (SM-2, FSRS)
> - Review workflow and interface
> - Advanced features (tags, decks, buried cards, etc.)
> - Configuration options and settings
> - Integration with Obsidian features
> - Best practices for card design
> - Common pitfalls and troubleshooting
> - Performance optimization
> 
> After research, I'll create a detailed blueprint covering:
> 1. Introduction and core concepts
> 2. Installation and configuration
> 3. Card creation methods and syntax
> 4. Review workflow
> 5. Advanced features
> 6. Best practices
> 7. Troubleshooting
> 8. Integration patterns
> Based on my research, I now have comprehensive information about the Obsidian Spaced Repetition plugin. Let me create a detailed blueprint and then generate the reference note.

---
tags: #obsidian #spaced-repetition #plugin #flashcards #learning #reference-note
aliases: [Obsidian SR, SR Plugin, Spaced Repetition Plugin Guide, Flashcard Review in Obsidian]
---

> [!the-purpose]
> **Comprehensive operational guide for the Obsidian Spaced Repetition plugin—covering installation, flashcard syntax, review workflows, algorithm configuration, and best practices for building an effective spaced repetition system within your Personal Knowledge Base.**

---

## 📖 Introduction to Spaced Repetition in Obsidian

[<span style='color: #FFC700;'>**Spaced Repetition**</span>:: a learning technique that schedules review of information at progressively increasing intervals to combat the forgetting curve and optimize long-term retention.] The [[Obsidian]] Spaced Repetition plugin (commonly abbreviated as <span style='color: #72FFF1;'>SR Plugin</span>) brings this scientifically-validated learning methodology directly into your [[Personal Knowledge Base]], allowing you to transform passive notes into active learning materials without leaving your vault.

Developed by <span style='color: #FF5700;'>Stephen Mwangi (st3v3nmw)</span>, the plugin supports **both flashcard-based review and whole-note review**, enabling flexible learning workflows that integrate seamlessly with your existing [[Zettelkasten]] or [[PARA Method]] organizational systems.

> [!core-principle]
> The SR Plugin operates on a fundamental principle: [<span style='color: #27FF00;'>**Learning is strengthened through active retrieval**</span>:: the act of recalling information from memory creates stronger neural pathways than passive re-reading], and [<span style='color: #27FF00;'>**optimal spacing defeats the forgetting curve**</span>:: reviewing material just before you're likely to forget it maximizes retention while minimizing total review time].

### Key Capabilities

The plugin provides:

- **Multiple flashcard formats**: Single-line (`Question::Answer`), multi-line (separated by `?`), reversed cards (bidirectional), and [[Cloze Deletion|cloze deletions]]
- **Flexible organization**: Deck creation via [[Obsidian Tags|hierarchical tags]] (`#flashcards/subdeck`) or vault folder structure
- **Rich content support**: LaTeX equations, code blocks, images, audio, and all [[Markdown]] formatting
- **Contextual review**: Automatic display of note titles and heading hierarchy during review sessions
- **Scheduling algorithms**: Implements <span style='color: #72FFF1;'>SM-2-OSR</span> (SuperMemo-2 variant) with planned support for [[FSRS Algorithm|FSRS]]
- **Whole-note review**: Tag entire notes with `#review` for periodic reinforcement of conceptual understanding
- **Statistics tracking**: Retention rates, review counts, and deck-specific analytics

---

## ⚙️ Installation & Initial Configuration

### Standard Installation

The SR Plugin is available through [[Obsidian]]'s Community Plugins marketplace:

1. Open **Settings** → **Community plugins** → **Browse**
2. Search for <span style='color: #72FFF1;'>"Spaced Repetition"</span>
3. Click **Install**, then **Enable**
4. Configure initial settings (see below)

> [!helpful-tip]
> After enabling the plugin, you'll see a **status bar indicator** at the bottom of the Obsidian window showing the number of cards and notes currently due for review. Clicking this opens the review interface.

### Manual Installation

For advanced users or beta versions:

1. Download `main.js`, `manifest.json`, and `styles.css` from the [GitHub Releases](https://github.com/st3v3nmw/obsidian-spaced-repetition/releases)
2. Create folder: `.obsidian/plugins/obsidian-spaced-repetition/`
3. Place downloaded files in this folder
4. Enable the plugin in **Settings** → **Community plugins**

### Essential Initial Settings

Navigate to **Settings** → **Spaced Repetition** to configure:

| **Setting** | **Recommended Value** | **Purpose** |
|-------------|----------------------|-------------|
| <span style='color: #72FFF1;'>Flashcards folder tag</span> | `#flashcards` | Default tag for identifying flashcard-containing notes |
| <span style='color: #72FFF1;'>Review note tag</span> | `#review` | Tag for marking notes for whole-note review |
| <span style='color: #72FFF1;'>Enable folder-based decks</span> | OFF (use tags initially) | Alternative to tag-based organization |
| <span style='color: #72FFF1;'>Bury sibling cards</span> | ON | Prevents seeing related cards in same session |
| <span style='color: #72FFF1;'>Show context in cards</span> | ON | Displays note title and headings during review |

> [!warning]
> <span style='color: #FF00DC;'>**Do NOT**</span> enable both tag-based AND folder-based deck organization simultaneously—this creates conflicting hierarchies. Choose one organizational method and commit to it.

---

## 💳 Flashcard Creation Syntax

The SR Plugin supports multiple flashcard formats, each with specific syntax patterns. Understanding these formats allows you to choose the most appropriate structure for different types of information.

### Single-Line Format (Basic Q&A)

[<span style='color: #FFC700;'>**Single-Line Flashcard**</span>:: a flashcard where both question and answer appear on the same line, separated by `::` delimiter.] This is the simplest and most common format.

**Syntax:**
```markdown
#flashcards

Question text goes here::Answer text goes here
```

**Example:**
```markdown
#flashcards/biology/cells

The powerhouse of the cell::Mitochondria
What process produces ATP?::Cellular respiration
```

[<span style='color: #72FFF1;'>**Separator Configuration**</span>:: the `::` delimiter can be customized in Settings → Spaced Repetition → Flashcards → Single-line card separator.]

### Single-Line Reversed Format (Bidirectional)

[<span style='color: #FFC700;'>**Reversed Card**</span>:: creates TWO flashcards from a single line—one in each direction—using the `:::` delimiter (three colons).] Ideal for paired concepts, definitions, or translations.

**Syntax:**
```markdown
Term A:::Term B
```

This generates:
- **Card 1 Front**: "Term A" → **Back**: "Term B"
- **Card 2 Front**: "Term B" → **Back**: "Term A"

**Example:**
```markdown
#flashcards/language/spanish

Hola:::Hello
Buenos días:::Good morning
```

> [!principle-point]
> Reversed cards are [<span style='color: #27FF00;'>**sibling cards**</span>:: flashcards generated from the same source text that share scheduling history]. When **Bury sibling cards** is enabled, seeing one card prevents the other from appearing until the next day, avoiding immediate repetition.

### Multi-Line Format (Extended Content)

[<span style='color: #FFC700;'>**Multi-Line Flashcard**</span>:: a flashcard where question and answer are separated by a `?` on its own line, allowing for complex, multi-paragraph content on each side.]

**Syntax:**
```markdown
#flashcards

Question text here.
This can span multiple lines.
?
Answer text here.
This can also span multiple lines.
```

**Example:**
```markdown
#flashcards/programming/python

What are the key differences between lists and tuples in Python?
?
**Lists:**
- Mutable (can be modified)
- Use square brackets `[]`
- Slightly slower performance

**Tuples:**
- Immutable (cannot be modified)
- Use parentheses `()`
- Faster, lower memory footprint
```

> [!constraints-and-pitfalls]
> <span style='color: #FF00DC;'>**Critical Limitation:**</span> By default, multi-line flashcards **cannot contain blank lines** within the question or answer text. A blank line signals the end of the flashcard. To include blank lines, see the [Cards with Blank Lines](https://www.stephenmwangi.com/obsidian-spaced-repetition/flashcards/cards-with-blank-lines/) documentation for workarounds using HTML comments.

### Multi-Line Reversed Format

**Syntax:**
```markdown
Front content
Multiple lines allowed
??
Back content
Multiple lines allowed
```

This creates two bidirectional cards, just like single-line reversed but with extended content support.

### Cloze Deletions (Fill-in-the-Blank)

[<span style='color: #FFC700;'>**Cloze Deletion**</span>:: a flashcard format that hides specific words or phrases in a sentence, prompting recall of the missing information in context.] This format is particularly effective for definitions, processes, and conceptual understanding.

#### Simplified Cloze (Most Common)

**Default Delimiter:** `==highlighted text==` (standard Obsidian highlight syntax)

**Syntax:**
```markdown
#flashcards/cognitive-science

The first female prime minister of Australia was ==Julia Gillard==.

Working memory can hold approximately ==7 ± 2 items== at once.
```

**Alternative Delimiters:**
- `**bolded text**`
- `{{text in curly braces}}`
- Custom patterns via Settings → Flashcards → Cloze Patterns

> [!example]
> **Multiple Deletions in One Card:**
> ```markdown
> #flashcards/chemistry
> 
> Water has a molecular formula of ==H₂O==, consisting of ==two hydrogen atoms== and ==one oxygen atom==.
> ```
> This creates **THREE separate flashcards**, each occluding one deletion while showing the others:
> - Card 1: "Water has a molecular formula of `[...]`, consisting of two hydrogen atoms and one oxygen atom."
> - Card 2: "Water has a molecular formula of H₂O, consisting of `[...]` and one oxygen atom."
> - Card 3: "Water has a molecular formula of H₂O, consisting of two hydrogen atoms and `[...]`."

#### Classic Cloze (With Sequence Numbers)

[<span style='color: #FFC700;'>**Classic Cloze**</span>:: cloze deletions with explicit sequence numbers using footnote syntax `[^1]`, allowing multiple deletions to be grouped and hidden together on the same card.]

**Syntax:**
```markdown
#flashcards

This is a ==cloze deletion==[^1]. This is ==another one==[^2]. This ==groups with the first==[^1].
```

This generates **two cards**:
- Card 1: Hides deletions marked `[^1]` (first and third)
- Card 2: Hides deletion marked `[^2]` (second)

**With Hints:**
```markdown
This is a ==cloze==^[a hint][^1]. This is ==another==[^2].
```
The hint appears as `[a hint]` when the deletion is hidden.

> [!methodology-and-sources]
> **Cloze Overlapping Generalization** (advanced feature):
> Uses action markers to control individual deletion behavior:
> - `a` = ask (hide on front, show on back)
> - `s` = show (always visible)
> - `h` = hide (never visible)
> 
> Example:
> ```markdown
> ==Context that spoils later items==[^hshs]
> ==Item 1==[^ashh]
> ==Item 2==[^hash]
> ```

---

## 🗂️ Deck Organization Strategies

Decks are the primary organizational unit for flashcards, analogous to categories or subjects. The SR Plugin offers two mutually exclusive organization methods.

### Tag-Based Decks (Recommended for Most Users)

[<span style='color: #FFC700;'>**Tag-Based Deck**</span>:: using Obsidian's hierarchical tag system to create nested deck structures, with each tag level representing a subdeck.]

**Structure:** `#flashcards/domain/subdomain/topic`

**Example Hierarchy:**
```markdown
#flashcards                          → Root deck
#flashcards/science                  → Science deck
#flashcards/science/physics          → Physics subdeck
#flashcards/science/physics/quantum  → Quantum physics sub-subdeck
```

**Multi-Deck Assignment:**

A single card can belong to multiple decks by listing tags on the same line:

```markdown
#flashcards/biology/cells #flashcards/medicine/pathology

Cancer involves uncontrolled ==cell division==.
```

**Tag Scope Rules:**

1. **File-level tags**: Apply to ALL flashcards in the note unless overridden
2. **Section-level tags**: Apply from their position until the next tag or end of file
3. **Card-level tags**: Apply only to the specific card when placed on its first line

**Example:**
```markdown
---
tags: #flashcards/defaultdeck
---

This card inherits the file-level tag::Goes to defaultdeck

#flashcards/physics

Force equals mass times::acceleration  
<!-- This card goes to physics deck -->

#flashcards/chemistry
Molecular formula of water::H₂O  
<!-- This card goes to chemistry deck -->
```

> [!helpful-tip]
> Use [[YAML Frontmatter|frontmatter tags]] for default deck assignment, then override with inline tags for cards that belong in specialized subdecks. This minimizes tag clutter.

### Folder-Based Decks (Alternative Method)

[<span style='color: #FFC700;'>**Folder-Based Deck**</span>:: automatic deck creation based on vault folder hierarchy, where `Folder/Subfolder/File.md` maps to `Deck/Subdeck`.]

**Enable:** Settings → Spaced Repetition → Flashcards → Convert folders to decks

**Example Mapping:**
```
Vault/
├── Knowledge/
│   ├── Science/
│   │   ├── Physics.md     → Deck: Knowledge::Science
│   │   └── Chemistry.md   → Deck: Knowledge::Science
│   └── History/
│       └── Ancient.md     → Deck: Knowledge::History
```

> [!warning]
> <span style='color: #FF00DC;'>**Limitation:**</span> Folder-based decks do NOT support multi-deck assignment. A card's deck is determined solely by its file location. This is less flexible than tag-based organization.

---

## 🔄 Review Workflow & Interface

### Initiating a Review Session

There are three ways to start reviewing:

1. **Status Bar Click**: Click the review count indicator at the bottom of the Obsidian window
2. **Ribbon Icon**: Click the flashcard icon in the left sidebar (if enabled in Settings)
3. **Command Palette**: `Ctrl/Cmd + P` → "Review flashcards"

The review interface displays:
- **Card Front** (question or cloze-deleted text)
- **Context Line**: `Note Title > Heading 1 > Subheading` (if enabled)
- **Show Answer Button**: Reveals the back of the card
- **Response Buttons**: Hard, Good, Easy (after answer is revealed)

> [!what-this-does]
> **Context Display**: When **Show context in cards** is enabled, each flashcard shows the hierarchical path from note title through all parent headings to the card's location. This provides associative cues that strengthen memory encoding and prevent context-free memorization.

### Response Button Meanings

| Button | Meaning | Next Interval Effect |
|--------|---------|---------------------|
| <span style='color: #FF00DC;'>**Hard**</span> | Difficult to recall; took significant effort | Shortest interval; reduces card ease |
| <span style='color: #FFC700;'>**Good**</span> | Recalled correctly with normal effort | Moderate interval based on current ease |
| <span style='color: #27FF00;'>**Easy**</span> | Instant recall; trivial | Longest interval; increases card ease |

[<span style='color: #FFC700;'>**Card Ease**</span>:: a multiplier (default 250%) that determines how quickly intervals grow for a specific card, adjusted dynamically based on review performance.]

> [!principle-point]
> <span style='color: #27FF00;'>**Honest Self-Assessment Principle:**</span> The algorithm's effectiveness depends on accurate button selection. Consistently choosing "Good" when you struggled (or vice versa) degrades scheduling accuracy. Use "Hard" without guilt—it's information, not failure.

### Cramming Mode (Optional Review)

**Access:** Command Palette → "Cram flashcards"

[<span style='color: #FFC700;'>**Cramming**</span>:: reviewing flashcards outside the normal scheduling algorithm without affecting their scheduling data—useful for exam preparation or knowledge refreshing.]

Cramming sessions:
- Present cards regardless of due date
- Do NOT update scheduling information
- Useful for pre-exam review or confidence building

---

## 📝 Whole-Note Review

Beyond flashcards, the SR Plugin supports reviewing **entire notes** at scheduled intervals. This is ideal for:
- **Conceptual reinforcement**: Revisiting complex topics to deepen understanding
- **Synthesis notes**: Periodically reviewing [[Maps of Content (MOCs)|MOCs]] or summary documents
- **Project notes**: Scheduled check-ins on active projects or research areas

### Tagging Notes for Review

Add the `#review` tag anywhere in the note (typically in frontmatter):

```markdown
---
tags: [#review, #project/active]
---

# Project Strategy Document

...content...
```

> [!helpful-tip]
> Notes tagged with `#review` do NOT immediately appear in the review queue. You must first click the **status bar** or use the **"Open note review queue"** command to initialize the queue.

### Note Review Workflow

1. Tag note with `#review`
2. Click status bar or use command: "Open notes review queue in sidebar"
3. Review interface displays the note in **reading mode**
4. After reviewing, right-click the note in queue → Select rating:
   - **Easy**: Long interval (e.g., 30 days)
   - **Good**: Moderate interval (e.g., 10 days)
   - **Hard**: Short interval (e.g., 3 days)
5. Scheduling data is added to the note's frontmatter:

```markdown
---
sr-due: 2025-12-24
sr-interval: 10
sr-ease: 250
---
```

> [!important-links]
> **Note Review vs. Flashcard Review:**
> - **Flashcards**: Focused, atomic knowledge testing
> - **Note Review**: Holistic understanding and concept reinforcement
> 
> These are complementary strategies—use both for comprehensive learning.

---

## 🧮 Scheduling Algorithm: SM-2-OSR

The SR Plugin implements <span style='color: #72FFF1;'>**SM-2-OSR**</span> (SuperMemo-2 Obsidian Spaced Repetition), a variant of the classic [[SuperMemo|SM-2 algorithm]] with Obsidian-specific enhancements.

### Core Algorithm Principles

[<span style='color: #FFC700;'>**SM-2 Algorithm**</span>:: a spaced repetition scheduling algorithm developed by Piotr Woźniak in 1987 that uses exponentially increasing intervals adjusted by user performance ratings.]

**Key Variables:**

- [<span style='color: #72FFF1;'>**Interval**</span>:: number of days until the card is next due for review]
- [<span style='color: #72FFF1;'>**Ease Factor**</span>:: multiplier determining interval growth rate (minimum 130%, typical start 250%)]
- [<span style='color: #72FFF1;'>**Repetition Count**</span>:: number of successful reviews for the current card]

**Interval Calculation (Simplified):**

```python
# After a "Good" response:
new_interval = previous_interval * ease_factor

# After "Hard":
ease_factor -= 0.15  # Reduce ease
new_interval = previous_interval * 1.2

# After "Easy":
ease_factor += 0.15  # Increase ease  
new_interval = previous_interval * ease_factor * easy_bonus
```

> [!equation]
> **Initial Ease Calculation (OSR Enhancement):**
> 
> If a note has backlinks (linked notes):
> ```
> link_contribution = max_link_factor × min(1.0, log(link_count + 0.5) / log(64))
> initial_ease = (1 - link_contribution) × base_ease + link_contribution × average_ease
> ```
> 
> This means cards in well-connected notes start with higher ease, reflecting the assumption that densely linked knowledge is easier to recall due to multiple retrieval pathways.

### Configurable Parameters

Navigate to **Settings → Spaced Repetition → Algorithm** to adjust:

| **Parameter** | **Default** | **Effect** |
|---------------|-------------|-----------|
| <span style='color: #72FFF1;'>Base ease</span> | 250% | Starting ease for new cards |
| <span style='color: #72FFF1;'>Easy bonus</span> | 130% | Additional interval multiplier for "Easy" responses |
| <span style='color: #72FFF1;'>Hard interval</span> | 1.2× | Interval multiplier for "Hard" responses |
| <span style='color: #72FFF1;'>Maximum interval</span> | 365 days | Cap on how far out a card can be scheduled |
| <span style='color: #72FFF1;'>Max link factor</span> | 1.0 | Weight given to backlink-based ease adjustment |

> [!warning]
> <span style='color: #FF00DC;'>**Advanced Users Only:**</span> Modifying algorithm parameters requires understanding their interactions. Aggressive changes can destabilize scheduling. Start with defaults and adjust incrementally based on empirical observation of your review burden.

### Future Algorithm: FSRS

[<span style='color: #FFC700;'>**FSRS (Free Spaced Repetition Scheduler)**</span>:: a next-generation algorithm developed by the Open Spaced Repetition community that uses machine learning-optimized parameters and achieves 20-30% fewer reviews for equivalent retention compared to SM-2.]

**Status:** Not yet implemented in the main SR Plugin (as of December 2024). A fork called [[Obsidian Spaced Repetition Recall|obsidian-spaced-repetition-recall]] includes FSRS support.

**Planned Features:**
- Automatic parameter optimization based on review history
- Four-button response system (Again, Hard, Good, Easy)
- More accurate retention predictions

---

## 🛠️ Advanced Features & Customization

### Card Context Customization

**Settings → Flashcards → Show context in cards**

When enabled, displays a breadcrumb trail above each flashcard:

```
Note Title > Section Heading > Subsection
```

This feature:
- Provides **retrieval cues** that strengthen memory encoding
- Prevents **context-free memorization** (knowing the answer but not its significance)
- Helps distinguish between similar cards from different domains

> [!analogy]
> Think of card context like a file path in your knowledge base—it tells you not just *what* the information is, but *where it lives* in your conceptual architecture.

### Burying Sibling Cards

**Settings → Flashcards → Bury sibling cards until the next day**

[<span style='color: #FFC700;'>**Card Burying**</span>:: temporarily removing sibling cards from the current review session to prevent revealing related information, resurfacing them the next day.]

**Affects:**
- Reversed cards (both directions of a bidirectional card)
- Multiple cloze deletions from the same source text

**Rationale:** If you see "Front→Back" for a reversed card, seeing "Back→Front" immediately afterward provides no learning benefit—you just saw the answer.

> [!principle-point]
> Enable this unless you specifically want to test bidirectional recall in the same session (rare use case).

### Statistics & Analytics

**Access:** Command Palette → "View statistics"

The statistics panel provides:
- **Review Forecast**: Number of cards due each day for the next 30 days
- **Card Type Breakdown**: Distribution of new, learning, and mature cards
- **Deck-Specific Stats**: Per-deck retention rates and review counts
- **Daily Review Count**: Historical tracking of reviews completed

Use this data to:
- Identify overloaded decks requiring cleanup
- Assess retention rates (goal: >85% for most material)
- Balance daily review burden

### Custom Cloze Patterns (Advanced)

**Settings → Flashcards → Cloze Patterns**

You can define custom delimiters beyond `==highlight==`:

**Example Custom Pattern (Anki-Style):**
```
{{c1::answer::hint}}
```

Pattern structure uses placeholders:
- `[123]` = sequence number
- `answer` = the deleted text
- `hint` = optional hint text

**Configuration:**
```
{{[123::]answer[::hint]}}
```

> [!warning]
> <span style='color: #FF00DC;'>**Conflict Alert:**</span> Ensure custom cloze patterns do NOT overlap with other flashcard separators. For example, the pattern `{{[123::]answer[::hint]}}` conflicts with the default `::` single-line separator.

---

## 📊 Data Storage & Portability

### Scheduling Data Location

The SR Plugin stores scheduling information **directly in your notes** using HTML comments:

```markdown
What is the capital of France?::Paris
<!--SR:!2025-12-20,15,250-->
```

**Format:** `<!--SR:!due-date,interval,ease-->`

> [!core-principle]
> **Plaintext Storage Philosophy:**
> 
> By embedding scheduling data in markdown files rather than a separate database, the plugin ensures:
> 1. **Portability**: Your notes remain functional if you switch tools
> 2. **Version Control**: Git can track scheduling history
> 3. **No Database Corruption**: No risk of losing all progress due to database file corruption
> 
> <span style='color: #FF00DC;'>**Trade-off:**</span> This approach modifies your note files. If you prefer pristine notes, consider the [[Obsidian Spaced Repetition Recall]] fork which uses external JSON storage.

### Backup Strategy

Since scheduling data lives in your notes:
1. **Your vault backup = your review progress backup**
2. Use [[Obsidian Git]] or similar plugins for automatic version control
3. Exclude scheduling comments from published notes using [[Obsidian Publish|publish]] settings

### Migrating from Anki

If transitioning from [[Anki]]:
1. Export Anki decks as markdown
2. Reformat cards using SR Plugin syntax
3. Manually set initial intervals using `<!--SR:!due-date,interval,ease-->`

*Note: No automated import tool currently exists.*

---

## 🎯 Best Practices for Effective Spaced Repetition

### Card Design Principles

> [!principle-point]
> **Atomic Card Principle:**
> 
> Each flashcard should test **one** piece of information. Complex multi-part questions should be split into multiple cards.

**Bad:**
```markdown
What are the differences between mitosis and meiosis, and what are their purposes?::
Mitosis produces two identical diploid cells for growth and repair. 
Meiosis produces four genetically diverse haploid cells for sexual reproduction.
```

**Good:**
```markdown
How many cells does mitosis produce?::Two

Are mitosis daughter cells identical or diverse?::Identical

What is the chromosome count of mitosis daughter cells?::Diploid (same as parent)

What is the primary purpose of mitosis?::Growth and tissue repair

How many cells does meiosis produce?::Four

What is the chromosome count of meiosis daughter cells?::Haploid (half of parent)
```

### Use Cloze for Contextual Learning

Cloze deletions preserve sentence structure, making them ideal for:
- Definitions embedded in explanatory text
- Process descriptions
- Technical concepts requiring context

**Example:**
```markdown
#flashcards/cognitive-science

The ==testing effect== demonstrates that retrieving information from memory strengthens that memory more than ==re-reading== the same material.
```

This is superior to decontextualized Q&A:
```markdown
What is the testing effect?::Retrieval strengthens memory more than re-reading
```

### Leverage Hierarchical Tags for Progressive Disclosure

Structure your decks to support learning progressions:

```
#flashcards/math
#flashcards/math/basics       ← Master fundamentals first
#flashcards/math/algebra      ← Build on basics
#flashcards/math/calculus     ← Advanced applications
```

Review broader decks (#flashcards/math) to ensure comprehensive coverage, or narrow decks for focused study.

### Regular Maintenance Rituals

1. **Weekly Deck Review**: Assess retention rates, identify problem cards
2. **Card Improvement**: Rewrite cards with <80% retention
3. **Pruning**: Delete or suspend cards for outdated/irrelevant information
4. **Tag Reorganization**: Refactor deck hierarchy as your knowledge evolves

> [!helpful-tip]
> **Suspend vs. Delete:**
> - **Suspend**: Comment out the card with HTML comments to preserve it but remove from review queue
> - **Delete**: Completely remove card text and scheduling data
> 
> Prefer suspension for temporarily irrelevant material you might need later.

---

## 🐛 Troubleshooting Common Issues

### Cards Not Appearing in Review Queue

**Possible Causes:**

1. **Missing deck tag**: Ensure notes contain `#flashcards` or your configured tag
2. **Incorrect syntax**: Verify separator (`::` for single-line, `?` for multi-line)
3. **Cards not due**: Check status bar count—zero due cards is normal if all reviews current
4. **Plugin not loaded**: Confirm plugin is enabled in Settings → Community plugins

**Diagnostic Steps:**

1. Open Command Palette → "Rebuild flashcard index"
2. Check status bar for updated count
3. Manually inspect note for correct syntax and tags

### Cloze Deletions Not Working

**Common Mistakes:**

1. **Wrong delimiter**: Default is `==highlight==`, not `**bold**` (unless configured)
2. **Missing deck tag**: Cloze cards still require `#flashcards` or equivalent
3. **Conflicting custom pattern**: If using custom cloze syntax, ensure it's properly configured
4. **Blank lines in multi-line cloze**: Standard cloze doesn't support blank lines within deletion

**Fix:**
```markdown
# Correct
#flashcards/test

The first president was ==George Washington==.

# Incorrect (missing deck tag)
The first president was ==George Washington==.
```

### Scheduling Data Not Persisting

**Issue:** Review progress resets after reopening vault.

**Cause:** Plugin failed to write scheduling comments to file.

**Solutions:**

1. **Check file permissions**: Ensure vault folder is writable
2. **Disable conflicting plugins**: Some editing plugins may interfere
3. **Review settings**: Confirm "Store scheduling comment on the same line" is OFF (default)

### Performance Issues with Large Vaults

**Symptom:** Lag when opening review interface or updating statistics.

**Optimizations:**

1. **Exclude folders**: Settings → Flashcards → Folders to ignore (exclude large archives)
2. **Reduce deck count**: Consolidate fragmented subdecks
3. **Limit card context**: Disable "Show context in cards" if unnecessary
4. **Archive mature cards**: Move well-learned cards to separate "archive" deck reviewed quarterly

---

## 🔗 Integration with Other Obsidian Workflows

### PKM System Integration

The SR Plugin complements various [[Personal Knowledge Management]] methodologies:

**With [[Zettelkasten]]:**
- Create atomic notes with embedded flashcards
- Use `#flashcards` tags to mark evergreen notes for review
- Leverage backlink-based ease adjustment (OSR's PageRank feature)

**With [[PARA Method]]:**
- Store flashcards in relevant PARA categories:
  - **Projects**: Active learning materials
  - **Areas**: Ongoing knowledge domains (#flashcards/areas/finance)
  - **Resources**: Reference flashcards
  - **Archives**: Suspended/historical cards

**With [[Linking Your Thinking (LYT)]]:**
- Embed flashcards in [[Maps of Content (MOCs)|MOCs]] for domain-specific review
- Use whole-note review for periodic MOC reinforcement

### Plugin Synergies

**[[Dataview]]:**
Query cards with specific properties:
```dataview
TABLE file.name AS "Note", file.tags AS "Tags"
FROM #flashcards
WHERE contains(file.name, "Python")
```

**[[Templater]]:**
Auto-generate flashcard templates:
```javascript
---
tags: [#flashcards/<% tp.file.folder() %>]
---

## Flashcards

<% tp.file.cursor(1) %>
```

**[[Tasks Plugin]]:**
Track "Create flashcards for X" tasks:
```markdown
- [ ] Convert [[Cognitive Load Theory]] notes to flashcards #task/learning
```

---

## 🧭 Further Exploration

### Related Concepts for PKB Expansion

1. **[[Spaced Repetition Theory]]**
   - *Connection*: Theoretical foundation underlying the SR Plugin's scheduling algorithms
   - *Depth Potential*: Understanding forgetting curves, retention functions, and optimal spacing
   - *Knowledge Graph Role*: Core learning science concept connecting to memory, [[Cognitive Psychology]], and [[Educational Technology]]

2. **[[SuperMemo Algorithm (SM-2)]]**
   - *Connection*: The scheduling algorithm implemented by the SR Plugin
   - *Depth Potential*: Historical development, mathematical formulation, and comparative analysis with newer algorithms like [[FSRS Algorithm|FSRS]]
   - *Knowledge Graph Role*: Bridges computer science, cognitive science, and learning optimization

3. **[[Effective Flashcard Design]]**
   - *Connection*: Principles for creating high-quality flashcards that maximize retention
   - *Depth Potential*: Atomic card principle, context preservation, mnemonic techniques, multi-modal learning
   - *Knowledge Graph Role*: Practical application of [[Cognitive Load Theory]], [[Dual Coding Theory]], and [[Desirable Difficulties]]

4. **[[Active Recall vs. Passive Review]]**
   - *Connection*: The cognitive mechanism that makes spaced repetition effective
   - *Depth Potential*: Testing effect, retrieval practice, production effect, generation effect
   - *Knowledge Graph Role*: Foundational concept in [[Learning Science]], connecting to [[Metacognition]] and [[Study Strategies]]

---

**Last Updated:** 2024-12-14  
**Plugin Version Documented:** 1.13.4+  
**Official Documentation:** https://www.stephenmwangi.com/obsidian-spaced-repetition/

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
