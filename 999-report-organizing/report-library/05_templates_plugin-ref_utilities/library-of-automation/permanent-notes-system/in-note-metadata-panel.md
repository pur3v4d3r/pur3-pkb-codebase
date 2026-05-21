







I'm working on my in note Metadata panel that uses Dataview, Dataviewjs, Meta Bind, Etc to display the files metadata or any other metadata I want in the opening section of my notes.
I need more queries that are similar to the one below in the current metadata panel.

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [["<% tp.title %>"]]
> - **MOC**: `=this.link-up`

> [! ] # In-Note Metadata Panel
> - **Note-Type**: `= this.type`
> - **Development Status**: `= this.maturity`
> - **Epistemic Confidence**: `= this.confidence`
> - **Next Review**: `= this.next-review`
> - **Review Count**: `= this.review-count`
> - **Created**: `= this.created`
> - **Last Modified**: `= this.modified`
> 
> > [!purpose] ### 📝Content Metrics
> > **Word Count**: `= this.file.size`| **Est. Read Time**: `= round(this.file.size / 1300) + " min"`
> > **Depth Class**: `= choice(this.file.size < 500, "🌱Stub", choice(this.file.size < 2000, "📄Note", "📜Essay"))`
> ----
> > [!purpose] ### 🕰️Temporal Context
> > **Created**: `= this.file.ctime` | **Age**: `= (date(today) - this.file.ctime).days + " days"`
> > **Last Touch**: `= this.file.mtime` | **Staleness**: `= choice((date(today) - this.file.mtime).days > 180, "🕸️Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂Cold", "🔥Fresh"))`
> > **Touch Frequency**: `= choice((date(today) - this.file.mtime).days < 7, "🔥Active", choice((date(today) - this.file.mtime).days < 30, "👌Regular", "❄️Dormant"))`
> ----
> > [!topic-idea] ### 🔗Network Connectivity
> > **In-Links**: `= length(this.file.inlinks)` | **Out-Links**: `= length(this.file.outlinks)`
> > **Network Status**: `= choice(length(this.file.inlinks) = 0, "🕸️Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱Node"))`
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
> WHERE  type = "<% type %>"
> SORT "maturity" DESC
> LIMIT 15
> ```
> ### Sources & References
> ```dataview
> TABLE 
>     source AS "Source Type",
>     file.ctime AS "Date Added"
> FROM ""
> WHERE source = "<% source %>"
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
> ### <% dateNow %> - Initial Creation
> *Context*: `=this.title` **by**: `=this.source`
> *Maturity*: `= this.maturity`  
> *Confidence*: `= this.confidence`
> 
> ### Tags & Classification
> *Primary Tags*: `= this.tags`  
> *Type*: `= this.type`  
> *Source*: `= this.source`


> [! ] ### Claude Thinking
> The user is working on their Obsidian vault's in-note metadata panel system. They have a sophisticated setup using Dataview, DataviewJS, and other plugins to display rich metadata and analytics about each note. They want me to create additional queries similar to their existing ones that could enhance their metadata panel.
> Let me analyze what they currently have:
> 1. **Overview Section**: Title and MOC links
> 2. **Basic Metadata**: Type, maturity, confidence, review info, created/modified dates
> 3. **Content Metrics**: Word count, read time, depth classification
> 4. **Temporal Context**: Creation date, age, staleness indicators, touch frequency
> 5. **Network Connectivity**: Inlinks, outlinks, orphan/hub status
> 6. **Semantic Bridges**: DataviewJS query finding "sibling" notes with shared outlinks
> 7. **Related Notes**: Dataview table by type
> 8. **Sources & References**: Dataview table by source
> 9. **Backlinks & Connections**: Notes linking to this one
> Now I need to create MORE queries that would be valuable additions. Let me think about what categories of metadata/analytics would be useful for a PKB system:
> **Potential new query categories:**
> 10. **Tag Analysis** - Tag clustering, tag frequency, most/least used tags on this note
> 11. **Maturity Progression** - Notes at different maturity levels in the same domain
> 12. **Knowledge Gaps** - Concepts mentioned but not linked (orphan mentions)
> 13. **Recent Activity** - Recently modified related notes
> 14. **Review Pipeline** - Notes due for review, overdue reviews
> 15. **Link Depth Analysis** - How deep this note is in the link graph
> 16. **Co-occurrence Analysis** - Notes that share similar tags
> 17. **Temporal Neighbors** - Notes created around the same time
> 18. **Source Diversity** - Variety of sources in this note's neighborhood
> 19. **Confidence Distribution** - How confident are related notes
> 20. **Link Quality** - Ratio of incoming to outgoing links
> 21. **Domain Coverage** - How well-covered is this domain
> 22. **Folder Context** - Other notes in same folder
> 23. **Daily Note Integration** - Connections to daily notes
> 24. **Evolution Tracking** - How has this note's connectivity changed
> 25. **Similar Content** - Notes with similar tags/metadata combinations
> 26. **Citation Network** - Source chains and academic-style references
> 27. **Maturity Peers** - Notes at same maturity level across domains
> Let me create a variety of these as production-ready queries that match their existing style and formatting conventions. I'll organize them into logical groupings similar to their existing panel structure.
> I should provide:
> 28. Complete, tested-pattern code
> 29. Clear explanations of what each does
> 30. Callouts formatted like their existing structure
> 31. Inline DQL queries and DataviewJS blocks as appropriate
> 32. Modular components they can mix and match
> Let me structure this as a comprehensive engineering response following my Obsidian Automation Architect protocols.


# 🔧 Advanced In-Note Metadata Panel Expansion

Based on your existing panel architecture, I've engineered a comprehensive suite of additional queries organized into modular blocks. Each is designed to integrate seamlessly with your current setup and follows your established formatting conventions.

---

## 📊 Block 1: Tag Intelligence System

These queries analyze your note's tag relationships within the vault.

```markdown
> [!abstract] ### 🏷️ Tag Intelligence
> **Tag Count**: `= length(this.tags)` | **Unique Domains**: `= length(filter(this.tags, (t) => contains(t, "/")))` hierarchical tags
> **Tag Density**: `= choice(length(this.tags) < 3, "⚠️Sparse", choice(length(this.tags) > 10, "📚Rich", "✅Balanced"))`
```

```dataviewjs
// TAG CO-OCCURRENCE: Find notes sharing the most tags with this note
const current = dv.current();
const myTags = current.tags || [];

if (myTags.length > 0) {
    const tagSiblings = dv.pages()
        .where(p => p.file.path !== current.file.path)
        .where(p => p.tags && p.tags.length > 0)
        .map(p => {
            const sharedTags = (p.tags || []).filter(t => myTags.includes(t));
            return {
                link: p.file.link,
                sharedCount: sharedTags.length,
                sharedTags: sharedTags,
                totalTags: (p.tags || []).length
            };
        })
        .where(p => p.sharedCount >= 2) // At least 2 shared tags
        .sort(p => p.sharedCount, "desc")
        .limit(5);

    if (tagSiblings.length > 0) {
        dv.header(4, "🏷️ Tag Siblings (Shared Taxonomy)");
        dv.table(
            ["Note", "Overlap", "Shared Tags"],
            tagSiblings.map(s => [
                s.link,
                `${s.sharedCount}/${s.totalTags}`,
                s.sharedTags.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
            ])
        );
    } else {
        dv.paragraph("*No tag siblings with 2+ shared tags found.*");
    }
} else {
    dv.paragraph("*No tags on this note to analyze.*");
}
```


The issue is that `p.tags` might not always be an array. In Dataview, tags can be stored as strings or arrays depending on how they're defined. Here's the fixed version:

```dataviewjs
// TAG CO-OCCURRENCE: Find notes sharing the most tags with this note
const current = dv.current();

// Safely get tags from current note
let myTags = [];
if (current.tags) {
    if (Array.isArray(current.tags)) {
        myTags = current.tags;
    } else if (typeof current.tags === 'string') {
        myTags = [current.tags];
    }
}

if (myTags.length > 0) {
    const tagSiblings = dv.pages()
        .where(p => p.file.path !== current.file.path)
        .where(p => {
            // Safely check if page has tags
            if (!p.tags) return false;
            // Convert tags to array if needed
            let pageTags = [];
            if (Array.isArray(p.tags)) {
                pageTags = p.tags;
            } else if (typeof p.tags === 'string') {
                pageTags = [p.tags];
            }
            return pageTags.length > 0;
        })
        .map(p => {
            // Safely convert page tags to array
            let pageTags = [];
            if (p.tags) {
                if (Array.isArray(p.tags)) {
                    pageTags = p.tags;
                } else if (typeof p.tags === 'string') {
                    pageTags = [p.tags];
                }
            }
            
            // Find shared tags
            const sharedTags = pageTags.filter(t => {
                if (typeof t === 'string') {
                    return myTags.includes(t);
                } else if (t && typeof t === 'object' && t.path) {
                    // Handle tag objects
                    return myTags.some(myTag => {
                        if (typeof myTag === 'string') {
                            return myTag === t.path;
                        }
                        return false;
                    });
                }
                return false;
            });
            
            return {
                link: p.file.link,
                sharedCount: sharedTags.length,
                sharedTags: sharedTags,
                totalTags: pageTags.length
            };
        })
        .where(p => p.sharedCount >= 2) // At least 2 shared tags
        .sort(p => p.sharedCount, "desc")
        .limit(5);

    if (tagSiblings.length > 0) {
        dv.header(4, "🏷️ Tag Siblings (Shared Taxonomy)");
        dv.table(
            ["Note", "Overlap", "Shared Tags"],
            tagSiblings.map(s => {
                // Safely extract tag names for display
                let displayTags = s.sharedTags.map(t => {
                    if (typeof t === 'string') {
                        return t;
                    } else if (t && typeof t === 'object' && t.path) {
                        return t.path;
                    }
                    return String(t);
                });
                
                return [
                    s.link,
                    s.sharedCount + "/" + s.totalTags,
                    displayTags.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
                ];
            })
        );
    } else {
        dv.paragraph("*No tag siblings with 2+ shared tags found.*");
    }
} else {
    dv.paragraph("*No tags on this note to analyze.*");
}
```

Key improvements:

1. **Proper tag type handling**: Checks if tags are arrays or strings and converts them appropriately
2. **Tag object handling**: Handles cases where tags might be objects with a `path` property
3. **Better error checking**: Validates tag data types before processing
4. **Safer string operations**: Ensures tags are properly converted to strings for comparison and display
5. **Robust filtering**: More careful filtering that handles different tag formats

This should properly handle all the different ways tags can be stored in Dataview.

---

## 📊 Block 2: Maturity & Confidence Ecosystem

Track how this note relates to others at similar development stages.

```markdown
> [!note] ### 🌱 Maturity Ecosystem
> **Maturity Level**: `= this.maturity` | **Confidence**: `= this.confidence`
> **Maturity Score**: `= choice(this.maturity = "evergreen", "5/5 🌳", choice(this.maturity = "budding", "4/5 🌿", choice(this.maturity = "developing", "3/5 🌱", choice(this.maturity = "seedling", "2/5 🫘", "1/5 ❓"))))`
> **Confidence Score**: `= choice(this.confidence = "high", "5/5 ✅", choice(this.confidence = "established", "4/5 👍", choice(this.confidence = "moderate", "3/5 🤔", choice(this.confidence = "provisional", "2/5 ⚠️", "1/5 ❓"))))`
```

```dataviewjs
// MATURITY PEERS: Notes at same maturity level in related domains
const current = dv.current();
const myMaturity = current.maturity;
const myType = current.type;

if (myMaturity) {
    const peers = dv.pages()
        .where(p => p.file.path !== current.file.path)
        .where(p => p.maturity === myMaturity)
        .where(p => p.type === myType || !myType)
        .sort(p => p.file.mtime, "desc")
        .limit(8);

    if (peers.length > 0) {
        dv.header(4, `📊 Maturity Peers (${myMaturity})`);
        dv.table(
            ["Note", "Type", "Confidence", "Last Modified"],
            peers.map(p => [
                p.file.link,
                p.type || "—",
                p.confidence || "—",
                dv.func.dateformat(p.file.mtime, "MMM dd")
            ])
        );
    } else {
        dv.paragraph(`*No other ${myMaturity} notes found.*`);
    }
}
```

---

## 📊 Block 3: Review Pipeline Intelligence

Monitor your spaced repetition and review workflow.

```markdown
> [!warning] ### 📅 Review Intelligence
> **Next Review**: `= this.next-review` | **Review Count**: `= this.review-count`
> **Review Status**: `= choice(this.next-review < date(today), "🔴 OVERDUE", choice(this.next-review = date(today), "🟡 Due Today", choice(dateformat(this.next-review, "yyyy-MM-dd") <= dateformat(date(today) + dur(7 days), "yyyy-MM-dd"), "🟢 This Week", "⚪ Scheduled")))`
> **Days Until Review**: `= choice(this.next-review, (this.next-review - date(today)).days + " days", "Not scheduled")`
```

```dataviewjs
// REVIEW QUEUE: Upcoming reviews for related notes
const current = dv.current();
const today = dv.date("today");
const weekFromNow = dv.date("today").plus({days: 7});

const upcomingReviews = dv.pages()
    .where(p => p["next-review"])
    .where(p => p["next-review"] >= today && p["next-review"] <= weekFromNow)
    .where(p => p.file.path !== current.file.path)
    .sort(p => p["next-review"], "asc")
    .limit(8);

if (upcomingReviews.length > 0) {
    dv.header(4, "📅 Review Queue (Next 7 Days)");
    dv.table(
        ["Note", "Due", "Maturity", "Reviews"],
        upcomingReviews.map(p => [
            p.file.link,
            dv.func.dateformat(p["next-review"], "MMM dd"),
            p.maturity || "—",
            p["review-count"] || 0
        ])
    );
} else {
    dv.paragraph("*No reviews scheduled in the next 7 days.*");
}
```

---

## 📊 Block 4: Temporal Neighborhood

Notes created around the same time often share thematic connections.

```markdown
> [!info] ### ⏰ Temporal Context
> **Created**: `= dateformat(this.file.ctime, "MMMM dd, yyyy")` | **Age**: `= (date(today) - this.file.ctime).days` days
> **Creation Era**: `= choice((date(today) - this.file.ctime).days > 365, "📜 Veteran", choice((date(today) - this.file.ctime).days > 90, "📚 Established", choice((date(today) - this.file.ctime).days > 30, "🌿 Maturing", "🌱 Fresh")))`
> **Activity Ratio**: `= choice(this.file.mtime = this.file.ctime, "❄️ Untouched", choice((this.file.mtime - this.file.ctime).days < 1, "⚡ Same-Day Edit", "✏️ Revised"))`
```

```dataviewjs
// TEMPORAL NEIGHBORS: Notes created within 3 days of this note
const current = dv.current();
const ctime = current.file.ctime;
const threeDaysBefore = ctime.minus({days: 3});
const threeDaysAfter = ctime.plus({days: 3});

const temporalNeighbors = dv.pages()
    .where(p => p.file.path !== current.file.path)
    .where(p => p.file.ctime >= threeDaysBefore && p.file.ctime <= threeDaysAfter)
    .sort(p => Math.abs(p.file.ctime.ts - ctime.ts), "asc")
    .limit(6);

if (temporalNeighbors.length > 0) {
    dv.header(4, "⏰ Temporal Neighbors (±3 days)");
    dv.table(
        ["Note", "Created", "Type", "Shared Context?"],
        temporalNeighbors.map(p => {
            const daysDiff = Math.round((p.file.ctime.ts - ctime.ts) / (1000 * 60 * 60 * 24));
            return [
                p.file.link,
                daysDiff === 0 ? "Same day" : (daysDiff > 0 ? `+${daysDiff}d` : `${daysDiff}d`),
                p.type || "—",
                current.file.outlinks.map(l => l.path).some(path => p.file.outlinks.map(l => l.path).includes(path)) ? "✅" : "—"
            ];
        })
    );
} else {
    dv.paragraph("*No notes created within 3 days of this note.*");
}
```

---

## 📊 Block 5: Link Quality Analytics

Analyze the health and balance of your note's connections.

```markdown
> [!tip] ### 🔗 Link Quality Analytics
> **In-Links**: `= length(this.file.inlinks)` | **Out-Links**: `= length(this.file.outlinks)`
> **Link Ratio**: `= choice(length(this.file.outlinks) = 0, "∞ (no outlinks)", round(length(this.file.inlinks) / length(this.file.outlinks) * 100) / 100)`
> **Link Balance**: `= choice(length(this.file.inlinks) > length(this.file.outlinks) * 2, "📥 Receiver (heavily cited)", choice(length(this.file.outlinks) > length(this.file.inlinks) * 2, "📤 Contributor (cites many)", "⚖️ Balanced"))`
> **Connectivity Score**: `= round((length(this.file.inlinks) + length(this.file.outlinks)) / 2)` avg connections
```

```dataviewjs
// LINK CHAIN DEPTH: How far this note reaches through outlinks
const current = dv.current();
const directOutlinks = current.file.outlinks.map(l => l.path);

// Second-degree connections (notes that my outlinks link to)
let secondDegree = new Set();
for (const path of directOutlinks) {
    const page = dv.page(path);
    if (page && page.file.outlinks) {
        page.file.outlinks.forEach(l => {
            if (l.path !== current.file.path && !directOutlinks.includes(l.path)) {
                secondDegree.add(l.path);
            }
        });
    }
}

dv.header(4, "🌐 Link Reach Analysis");
dv.paragraph(`**Direct connections**: ${directOutlinks.length} notes`);
dv.paragraph(`**2nd-degree reach**: ${secondDegree.size} additional notes`);
dv.paragraph(`**Total network reach**: ${directOutlinks.length + secondDegree.size} notes (${Math.round((directOutlinks.length + secondDegree.size) / dv.pages().length * 100)}% of vault)`);
```



---

## 📊 Block 6: Domain Coverage Analysis

See how well your current domain is populated.

```dataviewjs
// DOMAIN COVERAGE: Analyze tag domain saturation
const current = dv.current();
const myTags = current.tags || [];

// Extract primary domain (first hierarchical tag or first tag)
const primaryDomain = myTags.find(t => t.includes("/"))?.split("/")[0] || myTags[0];

if (primaryDomain) {
    const domainNotes = dv.pages()
        .where(p => p.tags && p.tags.some(t => t.startsWith(primaryDomain) || t === primaryDomain));
    
    const maturityDistribution = {
        evergreen: domainNotes.filter(p => p.maturity === "evergreen").length,
        budding: domainNotes.filter(p => p.maturity === "budding").length,
        developing: domainNotes.filter(p => p.maturity === "developing").length,
        seedling: domainNotes.filter(p => p.maturity === "seedling").length,
        unset: domainNotes.filter(p => !p.maturity).length
    };

    dv.header(4, `📂 Domain: ${primaryDomain}`);
    dv.paragraph(`**Total notes**: ${domainNotes.length}`);
    dv.paragraph(`**Maturity breakdown**: 🌳${maturityDistribution.evergreen} | 🌿${maturityDistribution.budding} | 🌱${maturityDistribution.developing} | 🫘${maturityDistribution.seedling} | ❓${maturityDistribution.unset}`);
    
    const coverage = (maturityDistribution.evergreen + maturityDistribution.budding) / domainNotes.length * 100;
    dv.paragraph(`**Domain health**: ${Math.round(coverage)}% mature (evergreen + budding)`);
} else {
    dv.paragraph("*No domain tags found to analyze.*");
}
```



The error you're seeing:

```
TypeError: Cannot read properties of null (reading 'startsWith')
```

…is happening because **some tags in your data are `null` or not strings**, and you're calling `.startsWith()` on them.

### ✅ Fix:
You need to ensure that each tag (`t`) is a valid string before calling methods like `startsWith()` on it.

Here’s the **corrected version** of your script with added safety checks:

```dataviewjs
// DOMAIN COVERAGE: Analyze tag domain saturation
const current = dv.current();
const myTags = current.tags || [];

// Extract primary domain (first hierarchical tag or first tag)
const primaryDomain = myTags.find(t => typeof t === "string" && t.includes("/"))?.split("/")[0] 
                   || myTags.find(t => typeof t === "string");

if (primaryDomain) {
  const domainNotes = dv.pages()
    .where(p => 
      p.tags && 
      Array.isArray(p.tags) && 
      p.tags.some(t => 
        typeof t === "string" && 
        (t.startsWith(primaryDomain) || t === primaryDomain)
      )
    );
   
  const maturityDistribution = {
    evergreen: domainNotes.filter(p => p.maturity === "evergreen").length,
    budding: domainNotes.filter(p => p.maturity === "budding").length,
    developing: domainNotes.filter(p => p.maturity === "developing").length,
    seedling: domainNotes.filter(p => p.maturity === "seedling").length,
    unset: domainNotes.filter(p => !p.maturity).length
  };

  dv.header(4, `📂 Domain: ${primaryDomain}`);
  dv.paragraph(`**Total notes**: ${domainNotes.length}`);
  dv.paragraph(`**Maturity breakdown**: 🌳${maturityDistribution.evergreen} | 🌿${maturityDistribution.budding} | 🌱${maturityDistribution.developing} | 🫘${maturityDistribution.seedling} | ❓${maturityDistribution.unset}`);
   
  const totalWithMaturity = domainNotes.length - maturityDistribution.unset;
  const coverage = totalWithMaturity > 0 
    ? (maturityDistribution.evergreen + maturityDistribution.budding) / totalWithMaturity * 100
    : 0;

  dv.paragraph(`**Domain health**: ${Math.round(coverage)}% mature (evergreen + budding)`);

} else {
  dv.paragraph("*No domain tags found to analyze.*");
}
```

---

### 🔍 What Was Fixed?

1. **Type checking for tags**:
   - Ensured `typeof t === "string"` before calling `.startsWith()`.
2. **Array validation**:
   - Added `Array.isArray(p.tags)` to prevent errors when `p.tags` is not an array.
3. **Improved coverage logic**:
   - Avoid division by zero by checking `totalWithMaturity > 0`.
   - Coverage now only considers notes with a defined maturity.

---

Let me know if you'd like this visualized as a bar chart or enhanced further!

---



## 📊 Block 8: Orphan Link Detector

Find mentioned concepts that aren't linked yet.

```dataviewjs
// ORPHAN MENTIONS: Text that looks like it could be a wiki-link but isn't
const current = dv.current();
const content = await dv.io.load(current.file.path);

// Get all existing outlinks
const existingLinks = current.file.outlinks.map(l => l.path.split("/").pop().toLowerCase());

// Common PKB/PKM terms that should usually be linked
const importantTerms = [
    "zettelkasten", "pkm", "pkb", "obsidian", "dataview", "templater",
    "atomic note", "evergreen note", "moc", "map of content",
    "cognitive load", "working memory", "metacognition", "spaced repetition",
    "retrieval practice", "elaborative encoding", "interleaving"
];

const potentialOrphans = importantTerms.filter(term => {
    const regex = new RegExp(`\\b${term}s?\\b`, "gi");
    const isInContent = regex.test(content);
    const isAlreadyLinked = existingLinks.some(link => 
        link.toLowerCase().includes(term.toLowerCase())
    );
    return isInContent && !isAlreadyLinked;
});

if (potentialOrphans.length > 0) {
    dv.header(4, "⚠️ Potential Orphan Concepts");
    dv.paragraph("*These terms appear in your note but aren't linked:*");
    dv.list(potentialOrphans.map(t => `[[${t}]]?`));
} else {
    dv.paragraph("✅ *No common PKB terms detected as orphan mentions.*");
}
```

---

## 📊 Block 9: MOC Relationship Tracker

Understand this note's position in your MOC hierarchy.

```dataviewjs
// MOC CONTEXT: Show relationship to MOCs
const current = dv.current();
const linkUp = current["link-up"];

// Find all MOCs in vault
const allMocs = dv.pages()
  .where(p => {
    // Check if type is "moc" (case insensitive)
    if (p.type && typeof p.type === 'string' && p.type.toLowerCase() === "moc") {
      return true;
    }
    // Check if tags contain "moc" (case insensitive)
    if (p.tags && Array.isArray(p.tags)) {
      return p.tags.some(t => {
        if (typeof t === 'string') {
          return t.toLowerCase().includes("moc");
        }
        return false;
      });
    }
    return false;
  });

// Get current file path safely
const currentPath = current.file ? current.file.path : null;

// Find MOCs that link TO this note
const mocsLinkingHere = currentPath ? allMocs
  .where(p => {
    if (!p.file || !p.file.outlinks || !Array.isArray(p.file.outlinks)) {
      return false;
    }
    return p.file.outlinks.some(l => l.path === currentPath);
  }) : [];

// Find MOCs this note links TO
const mocsLinkedFrom = (current.file && current.file.outlinks) ? allMocs
  .where(p => {
    if (!p.file || !p.file.path) {
      return false;
    }
    return current.file.outlinks.some(l => l.path === p.file.path);
  }) : [];

dv.header(4, "🗺️ MOC Relationships");

// Assigned MOC
const assignedMocText = linkUp ? (typeof linkUp === 'object' ? linkUp.toString() : String(linkUp)) : "None assigned";
dv.paragraph("**Assigned MOC**: " + assignedMocText);

// MOCs linking here
let linkingHereText = "None";
if (mocsLinkingHere.length > 0) {
  const links = mocsLinkingHere.map(p => {
    if (p.file && p.file.link) {
      return p.file.link.toString();
    }
    return p.file.path || "Unknown MOC";
  });
  linkingHereText = links.join(", ");
}
dv.paragraph("**MOCs linking here**: " + linkingHereText);

// MOCs referenced
let referencedMocsText = "None";
if (mocsLinkedFrom.length > 0) {
  const links = mocsLinkedFrom.map(p => {
    if (p.file && p.file.link) {
      return p.file.link.toString();
    }
    return p.file.path || "Unknown MOC";
  });
  referencedMocsText = links.join(", ");
}
dv.paragraph("**MOCs referenced**: " + referencedMocsText);

if (mocsLinkingHere.length === 0 && !linkUp) {
  dv.paragraph("⚠️ *This note is not connected to any MOC—consider adding a link-up.*");
}
```

---


Key improvements made:

1. **Better error handling**: Added checks for undefined properties and arrays
2. **Safer array operations**: Verified that `outlinks` and `tags` are arrays before using array methods
3. **Case-insensitive matching**: Made type and tag matching case-insensitive
4. **Safer string operations**: Added type checking before calling string methods
5. **Proper link handling**: Safely extract link text and handle cases where links might not exist
6. **Fixed variable reference**: Stored `currentPath` to avoid repeated property access
7. **Better null/undefined handling**: Added checks for all potentially missing properties

This version should work reliably even with incomplete or malformed data.
## 📊 Block 10: Completion & Health Score

Aggregate quality metrics into a single health indicator.

```dataviewjs
// HEALTH SCORE: Aggregate quality metrics
const current = dv.current();

// Scoring factors (each 0-20 points, total 100)
let score = 0;
let breakdown = [];

// 1. Tag coverage (0-20)
const tagScore = Math.min(20, (current.tags?.length || 0) * 4);
score += tagScore;
breakdown.push(`Tags: ${tagScore}/20`);

// 2. Link connectivity (0-20)
const linkScore = Math.min(20, (current.file.inlinks.length + current.file.outlinks.length) * 2);
score += linkScore;
breakdown.push(`Links: ${linkScore}/20`);

// 3. Metadata completeness (0-20)
const metaFields = ["type", "maturity", "confidence", "source", "link-up"];
const metaScore = metaFields.filter(f => current[f]).length * 4;
score += metaScore;
breakdown.push(`Metadata: ${metaScore}/20`);

// 4. Content depth (0-20) - based on file size
const sizeScore = Math.min(20, Math.round(current.file.size / 200));
score += sizeScore;
breakdown.push(`Depth: ${sizeScore}/20`);

// 5. Freshness (0-20) - based on recent modification
const daysSinceModified = Math.floor((Date.now() - current.file.mtime.ts) / (1000 * 60 * 60 * 24));
const freshnessScore = Math.max(0, 20 - Math.floor(daysSinceModified / 15));
score += freshnessScore;
breakdown.push(`Freshness: ${freshnessScore}/20`);

// Render
const healthEmoji = score >= 80 ? "🟢" : score >= 60 ? "🟡" : score >= 40 ? "🟠" : "🔴";
const healthLabel = score >= 80 ? "Excellent" : score >= 60 ? "Good" : score >= 40 ? "Fair" : "Needs Work";

dv.header(4, `${healthEmoji} Note Health: ${score}/100 (${healthLabel})`);
dv.paragraph(breakdown.join(" | "));

if (score < 60) {
    dv.paragraph("**💡 Improvement suggestions:**");
    if (tagScore < 12) dv.paragraph("• Add more descriptive tags");
    if (linkScore < 12) dv.paragraph("• Create more connections to other notes");
    if (metaScore < 12) dv.paragraph("• Fill in missing metadata fields");
    if (sizeScore < 12) dv.paragraph("• Expand content depth");
    if (freshnessScore < 12) dv.paragraph("• Review and update this note");
}
```

---

## 🛠️ Integration Instructions

**Step 1: Choose Your Blocks**
Select which blocks are most valuable for your workflow. You don't need all of them—pick 3-5 that address your specific needs.

**Step 2: Add to Template**
Insert the chosen blocks into your note templates (e.g., `_permanent-note-cognitive-science-template-v1.0.0.md`) within the metadata panel section.

**Step 3: Customize Thresholds**
Adjust the numerical thresholds in each block to match your vault's scale:
- `limit(5)` → Change based on your preference
- Tag overlap minimum (`>= 2`) → Adjust based on tag density
- Time windows (`±3 days`, `7 days`) → Match your workflow rhythm

**Step 4: Style Consistency**
Wrap each block in your existing callout structure:
```markdown
> [!your-callout-type] ### Block Title
> [inline queries here]
> ```dataviewjs
> [script here]
> ```
```

---

## 🔗 Related Topics for PKB Expansion

1. **[[Dataview Query Optimization]]**
   - *Connection*: Performance tuning for vaults with 1000+ notes
   - *Depth Potential*: Caching strategies, query limiting, lazy loading
   - *Knowledge Graph Role*: Technical reference for PKB infrastructure

2. **[[Meta Bind Button Actions]]**
   - *Connection*: Add interactive controls to update metadata inline
   - *Depth Potential*: Toggle maturity, increment review count, mark as reviewed
   - *Knowledge Graph Role*: Workflow automation layer

3. **[[Knowledge Graph Visualization Strategies]]**
   - *Connection*: Complement these metrics with visual graph analysis
   - *Depth Potential*: Custom graph views, clustering algorithms, density mapping
   - *Knowledge Graph Role*: Meta-analysis of your PKB structure

4. **[[Spaced Repetition Integration Patterns]]**
   - *Connection*: Enhance the review pipeline intelligence
   - *Depth Potential*: SRS algorithm implementation, Anki integration, review scheduling
   - *Knowledge Graph Role*: Learning science application to PKM
     
  