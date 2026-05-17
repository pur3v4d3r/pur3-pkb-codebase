'use client';

import { useCallback, useEffect, useRef, useState } from 'react';
import Link from 'next/link';
import { SkeletonBlock } from '@/components/ui/Skeleton';
import {
  type SRSCard,
  type UserSRSCard,
  type CardProgress,
  type Quality,
  sm2Update,
  getSRSProgress,
  saveCardProgress,
  resetSRSProgress,
  isDue,
  getNextReviewDate,
  getUserSRSCards,
  saveUserSRSCard,
  deleteUserSRSCard,
  todayISO,
} from '@/lib/srs';
import { generateId } from '@/lib/storage';

// ---- Raw JSON types (minimal — only fields we use) ----

interface RawModel {
  id: string;
  name: string;
  category: string;
  definition: string;
  example?: string;
}

interface RawPhase {
  number: number;
  name: string;
  definition: string;
  dewey_quote?: { text: string };
}

interface RawFallacy {
  id: string;
  name: string;
  category: string;
  definition: string;
  example?: string;
}

interface RawMentalModelsData {
  models: RawModel[];
}

interface RawDeweyData {
  phases: RawPhase[];
}

interface RawFallaciesData {
  fallacies: RawFallacy[];
}

// ---- Card builders ----

function buildCards(
  mm: RawMentalModelsData,
  dw: RawDeweyData,
  fl: RawFallaciesData,
): SRSCard[] {
  const cards: SRSCard[] = [];

  mm.models.forEach((m) => {
    cards.push({
      id: m.id,
      source: 'mental-model',
      category: m.category,
      front: m.name,
      back: m.definition,
      backDetail: m.example,
    });
  });

  dw.phases.forEach((p) => {
    cards.push({
      id: `dewey-phase-${p.number}`,
      source: 'dewey-phase',
      category: "Dewey's Five Phases",
      front: `Phase ${p.number}: ${p.name}`,
      back: p.definition,
      backDetail: p.dewey_quote?.text,
    });
  });

  fl.fallacies.forEach((f) => {
    cards.push({
      id: f.id,
      source: 'fallacy',
      category: f.category,
      front: f.name,
      back: f.definition,
      backDetail: f.example,
    });
  });

  return cards;
}

// ---- Session builder ----

/** Max new (never-reviewed) cards shown per session to avoid first-session overload. */
const MAX_NEW_CARDS = 10;

function buildSession(
  cards: SRSCard[],
  progress: Record<string, CardProgress>,
  filterSource: string,
): SRSCard[] {
  const filtered =
    filterSource === 'all'
      ? cards
      : cards.filter((c) => c.source === filterSource);

  const due = filtered.filter((c) => {
    const p = progress[c.id];
    return p !== undefined && isDue(p);
  });

  const isNew = filtered.filter((c) => progress[c.id] === undefined);
  const newSlice = isNew.slice(0, MAX_NEW_CARDS);

  // Due cards first, then new introductions.
  return [...due, ...newSlice];
}

// ---- Rating config ----

interface Rating {
  label: string;
  quality: Quality;
  sublabel: string;
  className: string;
}

const RATINGS: Rating[] = [
  {
    label: 'Again',
    quality: 0,
    sublabel: "Didn't know",
    className:
      'border-red-200 bg-red-50 text-red-700 hover:bg-red-100 active:bg-red-200',
  },
  {
    label: 'Hard',
    quality: 1,
    sublabel: 'Partial recall',
    className:
      'border-orange-200 bg-orange-50 text-orange-700 hover:bg-orange-100 active:bg-orange-200',
  },
  {
    label: 'Good',
    quality: 3,
    sublabel: 'Knew it',
    className:
      'border-green-200 bg-green-50 text-green-700 hover:bg-green-100 active:bg-green-200',
  },
  {
    label: 'Easy',
    quality: 5,
    sublabel: 'Too easy',
    className:
      'border-indigo-200 bg-indigo-50 text-indigo-700 hover:bg-indigo-100 active:bg-indigo-200',
  },
];

// ---- Badge helpers ----

const SOURCE_LABEL: Record<string, string> = {
  'mental-model': 'Mental Model',
  'dewey-phase': 'Dewey Phase',
  fallacy: 'Fallacy',
  user: 'My Card',
};

const SOURCE_BADGE: Record<string, string> = {
  'mental-model': 'bg-violet-100 text-violet-800',
  'dewey-phase': 'bg-blue-100 text-blue-800',
  fallacy: 'bg-amber-100 text-amber-800',
  user: 'bg-teal-100 text-teal-800',
};

const FILTER_TABS = [
  { key: 'all', label: 'All' },
  { key: 'mental-model', label: 'Mental Models' },
  { key: 'dewey-phase', label: 'Dewey' },
  { key: 'fallacy', label: 'Fallacies' },
  { key: 'user', label: 'Mine' },
];

// ---- Page component ----

export default function ReviewPage() {
  // Prevents useEffect from resetting the session when a card is created/deleted directly
  const skipNextRebuildRef = useRef(false);

  const [allCards, setAllCards] = useState<SRSCard[]>([]);
  const [progress, setProgress] = useState<Record<string, CardProgress>>({});
  const [session, setSession] = useState<SRSCard[]>([]);
  const [sessionIdx, setSessionIdx] = useState(0);
  const [showBack, setShowBack] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [filterSource, setFilterSource] = useState<string>('all');

  // Create card form
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [newFront, setNewFront] = useState('');
  const [newBack, setNewBack] = useState('');
  const [newCategory, setNewCategory] = useState('');

  // ---- Load all card data once ----
  useEffect(() => {
    async function load() {
      try {
        const [mmRes, dwRes, flRes] = await Promise.all([
          fetch('/data/frameworks/mental-models.json'),
          fetch('/data/frameworks/dewey-five-phases.json'),
          fetch('/data/frameworks/logical-fallacies.json'),
        ]);

        if (!mmRes.ok || !dwRes.ok || !flRes.ok) {
          throw new Error('Failed to fetch one or more card source files.');
        }

        const [mmData, dwData, flData] = (await Promise.all([
          mmRes.json(),
          dwRes.json(),
          flRes.json(),
        ])) as [RawMentalModelsData, RawDeweyData, RawFallaciesData];

        const userCards = getUserSRSCards();
        setAllCards([...buildCards(mmData, dwData, flData), ...userCards]);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error loading cards.');
      } finally {
        setLoading(false);
      }
    }
    void load();
  }, []);

  // ---- Rebuild session when cards or filter source changes ----
  useEffect(() => {
    if (allCards.length === 0) return;
    // Skip full rebuild when a card was just added/deleted (session updated directly)
    if (skipNextRebuildRef.current) {
      skipNextRebuildRef.current = false;
      return;
    }
    const p = getSRSProgress();
    setProgress(p);
    setSession(buildSession(allCards, p, filterSource));
    setSessionIdx(0);
    setShowBack(false);
  }, [allCards, filterSource]);

  // ---- Handlers ----

  const handleRate = useCallback(
    (quality: Quality) => {
      const card = session[sessionIdx];
      if (!card) return;

      const existing = progress[card.id];
      const current: CardProgress = existing ?? {
        cardId: card.id,
        efactor: 2.5,
        interval: 1,
        repetitions: 0,
        dueDate: todayISO(),
      };

      const updated = sm2Update(current, quality);
      saveCardProgress(updated);
      setProgress((prev) => ({ ...prev, [card.id]: updated }));
      setShowBack(false);
      setSessionIdx((i) => i + 1);
    },
    [session, sessionIdx, progress],
  );

  function handleReset() {
    if (!confirm('Reset all review progress? This cannot be undone.')) return;
    resetSRSProgress();
    const empty: Record<string, CardProgress> = {};
    setProgress(empty);
    setSession(buildSession(allCards, empty, filterSource));
    setSessionIdx(0);
    setShowBack(false);
  }

  function handleCloseCreateForm() {
    setShowCreateForm(false);
    setNewFront('');
    setNewBack('');
    setNewCategory('');
  }

  function handleCreateCard() {
    if (!newFront.trim() || !newBack.trim()) return;
    const card: UserSRSCard = {
      id: `user-${generateId()}`,
      source: 'user',
      category: newCategory.trim() || 'Custom',
      front: newFront.trim(),
      back: newBack.trim(),
      createdAt: new Date().toISOString(),
    };
    saveUserSRSCard(card);
    // Skip the useEffect rebuild — update session directly so sessionIdx is preserved
    skipNextRebuildRef.current = true;
    setAllCards((prev) => [...prev, card]);
    if (filterSource === 'all' || filterSource === 'user') {
      setSession((prev) => [...prev, card]);
    }
    handleCloseCreateForm();
  }

  function handleDeleteUserCard(cardId: string) {
    if (!confirm('Delete this card? This cannot be undone.')) return;
    deleteUserSRSCard(cardId);
    // Skip the useEffect rebuild — update session directly
    skipNextRebuildRef.current = true;
    setAllCards((prev) => prev.filter((c) => c.id !== cardId));
    setSession((prev) => prev.filter((c) => c.id !== cardId));
  }

  // ---- Keyboard shortcuts ----
  // Space → reveal answer; 1/2/3/4 → rate Again/Hard/Good/Easy
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      // Compute derived values directly to avoid forward-reference issues
      const isComplete = sessionIdx >= session.length;
      const card = session[sessionIdx];
      if (isComplete || !card) return;
      // Don't fire when user is typing in an input or clicking a button
      if (
        e.target instanceof HTMLInputElement ||
        e.target instanceof HTMLTextAreaElement ||
        e.target instanceof HTMLButtonElement
      )
        return;

      if (e.code === 'Space' && !showBack) {
        e.preventDefault();
        setShowBack(true);
      } else if (showBack) {
        if (e.key === '1') handleRate(0);
        else if (e.key === '2') handleRate(1);
        else if (e.key === '3') handleRate(3);
        else if (e.key === '4') handleRate(5);
      }
    }

    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [showBack, sessionIdx, session, handleRate]);

  // ---- Derived stats ----

  const today = todayISO();
  const totalCards = allCards.length;
  const userCardCount = allCards.filter((c) => c.source === 'user').length;
  const reviewedCount = Object.keys(progress).length;
  const dueCount = allCards.filter((c) => {
    const p = progress[c.id];
    return p !== undefined ? isDue(p) : true; // new = due
  }).length;

  const nextDate = getNextReviewDate(allCards, progress);
  const sessionComplete = sessionIdx >= session.length;
  const currentCard = session[sessionIdx];

  // ---- Render: loading / error ----

  if (loading) {
    return (
      <div className="mx-auto max-w-2xl space-y-6 pb-16">
        <div className="space-y-2">
          <SkeletonBlock className="h-7 w-48" />
          <SkeletonBlock className="h-4 w-72" />
        </div>
        <SkeletonBlock className="h-10 w-full" />
        <SkeletonBlock className="h-2 w-full" />
        <div className="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
          <div className="border-b border-slate-100 bg-slate-50/60 px-5 py-3">
            <SkeletonBlock className="h-5 w-24" />
          </div>
          <div className="space-y-5 p-8">
            <SkeletonBlock className="h-3 w-14" />
            <SkeletonBlock className="h-8 w-2/3" />
            <SkeletonBlock className="h-14 w-full" />
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="mx-auto max-w-md py-24 text-center">
        <p className="font-semibold text-red-600">Failed to load cards</p>
        <p className="mt-1 text-sm text-slate-500">{error}</p>
      </div>
    );
  }

  // ---- Render: main ----

  return (
    <div className="mx-auto max-w-2xl space-y-6 pb-16">
      {/* ── Page header ── */}
      <div className="flex items-start justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">
            Review Queue
          </h1>
          <p className="mt-1 text-sm text-slate-500">
            <span className="font-semibold text-slate-700">{dueCount}</span> due
            {' · '}
            <span className="font-semibold text-slate-700">{reviewedCount}</span>{' '}
            reviewed
            {' · '}
            <span className="font-semibold text-slate-700">{totalCards}</span>{' '}
            total cards
          </p>
        </div>
        <div className="flex shrink-0 items-center gap-3">
          <button
            type="button"
            onClick={() => setShowCreateForm(true)}
            className="rounded-lg bg-teal-600 px-3 py-1.5 text-xs font-semibold text-white shadow-sm transition hover:bg-teal-700"
          >
            + New Card
          </button>
          {reviewedCount > 0 && (
            <>
              <Link
                href="/review/stats"
                className="text-xs font-medium text-indigo-600 hover:text-indigo-800 transition"
              >
                📊 Stats
              </Link>
              <button
                type="button"
                onClick={handleReset}
                className="text-xs text-slate-400 transition hover:text-red-500"
              >
                Reset
              </button>
            </>
          )}
        </div>
      </div>

      {/* ── Source filter tabs ── */}
      <div className="flex gap-1 rounded-xl bg-slate-100 p-1">
        {FILTER_TABS.map((tab) => (
          <button
            key={tab.key}
            type="button"
            onClick={() => setFilterSource(tab.key)}
            className={`flex-1 rounded-lg py-1.5 text-xs font-medium transition ${
              filterSource === tab.key
                ? 'bg-white text-slate-900 shadow-sm'
                : 'text-slate-500 hover:text-slate-700'
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* ── Session complete ── */}
      {sessionComplete ? (
        filterSource === 'user' && userCardCount === 0 ? (
          /* Mine tab — no personal cards created yet */
          <div className="flex flex-col items-center rounded-xl border border-dashed border-teal-200 bg-teal-50/40 px-8 py-20 text-center shadow-sm dark:border-teal-800 dark:bg-teal-900/20">
            <span className="text-4xl">🃏</span>
            <p className="mt-4 text-lg font-semibold text-slate-800 dark:text-slate-100">
              No personal cards yet
            </p>
            <p className="mt-1.5 max-w-xs text-sm text-slate-500 dark:text-slate-400">
              Create your own flashcards for any concept you want to memorise — from
              a book, a lecture, or your own thinking.
            </p>
            <button
              type="button"
              onClick={() => setShowCreateForm(true)}
              className="mt-6 rounded-lg bg-teal-600 px-6 py-2.5 text-sm font-semibold text-white shadow-sm transition hover:bg-teal-700"
            >
              + Create Your First Card
            </button>
          </div>
        ) : (
        <div className="flex flex-col items-center rounded-xl border border-dashed border-slate-200 bg-white px-8 py-20 text-center shadow-sm dark:border-slate-700 dark:bg-slate-800">
          <span className="text-4xl">✓</span>
          <p className="mt-4 text-lg font-semibold text-slate-800 dark:text-slate-100">
            All caught up!
          </p>
          <p className="mt-1.5 text-sm text-slate-500 dark:text-slate-400">
            {session.length === 0
              ? 'No cards are due right now.'
              : `You reviewed ${session.length} card${session.length === 1 ? '' : 's'} this session.`}
          </p>
          {nextDate && (
            <p className="mt-2 text-xs text-slate-400">
              Next review:{' '}
              <span className="font-medium text-slate-600 dark:text-slate-300">
                {new Date(`${nextDate}T12:00:00`).toLocaleDateString('en-US', {
                  weekday: 'short',
                  month: 'short',
                  day: 'numeric',
                })}
              </span>
            </p>
          )}
          {session.length > 0 && (
            <button
              type="button"
              onClick={() => {
                setSessionIdx(0);
                setShowBack(false);
              }}
              className="mt-6 rounded-lg bg-slate-900 px-5 py-2 text-sm font-semibold text-white transition hover:bg-slate-700 dark:bg-slate-100 dark:text-slate-900 dark:hover:bg-slate-300"
            >
              Review again
            </button>
          )}
        </div>
        )
      ) : (
        <>
          {/* ── Session progress bar ── */}
          <div>
            <div className="mb-1 flex items-center justify-between text-xs text-slate-400">
              <span>
                Card {sessionIdx + 1} of {session.length}
              </span>
              <span>{Math.round((sessionIdx / session.length) * 100)}%</span>
            </div>
            <div className="h-1.5 w-full overflow-hidden rounded-full bg-slate-200">
              <div
                className="h-full rounded-full bg-slate-700 transition-all duration-500"
                style={{ width: `${(sessionIdx / session.length) * 100}%` }}
              />
            </div>
          </div>

          {/* ── Flash card ── */}
          {currentCard && (
            <div className="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
              {/* Card header */}
              <div className="flex items-center justify-between border-b border-slate-100 bg-slate-50/60 px-5 py-3">
                <span
                  className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${
                    SOURCE_BADGE[currentCard.source] ??
                    'bg-slate-100 text-slate-600'
                  }`}
                >
                  {SOURCE_LABEL[currentCard.source] ?? currentCard.source}
                </span>
                <div className="flex items-center gap-3">
                  <span className="text-xs text-slate-400">
                    {currentCard.category}
                  </span>
                  {currentCard.source === 'user' && (
                    <button
                      type="button"
                      onClick={() => handleDeleteUserCard(currentCard.id)}
                      className="text-slate-300 transition hover:text-red-400"
                      aria-label="Delete this card"
                      title="Delete card"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                      </svg>
                    </button>
                  )}
                </div>
              </div>

              <div className="p-6 sm:p-8">
                {/* Front — question */}
                <div>
                  <p className="mb-2 text-[10px] font-semibold uppercase tracking-widest text-slate-400">
                    {showBack ? 'Term' : 'Define'}
                  </p>
                  <p className="text-2xl font-bold leading-snug text-slate-900">
                    {currentCard.front}
                  </p>
                </div>

                {/* Back — revealed after clicking */}
                {showBack ? (
                  <div className="mt-7 space-y-5 border-t border-slate-100 pt-6">
                    {/* Definition */}
                    <div>
                      <p className="mb-2 text-[10px] font-semibold uppercase tracking-widest text-slate-400">
                        Definition
                      </p>
                      <p className="text-sm leading-relaxed text-slate-700">
                        {currentCard.back}
                      </p>
                    </div>

                    {/* Example / quote */}
                    {currentCard.backDetail && (
                      <div className="rounded-lg border-l-[3px] border-slate-300 bg-slate-50 px-4 py-3.5">
                        <p className="mb-1.5 text-[10px] font-semibold uppercase tracking-widest text-slate-400">
                          {currentCard.source === 'dewey-phase'
                            ? 'Dewey Quote'
                            : 'Example'}
                        </p>
                        <p className="text-sm italic leading-relaxed text-slate-600">
                          {currentCard.backDetail}
                        </p>
                      </div>
                    )}
                  </div>
                ) : (
                  <button
                    type="button"
                    onClick={() => setShowBack(true)}
                    className="mt-8 w-full rounded-lg border-2 border-dashed border-slate-300 py-4 text-sm font-medium text-slate-400 transition hover:border-slate-400 hover:text-slate-600 focus:outline-none focus:ring-2 focus:ring-slate-400 focus:ring-offset-2"
                  >
                    Show answer
                  </button>
                )}
              </div>
            </div>
          )}

          {/* ── Rating buttons (visible only after reveal) ── */}
          {showBack && (
            <div className="grid grid-cols-4 gap-2.5">
              {RATINGS.map((r) => (
                <button
                  key={r.label}
                  type="button"
                  onClick={() => handleRate(r.quality)}
                  className={`rounded-xl border px-2 py-3.5 text-center transition focus:outline-none focus:ring-2 focus:ring-slate-400 focus:ring-offset-1 ${r.className}`}
                >
                  <p className="text-sm font-bold">{r.label}</p>
                  <p className="mt-0.5 text-[11px] opacity-70">{r.sublabel}</p>
                </button>
              ))}
            </div>
          )}

          {/* ── Keyboard hint ── */}
          {!showBack && (
            <p className="text-center text-xs text-slate-400">
              Press{' '}
              <kbd className="rounded border border-slate-300 bg-slate-100 px-1 py-0.5 font-mono text-[10px]">
                Space
              </kbd>{' '}
              or click to reveal the answer
            </p>
          )}
        </>
      )}

      {/* ── Legend ── */}
      {!sessionComplete && showBack && (
        <p className="text-center text-[11px] leading-6 text-slate-400">
          <kbd className="rounded border border-slate-200 bg-slate-100 px-1 font-mono text-[10px]">1</kbd>{' '}
          Again ·{' '}
          <kbd className="rounded border border-slate-200 bg-slate-100 px-1 font-mono text-[10px]">2</kbd>{' '}
          Hard ·{' '}
          <kbd className="rounded border border-slate-200 bg-slate-100 px-1 font-mono text-[10px]">3</kbd>{' '}
          Good ·{' '}
          <kbd className="rounded border border-slate-200 bg-slate-100 px-1 font-mono text-[10px]">4</kbd>{' '}
          Easy
          <br />
          <span className="font-medium text-red-600">Again / Hard</span> → resets schedule ·{' '}
          <span className="font-medium text-green-600">Good / Easy</span> → advances interval
        </p>
      )}

      {/* ── Deck info (collapsed footer) ── */}
      <details className="rounded-lg border border-slate-200 bg-white px-4 py-3 text-xs text-slate-500 shadow-sm">
        <summary className="cursor-pointer font-medium text-slate-600">
          About this deck
        </summary>
        <div className="mt-3 space-y-1 leading-5">
          <p>
            Cards are scheduled using the{' '}
            <span className="font-medium text-slate-700">SM-2 algorithm</span>. Each
            rating updates the card&apos;s ease factor and next review date.
          </p>
          <p>
            <span className="font-medium text-slate-700">Again (0)</span> and{' '}
            <span className="font-medium text-slate-700">Hard (1)</span> reset a card
            to the beginning. <span className="font-medium text-slate-700">Good (3)</span>{' '}
            and <span className="font-medium text-slate-700">Easy (5)</span> advance
            the interval (1 → 6 → n × ease days).
          </p>
          <p>
            Up to <span className="font-medium text-slate-700">10 new cards</span> are
            introduced per session to avoid overload. All progress is saved locally in
            your browser.
          </p>
          <p className="pt-1 text-slate-400">
            Last full rebuild:{' '}
            {new Date(`${today}T12:00:00`).toLocaleDateString('en-US', {
              year: 'numeric',
              month: 'long',
              day: 'numeric',
            })}
          </p>
        </div>
      </details>

      {/* ── Create Card modal ── */}
      {showCreateForm && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center p-4"
          style={{ background: 'rgba(0,0,0,0.45)' }}
          onClick={(e) => {
            if (e.target === e.currentTarget) handleCloseCreateForm();
          }}
        >
          <div className="w-full max-w-md rounded-2xl border border-slate-200 bg-white shadow-2xl dark:border-slate-700 dark:bg-slate-800">
            {/* Header */}
            <div className="flex items-center justify-between border-b border-slate-100 px-6 py-4 dark:border-slate-700">
              <h2 className="font-semibold text-slate-800 dark:text-slate-100">
                Create Flashcard
              </h2>
              <button
                type="button"
                onClick={handleCloseCreateForm}
                className="rounded text-slate-400 transition hover:text-slate-600 dark:hover:text-slate-200"
                aria-label="Close"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            {/* Body */}
            <div className="space-y-4 p-6">
              <div>
                <label className="mb-1.5 block text-xs font-semibold uppercase tracking-widest text-slate-400">
                  Front — question or term <span className="text-red-400">*</span>
                </label>
                <textarea
                  rows={2}
                  className="w-full resize-none rounded-lg border border-slate-200 bg-white px-3 py-2 text-sm text-slate-800 placeholder-slate-400 focus:border-teal-400 focus:outline-none focus:ring-2 focus:ring-teal-200 dark:border-slate-600 dark:bg-slate-700 dark:text-slate-100 dark:placeholder-slate-500"
                  placeholder="e.g. What is Occam's Razor?"
                  value={newFront}
                  onChange={(e) => setNewFront(e.target.value)}
                  autoFocus
                  onKeyDown={(e) => {
                    if (e.key === 'Enter' && e.ctrlKey) handleCreateCard();
                  }}
                />
              </div>
              <div>
                <label className="mb-1.5 block text-xs font-semibold uppercase tracking-widest text-slate-400">
                  Back — answer or definition <span className="text-red-400">*</span>
                </label>
                <textarea
                  rows={4}
                  className="w-full resize-none rounded-lg border border-slate-200 bg-white px-3 py-2 text-sm text-slate-800 placeholder-slate-400 focus:border-teal-400 focus:outline-none focus:ring-2 focus:ring-teal-200 dark:border-slate-600 dark:bg-slate-700 dark:text-slate-100 dark:placeholder-slate-500"
                  placeholder="e.g. The principle that the simplest explanation consistent with the evidence should be preferred."
                  value={newBack}
                  onChange={(e) => setNewBack(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter' && e.ctrlKey) handleCreateCard();
                  }}
                />
              </div>
              <div>
                <label className="mb-1.5 block text-xs font-semibold uppercase tracking-widest text-slate-400">
                  Category{' '}
                  <span className="font-normal normal-case text-slate-300">(optional — defaults to Custom)</span>
                </label>
                <input
                  type="text"
                  className="w-full rounded-lg border border-slate-200 bg-white px-3 py-2 text-sm text-slate-800 placeholder-slate-400 focus:border-teal-400 focus:outline-none focus:ring-2 focus:ring-teal-200 dark:border-slate-600 dark:bg-slate-700 dark:text-slate-100 dark:placeholder-slate-500"
                  placeholder="e.g. Mental Models, Philosophy, Personal"
                  value={newCategory}
                  onChange={(e) => setNewCategory(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter') handleCreateCard();
                  }}
                />
              </div>
              <p className="text-[11px] text-slate-400">
                <kbd className="rounded border border-slate-200 bg-slate-100 px-1 py-0.5 font-mono text-[10px] dark:border-slate-600 dark:bg-slate-700">Ctrl</kbd>
                {' '}+{' '}
                <kbd className="rounded border border-slate-200 bg-slate-100 px-1 py-0.5 font-mono text-[10px] dark:border-slate-600 dark:bg-slate-700">Enter</kbd>
                {' '}to save
              </p>
            </div>

            {/* Footer */}
            <div className="flex justify-end gap-3 border-t border-slate-100 px-6 py-4 dark:border-slate-700">
              <button
                type="button"
                onClick={handleCloseCreateForm}
                className="rounded-lg px-4 py-2 text-sm text-slate-500 transition hover:bg-slate-100 dark:hover:bg-slate-700 dark:text-slate-400"
              >
                Cancel
              </button>
              <button
                type="button"
                onClick={handleCreateCard}
                disabled={!newFront.trim() || !newBack.trim()}
                className="rounded-lg bg-teal-600 px-5 py-2 text-sm font-semibold text-white shadow-sm transition hover:bg-teal-700 disabled:opacity-40"
              >
                Save Card
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
