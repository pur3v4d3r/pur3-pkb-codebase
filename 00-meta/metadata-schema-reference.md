---
tags: #spes #reference #metadata #schema
aliases: [Metadata Schema, Field Reference, YAML Guide]
status: reference
certainty: ^verified
priority: high
created: 2025-12-20
project: prompt-engineering-templater-system
link-up: "[[00-prompt-engineering-system-design]]"
---

# Metadata Schema Reference

> [!abstract] Purpose
> Complete reference for all metadata fields used in the prompt engineering system. Use this as the authoritative source for field names, types, and controlled vocabularies.

---

## 📊 UNIVERSAL FIELDS (All Types)

These fields appear in ALL notes (prompts, components, workflows, tests).

### Core Identity
```yaml
type: string [REQUIRED]
  # Prompt types: "prompt" | "component" | "workflow" | "test-result"

id: string [REQUIRED]
  # Unique identifier
  # Format: YYYYMMDDHHmmss (timestamp-based)
  # Generated: tp.date.now("YYYYMMDDHHmmss")

status: string [REQUIRED]
  # Options: "active" | "testing" | "production" | "deprecated" | "archived"
  # Default: "active"

version: string [REQUIRED]
  # Semantic versioning: "MAJOR.MINOR.PATCH"
  # Default: "1.0.0"
  # Bump: MAJOR (breaking), MINOR (feature), PATCH (fix)
```

### Quality Metrics
```yaml
rating: float [REQUIRED]
  # User quality assessment
  # Range: 0.0-10.0
  # Default: "0.0"
  # Update: After testing or usage

confidence: string [REQUIRED]
  # Epistemic certainty
  # Options: "speculative" | "provisional" | "moderate" | "established" | "high"
  # Default: "speculative" (new prompts)

maturity: string [REQUIRED]
  # Development stage
  # Options: "seedling" | "developing" | "budding" | "evergreen"
  # Default: "seedling"
  # Progression: seedling → developing → budding → evergreen

priority: string [OPTIONAL]
  # Work priority
  # Options: "low" | "medium" | "high" | "urgent"
  # Default: "medium"
```

### Source & Attribution
```yaml
source: string [REQUIRED]
  # Origin of content
  # Options: "claude-sonnet-4.5" | "claude-opus-4.5" | "gemini-3.0-pro" |
  #          "gemini-3.0-flash" | "original" | "local-llm" | "other"
  # Use: Track which model generated/refined the prompt
```

### Temporal Fields
```yaml
created: date [REQUIRED]
  # Creation date
  # Format: YYYY-MM-DD
  # Generated: tp.date.now("YYYY-MM-DD")

modified: date [REQUIRED]
  # Last modification date
  # Format: YYYY-MM-DD
  # Update: On every edit
```

### Usage Tracking
```yaml
usage-count: integer [REQUIRED]
  # Number of times used in production
  # Default: 0
  # Increment: Via macro or manually

last-used: string [OPTIONAL]
  # Link to daily note when last used
  # Format: "[[YYYY-MM-DD]]" or empty string ""
  # Update: When prompt is deployed
```

### Review System (Spaced Repetition)
```yaml
review-next: date [OPTIONAL]
  # Next review date
  # Format: YYYY-MM-DD
  # Calculate: Based on maturity level
  #   seedling: +7 days
  #   developing: +14 days
  #   budding: +30 days
  #   evergreen: +90 days

review-interval: integer [OPTIONAL]
  # Days between reviews
  # Default: 7
  # Adjust: Based on usage frequency and maturity

review-count: integer [OPTIONAL]
  # Number of reviews completed
  # Default: 0
  # Increment: Each review session
```

### Categorization
```yaml
tags: array [REQUIRED]
  # Hierarchical tags
  # Required tags:
  #   - "year/YYYY" (always include current year)
  #   - "prompt-engineering" (umbrella category)
  # Common tags:
  #   - "llm-capability/generation|reasoning|analysis|creative"
  #   - "prompt-workflow/creation|testing|deployment|optimization"
  #   - "component-type/persona|instruction|constraint|format|context"
  #   - "domain/general|technical|creative|educational|pkb"
  #   - "advanced-prompting/chain-of-thought|few-shot|tree-of-thoughts"

aliases: array [OPTIONAL]
  # Alternative names
  # Include: Filename, common abbreviations, synonyms
  # Default: [filename]
```

### Graph Integration
```yaml
link-up: string [OPTIONAL]
  # Parent MOC (Map of Content)
  # Format: "[[moc-name]]"
  # Default: "[[prompt-engineering-moc]]"

link-related: array [OPTIONAL]
  # Related notes
  # Suggested: ["[[YYYY-MM-DD|Daily Note]]", "[[YYYY-WW|Weekly Review]]"]
  # Add: Links to related prompts, projects, resources
```

### Sample YAML

```YAML
---
type:
id:
status:
version:
rating:
confidence:
maturity:
source:
created:
modified:
usage-count:
tags:
aliases:
link-up:
link-related:
---

```

---

## 🎯 PROMPT-SPECIFIC FIELDS

Additional fields for `type: "prompt"` notes.

```yaml
components-used: array [OPTIONAL]
  # Links to component library items
  # Format: ["[[component-1]]", "[[component-2]]"]
  # Purpose: Track component reuse, enable analytics
  # Update: When inserting components

test-results: array [OPTIONAL]
  # Links to test result notes
  # Format: ["[[test-result-1]]", "[[test-result-2]]"]
  # Purpose: Track testing history
  # Update: After each test
```

---

## 🧩 COMPONENT-SPECIFIC FIELDS

Additional fields for `type: "component"` notes.

```yaml
component-type: string [REQUIRED]
  # Component category
  # Options: "persona" | "instruction" | "constraint" | "format" |
  #          "context" | "example"
  # Use: Organize library, filter searches

atomic-composite: string [REQUIRED]
  # Component complexity
  # Options: "atomic" | "composite"
  # atomic: Single-purpose, indivisible
  # composite: Combines multiple atomics

domain: string [REQUIRED]
  # Application domain
  # Options: "general" | "technical" | "creative" | "educational" | "pkb"
  # Use: Domain-specific filtering

performance-score: float [OPTIONAL]
  # Average quality across uses
  # Range: 0.0-10.0
  # Calculate: Average of ratings from used-in-prompts
  # Default: "0.0"

conflicts-with: array [OPTIONAL]
  # Components that shouldn't be used together
  # Format: ["[[conflicting-component]]"]
  # Example: Different personas, contradictory constraints

synergies-with: array [OPTIONAL]
  # Components that work well together
  # Format: ["[[synergistic-component]]"]
  # Use: Recommend combos

used-in-prompts: array [OPTIONAL]
  # Links to prompts using this component
  # Format: ["[[prompt-1]]", "[[prompt-2]]"]
  # Update: Via macro or manually
  # Use: Usage analytics
```

---

## 🔗 WORKFLOW-SPECIFIC FIELDS

Additional fields for `type: "workflow"` notes.

```yaml
workflow-type: string [OPTIONAL]
  # Workflow category
  # Options: "sequential" | "parallel" | "recursive" | "hybrid"

problem-types: array [OPTIONAL]
  # Problems this workflow addresses
  # Format: ["long-form-generation", "technical-analysis", "comparison"]

typical-turns: integer [OPTIONAL]
  # Average number of turns/steps
  # Range: 1-20+

context-strategy: string [OPTIONAL]
  # How context is managed across turns
  # Options: "strict-isolation" | "sequential-building" | "parallel-convergence"
```

---

## 🧪 TEST-RESULT-SPECIFIC FIELDS

Additional fields for `type: "test-result"` notes.

```yaml
prompt-tested: string [REQUIRED]
  # Link to prompt being tested
  # Format: "[[prompt-name]]"

test-date: date [REQUIRED]
  # When test was conducted
  # Format: YYYY-MM-DD

test-type: string [REQUIRED]
  # Type of test
  # Options: "functional" | "quality" | "performance" | "ab-comparison"

success: boolean [REQUIRED]
  # Did prompt meet objectives?
  # Options: true | false

quality-score: float [OPTIONAL]
  # Numeric quality assessment
  # Range: 0.0-10.0

issues-found: array [OPTIONAL]
  # List of problems identified
  # Format: ["Issue 1 description", "Issue 2 description"]

recommendations: array [OPTIONAL]
  # Suggested improvements
  # Format: ["Recommendation 1", "Recommendation 2"]
```

---

## 📋 CONTROLLED VOCABULARIES

### Status Values
- **active**: Currently in use, maintained
- **testing**: Under evaluation, not production-ready
- **production**: Proven, deployed, stable
- **deprecated**: Replaced, no longer recommended
- **archived**: Historical, no longer maintained

### Confidence Values
- **speculative**: Unproven, experimental
- **provisional**: Some testing, preliminary results
- **moderate**: Tested multiple times, generally reliable
- **established**: Extensively tested, consistently good
- **high**: Proven excellent, gold standard

### Maturity Values
- **seedling**: New, unrefined, needs development
- **developing**: Growing, improving, getting tested
- **budding**: Solid foundation, minor refinements needed
- **evergreen**: Mature, stable, proven over time

### Priority Values
- **low**: Nice to have, no urgency
- **medium**: Standard work priority
- **high**: Important, needs attention soon
- **urgent**: Critical, address immediately

### Source Values
- **claude-sonnet-4.5**: Claude Sonnet 4.5 generated
- **claude-opus-4.5**: Claude Opus 4.5 generated
- **gemini-3.0-pro**: Gemini 3.0 Pro generated
- **gemini-3.0-flash**: Gemini 3.0 Flash generated
- **original**: User-created (Pur3v4d3r)
- **local-llm**: Local model generated
- **other**: Other source

### Component Types
- **persona**: Role/identity frames
- **instruction**: Task directives
- **constraint**: Boundaries/restrictions
- **format**: Output templates
- **context**: Background/framing
- **example**: Few-shot demonstrations

### Domains
- **general**: Universal, any domain
- **technical**: Code, engineering, analysis
- **creative**: Writing, ideation, art
- **educational**: Teaching, explanation, tutoring
- **pkb**: PKB/knowledge management specific

---

## ✅ VALIDATION RULES

### Required Field Checks
```javascript
// Fields that MUST be present
const required = ["type", "id", "status", "version", "rating",
                  "source", "created", "modified", "confidence",
                  "maturity", "tags"];

// Type-specific requirements
if (type === "component") {
  required.push("component-type", "atomic-composite", "domain");
}
if (type === "test-result") {
  required.push("prompt-tested", "test-date", "test-type", "success");
}
```

### Format Validation
```javascript
// ID format: 14 digits (YYYYMMDDHHmmss)
const validID = /^\d{14}$/.test(id);

// Version format: semver (X.Y.Z)
const validVersion = /^\d+\.\d+\.\d+$/.test(version);

// Date format: YYYY-MM-DD
const validDate = /^\d{4}-\d{2}-\d{2}$/.test(created);

// Rating range: 0.0-10.0
const validRating = rating >= 0 && rating <= 10;
```

### Tag Requirements
```javascript
// Must have year tag
const hasYearTag = tags.some(t => t.startsWith("year/"));

// Must have prompt-engineering umbrella
const hasPETag = tags.includes("prompt-engineering");
```

---

## 📊 META-BIND EXAMPLES

### View Fields (Read-Only)
```markdown
**Type**: `VIEW[{type}]`
**Status**: `VIEW[{status}]`
**Version**: `VIEW[{version}]`
**Rating**: `VIEW[{rating}]`/10
**Usage Count**: `VIEW[{usage-count}]`
```

### Input Fields (Editable)
```markdown
**Rating**: `INPUT[slider(min(0), max(10), step(0.5)):rating]`
**Priority**: `INPUT[suggester(option(Low), option(Medium), option(High), option(Urgent)):priority]`
**Status**: `INPUT[suggester(option(Active), option(Testing), option(Production)):status]`
**Tested**: `INPUT[toggle:is-tested]`
```

---

## 🔍 DATAVIEW QUERY PATTERNS

### All Prompts by Rating
```dataview
TABLE status, rating, maturity, usage-count
FROM ""
WHERE type = "prompt"
SORT rating DESC, usage-count DESC
```

### Components by Usage
```dataview
TABLE component-type, domain, usage-count, performance-score
FROM ""
WHERE type = "component"
SORT usage-count DESC
```

### Prompts Needing Review
```dataview
TABLE review-next, maturity, last-used
FROM ""
WHERE type = "prompt" AND review-next <= date(today)
SORT review-next ASC
```

### Recent Test Results
```dataview
TABLE prompt-tested, test-type, success, quality-score
FROM ""
WHERE type = "test-result"
SORT test-date DESC
LIMIT 10
```

---

## 📝 USAGE NOTES

### When Creating New Prompts
1. Use master template (auto-populates most fields)
2. Answer guided questions (suggesters ensure controlled vocabulary)
3. Required fields are marked [REQUIRED] in this doc
4. Optional fields can be added as needed
5. Update `modified` date on every edit

### When Creating Components
1. Use component template
2. Must specify: component-type, atomic-composite, domain
3. Document conflicts and synergies as discovered
4. Track usage via `used-in-prompts` array

### When Updating Metadata
1. Bump `version` for significant changes
2. Update `modified` date
3. Adjust `maturity` as prompt evolves
4. Increment `usage-count` when deploying
5. Update `last-used` with daily note link
6. Recalculate `review-next` based on new maturity

---

## ✅ COMPLIANCE CHECKLIST

Before considering a note "production-ready":

- [ ] All required fields present
- [ ] ID format correct (14 digits)
- [ ] Version format correct (semver)
- [ ] Dates in YYYY-MM-DD format
- [ ] Rating between 0.0-10.0
- [ ] Status from controlled vocabulary
- [ ] Confidence from controlled vocabulary
- [ ] Maturity from controlled vocabulary
- [ ] Source from controlled vocabulary
- [ ] Tags include "year/YYYY"
- [ ] Tags include "prompt-engineering"
- [ ] Aliases include filename
- [ ] Type-specific fields present (if applicable)

---

*Schema Version: 1.0.0 | Created: 2025-12-20 | Authoritative Reference*
