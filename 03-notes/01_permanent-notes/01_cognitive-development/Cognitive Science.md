---
aliases:
  - Cognitive Science
  - cognitive science
  - Cognition Research
  - Mind Studies
tags:
  - type/permanent
  - year/2025
  - status/seedling
  - cognitive-science
  - cognitive-psychology
  - processing-workflow
  - cognitive-science/metacognition
  - learning-processes
  - information-processing-theory
  - working-memory
  - reasoning
  - cognitive-modeling
  - permanent-note
  - permanent-note/project-pur3v4d3r
  - permanent-note/pkb
  - prompt-engineering
source: ""
id: 20251110-162852
created: 2025-12-13T06:18:58
modified: 2025-12-13T06:18:58
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
  - "[[Chain-of-Thought]]"
  - "[[Generative Ai]]"
  - "[[Large Language Models]]"
  - "[[Cognitive Load Management]]"
  - "[[Critical Thinking]]"
  - "[[Dichotomy Of Control]]"
  - "[[Educational Psychology]]"
  - "[[Locus Of Control]]"
  - "[[Metacognition]]"
  - "[[Self-Behavioral Management]]"
  - "[[Self-Regulated Learning]]"
  - "[[Self-Determination Theory]]"
  - "[[Self-Regulation Theory]]"
title: cognitive science
summary: Cognitive science is an interdisciplinary field dedicated to the scientific study of the mind and its processes, integrating insights from various academic disciplines. It explores the nature of thought, perception, memory, language, and intelligence across humans, animals, and machines.
status: active


review-last-reviewed: null
review-next-review: 2025-12-17
review-count: 0
review-interval: 3

review-priority: medium
---

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Cognitive Science]]
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
> [**Cognitive Science**:: Cognitive Science is the interdisciplinary scientific study of the mind and its processes. It investigates the nature of intelligence, focusing on how information is processed, understood, and used by the brain. Combining insights from various fields, it seeks to understand perception, thinking, memory, language, learning, and other mental faculties.]
> 
> ##### [✅`= dateformat(this.file.ctime, "MMMM dd, yyyy")` - Initial Creation]

> [! ] # Outline
> - ## Introduction to Cognitive Science
>     - Interdisciplinary Nature
>     - Core Questions and Goals
> - **Foundational Disciplines**
>     - **Psychology**
>         - Cognitive Psychology
>         - Developmental Psychology
>     - **Neuroscience**
>         - Cognitive Neuroscience
>         - Computational Neuroscience
>     - **Computer Science**
>         - Artificial Intelligence (AI)
>         - Computational Modeling
>         - Robotics
>     - **Linguistics**
>         - Psycholinguistics
>         - Computational Linguistics
>     - **Philosophy**
>         - Philosophy of Mind
>         - Epistemology
>     - **Anthropology**
>         - Cognitive Anthropology
> - **Key Concepts and Theories**
>     - **Representation**
>         - Mental Representations
>         - Symbolic vs. Connectionist Approaches
>     - **Computation**
>         - Information Processing Theory
>         - Algorithms and Processes
>     - **Modularity of Mind**
>     - **Embodied Cognition**
>     - **Situated Cognition**
>     - **Distributed Cognition**
>     - **Cognitive Architectures**
> - **Major Areas of Study**
>     - **Perception**
>         - Visual Perception
>         - Auditory Perception
>         - Multimodal Perception
>     - **Attention**
>         - Selective Attention
>         - Divided Attention
>     - **Memory**
>         - Working Memory
>         - Long-Term Memory (Episodic, Semantic, Procedural)
>     - **Language**
>         - Language Acquisition
>         - Language Production and Comprehension
>         - Semantics and Syntax
>     - **Reasoning and Problem Solving**
>         - Deductive and Inductive Reasoning
>         - Heuristics and Biases
>     - **Decision Making**
>         - Rational Choice Theory
>         - Behavioral Economics
>     - **Learning**
>         - Classical and Operant Conditioning
>         - Skill Acquisition
>     - **Consciousness**
>         - Theories of Consciousness
>         - Neural Correlates of Consciousness
> - **Research Methodologies**
>     - **Behavioral Experiments**
>         - Reaction Time
>         - Accuracy
>         - Eye-tracking
>     - **Neuroimaging Techniques**
>         - fMRI (functional Magnetic Resonance Imaging)
>         - EEG (Electroencephalography)
>         - MEG (Magnetoencephalography)
>         - PET (Positron Emission Tomography)
>     - **Computational Modeling**
>         - Neural Networks
>         - Bayesian Models
>     - **Lesion Studies** (Neuropsychology)
>     - **Developmental Studies**
> - **Applications of Cognitive Science**
>     - Artificial Intelligence (AI) and Machine Learning
>     - Human-Computer Interaction (HCI)
>     - Education and Learning Technologies
>     - Clinical Psychology and Psychiatry
>     - Ergonomics and Human Factors Engineering
>     - Robotics
> - **Challenges and Future Directions**
>     - Integrating different levels of analysis
>     - Understanding complex cognitive phenomena (e.g., creativity, wisdom)
>     - The role of emotion in cognition
>     - Ethical implications of AI and neuroscience
>     - Developing unified theories of cognition

----

> [!key-changes] ## Core Disciplines
> 
> Cognitive science is inherently interdisciplinary, drawing upon and integrating methodologies and theories from several key fields:
> 
> *   **Psychology (Cognitive Psychology)**: Studies mental processes such as attention, memory, perception, language, problem-solving, and thinking.
> *   **Neuroscience (Cognitive Neuroscience)**: Investigates the neural bases of mental processes, often using brain imaging techniques and studying brain injuries.
> *   **Artificial Intelligence (AI)**: Develops computational models of cognitive processes and intelligent agents, often testing theories of cognition.
> *   **Linguistics**: Explores the structure, acquisition, and use of language, including its relation to thought.
> *   **Philosophy of Mind**: Examines fundamental questions about the nature of mind, consciousness, free will, and knowledge.
> *   **Anthropology**: Contributes insights into how cultural and social contexts influence cognitive processes.
> ----
> 
> ## Methodologies
> 
> Cognitive scientists employ a diverse set of research methods:
> 
> *   **Experimental Psychology**: Controlled experiments to test hypotheses about cognitive processes, often measuring reaction times, accuracy, and subjective reports.
> *   **Neuroimaging**: Techniques like fMRI (functional Magnetic Resonance Imaging), EEG (Electroencephalography), and MEG (Magnetoencephalography) to observe brain activity during cognitive tasks.
> *   **Computational Modeling**: Creating computer simulations to mimic and test theories of cognitive processes.
> *   **Linguistic Analysis**: Studying language structures, patterns of language use, and developmental aspects of language acquisition.
> *   **Philosophical Argumentation**: Conceptual analysis and logical reasoning to address foundational questions about the mind.
> *   **Neuropsychology**: Studying individuals with brain damage to understand the functional specialization of brain regions.

>[! ]  ## Key Areas of Study
> 
> Cognitive science explores a wide range of mental phenomena:
> 
> *   **Perception**: How sensory information from the world is interpreted and transformed into meaningful experiences (e.g., vision, audition, touch).
> *   **Attention**: The mechanisms by which the mind selects and focuses on certain stimuli while ignoring others.
> *   **Memory**: The processes involved in encoding, storing, and retrieving information (e.g., working memory, long-term memory, episodic, semantic).
> *   **Language**: How humans acquire, produce, and comprehend language, including its underlying cognitive and neural mechanisms.
> *   **Reasoning and Problem-Solving**: The cognitive processes involved in drawing inferences, making logical deductions, and finding solutions to complex tasks.
> *   **Decision-Making**: How individuals choose among various options, often under conditions of uncertainty.
> *   **Learning**: The mechanisms by which knowledge and skills are acquired and modified over time.
> *   **Consciousness**: Though highly complex and debated, some areas of cognitive science explore the neural correlates and computational aspects of conscious experience.
> >[! ] ## Applications and Impact
> >
> > Insights from cognitive science have significant practical applications across various domains:
> > 
> > *   **Artificial Intelligence**: Informing the design of intelligent systems, machine learning algorithms, and natural language processing.
> > *   **Education**: Developing more effective teaching methods, learning strategies, and educational technologies.
> > *   **Human-Computer Interaction (HCI)**: Designing user-friendly interfaces and systems that align with human cognitive capabilities and limitations.
> > *   **Clinical Psychology and Psychiatry**: Understanding the cognitive deficits associated with mental disorders and developing targeted interventions.
> > *   **Neurorehabilitation**: Designing therapies for individuals with cognitive impairments due to brain injury or disease.
> > *   **Marketing and Economics**: Understanding consumer behavior and decision-making processes.

> [!abstract] ## Conclusion
> 
> Cognitive science stands as a vibrant and evolving field that continues to deepen our understanding of the human mind. By integrating diverse perspectives and methodologies, it strives to unravel the complexities of intelligence and consciousness, offering profound insights into what it means to think, perceive, and learn. Its continued advancement promises to reshape our understanding of ourselves and our technologies.

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
> - **Key-Term**:[[Cognitive Science1]]
> - [**Definition**:The field of science concerned with cognition; includes parts of cognitive psychology and linguistics and computer science and cognitive neuroscience and philosophy of mind.]



> [!connections-and-links]
> - [[atomic-notes_moc]]: This is a link to the *Main Hub* for all **Atomic Notes**, from there you will find sections of each of the various *Subjects* I have been **working on**.
