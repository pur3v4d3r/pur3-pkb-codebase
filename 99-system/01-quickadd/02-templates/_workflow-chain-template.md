<%*
// FILE NAMING AUTOMATION
// Convention: workflow-[semantic-title]-[version]-[timestamp].md
// Example: workflow-code-review-pipeline-1.0.0-20251220143022.md

// 1. Prompt for semantic title
const semanticTitle = await tp.system.prompt("Workflow title (e.g., 'code-review-pipeline', 'content-creation'):");
if (!semanticTitle) {
    throw new Error("❌ Cancelled: No title provided");
}

// 2. Sanitize title (lowercase, replace spaces with hyphens, remove special chars)
const sanitized = semanticTitle
    .toLowerCase()
    .trim()
    .replace(/\s+/g, '-')
    .replace(/[^a-z0-9-]/g, '')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');

// 3. Fixed prefix for workflow prompts
const prefix = "workflow";

// 4. Generate version and timestamp
const version = "1.0.0";
const timestamp = tp.date.now("YYYY-MM-DD-HH-mm-ss");

// 5. Construct filename
const filename = `${prefix}-${sanitized}-${version}-${timestamp}`;

// 6. Rename file
await tp.file.rename(filename);
_%>
---
type: "workflow-chain"
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
status: "<% await tp.system.suggester(["Active", "Testing", "Production", "Deprecated", "Archived"], ["active", "testing", "production", "deprecated", "archived"], false, "Status?") %>"
version: "1.0.0"
rating: "0.0"
source: "<% await tp.system.suggester(["Claude Sonnet 4.5", "Claude Opus 4.5", "Gemini 3.0 Pro", "Gemini 3.0 Flash", "Original (Pur3v4d3r)", "Local LLM", "Other"], ["claude-sonnet-4.5", "claude-opus-4.5", "gemini-3.0-pro", "gemini-3.0-flash", "original", "local-llm", "other"], false, "Source of prompt?") %>"
created: "<% tp.date.now("YYYY-MM-DD") %>"
modified: "<% tp.date.now("YYYY-MM-DD") %>"
usage-count: 0
last-used: ""
review-next: "<% tp.date.now("YYYY-MM-DD", 7) %>"
review-interval: 7
review-count: 0
confidence: "<% await tp.system.suggester(["Speculative", "Provisional", "Moderate", "Established", "High"], ["speculative", "provisional", "moderate", "established", "high"], false, "Confidence level?") %>"
maturity: "seedling"
priority: "<% await tp.system.suggester(["Low", "Medium", "High", "Urgent"], ["low", "medium", "high", "urgent"], false, "Priority?") %>"
workflow-steps: 0
tags:
  - "year/<% tp.date.now("YYYY") %>"
  - "prompt-engineering"
  - "workflow-chain"
  - "llm-capability/orchestration"
  - "prompt-workflow/sequential"
aliases:
  - "<% tp.file.title %>"
link-up: "[[prompt-engineering-moc]]"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily Note]]"
  - "[[<% tp.date.now("gggg-[W]WW") %>|Weekly Review]]"
components-used: []
test-results: []
---

> [!usage] Template Usage Instructions
> **Purpose**: Multi-step sequential processes that orchestrate complex tasks through chained operations.
>
> **How to Use**:
> 1. Define **Workflow Overview** (high-level process map)
> 2. Specify **Step Definitions** (detailed instructions per step)
> 3. Set **Transition Logic** (how outputs feed into next steps)
> 4. Include **Output Aggregation** (how to combine results)
>
> **Workflow Chain Characteristics**:
> - Multiple discrete steps executed sequentially
> - Each step's output feeds into next step
> - Can include branching/conditional logic
> - Enables complex multi-stage processes
>
> **Best Practices**:
> - Make each step self-contained and testable
> - Define clear input/output contracts
> - Include error handling at each step
> - Document data flow between steps

> [!metadata] Metadata Health Check
> **Type**: `VIEW[{type}]`
> **Status**: `VIEW[{status}]` | **Version**: `VIEW[{version}]` | **Rating**: `VIEW[{rating}]`/10
> **Maturity**: `VIEW[{maturity}]` | **Confidence**: `VIEW[{confidence}]` | **Priority**: `VIEW[{priority}]`
> **Usage Count**: `VIEW[{usage-count}]` | **Workflow Steps**: `VIEW[{workflow-steps}]`
>
> > [!temporal] 🕰️ Temporal Context
> > **Created**: `= this.file.ctime` | **Age**: `= (date(today) - this.file.ctime).days + " days"`
> > **Modified**: `= this.file.mtime` | **Staleness**: `= choice((date(today) - this.file.mtime).days > 180, "🕸️ Cobwebs", choice((date(today) - this.file.mtime).days > 30, "🍂 Cold", "🔥 Fresh"))`
> > **Next Review**: `= this.review-next` | **Review Interval**: `= this.review-interval + " days"`
>
> > [!quality] 📊 Quality Metrics
> > **Word Count**: `= this.file.size` bytes | **Est. Read Time**: `= round(this.file.size / 1300) + " min"`
> > **Components Used**: `= length(this.components-used)` | **Test Results**: `= length(this.test-results)`
> > **Health Status**: `$= const fields = ["type", "status", "version", "source", "tags"]; const missing = fields.filter(f => !dv.current()[f]); missing.length > 0 ? "⚠️ Missing: " + missing.join(", ") : "✅ All Systems Go"`
>
> > [!network] 🔗 Network Connectivity
> > **In-Links**: `= length(this.file.inlinks)` | **Out-Links**: `= length(this.file.outlinks)`
> > **Network Status**: `= choice(length(this.file.inlinks) = 0, "🕸️ Orphan", choice(length(this.file.inlinks) > 5, "⚡ Hub", "🌱 Node"))`
> > **Folder**: `= this.file.folder`

[Initial Creation: [[<% tp.date.now("YYYY-MM-DD") %>|<% tp.date.now("dddd, MMMM Do, YYYY") %>]]]

---

# <% tp.file.title %>

> [!abstract] Purpose
> <!-- Brief description of what this workflow accomplishes -->
> <% tp.file.cursor(1) %>

## 🎯 Use Cases

<!-- When should this workflow be used? -->
- <% tp.file.cursor(2) %>

## 🚫 When NOT to Use

<!-- Scenarios where this workflow is inappropriate -->
- <% tp.file.cursor(3) %>

---

## 📝 WORKFLOW CHAIN CONTENT

### 1. WORKFLOW OVERVIEW

<!-- High-level process map and architecture -->
```markdown
<% tp.file.cursor(4) %>

**Workflow Name**:


**Objective**:


**Input Requirements**:
-
-
-

**Final Output**:


**Process Flow**:
```
[Input] → [Step 1] → [Step 2] → [Step 3] → [Step 4] → [Final Output]
```

**Key Characteristics**:
- Total Steps:
- Estimated Duration:
- Complexity Level:
- Dependencies:
```

---

### 2. STEP DEFINITIONS

<!-- Detailed instructions for each workflow step -->

#### Step 1: [Step Name]

**Purpose**:
<% tp.file.cursor(5) %>

**Input**:
```
Format:
Source:
Required Fields:
-
-
```

**Instructions**:
```markdown
<% tp.file.cursor(6) %>

1.
2.
3.

**Quality Criteria**:
-
-

**Common Issues**:
-
-
```

**Output**:
```
Format:
Destination:
Fields:
-
-
```

**Error Handling**:
- If [condition], then:
- If [condition], then:

---

#### Step 2: [Step Name]

**Purpose**:
<% tp.file.cursor(7) %>

**Input**:
```
Format:
Source: [Output from Step 1]
Required Fields:
-
-
```

**Instructions**:
```markdown

1.
2.
3.

**Quality Criteria**:
-
-

**Common Issues**:
-
-
```

**Output**:
```
Format:
Destination:
Fields:
-
-
```

**Error Handling**:
- If [condition], then:
- If [condition], then:

---

#### Step 3: [Step Name]

**Purpose**:
<% tp.file.cursor(8) %>

**Input**:
```
Format:
Source: [Output from Step 2]
Required Fields:
-
-
```

**Instructions**:
```markdown

1.
2.
3.

**Quality Criteria**:
-
-

**Common Issues**:
-
-
```

**Output**:
```
Format:
Destination:
Fields:
-
-
```

**Error Handling**:
- If [condition], then:
- If [condition], then:

---

#### Step 4: [Step Name] (Optional)

**Purpose**:

**Input**:
```
Format:
Source: [Output from Step 3]
Required Fields:
-
-
```

**Instructions**:
```markdown

1.
2.
3.

**Quality Criteria**:
-
-

**Common Issues**:
-
-
```

**Output**:
```
Format:
Destination:
Fields:
-
-
```

**Error Handling**:
- If [condition], then:
- If [condition], then:

---

### 3. TRANSITION LOGIC

<!-- How data flows between steps -->
```markdown
**Data Transformation Rules**:

**Step 1 → Step 2**:
- Extract:
- Transform:
- Validate:

**Step 2 → Step 3**:
- Extract:
- Transform:
- Validate:

**Step 3 → Step 4**:
- Extract:
- Transform:
- Validate:

**Conditional Branching**:
- If [condition at Step X], skip to Step Y
- If [condition at Step X], repeat Step X
- If [condition at Step X], terminate workflow

**State Management**:
- Persist between steps:
- Reset between steps:
- Accumulate across steps:
```

---

### 4. OUTPUT AGGREGATION

<!-- How to combine and present final results -->
```markdown
**Final Output Assembly**:

**Combine Results From**:
- Step 1 contributes:
- Step 2 contributes:
- Step 3 contributes:
- Step 4 contributes:

**Output Format**:
```
[Specify final output structure]
```

**Quality Validation**:
- Check:
- Verify:
- Ensure:

**Presentation**:
- Format as:
- Structure as:
- Include:

**Metadata to Include**:
- Workflow version:
- Execution timestamp:
- Step completion status:
- Quality scores:
```

---

## 🧩 COMPONENTS USED

<!-- Link to reusable components from library -->
<!-- Use Component Search macro to find and insert -->
<!-- Update components-used in frontmatter -->

**Step Templates**:
-

**Validation Rules**:
-

**Error Handlers**:
-

**Output Formatters**:
-

---

## 🧪 TESTING & VALIDATION

### Test 1: [Date]
**Objective**: End-to-end workflow test
**Input**:
**Step 1 Result**:
**Step 2 Result**:
**Step 3 Result**:
**Final Output**:
**Result**: ✅ Pass | ❌ Fail
**Quality Score**: /10
**Bottlenecks Found**:
-

**Link**: [[test-result-link]]

---

### Test 2: [Date]
**Objective**: Error handling test
**Failure Injected At**: Step X
**Error Type**:
**Recovery Success**: Yes | No
**Result**: ✅ Pass | ❌ Fail
**Notes**:

---

### Version History

| Version | Date | Changes | Steps | Quality Δ | Link |
|---------|------|---------|-------|-----------|------|
| 1.0.0 | <% tp.date.now("YYYY-MM-DD") %> | Initial creation | 3 | - | - |

---

## 📊 USAGE TRACKING

### Production Usage
<!-- Where and when this workflow was used -->

**Project/Context**:
**Date**:
**Input Type**:
**Processing Time**:
**Output Quality**:
**Bottlenecks**:
**Outcome**:

---

### Performance Notes
<!-- Observations about effectiveness -->

**Step Performance**:
- Fastest step:
- Slowest step:
- Most error-prone:

**Data Flow Quality**:
-

**Optimization Opportunities**:
-

**Improvement Ideas**:
-

---

## 🔗 RELATED PROMPTS

```dataviewjs
// Semantic Bridge: Find related workflow prompts
const current = dv.current();
const myOutlinks = current.file.outlinks.map(l => l.path);

const siblings = dv.pages()
    .where(p => (p.type === "workflow-chain" || p.type === "component"))
    .where(p => p.file.path !== current.file.path)
    .map(p => {
        const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
        return {
            link: p.file.link,
            type: p.type,
            rating: p.rating || 0,
            steps: p["workflow-steps"] || 0,
            sharedCount: shared.length
        };
    })
    .where(p => p.sharedCount > 0)
    .sort(p => p.sharedCount, "desc")
    .limit(5);

if (siblings.length > 0) {
    dv.header(4, "🌉 Similar Workflows (Shared Context)");
    dv.table(
        ["Workflow", "Type", "Rating", "Steps", "Shared Links"],
        siblings.map(s => [s.link, s.type, s.rating + "/10", s.steps, "🔗 " + s.sharedCount])
    );
} else {
    dv.paragraph("*No related workflows found yet.*");
}
```

### Manual Links
<!-- Add links to related prompts, workflows, or projects -->
-

---

## 💡 OPTIMIZATION LOG

### Optimization Attempt: [Date]
**Hypothesis**: (e.g., "Merging Steps 2&3 will improve efficiency")
**Changes Made**:
- Steps modified:
- Transition logic updated:

**Result**:
**Performance Impact**:
**New Rating**: /10
**Keep Changes?**: Yes | No

---

## 🎓 LESSONS LEARNED

<!-- Document insights for future workflow creation -->

**Step Design**:
-

**Data Flow**:
-

**Error Recovery**:
-

**Performance**:
-

**Key Insights**:
-

---

## 📋 QUICK ACTIONS

**Meta-Bind Buttons** (if configured):
- `BUTTON[increment-usage]` - Increment usage count
- `BUTTON[add-step]` - Add workflow step
- `BUTTON[run-test]` - Quick test documentation
- `BUTTON[bump-version]` - Version increment
- `BUTTON[archive]` - Move to archive

---

## 📚 REFERENCES & RESOURCES

<!-- Links to documentation, research, examples -->

**Workflow Patterns**:
-

**Related Systems**:
-

**Integration Points**:
-

---

*Template Version: 1.0.0 | Created: 2025-12-20 | Workflow Chain Template*
