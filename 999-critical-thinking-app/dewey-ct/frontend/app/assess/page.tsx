'use client';

import { useEffect, useMemo, useState } from 'react';
import Link from 'next/link';
import { getPortfolio, savePortfolioEntry, generateId } from '@/lib/storage';
import type { PortfolioEntry } from '@/types/framework';

// ---- Types ----

interface DispositionItem {
  id: string;
  framework: 'ennis' | 'delphi';
  cluster: string;
  label: string;
}

interface DispositionCluster {
  cluster: string;
  items: DispositionItem[];
}

interface FrameworkSection {
  key: 'ennis' | 'delphi';
  title: string;
  description: string;
  clusters: DispositionCluster[];
}

// ---- Raw JSON shape (minimal — only fields we need) ----

interface RawCluster {
  cluster: string;
  dispositions: string[];
}

interface RawSynthesisData {
  ennis_14_dispositions: {
    description: string;
    clusters: RawCluster[];
  };
  delphi_disposition_profile: {
    description: string;
    clusters: RawCluster[];
  };
}

// ---- Utilities ----

const TEMPLATE_ID = 'disposition-assessment';

/**
 * Stable, human-readable key from disposition text.
 * Uses underscores so the portfolio detail fallback renders it as plain words.
 * E.g. "Seek and offer reasons" → "ennis_seek_and_offer_reasons"
 */
function slugify(text: string, prefix: string): string {
  return (
    prefix +
    '_' +
    text
      .toLowerCase()
      .replace(/[^a-z0-9\s]/g, '')
      .trim()
      .split(/\s+/)
      .join('_')
  );
}

function buildSections(data: RawSynthesisData): FrameworkSection[] {
  function build(
    key: 'ennis' | 'delphi',
    title: string,
    description: string,
    rawClusters: RawCluster[],
  ): FrameworkSection {
    return {
      key,
      title,
      description,
      clusters: rawClusters.map((rc) => ({
        cluster: rc.cluster,
        items: rc.dispositions.map((label) => ({
          id: slugify(label, key),
          framework: key,
          cluster: rc.cluster,
          label,
        })),
      })),
    };
  }
  return [
    build(
      'ennis',
      "Ennis's Critical Thinking Dispositions",
      data.ennis_14_dispositions.description,
      data.ennis_14_dispositions.clusters,
    ),
    build(
      'delphi',
      'Delphi Disposition Profile',
      data.delphi_disposition_profile.description,
      data.delphi_disposition_profile.clusters,
    ),
  ];
}

function scoreColor(v: number): string {
  if (v <= 3) return 'text-red-600';
  if (v <= 6) return 'text-amber-500';
  return 'text-green-600';
}

function scoreBg(v: number): string {
  if (v <= 3) return 'bg-red-400';
  if (v <= 6) return 'bg-amber-400';
  return 'bg-green-500';
}

function average(values: number[]): number {
  if (values.length === 0) return 0;
  const sum = values.reduce((a, b) => a + b, 0);
  return Math.round((sum / values.length) * 10) / 10;
}

function loadPreviousAssessment(): PortfolioEntry | null {
  const portfolio = getPortfolio();
  const sorted = portfolio
    .filter((e) => e.templateId === TEMPLATE_ID)
    .sort(
      (a, b) =>
        new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime(),
    );
  return sorted[0] ?? null;
}

// ---- Sub-components ----

interface DispositionRowProps {
  label: string;
  value: number;
  delta: number | null;
  showDeltaCol: boolean;
  onChange: (v: number) => void;
}

function DispositionRow({
  label,
  value,
  delta,
  showDeltaCol,
  onChange,
}: DispositionRowProps) {
  return (
    <div className="flex items-center gap-3 rounded-lg px-3 py-2.5 transition hover:bg-slate-50">
      <p className="flex-1 text-sm leading-snug text-slate-700">{label}</p>

      <div className="flex shrink-0 items-center gap-3">
        {/* Scale labels */}
        <span className="hidden text-[10px] text-slate-400 sm:block">1</span>

        {/* Slider */}
        <input
          type="range"
          min={1}
          max={10}
          step={1}
          value={value}
          onChange={(e) => onChange(Number(e.target.value))}
          className="w-28 cursor-pointer accent-slate-700 sm:w-36"
          aria-label={label}
        />

        <span className="hidden text-[10px] text-slate-400 sm:block">10</span>

        {/* Value badge */}
        <span
          className={`w-6 text-center text-sm font-bold tabular-nums ${scoreColor(value)}`}
        >
          {value}
        </span>

        {/* Delta column — always rendered to keep alignment */}
        <span
          className={`w-7 text-right text-[11px] font-semibold tabular-nums ${
            showDeltaCol
              ? delta === null || delta === 0
                ? 'text-slate-300'
                : delta > 0
                  ? 'text-green-600'
                  : 'text-red-500'
              : 'invisible'
          }`}
        >
          {showDeltaCol
            ? delta === null || delta === 0
              ? '—'
              : delta > 0
                ? `▲${delta}`
                : `▼${Math.abs(delta)}`
            : '—'}
        </span>
      </div>
    </div>
  );
}

// ---- Recommendations engine ----

interface DispRec {
  chapters: { num: number }[];
  templateId?: string;
  templateName?: string;
  fallacyDrill?: boolean;
}

const DISP_RECS: { keywords: string[]; rec: DispRec }[] = [
  {
    keywords: ['reason', 'evidence', 'source', 'credible', 'information', 'well-informed'],
    rec: { chapters: [{ num: 11 }, { num: 5 }], templateId: 'argument-analysis-v1', templateName: 'Argument Analysis', fallacyDrill: true },
  },
  {
    keywords: ['open', 'fair', 'alternative', 'position', 'change'],
    rec: { chapters: [{ num: 2 }, { num: 4 }], templateId: 'socratic-questioning-v1', templateName: 'Socratic Questioning' },
  },
  {
    keywords: ['clear', 'precise', 'definition', 'thesis', 'statement', 'question'],
    rec: { chapters: [{ num: 10 }, { num: 9 }], templateId: 'see-i-elaboration-v1', templateName: 'SEE-I Elaboration' },
  },
  {
    keywords: ['systematic', 'orderly', 'complex', 'whole', 'relevant', 'main point'],
    rec: { chapters: [{ num: 7 }], templateId: 'dewey-reflective-v1', templateName: 'Dewey Reflective' },
  },
  {
    keywords: ['sensitiv', 'sophistication', 'feeling'],
    rec: { chapters: [{ num: 2 }], templateId: 'socratic-questioning-v1', templateName: 'Socratic Questioning' },
  },
  {
    keywords: ['confidence', 'trust', 'self', 'mature'],
    rec: { chapters: [{ num: 1 }], templateId: 'metacognitive-reflection-v1', templateName: 'Metacognitive Reflection' },
  },
  {
    keywords: ['inquisit', 'curious', 'inquir', 'aware'],
    rec: { chapters: [{ num: 3 }, { num: 1 }], templateId: 'paul-elder-analysis-v1', templateName: 'Paul-Elder Analysis' },
  },
  {
    keywords: ['analyt', 'interpret', 'inference', 'conclusion', 'truth-seek', 'truth seek'],
    rec: { chapters: [{ num: 5 }, { num: 12 }], templateId: 'argument-analysis-v1', templateName: 'Argument Analysis', fallacyDrill: true },
  },
];

function getRecForDisposition(label: string): DispRec {
  const lower = label.toLowerCase();
  for (const { keywords, rec } of DISP_RECS) {
    if (keywords.some((kw) => lower.includes(kw))) return rec;
  }
  // Default fallback
  return { chapters: [{ num: 7 }], templateId: 'paul-elder-analysis-v1', templateName: 'Paul-Elder Analysis' };
}

interface AssessRecItem {
  id: string;
  label: string;
  value: number;
}

function AssessRecommendations({ bottomItems }: { bottomItems: AssessRecItem[] }) {
  const recs = bottomItems.map((item) => ({
    item,
    rec: getRecForDisposition(item.label),
  }));

  return (
    <div className="rounded-xl border border-amber-200 bg-amber-50 p-5">
      <h3 className="mb-1 font-semibold text-amber-900">Recommended next steps</h3>
      <p className="mb-4 text-xs text-amber-700">
        Based on your lowest-rated dispositions — pick one to work on first.
      </p>
      <div className="space-y-4">
        {recs.map(({ item, rec }) => (
          <div key={item.id} className="rounded-lg border border-amber-100 bg-white p-4 shadow-sm">
            <p className="mb-2 text-xs font-semibold text-slate-700">
              <span className="mr-1.5 rounded-full bg-red-100 px-1.5 py-0.5 text-xs font-bold text-red-700">
                {item.value}
              </span>
              {item.label}
            </p>
            <div className="flex flex-wrap gap-2">
              {rec.chapters.slice(0, 2).map(({ num }) => (
                <a
                  key={num}
                  href={`/chapter/${num}`}
                  className="rounded-md border border-indigo-200 bg-indigo-50 px-2.5 py-1 text-xs font-medium text-indigo-700 transition hover:bg-indigo-100"
                >
                  📖 Ch. {num}
                </a>
              ))}
              {rec.templateId && (
                <a
                  href={`/templates/${rec.templateId}`}
                  className="rounded-md border border-violet-200 bg-violet-50 px-2.5 py-1 text-xs font-medium text-violet-700 transition hover:bg-violet-100"
                >
                  📝 {rec.templateName}
                </a>
              )}
              {rec.fallacyDrill && (
                <a
                  href="/review"
                  className="rounded-md border border-amber-200 bg-amber-50 px-2.5 py-1 text-xs font-medium text-amber-700 transition hover:bg-amber-100"
                >
                  🃏 Drill fallacies
                </a>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

// ---- Cluster Breakdown (#14) ----

function ClusterBreakdown({
  sections,
  ratings,
}: {
  sections: FrameworkSection[];
  ratings: Record<string, number>;
}) {
  return (
    <div className="mt-6 space-y-5 border-t border-slate-100 pt-6">
      <p className="text-[10px] font-semibold uppercase tracking-widest text-slate-500">
        Cluster Breakdown
      </p>
      {sections.map((section) => (
        <div key={section.key}>
          <p className="mb-2.5 text-[11px] font-semibold text-slate-700">
            {section.title}
          </p>
          <div className="space-y-2">
            {section.clusters.map((cluster) => {
              const avg = average(
                cluster.items.map((i) => ratings[i.id] ?? 5),
              );
              return (
                <div key={cluster.cluster} className="flex items-center gap-3">
                  <span
                    className="w-48 shrink-0 truncate text-[11px] text-slate-600"
                    title={cluster.cluster}
                  >
                    {cluster.cluster}
                  </span>
                  <div className="flex-1 overflow-hidden rounded-full bg-slate-100 h-2">
                    <div
                      className={`h-full rounded-full transition-all duration-700 ${scoreBg(avg)}`}
                      style={{ width: `${((avg - 1) / 9) * 100}%` }}
                    />
                  </div>
                  <span
                    className={`w-7 shrink-0 text-right text-xs font-bold tabular-nums ${scoreColor(avg)}`}
                  >
                    {avg}
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      ))}
    </div>
  );
}

// ---- Sparkline + TrendRow (#15) ----

function Sparkline({
  values,
  width = 80,
  height = 24,
}: {
  values: number[];
  width?: number;
  height?: number;
}) {
  if (values.length < 2) return null;
  const min = Math.min(...values);
  const max = Math.max(...values);
  const range = max - min || 1;
  const pts = values
    .map((v, i) => {
      const x = (i / (values.length - 1)) * (width - 4) + 2;
      const y = height - 2 - ((v - min) / range) * (height - 4);
      return `${x},${y}`;
    })
    .join(' ');
  const lastVal = values[values.length - 1];
  const lx = width - 2;
  const ly = height - 2 - ((lastVal - min) / range) * (height - 4);
  return (
    <svg
      width={width}
      height={height}
      viewBox={`0 0 ${width} ${height}`}
      className="overflow-visible"
      aria-hidden="true"
    >
      <polyline
        points={pts}
        fill="none"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinejoin="round"
        strokeLinecap="round"
      />
      <circle cx={lx} cy={ly} r={2.5} fill="currentColor" />
    </svg>
  );
}

function TrendRow({
  label,
  values,
}: {
  label: string;
  values: number[];
}) {
  const latest = values[values.length - 1];
  const first = values[0];
  const delta = Math.round((latest - first) * 10) / 10;
  return (
    <div className="flex items-center gap-3 rounded px-2 py-1.5 hover:bg-slate-50">
      <span
        className="w-44 shrink-0 truncate text-[11px] text-slate-600"
        title={label}
      >
        {label}
      </span>
      <span
        className={`w-7 shrink-0 text-right text-[11px] font-bold tabular-nums ${scoreColor(latest)}`}
      >
        {latest}
      </span>
      <div className={`flex-1 ${scoreColor(latest)}`}>
        <Sparkline values={values} width={100} height={22} />
      </div>
      <span
        className={`w-8 shrink-0 text-right text-[10px] font-semibold tabular-nums ${
          delta > 0
            ? 'text-green-600'
            : delta < 0
              ? 'text-red-500'
              : 'text-slate-300'
        }`}
      >
        {delta === 0 ? '—' : delta > 0 ? `▲${delta}` : `▼${Math.abs(delta)}`}
      </span>
    </div>
  );
}

// ---- Past assessments ----

interface PastAssessmentsProps {
  refreshKey: number;
  sections: FrameworkSection[];
}

function PastAssessments({ refreshKey, sections }: PastAssessmentsProps) {
  const [history, setHistory] = useState<PortfolioEntry[]>([]);

  useEffect(() => {
    const all = getPortfolio()
      .filter((e) => e.templateId === TEMPLATE_ID)
      .sort(
        (a, b) =>
          new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime(),
      );
    setHistory(all);
  }, [refreshKey]);

  if (history.length === 0) return null;

  // Oldest-first for charting
  const chronological = [...history].reverse();

  const allItems = sections.flatMap((s) =>
    s.clusters.flatMap((c) => c.items),
  );

  function clusterAvg(
    e: PortfolioEntry,
    items: DispositionItem[],
  ): number {
    const r = e.responses as Record<string, number>;
    const vals = items
      .map((i) => r[i.id])
      .filter((v): v is number => typeof v === 'number');
    return average(vals);
  }

  function overallAvgFor(e: PortfolioEntry): number {
    const r = e.responses as Record<string, number>;
    const vals = allItems
      .map((i) => r[i.id])
      .filter((v): v is number => typeof v === 'number');
    return average(vals);
  }

  const showTrend = history.length >= 3;

  return (
    <div className="space-y-4">
      {/* ── Trend chart (#15) ── */}
      {showTrend && (
        <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
          <div className="mb-4 flex items-center justify-between">
            <h3 className="text-xs font-semibold uppercase tracking-widest text-slate-500">
              Trend
            </h3>
            <span className="text-[10px] text-slate-400">
              {chronological.length} assessments · oldest → newest
            </span>
          </div>
          <div className="space-y-1">
            {/* Overall */}
            <TrendRow
              label="Overall average"
              values={chronological.map(overallAvgFor)}
            />
            <div className="my-2 border-t border-slate-100" />
            {/* Per cluster */}
            {sections.flatMap((section) =>
              section.clusters.map((cluster) => (
                <TrendRow
                  key={`${section.key}-${cluster.cluster}`}
                  label={cluster.cluster}
                  values={chronological.map((e) =>
                    clusterAvg(e, cluster.items),
                  )}
                />
              )),
            )}
          </div>
        </div>
      )}

      {/* ── History list ── */}
      <details className="rounded-xl border border-slate-200 bg-white px-4 py-3 shadow-sm">
        <summary className="cursor-pointer select-none text-xs font-medium text-slate-600">
          Past assessments ({history.length})
        </summary>
        <div className="mt-3 divide-y divide-slate-100">
          {history.map((e) => {
            const avg = overallAvgFor(e);
            return (
              <div
                key={e.id}
                className="flex items-center justify-between py-2 text-xs"
              >
                <span className="text-slate-600">{e.title}</span>
                <div className="flex items-center gap-3">
                  <span className={`font-bold ${scoreColor(avg)}`}>
                    {avg}/10
                  </span>
                  <Link
                    href={`/portfolio/${e.id}`}
                    className="text-slate-400 hover:text-slate-700"
                  >
                    view →
                  </Link>
                </div>
              </div>
            );
          })}
        </div>
      </details>
    </div>
  );
}

// ---- Page ----

export default function AssessPage() {
  const [sections, setSections] = useState<FrameworkSection[]>([]);
  const [ratings, setRatings] = useState<Record<string, number>>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [previousEntry, setPreviousEntry] = useState<PortfolioEntry | null>(
    null,
  );
  const [saved, setSaved] = useState(false);
  const [saveCount, setSaveCount] = useState(0);

  // ---- Load data ----
  useEffect(() => {
    // Sync: most recent past assessment for comparison
    setPreviousEntry(loadPreviousAssessment());

    // Async: fetch disposition data
    async function load() {
      try {
        const res = await fetch('/data/frameworks/cross-framework-synthesis.json');
        if (!res.ok) throw new Error('Failed to fetch disposition data.');
        const data = (await res.json()) as RawSynthesisData;
        const built = buildSections(data);
        setSections(built);

        // Default all sliders to 5
        const init: Record<string, number> = {};
        built.forEach((s) =>
          s.clusters.forEach((c) =>
            c.items.forEach((item) => {
              init[item.id] = 5;
            }),
          ),
        );
        setRatings(init);
      } catch (err) {
        setError(
          err instanceof Error ? err.message : 'Unknown error loading data.',
        );
      } finally {
        setLoading(false);
      }
    }
    void load();
  }, []);

  // ---- Handlers ----

  function handleChange(id: string, value: number) {
    setRatings((prev) => ({ ...prev, [id]: value }));
    setSaved(false);
  }

  function handleSave() {
    const now = new Date();
    const entry: PortfolioEntry = {
      id: generateId(),
      createdAt: now.toISOString(),
      updatedAt: now.toISOString(),
      type: 'reflection',
      title: `Disposition Self-Assessment — ${now.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })}`,
      templateId: TEMPLATE_ID,
      responses: { ...ratings } as Record<string, unknown>,
      tags: ['disposition', 'self-assessment', 'ennis', 'delphi'],
    };
    savePortfolioEntry(entry);
    setPreviousEntry(entry);
    setSaved(true);
    setSaveCount((n) => n + 1);
  }

  // ---- Derived stats ----

  const allItems = useMemo(
    () => sections.flatMap((s) => s.clusters.flatMap((c) => c.items)),
    [sections],
  );

  const previousResponses = previousEntry?.responses as
    | Record<string, number>
    | undefined;

  const ratedItems = allItems.map((item) => ({
    ...item,
    value: ratings[item.id] ?? 5,
    prev: previousResponses?.[item.id] ?? null,
  }));

  const sorted = [...ratedItems].sort((a, b) => b.value - a.value);
  const top3 = sorted.slice(0, 3);
  const bottom3 = [...sorted].slice(-3).reverse();
  const overallAvg = average(ratedItems.map((i) => i.value));

  const hasPrevious = previousEntry !== null && !saved;
  const showDeltaCol = hasPrevious || (saved && saveCount > 1);

  // ---- Render ----

  if (loading) {
    return (
      <div className="flex items-center justify-center py-32 text-sm text-slate-400">
        Loading dispositions…
      </div>
    );
  }

  if (error) {
    return (
      <div className="mx-auto max-w-md py-24 text-center">
        <p className="font-semibold text-red-600">Failed to load</p>
        <p className="mt-1 text-sm text-slate-500">{error}</p>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-3xl space-y-10 pb-20">
      {/* ── Page header ── */}
      <div className="space-y-3">
        <h1 className="text-2xl font-bold tracking-tight text-slate-900">
          Disposition Self-Assessment
        </h1>
        <p className="max-w-xl text-sm leading-relaxed text-slate-500">
          Rate yourself on each critical thinking disposition:{' '}
          <span className="font-medium text-slate-700">1</span> = rarely or
          never, <span className="font-medium text-slate-700">5</span> = sometimes,{' '}
          <span className="font-medium text-slate-700">10</span> = consistently.
          Dispositions are the motivational engine behind CT skills — skill
          without disposition produces no reliable thinking.
        </p>
        {previousEntry && hasPrevious && (
          <div className="flex items-center gap-2 rounded-lg border border-slate-200 bg-slate-50 px-3 py-2 text-xs">
            <span className="text-slate-400">Comparing with:</span>
            <span className="font-medium text-slate-700">
              {previousEntry.title}
            </span>
            <Link
              href={`/portfolio/${previousEntry.id}`}
              className="ml-auto shrink-0 text-slate-400 hover:text-slate-700"
            >
              view →
            </Link>
          </div>
        )}
      </div>

      {/* ── Framework sections ── */}
      {sections.map((section) => {
        const sectionAvg = average(
          section.clusters
            .flatMap((c) => c.items)
            .map((item) => ratings[item.id] ?? 5),
        );

        return (
          <div key={section.key} className="space-y-6">
            {/* Section header */}
            <div className="flex items-start justify-between gap-4 border-b border-slate-200 pb-4">
              <div>
                <h2 className="text-base font-semibold text-slate-900">
                  {section.title}
                </h2>
                <p className="mt-1 max-w-xl text-xs leading-relaxed text-slate-500">
                  {section.description}
                </p>
              </div>
              <div className="shrink-0 text-right">
                <p
                  className={`text-2xl font-bold tabular-nums ${scoreColor(sectionAvg)}`}
                >
                  {sectionAvg}
                </p>
                <p className="text-[10px] text-slate-400">section avg</p>
              </div>
            </div>

            {/* Cluster groups */}
            {section.clusters.map((cluster) => (
              <div key={cluster.cluster}>
                <p className="mb-2 text-[10px] font-semibold uppercase tracking-widest text-slate-400">
                  {cluster.cluster}
                </p>
                <div className="rounded-xl border border-slate-200 bg-white shadow-sm">
                  {cluster.items.map((item, idx) => {
                    const value = ratings[item.id] ?? 5;
                    const prev = previousResponses?.[item.id] ?? null;
                    const delta = prev !== null ? value - prev : null;
                    return (
                      <div
                        key={item.id}
                        className={
                          idx < cluster.items.length - 1
                            ? 'border-b border-slate-100'
                            : ''
                        }
                      >
                        <DispositionRow
                          label={item.label}
                          value={value}
                          delta={delta}
                          showDeltaCol={showDeltaCol}
                          onChange={(v) => handleChange(item.id, v)}
                        />
                      </div>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        );
      })}

      {/* ── Profile summary ── */}
      {allItems.length > 0 && (
        <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
          <div className="flex items-center justify-between">
            <h3 className="font-semibold text-slate-900">Your Profile</h3>
            <div className="text-right">
              <span
                className={`text-3xl font-bold tabular-nums ${scoreColor(overallAvg)}`}
              >
                {overallAvg}
              </span>
              <span className="ml-1 text-xs text-slate-400">/ 10</span>
            </div>
          </div>

          {/* Progress bar */}
          <div className="my-4 h-2.5 w-full overflow-hidden rounded-full bg-slate-100">
            <div
              className={`h-full rounded-full transition-all duration-700 ${scoreBg(overallAvg)}`}
              style={{ width: `${((overallAvg - 1) / 9) * 100}%` }}
            />
          </div>

          <p className="mb-6 text-[11px] text-slate-400">
            1 = Rarely · 5 = Sometimes · 10 = Consistently
          </p>

          {/* Cluster breakdown */}
          <ClusterBreakdown sections={sections} ratings={ratings} />

          {/* Strengths & development areas */}
          <div className="grid grid-cols-1 gap-5 sm:grid-cols-2">
            <div>
              <p className="mb-3 text-[10px] font-semibold uppercase tracking-widest text-green-700">
                Current strengths
              </p>
              <div className="space-y-2">
                {top3.map((item) => (
                  <div key={item.id} className="flex items-start gap-2.5">
                    <span
                      className={`mt-0.5 shrink-0 text-sm font-bold tabular-nums ${scoreColor(item.value)}`}
                    >
                      {item.value}
                    </span>
                    <span className="text-xs leading-snug text-slate-600">
                      {item.label}
                    </span>
                  </div>
                ))}
              </div>
            </div>
            <div>
              <p className="mb-3 text-[10px] font-semibold uppercase tracking-widest text-amber-700">
                For development
              </p>
              <div className="space-y-2">
                {bottom3.map((item) => (
                  <div key={item.id} className="flex items-start gap-2.5">
                    <span
                      className={`mt-0.5 shrink-0 text-sm font-bold tabular-nums ${scoreColor(item.value)}`}
                    >
                      {item.value}
                    </span>
                    <span className="text-xs leading-snug text-slate-600">
                      {item.label}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ── Recommendations ── */}
      {allItems.length > 0 && bottom3.length > 0 && (
        <AssessRecommendations bottomItems={bottom3} />
      )}

      {/* ── Save ── */}
      <div className="flex items-center gap-4">
        <button
          type="button"
          onClick={handleSave}
          disabled={saved}
          className={`rounded-lg px-5 py-2.5 text-sm font-semibold transition ${
            saved
              ? 'cursor-default bg-green-100 text-green-700'
              : 'bg-slate-900 text-white hover:bg-slate-700 active:bg-slate-800'
          }`}
        >
          {saved ? '✓ Saved to Portfolio' : 'Save Assessment'}
        </button>
        {saved && (
          <Link
            href="/portfolio"
            className="text-xs text-slate-500 hover:text-slate-700"
          >
            View in Portfolio →
          </Link>
        )}
      </div>

      {/* ── Past assessments ── */}
      <PastAssessments refreshKey={saveCount} sections={sections} />
    </div>
  );
}
