/**
 * useDashboardStats — aggregates all localStorage + fetched data into
 * a single stats object for the /dashboard page.
 *
 * Computed metrics:
 *   srsTotal       — total cards in the SRS deck
 *   srsDue         — cards due today or overdue
 *   srsNew         — cards never reviewed
 *   retentionRate  — % of cards reviewed this week whose last review succeeded
 *   retentionReviewed — # cards reviewed in last 7 days
 *   lastAssessScore   — average disposition score (1–10) from most recent assessment
 *   assessDelta       — delta vs previous assessment, null if only one
 *   chaptersRead      — # chapters with a completedAt record
 *   portfolioThisMonth — # portfolio entries created this calendar month
 *   streak            — consecutive days with at least one SRS review (best-effort,
 *                       derived from lastReviewedAt per-card — accurate when cards
 *                       are spread across the deck, which SM-2 guarantees over time)
 */

import { useEffect, useState } from 'react';
import {
  getSRSProgress,
  getUserSRSCards,
  isDue,
  todayISO,
  type CardProgress,
} from '@/lib/srs';
import { getProgress, getPortfolio } from '@/lib/storage';

const DISPOSITION_TEMPLATE_ID = 'disposition-assessment';

export interface DashboardStats {
  loading: boolean;
  srsTotal: number;
  srsDue: number;
  srsNew: number;
  retentionRate: number | null;   // 0–100, null if no reviews this week
  retentionReviewed: number;
  lastAssessScore: number | null; // 1–10 avg, null if no assessment
  assessDelta: number | null;     // null if only one assessment
  chaptersRead: number;
  portfolioThisMonth: number;
  streak: number;                 // days
}

// ---- Computation helpers ----

function avgNumericValues(responses: Record<string, unknown>): number | null {
  const vals = Object.values(responses).filter(
    (v): v is number => typeof v === 'number',
  );
  if (vals.length === 0) return null;
  const sum = vals.reduce((a, b) => a + b, 0);
  return Math.round((sum / vals.length) * 10) / 10;
}

/** Convert an ISO timestamp to a local YYYY-MM-DD string. */
function isoToLocalDate(iso: string): string {
  const d = new Date(iso);
  return (
    `${d.getFullYear()}-` +
    `${String(d.getMonth() + 1).padStart(2, '0')}-` +
    `${String(d.getDate()).padStart(2, '0')}`
  );
}

/** Add `n` days to a YYYY-MM-DD date string. */
function shiftDate(dateStr: string, n: number): string {
  const d = new Date(`${dateStr}T12:00:00`);
  d.setDate(d.getDate() + n);
  return (
    `${d.getFullYear()}-` +
    `${String(d.getMonth() + 1).padStart(2, '0')}-` +
    `${String(d.getDate()).padStart(2, '0')}`
  );
}

function computeStreak(progressMap: Record<string, CardProgress>): number {
  const dateSet = new Set<string>();
  for (const p of Object.values(progressMap)) {
    if (p.lastReviewedAt) {
      dateSet.add(isoToLocalDate(p.lastReviewedAt));
    }
  }
  if (dateSet.size === 0) return 0;

  const today = todayISO();
  const yesterday = shiftDate(today, -1);

  // Allow streak to be alive if user hasn't reviewed yet today
  let cursor = dateSet.has(today)
    ? today
    : dateSet.has(yesterday)
      ? yesterday
      : null;

  if (!cursor) return 0;

  let count = 0;
  while (dateSet.has(cursor)) {
    count++;
    cursor = shiftDate(cursor, -1);
  }
  return count;
}

function computeRetention(
  progressMap: Record<string, CardProgress>,
): { rate: number | null; reviewed: number } {
  const cutoff = Date.now() - 7 * 24 * 60 * 60 * 1000;
  let reviewed = 0;
  let successful = 0;

  for (const p of Object.values(progressMap)) {
    if (!p.lastReviewedAt) continue;
    if (new Date(p.lastReviewedAt).getTime() < cutoff) continue;
    reviewed++;
    // SM-2: repetitions resets to 0 on failure (quality < 3).
    // So repetitions >= 1 means the most recent review was a pass.
    if (p.repetitions >= 1) successful++;
  }

  if (reviewed === 0) return { rate: null, reviewed: 0 };
  return {
    rate: Math.round((successful / reviewed) * 100),
    reviewed,
  };
}

// ---- Hook ----

const INITIAL: DashboardStats = {
  loading: true,
  srsTotal: 0,
  srsDue: 0,
  srsNew: 0,
  retentionRate: null,
  retentionReviewed: 0,
  lastAssessScore: null,
  assessDelta: null,
  chaptersRead: 0,
  portfolioThisMonth: 0,
  streak: 0,
};

export function useDashboardStats(): DashboardStats {
  const [stats, setStats] = useState<DashboardStats>(INITIAL);

  useEffect(() => {
    // ---- Synchronous localStorage reads ----
    const srsProgress = getSRSProgress();
    const chapterProgress = getProgress();
    const portfolio = getPortfolio();

    // Assess scores
    const assessHistory = portfolio
      .filter((e) => e.templateId === DISPOSITION_TEMPLATE_ID)
      .sort(
        (a, b) =>
          new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime(),
      );
    const lastAssessScore = assessHistory[0]
      ? avgNumericValues(
          assessHistory[0].responses as Record<string, unknown>,
        )
      : null;
    const prevAssessScore = assessHistory[1]
      ? avgNumericValues(
          assessHistory[1].responses as Record<string, unknown>,
        )
      : null;
    const assessDelta =
      lastAssessScore !== null && prevAssessScore !== null
        ? Math.round((lastAssessScore - prevAssessScore) * 10) / 10
        : null;

    // Portfolio this month
    const nowDate = new Date();
    const thisYearMonth = `${nowDate.getFullYear()}-${String(
      nowDate.getMonth() + 1,
    ).padStart(2, '0')}`;
    const portfolioThisMonth = portfolio.filter((e) =>
      e.createdAt.startsWith(thisYearMonth),
    ).length;

    const { rate: retentionRate, reviewed: retentionReviewed } =
      computeRetention(srsProgress);
    const streak = computeStreak(srsProgress);
    const chaptersRead = Object.keys(chapterProgress).length;

    // ---- Async: fetch SRS deck to count total / due / new ----
    async function loadSRSDeck() {
      try {
        const [mmRes, dwRes, flRes] = await Promise.all([
          fetch('/data/frameworks/mental-models.json'),
          fetch('/data/frameworks/dewey-five-phases.json'),
          fetch('/data/frameworks/logical-fallacies.json'),
        ]);
        const [mmData, dwData, flData] = (await Promise.all([
          mmRes.json(),
          dwRes.json(),
          flRes.json(),
        ])) as [
          { models: { id: string }[] },
          { phases: { number: number }[] },
          { fallacies: { id: string }[] },
        ];

        const today = todayISO();
        let due = 0;
        let newCount = 0;

        const userSrsCards = getUserSRSCards();
        const allIds: string[] = [
          ...(mmData.models ?? []).map((m) => m.id),
          ...(dwData.phases ?? []).map((p) => `dewey-phase-${p.number}`),
          ...(flData.fallacies ?? []).map((f) => f.id),
          ...userSrsCards.map((c) => c.id),
        ];

        for (const id of allIds) {
          const p = srsProgress[id];
          if (!p) {
            newCount++;
          } else if (p.dueDate <= today) {
            due++;
          }
        }

        setStats({
          loading: false,
          srsTotal: allIds.length,
          srsDue: due,
          srsNew: newCount,
          retentionRate,
          retentionReviewed,
          lastAssessScore,
          assessDelta,
          chaptersRead,
          portfolioThisMonth,
          streak,
        });
      } catch {
        // Graceful fallback using only progress records
        const userSrsCards = getUserSRSCards();
        const srsDue = Object.values(srsProgress).filter(isDue).length;
        setStats({
          loading: false,
          srsTotal: userSrsCards.length,
          srsDue,
          srsNew: 0,
          retentionRate,
          retentionReviewed,
          lastAssessScore,
          assessDelta,
          chaptersRead,
          portfolioThisMonth,
          streak,
        });
      }
    }

    void loadSRSDeck();
  }, []);

  return stats;
}
