'use client';

import { useState, useMemo } from 'react';
import type { WorkedExample } from '@/types/framework';
import WorkedExampleCard from './WorkedExampleCard';

interface Props {
  examples: WorkedExample[];
}

const ALL = 'all';

export default function FilteredWorkedExampleGrid({ examples }: Props) {
  const [framework, setFramework] = useState(ALL);
  const [difficulty, setDifficulty] = useState(ALL);

  const frameworks = useMemo(() => {
    const seen = new Map<string, string>();
    for (const e of examples) seen.set(e.framework, e.framework_label);
    return Array.from(seen.entries()).sort((a, b) => a[1].localeCompare(b[1]));
  }, [examples]);

  const filtered = useMemo(
    () =>
      examples.filter(
        (e) =>
          (framework === ALL || e.framework === framework) &&
          (difficulty === ALL || e.difficulty === difficulty),
      ),
    [examples, framework, difficulty],
  );

  return (
    <div className="space-y-6">
      {/* Filters */}
      <div className="flex flex-wrap gap-3">
        <div className="flex items-center gap-2">
          <label htmlFor="we-framework" className="text-xs font-medium text-slate-500">
            Framework
          </label>
          <select
            id="we-framework"
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
          <label htmlFor="we-difficulty" className="text-xs font-medium text-slate-500">
            Difficulty
          </label>
          <select
            id="we-difficulty"
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)}
            className="rounded-md border border-slate-200 bg-white px-3 py-1.5 text-sm text-slate-700 shadow-sm focus:border-indigo-400 focus:outline-none focus:ring-1 focus:ring-indigo-400"
          >
            <option value={ALL}>All difficulties</option>
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
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
          {filtered.length} of {examples.length}
        </span>
      </div>

      {/* Grid */}
      {filtered.length === 0 ? (
        <p className="py-12 text-center text-sm text-slate-400">
          No examples match the selected filters.
        </p>
      ) : (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {filtered.map((we) => (
            <WorkedExampleCard key={we.id} we={we} />
          ))}
        </div>
      )}
    </div>
  );
}
