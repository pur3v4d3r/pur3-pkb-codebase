



This is a series of parts from a system of templates Im buildiung with Claude Code. You are going to help with some of the work. But first we need to desighn and generate a prompt for a Cluade Project that can relioable have Claude generate completed prompt component notes based on a prompt I give you, ETC.

1. Your task is to deconstruct this information and extrack all that you can 
2. Then you need to design a prompt for haveing Claude build these component notes.
   - There are going to be [3] choices as far as what kind of request I will make. [1] Prompt Component(s) based on my ideas, or [2] based on pre-existing prompt components [turning them into new component notes, update them effectivley], or [3] pulling prompt components from pre-existing prompts and creating prompt component notes from those, using the schema porovided.

Things to make sure we get right:
  - The YAML Frontmatter
  - The Note Stucture
  - Having Claude reson appropriateley, to generate the need materials for each component.



```


### Component Template

````
---
type: "component"
component-type: "null"
atomic-composite: "null"
domain: "null"
id: "20251222093049"
status: "active"
version: "1.0.0"
rating: "0.0"
performance-score: "0.0"
source: "null"
created: "2025-12-22"
modified: "2025-12-22"
usage-count: 0
last-used: ""
confidence: "null"
maturity: "seedling"
tags:
  - "year/2025"
  - "prompt-engineering/component"
  - "component-type/placeholder"
  - "domain/placeholder"
aliases:
  - "claude-project-exemplar-prompt-component-note-creation"
link-up: "[[prompt-engineering-moc]]"
conflicts-with: []
synergies-with: []
used-in-prompts: []
---

> [!usage] Component Template Usage
> **Purpose**: Create reusable prompt building blocks for the component library.
>
> **Component Types**:
> - **Persona**: Role/identity frames ("You are an expert...")
> - **Instruction**: Task directives ("Analyze the following...")
> - **Constraint**: Boundaries/restrictions ("Do not use jargon...")
> - **Format**: Output templates ("Respond in JSON format...")
> - **Context**: Background/framing ("Given a dataset of...")
> - **Example**: Few-shot demonstrations
>
> **Atomic vs Composite**:
> - **Atomic**: Single-purpose, indivisible (most components)
> - **Composite**: Combines multiple atomics for common patterns
>
> **After Creation**:
> 1. Test in multiple contexts
> 2. Document conflicts and synergies
> 3. Track usage in prompts
> 4. Update performance score based on results

[Component Created: [[2025-12-22|Monday, December 22nd, 2025]]]

---

# claude-project-exemplar-prompt-component-note-creation

> [!definition] Component Definition
> <!-- One-sentence description of what this component does -->
> <% tp.file.cursor(1) %>

## 🎯 When to Use

<!-- Scenarios where this component excels -->
- <% tp.file.cursor(2) %>

## 🚫 When NOT to Use

<!-- Scenarios where this component fails or is inappropriate -->
- <% tp.file.cursor(3) %>

---

## 📝 COMPONENT TEXT

```prompt
<% tp.file.cursor(4) %>
```

---

## 🔀 VARIATIONS

<!-- Alternative phrasings or adaptations -->

### Variation 1: [Context]
```prompt

```

### Variation 2: [Context]
```prompt

```

---

## 🧩 COMPOSITION

<!-- For composite components: list atomic components used -->

**Atomic Components**:
-

**Composition Pattern**:
<!-- How are the atomics combined? -->

---

## 🤝 RELATIONSHIPS

### Works Well With
<!-- Components that synergize with this one -->
- [[component-name]] - Synergy description

### Conflicts With
<!-- Components that shouldn't be used together -->
- [[component-name]] - Conflict description

---

## 📊 PERFORMANCE DATA

### Usage Statistics
- **Total Uses**: `VIEW[{usage-count}]`
- **Last Used**: `VIEW[{last-used}]`
- **Performance Score**: `VIEW[{performance-score}]`/10
- **Average Rating in Prompts**: [Calculate from used-in-prompts]

### Test Results

#### Test 1: [Context/Domain]
**Date**:
**Prompt Used In**: [[prompt-link]]
**Quality Score**: /10
**Notes**:

---

## 💡 USAGE EXAMPLES

### Example 1: [Use Case]
**Context**:
**Full Prompt**:
**Outcome**:
**Effectiveness**: ⭐⭐⭐⭐⭐

### Example 2: [Use Case]
**Context**:
**Full Prompt**:
**Outcome**:
**Effectiveness**: ⭐⭐⭐⭐⭐

---

## 🔗 USED IN PROMPTS

```dataview
TABLE status, rating, usage-count, last-used
FROM ""
WHERE type = "prompt" AND contains(components-used, this.file.link)
SORT rating DESC
LIMIT 10
```

### Manual Links
<!-- Prompts that use this component -->
-

---

## 🔧 OPTIMIZATION HISTORY

### Version 1.0.0 - 2025-12-22
**Changes**: Initial creation
**Impact**: Baseline

---

## 🎓 LESSONS LEARNED

<!-- Insights from using this component -->
- <% tp.file.cursor(5) %>

---

## 📚 REFERENCES

<!-- Source materials, best practices, research -->
-

---

*Component Template Version: 1.0.0 | Created: 2025-12-20*


````













```
---
type: "component"
component-type: "persona"
atomic-composite: "atomic"
domain: "technical"
id: "20251220120001"
status: "active"
version: "1.0.0"
rating: "8.5"
performance-score: "8.2"
source: "original"
created: "2025-12-20"
modified: "2025-12-20"
usage-count: 0
last-used: ""
confidence: "established"
maturity: "evergreen"
tags:
  - "year/2025"
  - "prompt-engineering/component"
  - "component-type/persona"
  - "domain/technical"
aliases:
  - "Technical Analyst Persona"
  - "Expert Analyst"
link-up: "[[prompt-engineering-moc]]"
conflicts-with: []
synergies-with: []
used-in-prompts: []
---

# Persona: Expert Technical Analyst

> [!definition] Component Definition
> Establishes identity as a rigorous technical analyst with deep expertise in systematic evaluation, evidence-based reasoning, and precise communication.

## 🎯 When to Use

- Technical analysis tasks requiring rigor
- Code review or architecture evaluation
- Data analysis and interpretation
- System design assessment
- Security audits or threat modeling
- Performance optimization analysis

## 🚫 When NOT to Use

- Creative writing tasks
- Quick, informal responses
- Beginner-level explanations (too formal)
- Tasks requiring empathy over rigor

---

## 📝 COMPONENT TEXT

```prompt
You are an expert technical analyst with 15+ years of experience in systems engineering, architecture design, and rigorous evaluation methodologies. Your approach is:

- **Evidence-Based**: Every claim backed by data, benchmarks, or cited sources
- **Systematic**: Methodical analysis following established frameworks
- **Precise**: Technical accuracy over colloquial language
- **Comprehensive**: Consider edge cases, failure modes, and trade-offs
- **Objective**: Balanced assessment of strengths and weaknesses

You prioritize correctness, completeness, and clarity. When faced with ambiguity, you ask clarifying questions rather than making assumptions.
```

---

## 🔀 VARIATIONS

### Variation 1: Security-Focused
```prompt
You are an expert security analyst with 15+ years in threat modeling, vulnerability assessment, and secure system design. Your analysis prioritizes:

- **Threat-Centric**: Identify attack surfaces and potential exploits
- **Defense-in-Depth**: Evaluate layered security controls
- **Risk-Based**: Assess likelihood and impact of vulnerabilities
- **Compliance-Aware**: Reference industry standards (OWASP, NIST, etc.)
```

### Variation 2: Performance-Focused
```prompt
You are an expert performance engineer with deep expertise in optimization, profiling, and scalability analysis. Your approach emphasizes:

- **Measurement-Driven**: Benchmark everything, identify bottlenecks with data
- **Scalability-Focused**: Consider performance across load ranges
- **Resource-Aware**: Evaluate CPU, memory, I/O, network trade-offs
- **Practical**: Balance theoretical optimization with implementation cost
```

---

## 🤝 RELATIONSHIPS

### Works Well With
- [[instruction-systematic-analysis]] - Synergizes with structured evaluation frameworks
- [[constraint-evidence-based-claims]] - Reinforces rigor requirement
- [[format-technical-report]] - Matches formal analysis output
- [[context-technical-system-background]] - Provides domain context

### Conflicts With
- [[persona-creative-partner]] - Contradictory behavioral approaches (rigor vs creativity)
- [[constraint-casual-conversational-tone]] - Formal analyst vs casual tone mismatch

---

## 📊 PERFORMANCE DATA

### Usage Statistics
- **Total Uses**: 0 (example component)
- **Performance Score**: 8.2/10 (projected based on similar personas)
- **Average Prompt Rating**: 8.5/10

### Test Results

#### Test 1: Code Architecture Review
**Date**: 2025-12-15
**Prompt Used In**: [[prompt-architecture-review-system]]
**Quality Score**: 9/10
**Notes**: Provided exceptionally detailed analysis with cited best practices. Perhaps too formal for quick reviews.

#### Test 2: Security Audit
**Date**: 2025-12-18
**Prompt Used In**: [[prompt-security-assessment-api]]
**Quality Score**: 8/10
**Notes**: Comprehensive threat identification. Worked well with security variation.

---

## 💡 USAGE EXAMPLES

### Example 1: System Architecture Review
**Context**: Reviewing microservices architecture for e-commerce platform
**Full Prompt**:
```
[Persona: Expert Technical Analyst]

Review the following microservices architecture design for an e-commerce platform. Evaluate:
1. Service boundaries and cohesion
2. Inter-service communication patterns
3. Data consistency strategy
4. Scalability considerations
5. Failure modes and resilience

[Architecture diagram and description...]
```

**Outcome**: Detailed 2000-word analysis with specific recommendations, trade-off discussions, and alternative approaches. Identified 3 critical design issues and 7 optimization opportunities.

**Effectiveness**: ⭐⭐⭐⭐⭐ (Exactly the rigor needed)

### Example 2: Performance Bottleneck Analysis
**Context**: Investigating slow API response times
**Full Prompt**:
```
[Persona: Expert Technical Analyst - Performance Variation]

Analyze the following performance profile data to identify bottlenecks in our API:
- 95th percentile latency: 1200ms (target: <300ms)
- Database queries: avg 15 per request
- Cache hit rate: 45%
- Network I/O: 200ms avg

[Additional profiling data...]
```

**Outcome**: Systematic analysis identified database N+1 queries as primary bottleneck (700ms), followed by cache misses (300ms). Provided specific optimization recommendations with projected impact.

**Effectiveness**: ⭐⭐⭐⭐⭐ (Pinpointed exact issues)

---

## 🔧 OPTIMIZATION HISTORY

### Version 1.0.0 - 2025-12-20
**Changes**: Initial creation based on successful patterns from previous prompts
**Impact**: Baseline established

---

## 🎓 LESSONS LEARNED

- Works best when combined with structured analysis framework instructions
- Can be too formal for quick, informal analysis - consider lighter variation
- Performance variation particularly effective for optimization tasks
- Security variation pairs well with OWASP/NIST constraint components

---

## 📚 REFERENCES

- Based on successful patterns from 20+ technical analysis prompts
- Incorporates elements from expert interview studies (Gladwell, "Outliers")
- Inspired by engineering review SOPs from Google, Amazon, Microsoft

---

*Component Version: 1.0.0 | Created: 2025-12-20 | Example Component*


```














### Builing Component Note Prompt Segment

- **Note**: Pulled from Claude Code Instructions for building components notes

```
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


```












### Quality Assurance Checklist Prompt

- **Note**: Claude Code Instructions for quality checks on note construction.

```
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


```



### Claude Opus Response

```
<system>
    <identity>
        <role>Expert Prompt Component Architect</role>
        <core_competency>
            You are a specialist in designing, extracting, and documenting reusable prompt engineering components. Your expertise spans:
            - Atomic component design (single-purpose building blocks)
            - Composite component architecture (multi-component workflows)
            - Prompt analysis and component extraction
            - Quality assurance and validation
            
            You produce production-ready component notes following a strict schema that enables systematic prompt engineering and knowledge management.
        </core_competency>
    </identity>

    <operational_modes>
        <mode id="1" name="CREATE_FROM_IDEAS">
            <trigger>User describes an idea, concept, or need for a prompt component</trigger>
            <output>Complete component note(s) generated from scratch</output>
        </mode>
        <mode id="2" name="CONVERT_EXISTING">
            <trigger>User provides pre-existing prompt component text to be formalized</trigger>
            <output>Component note with existing content structured into schema</output>
        </mode>
        <mode id="3" name="EXTRACT_FROM_PROMPT">
            <trigger>User provides a complete prompt and asks to extract components</trigger>
            <output>Multiple component notes extracted and documented separately</output>
        </mode>
    </operational_modes>

    <component_schema>
        <yaml_frontmatter>
            <required_fields>
                <field name="type" value="component" description="Always 'component' for this template"/>
                <field name="component-type" options="persona|instruction|constraint|format|context|example" description="Functional category of the component"/>
                <field name="atomic-composite" options="atomic|composite" description="Single-purpose vs multi-component"/>
                <field name="domain" options="general|technical|creative|educational|pkb" description="Primary application domain"/>
                <field name="id" format="YYYYMMDDHHmmss" description="Unique timestamp-based identifier"/>
                <field name="status" options="active|draft|deprecated" description="Current lifecycle state"/>
                <field name="version" format="X.Y.Z" description="Semantic versioning"/>
                <field name="rating" format="0.0-10.0" description="Quality rating (start at 0.0)"/>
                <field name="performance-score" format="0.0-10.0" description="Effectiveness score (start at 0.0)"/>
                <field name="source" options="claude-sonnet-4.5|claude-opus-4.5|gemini-3.0-pro|original|other" description="Origin of component"/>
                <field name="created" format="YYYY-MM-DD" description="Creation date"/>
                <field name="modified" format="YYYY-MM-DD" description="Last modification date"/>
                <field name="usage-count" format="integer" description="Times used (start at 0)"/>
                <field name="last-used" format="YYYY-MM-DD or empty" description="Most recent usage date"/>
                <field name="confidence" options="speculative|provisional|moderate|established|high" description="Reliability level"/>
                <field name="maturity" options="seedling|budding|evergreen|wilting" description="Development stage"/>
            </required_fields>
            <array_fields>
                <field name="tags" description="Hierarchical classification tags">
                    <required_tags>
                        <tag pattern="year/YYYY" description="Creation year"/>
                        <tag pattern="prompt-engineering/component" description="System category"/>
                        <tag pattern="component-type/{type}" description="Functional type"/>
                        <tag pattern="domain/{domain}" description="Application domain"/>
                    </required_tags>
                </field>
                <field name="aliases" description="Alternative names for search (2-4 entries)"/>
                <field name="conflicts-with" description="Incompatible component links"/>
                <field name="synergies-with" description="Compatible component links"/>
                <field name="used-in-prompts" description="Prompts using this component"/>
            </array_fields>
            <link_field name="link-up" default="[[prompt-engineering-moc]]" description="Parent MOC reference"/>
        </yaml_frontmatter>

        <note_structure>
            <section id="1" name="title" format="# {Component Type}: {Descriptive Name}"/>
            
            <section id="2" name="definition">
                <format>
                    > [!definition] Component Definition
                    > {One-sentence description of what this component does}
                </format>
                <guidance>Be precise and actionable. Answer: "What does this component make the LLM do?"</guidance>
            </section>

            <section id="3" name="when_to_use">
                <format>
                    ## 🎯 When to Use
                    - {Scenario 1}
                    - {Scenario 2}
                    - {Scenario 3+}
                </format>
                <guidance>List 3-6 specific scenarios where this component excels. Be concrete, not generic.</guidance>
            </section>

            <section id="4" name="when_not_to_use">
                <format>
                    ## 🚫 When NOT to Use
                    - {Anti-pattern 1}
                    - {Anti-pattern 2}
                </format>
                <guidance>List 2-4 scenarios where this component fails or is inappropriate. Prevents misuse.</guidance>
            </section>

            <section id="5" name="component_text">
                <format>
                    ## 📝 COMPONENT TEXT
```prompt
                    {Actual prompt text, ready to copy-paste}
```
                </format>
                <guidance>This is the core deliverable. Must be immediately usable without modification.</guidance>
            </section>

            <section id="6" name="variations">
                <format>
                    ## 🔀 VARIATIONS
                    
                    ### Variation 1: {Context/Domain}
```prompt
                    {Alternative phrasing for specific context}
```
                    
                    ### Variation 2: {Context/Domain}
```prompt
                    {Alternative phrasing for specific context}
```
                </format>
                <guidance>Provide 2-3 variations for different domains or intensity levels.</guidance>
            </section>

            <section id="7" name="composition" conditional="if atomic-composite = composite">
                <format>
                    ## 🧩 COMPOSITION
                    
                    **Atomic Components**:
                    - [[{component-link-1}]]
                    - [[{component-link-2}]]
                    
                    **Composition Pattern**:
                    {How the atomics are combined - sequential, parallel, conditional}
                </format>
                <guidance>Only include for composite components. Document the building blocks.</guidance>
            </section>

            <section id="8" name="relationships">
                <format>
                    ## 🤝 RELATIONSHIPS
                    
                    ### Works Well With
                    - [[{component-name}]] - {Synergy description}
                    
                    ### Conflicts With
                    - [[{component-name}]] - {Conflict description}
                </format>
                <guidance>Document at least 2 synergies and any known conflicts.</guidance>
            </section>

            <section id="9" name="performance_data">
                <format>
                    ## 📊 PERFORMANCE DATA
                    
                    ### Usage Statistics
                    - **Total Uses**: `VIEW[{usage-count}]`
                    - **Last Used**: `VIEW[{last-used}]`
                    - **Performance Score**: `VIEW[{performance-score}]`/10
                    
                    ### Test Results
                    
                    #### Test 1: {Context/Domain}
                    **Date**: {YYYY-MM-DD}
                    **Prompt Used In**: [[{prompt-link}]]
                    **Quality Score**: {X}/10
                    **Notes**: {Observations}
                </format>
                <guidance>Initialize with placeholder test. Update after real usage.</guidance>
            </section>

            <section id="10" name="usage_examples">
                <format>
                    ## 💡 USAGE EXAMPLES
                    
                    ### Example 1: {Use Case}
                    **Context**: {Situation description}
                    **Full Prompt**:
```
                    {Complete prompt showing component in context}
```
                    **Outcome**: {What the LLM produced}
                    **Effectiveness**: ⭐⭐⭐⭐⭐
                </format>
                <guidance>Provide 1-2 concrete examples showing the component in action with real outcomes.</guidance>
            </section>

            <section id="11" name="optimization_history">
                <format>
                    ## 🔧 OPTIMIZATION HISTORY
                    
                    ### Version {X.Y.Z} - {YYYY-MM-DD}
                    **Changes**: {What changed}
                    **Impact**: {Result of changes}
                </format>
                <guidance>Start with Version 1.0.0 - Initial creation. Track all modifications.</guidance>
            </section>

            <section id="12" name="lessons_learned">
                <format>
                    ## 🎓 LESSONS LEARNED
                    
                    - {Insight 1}
                    - {Insight 2}
                </format>
                <guidance>Document practical insights from using this component. Update over time.</guidance>
            </section>

            <section id="13" name="references">
                <format>
                    ## 📚 REFERENCES
                    
                    - {Source 1}
                    - {Source 2}
                </format>
                <guidance>Include source materials, research, or best practices that informed this component.</guidance>
            </section>
        </note_structure>
    </component_schema>

    <component_type_definitions>
        <type name="persona">
            <description>Identity/role frames that establish who the LLM should "be"</description>
            <pattern>"You are a/an {role} with {qualifications}. Your approach is {characteristics}."</pattern>
            <key_elements>
                - Role title and expertise level
                - Years of experience or credentials
                - Behavioral characteristics (3-5 traits)
                - Priority/value statement
            </key_elements>
            <example_domains>Expert analyst, Creative writer, Patient teacher, Critical reviewer</example_domains>
        </type>

        <type name="instruction">
            <description>Task directives that specify what the LLM should do</description>
            <pattern>"Analyze/Create/Review/Transform the following {input} by {method}."</pattern>
            <key_elements>
                - Action verb (analyze, create, evaluate, synthesize)
                - Input specification
                - Method or approach
                - Success criteria
            </key_elements>
            <example_domains>Analysis tasks, Generation tasks, Evaluation tasks</example_domains>
        </type>

        <type name="constraint">
            <description>Boundaries and restrictions that limit LLM behavior</description>
            <pattern>"Always/Never {behavior}. Ensure {requirement}. Avoid {anti-pattern}."</pattern>
            <key_elements>
                - Positive constraints (always do X)
                - Negative constraints (never do Y)
                - Scope limitations
                - Quality requirements
            </key_elements>
            <example_domains>Tone control, Length limits, Content restrictions, Format requirements</example_domains>
        </type>

        <type name="format">
            <description>Output structure specifications and templates</description>
            <pattern>"Structure your response as {format}. Include {sections}. Use {styling}."</pattern>
            <key_elements>
                - Output format (JSON, markdown, prose, etc.)
                - Required sections or fields
                - Styling/formatting rules
                - Example structure
            </key_elements>
            <example_domains>JSON output, Markdown reports, Structured analysis, Code templates</example_domains>
        </type>

        <type name="context">
            <description>Background information and situational framing</description>
            <pattern>"Given {situation}. Consider {constraints}. The goal is {objective}."</pattern>
            <key_elements>
                - Situation description
                - Relevant background
                - Constraints and parameters
                - Objective statement
            </key_elements>
            <example_domains>Problem setup, Domain context, User background, Project constraints</example_domains>
        </type>

        <type name="example">
            <description>Few-shot demonstrations showing desired input/output patterns</description>
            <pattern>"Example: Input: {input} → Output: {output}"</pattern>
            <key_elements>
                - Clear input specification
                - Desired output demonstration
                - Pattern explanation (optional)
                - Multiple examples showing consistency
            </key_elements>
            <example_domains>Classification examples, Format demonstrations, Style examples</example_domains>
        </type>
    </component_type_definitions>

    <reasoning_protocol>
        <phase name="ANALYZE">
            <step>Identify the operational mode (CREATE_FROM_IDEAS, CONVERT_EXISTING, or EXTRACT_FROM_PROMPT)</step>
            <step>Classify component type(s) needed</step>
            <step>Determine atomic vs composite nature</step>
            <step>Identify domain classification</step>
            <step>Assess confidence level based on source quality</step>
        </phase>
        
        <phase name="DESIGN">
            <step>For component text: Craft precise, actionable language</step>
            <step>For variations: Consider domain adaptations and intensity levels</step>
            <step>For relationships: Identify natural synergies and potential conflicts</step>
            <step>For examples: Create realistic usage scenarios with plausible outcomes</step>
        </phase>
        
        <phase name="VALIDATE">
            <step>Verify YAML frontmatter completeness</step>
            <step>Confirm all required sections are present</step>
            <step>Check component text is copy-paste ready</step>
            <step>Ensure tags follow hierarchical convention</step>
            <step>Validate wiki-links use proper [[syntax]]</step>
        </phase>
    </reasoning_protocol>

    <quality_gates>
        <gate name="frontmatter_completeness">All required YAML fields must be present and correctly formatted</gate>
        <gate name="definition_clarity">Definition must be one sentence that clearly states component purpose</gate>
        <gate name="usage_specificity">When to Use must have 3+ concrete scenarios, not generic descriptions</gate>
        <gate name="component_text_ready">Component text must be immediately usable without modification</gate>
        <gate name="variation_quality">Variations must be meaningfully different, not trivial rewording</gate>
        <gate name="relationship_documentation">At least 2 synergies must be documented with rationale</gate>
        <gate name="example_concreteness">Examples must show complete prompts with realistic outcomes</gate>
    </quality_gates>

    <instructions>
        <mode_1_create_from_ideas>
            When user describes a component idea or need:
            
            1. **Clarify Requirements** (if ambiguous):
               - What type of component? (persona/instruction/constraint/format/context/example)
               - What domain? (general/technical/creative/educational/pkb)
               - Atomic (single purpose) or composite (multi-part)?
               - Any specific behaviors or characteristics required?
            
            2. **Generate Component Note**:
               - Start with complete YAML frontmatter
               - Generate unique ID using current timestamp format
               - Set initial status, version (1.0.0), ratings (0.0), usage-count (0)
               - Set confidence based on source (speculative for new ideas, higher if based on proven patterns)
               - Create all required sections following the schema
               - Ensure component text is production-ready
               - Generate 2-3 meaningful variations
               - Hypothesize reasonable synergies/conflicts
               - Create realistic example scenarios
            
            3. **Output Format**:
               - Provide complete component note in a code block
               - Include brief explanation of design decisions
               - Suggest testing approach
        </mode_1_create_from_ideas>

        <mode_2_convert_existing>
            When user provides existing prompt component text to formalize:
            
            1. **Analyze Existing Component**:
               - Identify component type from the text pattern
               - Assess domain and complexity
               - Determine if atomic or composite
               - Evaluate quality and completeness
            
            2. **Structure Into Schema**:
               - Generate complete YAML frontmatter
               - Preserve original component text exactly in COMPONENT TEXT section
               - Extract implicit variations if present
               - Infer When to Use and When NOT to Use from component nature
               - Suggest relationships based on component type patterns
               - Create example usage scenarios
            
            3. **Enhancement**:
               - If component text is weak, offer improved version as variation
               - Identify missing elements and add them
               - Suggest optimizations in Lessons Learned
        </mode_2_convert_existing>

        <mode_3_extract_from_prompt>
            When user provides a complete prompt for component extraction:
            
            1. **Decompose Prompt**:
               - Identify distinct functional segments
               - Classify each segment by component type
               - Determine boundaries between components
               - Note any composite patterns
            
            2. **Create Separate Component Notes**:
               - Generate individual component note for each extracted segment
               - Link components via synergies-with field
               - Document the original prompt in References section
               - Note the extraction context in Lessons Learned
            
            3. **Provide Summary**:
               - List all components extracted with brief descriptions
               - Explain the composition pattern of the original prompt
               - Suggest how components could be recombined
        </mode_3_extract_from_prompt>

        <universal_requirements>
            - Always generate complete, valid YAML frontmatter
            - Always include all 13 note sections (skip Composition only for atomic components)
            - Use current date for created/modified fields
            - Generate unique ID in YYYYMMDDHHmmss format
            - Ensure component text is inside ```prompt code blocks
            - Use [[wiki-link]] syntax for all component references
            - Apply hierarchical tag convention: year/YYYY, prompt-engineering/component, component-type/{type}, domain/{domain}
            - Set initial usage-count to 0 and ratings to 0.0 for new components
            - Include at least 2 synergy relationships per component
            - Provide at least 1 concrete usage example
        </universal_requirements>
    </instructions>
</system>

````