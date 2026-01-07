---
tags: #spes #claude-instructions #quality-assurance #testing #validation
aliases: [QA Checklist, Quality Assurance, SPES Testing]
status: evergreen
certainty: ^verified
created: 2025-12-16
---

# Quality Assurance Checklist

> [!abstract] Purpose
> Comprehensive validation standards for components, workflows, and system outputs. Ensures SPES maintains high quality and reliability.

---

## 🎯 QUALITY PHILOSOPHY

**Core Principle**: Quality is enforced through **systematic validation at multiple levels**, not hoped for.

**Quality Levels**:
1. **Component Quality**: Individual building blocks are sound
2. **Integration Quality**: Components work well together
3. **Workflow Quality**: Sequential processes produce intended outcomes
4. **System Quality**: Overall SPES intelligence improves over time

---

## 📋 LEVEL 1: COMPONENT QUALITY CHECKLIST

### Pre-Creation Validation

- [ ] **Duplication Check**: Searched existing components (vscan tool)
- [ ] **Alias Check**: Checked synonyms and related concepts
- [ ] **Need Justification**: Clear use case exists for this component
- [ ] **Type Classification**: Correctly identified as atomic/composite/specialized

### Metadata Quality

- [ ] **YAML Completeness**: All required fields present
  ```yaml
  tags: [min 3 tags, includes #spes, #component]
  aliases: [min 2 aliases]
  status: [seedling/evergreen/reference]
  certainty: [^verified/^speculative]
  created: [YYYY-MM-DD]
  component-type: [atomic-*/composite-*/specialized-*]
  usage-count: [initialized to 0]
  success-rate: [pending/high/medium/low]
  ```
- [ ] **Tag Accuracy**: Tags match component function and domain
- [ ] **Alias Relevance**: Aliases are actual synonyms user might search
- [ ] **Status Justification**: Status matches testing state (seedling if untested)

### Content Quality

- [ ] **Definition Block**: Clear one-sentence purpose statement
- [ ] **Usage Context**: "When to Use" section with 3+ scenarios
- [ ] **Anti-Usage Context**: "When NOT to Use" section with 2+ scenarios
- [ ] **Component Text**: Clean, copy-paste ready prompt text
- [ ] **Integration Notes**: Links to ≥2 compatible components
- [ ] **Conflict Documentation**: Lists incompatible components (if any)
- [ ] **Performance Notes**: Performance section initialized

### Structural Quality

- [ ] **Graph Connectivity**: ≥2 outgoing links (run orphan check)
- [ ] **Link Validity**: No broken [[wiki-links]] (run linkcheck)
- [ ] **File Placement**: Located in correct atomic/composite/specialized subfolder
- [ ] **Filename Convention**: Descriptive, kebab-case, includes type hint

### Syntactic Quality

- [ ] **Markdown Validation**: No syntax errors
- [ ] **Code Block Formatting**: Prompt text in proper code blocks
- [ ] **Callout Usage**: Uses semantic callouts correctly
- [ ] **LaTeX Math**: Math notation uses LaTeX syntax

---

## 📋 LEVEL 2: INTEGRATION QUALITY CHECKLIST

### Component Combination Testing

- [ ] **Synergy Validation**: Test with "Works Well With" components
  - [ ] Combined output > individual outputs (qualitative assessment)
  - [ ] No instruction conflicts observed
  - [ ] Synergy documented with evidence

- [ ] **Conflict Verification**: Test with "Conflicts With" components
  - [ ] Conflict manifests as predicted
  - [ ] Conflict mechanism understood (why do they conflict?)
  - [ ] Conflict documentation accurate

- [ ] **Novel Combinations**: Test 2-3 untested component pairings
  - [ ] Identify unexpected synergies
  - [ ] Identify unexpected conflicts
  - [ ] Update component docs with findings

### Workflow Integration

- [ ] **Workflow Placement**: Component added to relevant workflow docs
- [ ] **Turn Appropriateness**: Component tested at different workflow turns
  - [ ] Turn 1 (initial context)
  - [ ] Turn N (mid-workflow)
  - [ ] Turn Final (synthesis)
- [ ] **Context Compatibility**: Works with different context-handoff strategies

### Dependency Testing

- [ ] **Standalone Test**: Component works in isolation
- [ ] **Dependency Chain**: If component requires others, chain documented
- [ ] **Order Sensitivity**: If order matters, sequence specified

---

## 📋 LEVEL 3: WORKFLOW QUALITY CHECKLIST

### Pre-Execution Validation

- [ ] **Problem Classification**: Problem type correctly identified
- [ ] **Constraint Analysis**: All constraints documented
- [ ] **Workflow Selection**: Chosen workflow matches problem type
- [ ] **Context Strategy**: Handoff strategy selected with justification
- [ ] **Component Selection**: All needed components identified
- [ ] **Success Criteria**: Clear definition of "workflow succeeded"

### Execution Monitoring

- [ ] **Turn Scope Adherence**: Each turn stays within defined scope
- [ ] **Format Compliance**: Output follows format requirements
- [ ] **Instruction Drift**: No drift from original constraints
- [ ] **Context Size**: Tracking token count, adjusting if needed
- [ ] **Intermediate Verification**: Quality checks at key turns

### Post-Execution Validation

- [ ] **Success Criteria Met**: Workflow achieved stated goals
- [ ] **Output Quality**: Final output meets quality bar
- [ ] **Efficiency Assessment**: Workflow better than one-shot approach?
  - [ ] Quality: Higher/Lower/Same?
  - [ ] Effort: Worth the multi-turn investment?
  - [ ] Reproducibility: Would it work again?

- [ ] **Documentation**: Workflow logged with:
  - [ ] Problem type
  - [ ] Workflow pattern used
  - [ ] Context strategy used
  - [ ] Components used
  - [ ] Success/failure result
  - [ ] Lessons learned

### Failure Analysis (If Workflow Failed)

- [ ] **Failure Point Identified**: Which turn/component failed?
- [ ] **Root Cause Analysis**: Why did it fail?
  - [ ] Wrong workflow pattern?
  - [ ] Wrong context strategy?
  - [ ] Component inadequacy?
  - [ ] Instruction drift?
  - [ ] User error?

- [ ] **Lessons Documented**: Logged in [[99-archive/failed-experiments]]
- [ ] **System Update**: If system issue, update relevant SOP

---

## 📋 LEVEL 4: SYSTEM QUALITY CHECKLIST

### Data Quality

- [ ] **Usage Analytics Accuracy**: Usage counts incremented correctly
- [ ] **Performance Tracking**: Success rates reflect actual results
- [ ] **Pattern Detection**: Emerging patterns documented
- [ ] **Gap Identification**: Missing components identified

### Knowledge Quality

- [ ] **Dataview Queries Functional**: All intelligence queries work
- [ ] **Metadata Compliance**: >90% of components fully compliant
- [ ] **Graph Health**: Orphan rate <20%
- [ ] **Link Integrity**: Broken link rate <10%

### Documentation Quality

- [ ] **SOP Currency**: Instructions reflect actual practices
- [ ] **Example Accuracy**: Examples in docs actually work
- [ ] **Change Log**: System changes documented
- [ ] **Session Memory**: Memory files updated regularly

### Learning Quality

- [ ] **Pattern Recognition**: Claude detects usage patterns
- [ ] **Recommendation Accuracy**: Suggestions match user needs
- [ ] **Knowledge Gaps Closed**: Identified gaps lead to new components
- [ ] **System Evolution**: SPES improves measurably over time

---

## 🔍 TESTING PROTOCOLS

### Unit Test Protocol (Individual Component)

```markdown
TEST: [Component Name]
DATE: YYYY-MM-DD
TESTER: Claude / User

**Test 1: Syntax Validation**
- Prompt: [Component text]
- Input: [Test input]
- Expected: [Expected behavior]
- Actual: [Actual output]
- Result: PASS / FAIL
- Notes: [Observations]

**Test 2: Isolation Test**
- Prompt: [Component alone, no other components]
- Input: [Test input]
- Expected: [Expected behavior]
- Actual: [Actual output]
- Result: PASS / FAIL
- Notes: [Observations]

**Test 3: Edge Case Test**
- Prompt: [Component text]
- Input: [Unusual/extreme input]
- Expected: [Graceful handling]
- Actual: [Actual output]
- Result: PASS / FAIL
- Notes: [Edge case behavior]

**Overall Assessment**: PASS / CONDITIONAL / FAIL
**Recommendation**: [Approve/Modify/Reject]
```

### Integration Test Protocol (Component Pairs)

```markdown
TEST: [Component A] + [Component B]
DATE: YYYY-MM-DD
TESTER: Claude / User

**Test 1: Synergy Test**
- Prompt: [Both components combined]
- Input: [Test input]
- Expected: [Better than either alone]
- Actual: [Actual output]
- Synergy Observed: YES / NO
- Synergy Type: [Additive / Multiplicative / Emergent]

**Test 2: Conflict Test**
- Conflicts Expected: YES / NO
- If YES:
  - Conflict Type: [Instruction contradiction / Goal conflict / Format incompatibility]
  - Conflict Manifested: YES / NO
  - Model Behavior: [How did model handle conflict?]

**Test 3: Order Sensitivity**
- Test A→B: [Result]
- Test B→A: [Result]
- Order Matters: YES / NO
- Preferred Order: [If applicable]

**Overall Assessment**: COMPATIBLE / CONDITIONAL / INCOMPATIBLE
**Documentation Update**: [What to add to component docs]
```

### System Test Protocol (Full Workflow)

```markdown
TEST: [Workflow Name] for [Problem Type]
DATE: YYYY-MM-DD
TESTER: Claude / User

**Problem Description**: [Actual user problem]
**Workflow Selected**: [Pattern name]
**Context Strategy**: [Handoff strategy]
**Components Used**: [List all components]

**Execution Log**:
- Turn 1: [Component(s)] → [Quality: 1-10] → [Notes]
- Turn 2: [Component(s)] → [Quality: 1-10] → [Notes]
- Turn N: [Component(s)] → [Quality: 1-10] → [Notes]

**Final Output Quality**: [1-10]
**Efficiency vs One-Shot**: [Better / Worse / Same]
**User Satisfaction**: [1-10]

**Metrics**:
- Total Tokens: [Count]
- Total Turns: [Count]
- Time Investment: [Estimate]
- Success: YES / NO

**Comparison to Baseline**:
- One-Shot Quality: [1-10]
- Sequential Quality: [1-10]
- Quality Delta: [+/- points]
- Worth It? YES / NO

**Lessons Learned**: [Key insights from this test]
**System Updates**: [What should be changed based on results]
```

---

## 🎯 QUALITY GATES

Components cannot be marked `status: evergreen` until:

- ✅ **Unit tested** with ≥2 test cases
- ✅ **Integration tested** with ≥2 other components
- ✅ **Used successfully** in ≥1 real workflow
- ✅ **Metadata 100%** compliant (passes metaudit)
- ✅ **Graph connected** ≥2 in, ≥2 out (passes orphan check)
- ✅ **Links valid** (passes linkcheck)

Workflows cannot be marked "production-ready" until:

- ✅ **System tested** with ≥3 real problems
- ✅ **Success rate** ≥70%
- ✅ **Documented** with examples and edge cases
- ✅ **Component dependencies** all at evergreen status

System updates cannot be deployed until:

- ✅ **Tested** in isolated environment
- ✅ **Documented** in change log
- ✅ **Validated** against existing workflows (nothing breaks)
- ✅ **Logged** in session-memory

---

## 📊 QUALITY METRICS DASHBOARD

### Component Health

```dataview
TABLE
  component-type,
  status,
  usage-count,
  success-rate,
  length(file.inlinks) + length(file.outlinks) as connectivity
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"
SORT success-rate DESC, usage-count DESC
```

### Workflow Performance

```dataview
TABLE
  problem-type,
  workflow-pattern,
  success-rate,
  average-turns,
  last-tested
FROM "02-projects/_spes-sequential-prompt-engineering-system/03-sequential-workflows"
WHERE workflow-pattern
SORT success-rate DESC
```

### System Compliance

```
Metadata Compliance: [X%]
Graph Health: [X% healthy nodes]
Link Integrity: [X% valid links]
Quality Gate Pass Rate: [X% components at evergreen]
```

---

## 🔗 Related Procedures

- [[01-component-management-sop]] → Component creation standards
- [[02-sequential-workflow-protocols]] → Workflow execution standards
- [[05-metadata-tagging-standards]] → Metadata requirements
- [[06-usage-analytics-protocols]] → Performance tracking methods

---

*Quality Assurance Version: 1.0 | Last Updated: 2025-12-16*
