'use client';

import Link from 'next/link';
import { useDashboardStats } from '@/lib/dashboard';

// ---- Helpers ----

function pct(n: number): string {
  return `${n}%`;
}

function scoreBg(score: number): string {
  if (score <= 3) return 'bg-red-500';
  if (score <= 6) return 'bg-amber-500';
  return 'bg-emerald-500';
}

function streakMessage(days: number): string {
  if (days === 0) return 'Start your streak today';
  if (days === 1) return 'Good start — come back tomorrow';
  if (days < 5) return 'Building momentum';
  if (days < 14) return 'Consistent practice';
  if (days < 30) return 'Strong habit forming';
  return 'Exceptional dedication';
}

// ---- Skeleton ----

function Skeleton({ className }: { className?: string }) {
  return (
    <div
      className={`animate-pulse rounded bg-slate-100 ${className ?? ''}`}
    />
  );
}

// ---- Stat card shells ----

interface StatCardProps {
  label: string;
  children: React.ReactNode;
  href?: string;
  hrefLabel?: string;
  accent?: string; // Tailwind border-l color e.g. 'border-indigo-400'
}

function StatCard({ label, children, href, hrefLabel, accent = 'border-slate-300' }: StatCardProps) {
  return (
    <div
      className={`flex flex-col gap-3 rounded-xl border border-slate-200 bg-white p-5 shadow-sm border-l-4 ${accent}`}
    >
      <p className="text-xs font-semibold uppercase tracking-wider text-slate-400">
        {label}
      </p>
      <div className="flex-1">{children}</div>
      {href && (
        <Link
          href={href}
          className="mt-auto text-xs font-medium text-indigo-600 hover:text-indigo-800 transition"
        >
          {hrefLabel ?? 'View →'}
        </Link>
      )}
    </div>
  );
}

// ---- Individual cards ----

function SRSCard({
  loading,
  srsDue,
  srsNew,
  srsTotal,
}: {
  loading: boolean;
  srsDue: number;
  srsNew: number;
  srsTotal: number;
}) {
  const reviewed = srsTotal - srsNew;
  const progressPct = srsTotal > 0 ? Math.round((reviewed / srsTotal) * 100) : 0;

  return (
    <StatCard
      label="SRS Review"
      href="/review"
      hrefLabel={srsDue + srsNew > 0 ? 'Start session →' : 'Review deck →'}
      accent="border-indigo-400"
    >
      {loading ? (
        <Skeleton className="h-8 w-24 mb-2" />
      ) : (
        <>
          <p className="text-3xl font-bold tabular-nums text-slate-900">
            {srsDue + srsNew}
            <span className="ml-1.5 text-base font-normal text-slate-400">due</span>
          </p>
          <p className="mt-1 text-xs text-slate-500">
            {srsDue > 0 && <span className="text-indigo-600 font-medium">{srsDue} review{srsDue !== 1 ? 's' : ''}</span>}
            {srsDue > 0 && srsNew > 0 && ' · '}
            {srsNew > 0 && <span className="text-violet-600 font-medium">{srsNew} new</span>}
            {srsDue === 0 && srsNew === 0 && (
              <span className="text-emerald-600 font-medium">All caught up ✓</span>
            )}
          </p>
          {srsTotal > 0 && (
            <div className="mt-3">
              <div className="flex justify-between text-[10px] text-slate-400 mb-1">
                <span>Deck progress</span>
                <span>{progressPct}% reviewed</span>
              </div>
              <div className="h-1.5 w-full overflow-hidden rounded-full bg-slate-100">
                <div
                  className="h-full rounded-full bg-indigo-400 transition-all duration-700"
                  style={{ width: pct(progressPct) }}
                />
              </div>
            </div>
          )}
        </>
      )}
    </StatCard>
  );
}

function RetentionCard({
  loading,
  retentionRate,
  retentionReviewed,
}: {
  loading: boolean;
  retentionRate: number | null;
  retentionReviewed: number;
}) {
  return (
    <StatCard label="Retention (7 days)" href="/review" hrefLabel="Review →" accent="border-emerald-400">
      {loading ? (
        <Skeleton className="h-8 w-20 mb-2" />
      ) : retentionRate === null ? (
        <div>
          <p className="text-2xl font-bold text-slate-300">—</p>
          <p className="mt-1 text-xs text-slate-400">No reviews this week</p>
        </div>
      ) : (
        <>
          <p className="text-3xl font-bold tabular-nums text-slate-900">
            {retentionRate}
            <span className="ml-0.5 text-base font-normal text-slate-400">%</span>
          </p>
          <p className="mt-1 text-xs text-slate-500">
            {retentionReviewed} card{retentionReviewed !== 1 ? 's' : ''} reviewed
          </p>
          <div className="mt-3 h-1.5 w-full overflow-hidden rounded-full bg-slate-100">
            <div
              className={`h-full rounded-full transition-all duration-700 ${
                retentionRate >= 80
                  ? 'bg-emerald-400'
                  : retentionRate >= 60
                    ? 'bg-amber-400'
                    : 'bg-red-400'
              }`}
              style={{ width: pct(retentionRate) }}
            />
          </div>
        </>
      )}
    </StatCard>
  );
}

function AssessCard({
  loading,
  lastAssessScore,
  assessDelta,
}: {
  loading: boolean;
  lastAssessScore: number | null;
  assessDelta: number | null;
}) {
  return (
    <StatCard label="Last Assessment" href="/assess" hrefLabel="Assess again →" accent="border-amber-400">
      {loading ? (
        <Skeleton className="h-8 w-24 mb-2" />
      ) : lastAssessScore === null ? (
        <div>
          <p className="text-2xl font-bold text-slate-300">—</p>
          <p className="mt-1 text-xs text-slate-400">No assessment yet</p>
          <Link
            href="/assess"
            className="mt-2 inline-block text-xs font-medium text-amber-600 hover:text-amber-800"
          >
            Take your first assessment →
          </Link>
        </div>
      ) : (
        <>
          <div className="flex items-baseline gap-2">
            <p className="text-3xl font-bold tabular-nums text-slate-900">
              {lastAssessScore}
              <span className="ml-0.5 text-base font-normal text-slate-400">/10</span>
            </p>
            {assessDelta !== null && assessDelta !== 0 && (
              <span
                className={`text-sm font-semibold ${
                  assessDelta > 0 ? 'text-emerald-600' : 'text-red-500'
                }`}
              >
                {assessDelta > 0 ? `▲ ${assessDelta}` : `▼ ${Math.abs(assessDelta)}`}
              </span>
            )}
            {assessDelta === 0 && (
              <span className="text-xs text-slate-400">no change</span>
            )}
          </div>
          <div className="mt-3 h-1.5 w-full overflow-hidden rounded-full bg-slate-100">
            <div
              className={`h-full rounded-full transition-all duration-700 ${scoreBg(lastAssessScore)}`}
              style={{ width: pct((lastAssessScore / 10) * 100) }}
            />
          </div>
          <p className="mt-1.5 text-[10px] text-slate-400">
            Paul-Elder disposition scale
          </p>
        </>
      )}
    </StatCard>
  );
}

function ChaptersCard({
  loading,
  chaptersRead,
}: {
  loading: boolean;
  chaptersRead: number;
}) {
  const total = 19;
  const progressPct = Math.round((chaptersRead / total) * 100);

  return (
    <StatCard label="Chapters Read" href="/chapters" hrefLabel="Continue reading →" accent="border-violet-400">
      {loading ? (
        <Skeleton className="h-8 w-20 mb-2" />
      ) : (
        <>
          <p className="text-3xl font-bold tabular-nums text-slate-900">
            {chaptersRead}
            <span className="ml-1 text-base font-normal text-slate-400">/ {total}</span>
          </p>
          <div className="mt-3 h-1.5 w-full overflow-hidden rounded-full bg-slate-100">
            <div
              className="h-full rounded-full bg-violet-400 transition-all duration-700"
              style={{ width: pct(progressPct) }}
            />
          </div>
          <p className="mt-1.5 text-[10px] text-slate-400">
            {progressPct}% of Dewey&apos;s curriculum complete
          </p>
        </>
      )}
    </StatCard>
  );
}

function PortfolioCard({
  loading,
  portfolioThisMonth,
}: {
  loading: boolean;
  portfolioThisMonth: number;
}) {
  const month = new Date().toLocaleString('default', { month: 'long' });

  return (
    <StatCard label="Portfolio" href="/portfolio" hrefLabel="View portfolio →" accent="border-rose-400">
      {loading ? (
        <Skeleton className="h-8 w-16 mb-2" />
      ) : (
        <>
          <p className="text-3xl font-bold tabular-nums text-slate-900">
            {portfolioThisMonth}
            <span className="ml-1.5 text-base font-normal text-slate-400">
              this {month}
            </span>
          </p>
          <p className="mt-1 text-xs text-slate-500">
            {portfolioThisMonth === 0
              ? 'No entries yet — complete a template or practice problem'
              : portfolioThisMonth === 1
                ? '1 entry saved'
                : `${portfolioThisMonth} entries saved`}
          </p>
        </>
      )}
    </StatCard>
  );
}

function StreakCard({
  loading,
  streak,
}: {
  loading: boolean;
  streak: number;
}) {
  return (
    <StatCard label="Study Streak" href="/review" hrefLabel="Keep it going →" accent="border-orange-400">
      {loading ? (
        <Skeleton className="h-8 w-16 mb-2" />
      ) : (
        <>
          <div className="flex items-center gap-2">
            <span className="text-2xl" aria-hidden="true">
              {streak === 0 ? '💤' : streak >= 14 ? '🔥🔥' : '🔥'}
            </span>
            <p className="text-3xl font-bold tabular-nums text-slate-900">
              {streak}
              <span className="ml-1 text-base font-normal text-slate-400">
                day{streak !== 1 ? 's' : ''}
              </span>
            </p>
          </div>
          <p className="mt-1 text-xs text-slate-500">{streakMessage(streak)}</p>
        </>
      )}
    </StatCard>
  );
}

// ---- Quick-links strip ----

const QUICK_LINKS = [
  { href: '/review', label: '🃏 Review cards' },
  { href: '/practice/problems', label: '📝 Practice problems' },
  { href: '/ask', label: '💬 Ask the tutor' },
  { href: '/assess', label: '📊 Self-assess' },
  { href: '/argument-map', label: '🗺 Argument map' },
  { href: '/portfolio', label: '📁 Portfolio' },
];

// ---- Page ----

export default function DashboardPage() {
  const stats = useDashboardStats();

  return (
    <div className="mx-auto max-w-5xl space-y-10">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-bold text-slate-900">Your Progress</h1>
        <p className="mt-1 text-sm text-slate-500">
          Everything in one place — SRS queue, retention, assessment, reading, and study habit.
        </p>
      </div>

      {/* Stat grid */}
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <SRSCard
          loading={stats.loading}
          srsDue={stats.srsDue}
          srsNew={stats.srsNew}
          srsTotal={stats.srsTotal}
        />
        <RetentionCard
          loading={stats.loading}
          retentionRate={stats.retentionRate}
          retentionReviewed={stats.retentionReviewed}
        />
        <AssessCard
          loading={stats.loading}
          lastAssessScore={stats.lastAssessScore}
          assessDelta={stats.assessDelta}
        />
        <ChaptersCard loading={stats.loading} chaptersRead={stats.chaptersRead} />
        <PortfolioCard
          loading={stats.loading}
          portfolioThisMonth={stats.portfolioThisMonth}
        />
        <StreakCard loading={stats.loading} streak={stats.streak} />
      </div>

      {/* Quick links */}
      <div>
        <p className="mb-3 text-xs font-semibold uppercase tracking-wider text-slate-400">
          Quick access
        </p>
        <div className="flex flex-wrap gap-2">
          {QUICK_LINKS.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="rounded-lg border border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-700 shadow-sm transition hover:border-slate-300 hover:bg-slate-50"
            >
              {link.label}
            </Link>
          ))}
        </div>
      </div>

      {/* Footer note */}
      <p className="text-[11px] text-slate-300 text-center">
        All data is stored locally in your browser. Streak is computed from your most recent card
        reviews — accuracy improves as your deck matures.
      </p>
    </div>
  );
}
