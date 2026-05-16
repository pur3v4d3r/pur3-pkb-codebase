# DeweyCT

Interactive companion to John Dewey's *How We Think* (1933 revised edition).

## Stack

| Layer | Tech |
|-------|------|
| Frontend | Next.js 14 (App Router), TypeScript, Tailwind CSS |
| Backend | Python 3.11+, FastAPI, Uvicorn |
| AI | Anthropic Claude API |
| Storage | localStorage (V1) |
| Deploy | Frontend → Vercel, Backend → Railway/Render |

## Project Structure

```
dewey-ct/
├── frontend/          # Next.js app
├── backend/           # FastAPI service
│   ├── main.py
│   ├── requirements.txt
│   └── routers/
│       ├── qa.py      # Socratic Q&A endpoint
│       └── feedback.py # Template feedback endpoint
├── data/              # Canonical JSON data
│   ├── chapters/      # chapter-01.json … chapter-19.json
│   ├── frameworks/    # 15 framework JSONs
│   └── templates/     # 5 template JSONs
└── README.md
```

## Quick Start

### Frontend (Development)

```bash
cd frontend
npm install
npm run dev
# → http://localhost:3000
```

### Backend (Development)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp ../.env.example .env     # then add your ANTHROPIC_API_KEY
uvicorn main:app --reload --port 8000
# → http://localhost:8000/health
```

## Environment Variables

See `.env.example`. The only required secret is `ANTHROPIC_API_KEY`.

## Data

All content is derived from the 1933 revised edition of *How We Think* by John Dewey, plus 15 modern critical-thinking frameworks. JSON files live in `data/` and are copied to `frontend/public/data/` for static serving.

## Phases

- **Phase 0** (current): Chapter library, framework reference, static data
- **Phase 1**: Interactive templates, portfolio (localStorage)
- **Phase 2**: AI Q&A and feedback (requires backend + API key)
- **Phase 3**: Exercises, progress tracking, export
