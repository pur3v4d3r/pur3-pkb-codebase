<%*
// FILE NAMING AUTOMATION
// Convention: claude-project-[semantic-title]-[version]-[timestamp].md

const semanticTitle = await tp.system.prompt("Project semantic title:");
if (!semanticTitle) {
    throw new Error("❌ Cancelled: No title provided");
}

const sanitized = semanticTitle.toLowerCase().trim().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '').replace(/-+/g, '-').replace(/^-|-$/g, '');
const version = "1.0.0";
const timestamp = tp.date.now("YYYY-MM-DD-HH-mm-ss");
const filename = `claude-project-${sanitized}-${version}-${timestamp}`;

await tp.file.rename(filename);
_%>
---
type: "claude-project"
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
claude-model: "<% await tp.system.suggester(["Claude Sonnet 4.5 (Default)", "Claude Opus 4.5 (Advanced)", "Claude Haiku 3.5 (Fast)"], ["sonnet-4.5", "opus-4.5", "haiku-3.5"], false, "Model?") %>"
project-url: ""
tags:
  - "year/<% tp.date.now("YYYY") %>"
  - "prompt-engineering/agentic"
  - "platform/claude"
  - "project-type/claude-project"
aliases:
  - "<% tp.file.title %>"
link-up: "[[prompt-engineering-moc]]"
link-related:
  - "[[<% tp.date.now("YYYY-MM-DD") %>|Daily Note]]"
components-used: []
test-results: []
---

> [!abstract] Claude Project Template
> **Purpose**: Configure persistent Claude Projects with custom instructions, knowledge base, and workflow context.
>
> **What is a Claude Project?**
> - Persistent workspace with custom instructions
> - Knowledge base integration (PDFs, docs, code)
> - Conversation history and context persistence
> - Ideal for ongoing work, domain-specific agents, and team collaboration
>
> **Use Cases**:
> - Long-term technical documentation
> - Specialized domain agents (legal, medical, technical)
> - Team workflows with shared context
> - Iterative research projects

> [!metadata] Project Health Check
> **Status**: `VIEW[{status}]` | **Version**: `VIEW[{version}]` | **Rating**: `VIEW[{rating}]`/10
> **Model**: `VIEW[{claude-model}]` | **Confidence**: `VIEW[{confidence}]`
> **Project URL**: `VIEW[{project-url}]`

[Created: [[<% tp.date.now("YYYY-MM-DD") %>|<% tp.date.now("dddd, MMMM Do, YYYY") %>]]]

---

# <% tp.file.title %>

> [!definition] Project Definition
> <!-- One-sentence description of what this project does -->
> <% tp.file.cursor(1) %>

## 🎯 Project Objectives

<!-- What should this Claude Project accomplish? -->
- <% tp.file.cursor(2) %>

## 📚 Knowledge Base Requirements

<!-- What documents/files should be uploaded to the project? -->
- <% tp.file.cursor(3) %>

---

## 🤖 CUSTOM INSTRUCTIONS

### Core Identity & Role

```plaintext
<% tp.file.cursor(4) %>
```

### Domain Expertise

```plaintext
<% tp.file.cursor(5) %>
```

### Behavioral Guidelines

```plaintext
<% tp.file.cursor(6) %>
```

### Output Preferences

```plaintext
<% tp.file.cursor(7) %>
```

### Context Management

```plaintext
How to handle conversation history, when to summarize, what to remember.
```

---

## 📁 KNOWLEDGE BASE SETUP

### Required Documents

| Document | Purpose | Status |
|----------|---------|--------|
| | | ⬜ Not uploaded |

### Document Instructions

<!-- How should Claude use the uploaded documents? -->
-

---

## 🔧 PROJECT CONFIGURATION

### Model Selection
- **Recommended**: `VIEW[{claude-model}]`
- **Rationale**: <% tp.file.cursor(8) %>

### Context Window Strategy
<!-- How to manage the 200k context window -->
- Priority documents:
- Context refresh triggers:

### Conversation Management
<!-- Guidelines for chat organization -->
- New chat triggers:
- Archive strategy:

---

## 💬 STARTER PROMPTS

### Initial Setup Prompt
```plaintext
<!-- First message to establish context -->
```

### Common Workflows

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

<!-- Components frequently used in this project -->

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
**Result**: ✅ Pass | ❌ Fail
**Quality Score**: /10
**Notes**:

---

## 📊 PROJECT METRICS

### Usage Statistics
- **Total Conversations**: `VIEW[{usage-count}]`
- **Last Used**: `VIEW[{last-used}]`
- **Active Chats**: <!-- Manual tracking -->
- **Documents Uploaded**: <!-- From Knowledge Base section -->

### Quality Assessment
- **Instruction Clarity**: /10
- **Context Relevance**: /10
- **Response Quality**: /10
- **Overall Rating**: `VIEW[{rating}]`/10

---

## 🔄 VERSION HISTORY

| Version | Date | Changes | Quality Δ |
|---------|------|---------|-----------|
| 1.0.0 | <% tp.date.now("YYYY-MM-DD") %> | Initial project setup | Baseline |

---

## 🎓 LESSONS LEARNED

<!-- Insights from using this project -->
-

---

## 🔗 RELATED RESOURCES

**Related Projects**:
-

**Component Library**:
- [[00-library-index|Component Library]]

**Templates**:
- [[_prompt-master-template|Master Prompt Template]]
- [[_gemini-gem-template|Gemini Gem Template]]

---

## 📋 DEPLOYMENT CHECKLIST

- [ ] Project created in Claude interface
- [ ] Custom instructions configured
- [ ] Knowledge base documents uploaded
- [ ] Starter prompts tested
- [ ] Project URL added to frontmatter
- [ ] Initial conversation logged
- [ ] Review schedule set

---

## 💡 OPTIMIZATION IDEAS

<!-- Future improvements to consider -->
-

---

*Template Version: 1.0.0 | Created: 2025-12-20 | Claude Project Configuration*
