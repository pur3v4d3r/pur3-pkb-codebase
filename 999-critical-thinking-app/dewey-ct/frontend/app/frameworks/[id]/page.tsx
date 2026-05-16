import { getFramework, type FrameworkId } from '@/lib/content';
import Link from 'next/link';
import { notFound } from 'next/navigation';

// Must stay in sync with FRAMEWORK_FILES in lib/content.ts
const VALID_IDS = [
  'paul-elder',
  'blooms-taxonomy',
  'socratic-questioning',
  'toulmin-argument',
  'mental-models',
  'logical-fallacies',
  'dewey-five-phases',
  'ennis-framework',
  'delphi-consensus',
  'dual-process-theory',
  'habits-of-mind',
  'browne-keeley',
  'paul-elder-enrichments',
  'acer-critical-thinking',
  'acer-metacognitive',
  'developmental-models',
  'cognitive-biases',
  'cross-framework-synthesis',
  'siegel-reasons-conception',
  'halpern-critical-thinking',
  'webbs-depth-of-knowledge',
  'marzano-new-taxonomy',
  'solo-taxonomy',
  'watson-glaser',
  'cctdi',
  'walton-argumentation-schemes',
  'lipman-community-of-inquiry',
  'brookfield-critical-thinking',
  'dikw-pyramid',
  'bailin-reconception',
] satisfies FrameworkId[];

// ---- Local types reflecting the actual JSON structure ----

interface Misconception {
  misconception: string;
  correction: string;
  practical_implication?: string;
  pedagogical_implication?: string;
}

interface ElementOfThought {
  number: number;
  element: string;
  definition: string;
  probing_questions?: string[];
  common_failure?: string;
  example_well_stated?: string;
  example_poorly_stated?: string;
  dewey_connection?: string;
  intellectual_standards_most_relevant?: string[];
  template_field_label?: string;
  template_field_placeholder?: string;
}

interface BloomLevel {
  level: number;
  name: string;
  verb?: string;
  cognitive_process?: string;
  key_verbs?: string[];
  bloom_to_dewey?: string;
  example?: string;
  questions?: string[];
}

interface FrameworkData {
  framework?: string;
  name?: string;
  authors?: string[];
  year?: number;
  original_year?: number;
  source?: string;
  publisher?: string;
  website?: string;
  description?: string;
  dewey_integration?: string;
  common_misconceptions?: Misconception[];
  app_usage?: {
    primary_template?: string;
    primary_template_description?: string;
    [key: string]: unknown;
  };
  components?: {
    elements_of_thought?: ElementOfThought[];
    [key: string]: unknown;
  };
  levels?: BloomLevel[];
  // Generic list shapes that other frameworks may use
  abilities?: Array<{ name: string; description?: string; [key: string]: unknown }>;
  dispositions?: Array<{ name: string; description?: string; [key: string]: unknown }>;
  phases?: Array<{ phase?: number; name: string; description?: string; [key: string]: unknown }>;
  habits?: Array<{ number?: number; name: string; description?: string; [key: string]: unknown }>;
  questions?: Array<{ number?: number; question?: string; name?: string; description?: string; purpose?: string; [key: string]: unknown }>;
  types?: Array<{ name: string; description?: string; [key: string]: unknown }>;
  fallacies?: Array<{ name: string; definition?: string; description?: string; [key: string]: unknown }>;
  models?: Array<{ name: string; description?: string; [key: string]: unknown }>;
  [key: string]: unknown;
}

// ---- Utility ----

function displayName(fw: FrameworkData): string {
  return fw.framework ?? fw.name ?? 'Framework';
}

// ---- Sub-renderers ----

function MisconceptionBlock({ m, index }: { m: Misconception; index: number }) {
  const implication = m.practical_implication ?? m.pedagogical_implication;
  return (
    <details className="group rounded-lg border border-amber-200 bg-amber-50">
      <summary className="flex cursor-pointer items-start gap-3 p-4 marker:hidden list-none">
        <span className="flex-shrink-0 mt-0.5 flex h-5 w-5 items-center justify-center rounded-full bg-amber-200 text-xs font-bold text-amber-800">
          {index + 1}
        </span>
        <span className="text-sm font-medium leading-snug text-amber-900">{m.misconception}</span>
        <svg
          className="ml-auto flex-shrink-0 h-4 w-4 text-amber-500 transition-transform group-open:rotate-180"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          strokeWidth={2}
        >
          <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
        </svg>
      </summary>
      <div className="space-y-3 border-t border-amber-200 px-4 py-3">
        <div>
          <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-amber-600">Correction</p>
          <p className="text-sm leading-relaxed text-amber-900">{m.correction}</p>
        </div>
        {implication && (
          <div>
            <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-amber-600">Practical Implication</p>
            <p className="text-sm leading-relaxed text-amber-900">{implication}</p>
          </div>
        )}
      </div>
    </details>
  );
}

function ElementBlock({ el }: { el: ElementOfThought }) {
  return (
    <details className="group rounded-lg border border-slate-200 bg-white">
      <summary className="flex cursor-pointer items-start gap-3 p-4 marker:hidden list-none">
        <span className="flex-shrink-0 mt-0.5 flex h-7 w-7 items-center justify-center rounded-full bg-slate-900 text-xs font-bold text-white">
          {el.number}
        </span>
        <div className="min-w-0">
          <p className="font-semibold text-slate-900">{el.element}</p>
          <p className="mt-0.5 text-xs leading-relaxed text-slate-500 line-clamp-2">{el.definition}</p>
        </div>
        <svg
          className="ml-auto mt-1 flex-shrink-0 h-4 w-4 text-slate-400 transition-transform group-open:rotate-180"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          strokeWidth={2}
        >
          <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
        </svg>
      </summary>
      <div className="space-y-4 border-t border-slate-100 px-4 py-4">
        <p className="text-sm leading-relaxed text-slate-700">{el.definition}</p>

        {el.intellectual_standards_most_relevant && el.intellectual_standards_most_relevant.length > 0 && (
          <div>
            <p className="mb-2 text-xs font-semibold uppercase tracking-wider text-slate-400">Key Standards</p>
            <div className="flex flex-wrap gap-1.5">
              {el.intellectual_standards_most_relevant.map((s) => (
                <span key={s} className="rounded-full border border-slate-200 bg-slate-50 px-2.5 py-0.5 text-xs font-medium text-slate-600">
                  {s}
                </span>
              ))}
            </div>
          </div>
        )}

        {el.probing_questions && el.probing_questions.length > 0 && (
          <div>
            <p className="mb-2 text-xs font-semibold uppercase tracking-wider text-slate-400">Probing Questions</p>
            <ul className="space-y-1.5">
              {el.probing_questions.map((q, i) => (
                <li key={i} className="flex items-start gap-2 text-sm text-slate-600">
                  <span className="mt-1 flex-shrink-0 h-1.5 w-1.5 rounded-full bg-slate-400" />
                  {q}
                </li>
              ))}
            </ul>
          </div>
        )}

        {el.common_failure && (
          <div className="rounded-md border-l-2 border-red-200 bg-red-50 px-4 py-2.5">
            <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-red-400">Common Failure</p>
            <p className="text-xs leading-relaxed text-red-800">{el.common_failure}</p>
          </div>
        )}

        {el.dewey_connection && (
          <div className="rounded-md border-l-2 border-blue-200 bg-blue-50 px-4 py-2.5">
            <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-blue-400">Dewey Connection</p>
            <p className="text-xs leading-relaxed text-blue-800">{el.dewey_connection}</p>
          </div>
        )}

        {(el.example_well_stated || el.example_poorly_stated) && (
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
            {el.example_well_stated && (
              <div className="rounded-md border border-green-200 bg-green-50 p-3">
                <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-green-600">Well-stated</p>
                <p className="text-xs leading-relaxed text-green-900 italic">{el.example_well_stated}</p>
              </div>
            )}
            {el.example_poorly_stated && (
              <div className="rounded-md border border-red-200 bg-red-50 p-3">
                <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-red-500">Poorly stated</p>
                <p className="text-xs leading-relaxed text-red-900 italic">{el.example_poorly_stated}</p>
              </div>
            )}
          </div>
        )}
      </div>
    </details>
  );
}

function LevelBlock({ lvl }: { lvl: BloomLevel }) {
  return (
    <details className="group rounded-lg border border-slate-200 bg-white">
      <summary className="flex cursor-pointer items-start gap-3 p-4 marker:hidden list-none">
        <span className="flex-shrink-0 mt-0.5 flex h-7 w-7 items-center justify-center rounded-full bg-slate-900 text-xs font-bold text-white">
          {lvl.level}
        </span>
        <div className="min-w-0">
          <p className="font-semibold text-slate-900">{lvl.name}</p>
          {lvl.verb && (
            <p className="mt-0.5 text-xs text-slate-500">Cognitive process: <em>{lvl.verb}</em></p>
          )}
        </div>
        <svg
          className="ml-auto mt-1 flex-shrink-0 h-4 w-4 text-slate-400 transition-transform group-open:rotate-180"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          strokeWidth={2}
        >
          <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
        </svg>
      </summary>
      <div className="space-y-4 border-t border-slate-100 px-4 py-4">
        {lvl.cognitive_process && (
          <p className="text-sm leading-relaxed text-slate-700">{lvl.cognitive_process}</p>
        )}
        {lvl.key_verbs && lvl.key_verbs.length > 0 && (
          <div>
            <p className="mb-2 text-xs font-semibold uppercase tracking-wider text-slate-400">Key Verbs</p>
            <div className="flex flex-wrap gap-1.5">
              {lvl.key_verbs.map((v) => (
                <span key={v} className="rounded bg-slate-100 px-2 py-0.5 text-xs font-mono text-slate-600">{v}</span>
              ))}
            </div>
          </div>
        )}
        {lvl.example && (
          <div className="rounded-md border-l-2 border-slate-300 bg-slate-50 px-4 py-2.5">
            <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-slate-400">Example</p>
            <p className="text-xs leading-relaxed text-slate-700 italic">{lvl.example}</p>
          </div>
        )}
        {lvl.bloom_to_dewey && (
          <div className="rounded-md border-l-2 border-blue-200 bg-blue-50 px-4 py-2.5">
            <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-blue-400">Dewey Mapping</p>
            <p className="text-xs leading-relaxed text-blue-800">{lvl.bloom_to_dewey}</p>
          </div>
        )}
      </div>
    </details>
  );
}

/** Generic list section for habits, abilities, dispositions, etc. */
function GenericListSection({
  title,
  items,
}: {
  title: string;
  items: Array<{ number?: number; name?: string; element?: string; question?: string; definition?: string; description?: string; purpose?: string; [key: string]: unknown }>;
}) {
  return (
    <section className="space-y-3">
      <h2 className="text-xs font-semibold uppercase tracking-widest text-slate-400">{title}</h2>
      <div className="space-y-2">
        {items.map((item, i) => {
          const label = item.name ?? item.element ?? item.question ?? `Item ${i + 1}`;
          const body = item.description ?? item.definition ?? item.purpose ?? '';
          return (
            <div key={i} className="rounded-lg border border-slate-200 bg-white p-4">
              <div className="flex items-start gap-3">
                {(item.number !== undefined || item.level !== undefined) && (
                  <span className="flex-shrink-0 flex h-6 w-6 items-center justify-center rounded-full bg-slate-100 text-xs font-bold text-slate-600">
                    {(item.number as number | undefined) ?? (item.level as number | undefined)}
                  </span>
                )}
                <div>
                  <p className="text-sm font-semibold text-slate-900">{label as string}</p>
                  {body && <p className="mt-1 text-xs leading-relaxed text-slate-600">{body as string}</p>}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}

// ---- Page ----

export function generateStaticParams() {
  return VALID_IDS.map((id) => ({ id }));
}

export async function generateMetadata({ params }: { params: { id: string } }) {
  if (!VALID_IDS.includes(params.id as FrameworkId)) return {};
  const fw = getFramework(params.id as FrameworkId) as unknown as FrameworkData;
  return {
    title: `${displayName(fw)} — DeweyCT`,
    description: fw.description?.slice(0, 160),
  };
}

export default function FrameworkPage({ params }: { params: { id: string } }) {
  if (!VALID_IDS.includes(params.id as FrameworkId)) notFound();

  const fw = getFramework(params.id as FrameworkId) as unknown as FrameworkData;
  const name = displayName(fw);

  const elements = fw.components?.elements_of_thought;
  const levels = fw.levels;

  // Detect other generic list structures
  const genericSections: Array<{ key: string; label: string }> = [
    { key: 'abilities', label: 'Abilities' },
    { key: 'dispositions', label: 'Dispositions' },
    { key: 'phases', label: 'Phases' },
    { key: 'habits', label: 'Habits of Mind' },
    { key: 'questions', label: 'Questions' },
    { key: 'types', label: 'Types' },
    { key: 'fallacies', label: 'Fallacies' },
    { key: 'models', label: 'Models' },
  ];

  return (
    <div className="mx-auto max-w-3xl space-y-8">
      {/* Breadcrumb */}
      <nav className="flex items-center gap-2 text-sm text-slate-500">
        <Link href="/frameworks" className="hover:text-slate-800">
          Frameworks
        </Link>
        <span>/</span>
        <span className="text-slate-800">{name}</span>
      </nav>

      {/* Header */}
      <header className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
        <h1 className="text-2xl font-bold leading-tight text-slate-900">{name}</h1>

        <div className="mt-3 flex flex-wrap items-center gap-3 text-xs text-slate-500">
          {fw.authors && fw.authors.length > 0 && (
            <span>{fw.authors.join(', ')}</span>
          )}
          {fw.year && (
            <span className="rounded-full bg-slate-100 px-2.5 py-0.5 font-medium">
              {fw.original_year ? `${fw.original_year} / rev. ${fw.year}` : fw.year}
            </span>
          )}
          {fw.source && (
            <span className="italic text-slate-400 truncate max-w-xs">{fw.source}</span>
          )}
        </div>

        {fw.app_usage?.primary_template && (
          <div className="mt-4 flex items-center gap-2 rounded-lg border border-blue-100 bg-blue-50 px-4 py-2.5">
            <svg className="h-4 w-4 flex-shrink-0 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
            <p className="flex-1 text-xs text-blue-800">
              {fw.app_usage.primary_template_description as string | undefined ?? 'Companion template available.'}
            </p>
            <Link
              href={`/templates/${fw.app_usage.primary_template}`}
              className="flex-shrink-0 rounded-md bg-blue-600 px-3 py-1.5 text-xs font-semibold text-white hover:bg-blue-700"
            >
              Open template
            </Link>
          </div>
        )}
      </header>

      {/* Description */}
      {fw.description && (
        <section className="space-y-3">
          <h2 className="text-xs font-semibold uppercase tracking-widest text-slate-400">Overview</h2>
          <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
            {fw.description.split('\n\n').map((para, i) => (
              <p key={i} className={`text-sm leading-relaxed text-slate-700 ${i > 0 ? 'mt-4' : ''}`}>
                {para.trim()}
              </p>
            ))}
          </div>
        </section>
      )}

      {/* Dewey Integration */}
      {fw.dewey_integration && (
        <section className="space-y-3">
          <h2 className="text-xs font-semibold uppercase tracking-widest text-slate-400">Dewey Integration</h2>
          <div className="rounded-xl border border-blue-200 bg-blue-50 p-6">
            {fw.dewey_integration.split('\n\n').map((para, i) => (
              <p key={i} className={`text-sm leading-relaxed text-blue-900 ${i > 0 ? 'mt-4' : ''}`}>
                {para.trim()}
              </p>
            ))}
          </div>
        </section>
      )}

      {/* Elements of Thought */}
      {elements && elements.length > 0 && (
        <section className="space-y-3">
          <h2 className="text-xs font-semibold uppercase tracking-widest text-slate-400">
            Elements of Thought ({elements.length})
          </h2>
          <p className="text-xs text-slate-400">Click any element to expand probing questions, common failures, and Dewey connections.</p>
          <div className="space-y-2">
            {elements.map((el) => (
              <ElementBlock key={el.number} el={el} />
            ))}
          </div>
        </section>
      )}

      {/* Bloom Levels */}
      {levels && levels.length > 0 && (
        <section className="space-y-3">
          <h2 className="text-xs font-semibold uppercase tracking-widest text-slate-400">
            Cognitive Levels ({levels.length})
          </h2>
          <div className="space-y-2">
            {levels.map((lvl) => (
              <LevelBlock key={lvl.level} lvl={lvl} />
            ))}
          </div>
        </section>
      )}

      {/* Generic list sections */}
      {genericSections.map(({ key, label }) => {
        const items = fw[key] as Array<Record<string, unknown>> | undefined;
        if (!items || items.length === 0) return null;
        return (
          <GenericListSection
            key={key}
            title={`${label} (${items.length})`}
            items={items}
          />
        );
      })}

      {/* Common Misconceptions */}
      {fw.common_misconceptions && fw.common_misconceptions.length > 0 && (
        <section className="space-y-3">
          <h2 className="text-xs font-semibold uppercase tracking-widest text-slate-400">
            Common Misconceptions ({fw.common_misconceptions.length})
          </h2>
          <p className="text-xs text-slate-400">Click to expand each misconception and its correction.</p>
          <div className="space-y-2">
            {fw.common_misconceptions.map((m, i) => (
              <MisconceptionBlock key={i} m={m} index={i} />
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
