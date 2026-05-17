'use client';

import { useState, useMemo } from 'react';
import CheatSheetCard, { CATEGORY_COLORS } from './CheatSheetCard';
import type { CheatSheet } from '@/types/framework';

// Static category assignment — derived from framework names, not stored in JSON
const CATEGORY_MAP: Record<string, string> = {
  'Ennis — FRISCO': 'CT Frameworks',
  'Delphi — Six Core Skills': 'CT Frameworks',
  'Halpern — Five Skill Categories': 'CT Frameworks',
  'Lipman — Three Thinking Modes': 'CT Frameworks',
  'Brookfield — Four Activities': 'CT Frameworks',
  'Watson-Glaser — RED Model': 'Argument Analysis',
  'Toulmin Argument Model': 'Argument Analysis',
  'Browne & Keeley — 10 Critical Questions': 'Argument Analysis',
  'CCTDI — Seven Dispositions': 'Dispositions',
  'Dual-Process Theory': 'Cognitive Models',
  'Developmental Models Quick Reference': 'Cognitive Models',
  "Marzano's Three Systems": 'Cognitive Models',
  'Bloom Revised — Cognitive Levels': 'Taxonomies',
  'SOLO Taxonomy': 'Taxonomies',
  "Webb's Depth of Knowledge (DOK)": 'Taxonomies',
  'DIKW Pyramid': 'Taxonomies',
  'Bloom Affective Domain': 'Taxonomies',
};

const ALL_CATEGORIES = [
  'All',
  'CT Frameworks',
  'Argument Analysis',
  'Dispositions',
  'Cognitive Models',
  'Taxonomies',
] as const;

const CATEGORY_COUNT: Record<string, number> = {
  'CT Frameworks': 5,
  'Argument Analysis': 3,
  Dispositions: 1,
  'Cognitive Models': 3,
  Taxonomies: 5,
};

interface Props {
  sheets: CheatSheet[];
}

export default function CheatSheetsHub({ sheets }: Props) {
  const [query, setQuery] = useState('');
  const [activeCategory, setActiveCategory] = useState<string>('All');

  const sheetsWithCategory = useMemo(
    () =>
      sheets.map((sheet) => ({
        sheet,
        category: CATEGORY_MAP[sheet.framework] ?? 'CT Frameworks',
      })),
    [sheets],
  );

  const filtered = useMemo(() => {
    return sheetsWithCategory.filter(({ sheet, category }) => {
      if (activeCategory !== 'All' && category !== activeCategory) return false;
      if (query.trim()) {
        return sheet.framework.toLowerCase().includes(query.toLowerCase());
      }
      return true;
    });
  }, [sheetsWithCategory, activeCategory, query]);

  return (
    <div>
      {/* Filter bar */}
      <div className="flex flex-col sm:flex-row gap-3 mb-5">
        <input
          type="search"
          placeholder="Search frameworks…"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="flex-1 px-4 py-2 rounded-lg border border-slate-300 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400 bg-white"
        />
        <div className="flex flex-wrap gap-2">
          {ALL_CATEGORIES.map((cat) => {
            const isActive = activeCategory === cat;
            const count = cat === 'All' ? sheets.length : (CATEGORY_COUNT[cat] ?? 0);
            const activeStyle =
              cat === 'All'
                ? 'bg-slate-700 text-white'
                : `${CATEGORY_COLORS[cat]?.header ?? 'bg-slate-600'} text-white`;
            return (
              <button
                key={cat}
                onClick={() => setActiveCategory(cat)}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-colors flex items-center gap-1.5 ${
                  isActive ? activeStyle : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                }`}
              >
                {cat}
                <span
                  className={`text-[10px] px-1 py-0.5 rounded-full ${
                    isActive ? 'bg-white/20' : 'bg-slate-300/60 text-slate-600'
                  }`}
                >
                  {count}
                </span>
              </button>
            );
          })}
        </div>
      </div>

      {/* Result count */}
      <p className="text-xs text-slate-500 mb-5">
        Showing <span className="font-semibold text-slate-700">{filtered.length}</span> of{' '}
        {sheets.length} cheat sheets
        {query && (
          <>
            {' '}
            matching <span className="italic">&ldquo;{query}&rdquo;</span>
          </>
        )}
      </p>

      {/* Grid */}
      {filtered.length === 0 ? (
        <div className="text-center py-16 text-slate-500">
          <p className="text-4xl mb-3">🔍</p>
          <p className="font-medium">No sheets match your filters.</p>
          <button
            onClick={() => {
              setQuery('');
              setActiveCategory('All');
            }}
            className="mt-3 text-sm text-indigo-600 hover:underline"
          >
            Clear filters
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
          {filtered.map(({ sheet, category }) => (
            <CheatSheetCard key={sheet.framework} sheet={sheet} category={category} />
          ))}
        </div>
      )}
    </div>
  );
}
