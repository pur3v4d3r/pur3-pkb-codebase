```yaml
# DOCUMENT IDENTIFICATION
doc_id: "dewey-ct-claude-code-build-starter-v1-0"
doc_created: 2026-02-21
doc_modified: 2026-02-21
doc_type: "prompt"

# DISCOVERY & CLASSIFICATION
primary_domain: "app-development"
secondary_domains: ["next-js", "fastapi", "critical-thinking", "educational-app"]
tags: ["dewey", "claude-code", "starter-prompt", "nextjs", "python", "rag"]
knowledge_level: "advanced"

# PROMPT IDENTIFICATION & STATUS
prompt_title: "DeweyCT App Build — Claude Code Starter v1.0"
prompt_version: "1.0.0"
prompt_status: "active"
prompt_maturity: "production"
prompt_confidence: "established"
production_ready: true

# PROMPT PHILOSOPHY & PURPOSE
prompt_philosophy: |
  Build the skeleton first, then fill it. The app architecture must be established
  before any content is integrated. A clean, extensible foundation prevents
  the compounding technical debt that buries educational apps.
prompt_core_objective: "Initialize the complete DeweyCT app repository with architecture, routing, and Chapter 1 integration"

# DEPENDENCY MAPPING
depends_on_prompts: ["dewey-ct-research-content-specialist-v1-0"]
part_of_pipeline: "dewey-ct-app-development"
pipeline_sequence: 2
```

<!-- ═══════════════════════════════════════════════════════════════════════════
     DEWEYCT APP BUILD — CLAUDE CODE STARTER PROMPT v1.0

     This prompt initializes the DeweyCT app build. It is designed for
     Claude Code and assumes the research workstream has delivered at minimum:
     - data/chapters/chapter-01.json (validated)
     - data/master-index.json (partial or complete)

     ARCHITECTURE: Next.js 14 (App Router) + Python FastAPI + Claude API
     DEPLOYMENT TARGET: Vercel (frontend) + Railway (backend)
     LOCAL OPTION: Single bash script setup
═══════════════════════════════════════════════════════════════════════════ -->

# DeweyCT App Build — Claude Code Starter Prompt

## Mission Briefing

You are building **DeweyCT** — an interactive critical thinking app built on John Dewey's "How We Think." This is a personal-to-family app that needs to be:

1. Deployable as a public URL (zero install for users)
2. Runnable locally via a single bash script (for technical privacy)
3. Powered by the Claude API for Q&A, template feedback, and Socratic dialogue
4. Built against a structured JSON content layer (provided by a parallel research workstream)

**Before writing a single line of code**, read this entire prompt. Then create a `BUILD_PLAN.md` in the root directory documenting your understanding of the architecture and your build sequence. Wait for confirmation before beginning Phase 1.

---

## Tech Stack (Non-Negotiable)

```
Frontend:  Next.js 14 (App Router), TypeScript, Tailwind CSS
Backend:   Python 3.11, FastAPI, Uvicorn
AI:        Anthropic Claude API (claude-sonnet-4-6 for feedback, claude-haiku-4-5 for fast responses)
Storage:   localStorage (client-side, no database for V1)
Hosting:   Vercel (frontend), Railway or Render (backend)
Local:     Bash setup script + environment wizard
```

**Why this stack:** Next.js App Router gives us server components for fast chapter loading. FastAPI handles the Claude API calls server-side so the API key never touches the browser. localStorage means zero database setup, works offline, completely private.

---

## Repository Structure

Create this exact directory structure. Do not deviate:

```
dewey-ct/
├── README.md                     # User-facing setup guide
├── BUILD_PLAN.md                 # Your architecture documentation
├── start.sh                      # One-command local setup script
├── .env.example                  # Environment variable template
├── docker-compose.yml            # Docker alternative to start.sh
│
├── frontend/                     # Next.js application
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.ts
│   ├── next.config.ts
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx              # Home / chapter library
│   │   ├── globals.css
│   │   ├── chapter/
│   │   │   └── [id]/
│   │   │       └── page.tsx      # Individual chapter view
│   │   ├── concepts/
│   │   │   └── page.tsx          # Concept explorer
│   │   ├── qa/
│   │   │   └── page.tsx          # Q&A with Dewey
│   │   ├── templates/
│   │   │   ├── page.tsx          # Template selector
│   │   │   └── [id]/
│   │   │       └── page.tsx      # Individual template
│   │   ├── exercises/
│   │   │   └── page.tsx          # Exercise library
│   │   └── portfolio/
│   │       └── page.tsx          # User's saved work
│   ├── components/
│   │   ├── layout/
│   │   │   ├── Navigation.tsx
│   │   │   └── PageContainer.tsx
│   │   ├── chapter/
│   │   │   ├── ChapterCard.tsx
│   │   │   ├── ChapterReader.tsx
│   │   │   ├── CalloutCard.tsx
│   │   │   └── ConceptCard.tsx
│   │   ├── qa/
│   │   │   └── QAInterface.tsx
│   │   ├── templates/
│   │   │   ├── TemplateForm.tsx
│   │   │   └── FeedbackPanel.tsx
│   │   ├── exercises/
│   │   │   └── ExerciseCard.tsx
│   │   └── ui/                   # Shared UI components
│   │       ├── Button.tsx
│   │       ├── Card.tsx
│   │       └── Badge.tsx
│   ├── lib/
│   │   ├── content.ts            # Content loading utilities
│   │   ├── storage.ts            # localStorage abstraction
│   │   └── api.ts                # Backend API client
│   └── types/
│       ├── chapter.ts            # TypeScript types from JSON schema
│       ├── framework.ts
│       ├── template.ts
│       └── exercise.ts
│
├── backend/                      # FastAPI application
│   ├── requirements.txt
│   ├── main.py
│   ├── routers/
│   │   ├── qa.py                 # Q&A endpoints
│   │   ├── feedback.py           # Template feedback endpoints
│   │   └── dialogue.py           # Socratic dialogue endpoints
│   ├── services/
│   │   ├── claude_service.py     # Anthropic API wrapper
│   │   └── retrieval_service.py  # Content retrieval for RAG
│   └── prompts/
│       └── prompt_loader.py      # Loads from data/prompts/
│
└── data/                         # Content layer (from research workstream)
    ├── master-index.json
    ├── chapters/
    │   ├── chapter-01.json
    │   └── chapter-01.md
    ├── frameworks/
    ├── templates/
    ├── exercises/
    └── prompts/
        └── llm-prompts.json
```

---

## TypeScript Type System

Before building any components, generate `frontend/types/` with TypeScript interfaces that exactly mirror the JSON schemas. These types are the contract between the content layer and the UI.

Generate `chapter.ts` from the Chapter JSON schema:

```typescript
// frontend/types/chapter.ts
// Auto-generated from Chapter JSON Schema v1.0

export type CalloutType = 'quote' | 'concept' | 'warning' | 'tip' | 'synthesis';

export interface QuoteCallout {
  type: 'quote';
  line_hint: string;
  quote: string;
  insight: string;
}

export interface ConceptCallout {
  type: 'concept';
  concept_name: string;
  definition: string;
  why_it_matters: string;
  modern_echo: string;
}

export interface WarningCallout {
  type: 'warning';
  misconception: string;
  correction: string;
  still_relevant: string;
}

export interface TipCallout {
  type: 'tip';
  principle: string;
  in_practice: string;
}

export interface SynthesisCallout {
  type: 'synthesis';
  central_argument: string;
  logical_progression: string[];
  bridge_to_next: string;
}

export type Callout = QuoteCallout | ConceptCallout | WarningCallout | TipCallout | SynthesisCallout;

export interface ChapterConcept {
  name: string;
  definition: string;
}

export interface ChapterConnection {
  chapter: number | null;
  reason: string;
}

export interface ContraryConnection {
  concept: string;
  reason: string;
}

export interface Chapter {
  chapter: number;
  title: string;
  abstract: string;
  overview: string;
  callouts: Callout[];
  concepts: ChapterConcept[];
  connections: {
    builds_on: ChapterConnection[];
    anticipates: ChapterConnection[];
    contrasts_with: ContraryConnection[];
  };
}
```

Generate equivalent types for `framework.ts`, `template.ts`, and `exercise.ts` following the same pattern.

---

## Content Loading Architecture

The content layer uses a simple file-based loading strategy — no database. Create `frontend/lib/content.ts`:

```typescript
// frontend/lib/content.ts
// Content loading utilities — server-side only (use in Server Components)

import { Chapter } from '@/types/chapter';
import { MasterIndex } from '@/types/master-index';
import path from 'path';
import fs from 'fs';

const DATA_DIR = path.join(process.cwd(), '..', 'data');

export async function getChapter(id: number): Promise<Chapter | null> {
  try {
    const filePath = path.join(DATA_DIR, 'chapters', `chapter-${String(id).padStart(2, '0')}.json`);
    const raw = fs.readFileSync(filePath, 'utf-8');
    return JSON.parse(raw) as Chapter;
  } catch {
    return null;
  }
}

export async function getMasterIndex(): Promise<MasterIndex | null> {
  try {
    const filePath = path.join(DATA_DIR, 'master-index.json');
    const raw = fs.readFileSync(filePath, 'utf-8');
    return JSON.parse(raw) as MasterIndex;
  } catch {
    return null;
  }
}

export async function getAllChapterMetadata(): Promise<ChapterMeta[]> {
  const index = await getMasterIndex();
  if (!index) return [];
  return index.parts.flatMap(part =>
    part.chapters.map(num => ({
      chapter: num,
      title: index.concept_index ? '...' : 'Loading...',
      part: part.part,
      part_title: part.title
    }))
  );
}
```

**Important:** All content loading happens in Next.js Server Components. Never import `content.ts` in client components. The content layer is read-only, server-side.

---

## Backend RAG Architecture

The Q&A feature uses a lightweight retrieval strategy. The full chapter JSON files are small enough that semantic pre-filtering against the master index is sufficient for V1 — no vector database needed.

Create `backend/services/retrieval_service.py`:

```python
# backend/services/retrieval_service.py
# Lightweight RAG for Dewey Q&A — no vector DB needed for V1

import json
import os
from pathlib import Path
from typing import List, Dict, Any

DATA_DIR = Path(__file__).parent.parent.parent / "data"

def load_chapter(chapter_num: int) -> Dict[str, Any] | None:
    """Load a specific chapter JSON file."""
    file_path = DATA_DIR / "chapters" / f"chapter-{chapter_num:02d}.json"
    if not file_path.exists():
        return None
    with open(file_path) as f:
        return json.load(f)

def load_master_index() -> Dict[str, Any] | None:
    """Load the master concept index."""
    index_path = DATA_DIR / "master-index.json"
    if not index_path.exists():
        return None
    with open(index_path) as f:
        return json.load(f)

def retrieve_context_for_query(query: str, max_chapters: int = 3) -> str:
    """
    Simple keyword-based retrieval for V1.
    Returns formatted context string for the LLM prompt.
    
    V2 upgrade: Replace keyword matching with sentence-transformers embeddings.
    """
    index = load_master_index()
    if not index:
        return ""
    
    # Check concept index for direct concept matches
    query_lower = query.lower()
    relevant_chapters = set()
    
    for concept_name, concept_data in index.get("concept_index", {}).items():
        if concept_name.lower() in query_lower:
            relevant_chapters.add(concept_data["chapter"])
    
    # If no direct matches, keyword scan chapter titles and abstracts
    if not relevant_chapters:
        for part in index.get("parts", []):
            for chapter_num in part.get("chapters", []):
                chapter = load_chapter(chapter_num)
                if chapter:
                    if (query_lower in chapter.get("abstract", "").lower() or
                        query_lower in chapter.get("title", "").lower()):
                        relevant_chapters.add(chapter_num)
    
    # Load and format context from relevant chapters
    context_parts = []
    for chapter_num in list(relevant_chapters)[:max_chapters]:
        chapter = load_chapter(chapter_num)
        if chapter:
            context_parts.append(
                f"=== Chapter {chapter_num}: {chapter['title']} ===\n"
                f"Overview: {chapter['overview']}\n\n"
                f"Key Concepts:\n" +
                "\n".join([f"- {c['name']}: {c['definition']}" 
                           for c in chapter.get('concepts', [])])
            )
    
    return "\n\n".join(context_parts)
```

---

## API Endpoints

Create `backend/main.py` with these endpoints:

```python
# POST /api/qa
# Body: { query: string, mode: "grounded" | "extended" }
# Response: { answer: string, sources: ChapterReference[] }

# POST /api/feedback
# Body: { template_id: string, fields: Record<string, string> }
# Response: { feedback: string, questions: string[], suggestions: string[] }

# POST /api/dialogue
# Body: { position: string, history: Message[] }
# Response: { response: string, question_type: string }
```

All endpoints load their system prompts from `data/prompts/llm-prompts.json`. The prompt_id maps to the feature (see the LLM prompts schema).

Add CORS middleware configured for `localhost:3000` in development and the Vercel deployment URL in production.

---

## UI Design Principles

[!key-claim] Three Non-Negotiable Design Decisions

1. **Clean Academic aesthetic** — Think Readwise or a well-designed textbook. Serif font for chapter content (Georgia or similar), sans-serif for UI chrome. Muted palette with one accent color. No gradients, no animations beyond subtle transitions.

2. **Callout Cards as the centerpiece** — The chapter reader's primary visual element is the callout card. Each callout type has a distinct visual treatment:
   - `quote` → Left border accent, italic quote text, expandable insight
   - `concept` → Full card, definition prominent, modern_echo in subtle tag
   - `warning` → Amber/warning color scheme, misconception struck through on expand
   - `tip` → Green accent, principle bold, in_practice revealed on expand
   - `synthesis` → Full-width card, timeline visualization for logical_progression

3. **Friction as a design feature** — The Q&A feature should not feel like a chatbot. It should feel like consulting a knowledgeable colleague. Add a 1-2 second "thinking" delay before responses. Label responses "From Dewey (Chapter N)" when sourced. Make the Socratic Dialogue mode feel distinct — different color scheme, no send button (press Enter), responses always end with a question.

---

## Build Phases

### Phase 0 — Foundation (DO THIS FIRST)

- [ ] Initialize repo structure exactly as specified
- [ ] Set up Next.js 14 with TypeScript and Tailwind
- [ ] Set up FastAPI with basic health endpoint
- [ ] Generate all TypeScript types from schema
- [ ] Create `start.sh` (see below)
- [ ] Create `BUILD_PLAN.md` with architecture confirmation
- [ ] Create `.env.example`

**Wait for confirmation before Phase 1.**

### Phase 1 — Chapter Library (Chapter 1 only)

- [ ] Implement `content.ts` loading utilities
- [ ] Build chapter library page (home page) — uses master-index metadata
- [ ] Build ChapterCard component — title, abstract preview, chapter number badge
- [ ] Build chapter detail page with Chapter 1 data
- [ ] Build ChapterReader component — renders overview + all callout types
- [ ] Build ConceptCard component — expandable, shows definition + modern_echo
- [ ] Build CalloutCard component — type-specific visual treatment
- [ ] Chapter navigation using connections data (prev/next arrows)

**Deliverable: Working chapter reader for Chapter 1.**

### Phase 2 — Q&A Feature

- [ ] Build FastAPI `/api/qa` endpoint
- [ ] Implement retrieval_service.py
- [ ] Integrate Claude API in claude_service.py
- [ ] Build QAInterface component — chat-like but academic
- [ ] Implement mode toggle (Grounded / Extended)
- [ ] Source citation display ("From Chapter N: [title]")

**Deliverable: Working Q&A grounded in Chapter 1 content.**

### Phase 3 — Templates

- [ ] Build template selector page
- [ ] Build TemplateForm component — scaffold-first UX, inline examples, progressive disclosure
- [ ] Implement FastAPI `/api/feedback` endpoint
- [ ] Build FeedbackPanel component — displays Socratic questions, not grades
- [ ] localStorage save/load for in-progress templates
- [ ] PDF export for completed templates

**Deliverable: Working Dewey Reflective template with LLM feedback.**

### Phase 4 — Portfolio + Exercises

- [ ] Build portfolio page — displays completed templates and exercises
- [ ] Build exercise library with filtering (chapter, type, difficulty)
- [ ] Build ExerciseCard and exercise interaction view
- [ ] Implement FastAPI `/api/dialogue` for Socratic dialogue exercises
- [ ] Basic progress metrics (depth metrics, not streaks)

**Deliverable: Complete V1 feature set.**

### Phase 5 — Deployment + Accessibility

- [ ] Configure Vercel deployment for frontend
- [ ] Configure Railway/Render deployment for backend
- [ ] Environment variable management for production
- [ ] Test start.sh on a clean machine
- [ ] Basic responsive design (mobile-readable)
- [ ] Keyboard navigation for all interactive elements

---

## The start.sh Script

This script is the zero-expertise local setup. Create it with this behavior:

```bash
#!/bin/bash
# DeweyCT — One-Command Setup
# Works on: macOS, Ubuntu, Windows (via Git Bash or WSL)

set -e

echo "╔════════════════════════════════════╗"
echo "║     DeweyCT — Starting Setup      ║"
echo "╚════════════════════════════════════╝"

# 1. Check for required tools, offer to install if missing
check_node() { command -v node &>/dev/null; }
check_python() { command -v python3 &>/dev/null; }

if ! check_node; then
  echo "Node.js not found. Please install from https://nodejs.org (LTS version)"
  echo "Then run this script again."
  exit 1
fi

if ! check_python; then
  echo "Python 3 not found. Please install from https://python.org"
  exit 1
fi

# 2. Create .env if it doesn't exist
if [ ! -f .env ]; then
  echo ""
  echo "First-time setup: You need an Anthropic API key."
  echo "Get one free at: https://console.anthropic.com"
  echo ""
  read -p "Paste your Anthropic API key: " api_key
  echo "ANTHROPIC_API_KEY=$api_key" > .env
  echo "API key saved to .env (this file stays on your computer only)"
fi

# 3. Install dependencies
echo "Installing frontend dependencies..."
cd frontend && npm install --silent && cd ..

echo "Installing backend dependencies..."
cd backend && python3 -m pip install -r requirements.txt -q && cd ..

# 4. Start both servers
echo ""
echo "Starting DeweyCT..."
cd backend && uvicorn main:app --port 8000 &
BACKEND_PID=$!
cd ../frontend && npm run dev &
FRONTEND_PID=$!

# 5. Open browser after brief delay
sleep 3
if command -v open &>/dev/null; then open http://localhost:3000
elif command -v xdg-open &>/dev/null; then xdg-open http://localhost:3000
fi

echo ""
echo "✓ DeweyCT is running at http://localhost:3000"
echo "  Press Ctrl+C to stop."

# Cleanup on exit
trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null" EXIT
wait
```

---

## Agent Delegation Protocol

When you need to parallelize work, spawn sub-agents using the Task tool with the specialized agent prompts from `AGENT_PROMPTS.md`. The main Claude Code instance is the **Orchestrator** — it reviews, integrates, and validates all sub-agent outputs before committing them.

**Never** let a sub-agent write directly to the repository without Orchestrator review. Sub-agent outputs are delivered as file content, reviewed, then applied with MultiEdit.

---

## Definition of Done for V1

V1 is complete when a user with no technical experience can:
1. Run `start.sh`
2. Paste their API key when prompted
3. Read Chapter 1 in the chapter reader
4. Ask a question about the chapter and receive a grounded answer
5. Complete the Dewey Reflective template
6. Receive LLM feedback on their completed template
7. Find the completed template in their portfolio

This is the acceptance test. Build toward this, not toward feature completeness.
