

















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













> [!info] ### ⏰ Temporal Context
> **Created**: `= dateformat(this.file.ctime, "MMMM dd, yyyy")` | **Age**: `= (date(today) - this.file.ctime).days` days
> **Creation Era**: `= choice((date(today) - this.file.ctime).days > 365, "📜 Veteran", choice((date(today) - this.file.ctime).days > 90, "📚 Established", choice((date(today) - this.file.ctime).days > 30, "🌿 Maturing", "🌱 Fresh")))`
> **Activity Ratio**: `= choice(this.file.mtime = this.file.ctime, "❄️ Untouched", choice((this.file.mtime - this.file.ctime).days < 1, "⚡ Same-Day Edit", "✏️ Revised"))`
> ```dataviewjs
> // TEMPORAL NEIGHBORS: Notes created within 3 days of this note
> const current = dv.current();
> const ctime = current.file.ctime;
> const threeDaysBefore = ctime.minus({days: 3});
> const threeDaysAfter = ctime.plus({days: 3});
> 
> const temporalNeighbors = dv.pages()
>     .where(p => p.file.path !== current.file.path)
>     .where(p => p.file.ctime >= threeDaysBefore && p.file.ctime <= threeDaysAfter)
>     .sort(p => Math.abs(p.file.ctime.ts - ctime.ts), "asc")
>     .limit(6);
> 
> if (temporalNeighbors.length > 0) {
>     dv.header(4, "⏰ Temporal Neighbors (±3 days)");
>     dv.table(
>         ["Note", "Created", "Type", "Shared Context?"],
>         temporalNeighbors.map(p => {
>             const daysDiff = Math.round((p.file.ctime.ts - ctime.ts) / (1000 * 60 * 60 * 24));
>             return [
>                 p.file.link,
>                 daysDiff === 0 ? "Same day" : (daysDiff > 0 ? `+${daysDiff}d` : `${daysDiff}d`),
>                 p.type || "—",
>                 current.file.outlinks.map(l => l.path).some(path => p.file.outlinks.map(l => l.path).includes(path)) ? "✅" : "—"
>             ];
>         })
>     );
> } else {
>     dv.paragraph("*No notes created within 3 days of this note.*");
> }
> ```





















> [!warning] ### 📅 Review Intelligence
> **Next Review**: `= this.next-review` | **Review Count**: `= this.review-count`
> **Review Status**: `= choice(this.next-review < date(today), "🔴 OVERDUE", choice(this.next-review = date(today), "🟡 Due Today", choice(dateformat(this.next-review, "yyyy-MM-dd") <= dateformat(date(today) + dur(7 days), "yyyy-MM-dd"), "🟢 This Week", "⚪ Scheduled")))`
> **Days Until Review**: `= choice(this.next-review, (this.next-review - date(today)).days + " days", "Not scheduled")`
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







Here's the **updated and enhanced version** using advanced DataviewJS features with better error handling, performance optimizations, and additional insights:

```dataviewjs
// SYSTEM: Enhanced Semantic Bridge Engine v2.0
// PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts) with advanced analytics

const current = dv.current();
const myOutlinks = current.file.outlinks?.map(l => l.path) || [];

// Performance optimization: Create Set for faster lookups
const myOutlinkSet = new Set(myOutlinks);
const currentPath = current.file.path;

// Advanced sibling analysis with metadata
const siblings = dv.pages()
  .where(p => {
    // Safety checks
    if (!p.file?.path || p.file.path === currentPath) return false;
    // Exclude already linked notes
    if (current.file.outlinks?.some(l => l.path === p.file.path)) return false;
    return true;
  })
  .map(p => {
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
  })
  .where(p => p.sharedCount > 0)
  .sort(p => p.similarityScore, "desc")
  .limit(8);

// Render enhanced semantic bridges
if (siblings.length > 0) {
  dv.header(3, "🔗 Semantic Bridges (Missing Connections)");
  
  // Add summary statistics
  const totalSharedConnections = siblings.reduce((sum, s) => sum + s.sharedCount, 0);
  const avgSimilarity = Math.round(siblings.reduce((sum, s) => sum + s.similarityScore, 0) / siblings.length);
  
  dv.paragraph(`**Found ${siblings.length} semantic siblings** • Total shared: ${totalSharedConnections} connections • Avg. similarity: ${avgSimilarity}%`);
  
  dv.table(
    ["Note", "Similarity", "Strength", "Maturity", "Type", "Shared Context"], 
    siblings.map(s => [
      s.link, 
      `📊${s.similarityScore}%`,
      "🔗" + s.sharedCount, 
      s.maturity === "evergreen" ? "🌳" + s.maturity : 
      s.maturity === "budding" ? "🌿" + s.maturity :
      s.maturity === "developing" ? "🌱" + s.maturity :
      s.maturity === "seedling" ? "大豆" + s.maturity : "❓unset",
      s.type,
      s.sharedLinks.slice(0, 2).map(l => l.displayName).join(", ") + (s.sharedCount > 2 ? "…" : "")
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

  // Advanced domain health metrics
  const totalNotes = domainNotes.length;
  const matureNotes = maturityDistribution.evergreen + maturityDistribution.budding;
  const coverage = totalNotes > 0 ? Math.round((matureNotes / totalNotes) * 100) : 0;
  
  // Domain activity score (based on recent modifications)
  const recentNotes = domainNotes.filter(p => {
    const daysOld = (new Date() - new Date(p.file.mtime)) / (1000 * 60 * 60 * 24);
    return daysOld < 30;
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
```

### Key Enhancements:

1. **Performance Optimizations**:
   - Uses `Set` for faster link lookups
   - Better null safety checks
   - Reduced redundant calculations

2. **Advanced Analytics**:
   - Similarity scoring algorithm
   - Domain activity metrics
   - Network intelligence scoring
   - Temporal analysis with insights

3. **Enhanced Visuals**:
   - Emoji indicators for maturity states
   - Health status indicators
   - Better formatting and organization

4. **New Features**:
   - Domain activity score (recent modifications)
   - Network intelligence metrics
   - Temporal review insights
   - Summary statistics

5. **Error Handling**:
   - Comprehensive null/undefined checks
   - Safe array operations
   - Type validation

This enhanced version provides much deeper insights into your knowledge base while maintaining performance and reliability. The semantic bridge engine now includes similarity scores, and the domain analysis adds activity metrics to complement maturity analysis.




The error occurs because `siblings` is not an array at that point. This can happen if the `.map()` operation fails or returns an unexpected type. Here's the **fixed version** with proper error handling and debugging:

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

### Key Fixes:

1. **Error Handling**: Added try/catch blocks around critical operations
2. **Array Validation**: Ensured `siblings` is always an array
3. **Null Safety**: Added proper null/undefined checks throughout
4. **Property Validation**: Checked for existence of properties before using them
5. **Fallback Values**: Provided default values for missing data
6. **Debugging**: Added console warnings for troubleshooting

The script now gracefully handles edge cases and provides informative output even when some data is missing or malformed.



## 🏷️ Tag Intelligence

> [!abstract] ### 🏷️ Tag Intelligence
> **Tag Count**: `= length(this.tags)` | **Unique Domains**: `= length(filter(this.tags, (t) => contains(t, "/")))` hierarchical tags
> **Tag Density**: `= choice(length(this.tags) < 3, "⚠️Sparse", choice(length(this.tags) > 10, "📚Rich", "✅Balanced"))`
> 
> ---
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



[!abstract] ### 🏷️ Tag Intelligence
**Tag Count**: `= length(this.tags)` | **Unique Domains**: `= length(filter(this.tags, (t) => contains(t, "/")))` hierarchical tags
**Tag Density**: `= choice(length(this.tags) < 3, "⚠️Sparse", choice(length(this.tags) > 10, "📚Rich", "✅Balanced"))`

---

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
        dv.header(5, "🏷️ Tag Siblings (Shared Taxonomy)");
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





## 🔗 Link Quality

> [!tip] ### 🔗 Link Quality Analytics
> **In-Links**: `= length(this.file.inlinks)` | **Out-Links**: `= length(this.file.outlinks)`
> **Link Ratio**: `= choice(length(this.file.outlinks) = 0, "∞ (no outlinks)", round(length(this.file.inlinks) / length(this.file.outlinks) * 100) / 100)`
> **Link Balance**: `= choice(length(this.file.inlinks) > length(this.file.outlinks) * 2, "📥 Receiver (heavily cited)", choice(length(this.file.outlinks) > length(this.file.inlinks) * 2, "📤 Contributor (cites many)", "⚖️ Balanced"))`
> **Connectivity Score**: `= round((length(this.file.inlinks) + length(this.file.outlinks)) / 2)` avg connections
> 
> ---
> 
> ```dataviewjs
> // LINK CHAIN DEPTH: How far this note reaches through outlinks
> const current = dv.current();
> const directOutlinks = current.file.outlinks.map(l => l.path);
> 
> // Second-degree connections (notes that my outlinks link to)
> let secondDegree = new Set();
> for (const path of directOutlinks) {
>     const page = dv.page(path);
>     if (page && page.file.outlinks) {
>         page.file.outlinks.forEach(l => {
>             if (l.path !== current.file.path && !directOutlinks.includes(l.path)) {
>                 secondDegree.add(l.path);
>             }
>         });
>     }
> }
> 
> dv.header(4, "🌐 Link Reach Analysis");
> dv.paragraph(`**Direct connections**: ${directOutlinks.length} notes`);
> dv.paragraph(`**2nd-degree reach**: ${secondDegree.size} additional notes`);
> dv.paragraph(`**Total network reach**: ${directOutlinks.length + secondDegree.size} notes (${Math.round((directOutlinks.length + secondDegree.size) / dv.pages().length * 100)}% of vault)`);
> ```

> [!tip] ### 🔗 Link Quality Analytics
> **In-Links**: `= length(this.file.inlinks)` | **Out-Links**: `= length(this.file.outlinks)`
> **Link Ratio**: `= choice(length(this.file.outlinks) = 0, "∞ (no outlinks)", round(length(this.file.inlinks) / length(this.file.outlinks) * 100) / 100)`
> **Link Balance**: `= choice(length(this.file.inlinks) > length(this.file.outlinks) * 2, "📥 Receiver (heavily cited)", choice(length(this.file.outlinks) > length(this.file.inlinks) * 2, "📤 Contributor (cites many)", "⚖️ Balanced"))`
> **Connectivity Score**: `= round((length(this.file.inlinks) + length(this.file.outlinks)) / 2)` avg connections
> 
> ---
> 
> ```dataviewjs
> // LINK CHAIN DEPTH: How far this note reaches through outlinks
> const current = dv.current();
> const directOutlinks = current.file.outlinks.map(l => l.path);
> 
> // Second-degree connections (notes that my outlinks link to)
> let secondDegree = new Set();
> for (const path of directOutlinks) {
>     const page = dv.page(path);
>     if (page && page.file.outlinks) {
>         page.file.outlinks.forEach(l => {
>             if (l.path !== current.file.path && !directOutlinks.includes(l.path)) {
>                 secondDegree.add(l.path);
>             }
>         });
>     }
> }
> 
> dv.header(4, "🌐 Link Reach Analysis");
> dv.paragraph(`**Direct connections**: ${directOutlinks.length} notes`);
> dv.paragraph(`**2nd-degree reach**: ${secondDegree.size} additional notes`);
> dv.paragraph(`**Total network reach**: ${directOutlinks.length + secondDegree.size} notes (${Math.round((directOutlinks.length + secondDegree.size) / dv.pages().length * 100)}% of vault)`);
> ```










