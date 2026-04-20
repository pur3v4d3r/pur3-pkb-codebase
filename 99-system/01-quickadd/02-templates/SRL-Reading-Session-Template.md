<%*
// ═══════════════════════════════════════════════════════════════════════════
// SRL READING SESSION TEMPLATE v1.0
// Zimmerman's Forethought + Self-Reflection Phases
// For PKB-Integrated Academic Reading
// ═══════════════════════════════════════════════════════════════════════════
// SETUP: Place this file in your Templater templates folder.
// TRIGGER: Use QuickAdd or Templater to create a new session note.
// ═══════════════════════════════════════════════════════════════════════════

const sessionDate = tp.date.now("YYYY-MM-DD");
const sessionTime = tp.date.now("HHmm");
const sessionId = `${sessionDate}-${sessionTime}-srl-session`;

// Prompt for the text being read
const textTitle = await tp.system.prompt("📖 What text/report are you reading?");
const textType = await tp.system.suggester(
    ["Foundational Report", "Focused Analysis", "Dialectical Re-Examination", "Academic Paper", "Book Chapter", "Other"],
    ["foundational", "focused-analysis", "dialectical", "academic-paper", "book-chapter", "other"]
);

// Schema level assessment
const schemaLevel = await tp.system.suggester(
    ["Schema-Rich (solid prior knowledge)", "Schema-Moderate (some background)", "Schema-Sparse (genuinely new territory)"],
    ["rich", "moderate", "sparse"]
);
_%>
---
# ═══════════════════════════════════════════════════════════════════════════
# SRL READING SESSION
# ═══════════════════════════════════════════════════════════════════════════
type: srl-reading-session
session-id: "<% sessionId %>"
date: <% sessionDate %>
time-started: <% tp.date.now("HH:mm") %>
text-title: "<% textTitle %>"
text-type: <% textType %>
schema-level: <% schemaLevel %>

# ── Forethought Phase Metadata ──
forethought-completed: false
outcome-goal: ""
process-goals-count: 0
self-efficacy-pre: 0
confidence-calibration: ""

# ── Self-Reflection Phase Metadata ──
reflection-completed: false
comprehension-level: ""
process-integrity-rating: 0
self-efficacy-post: 0
attribution-type: ""
attribution-controllable: false
adaptive-inference: ""
defensive-inference-detected: false

# ── Calibration Metrics ──
prediction-accuracy: ""
calibration-delta: 0

# ── PKB Integration ──
new-notes-created: 0
connections-established: 0
learning-agenda-updated: false

# ── Classification ──
tags:
  - srl-session
  - forethought-phase
  - self-reflection-phase
  - <% textType %>
  - schema-<% schemaLevel %>
  - reading-session

status: active
linked-learning-agenda: "[[SRL-Living-Learning-Agenda]]"
linked-calibration-log: "[[SRL-Calibration-Log]]"
---

# 📖 SRL Reading Session: <% textTitle %>

> [!info] Session Info
> **Date:** <% sessionDate %> | **Session ID:** `<% sessionId %>`
> **Text Type:** <% textType %> | **Schema Level:** <% schemaLevel %>
> **Linked:** [[SRL-Living-Learning-Agenda]] | [[SRL-Calibration-Log]]

---

# ═══════════════════════════════════════════════════════════════════════════
# PHASE 1: FORETHOUGHT (Complete Before Reading)
# ═══════════════════════════════════════════════════════════════════════════

> [!important] Complete this entire section BEFORE you begin reading.
> Time investment: 5–10 minutes. This is not optional overhead — it is the structural mechanism that makes the reading session productive. See [[Zimmerman's-Cyclical-SRL-Model]] and [[forethought-phase]].

---

## 🔍 Zone 1: Prior Knowledge Activation

> [!tip] Purpose
> Activate relevant [[prior-knowledge-activation|prior knowledge]] and existing schema before encountering new material. This reduces [[cognitive-load-theory|cognitive load]] and creates explicit baselines for later calibration. See [[advance-organizers]].

**Related concepts already in my PKB:**
- [[]] — 
- [[]] — 
- [[]] — 

**Gaps I've identified in my current understanding:**
- Gap 1: 
- Gap 2: 

**Connection hypotheses I'm bringing to this reading:**
- I predict this text will extend / challenge / complement [[]] because…
- I expect tension with [[]] around the issue of…

**Handoff from previous session:**
*(Copy from last session's Self-Reflection adaptive inference, or from [[SRL-Living-Learning-Agenda]])*
- 

---

## 📋 Zone 2: Task Characterization

> [!tip] Purpose
> Accurately assess what this reading task demands so that goal-setting and strategy selection are appropriately calibrated. See [[strategic-planning]].

| Dimension | Assessment |
|-----------|-----------|
| **Conceptual complexity** | `INPUT[inlineSelect(option(High), option(Moderate), option(Low)):complexity]` |
| **Estimated reading time** | ___ minutes |
| **Primary challenge anticipated** | |
| **Prior knowledge estimate** | <% schemaLevel %> |

---

## 🎯 Zone 3: Goal Setting — Three-Part Structure

> [!tip] Purpose
> Set specific, mastery-framed goals using the three-part structure that activates attentional direction, provides evaluable standards, and sustains [[intrinsic-motivation]]. See [[achievement-goal-theory]] and [[goal-setting-theory]].

### Learning Outcome Goal *(mastery-framed, specific, proximal)*

**Content Anchor** — *What specific concept/mechanism am I targeting?*
> 

**Comprehension Criterion** — *How will I know I've achieved this? (Must require cognitive production, not recognition)*
> I will know I've achieved this when I can (without looking at the text): 
> *(Examples: explain the mechanism in my own words / generate 2 original examples / identify implications for X / articulate how this connects to [[]] and where they create tension)*

**Transfer Target** — *Why does this matter to me?*
> I want this understanding because: 
> *(Connect to genuine intellectual interest or PKB goal — not "I should know this" but "I want to understand this because…")*

### Process Goals *(behavioral, under my direct control)*

> [!warning] Process goals are what you actually DO, not what you hope to understand. They should be specific enough that you can definitively say Yes or No to whether you executed them. See [[deliberate-practice]].

- [ ] **PG1:** I will pause at each section break and write a one-sentence summary
- [ ] **PG2:** I will flag any passage where I experience genuine confusion (not explain it away)
- [ ] **PG3:** I will check each major claim against my connection hypothesis from Zone 1
- [ ] **PG4 (custom):** 

### Stopping Rule
> If I have been genuinely confused for more than ___ minutes without progress, I will: 
> *(search PKB for prerequisites / accept this passage needs return after preparation / adjust comprehension criterion scope)*

---

## 💪 Zone 4: Self-Efficacy Calibration

> [!tip] Purpose
> Generate an *accurately calibrated* confidence estimate — not high confidence, but honest confidence. The target is [[metacognitive-calibration|calibration]], not elevation. See [[self-efficacy]] and [[the-fluency-illusion]].

**My confidence that I can meet the comprehension criterion (1–10):** ___

**What specifically is driving this rating?**
> 

**Calibration check:** *What would need to be true for me to achieve this criterion? Does my confidence rating reflect the actual task demands?*
> 

**If confidence is below 5:** Consider whether the comprehension criterion needs adjustment, or whether a preliminary schema-building activity is needed first. *(This is not failure — it is accurate [[metacognitive-monitoring|metacognitive monitoring]].)*

**Recent mastery experience I can recall that is relevant:**
> *(A time I successfully understood material of similar complexity — this is the [[self-efficacy|mastery experience]] source of self-efficacy.)*

---

## ✨ Zone 5: Motivational Priming

> [!tip] Purpose
> Activate [[self-determination-theory|autonomous motivation]] by connecting to genuine interest and [[autonomy-support|autonomy-supportive]] framing. See [[intrinsic-motivation]].

**What specifically interests me about this topic?**
> *(Not "I should know this" — that's controlling language. What genuinely draws me to this?)*

**How does this reading connect to a question or project I genuinely care about?**
> 

**Today's session is successful if:**
> *(Focus on process goals — a self-efficacy-protecting standard that remains achievable even if comprehension is incomplete)*

---

> [!success] Forethought Phase Complete
> You are now ready to begin reading. Open the text and execute your process goals.
> **Remember:** Flag confusion rather than explaining it away. That data is the raw material for Self-Reflection.

---

# ═══════════════════════════════════════════════════════════════════════════
# PHASE 2: SELF-REFLECTION (Complete After Reading)
# ═══════════════════════════════════════════════════════════════════════════

> [!important] Complete within 30 minutes of finishing the reading session.
> Time investment: 10–15 minutes. This is the generative engine of the SRL cycle — where [[adaptive-inference|adaptive inferences]] are produced that improve the next session. See [[self-reflection-phase]].

**Reading duration:** ___ minutes
**Time completed:** <% tp.date.now("HH:mm") %>

---

## 📊 Zone 1: Cold Reconstruction *(Retrieval-Based Comprehension Test)*

> [!warning] Do NOT consult any notes or the text for this zone.
> Write from memory only. Set a 5-minute timer. This is the mechanism that defeats the [[the-fluency-illusion|fluency illusion]] — if you can't produce it, you didn't learn it. See [[retrieval-practice]] and [[testing-effect-retrieval-practice-effect]].

**Core claim of this text (in my own words):**
> 

**Key mechanism/process the author describes:**
> 

**Key distinctions made:**
> 

**One connection to existing PKB knowledge:**
> [[]] — 

**One question that arose during reading:**
> 

---

### Generativity Tests *(Calibration instruments — go beyond recognition)*

**Test 1: Novel Example Generation**
> Identify one mechanism from this reading. Generate an example the text did NOT provide.
- *Concept:* 
- *My example:* 
- *What this reveals about my understanding:* 

**Test 2: Mechanism Reconstruction**
> Without looking at the text, reconstruct the causal chain of one core mechanism.
- *Mechanism:* 
- *My reconstruction:* 
- *After checking — accurate? What was missing?* 

**Test 3: Novel Connection**
> What connection between this report's content and an existing PKB node did you make that the report did NOT make explicitly?
- *Connection:* [[]] ↔ [[]]
- *Why this connection matters:* 

---

*(Now compare reconstruction to text/notes. Mark gaps.)*

**Comprehension gaps identified:**
- Gap 1: 
- Gap 2: 

**Comprehension level against criterion:**
`INPUT[inlineSelect(option(Full — met criterion completely), option(Substantial — mostly met criterion), option(Partial — significant gaps remain), option(Minimal — criterion largely unmet)):comprehension-level]`

---

## ✅ Zone 2: Process Goal Audit

> [!tip] Purpose
> Evaluate each process goal against behavioral evidence, not impressions. This is [[formative-assessment|formative self-assessment]] — descriptive, not evaluative. See [[self-evaluation]].

| Process Goal | Executed? | Evidence | Quality (1–5) |
|---|---|---|---|
| PG1: | Yes / Partial / No | | |
| PG2: | Yes / Partial / No | | |
| PG3: | Yes / Partial / No | | |
| PG4: | Yes / Partial / No | | |

**Overall process integrity rating (1–10):** ___
**What this rating is based on:** *(specific behaviors, not global impressions)*

---

## 🔬 Zone 3: Causal Attribution Analysis

> [!warning] CRITICAL ZONE — This is the hinge on which the entire cycle turns.
> The attribution you generate here determines whether the next session improves or stagnates. See [[attribution-theory]], [[bernard-weiner]], and [[attribution-retraining]].

> [!important] Before generating ANY global conclusion about your ability or the text's difficulty, complete the strategy-level search below.

### Attribution Analysis — For Each Comprehension Gap:

**Gap/Failure:** 

**First-response attribution** *(what automatically comes to mind)*:
> 

**Attribution dimensions:**
- Locus: Internal / External
- Stability: Stable / Unstable  
- Controllability: Controllable / Uncontrollable

**Strategy-Level Explanation Search:**

| Question | Y/N | Details |
|----------|-----|---------|
| Did I have sufficient prior schema? | | |
| Was my goal specific enough? | | |
| Did I use [[elaborative-interrogation|elaborative interrogation]]? | | |
| Did I self-explain at section boundaries? | | |
| Was my comprehension criterion calibrated to my actual level? | | |
| Was my attention available for the cognitive demands? | | |
| Did I attempt too much in this session? | | |

**Revised attribution** *(specific, unstable, controllable)*:
> "The strategy I used was ___. It was insufficient because ___. A better approach for next time would be ___."

> [!danger] Attribution Safety Check
> If your natural attribution is "this material is too difficult for me" or "I'm not good at this type of content" — these are global, stable, internal attributions. Before accepting them, you MUST list at least two specific strategy-level explanations you could test in the next session. See [[mastery-oriented-response-pattern]] and [[growth-mindset]].

---

## ⚡ Zone 4: Self-Reaction — Adaptive Inference Generation

> [!tip] Purpose
> Generate specific, actionable strategy adjustments that feed directly into the next Forethought Phase. This is where the cycle closes. See [[adaptive-inference]] and [[defensive-inference]].

### Affect Acknowledgment
**My honest emotional reaction to this session's outcomes:**
> *(Frustration and disappointment are appropriate and informative. Shame or global self-criticism are signals that Zone 3 attribution may not be working — return to the strategy-level search.)*

### What Worked — Sustain These
- 
- 

### Strategy Revisions for Next Session
*(Be concrete: not "I'll be more careful" but "Instead of X, I will try Y because Z")*
- Revision 1: 
- Revision 2: 

### Goal Adjustments
> Were the process goals appropriately challenging?
> - If consistently met easily → raise the bar
> - If consistently not met → diagnose: too ambitious, or execution support needed?

**Goal adjustment for next session:**
> 

### Defensive Inference Check
> Did I generate any of these? If so, flag for [[attribution-retraining]].
- [ ] "I should just read easier material"
- [ ] "Maybe this topic isn't for me"
- [ ] "I'll try harder next time" (without strategy specificity)
- [ ] Desire to lower goals to avoid future failure
- [ ] None detected

---

## 🔗 Zone 5: PKB Integration & Forward Planning

### New Permanent Notes to Create/Update
- [ ] [[]] — Key content: 
- [ ] [[]] — Update needed: 

### New Connections Established
- [[]] ↔ [[]] — Relationship: 

### Flagged Gaps for Follow-Up
- Gap: ___ — Suggested resource: [[]]

### Carry-Forward to [[SRL-Living-Learning-Agenda]]
- New question: 
- Strategy insight: 
- Next reading priority: 

---

## 🤝 Zone 6: Handoff to Next Forethought Phase

> [!success] THE HANDOFF MECHANISM
> This is the physical link that ensures the SRL cycle actually closes. Copy this content to the Handoff field of your next session's Forethought Protocol, and update your [[SRL-Living-Learning-Agenda]].

**Adjustments for next Forethought Phase session:**
> 

**Self-efficacy note for next session:**
> *(Brief honest assessment — updated by this session's mastery experience)*

**Self-efficacy post-session (1–10):** ___

---

## 💬 Mastery Reflection *(Close the emotional loop)*

> [!quote] Use mastery grammar to close productively. See [[achievement-goal-theory]].

**What do I understand better now than I did at the start of this session?**
> 

**What genuinely surprised, challenged, or shifted my thinking?**
> 

**What question am I now more precisely able to ask than before?**
> 

---

> [!success] Session Complete
> **Next Steps:**
> 1. Update [[SRL-Calibration-Log]] with this session's metrics
> 2. Update [[SRL-Living-Learning-Agenda]] with carry-forward items
> 3. Create any permanent notes flagged in Zone 5
> 4. Schedule next reading session

<%*
// Auto-update frontmatter completion flags
// (Uncomment when ready to use with MetaEdit or similar)
// await app.fileManager.processFrontMatter(tp.file.find_tfile(tp.file.path), (fm) => {
//     fm["forethought-completed"] = true;
//     fm["reflection-completed"] = true;
// });
_%>
