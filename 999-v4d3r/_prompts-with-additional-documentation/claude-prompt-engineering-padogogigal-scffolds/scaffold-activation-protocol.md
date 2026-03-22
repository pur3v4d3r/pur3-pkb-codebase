# 🎯 Scaffold Activation Protocol

## Purpose

This document defines **when** and **which** pedagogical scaffolds should be injected during LLM response generation for Obsidian PKB content creation. It replaces the need to load the entire 35,000-token mega prompt by providing just-in-time guidance.

---

## 🔄 Core Activation Philosophy

**Progressive Disclosure Principle:**
- Load only the scaffolds needed for the current task
- Inject sequentially as needed during generation
- Avoid cognitive overload from loading all systems

**Token Budget Management:**
- Each scaffold ≤500 tokens
- Typical request requires 3-7 scaffolds (~1,500-2,500 tokens)
- 91-95% token reduction vs. full mega prompt

**Task-Aware Selection:**
- Simple queries: 3-4 scaffolds
- Comprehensive notes: 6-7 scaffolds
- Technical documentation: 5-6 scaffolds

---

## 📊 Scaffold Inventory

| ID | Scaffold Name | Token Count | Primary Use Case |
|----|---------------|-------------|------------------|
| 01 | Note Type Selector | ~300 | Start of any note creation |
| 02 | Frontmatter Builder | ~400 | After note type selected |
| 03 | Wiki-Link Density Guide | ~250 | During content writing |
| 04 | Callout Semantic Selector | ~450 | During content enhancement |
| 05 | Validation Checklist | ~350 | Before finalizing output |
| 06 | Expansion Template | ~400 | At end of comprehensive notes |
| 07 | Inline Field Guide | ~450 | For reference/technical notes |
| 08 | Color Coding Guide | ~400 | For high-priority visual notes |

**Total Available:** ~3,000 tokens
**Typical Usage:** ~1,500-2,500 tokens per request

---

## 🌳 Master Decision Tree

```
USER REQUEST RECEIVED
↓
┌─────────────────────────────────────────┐
│ PHASE 1: CLASSIFY REQUEST TYPE         │
└─────────────────────────────────────────┘
↓
┌─ REQUEST TYPE? ─────────────────────────┐
│                                          │
├─ Creating New Note? ──→ Go to TREE A    │
│                                          │
├─ Formatting Existing? ─→ Go to TREE B   │
│                                          │
├─ Adding Semantic? ────→ Go to TREE C    │
│                                          │
├─ Finalizing Output? ──→ Go to TREE D    │
│                                          │
└─ Simple Query? ───────→ Go to TREE E    │
```

---

## 🌲 TREE A: Creating New Note

**Trigger Phrases:**
- "Create a note about..."
- "Write an atomic/reference/MOC note on..."
- "Generate a comprehensive explanation of..."
- "Build a knowledge base entry for..."

**Sequential Scaffold Injection:**

```
START
↓
[INJECT SCAFFOLD 01: Note Type Selector]
↓
Determine: Atomic | Reference | MOC | Synthesis | Project Hub
↓
[INJECT SCAFFOLD 02: Frontmatter Builder]
↓
Generate YAML header with:
- 5-position tag system
- 2-4 aliases
- Status, certainty, type fields
↓
[INJECT SCAFFOLD 03: Wiki-Link Density Guide] ──┐
[INJECT SCAFFOLD 04: Callout Semantic Selector] ─┤─→ ACTIVE DURING WRITING
↓                                                 │
BEGIN CONTENT GENERATION                          │
↓                                                 │
Write content while consulting Scaffolds 03 & 04 ─┘
↓
IF (Note Type == Reference OR Technical):
  [INJECT SCAFFOLD 07: Inline Field Guide] ──→ ADD INLINE FIELDS
↓
IF (High Priority OR Complex Visuals):
  [INJECT SCAFFOLD 08: Color Coding Guide] ──→ ADD COLOR CODING
↓
[INJECT SCAFFOLD 06: Expansion Template]
↓
Generate "Related Topics for PKB Expansion" section
↓
[INJECT SCAFFOLD 05: Validation Checklist]
↓
Run all 7 gates:
1. Metadata Compliance
2. Wiki-Link Density
3. Callout Usage
4. Format Compliance
5. Expansion Section
6. Content Quality
7. Obsidian Optimization
↓
IF (All Gates Pass):
  OUTPUT ✅
ELSE:
  IDENTIFY ISSUES → FIX → RE-VALIDATE
```

**Token Budget for Tree A:**
- Minimum (Atomic Note): 01 + 02 + 03 + 04 + 05 = ~1,750 tokens
- Typical (Reference Note): 01 + 02 + 03 + 04 + 06 + 07 + 05 = ~2,600 tokens
- Maximum (with color coding): All 8 scaffolds = ~3,000 tokens

---

## 🌲 TREE B: Formatting Existing Content

**Trigger Phrases:**
- "Format this text for Obsidian..."
- "Add wiki-links to this content..."
- "Enhance this with callouts..."
- "Apply metadata to this note..."

**Sequential Scaffold Injection:**

```
START
↓
[INJECT SCAFFOLD 01: Note Type Selector]
↓
Classify existing content: What type of note should this be?
↓
[INJECT SCAFFOLD 02: Frontmatter Builder]
↓
Add YAML frontmatter if missing
↓
[INJECT SCAFFOLD 03: Wiki-Link Density Guide]
↓
Scan content for linkable concepts:
- Core concepts → [[wiki-links]]
- Technical terms → [[wiki-links]]
- Frameworks → [[wiki-links]]
- Prerequisites → [[wiki-links]]
↓
[INJECT SCAFFOLD 04: Callout Semantic Selector]
↓
Identify sections needing semantic structure:
- Definitions → [!definition]
- Examples → [!example]
- Warnings → [!warning]
- Key claims → [!key-claim]
- Evidence → [!evidence]
↓
IF (User Requests Color Coding):
  [INJECT SCAFFOLD 08: Color Coding Guide]
  ↓
  Apply semantic colors:
  - Primary concepts → Gold
  - Technical terms → Cyan
  - Warnings → Magenta
  - Verified info → Green
  - Citations → Orange
↓
IF (Missing Expansion Section):
  [INJECT SCAFFOLD 06: Expansion Template]
  ↓
  Generate "Related Topics" section
↓
[INJECT SCAFFOLD 05: Validation Checklist]
↓
Validate all formatting improvements
↓
OUTPUT ✅
```

**Token Budget for Tree B:**
- Minimum (Basic Formatting): 01 + 03 + 04 + 05 = ~1,350 tokens
- Typical (Full Enhancement): 01 + 02 + 03 + 04 + 06 + 05 = ~2,150 tokens
- Maximum (with color): 01 + 02 + 03 + 04 + 06 + 08 + 05 = ~2,550 tokens

---

## 🌲 TREE C: Adding Semantic Markup

**Trigger Phrases:**
- "Add inline fields to this note..."
- "Apply color coding for better visual hierarchy..."
- "Enhance this with Dataview fields..."
- "Make this more queryable..."

**Sequential Scaffold Injection:**

```
START
↓
[INJECT SCAFFOLD 07: Inline Field Guide]
↓
Scan content for field-worthy information:
- Definitions → [**Term-Name**:: definition]
- Principles → [**Principle-of-X**:: statement]
- Distinctions → [**X-vs-Y**:: contrast]
- Claims → [**Empirical-Finding**:: claim + source]
- Quotes → [**Quote-Author**:: "text"]
- Frameworks → [**Model-Name**:: description]
- Warnings → [**Caution-Note**:: advisory]
- Processes → [**Process-Name**:: steps]
↓
IF (User Requests Color Coding):
  [INJECT SCAFFOLD 08: Color Coding Guide]
  ↓
  Apply semantic HTML spans:
  - <span style='color: #FFC700;'>Primary Concepts</span>
  - <span style='color: #72FFF1;'>Technical Terms</span>
  - <span style='color: #FF00DC;'>Warnings</span>
  - <span style='color: #27FF00;'>Verified Info</span>
  - <span style='color: #FF5700;'>Citations</span>
↓
[INJECT SCAFFOLD 05: Validation Checklist]
↓
Validate:
- Inline field syntax correct
- Field density appropriate (not >30%)
- Color density appropriate (15-30%)
- Accessibility maintained
↓
OUTPUT ✅
```

**Token Budget for Tree C:**
- Inline Fields Only: 07 + 05 = ~800 tokens
- Color Coding Only: 08 + 05 = ~750 tokens
- Both Systems: 07 + 08 + 05 = ~1,200 tokens

---

## 🌲 TREE D: Finalizing Output

**Trigger Phrases:**
- "Check if this is ready to output..."
- "Validate this note before I paste it..."
- "Run quality checks on this content..."
- "Is this production-ready?"

**Sequential Scaffold Injection:**

```
START
↓
[INJECT SCAFFOLD 05: Validation Checklist]
↓
Run All 7 Gates:

Gate 1: Metadata Compliance
- [ ] YAML frontmatter present (if note-type)
- [ ] 3-7 tags, 2-4 aliases
- [ ] Status, certainty, type fields

Gate 2: Wiki-Link Density
- [ ] Count within target range for note type
- [ ] Key concepts linked
- [ ] Correct syntax

Gate 3: Callout Usage
- [ ] Count within target range
- [ ] Semantic types match content
- [ ] Valid syntax

Gate 4: Format Compliance
- [ ] Prose-dominant structure
- [ ] Header hierarchy correct
- [ ] Code blocks fenced
- [ ] No placeholders

Gate 5: Expansion Section
- [ ] 4-6 topics with connections
- [ ] Priority levels assigned
- [ ] Prerequisites identified

Gate 6: Content Quality
- [ ] Depth mandate satisfied
- [ ] Claims supported
- [ ] Information flows logically

Gate 7: Obsidian Optimization
- [ ] Production-ready
- [ ] Plugin-compatible
- [ ] Knowledge graph contribution
↓
Score Each Dimension (1-10):
- Format Compliance: ___
- Knowledge Graph: ___
- Content Quality: ___
- Obsidian Optimization: ___
- Overall: ___
↓
IF (All ≥7 AND Overall ≥8):
  OUTPUT APPROVED ✅
ELSE:
  IDENTIFY ISSUES ⛔
  ↓
  FIX SPECIFIC PROBLEMS
  ↓
  RE-VALIDATE
  ↓
  IF (Still Failing):
    RECOMMEND REGENERATION
```

**Token Budget for Tree D:**
- Single scaffold: 05 only = ~350 tokens

---

## 🌲 TREE E: Simple Query Response

**Trigger Phrases:**
- "What is [concept]?"
- "Explain [topic] briefly..."
- "Quick question about..."
- "Define [term]..."

**Sequential Scaffold Injection:**

```
START
↓
IF (Response will be <600 words):
  ↓
  [INJECT SCAFFOLD 03: Wiki-Link Density Guide]
  ↓
  Target: 3-6 wiki-links for key concepts
  ↓
  [INJECT SCAFFOLD 04: Callout Semantic Selector]
  ↓
  Target: 2-3 callouts (definition, example, key point)
  ↓
  [INJECT SCAFFOLD 06: Expansion Template]
  ↓
  Generate 4 related topics
  ↓
  [INJECT SCAFFOLD 05: Validation Checklist]
  ↓
  Quick validation:
  - No metadata header needed (conversational response)
  - Wiki-links: 3-6 ✓
  - Callouts: 2-3 ✓
  - Expansion: 4 topics ✓
  ↓
  OUTPUT ✅
ELSE:
  Reclassify as note creation → Go to TREE A
```

**Token Budget for Tree E:**
- ~1,450 tokens (03 + 04 + 06 + 05)

---

## 🎮 Activation Examples

### Example 1: "Create an atomic note about Spaced Repetition"

**Classification:** Creating New Note → TREE A

**Scaffold Sequence:**
1. **Inject 01** (Note Type Selector) → Classifies as Atomic Note
2. **Inject 02** (Frontmatter Builder) → Generates:
   ```yaml
   ---
   tags: #learning-theory #spaced-repetition #atomic-note #memory
   aliases: [Distributed Practice, Spacing Effect, Spaced Review]
   status: evergreen
   certainty: verified
   type: atomic
   ---
   ```
3. **Inject 03** (Wiki-Link Density) → Targets 3-8 links
4. **Inject 04** (Callout Selector) → Targets 2-4 callouts
5. **Inject 06** (Expansion Template) → Generates 4 related topics
6. **Inject 05** (Validation) → Final quality check

**Token Load:** ~2,100 tokens
**Time to Apply:** Sequential during generation
**Output Quality:** High fidelity, production-ready

---

### Example 2: "Add wiki-links and callouts to this existing text [paste]"

**Classification:** Formatting Existing Content → TREE B

**Scaffold Sequence:**
1. **Inject 01** (Note Type Selector) → Analyzes content type
2. **Inject 03** (Wiki-Link Density) → Scans for linkable concepts
3. **Inject 04** (Callout Selector) → Identifies sections needing structure
4. **Inject 05** (Validation) → Checks formatting improvements

**Token Load:** ~1,350 tokens
**Time to Apply:** During formatting pass
**Output Quality:** Enhanced structure, maintained content

---

### Example 3: "What is Cognitive Load Theory?"

**Classification:** Simple Query → TREE E

**Scaffold Sequence:**
1. **Inject 03** (Wiki-Link Density) → Targets 3-6 links
2. **Inject 04** (Callout Selector) → Targets 2-3 callouts
3. **Inject 06** (Expansion Template) → Generates 4 related topics
4. **Inject 05** (Validation) → Quick check (no metadata needed)

**Token Load:** ~1,450 tokens
**Time to Apply:** Quick response generation
**Output Quality:** Informative, well-structured, expandable

---

### Example 4: "Create a comprehensive reference note on Dataview plugin"

**Classification:** Creating New Note (Reference) → TREE A

**Scaffold Sequence:**
1. **Inject 01** (Note Type Selector) → Classifies as Reference Note
2. **Inject 02** (Frontmatter Builder) → Comprehensive YAML
3. **Inject 03** (Wiki-Link Density) → Targets 15-40 links
4. **Inject 04** (Callout Selector) → Targets 8-15 callouts
5. **Inject 07** (Inline Field Guide) → Add definitional fields
6. **Inject 06** (Expansion Template) → 6 related topics
7. **Inject 05** (Validation) → Comprehensive quality check

**Token Load:** ~2,600 tokens
**Time to Apply:** Extended generation with multiple passes
**Output Quality:** Exhaustive, heavily cross-referenced, queryable

---

## 🔍 Conditional Injection Rules

### Rule 1: Inline Fields (Scaffold 07)

**INJECT WHEN:**
- ✅ Note type is Reference
- ✅ Note type is Technical Guide
- ✅ Content contains multiple definitions
- ✅ Content includes empirical claims
- ✅ User explicitly requests queryable content

**SKIP WHEN:**
- ❌ Note type is Atomic (unless specifically requested)
- ❌ Note type is MOC
- ❌ Conversational response
- ❌ Simple query (<600 words)

### Rule 2: Color Coding (Scaffold 08)

**INJECT WHEN:**
- ✅ User explicitly requests visual hierarchy
- ✅ Content has complex categorization needs
- ✅ High-priority note requiring maximum attention
- ✅ Multiple semantic layers (primary, technical, warnings, etc.)

**SKIP WHEN:**
- ❌ User prefers plain formatting
- ❌ Simple content without categories
- ❌ Accessibility concerns raised
- ❌ Output platform doesn't support HTML

### Rule 3: Expansion Template (Scaffold 06)

**INJECT WHEN:**
- ✅ Comprehensive response (>600 words)
- ✅ Reference note or synthesis note
- ✅ Content introduces new concepts
- ✅ Topic has clear extension opportunities

**SKIP WHEN:**
- ❌ Trivial query
- ❌ User requests minimal output
- ❌ Content is self-contained with no extensions
- ❌ MOC (already heavy on links)

### Rule 4: Frontmatter Builder (Scaffold 02)

**INJECT WHEN:**
- ✅ Creating permanent note (Atomic, Reference, MOC, Synthesis, Project Hub)
- ✅ User requests metadata
- ✅ Formatting existing content that lacks metadata

**SKIP WHEN:**
- ❌ Conversational response
- ❌ Simple query
- ❌ User explicitly states "no metadata"
- ❌ Non-Obsidian output format

---

## 📏 Token Budget Management

### Budget Allocation by Request Type

| Request Type | Scaffold Count | Token Range | % of Mega Prompt |
|--------------|----------------|-------------|------------------|
| Simple Query | 3-4 | 1,350-1,750 | 3.9-5.0% |
| Basic Note | 5 | 1,750-2,100 | 5.0-6.0% |
| Comprehensive Note | 6-7 | 2,100-2,600 | 6.0-7.4% |
| Technical Doc | 6-7 | 2,200-2,800 | 6.3-8.0% |
| Full Enhancement | 8 | 2,800-3,000 | 8.0-8.6% |

**Average Savings:** ~93% token reduction vs. mega prompt

### Token Conservation Strategies

**Strategy 1: Lazy Loading**
- Load scaffolds only as needed
- Don't preload "just in case"
- Inject at point of application

**Strategy 2: Conditional Skipping**
- Use conditional injection rules
- Skip optional scaffolds when not needed
- Prioritize core scaffolds

**Strategy 3: Sequential Application**
- Load → Apply → Unload → Load Next
- Don't hold all in context simultaneously
- Progressive disclosure through generation

**Strategy 4: Reuse Within Session**
- If scaffold already loaded in request, reference it
- Don't reload identical scaffolds
- But DO reload if different note type

---

## 🎯 Quality Assurance Integration

### Checkpoint System

**Checkpoint 1: After Note Type Selection**
- Confirm correct classification
- Verify frontmatter structure
- Plan density targets

**Checkpoint 2: Mid-Generation**
- Verify wiki-link count tracking correctly
- Check callout distribution
- Ensure prose-dominant structure

**Checkpoint 3: Before Expansion Section**
- Validate content completeness
- Confirm all sections addressed
- Check for placeholders

**Checkpoint 4: Final Pre-Output**
- Run full validation checklist (Scaffold 05)
- Score all 7 dimensions
- Fix any issues before output

### Pass/Fail Integration

**Validation Triggers Scaffold 05 Automatically:**
```
IF (About to output comprehensive content):
  Inject Scaffold 05
  Run validation
  IF (Any dimension <7 OR Overall <8):
    STOP
    IDENTIFY issues
    DETERMINE which scaffold(s) to re-inject for fixing
    APPLY fixes
    RE-VALIDATE
```

**Scaffold Re-Injection for Fixes:**
- Metadata issues → Re-inject Scaffold 02
- Link density low → Re-inject Scaffold 03
- Callout problems → Re-inject Scaffold 04
- Expansion missing → Re-inject Scaffold 06
- Inline field errors → Re-inject Scaffold 07

---

## 🚀 Implementation Checklist

**Phase 1: Deploy Core Scaffolds**
- [ ] Scaffold 01: Note Type Selector
- [ ] Scaffold 02: Frontmatter Builder
- [ ] Scaffold 05: Validation Checklist
- [ ] Scaffold 06: Expansion Template
- [ ] Test with 5 example requests

**Phase 2: Add Enhancement Scaffolds**
- [ ] Scaffold 03: Wiki-Link Density Guide
- [ ] Scaffold 04: Callout Semantic Selector
- [ ] Test formatting improvements
- [ ] Validate token savings

**Phase 3: Add Advanced Scaffolds**
- [ ] Scaffold 07: Inline Field Guide
- [ ] Scaffold 08: Color Coding Guide
- [ ] Test with technical documentation
- [ ] Measure quality improvements

**Phase 4: Optimize Activation Logic**
- [ ] Refine conditional injection rules
- [ ] Monitor token usage patterns
- [ ] Collect user feedback
- [ ] Adjust thresholds as needed

---

## 📊 Success Metrics

### Quantitative Metrics
- **Token Efficiency:** 91-95% reduction vs. mega prompt
- **Format Compliance:** 95%+ pass rate on validation
- **Density Targets:** 90%+ within target ranges
- **Placeholder Elimination:** 100% (zero TODO markers)

### Qualitative Metrics
- **User Satisfaction:** Scaffolds helpful, not overwhelming
- **Production Readiness:** 90%+ immediate paste-to-Obsidian
- **Generation Speed:** 50%+ faster (less context processing)
- **Re-Generation Reduction:** 60%+ fewer format fix requests

### Cognitive Load Metrics
- **Working Memory Load:** ~70% reduction (3-7 focused checklists vs. 11 simultaneous systems)
- **Decision Complexity:** Simplified (binary decision trees vs. comprehensive lists)
- **Error Rate:** 40-60% reduction in formatting errors

---

**END OF ACTIVATION PROTOCOL**

**Key Takeaway:** Match scaffolds to task type. Load progressively. Validate before output. Achieve 93% token savings with maintained quality.
