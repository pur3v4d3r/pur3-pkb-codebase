/**
 * Spaced Repetition System — SM-2 Algorithm
 *
 * Standard SM-2 implementation with localStorage persistence.
 * Quality ratings (0–5) map to 4 UI buttons: Again(0) / Hard(1) / Good(3) / Easy(5).
 * Cards with no progress record are treated as new (due immediately).
 */

import { syncToBackend } from '@/lib/storage';

// ---- Types ----

export type CardSource = 'mental-model' | 'dewey-phase' | 'fallacy' | 'user';

/** A single flashcard built from the content JSON files. */
export interface SRSCard {
  id: string;
  source: CardSource;
  category: string;
  /** The question / term to memorise. */
  front: string;
  /** The primary answer / definition. */
  back: string;
  /** Optional secondary detail: example sentence or Dewey quote. */
  backDetail?: string;
}

/** A user-created card (saved from highlighted chapter text). */
export interface UserSRSCard extends SRSCard {
  source: 'user';
  /** ISO timestamp when the card was created. */
  createdAt: string;
  /** The chapter this card was created from, if any. */
  chapterId?: number;
}

/** SM-2 progress record stored in localStorage per card. */
export interface CardProgress {
  cardId: string;
  /** Ease factor — starts at 2.5, min 1.3. */
  efactor: number;
  /** Current inter-repetition interval in days. */
  interval: number;
  /** Consecutive successful repetitions. */
  repetitions: number;
  /** Next due date as YYYY-MM-DD string. */
  dueDate: string;
  /** ISO timestamp of last review. */
  lastReviewedAt?: string;
}

/**
 * Simplified quality scale used by the 4-button UI.
 * Maps to SM-2: 0=Again, 1=Hard, 3=Good, 5=Easy.
 */
export type Quality = 0 | 1 | 3 | 5;

// ---- Date helpers ----

/** Returns today's date as a YYYY-MM-DD string (local time). */
export function todayISO(): string {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
}

function addDays(dateStr: string, days: number): string {
  // Parse as local noon to avoid DST shifts flipping the date.
  const d = new Date(`${dateStr}T12:00:00`);
  d.setDate(d.getDate() + days);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
}

// ---- SM-2 Algorithm ----

/**
 * Apply an SM-2 update to a card's progress record.
 *
 * @param progress - Current progress state for the card.
 * @param quality  - User-reported recall quality (0–5).
 * @returns        - Updated progress record.
 */
export function sm2Update(progress: CardProgress, quality: Quality): CardProgress {
  let { efactor, interval, repetitions } = progress;

  if (quality < 3) {
    // Failed review — reset to beginning of schedule.
    repetitions = 0;
    interval = 1;
  } else {
    // Successful review — advance the schedule.
    if (repetitions === 0) {
      interval = 1;
    } else if (repetitions === 1) {
      interval = 6;
    } else {
      interval = Math.round(interval * efactor);
    }
    repetitions += 1;
  }

  // Update ease factor; clamp to minimum 1.3.
  // Formula: EF' = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
  efactor = Math.max(
    1.3,
    efactor + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02),
  );

  return {
    ...progress,
    efactor: Math.round(efactor * 1000) / 1000,
    interval,
    repetitions,
    dueDate: addDays(todayISO(), interval),
    lastReviewedAt: new Date().toISOString(),
  };
}

/** Returns true if the card is due today or overdue. */
export function isDue(progress: CardProgress): boolean {
  return progress.dueDate <= todayISO();
}

// ---- localStorage ----

const SRS_KEY = 'deweyct-srs-progress';

/** Reads all SRS progress records from localStorage. */
export function getSRSProgress(): Record<string, CardProgress> {
  if (typeof window === 'undefined') return {};
  try {
    const raw = localStorage.getItem(SRS_KEY);
    return raw ? (JSON.parse(raw) as Record<string, CardProgress>) : {};
  } catch {
    return {};
  }
}

/** Persists a single card's progress to localStorage. */
export function saveCardProgress(progress: CardProgress): void {
  const all = getSRSProgress();
  all[progress.cardId] = progress;
  localStorage.setItem(SRS_KEY, JSON.stringify(all));
  syncToBackend();
}

/** Removes all SRS progress from localStorage. */
export function resetSRSProgress(): void {
  if (typeof window !== 'undefined') {
    localStorage.removeItem(SRS_KEY);
  }
}

// ---- Session helpers ----

/**
 * Returns the earliest future due date across all cards,
 * or null if no cards have been scheduled yet.
 */
export function getNextReviewDate(
  cards: SRSCard[],
  progress: Record<string, CardProgress>,
): string | null {
  const today = todayISO();
  const future = cards
    .map((c) => progress[c.id]?.dueDate)
    .filter((d): d is string => !!d && d > today)
    .sort();
  return future[0] ?? null;
}

// ---- User-created cards ----

const USER_CARDS_KEY = 'deweyct-srs-user-cards';

/** Returns all user-created SRS cards from localStorage. */
export function getUserSRSCards(): UserSRSCard[] {
  if (typeof window === 'undefined') return [];
  try {
    const raw = localStorage.getItem(USER_CARDS_KEY);
    return raw ? (JSON.parse(raw) as UserSRSCard[]) : [];
  } catch {
    return [];
  }
}

/** Saves (inserts or updates) a user-created card in localStorage. */
export function saveUserSRSCard(card: UserSRSCard): void {
  const cards = getUserSRSCards();
  const idx = cards.findIndex((c) => c.id === card.id);
  if (idx >= 0) {
    cards[idx] = card;
  } else {
    cards.push(card);
  }
  localStorage.setItem(USER_CARDS_KEY, JSON.stringify(cards));
}

/** Removes a user-created card and its SRS progress from localStorage. */
export function deleteUserSRSCard(id: string): void {
  const cards = getUserSRSCards().filter((c) => c.id !== id);
  localStorage.setItem(USER_CARDS_KEY, JSON.stringify(cards));
  // Also remove progress record so it doesn't linger
  const progress = getSRSProgress();
  if (id in progress) {
    delete progress[id];
    localStorage.setItem(SRS_KEY, JSON.stringify(progress));
  }
}
