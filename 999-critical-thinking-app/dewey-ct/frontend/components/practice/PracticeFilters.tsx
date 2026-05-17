'use client';

import { useState, useMemo } from 'react';
import Link from 'next/link';
import type { WorkedExample, PracticeProblem } from '@/types/framework';
import WorkedExampleCard from '@/components/practice/WorkedExampleCard';
import PracticeProblemCard from '@/components/practice/PracticeProblemCard';

interface Props {
  workedExamples: WorkedExample[];
  practiceProblems: PracticeProblem[];
}

// Normalize the two difficulty vocabularies into one for filtering
const DIFFICULTY_NORM: Record<string, string> = {
  beginner: 'Beginner',
  easy: 'Beginner',
  intermediate: 'Intermediate',
  medium: 'Intermediate',
  advanced: 'Advanced',
  hard: 'Advanced',
};

const DIFFICULTY_LEVELS = ['Beginner', 'Intermediate', 'Advanced'];

export default function PracticeFilters({ workedExamples, practiceProblems }: Props) {
  const [framework, setFramework] = useState('');
  const [difficulty, setDifficulty] = useState('');

  // Build unified sorted framework list
  const allFrameworks = useMemo(() => {
    const set = new Set([
      ...workedExamples.map((w) => w.framework_label),
      ...practiceProblems.map((p) => p.framework_label),
    ]);
    return Array.from(set).sort();
  }, [workedExamples, practiceProblems]);

  const filteredWEs = useMemo(
    () =>
      workedExamples.filter((w) => {
        const fwMatch = !framework || w.framework_label === framework;
        const diffMatch = !difficulty || DIFFICULTY_NORM[w.difficulty] === difficulty;
        return fwMatch && diffMatch;
      }),
    [workedExamples, framework, difficulty],
  );

  const filteredPPs = useMemo(
    () =>
      practiceProblems.filter((p) => {
        const fwMatch = !framework || p.framework_label === framework;
        const diffMatch = !difficulty || DIFFICULTY_NORM[p.difficulty] === difficulty;
        return fwMatch && diffMatch;
      }),
    [practiceProblems, framework, difficulty],
  );

  const isFiltered = framework !== '' || difficulty !== '';

  return (
    <>
      {/* Filter bar */}
      <div className="flex flex-wrap items-center gap-3 rounded-xl border border-slate-200 bg-slate-50 p-4">
        <div className="flex items-center gap-2">
          <label htmlFor="framework-filter" className="text-sm font-medium text-slate-700">
            Framework
          </label>
          <select
            id="framework-filter"
            value={framework}
            onChange={(e) => setFramework(e.target.value)}
            className="rounded-md border border-slate-300 bg-white px-3 py-1.5 text-sm text-slate-700 focus:border-indigo-400 focus:outline-none focus:ring-1 focus:ring-indigo-400"
          >
            <option value="">All frameworks</option>
            {allFrameworks.map((fw) => (
              <option key={fw} value={fw}>
                {fw}
              </option>
            ))}
          </select>
        </div>

        <div className="flex items-center gap-2">
          <label htmlFor="difficulty-filter" className="text-sm font-medium text-slate-700">
            Difficulty
          </label>
          <select
            id="difficulty-filter"
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)}
            className="rounded-md border border-slate-300 bg-white px-3 py-1.5 text-sm text-slate-700 focus:border-indigo-400 focus:outline-none focus:ring-1 focus:ring-indigo-400"
          >
            <option value="">All levels</option>
            {DIFFICULTY_LEVELS.map((d) => (
              <option key={d} value={d}>
                {d}
              </option>
            ))}
          </select>
        </div>

        {isFiltered && (
          <>
            <button
              onClick={() => {
                setFramework('');
                setDifficulty('');
              }}
              className="rounded-md px-2 py-1.5 text-sm text-slate-500 underline hover:text-slate-800"
            >
              Clear filters
            </button>
            <span className="ml-auto text-sm text-slate-500">
              {filteredWEs.length} example{filteredWEs.length !== 1 ? 's' : ''} ·{' '}
              {filteredPPs.length} problem{filteredPPs.length !== 1 ? 's' : ''}
            </span>
          </>
        )}
      </div>

      {/* Worked Examples */}
      <section id="worked-examples" className="space-y-5">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-bold text-slate-900">
            Worked Examples
            <span className="ml-2 text-base font-normal text-slate-400">
              ({filteredWEs.length})
            </span>
          </h2>
          <Link href="/practice/worked-examples" className="text-sm text-indigo-600 hover:underline">
            View all →
          </Link>
        </div>
        <p className="text-sm text-slate-500">
          Complete analyses with annotations, confidence tracking, and learning objectives. Read
          these before attempting the corresponding practice problems.
        </p>
        {filteredWEs.length === 0 ? (
          <p className="py-8 text-center text-sm text-slate-400">
            No worked examples match the current filters.
          </p>
        ) : (
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {filteredWEs.map((we) => (
              <WorkedExampleCard key={we.id} we={we} />
            ))}
          </div>
        )}
      </section>

      {/* Practice Problems */}
      <section id="practice-problems" className="space-y-5">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-bold text-slate-900">
            Practice Problems
            <span className="ml-2 text-base font-normal text-slate-400">
              ({filteredPPs.length})
            </span>
          </h2>
          <Link href="/practice/problems" className="text-sm text-indigo-600 hover:underline">
            View all →
          </Link>
        </div>
        <p className="text-sm text-slate-500">
          Independent practice with hints, solution sketches, and direct links to the relevant
          template. Attempt problems without hints first.
        </p>
        {filteredPPs.length === 0 ? (
          <p className="py-8 text-center text-sm text-slate-400">
            No practice problems match the current filters.
          </p>
        ) : (
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {filteredPPs.map((pp) => (
              <PracticeProblemCard key={pp.id} pp={pp} />
            ))}
          </div>
        )}
      </section>
    </>
  );
}
