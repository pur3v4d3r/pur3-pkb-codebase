---
aliases:
  - Meta-Level Cognition
  - meta-level cognition
tags:
  - type/permanent
  - year/2025
  - type/report
  - status/budding
  - cognitive-psychology
  - cognitive-science
  - processing-workflow
  - cognitive-science/metacognition
  - metacognitive-monitoring
  - dual-process-theory
  - attention
  - executive-function
  - cognitive-pkm
  - project/pur3v4d3r
  - type/report/psychology
source: ""
id: 20251104-041821
created: 2025-12-13T00:59:15
modified: 2025-12-13T00:59:15
week: "[[2025-W50]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: 🧬concept
maturity: seedling
confidence: speculative
next-review: 2025-12-20
link-up: "[[🧠Report_A-Comprehensive-Analysis-of-Metacognition-as-the-Central-Integrating-Mechanism-for-Personal-Development_🆔20251028024951]]"
link-related:
  - "[[2025-12-13|Daily-Note]]"
  - "[[Metacognitive Experiences]]"
  - "[[Metacognitive Knowledge]]"
  - "[[Constructivist Learning]]"
title: Meta-Level Cognition
status: active
rating: ""
url: ""
date created: 2025-11-04T04:17:20
date modified: 2025-11-05T21:47:59


review-last-reviewed: null
review-next-review: 2025-12-17
review-count: 0
review-interval: 3

review-priority: medium
---

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Meta-Level Cognition]]
> - **MOC**: `this.link-up`

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
> [**Meta-Level Cognition**:encompasses a broad range of mental activities that involve monitoring and controlling one's own cognitive processes. It's crucial for effective learning, problem-solving, and decision-making, allowing individuals to become more strategic and efficient thinkers.]
> 
> ##### [✅`= dateformat(this.file.ctime, "MMMM dd, yyyy")` - Initial Creation]


>[! ] ## Outline
> - ## **Meta-Level Cognition**
>     - **Definition**
>         - Cognition about cognition
>         - Thinking about thinking
>         - Awareness and control of one's own thought processes
>     - **Key Components**
>         - *Metacognitive Knowledge*
>             - Person knowledge (e.g., "I learn best by doing")
>             - Task knowledge (e.g., "Memorizing poetry is harder than reading an article")
>             - Strategy knowledge (e.g., "Summarizing helps me understand")
>         - *Metacognitive Regulation*
>             - Planning (e.g., setting goals, allocating resources)
>             - Monitoring (e.g., checking progress, understanding comprehension)
>             - Evaluating (e.g., assessing outcomes, reflecting on strategy effectiveness)
>         - *Metacognitive Experiences*
>             - Feelings and judgments (e.g., "feeling of knowing," "feeling of confusion")
>             - Subjective awareness during cognitive tasks
>     - **Importance and Benefits**
>         - *Enhanced Learning*
>             - Improved comprehension and retention
>             - Strategic problem-solving
>             - Self-directed learning
>         - *Better Decision-Making*
>         - *Increased Self-Awareness*
>         - *Improved Self-Regulation*
>     - **Development of Metacognition**
>         - Early childhood development
>         - Influencing factors (e.g., instruction, experience)
>     - **Applications**
>         - *Education*
>             - Promoting effective study habits
>             - Teaching critical thinking
>         - *Psychology and Therapy*
>             - Cognitive Behavioral Therapy (CBT)
>             - Mindfulness practices
>         - *Everyday Life*
>             - Time management
>             - Conflict resolution
>     - **Strategies for Developing/Improving Metacognition**
>         - Self-Questioning (e.g., "What do I already know?", "How am I doing?")
>         - Reflective Journaling
>         - Planning and Goal Setting
>         - Monitoring Progress
>         - Self-Correction and Evaluation
>         - Using Metacognitive Prompts
>         - Explicit Instruction in Metacognitive Strategies


> [! ] ## Introduction
> Meta-level cognition, often referred to as **metacognition**, is the human ability to think about one's own thinking. It involves an awareness of one's thought processes, understanding how one learns, and the capacity to regulate these processes to achieve cognitive goals. Essentially, it's "cognition about cognition."
> 
> ---
> 
> ##### What is Meta-Level Cognition?
> Meta-level cognition encompasses a broad range of mental activities that involve monitoring and controlling one's own cognitive processes. It's crucial for effective learning, problem-solving, and decision-making, allowing individuals to become more strategic and efficient thinkers.
> 

>[! ] ## Key Components
> <u>Metacognition</u> is <span style='color: #d8be34;'>typically broken down</span> into <span style='font-size: 1.3em;'><u><span style='color: #ff0075;'>two main components</span></u></span>:
> ---
> ##### 1. Metacognitive Knowledge
> This refers to what individuals know about themselves as cognitive beings, about tasks, and about strategies.
> *   **Person Variables**: Knowledge about one's own cognitive strengths and weaknesses (e.g., "I learn best by making flashcards," or "I struggle with abstract concepts without concrete examples").
> *   **Task Variables**: Knowledge about the nature of a task and the demands it places on one's cognitive system (e.g., "This essay requires deep analysis, not just summarization," or "Memorizing dates is different from understanding a historical trend").
> *   **Strategy Variables**: Knowledge about available strategies and their effectiveness for different tasks and goals (e.g., "Rereading is less effective than active recall for long-term retention," or "Mind mapping helps me organize complex ideas").
> 
> ##### 2. Metacognitive Regulation
> This refers to the processes used to control and monitor one's cognitive activities during learning and problem-solving. It involves three key stages:
> *   **Planning**: Setting goals, activating relevant background knowledge, and selecting appropriate strategies before engaging in a task (e.g., "Before reading this chapter, I'll skim the headings and formulate questions").
> *   **Monitoring**: Continuously checking one's understanding and progress during a task, making adjustments as needed (e.g., "Am I understanding this paragraph? If not, I need to reread or look up terms"). This often involves **metacognitive experiences** like the "feeling of knowing" or "judgment of learning."
> *   **Evaluating**: Assessing the outcome of one's cognitive efforts and the effectiveness of the strategies used after completing a task (e.g., "Did my study method work for the exam? What could I do differently next time?").

>[! ] #### Benefits of Developing Meta-Level Cognition
> Cultivating metacognitive skills offers numerous advantages:
> 
> *   **Improved Learning & Memory**: Learners become more aware of what they know and what they don't, leading to more targeted and effective study strategies.
> *   **Enhanced Problem-Solving**: Individuals can better assess the nature of a problem, select appropriate strategies, and monitor their progress towards a solution.
> *   **Better Decision-Making**: By reflecting on their thought processes, individuals can identify biases, evaluate evidence more critically, and make more informed choices.
> *   **Increased Self-Awareness**: A deeper understanding of one's own cognitive processes fosters greater self-knowledge and intellectual humility.
> *   **More Effective Self-Regulation**: The ability to plan, monitor, and evaluate one's thinking contributes to greater autonomy and control over one's intellectual development.

>[! ] ### Meta-Level Cognition in Obsidian
> 
> Obsidian, as a personal knowledge management (PKM) system, provides an excellent environment for practicing and enhancing meta-level cognition. Its flexible, graph-based structure inherently supports reflective practices.
> 
> ##### 1. [Planning]
> *   **Outline Notes**: Creating structured outlines for projects, essays, or learning new topics.
> *   **Project Notes**: Defining goals, listing tasks, and linking to relevant resources.
> *   **Goal Setting**: Using daily notes or dedicated "MOCs" (Maps of Content) to articulate learning objectives and plan how to achieve them.
> 
> ##### 2. [Monitoring]
> *   **Reviewing Notes**: Regularly revisiting notes to check understanding, identify gaps, and consolidate knowledge.
> *   **Linking Ideas**: Actively creating connections between disparate notes helps to see the bigger picture and identify areas where understanding is weak or incomplete.
> *   **Graph View**: Visually inspecting the connections in your vault can reveal clusters of ideas, isolated concepts, or unexpected relationships, prompting further inquiry.
> *   **Questions in Notes**: Writing down questions as they arise in your notes serves as a powerful monitoring tool, indicating areas needing further thought or research.
> 
> ##### 3. [Evaluating]
> *   **Reflective Journaling**: Using daily notes or dedicated "reflection" notes to ponder what was learned, what worked well, and what could be improved in your learning process.
> *   **Refactoring Notes**: Revisiting and reorganizing existing notes (e.g., merging, splitting, renaming) demonstrates an evolving understanding and an evaluation of the clarity and utility of your knowledge structure.
> *   **Identifying New Connections**: As your understanding grows, you'll naturally find new ways to connect existing notes, which is a form of metacognitive evaluation of your knowledge base.
> *   **Tags & Properties (YAML)**: Using tags or properties to categorize learning phases, confidence levels, or areas of uncertainty (e.g., `#review`, `status: draft`, `confidence: low`) can help track and evaluate progress.
> 


>[! ] ## Conclusion
> 
> Meta-level cognition is a fundamental skill for lifelong learning and effective thinking. By consciously engaging in the planning, monitoring, and evaluating of our own cognitive processes, we can become more strategic learners, better problem-solvers, and more reflective individuals. Tools like Obsidian, with their emphasis on interconnectedness and personal knowledge construction, offer a fertile ground for cultivating and exercising these vital metacognitive abilities.

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

> [!definition]
> [[Meta-Level Cognition]]
> - **Definition**: **Thinking** about **one's own** *thinking processes*.
