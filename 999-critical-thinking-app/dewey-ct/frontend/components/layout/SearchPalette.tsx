'use client';

import Fuse from 'fuse.js';
import { useCallback, useEffect, useRef, useState } from 'react';
import { useRouter } from 'next/navigation';
import type { SearchItem } from '@/app/api/search/route';

// ---- Badge styles per type ----

const TYPE_BADGE: Record<string, string> = {
  chapter: 'bg-blue-100 text-blue-700',
  framework: 'bg-violet-100 text-violet-700',
  'mental-model': 'bg-teal-100 text-teal-700',
  template: 'bg-amber-100 text-amber-700',
};

const TYPE_LABEL: Record<string, string> = {
  chapter: 'Chapter',
  framework: 'Framework',
  'mental-model': 'Mental Model',
  template: 'Template',
};

// ---- Fuse config ----

const FUSE_OPTIONS = {
  keys: [
    { name: 'title', weight: 2 },
    { name: 'subtitle', weight: 1 },
  ],
  threshold: 0.35,
  minMatchCharLength: 2,
  includeMatches: false,
};

// ---- Component ----

export default function SearchPalette() {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [allItems, setAllItems] = useState<SearchItem[]>([]);
  const [results, setResults] = useState<SearchItem[]>([]);
  const [activeIdx, setActiveIdx] = useState(0);
  const [loadError, setLoadError] = useState(false);
  const fuseRef = useRef<Fuse<SearchItem> | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const listRef = useRef<HTMLUListElement>(null);
  const fetchedRef = useRef(false);

  // --- Keyboard shortcut to open ---
  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setOpen((o) => !o);
      }
      if (e.key === 'Escape') setOpen(false);
    }
    document.addEventListener('keydown', onKeyDown);
    return () => document.removeEventListener('keydown', onKeyDown);
  }, []);

  // --- Focus input when opened ---
  useEffect(() => {
    if (open) {
      // Fetch index on first open
      if (!fetchedRef.current) {
        fetchedRef.current = true;
        fetch('/api/search')
          .then((r) => r.json())
          .then((data: SearchItem[]) => {
            setAllItems(data);
            fuseRef.current = new Fuse(data, FUSE_OPTIONS);
            // Show top items immediately
            setResults(data.slice(0, 8));
          })
          .catch(() => setLoadError(true));
      }
      setTimeout(() => inputRef.current?.focus(), 30);
    } else {
      setQuery('');
      setActiveIdx(0);
    }
  }, [open]);

  // --- Fuse search ---
  const handleQuery = useCallback(
    (q: string) => {
      setQuery(q);
      setActiveIdx(0);
      if (!fuseRef.current) return;
      if (q.trim().length < 2) {
        setResults(allItems.slice(0, 8));
        return;
      }
      setResults(fuseRef.current.search(q).map((r) => r.item).slice(0, 10));
    },
    [allItems],
  );

  // --- Scroll active item into view ---
  useEffect(() => {
    const el = listRef.current?.querySelector(`[data-idx="${activeIdx}"]`) as HTMLElement | null;
    el?.scrollIntoView({ block: 'nearest' });
  }, [activeIdx]);

  // --- Navigate to selected item ---
  function navigateTo(item: SearchItem) {
    setOpen(false);
    router.push(item.href);
  }

  // --- Keyboard navigation inside palette ---
  function handleKeyDown(e: React.KeyboardEvent<HTMLInputElement>) {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setActiveIdx((i) => Math.min(i + 1, results.length - 1));
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setActiveIdx((i) => Math.max(i - 1, 0));
    } else if (e.key === 'Enter') {
      e.preventDefault();
      const item = results[activeIdx];
      if (item) navigateTo(item);
    }
  }

  if (!open) {
    return null;
  }

  return (
    <>
      {/* Backdrop */}
      <div
        className="fixed inset-0 z-40 bg-black/40 backdrop-blur-[2px]"
        onClick={() => setOpen(false)}
        aria-hidden="true"
      />

      {/* Palette */}
      <div
        className="fixed left-1/2 top-[15vh] z-50 w-full max-w-xl -translate-x-1/2 overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-2xl"
        role="dialog"
        aria-label="Search"
        aria-modal="true"
      >
        {/* Input row */}
        <div className="flex items-center gap-3 border-b border-slate-100 px-4 py-3">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 shrink-0 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="m21 21-4.35-4.35m0 0A7.5 7.5 0 1 0 5.15 5.15a7.5 7.5 0 0 0 11.5 11.5Z" />
          </svg>
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={(e) => handleQuery(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Search chapters, frameworks, models, templates…"
            className="min-w-0 flex-1 bg-transparent text-sm text-slate-900 placeholder-slate-400 focus:outline-none"
            autoComplete="off"
            spellCheck={false}
          />
          <button
            type="button"
            onClick={() => setOpen(false)}
            className="shrink-0 rounded border border-slate-200 bg-slate-100 px-1.5 py-0.5 font-mono text-[10px] text-slate-500"
          >
            Esc
          </button>
        </div>

        {/* Results */}
        <div className="max-h-[min(60vh,400px)] overflow-y-auto">
          {loadError ? (
            <p className="px-4 py-6 text-center text-sm text-slate-400">Failed to load search index.</p>
          ) : results.length === 0 && query.trim().length >= 2 ? (
            <p className="px-4 py-6 text-center text-sm text-slate-400">No results for &ldquo;{query}&rdquo;</p>
          ) : (
            <ul ref={listRef} role="listbox" aria-label="Search results">
              {results.map((item, idx) => (
                <li
                  key={item.id}
                  data-idx={idx}
                  role="option"
                  aria-selected={activeIdx === idx}
                  onMouseEnter={() => setActiveIdx(idx)}
                  onClick={() => navigateTo(item)}
                  className={`flex cursor-pointer items-center gap-3 px-4 py-3 transition ${
                    activeIdx === idx ? 'bg-indigo-50' : 'hover:bg-slate-50'
                  }`}
                >
                  <div className="min-w-0 flex-1">
                    <p className={`truncate text-sm font-medium ${activeIdx === idx ? 'text-indigo-900' : 'text-slate-800'}`}>
                      {item.title}
                    </p>
                    {item.subtitle && (
                      <p className="truncate text-xs text-slate-400">{item.subtitle}</p>
                    )}
                  </div>
                  <span
                    className={`shrink-0 rounded-full px-2 py-0.5 text-[10px] font-semibold ${TYPE_BADGE[item.type] ?? 'bg-slate-100 text-slate-600'}`}
                  >
                    {TYPE_LABEL[item.type] ?? item.type}
                  </span>
                </li>
              ))}
            </ul>
          )}
        </div>

        {/* Footer hint */}
        {results.length > 0 && (
          <div className="flex items-center gap-3 border-t border-slate-100 px-4 py-2 text-[10px] text-slate-400">
            <span><kbd className="font-mono">↑↓</kbd> navigate</span>
            <span><kbd className="font-mono">↵</kbd> open</span>
            <span><kbd className="font-mono">Esc</kbd> close</span>
          </div>
        )}
      </div>
    </>
  );
}
