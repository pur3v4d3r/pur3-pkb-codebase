# 🎨 Self-Documenting System: Domain Implementation Templates

---
tags: #pkm #domain-templates #implementation-guide #dataview #reference-note
aliases: [Domain Templates Library, Ready-to-Use Domain Configurations, Domain Instantiation Examples]
---

> [!abstract] Document Purpose
> This document provides **production-ready templates** for instantiating the self-documenting knowledge framework across different domains. Each template includes complete configuration, customized note templates, and example implementations. These are **copy-paste-customize** resources designed for immediate deployment in your [[Obsidian]] vault.

---

## 📚 Template Library Overview

This document contains five complete domain configurations:

1. **[[#Template A Cognitive Science Domain]]** - For psychology, neuroscience, learning theory research
2. **[[#Template B PKM Methodology Domain]]** - For knowledge management methods and workflows  
3. **[[#Template C Prompt Engineering Domain]]** - For LLM prompting techniques and frameworks
4. **[[#Template D Cosmology Scientific Theory Domain]]** - For astrophysics, cosmology, theoretical physics
5. **[[#Template E Custom Domain Blank Slate]]** - Fully customizable template for any domain

Each template includes:
- ✅ Domain Configuration Note
- ✅ Customized Concept Note Template
- ✅ Customized Application Note Template
- ✅ Example Concept Note
- ✅ Example Application Note
- ✅ Domain Health Dashboard

---

# Template A: Cognitive Science Domain

## 1. Domain Configuration Note

**File Location**: `Knowledge Domains/Cognitive Science/03-Meta/_Domain-Config.md`

```markdown
---
tags: #domain-config #cognitive-science #meta
Type: Domain Configuration
---

# Cognitive Science Domain - Configuration

## Domain Identity
- **Domain Name**: Cognitive Science Research & Theory
- **Scope**: Theories, phenomena, methods, and models in cognitive psychology, neuroscience, learning science, and related fields
- **Primary MOC**: [[Cognitive Science Overview MOC]]
- **Folder Structure**: `Knowledge Domains/Cognitive Science/`

## Taxonomy Definition

### Concept Types

- **Theory**: Explanatory frameworks for cognitive phenomena
  - Examples: Working Memory Theory, Cognitive Load Theory, Dual Process Theory
- **Phenomenon**: Observed cognitive effects or behaviors
  - Examples: Spacing Effect, Testing Effect, Cognitive Dissonance
- **Method**: Research methodologies or experimental paradigms
  - Examples: fMRI Analysis, Eye-Tracking Studies, Think-Aloud Protocol
- **Model**: Formal or computational representations
  - Examples: ACT-R Model, Connectionist Networks, Bayesian Brain Model

### Metadata Field Schema

Application notes (research papers, study analyses, experimental designs) should include:

1. **StudyType**::`<value>`
   - **Purpose**: Classification of research methodology
   - **Controlled Vocabulary**: 
     - Experimental
     - Observational
     - Meta-Analysis
     - Theoretical Review
     - Computational Modeling
     - Mixed Methods
   - **Example**: `StudyType:: Experimental`

2. **Theories**::`[[Theory 1]], [[Theory 2]]`
   - **Purpose**: Which theoretical frameworks the research engages with
   - **Format**: Array of wiki-links to theory concept notes
   - **Example**: `Theories:: [[Working Memory]], [[Cognitive Load Theory]]`

3. **Paradigm**::`<value>`
   - **Purpose**: Broader research paradigm or school of thought
   - **Controlled Vocabulary**:
     - Cognitivist
     - Behaviorist
     - Constructivist
     - Connectionist
     - Embodied Cognition
     - Evolutionary Psychology
   - **Example**: `Paradigm:: Cognitivist`

4. **Population**::`<value>` (Optional)
   - **Purpose**: Study population characteristics
   - **Format**: Free text
   - **Example**: `Population:: University undergraduates, N=120`

5. **KeyFindings**::`<value>` (Optional)
   - **Purpose**: Brief summary of major results
   - **Format**: Free text
   - **Example**: `KeyFindings:: Spacing increased retention by 40% vs. massed practice`

## Folder Architecture

```
Knowledge Domains/Cognitive Science/
├── 00-Concepts/              # Theory, Phenomenon, Method, Model notes
├── 01-Applications/          # Research papers, study analyses
├── 02-Synthesis/            # Literature reviews, meta-analyses
└── 03-Meta/                 # This config + domain overview MOC
```

## Status Tasks Template for Concepts

Cognitive Science concepts should document:

- [ ] Core definition with citations
- [ ] Key characteristics identified
- [ ] Empirical evidence summarized
- [ ] Related theories/phenomena linked
- [ ] Applications in research documented
- [ ] Limitations and critiques noted
- [ ] Seminal references cited

## Sample Query Patterns

### Find Studies Using a Theory
```dataview
TABLE WITHOUT ID
  file.link as "📄 Study",
  StudyType,
  Theories,
  KeyFindings
FROM "Knowledge Domains/Cognitive Science/01-Applications"
WHERE contains(Theories, [[Current Theory]])
```

### Find Experimental Methods
```dataview
LIST
FROM "Knowledge Domains/Cognitive Science/00-Concepts"
WHERE Type = "Method" AND contains(StudyType, "Experimental")
```
```

---

## 2. Concept Note Template (Cognitive Science)

**File Location**: `Knowledge Domains/Cognitive Science/03-Meta/_Concept-Template.md`

```markdown
---
aliases: []
Type: Theory | Phenomenon | Method | Model
MOC: "[[Cognitive Science Overview MOC]]"
---

# [CONCEPT NAME]

status:: `$= dv.current().status`

## 🎯 Definition

> [!definition]
> [Provide formal definition with citation if available]
>
> **Origin**: [Who first proposed/discovered this, when]
> **Field**: [Subdiscipline - e.g., Cognitive Psychology, Neuroscience]

## 🧠 Core Characteristics

[Describe essential features in prose or structured format]

### Key Components

1. **[Component 1]**: [Description]
2. **[Component 2]**: [Description]
3. **[Component 3]**: [Description]

## 🔬 Empirical Support

> [!evidence]
> **Major Findings**:
> - [Finding 1 with citation]
> - [Finding 2 with citation]
> - [Finding 3 with citation]

### Seminal Studies

- [[Study Author Year]] - [Brief description of contribution]
- [[Study Author Year]] - [Brief description of contribution]

## 🔗 Applications in Research

### Studies Using This Concept

**Self-Discovery Query**: This automatically populates with research that applies or tests this concept.

```dataview
TABLE WITHOUT ID
  file.link as "📄 Research Note",
  StudyType as "Type",
  Theories as "Frameworks",
  KeyFindings as "Key Findings"
FROM "Knowledge Domains/Cognitive Science/01-Applications"
FLATTEN file.outlinks as links
WHERE meta(links).path = this.file.path
GROUP BY file.link
SORT StudyType ASC
```

### Common Applications

[Describe how this concept is typically used in research]

## 🔗 Related Concepts

### Theoretical Connections
- [[Related Theory 1]] - [Nature of relationship]
- [[Related Theory 2]] - [Nature of relationship]

### Related Phenomena
- [[Related Phenomenon]] - [How they connect]

### Methodological Links
- [[Method]] - [Common method for studying this concept]

## ⚠️ Limitations & Critiques

> [!warning]
> **Known Limitations**:
> - [Limitation 1]
> - [Limitation 2]
>
> **Critical Perspectives**:
> - [Critique with citation]

## 📚 Key References

1. [Author, Year]. *Title*. Journal.
2. [Author, Year]. *Title*. Journal.
3. [Author, Year]. *Title*. Journal.

## 📊 Status Tasks

- [ ] Core definition with citations documented
- [ ] Key characteristics identified
- [ ] Empirical evidence summarized
- [ ] Related theories/phenomena linked
- [ ] Applications in research documented
- [ ] Limitations and critiques noted
- [ ] Seminal references cited

## 🔍 Query Meta

- QueryType:: [[Self-Discovery Query]]
- dataCommands:: [[TABLE]], [[FROM]], [[FLATTEN]], [[WHERE]], [[GROUP BY]]
- functions:: [[meta()]]
- targetFolder:: "01-Applications"

## 🌐 Knowledge Graph Position

```dataviewjs
const inboundLinks = dv.page(dv.current().file.path).file.inlinks;
const outboundLinks = dv.page(dv.current().file.path).file.outlinks;

dv.table(
    ["📥 Used In (Inbound)", "📤 Builds On (Outbound)"],
    Array.from({length: Math.max(inboundLinks.length, outboundLinks.length)}, (_, i) => [
        inboundLinks[i] || "",
        outboundLinks[i] || ""
    ])
);
```
```

---

## 3. Application Note Template (Cognitive Science)

**File Location**: `Knowledge Domains/Cognitive Science/03-Meta/_Application-Template.md`

```markdown
---
tags: #cognitive-science #research #application-note
Type: Application
MOC: "[[Cognitive Science Overview MOC]]"
---

# [STUDY/PAPER TITLE]

## 📊 Research Metadata

StudyType:: Experimental | Observational | Meta-Analysis | Theoretical Review | Computational Modeling
Theories:: [[Theory 1]], [[Theory 2]], [[Theory 3]]
Paradigm:: Cognitivist | Behaviorist | Constructivist | Connectionist
Population:: [Sample characteristics - e.g., "Adults 18-65, N=200"]
KeyFindings:: [One-sentence summary of major results]

## 🎯 Research Question

[What question does this study address?]

## 🧠 Theoretical Framework

This research builds on and contributes to:

- **[[Theory 1]]** - [How it's applied or tested]
- **[[Theory 2]]** - [How it's applied or tested]
- **[[Phenomenon]]** - [How it relates]

## 🔬 Methodology

### Design
[Study design overview - experimental manipulation, controls, etc.]

### Participants
[Sample description]

### Measures
[What was measured and how]

### Procedure
[How the study was conducted]

## 📊 Key Findings

### Primary Results

1. **[Finding 1]**: [Description with statistics if relevant]
2. **[Finding 2]**: [Description with statistics if relevant]
3. **[Finding 3]**: [Description with statistics if relevant]

### Implications

[What do these results mean for theory? For practice?]

## 💡 Personal Analysis & Integration

[Your thoughts on the research]

### Connections to Other Work
- [[Related Study 1]] - [How they connect]
- [[Related Study 2]] - [How they compare/contrast]

### Questions Raised
- [Question 1]
- [Question 2]

### Application to My Work
[How this relates to your research interests or PKB development]

## ⚠️ Limitations

- [Limitation 1]
- [Limitation 2]

## 📚 Citation

[Full APA citation]

**DOI/Link**: [If available]

## 🏷️ Tags & Classification

Paradigm: `=this.Paradigm`
Study Type: `=this.StudyType`
Theories Engaged: `=this.Theories`
```

---

## 4. Example Concept Note (Cognitive Science)

**File Location**: `Knowledge Domains/Cognitive Science/00-Concepts/Working Memory.md`

```markdown
---
aliases: [WM, Short-Term Memory, Phonological Loop, Visuospatial Sketchpad]
Type: Theory
MOC: "[[Cognitive Science Overview MOC]]"
---

# Working Memory

status:: `$= dv.current().status`

## 🎯 Definition

> [!definition]
> **Working Memory** is the cognitive system responsible for temporarily holding and manipulating information necessary for complex tasks such as reasoning, comprehension, and learning. Unlike passive short-term memory, working memory involves active processing and manipulation of information.
>
> **Origin**: Baddeley & Hitch (1974) proposed the multi-component model
> **Field**: Cognitive Psychology, Cognitive Neuroscience

## 🧠 Core Characteristics

Working memory is characterized by its limited capacity (approximately 7±2 chunks), active processing requirements, and multi-component architecture. The classic Baddeley model includes:

### Key Components

1. **Central Executive**: Attentional control system that coordinates subsystems and manages cognitive resources
2. **Phonological Loop**: Maintains verbal and acoustic information through rehearsal
3. **Visuospatial Sketchpad**: Stores and manipulates visual and spatial information
4. **Episodic Buffer** (added 2000): Integrates information across subsystems and links to long-term memory

### Capacity Constraints

The limited capacity of working memory (typically 7±2 items, or 4±1 chunks per Cowan) creates a fundamental bottleneck in human cognition, directly impacting learning, problem-solving, and decision-making.

## 🔬 Empirical Support

> [!evidence]
> **Major Findings**:
> - Dual-task studies show interference between tasks competing for same WM subsystem (Baddeley & Hitch, 1974)
> - Neuroimaging reveals prefrontal cortex activation during WM tasks (D'Esposito et al., 1995)
> - Individual differences in WM capacity predict academic achievement and fluid intelligence (Engle et al., 1999)

### Seminal Studies

- [[Baddeley & Hitch 1974]] - Original multi-component model proposal
- [[Miller 1956]] - The magical number seven plus or minus two
- [[Cowan 2001]] - Revised capacity estimate (~4 chunks)

## 🔗 Applications in Research

### Studies Using This Concept

**Self-Discovery Query**:

```dataview
TABLE WITHOUT ID
  file.link as "📄 Research Note",
  StudyType as "Type",
  Theories as "Frameworks",
  KeyFindings as "Key Findings"
FROM "Knowledge Domains/Cognitive Science/01-Applications"
FLATTEN file.outlinks as links
WHERE meta(links).path = this.file.path
GROUP BY file.link
SORT StudyType ASC
```

### Common Applications

- **[[Cognitive Load Theory]]** directly builds on WM capacity limitations
- Educational interventions designed to reduce WM load
- Clinical assessments of cognitive impairment
- Human-computer interaction research

## 🔗 Related Concepts

### Theoretical Connections
- [[Cognitive Load Theory]] - Explains learning difficulty based on WM limits
- [[Attention]] - Central executive function overlaps with attentional control
- [[Long-Term Memory]] - Information transfer mechanisms

### Related Phenomena
- [[Chunking]] - Strategy to overcome capacity limits
- [[Cognitive Interference]] - Disruption of WM processing

### Methodological Links
- [[N-Back Task]] - Common WM assessment method
- [[Dual-Task Paradigm]] - Tests WM subsystem independence

## ⚠️ Limitations & Critiques

> [!warning]
> **Known Limitations**:
> - Capacity estimates vary significantly across measurement methods
- Debate over whether WM is truly separate from long-term memory or just activated LTM (Cowan)
> 
> **Critical Perspectives**:
> - Some researchers argue for domain-general vs. domain-specific capacity (Kane & Engle, 2002)
> - Neural evidence suggests more distributed networks than original model proposed

## 📚 Key References

1. Baddeley, A. D., & Hitch, G. (1974). Working memory. *Psychology of Learning and Motivation*, 8, 47-89.
2. Miller, G. A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2), 81-97.
3. Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences*, 24(1), 87-114.

## 📊 Status Tasks

- [x] Core definition with citations documented
- [x] Key characteristics identified
- [x] Empirical evidence summarized
- [x] Related theories/phenomena linked
- [ ] Applications in research documented (partial)
- [x] Limitations and critiques noted
- [x] Seminal references cited

## 🔍 Query Meta

- QueryType:: [[Self-Discovery Query]]
- dataCommands:: [[TABLE]], [[FROM]], [[FLATTEN]], [[WHERE]], [[GROUP BY]]
- functions:: [[meta()]]
- targetFolder:: "01-Applications"

## 🌐 Knowledge Graph Position

```dataviewjs
const inboundLinks = dv.page(dv.current().file.path).file.inlinks;
const outboundLinks = dv.page(dv.current().file.path).file.outlinks;

dv.table(
    ["📥 Used In (Inbound)", "📤 Builds On (Outbound)"],
    Array.from({length: Math.max(inboundLinks.length, outboundLinks.length)}, (_, i) => [
        inboundLinks[i] || "",
        outboundLinks[i] || ""
    ])
);
```
```

---

## 5. Example Application Note (Cognitive Science)

**File Location**: `Knowledge Domains/Cognitive Science/01-Applications/Study - WM Training Transfer 2023.md`

```markdown
---
tags: #cognitive-science #research #working-memory #application-note
Type: Application
MOC: "[[Cognitive Science Overview MOC]]"
---

# Does Working Memory Training Transfer to Fluid Intelligence?

## 📊 Research Metadata

StudyType:: Meta-Analysis
Theories:: [[Working Memory]], [[Fluid Intelligence]], [[Transfer of Training]]
Paradigm:: Cognitivist
Population:: Meta-analysis of 87 studies, total N=4,536
KeyFindings:: Small near-transfer effects (d=0.24), negligible far-transfer to fluid intelligence (d=0.09)

## 🎯 Research Question

Does cognitive training targeting working memory capacity produce transfer effects to untrained cognitive abilities, specifically fluid intelligence?

## 🧠 Theoretical Framework

This meta-analysis tests predictions from:

- **[[Working Memory]]** - If WM is a domain-general capacity, training should show broad transfer
- **[[Fluid Intelligence]]** - Hypothesized relationship with WM capacity (individual differences research)
- **[[Transfer of Training]]** - Conditions under which learning transfers to new domains

The theoretical motivation stems from correlational research showing WM capacity predicts fluid intelligence (r≈.50), leading to hypothesis that improving WM should improve gF.

## 🔬 Methodology

### Design
Systematic review and meta-analysis of randomized controlled trials

### Inclusion Criteria
- RCT design with active or passive control
- Pre/post measures of WM and at least one far-transfer measure
- Published 2008-2023

### Measures
- **Near Transfer**: Untrained WM tasks (N-back, complex span)
- **Far Transfer**: Fluid intelligence (Raven's Matrices, WAIS subtests)
- **Very Far Transfer**: Academic achievement, ADHD symptoms

### Analysis
Random-effects meta-analysis with publication bias correction

## 📊 Key Findings

### Primary Results

1. **Near Transfer Effect**: Small but significant (g = 0.24, 95% CI [0.15, 0.33])
   - Training improves performance on untrained WM tasks
   - Effect size decreases with study quality (well-controlled studies: g = 0.15)

2. **Far Transfer to Fluid Intelligence**: Negligible (g = 0.09, 95% CI [-0.01, 0.19])
   - No significant improvement in reasoning ability
   - Publication bias likely inflates even this small effect

3. **Moderator Analyses**:
   - Younger participants show slightly larger effects
   - Training duration (10-40 sessions) doesn't predict transfer magnitude
   - Adaptive training no better than non-adaptive

### Implications

Results challenge the theoretical assumption that WM training can enhance domain-general cognitive capacity. The correlation between WM and gF may reflect shared genetic factors or common neural substrates rather than causal relationship.

## 💡 Personal Analysis & Integration

### Connections to Other Work

- **[[Cognitive Training Debate]]** - Adds to skeptical literature on "brain training" efficacy
- **[[Dual Process Theory]]** - Suggests System 2 processing limitations may not be malleable through training
- **[[Learning Transfer]]** - Consistent with specificity of learning principle

### Questions Raised

1. If WM and gF are correlated but training doesn't transfer, what explains the correlation?
   - Genetic factors?
   - Shared neural networks that develop together but resist modification?

2. Are there *any* cognitive interventions that produce robust far transfer?
   - Strategy training?
   - Metacognitive interventions?

3. What about very long-term training (>100 sessions) - would neural plasticity emerge?

### Application to My Work

This has major implications for my [[Learning System Design]] notes:
- Don't rely on domain-general "capacity building" approaches
- Focus on domain-specific practice with meaningful contexts
- Consider if PKB development itself is a form of "cognitive training" - does it transfer?

Relevant to [[Cognitive Load Theory]] application in my vault design:
- If WM capacity is relatively fixed, offloading to external systems (PKB) becomes even more critical
- This justifies investment in automation and smart note-taking systems

## ⚠️ Limitations

- Publication bias likely present despite correction attempts
- Most studies use adaptive N-back training (limited generalizability)
- Measurement reliability of gF measures varies across studies
- Short-term post-tests (median = 2 weeks) - no data on long-term persistence

## 📚 Citation

Sala, G., & Gobet, F. (2023). Do working memory training programs transfer to fluid intelligence? A meta-analysis of 87 randomized controlled trials. *Psychological Bulletin*, 149(1), 1-31. https://doi.org/10.1037/bul0000398

## 🏷️ Tags & Classification

Paradigm: `=this.Paradigm`
Study Type: `=this.StudyType`
Theories Engaged: `=this.Theories`
```

---

## 6. Domain Health Dashboard (Cognitive Science)

**File Location**: `Knowledge Domains/Cognitive Science/03-Meta/Domain Health Dashboard.md`

```markdown
---
tags: #cognitive-science #dashboard #analytics
Type: Meta
---

# Cognitive Science Domain - Health Dashboard

## 📊 Domain Statistics

**Concept Count**: `$= dv.pages('"Knowledge Domains/Cognitive Science/00-Concepts"').length`
**Application Count**: `$= dv.pages('"Knowledge Domains/Cognitive Science/01-Applications"').length`
**Synthesis Count**: `$= dv.pages('"Knowledge Domains/Cognitive Science/02-Synthesis"').length`

**Total Notes**: `$= dv.pages('"Knowledge Domains/Cognitive Science"').length`

---

## 🏆 Most Referenced Concepts

```dataview
TABLE
  Type as "Concept Type",
  length(file.inlinks) as "Usage Count",
  status as "📊 Status"
FROM "Knowledge Domains/Cognitive Science/00-Concepts"
WHERE Type != null
SORT length(file.inlinks) DESC
LIMIT 10
```

---

## 🚨 Orphan Concepts (Unused)

```dataview
LIST
FROM "Knowledge Domains/Cognitive Science/00-Concepts"
WHERE length(file.inlinks) = 0 AND Type != null
```

> [!attention]
> Orphan concepts should either have application notes created OR be removed if obsolete.

---

## 📈 Recent Activity

```dataview
TABLE
  StudyType as "Type",
  Theories as "Concepts Used",
  file.cday as "Created"
FROM "Knowledge Domains/Cognitive Science/01-Applications"
SORT file.cday DESC
LIMIT 15
```

---

## ⚙️ Concept Type Distribution

```dataview
TABLE
  length(rows) as "Count"
FROM "Knowledge Domains/Cognitive Science/00-Concepts"
GROUP BY Type
SORT length(rows) DESC
```

---

## 🎯 Incomplete Documentation

```dataview
TABLE
  Type as "Type",
  status as "Completion"
FROM "Knowledge Domains/Cognitive Science/00-Concepts"
WHERE !contains(status, "100%")
SORT status ASC
```

---

## 📊 Study Type Distribution

```dataview
TABLE
  length(rows) as "Count",
  rows.file.link as "Studies"
FROM "Knowledge Domains/Cognitive Science/01-Applications"
WHERE StudyType != null
GROUP BY StudyType
SORT length(rows) DESC
```

---

## 🌐 Paradigm Distribution

```dataview
TABLE
  length(rows) as "Count"
FROM "Knowledge Domains/Cognitive Science/01-Applications"
WHERE Paradigm != null
GROUP BY Paradigm
SORT length(rows) DESC
```
```

---

# Template B: PKM Methodology Domain

## 1. Domain Configuration Note

**File Location**: `Knowledge Domains/PKM Methodology/03-Meta/_Domain-Config.md`

```markdown
---
tags: #domain-config #pkm #meta
Type: Domain Configuration
---

# PKM Methodology Domain - Configuration

## Domain Identity
- **Domain Name**: Personal Knowledge Management Methodology
- **Scope**: Methods, tools, workflows, principles for building and maintaining personal knowledge systems
- **Primary MOC**: [[PKM Overview MOC]]
- **Folder Structure**: `Knowledge Domains/PKM Methodology/`

## Taxonomy Definition

### Concept Types

- **Method**: Systematic approaches to knowledge work
  - Examples: Zettelkasten, PARA Method, Cornell Notes, Progressive Summarization
- **Tool**: Software, plugins, or physical instruments
  - Examples: Obsidian, Dataview Plugin, Index Cards, Commonplace Book
- **Workflow**: Process or routine for knowledge activities
  - Examples: Daily Review Workflow, Capture-Process-Review, Spaced Repetition Scheduling
- **Principle**: Foundational concepts or best practices
  - Examples: Atomic Notes, Progressive Disclosure, Compound Interest of Knowledge

### Metadata Field Schema

Application notes (workflow implementations, tool configurations, case studies) should include:

1. **MethodType**::`<value>`
   - **Purpose**: Classification of PKM approach
   - **Controlled Vocabulary**:
     - Capture
     - Process/Organize
     - Connect/Link
     - Create/Synthesize
     - Review/Maintain
     - Search/Retrieve
   - **Example**: `MethodType:: Capture`

2. **Tools**::`[[Tool 1]], [[Tool 2]]`
   - **Purpose**: Which tools/plugins the implementation uses
   - **Format**: Array of wiki-links to tool concept notes
   - **Example**: `Tools:: [[Dataview]], [[Templater]], [[QuickAdd]]`

3. **Complexity**::`<value>`
   - **Purpose**: Implementation difficulty level
   - **Controlled Vocabulary**:
     - Beginner (< 30 min setup)
     - Intermediate (30 min - 2 hours)
     - Advanced (> 2 hours or requires coding)
   - **Example**: `Complexity:: Intermediate`

4. **AutomationLevel**::`<value>` (Optional)
   - **Purpose**: Degree of automation
   - **Controlled Vocabulary**: Manual | Semi-Automated | Fully Automated
   - **Example**: `AutomationLevel:: Semi-Automated`

## Folder Architecture

```
Knowledge Domains/PKM Methodology/
├── 00-Concepts/              # Method, Tool, Workflow, Principle notes
├── 01-Applications/          # Workflow docs, implementations, configs
├── 02-Synthesis/            # PKM system designs, methodology comparisons
└── 03-Meta/                 # This config + domain overview MOC
```

## Status Tasks Template for Concepts

PKM concepts should document:

- [ ] Core definition with examples
- [ ] Key characteristics identified
- [ ] Implementation guidance provided
- [ ] Related methods/tools linked
- [ ] Use cases documented
- [ ] Pros/cons or limitations noted
- [ ] Resources and references cited

## Sample Query Patterns

### Find Workflows Using a Method
```dataview
TABLE WITHOUT ID
  file.link as "📄 Workflow",
  MethodType,
  Tools,
  Complexity
FROM "Knowledge Domains/PKM Methodology/01-Applications"
WHERE contains(file.outlinks, [[Current Method]])
```

### Find Beginner-Friendly Implementations
```dataview
LIST
FROM "Knowledge Domains/PKM Methodology/01-Applications"
WHERE Complexity = "Beginner"
```
```

---

## 2. Concept Note Template (PKM)

**File Location**: `Knowledge Domains/PKM Methodology/03-Meta/_Concept-Template.md`

```markdown
---
aliases: []
Type: Method | Tool | Workflow | Principle
MOC: "[[PKM Overview MOC]]"
---

# [CONCEPT NAME]

status:: `$= dv.current().status`

## 🎯 Definition

> [!definition]
> [Clear explanation of what this method/tool/workflow/principle is]
>
> **Origin**: [Creator or first documented use if known]
> **Category**: [Method | Tool | Workflow | Principle]

## 🔑 Core Characteristics

[Essential features and attributes]

### Key Components

1. **[Component 1]**: [Description]
2. **[Component 2]**: [Description]
3. **[Component 3]**: [Description]

## 💡 Core Principles (if applicable)

> [!principle-point]
> [Fundamental ideas that guide this approach]

## ⚙️ Implementation Guide

### Basic Setup

[Step-by-step for getting started]

### Configuration Options

[Customization possibilities]

### Best Practices

- [Practice 1]
- [Practice 2]
- [Practice 3]

## 🔗 Applications & Implementations

### Workflows Using This Concept

**Self-Discovery Query**:

```dataview
TABLE WITHOUT ID
  file.link as "📄 Implementation",
  MethodType as "Type",
  Tools as "Tools Used",
  Complexity as "Difficulty"
FROM "Knowledge Domains/PKM Methodology/01-Applications"
FLATTEN file.outlinks as links
WHERE meta(links).path = this.file.path
GROUP BY file.link
SORT Complexity ASC
```

### Common Use Cases

[Where this is typically applied]

## 🔗 Related Concepts

### Complementary Methods/Tools
- [[Related Method 1]] - [How they work together]
- [[Related Tool 1]] - [Integration possibilities]

### Contrasting Approaches
- [[Alternative Method]] - [Key differences]

## ⚖️ Pros & Cons

> [!key-claim] Advantages
> - [Advantage 1]
> - [Advantage 2]
> - [Advantage 3]

> [!warning] Limitations
> - [Limitation 1]
> - [Limitation 2]
> - [Limitation 3]

## 📚 Resources & References

### Key Articles/Books
- [Resource 1]
- [Resource 2]

### Community Resources
- [Forum/Guide 1]
- [Tutorial 1]

## 📊 Status Tasks

- [ ] Core definition with examples
- [ ] Key characteristics identified
- [ ] Implementation guidance provided
- [ ] Related methods/tools linked
- [ ] Use cases documented
- [ ] Pros/cons or limitations noted
- [ ] Resources and references cited

## 🔍 Query Meta

- QueryType:: [[Self-Discovery Query]]
- dataCommands:: [[TABLE]], [[FROM]], [[FLATTEN]], [[WHERE]], [[GROUP BY]]
- functions:: [[meta()]]
- targetFolder:: "01-Applications"

## 🌐 Knowledge Graph Position

```dataviewjs
const inboundLinks = dv.page(dv.current().file.path).file.inlinks;
const outboundLinks = dv.page(dv.current().file.path).file.outlinks;

dv.table(
    ["📥 Used In (Inbound)", "📤 Builds On (Outbound)"],
    Array.from({length: Math.max(inboundLinks.length, outboundLinks.length)}, (_, i) => [
        inboundLinks[i] || "",
        outboundLinks[i] || ""
    ])
);
```
```

---

## 3. Application Note Template (PKM)

**File Location**: `Knowledge Domains/PKM Methodology/03-Meta/_Application-Template.md`

```markdown
---
tags: #pkm #workflow #application-note
Type: Application
MOC: "[[PKM Overview MOC]]"
---

# [WORKFLOW/IMPLEMENTATION NAME]

## 📊 Implementation Metadata

MethodType:: Capture | Process/Organize | Connect/Link | Create/Synthesize | Review/Maintain | Search/Retrieve
Tools:: [[Tool 1]], [[Tool 2]], [[Tool 3]]
Complexity:: Beginner | Intermediate | Advanced
AutomationLevel:: Manual | Semi-Automated | Fully Automated

## 🎯 Purpose

[What problem does this workflow solve? What need does it address?]

## 🧠 Concepts Applied

This implementation uses:

- **[[Method 1]]** - [How it's applied]
- **[[Tool 1]]** - [Role in the workflow]
- **[[Principle 1]]** - [How it informs design]

## ⚙️ Implementation Details

### Prerequisites

[What needs to be in place before this can be used]

- Plugin: [[Tool Name]]
- Folder structure: `[Path]`
- Templates: `[Required templates]`

### Step-by-Step Setup

1. **[Step 1]**: [Detailed instruction]
2. **[Step 2]**: [Detailed instruction]
3. **[Step 3]**: [Detailed instruction]

### Configuration

[Code blocks, settings, or configuration details]

```[language]
[Code or configuration]
```

## 🔄 Usage Workflow

### Daily/Regular Use

1. **[Action 1]**: [How to perform]
2. **[Action 2]**: [How to perform]
3. **[Action 3]**: [How to perform]

### Triggers

[When should this workflow be executed?]

## 📊 Benefits Realized

[Concrete outcomes from using this implementation]

- **Time Savings**: [Specific metrics if available]
- **Quality Improvements**: [Observable benefits]
- **Integration**: [How it connects with other workflows]

## 🔧 Customization Options

[How this can be adapted for different needs]

### Variations

- **Variation 1**: [Description and use case]
- **Variation 2**: [Description and use case]

## ⚠️ Limitations & Gotchas

- [Issue 1 and workaround]
- [Issue 2 and workaround]

## 💡 Lessons Learned

[Insights from implementing and using this]

### What Works Well
- [Positive observation]

### What Could Be Improved
- [Area for refinement]

## 🔗 Related Implementations

- [[Related Workflow 1]] - [How they connect]
- [[Related Workflow 2]] - [How they compare]

## 🏷️ Classification

Method Type: `=this.MethodType`
Tools Used: `=this.Tools`
Complexity: `=this.Complexity`
Automation: `=this.AutomationLevel`
```

---

*[Templates C, D, and E follow similar pattern - continuing with key differences only]*

---

# Template C: Prompt Engineering Domain

## 1. Domain Configuration Note (Abbreviated)

```markdown
## Taxonomy Definition

### Concept Types
- **Technique**: Specific prompting methods
  - Examples: Chain-of-Thought, Few-Shot Learning, ReAct
- **Pattern**: Structural templates
  - Examples: Role-Task-Format, Constitutional AI, Tree of Thoughts
- **Framework**: Comprehensive prompting systems
  - Examples: PROMPT Framework, APE (Automatic Prompt Engineer)
- **Strategy**: High-level approaches
  - Examples: Prompt Chaining, Self-Consistency, Verification

### Metadata Field Schema

1. **PromptType**::`<value>`
   - Controlled Vocabulary: Zero-Shot | Few-Shot | Chain-of-Thought | Constitutional | Multi-Turn | Agentic

2. **Techniques**::`[[Technique 1]], [[Technique 2]]`
   - Array of technique concept links

3. **Model**::`<value>`
   - Example: `Model:: Claude Sonnet 4, GPT-4, Gemini`

4. **UseCase**::`<value>`
   - Example: `UseCase:: Research Synthesis, Code Generation, Creative Writing`

5. **Effectiveness**::`<value>` (Optional)
   - Rating: Low | Medium | High | Variable
```

---

# Template D: Cosmology / Scientific Theory Domain

## 1. Domain Configuration Note (Abbreviated)

```markdown
## Taxonomy Definition

### Concept Types
- **Theory**: Comprehensive explanatory frameworks
  - Examples: ΛCDM Model, Inflation Theory, String Theory
- **Phenomenon**: Observable effects or objects
  - Examples: Dark Matter, Cosmic Microwave Background, Black Holes
- **Law**: Fundamental physical principles
  - Examples: Hubble's Law, Conservation Laws, General Relativity
- **Model**: Formal mathematical representations
  - Examples: Friedmann Equations, Density Perturbation Spectrum

### Metadata Field Schema

1. **ObservationType**::`<value>`
   - Controlled Vocabulary: Observational | Theoretical | Computational | Experimental

2. **Theories**::`[[Theory 1]], [[Theory 2]]`

3. **Scale**::`<value>`
   - Controlled Vocabulary: Quantum | Stellar | Galactic | Cosmological

4. **EvidenceStrength**::`<value>` (Optional)
   - Controlled Vocabulary: Speculative | Supported | Well-Established | Consensus
```

---

# Template E: Custom Domain (Blank Slate)

## 1. Domain Configuration Template

```markdown
---
tags: #domain-config #[YOUR-DOMAIN-TAG] #meta
Type: Domain Configuration
---

# [YOUR DOMAIN NAME] - Configuration

## Domain Identity
- **Domain Name**: [Full name of your knowledge domain]
- **Scope**: [What this domain encompasses - be specific]
- **Primary MOC**: [[Your Domain Overview MOC]]
- **Folder Structure**: `Knowledge Domains/[Your Domain Name]/`

## Taxonomy Definition

### Concept Types

Define 3-5 categorical types for concepts in your domain:

- **Type 1**: [Name] - [Description of what falls in this category]
  - Examples: [Example 1], [Example 2], [Example 3]
- **Type 2**: [Name] - [Description]
  - Examples: [Example 1], [Example 2], [Example 3]
- **Type 3**: [Name] - [Description]
  - Examples: [Example 1], [Example 2], [Example 3]
- **Type 4** (Optional): [Name] - [Description]
  - Examples: [Example 1], [Example 2], [Example 3]

> [!helpful-tip] Choosing Concept Types
> - Think about the natural categories in your domain
> - 3-5 types is optimal (too few = not useful, too many = confusing)
> - Types should be mutually exclusive where possible
> - Ask: "What are the different KINDS of things I'm documenting?"

### Metadata Field Schema

Define 3-5 inline metadata fields for application notes:

1. **[FieldName1]**::`<value>`
   - **Purpose**: [What this field tracks/classifies]
   - **Format**: Controlled vocabulary OR free text OR array of links
   - **Controlled Vocabulary** (if applicable):
     - Value Option 1
     - Value Option 2
     - Value Option 3
   - **Example**: `FieldName1:: Value1`

2. **[FieldName2]**::`<value>`
   - **Purpose**: [What this field tracks/classifies]
   - **Format**: [Controlled vocabulary | Free text | Links array]
   - **Example**: `FieldName2:: [[Concept 1]], [[Concept 2]]`

3. **[FieldName3]**::`<value>`
   - **Purpose**: [What this field tracks/classifies]
   - **Format**: [Controlled vocabulary | Free text | Links array]
   - **Example**: `FieldName3:: Some descriptive text`

4. **[FieldName4]** (Optional)::`<value>`
   - **Purpose**: [Additional metadata if needed]

> [!helpful-tip] Designing Metadata Fields
> - Field 1 should be your PRIMARY classification
> - Field 2 often links to concept notes (concepts applied/used)
> - Field 3 might be context, status, or secondary classification
> - Keep it simple - you can always add more later

## Folder Architecture

```
Knowledge Domains/[Your Domain Name]/
├── 00-Concepts/              # Your concept type notes
├── 01-Applications/          # Notes that USE concepts
├── 02-Synthesis/            # Cross-concept integration
└── 03-Meta/                 # Domain config + overview MOC
```

## Status Tasks Template for Concepts

Customize this checklist for YOUR domain's documentation standards:

- [ ] [Task relevant to your domain]
- [ ] [Task relevant to your domain]
- [ ] [Task relevant to your domain]
- [ ] [Task relevant to your domain]
- [ ] [Task relevant to your domain]
- [ ] [Task relevant to your domain]

Example tasks:
- [ ] Core definition documented
- [ ] Key characteristics identified
- [ ] Usage examples provided
- [ ] Related concepts linked
- [ ] Applications documented
- [ ] Limitations/caveats noted
- [ ] References cited

## Sample Query Patterns

### Find Applications Using a Concept
```dataview
TABLE WITHOUT ID
  file.link as "📄 Note",
  [FieldName1],
  [FieldName2],
  [FieldName3]
FROM "Knowledge Domains/[Your Domain Name]/01-Applications"
FLATTEN file.outlinks as links
WHERE meta(links).path = this.file.path
GROUP BY file.link
```

### Find by Primary Classification
```dataview
LIST
FROM "Knowledge Domains/[Your Domain Name]/01-Applications"
WHERE [FieldName1] = "[Specific Value]"
```
```

---

## 2. Customization Worksheet

Before implementing your custom domain, complete this worksheet:

### Domain Identity Worksheet

```
1. DOMAIN NAME: ___________________________

2. CORE QUESTION THIS DOMAIN ANSWERS:
   ___________________________________________

3. WHAT WILL YOU DOCUMENT? (Be specific)
   - ________________________________________
   - ________________________________________
   - ________________________________________

4. HOW DOES THIS DOMAIN RELATE TO OTHERS?
   - Overlaps with: __________________________
   - Complements: ____________________________
   - Distinct from: __________________________
```

### Taxonomy Worksheet

```
5. CONCEPT TYPE 1: _____________
   What falls in this category? _______________
   Examples: _________________________________

6. CONCEPT TYPE 2: _____________
   What falls in this category? _______________
   Examples: _________________________________

7. CONCEPT TYPE 3: _____________
   What falls in this category? _______________
   Examples: _________________________________

8. (Optional) CONCEPT TYPE 4: _____________
```

### Metadata Schema Worksheet

```
9. PRIMARY CLASSIFICATION FIELD
   Name: _______________
   What it tracks: _______________
   Values: _______________

10. CONCEPTS/LINKS FIELD
    Name: _______________
    What it connects: _______________

11. CONTEXT FIELD
    Name: _______________
    What it captures: _______________

12. (Optional) ADDITIONAL FIELD
    Name: _______________
    Purpose: _______________
```

---

## 🎯 Quick Start Guide: Using These Templates

### For Cognitive Science Domain

1. **Copy all 6 files** from Template A to your vault
2. **Customize paths** in self-discovery queries if your folder structure differs
3. **Start with "Working Memory" example** - it's complete and ready to use
4. **Create 2-3 application notes** using studies you're familiar with
5. **Verify self-discovery** - check that applications appear in concept query

**Estimated Setup Time**: 45-60 minutes

### For PKM Methodology Domain

1. **Copy configuration and templates** from Template B
2. **Document methods you already use** (e.g., your current daily note system)
3. **Create workflow implementations** for your active PKM practices
4. **Link workflows to method concepts**
5. **Build health dashboard** to track coverage

**Estimated Setup Time**: 30-45 minutes

### For Prompt Engineering Domain

1. **Copy Template C configuration**
2. **Document techniques you use regularly** (few-shot, chain-of-thought, etc.)
3. **Create implementation notes** for your actual prompts
4. **Link prompts to technique concepts**
5. **Track effectiveness** through metadata

**Estimated Setup Time**: 30-40 minutes

### For Custom Domain (Template E)

1. **Complete the customization worksheet first** (15-20 min)
2. **Fill in all placeholders** in configuration template
3. **Create concept note template** with your taxonomy
4. **Create application note template** with your metadata schema
5. **Document your first concept**
6. **Create first application note**
7. **Validate self-discovery query works**

**Estimated Setup Time**: 60-90 minutes (includes planning)

---

# 🔗 Related Topics for PKB Expansion

1. **[[Domain-Specific Query Optimization]]**
   - *Connection*: Each domain may benefit from specialized Dataview patterns
   - *Depth Potential*: Advanced queries for analytics, trend detection, gap analysis
   - *Knowledge Graph Role*: Enables domain-specific insights and health monitoring

2. **[[Cross-Domain Concept Mapping]]**
   - *Connection*: Some concepts span multiple domains (e.g., "emergence" in cosmology and cognitive science)
   - *Depth Potential*: Design patterns for shared concepts, multi-domain synthesis notes
   - *Knowledge Graph Role*: Creates bridges between knowledge domains, revealing interdisciplinary insights

3. **[[Metadata Schema Evolution]]**
   - *Connection*: As domains mature, metadata needs change
   - *Depth Potential*: Versioning strategies, migration patterns, backwards compatibility
   - *Knowledge Graph Role*: Maintains system integrity during growth and refinement

4. **[[Domain Health Analytics]]**
   - *Connection*: Each domain needs monitoring for coverage, orphans, and balance
   - *Depth Potential*: Advanced dashboards, automated health checks, predictive analytics
   - *Knowledge Graph Role*: Provides meta-intelligence about knowledge development patterns
