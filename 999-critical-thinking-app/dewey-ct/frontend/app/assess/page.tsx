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

interface PastAssessmentsProps {
  refreshKey: number;
}

function PastAssessments({ refreshKey }: PastAssessmentsProps) {
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

  return (
    <details className="rounded-xl border border-slate-200 bg-white px-4 py-3 shadow-sm">
      <summary className="cursor-pointer select-none text-xs font-medium text-slate-600">
        Past assessments ({history.length})
      </summary>
      <div className="mt-3 divide-y divide-slate-100">
        {history.map((e) => {
          const responses = e.responses as Record<string, unknown>;
          const vals = Object.values(responses)
            .map((v) => (typeof v === 'number' ? v : null))
            .filter((v): v is number => v !== null);
          const avg = vals.length > 0 ? average(vals) : null;
          return (
            <div
              key={e.id}
              className="flex items-center justify-between py-2 text-xs"
            >
              <span className="text-slate-600">{e.title}</span>
              <div className="flex items-center gap-3">
                {avg !== null && (
                  <span className={`font-bold ${scoreColor(avg)}`}>
                    {avg}/10
                  </span>
                )}
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
      <PastAssessments refreshKey={saveCount} />
    </div>
  );
}
