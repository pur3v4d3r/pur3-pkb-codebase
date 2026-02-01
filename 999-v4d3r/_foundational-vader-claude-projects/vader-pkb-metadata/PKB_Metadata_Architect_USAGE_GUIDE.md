# PKB Metadata Architect - Usage Guide & Examples

## Quick Start

### Basic Usage Pattern

1. **Upload a file** to Claude (markdown, text, PDF, etc.)
2. **Simple request**: "Generate frontmatter for this file"
3. **Receive**: Complete YAML frontmatter ready to paste into your note

### Advanced Usage

**Customize the output:**
- "Generate frontmatter using my custom tag structure: projects/[name]"
- "Add Dataview fields for tracking progress"
- "Include spaced repetition metadata"
- "Use my company's classification system"

---

## Example 1: Academic Paper Notes

### Input File Content

```markdown
# Attention Is All You Need - Paper Notes

This paper introduces the Transformer architecture, a novel neural network
architecture based solely on attention mechanisms, dispensing with recurrence
and convolutions entirely.

Key innovations:
- Multi-head attention
- Positional encoding
- Encoder-decoder structure
- Parallelizable training

The model achieves SOTA on WMT 2014 English-to-German and English-to-French
translation tasks.

Authors: Vaswani et al. (2017)
Published: NeurIPS 2017
```

### User Request
"Generate frontmatter for this paper note"

### Output Generated

```yaml
---
title: Vaswani et al - Attention Is All You Need (2017)
aliases:
  - Attention Is All You Need
  - Transformer Paper
  - Vaswani 2017
  - AIAYN
  - Original Transformer Architecture
type: literature-note
status: complete
confidence: high

tags:
  - literature-note
  - source/paper
  - ai/deep-learning/transformers
  - ai/nlp/machine-translation
  - paper/neurips
  - foundational-paper

# Source Information
source-type: paper
author: Vaswani et al.
year: 2017
publisher: NeurIPS
venue: NeurIPS 2017
doi: [Add if available]
url: https://arxiv.org/abs/1706.03762

# Reading Metadata
read-date: 2024-02-01
rating: 10/10
pages: 15
significance: foundational

# Content
domain: artificial-intelligence
subfield: deep-learning
key-concepts:
  - Transformer Architecture
  - Multi-Head Attention
  - Self-Attention Mechanism
  - Positional Encoding
  - Encoder-Decoder Architecture

key-findings:
  - First sequence transduction model relying entirely on attention
  - Achieves SOTA on translation tasks
  - More parallelizable than RNNs
  - Superior quality with less training time

# Relationships
created: 2024-02-01
updated: 2024-02-01

related:
  - "[[Attention Mechanism]]"
  - "[[Self-Attention]]"
  - "[[Neural Machine Translation]]"
  - "[[Sequence-to-Sequence Models]]"

influenced:
  - "[[BERT Architecture]]"
  - "[[GPT Models]]"
  - "[[Vision Transformers]]"
  - "[[Modern LLM Architectures]]"

prerequisites:
  - "[[Neural Network Fundamentals]]"
  - "[[Recurrent Neural Networks]]"
  - "[[Seq2Seq Models]]"

see-also:
  - "[[Transformer Implementation Notes]]"
  - "[[Attention Mechanisms Survey]]"
---
```

### Explanation Provided

"I've generated comprehensive frontmatter for this foundational AI paper. Key decisions:

- **Type**: Literature note (paper summary)
- **Status**: Complete (full paper coverage)
- **Significance**: Marked as foundational (highly influential)
- **Relationships**: Extensive mapping showing prerequisites (what to learn first), related concepts, and papers influenced by this work
- **Key Concepts**: Extracted the 5 main innovations
- **Tags**: Multi-dimensional (source type, domain hierarchy, significance)

This frontmatter enables Dataview queries like:
```
TABLE rating, year, significance
WHERE source-type = "paper" AND contains(tags, "foundational-paper")
```"

---

## Example 2: Personal Project Note

### Input File Content

```markdown
# Website Redesign Project

Starting redesign of company website. Goals:
- Improve mobile experience
- Modernize design
- Better SEO
- Faster load times

Team: Sarah (design), Mike (frontend), Me (PM)
Deadline: Q2 2024
Budget: $50k

Current phase: Planning
```

### User Request
"Generate project frontmatter with GTD fields"

### Output Generated

```yaml
---
title: Website Redesign Project
aliases:
  - Website Redesign
  - Company Site Redesign
  - Q2 Website Project
type: project-note
status: active

tags:
  - project
  - project/website-redesign
  - work/web-development
  - quarter/2024-q2
  - status/planning

# Project Metadata
project: website-redesign
project-status: planning
priority: high
start-date: 2024-02-01
deadline: 2024-06-30
budget: 50000
currency: USD

# Team
role: project-manager
team:
  - name: Sarah
    role: designer
  - name: Mike
    role: frontend-developer
stakeholders:
  - Engineering Team
  - Marketing Team

# Goals
goals:
  - Improve mobile experience
  - Modernize design
  - Better SEO
  - Faster load times

# GTD Fields
context: "@work"
energy: high
next-action: Finalize wireframes with Sarah
waiting-for: Budget approval from finance

# Deliverables
deliverables:
  - Mobile-responsive design
  - New design system
  - SEO optimization
  - Performance improvements

# Tracking
created: 2024-02-01
updated: 2024-02-01
progress: 15
estimated-completion: 2024-06-30

# Relationships
related:
  - "[[Design System Documentation]]"
  - "[[SEO Strategy]]"
  - "[[Frontend Architecture]]"

resources:
  - "[[Project Budget Tracker]]"
  - "[[Team Capacity Planning]]"
---
```

### Explanation

"I've generated project-focused frontmatter with GTD integration. Key features:

- **GTD Fields**: context, energy, next-action, waiting-for enable task management
- **Team Structure**: Captures roles and stakeholders
- **Progress Tracking**: Numeric progress field for Dataview charts
- **Timeline**: Start, deadline, and estimated completion
- **Tags**: Hierarchical project tagging (project/website-redesign) plus temporal (quarter/2024-q2)

This enables GTD queries like:
```
TASK
WHERE context = "@work" AND status = "active"
SORT BY priority DESC
```"

---

## Example 3: Learning/Concept Note

### Input File Content

```markdown
# Working Memory and Cognitive Load

Working memory is the cognitive system responsible for temporarily holding
and manipulating information during complex tasks.

Capacity: Limited to about 7±2 items (Miller's Law)

Components (Baddeley's Model):
- Central Executive
- Phonological Loop  
- Visuospatial Sketchpad
- Episodic Buffer

Implications for learning:
- Reduce extraneous cognitive load
- Chunk information
- Use worked examples
- Minimize split attention
```

### User Request
"Generate frontmatter with spaced repetition fields"

### Output Generated

```yaml
---
title: Working Memory and Cognitive Load Theory
aliases:
  - Working Memory
  - WM and Cognitive Load
  - Miller's Law
  - 7±2 Rule
  - Baddeley's Model
type: permanent-note
status: evergreen
confidence: high

tags:
  - permanent-note
  - cognitive-science/memory
  - cognitive-science/learning
  - psychology/cognitive
  - learning-theory
  - instructional-design

# Learning Metadata
domain: cognitive-science
subdomain: memory-systems
difficulty: intermediate
learning-stage: practice
mastery-level: 75

# Spaced Repetition
sr-due: 2024-02-15
sr-interval: 14
sr-ease: 250
last-reviewed: 2024-02-01
next-review: 2024-02-15
review-count: 3

# Key Concepts
key-concepts:
  - Working Memory Capacity
  - Miller's Law (7±2)
  - Baddeley's Model
  - Cognitive Load Types
  - Central Executive
  - Phonological Loop
  - Visuospatial Sketchpad

# Quiz Questions (for review)
quiz-questions:
  - "What is the typical capacity of working memory?"
  - "Name the four components of Baddeley's working memory model"
  - "How does cognitive load theory apply to instructional design?"

# Temporal
created: 2024-02-01
updated: 2024-02-01

# Relationships
related:
  - "[[Cognitive Load Theory]]"
  - "[[Long-Term Memory]]"
  - "[[Attention and Focus]]"
  - "[[Chunking Strategy]]"

prerequisites:
  - "[[Memory Systems Overview]]"
  - "[[Cognitive Psychology Fundamentals]]"

applications:
  - "[[Instructional Design Principles]]"
  - "[[Learning Strategy Development]]"
  - "[[Interface Design Guidelines]]"

see-also:
  - "[[Worked Example Effect]]"
  - "[[Split Attention Effect]]"
  - "[[Expertise Reversal Effect]]"

# Empirical Foundation
based-on:
  - "[[Miller - Magical Number Seven (1956)]]"
  - "[[Baddeley - Working Memory Model (1974)]]"
  - "[[Sweller - Cognitive Load Theory (1988)]]"
---
```

### Explanation

"I've created learning-optimized frontmatter with spaced repetition integration:

- **SR Fields**: Due dates, intervals, ease ratings for Anki-style review
- **Mastery Tracking**: Numeric mastery level (0-100) for progress visualization
- **Quiz Questions**: Built-in questions for self-testing
- **Learning Stage**: Tracks progression through learning phases
- **Prerequisites**: Clear learning dependencies
- **Empirical Foundation**: Links to original research

This enables learning-focused queries:
```
TABLE mastery-level, next-review, difficulty
WHERE learning-stage = "practice"
SORT BY next-review ASC
```"

---

## Example 4: Code/Technical Reference

### Input File Content

```python
# React useEffect Hook Patterns

## Basic Usage
useEffect(() => {
  // Side effect code
  return () => {
    // Cleanup
  };
}, [dependencies]);

## Common Patterns

1. Data Fetching
2. Event Listeners
3. Timers/Intervals
4. Subscriptions

Dependencies array controls when effect runs.
Empty array [] = run once on mount.
No array = run after every render.
```

### User Request
"Generate technical reference frontmatter"

### Output Generated

```yaml
---
title: React useEffect Hook - Patterns and Best Practices
aliases:
  - useEffect Hook
  - React Side Effects
  - useEffect Patterns
  - Effect Hook
type: reference-note
status: evergreen

tags:
  - reference
  - technical/react
  - code/react-hooks
  - javascript/react
  - web-development/frontend
  - pattern-library

# Technical Details
language: javascript
framework: react
framework-version: "18.x"
hook-type: effect-hook
complexity: intermediate
tested: true

# Context
domain: software-engineering
subdomain: frontend-development
use-cases:
  - data-fetching
  - event-listeners
  - subscriptions
  - timers-intervals

# Code Metadata
code-type: hook-pattern
api-stability: stable
deprecation-status: current
alternative-patterns:
  - "[[React useLayoutEffect]]"
  - "[[React useMemo]]"
  - "[[React useCallback]]"

# Learning Resources
difficulty: intermediate
prerequisites:
  - "[[JavaScript Closures]]"
  - "[[React Component Lifecycle]]"
  - "[[React Hooks Basics]]"

# Temporal
created: 2024-02-01
updated: 2024-02-01

# Relationships
related:
  - "[[React Component Lifecycle]]"
  - "[[React Hooks Overview]]"
  - "[[Side Effects in React]]"
  - "[[Dependency Array Patterns]]"

part-of:
  - "[[React Hooks Reference]]"
  - "[[React Best Practices]]"

see-also:
  - "[[React Official Docs - useEffect]]"
  - "[[Common useEffect Mistakes]]"
  - "[[Effect Cleanup Patterns]]"

# Common Issues
common-pitfalls:
  - Infinite render loops
  - Missing dependencies
  - Incorrect cleanup
  - Stale closures
---
```

### Explanation

"Technical reference frontmatter with code-specific metadata:

- **Framework Versioning**: Tracks React version compatibility
- **API Stability**: Indicates if pattern is current/deprecated
- **Common Pitfalls**: Documents known issues
- **Use Cases**: Lists practical applications
- **Alternative Patterns**: Related hooks/approaches
- **Testing Status**: Indicates code has been verified

Enables technical queries:
```
TABLE language, framework-version, tested
WHERE code-type = "hook-pattern" AND framework = "react"
```"

---

## Example 5: Meeting Notes

### Input File Content

```markdown
# Weekly Team Sync - Feb 1, 2024

Attendees: Alice, Bob, Carol, Dan
Duration: 30 mins

Topics:
- Sprint review
- Blocker: Database migration
- New feature requests

Decisions:
- Postpone migration to next sprint
- Prioritize feature X over Y

Action items:
- Alice: Draft feature spec by Friday
- Bob: Research migration tools
```

### User Request
"Generate meeting note frontmatter with GTD fields"

### Output Generated

```yaml
---
title: 2024-02-01 - Weekly Team Sync
aliases:
  - Feb 1 Team Meeting
  - Weekly Sync Feb 1
type: meeting-note
date: 2024-02-01

tags:
  - meeting
  - meeting/team-sync
  - work/engineering
  - year/2024
  - month/2024-02

# Meeting Metadata
meeting-type: team-sync
recurring: true
recurrence: weekly
duration: 30
duration-unit: minutes

# Participants
attendees:
  - Alice
  - Bob
  - Carol
  - Dan
organizer: Alice
required: true

# Content
topics:
  - Sprint Review
  - Database Migration Blocker
  - New Feature Requests

decisions:
  - Postpone database migration to next sprint
  - Prioritize feature X over feature Y

# Action Items (GTD)
actions:
  - task: Draft feature spec
    owner: Alice
    due: 2024-02-05
    status: todo
    context: "@work"
  - task: Research migration tools
    owner: Bob
    due: 2024-02-08
    status: todo
    context: "@computer"

# Tracking
created: 2024-02-01
updated: 2024-02-01
next-meeting: 2024-02-08

# Relationships
related:
  - "[[Sprint Planning Notes]]"
  - "[[Database Migration Project]]"
  - "[[Feature Request Log]]"

previous-meeting: "[[2024-01-25 - Weekly Team Sync]]"
next-meeting-note: "[[2024-02-08 - Weekly Team Sync]]"

# Follow-up
follow-up-required: true
follow-up-date: 2024-02-08
blockers:
  - Database migration complexity
---
```

### Explanation

"Meeting-specific frontmatter with action tracking:

- **Attendee List**: Queryable participant data
- **Action Items**: Structured tasks with owners, due dates, GTD contexts
- **Decisions**: Documented for future reference
- **Meeting Chain**: Links to previous/next meetings
- **Follow-up**: Tracks what needs revisiting

Enables meeting queries:
```
TABLE attendees, actions, follow-up-required
WHERE meeting-type = "team-sync" AND follow-up-date < date(today)
```"

---

## Customization Examples

### Custom Tag Structure

**User**: "Use my company's tag structure: dept/[team], project/[name], priority/[level]"

```yaml
tags:
  - dept/engineering
  - project/website-redesign
  - priority/high
```

### Custom Fields

**User**: "Always include: budget-code, approver, compliance-required for project notes"

```yaml
# Custom Corporate Fields
budget-code: ENG-2024-Q2-001
approver: Director of Engineering
compliance-required: true
compliance-type: SOC2
```

### Domain-Specific Taxonomy

**User**: "For research notes, use: hypothesis, methodology, findings, limitations"

```yaml
# Research-Specific Fields
hypothesis: "Increased batch size improves model convergence"
methodology: controlled-experiment
findings: "Batch size 128 optimal for this dataset"
limitations:
  - Limited to single GPU
  - Small dataset size
confidence-interval: 95%
statistical-significance: p < 0.01
```

---

## Power User Tips

### 1. Dataview Integration

Request frontmatter optimized for specific Dataview queries:

**Request**: "Generate frontmatter that enables this query: `TABLE status, progress WHERE type = 'project'`"

### 2. Template Variables

Ask for Templater-compatible frontmatter:

**Request**: "Use Templater syntax for dynamic fields"

```yaml
created: 2026-02-01
title: PKB_Metadata_Architect_USAGE_GUIDE
```

### 3. Bulk Consistency

Generate multiple related frontmatters:

**Request**: "Generate frontmatter for all my project notes using consistent structure"

### 4. Migration Support

Convert existing metadata formats:

**Request**: "Convert this old frontmatter to my new structure"

### 5. Graph Optimization

Request graph-aware metadata:

**Request**: "Add fields that enhance graph view connections"

```yaml
graph-color: "#4A90E2"
centrality: hub
connection-strength: strong
```

---

## Common Workflows

### Workflow 1: New Note Creation

1. Write note content
2. Upload to Claude: "Generate frontmatter"
3. Copy YAML block
4. Paste at top of note
5. Done!

### Workflow 2: Existing Note Enhancement

1. Upload existing note
2. "Enhance frontmatter with relationships and tags"
3. Review suggestions
4. Update note

### Workflow 3: Batch Processing

1. "Generate template frontmatter for project notes"
2. Receive template
3. Adapt template for each note
4. Maintain consistency

### Workflow 4: Custom Taxonomy Setup

1. "Here's my custom classification system: [details]"
2. "Generate example frontmatter using this system"
3. Review and refine
4. Use as template going forward

---

## Troubleshooting

### Issue: Tags too generic

**Solution**: Request more specific, hierarchical tags
"Make tags more specific using domain/subdomain/topic structure"

### Issue: Too many relationships

**Solution**: Request focused relationships
"Only include top 5 most important relationships"

### Issue: Wrong note type classification

**Solution**: Specify the type explicitly
"This is a reference note, not a permanent note"

### Issue: Missing domain-specific fields

**Solution**: Describe your domain requirements
"This is for medical research, include: patient-count, study-design, IRB-approval"

---

## Advanced Patterns

### Pattern 1: Progressive Enhancement

Start minimal, add complexity as needed:

1. Basic frontmatter first
2. Add relationships after vault grows
3. Add custom fields for specific workflows
4. Add automation fields (Templater/Dataview) when ready

### Pattern 2: Vault-Wide Standards

Establish vault-wide conventions:

"For all permanent notes, always include: status, confidence, prerequisites, related"

### Pattern 3: Context-Aware Generation

Provide vault context:

"Here are my existing tags: [list]. Use only these or suggest new ones that fit the taxonomy."

### Pattern 4: Integration-First Design

Design for specific tools:

"Generate frontmatter optimized for Obsidian Dataview, Charts plugin, and Timeline view"

---

## Best Practices

1. **Start Simple**: Basic frontmatter first, enhance later
2. **Be Consistent**: Use same structure for similar note types
3. **Enable Queries**: Think about what questions you'll ask your vault
4. **Maintain Relationships**: Keep related/prerequisites updated
5. **Review Periodically**: Update status and maturity as notes evolve
6. **Document Taxonomy**: Keep a note explaining your tag/field conventions
7. **Validate YAML**: Always check generated frontmatter is valid
8. **Customize Gradually**: Add custom fields as specific needs emerge

---

## Getting Help

### For Better Results:

**Provide Context**:
- "This is for my [work/personal/research] vault"
- "I use [Dataview/Templater/other plugins]"
- "My taxonomy is [describe structure]"

**Be Specific**:
- "I need these exact fields: [list]"
- "Use this tag format: [example]"
- "Don't include: [fields to omit]"

**Show Examples**:
- "Here's my existing frontmatter for similar notes: [paste]"
- "Match this style: [example]"

### Request Explanation:

"Explain why you chose these tags/relationships/classifications"

### Request Alternatives:

"Show me 2 different frontmatter approaches for this note type"

---

This system is designed to be flexible and adapt to your specific PKB needs. Start with the defaults and customize as your requirements become clear.
