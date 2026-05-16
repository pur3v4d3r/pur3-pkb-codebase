import type { PortfolioEntry } from '@/types/framework';

const PORTFOLIO_KEY = 'deweyct-portfolio';
const PROGRESS_KEY = 'deweyct-progress';

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
}

export function deletePortfolioEntry(id: string): void {
  const portfolio = getPortfolio().filter((e) => e.id !== id);
  localStorage.setItem(PORTFOLIO_KEY, JSON.stringify(portfolio));
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
}

export function isChapterRead(chapterId: number): boolean {
  return chapterId in getProgress();
}

// ---- Simple ID generator ----

export function generateId(): string {
  return `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 7)}`;
}
