import { getTemplate, type TemplateId } from '@/lib/content';
import TemplateForm, { type RawTemplate } from '@/components/template/TemplateForm';
import Link from 'next/link';
import { notFound } from 'next/navigation';

// Must stay in sync with TEMPLATE_FILES in lib/content.ts
const VALID_IDS = [
  'dewey-reflective-v1',
  'argument-analysis-v1',
  'blooms-scaffold-v1',
  'socratic-questioning-v1',
  'paul-elder-analysis-v1',
  'frisco-quick-analysis-v1',
  'see-i-elaboration-v1',
  'metacognitive-reflection-v1',
  'deliberate-practice-full-v1',
] satisfies TemplateId[];

export function generateStaticParams() {
  return VALID_IDS.map((id) => ({ id }));
}

export async function generateMetadata({ params }: { params: { id: string } }) {
  if (!VALID_IDS.includes(params.id as TemplateId)) return {};
  const data = getTemplate(params.id as TemplateId) as unknown as RawTemplate;
  return {
    title: `${data.name} — DeweyCT`,
    description: data.description,
  };
}

export default function TemplatePage({
  params,
  searchParams,
}: {
  params: { id: string };
  searchParams?: { context?: string };
}) {
  if (!VALID_IDS.includes(params.id as TemplateId)) notFound();

  const rawData = getTemplate(params.id as TemplateId);
  // Cast to RawTemplate: the actual JSON uses `template_id` and `fields`,
  // both accessible via Template's [key: string]: unknown index signature.
  const template = rawData as unknown as RawTemplate;
  const contextNote = searchParams?.context ?? null;

  return (
    <div className="mx-auto max-w-3xl space-y-8">
      {/* Breadcrumb */}
      <nav className="flex items-center gap-2 text-sm text-slate-500">
        <Link href="/templates" className="hover:text-slate-800">
          Templates
        </Link>
        <span>/</span>
        <span className="text-slate-800">{template.name}</span>
      </nav>

      {/* Context banner — shown when arriving from a Practice Problem */}
      {contextNote && (
        <div className="rounded-lg border border-indigo-200 bg-indigo-50 px-4 py-3 text-sm text-indigo-800">
          <span className="font-semibold">Practice Problem context loaded: </span>
          {contextNote} —{' '}
          <Link
            href={`/practice/problems/${contextNote}`}
            className="underline hover:text-indigo-600"
          >
            View full problem
          </Link>
        </div>
      )}

      {/* Page header */}
      <header className="space-y-2">
        <h1 className="text-2xl font-bold leading-tight text-slate-900">{template.name}</h1>
        {template.print_template_available && (
          <p className="text-xs text-slate-400">Print template available</p>
        )}
      </header>

      {/* The interactive form */}
      <TemplateForm template={template} />
    </div>
  );
}
