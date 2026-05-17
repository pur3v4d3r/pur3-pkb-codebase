'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import {
  getSRSProgress,
  isDue,
  todayISO,
  type SRSCard,
  type CardProgress,
} from '@/lib/srs';

// ---- Raw JSON types (same minimal subset as review page) ----

interface RawModel { id: string; name: string; category: string; }
interface RawPhase { number: number; name: string; }
interface RawFallacy { id: string; name: string; category: string; }
interface RawMentalModelsData { models: RawModel[]; }
interface RawDeweyData { phases: RawPhase[]; }
interface RawFallaciesData { fallacies: RawFallacy[]; }

function buildCards(mm: RawMentalModelsData, dw: RawDeweyData, fl: RawFallaciesData): SRSCard[] {
  return [
    ...mm.models.map((m) => ({
      id: m.id, source: 'mental-model' as const,
      category: m.category, front: m.name, back: '',
    })),
    ...dw.phases.map((p) => ({
      id: `dewey-phase-${p.number}`, source: 'dewey-phase' as const,
      category: "Dewey's Five Phases", front: `Phase ${p.number}: ${p.name}`, back: '',
    })),
    ...fl.fallacies.map((f) => ({
      id: f.id, source: 'fallacy' as const,
      category: f.category, front: f.name, back: '',
    })),
  ];
}

// ---- Date helpers ----

function addDaysToISO(dateStr: string, days: number): string {
  const d = new Date(`${dateStr}T12:00:00`);
  d.setDate(d.getDate() + days);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
}

function formatDate(iso: string): string {
  const [y, m, d] = iso.split('-').map(Number);
  const dt = new Date(y, m - 1, d);
  return dt.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
}

// ---- Stats computation ----

interface SourceStats {
  source: string;
  label: string;
  total: number;
  reviewed: number;
  dueTodayOrOverdue: number;
  struggling: number;  // EF < 1.8
}

interface StatsResult {
  total: number;
  reviewed: number;
  newCards: number;           // never reviewed
  dueTodayOrOverdue: number;
  upcomingWeek: number;       // due in the next 7 days (not today)
  struggling: number;         // EF < 1.8 (low ease = hard cards)
  strongCards: number;        // interval >= 21 days
  bySource: SourceStats[];
  dueDateBuckets: { date: string; count: number }[];  // next 14 days
}

const SOURCE_LABEL: Record<string, string> = {
  'mental-model': 'Mental Models',
  'dewey-phase': 'Dewey Phases',
  fallacy: 'Fallacies',
};

function computeStats(cards: SRSCard[], progress: Record<string, CardProgress>): StatsResult {
  const today = todayISO();
  const in7 = addDaysToISO(today, 7);
  const in14 = addDaysToISO(today, 14);

  let reviewed = 0, dueTodayOrOverdue = 0, upcomingWeek = 0, struggling = 0, strongCards = 0;

  for (const card of cards) {
    const p = progress[card.id];
    if (!p) continue;
    reviewed++;
    if (p.dueDate <= today) dueTodayOrOverdue++;
    else if (p.dueDate <= in7) upcomingWeek++;
    if (p.efactor < 1.8) struggling++;
    if (p.interval >= 21) strongCards++;
  }

  // By source
  const sources = ['mental-model', 'dewey-phase', 'fallacy'];
  const bySource: SourceStats[] = sources.map((src) => {
    const subset = cards.filter((c) => c.source === src);
    const rev = subset.filter((c) => progress[c.id]);
    const due = subset.filter((c) => {
      const p = progress[c.id];
      return p ? p.dueDate <= today : false;
    });
    const str = subset.filter((c) => {
      const p = progress[c.id];
      return p ? p.efactor < 1.8 : false;
    });
    return {
      source: src,
      label: SOURCE_LABEL[src] ?? src,
      total: subset.length,
      reviewed: rev.length,
      dueTodayOrOverdue: due.length,
      struggling: str.length,
    };
  });

  // Due-date distribution (next 14 days)
  const dueDateBuckets: { date: string; count: number }[] = [];
  for (let i = 0; i <= 13; i++) {
    const d = addDaysToISO(today, i);
    if (d > in14) break;
    const count = cards.filter((c) => progress[c.id]?.dueDate === d).length;
    dueDateBuckets.push({ date: d, count });
  }

  return {
    total: cards.length,
    reviewed,
    newCards: cards.length - reviewed,
    dueTodayOrOverdue,
    upcomingWeek,
    struggling,
    strongCards,
    bySource,
    dueDateBuckets,
  };
}

// ---- Component ----

export default function ReviewStatsPage() {
  const [stats, setStats] = useState<StatsResult | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function load() {
      try {
        const [mmRes, dwRes, flRes] = await Promise.all([
          fetch('/data/frameworks/mental-models.json'),
          fetch('/data/frameworks/dewey-five-phases.json'),
          fetch('/data/frameworks/logical-fallacies.json'),
        ]);
        if (!mmRes.ok || !dwRes.ok || !flRes.ok) throw new Error('Failed to fetch card data.');
        const [mmData, dwData, flData] = await Promise.all([
          mmRes.json() as Promise<RawMentalModelsData>,
          dwRes.json() as Promise<RawDeweyData>,
          flRes.json() as Promise<RawFallaciesData>,
        ]);
        const cards = buildCards(mmData, dwData, flData);
        const progress = getSRSProgress();
        setStats(computeStats(cards, progress));
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
      } finally {
        setLoading(false);
      }
    }
    void load();
  }, []);

  if (loading) {
    return <div className="flex items-center justify-center py-32 text-sm text-slate-400">Loading…</div>;
  }
  if (error || !stats) {
    return (
      <div className="mx-auto max-w-md py-24 text-center">
        <p className="font-semibold text-red-600">Failed to load stats</p>
        <p className="mt-1 text-sm text-slate-500">{error}</p>
      </div>
    );
  }

  const maxBucket = Math.max(...stats.dueDateBuckets.map((b) => b.count), 1);

  return (
    <div className="mx-auto max-w-2xl space-y-8 pb-16">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Review Stats</h1>
          <p className="mt-1 text-sm text-slate-500">Your SRS progress across all card sets</p>
        </div>
        <Link
          href="/review"
          className="rounded-lg bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm transition hover:bg-indigo-700"
        >
          Start review →
        </Link>
      </div>

      {/* Summary cards */}
      <div className="grid grid-cols-2 gap-4 sm:grid-cols-4">
        {[
          { label: 'Total cards', value: stats.total, className: 'text-slate-800' },
          { label: 'Reviewed', value: stats.reviewed, className: 'text-indigo-700' },
          { label: 'Due today', value: stats.dueTodayOrOverdue, className: stats.dueTodayOrOverdue > 0 ? 'text-amber-600' : 'text-green-600' },
          { label: 'Not started', value: stats.newCards, className: 'text-slate-500' },
        ].map(({ label, value, className }) => (
          <div key={label} className="rounded-xl border border-slate-200 bg-white p-4 text-center shadow-sm">
            <p className={`text-3xl font-bold ${className}`}>{value}</p>
            <p className="mt-1 text-xs text-slate-500">{label}</p>
          </div>
        ))}
      </div>

      {/* Retention indicators */}
      <div className="grid grid-cols-2 gap-4">
        <div className="rounded-xl border border-green-200 bg-green-50 p-4">
          <p className="text-2xl font-bold text-green-700">{stats.strongCards}</p>
          <p className="mt-1 text-sm font-medium text-green-800">Strong cards</p>
          <p className="text-xs text-green-600">interval ≥ 21 days — well retained</p>
        </div>
        <div className="rounded-xl border border-red-200 bg-red-50 p-4">
          <p className="text-2xl font-bold text-red-700">{stats.struggling}</p>
          <p className="mt-1 text-sm font-medium text-red-800">Struggling cards</p>
          <p className="text-xs text-red-600">ease factor &lt; 1.8 — needs extra review</p>
        </div>
      </div>

      {/* Due-date distribution chart */}
      <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
        <h2 className="mb-4 text-sm font-semibold text-slate-800">Due dates — next 14 days</h2>
        <div className="flex items-end gap-1" style={{ height: '6rem' }}>
          {stats.dueDateBuckets.map(({ date, count }) => {
            const today = todayISO();
            const heightPct = count === 0 ? 2 : Math.round((count / maxBucket) * 100);
            const isToday = date === today;
            return (
              <div key={date} className="group relative flex flex-1 flex-col items-center justify-end gap-1">
                {/* Bar */}
                <div
                  className={`w-full rounded-t transition-all ${isToday ? 'bg-amber-400' : 'bg-indigo-200'}`}
                  style={{ height: `${heightPct}%` }}
                />
                {/* Tooltip */}
                {count > 0 && (
                  <div className="pointer-events-none absolute bottom-full mb-1 hidden rounded bg-slate-800 px-1.5 py-0.5 text-xs text-white group-hover:block whitespace-nowrap">
                    {formatDate(date)}: {count}
                  </div>
                )}
              </div>
            );
          })}
        </div>
        {/* X-axis labels */}
        <div className="mt-1 flex gap-1 text-[10px] text-slate-400">
          {stats.dueDateBuckets.map(({ date }, i) => (
            <div key={date} className="flex-1 truncate text-center">
              {i === 0 ? 'Today' : i % 3 === 0 ? formatDate(date).split(',')[0] : ''}
            </div>
          ))}
        </div>
      </div>

      {/* Per-source breakdown */}
      <div className="space-y-2">
        <h2 className="text-sm font-semibold text-slate-800">By card set</h2>
        {stats.bySource.map((src) => {
          const pct = src.total > 0 ? Math.round((src.reviewed / src.total) * 100) : 0;
          return (
            <div key={src.source} className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
              <div className="flex items-center justify-between">
                <p className="text-sm font-semibold text-slate-800">{src.label}</p>
                <div className="flex items-center gap-3 text-xs text-slate-500">
                  {src.dueTodayOrOverdue > 0 && (
                    <span className="font-medium text-amber-600">{src.dueTodayOrOverdue} due</span>
                  )}
                  {src.struggling > 0 && (
                    <span className="text-red-500">{src.struggling} struggling</span>
                  )}
                  <span>{src.reviewed}/{src.total}</span>
                </div>
              </div>
              {/* Progress bar */}
              <div className="mt-2 h-1.5 w-full overflow-hidden rounded-full bg-slate-100">
                <div
                  className="h-full rounded-full bg-indigo-500 transition-all"
                  style={{ width: `${pct}%` }}
                />
              </div>
              <p className="mt-1 text-xs text-slate-400">{pct}% reviewed</p>
            </div>
          );
        })}
      </div>

      {/* Upcoming */}
      {stats.upcomingWeek > 0 && (
        <p className="text-center text-sm text-slate-500">
          <span className="font-semibold text-slate-700">{stats.upcomingWeek}</span> more cards due in the next 7 days
        </p>
      )}
    </div>
  );
}
