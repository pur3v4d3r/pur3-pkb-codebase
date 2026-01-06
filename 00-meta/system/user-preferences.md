---
tags: #meta #system #user-profile #preferences
aliases: [User Profile, Workflow Preferences, User Config]
status: evergreen
certainty: ^verified
created: 2025-12-16
---

# User Preferences

> [!abstract] Purpose
> Centralized documentation of discovered user workflow patterns, communication preferences, and vault management style.

---

## 🗣️ Communication Preferences

### Response Style
- **Conciseness**: No conversational filler or preambles
- **Action-Oriented**: Direct task execution over explanation
- **Format**: Production-ready output (no "Here's what I created...")
- **Efficiency**: Values speed and directness

### Feedback Style
- Direct questions when clarification needed
- Prefers options presented with clear reasoning
- Values architectural thinking ("which is best" vs "can you do this")

---

## 🏗️ Vault Management Philosophy

### Core Principles
- **Knowledge as Code**: Treats PKB with software engineering rigor
- **Graph Integrity**: Strong emphasis on link density and connectivity
- **Anti-Duplication**: Reconnaissance before creation (mandatory)
- **Atomicity**: One concept = One file

### Quality Standards
- Every note needs 2+ incoming and 2+ outgoing links
- Proper YAML frontmatter (5-tag system) is non-negotiable
- Wiki-links only for internal references
- LaTeX for all mathematical notation

---

## 🔧 Technical Environment

### Setup
- **Editor**: VS Code
- **Platform**: Windows (based on file paths)
- **KB System**: Obsidian vault
- **Version Control**: Git (implied by .claude/ structure)

### Directory Conventions
- Numerical prefixes for ordering (00-, 01-, etc.)
- Kebab-case for multi-word names
- System files in hidden directories (.claude/)

---

## 📋 Task Management Style

### Project Approach
- Appreciates phased implementation
- Values architectural decisions over immediate coding
- Prefers seeing structure before content

### Decision Making
- Asks for "best option" when presented with choices
- Trusts expert recommendation with clear rationale
- Direct approval style ("yes commence the operation")

---

## 🎯 Known Priorities

### High Priority
1. Graph connectivity (prevent orphans)
2. Metadata consistency
3. Duplication prevention
4. System reliability (session persistence)

### Medium Priority
- MOC creation when clusters emerge
- Dataview query optimization
- Format standardization

---

## 🚫 Dislikes / Avoid

- Conversational filler ("I'd be happy to...", "Let me explain...")
- Broken or unverified links
- Markdown links for internal files
- Creating files without reconnaissance
- Long explanations before action
- System hangs or unexplained delays

---

## 🔗 Related

- [[session-memory]] - Active session context
- [[vault-map]] - Structural patterns
- [[project-tracker]] - Current work

---

*Profile Confidence: High | Last Updated: 2025-12-16*
