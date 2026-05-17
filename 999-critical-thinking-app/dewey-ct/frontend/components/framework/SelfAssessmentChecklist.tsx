'use client';

import { useState, useEffect } from 'react';

interface Props {
  frameworkId: string;
  data: Record<string, unknown>;
}

function s2t(key: string): string {
  return key.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());
}

export default function SelfAssessmentChecklist({ frameworkId, data }: Props) {
  const categories = Object.entries(data).filter(([, v]) => Array.isArray(v)) as [
    string,
    string[],
  ][];
  const totalQuestions = categories.reduce((acc, [, qs]) => acc + qs.length, 0);

  const [checked, setChecked] = useState<Record<string, boolean>>({});
  const [loaded, setLoaded] = useState(false);

  const storageKey = `dewey-ct:checklist:${frameworkId}`;

  // Load persisted state once on mount
  useEffect(() => {
    const initial: Record<string, boolean> = {};
    for (const [cat, qs] of categories) {
      for (let i = 0; i < qs.length; i++) {
        initial[`${cat}:${i}`] = false;
      }
    }
    try {
      const stored = localStorage.getItem(storageKey);
      if (stored) {
        const parsed = JSON.parse(stored) as Record<string, boolean>;
        Object.assign(initial, parsed);
      }
    } catch {
      // localStorage unavailable — continue with defaults
    }
    setChecked(initial);
    setLoaded(true);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [storageKey]);

  // Persist on every change (skip first render before load)
  useEffect(() => {
    if (!loaded) return;
    try {
      localStorage.setItem(storageKey, JSON.stringify(checked));
    } catch {
      // ignore write errors
    }
  }, [checked, loaded, storageKey]);

  const toggle = (key: string) =>
    setChecked((prev) => ({ ...prev, [key]: !prev[key] }));

  const reset = () => {
    const blank: Record<string, boolean> = {};
    for (const [cat, qs] of categories) {
      for (let i = 0; i < qs.length; i++) {
        blank[`${cat}:${i}`] = false;
      }
    }
    setChecked(blank);
  };

  const totalChecked = Object.values(checked).filter(Boolean).length;
  const pct = totalQuestions > 0 ? Math.round((totalChecked / totalQuestions) * 100) : 0;

  if (!categories.length) return null;

  return (
    <section className="space-y-3">
      {/* Header row */}
      <div className="flex items-center justify-between">
        <h2 className="text-xs font-semibold uppercase tracking-widest text-slate-400">
          Self-Assessment Checklist
        </h2>
        <div className="flex items-center gap-3">
          <span className="text-xs tabular-nums text-slate-500">
            {totalChecked}/{totalQuestions}
          </span>
          {totalChecked > 0 && (
            <button
              onClick={reset}
              className="rounded border border-slate-200 px-2 py-0.5 text-xs text-slate-500 transition-colors hover:bg-slate-50 hover:text-slate-700"
            >
              Reset
            </button>
          )}
        </div>
      </div>

      {/* Overall progress bar */}
      <div className="h-1.5 w-full overflow-hidden rounded-full bg-slate-100">
        <div
          className="h-full rounded-full bg-slate-600 transition-all duration-300"
          style={{ width: `${pct}%` }}
        />
      </div>

      {/* Categories */}
      <div className="space-y-3">
        {categories.map(([key, questions]) => {
          const catChecked = questions.filter((_, i) => checked[`${key}:${i}`]).length;
          const catPct =
            questions.length > 0 ? Math.round((catChecked / questions.length) * 100) : 0;
          return (
            <div key={key} className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
              <div className="mb-1 flex items-center justify-between">
                <h3 className="text-sm font-semibold text-slate-800">{s2t(key)}</h3>
                <span className="text-xs tabular-nums text-slate-400">
                  {catChecked}/{questions.length}
                </span>
              </div>
              {/* Per-category progress bar */}
              <div className="mb-4 h-1 w-full overflow-hidden rounded-full bg-slate-100">
                <div
                  className="h-full rounded-full bg-slate-400 transition-all duration-300"
                  style={{ width: `${catPct}%` }}
                />
              </div>
              <ul className="space-y-2.5">
                {questions.map((q, i) => {
                  const k = `${key}:${i}`;
                  const isChecked = checked[k] ?? false;
                  return (
                    <li key={i}>
                      <label className="group flex cursor-pointer items-start gap-3">
                        <input
                          type="checkbox"
                          checked={isChecked}
                          onChange={() => toggle(k)}
                          className="mt-0.5 h-4 w-4 flex-shrink-0 cursor-pointer rounded border-slate-300 accent-slate-700"
                        />
                        <span
                          className={`text-sm leading-relaxed transition-colors ${
                            isChecked
                              ? 'text-slate-400 line-through'
                              : 'text-slate-600 group-hover:text-slate-900'
                          }`}
                        >
                          {q}
                        </span>
                      </label>
                    </li>
                  );
                })}
              </ul>
            </div>
          );
        })}
      </div>
    </section>
  );
}
