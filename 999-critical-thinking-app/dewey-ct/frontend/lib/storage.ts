import type { PortfolioEntry } from '@/types/framework';

const PORTFOLIO_KEY = 'deweyct-portfolio';
const PROGRESS_KEY = 'deweyct-progress';

const BACKEND_URL = (process.env.NEXT_PUBLIC_BACKEND_URL ?? 'http://localhost:8000') as string;
let _syncTimer: ReturnType<typeof setTimeout> | null = null;

// ---- Portfolio ----

export function getPortfolio(): PortfolioEntry[] {
  if (typeof window === 'undefined') return [];
  try {
    const raw = localStorage.getItem(PORTFOLIO_KEY);
    return raw ? (JSON.parse(raw) as PortfolioEntry[]) : [];
  } catch {
    return [];
  }
}

export function savePortfolioEntry(entry: PortfolioEntry): void {
  const portfolio = getPortfolio();
  const idx = portfolio.findIndex((e) => e.id === entry.id);
  if (idx >= 0) {
    portfolio[idx] = entry;
  } else {
    portfolio.push(entry);
  }
  localStorage.setItem(PORTFOLIO_KEY, JSON.stringify(portfolio));
  syncToBackend();
}

export function getPortfolioEntry(id: string): PortfolioEntry | undefined {
  return getPortfolio().find((e) => e.id === id);
}

export function deletePortfolioEntry(id: string): void {
  const portfolio = getPortfolio().filter((e) => e.id !== id);
  localStorage.setItem(PORTFOLIO_KEY, JSON.stringify(portfolio));
  syncToBackend();
}

// ---- Reading Progress ----

export interface ChapterProgress {
  chapterId: number;
  completedAt: string;
  timeSpentSeconds?: number;
}

export function getProgress(): Record<number, ChapterProgress> {
  if (typeof window === 'undefined') return {};
  try {
    const raw = localStorage.getItem(PROGRESS_KEY);
    return raw ? (JSON.parse(raw) as Record<number, ChapterProgress>) : {};
  } catch {
    return {};
  }
}

export function markChapterRead(chapterId: number, timeSpentSeconds?: number): void {
  const progress = getProgress();
  progress[chapterId] = {
    chapterId,
    completedAt: new Date().toISOString(),
    timeSpentSeconds,
  };
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress));
  syncToBackend();
}

export function isChapterRead(chapterId: number): boolean {
  return chapterId in getProgress();
}

// ---- Simple ID generator ----

export function generateId(): string {
  return `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 7)}`;
}

// ---- Export / Import all local data ----

/** All localStorage keys managed by this app. */
const ALL_STORAGE_KEYS = {
  portfolio: PORTFOLIO_KEY,
  chapterProgress: PROGRESS_KEY,
  srsProgress: 'deweyct-srs-progress',
} as const;

export interface AppBackup {
  version: 1;
  exportedAt: string;
  data: {
    portfolio: unknown;
    chapterProgress: unknown;
    srsProgress: unknown;
  };
}

/** Serialise all localStorage data and trigger a JSON file download. */
export function exportAllData(): void {
  const backup: AppBackup = {
    version: 1,
    exportedAt: new Date().toISOString(),
    data: {
      portfolio: safeParseLS(ALL_STORAGE_KEYS.portfolio),
      chapterProgress: safeParseLS(ALL_STORAGE_KEYS.chapterProgress),
      srsProgress: safeParseLS(ALL_STORAGE_KEYS.srsProgress),
    },
  };
  const blob = new Blob([JSON.stringify(backup, null, 2)], {
    type: 'application/json',
  });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `deweyct-backup-${new Date().toISOString().slice(0, 10)}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function safeParseLS(key: string): unknown {
  try {
    const raw = localStorage.getItem(key);
    return raw ? (JSON.parse(raw) as unknown) : null;
  } catch {
    return null;
  }
}

/**
 * Restore all localStorage keys from a backup file.
 * Existing data is overwritten only for keys present in the backup.
 * Rejects with a descriptive error if the file is invalid.
 */
export function importAllData(file: File): Promise<void> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      try {
        const raw = e.target?.result;
        if (typeof raw !== 'string') {
          reject(new Error('Could not read file contents.'));
          return;
        }
        const backup = JSON.parse(raw) as AppBackup;
        if (
          !backup ||
          backup.version !== 1 ||
          typeof backup.data !== 'object' ||
          backup.data === null
        ) {
          reject(
            new Error(
              'Invalid backup format. Expected a DeweyCT backup with version: 1.',
            ),
          );
          return;
        }
        const { data } = backup;
        if (data.portfolio != null) {
          localStorage.setItem(
            ALL_STORAGE_KEYS.portfolio,
            JSON.stringify(data.portfolio),
          );
        }
        if (data.chapterProgress != null) {
          localStorage.setItem(
            ALL_STORAGE_KEYS.chapterProgress,
            JSON.stringify(data.chapterProgress),
          );
        }
        if (data.srsProgress != null) {
          localStorage.setItem(
            ALL_STORAGE_KEYS.srsProgress,
            JSON.stringify(data.srsProgress),
          );
        }
        resolve();
      } catch (err) {
        reject(
          err instanceof Error
            ? err
            : new Error('Failed to parse backup file.'),
        );
      }
    };
    reader.onerror = () => reject(new Error('Failed to read file.'));
    reader.readAsText(file);
  });
}

// ---- Backend sync ----

/**
 * Debounced (400 ms) fire-and-forget sync of all localStorage data to the
 * FastAPI backend SQLite store. Silent on failure — localStorage remains the
 * primary source of truth; the backend is a durable mirror.
 */
export function syncToBackend(): void {
  if (typeof window === 'undefined') return;
  if (_syncTimer !== null) clearTimeout(_syncTimer);
  _syncTimer = setTimeout(() => {
    const payload = {
      portfolio: safeParseLS(ALL_STORAGE_KEYS.portfolio),
      chapterProgress: safeParseLS(ALL_STORAGE_KEYS.chapterProgress),
      srsProgress: safeParseLS(ALL_STORAGE_KEYS.srsProgress),
    };
    fetch(`${BACKEND_URL}/api/data`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    }).catch(() => {
      /* backend unavailable — localStorage is still persisted locally */
    });
  }, 400);
}

/**
 * Called once on app startup. For each localStorage key that is absent,
 * fills it from the backend SQLite store. Non-destructive: only populates
 * empty slots so existing local edits are never overwritten.
 */
export async function hydrateFromBackend(): Promise<void> {
  if (typeof window === 'undefined') return;
  try {
    const res = await fetch(`${BACKEND_URL}/api/data`);
    if (!res.ok) return;
    const remote = (await res.json()) as {
      portfolio: unknown;
      chapterProgress: unknown;
      srsProgress: unknown;
    };
    if (remote.portfolio != null && !localStorage.getItem(ALL_STORAGE_KEYS.portfolio)) {
      localStorage.setItem(ALL_STORAGE_KEYS.portfolio, JSON.stringify(remote.portfolio));
    }
    if (
      remote.chapterProgress != null &&
      !localStorage.getItem(ALL_STORAGE_KEYS.chapterProgress)
    ) {
      localStorage.setItem(
        ALL_STORAGE_KEYS.chapterProgress,
        JSON.stringify(remote.chapterProgress),
      );
    }
    if (remote.srsProgress != null && !localStorage.getItem(ALL_STORAGE_KEYS.srsProgress)) {
      localStorage.setItem(ALL_STORAGE_KEYS.srsProgress, JSON.stringify(remote.srsProgress));
    }
  } catch {
    /* backend unavailable on load — fall through; localStorage is sufficient */
  }
}
