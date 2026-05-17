








# Running the Critical Thinking Application
To run the Critical Thinking Application, enter these commands into PowerShell:

```powershell

cd "d:\10_pur3v4d3r's-vault\999-critical-thinking-app\dewey-ct\frontend"
npm run dev

```

`npm run dev` now starts **both** the FastAPI backend (port 8000) and the Next.js frontend (port 3001) together via `concurrently`.

To run them separately:
```powershell
npm run dev:frontend   # Next.js only
npm run dev:backend    # FastAPI/uvicorn only
```
## Opening the Application

After running the above command, the application will start and you should see output in the terminal indicating that the development server is running.
Then open your browser and navigate to:

```html

http://localhost:3000
http://localhost:3001

```


# NOTES ON APPLICATION


# DeweyCT — App Review & Improvement Backlog

## What's there now

**Frontend** (Next.js 15, client-heavy, localStorage for state):
- `/` Chapters index • `/chapter/[id]` reader • `/frameworks` + per-framework pages • `/mental-models` • `/cheat-sheets` • `/templates` • `/practice` • `/ask` (LLM Q&A) • `/portfolio` (+ detail/download) • `/review` (SM-2 SRS, 63 cards) • `/assess` (32-disposition self-rating)

**Backend** (FastAPI): only `qa` + `feedback` routers; CORS wide-open (`allow_origins=["*"]`).

**Data**: 30 framework JSONs, chapters, templates, practice problems, worked examples.

---

## A. Critical issues (do first)

1. **CORS wildcard** — `allow_origins=["*"]` in main.py. Lock to `http://localhost:3001` (+ prod origin via env var).
2. **No request-size / rate limiting on `/api/qa`** — any LLM endpoint without throttling is a wallet-burn vector. Add `slowapi` or simple in-memory limiter.
3. **localStorage is the only persistence layer** — Portfolio, SRS progress, chapter reading state, assessments all live in one browser. Loss = total loss. Need (a) export-all-data button and (b) import-from-JSON to migrate browsers.
4. **No error boundaries** — a single client fetch failure on `/review` or `/assess` whitescreens the route. Wrap each page route in a small `ErrorBoundary` that surfaces the message + a retry button.

## B. High-leverage feature additions

5. **Global search (Cmd-K palette)** — index chapters, frameworks, mental models, fallacies, templates client-side; fuzzy-search with `cmdk` or `fuse.js`. This is the single biggest UX win for a content-dense app.
6. **Cross-link Assess → Review → Templates** — when an Assess shows low scores on a disposition (e.g., "Open-mindedness"), recommend (a) specific chapter sections, (b) related fallacies to drill in `/review`, (c) the Browne-Keeley template. Turns the assessment from an isolated number into an actionable next-step.
7. **Highlights & margin notes on chapter pages** — text-selection → save as `'reflection'` portfolio entry with `chapterRef`. Pairs naturally with existing portfolio detail view.
8. **Practice problem worked-example reveal** — `data/worked-examples/` exists but I'd verify it's wired. If not: progressive disclosure (hint → partial → full solution), saved to portfolio with which level of hint was used.
9. **SRS analytics page** — `/review/stats`: cards-due-by-day heatmap, retention rate (% Good+Easy), per-source breakdown, longest streak. Currently you have the SRS but no visibility into how it's going.
10. **Tagging + filtering on Portfolio** — `PortfolioEntry.tags` already exists but isn't surfaced. Add a tag-filter pill bar at `/portfolio` and tag chips on each card.

## C. Content/depth additions

11. **Add fallacy → real-world example pairs** — most `logical-fallacies.json` entries probably have abstract examples. A "spot-the-fallacy" practice mode (paragraph → multiple-choice) would compound the SRS work.
12. **Dewey passage → modern-framework crosswalk** — sidebar on chapter pages: "This passage maps to [Paul-Elder Standards: Clarity, Logic]". You already have `cross-framework-synthesis.json`; mine it.
13. **Argument-map builder** — Toulmin (claim/warrant/data/backing/rebuttal) as a structured form template, save as portfolio entry, render as a diagram on the detail view.
14. **Assess sub-scores by cluster** — currently `/assess` shows section averages (Ennis/Delphi) and one overall. Add per-cluster (e.g., "Care that beliefs are true" sub-score) so users see which behavior pattern is weakest, not just which framework.
15. **Trend chart on `/assess`** — if 3+ past assessments exist, render a sparkline per disposition. Pure CSS or `recharts`.

## D. Backend hardening

16. **Move LLM provider behind an interface** — single `services/llm.py` with `complete(prompt) -> str`; swap OpenAI/Anthropic/local via env. Currently each router likely calls SDK directly.
17. **Cache QA responses** — same question → same answer for N hours. SQLite or `cachetools.TTLCache`. Cheap, fast win.
18. **Structured logging** — `logging` with JSON formatter; log every QA call with `prompt_hash`, `tokens`, `latency_ms`. Without this you can't tune costs.
19. **`/health` should check downstream** — currently returns hardcoded `"ok"`. Verify LLM key present, data dir readable.
20. **Add `/api/export` and `/api/import`** — even if localStorage stays client-side, optional server-side backup endpoint (gated by an auth token in env) gives users an opt-in safety net.

## E. UX polish

21. **Dark mode** — Tailwind + `next-themes`. Slate palette already chosen — easy port.
22. **Keyboard shortcuts on `/review`** — `1`/`2`/`3`/`4` for Again/Hard/Good/Easy, `Space` for show-answer. Current click-based flow is slow.
23. **Mobile review polish** — slider thumb targets and rating buttons need ≥44px tap targets; verify on a real phone width.
24. **Print stylesheet for `/cheat-sheets`** — these are reference material; users will want to print. `@media print` rules to strip nav/chrome.
25. **Page transitions + skeleton loaders** — current loading text ("Loading dispositions…") is fine but feels static. Skeleton blocks matching final layout reduce perceived latency.
26. **Sticky section nav on long chapter pages** — TOC drawer on the right, scroll-spy.

## F. Testing & DX

27. **Zero tests right now** (I'd bet). Add at minimum: Vitest for `lib/srs.ts` (SM-2 math is the highest-risk piece), `lib/storage.ts`. Maybe Playwright smoke for the 3 routes that hit localStorage.
28. **Pre-commit hook** — `husky` + `lint-staged` running `eslint --fix` and `tsc --noEmit`.
29. **README.md quickstart** — verify it covers env setup, both `npm run dev` and `uvicorn`, and the data directory.
30. **CI** — GitHub Actions: `tsc`, `eslint`, `pytest` on every push. Even just type-check catches regressions for free.

---

## Suggested next 3 (in order)

1. **#5 Cmd-K global search** — highest user-facing leverage; touches no backend; ~1 day.
2. **#6 Assess → recommendation engine** — closes the loop on the feature you just shipped; turns it from a measurement into a practice tool.
3. **#1 + #2 + #4 security/error hardening** — boring but irresponsible to skip before any deployment.






---

Im working on building an app for Critical thinking, its a full stack app with a FastAPI backend and Next.js frontend. The app is designed to help users learn and practice critical thinking skills through a structured curriculum, interactive exercises, and an AI tutor.
Review the files and then start the task.

## KEY LOCATIONS

D:\10_pur3v4d3r's-vault\999-critical-thinking-app

## TASK

**8. Spaced repetition review queue**  
Flash-card style review for mental model definitions, framework cheat sheets, and Dewey concepts — with a simple SM-2 scheduling algorithm. Entirely client-side (localStorage). High retention value, ~1 week of build time.













