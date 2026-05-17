'use client';

import { getPortfolio, deletePortfolioEntry, exportAllData, importAllData } from '@/lib/storage';
import { useEffect, useRef, useState } from 'react';
import Link from 'next/link';
import type { PortfolioEntry } from '@/types/framework';

const typeColors: Record<string, string> = {
  template: 'bg-indigo-100 text-indigo-800',
  exercise: 'bg-green-100 text-green-800',
  reflection: 'bg-amber-100 text-amber-800',
};

export default function PortfolioPage() {
  const [entries, setEntries] = useState<PortfolioEntry[]>([]);
  const [confirmDelete, setConfirmDelete] = useState<string | null>(null);
  const [importStatus, setImportStatus] = useState<
    { type: 'success' | 'error'; message: string } | null
  >(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    setEntries(getPortfolio());
  }, []);

  function handleDelete(id: string) {
    if (confirmDelete !== id) {
      setConfirmDelete(id);
      return;
    }
    deletePortfolioEntry(id);
    setEntries(getPortfolio());
    setConfirmDelete(null);
  }

  function handleExport() {
    exportAllData();
  }

  function handleImportClick() {
    setImportStatus(null);
    fileInputRef.current?.click();
  }

  async function handleFileChange(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;
    // Reset input so the same file can be re-selected if needed
    e.target.value = '';
    try {
      await importAllData(file);
      setEntries(getPortfolio());
      setImportStatus({ type: 'success', message: 'Data imported successfully.' });
    } catch (err) {
      setImportStatus({
        type: 'error',
        message: err instanceof Error ? err.message : 'Import failed.',
      });
    }
  }

  // Sort newest first
  const sorted = [...entries].sort(
    (a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime(),
  );

  return (
    <div className="space-y-6">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
        <div className="space-y-1">
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Portfolio</h1>
          <p className="text-sm text-slate-500">
            Your saved thinking exercises, template responses, and reflections — stored locally in your browser.
          </p>
        </div>

        {/* Export / Import toolbar */}
        <div className="flex shrink-0 items-center gap-2">
          <button
            type="button"
            onClick={handleExport}
            title="Download all portfolio, SRS, and chapter progress as a JSON file"
            className="rounded-lg border border-slate-200 bg-white px-3 py-1.5 text-xs font-medium text-slate-600 shadow-sm transition hover:border-slate-300 hover:bg-slate-50 active:bg-slate-100"
          >
            ↓ Export all
          </button>
          <button
            type="button"
            onClick={handleImportClick}
            title="Restore from a previously exported JSON backup"
            className="rounded-lg border border-slate-200 bg-white px-3 py-1.5 text-xs font-medium text-slate-600 shadow-sm transition hover:border-slate-300 hover:bg-slate-50 active:bg-slate-100"
          >
            ↑ Import
          </button>
          <input
            ref={fileInputRef}
            type="file"
            accept=".json,application/json"
            onChange={handleFileChange}
            className="hidden"
            aria-hidden="true"
          />
        </div>
      </div>

      {/* Import feedback */}
      {importStatus && (
        <div
          className={`rounded-lg px-4 py-2.5 text-sm ${
            importStatus.type === 'success'
              ? 'bg-green-50 text-green-800'
              : 'bg-red-50 text-red-700'
          }`}
        >
          {importStatus.message}
        </div>
      )}

      {sorted.length === 0 ? (
        <div className="rounded-lg border border-dashed border-slate-300 bg-white p-12 text-center">
          <p className="text-sm text-slate-500">No portfolio entries yet.</p>
          <p className="mt-1 text-xs text-slate-400">
            Complete a template or exercise to save your first entry.
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-4">
          {sorted.map((entry) => (
            <div
              key={entry.id}
              className="group rounded-lg border border-slate-200 bg-white shadow-sm transition hover:border-slate-300 hover:shadow"
            >
              <Link href={`/portfolio/${entry.id}`} className="block p-4">
                <div className="flex items-start justify-between gap-2">
                  <h2 className="text-sm font-semibold text-slate-900 group-hover:text-indigo-700">
                    {entry.title}
                  </h2>
                  <span
                    className={`flex-shrink-0 rounded-full px-2 py-0.5 text-xs font-medium ${typeColors[entry.type] ?? 'bg-slate-100 text-slate-600'}`}
                  >
                    {entry.type}
                  </span>
                </div>
                <div className="mt-1 flex flex-wrap items-center gap-2 text-xs text-slate-500">
                  <span>{new Date(entry.createdAt).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}</span>
                  {entry.chapterRef && <span>· Ch {entry.chapterRef}</span>}
                  {entry.tags.map((tag) => (
                    <span key={tag} className="rounded-full bg-slate-100 px-1.5 py-0.5 text-slate-600">
                      #{tag}
                    </span>
                  ))}
                </div>
              </Link>

              {/* Delete controls — outside the Link to avoid nested interactive elements */}
              <div className="flex items-center justify-end gap-2 border-t border-slate-100 px-4 py-2">
                {confirmDelete === entry.id && (
                  <>
                    <span className="text-xs text-red-600">Delete this entry?</span>
                    <button
                      type="button"
                      onClick={() => setConfirmDelete(null)}
                      className="text-xs text-slate-400 hover:text-slate-600"
                    >
                      Cancel
                    </button>
                  </>
                )}
                <button
                  type="button"
                  onClick={() => handleDelete(entry.id)}
                  className={`rounded px-2 py-1 text-xs font-medium transition ${
                    confirmDelete === entry.id
                      ? 'bg-red-600 text-white hover:bg-red-700'
                      : 'text-slate-400 hover:text-red-500'
                  }`}
                >
                  {confirmDelete === entry.id ? 'Confirm' : 'Delete'}
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
