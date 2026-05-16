'use client';

import { getPortfolio } from '@/lib/storage';
import { useEffect, useState } from 'react';
import type { PortfolioEntry } from '@/types/framework';

export default function PortfolioPage() {
  const [entries, setEntries] = useState<PortfolioEntry[]>([]);

  useEffect(() => {
    setEntries(getPortfolio());
  }, []);

  return (
    <div className="space-y-6">
      <div className="space-y-1">
        <h1 className="text-2xl font-bold tracking-tight text-slate-900">Portfolio</h1>
        <p className="text-sm text-slate-500">
          Your saved thinking exercises, template responses, and reflections — stored locally in your browser.
        </p>
      </div>

      {entries.length === 0 ? (
        <div className="rounded-lg border border-dashed border-slate-300 bg-white p-12 text-center">
          <p className="text-sm text-slate-500">No portfolio entries yet.</p>
          <p className="mt-1 text-xs text-slate-400">
            Complete a template or exercise to save your first entry.
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-4">
          {entries.map((entry) => (
            <div key={entry.id} className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
              <div className="flex items-start justify-between gap-2">
                <h2 className="text-sm font-semibold text-slate-900">{entry.title}</h2>
                <span className="rounded-full bg-slate-100 px-2 py-0.5 text-xs text-slate-600">{entry.type}</span>
              </div>
              <p className="mt-1 text-xs text-slate-500">
                {new Date(entry.createdAt).toLocaleDateString()}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
