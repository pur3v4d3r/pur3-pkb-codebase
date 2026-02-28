# 🌐 Obsidian Web Clipper System for Project Pur3v4d3r

> [!abstract] System Overview
> A comprehensive, modular web clipping system designed to integrate seamlessly with your existing PKB architecture. This system leverages the Obsidian Web Clipper's Interpreter AI to replicate the formatting, metadata generation, and knowledge extraction patterns you use with Claude.

---

## 📁 System Architecture

```
webclipper-system/
├── README.md                          # This file
├── templates/
│   ├── pur3v4d3r-universal.json       # Universal catch-all template
│   ├── pur3v4d3r-research-article.json # Academic/research content
│   ├── pur3v4d3r-video-transcript.json # YouTube/video content
│   ├── pur3v4d3r-documentation.json   # Technical docs
│   ├── pur3v4d3r-quick-capture.json   # Fast capture, minimal AI
│   └── pur3v4d3r-definition-extractor.json # Key term extraction
├── interpreter-prompts/
│   ├── universal-pkb-processor.md     # Main processing prompt
│   ├── tag-generator.md               # Taxonomy-aware tagging
│   ├── definition-extractor.md        # Key:: Value extraction
│   └── wiki-link-detector.md          # Concept linking
└── setup-guide.md                     # Installation instructions
```

---

## 🎯 Design Principles

1. **Metadata Fidelity**: Every clipped note matches your existing YAML frontmatter schema
2. **Taxonomy Compliance**: Tags generated from your 577-tag hierarchical system
3. **Progressive Disclosure**: Simple templates for quick capture, advanced for deep processing
4. **Modular Prompts**: Interpreter prompts can be mixed/matched based on content type
5. **Definition Extraction**: Inline `[**Key**:: Value]` fields for Dataview parsing

---

## 🔧 Prerequisites

- Obsidian v1.7.2+
- Obsidian Web Clipper browser extension
- API key for your preferred LLM provider (Anthropic Claude, OpenAI, Google Gemini, or Ollama local)

---

## 📖 Quick Start

1. **Install Web Clipper**: [obsidian.md/clipper](https://obsidian.md/clipper)
2. **Configure Interpreter**: Settings → Interpreter → Enable → Add API Key
3. **Import Templates**: Settings → Templates → Import → Select JSON files
4. **Test Capture**: Visit any article → Click Obsidian icon → Select template → Interpret → Add to Obsidian

---

## 📚 Template Reference

| Template | Use Case | AI Processing | Best For |
|----------|----------|---------------|----------|
| Universal | Catch-all | Full metadata + summary | Articles, blog posts |
| Research Article | Academic content | Deep analysis + definitions | Papers, studies |
| Video Transcript | YouTube/courses | Timestamp extraction | Learning content |
| Documentation | Technical docs | Code extraction + wiki-links | Tutorials, guides |
| Quick Capture | Fast save | Minimal AI | Reference saves |
| Definition Extractor | Key terms | Heavy definition extraction | Glossary building |

---

## 🏷️ Metadata Schema Mapping

Your templates generate this frontmatter structure:

```yaml
---
aliases:
  - [AI-generated aliases]
tags:
  - type/[note-type]        # From typeList
  - year/2025
  - status/[maturity]       # From maturityLevels
  - [domain-tags]           # From groupB1/B2 taxonomy
  - [concept-tags]          # From groupC-J taxonomy
source: [sourceList value]  # article, video, paper, etc.
id: "[YYYYMMDDHHmmss]"
created: "[YYYY-MM-DDTHH:mm:ss]"
modified: "[YYYY-MM-DDTHH:mm:ss]"
week: "[[YYYY-Www]]"
month: "[[YYYY-MM]]"
quarter: "[[YYYY-Qq]]"
year: "[[YYYY]]"
type: [typeList value]
maturity: seedling          # Default for new clips
confidence: provisional     # Default for new clips
next-review: "[7 days from capture]"
review-count: 0
link-up:
  - "[[appropriate-moc]]"   # AI-selected from linkUpList
link-related:
  - "[[YYYY-MM-DD|Daily-Note]]"
---
```

---

## 📂 File Organization

The system saves clips to organized paths based on content type:

- **Research articles**: `03-notes/literature/`
- **Technical docs**: `03-notes/reference/`
- **Videos**: `03-notes/media/`
- **Quick captures**: `00-inbox/webclips/`

Adjust paths in template JSON to match your vault structure.
