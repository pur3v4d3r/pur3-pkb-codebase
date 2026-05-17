'use client';

import React from 'react';
import type { CheatSheet } from '@/types/framework';

type AnyRecord = Record<string, unknown>;

// ---------- Category colour map ----------
export const CATEGORY_COLORS: Record<
  string,
  { header: string; lead: string; badge: string }
> = {
  'CT Frameworks': {
    header: 'bg-indigo-600',
    lead: 'bg-indigo-100 text-indigo-700',
    badge: 'bg-indigo-100 text-indigo-700',
  },
  'Argument Analysis': {
    header: 'bg-violet-600',
    lead: 'bg-violet-100 text-violet-700',
    badge: 'bg-violet-100 text-violet-700',
  },
  Dispositions: {
    header: 'bg-amber-500',
    lead: 'bg-amber-100 text-amber-700',
    badge: 'bg-amber-100 text-amber-700',
  },
  'Cognitive Models': {
    header: 'bg-teal-600',
    lead: 'bg-teal-100 text-teal-700',
    badge: 'bg-teal-100 text-teal-700',
  },
  Taxonomies: {
    header: 'bg-emerald-600',
    lead: 'bg-emerald-100 text-emerald-700',
    badge: 'bg-emerald-100 text-emerald-700',
  },
};

// ---------- helpers ----------

function getLeading(elem: AnyRecord): string | number | undefined {
  if (typeof elem.letter === 'string') return elem.letter;
  if (typeof elem.number === 'number') return elem.number;
  if (typeof elem.level === 'number') return elem.level;
  if (typeof elem.level === 'string') return elem.level;
  return undefined;
}

function getTitle(elem: AnyRecord): string {
  return String(
    elem.name ??
      elem.activity ??
      elem.mode ??
      elem.disposition ??
      elem.element ??
      elem.phase ??
      elem.commitment ??
      '',
  );
}

// Extra callout fields appended at the bottom of a card
function collectExtras(
  sheet: AnyRecord,
): Array<{ label: string; value: string | string[] }> {
  const result: Array<{ label: string; value: string | string[] }> = [];
  if (sheet.ct_threshold) result.push({ label: 'CT Threshold', value: sheet.ct_threshold as string });
  if (sheet.ct_implication) result.push({ label: 'CT Implication', value: sheet.ct_implication as string });
  if (sheet.ct_connection) result.push({ label: 'CT Connection', value: sheet.ct_connection as string });
  if (sheet.key_insight) result.push({ label: 'Key Insight', value: sheet.key_insight as string });
  if (sheet.memory_aid) result.push({ label: 'Memory Aid', value: sheet.memory_aid as string });
  if (sheet.knowledge_dimension)
    result.push({ label: 'Knowledge Dimension', value: sheet.knowledge_dimension as string[] });
  if (sheet.five_subtests)
    result.push({ label: 'Five Subtests', value: sheet.five_subtests as string[] });
  if (sheet.assumption_types)
    result.push({ label: 'Assumption Types', value: sheet.assumption_types as string[] });
  return result;
}

// ---------- Row: handles all "element / level" variants ----------

function ElementRow({
  elem,
  leadColor,
}: {
  elem: AnyRecord;
  leadColor: string;
}) {
  const lead = getLeading(elem);
  const titleText = getTitle(elem);
  const desc = elem.description as string | undefined;
  const subSkills = elem.sub_skills as string[] | undefined;
  const required = elem.required as boolean | undefined;
  const question = elem.question as string | undefined;
  const example = elem.example as string | undefined;

  return (
    <div className="flex gap-3 py-2 border-b border-slate-100 last:border-0">
      {lead !== undefined && (
        <span
          className={`flex-shrink-0 w-7 h-7 rounded-full text-xs font-bold flex items-center justify-center ${leadColor}`}
        >
          {lead}
        </span>
      )}
      <div className="flex-1 min-w-0">
        {/* Browne & Keeley: element has only a question, no name */}
        {question && !titleText ? (
          <p className="text-sm text-slate-700 leading-relaxed">{question}</p>
        ) : (
          <>
            <div className="flex items-baseline gap-2 flex-wrap">
              {titleText && (
                <span className="text-sm font-semibold text-slate-800">{titleText}</span>
              )}
              {required !== undefined && (
                <span
                  className={`text-[10px] px-1.5 py-0.5 rounded font-medium ${
                    required
                      ? 'bg-emerald-100 text-emerald-700'
                      : 'bg-slate-100 text-slate-500'
                  }`}
                >
                  {required ? 'required' : 'optional'}
                </span>
              )}
            </div>
            {desc && (
              <p className="text-xs text-slate-500 mt-0.5 leading-relaxed">{desc}</p>
            )}
            {question && titleText && (
              <p className="text-xs text-slate-500 mt-0.5 leading-relaxed">{question}</p>
            )}
            {subSkills && (
              <div className="flex flex-wrap gap-1 mt-1.5">
                {subSkills.map((s) => (
                  <span
                    key={s}
                    className="text-xs bg-indigo-50 text-indigo-600 px-1.5 py-0.5 rounded"
                  >
                    {s}
                  </span>
                ))}
              </div>
            )}
            {example && (
              <p className="text-xs italic text-slate-400 mt-0.5">e.g. {example}</p>
            )}
          </>
        )}
      </div>
    </div>
  );
}

// ---------- Block: for `systems` arrays (Dual-Process, Marzano) ----------

function SystemBlock({ sys, leadColor }: { sys: AnyRecord; leadColor: string }) {
  const name = String(sys.system ?? '');
  const desc = sys.description as string | undefined;
  const fn = sys.function as string | undefined;
  const props = sys.properties as string[] | undefined;
  const components = sys.components as string[] | undefined;

  return (
    <div className="mb-3 last:mb-0 pb-3 last:pb-0 border-b border-slate-100 last:border-0">
      <span
        className={`inline-block text-xs font-bold px-2 py-0.5 rounded mb-1 ${leadColor}`}
      >
        {name}
      </span>
      {fn && <p className="text-xs text-slate-500 mb-1">{fn}</p>}
      {desc && <p className="text-xs text-slate-600 leading-relaxed">{desc}</p>}
      {props && (
        <div className="flex flex-wrap gap-1 mt-1.5">
          {props.map((p) => (
            <span key={p} className="text-xs bg-slate-100 text-slate-600 px-1.5 py-0.5 rounded">
              {p}
            </span>
          ))}
        </div>
      )}
      {components && (
        <ul className="mt-1 space-y-0.5">
          {components.map((c) => (
            <li key={c} className="text-xs text-slate-600 flex items-start gap-1.5">
              <span className="text-slate-400 mt-0.5 flex-shrink-0">•</span>
              {c}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

// ---------- Sub-section: for Developmental Models ----------

function SubSection({
  title,
  items,
  leadColor,
}: {
  title: string;
  items: AnyRecord[];
  leadColor: string;
}) {
  return (
    <div className="mb-4 last:mb-0">
      <p className="text-[10px] font-semibold text-slate-400 uppercase tracking-wider mb-1">
        {title}
      </p>
      {items.map((item, i) => (
        <ElementRow key={i} elem={item} leadColor={leadColor} />
      ))}
    </div>
  );
}

// ---------- Main card ----------

interface CheatSheetCardProps {
  sheet: CheatSheet;
  category: string;
}

export default function CheatSheetCard({ sheet, category }: CheatSheetCardProps) {
  const colors = CATEGORY_COLORS[category] ?? CATEGORY_COLORS['CT Frameworks'];

  const elements = sheet.elements as AnyRecord[] | undefined;
  const levels = sheet.levels as AnyRecord[] | undefined;
  const systems = sheet.systems as AnyRecord[] | undefined;
  const perryPhases = sheet.perry_phases as AnyRecord[] | undefined;
  const kingKitchener = sheet.king_kitchener_levels as AnyRecord[] | undefined;
  const kuhnLevels = sheet.kuhn_levels as AnyRecord[] | undefined;
  const stanovich = sheet.stanovich_tripartite as AnyRecord | undefined;
  const extras = collectExtras(sheet);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden flex flex-col">
      {/* Header */}
      <div className={`${colors.header} px-4 py-3 flex items-start justify-between gap-2`}>
        <h3 className="text-white font-semibold text-sm leading-snug">{sheet.framework}</h3>
        <span className="text-[10px] px-2 py-0.5 rounded-full bg-white/20 text-white font-medium flex-shrink-0">
          {category}
        </span>
      </div>

      {/* Body */}
      <div className="p-4 flex-1">
        {/* elements (FRISCO, Delphi, Bloom, Halpern, Watson-Glaser, Toulmin, B&K, Lipman, Brookfield, CCTDI) */}
        {elements && (
          <div>
            {elements.map((elem, i) => (
              <ElementRow key={i} elem={elem} leadColor={colors.lead} />
            ))}
          </div>
        )}

        {/* levels (SOLO, Webb DOK, DIKW, Bloom Affective) */}
        {levels && (
          <div>
            {levels.map((lvl, i) => (
              <ElementRow key={i} elem={lvl} leadColor={colors.lead} />
            ))}
          </div>
        )}

        {/* systems (Dual-Process Theory, Marzano's Three Systems) */}
        {systems && (
          <div>
            {systems.map((sys, i) => (
              <SystemBlock key={i} sys={sys} leadColor={colors.lead} />
            ))}
          </div>
        )}

        {/* Stanovich Tripartite (nested in Dual-Process sheet) */}
        {stanovich && (
          <div className="mt-3 border-t border-slate-100 pt-3">
            <p className="text-[10px] font-semibold text-slate-400 uppercase tracking-wider mb-2">
              Stanovich Tripartite
            </p>
            {Object.entries(stanovich).map(([k, v]) => (
              <div key={k} className="flex gap-2 py-1 border-b border-slate-50 last:border-0">
                <span className="text-xs font-medium text-slate-700 capitalize w-32 flex-shrink-0">
                  {k.replace(/_/g, ' ')}
                </span>
                <span className="text-xs text-slate-500 leading-relaxed">{String(v)}</span>
              </div>
            ))}
          </div>
        )}

        {/* Developmental Models — three parallel sub-sections */}
        {perryPhases && (
          <SubSection title="Perry's Phases" items={perryPhases} leadColor={colors.lead} />
        )}
        {kingKitchener && (
          <SubSection title="King & Kitchener" items={kingKitchener} leadColor={colors.lead} />
        )}
        {kuhnLevels && (
          <SubSection title="Kuhn's Levels" items={kuhnLevels} leadColor={colors.lead} />
        )}

        {/* Extra callout fields (key_insight, ct_connection, memory_aid, etc.) */}
        {extras.length > 0 && (
          <div className="mt-3 border-t border-slate-100 pt-3 space-y-2">
            {extras.map(({ label, value }) => (
              <div key={label} className="bg-slate-50 rounded-lg p-2.5">
                <p className="text-[10px] font-semibold text-slate-400 uppercase tracking-wider mb-1">
                  {label}
                </p>
                {Array.isArray(value) ? (
                  <div className="flex flex-wrap gap-1">
                    {value.map((v) => (
                      <span
                        key={v}
                        className="text-xs bg-white border border-slate-200 text-slate-600 px-1.5 py-0.5 rounded"
                      >
                        {v}
                      </span>
                    ))}
                  </div>
                ) : (
                  <p className="text-xs text-slate-600 leading-relaxed">{value}</p>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
