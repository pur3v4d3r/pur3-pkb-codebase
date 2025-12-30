---
aliases:
  - Self-Determination Theory
  - Self Determination Theory
tags:
  - type/permanent
  - year/2025
  - status/budding
  - educational-psychology
  - learning-science
  - processing-workflow
  - self-regulation/motivation
  - self-directed-learning
  - cognitive-resources
  - attention
  - self-regulation
  - learning-optimization
source: article
id: "20251213090604"
created: 2025-12-13T09:06:04
modified: 2025-12-13T09:06:04
week: "[[2025-W50]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: theory
maturity: seedling
confidence: speculative
next-review: 2025-12-20
link-up:
  - "[[educational-psychology-moc]]"
link-related:
  - "[[2025-12-13|Daily-Note]]"
  - "[[Autonomy]]"
  - "[[Competence]]"
  - "[[Relatedness]]"
  - "[[Intrinsic Motivation]]"
  - "[[Extrinsic Motivation]]"
status: active


review-last-reviewed: null
review-next-review: 2025-12-17
review-count: 0
review-interval: 3

review-priority: medium
---


> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Self-Determination Theory]]
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
# Foundational Understanding
> [!definition] # Definition
> [**Self-Determination Theory**:: Self-Determination Theory (SDT) is a macro theory of human motivation, development, and well-being developed by psychologists Edward L. Deci and Richard M. Ryan. It focuses on the degree to which an individual's behavior is self-motivated and self-determined. SDT posits that people are naturally endowed with an innate tendency toward growth, integration, and the proactive mastery of internal and external environments. This natural tendency flourishes when specific psychological needs are met.]
> 
> ##### [✅`= dateformat(this.file.ctime, "MMMM dd, yyyy")` - Initial Creation]


>[!phase-one] # Overview
> ## Self-Determination Theory (SDT)
> 
> >[! ] ### I. Introduction
> > - A. Definition: A macro theory of human motivation, personality, and well-being focused on the innate psychological needs and the degree to which an individual's behavior is self-motivated and self-determined.
> > - B. Founders: Edward L. Deci and Richard M. Ryan (1985, 2000).
> > - C. Core Premise: **Organismic Dialectical Perspective**
> >     - 1. Humans are active, growth-oriented organisms.
> >     - 2. Social contexts can either support or thwart these natural tendencies.
> >     - 3. The interplay between individuals' inner resources and social environments.
> 
> >[! ] ### II. Basic Psychological Needs Theory (BPNT)
> > - A. Three Universal, Innate Psychological Needs (Essential for psychological growth, integrity, and well-being):
> >     - 1. **Autonomy**: The need to experience choice and volition, feeling like the origin of one's own actions rather than being controlled.
> >     - 2. **Competence**: The need to feel effective in interacting with the environment, experiencing mastery and efficacy.
> >     - 3. **Relatedness**: The need to feel connected to others, experiencing care and belongingness.
> > - B. Need Satisfaction vs. Need Frustration: Direct impact on well-being, motivation, and psychological health.
> > - C. Cross-Cultural Applicability: Proposed to be universal, though expressions may vary culturally.
> 
> >[! ] ### III. Motivation Continuum (Organismic Integration Theory - OIT)
> > - A. Amotivation: Lack of intention or motivation to act.
> > - B. Extrinsic Motivation: Performing an activity to attain some separable outcome.
> >     - 1. **External Regulation**: Behavior controlled by external rewards or punishments (e.g., studying for a grade).
> >     - 2. **Introjected Regulation**: Behavior performed to avoid guilt or enhance ego (e.g., exercising to avoid feeling ashamed).
> >     - 3. **Identified Regulation**: Behavior performed because it is personally valued and consciously chosen (e.g., volunteering because it aligns with personal values).
> >     - 4. **Integrated Regulation**: Behavior is fully assimilated with one's self and values; most autonomous form of extrinsic motivation (e.g., choosing a career path that reflects deeply held beliefs).
> > - C. Intrinsic Motivation: Performing an activity for its inherent satisfaction, enjoyment, or interest.
> 
> >[! ] ### IV. Key Mini-Theories (Complementing BPNT and OIT)
> > - A. **Cognitive Evaluation Theory (CET)**
> >     - 1. Focus: How social and environmental factors (e.g., rewards, feedback) affect intrinsic motivation and autonomy.
> >     - 2. Impact on perceived locus of causality and perceived competence.
> > - B. **Causality Orientations Theory (COT)**
> >     - 1. Focus: Individual differences in people's general motivational styles toward the environment (e.g., autonomous, controlled, impersonal orientations).
> > - C. **Goal Content Theory (GCT)**
> >     - 1. Focus: The impact of different types of goals (intrinsic vs. extrinsic) on psychological well-being.
> >     - 2. Intrinsic goals (e.g., personal growth, community contribution) are associated with higher well-being than extrinsic goals (e.g., wealth, fame).
> > - D. **Relationship Motivation Theory (RMT)**
> >     - 1. Focus: The role of basic psychological needs in the formation and maintenance of close relationships.
> 
> >[! ] ### V. Applications and Implications
> > - A. **Education**: Fostering student engagement, creativity, and deeper learning.
> > - B. **Work and Organizations**: Enhancing employee satisfaction, productivity, and organizational commitment.
> > - C. **Healthcare**: Promoting adherence to treatment, healthy lifestyle changes, and patient well-being.
> > - D. **Parenting and Child Development**: Supporting children's autonomy and intrinsic motivation.
> > - E. **Sports and Exercise**: Increasing participation and sustained engagement.
> > 
> >[! ] #### VI. Criticisms and Future Directions
> > - A. **Cultural Specificity Debate**: While universal, cultural contexts influence expression and pathways to satisfaction.
> > - B. **Measurement Challenges**: Developing robust and culturally sensitive measures for needs satisfaction.
> > - C. **Integration with other theories**: Exploring connections with positive psychology, mindfulness, and neurobiology.
> > - 

>[! ] ## Introduction

> [!ask-yourself-this] ## Core Concepts: The Three Basic Psychological Needs
> **Note**: At the heart of SDT are three universal and innate psychological needs, the satisfaction of which is essential for psychological growth, integrity, well-being, and vitality.
> 
> ---
> 
> ### 1. Autonomy
> The need to feel like the origin of one's own actions; to experience a sense of choice, volition, and freedom in initiating and regulating one's behavior. This is not about independence from others, but rather about acting with a sense of personal endorsement and wholeheartedness.
> 
> ---
> 
> ### 2. Competence
> The need to feel effective in one's interactions with the environment; to experience opportunities to exercise and express one's capabilities, and to attain desired outcomes. This involves feeling capable and successful in mastering challenging tasks and environments.
> 
> ---
> 
> ### 3. Relatedness
> The need to feel connected to others; to experience a sense of belonging, intimacy, and secure attachment with important people in one's life. This involves feeling cared for, valued, and respected by others, and having the opportunity to care for others.

>[! ] ## Mini-Theories within SDT
> SDT is comprised of several interconnected mini-theories that elaborate on specific aspects of motivation and personality:
> 
> >[!the-goal] ### 1. Cognitive Evaluation Theory (CET)
> > 
> > Focuses on intrinsic motivation, explaining how external factors (like rewards, feedback, controls) affect an individual's intrinsic motivation. It suggests that factors perceived as controlling tend to undermine autonomy and intrinsic motivation, while factors perceived as informational (e.g., positive feedback) can enhance competence and intrinsic motivation.
> 
> >[!the-goal] ### 2. Organismic Integration Theory (OIT)
> > Details the different forms of extrinsic motivation and the factors that promote or hinder their internalization and integration. It describes a continuum of motivation from amotivation to intrinsic motivation, including various types of extrinsic regulation:
> > *   **External Regulation**: Behavior controlled by external rewards/punishments.
> > *   **Introjected Regulation**: Behavior driven by internal pressures, guilt, or ego-enhancement.
> > *   **Identified Regulation**: Behavior is personally valued and consciously chosen.
> > *   **Integrated Regulation**: Behavior is fully assimilated with one's self and values, leading to coherent self-regulation.
> 
> >[!the-goal] ### 3. Causality Orientations Theory (COT)
> > Describes individual differences in people's general motivational styles or orientations toward the environment. It identifies three orientations:
> > *   **Autonomous Orientation**: Individuals are guided by their interests and values.
> > *   **Controlled Orientation**: Individuals are sensitive to external controls and internal demands.
> > *   **Impersonal Orientation**: Individuals feel incompetent and attribute outcomes to forces beyond their control.
> 
> >[!the-goal] ### 4. Basic Psychological Needs Theory (BPNT)
> > Asserts the universality of the three basic psychological needs (autonomy, competence, relatedness) across cultures and life stages, emphasizing that their satisfaction is essential for psychological health and well-being.
> 
> >[!the-goal] ### 5. Goal Contents Theory (GCT)
> > Distinguishes between different types of goals individuals pursue, categorizing them as either intrinsic (e.g., community contribution, personal growth) or extrinsic (e.g., financial success, physical attractiveness, fame). It posits that pursuing intrinsic goals is more directly linked to need satisfaction and well-being than pursuing extrinsic goals.
> 
> >[!the-goal] ### 6. Relationships Motivation Theory (RMT)
> > Examines how the three basic psychological needs are fulfilled within close relationships, and how this satisfaction contributes to relationship quality and individual well-being within those relationships.


> [! ] ### Applications of SDT
> SDT has broad applications across various domains, including:
> 
> *   **Education**: Designing curricula and teaching methods that foster student autonomy, competence, and relatedness to enhance engagement and learning.
> *   **Workplace**: Creating work environments that support employee autonomy, provide opportunities for mastery, and foster positive team dynamics to boost job satisfaction, productivity, and retention.
> *   **Healthcare**: Motivating patients for behavior change by supporting their autonomy in treatment decisions, building confidence in managing their health, and fostering supportive relationships with providers.
> *   **Sports & Exercise**: Designing training programs and coaching styles that enhance athletes' sense of choice, competence, and connection to their team or activity.
> *   **Parenting**: Encouraging child development by providing choices, supporting their efforts, and fostering warm, supportive relationships.



>[! ] # Conclusion
> Self-Determination Theory provides a powerful framework for understanding human motivation, personality development, and well-being. By emphasizing the fundamental role of the innate psychological needs for autonomy, competence, and relatedness, SDT highlights the conditions under which individuals flourish, achieve optimal functioning, and experience sustained personal growth. Understanding and supporting these needs in various life contexts is crucial for fostering engagement, vitality, and overall psychological health.

---

>[! ] ### 🔗Backlinks & Connections
> ```dataview
> TABLE 
>     type AS "Type",
>     maturity AS "Maturity",
>     created AS "Created"
> FROM [[#]]
> SORT created DESC
> LIMIT 15
> ```

> [!warning] ### 📅 Review Intelligence
> **Next Review**: `= this.next-review` | **Review Count**: `= this.review-count`
> **Review Status**: `= choice(this.next-review < date(today), "🔴 OVERDUE", choice(this.next-review = date(today), "🟡 Due Today", choice(dateformat(this.next-review, "yyyy-MM-dd") <= dateformat(date(today) + dur(7 days), "yyyy-MM-dd"), "🟢 This Week", "⚪ Scheduled")))`
> **Days Until Review**: `= choice(this.next-review, (this.next-review - date(today)).days + " days", "Not scheduled")`

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
---

### 📖 Extracted Definitions From Cognitive Science
```dataviewjs
try {
  // Configuration
  const folderPath = "03-notes/01_permanent-notes/01_cognitive-development"; // Change this to your folder
  
  // Get all pages from the specified folder
  const pages = dv.pages(`"${folderPath}"`);
  
  // Storage for all definitions across files
  let allDefinitions = [];
  
  // Process each file
  for (let page of pages) {
    try {
      const content = await dv.io.load(page.file.path);
      const bracketedFieldRegex = /\[\*\*([^*]+?)\*\*::\s*([^\]]+?)\]/g;
       
      let match;
      while ((match = bracketedFieldRegex.exec(content)) !== null) {
        allDefinitions.push({
          source: page.file.link,
          key: match[1].trim(), // This is the clean term without ** markdown
          value: match[2].trim()
        });
      }
    } catch (e) {
      console.warn(`Error processing file ${page.file.path}:`, e);
      continue;
    }
  }
  
  // Display aggregated results
  if (allDefinitions.length > 0) {
    dv.header(3, `📚 All Definitions Across ${folderPath} (${allDefinitions.length} total)`);
    
    // Group by first letter (using the clean key)
    const grouped = {};
    allDefinitions.forEach(d => {
      const firstLetter = d.key[0].toUpperCase();
      if (!grouped[firstLetter]) grouped[firstLetter] = [];
      grouped[firstLetter].push(d);
    });
    
    // Sort letters alphabetically
    const sortedLetters = Object.keys(grouped).sort();
    
    // Display grouped results
    for (let letter of sortedLetters) {
      dv.header(4, `${letter} (${grouped[letter].length} terms)`);
      dv.table(
        ["📄 Source", "🔑 Term", "📝 Definition"],
        grouped[letter].map(d => [
          d.source,
          `**${d.key}**`,
          d.value
        ])
      );
      dv.paragraph(""); // Add spacing between groups
    }
    
  } else {
    dv.paragraph(`*No bracketed inline fields found in "${folderPath}".*`);
  }
  
} catch (error) {
  console.error("Error in definitions aggregation script:", error);
  dv.paragraph("*Error loading definitions. Check console for details.*");
}
```


---
