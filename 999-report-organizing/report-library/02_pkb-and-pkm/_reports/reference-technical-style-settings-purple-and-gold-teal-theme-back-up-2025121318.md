---
aliases:
  - "Style Settings"
  - "Back up"
tags:
  - "type/report"
  - "year/2025"
  - "type/template"
  - "status/proven"
  - "pkb"
  - "pkm"
  - "synthesis-workflow"
  - "self-improvement/productivity"
  - "instructional-design-pkm"
  - "cognitive-resources"
  - "pkb/optimization"
  - "automation"
  - "cognitive-pkm"
source: "original-synthesis"
id: "20251213190059"
created: "2025-12-13T19:00:59"
modified: "2025-12-13T19:00:59"
week: "[[2025-W50]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: "reference"
maturity: "seedling"
confidence: "provisional"
next-review: "2025-12-20"
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-13|Daily-Note]]"
---

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Style Setting Back Up]]
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

##### Style Setting Back Up

```
{
  "minimal-style@@bg2@@dark": "#25212E",
  "minimal-style@@bg3@@dark": "#2D2838",
  "minimal-style@@ui2@@dark": "#7800F4",
  "minimal-style@@ax1@@dark": "#FFC700",
  "minimal-style@@ax2@@dark": "#FFE066",
  "minimal-theme@@color-accent-light": "#BE93FD",
  "minimal-theme@@color-accent-dark": "#BE93FD",
  "minimal-theme@@color-bg-primary-light": "#fcfcfc",
  "minimal-theme@@color-bg-secondary-light": "#f2f2f7",
  "minimal-theme@@color-bg-primary-dark": "#1c1c1e",
  "minimal-theme@@color-bg-secondary-dark": "#2c2c2e",
  "minimal-theme@@color-text-primary-light": "#1c1c1e",
  "minimal-theme@@color-text-primary-dark": "#f2f2f7",
  "minimal-theme@@color-text-normal-light": "#1c1c1e",
  "minimal-theme@@color-text-normal-dark": "#f2f2f7",
  "minimal-theme@@color-text-secondary-light": "#6e6e73",
  "minimal-theme@@color-text-secondary-dark": "#8d8d93",
  "minimal-theme@@color-text-faint-light": "#999999",
  "minimal-theme@@color-text-faint-dark": "#777777",
  "minimal-theme@@color-interactive-accent-light": "#BE93FD",
  "minimal-theme@@color-interactive-accent-dark": "#BE93FD",
  "minimal-theme@@link-unresolved-color-light": "#a8a8a8",
  "minimal-theme@@link-unresolved-color-dark": "#7a7a7a",
  "minimal-theme@@code-background-light": "#f2f2f7",
  "minimal-theme@@code-background-dark": "#2c2c2e",
  "minimal-style@@file-header-justify": "center",
  "minimal-style@@tag-color@@dark": "#FFC700",
  "minimal-style@@tag-background@@dark": "#212324",
  "minimal-style@@tag-background-hover@@dark": "#282838",
  "minimal-style@@tag-radius": "14px",
  "minimal-style@@minimal-tab-text-color@@dark": "#FFC700",
  "minimal-style@@minimal-tab-text-color-active@@dark": "#EAEAEA",
  "minimal-style@@row-lines": true,
  "minimal-style@@col-lines": true,
  "minimal-style@@table-lines": false,
  "minimal-style@@row-alt": true,
  "minimal-style@@col-alt": true,
  "minimal-style@@table-tabular": false,
  "minimal-style@@table-numbers": false,
  "minimal-style@@table-center": true,
  "minimal-style@@table-nowrap": false,
  "minimal-style@@row-hover": true,
  "minimal-style@@table-row-background-hover@@dark": "#4F00FF47",
  "minimal-style@@maximize-tables-off": "maximize-tables",
  "minimal-style@@ribbon-style": "ribbon-bottom-left-hover",
  "minimal-style@@sidebar-tabs-style": "sidebar-tabs-wide",
  "minimal-style@@hide-help": false,
  "minimal-style@@hide-settings": false,
  "minimal-style@@sidebar-tabs-names": "tab-names-single",
  "minimal-style@@metadata-heading-off": true,
  "minimal-style@@metadata-add-property-off": true,
  "minimal-style@@metadata-icons-off": false,
  "minimal-style@@metadata-dividers": true,
  "minimal-style@@progress-complete@@dark": "#BE93FD",
  "minimal-style@@pdf-page-style": "pdf-shadows-on",
  "minimal-style@@pdf-invert-dark": false,
  "minimal-style@@checkbox-shape": "checkbox-square",
  "minimal-style@@minimal-strike-lists": true,
  "minimal-style@@active-line-on": true,
  "minimal-style@@workspace-background-translucent@@dark": "#7800F420",
  "minimal-style@@indentation-guide-color-active@@dark": "#FFC700",
  "minimal-style@@indentation-guide-color@@dark": "#7D00FF",
  "minimal-style@@icon-color@@dark": "#FFC700",
  "minimal-style@@icon-color-hover@@dark": "#00FFEF",
  "minimal-style@@icon-color-focused@@dark": "#7D00FF",
  "minimal-style@@embed-strict": false,
  "minimal-style@@embed-underline": false,
  "minimal-style@@dataview-inline-lists": true,
  "minimal-style@@callouts-style": "callouts-default",
  "minimal-style@@h1-l": true,
  "minimal-style@@h2-l": true,
  "minimal-style@@h3-l": false,
  "minimal-style@@h4-l": false,
  "minimal-style@@h5-l": false,
  "minimal-style@@h6-l": false,
  "minimal-style@@bold-color@@dark": "#FFC700",
  "minimal-style@@tx2@@dark": "#EAEAEA",
  "minimal-style@@tx3@@dark": "#EAEAEA",
  "minimal-style@@tx1@@dark": "#EAEAEA",
  "minimal-style@@h1-font": "Jetbrains Mono",
  "minimal-style@@h2-font": "Jetbrains Mono",
  "minimal-style@@h3-color@@dark": "#D2C170",
  "minimal-style@@h4-color@@dark": "#00FFEF",
  "minimal-style@@h5-color@@dark": "#C071FA",
  "minimal-style@@h6-color@@dark": "#A6FFFD",
  "minimal-style@@h6-font": "Jetbrains Mono",
  "minimal-style@@h5-font": "Jetbrains Mono",
  "minimal-style@@h4-font": "Jetbrains Mono",
  "minimal-style@@h3-font": "Jetbrains Mono",
  "minimal-style@@h4-weight": 100,
  "minimal-style@@minimal-code-scroll": false,
  "minimal-advanced@@hide-markdown": false,
  "minimal-advanced@@hide-settings-desc": false,
  "minimal-advanced@@animations": "default",
  "minimal-style@@trim-cols": true,
  "minimal-style@@inline-title-font": "Jetbrains Mono",
  "minimal-style@@file-header-visibility": "minimal-tab-title-hover",
  "minimal-style@@blockquote-font-style": "normal",
  "minimal-style@@image-grid-fit": "cover",
  "minimal-style@@list-indent": 1.3,
  "minimal-style@@code-function@@dark": "#9E6AD3",
  "minimal-style@@code-string@@dark": "#B58900",
  "minimal-style@@code-operator@@dark": "#D33682",
  "minimal-style@@code-punctuation@@dark": "#839496",
  "minimal-style@@code-important@@dark": "#CB4B16",
  "minimal-style@@code-property@@dark": "#9E6AD3",
  "minimal-style@@code-comment@@dark": "#7A00FF",
  "minimal-style@@ax3@@dark": "#FFC700",
  "minimal-style@@color-yellow@@dark": "#A5FF00",
  "minimal-style@@color-green@@dark": "#27FF00",
  "minimal-style@@color-cyan@@dark": "#00FFEA",
  "minimal-style@@color-blue@@dark": "#006CFF",
  "minimal-style@@color-purple@@dark": "#9E6AD3",
  "minimal-style@@color-pink@@dark": "#FF00DC",
  "minimal-style@@h1-color@@dark": "#FFC700",
  "minimal-style@@h2-color@@dark": "#8000FF",
  "minimal-style@@h6-variant": "all-small-caps",
  "minimal-style@@h5-variant": "all-small-caps",
  "minimal-style@@h4-variant": "all-small-caps",
  "minimal-style@@text-formatting@@dark": "#FFC700",
  "minimal-style@@bold-modifier": 100,
  "minimal-style@@file-header-font-weight": 100,
  "minimal-style@@inline-title-color@@dark": "#72FFF1",
  "minimal-style@@inline-title-weight": 100,
  "minimal-style@@frame-background@@dark": "#25212E",
  "minimal-style@@blockquote-color@@dark": "#EAEAEA",
  "minimal-style@@code-background@@dark": "#18151D",
  "minimal-style@@code-normal@@dark": "#EAEAEA",
  "minimal-style@@blockquote-background-color@@dark": "#1E1B24",
  "minimal-style@@sp1@@dark": "#EAEAEA",
  "minimal-style@@color-red@@dark": "#FF0000",
  "minimal-style@@color-orange@@dark": "#FF5700",
  "minimal-style@@h1-variant": "all-small-caps",
  "minimal-style@@h2-variant": "all-small-caps",
  "minimal-style@@h3-variant": "all-small-caps",
  "minimal-style@@gutter-background@@dark": "#25212E",
  "minimal-style@@line-number-color@@dark": "#8d8d93",
  "minimal-style@@checkbox-color@@dark": "#FFC700",
  "minimal-style@@h2-weight": 100,
  "minimal-style@@h1-weight": 200,
  "minimal-style@@h3-weight": 200,
  "minimal-style@@h5-weight": 100,
  "minimal-style@@h6-weight": 100,
  "id@@callout-on": true,
  "id@@h1-underline": true,
  "id@@h2-underline": true,
  "id@@headers-one-color": true,
  "minimal-style@@blockquote-border-color@@dark": "#FFC700",
  "minimal-style@@embed-max-height": "1000",
  "minimal-style@@embed-background@@dark": "#101010",
  "minimal-style@@embed-hide-title": false,
  "minimal-style@@embed-decoration-style": "dashed",
  "minimal-style@@embed-decoration-color@@dark": "#9E6AD3",
  "minimal-style@@code-size": "0.93em",
  "minimal-style@@link-external-color-hover@@dark": "#FFC700",
  "minimal-style@@link-external-color@@dark": "#828282",
  "minimal-style@@link-color@@dark": "#72FFF1",
  "minimal-style@@link-color-hover@@dark": "#FFC700",
  "minimal-style@@link-unresolved-color@@dark": "#D4B832",
  "minimal-style@@blockquote-size": "20",
  "minimal-style@@blockquote-border-thickness": 5,
  "minimal-style@@h1-size": "3.2em",
  "minimal-style@@h1-style": "normal",
  "minimal-style@@h2-style": "normal",
  "minimal-style@@h2-size": "2.8em",
  "minimal-style@@h3-size": "2.4em",
  "minimal-style@@h4-size": "2.0em",
  "minimal-style@@h5-size": "1.8em",
  "minimal-style@@h6-size": "1.4em",
  "minimal-style@@list-spacing": 0.015,
  "minimal-style@@metadata-label-width-multiplier": 11,
  "minimal-style@@vault-profile-display": "vault-profile-default",
  "minimal-style@@minimal-unstyled-tags": false,
  "minimal-style@@tag-border-width": "1px",
  "minimal-style@@file-header-font-size": "1.25em",
  "minimal-style@@inline-title-size": "1.6em",
  "minimal-style@@bg1@@dark": "#1E1B24",
  "minimal-cards-style@@cards-min-width": "200x",
  "minimal-advanced@@cursor": "default",
  "minimal-style@@tabs-style": "tabs-modern",
  "minimal-style@@hl2@@dark": "#CCB20047",
  "minimal-style@@hl1@@dark": "#5E00FF47",
  "minimal-style@@p-spacing": "1.3.7rem",
  "minimal-style@@title-color@@dark": "#5400FF",
  "minimal-style@@title-color-inactive@@dark": "#7E00FF",
  "minimal-style@@window-title-off": true,
  "minimal-style@@frame-icon-color@@dark": "#7E00FF",
  "minimal-style@@titlebar-text-color-focused@@dark": "#FFD400",
  "minimal-style@@titlebar-text-color@@dark": "#6900FF",
  "minimal-style@@titlebar-text-weight": 200,
  "minimal-style@@italic-color@@dark": "#D1A1FF",
  "minimal-advanced@@font-ui-small": 16,
  "minimal-advanced@@font-ui-smaller": 16,
  "minimal-style@@bases-table-row-height": 40,
  "checkbox@@checkbox-strike-regular": false,
  "checkbox@@checkbox-strike-checked": true,
  "minimal-style@@ui3@@dark": "#7800F4",
  "minimal-style@@ui1@@dark": "#3D007C",
  "minimal-style@@max-col-width": "18em",
  "minimal-style@@callout-blend-mode": "var(--highlight-mix-blend-mode)",
  "minimal-style@@icon-color-active@@dark": "#3D007C",
  "minimal-style@@link-unresolved-decoration-color@@dark": "#7D00FF",
  "minimal-style@@link-unresolved-opacity": 0.7
  }

```

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
