'use client';

import { useState, useMemo } from 'react';
import Link from 'next/link';
import type { MentalModel, MentalModelCategory } from '@/types/framework';

interface Props {
  models: MentalModel[];
  categories: MentalModelCategory[];
}

const BLOOM_LEVELS = ['Remember', 'Understand', 'Apply', 'Analyze', 'Evaluate', 'Create'];

const CATEGORY_COLORS: Record<string, string> = {
  'Reasoning and Logic': 'bg-indigo-50 text-indigo-700 border-indigo-200',
  'Systems Thinking': 'bg-teal-50 text-teal-700 border-teal-200',
  'Decision Making': 'bg-amber-50 text-amber-700 border-amber-200',
  'Cognitive Biases': 'bg-rose-50 text-rose-700 border-rose-200',
  'Epistemology': 'bg-violet-50 text-violet-700 border-violet-200',
};

const BLOOM_COLORS: Record<string, string> = {
  Remember: 'bg-slate-100 text-slate-600',
  Understand: 'bg-blue-50 text-blue-600',
  Apply: 'bg-green-50 text-green-600',
  Analyze: 'bg-amber-50 text-amber-700',
  Evaluate: 'bg-orange-50 text-orange-700',
  Create: 'bg-purple-50 text-purple-700',
};

function CategoryBadge({ category }: { category: string }) {
  const cls = CATEGORY_COLORS[category] ?? 'bg-slate-50 text-slate-600 border-slate-200';
  return (
    <span className={`inline-flex items-center rounded border px-1.5 py-0.5 text-[10px] font-medium ${cls}`}>
      {category}
    </span>
  );
}

function BloomBadge({ level }: { level: string }) {
  const cls = BLOOM_COLORS[level] ?? 'bg-slate-100 text-slate-600';
  return (
    <span className={`inline-flex items-center rounded px-1.5 py-0.5 text-[10px] font-medium ${cls}`}>
      Bloom: {level}
    </span>
  );
}

export default function MentalModelsHub({ models, categories }: Props) {
  const [activeCategory, setActiveCategory] = useState('');
  const [activeBloom, setActiveBloom] = useState('');
  const [query, setQuery] = useState('');

  const filtered = useMemo(() => {
    return models.filter((m) => {
      if (activeCategory && m.category !== activeCategory) return false;
      if (activeBloom && m.bloom_level !== activeBloom) return false;
      if (query) {
        const q = query.toLowerCase();
        return (
          m.name.toLowerCase().includes(q) ||
          m.definition.toLowerCase().includes(q) ||
          m.category.toLowerCase().includes(q)
        );
      }
      return true;
    });
  }, [models, activeCategory, activeBloom, query]);

  const bloomsPresent = useMemo(
    () => BLOOM_LEVELS.filter((b) => models.some((m) => m.bloom_level === b)),
    [models],
  );

  const clearAll = () => {
    setActiveCategory('');
    setActiveBloom('');
    setQuery('');
  };

  const hasFilters = activeCategory || activeBloom || query;

  return (
    <div className="space-y-6">
      {/* Filters */}
      <div className="space-y-3 rounded-xl border border-slate-200 bg-white p-4">
        {/* Search */}
        <div>
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search models by name or definition…"
            className="w-full rounded-md border border-slate-300 px-3 py-2 text-sm text-slate-800 placeholder-slate-400 focus:border-indigo-400 focus:outline-none focus:ring-1 focus:ring-indigo-300"
          />
        </div>

        {/* Category filter */}
        <div className="space-y-1.5">
          <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">Category</p>
          <div className="flex flex-wrap gap-2">
            <button
              onClick={() => setActiveCategory('')}
              className={`rounded-full px-3 py-1 text-xs font-medium transition ${
                !activeCategory
                  ? 'bg-slate-800 text-white'
                  : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
              }`}
            >
              All ({models.length})
            </button>
            {categories.map((cat) => (
              <button
                key={cat.category}
                onClick={() => setActiveCategory(cat.category === activeCategory ? '' : cat.category)}
                className={`rounded-full px-3 py-1 text-xs font-medium transition ${
                  activeCategory === cat.category
                    ? 'bg-slate-800 text-white'
                    : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                }`}
              >
                {cat.category} ({cat.model_count})
              </button>
            ))}
          </div>
        </div>

        {/* Bloom filter */}
        <div className="space-y-1.5">
          <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">Bloom Level</p>
          <div className="flex flex-wrap gap-2">
            <button
              onClick={() => setActiveBloom('')}
              className={`rounded-full px-3 py-1 text-xs font-medium transition ${
                !activeBloom
                  ? 'bg-slate-800 text-white'
                  : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
              }`}
            >
              All
            </button>
            {bloomsPresent.map((b) => (
              <button
                key={b}
                onClick={() => setActiveBloom(b === activeBloom ? '' : b)}
                className={`rounded-full px-3 py-1 text-xs font-medium transition ${
                  activeBloom === b
                    ? 'bg-slate-800 text-white'
                    : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                }`}
              >
                {b}
              </button>
            ))}
          </div>
        </div>

        {/* Results count + clear */}
        <div className="flex items-center justify-between pt-1">
          <p className="text-xs text-slate-500">
            Showing <span className="font-semibold text-slate-700">{filtered.length}</span> of {models.length} models
          </p>
          {hasFilters && (
            <button
              onClick={clearAll}
              className="text-xs font-medium text-indigo-600 hover:underline"
            >
              Clear filters
            </button>
          )}
        </div>
      </div>

      {/* Model grid */}
      {filtered.length === 0 ? (
        <div className="rounded-xl border border-dashed border-slate-300 py-12 text-center">
          <p className="text-sm text-slate-500">No models match your filters.</p>
          <button onClick={clearAll} className="mt-2 text-xs font-medium text-indigo-600 hover:underline">
            Clear filters
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {filtered.map((model) => (
            <Link
              key={model.id}
              href={`/mental-models/${model.id}`}
              className="group flex flex-col rounded-lg border border-slate-200 bg-white p-4 shadow-sm transition hover:border-slate-400 hover:shadow-md"
            >
              <div className="mb-2 flex flex-wrap gap-1.5">
                <CategoryBadge category={model.category} />
                <BloomBadge level={model.bloom_level} />
              </div>
              <h3 className="mb-1.5 text-sm font-semibold text-slate-900 group-hover:text-indigo-700">
                {model.name}
              </h3>
              <p className="flex-1 text-xs leading-relaxed text-slate-600 line-clamp-3">
                {model.definition}
              </p>
              <p className="mt-3 text-xs font-medium text-slate-400 group-hover:text-indigo-500">
                View model →
              </p>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
