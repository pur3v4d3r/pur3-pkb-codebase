'use client';

import { useEffect, useRef, useState } from 'react';
import { useTheme } from 'next-themes';
import { exportAllData, importAllData } from '@/lib/storage';

type ImportState =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; message: string }
  | { status: 'error'; message: string };

export default function SettingsPage() {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [importState, setImportState] = useState<ImportState>({ status: 'idle' });
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);

  function handleExport() {
    exportAllData();
  }

  async function handleImport(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;
    setImportState({ status: 'loading' });
    try {
      await importAllData(file);
      setImportState({
        status: 'success',
        message: `Restored from "${file.name}". Refresh the page to see your data.`,
      });
    } catch (err) {
      setImportState({
        status: 'error',
        message: err instanceof Error ? err.message : 'Import failed.',
      });
    } finally {
      // Reset the file input so the same file can be re-selected
      if (fileInputRef.current) fileInputRef.current.value = '';
    }
  }

  return (
    <div className="mx-auto max-w-2xl space-y-10 pb-16">
      {/* ── Header ── */}
      <div>
        <h1 className="text-2xl font-bold tracking-tight text-slate-900 dark:text-slate-100">
          Settings
        </h1>
        <p className="mt-1.5 text-sm text-slate-500 dark:text-slate-400">
          Manage your application data and preferences.
        </p>
      </div>

      {/* ── Appearance ── */}
      <section className="space-y-4">
        <h2 className="text-base font-semibold text-slate-800 dark:text-slate-100">
          Appearance
        </h2>
        <div className="rounded-xl border border-slate-200 bg-white px-6 py-5 shadow-sm dark:border-slate-700 dark:bg-slate-800">
          <div className="flex items-center justify-between gap-6">
            <div>
              <p className="font-medium text-slate-800 dark:text-slate-100">Colour theme</p>
              <p className="mt-0.5 text-sm text-slate-500 dark:text-slate-400">
                Choose light, dark, or follow your system setting.
              </p>
            </div>
            {mounted ? (
              <div className="flex shrink-0 rounded-lg border border-slate-200 bg-slate-100 p-1 dark:border-slate-600 dark:bg-slate-700" role="group" aria-label="Choose colour theme">
                {([
                  { value: 'light', label: 'Light', icon: '☀️' },
                  { value: 'system', label: 'System', icon: '💻' },
                  { value: 'dark',  label: 'Dark',   icon: '🌙' },
                ] as const).map(({ value, label, icon }) => (
                  <button
                    key={value}
                    type="button"
                    onClick={() => setTheme(value)}
                    aria-pressed={theme === value}
                    className={
                      theme === value
                        ? 'flex items-center gap-1.5 rounded-md bg-white px-3 py-1.5 text-sm font-semibold text-slate-900 shadow-sm dark:bg-slate-900 dark:text-slate-100'
                        : 'flex items-center gap-1.5 rounded-md px-3 py-1.5 text-sm font-medium text-slate-500 transition hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200'
                    }
                  >
                    <span aria-hidden>{icon}</span>
                    {label}
                  </button>
                ))}
              </div>
            ) : (
              <div className="h-10 w-52 animate-pulse rounded-lg bg-slate-100 dark:bg-slate-700" />
            )}
          </div>
        </div>
      </section>

      {/* ── Data management ── */}
      <section className="space-y-4">
        <h2 className="text-base font-semibold text-slate-800 dark:text-slate-100">
          Data &amp; Backup
        </h2>
        <p className="text-sm text-slate-500 dark:text-slate-400">
          All your data — portfolio entries, reading progress, SRS review
          history, and custom cards — is stored locally in your browser.
          Export a backup before clearing your browser data or switching
          devices.
        </p>

        <div className="rounded-xl border border-slate-200 bg-white shadow-sm dark:border-slate-700 dark:bg-slate-800">
          {/* Export */}
          <div className="flex items-start justify-between gap-6 border-b border-slate-100 px-6 py-5 dark:border-slate-700">
            <div>
              <p className="font-medium text-slate-800 dark:text-slate-100">
                Export all data
              </p>
              <p className="mt-0.5 text-sm text-slate-500 dark:text-slate-400">
                Downloads a <code className="text-xs">deweyct-backup-YYYY-MM-DD.json</code>{' '}
                file containing your portfolio, SRS progress, chapter progress,
                and custom flashcards.
              </p>
            </div>
            <button
              type="button"
              onClick={handleExport}
              className="shrink-0 rounded-lg border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-700 shadow-sm transition hover:bg-slate-50 active:bg-slate-100 dark:border-slate-600 dark:bg-slate-700 dark:text-slate-200 dark:hover:bg-slate-600"
            >
              ↓ Export
            </button>
          </div>

          {/* Import */}
          <div className="flex items-start justify-between gap-6 px-6 py-5">
            <div className="min-w-0">
              <p className="font-medium text-slate-800 dark:text-slate-100">
                Import backup
              </p>
              <p className="mt-0.5 text-sm text-slate-500 dark:text-slate-400">
                Restore from a previously exported backup file. Existing data
                for each restored key will be overwritten.
              </p>

              {/* Status message */}
              {importState.status === 'loading' && (
                <p className="mt-3 text-sm text-slate-500">Importing…</p>
              )}
              {importState.status === 'success' && (
                <div className="mt-3 rounded-lg bg-green-50 px-3 py-2 text-sm text-green-800 dark:bg-green-900/30 dark:text-green-300">
                  ✓ {importState.message}
                </div>
              )}
              {importState.status === 'error' && (
                <div className="mt-3 rounded-lg bg-red-50 px-3 py-2 text-sm text-red-700 dark:bg-red-900/30 dark:text-red-300">
                  ✗ {importState.message}
                </div>
              )}
            </div>

            <div className="shrink-0">
              <input
                ref={fileInputRef}
                type="file"
                accept=".json,application/json"
                className="hidden"
                onChange={(e) => void handleImport(e)}
              />
              <button
                type="button"
                onClick={() => fileInputRef.current?.click()}
                disabled={importState.status === 'loading'}
                className="rounded-lg border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-700 shadow-sm transition hover:bg-slate-50 active:bg-slate-100 disabled:opacity-40 dark:border-slate-600 dark:bg-slate-700 dark:text-slate-200 dark:hover:bg-slate-600"
              >
                ↑ Import
              </button>
            </div>
          </div>
        </div>

        <p className="text-xs text-slate-400">
          Backup format version 1. Only DeweyCT backup files are accepted.
        </p>
      </section>

      {/* ── Danger zone ── */}
      <section className="space-y-4">
        <h2 className="text-base font-semibold text-red-700 dark:text-red-400">
          Danger Zone
        </h2>
        <div className="rounded-xl border border-red-200 bg-white px-6 py-5 shadow-sm dark:border-red-800 dark:bg-slate-800">
          <div className="flex items-start justify-between gap-6">
            <div>
              <p className="font-medium text-slate-800 dark:text-slate-100">
                Clear all local data
              </p>
              <p className="mt-0.5 text-sm text-slate-500 dark:text-slate-400">
                Permanently deletes all portfolio entries, SRS progress, chapter
                progress, and custom flashcards from this browser.{' '}
                <strong>Export a backup first.</strong>
              </p>
            </div>
            <button
              type="button"
              onClick={() => {
                if (
                  confirm(
                    'This will permanently delete ALL your DeweyCT data in this browser.\n\nExport a backup first. Are you sure?',
                  )
                ) {
                  [
                    'deweyct-portfolio',
                    'deweyct-progress',
                    'deweyct-srs-progress',
                    'deweyct-srs-user-cards',
                  ].forEach((key) => localStorage.removeItem(key));
                  window.location.reload();
                }
              }}
              className="shrink-0 rounded-lg border border-red-200 bg-white px-4 py-2 text-sm font-medium text-red-600 shadow-sm transition hover:bg-red-50 active:bg-red-100 dark:border-red-700 dark:bg-slate-700 dark:text-red-400 dark:hover:bg-slate-600"
            >
              Clear data
            </button>
          </div>
        </div>
      </section>
    </div>
  );
}
