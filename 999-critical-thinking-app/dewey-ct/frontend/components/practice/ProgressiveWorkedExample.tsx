'use client';

import { useState } from 'react';

interface Field {
  label: string;
  content: string;
}

interface Section {
  section_label: string;
  content?: string;
  fields?: Field[];
}

interface ProgressiveWorkedExampleProps {
  sections: Section[];
  /** If true, the first section (Pre-Analysis Snapshot) is always visible. */
  alwaysVisibleCount?: number;
}

export default function ProgressiveWorkedExample({
  sections,
  alwaysVisibleCount = 1,
}: ProgressiveWorkedExampleProps) {
  // Track how many sections the user has revealed (beyond the always-visible ones)
  const [revealedCount, setRevealedCount] = useState(alwaysVisibleCount);
  const allRevealed = revealedCount >= sections.length;

  function revealNext() {
    setRevealedCount((n) => Math.min(n + 1, sections.length));
  }

  function revealAll() {
    setRevealedCount(sections.length);
  }

  function reset() {
    setRevealedCount(alwaysVisibleCount);
  }

  return (
    <div className="space-y-8">
      {/* Control row */}
      <div className="flex items-center justify-between rounded-lg border border-indigo-100 bg-indigo-50 px-4 py-3">
        <div className="text-sm text-indigo-800">
          <span className="font-semibold">{revealedCount}</span> of{' '}
          <span className="font-semibold">{sections.length}</span> sections revealed
        </div>
        <div className="flex gap-2">
          {!allRevealed && (
            <>
              <button
                type="button"
                onClick={revealNext}
                className="rounded-md bg-indigo-600 px-3 py-1.5 text-xs font-medium text-white shadow-sm transition hover:bg-indigo-700 active:bg-indigo-800"
              >
                Reveal next →
              </button>
              <button
                type="button"
                onClick={revealAll}
                className="rounded-md border border-indigo-300 bg-white px-3 py-1.5 text-xs font-medium text-indigo-700 transition hover:bg-indigo-50"
              >
                Reveal all
              </button>
            </>
          )}
          {allRevealed && revealedCount > alwaysVisibleCount && (
            <button
              type="button"
              onClick={reset}
              className="rounded-md border border-slate-200 bg-white px-3 py-1.5 text-xs font-medium text-slate-600 transition hover:bg-slate-50"
            >
              ↩ Reset
            </button>
          )}
          {allRevealed && (
            <span className="flex items-center gap-1 text-xs font-medium text-green-700">
              ✓ Fully revealed
            </span>
          )}
        </div>
      </div>

      {/* Sections */}
      {sections.map((section, i) => {
        const isVisible = i < revealedCount;
        const isAlwaysVisible = i < alwaysVisibleCount;

        if (!isVisible) {
          // Locked placeholder
          return (
            <div
              key={i}
              className="cursor-pointer select-none rounded-xl border border-dashed border-slate-200 bg-slate-50 px-6 py-8 text-center transition hover:border-indigo-300 hover:bg-indigo-50"
              onClick={revealNext}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => e.key === 'Enter' && revealNext()}
              aria-label={`Reveal section: ${section.section_label}`}
            >
              <p className="text-sm font-medium text-slate-400">
                🔒 {section.section_label}
              </p>
              <p className="mt-1 text-xs text-slate-400">Click to reveal this section</p>
            </div>
          );
        }

        return (
          <section
            key={i}
            className={`space-y-3 ${!isAlwaysVisible ? 'animate-in' : ''}`}
          >
            <h2
              className={`border-b pb-1.5 text-base font-semibold ${
                isAlwaysVisible
                  ? 'border-slate-200 text-slate-800'
                  : 'border-indigo-200 text-indigo-900'
              }`}
            >
              {!isAlwaysVisible && (
                <span className="mr-2 inline-block rounded bg-indigo-100 px-1.5 py-0.5 text-xs font-bold text-indigo-700">
                  Revealed
                </span>
              )}
              {section.section_label}
            </h2>
            {section.content && (
              <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
                {section.content}
              </p>
            )}
            {section.fields && (
              <dl className="space-y-4">
                {section.fields.map((field, j) => (
                  <div key={j} className="space-y-1">
                    <dt className="text-xs font-semibold uppercase tracking-wide text-slate-500">
                      {field.label}
                    </dt>
                    <dd className="whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
                      {field.content}
                    </dd>
                  </div>
                ))}
              </dl>
            )}
          </section>
        );
      })}
    </div>
  );
}
