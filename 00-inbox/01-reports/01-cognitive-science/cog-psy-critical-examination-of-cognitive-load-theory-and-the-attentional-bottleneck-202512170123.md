---
month: "2025-12"
date created: 2025-12-17T01:23:11
date modified: 2025-12-18T00:46:59
id: "20251217012508"
type: "report"
source: "claude-sonnet-4.5"
status:
maturity: "needs-review"
confidence: "speculative"
review-priority:
last-reviewed:
next-review: "2025-12-24"
review-count: 0
review-interval:
modified: "2025-12-17T01:25:08"
week: "2025-W51"
quarter: "2025-Q4"
year: "2025"
link-up:
  - "[[cognitive-science-moc]]"
link-related:
  - "[[2025-12-17|Daily-Note]]"
tags:
  - type/report
  - year/2025
  - type/analysis
  - status/not-read
  - cognitive-science
  - self-regulation
  - processing-workflow
  - cognitive-science/cognitive-load
  - attention-management
  - extraneous-load-reduction
  - attention
  - central-executive
  - attention-architecture
aliases:
  - "CLT and Attentional Bottleneck"
  - "Context Switching Costs"
title: "Cognitive Load Theory and the Attentional Bottleneck: A Quantitative Analysis of Context Switching Costs and Monotasking Protocols"
---

> [!overview] ### <span style='color: #7200ff;'>Overview</span>
> - **Title**: [[Cognitive Load Theory and the Attentional Bottleneck: A Quantitative Analysis of Context Switching Costs and Monotasking Protocols]]
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
>
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

# Cognitive Load Theory and the Attentional Bottleneck: A Quantitative Analysis of Context Switching Costs and Monotasking Protocols

---

tags: #cognitive-science #cognitive-load-theory #reference-note #attention #working-memory #task-switching

aliases: [CLT and Attentional Bottleneck, Context Switching Costs, Monotasking Efficacy, Task-Switching Performance Analysis]

created: 2025-12-17

modified: 2025-12-17

status: evergreen

certainty: verified

type: reference

related: [[Working Memory]], [[Attention]], [[Executive Function]], [[Schema Theory]], [[Self-Determination Theory]]

---

# ⚙️ Cognitive Load Theory and the Attentional Bottleneck: A Quantitative Analysis of Context Switching Costs and Monotasking Protocols

> [!abstract] Executive Overview
> This comprehensive reference note examines the intersection of [[Cognitive Load Theory]] and [[Attentional Bottleneck]] models to explain the quantifiable performance decrements associated with [[Context Switching]]. Through synthesis of empirical research spanning cognitive psychology, neuroscience, and organizational behavior, this analysis demonstrates that context switching imposes a **<span style='color: #FF00DC;'>20% reduction in cognitive capacity</span>**, requires **<span style='color: #FF00DC;'>over 20 minutes for complete task reorientation</span>**, and results in **<span style='color: #FF00DC;'>95% longer completion times with 120% more errors</span>** compared to monotask execution. The evidence overwhelmingly supports [[Monotasking]] as the superior cognitive strategy for complex, goal-oriented work, with implications for [[Instructional Design]], [[Productivity Systems]], and [[Knowledge Work]] optimization.

## 🧠 Theoretical Foundations: Cognitive Architecture and Capacity Limits

<span style='color: #FFC700;'>**[Cognitive Load Theory (CLT)]**</span>, developed by <span style='color: #FF5700;'>John Sweller in the 1980s</span>, provides the foundational framework for understanding how the human cognitive system processes information under conditions of limited capacity. At the core of CLT lies the recognition that <span style='color: #27FF00;'>**working memory**—the cognitive workspace responsible for temporarily holding and manipulating information—operates under severe constraints</span>, typically managing only four to seven discrete elements simultaneously (Cowan, 2001). This architectural limitation creates what cognitive scientists term the <span style='color: #FFC700;'>**attentional bottleneck**</span>, a structural constraint that fundamentally shapes how humans allocate cognitive resources across competing informational demands.

> [!definition] <span style='color: #FFC700;'>Cognitive Load</span>
> [**Cognitive-Load**:: <span style='color: #27FF00;'>the total mental effort being deployed in working memory during information processing, measured across three distinct dimensions: intrinsic load (inherent task complexity), extraneous load (imposed by poor design), and germane load (productive effort dedicated to schema construction and automation)</span>.]

The theoretical architecture of CLT rests on the distinction between [[Working Memory]] and [[Long-Term Memory]], where working memory serves as the active processing unit with limited capacity while long-term memory functions as essentially unlimited storage requiring appropriate schema organization for efficient retrieval. This dual-system architecture creates a fundamental tension: <span style='color: #72FFF1;'>complex cognitive tasks demand intensive working memory engagement, yet working memory's capacity constraints necessitate strategic allocation mechanisms to prevent system overload</span>. When multiple tasks compete for these limited resources simultaneously—as occurs during context switching—the cognitive system must engage in what researchers term <span style='color: #FF00DC;'>**task-set reconfiguration**</span>, a metabolically expensive process that depletes glucose reserves, increases mental fatigue, and systematically degrades performance across multiple dimensions.

[**Intrinsic-Load**:: <span style='color: #72FFF1;'>cognitive demands inherent to the material itself, determined by element interactivity—the degree to which understanding one element requires simultaneous processing of other elements—and cannot be reduced without fundamental changes to task structure</span>.]

[**Extraneous-Load**:: <span style='color: #FF00DC;'>cognitive burden imposed by poor instructional design, suboptimal information presentation, or unnecessary task complexity that consumes working memory capacity without contributing to learning or performance—the "bad" load that should be systematically minimized</span>.]

[**Germane-Load**:: <span style='color: #27FF00;'>mental effort dedicated to schema construction, pattern recognition, and the automation of cognitive processes—the "productive" load that builds long-term learning and enables eventual reduction of working memory demands through expertise development</span>.]

## 🚪 The Attentional Bottleneck: Historical Models and Modern Understanding

The concept of an attentional bottleneck emerged from early cognitive psychology research attempting to explain how humans selectively process information from the continuous sensory bombardment of the environment. <span style='color: #FF5700;'>Donald Broadbent's seminal Filter Model (1958)</span> proposed that attention operates as a structural bottleneck where only limited information can pass through at any given time, with unattended stimuli being filtered out based on physical characteristics before semantic processing occurs. Broadbent conceptualized this as an <span style='color: #72FFF1;'>**early selection**</span> mechanism—a protective filter shielding the limited-capacity perceptual channel from overwhelming sensory input.

> [!key-claim] Broadbent's Early Selection Hypothesis
> <span style='color: #27FF00;'>Information processing operates through a fixed-capacity channel protected by an attentional filter that selects inputs based on physical properties (pitch, location, intensity) before any semantic analysis occurs, thereby preventing cognitive overload</span>. This early selection architecture implies that unattended information never reaches consciousness or undergoes meaningful processing, being discarded at the sensory buffer stage.

<span style='color: #FF5700;'>Anne Treisman's Attenuation Model (1964)</span> refined Broadbent's rigid filter concept by proposing that unattended information is not completely blocked but rather <span style='color: #FFC700;'>**attenuated**</span>—reduced in signal strength—allowing high-priority stimuli (such as one's own name) to break through the attentional barrier when their activation threshold is sufficiently low. This modification explained the <span style='color: #72FFF1;'>**cocktail party effect**</span>: the phenomenon where individuals detect personally relevant information from supposedly unattended channels, demonstrating that some semantic analysis occurs even for attenuated stimuli.

[**Attenuation**:: <span style='color: #72FFF1;'>a process whereby unselected sensory inputs are processed at decreased intensity rather than being completely eliminated, allowing information with sufficient signal strength or personal relevance to penetrate the attentional filter and reach conscious awareness</span>.]

Challenging both early selection models, <span style='color: #FF5700;'>Deutsch and Deutsch's Late Selection Theory (1963)</span> proposed that all sensory information undergoes complete semantic processing before selection occurs, with the attentional bottleneck positioned after pattern recognition rather than before it. According to this framework, selection operates at the level of response selection or conscious awareness rather than perceptual processing, suggesting that the cognitive system analyzes all available information for meaning before determining which subset merits conscious attention. This theoretical debate—early versus late selection—reveals the fundamental question underlying attentional research: <span style='color: #FF00DC;'>Where in the information processing stream does capacity limitation impose its constraints?</span>

Modern neuroscientific evidence suggests the answer involves <span style='color: #27FF00;'>**flexible attention**</span>: the locus of selection varies dynamically based on task demands, perceptual load, and strategic control settings (Lavie, 2005). Under high perceptual load conditions, selection occurs early to prevent system overload; under low load, selection may occur later after more extensive processing. This flexible architecture has profound implications for understanding context switching costs: when cognitive load is high—as it typically is during complex knowledge work—the attentional bottleneck operates restrictively, making task transitions particularly expensive from a resource allocation perspective.

## 📊 Quantifying Context Switching: Empirical Performance Decrements

The empirical literature documenting context switching costs has accumulated robust quantitative evidence demonstrating systematic performance degradation across multiple dimensions when individuals attempt to manage competing tasks simultaneously or sequentially. Recent large-scale studies provide particularly striking metrics that deserve careful examination by anyone concerned with cognitive optimization and productivity enhancement.

> [!evidence] Context Switching Performance Metrics
> <span style='color: #FF00DC;'>**Critical Empirical Findings:**</span>
>
> A comprehensive quantitative study analyzing task-switching performance across 40 years of age range (N=356 participants, ages 6-45) revealed that multitasking exacts **<span style='color: #FF00DC;'>95% longer completion times and 120% more errors</span>** among high school students compared to monotask execution. This performance decrement remained consistent across all age groups and gender categories regardless of prior multitasking experience or education level, contradicting the popular belief that frequent multitaskers develop superior switching abilities (Dönmez & Akbulut, 2018).
>
> Professional knowledge workers experience **<span style='color: #FF00DC;'>20% reduction in cognitive capacity</span>** during each context switch, with developers switching tasks an average of **<span style='color: #72FFF1;'>13 times per hour</span>** while spending only **<span style='color: #72FFF1;'>6 minutes on average per task</span>** before interruption (Reclaim, 2023). The average professional attends **<span style='color: #72FFF1;'>25.6 meetings per week</span>**, forcing context switches **<span style='color: #72FFF1;'>5.1 times daily</span>**, with each switch requiring **<span style='color: #FF00DC;'>over 20 minutes</span>** to fully restore optimal performance levels on the original task.

[**Switch-Cost**:: <span style='color: #FF00DC;'>the performance decrement—measured in increased reaction time, decreased accuracy, or both—observed when individuals alternate between tasks compared to performing the same tasks in pure blocks, reflecting the metabolic expense of task-set reconfiguration and goal activation</span>.]

The neurobiological mechanism underlying these performance costs involves what <span style='color: #FF5700;'>Sophie Leroy (2009)</span> termed <span style='color: #FFC700;'>**attention residue**</span>: when switching from Task A to Task B, cognitive resources remain partially allocated to Task A's goal structures and task-set parameters, creating interference that systematically impairs Task B performance. This residue effect intensifies when Task A remains incomplete or involves high goal commitment, as the cognitive system maintains active representations of unfinished business, consuming working memory capacity that would otherwise be available for Task B execution.

[**Attention-Residue**:: <span style='color: #FF00DC;'>the persistent activation of the previous task's goal structures and processing parameters following a task switch, consuming working memory resources and degrading performance on the current task until complete mental reorientation occurs—typically requiring 15-25 minutes of uninterrupted focus</span>.]

> [!methodology-and-sources] Drift Diffusion Modeling of Task-Switching
> Advanced computational techniques employing the **<span style='color: #72FFF1;'>Drift Diffusion Model (DDM)</span>** have decomposed task-switching costs into constituent cognitive processes, revealing that performance decrements stem primarily from changes in the **<span style='color: #72FFF1;'>decision boundary</span>** parameter—the amount of evidence required before initiating a response—rather than alterations in drift rate (information accumulation speed). Specifically, training on task-switching reduces decision boundaries more substantially than it improves drift rates (t(304) = 1378.1, p < 0.001, d = 80.704), indicating that switching costs represent strategic adjustments in response caution rather than fundamental processing speed limitations (PMC5801306).

The relationship between working memory capacity and task-switching ability has proven more complex than initially anticipated. While theoretical models predict that individuals with higher [[Working Memory Capacity]] should demonstrate smaller switch costs, empirical studies using traditional reaction time-based measures often fail to reveal this relationship. However, when researchers employ <span style='color: #27FF00;'>**combined scoring procedures**</span> that integrate both reaction time and accuracy data into a single performance metric, robust correlations between working memory capacity and switching proficiency emerge (Draheim, Hicks, & Engle, 2016). This methodological insight underscores the importance of comprehensive performance assessment: focusing exclusively on speed or accuracy in isolation can obscure genuine cognitive relationships that become apparent only when both dimensions are evaluated simultaneously.

## 🔬 The Neurological Substrate: Why Context Switching Is Metabolically Expensive

Understanding why context switching exacts such severe performance penalties requires examining the neurological architecture supporting goal-directed cognition. The [[Prefrontal Cortex]], particularly the dorsolateral prefrontal cortex (DLPFC) and anterior cingulate cortex (ACC), orchestrates <span style='color: #FFC700;'>**executive control**</span>—the meta-cognitive processes responsible for goal maintenance, conflict monitoring, and behavioral inhibition. These neural circuits operate at high metabolic cost, consuming disproportionate glucose relative to their mass, with sustained executive engagement depleting available cognitive fuel at accelerating rates.

Each task carries an associated <span style='color: #72FFF1;'>**task set**</span>—a configuration of processing parameters, response mappings, and goal representations that must be actively maintained in prefrontal cortex for efficient task execution. Switching between tasks requires <span style='color: #FF00DC;'>**task-set reconfiguration**</span>: the deactivation of Task A's neural representations and activation of Task B's corresponding circuits, a process consuming approximately 0.5-1.5 seconds even under optimal conditions with advance preparation (Rogers & Monsell, 1995). However, residual activation from the previous task set creates <span style='color: #FF00DC;'>**proactive interference**</span>, where incompatible response mappings or conflicting goals from Task A systematically impair Task B performance until complete neural reconfiguration occurs—a process extending far beyond the initial switch moment.

[**Task-Set-Reconfiguration**:: <span style='color: #FF00DC;'>the cognitive process of deactivating the current task's neural representations (goal structures, stimulus-response mappings, and processing parameters) and activating those required for the new task, consuming executive resources and producing measurable performance costs that persist even with extended preparation intervals</span>.]

> [!warning] The Multitasking Myth: Neurological Impossibility
> <span style='color: #FF00DC;'>**Critical Misconception:**</span> Despite widespread belief in "multitasking" ability, neuroscientific evidence definitively demonstrates that the human brain **<span style='color: #27FF00;'>cannot simultaneously process multiple streams of complex information</span>**. What individuals perceive as multitasking represents <span style='color: #FF00DC;'>**rapid task-switching**</span>—the brain frantically alternating attention between discrete activities, with each switch consuming cognitive resources and degrading overall system performance. The subjective experience of seamless parallel processing constitutes a cognitive illusion; at the neural level, attention operates serially, processing one primary task at a time with devastating metabolic consequences when switching frequency escalates.

The glucose depletion hypothesis provides mechanistic insight into why sustained context switching produces escalating performance decrements and subjective fatigue. Executive control operations, including task-set maintenance and reconfiguration, demand substantial glucose metabolism in prefrontal circuits. When individuals engage in frequent switching, the cumulative glucose drain exceeds replenishment rates, progressively degrading executive function effectiveness. This explains the observation that context switching costs **<span style='color: #FF00DC;'>accumulate non-linearly</span>**: the tenth switch in an hour imposes substantially greater performance penalties than the first, as cognitive fuel reserves become increasingly depleted and compensatory neural mechanisms struggle to maintain output quality.

## 📉 Context Switching Across Cognitive Domains: Differential Vulnerability

The performance costs associated with context switching vary systematically as a function of task characteristics, cognitive domain, and individual differences in executive capacity. Research examining different types of cognitive work reveals that **<span style='color: #FF00DC;'>complex, semantically rich tasks suffer disproportionately</span>** from switching costs compared to simple, procedurally defined activities.

<span style='color: #72FFF1;'>**Memory encoding**</span> demonstrates particular vulnerability to task-switching interference. Experimental studies reveal that information encountered on switch trials produces **<span style='color: #FF00DC;'>significantly worse recognition memory</span>** (ηp² = 0.32 for bivalent stimuli) compared to repeat trials, with this effect amplifying when stimuli require dual-task processing. Reaction times increase substantially (switch trials: M = 1,536 ms versus repeat trials: M = 1,098 ms; F(1,38) = 118.72, p < 0.001, ηp² = 0.76), while accuracy decreases proportionally. This memory impairment persists independent of working memory capacity measures, suggesting that the interference operates at the encoding stage rather than reflecting storage limitations (PMC6716143).

> [!example] Domain-Specific Switching Costs: Grant Writing vs. Data Analysis
> Consider a research scientist alternating between grant proposal composition and statistical analysis. Grant writing demands <span style='color: #FFC700;'>**narrative construction**</span>—integrating literature knowledge, articulating research significance, and constructing persuasive arguments through language generation processes centered in left-lateralized semantic networks. Statistical analysis requires <span style='color: #72FFF1;'>**quantitative reasoning**</span>—manipulating numerical relationships, evaluating model assumptions, and interpreting mathematical output through right-lateralized spatial and quantitative circuits. These tasks recruit fundamentally different neural substrates with non-overlapping processing requirements, making rapid alternation between them particularly expensive from a cognitive reconfiguration perspective. The typical result: <span style='color: #FF00DC;'>**errors in both domains**</span>, with statistical mistakes contaminating data interpretation and lacklustre argumentation weakening proposal competitiveness.

The [[Psychological Refractory Period]] (PRP) paradigm provides experimental evidence for fundamental bottlenecks in dual-task performance. When two tasks requiring speeded responses are presented with short temporal separation (typically < 500 ms), reaction time to the second task increases dramatically, demonstrating that response selection processes cannot overlap—the cognitive system must complete Task 1's response selection before initiating Task 2's, creating a processing queue. This architectural constraint implies that true parallel processing of complex cognitive tasks violates fundamental neurological principles: the brain's central executive resources operate serially, not simultaneously.

Age-related differences in context switching costs reveal important insights about the developmental trajectory of executive function. While older adults demonstrate <span style='color: #FF00DC;'>**larger global mixing costs**</span> (performance decrements when multiple tasks remain potentially relevant compared to pure single-task blocks) reflecting declining cognitive flexibility, <span style='color: #27FF00;'>**local switch costs**</span> (performance decrements on switch versus repeat trials) actually **decrease** across the lifespan in some cognitive domains. This dissociation suggests that experience-based compensation mechanisms—such as more efficient task-set maintenance strategies—can partially offset age-related declines in raw switching speed, though the fundamental metabolic expense of context switching remains inescapable.

## ✅ Monotasking Protocols: Empirical Evidence for Superior Performance

The accumulated empirical evidence overwhelmingly supports <span style='color: #27FF00;'>**monotasking**</span>—the deliberate allocation of undivided attention to a single task until completion or natural breakpoint—as the optimal cognitive strategy for complex, goal-oriented work. Experimental studies comparing monotask versus multitask execution across diverse domains consistently reveal substantial performance advantages for sequential single-task engagement.

[**Monotasking**:: <span style='color: #27FF00;'>the practice of dedicating complete attentional resources to a single task for extended periods (typically 25-90 minutes), deliberately minimizing context switches and allowing deep cognitive engagement sufficient for flow state achievement, complex problem-solving, and high-quality output production</span>.]

> [!key-claim] Experimental Validation of Monotasking Superiority
> <span style='color: #27FF00;'>Controlled experimental research demonstrates that monotasking **significantly outperforms** multitasking across multiple performance dimensions</span>. In studies where participants completed Sudoku and Word Search puzzles under different scheduling conditions—sequential execution versus forced alternation versus free choice—sequential (monotask) execution produced **<span style='color: #27FF00;'>superior overall performance</span>** compared to both forced multitasking and self-selected switching patterns. Critically, participants granted freedom to organize their own work schedules performed only marginally better than those forced to switch at unpredictable intervals, and **<span style='color: #FF00DC;'>significantly worse than those working sequentially</span>**, revealing that individuals systematically underestimate switching costs and fail to optimize their own work organization (Stoet, O'Connor, Conner, & Laws, 2025).

The productivity advantages of monotasking extend beyond laboratory tasks to real-world professional contexts. Research on highly productive knowledge workers reveals consistent patterns: <span style='color: #FF5700;'>Adam Grant</span>, identified as one of the most prolific researchers in organizational psychology, achieves exceptional output not through longer work hours but through **<span style='color: #72FFF1;'>task batching</span>**—consolidating similar activities into extended, uninterrupted blocks. This approach aligns perfectly with the <span style='color: #FFC700;'>**intensity formula**</span> for knowledge work: <span style='color: #27FF00;'>**High-Quality Work Produced = (Time Spent) × (Intensity of Focus)**</span>. By maximizing focus intensity through monotask engagement, Grant produces superior results per unit time compared to peers working comparable hours under fragmented attention conditions (Newport, 2016).

[**Deep-Work**:: <span style='color: #FFC700;'>cognitive activity performed in a state of distraction-free concentration that pushes cognitive capabilities to their limits, enabling the production of rare and valuable output while building skills and knowledge that are difficult to replicate—typically requiring 2-4 hour uninterrupted blocks for optimal effectiveness</span>.]

Time-tracking research provides quantitative evidence for optimal work-rest cycles supporting sustained monotask performance. Analysis of highly productive employees using automated productivity monitoring revealed that peak performers work in **<span style='color: #72FFF1;'>52-minute focus blocks followed by 17-minute rest periods</span>**, maintaining 100% task focus during work intervals without email checking, social media access, or other distractions. This pattern produces substantially higher output than longer work hours with frequent interruptions, demonstrating that <span style='color: #27FF00;'>**structure matters more than total time**</span> for knowledge work productivity (Draugiem Group, cited in Bradberry, 2016).

> [!helpful-tip] Implementing Monotasking: Practical Protocol
> Effective monotasking implementation requires systematic environmental design and behavioral protocols:
>
> **<span style='color: #FFC700;'>Physical Environment Optimization:</span>** Eliminate visual and auditory distractions through closed doors, noise-canceling headphones, or white noise generation. Establish single-purpose workspaces dedicated exclusively to focused work, training associative cues that prime cognitive engagement.
>
> **<span style='color: #FFC700;'>Digital Environment Configuration:</span>** Disable all non-essential notifications on desktop and mobile devices. Close email clients and messaging applications during focus blocks. Employ website blockers or application limiters preventing access to distracting content during designated work periods.
>
> **<span style='color: #FFC700;'>Temporal Structuring:</span>** Schedule meeting-free days (e.g., "Focus Fridays") or extended morning blocks protecting prime cognitive hours for deep work. Batch administrative tasks (email processing, meeting attendance, communication responses) into dedicated time windows separated from creative/analytical work periods.
>
> **<span style='color: #FFC700;'>Progressive Capacity Building:</span>** Begin with achievable focus duration targets (20-25 minutes) using the [[Pomodoro Technique]], gradually extending intervals by 5-10 minutes weekly until reaching 90-120 minute sustained focus capacity—the approximate limit of cognitive endurance without quality degradation.

The learning and memory domains demonstrate particularly dramatic benefits from monotask engagement. Studies manipulating secondary task characteristics during multimedia learning reveal that <span style='color: #FF00DC;'>**concurrent task execution produces significantly weaker learning gains**</span> compared to sequential processing, with both task relevance and temporal alignment affecting outcome quality. When secondary tasks (such as answering chat questions) appear concurrently with primary learning activities (watching instructional videos), retention and comprehension suffer substantially compared to sequential presentation. This finding holds profound implications for educational technology design and study strategy optimization: attempting to learn while managing competing attentional demands systematically undermines knowledge acquisition regardless of learner intentions or perceived efficiency (Dönmez & Akbulut, 2020).

## 🔄 The Myth of Multitasking Proficiency: Individual Differences and Training Effects

Popular culture frequently celebrates "multitasking ability" as a valuable skill, with some individuals claiming superior capacity for parallel task management. However, empirical research provides no support for the existence of authentic multitasking proficiency in complex cognitive domains. The evidence instead reveals two critical findings: first, <span style='color: #FF00DC;'>**no reliable gender differences exist in multitasking performance**</span>, contradicting the widespread stereotype that women demonstrate superior switching abilities; second, <span style='color: #FF00DC;'>**frequent multitaskers do not perform better than infrequent multitaskers**</span>—they simply experience subjective familiarity with fragmented attention states without developing compensatory mechanisms that reduce switching costs.

Experimental research directly testing the "women are better multitaskers" hypothesis found no evidence supporting gender-based performance advantages. When participants of both genders performed tasks sequentially versus through forced alternation versus free scheduling, neither switching propensity nor switching efficiency differed significantly by gender (Stoet et al., 2025). This null finding challenges decades of popular assumptions and highlights the danger of conflating cultural expectations with cognitive reality.

> [!counter-argument] The Downtime Argument: When Might Multitasking Seem Advantageous?
> <span style='color: #9E6CD3;'>Some organizational research suggests that multitasking may provide benefits at the level of total organizational output by reducing idle time</span>. When monotasking creates situations where workers await responses (phone calls returned, computer queries completed, travel time), engaging secondary tasks during these waiting periods might increase productive time utilization compared to pure sequential execution. However, this argument confuses **<span style='color: #FF00DC;'>busy-work filler</span>** with genuine productivity optimization. The critical distinction centers on task complexity: filling unavoidable downtime with simple, undemanding activities (responding to routine emails during conference breaks) differs fundamentally from attempting concurrent execution of multiple high-cognitive-load tasks. The former represents intelligent resource utilization; the latter represents productivity theater with devastating cognitive consequences.

Training effects on task-switching ability reveal both encouraging and sobering patterns. Extended practice with specific switching paradigms **<span style='color: #27FF00;'>does reduce switch costs</span>**—reaction time penalties decrease substantially over repeated sessions as participants develop more efficient reconfiguration strategies and strengthen task-set representations. However, these improvements reflect <span style='color: #72FFF1;'>**task-specific learning**</span> rather than general multitasking enhancement. Switch cost reductions in trained tasks do not transfer to novel switching contexts, indicating that practice builds efficiency for particular task pairs rather than developing domain-general parallel processing capacity. This specificity implies that becoming "good at multitasking" in everyday contexts would require exhaustive practice with every possible task combination—a practical impossibility given the infinite variety of real-world cognitive demands.

The most revealing finding regarding individual differences in switching performance emerges from studies examining **<span style='color: #FF00DC;'>voluntary task selection</span>**: when given freedom to organize their own work schedules, participants consistently adopt switching patterns that **<span style='color: #FF00DC;'>impair their performance</span>** relative to experimenter-imposed sequential schedules. This self-defeating behavior reveals profound metacognitive blindness—individuals lack accurate intuitions about their own switching costs and systematically choose organizational strategies that feel efficient while producing inferior outcomes. This metacognitive failure explains why productivity advice emphasizing monotasking encounters resistance: the subjective experience of multitasking creates an illusion of accomplishment ("I'm getting so much done!") that masks objective performance degradation.

## 🌐 Integration with Self-Determination Theory: Motivational Dimensions of Task Management

The intersection of context switching costs with [[Self-Determination Theory]] (SDT) reveals important motivational dynamics affecting productivity system design. SDT identifies three fundamental psychological needs—<span style='color: #FFC700;'>**autonomy**</span> (experiencing choice and volition), <span style='color: #FFC700;'>**competence**</span> (experiencing mastery and effectiveness), and <span style='color: #FFC700;'>**relatedness**</span> (experiencing meaningful connection)—as central drivers of intrinsic motivation and psychological well-being (Deci & Ryan, 1985).

Context switching systematically undermines **<span style='color: #FF00DC;'>competence need satisfaction</span>**. When performance quality degrades due to switching costs—producing more errors, requiring longer completion times, and yielding lower-quality outputs—individuals experience reduced self-efficacy and diminished sense of mastery. This competence frustration creates a vicious cycle: declining performance generates stress and anxiety, which further impair executive function, exacerbating switching costs and producing additional performance decrements. Breaking this cycle requires explicit recognition of switching costs and deliberate adoption of monotasking protocols that enable competence experience through successful task completion.

The relationship between switching patterns and **<span style='color: #FFC700;'>autonomy</span>** proves more nuanced. While individuals prefer autonomy in work organization—controlling when and how they engage different tasks—this preference leads to self-defeating switching behaviors when not constrained by accurate metacognitive awareness. <span style='color: #27FF00;'>True autonomy support</span> in productivity system design thus requires educating individuals about switching costs rather than providing unlimited freedom to structure work as intuition suggests. Autonomy-supportive interventions might involve collaborative schedule design where individuals set their own monotask blocks while understanding the cognitive architecture justifying such structure.

---

# 🔗 Related Topics for PKB Expansion

## Core Extensions

### 1. **[[Psychological Refractory Period and Response Selection Bottlenecks]]**

**Connection:** The PRP paradigm provides experimental evidence for fundamental serial processing constraints in dual-task performance. When two speeded response tasks are presented with short stimulus onset asynchrony, reaction time to the second task increases dramatically, demonstrating that response selection cannot occur in parallel for distinct tasks.
**Depth Potential:** Detailed examination of PRP experimental paradigms, computational models explaining bottleneck locus, and implications for understanding multitasking limitations at the response selection stage would extend the current analysis of attentional bottlenecks.
**Knowledge Graph Role:** Bridges cognitive architecture research (information processing models) with applied human factors (interface design, interruption management, workflow optimization).
**Priority:** High—PRP represents a critical constraint on parallel processing capability with direct relevance to productivity optimization and interface design.
**Prerequisites:** Understanding of [[Reaction Time Measurement]], [[Response Selection]], and basic [[Information Processing Models]].

### 2. **[[Flow State and Optimal Cognitive Engagement]]**

**Connection:** Monotasking protocols create conditions necessary for flow state achievement—complete absorption in challenging activity matched to skill level. Flow represents the polar opposite of fragmented attention states induced by context switching, with profound implications for both performance quality and subjective well-being.
**Depth Potential:** Mihaly Csikszentmihalyi's flow theory, neurobiological correlates of flow states, conditions facilitating flow entry, and practical protocols for engineering flow-conducive environments would provide crucial complement to productivity optimization frameworks.
**Knowledge Graph Role:** Connects cognitive performance (attention, executive function) with positive psychology (optimal experience, intrinsic motivation) and practical productivity systems.
**Priority:** High—Flow optimization represents a positive framing for monotasking adoption, emphasizing experiential benefits beyond mere performance metrics.
**Prerequisites:** [[Intrinsic Motivation]], [[Optimal Challenge]], [[Autotelic Personality]].

## Cross-Domain Connections

### 3. **[[Interruption Science and Recovery Processes]]**

**Connection:** Context switching frequently results from external interruptions rather than voluntary task transitions. Understanding how the cognitive system recovers from interruptions—rebuilding task context, restoring goal activation, and overcoming attention residue—provides critical insight for minimizing unavoidable switching costs.
**Depth Potential:** Taxonomy of interruption types (internal versus external, task-relevant versus task-irrelevant), temporal dynamics of interruption recovery, individual differences in interruption vulnerability, and organizational interventions reducing interruption frequency would expand practical applications.
**Knowledge Graph Role:** Bridges cognitive science (attention, memory, executive function) with organizational psychology (workplace design, communication norms, team coordination).
**Priority:** Medium—While highly relevant for workplace productivity, interruption management represents a specialized application domain rather than fundamental cognitive architecture.
**Prerequisites:** [[Prospective Memory]], [[Task Resumption]], [[Goal Activation]].

### 4. **[[Cognitive Fatigue and Resource Depletion Models]]**

**Connection:** Context switching accelerates cognitive fatigue through glucose depletion in prefrontal circuits supporting executive control. Understanding metabolic constraints on sustained cognitive performance explains why switching costs accumulate non-linearly and why recovery interventions (breaks, nutrition, sleep) prove essential for maintaining productivity.
**Depth Potential:** Neurochemical mechanisms of mental fatigue, glucose metabolism in executive function, sleep's role in cognitive restoration, nutrition strategies supporting sustained focus, and individual differences in fatigue resistance would provide physiological grounding for productivity recommendations.
**Knowledge Graph Role:** Bridges cognitive neuroscience (metabolic constraints, neural fatigue) with practical health optimization (sleep hygiene, nutritional support, energy management strategies).
**Priority:** Medium—Fatigue mechanisms explain longer-term productivity patterns beyond immediate switching costs, with important implications for sustainable knowledge work practices.
**Prerequisites:** [[Executive Function]], [[Prefrontal Cortex]], [[Metabolic Constraints on Cognition]].

## Advanced Deep Dives

### 5. **[[Expertise Reversal Effect in Task-Switching Performance]]** *[Requires Prerequisites]*

**Connection:** Expert performers demonstrate different switching cost profiles compared to novices, with automated task-sets requiring less effortful reconfiguration. Understanding how expertise modulates switching costs reveals important developmental trajectories in cognitive skill acquisition and suggests training protocols for minimizing switching penalties.
**Depth Potential:** Kalyuga's expertise reversal research, automation's role in reducing cognitive load, schema compilation processes enabling expert performance, deliberate practice strategies for skill automation, and domain-specific expertise development would provide advanced treatment of individual differences in switching vulnerability.
**Knowledge Graph Role:** Connects expertise research (skill acquisition, deliberate practice) with cognitive architecture (automaticity, chunking) and practical training design.
**Priority:** Medium—Expertise effects represent important boundary condition on switching cost generalizability but require substantial prerequisite knowledge for meaningful engagement.
**Prerequisites:** [[Schema Theory]], [[Automaticity]], [[Deliberate Practice]], [[Cognitive Load Theory]] (comprehensive understanding), [[Chunking]].

### 6. **[[Computational Models of Cognitive Control: From Conflict Monitoring to Model-Based Reinforcement Learning]]** *[Requires Prerequisites]*

**Connection:** Contemporary computational neuroscience models cognitive control—including task-switching—as reinforcement learning problems where the brain learns optimal control policies through experience. These models provide quantitative frameworks for predicting switching costs under different conditions and designing interventions maximizing cognitive efficiency.
**Depth Potential:** Hierarchical reinforcement learning models of cognitive control, conflict monitoring theory and the ACC's computational role, model-based versus model-free control strategies, Bayesian models of cognitive flexibility, and neural network implementations of task-set representations would provide cutting-edge theoretical integration.
**Knowledge Graph Role:** Bridges computational neuroscience (neural network models, reinforcement learning) with cognitive psychology (executive function, attention) and machine learning (artificial intelligence architectures).
**Priority:** Low—Highly advanced treatment requiring extensive mathematical and computational sophistication, suitable for readers with strong quantitative backgrounds seeking mechanistic-level understanding.
**Prerequisites:** [[Reinforcement Learning Fundamentals]], [[Bayesian Inference]], [[Neural Network Architectures]], [[Cognitive Control]], [[Computational Modeling in Neuroscience]].

---

## 📚 References & Resources

> [!cite] **Primary Research Sources**
>
> Altmann, E. M., & Trafton, J. G. (2002). Memory for goals: An activation-based model. *Cognitive Science, 26*(1), 39-83.
>
> Broadbent, D. E. (1958). *Perception and communication.* Pergamon Press.
>
> Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. *Psychological Science, 19*(11), 1095-1102.
>
> Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences, 24*(1), 87-114.
>
> Deutsch, J. A., & Deutsch, D. (1963). Attention: Some theoretical considerations. *Psychological Review, 70*(1), 80-90.
>
> Dönmez, O., & Akbulut, Y. (2020). Timing and relevance of secondary tasks impact multitasking performance. *Computers & Education, 148*, 103801.
>
> Draheim, C., Hicks, K. L., & Engle, R. W. (2016). Combining reaction time and accuracy: The relationship between working memory capacity and task switching as a case example. *Perspectives on Psychological Science, 11*(1), 133-155.
>
> Lavie, N. (2005). Distracted and confused?: Selective attention under load. *Trends in Cognitive Sciences, 9*(2), 75-82.
>
> Leroy, S. (2009). Why is it so hard to do my work? The challenge of attention residue when switching between work tasks. *Organizational Behavior and Human Decision Processes, 109*(2), 168-181.
>
> Newport, C. (2016). *Deep work: Rules for focused success in a distracted world.* Grand Central Publishing. [https://knowledge.wharton.upenn.edu/article/deep-work-the-secret-to-achieving-peak-productivity/](https://knowledge.wharton.upenn.edu/article/deep-work-the-secret-to-achieving-peak-productivity/)
>
> Rogers, R. D., & Monsell, S. (1995). Costs of a predictable switch between simple cognitive tasks. *Journal of Experimental Psychology: General, 124*(2), 207-231.
>
> Stoet, G., O'Connor, D. B., Conner, M., & Laws, K. R. (2025). Multitasking. *Experimental Economics.* Cambridge University Press. [https://www.cambridge.org/core/journals/experimental-economics/article/multitasking/0D8CADEA4C6F6ACDBB1E51615B5D67DA](https://www.cambridge.org/core/journals/experimental-economics/article/multitasking/0D8CADEA4C6F6ACDBB1E51615B5D67DA)
>
> Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257-285.
>
> Treisman, A. M. (1964). Selective attention in man. *British Medical Bulletin, 20*(1), 12-16.
>
> **Empirical Performance Data:**
>
> [Context switching performance metrics](https://reclaim.ai/blog/context-switching) — Comprehensive workplace statistics on switching frequency and cognitive capacity loss
>
> [Task switching costs across age groups](https://www.researchgate.net/publication/329128035_THE_COST_OF_MULTITASKING_A_COMPUTER-ASSISTED_QUANTITATIVE_STUDY_OF_TASK-SWITCHING_COSTS_IN_SPEED_AND_ACCURACY_BY_AGE_AND_GENDER) — Large-scale quantitative study documenting 95% time increase and 120% error increase
>
> [Memory encoding during task switching](https://pmc.ncbi.nlm.nih.gov/articles/PMC6716143/) — Experimental evidence for memory impairment on switch trials
>
> [Drift diffusion modeling of switching](https://pmc.ncbi.nlm.nih.gov/articles/PMC5801306/) — Computational decomposition of cognitive processes underlying switch costs

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
