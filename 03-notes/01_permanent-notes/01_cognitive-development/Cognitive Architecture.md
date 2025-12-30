---
aliases:
  - Cognitive Architecture
  - cognitive architecture
  - AI Architecture
  - Mind Models
  - Cognitive Systems
tags:
  - type/permanent
  - year/2025
  - status/in-progress
  - cognitive-science
  - artificial-intelligence
  - processing-workflow
  - cognitive-science/executive-function
  - learning-processes
  - ACT-R
  - working-memory
  - executive-function
  - cognitive-modeling
  - neuroscience
source: claude-sonnet-4.5
id: "20251129024304"
created: 2025-11-29T02:43:04
modified: 2025-11-29T02:43:04
week: "[[2025-W48]]"
month: "[[2025-11]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: theory
maturity: seedling
confidence: speculative
next-review: 2025-12-06
link-up:
  - "[[99-archive/05-moc's/cognitive-science-moc]]"
link-related:
  - "[[2025-12-13|Daily-Note]]"
  - "[[2025-11-29|Daily-Note]]"
link-count: 0
backlink-count: 0
summary: A cognitive architecture is a theoretical framework for the structure of intelligent systems, aiming to define the fixed parts of a mind and how they interact to produce intelligent behavior.
status: active


review-last-reviewed: null
review-next-review: 2025-12-17
review-count: 0
review-interval: 3

review-priority: medium
---

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Cognitive Architecture]]
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
> [**Cognitive Architecture**:: Cognitive architecture refers to a broad theory about the structure of the human mind or a computational framework designed to emulate human-like intelligence. It provides a fixed, foundational structure that enables a system to perceive, understand, learn, remember, and reason, ultimately allowing it to perform intelligent tasks and adapt to its environment.]
> 
> ##### [✅`= dateformat(this.file.ctime, "MMMM dd, yyyy")` - Initial Creation]

> [!plan] # Overview
> ### Cognitive Architecture
> 
> - **Definition and Purpose**
>     - What is a Cognitive Architecture?
>     - Goals and Objectives
>     - Core Assumptions
> - **Historical Context**
>     - Early Theories of Mind
>     - Emergence of Computational Models
>     - Evolution of Architectures
> - **Key Components of Cognitive Architectures**
>     - Memory Systems
>         - Working Memory
>         - Long-Term Memory (Semantic, Episodic, Procedural)
>     - Perceptual Systems
>     - Motor/Action Systems
>     - Learning Mechanisms
>     - Problem-Solving and Reasoning Modules
>     - Control Structures
> - **Major Cognitive Architectures**
>     - **Symbolic Architectures**
>         - **SOAR (State Operator And Result)**
>             - Principles: Problem space, universal subgoaling, chunking
>             - Key features and components
>             - Applications
>         - **ACT-R (Adaptive Control of Thought—Rational)**
>             - Principles: Modules, buffers, production rules
>             - Declarative and Procedural knowledge
>             - Applications and successes
>         - **LIDA (Learning Intelligent Distribution Agent)**
>             - Principles: Global Workspace Theory, "sense-think-act" cycle
>             - Modules: Sensory, Perceptual, Working Memory, Procedural Memory, Attention Codelet Pool
>             - Applications
>     - **Connectionist/Sub-symbolic Architectures**
>         - Principles: Neural networks, distributed representation
>         - Examples (though often integrated into hybrid models)
>     - **Hybrid Architectures**
>         - **CLARION (Connectionist Learning with Adaptive Rule Induction ON-line)**
>             - Principles: Dual-representation (implicit/explicit), bottom-up/top-down learning
>             - Modules: Action-centered subsystem, non-action-centered subsystem
>             - Applications
>         - **Other Hybrid Approaches**
> - **Fundamental Concepts and Principles**
>     - Modularity vs. Distributed Processing
>     - Embodiment and Situated Cognition
>     - Learning and Adaptation
>     - Attention and Consciousness
>     - Rationality and Bounded Rationality
> - **Applications and Impact**
>     - Artificial Intelligence (AI)
>     - Robotics
>     - Human-Computer Interaction (HCI)
>     - Cognitive Modeling and Simulation
>     - Understanding Human Cognition
> - **Challenges and Future Directions**
>     - Integration of Levels of Cognition (micro vs. macro)
>     - Bridging Symbolic and Sub-symbolic Gaps
>     - Handling Open-Ended Learning
>     - Scalability and Complexity
>     - Ethical Considerations
>     - Towards General Artificial Intelligence (AGI)

>[!fleeting-thought] ## Core Concepts
>
> *   **Definition:** A fixed set of mechanisms that underlie and constrain cognitive processes. It's not a specific algorithm, but rather a blueprint for how different cognitive functions interact.
> *   **Purpose:**
>     *   **Understanding Human Cognition:** To develop computational models that explain and predict human behavior and mental processes.
>     *   **Building Intelligent Systems:** To create artificial intelligence (AI) systems that exhibit human-like flexibility, learning, and reasoning across diverse tasks.
>     *   **General Intelligence:** To move beyond narrow AI toward systems capable of general problem-solving and adaptation.
> 
> > [!gemini-pro-response] ## Key Components and Characteristics
> > 
> > Most cognitive architectures propose a set of fundamental, interacting components:
> > 
> > *   **Memory Systems:**
> >     *   **Working Memory:** Short-term, limited capacity storage for actively processing information.
> >     *   **Long-Term Memory:** Permanent storage for knowledge and experiences. Often subdivided into:
> >         *   **Declarative Memory:** Facts and events (e.g., semantic, episodic).
> >         *   **Procedural Memory:** Skills and habits ("knowing how").
> > *   **Perceptual Systems:** Mechanisms for receiving and interpreting sensory information from the environment (e.g., vision, audition).
> > *   **Motor Systems:** Mechanisms for generating actions and interacting with the physical world.
> > *   **Cognitive Control/Executive Functions:** Processes responsible for planning, decision-making, attention allocation, problem-solving, and goal management.
> > *   **Learning Mechanisms:** Capabilities to acquire new knowledge, skills, and adapt behaviors over time (e.g., reinforcement learning, supervised learning, chunking).
> > *   **Knowledge Representation:** How information is stored and organized within the system (e.g., symbolic, connectionist, hybrid).


>[! ] ### Prominent Examples of Cognitive Architectures
>
> 
> Several influential cognitive architectures have been developed, each with distinct features:
> 
> *   **SOAR (State, Operator, And Result):**
>     *   **Focus:** Problem-solving and learning from experience.
>     *   **Key Idea:** All goal-oriented behavior is formulated as problem-solving in problem spaces. Learning occurs through "chunking" — compiling sequences of successful operations into new, executable knowledge.
> *   **ACT-R (Adaptive Control of Thought—Rational):**
>     *   **Focus:** Modeling human cognition across a wide range of tasks, emphasizing the interaction between declarative and procedural knowledge.
>     *   **Key Idea:** Uses a modular structure with symbolic modules (e.g., declarative memory) and subsymbolic processes (e.g., activation spreading, utility learning) to model resource allocation and timing.
> *   **CLARION (Connectionist Learning with Adaptive Rule Induction ON-line):**
>     *   **Focus:** Modeling the interaction between implicit and explicit knowledge, and bottom-up/top-down learning.
>     *   **Key Idea:** Features a dual-representational structure where implicit knowledge is learned via neural networks and explicit knowledge is represented by symbolic rules, which can influence each other.
> *   **LIDA (Learning Intelligent Distribution Agent):**
>     *   **Focus:** A comprehensive architecture inspired by Global Workspace Theory, aiming to model human-like awareness and attention.
>     *   **Key Idea:** Emphasizes perception-action cycles, where information from various sensory modalities competes for "attention" to enter a global workspace, leading to action selection.
> >[! ] #### Significance and Applications
> > 
> > Cognitive architectures are crucial for:
> > 
> > *   **Developing General AI:** Providing a framework for building AI systems that are not limited to narrow tasks but can learn and adapt broadly.
> > *   **Cognitive Modeling:** Creating precise, testable models of human psychological phenomena, leading to deeper insights into how the mind works.
> > *   **Robotics:** Endowing robots with more intelligent, flexible, and adaptive control mechanisms.
> > *   **Human-Computer Interaction (HCI):** Designing user interfaces and systems that align better with human cognitive processes.
> > *   **Education and Training:** Informing the design of intelligent tutoring systems and training methodologies.
> > 
> > >[! ] #### Challenges and Future Directions
> > > 
> > > *   **Complexity and Scalability:** Building and validating comprehensive architectures that scale to real-world complexity is a significant challenge.
> > > *   **Integration:** Effectively integrating diverse cognitive functions (e.g., perception, emotion, social cognition) within a unified framework.
> > > *   **Neuroscientific Plausibility:** Bridging the gap between high-level cognitive models and low-level neural mechanisms.
> > > *   **Learning and Adaptation:** Developing architectures that can continuously learn from experience, adapt to novelty, and transfer knowledge across domains.
> > > 
> > > Cognitive architecture remains a vibrant and essential field, driving progress in both artificial intelligence and our fundamental understanding of the human mind.
> > >


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
> **Days Until Review**: `= choice(this.next-review, (this.next-review - date(today)).days + " days", "Not scheduled")

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

# Cognitive Architecture



## 📊 Note Metadata Dashboard

**Development Status**: `= this.maturity`  
**Epistemic Confidence**: `= this.confidence`  
**Next Review**: `= this.next-review`  
**Review Count**: `= this.review-count`  
**Created**: `= this.created`  
**Last Modified**: `= this.modified`



## Related Notes

```dataview
TABLE type, maturity, confidence
FROM [[]]
WHERE type = "theory"
SORT "maturity" DESC
LIMIT 10
```

## Evolution Log

> [!timeline] Development History
> `= this.review-count` total reviews

### 2025-11-29 - Initial Creation
**Context**: `=this.summary`
**Maturity**: `= this.maturity`  
**Confidence**: `= this.confidence`

---

## 📚 Sources & References

```dataview
TABLE 
    source AS "Source Type",
    created AS "Date Added"
FROM [[]]
WHERE source
SORT created DESC
```

## 🔗 Backlinks & Connections
```dataview
TABLE 
    type AS "Type",
    maturity AS "Maturity",
    created AS "Created"
FROM [[#]]
SORT created DESC
LIMIT 15
```

---


---

## 🏷️ Tags & Classification

Primary Tags: `= this.tags`  
Type: `= this.type`  
Source: `= this.source`

---