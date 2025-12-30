<%*
// FILE NAMING AUTOMATION
// Convention: system-prompt-[semantic-title]-[version]-[timestamp].md
// Example: system-prompt-expert-coder-1.0.0-20251220143022.md

// 1. Prompt for semantic title
const semanticTitle = await tp.system.prompt("System prompt title (e.g., 'expert-coder', 'research-assistant'):");
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

// 3. Fixed prefix for system prompts
const prefix = "system-prompt";

// 4. Generate version and timestamp
const version = "1.0.0";
const timestamp = tp.date.now("YYYY-MM-DD-HH-mm-ss");

// 5. Construct filename
const filename = `${prefix}-${sanitized}-${version}-${timestamp}`;

// 6. Rename file
await tp.file.rename(filename);
_%>
---
type: "system-prompt"
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
tags:
  - "year/<% tp.date.now("YYYY") %>"
  - "prompt-engineering"
  - "system-prompt"
  - "llm-capability/role-assignment"
  - "prompt-workflow/foundation"
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
> **Purpose**: System-level instructions that establish model behavior, identity, and operational parameters.
>
> **How to Use**:
> 1. Define the **Role & Identity** (who the model should be)
> 2. Establish **Behavioral Guidelines** (how it should act)
> 3. Specify **Knowledge Domain** (what it should know)
> 4. Set **Response Format** (how it should output)
> 5. Provide **Examples** (demonstrations of desired behavior)
>
> **System Prompt Characteristics**:
> - Sets foundational behavior for entire conversation
> - Typically loaded at session start
> - Should be comprehensive but not overly restrictive
> - Acts as "personality" and "operating system" for the model
>
> **Best Practices**:
> - Be explicit about tone, style, and approach
> - Define boundaries and limitations
> - Include output formatting preferences
> - Add constraints to prevent undesired behavior

> [!metadata] Metadata Health Check
> **Type**: `VIEW[{type}]`
> **Status**: `VIEW[{status}]` | **Version**: `VIEW[{version}]` | **Rating**: `VIEW[{rating}]`/10
> **Maturity**: `VIEW[{maturity}]` | **Confidence**: `VIEW[{confidence}]` | **Priority**: `VIEW[{priority}]`
> **Usage Count**: `VIEW[{usage-count}]` | **Last Used**: `VIEW[{last-used}]`
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
> <!-- Brief description of this system prompt's role and objective -->
> <% tp.file.cursor(1) %>

## 🎯 Use Cases

<!-- When should this system prompt be used? -->
- <% tp.file.cursor(2) %>

## 🚫 When NOT to Use

<!-- Scenarios where this system prompt is inappropriate -->
- <% tp.file.cursor(3) %>

---

## 📝 SYSTEM PROMPT CONTENT

### 1. ROLE DEFINITION

<!-- Define the model's identity, expertise, and perspective -->
```markdown
You are <% tp.file.cursor(4) %>

Your core expertise includes:
-
-
-

Your approach is characterized by:
-
-
-
```

### 2. BEHAVIORAL GUIDELINES

<!-- Establish how the model should interact and respond -->
```markdown
**Communication Style**:
-
-

**Problem-Solving Approach**:
-
-

**Interaction Principles**:
-
-

**Prohibited Behaviors**:
- DO NOT:
- NEVER:
- AVOID:
```

### 3. KNOWLEDGE DOMAIN

<!-- Specify areas of expertise and knowledge boundaries -->
```markdown
**Core Knowledge Areas**:
1. <% tp.file.cursor(5) %>
2.
3.

**Specializations**:
-
-

**Known Limitations**:
- Not expert in:
- Will defer to user on:
- Should verify before claiming:
```

### 4. RESPONSE FORMAT

<!-- Define output structure and formatting preferences -->
```markdown
**Standard Response Structure**:
1.
2.
3.

**Formatting Requirements**:
- Use [specific format] for [type of content]
- Always include [required elements]
- Structure long responses as [format]

**Tone & Style**:
- Formality level:
- Technical depth:
- Verbosity:
```

### 5. EXAMPLES

<!-- Demonstrate desired behavior with concrete examples -->

#### Example Interaction 1

**User Query**:
```
<% tp.file.cursor(6) %>
```

**Expected Response**:
```
<% tp.file.cursor(7) %>
```

**Why This Works**:
-
-

#### Example Interaction 2

**User Query**:
```
<% tp.file.cursor(8) %>
```

**Expected Response**:
```

```

**Why This Works**:
-
-

---

## 🧩 COMPONENTS USED

<!-- Link to reusable components from library -->
<!-- Use Component Search macro to find and insert -->
<!-- Update components-used in frontmatter -->

**Persona Components**:
-

**Instruction Blocks**:
-

**Constraint Sets**:
-

**Format Templates**:
-

**Knowledge Framers**:
-

---

## 🧪 TESTING & VALIDATION

### Test 1: [Date]
**Objective**: Test role adherence
**Scenario**:
**Result**: ✅ Pass | ❌ Fail
**Quality Score**: /10
**Notes**:

**Issues Found**:
-

**Link**: [[test-result-link]]

---

### Test 2: [Date]
**Objective**: Test behavioral guidelines
**Scenario**:
**Result**: ✅ Pass | ❌ Fail
**Quality Score**: /10
**Notes**:

**Issues Found**:
-

---

### Version History

| Version | Date | Changes | Quality Δ | Link |
|---------|------|---------|-----------|------|
| 1.0.0 | <% tp.date.now("YYYY-MM-DD") %> | Initial creation | - | - |

---

## 📊 USAGE TRACKING

### Production Usage
<!-- Where and when this system prompt was used -->

**Project/Context**:
**Date**:
**Session Duration**:
**Outcome**:
**User Feedback**:

---

### Performance Notes
<!-- Observations about effectiveness -->

**Strengths**:
-

**Weaknesses**:
-

**Edge Cases Discovered**:
-

**Improvement Ideas**:
-

---

## 🔗 RELATED PROMPTS

```dataviewjs
// Semantic Bridge: Find related prompts
const current = dv.current();
const myOutlinks = current.file.outlinks.map(l => l.path);

const siblings = dv.pages()
    .where(p => (p.type === "system-prompt" || p.type === "component"))
    .where(p => p.file.path !== current.file.path)
    .map(p => {
        const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
        return {
            link: p.file.link,
            type: p.type,
            rating: p.rating || 0,
            sharedCount: shared.length
        };
    })
    .where(p => p.sharedCount > 0)
    .sort(p => p.sharedCount, "desc")
    .limit(5);

if (siblings.length > 0) {
    dv.header(4, "🌉 Similar System Prompts (Shared Context)");
    dv.table(
        ["Prompt", "Type", "Rating", "Shared Links"],
        siblings.map(s => [s.link, s.type, s.rating + "/10", "🔗 " + s.sharedCount])
    );
} else {
    dv.paragraph("*No related system prompts found yet.*");
}
```

### Manual Links
<!-- Add links to related prompts, workflows, or projects -->
-

---

## 💡 OPTIMIZATION LOG

### Optimization Attempt: [Date]
**Hypothesis**:
**Changes Made**:
**Result**:
**New Rating**: /10
**Keep Changes?**: Yes | No

---

## 🎓 LESSONS LEARNED

<!-- Document insights for future system prompt creation -->

**What Worked Well**:
-

**What Didn't Work**:
-

**Unexpected Behaviors**:
-

**Key Insights**:
-

---

## 📋 QUICK ACTIONS

**Meta-Bind Buttons** (if configured):
- `BUTTON[increment-usage]` - Increment usage count
- `BUTTON[run-test]` - Quick test documentation
- `BUTTON[bump-version]` - Version increment
- `BUTTON[archive]` - Move to archive

---

## 📚 REFERENCES & RESOURCES

<!-- Links to documentation, research, examples -->

**Prompt Engineering Principles**:
-

**Related Research**:
-

**Inspiration Sources**:
-

---

*Template Version: 1.0.0 | Created: 2025-12-20 | System Prompt Template*
