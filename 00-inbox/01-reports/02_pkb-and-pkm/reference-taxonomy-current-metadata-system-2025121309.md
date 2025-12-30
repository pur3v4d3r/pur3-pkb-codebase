---
aliases:
  - Quick Reference
  - Metadata Quick Reference
  - Dataview Query Reference
  - DQL Cheatsheet
  - Metadata Query Guide
tags:
  - type/report
  - year/2025
  - type/analysis
  - status/evergreen
  - pkb
  - pkm
  - metadata-systems
  - cognitive-science/cognitive-load
  - cognitive-load-management
  - cognitive-resources
  - pkb/optimization
  - cognitive-pkm
  - quick-reference
source: documentation
id: "20251213093655"
created: 2025-12-13T09:36:55
modified: 2025-12-13T09:36:55
week: "[[2025-W50]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: reference
maturity: budding
confidence: established
next-review: 2025-12-20
review-count: 0
link-up:
  - "[[pkb-&-pkm-moc]]"
link-related:
  - "[[2025-12-13|Daily-Note]]"
---

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Metadata System Quick Reference]]
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

### Metadata System Quick Reference
> [! ] I'll create comprehensive quick reference tables for Dataview metadata queries based on the template structure. These tables will be organized by query type and complexity level.

tags: #obsidian #dataview #reference-note #quick-reference
aliases: [Dataview Query Reference, DQL Cheatsheet, Metadata Query Guide]

---

# 📊 Dataview Metadata Query Quick Reference

> [!abstract] Purpose
> Comprehensive quick-reference tables for querying metadata in Obsidian using [[Dataview]]. Organized by common use cases with ready-to-use query patterns.

---
# Claude Sonnet 4.5 Quick Reference
## 🎯 Core Metadata Fields Reference

> [!definition] Standard Template Metadata
> Based on the permanent note template structure, these are the queryable fields available in every note.

| Field Name | Type | Example Value | Query Usage |
|------------|------|---------------|-------------|
| `type` | String | `"permanent-note"` | `WHERE type = "permanent-note"` |
| `source` | String | `"claude-sonnet-4.5"` | `WHERE source = "claude-sonnet-4.5"` |
| `maturity` | String | `"evergreen"` | `WHERE maturity = "evergreen"` |
| `confidence` | String | `"high"` | `WHERE confidence = "high"` |
| `created` | DateTime | `"2025-12-13T14:30:00"` | `WHERE created >= date(2025-12-01)` |
| `modified` | DateTime | `"2025-12-13T14:30:00"` | `WHERE modified <= date(today)` |
| `next-review` | Date | `"2025-12-20"` | `WHERE next-review < date(today)` |
| `review-count` | Number | `5` | `WHERE review-count > 0` |
| `tags` | List | `["type/permanent", "cognitive-science"]` | `WHERE contains(tags, "cognitive-science")` |
| `link-up` | List | `["[[cognitive-science-moc]]"]` | `WHERE contains(link-up, [[cognitive-science-moc]])` |
| `week` | Link | `"[[2025-W50]]"` | `WHERE week = [[2025-W50]]` |
| `month` | Link | `"[[2025-12]]"` | `WHERE month = [[2025-12]]` |
| `quarter` | Link | `"[[2025-Q4]]"` | `WHERE quarter = [[2025-Q4]]` |
| `year` | Link | `"[[2025]]"` | `WHERE year = [[2025]]` |

---

## 📋 Query Pattern Tables by Use Case

### 1️⃣ Status & Maturity Queries

> [!helpful-tip] Use Case
> Track note development stages, identify notes needing review, monitor confidence levels.

| Query Goal | DQL Pattern | Result |
|------------|-------------|---------|
| All seedling notes | `LIST WHERE maturity = "seedling"` | Simple list of immature notes |
| Evergreen high-confidence notes | `TABLE confidence, created WHERE maturity = "evergreen" AND confidence = "high"` | Table showing stable knowledge |
| Notes needing review (overdue) | `TABLE next-review, maturity WHERE next-review < date(today)` | Overdue review items |
| Notes by maturity distribution | `TABLE maturity, length(rows) GROUP BY maturity` | Count per maturity level |
| Low confidence notes for revision | `LIST WHERE confidence IN ["speculative", "provisional"]` | Notes needing verification |
| Recent seedlings (last 7 days) | `TABLE created, source WHERE maturity = "seedling" AND created >= date(today) - dur(7 days)` | New immature notes |

**DataviewJS Advanced Pattern:**
```dataviewjs
// Maturity progression tracker
const maturityOrder = ["seedling", "budding", "developing", "evergreen"];
const pages = dv.pages('"Path/To/Notes"')
    .groupBy(p => p.maturity)
    .map(g => ({
        Maturity: g.key,
        Count: g.rows.length,
        "Avg Reviews": Math.round(g.rows.map(r => r["review-count"]).reduce((a,b) => a+b, 0) / g.rows.length)
    }))
    .sort(p => maturityOrder.indexOf(p.Maturity));

dv.table(["Maturity", "Count", "Avg Reviews"], pages.map(p => [p.Maturity, p.Count, p["Avg Reviews"]]));
```

---

### 2️⃣ Temporal / Date-Based Queries

> [!helpful-tip] Use Case
> Find notes by creation date, track modification patterns, identify stale content.

| Query Goal | DQL Pattern | Result |
|------------|-------------|---------|
| Notes created this week | `LIST WHERE week = [[2025-W50]]` | This week's notes |
| Notes modified today | `TABLE modified WHERE modified >= date(today)` | Today's edits |
| Notes created in December | `LIST WHERE month = [[2025-12]]` | Monthly notes |
| Notes older than 90 days | `TABLE created, maturity WHERE created < date(today) - dur(90 days)` | Potentially stale notes |
| Notes modified in last 7 days | `TABLE modified, type WHERE modified >= date(today) - dur(7 days)` | Recent activity |
| Q4 2025 notes | `LIST WHERE quarter = [[2025-Q4]]` | Quarterly notes |
| Notes created between dates | `TABLE created WHERE created >= date(2025-12-01) AND created <= date(2025-12-13)` | Date range filter |
| Unmodified since creation | `LIST WHERE created = modified` | Never-revised notes |

**DataviewJS Advanced Pattern:**
```dataviewjs
// Staleness report (last modified analysis)
const now = dv.date('today');
const pages = dv.pages('"Path/To/Notes"')
    .map(p => {
        const daysSince = (now.diff(p.modified, 'days')).days;
        return {
            File: p.file.link,
            "Days Since Edit": daysSince,
            Status: daysSince > 180 ? "🕸️ Stale" : daysSince > 30 ? "🍂 Cold" : "🔥 Fresh"
        };
    })
    .sort(p => p["Days Since Edit"], "desc");

dv.table(["File", "Days Since Edit", "Status"], pages.map(p => [p.File, p["Days Since Edit"], p.Status]));
```

---

### 3️⃣ Source & Type Queries

> [!helpful-tip] Use Case
> Filter by origin (AI model, book, article), categorize by note type.

| Query Goal | DQL Pattern | Result |
|------------|-------------|---------|
| All Claude-generated notes | `LIST WHERE contains(source, "claude")` | Claude-sourced notes |
| Permanent notes only | `TABLE maturity, created WHERE type = "permanent-note"` | Core atomic notes |
| Literature notes from books | `LIST WHERE type = "literature" AND source = "book"` | Book summaries |
| AI-generated reports | `TABLE source, created WHERE type = "report" AND contains(source, "claude" OR "gemini")` | AI reports |
| Reference notes needing review | `TABLE next-review WHERE type = "reference" AND next-review < date(today)` | Overdue references |
| Original synthesis notes | `LIST WHERE source = "original-synthesis"` | User-created content |
| Gemini vs Claude output | `TABLE source, type GROUP BY source WHERE contains(source, "gemini" OR "claude")` | AI source comparison |

**DataviewJS Advanced Pattern:**
```dataviewjs
// Source distribution by type
const pages = dv.pages('"Path/To/Notes"')
    .groupBy(p => p.type)
    .map(g => ({
        Type: g.key,
        "Total": g.rows.length,
        "Claude": g.rows.filter(r => r.source?.includes("claude")).length,
        "Gemini": g.rows.filter(r => r.source?.includes("gemini")).length,
        "Human": g.rows.filter(r => r.source === "original-synthesis").length
    }));

dv.table(["Type", "Total", "Claude", "Gemini", "Human"], 
    pages.map(p => [p.Type, p.Total, p.Claude, p.Gemini, p.Human]));
```

---

### 4️⃣ Tag-Based Queries

> [!helpful-tip] Use Case
> Filter by hierarchical tags, domain categories, metadata tags.

| Query Goal | DQL Pattern | Result |
|------------|-------------|---------|
| Cognitive science notes | `LIST WHERE contains(tags, "cognitive-science")` | Domain-filtered |
| Permanent notes in PKM domain | `TABLE maturity WHERE type = "permanent-note" AND contains(tags, "pkm")` | Domain + type filter |
| Notes with specific tag path | `LIST WHERE contains(tags, "cognitive-science/memory")` | Hierarchical tag |
| Notes missing domain tags | `LIST WHERE !contains(tags, "#cognitive-science") AND !contains(tags, "#pkm")` | Untagged notes |
| Multiple tag intersection | `TABLE tags WHERE contains(tags, "cognitive-science") AND contains(tags, "learning-theory")` | Cross-domain notes |
| Notes by primary domain | `TABLE tags[0] AS "Primary Tag", length(rows) GROUP BY tags[0]` | Tag distribution |
| Year-tagged notes | `LIST WHERE contains(tags, "year/2025")` | Temporal tags |

**DataviewJS Advanced Pattern:**
```dataviewjs
// Tag hierarchy exploration (L1 tags only)
const pages = dv.pages('"Path/To/Notes"');
const tagCounts = {};

pages.forEach(p => {
    if (p.tags) {
        p.tags.forEach(tag => {
            // Extract L1 tag (first segment)
            const l1Tag = tag.split('/')[0].replace('#', '');
            tagCounts[l1Tag] = (tagCounts[l1Tag] || 0) + 1;
        });
    }
});

const sorted = Object.entries(tagCounts)
    .map(([tag, count]) => ({ Tag: `#${tag}`, Count: count }))
    .sort((a, b) => b.Count - a.Count);

dv.table(["Tag", "Count"], sorted.map(t => [t.Tag, t.Count]));
```

---

### 5️⃣ Link & Connection Queries

> [!helpful-tip] Use Case
> Track MOC relationships, find orphan notes, analyze link networks.

| Query Goal                    | DQL Pattern                                                                                             | Result             |
| ----------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------ |
| Notes linking to specific MOC | `LIST WHERE contains(link-up, [[cognitive-science-moc]])`                                               | MOC children       |
| Orphan notes (no inlinks)     | `LIST WHERE length(file.inlinks) = 0`                                                                   | Disconnected notes |
| Hub notes (many inlinks)      | `TABLE length(file.inlinks) AS "Inlinks" WHERE length(file.inlinks) > 5 SORT length(file.inlinks) DESC` | Highly connected   |
| Notes with few outlinks       | `TABLE length(file.outlinks) AS "Outlinks" WHERE length(file.outlinks) < 3`                             | Weakly connected   |
| Backlinks to current note     | `TABLE type, maturity FROM [[#]]`                                                                       | Notes linking here |
| Link density analysis         | `TABLE length(file.inlinks) AS "In", length(file.outlinks) AS "Out" SORT length(file.inlinks) DESC`     | Connection metrics |

**DataviewJS Advanced Pattern:**
```dataviewjs
// Network health dashboard
const pages = dv.pages('"03-notes/01_permanent-notes/01_cognitive-development"').array();

// Handle empty page collection
if (pages.length === 0) {
    dv.paragraph("No pages found in the specified folder.");
} else {
    const metrics = {
        "Total Notes": pages.length,
        "Orphans (0 inlinks)": pages.filter(p => !p.file.inlinks || p.file.inlinks.length === 0).length,
        "Hubs (5+ inlinks)": pages.filter(p => p.file.inlinks && p.file.inlinks.length >= 5).length,
        "Weakly Connected (<3 outlinks)": pages.filter(p => !p.file.outlinks || p.file.outlinks.length < 3).length,
    };

    // Calculate averages safely
    const totalInlinks = pages.reduce((sum, p) => sum + (p.file.inlinks ? p.file.inlinks.length : 0), 0);
    const totalOutlinks = pages.reduce((sum, p) => sum + (p.file.outlinks ? p.file.outlinks.length : 0), 0);

    metrics["Average Inlinks"] = pages.length > 0 ? Math.round(totalInlinks / pages.length) : 0;
    metrics["Average Outlinks"] = pages.length > 0 ? Math.round(totalOutlinks / pages.length) : 0;

    dv.table(["Metric", "Value"], Object.entries(metrics));
}
```

---

### 6️⃣ Review & Maintenance Queries

> [!helpful-tip] Use Case
> Track review schedules, identify neglected notes, monitor review frequency.

| Query Goal | DQL Pattern | Result |
|------------|-------------|---------|
| Notes due for review today | `TABLE next-review, maturity WHERE next-review = date(today)` | Today's reviews |
| Overdue reviews | `TABLE next-review, review-count WHERE next-review < date(today) SORT next-review ASC` | Past-due items |
| Never reviewed notes | `LIST WHERE review-count = 0` | Unreviewed content |
| Most reviewed notes | `TABLE review-count, maturity WHERE review-count > 0 SORT review-count DESC LIMIT 10` | Frequently reviewed |
| Review schedule by maturity | `TABLE next-review, maturity WHERE maturity = "seedling" AND next-review > date(today)` | Upcoming seedling reviews |
| High-confidence overdue | `LIST WHERE next-review < date(today) AND confidence = "high"` | Priority reviews |

**DataviewJS Advanced Pattern:**
```dataviewjs
// Review workload calendar (next 7 days)
const today = dv.date('today');
const weekAhead = [];

for (let i = 0; i < 7; i++) {
    const day = today.plus({ days: i });
    const due = dv.pages('"Path/To/Notes"')
        .where(p => p["next-review"]?.hasSame(day, 'day'))
        .length;
    
    weekAhead.push({
        Date: day.toFormat("EEE MMM dd"),
        "Due": due,
        "Status": due === 0 ? "✅" : due < 5 ? "⚠️" : "🔥"
    });
}

dv.table(["Date", "Due", "Status"], weekAhead.map(d => [d.Date, d.Due, d.Status]));
```

---

### 7️⃣ Aggregation & Analytics Queries

> [!helpful-tip] Use Case
> Statistical analysis, trend identification, vault health metrics.

| Query Goal | DQL Pattern | Result |
|------------|-------------|---------|
| Count notes by type | `TABLE length(rows) AS "Count" GROUP BY type` | Type distribution |
| Average reviews by maturity | `TABLE round(average(review-count), 1) AS "Avg Reviews" GROUP BY maturity` | Review patterns |
| Notes created per month | `TABLE length(rows) AS "Count" GROUP BY month SORT month DESC` | Monthly creation rate |
| Confidence distribution | `TABLE length(rows) AS "Count" GROUP BY confidence` | Confidence levels |
| Source diversity | `TABLE length(rows) AS "Count" GROUP BY source SORT length(rows) DESC` | Source analysis |
| Tag popularity | `FLATTEN tags TABLE length(rows) AS "Uses" GROUP BY tags SORT length(rows) DESC LIMIT 20` | Most-used tags |

**DataviewJS Advanced Pattern:**
```dataviewjs
// Vault growth over time (monthly)
const pages = dv.pages('"Path/To/Notes"');
const byMonth = pages
    .groupBy(p => p.month)
    .map(g => ({
        Month: g.key,
        Created: g.rows.length,
        "Evergreen": g.rows.filter(r => r.maturity === "evergreen").length,
        "Avg Confidence": g.rows.filter(r => r.confidence).length > 0 
            ? Math.round(g.rows.filter(r => r.confidence === "high" || r.confidence === "established").length / g.rows.length * 100) + "%"
            : "N/A"
    }))
    .sort(g => g.Month, "desc")
    .limit(6);

dv.table(["Month", "Created", "Evergreen", "High Confidence %"], 
    byMonth.map(m => [m.Month, m.Created, m.Evergreen, m["Avg Confidence"]]));
```

---

## 🔧 Inline Query Patterns

> [!methodology-and-sources] Inline Dataview
> These queries embed directly in note text using backticks.

| Use Case | Inline Query | Renders As |
|----------|--------------|------------|
| Current note maturity | `` `= this.maturity` `` | `evergreen` |
| Days since creation | `` `= (date(today) - this.created).days` `` | `45 days` |
| Review count | `` `= this.review-count` `` | `3` |
| Next review date | `` `= this.next-review` `` | `2025-12-20` |
| Note age | `` `= round((date(today) - this.created).days / 365, 1) + " years"` `` | `0.1 years` |
| Staleness indicator | `` `= choice((date(today) - this.modified).days > 30, "🍂 Cold", "🔥 Fresh")` `` | `🔥 Fresh` |
| Link count | `` `= length(this.file.outlinks)` `` | `12` |
| Inlink count | `` `= length(this.file.inlinks)` `` | `5` |
| File size | `` `= this.file.size + " bytes"` `` | `4532 bytes` |
| Estimated read time | `` `= round(this.file.size / 1300) + " min"` `` | `3 min` |

---

## 🎨 Dashboard Query Patterns

> [!helpful-tip] Complete Dashboard Components
> Ready-to-use query blocks for note dashboards.

### Health Check Dashboard
```dataview
TABLE 
    maturity AS "Maturity",
    confidence AS "Confidence",
    next-review AS "Next Review",
    review-count AS "Reviews"
WHERE file = this.file
```

### Content Metrics Dashboard
```dataviewjs
const page = dv.current();
const wordCount = page.file.size;
const readTime = Math.round(wordCount / 1300);
const staleness = (dv.date('today').diff(page.modified, 'days')).days;

dv.table(["Metric", "Value"], [
    ["Word Count", wordCount + " bytes"],
    ["Est. Read Time", readTime + " min"],
    ["Days Since Edit", staleness],
    ["Freshness", staleness < 30 ? "🔥 Fresh" : "🍂 Cold"]
]);
```

### Network Connectivity Dashboard
```dataviewjs
const page = dv.current();
const inlinks = page.file.inlinks.length;
const outlinks = page.file.outlinks.length;
const status = inlinks === 0 ? "🕸️ Orphan" : inlinks > 5 ? "⚡ Hub" : "🌱 Node";

dv.table(["Metric", "Value"], [
    ["Inlinks", inlinks],
    ["Outlinks", outlinks],
    ["Network Status", status]
]);
```

---

## 🚨 Common Pitfalls & Solutions

> [!warning] Frequent Errors

| Problem | Cause | Solution |
|---------|-------|----------|
| Query returns nothing | Field name mismatch | Check exact field name in YAML (case-sensitive) |
| Date comparison fails | Wrong date format | Use `date(YYYY-MM-DD)` function |
| List field not filtering | Wrong syntax | Use `contains(field, value)` not `field = value` |
| DateTime vs Date confusion | Mixed formats | Use `dateformat()` or extract date component |
| GROUP BY not working | Non-existent field | Verify field exists in frontmatter |
| Inline query blank | Missing `this.` prefix | Always use `this.fieldname` in inline queries |

---
# Gemini Pro 3.0 Quick Reference

Based on the sophisticated logic within your `_permanent-note-cognitive-science-template-v1.0.0.md`, I have constructed a set of **Quick Reference Metadata Tables**.

These tables are designed to be placed in a separate [[Reference Note]] or on your [[Dashboard]] to assist with writing **Dataview queries**, ensuring tag consistency, and debugging your vault taxonomy.

> [\!methodology-and-sources]
> **Source Material Extraction**
> This reference guide extracts data directly from the `const` arrays defined in your Templater script. It maps the **Input Variable** (e.g., `groupB1_Tags`) to its **Semantic Function** within your [[Knowledge Graph]].
>
>   * **Extraction Source**: `_permanent-note-cognitive-science-template-v1.0.0.md`
>   * **Taxonomy Logic**: Hierarchical structure (Meta $\to$ Domain $\to$ Path $\to$ Granular Leaf)

-----

### 1\. Core Metadata & Status Enums

Use these values for `WHERE` clauses in [[Dataview]] to filter by note state or origin.

| YAML Property | Variable Name | Allowed Values (Enums) | Usage Context |
| :--- | :--- | :--- | :--- |
| `type` | `typeList` | `analysis`, `case-study`, `concept`, `framework`, `guide`, `insight`, `literature`, `moc`, `pattern`, `permanent-note`, `principle`, `reference`, `reflection`, `report`, `strategy`, `technique`, `theory`, `tutorial` | Defines the **structure** and intent of the note. |
| `source` | `sourceList` | `article`, `book`, `claude-opus-4.1`, `claude-sonnet-4.5`, `community`, `conversation`, `course`, `experience`, `gemini-flash-2.5`, `gemini-pro-3.0`, `local-llm`, `paper`, `video` | [**Provenance**:: The origin point of the information.] |
| `maturity` | `maturityLevels` | `seedling` 🌱, `developing` 🌿, `budding` 🌳, `evergreen` 🌲, `needs-review` 🔴 | Indicates how "finished" the thought is. |
| `confidence` | `confidenceLevels` | `speculative`, `provisional`, `moderate`, `established`, `high` | [**Epistemic-Status**:: The certainty level of the claim.] |

> [!helpful-tip] Dataview Query Example
>
> ```sql
> TABLE type, maturity
> FROM "03-notes"
> WHERE maturity = "evergreen" AND source = "claude-sonnet-4.5"
> ```

-----

### 2\. The Hub Network (MOC Link-Ups)

These are your defined "Primary Domains." Every note links up to one of these via the `link-up` YAML field.

| Primary Hub MOC | Variable: `linkUpList` | Focus Area |
| :--- | :--- | :--- |
| `[[artificial-intelligence-moc]]` | **AI & LLMs** | General AI theory and news. |
| `[[cognitive-science-moc]]` | **CogSci** | [**Cognitive-Science**:: Study of mind and intelligence.] |
| `[[cosmology-moc]]` | **Physics** | Astrophysics and space. |
| `[[educational-psychology-moc]]` | **EdPsych** | Learning mechanics. |
| `[[learning-theory-moc]]` | **Pedagogy** | Theoretical frameworks of learning. |
| `[[neuroscience-moc]]` | **Brain** | Biological substrates. |
| `[[pkb-&-pkm-moc]]` | **PKM** | Knowledge management systems. |
| `[[practical-philosophy-moc]]` | **Stoicism** | Living systems and ethics. |
| `[[prompt-engineering-moc]]` | **Prompting** | Technical LLM interaction. |

-----

### 3\. Tag Taxonomy Atlas (Hierarchical Groups)

Your tags are split into specific logic groups to prevent namespace pollution. Use this to find which "Group" a concept belongs to.

#### Group A: Meta-Dimensions

*Controls the nature of the note rather than the topic.*

| Group ID | Variable | Category Name | Key Tag Examples |
| :--- | :--- | :--- | :--- |
| **A1** | `groupA1_Tags` | **Type** | `#type/framework`, `#type/synthesis`, `#type/prompt-library` |
| **A2** | `groupA2_Tags` | **Status** | `#status/evergreen`, `#status/production`, `#status/review` |
| **A3** | `groupA3_Tags` | **Context** | `#context/research`, `#source/course`, `#source/conversation` |
| **A4** | `groupA4_Tags` | **Nature/Mode** | `#complexity/advanced`, `#mode/analytical`, `#model/gemini` |

#### Group B & C: Domains & Pathways

*The "Where" in the library.*

| Group ID | Variable | Category Name | Key Tag Examples |
| :--- | :--- | :--- | :--- |
| **B1** | `groupB1_Tags` | **Top Domains** | `#cognitive-science`, `#cosmology`, `#prompt-engineering` |
| **B2** | `groupB2_Tags` | **High Systems** | `#zettelkasten`, `#building-second-brain`, `#tag-taxonomy` |
| **C1** | `groupC1_Tags` | **PKM Paths** | `#knowledge-graph/structure`, `#obsidian/dataview`, `#pkm/workflow` |
| **C2** | `groupC2_Tags` | **CogSci Paths** | `#cognitive-science/memory`, `#self-regulation/dopamine` |
| **C3** | `groupC3_Tags` | **Prompt Paths** | `#prompt-engineering/optimization`, `#llm-architecture/transformer` |

#### Group D-J: Granular Mechanisms (Leaf Nodes)

*The specific atomic concepts.*

| Group ID | Variable | Domain Focus | Key Tag Examples |
| :--- | :--- | :--- | :--- |
| **D** | `groupD_Tags` | **Memory/Attention** | `#working-memory`, `#encoding`, `#selective-attention` |
| **E** | `groupE_Tags` | **Executive Func.** | `#problem-solving`, `#critical-thinking`, `#cognitive-control` |
| **F** | `groupF_Tags` | **Metacognition** | `#cognitive-load-theory`, `#active-recall`, `#transfer-of-learning` |
| **G** | `groupG_Tags` | **Theories** | `#embodied-cognition`, `#global-workspace-theory`, `#dual-process` |
| **H** | `groupH_Tags` | **PKM Tech** | `#dataviewjs`, `#templater`, `#frontmatter-design` |
| **I** | `groupI_Tags` | **Prompt Tech** | `#chain-of-thought`, `#rag`, `#few-shot`, `#adversarial-prompting` |
| **J** | `groupJ_Tags` | **Research/Cross** | `#neuroimaging-studies`, `#longitudinal-research`, `#aging-cognition` |

-----

### 4\. Semantic Iconography Key

Your script automatically assigns icons based on domain keywords. This helps you visually identify note types in [[Quick Switcher]] or lists.

| Icon | Semantic Trigger (Keywords) | Domain |
| :---: | :--- | :--- |
| 📑 | `type/` | Note Type |
| 🚦 | `status/` | Status |
| 🍷 | `maturity/` | Maturity Level |
| 💎 | `obsidian`, `dataview`, `plugin` | **Obsidian Tech** |
| 🧠 | `pkm`, `zettelkasten`, `brain` | **PKM / Brain** |
| 🎓 | `learning`, `education` | **Pedagogy** |
| 🤖 | `llm`, `gpt`, `claude`, `agent` | **AI / Agents** |
| 💬 | `prompt`, `chain-of-thought` | **Prompting** |
| 🌌 | `cosmology`, `universe` | **Cosmology** |
| 🔬 | `research`, `analysis`, `study` | **Research** |

-----

## 🔗 Related Topics for PKB Expansion

1.  [[Dataviewjs Query Snippets]]
      * **Connection:** This reference table provides the *data values* needed to write the *queries* in a snippet library.
      * **Depth Potential:** High. You can create a reusable library of JS scripts that query these specific tags to build dashboards.
      * **Knowledge Graph Role:** A functional "Tool" note that powers the [[Dashboard]] infrastructure.
2.  [[Taxonomy Design Principles]]
      * **Connection:** Explains *why* the groups (A-J) are split this way (Generic vs. Specific).
      * **Depth Potential:** Explore [[Facetted Classification]] vs. [[Hierarchical Taxonomy]].
      * **Knowledge Graph Role:** A theoretical "Concept" note in the [[Information Architecture]] domain.
3.  [[Prompt Component Library]]
      * **Connection:** Group I (`groupI_Tags`) contains the atomic components (CoT, Few-Shot) needed for your prompt library.
      * **Depth Potential:** Each tag in Group I warrants an atomic note defining that specific prompting technique.
      * **Knowledge Graph Role:** A "Collection" or "MOC" within the [[Prompt Engineering]] domain.
4.  [[Cognitive Load Theory]]
      * **Connection:** Referenced in Group F (`cognitive-load-theory`), this is central to your learning domain.
      * **Depth Potential:** Deep dive into *intrinsic*, *extraneous*, and *germane* load (all present in your tag list).
      * **Knowledge Graph Role:** A foundational "Framework" note in the [[Cognitive Science]] domain.

# 🔗 Related Topics for PKB Expansion

1. **[[DataviewJS Advanced Patterns]]**
   - *Connection*: Complex queries requiring JavaScript logic
   - *Depth Potential*: Custom aggregations, API integration, dynamic dashboards
   - *Knowledge Graph Role*: Technical implementation layer

2. **[[Metadata Schema Design]]**
   - *Connection*: Designing effective frontmatter structures
   - *Depth Potential*: Hierarchical metadata, controlled vocabularies, semantic relationships
   - *Knowledge Graph Role*: Information architecture foundation

3. **[[Obsidian Query Optimization]]**
   - *Connection*: Performance tuning for large vaults
   - *Depth Potential*: Indexing strategies, query caching, pagination
   - *Knowledge Graph Role*: System performance domain

4. **[[YAML Frontmatter Best Practices]]**
   - *Connection*: Proper metadata formatting and validation
   - *Depth Potential*: Type safety, validation patterns, linting
   - *Knowledge Graph Role*: Data quality assurance

---

This reference provides immediate access to working query patterns while maintaining educational depth. Each table follows the <span style='color: #FFC700;'>progressive revelation</span> principle—starting with simple patterns and building to complex analytics.



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
