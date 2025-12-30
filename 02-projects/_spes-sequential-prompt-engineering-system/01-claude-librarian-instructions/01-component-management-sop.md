---
tags: #spes #claude-instructions #sop #component-management
aliases: [Component SOP, Component Management, SPES Component Procedures]
status: evergreen
certainty: ^verified
created: 2025-12-16
---

# Component Management SOP

> [!abstract] Purpose
> Standard Operating Procedures for creating, modifying, discovering, and retiring prompt engineering components in the SPES library.

---

## 📋 TABLE OF CONTENTS

1. [[#PHASE 1 Component Discovery]]
2. [[#PHASE 2 Component Creation]]
3. [[#PHASE 3 Component Modification]]
4. [[#PHASE 4 Component Retirement]]
5. [[#PHASE 5 Component Testing]]

---

## PHASE 1: Component Discovery

### When to Search for Existing Components

**ALWAYS search before creating**. Search when:
- User describes a need that sounds familiar
- You're about to create something "basic" or "common"
- User mentions a specific technique or pattern
- You think "we probably have something like this"

### Discovery Protocol

```markdown
STEP 1: Semantic Search
- Search by CONCEPT, not filename
- Example: "academic writing" finds [[scholarly-tone]], [[citation-format]], [[formal-voice]]
- Use vault_scan tool: `vscan "concept term"`

STEP 2: Alias Matching
- Check frontmatter aliases in discovered notes
- Example: [[technical-accuracy]] might have alias "precision-mode"

STEP 3: Fuzzy Matching
- If exact match fails, search for related terms
- Example: "detailed" → "comprehensive", "in-depth", "exhaustive"

STEP 4: Graph Traversal
- Check outlinks from discovered components
- Related components often cluster together
```

### Discovery Decision Tree

```
FOUND exact match?
├─ YES → Use existing component
│   └─ Check: Does it need updating? (Go to PHASE 3)
│
├─ FOUND similar component?
│   ├─ Can it be adapted with minor changes?
│   │   └─ YES → Modify existing (Go to PHASE 3)
│   │   └─ NO → Create variant component (Go to PHASE 2)
│   │
│   └─ Is user's need a special case of this component?
│       └─ YES → Create composite using existing (Go to PHASE 2: Composite)
│       └─ NO → Create new component (Go to PHASE 2)
│
└─ FOUND nothing similar?
    └─ Create new component (Go to PHASE 2)
```

---

## PHASE 2: Component Creation

### 2.1: Determine Component Type

**Atomic Component** (Single-purpose building block)
- Personas: "You are a..."
- Instructions: "Always include..."
- Constraints: "Never use..."
- Output Formats: "Structure response as..."
- Context Framers: "Consider this background..."

**Composite Component** (Multi-component workflow)
- Sequential Chains: Component A → Component B → Component C
- Parallel Branches: Run multiple prompts simultaneously
- Recursive Loops: Repeat with previous output

**Specialized Component** (Domain-specific template)
- Educational Content: Pedagogy-optimized
- Technical Analysis: Rigor-focused
- Creative Writing: Style-focused
- PKB Operations: Graph-aware

### 2.2: Component Creation Checklist

#### Required Elements

- [ ] **Filename**: Descriptive, kebab-case, includes type hint
  - Good: `persona-technical-accuracy-enforcer.md`
  - Bad: `component1.md`, `new-thing.md`

- [ ] **YAML Frontmatter**: Complete 5-tag system
  ```yaml
  ---
  tags: #spes #component #persona #technical #atomic
  aliases: [Accuracy Mode, Precision Enforcer, Technical Rigor]
  status: seedling  # or evergreen after validation
  certainty: ^verified  # or ^speculative if untested
  created: YYYY-MM-DD
  component-type: atomic-persona  # atomic/composite/specialized
  usage-count: 0  # Auto-increment via dataview
  success-rate: pending  # Track after testing
  ---
  ```

- [ ] **Component Definition Block**
  ```markdown
  > [!definition] Component Purpose
  > One-sentence description of what this component does and when to use it.
  ```

- [ ] **Usage Context Section**
  ```markdown
  ## 🎯 When to Use
  - Scenario 1
  - Scenario 2

  ## 🚫 When NOT to Use
  - Scenario 1
  - Scenario 2
  ```

- [ ] **Component Content** (The actual prompt text)
  ```markdown
  ## 📝 Component Text

  ```
  [Actual prompt content here, ready to copy-paste]
  ```
  ```

- [ ] **Integration Notes**
  ```markdown
  ## 🔗 Works Well With
  - [[component-a]] → Why/how they combine
  - [[component-b]] → Synergy description

  ## ⚠️ Conflicts With
  - [[component-c]] → Why they conflict
  ```

- [ ] **Semantic Links** (Minimum 2 outgoing)
  - Link to related components
  - Link to relevant workflows
  - Link to problem types this solves

- [ ] **Performance Tracking Section**
  ```markdown
  ## 📊 Performance Notes

  **Last Tested**: YYYY-MM-DD
  **Success Rate**: [Pending/High/Medium/Low]
  **Known Issues**: None reported / [List issues]
  **Edge Cases**: [Document unusual behavior]
  ```

### 2.3: Component File Placement

**Atomic Components**
```
02-component-library/atomic/
├── personas/           → "You are..." identity frames
├── instructions/       → "Always do..." directives
├── constraints/        → "Never..." restrictions
├── output-formats/     → "Structure as..." templates
└── context-framers/    → "Given that..." background setters
```

**Composite Components**
```
02-component-library/composite/
├── sequential-chains/  → A → B → C workflows
├── parallel-branches/  → Multiple simultaneous prompts
└── recursive-loops/    → Iterative refinement patterns
```

**Specialized Components**
```
02-component-library/specialized/
├── educational-content/  → Pedagogy-optimized templates
├── technical-analysis/   → Rigor-focused workflows
├── creative-writing/     → Style-focused patterns
└── pkb-operations/       → Graph-aware vault operations
```

### 2.4: Post-Creation Actions

- [ ] Run `metaudit` to verify frontmatter compliance
- [ ] Run `linkcheck` to verify no broken links
- [ ] Run `orphan` to verify graph connectivity (≥2 in, ≥2 out)
- [ ] Add component to relevant workflow docs in `[[03-sequential-workflows]]`
- [ ] Update `[[06-analytics-dashboards/component-usage-dashboard]]`
- [ ] Log creation in `[[00-meta/session-memory]]`

---

## PHASE 3: Component Modification

### When to Modify vs Create New

**MODIFY existing when**:
- Fixing errors or typos
- Adding clarifications to existing content
- Updating metadata (usage count, performance notes)
- Improving formatting without changing function

**CREATE NEW variant when**:
- Functionality changes significantly
- Use case diverges from original intent
- Modifications would break existing workflows using this component

### Modification Protocol

```markdown
STEP 1: Document Current State
- Note current version in component's history section
- Example: "Version 1.0 (2025-12-16): Original creation"

STEP 2: Make Changes
- Update component content
- Update "Last Tested" date
- Increment version in history
- Example: "Version 1.1 (2025-12-17): Added edge case handling for X"

STEP 3: Update Dependencies
- Find all workflows using this component (use backlinks)
- Test if modification breaks those workflows
- Update workflow docs if behavior changed

STEP 4: Retest
- Run component through validation (PHASE 5)
- Update success-rate if performance changed
```

---

## PHASE 4: Component Retirement

### When to Retire a Component

- Component is superseded by better variant
- Component has consistent low success rate
- Component no longer aligns with system standards
- Component is unused (usage-count = 0 after 90 days)

### Retirement Protocol

```markdown
STEP 1: Check Dependencies
- Find all workflows using this component
- Identify replacement component
- Update workflows to use replacement

STEP 2: Archive Properly
- Move to `99-archive/retired-components/`
- Add retirement metadata:
  ```yaml
  retired: YYYY-MM-DD
  retirement-reason: [superseded/low-performance/unused/obsolete]
  replacement: [[new-component-name]]
  ```

STEP 3: Update Documentation
- Remove from active component lists
- Add "RETIRED" callout to component:
  ```markdown
  > [!warning] RETIRED COMPONENT
  > This component was retired on YYYY-MM-DD.
  > Reason: [reason]
  > Use [[replacement-component]] instead.
  ```

STEP 4: Log Lessons Learned
- Document why it failed (if applicable)
- Add insights to `99-archive/failed-experiments/`
- Update system knowledge based on learnings
```

---

## PHASE 5: Component Testing

### Unit Testing (Individual Component)

```markdown
TEST 1: Syntax Validation
- [ ] Component text is syntactically valid
- [ ] No ambiguous language
- [ ] Clear, actionable instructions

TEST 2: Isolation Test
- [ ] Use component alone in a prompt
- [ ] Verify expected behavior
- [ ] Document actual vs expected output

TEST 3: Metadata Validation
- [ ] Frontmatter complete (run metaudit)
- [ ] No broken links (run linkcheck)
- [ ] Sufficient connectivity (run orphan check)
```

### Integration Testing (Component Combinations)

```markdown
TEST 1: Synergy Test
- [ ] Combine with "Works Well With" components
- [ ] Verify synergy produces better results than either alone
- [ ] Document performance delta

TEST 2: Conflict Test
- [ ] Combine with "Conflicts With" components (intentionally)
- [ ] Verify conflict manifests as predicted
- [ ] Update conflict documentation if behavior differs

TEST 3: Workflow Test
- [ ] Use component in relevant sequential workflow
- [ ] Verify it performs as expected in multi-turn context
- [ ] Document context-handoff behavior
```

### System Testing (Full Workflow Validation)

```markdown
TEST 1: Real-World Scenario
- [ ] Apply workflow to actual user problem
- [ ] Measure: Quality, time-to-completion, user satisfaction
- [ ] Compare to one-shot baseline (is sequential better?)

TEST 2: Edge Case Testing
- [ ] Test unusual inputs
- [ ] Test at scale (very long/short content)
- [ ] Test with conflicting constraints

TEST 3: Reproducibility
- [ ] Run same workflow 3 times
- [ ] Verify consistent quality
- [ ] Document variance
```

### Validation Outcomes

```markdown
✅ PASS: success-rate → "High"
- Component/workflow performs reliably
- Update status: seedling → evergreen

⚠️ CONDITIONAL PASS: success-rate → "Medium"
- Works with caveats
- Document edge cases clearly
- Status remains: seedling

❌ FAIL: success-rate → "Low"
- Does not perform as intended
- Options:
  1. Modify and retest
  2. Retire and document learnings
  3. Mark as speculative research
```

---

## 🔍 QUALITY GATES

Before marking any component as `status: evergreen`:

- ✅ Passes all unit tests
- ✅ Passes integration tests with 2+ other components
- ✅ Used successfully in at least 1 real workflow
- ✅ Metadata 100% compliant
- ✅ Graph connectivity ≥2 in, ≥2 out
- ✅ Performance documented with evidence

---

## 🔗 Related Procedures

- [[00-librarian-core-identity]] → Core mission and principles
- [[02-sequential-workflow-protocols]] → How components compose into workflows
- [[04-quality-assurance-checklist]] → Validation standards
- [[05-metadata-tagging-standards]] → Metadata specifications
- [[06-usage-analytics-protocols]] → Performance tracking methods

---

*SOP Version: 1.0 | Last Updated: 2025-12-16*
