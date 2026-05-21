---
tags: #quick-start #getting-started #tutorial #pkb-integration #reference-note
aliases: [Getting Started, Quick Start, New User Guide, PKB Integration Tutorial]
status: evergreen
certainty: verified
created: 2024-12-16
updated: 2024-12-16
---

# PKB-LLM Integration System - Quick Start Guide

> [!abstract] Guide Purpose
> This guide helps new users understand and implement the PKB-LLM Integration System in 30 minutes or less. It provides step-by-step instructions for setting up the 3-Tier Architecture across 5 Claude Projects and creating your first integrated notes.

---

## ⏱️ Time Investment

- **Quick Setup**: 15 minutes (get one project running)
- **Full Setup**: 30-45 minutes (all 5 projects)
- **First Note**: 10 minutes (create and integrate)
- **Mastery**: 2-4 weeks (regular usage)

---

## 📋 Prerequisites

Before starting, ensure you have:

- ✅ **Obsidian** installed with a working vault
- ✅ **Claude.ai account** with access to Projects feature
- ✅ **Basic Obsidian knowledge**: Creating notes, using wiki-links
- ✅ **30-45 minutes** of focused time

### Recommended Obsidian Plugins

Install these for full functionality (optional but recommended):

- **Dataview**: Dynamic queries and data extraction
- **Templater**: Note templates and automation
- **Meta Bind**: Interactive buttons and controls
- **QuickAdd**: Fast note capture
- **Tasks**: Task management integration

---

## 🎯 Quick Start Path

Choose your path based on your needs:

### Path A: Minimal Setup (15 minutes)

**Best for**: Getting started quickly with one project

1. Set up CP-02 (Note Creator) only
2. Learn basic integration systems
3. Create your first atomic note
4. **Result**: Functional note creation system

### Path B: Essential Setup (30 minutes)

**Best for**: Core functionality with 3 projects

1. Set up CP-02 (Note Creator)
2. Set up CP-03 (Reference Generator)
3. Set up CP-01 (Report Generator)
4. **Result**: Full content creation workflow

### Path C: Complete Setup (45 minutes)

**Best for**: Full system implementation

1. Set up all 5 Claude Projects
2. Configure all integration systems
3. Create comprehensive examples
4. **Result**: Production-ready system

**Recommendation**: Start with Path A, expand to Path B within a week, complete Path C as needed.

---

## 🚀 Path A: Minimal Setup (15 Minutes)

### Step 1: Create Your First Claude Project (5 minutes)

1. **Go to Claude.ai**
2. **Click "Projects"** in the sidebar
3. **Create New Project**:
   - Name: "Note Creator"
   - Description: "Creates atomic and reference notes using PKB standards"

### Step 2: Load Core Context (5 minutes)

Navigate to your vault folder:
`02-projects/-ongoing-project-pur3v4d3r/01-pkb-plans/_further-pkb-llm-intergration/`

**Add Project Knowledge:**
1. Click "Add Content" → "Upload File"
2. Upload: `optimized-mega-prompt-v2.0.0.md`

**Configure Custom Instructions:**
1. Open in sequence and copy content:
   - `tier-1-universal-memory.md` (paste first)
   - `module-a-pkb-architecture-&-knowledge-graph.md` (paste second)
   - `module-c-project-context-&-history.md` (paste third)
   - `cp-02-p.i.e.-(note-creator).md` (paste fourth)

2. Paste all content into Project's Custom Instructions field

### Step 3: Test Your Setup (5 minutes)

**Test Prompt:**
```
Create an atomic note about the Pomodoro Technique.
Include proper metadata, wiki-links, and at least one semantic callout.
```

**Expected Output:**
- YAML frontmatter with tags
- 300-800 word content
- 3-8 wiki-links
- 2-4 callouts (purple/gold/teal)
- Integration system markers

**Verification Checklist:**
- ✅ Proper metadata structure
- ✅ Semantic callouts present
- ✅ Wiki-links used appropriately
- ✅ Content quality high
- ✅ Integration markers applied

**If successful**: You're ready to create notes! 🎉
**If issues**: Check the Troubleshooting section below.

---

## 🏗️ Path B: Essential Setup (30 Minutes)

### Complete Path A First

Follow all Path A steps, then continue:

### Step 4: Set Up CP-03 (Reference Generator) (8 minutes)

**Create Project:**
- Name: "Reference Generator"
- Description: "Creates comprehensive reference notes with citations and detailed analysis"

**Load Context:**
- Upload: `optimized-mega-prompt-v2.0.0.md`
- Custom Instructions (in order):
  1. `tier-1-universal-memory.md`
  2. `module-a-pkb-architecture-&-knowledge-graph.md`
  3. `module-b-technical-infrastructure-&-local-ai.md`
  4. `module-c-project-context-&-history.md`
  5. `cp-03-comprehensive-reference-(reference-note-generator).md`

**Test Prompt:**
```
Create a comprehensive reference note about Cognitive Load Theory.
Include 15+ wiki-links, 8+ callouts, and apply all relevant integration systems.
Target 1,500-2,000 words.
```

### Step 5: Set Up CP-01 (Report Generator) (8 minutes)

**Create Project:**
- Name: "Report Generator"
- Description: "Generates analytical reports and synthesis documents"

**Load Context:**
- Upload: `optimized-mega-prompt-v2.0.0.md`
- Custom Instructions (in order):
  1. `tier-1-universal-memory.md`
  2. `module-a-pkb-architecture-&-knowledge-graph.md`
  3. `module-d-cognitive-frameworks-(detailed-applications).md`
  4. `cp-01-foundation-03-(report-generator).md`

**Test Prompt:**
```
Generate a synthesis report analyzing the relationship between
Cognitive Load Theory and the Zettelkasten method for knowledge management.
```

### Step 6: Create Your First Workflow (9 minutes)

**Workflow: Research Paper → Notes → Report**

1. **Use CP-03** to create reference note from a research paper
2. **Use CP-02** to extract 2-3 atomic notes from the reference
3. **Use CP-01** to create synthesis report connecting concepts

**Example Workflow:**
```
Topic: "How spaced repetition improves memory retention"

CP-03 → Create reference note "Spaced Repetition Systems"
  ↓
CP-02 → Extract atomic notes:
  - "Forgetting Curve"
  - "Spacing Effect"
  - "Retrieval Practice"
  ↓
CP-01 → Generate report:
  "Cognitive Mechanisms Behind Spaced Repetition Effectiveness"
```

**Success Criteria:**
- Reference note: 1,500+ words, 15+ links
- Atomic notes: 300-800 words each, 3-8 links
- Report: Synthesizes all concepts, cites specific notes

---

## 🌟 Path C: Complete Setup (45 Minutes)

### Complete Path B First

Follow all Path B steps, then continue:

### Step 7: Set Up CP-04 (Automation Engineer) (8 minutes)

**Create Project:**
- Name: "Automation Engineer"
- Description: "Designs and implements Obsidian automations and templates"

**Load Context:**
- Upload: `optimized-mega-prompt-v2.0.0.md`
- Custom Instructions (in order):
  1. `tier-1-universal-memory.md`
  2. `module-b-technical-infrastructure-&-local-ai.md`
  3. `module-c-project-context-&-history.md`
  4. `cp-04-obsidian-automations-(template-automation-engineer).md`

**Test Prompt:**
```
Create a Templater script that generates a new atomic note template
with proper YAML frontmatter, including tag suggestions based on folder location.
```

### Step 8: Set Up CP-05 (Prompt Engineer) (8 minutes)

**Create Project:**
- Name: "Prompt Engineer"
- Description: "Meta-level prompt engineering and system optimization"

**Load Context:**
- Upload: `optimized-mega-prompt-v2.0.0.md`
- Custom Instructions (in order):
  1. `tier-1-universal-memory.md`
  2. `module-a-pkb-architecture-&-knowledge-graph.md`
  3. `module-b-technical-infrastructure-&-local-ai.md`
  4. `module-c-project-context-&-history.md`
  5. `module-d-cognitive-frameworks-(detailed-applications).md`
  6. `cp-05-meta-level-prompting-(prompt-engineer).md`

**Test Prompt:**
```
Analyze the prompt structure for CP-02 (Note Creator) and suggest
3 optimizations to improve atomic note quality and integration system application.
```

### Step 9: Master the Integration Systems (14 minutes)

Work through each integration system category:

**Practice Set 1: Epistemic Systems (4 minutes)**
```
Create a note that demonstrates:
1. Epistemic Confidence Encoding (^verified, ^established, etc.)
2. Evidence Weight Indicators (⚖️weak → ⚖️definitive)
3. Contradiction Markers (⚠️contradicts, ⚠️tensions-with)
```

**Practice Set 2: Structural Systems (4 minutes)**
```
Create a note that demonstrates:
4. Atomic Extraction Signaling (🔬atomic-candidate)
5. Prerequisite Mapping (📚requires-first)
6. Synthesis Potential Markers (🔗synthesis-opportunity)
```

**Practice Set 3: Temporal Systems (3 minutes)**
```
Create a note that demonstrates:
7. Semantic Versioning ([**Version**:: v1.0.0])
8. Temporal Decay Indicators (⏳review-quarterly)
9. Spaced Repetition Integration (🔄SR-eligible)
```

**Practice Set 4: Research & Application (3 minutes)**
```
Create a note that demonstrates all remaining systems:
10-16. (Source Provenance, Query Anchors, etc.)
```

---

## 📚 Understanding the 16 Integration Systems

### Quick Reference Table

| # | System | Marker Example | Purpose |
|---|--------|----------------|---------|
| 1 | Epistemic Confidence | `^verified` | Track certainty level |
| 2 | Semantic Relationships | `→causes` | Type wiki-link relationships |
| 3 | Evidence Weight | `⚖️strong` | Rate source reliability |
| 4 | Contradiction Markers | `⚠️contradicts` | Flag conflicts |
| 5 | Atomic Extraction | `🔬atomic-candidate` | Identify decomposition |
| 6 | Prerequisite Mapping | `📚requires-first` | Learning sequences |
| 7 | Synthesis Potential | `🔗synthesis-opportunity` | Integration chances |
| 8 | Mental Model Anchors | `🧠mental-model` | Core frameworks |
| 9 | Semantic Versioning | `v2.1.0` | Track evolution |
| 10 | Temporal Decay | `⏳review-quarterly` | Maintenance schedule |
| 11 | Spaced Repetition | `🔄SR-eligible` | Memory integration |
| 12 | Source Provenance | `Primary → Secondary` | Citation chains |
| 13 | Counterexamples | `❗counterexample` | Exceptions |
| 14 | Query Anchors | `#q/how-to-*` | Searchable tags |
| 15 | Application Context | `💼applies-to` | Use cases |
| 16 | Cognitive Load | `🧠heavy` | Complexity warnings |

### When to Use Each System

**Always Use** (Every Note):
- Epistemic Confidence (System 1)
- Semantic Relationships (System 2)
- Semantic Versioning (System 9)

**Use Often** (Most Notes):
- Evidence Weight (System 3) - when citing sources
- Prerequisite Mapping (System 6) - for learning content
- Query Anchors (System 14) - for discoverability

**Use Selectively** (As Needed):
- Contradiction Markers (System 4) - when conflicts exist
- Atomic Extraction (System 5) - for complex topics
- Synthesis Potential (System 7) - when connections spotted
- Mental Model Anchors (System 8) - for foundational concepts
- Temporal Decay (System 10) - for time-sensitive content
- Spaced Repetition (System 11) - for memorization targets
- Source Provenance (System 12) - for academic work
- Counterexamples (System 13) - to prevent overgeneralization
- Application Context (System 15) - for practical content
- Cognitive Load (System 16) - for complex material

---

## 🎓 Your First Real Note

Let's create a complete note using all best practices:

### Example: Create Note on "Working Memory"

**Step 1: Choose the Right Project**
→ Use **CP-02 (Note Creator)** for an atomic note

**Step 2: Provide Context-Rich Prompt**
```
Create an atomic note about Working Memory from cognitive science.

Requirements:
- 500-700 words
- YAML with appropriate tags (cognitive-science, learning-theory, memory-systems)
- Status: budding (still developing)
- Certainty: established (well-researched concept)
- 5-7 wiki-links to related concepts
- 3 semantic callouts (purple for definitions, gold for examples, teal for connections)
- Apply integration systems:
  * Epistemic confidence markers
  * Evidence weight indicators
  * Prerequisite mapping (what concepts needed first)
  * Query anchors (#q/what-is-working-memory)
  * Cognitive load indicator
```

**Step 3: Review and Refine**

Check the output against quality criteria:
- ✅ Proper YAML frontmatter
- ✅ Appropriate tag hierarchy (L1 → L2 → L3)
- ✅ 5-7 wiki-links present
- ✅ Callouts properly colored and used
- ✅ Integration systems applied
- ✅ Content accurate and well-structured

**Step 4: Save to Your Vault**

1. Copy the generated content
2. Create new note in Obsidian
3. Save in appropriate folder (e.g., `03-permanent-notes/cognitive-science/`)
4. Filename: `working-memory.md`

**Step 5: Verify Integration**

- Wiki-links resolve to other notes (or create stubs)
- Dataview queries can find the note by tags
- Integration markers are searchable

---

## 🔄 Daily Workflow Examples

### Workflow 1: Research Paper Processing

**Time**: 20-30 minutes per paper

```
1. Read paper and highlight key points (10 min)
   ↓
2. Use CP-03: Create comprehensive reference note (10 min)
   - Paste paper title and key excerpts
   - Request full reference note
   ↓
3. Use CP-02: Extract 2-4 atomic notes (5 min)
   - Identify key concepts from reference
   - Request atomic notes for each
   ↓
4. Manual: Link notes in your vault (5 min)
   - Add wiki-links between related notes
   - Update MOCs
```

### Workflow 2: Learning New Topic

**Time**: 30-45 minutes per session

```
1. Use CP-02: Create initial atomic note (10 min)
   - Basic concept understanding
   - Mark as 🌱 seedling
   ↓
2. Research and gather information (15 min)
   - Read sources
   - Collect evidence
   ↓
3. Use CP-03: Expand to reference note (15 min)
   - Comprehensive coverage
   - Multiple sources
   - Evidence weights
   ↓
4. Use CP-02: Extract specialized atomic notes (5 min)
   - Focused sub-concepts
   - Linked to main reference
```

### Workflow 3: Weekly Review & Synthesis

**Time**: 60 minutes weekly

```
1. Review notes created this week (20 min)
   - Check integration markers
   - Verify wiki-link connections
   - Update maturity status
   ↓
2. Use CP-01: Generate synthesis report (20 min)
   - Identify patterns across notes
   - Create integration report
   ↓
3. Update MOCs and dashboards (15 min)
   - Add new notes to appropriate MOCs
   - Update statistics
   ↓
4. Identify gaps and next priorities (5 min)
   - What needs elaboration?
   - What connections are missing?
```

---

## 🎯 Project Selection Guide

### When to Use Each Claude Project

**CP-01 (Report Generator)**
- Creating analytical reports
- Synthesizing multiple sources
- Generating executive summaries
- Cross-domain analysis
- **Token Load**: Medium (A + D modules)

**CP-02 (Note Creator)**
- Creating atomic notes (300-800 words)
- Quick concept capture
- Elaborating fleeting notes
- Breaking down complex topics
- **Token Load**: Medium (A + C modules)

**CP-03 (Reference Generator)**
- Comprehensive reference notes (1,500+ words)
- Research paper summaries
- In-depth topic exploration
- Technical documentation
- **Token Load**: Heavy (A + B + C modules)

**CP-04 (Automation Engineer)**
- Creating Templater scripts
- Designing Meta Bind buttons
- Building QuickAdd macros
- Obsidian automation
- **Token Load**: Medium (B + C modules)

**CP-05 (Prompt Engineer)**
- Optimizing prompts
- System improvements
- Meta-level analysis
- Troubleshooting integration
- **Token Load**: Heavy (All modules)

### Decision Tree

```
Need to create content?
├─ Yes → What type?
│   ├─ Short concept note → CP-02
│   ├─ Long reference → CP-03
│   └─ Synthesis report → CP-01
└─ No → What task?
    ├─ Automation → CP-04
    └─ System optimization → CP-05
```

---

## ⚠️ Common Pitfalls & Solutions

### Pitfall 1: Over-Application of Integration Systems

**Problem**: Adding every integration system to every note creates clutter.

**Solution**: Use the "Always / Often / Selectively" guide above. Not every note needs every system.

**Example**:
❌ Bad: Every note has all 16 systems
✅ Good: Core systems (1, 2, 9) always; others as relevant

### Pitfall 2: Incorrect Module Loading

**Problem**: Loading wrong modules wastes tokens and reduces performance.

**Solution**: Follow the Module Loading Matrix strictly.

**Example**:
❌ Bad: Loading Module D in CP-02 (not needed for note creation)
✅ Good: Only load A + C for CP-02

### Pitfall 3: Inconsistent Metadata

**Problem**: Tags and metadata don't follow taxonomy system.

**Solution**: Always use L1 → L2 → L3 → L4 tag hierarchy.

**Example**:
❌ Bad: `tags: #notes #stuff #things`
✅ Good: `tags: #cognitive-science #working-memory #atomic-note`

### Pitfall 4: Wiki-Link Overload

**Problem**: Too many wiki-links reduce signal-to-noise ratio.

**Solution**: Follow note type guidelines:
- Atomic: 3-8 links
- Reference: 15-40 links
- MOC: 20-50+ links

### Pitfall 5: Neglecting Maturity Status

**Problem**: All notes stay as seedlings forever.

**Solution**: Review and update maturity monthly:
- 🌱 Seedling → 🌿 Budding → 🌳 Evergreen

---

## 🔧 Troubleshooting

### Issue: Claude Project Not Following PKB Standards

**Symptoms**: Output lacks proper metadata, wiki-links, or callouts

**Diagnosis**:
1. Check if custom instructions were loaded correctly
2. Verify mega prompt is in Project Knowledge
3. Confirm modules are appropriate for project

**Solution**:
1. Re-copy custom instructions carefully
2. Ensure no truncation occurred
3. Test with simple prompt first

### Issue: Integration Systems Not Being Applied

**Symptoms**: Notes lack markers like ^verified, ⚖️strong, etc.

**Diagnosis**:
1. Check if Module A was loaded (contains integration systems)
2. Verify prompt mentions specific systems
3. Confirm project is CP-01, CP-02, CP-03, or CP-05 (not CP-04)

**Solution**:
1. Add Module A if missing
2. Request specific systems in prompt
3. Provide examples of desired markers

### Issue: Token Limit Errors

**Symptoms**: "Context window full" errors

**Diagnosis**:
1. Check total token count for project
2. Verify only appropriate modules loaded
3. Ensure mega prompt uploaded to Project Knowledge (not instructions)

**Solution**:
1. Remove unnecessary modules
2. Move mega prompt from instructions to knowledge
3. Use shorter prompts

### Issue: Inconsistent Output Quality

**Symptoms**: Sometimes good, sometimes poor results

**Diagnosis**:
1. Prompt clarity varies
2. Context not sufficient
3. Project selection inappropriate

**Solution**:
1. Use more specific, detailed prompts
2. Provide examples of desired output
3. Verify using correct project for task

---

## 📈 Progress Milestones

Track your mastery with these milestones:

### Week 1: Foundation
- ✅ Set up at least CP-02 (Note Creator)
- ✅ Create 5 atomic notes with proper metadata
- ✅ Understand 3-Tier Architecture concept
- ✅ Use 3 core integration systems (1, 2, 9)

### Week 2: Expansion
- ✅ Set up CP-01 and CP-03
- ✅ Complete first workflow (paper → reference → atomics → report)
- ✅ Use 8 integration systems comfortably
- ✅ Create first MOC with 15+ notes

### Week 3: Automation
- ✅ Set up CP-04 (Automation Engineer)
- ✅ Create first Templater script
- ✅ Build QuickAdd macro for note capture
- ✅ Use all 16 integration systems appropriately

### Week 4: Mastery
- ✅ Set up CP-05 (Prompt Engineer)
- ✅ Optimize prompts for your specific needs
- ✅ Create custom integration workflows
- ✅ Knowledge graph exceeds 30+ interconnected notes

---

## 🎯 Next Steps

After completing this quick start:

1. **Read the Full Documentation**:
   - [[pkb-and-llm-integration-moc]] - Main hub
   - [[system-architecture-overview]] - Deep dive into architecture
   - [[modular-prompt-components-from-pkb-llm-integration-update-project]] - All 16 systems detailed

2. **Explore Quick References**:
   - [[master-quick-reference-pkb-integration]] - Master QRC
   - [[quick-reference-callout-taxonomy]] - Callout system
   - [[quick-reference-wiki-link-protocol]] - Wiki-link best practices

3. **Review Deployment Guide**:
   - [[pkb-integration-system-deployment-v2.0.0]] - Complete deployment details

4. **Join the Workflow**:
   - Start your daily research workflow
   - Build your knowledge graph systematically
   - Refine your personal system

---

## 💡 Pro Tips

### Tip 1: Start Small, Scale Gradually
Don't try to apply all 16 integration systems immediately. Master 3-5 core systems first, then add others as needed.

### Tip 2: Use Templates
Create Templater templates for common note types. This ensures consistency and speeds up creation.

### Tip 3: Batch Similar Tasks
Use the same Claude Project for multiple similar tasks in one session. This leverages conversation context.

### Tip 4: Review Weekly
Set aside 30-60 minutes weekly to review notes, update maturity, and identify synthesis opportunities.

### Tip 5: Trust the Process
The system seems complex initially but becomes second nature with practice. Focus on one aspect at a time.

---

## 🎓 Learning Resources

### Video Tutorials (Coming Soon)
- Setting up your first Claude Project (5 min)
- Creating your first integrated note (10 min)
- Understanding the 16 integration systems (15 min)
- Building your first workflow (20 min)

### Example Vaults
- Starter vault with 10 example notes
- Template collection
- Sample workflows

### Community
- Discussion forum for questions
- Share your workflows
- Request features

---

## ✅ Quick Start Checklist

Print this checklist and track your progress:

### Immediate Setup (Today)
- [ ] Install Obsidian plugins (Dataview, Templater, etc.)
- [ ] Create first Claude Project (CP-02)
- [ ] Load Tier 1 + Modules A & C
- [ ] Upload mega prompt to Project Knowledge
- [ ] Test with simple note creation prompt
- [ ] Verify output quality

### Week 1 Goals
- [ ] Create 5 atomic notes using CP-02
- [ ] Set up CP-03 (Reference Generator)
- [ ] Set up CP-01 (Report Generator)
- [ ] Complete first workflow (paper → notes → report)
- [ ] Master 3 core integration systems

### Week 2-4 Goals
- [ ] Set up remaining projects (CP-04, CP-05)
- [ ] Use all 16 integration systems
- [ ] Create first MOC with 20+ notes
- [ ] Build custom Templater template
- [ ] Establish daily workflow

### Ongoing Mastery
- [ ] Weekly review and synthesis
- [ ] Monthly system optimization
- [ ] Quarterly architecture review
- [ ] Continuous learning and refinement

---

*Guide Version: v1.0.0*
*Last Updated: 2024-12-16*
*Estimated Completion Time: 15-45 minutes depending on path*
*Status: 🌳 Evergreen*
*Certainty: ^verified*
