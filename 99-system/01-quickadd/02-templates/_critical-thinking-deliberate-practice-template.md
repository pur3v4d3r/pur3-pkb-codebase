<%*
// ═══════════════════════════════════════════════════════════════════════════
// CRITICAL THINKING DELIBERATE PRACTICE TEMPLATE — TEMPLATER SETUP BLOCK
// ───────────────────────────────────────────────────────────────────────────
// This block runs ONCE at template instantiation. It prompts the user for
// session parameters, configures the YAML frontmatter, and renames the file.
// The triangulation principle is honored throughout: multiple frameworks are
// available for sequential or comparative application within a single session.
// ═══════════════════════════════════════════════════════════════════════════

// ─── Session Identification ────────────────────────────────────────────────
const sessionTitle = await tp.system.prompt(
  "What are you analyzing? (concise title — argument, claim, decision, text, belief)"
);

// ─── Practice Mode Selection ───────────────────────────────────────────────
const sessionType = await tp.system.suggester(
  [
    "🎯 Argument Analysis (external argument/text)",
    "🪞 Belief Examination (your own held position)",
    "⚖️  Decision Reasoning (pending choice)",
    "📄 Text Critique (article, essay, paper)",
    "🔄 Self-Reflection on Recent Thinking",
    "🏋️  Position Stress-Test (your strong view)",
    "🌐 Multi-Perspective Inquiry (contested issue)",
    "🧪 Hypothesis Evaluation"
  ],
  [
    "argument-analysis",
    "belief-examination",
    "decision-reasoning",
    "text-critique",
    "self-reflection",
    "position-stress-test",
    "multi-perspective-inquiry",
    "hypothesis-evaluation"
  ]
);

// ─── Primary Framework Selection ───────────────────────────────────────────
const primaryFramework = await tp.system.suggester(
  [
    "🏛️  Paul-Elder (Full 3-Layer Analysis)",
    "⚡ FRISCO (Ennis Quick Pass)",
    "🏗️  Toulmin Argument Mapping",
    "❓ Browne-Keeley 10-Question Sweep",
    "📐 SEE-I Concept Elaboration",
    "🔺 Multi-Framework Triangulation"
  ],
  [
    "paul-elder",
    "frisco",
    "toulmin",
    "browne-keeley",
    "see-i",
    "multi-framework"
  ]
);

// ─── Difficulty Calibration ────────────────────────────────────────────────
const difficulty = await tp.system.suggester(
  [
    "1 — Familiar & Comfortable (warm-up)",
    "2 — Some Discomfort (light stretch)",
    "3 — Moderately Challenging (productive struggle)",
    "4 — Significantly Challenging (edge of competence)",
    "5 — Genuinely Difficult (uncertain you can resolve)"
  ],
  ["1", "2", "3", "4", "5"]
);

// ─── Stakes Calibration ────────────────────────────────────────────────────
const stakes = await tp.system.suggester(
  [
    "🟢 Low — Practice only, no real-world consequences",
    "🟡 Medium — Decision-informing, modest consequences",
    "🟠 High — Significant real-world impact",
    "🔴 Critical — Life-direction-shaping"
  ],
  ["low", "medium", "high", "critical"]
);

// ─── Domain Context ────────────────────────────────────────────────────────
const domain = await tp.system.suggester(
  [
    "Philosophy / Ethics",
    "Science / Empirical",
    "Politics / Policy",
    "Personal / Psychological",
    "Professional / Career",
    "Epistemology / Knowledge",
    "Aesthetic / Interpretive",
    "Mathematical / Logical",
    "Mixed / Multi-Domain"
  ],
  [
    "philosophy",
    "science",
    "politics",
    "personal",
    "professional",
    "epistemology",
    "aesthetic",
    "mathematical",
    "mixed"
  ]
);

// ─── Target Intellectual Trait (Development Focus) ─────────────────────────
const targetTrait = await tp.system.suggester(
  [
    "Intellectual Humility",
    "Intellectual Courage",
    "Intellectual Empathy",
    "Intellectual Autonomy",
    "Intellectual Integrity",
    "Intellectual Perseverance",
    "Confidence in Reason",
    "(None — General Practice)"
  ],
  [
    "humility",
    "courage",
    "empathy",
    "autonomy",
    "integrity",
    "perseverance",
    "confidence-in-reason",
    "general"
  ]
);

// ─── File Renaming ─────────────────────────────────────────────────────────
const dateStr = tp.date.now("YYYY-MM-DD");
const safeTitle = sessionTitle
  .replace(/[^a-zA-Z0-9 -]/g, "")
  .replace(/\s+/g, "-")
  .toLowerCase()
  .substring(0, 60);
await tp.file.rename(`ct-${dateStr}-${safeTitle}`);

// ─── Computed Review Date (7 days out for spaced review) ───────────────────
const reviewDate = tp.date.now("YYYY-MM-DD", 7);
-%>
---
title: "<% sessionTitle %>"
aliases:
  - "CT Practice — <% sessionTitle %>"
session-type: <% sessionType %>
primary-framework: <% primaryFramework %>
difficulty: <% difficulty %>
stakes: <% stakes %>
domain: <% domain %>
target-trait: <% targetTrait %>
date-practiced: <% tp.date.now("YYYY-MM-DD") %>
time-started: <% tp.date.now("HH:mm") %>
time-completed: ""
duration-minutes: 0
review-due: <% reviewDate %>
review-count: 0
status: in-progress
confidence: developing
type: deliberate-practice-session
practice-cycle: cognitive-self-development
cssclasses:
  - wide-page
tags:
  - critical-thinking-practice
  - deliberate-practice
  - <% primaryFramework %>
  - <% sessionType %>
  - metacognition
  - cognitive-self-development
  - difficulty-<% difficulty %>
  - stakes-<% stakes %>
  - domain-<% domain %>
related-frameworks:
  - "[[paul-elder-framework-reference]]"
  - "[[critical-thinking-frameworks-master-reference]]"
overall-score: 0
elements-score: 0
standards-score: 0
traits-score: 0
integration-score: 0
---

# 🧠 Critical Thinking Practice Session

> [!abstract] Session Identity
> **Subject:** <% sessionTitle %>
> **Mode:** `<% sessionType %>` | **Primary Framework:** `<% primaryFramework %>`
> **Difficulty:** `<% difficulty %>/5` | **Stakes:** `<% stakes %>` | **Domain:** `<% domain %>`
> **Trait Focus:** `<% targetTrait %>`
> **Started:** <% tp.date.now("YYYY-MM-DD HH:mm") %>

[session-id:: ct-<% tp.date.now("YYYYMMDD-HHmm") %>]
[practice-mode:: <% sessionType %>]
[primary-framework:: <% primaryFramework %>]
[difficulty-level:: <% difficulty %>]
[stakes-level:: <% stakes %>]
[target-trait:: <% targetTrait %>]
[review-due:: <% reviewDate %>]

> [!key-claim] Triangulation Principle (from Master Reference)
> No single framework captures critical thinking exhaustively. Each illuminates aspects others obscure. This session is structured around your chosen **primary framework**, with **triangulation passes** through complementary frameworks to expose blind spots the primary cannot detect.

---

## 📑 Table of Contents

1. [[#🎯 Subject Under Analysis]]
2. [[#🪞 Pre-Analysis Priming Diagnostic]]
3. [[#🏛️ Paul-Elder Three-Layer Analysis]]
4. [[#📊 Standards-Elements Matrix Diagnosis]]
5. [[#🏗️ Toulmin Argument Architecture]]
6. [[#📐 SEE-I Elaboration of Key Concepts]]
7. [[#⚡ FRISCO Rapid Audit (Ennis)]]
8. [[#❓ Browne-Keeley Ten-Question Sweep]]
9. [[#🕳️ The Assumption Excavation]]
10. [[#🔄 Perspective Rotation Protocol]]
11. [[#🚨 Fallacy Scan by Element]]
12. [[#🧭 Metacognitive Reflection]]
13. [[#📊 Self-Assessment Rubrics]]
14. [[#🌟 Intellectual Traits Self-Inventory]]
15. [[#🎯 Development Targets & Action Items]]
16. [[#🔁 Revised Position Synthesis]]
17. [[#📈 Cross-Session Dataview Tracking]]

---

# 🎯 Subject Under Analysis

> [!example] Capture the Object of Thought
> Before analyzing reasoning, the reasoning itself must be made explicit. Write out the argument, claim, decision, text, or belief **in its strongest, most complete form** — as if presenting it to a hostile but fair critic. Vague subjects produce vague analysis.

### The Argument / Claim / Position

> [Paste or summarize the full argument here. If analyzing your own position, write it as if presenting it to someone who must understand it without prior context. If analyzing external text, quote and cite. Aim for completeness: the more thoroughly the subject is stated, the more precisely it can be examined.]

### Source & Context

[source:: ]
[author:: ]
[publication-venue:: ]
[date-encountered:: <% tp.date.now("YYYY-MM-DD") %>]

**Context that frames this argument:**
> [What surrounding circumstances, debates, or motivations shape how this argument should be interpreted? Whose interests does the argument serve? In what intellectual tradition does it sit?]

### Why This Subject Was Selected

> [What drew your attention to this? Is it a position you hold strongly? One you find suspicious? One that touches a personal interest? Naming the selection motive is the first metacognitive move — it reveals what *your* perspective is bringing to the encounter.]

[selection-motive:: ]

---

# 🪞 Pre-Analysis Priming Diagnostic

> [!warning] Honesty Required Here
> The point of this section is to surface, **before formal analysis begins**, what your starting position is. This protects against the post-hoc rationalization trap where formal analysis merely justifies a conclusion already reached emotionally. Be uncomfortable here.

### Initial Intuition Capture

> [!definition] Pre-Analysis Position
> **Your gut response to the subject — before any systematic analysis:**

- **Initial verdict:** [Agree / Disagree / Uncertain / Confused]
- **Confidence in initial verdict (1–10):** 
- **Emotional charge (1–10):** _How emotionally invested am I in a particular outcome?_
- **Single-sentence summary of my reaction:**

[initial-verdict:: ]
[initial-confidence:: ]
[emotional-charge:: ]

### Bias Acknowledgment Checklist

> [!example] What Predispositions Am I Bringing?
> Before analyzing, name what might be tilting the scales. Naming a bias does not neutralize it, but unnamed bias operates invisibly.

- [ ] **Confirmation bias check:** Am I likely to search for evidence supporting my initial verdict?
- [ ] **In-group bias check:** Does my social/professional/ideological identity tilt me toward a side?
- [ ] **Sunk-cost check:** Have I publicly committed to a position I'd lose face by abandoning?
- [ ] **Motivated reasoning check:** Would a particular conclusion be *convenient* for me?
- [ ] **Authority bias check:** Am I deferring to (or rebelling against) a particular authority?
- [ ] **Recency bias check:** Has something I read recently disproportionately shaped my view?
- [ ] **Affect heuristic check:** Am I confusing "this feels true" with "this is true"?

**Most active bias in this session:** 
[active-bias:: ]

### Dual-Process Engagement Declaration

> [!key-claim] System 2 Required Here
> Per [[Dual Process Theory]], System 1 (fast, automatic, heuristic) has already given its verdict above. The work of this session is **deliberate System 2 engagement** — slow, effortful, algorithmic reasoning that may override the System 1 verdict. The discomfort of System 2 is the signature of doing it correctly.

**Declaration:** I am committing the next __ minutes to deliberate slow thinking on this subject, suspending my initial verdict for the duration of analysis.

[system-2-time-budget-min:: ]

---

# 🏛️ Paul-Elder Three-Layer Analysis

> [!abstract] Layer Architecture
> The Paul-Elder framework operates on three interlocking layers: **Elements** (what is happening in thinking), **Standards** (how well it is happening), and **Traits** (who the thinker is becoming). This section walks the eight Elements; the next section cross-applies the nine Standards via the diagnostic matrix.

---

## Element 1 — Purpose

[element:: Purpose] [element-number:: 1]

> [!definition] Element Lens — Purpose
> The goal or objective driving this reasoning. Unclear purposes generate confused reasoning. Conflicting purposes produce contradictory conclusions.

### Diagnostic Questions

- **What is the explicit purpose of this reasoning?** 
- **What might be the *real* purpose, distinct from the stated one?** 
- **Are there multiple purposes pulling in different directions?** 
- **Is this purpose ethically justifiable?** 

### My Analysis

> [Write your analysis here. Don't just answer the questions — diagnose what the *quality* of the purpose is, where it's vague, where it's hidden, where it shifts.]

### Pathology Scan

- [ ] Purpose is *vague* — reasoning lacks direction
- [ ] Purpose is *hidden* — motive not openly stated
- [ ] Purpose is *shifting* — changes mid-argument
- [ ] Purpose is *unrealistic* — built toward incoherent goal
- [ ] Purpose is *unexamined* — accepted from culture/habit/authority

### Standards Applied to This Element

| Standard | Score (1–4) | Notes |
|---|---|---|
| Clarity | | Is the purpose clearly stated? |
| Significance | | Is this purpose worth pursuing? |
| Fairness | | Is the purpose pursued with intellectual integrity? |

[purpose-score:: ]

---

## Element 2 — Question at Issue

[element:: Question-at-Issue] [element-number:: 2]

> [!definition] Element Lens — Question
> The question, problem, or issue the reasoning attempts to address. Poorly formulated questions misdirect reasoning. The *type* of question determines which reasoning standards apply.

### Diagnostic Questions

- **What is the precise question being addressed?** 
- **What type of question is this?** *(Factual / Conceptual / Evaluative / Policy)*
- **Is this the right question, or does the real issue lie elsewhere?** 
- **Is this one question or several conflated?** 
- **What assumptions are embedded in the question's framing?** 

### My Analysis

> [Write here.]

### Pathology Scan

- [ ] Question is *ambiguous* — multiple interpretations conflated
- [ ] Question is *complex* — sub-questions tangled together
- [ ] Question is *wrong* — real issue elsewhere
- [ ] Question is *loaded* — presupposes a conclusion
- [ ] Question is *unanswerable as stated*

### Standards Applied

| Standard | Score (1–4) | Notes |
|---|---|---|
| Clarity | | |
| Precision | | |
| Significance | | |

[question-score:: ]

---

## Element 3 — Information

[element:: Information] [element-number:: 3]

> [!definition] Element Lens — Information
> The data, facts, observations, and evidence used. Conclusions are only as reliable as the information underlying them.

### Diagnostic Questions

- **What information is being used?** 
- **Is the information accurate and verifiable?** 
- **Is the information sufficient?** What's missing?
- **Have I sought disconfirming evidence?** 
- **What is the source — and how reliable is it?** 
- **Are facts being distinguished from interpretations?** 

### My Analysis

> [Write here.]

### Pathology Scan

- [ ] **Cherry-picking** — only confirming evidence selected
- [ ] **Outdated information** — stale data applied to current question
- [ ] **Conflating facts with interpretations**
- [ ] **Insufficient evidence** — strong conclusion from weak data
- [ ] **Biased sources** — partisan treated as neutral
- [ ] **Ignored disconfirming evidence** — motivated reasoning
- [ ] **Anecdotal evidence** treated as systematic data

### Standards Applied

| Standard | Score (1–4) | Notes |
|---|---|---|
| Accuracy | | |
| Relevance | | |
| Depth | | |
| Breadth | | |
| Fairness | | |

[information-score:: ]

---

## Element 4 — Interpretation & Inference

[element:: Interpretation-and-Inference] [element-number:: 4]

> [!definition] Element Lens — Inference
> The conclusions and interpretations drawn from information. The move from data to conclusion is where most reasoning errors occur.

### Diagnostic Questions

- **What conclusions are being drawn?** 
- **How does the reasoning move from information to conclusion?** 
- **Is the inference justified by the data, or does it go beyond?** 
- **Are there other reasonable inferences from the same data?** 
- **Have I over-generalized or under-generalized?** 
- **What would invalidate this inference?** 

### My Analysis

> [Write here.]

### Pathology Scan

- [ ] **Over-inference** — stronger conclusion than data supports
- [ ] **Under-inference** — failing to draw warranted conclusions
- [ ] **False dichotomy** — only two possibilities when more exist
- [ ] **Hasty generalization** — universal pattern from limited cases
- [ ] **Non-sequitur** — conclusion doesn't follow
- [ ] **Confirmation bias** in inference selection
- [ ] **Post hoc ergo propter hoc** — correlation treated as causation

### Standards Applied

| Standard | Score (1–4) | Notes |
|---|---|---|
| Logic | | |
| Accuracy | | |
| Depth | | |
| Significance | | |

[inference-score:: ]

---

## Element 5 — Concepts

[element:: Concepts] [element-number:: 5]

> [!definition] Element Lens — Concepts
> The ideas, theories, definitions, and models organizing the thinking. Concepts are rarely neutral; they embed assumptions and presuppose frameworks.

### Diagnostic Questions

- **What key concepts are being used?** 
- **Have they been defined clearly and precisely?** 
- **Are these the *right* concepts for this question?** 
- **What assumptions are embedded in these concepts?** 
- **Are concepts being used consistently throughout?** 

### My Analysis

> [Write here.]

### Pathology Scan

- [ ] **Vague concepts** — undefined terms shifting meaning
- [ ] **Equivocation** — same term, different meanings
- [ ] **Inappropriate concepts** — used outside valid range
- [ ] **Reification** — abstraction treated as concrete
- [ ] **Inherited concepts unexamined** — accepted without scrutiny
- [ ] **Conceptual disagreement disguised as factual**

### Standards Applied

| Standard | Score (1–4) | Notes |
|---|---|---|
| Clarity | | |
| Precision | | |
| Logic | | |

[concepts-score:: ]

---

## Element 6 — Assumptions

[element:: Assumptions] [element-number:: 6]

> [!warning] Highest-Leverage Element
> Assumptions are the *most dangerous* element because they operate invisibly. Per the master reference: "Surfacing and examining assumptions is one of the highest-leverage critical thinking moves." Spend extra time here.

### Diagnostic Questions

- **What is being taken for granted?** 
- **What must be true for this reasoning to hold?** 
- **Are these assumptions justified?** 
- **What would happen if a key assumption were false?** 
- **What are the assumptions of those who disagree?** 
- **Are my assumptions consistent with each other?** 

### My Analysis (Including Bedrock Excavation)

> **First-order assumptions (stated or near-surface):**
> 
> **Second-order assumptions (what must be true for first-order to hold):**
> 
> **Bedrock assumptions (foundational beliefs not further justifiable):**

### Pathology Scan

- [ ] **Hidden assumptions** — driving conclusions invisibly
- [ ] **Unjustified assumptions** — premises without grounds
- [ ] **Inconsistent assumptions** — contradictions within argument
- [ ] **Culturally inherited assumptions** — absorbed without examination
- [ ] **Assumption-as-conclusion** — circular reasoning
- [ ] **Naturalistic fallacy** — is/ought confusion

### Standards Applied

| Standard | Score (1–4) | Notes |
|---|---|---|
| Clarity | | |
| Logic | | |
| Fairness | | |
| Breadth | | |

[assumptions-score:: ]

---

## Element 7 — Implications & Consequences

[element:: Implications-and-Consequences] [element-number:: 7]

> [!definition] Element Lens — Implications
> What is *entailed* by the reasoning (logical implications) and what *results* from it in the world (practical consequences). Responsible reasoning follows logic wherever it leads.

### Diagnostic Questions

- **If I accept this, what else must I accept?** 
- **What are the practical consequences of acting on this?** 
- **Are there negative implications being ignored?** 
- **What would happen if everyone reasoned this way?** 
- **Am I willing to accept these consequences?** 
- **Short-term vs. long-term implications?** 

### My Analysis

> [Trace implications to at least 2–3 logical steps out. What does accepting this commit you to that you might not have noticed?]

### Pathology Scan

- [ ] **Implication-blindness** — unaware of position's commitments
- [ ] **Cherry-picked implications** — only favorable ones traced
- [ ] **Short-term bias** — ignoring long-term consequences
- [ ] **Scope insensitivity** — ignoring scale
- [ ] **Sunk-cost fallacy** — past investment driving future decisions
- [ ] **Slippery slope assertion** without justification

### Standards Applied

| Standard | Score (1–4) | Notes |
|---|---|---|
| Logic | | |
| Significance | | |
| Depth | | |
| Breadth | | |

[implications-score:: ]

---

## Element 8 — Point of View

[element:: Point-of-View] [element-number:: 8]

> [!definition] Element Lens — Point of View
> The perspective, frame of reference, or vantage point from which the reasoning is conducted. All thinking happens from somewhere; pretending to view from nowhere is the most common form of perspective-blindness.

### Diagnostic Questions

- **From what perspective is this reasoning conducted?** 
- **What does this perspective enable seeing?** 
- **What does this perspective prevent seeing?** 
- **What other perspectives could be brought to bear?** 
- **Am I confusing my perspective with objective reality?** 
- **What group memberships shape this view?** 

### My Analysis

> **My (or the author's) operative perspective:**
> 
> **What this perspective illuminates:**
> 
> **What this perspective obscures:**
> 
> **Alternative perspectives that should be considered:**

### Pathology Scan

- [ ] **Perspective-blindness** — treating own view as universal
- [ ] **Ethnocentrism** — own cultural frame as default
- [ ] **In-group bias** — favoring perspectives of one's tribe
- [ ] **Genetic fallacy** — dismissing view based on its source
- [ ] **Pseudo-objectivity** — claiming view from nowhere

### Standards Applied

| Standard | Score (1–4) | Notes |
|---|---|---|
| Breadth | | |
| Fairness | | |
| Significance | | |

[pov-score:: ]

---

# 📊 Standards-Elements Matrix Diagnosis

> [!methodology-and-sources] Matrix Application Protocol
> The master reference's central analytical tool: apply any **Standard** (row) to any **Element** (column) to generate a diagnostic question. After scoring elements individually above, this matrix surfaces the **weakest cells** — the specific Standard×Element intersections where reasoning breaks down. Those cells become your development targets.

### Scoring Grid

> Score each cell **1–4** based on how well the element meets that standard in this argument. Empty cells = not yet evaluated. The grid is intentionally daunting — populate the cells most relevant to the weaknesses you're already detecting, then come back to fill remaining cells if time permits.

|  | Purpose | Question | Information | Inference | Concepts | Assumptions | Implications | Point of View |
|---|---|---|---|---|---|---|---|---|
| **Clarity** | | | | | | | | |
| **Accuracy** | | | | | | | | |
| **Precision** | | | | | | | | |
| **Relevance** | | | | | | | | |
| **Depth** | | | | | | | | |
| **Breadth** | | | | | | | | |
| **Logic** | | | | | | | | |
| **Significance** | | | | | | | | |
| **Fairness** | | | | | | | | |

### Weakest Cell Identification

**Lowest-scoring cells (your highest-leverage development targets):**

1. **[Standard] × [Element]:** _Why this cell scored low:_
2. **[Standard] × [Element]:** _Why this cell scored low:_
3. **[Standard] × [Element]:** _Why this cell scored low:_

[weakest-standard:: ]
[weakest-element:: ]

---

# 🏗️ Toulmin Argument Architecture

> [!abstract] Triangulation Pass — Argument Structure
> Where Paul-Elder evaluates reasoning *quality*, [[Toulmin Argument Model|Toulmin]] makes argument *structure* visible. The warrant — the implicit principle linking data to claim — is most often where the real disagreement lies. Surfacing warrants is one of the highest-leverage moves in argument analysis.

### Argument Diagram

```
                              ┌─────────────────┐
                              │   Qualifier:    │
                              │                 │
                              └────────┬────────┘
                                       │
  ┌─────────────────┐                  ▼               ┌─────────────────┐
  │   Data:         │  ─────(so)───────────▶ ────────▶ │   Claim:        │
  │                 │                                  │                 │
  └────────┬────────┘                                  └─────────────────┘
           │                                                    ▲
        (since)                                              (unless)
           │                                                    │
           ▼                                                    │
  ┌─────────────────┐                                  ┌─────────────────┐
  │   Warrant:      │                                  │   Rebuttal:     │
  │                 │                                  │                 │
  └────────┬────────┘                                  └─────────────────┘
           │
       (because)
           │
           ▼
  ┌─────────────────┐
  │   Backing:      │
  │                 │
  └─────────────────┘
```

### Component Articulation

[claim:: ]
**Claim** *(the conclusion being argued for):*
> 

[data:: ]
**Data / Grounds** *(facts/evidence supporting the claim):*
> 

[warrant:: ]
**Warrant** *(the reasoning principle linking data to claim — often implicit):*
> 

[backing:: ]
**Backing** *(the support behind the warrant itself):*
> 

[qualifier:: ]
**Qualifier** *(the degree of certainty — "presumably," "probably," "certainly"):*
> 

[rebuttal:: ]
**Rebuttal** *(conditions under which the claim might not hold):*
> 

### Warrant Diagnosis (The Hidden Key)

> [!key-claim] Where Disagreements Actually Live
> "Most everyday arguments make the claim and provide data explicitly but leave the warrant implicit. The warrant is what *makes the data relevant to the claim* — and it is most often where the disagreement actually lies."

- **Is the warrant stated or implicit?** 
- **Is the warrant defensible if surfaced?** 
- **Would someone reasonable reject this warrant?** 
- **What does the warrant assume about the world?** 

---

# 📐 SEE-I Elaboration of Key Concepts

> [!methodology-and-sources] SEE-I Application
> The Paul-Elder operationalization of the Clarity standard. Pick the **1–3 most contested or important concepts** from the argument and run SEE-I on each. Doing this exposes definitional ambiguity that "clarity" alone cannot.

---

### Concept 1: [Name the concept]

[concept-1:: ]

**S — State it** *(one or two precise sentences):*
> 

**E — Elaborate it** *(three to five sentences expanding in different words, no examples yet):*
> 

**E — Exemplify it** *(a concrete, specific, real example):*
> 

**I — Illustrate it** *(an analogy, metaphor, or diagram from a different angle):*
> 

---

### Concept 2: [Name the concept]

[concept-2:: ]

**S — State it:**
> 

**E — Elaborate it:**
> 

**E — Exemplify it:**
> 

**I — Illustrate it:**
> 

---

### Concept 3: [Name the concept] *(optional)*

[concept-3:: ]

**S — State it:**
> 

**E — Elaborate it:**
> 

**E — Exemplify it:**
> 

**I — Illustrate it:**
> 

---

# ⚡ FRISCO Rapid Audit (Ennis)

> [!abstract] Triangulation Pass — Ennis's Six-Step Heuristic
> The [[Ennis-Streamlined-Conception|FRISCO model]] is deceptively simple. Applied systematically, it covers most of what more elaborate frameworks accomplish. Use it as a checksum: if Paul-Elder analysis missed something here, that's a warning.

| Letter | Step | Diagnostic Result |
|---|---|---|
| **F** | **Focus** — What is the main question, conclusion, or issue? | |
| **R** | **Reasons** — What reasons are offered in support? | |
| **I** | **Inference** — Is the reasoning from reasons to conclusion acceptable? | |
| **S** | **Situation** — What context frames the argument? | |
| **C** | **Clarity** — Are key terms clear? | |
| **O** | **Overview** — Does the reasoning hold up under integrated review? | |

[frisco-verdict:: ]
**FRISCO Verdict:** _One-sentence integrated judgment after running all six steps._

---

# ❓ Browne-Keeley Ten-Question Sweep

> [!abstract] Triangulation Pass — Question-Based Critical Reading
> [[Browne-Keeley-10-Questions|Browne and Keeley]] operationalize critical thinking as the disciplined sequential application of ten questions. Use this as a coverage check — anything the Paul-Elder + Toulmin passes missed should surface here.

| # | Question | Finding |
|---|---|---|
| 1 | What are the issue and conclusion? | |
| 2 | What are the reasons? | |
| 3 | Which words or phrases are ambiguous? | |
| 4 | What are the value conflicts and assumptions? | |
| 5 | What are the descriptive assumptions? | |
| 6 | Are there any fallacies in the reasoning? | |
| 7 | How good is the evidence? | |
| 8 | Are there rival causes? | |
| 9 | Are the statistics deceptive? | |
| 10 | What significant information is omitted? | |
| 11 | What reasonable conclusions are possible? | |

[bk-deceptive-stats:: ]
[bk-omitted-info:: ]
[bk-rival-causes:: ]

---

# 🕳️ The Assumption Excavation

> [!key-claim] Why a Dedicated Section
> Even after Element 6 above, dedicated assumption work pays disproportionate returns. The protocol below digs deeper than the element scan, following premises down to bedrock.

### The Excavation Protocol *(adapted from Paul-Elder Protocol 3)*

**Step 1 — Identify each premise in the argument:**

| # | Premise |
|---|---|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |

**Step 2 — For each premise, ask: "What must be true for me to accept this?"**

| Premise | First-Level Assumption | Second-Level Assumption | Bedrock |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Step 3 — Evaluate bedrock assumptions:**

> Which bedrock assumptions are *defensible*? Which are *cultural inheritance*? Which are *self-serving*? Which would the most charitable opposing thinker contest?

[bedrock-defensible:: ]
[bedrock-contested:: ]

**Step 4 — The Counterfactual Test:**

> Pick the single most important assumption. **If it were false, what would change?** If the answer is "nothing significant," it isn't actually doing work in the argument. If the answer is "the whole conclusion collapses," that assumption is load-bearing and demands extra scrutiny.

[load-bearing-assumption:: ]

---

# 🔄 Perspective Rotation Protocol

> [!warning] Steelman Standard
> Per the master reference Protocol 4: "The opposing argument you write should be compelling enough that someone who didn't know you wrote it would not be able to tell which side you are on." If your "opposing view" reads as a strawman, you have not yet done this exercise.

### The Strongest Opposing View

> [Write a one-page argument for the strongest opposing position to the one being analyzed — without including any counterarguments. Steelman, do not strawman.]

### What the Opposing Perspective Sees That Mine Misses

> 

### What My Perspective Sees That the Opposing Misses

> 

### Synthesis Move

> Is there a position that incorporates the legitimate insights of both? Or is the disagreement fundamentally about which considerations carry more weight? Name the structure of the disagreement explicitly.

[disagreement-structure:: ]

### Intellectual Empathy Check

- [ ] I represented the opposing view in language its proponents would recognize
- [ ] I did not insert subtle pejoratives or framings that betray my bias
- [ ] I identified at least one genuine insight in the opposing view
- [ ] I can name what would make a reasonable person hold that view

---

# 🚨 Fallacy Scan by Element

> [!warning] Common Fallacies Mapped to Elements
> Per the master reference's fallacy mapping: each element has characteristic failure modes. Scan systematically. A fallacy missed here usually corresponds to a Standard×Element cell scored too generously above.

| Element | Fallacy Candidates | Detected? | Evidence |
|---|---|---|---|
| **Purpose** | Hidden agenda, shifting goalposts, motivated reasoning | | |
| **Question** | False dilemma, loaded question, begging the question, wrong question | | |
| **Information** | Cherry-picking, anecdotal evidence, appeal to authority, hearsay | | |
| **Inference** | Hasty generalization, slippery slope, post hoc, non sequitur, false cause | | |
| **Concepts** | Equivocation, vague terms, category errors, reification | | |
| **Assumptions** | Circular reasoning, naturalistic fallacy, appeal to tradition, false premise | | |
| **Implications** | Ignoring consequences, sunk cost, short-termism, scope insensitivity | | |
| **Point of View** | Ad hominem, appeal to authority, genetic fallacy, in-group bias | | |

[fallacies-detected:: ]
[most-damaging-fallacy:: ]

---

# 🧭 Metacognitive Reflection

> [!key-claim] Self-Regulation as Capstone
> Per the [[Delphi-Consensus|Delphi Report]]: self-regulation is positioned as **the most distinctively critical** of the critical thinking skills. Without it, the other skills can be deployed in service of motivated reasoning. This section is where the thinking-about-thinking happens.

### How My Thinking Went

> **Where did my reasoning move quickly without examination?** _(System 1 takeover candidates)_
> 

> **Where did I notice myself wanting a particular conclusion?** _(Motivated reasoning candidates)_
> 

> **What questions did I avoid asking?** _(Self-protective omissions)_
> 

> **Where did I feel the most discomfort during analysis — and why?** _(Likely the highest-value learning sites)_
> 

### What Surprised Me

> **An insight I did not expect when I started:**
> 

> **A weakness in my reasoning I had not previously recognized:**
> 

> **A strength in the opposing view I had not previously credited:**
> 

### How My Verdict Shifted (or Didn't)

- **Initial verdict** *(from Pre-Analysis Priming):* 
- **Post-analysis verdict:** 
- **Confidence shift:** Initial __ → Final __
- **What drove the shift (or its absence)?** 

[verdict-shifted:: ]
[confidence-delta:: ]

### Quality of My Own Thinking This Session

> [!example] Self-Critique
> _What would a Paul-Elder Stage 5 ("Advanced") thinker have done that I did not? What is the next-most-sophisticated move I could have made and skipped?_

[stage-aspiration:: ]

---

# 📊 Self-Assessment Rubrics

> [!methodology-and-sources] Rubric Application
> The four rubrics below come from the Paul-Elder reference. Score each on **1–4**. Use the **lowest-scoring** dimension to identify your highest-priority development target. A score of 3+ across all four represents competent critical thinking at the practicing level.

### Rubric A — Elements of Thought

[elements-score:: ]

| Score | Descriptor | Selected? |
|---|---|---|
| 1 — Beginning | Applies one or two elements incidentally | |
| 2 — Developing | Identifies most elements when prompted; applies inconsistently | |
| 3 — Competent | Applies all eight elements systematically | |
| 4 — Advanced | Applies elements fluidly and simultaneously; generates new questions | |

**Evidence for this score:**

### Rubric B — Intellectual Standards

[standards-score:: ]

| Score | Descriptor | Selected? |
|---|---|---|
| 1 — Beginning | Uses colloquial terms without criteria | |
| 2 — Developing | Applies 2–4 standards; identifies violations without articulating why | |
| 3 — Competent | Applies all nine standards; explains depth vs. breadth | |
| 4 — Advanced | Uses Standards-Elements Matrix; diagnoses root causes | |

**Evidence for this score:**

### Rubric C — Intellectual Traits

[traits-score:: ]

| Score | Descriptor | Selected? |
|---|---|---|
| 1 — Beginning | No trait-oriented development; unreflective | |
| 2 — Developing | Can describe traits; occasional exhibition in comfort | |
| 3 — Competent | Consistently exhibits most traits; identifies own vices | |
| 4 — Advanced | Habitual; ongoing deliberate development | |

**Evidence for this score:**

### Rubric D — Integration

[integration-score:: ]

| Score | Descriptor | Selected? |
|---|---|---|
| 1 — Beginning | Elements/standards/traits treated as separate lists | |
| 2 — Developing | Applies elements and standards together on specific problems | |
| 3 — Competent | Routinely applies Standards × Elements; sees reasoning as unified | |
| 4 — Advanced | Full integration automatic; can teach while deepening | |

**Evidence for this score:**

### Overall Score

[overall-score:: ]

**Composite (average of A–D):** __
**Paul-Elder Developmental Stage estimate:** ([[#The Stages of Critical Thinking Development|reference stages]])

- [ ] Stage 1 — Unreflective Thinker
- [ ] Stage 2 — Challenged Thinker
- [ ] Stage 3 — Beginning Thinker
- [ ] Stage 4 — Practicing Thinker
- [ ] Stage 5 — Advanced Thinker
- [ ] Stage 6 — Master Thinker

[developmental-stage:: ]

---

# 🌟 Intellectual Traits Self-Inventory

> [!definition] Trait-Oriented Reflection
> Skill without disposition is, in Facione's terms, "unrealized critical thinking." Research on the [[CCTDI]] shows disposition predicts skill deployment better than skill predicts disposition use. Score honestly.

| Trait | Demonstrated This Session? (1–4) | Evidence | Vice Detected? |
|---|---|---|---|
| **Intellectual Humility** | | | Arrogance? |
| **Intellectual Courage** | | | Cowardice? |
| **Intellectual Empathy** | | | Narrow-mindedness? |
| **Intellectual Autonomy** | | | Conformity? |
| **Intellectual Integrity** | | | Hypocrisy? |
| **Intellectual Perseverance** | | | Laziness? |
| **Confidence in Reason** | | | Distrust of reason? |

[trait-strongest:: ]
[trait-weakest:: ]
[vice-detected:: ]

### Target Trait Reflection

> Your declared target trait for this session was: **<% targetTrait %>**

- **Did I make progress on this trait?** 
- **What specifically did I do that exhibited (or failed to exhibit) it?** 
- **What is the next deliberate practice for this trait?** 

---

# 🎯 Development Targets & Action Items

> [!key-claim] Deliberate Practice Requires Targeted Work
> "Random exposure to good reasoning does not produce critical thinking skill. Deliberate Practice requires: targeted work on specific weaknesses, immediate feedback, progressive difficulty, and metacognitive reflection on performance." This section converts session insights into next actions.

### Top Three Weaknesses Identified This Session

1. **Weakness:** 
   - **Evidence:** 
   - **Targeted practice:** 

2. **Weakness:** 
   - **Evidence:** 
   - **Targeted practice:** 

3. **Weakness:** 
   - **Evidence:** 
   - **Targeted practice:** 

### Action Items

- [ ] **Re-read** [[paul-elder-framework-reference#Element X]] — focus area 
- [ ] **Apply Protocol** [N] from the master reference to a new subject within 7 days
- [ ] **Specific element to audit daily** for the next week: 
- [ ] **Specific standard to apply** to my next written piece: 
- [ ] **Trait development exercise** to perform this week: 

[next-practice-element:: ]
[next-practice-standard:: ]
[next-practice-trait:: ]

### Spaced Review Hook

> [!example] Return to This Session
> Per [[Spaced Repetition]] principles, review this session on:
> - **+1 day:** Skim insights and verdict
> - **+7 days:** Re-evaluate verdict; have new information changed it?
> - **+30 days:** Audit the action items above — did targeted practice happen?
> - **+90 days:** Full re-read; would current-me reach the same conclusions?

[review-1d:: <% tp.date.now("YYYY-MM-DD", 1) %>]
[review-7d:: <% tp.date.now("YYYY-MM-DD", 7) %>]
[review-30d:: <% tp.date.now("YYYY-MM-DD", 30) %>]
[review-90d:: <% tp.date.now("YYYY-MM-DD", 90) %>]

---

# 🔁 Revised Position Synthesis

> [!summary] The Final Move
> After all the analysis, write the **revised version of the original claim** — incorporating what the questioning revealed. This is the deliverable of deliberate practice: not a debunking, not a reaffirmation, but a more precisely calibrated position.

### Revised Position

> [Write here. Should reflect: refined precision, acknowledged uncertainty, identified assumptions, accounted-for counterarguments, and confidence calibrated to evidence.]

### Confidence Calibration

[final-verdict:: ]
[final-confidence:: ]

| Dimension | Initial | Final | Notes |
|---|---|---|---|
| Verdict | | | |
| Confidence (1–10) | | | |
| Emotional charge (1–10) | | | |

### What Would Change My Mind

> Per the Confidence in Reason trait: name the specific evidence or argument that would shift you further. If no such evidence is conceivable, you may be holding the view non-rationally.

> 

---

<%*
// Update completion timestamp
const completionTime = tp.date.now("HH:mm");
-%>

[time-completed:: ]
[duration-minutes:: ]
[session-complete:: false]

---

# 📈 Cross-Session Dataview Tracking

> [!methodology-and-sources] Live Queries
> The queries below operate across **all your critical thinking practice sessions**. They surface patterns invisible within any single session: which elements you consistently underweight, which standards you fail to apply, which traits are systematically weakest.

### Your Recent Practice Sessions

```dataview
TABLE
  primary-framework AS "Framework",
  difficulty AS "Diff",
  stakes AS "Stakes",
  overall-score AS "Score",
  developmental-stage AS "Stage"
FROM #critical-thinking-practice 
WHERE file.name != this.file.name
SORT date-practiced DESC
LIMIT 10
```

### Sessions Due for Review

```dataview
TABLE
  primary-framework AS "Framework",
  review-due AS "Due",
  date-practiced AS "Practiced"
FROM #critical-thinking-practice 
WHERE review-due <= date(today) AND status != "archived"
SORT review-due ASC
```

### Your Weakest Elements (Across All Sessions)

```dataview
TABLE WITHOUT ID
  "Purpose" AS "Element",
  round(average(purpose-score), 2) AS "Avg Score"
FROM #critical-thinking-practice 
WHERE purpose-score
FLATTEN purpose-score AS scores

UNION

TABLE WITHOUT ID  
  "Question" AS "Element",
  round(average(question-score), 2) AS "Avg Score"
FROM #critical-thinking-practice
WHERE question-score
```

*Note: If the above doesn't render, use the simpler version below — average inline fields require manual querying patterns in some Dataview versions.*

### Element Score Distribution (Manual Query)

```dataview
TABLE
  purpose-score AS "P",
  question-score AS "Q",
  information-score AS "I",
  inference-score AS "Inf",
  concepts-score AS "C",
  assumptions-score AS "A",
  implications-score AS "Imp",
  pov-score AS "PoV"
FROM #critical-thinking-practice
WHERE purpose-score
SORT date-practiced DESC
LIMIT 10
```

### Frameworks Applied Distribution

```dataview
TABLE WITHOUT ID
  primary-framework AS "Framework",
  length(rows) AS "Sessions"
FROM #critical-thinking-practice
GROUP BY primary-framework
SORT length(rows) DESC
```

### Trait Focus Distribution

```dataview
TABLE WITHOUT ID
  target-trait AS "Trait Focus",
  length(rows) AS "Sessions"
FROM #critical-thinking-practice
GROUP BY target-trait
SORT length(rows) DESC
```

### Developmental Stage Progression

```dataview
TABLE
  date-practiced AS "Date",
  developmental-stage AS "Stage",
  overall-score AS "Score"
FROM #critical-thinking-practice
WHERE developmental-stage
SORT date-practiced ASC
```

### Pattern: Which Standards Do I Consistently Skip?

```dataview
TABLE
  weakest-standard AS "Weakest Standard",
  length(rows) AS "Times Identified as Weakest"
FROM #critical-thinking-practice
WHERE weakest-standard
GROUP BY weakest-standard
SORT length(rows) DESC
```

### Pattern: Which Elements Are My Persistent Blindspots?

```dataview
TABLE
  weakest-element AS "Weakest Element",
  length(rows) AS "Times Identified as Weakest"
FROM #critical-thinking-practice
WHERE weakest-element
GROUP BY weakest-element
SORT length(rows) DESC
```

---

# 🔗 Related Concepts & Wiki-Links

[[Critical Thinking]] · [[Paul-Elder Framework]] · [[Elements of Thought]] · [[Intellectual Standards]] · [[Intellectual Virtues]] · [[SEE-I Method]] · [[Toulmin Argument Model]] · [[FRISCO Model]] · [[Browne-Keeley 10 Questions]] · [[Robert Ennis]] · [[Delphi Consensus]] · [[Metacognition]] · [[Self-Regulated Learning]] · [[Deliberate Practice]] · [[Dual Process Theory]] · [[System 1 and System 2]] · [[Cognitive Bias]] · [[Confirmation Bias]] · [[Motivated Reasoning]] · [[Steelmanning]] · [[Intellectual Humility]] · [[Intellectual Courage]] · [[Intellectual Empathy]] · [[Intellectual Autonomy]] · [[Intellectual Integrity]] · [[Intellectual Perseverance]] · [[Confidence in Reason]] · [[Socratic Method]] · [[Epistemology]] · [[Fallacies]] · [[Reasoning]] · [[Argumentation Theory]] · [[Informal Logic]] · [[paul-elder-framework-reference]] · [[critical-thinking-frameworks-master-reference]]

---

> [!quote] Paul & Elder
> "Critical thinking is the art of analyzing and evaluating thinking with a view to improving it."

> [!quote] Closing Reflection Prompt
> Before closing this session, ask: *What is the single most important thing I learned about how I think — not about the subject, but about myself as a thinker?*

> 

[closing-insight:: ]

---

*Template version: 1.0.0 · Companion document: [[2026-05-16_metacog-reflection_daily]]*
*Session generated: <% tp.date.now("YYYY-MM-DD HH:mm") %>*

<% tp.file.cursor() %>
