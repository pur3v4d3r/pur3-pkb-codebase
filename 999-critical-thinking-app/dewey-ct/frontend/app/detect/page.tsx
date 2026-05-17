'use client';

import { useState } from 'react';
import { detectFallacies, type DetectedFallacy } from '@/lib/api';

const MAX_CHARS = 3000;

const CATEGORY_BADGE: Record<string, string> = {
  'Relevance Fallacies': 'bg-red-100 text-red-800',
  'Ambiguity Fallacies': 'bg-orange-100 text-orange-800',
  'Presumption Fallacies': 'bg-yellow-100 text-yellow-800',
  'Weak Induction Fallacies': 'bg-blue-100 text-blue-800',
  'Causal Fallacies': 'bg-purple-100 text-purple-800',
  'Statistical Fallacies': 'bg-teal-100 text-teal-800',
};

function categoryBadgeClass(category: string): string {
  return (
    CATEGORY_BADGE[category] ?? 'bg-slate-100 text-slate-700'
  );
}

function FallacyCard({ fallacy, idx }: { fallacy: DetectedFallacy; idx: number }) {
  return (
    <div className="rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-slate-100 bg-slate-50/60 px-5 py-3">
        <div className="flex items-center gap-2.5">
          <span className="flex h-6 w-6 items-center justify-center rounded-full bg-slate-900 text-[11px] font-bold text-white">
            {idx + 1}
          </span>
          <span className="font-semibold text-slate-900">{fallacy.name}</span>
        </div>
        <span
          className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${categoryBadgeClass(
            fallacy.category,
          )}`}
        >
          {fallacy.category}
        </span>
      </div>

      <div className="space-y-4 p-5">
        {/* Quote from the text */}
        <div>
          <p className="mb-1.5 text-[10px] font-semibold uppercase tracking-widest text-slate-400">
            Detected in your text
          </p>
          <blockquote className="rounded-lg border-l-[3px] border-amber-400 bg-amber-50 px-4 py-3 text-sm italic leading-relaxed text-amber-900">
            &ldquo;{fallacy.quote}&rdquo;
          </blockquote>
        </div>

        {/* Explanation */}
        <div>
          <p className="mb-1.5 text-[10px] font-semibold uppercase tracking-widest text-slate-400">
            Explanation
          </p>
          <p className="text-sm leading-relaxed text-slate-700">{fallacy.explanation}</p>
        </div>
      </div>
    </div>
  );
}

export default function DetectPage() {
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<DetectedFallacy[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function handleDetect() {
    if (!text.trim() || loading) return;
    setLoading(true);
    setResult(null);
    setError(null);
    try {
      const res = await detectFallacies({ text: text.trim() });
      setResult(res.fallacies);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : 'The analysis failed. Is the backend running?',
      );
    } finally {
      setLoading(false);
    }
  }

  const charsLeft = MAX_CHARS - text.length;
  const overLimit = charsLeft < 0;

  return (
    <div className="mx-auto max-w-3xl space-y-8 pb-16">
      {/* ── Header ── */}
      <div>
        <h1 className="text-2xl font-bold tracking-tight text-slate-900 dark:text-slate-100">
          Fallacy Detector
        </h1>
        <p className="mt-1.5 text-sm text-slate-500 dark:text-slate-400">
          Paste any argument, paragraph, or claim. The AI will identify logical
          fallacies using the same reference list you study in the review queue.
        </p>
      </div>

      {/* ── Input form ── */}
      <div className="space-y-3">
        <div className="relative">
          <textarea
            className={`w-full resize-y rounded-xl border bg-white px-4 py-3 text-sm leading-relaxed text-slate-800 placeholder-slate-400 shadow-sm focus:outline-none focus:ring-2 dark:bg-slate-800 dark:text-slate-100 dark:placeholder-slate-500 ${
              overLimit
                ? 'border-red-400 focus:ring-red-300'
                : 'border-slate-200 focus:border-indigo-400 focus:ring-indigo-200 dark:border-slate-700'
            }`}
            placeholder={
              'Paste the text you want to analyse here\u2026\n\nExample: \u201cEveryone knows this diet works because millions of people are trying it, and they can\u2019t all be wrong.\u201d'
            }
            rows={8}
            value={text}
            onChange={(e) => setText(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && e.ctrlKey) void handleDetect();
            }}
          />
          <span
            className={`absolute bottom-3 right-4 text-xs ${
              overLimit ? 'text-red-500' : 'text-slate-400'
            }`}
          >
            {charsLeft.toLocaleString()} / {MAX_CHARS.toLocaleString()}
          </span>
        </div>

        <div className="flex items-center justify-between">
          <p className="text-xs text-slate-400">
            <kbd className="rounded border border-slate-200 bg-slate-100 px-1 py-0.5 font-mono text-[10px] dark:border-slate-700 dark:bg-slate-800">
              Ctrl
            </kbd>
            {' '}+{' '}
            <kbd className="rounded border border-slate-200 bg-slate-100 px-1 py-0.5 font-mono text-[10px] dark:border-slate-700 dark:bg-slate-800">
              Enter
            </kbd>
            {' '}to analyse
          </p>
          <button
            type="button"
            onClick={() => void handleDetect()}
            disabled={!text.trim() || overLimit || loading}
            className="flex items-center gap-2 rounded-lg bg-slate-900 px-5 py-2.5 text-sm font-semibold text-white shadow-sm transition hover:bg-slate-700 disabled:opacity-40 dark:bg-slate-100 dark:text-slate-900 dark:hover:bg-slate-300"
          >
            {loading ? (
              <>
                <svg
                  className="h-4 w-4 animate-spin"
                  fill="none"
                  viewBox="0 0 24 24"
                >
                  <circle
                    className="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    strokeWidth="4"
                  />
                  <path
                    className="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8v4l3-3-3-3V4a8 8 0 00-8 8z"
                  />
                </svg>
                Analysing…
              </>
            ) : (
              'Detect Fallacies'
            )}
          </button>
        </div>
      </div>

      {/* ── Error ── */}
      {error && (
        <div className="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
          <span className="font-semibold">Error: </span>{error}
        </div>
      )}

      {/* ── Results ── */}
      {result !== null && (
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-base font-semibold text-slate-800 dark:text-slate-100">
              {result.length === 0
                ? 'No fallacies detected'
                : `${result.length} fallac${result.length === 1 ? 'y' : 'ies'} detected`}
            </h2>
            {result.length === 0 && (
              <span className="text-sm text-slate-400">
                The argument appears logically sound — or is too short to analyse.
              </span>
            )}
          </div>

          {result.length === 0 ? (
            <div className="flex flex-col items-center rounded-xl border border-dashed border-slate-200 bg-white px-8 py-14 text-center shadow-sm dark:border-slate-700 dark:bg-slate-800">
              <span className="text-4xl">✓</span>
              <p className="mt-3 text-sm font-medium text-slate-700 dark:text-slate-200">
                No logical fallacies found
              </p>
              <p className="mt-1 text-xs text-slate-400">
                Try a longer or more argumentative passage for better detection.
              </p>
            </div>
          ) : (
            <div className="space-y-4">
              {result.map((f, i) => (
                <FallacyCard key={`${f.name}-${i}`} fallacy={f} idx={i} />
              ))}
            </div>
          )}

          {/* Link to fallacy reference */}
          {result.length > 0 && (
            <p className="text-center text-xs text-slate-400">
              Study these fallacies in the{' '}
              <a
                href="/review"
                className="font-medium text-indigo-600 hover:text-indigo-800 transition"
              >
                Review Queue
              </a>{' '}
              or read the full list in{' '}
              <a
                href="/frameworks"
                className="font-medium text-indigo-600 hover:text-indigo-800 transition"
              >
                Frameworks
              </a>
              .
            </p>
          )}
        </div>
      )}
    </div>
  );
}
