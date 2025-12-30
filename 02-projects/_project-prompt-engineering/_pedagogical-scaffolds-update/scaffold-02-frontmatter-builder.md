# 🏷️ Frontmatter Generation Template

## Copy-Paste Base Template

```yaml
---
tags: #[domain] #[methodology] #[content-type] #[technical] #[status]
aliases: [Main Alternative, Abbreviation, Search Term]
created: {{date:YYYY-MM-DD}}
modified: {{date:YYYY-MM-DD}}
status: [seedling|budding|evergreen|wilting]
certainty: [speculative|probable|confident|verified]
type: [atomic|reference|moc|synthesis|project]
related: [[Note 1]], [[Note 2]], [[Note 3]]
---
```

---

## 5-Position Tag System

### Position 1: Primary Domain (MANDATORY)
**Purpose:** Broad knowledge category

**Common Examples:**
- `#cognitive-science` - Psychology, learning, memory, attention
- `#prompt-engineering` - LLM techniques, AI systems, optimization
- `#obsidian` - Vault management, plugins, features
- `#pkm` - Knowledge management methodology, systems
- `#software-development` - Programming, architecture, tools
- `#learning-theory` - Educational frameworks, instructional design
- `#productivity` - Time management, workflow optimization
- `#philosophy` - Ethics, epistemology, logic
- `#data-science` - Analysis, visualization, machine learning

### Position 2: Methodology/Framework (MANDATORY)
**Purpose:** Systematic approach or specific technique

**Common Examples:**
- `#zettelkasten` - Note-taking methodology
- `#react-framework` - Reasoning + Acting approach
- `#constitutional-ai` - AI safety principles
- `#dataview-query` - Obsidian plugin syntax
- `#spaced-repetition` - Learning technique
- `#moc-structure` - Maps of Content organization
- `#progressive-summarization` - Tiago Forte's method
- `#bloom-taxonomy` - Learning objectives framework
- `#agile-methodology` - Project management approach

### Position 3: Content Type (MANDATORY)
**Purpose:** Note's structural role in knowledge base

**Fixed Options:**
- `#atomic-note` - Single concept, thoroughly explained
- `#reference-note` - Comprehensive resource on topic
- `#moc` - Map of Content, navigation hub
- `#synthesis-note` - Integration of multiple concepts
- `#index-note` - Directory/catalog of related notes
- `#dashboard` - Functional workspace with queries
- `#template` - Reusable structure for note creation
- `#example-note` - Concrete illustration of concept
- `#process-note` - Step-by-step procedure documentation
- `#project-hub` - Project management coordination

### Position 4: Technical Specifics (OPTIONAL)
**Purpose:** Domain-specific technical details

**Examples by Domain:**

**Obsidian/PKM:**
- `#daily-notes`, `#periodic-notes`, `#project-hub`, `#literature-note`

**Prompt Engineering:**
- `#chain-of-thought`, `#few-shot`, `#system-prompt`, `#zero-shot`

**Cognitive Science:**
- `#working-memory`, `#cognitive-load`, `#metacognition`, `#attention`

**Plugin-Specific:**
- `#templater-script`, `#dataviewjs`, `#meta-bind-button`, `#quickadd-macro`

**Learning Theory:**
- `#spaced-repetition`, `#retrieval-practice`, `#interleaving`, `#elaboration`

### Position 5: Status/Meta (OPTIONAL)
**Purpose:** Workflow or priority indicators

**Common Options:**
- `#in-progress` - Active development
- `#needs-review` - Requires validation
- `#high-priority` - Important for current work
- `#outdated` - Needs updating
- `#to-expand` - Identified for future elaboration
- `#frequently-referenced` - High-utility note

---

## Alias Generation Rules

### Rule 1: Include Abbreviations
- "Personal Knowledge Management" → "PKM"
- "Chain of Thought" → "CoT"
- "Self-Determination Theory" → "SDT"
- "Cognitive Load Theory" → "CLT"
- "Map of Content" → "MOC"

### Rule 2: Include Alternative Phrasings
- "Knowledge Base Architecture" → "PKB Design"
- "Spaced Repetition" → "Distributed Practice"
- "Atomic Note" → "Concept Note"
- "Reference Note" → "Comprehensive Resource"
- "Wiki-Link" → "Internal Link"

### Rule 3: Include Related Search Terms
- "Cognitive Load Theory" → "CLT", "Mental Effort Theory", "Working Memory Load"
- "Zettelkasten" → "Slip Box", "Note Card System", "Luhmann Method"
- "Obsidian" → "Knowledge Graph Tool", "PKM Software", "Markdown Editor"

### Rule 4: Limit to 2-4 Aliases
**Why:** Avoids clutter, maintains focus

**Good Example:**
```yaml
aliases: [CoT Prompting, Chain of Thought, Reasoning Chain Techniques]
```

**Bad Example (Too Many):**
```yaml
aliases: [CoT, Chain of Thought, CoT Prompting, Reasoning Chains, Step-by-Step Reasoning, Sequential Thinking, Logical Reasoning Chain, Thought Process Documentation]
```

---

## Status Field Specification

**seedling** 🌱
- Initial capture, rough notes
- Basic structure established
- Core concept identified
- **Requires:** Significant development
- **Action:** Expand, refine, connect

**budding** 🌿
- Substantial content present
- Key connections identified
- Some examples and elaboration
- **Requires:** Refinement and expansion
- **Action:** Add examples, strengthen links

**evergreen** 🌳
- Comprehensive coverage
- Well-connected to knowledge graph
- Examples, evidence, elaboration complete
- **Requires:** Regular maintenance
- **Action:** Update, refine, expand as needed

**wilting** 🍂
- Content may be outdated
- Connections may have broken
- **Requires:** Revision or archival
- **Action:** Update or deprecate

---

## Certainty Field Specification

**speculative**
- Hypothesis or untested idea
- Early exploration phase
- Limited evidence or validation
- **Confidence:** Low - further investigation required

**probable**
- Some supporting evidence
- Preliminary validation present
- Reasonable confidence level
- **Confidence:** Moderate - likely true but not certain

**confident**
- Strong evidence from multiple sources
- Well-established in literature
- High reliability for practical use
- **Confidence:** High - very likely true

**verified**
- Empirically validated
- Authoritative consensus
- Established fact or proven principle
- **Confidence:** Maximum - known to be true

---

## Type Field Specification

**Match this to Position 3 tag:**

- `type: atomic` → `#atomic-note`
- `type: reference` → `#reference-note`
- `type: moc` → `#moc`
- `type: synthesis` → `#synthesis-note`
- `type: index` → `#index-note`
- `type: dashboard` → `#dashboard`
- `type: template` → `#template`
- `type: example` → `#example-note`
- `type: process` → `#process-note`
- `type: project` → `#project-hub`

---

## Related Field Best Practices

**Purpose:** Explicit cross-referencing for knowledge graph strengthening

**Guidelines:**
1. Include 3-5 most relevant notes
2. Prioritize bi-directional relationships
3. Include both prerequisite and extension notes
4. Update when new connections discovered

**Example:**
```yaml
related: [[Cognitive Load Theory]], [[Working Memory]], [[Schema Theory]], [[Instructional Design]]
```

**Why These?**
- [[Cognitive Load Theory]] - Theoretical foundation
- [[Working Memory]] - Prerequisite concept
- [[Schema Theory]] - Related framework
- [[Instructional Design]] - Application domain

---

## Complete Examples

### Example 1: Atomic Note on "Spaced Repetition"

```yaml
---
tags: #learning-theory #evidence-based-practice #atomic-note #cognitive-science #memory
aliases: [Distributed Practice, Spacing Effect, Spaced Review]
created: 2025-01-15
modified: 2025-01-15
status: evergreen
certainty: verified
type: atomic
related: [[Ebbinghaus Forgetting Curve]], [[Retrieval Practice]], [[Cognitive Load Theory]]
---
```

### Example 2: Reference Note on "Dataview Plugin"

```yaml
---
tags: #obsidian #dataview-query #reference-note #plugin-ecosystem #automation
aliases: [Dataview, DQL, Dataview Query Language, Dynamic Queries]
created: 2025-01-10
modified: 2025-01-15
status: evergreen
certainty: confident
type: reference
related: [[Obsidian Plugins MOC]], [[DataviewJS]], [[Inline Fields]], [[Query Syntax]]
source: https://blacksmithgu.github.io/obsidian-dataview/
---
```

### Example 3: MOC for "Prompt Engineering"

```yaml
---
tags: #prompt-engineering #moc #llm-optimization
aliases: [Prompt Engineering Map, LLM Techniques Hub, Prompting Methods Index]
created: 2025-01-01
modified: 2025-01-15
status: evergreen
type: moc
related: [[Cognitive Science MOC]], [[AI Development MOC]], [[Learning Theory MOC]]
---
```

### Example 4: Synthesis Note on "CLT × PKM"

```yaml
---
tags: #cognitive-science #pkm #synthesis-note #learning-theory #knowledge-management
aliases: [Cognitive Load in PKM, CLT Application to Knowledge Systems, Mental Load in Note-Taking]
created: 2025-01-12
modified: 2025-01-15
status: budding
certainty: confident
type: synthesis
related: [[Cognitive Load Theory]], [[Personal Knowledge Management]], [[Information Architecture]], [[Zettelkasten]]
---
```

---

## Common Mistakes to Avoid

**❌ Too Many Tags**
```yaml
tags: #cognitive-science #learning-theory #memory #attention #metacognition #psychology #neuroscience #education #instructional-design #pedagogy #andragogy
```
**Why Bad:** Overwhelming, reduces discoverability, no clear primary focus
**Better:** Limit to 3-5 tags, with clear primary domain

**❌ Vague Tags**
```yaml
tags: #important #interesting #to-review #notes
```
**Why Bad:** No semantic meaning, doesn't support discovery or organization
**Better:** Use specific domain tags and content type tags

**❌ Inconsistent Naming**
```yaml
tags: #CognitiveScience #Learning_Theory #atomic-note
```
**Why Bad:** Mixed conventions (PascalCase, snake_case, kebab-case)
**Better:** Always use lowercase, hyphenated format: `#cognitive-science`

**❌ Redundant Aliases**
```yaml
aliases: [Spaced Repetition, Spaced Repetition Technique, Spaced Repetition Method, Spaced Repetition Practice]
```
**Why Bad:** All essentially the same, clutters search
**Better:** Genuinely distinct alternatives: [Spaced Repetition, Distributed Practice, Spacing Effect]

**❌ Wrong Status**
```yaml
status: evergreen
# But content has "TODO: Add examples section" and "PLACEHOLDER - needs research"
```
**Why Bad:** Status doesn't match actual state
**Better:** Status should be `seedling` or `budding` until complete

---

**Token Count:** ~400 tokens
**Use Case:** Inject immediately after note type selection
**Next Scaffold:** Wiki-Link Density Guide or Callout Semantic Selector
