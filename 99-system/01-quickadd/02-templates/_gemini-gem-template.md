<%*
// FILE NAMING AUTOMATION
// Convention: gemini-gem-[semantic-title]-[version]-[timestamp].md

const semanticTitle = await tp.system.prompt("Gem semantic title:");
if (!semanticTitle) {
    throw new Error("❌ Cancelled: No title provided");
}

const sanitized = semanticTitle.toLowerCase().trim().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '').replace(/-+/g, '-').replace(/^-|-$/g, '');
const version = "1.0.0";
const timestamp = tp.date.now("YYYY-MM-DD-HH-mm-ss");
const filename = `gemini-gem-${sanitized}-${version}-${timestamp}`;

await tp.file.rename(filename);
_%>
---
type: "gemini-gem"
id: "<% tp.date.now("YYYYMMDDHHmmss") %>"
status: "<% await tp.system.suggester(["Active", "Testing", "Production", "Deprecated", "Archived"], ["active", "testing", "production", "deprecated", "archived"], false, "Status?") %>"
version: "1.0.0"
rating: "0.0"
source: "original"
created: "<% tp.date.now("YYYY-MM-DD") %>"
modified: "<% tp.date.now("YYYY-MM-DD") %>"
usage-count: 0
last-used: ""
review-next: "<% tp.date.now("YYYY-MM-DD", 14) %>"
review-interval: 14
review-count: 0
confidence: "<% await tp.system.suggester(["Speculative", "Provisional", "Moderate", "Established", "High"], ["speculative", "provisional", "moderate", "established", "high"], false, "Confidence?") %>"
maturity: "seedling"
priority: "<% await tp.system.suggester(["Low", "Medium", "High", "Urgent"], ["low", "medium", "high", "urgent"], false, "Priority?") %>"
gemini-model: "<% await tp.system.suggester(["Gemini 2.0 Flash Thinking (Latest)", "Gemini 2.0 Flash (Default)", "Gemini 1.5 Pro (Advanced)", "Gemini 1.5 Flash (Fast)"], ["gemini-2.0-flash-thinking", "gemini-2.0-flash", "gemini-1.5-pro", "gemini-1.5-flash"], false, "Model?") %>"
gem-url: ""
tags:
  - "year/<% tp.date.now("YYYY") %>"
  - "prompt-engineering/agentic"
  - "platform/gemini"
  - "project-type/gemini-gem"
aliases:
  - "<% tp.file.title %>"
link-up: "[[prompt-engineering-moc]]"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily Note]]"
components-used: []
test-results: []
---

> [!abstract] Gemini Gem Template
> **Purpose**: Configure reusable Gemini Gems with custom instructions and specialized behaviors.
>
> **What is a Gemini Gem?**
> - Customizable AI assistant with persistent instructions
> - Shareable via URL or within Google Workspace
> - Supports multimodal inputs (text, images, audio, video)
> - Ideal for specialized tasks, team workflows, and domain expertise
>
> **Use Cases**:
> - Specialized assistants (writing coach, code reviewer, research assistant)
> - Domain experts (legal advisor, medical consultant, technical specialist)
> - Team collaboration tools with shared context
> - Workflow automation agents

> [!metadata] Gem Health Check
> **Status**: `VIEW[{status}]` | **Version**: `VIEW[{version}]` | **Rating**: `VIEW[{rating}]`/10
> **Model**: `VIEW[{gemini-model}]` | **Confidence**: `VIEW[{confidence}]`
> **Gem URL**: `VIEW[{gem-url}]`

[Created: [[<% tp.date.now("YYYY-MM-DD") %>|<% tp.date.now("dddd, MMMM Do, YYYY") %>]]]

---

# <% tp.file.title %>

> [!definition] Gem Definition
> <!-- One-sentence description of what this Gem does -->
> <% tp.file.cursor(1) %>

## 🎯 Gem Objectives

<!-- What should this Gemini Gem accomplish? -->
- <% tp.file.cursor(2) %>

## 🎨 Gem Personality

<!-- What's the tone and style of this Gem? -->
- <% tp.file.cursor(3) %>

---

## 🤖 GEM INSTRUCTIONS

### Core Identity & Role

```plaintext
<% tp.file.cursor(4) %>
```

### Domain Knowledge

```plaintext
<% tp.file.cursor(5) %>
```

### Interaction Style

```plaintext
<% tp.file.cursor(6) %>
```

### Output Format & Structure

```plaintext
<% tp.file.cursor(7) %>
```

### Special Capabilities

```plaintext
What unique features or abilities should this Gem have?
```

---

## 🔧 GEM CONFIGURATION

### Model Selection
- **Recommended**: `VIEW[{gemini-model}]`
- **Rationale**: <% tp.file.cursor(8) %>

### Multimodal Capabilities
<!-- Which input types does this Gem support? -->
- Text: ✅
- Images: ☐
- Audio: ☐
- Video: ☐
- Code: ☐

### Response Settings
<!-- How should the Gem respond? -->
- Length preference:
- Detail level:
- Creativity vs. Precision:

---

## 💬 STARTER PROMPTS

### Introduction Prompt
```plaintext
<!-- First prompt to introduce users to the Gem -->
```

### Example Workflows

#### Workflow 1: [Name]
```plaintext
```

#### Workflow 2: [Name]
```plaintext
```

#### Workflow 3: [Name]
```plaintext
```

---

## 🧩 COMPONENT LIBRARY

<!-- Components frequently used in this Gem -->

**Personas**:
-

**Instructions**:
-

**Constraints**:
-

**Formats**:
-

---

## 🧪 TESTING & VALIDATION

### Test Scenario 1
**Date**:
**Objective**:
**Input**:
**Expected Output**:
**Actual Output**:
**Result**: ✅ Pass | ❌ Fail
**Quality Score**: /10
**Notes**:

---

## 📊 GEM METRICS

### Usage Statistics
- **Total Interactions**: `VIEW[{usage-count}]`
- **Last Used**: `VIEW[{last-used}]`
- **Shared With**: <!-- Manual tracking -->

### Quality Assessment
- **Instruction Clarity**: /10
- **Response Relevance**: /10
- **User Satisfaction**: /10
- **Overall Rating**: `VIEW[{rating}]`/10

---

## 🔄 VERSION HISTORY

| Version | Date | Changes | Quality Δ |
|---------|------|---------|-----------|
| 1.0.0 | <% tp.date.now("YYYY-MM-DD") %> | Initial Gem creation | Baseline |

---

## 🎓 LESSONS LEARNED

<!-- Insights from using this Gem -->
-

---

## 🔗 RELATED RESOURCES

**Related Gems**:
-

**Component Library**:
- [[00-library-index|Component Library]]

**Templates**:
- [[_prompt-master-template|Master Prompt Template]]
- [[_claude-project-template|Claude Project Template]]

---

## 📋 DEPLOYMENT CHECKLIST

- [ ] Gem created in Google AI Studio
- [ ] Instructions configured
- [ ] Model selected
- [ ] Starter prompts tested
- [ ] Gem URL generated
- [ ] URL added to frontmatter
- [ ] Shared with team (if applicable)
- [ ] Initial usage logged

---

## 💡 OPTIMIZATION IDEAS

<!-- Future improvements to consider -->
-

---

## 🌐 SHARING & COLLABORATION

### Share Settings
- **Public Link**: `VIEW[{gem-url}]`
- **Access Level**: <!-- Private/Workspace/Public -->
- **Shared With**: <!-- List team members -->

### Usage Guidelines
<!-- How should others use this Gem? -->
-

---

*Template Version: 1.0.0 | Created: 2025-12-20 | Gemini Gem Configuration*
