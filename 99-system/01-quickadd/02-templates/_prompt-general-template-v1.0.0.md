<%*
// ========================================================================
// SPES General-Purpose Prompt Template v1.0.0
// ========================================================================
// USE WHEN: Prompt doesn't fit specialized categories (system/few-shot/cot/workflow/idea)
// PROVIDES: Flexible structure with guided creation, SPES metadata, quality gates
// INTEGRATES: Component library, testing framework, version control
// ========================================================================

// Step 1: Gather core metadata
const promptTitle = await tp.system.prompt("Prompt title (will auto-generate filename):");
if (!promptTitle) {
    new Notice("❌ Title required. Template cancelled.");
    return;
}

const promptType = await tp.system.suggester(
    ["User Prompt", "Mixed Prompt", "Instruction Set", "Template", "Other"],
    ["user-prompt", "mixed-prompt", "instruction-set", "template", "other"],
    false,
    "What type of prompt is this?"
);

const promptCategory = await tp.system.suggester(
    ["Generation", "Analysis", "Transformation", "Orchestration", "Educational", "Technical", "Creative", "Other"],
    ["generation", "analysis", "transformation", "orchestration", "educational", "technical", "creative", "other"],
    false,
    "Primary category?"
);

const purposeStatement = await tp.system.prompt("One-sentence purpose:", "This prompt helps with...");

const targetModels = await tp.system.suggester(
    ["Claude Sonnet 4.5", "Claude Opus 4.5", "Gemini Pro 3.0", "Gemini Flash 3.0", "GPT-4", "Local LLM", "Multiple", "Model Agnostic"],
    ["claude-sonnet-4.5", "claude-opus-4.5", "gemini-pro-3.0", "gemini-flash-3.0", "gpt-4", "local-llm", "multiple", "model-agnostic"],
    true,
    "Target model(s)? (Multi-select enabled)"
);
const modelList = Array.isArray(targetModels) ? targetModels : [targetModels];
const modelYaml = modelList.map(m => `  - ${m}`).join('\n');

const useComponents = await tp.system.suggester(
    ["Yes - will link components", "No - standalone prompt"],
    [true, false],
    false,
    "Will this use SPES component library?"
);

const needsTesting = await tp.system.suggester(
    ["Yes - include test section", "No - skip testing"],
    [true, false],
    false,
    "Include testing section?"
);

// Step 2: Generate unique ID and filename
const timestamp = tp.date.now("YYYYMMDDHHmmss");
const dateStamp = tp.date.now("YYYY-MM-DD");
const slug = promptTitle.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
const fileName = `prompt-general-${slug}-v1.0.0-${timestamp}.md`;

// Step 3: Calculate review interval (based on maturity: seedling = 7 days)
const reviewDate = tp.date.now("YYYY-MM-DD", 7);

// Step 4: Render template
tR += `---
type: "prompt"
prompt-type: "${promptType}"
prompt-category: "${promptCategory}"
id: "${timestamp}"
status: "active"
maturity: "seedling"
confidence: "provisional"
version: "1.0.0"
rating: "0.0"
target-models:
${modelYaml}
usage-count: 0
last-used: ""
test-results: []
components-used: ${useComponents ? '[]' : 'null'}
link-up: "[[prompt-engineering-moc]]"
link-related:
  - "[[${dateStamp}]]"
  - "[[${tp.date.now("gggg-[W]WW")}]]"
tags:
  - "year/${tp.date.now("YYYY")}"
  - "prompt-engineering"
  - "type/${promptType}"
  - "category/${promptCategory}"
  - "maturity/seedling"
aliases:
  - "${promptTitle}"
created: "${dateStamp}"
modified: "${dateStamp}"
review-next: "${reviewDate}"
review-interval: 7
---

# ${promptTitle}

> [!abstract] Purpose
> ${purposeStatement}

---

## 📋 Prompt Content

### Context & Background
<!-- Provide any background information or context needed to understand this prompt -->

<% tp.file.cursor(1) %>

### Core Instructions
<!-- The main prompt instructions/directives -->

<% tp.file.cursor(2) %>

### Constraints & Boundaries
<!-- Any limitations, restrictions, or boundaries for the AI's response -->

<% tp.file.cursor(3) %>

### Output Format
<!-- Specify desired output format, structure, or style -->

<% tp.file.cursor(4) %>

### Examples (Optional)
<!-- Provide example inputs/outputs if applicable -->

<% tp.file.cursor(5) %>

---
`;

// Conditional: Component Integration Section
if (useComponents) {
    tR += `
## 🧩 SPES Component Integration

> [!helpful-tip] Component Library Usage
> Link to reusable atomic components from the SPES library to compose this prompt.

**Components Used**:
- [[component-name]] - *Purpose: ...*
- <% tp.file.cursor(6) %>

**Component Synergies**:
<!-- Document how components work together -->
<% tp.file.cursor(7) %>

---
`;
} else {
    tR += `<% tp.file.cursor(6) %>\n<% tp.file.cursor(7) %>\n\n---\n\n`;
}

// Conditional: Testing Section
if (needsTesting) {
    tR += `
## 🧪 Testing & Validation

### Test Objective
<!-- What are you testing? What's the success criteria? -->

<% tp.file.cursor(8) %>

### Test Case 1
**Input/Scenario**:
<% tp.file.cursor(9) %>

**Expected Output**:
<% tp.file.cursor(10) %>

**Actual Output**:
<!-- Fill after testing -->

**Result**: [ ] Pass  [ ] Fail

**Quality Score**: __ / 10

**Issues Found**:
-

**Link to Test Results**: [[test-result-link]]

### Test Case 2 (Optional)
<!-- Add more test cases as needed -->

<% tp.file.cursor(11) %>

---

`;
} else {
    tR += `<% tp.file.cursor(8) %>\n<% tp.file.cursor(9) %>\n<% tp.file.cursor(10) %>\n<% tp.file.cursor(11) %>\n\n---\n\n`;
}

// Always include: Metadata section
tR += `
## 📊 Metadata & Tracking

**Status**: \`VIEW[{status}]\`
**Maturity**: \`VIEW[{maturity}]\`
**Confidence**: \`VIEW[{confidence}]\`
**Rating**: \`VIEW[{rating}]\` / 10
**Usage Count**: \`VIEW[{usage-count}]\`
**Last Used**: \`VIEW[{last-used}]\`

**Target Models**: ${modelList.join(", ")}

**Review Schedule**:
- **Next Review**: ${reviewDate}
- **Interval**: 7 days

---

## 📝 Version History

| Version | Date | Changes | Quality Δ | Link |
|---------|------|---------|-----------|------|
| 1.0.0   | ${dateStamp} | Initial creation | N/A | Current |

**Version Bump Guide**:
- **Patch** (1.0.X): Minor tweaks, typo fixes
- **Minor** (1.X.0): Significant improvements, new sections
- **Major** (X.0.0): Complete restructure, different approach

---

## ✅ Quality Checklist

> [!important] Pre-Deployment Validation
> Complete before marking as \`production\` status

- [ ] **Clarity**: Instructions are unambiguous
- [ ] **Completeness**: All necessary context provided
- [ ] **Testability**: Success criteria are measurable
- [ ] **Format**: Output format is clearly specified
- [ ] **Constraints**: Boundaries are explicitly stated
- [ ] **Examples**: At least one example provided (if applicable)
- [ ] **Components**: Linked to relevant SPES components (if applicable)
- [ ] **Testing**: Tested with at least one real input
- [ ] **Rating**: Quality rating assigned based on performance
- [ ] **Links**: Minimum 2 inlinks and 2 outlinks (graph health)

---

## 🔗 Related Prompts

\`\`\`dataviewjs
// Find semantically related prompts
const currentFile = dv.current();
const currentTags = currentFile.tags || [];
const currentCategory = currentFile["prompt-category"];

const relatedPrompts = dv.pages('"02-projects/_spes-sequential-prompt-engineering-system" or "03-notes/prompt-engineering"')
    .where(p => p.file.path !== currentFile.file.path)
    .where(p => p.type === "prompt")
    .where(p => {
        // Match by category
        if (p["prompt-category"] === currentCategory) return true;
        // Match by shared tags
        const sharedTags = (p.tags || []).filter(t => currentTags.includes(t));
        return sharedTags.length >= 2;
    })
    .sort(p => p.rating, 'desc')
    .limit(5);

if (relatedPrompts.length > 0) {
    dv.table(
        ["Prompt", "Type", "Category", "Rating", "Status"],
        relatedPrompts.map(p => [
            p.file.link,
            p["prompt-type"],
            p["prompt-category"],
            p.rating + "/10",
            p.status
        ])
    );
} else {
    dv.paragraph("*No related prompts found yet. Create more prompts in this category!*");
}
\`\`\`

---

## 🔗 Graph Connections

**Link to**:
- [[prompt-engineering-moc]] - Main MOC
- [[${dateStamp}]] - Daily note
- [[${tp.date.now("gggg-[W]WW")}]] - Weekly review

**Additional Links**:
- <% tp.file.cursor(12) %>

---

## 💡 Usage Notes & Lessons Learned

<!-- Document insights from using this prompt -->

<% tp.file.cursor(13) %>

**Next Steps**:
- [ ] Test with sample inputs
- [ ] Refine based on results
- [ ] Update rating after testing
- [ ] Link to related prompts
- [ ] Consider extracting reusable components

---

## 🎯 Success Criteria

<!-- How do you know this prompt is working well? -->

<% tp.file.cursor(14) %>

---

*Generated: ${dateStamp} | Template: SPES General-Purpose v1.0.0 | ID: ${timestamp}*
*Part of SPES (Sequential Prompt Engineering System)*
`;

// Step 5: Rename file to generated name
await tp.file.rename(fileName);
new Notice(`✅ Created: ${fileName}`);
_%>
