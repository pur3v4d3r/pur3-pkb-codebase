'use client';

import { useState, useCallback } from 'react';
import { evaluatePracticeAnswer, type EvaluateResponse } from '@/lib/api';
import { savePortfolioEntry, generateId } from '@/lib/storage';

// ---- Score visual helpers ----

const SCORE_LABEL: Record<number, string> = {
  1: 'Major gaps',
  2: 'Partial',
  3: 'Adequate',
  4: 'Strong',
  5: 'Expert',
};

const SCORE_RING: Record<number, string> = {
  1: 'text-red-600 ring-red-200',
  2: 'text-orange-600 ring-orange-200',
  3: 'text-amber-600 ring-amber-200',
  4: 'text-emerald-600 ring-emerald-200',
  5: 'text-indigo-600 ring-indigo-200',
};

function ScoreBadge({ score }: { score: number }) {
  const ring = SCORE_RING[score] ?? 'text-slate-600 ring-slate-200';
  return (
    <span
      className={`inline-flex h-9 w-9 items-center justify-center rounded-full ring-2 text-sm font-bold ${ring}`}
    >
      {score}
    </span>
  );
}

// ---- Feedback result panel ----

function EvalResult({
  result,
  onSave,
  saved,
}: {
  result: EvaluateResponse;
  onSave: () => void;
  saved: boolean;
}) {
  return (
    <div className="space-y-6 rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
      {/* Overall score */}
      <div className="flex items-center gap-4">
        <ScoreBadge score={result.overall_score} />
        <div>
          <p className="text-sm font-semibold text-slate-800">
            Overall:{' '}
            <span className="font-normal text-slate-600">
              {SCORE_LABEL[result.overall_score] ?? result.overall_score} / 5
            </span>
          </p>
          <p className="text-xs text-slate-400">Paul-Elder evaluation</p>
        </div>
        {/* Save button */}
        <div className="ml-auto">
          {saved ? (
            <span className="inline-flex items-center gap-1.5 rounded-md bg-emerald-50 px-3 py-1.5 text-xs font-medium text-emerald-700 ring-1 ring-emerald-200">
              ✓ Saved to portfolio
            </span>
          ) : (
            <button
              onClick={onSave}
              className="rounded-md bg-slate-900 px-3 py-1.5 text-xs font-semibold text-white hover:bg-slate-700 transition"
            >
              Save to portfolio
            </button>
          )}
        </div>
      </div>

      {/* Strengths */}
      {result.strengths.length > 0 && (
        <div className="space-y-2">
          <h3 className="text-xs font-semibold uppercase tracking-wide text-emerald-700">
            Strengths
          </h3>
          <ul className="space-y-1.5">
            {result.strengths.map((s, i) => (
              <li key={i} className="flex gap-2 text-sm text-slate-700">
                <span className="mt-0.5 shrink-0 text-emerald-500">✓</span>
                {s}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Improvements */}
      {result.improvements.length > 0 && (
        <div className="space-y-2">
          <h3 className="text-xs font-semibold uppercase tracking-wide text-amber-700">
            Improvements needed
          </h3>
          <ul className="space-y-1.5">
            {result.improvements.map((im, i) => (
              <li key={i} className="flex gap-2 text-sm text-slate-700">
                <span className="mt-0.5 shrink-0 text-amber-500">→</span>
                {im}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Standards breakdown */}
      {result.standards_feedback.length > 0 && (
        <div className="space-y-2">
          <h3 className="text-xs font-semibold uppercase tracking-wide text-slate-500">
            Standards breakdown
          </h3>
          <div className="divide-y divide-slate-100 rounded-lg border border-slate-100">
            {result.standards_feedback.map((sf, i) => (
              <div key={i} className="flex items-start gap-3 px-4 py-3">
                <ScoreBadge score={sf.score} />
                <div className="min-w-0">
                  <p className="text-xs font-semibold text-slate-700">{sf.standard}</p>
                  <p className="text-xs leading-relaxed text-slate-500">{sf.comment}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Next step */}
      {result.next_step && (
        <div className="rounded-lg border border-indigo-100 bg-indigo-50 px-4 py-3">
          <p className="text-xs font-semibold uppercase tracking-wide text-indigo-600">
            Next step
          </p>
          <p className="mt-1 text-sm text-indigo-800">{result.next_step}</p>
        </div>
      )}
    </div>
  );
}

// ---- Main component ----

interface PracticeEvalPanelProps {
  problemId: string;   // e.g. "PP-09"
  problemTitle: string;
  framework: string;
}

export default function PracticeEvalPanel({
  problemId,
  problemTitle,
  framework,
}: PracticeEvalPanelProps) {
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<EvaluateResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [saved, setSaved] = useState(false);

  const handleSubmit = useCallback(async () => {
    const trimmed = answer.trim();
    if (!trimmed) return;
    setLoading(true);
    setError(null);
    setResult(null);
    setSaved(false);
    try {
      const data = await evaluatePracticeAnswer({
        problem_id: problemId,
        user_answer: trimmed,
      });
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Evaluation failed — check the backend is running.');
    } finally {
      setLoading(false);
    }
  }, [answer, problemId]);

  const handleSave = useCallback(() => {
    if (!result) return;
    const now = new Date().toISOString();
    savePortfolioEntry({
      id: generateId(),
      createdAt: now,
      updatedAt: now,
      type: 'practice-feedback',
      title: `Practice: ${problemTitle}`,
      responses: {
        user_answer: answer,
        overall_score: result.overall_score,
        strengths: result.strengths,
        improvements: result.improvements,
        next_step: result.next_step,
        standards_feedback: result.standards_feedback,
      },
      tags: ['practice', framework, problemId.toLowerCase()],
    });
    setSaved(true);
  }, [result, answer, problemTitle, framework, problemId]);

  const charCount = answer.length;
  const overLimit = charCount > 5000;

  return (
    <section className="space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-base font-semibold text-slate-800">Your Analysis</h2>
        <span className={`text-xs ${overLimit ? 'text-red-500' : 'text-slate-400'}`}>
          {charCount.toLocaleString()} / 5,000
        </span>
      </div>

      <p className="text-sm text-slate-500">
        Write your analysis below before revealing hints or the solution sketch. The AI evaluator
        will score it against Paul-Elder Intellectual Standards and the{' '}
        <span className="font-medium text-slate-700">{framework}</span> framework requirements.
      </p>

      <textarea
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        rows={12}
        placeholder="Write your full analysis here. Address each component listed in the Workspace Prompts above…"
        className="w-full resize-y rounded-lg border border-slate-200 bg-white px-4 py-3 text-sm leading-relaxed text-slate-800 shadow-sm placeholder:text-slate-400 focus:border-indigo-400 focus:outline-none focus:ring-2 focus:ring-indigo-100"
        disabled={loading}
      />

      <div className="flex items-center gap-3">
        <button
          onClick={handleSubmit}
          disabled={loading || !answer.trim() || overLimit}
          className="inline-flex items-center gap-2 rounded-md bg-indigo-600 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-indigo-700 disabled:cursor-not-allowed disabled:opacity-50"
        >
          {loading ? (
            <>
              <svg
                className="h-4 w-4 animate-spin"
                viewBox="0 0 24 24"
                fill="none"
                aria-hidden="true"
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
                  d="M4 12a8 8 0 018-8v4l3-3-3-3v4a8 8 0 100 16v-4l-3 3 3 3v-4a8 8 0 01-8-8z"
                />
              </svg>
              Evaluating…
            </>
          ) : (
            'Get AI Feedback'
          )}
        </button>
        {result && !loading && (
          <button
            onClick={() => {
              setResult(null);
              setError(null);
              setSaved(false);
            }}
            className="text-xs text-slate-400 hover:text-slate-600"
          >
            Clear
          </button>
        )}
      </div>

      {error && (
        <div className="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
          {error}
        </div>
      )}

      {result && (
        <EvalResult result={result} onSave={handleSave} saved={saved} />
      )}
    </section>
  );
}
