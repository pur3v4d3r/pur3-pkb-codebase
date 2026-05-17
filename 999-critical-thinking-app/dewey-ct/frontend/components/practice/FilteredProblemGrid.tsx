'use client';

import { useState, useMemo } from 'react';
import type { PracticeProblem } from '@/types/framework';
import PracticeProblemCard from './PracticeProblemCard';

interface Props {
  problems: PracticeProblem[];
  initialFramework?: string;
}

const ALL = 'all';

export default function FilteredProblemGrid({ problems, initialFramework }: Props) {
  const [framework, setFramework] = useState(initialFramework ?? ALL);
  const [difficulty, setDifficulty] = useState(ALL);

  const frameworks = useMemo(() => {
    const seen = new Map<string, string>();
    for (const p of problems) seen.set(p.framework, p.framework_label);
    return Array.from(seen.entries()).sort((a, b) => a[1].localeCompare(b[1]));
  }, [problems]);

  const filtered = useMemo(
    () =>
      problems.filter(
        (p) =>
          (framework === ALL || p.framework === framework) &&
          (difficulty === ALL || p.difficulty === difficulty),
      ),
    [problems, framework, difficulty],
  );

  return (
    <div className="space-y-6">
      {/* Filters */}
      <div className="flex flex-wrap gap-3">
        <div className="flex items-center gap-2">
          <label htmlFor="pp-framework" className="text-xs font-medium text-slate-500">
            Framework
          </label>
          <select
            id="pp-framework"
            value={framework}
            onChange={(e) => setFramework(e.target.value)}
            className="rounded-md border border-slate-200 bg-white px-3 py-1.5 text-sm text-slate-700 shadow-sm focus:border-indigo-400 focus:outline-none focus:ring-1 focus:ring-indigo-400"
          >
            <option value={ALL}>All frameworks</option>
            {frameworks.map(([id, label]) => (
              <option key={id} value={id}>
                {label}
              </option>
            ))}
          </select>
        </div>

        <div className="flex items-center gap-2">
          <label htmlFor="pp-difficulty" className="text-xs font-medium text-slate-500">
            Difficulty
          </label>
          <select
            id="pp-difficulty"
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)}
            className="rounded-md border border-slate-200 bg-white px-3 py-1.5 text-sm text-slate-700 shadow-sm focus:border-indigo-400 focus:outline-none focus:ring-1 focus:ring-indigo-400"
          >
            <option value={ALL}>All difficulties</option>
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
          </select>
        </div>

        {(framework !== ALL || difficulty !== ALL) && (
          <button
            onClick={() => { setFramework(ALL); setDifficulty(ALL); }}
            className="rounded-md border border-slate-200 px-3 py-1.5 text-xs text-slate-500 transition hover:bg-slate-50"
          >
            Clear filters
          </button>
        )}

        <span className="ml-auto self-center text-xs text-slate-400">
          {filtered.length} of {problems.length}
        </span>
      </div>

      {/* Grid */}
      {filtered.length === 0 ? (
        <p className="py-12 text-center text-sm text-slate-400">
          No problems match the selected filters.
        </p>
      ) : (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {filtered.map((pp) => (
            <PracticeProblemCard key={pp.id} pp={pp} />
          ))}
        </div>
      )}
    </div>
  );
}
