---
aliases:
  - cognitive psychology
  - Cognitive Psychology
  - Cognitive Science
  - Cognition Science
  - Study of Mind
tags:
  - type/permanent
  - year/2025
  - status/seedling
  - cognitive-psychology
  - cognitive-science
  - processing-workflow
  - cognitive-science/memory
  - learning-processes
  - information-processing-theory
  - perception
  - reasoning
  - applied-cognition
  - permanent-note
  - permanent-note/project-pur3v4d3r
  - permanent-note/pkb
source: ""
id: 20251108-004526
created: 2025-12-13T05:41:24
modified: 2025-12-13T05:41:24
week: "[[2025-W50]]"
month: "[[2025-12]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: 🧬concept
maturity: seedling
confidence: speculative
next-review: 2025-12-20
link-up:
  - "[[99-archive/05-moc's/cognitive-science-moc]]"
  - "[[self-learning-and-cognitive-development-moc]]"
link-related:
  - "[[2025-12-13|Daily-Note]]"
title: Cognitive Psychology
summary: Cognitive psychology is the scientific study of mental processes such as attention, language use, memory, perception, problem-solving, and thinking. It explores how people acquire, process, and store information.
status: active


review-last-reviewed: null
review-next-review: 2025-12-17
review-count: 0
review-interval: 3

review-priority: medium
---

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Cognitive Psychology]]
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
> [**Cognitive Psychology**:: Is a subdiscipline of psychology that investigates internal mental processes such as problem solving, memory, learning, and language. It is concerned with how people perceive, think, remember, and learn. Emerging in the mid-20th century as a significant departure from behaviorism, cognitive psychology views the mind as an information processor.]
> 
> ##### [✅`= dateformat(this.file.ctime, "MMMM dd, yyyy")` - Initial Creation]


>[! ] # Cognitive Psychology Outline
> 
> -   **Definition and Scope**
>     -   What is Cognitive Psychology?
>         -   Study of mental processes
>         -   Focus on how people think, perceive, remember, and learn
>     -   Relationship to other fields
>         -   Neuroscience (Cognitive Neuroscience)
>         -   Computer Science (Artificial Intelligence)
>         -   Linguistics
>         -   Philosophy
> -   **Core Cognitive Processes**
>     -   **Perception**
>         -   Bottom-up vs. Top-down processing
>         -   Object recognition
>         -   Sensory perception (visual, auditory, haptic)
>         -   Attention and perception
>     -   **Attention**
>         -   Selective attention
>         -   Divided attention
>         -   Sustained attention
>         -   Models of attention (e.g., Broadbent, Treisman)
>     -   **Memory**
>         -   Sensory memory
>         -   Short-term memory / Working memory
>             -   Baddeley's Model
>         -   Long-term memory
>             -   Declarative (Explicit) memory
>                 -   Episodic memory
>                 -   Semantic memory
>             -   Non-declarative (Implicit) memory
>                 -   Procedural memory
>                 -   Priming
>                 -   Classical conditioning
>         -   Memory processes (encoding, storage, retrieval)
>         -   Forgetting and memory distortion
>     -   **Language**
>         -   Language acquisition
>         -   Language comprehension
>         -   Language production
>         -   Components of language (phonology, morphology, syntax, semantics, pragmatics)
>         -   Brain and language (Broca's area, Wernicke's area)
>     -   **Problem Solving**
>         -   Types of problems
>         -   Problem-solving strategies (algorithms, heuristics)
>         -   Obstacles to problem solving (fixation, mental set)
>         -   Creativity and insight
>     -   **Decision Making**
>         -   Rational choice theory
>         -   Heuristics and biases (availability, representativeness, anchoring)
>         -   Framing effects
>         -   Risk assessment
>     -   **Reasoning**
>         -   Deductive reasoning
>         -   Inductive reasoning
>         -   Informal reasoning
> -   **Research Methods**
>     -   **Behavioral Methods**
>         -   Reaction time studies
>         -   Accuracy measures
>         -   Eyetracking
>     -   **Neuroscience Methods**
>         -   fMRI (functional Magnetic Resonance Imaging)
>         -   EEG (Electroencephalography)
>         -   MEG (Magnetoencephalography)
>         -   TMS (Transcranial Magnetic Stimulation)
>         -   Lesion studies
>     -   **Computational Modeling**
>     -   **Case Studies**
> -   **Applications of Cognitive Psychology**
>     -   Education (learning strategies, instructional design)
>     -   Human-computer interaction (usability, interface design)
>     -   Clinical psychology (cognitive behavioral therapy, memory disorders)
>     -   Forensic psychology (eyewitness testimony)
>     -   Artificial intelligence (developing intelligent systems)
>     -   Ergonomics and human factors
> -   **Historical Context**
>     -   Roots in Structuralism and Functionalism
>     -   Behaviorism's dominance and limitations
>     -   The "Cognitive Revolution" (1950s-1960s)
>         -   Influence of computer science and information theory
>         -   Key figures (e.g., Ulric Neisser, George Miller, Noam Chomsky, Herbert Simon)
>     -   Contemporary trends (e.g., embodied cognition, situated cognition)

>[! ] ### Core Areas of Study
> 
> Cognitive psychology delves into a wide range of mental operations, often broken down into specific domains:
> 
> -   **Perception:** How sensory information is received, interpreted, and organized to form a conscious experience of the world. This includes visual, auditory, and other sensory processes.
> -   **Attention:** The mechanisms by which the mind focuses on certain stimuli or tasks while ignoring others. This involves selective attention, sustained attention, and divided attention.
> -   **Memory:** The processes involved in encoding, storing, and retrieving information. Key distinctions include:
>     -   **Sensory Memory:** Brief storage of sensory information.
>     -   **Short-Term/Working Memory:** Temporary storage and manipulation of information.
>     -   **Long-Term Memory:** Permanent storage, further categorized into:
>         -   *Declarative Memory:* Explicit memory for facts and events (semantic and episodic).
>         -   *Non-Declarative Memory:* Implicit memory for skills, habits, and conditioning (procedural).
> -   **Language:** The cognitive processes involved in the comprehension, production, and acquisition of language. This includes phonology, morphology, syntax, semantics, and pragmatics.
> -   **Problem Solving:** The mental processes involved in discovering, analyzing, and solving problems. This often involves strategies like heuristics, algorithms, and insight.
> -   **Decision Making:** The cognitive process of choosing a course of action from various alternatives. This area explores biases, rationality, and the impact of emotion.
> -   **Reasoning:** The process of drawing conclusions from premises, including deductive reasoning (general to specific) and inductive reasoning (specific to general).
> 
> ----
> 
> ##### Research Methods
> 
> Cognitive psychologists employ diverse methodologies to study the mind:
> 
> -   **Experimental Studies:** Controlled laboratory experiments manipulating independent variables to observe their effect on dependent variables (e.g., reaction time, accuracy).
> -   **Neuroimaging Techniques:**
>     -   **fMRI (functional Magnetic Resonance Imaging):** Measures changes in blood flow to identify active brain regions during cognitive tasks.
>     -   **EEG (Electroencephalography):** Records electrical activity in the brain, useful for measuring the timing of cognitive processes.
>     -   **PET (Positron Emission Tomography):** Uses radioactive tracers to observe metabolic processes in the brain.
> -   **Computational Modeling:** Developing computer programs that simulate cognitive processes to test theoretical predictions.
> -   **Case Studies:** In-depth investigations of individuals with specific cognitive deficits (e.g., due to brain injury) to understand normal cognitive function.
> -   **Response Time and Accuracy Measures:** Quantifying how quickly and accurately individuals perform tasks provides insights into the efficiency and nature of cognitive processes.
> 
> ----
> 
> ##### Applications of Cognitive Psychology
> 
> The principles and findings of cognitive psychology have broad practical applications:
> 
> -   **Education:** Informing teaching methods, curriculum design, and learning strategies (e.g., spaced repetition, active recall).
> -   **Clinical Psychology:** Cognitive Behavioral Therapy (CBT) is a prominent therapeutic approach based on cognitive principles, focusing on changing maladaptive thought patterns.
> -   **Human-Computer Interaction (HCI):** Designing user-friendly interfaces and systems by understanding how people process information and interact with technology.
> -   **Forensic Psychology:** Improving eyewitness testimony accuracy, understanding memory distortions, and evaluating decision-making in legal contexts.
> -   **Artificial Intelligence (AI):** Informing the development of AI systems capable of learning, problem-solving, and natural language processing.
> -   **Marketing and Advertising:** Understanding how consumers perceive information, make decisions, and remember brands.
> > 

>[! ] ### Historical Context and Theoretical Approaches
> 
> ### The Cognitive Revolution
> 
> Prior to the 1950s, behaviorism dominated psychology, focusing only on observable behaviors. However, its inability to explain complex human behaviors like language acquisition led to the "Cognitive Revolution." Key figures like George A. Miller (memory limits), Ulric Neisser (coining "cognitive psychology"), and Noam Chomsky (critique of Skinner's verbal behavior) were instrumental.
> 
> ### Information Processing Model
> 
> A foundational metaphor, comparing the mind to a computer. It suggests that information flows through a series of stages: input, processing, storage, and output. This model emphasizes sequential processing and discrete stages.
> 
> ### Computational Models
> 
> These models seek to explain cognitive processes by specifying the algorithms and representations used by the mind. They often involve creating computer simulations to test hypotheses about mental operations.
> 
> ### Connectionism and Neural Networks
> 
> An alternative approach that views cognition as emerging from the interconnected activity of many simple processing units (neurons). It emphasizes parallel processing and learning through the strengthening or weakening of connections, mirroring neural processes in the brain.

> [!how-to-use] ## Conclusion
>
> Cognitive psychology stands as a cornerstone of modern psychological science, offering profound insights into the intricate workings of the human mind. By investigating processes from perception to problem-solving, it not only enhances our fundamental understanding of ourselves but also provides practical tools to improve learning, mental health, and technological interaction. Its interdisciplinary nature continues to foster collaborations with neuroscience, computer science, and linguistics, promising further advancements in uncovering the mysteries of cognition.

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

> [!definition]
> - **Key-Term**:[[Cognitive Psychology1]]
> - [**Definition**:]



> [!connections-and-links]
> - [[atomic-notes_moc]]: This is a link to the *Main Hub* for all **Atomic Notes**, from there you will find sections of each of the various *Subjects* I have been **working on**.
