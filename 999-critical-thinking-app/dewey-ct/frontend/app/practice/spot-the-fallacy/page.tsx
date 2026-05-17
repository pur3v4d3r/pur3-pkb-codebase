'use client';

import { useCallback, useEffect, useRef, useState } from 'react';

// ---- Types matching logical-fallacies.json ----

interface Fallacy {
  id: string;
  name: string;
  category: string;
  definition: string;
  example: string;
  why_it_fails: string;
  detection_prompt: string;
}

interface Question {
  fallacy: Fallacy;
  options: string[]; // 4 names, shuffled
  correctIndex: number;
}

// ---- Utilities ----

function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function buildQuestions(fallacies: Fallacy[]): Question[] {
  return shuffle(fallacies).map((f) => {
    // Pick 3 distractors from same category first, then any
    const sameCategory = fallacies.filter((x) => x.id !== f.id && x.category === f.category);
    const others = fallacies.filter((x) => x.id !== f.id && x.category !== f.category);
    const pool = shuffle([...sameCategory, ...others]);
    const distractors = pool.slice(0, 3).map((x) => x.name);
    const options = shuffle([f.name, ...distractors]);
    return {
      fallacy: f,
      options,
      correctIndex: options.indexOf(f.name),
    };
  });
}

// ---- Score badge ----

function scorePct(correct: number, total: number): number {
  return total === 0 ? 0 : Math.round((correct / total) * 100);
}

// ---- Component ----

export default function SpotTheFallacyPage() {
  const [fallacies, setFallacies] = useState<Fallacy[]>([]);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [qIdx, setQIdx] = useState(0);
  const [selected, setSelected] = useState<number | null>(null);
  const [correct, setCorrect] = useState(0);
  const [finished, setFinished] = useState(false);
  const [loadError, setLoadError] = useState(false);
  const inputRef = useRef<HTMLDivElement>(null);

  // Load fallacies from public JSON (no server route needed)
  useEffect(() => {
    fetch('/data/frameworks/logical-fallacies.json')
      .then((r) => r.json())
      .then((data: { fallacies: Fallacy[] }) => {
        setFallacies(data.fallacies);
        setQuestions(buildQuestions(data.fallacies));
      })
      .catch(() => setLoadError(true));
  }, []);

  const q = questions[qIdx];
  const isAnswered = selected !== null;
  const isCorrect = selected === q?.correctIndex;

  const handleSelect = useCallback(
    (idx: number) => {
      if (isAnswered) return;
      setSelected(idx);
      if (idx === q.correctIndex) setCorrect((c) => c + 1);
    },
    [isAnswered, q],
  );

  const handleNext = useCallback(() => {
    if (qIdx + 1 >= questions.length) {
      setFinished(true);
    } else {
      setQIdx((i) => i + 1);
      setSelected(null);
    }
  }, [qIdx, questions.length]);

  // Keyboard: 1-4 to select, Enter/Space to advance
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if (['1', '2', '3', '4'].includes(e.key)) {
        handleSelect(parseInt(e.key, 10) - 1);
      }
      if ((e.key === 'Enter' || e.key === ' ') && isAnswered && !finished) {
        handleNext();
      }
    }
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [handleSelect, handleNext, isAnswered, finished]);

  function restart() {
    setQuestions(buildQuestions(fallacies));
    setQIdx(0);
    setSelected(null);
    setCorrect(0);
    setFinished(false);
  }

  // ---- Loading / error states ----
  if (loadError) {
    return (
      <div className="mx-auto max-w-2xl pt-16 text-center text-sm text-slate-500">
        Failed to load fallacy data.
      </div>
    );
  }

  if (questions.length === 0) {
    return (
      <div className="mx-auto max-w-2xl pt-16 text-center text-sm text-slate-500">
        Loading…
      </div>
    );
  }

  // ---- Finished screen ----
  if (finished) {
    const pct = scorePct(correct, questions.length);
    return (
      <div className="mx-auto max-w-xl space-y-6 pt-12 text-center">
        <div className="text-5xl font-bold text-slate-900">{pct}%</div>
        <p className="text-lg text-slate-600">
          {correct} / {questions.length} correct
        </p>
        <p className="text-sm text-slate-500">
          {pct >= 80
            ? 'Strong pattern recognition! Keep drilling to cement these.'
            : pct >= 60
            ? 'Good foundation — revisit the fallacies you missed in /review.'
            : 'Challenging! Read through the fallacy definitions before your next attempt.'}
        </p>
        <div className="flex justify-center gap-3">
          <button
            onClick={restart}
            className="rounded-lg bg-indigo-600 px-5 py-2 text-sm font-semibold text-white transition hover:bg-indigo-700"
          >
            Try again (reshuffled)
          </button>
          <a
            href="/review"
            className="rounded-lg border border-slate-300 px-5 py-2 text-sm font-semibold text-slate-700 transition hover:bg-slate-100"
          >
            Go to SRS Review →
          </a>
        </div>
      </div>
    );
  }

  // ---- Question screen ----
  return (
    <div ref={inputRef} className="mx-auto max-w-2xl space-y-8" tabIndex={-1}>
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-xl font-bold text-slate-900">Spot the Fallacy</h1>
          <p className="text-xs text-slate-500">
            Read the scenario — which fallacy is being committed?
          </p>
        </div>
        <div className="text-right">
          <div className="text-2xl font-bold text-slate-900">
            {qIdx + 1}
            <span className="text-base font-normal text-slate-400"> / {questions.length}</span>
          </div>
          <div className="text-xs text-slate-400">
            {correct} correct · {scorePct(correct, qIdx)}%
          </div>
        </div>
      </div>

      {/* Progress bar */}
      <div className="h-1.5 w-full overflow-hidden rounded-full bg-slate-200">
        <div
          className="h-full bg-indigo-500 transition-all"
          style={{ width: `${((qIdx + (selected !== null ? 1 : 0)) / questions.length) * 100}%` }}
        />
      </div>

      {/* Scenario card */}
      <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
        <div className="mb-2 flex items-center gap-2">
          <span className="rounded-full bg-amber-100 px-2 py-0.5 text-[10px] font-semibold text-amber-700 uppercase tracking-wide">
            Scenario
          </span>
          <span className="text-xs text-slate-400">{q.fallacy.category}</span>
        </div>
        <p className="text-sm leading-relaxed text-slate-800">{q.fallacy.example}</p>
      </div>

      {/* Options */}
      <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
        {q.options.map((name, idx) => {
          let classes =
            'cursor-pointer rounded-lg border p-4 text-left text-sm font-medium transition ';
          if (!isAnswered) {
            classes += 'border-slate-200 bg-white hover:border-indigo-300 hover:bg-indigo-50 text-slate-800';
          } else if (idx === q.correctIndex) {
            classes += 'border-green-400 bg-green-50 text-green-900';
          } else if (idx === selected && selected !== q.correctIndex) {
            classes += 'border-red-300 bg-red-50 text-red-700';
          } else {
            classes += 'border-slate-200 bg-white text-slate-400';
          }
          return (
            <button
              key={idx}
              type="button"
              onClick={() => handleSelect(idx)}
              className={classes}
              aria-pressed={selected === idx}
            >
              <span className="mr-2 rounded bg-slate-100 px-1.5 py-0.5 text-[10px] font-bold text-slate-500">
                {idx + 1}
              </span>
              {name}
            </button>
          );
        })}
      </div>

      {/* Explanation (revealed after answer) */}
      {isAnswered && (
        <div
          className={`rounded-xl border p-5 text-sm ${
            isCorrect
              ? 'border-green-200 bg-green-50'
              : 'border-red-100 bg-red-50'
          }`}
        >
          <p className={`mb-1 font-semibold ${isCorrect ? 'text-green-800' : 'text-red-800'}`}>
            {isCorrect ? '✓ Correct!' : `✗ The fallacy is: ${q.fallacy.name}`}
          </p>
          <p className="mb-2 text-slate-700">{q.fallacy.why_it_fails}</p>
          <p className="italic text-slate-500">
            <span className="font-medium not-italic">Probe:</span> {q.fallacy.detection_prompt}
          </p>
        </div>
      )}

      {/* Next / keyboard hint */}
      {isAnswered && (
        <div className="flex items-center justify-between">
          <p className="text-xs text-slate-400">Press Enter or Space to continue</p>
          <button
            onClick={handleNext}
            className="rounded-lg bg-indigo-600 px-5 py-2 text-sm font-semibold text-white transition hover:bg-indigo-700"
          >
            {qIdx + 1 >= questions.length ? 'See results' : 'Next →'}
          </button>
        </div>
      )}
    </div>
  );
}
