'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { getPortfolioEntry, deletePortfolioEntry } from '@/lib/storage';
import type { PortfolioEntry } from '@/types/framework';
import type { RawTemplate, RawTemplateField } from '@/components/template/TemplateForm';
import ToulminDiagram from '@/components/argument-map/ToulminDiagram';

interface FieldDisplay {
  fieldId: string;
  label: string;
  type: RawTemplateField['type'];
  value: unknown;
}

function buildFieldDisplays(
  entry: PortfolioEntry,
  template: RawTemplate | null,
): FieldDisplay[] {
  const responses = entry.responses as Record<string, unknown>;

  if (template) {
    // Normalise: templates may use top-level `fields` or `sections[].fields`
    const allFields: RawTemplateField[] =
      template.fields && template.fields.length > 0
        ? template.fields
        : (template.sections ?? []).flatMap((s) => s.fields ?? []);

    return allFields
      .filter((f) => f.field_id in responses)
      .map((f) => ({
        fieldId: f.field_id,
        label: f.label,
        type: f.type,
        value: responses[f.field_id],
      }));
  }

  // Fallback: no template — derive a readable label from the key
  // Handles both snake_case and kebab-case keys, e.g.:
  //   "ennis_seek_and_offer_reasons" → "Ennis Seek And Offer Reasons"
  //   "field-name"                   → "Field Name"
  function keyToLabel(k: string): string {
    return k
      .replace(/[-_]/g, ' ')
      .replace(/\b\w/g, (c) => c.toUpperCase());
  }

  return Object.entries(responses).map(([k, v]) => ({
    fieldId: k,
    label: keyToLabel(k),
    type: typeof v === 'number' ? ('scale' as const) : ('textarea' as const),
    value: v,
  }));
}

function ResponseValue({ type, value }: { type: RawTemplateField['type']; value: unknown }) {
  if (value === null || value === undefined || value === '') {
    return <span className="text-sm italic text-slate-400">No response</span>;
  }

  // Checklist / multiselect — stored as JSON array string
  if (type === 'checklist' || type === 'multiselect') {
    let items: string[] = [];
    try {
      items = typeof value === 'string' ? (JSON.parse(value) as string[]) : (value as string[]);
    } catch {
      items = typeof value === 'string' ? [value] : [];
    }
    if (items.length === 0) {
      return <span className="text-sm italic text-slate-400">No items selected</span>;
    }
    return (
      <ul className="mt-1 space-y-1">
        {items.map((item, i) => (
          <li key={i} className="flex items-start gap-2 text-sm text-slate-700">
            <span className="mt-0.5 flex-shrink-0 text-slate-400">✓</span>
            <span>{item}</span>
          </li>
        ))}
      </ul>
    );
  }

  // Scale — show as a badge
  if (type === 'scale') {
    return (
      <span className="inline-flex h-9 w-9 items-center justify-center rounded-full border border-slate-900 bg-slate-900 text-sm font-semibold text-white">
        {String(value)}
      </span>
    );
  }

  // Select — show as a pill
  if (type === 'select') {
    return (
      <span className="rounded-full bg-slate-100 px-3 py-1 text-sm font-medium text-slate-700">
        {String(value)}
      </span>
    );
  }

  // textarea / text — show as preformatted paragraph
  return (
    <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-700">{String(value)}</p>
  );
}

// ---- Markdown export ----

function fieldValueToMarkdown(type: RawTemplateField['type'], value: unknown): string {
  if (value === null || value === undefined || value === '') return '*No response*';

  if (type === 'checklist' || type === 'multiselect') {
    let items: string[] = [];
    try {
      items = typeof value === 'string' ? (JSON.parse(value) as string[]) : (value as string[]);
    } catch {
      items = typeof value === 'string' ? [value] : [];
    }
    return items.length === 0
      ? '*No items selected*'
      : items.map((item) => `- [x] ${item}`).join('\n');
  }

  if (type === 'scale') return `**${String(value)}**`;

  return String(value);
}

function generateMarkdown(entry: PortfolioEntry, fields: FieldDisplay[]): string {
  const date = new Date(entry.createdAt).toISOString().split('T')[0];
  const tagsYaml = entry.tags.length > 0
    ? `tags: [${entry.tags.map((t) => `portfolio, ${t}`).join(', ')}]`
    : 'tags: [portfolio]';

  const lines: string[] = [
    '---',
    tagsYaml,
    `type: ${entry.type}`,
    `created: ${date}`,
    entry.templateId ? `template_id: ${entry.templateId}` : '',
    entry.chapterRef ? `chapter_ref: ${entry.chapterRef}` : '',
    '---',
    '',
    `# ${entry.title}`,
    '',
  ].filter((l) => l !== null);

  const filled = fields.filter((f) => {
    const v = f.value;
    return v !== null && v !== undefined && v !== '' &&
      !(typeof v === 'string' && v.trim() === '');
  });

  filled.forEach((f, idx) => {
    lines.push(`## ${idx + 1}. ${f.label}`);
    lines.push('');
    lines.push(fieldValueToMarkdown(f.type, f.value));
    lines.push('');
    lines.push('---');
    lines.push('');
  });

  return lines.join('\n');
}

function downloadBlob(content: string, filename: string, mimeType: string) {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.click();
  URL.revokeObjectURL(url);
}

// ---- Page component ----

export default function PortfolioDetailPage({ params }: { params: { id: string } }) {
  const router = useRouter();
  const [entry, setEntry] = useState<PortfolioEntry | null>(null);
  const [template, setTemplate] = useState<RawTemplate | null>(null);
  const [loading, setLoading] = useState(true);
  const [confirmDelete, setConfirmDelete] = useState(false);

  useEffect(() => {
    const found = getPortfolioEntry(params.id);
    if (!found) {
      setLoading(false);
      return;
    }
    setEntry(found);

    // Fetch template for field labels if we have a templateId
    if (found.templateId) {
      fetch(`/data/templates/${found.templateId}.json`)
        .then((r) => (r.ok ? r.json() : null))
        .then((data) => {
          if (data) setTemplate(data as RawTemplate);
        })
        .catch(() => {
          // Template not found — fall back to raw keys
        })
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, [params.id]);

  const handleDelete = () => {
    if (!confirmDelete) {
      setConfirmDelete(true);
      return;
    }
    deletePortfolioEntry(params.id);
    router.push('/portfolio');
  };

  const handleDownload = () => {
    if (!entry) return;
    const fields = buildFieldDisplays(entry, template);
    const md = generateMarkdown(entry, fields);
    // Sanitise title for use as a filename
    const slug = entry.title
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '')
      .slice(0, 80);
    const date = new Date(entry.createdAt).toISOString().split('T')[0];
    downloadBlob(md, `${date}-${slug}.md`, 'text/markdown;charset=utf-8');
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center py-24 text-sm text-slate-400">
        Loading…
      </div>
    );
  }

  if (!entry) {
    return (
      <div className="space-y-4">
        <Link href="/portfolio" className="text-sm text-slate-500 hover:text-slate-800">
          ← Portfolio
        </Link>
        <div className="rounded-lg border border-dashed border-slate-300 bg-white p-12 text-center">
          <p className="text-sm text-slate-500">Entry not found.</p>
          <p className="mt-1 text-xs text-slate-400">
            It may have been deleted or the link is incorrect.
          </p>
        </div>
      </div>
    );
  }

  const fields = buildFieldDisplays(entry, template);
  const filledFields = fields.filter((f) => {
    const v = f.value;
    if (v === null || v === undefined || v === '') return false;
    if (typeof v === 'string' && v.trim() === '') return false;
    return true;
  });

  const typeColors: Record<string, string> = {
    template: 'bg-indigo-100 text-indigo-800',
    exercise: 'bg-green-100 text-green-800',
    reflection: 'bg-amber-100 text-amber-800',
  };

  return (
    <div className="mx-auto max-w-3xl space-y-8">
      {/* Breadcrumb */}
      <nav className="flex items-center gap-2 text-sm text-slate-500">
        <Link href="/portfolio" className="hover:text-slate-800">
          Portfolio
        </Link>
        <span>/</span>
        <span className="line-clamp-1 text-slate-800">{entry.title}</span>
      </nav>

      {/* Header card */}
      <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
        <div className="flex flex-wrap items-start justify-between gap-3">
          <div className="space-y-1.5">
            <h1 className="text-xl font-bold tracking-tight text-slate-900">{entry.title}</h1>
            <div className="flex flex-wrap items-center gap-2 text-xs text-slate-500">
              <span className={`rounded-full px-2.5 py-0.5 font-medium ${typeColors[entry.type] ?? 'bg-slate-100 text-slate-700'}`}>
                {entry.type}
              </span>
              <span>Saved {new Date(entry.createdAt).toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}</span>
              {entry.chapterRef && <span>Chapter {entry.chapterRef}</span>}
              {entry.tags.length > 0 &&
                entry.tags.map((tag) => (
                  <span key={tag} className="rounded-full bg-slate-100 px-2 py-0.5 text-slate-600">
                    #{tag}
                  </span>
                ))}
            </div>
          </div>

          {/* Action buttons */}
          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={handleDownload}
              title="Download as Markdown"
              className="rounded-lg border border-slate-200 bg-white px-3 py-1.5 text-xs font-medium text-slate-600 transition hover:border-slate-300 hover:bg-slate-50"
            >
              ↓ Download .md
            </button>
            {confirmDelete && (
              <span className="text-xs text-red-600">Are you sure?</span>
            )}
            <button
              type="button"
              onClick={handleDelete}
              className={`rounded-lg border px-3 py-1.5 text-xs font-medium transition ${
                confirmDelete
                  ? 'border-red-300 bg-red-50 text-red-700 hover:bg-red-100'
                  : 'border-slate-200 bg-white text-slate-500 hover:border-slate-300 hover:text-red-600'
              }`}
            >
              {confirmDelete ? 'Confirm delete' : 'Delete'}
            </button>
            {confirmDelete && (
              <button
                type="button"
                onClick={() => setConfirmDelete(false)}
                className="text-xs text-slate-400 hover:text-slate-600"
              >
                Cancel
              </button>
            )}
          </div>
        </div>
        {/* end action buttons */}

        {/* Progress summary */}
        {fields.length > 0 && (
          <div className="mt-5">
            <div className="flex items-center justify-between text-xs text-slate-400">
              <span>{filledFields.length} of {fields.length} fields filled</span>
              <span>{Math.round((filledFields.length / fields.length) * 100)}%</span>
            </div>
            <div className="mt-1.5 h-1.5 w-full rounded-full bg-slate-200">
              <div
                className="h-1.5 rounded-full bg-slate-700 transition-all"
                style={{ width: `${Math.round((filledFields.length / fields.length) * 100)}%` }}
              />
            </div>
          </div>
        )}
      </div>

      {/* Toulmin Argument Diagram */}
      {entry.templateId === 'toulmin-map' && (() => {
        const r = entry.responses as Record<string, string>;
        return (
          <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
            <h2 className="mb-4 text-xs font-semibold uppercase tracking-widest text-slate-500">
              Argument Structure
            </h2>
            <ToulminDiagram
              claim={r.claim}
              data={r.data}
              warrant={r.warrant}
              backing={r.backing}
              qualifier={r.qualifier}
              rebuttal={r.rebuttal}
            />
          </div>
        );
      })()}

      {/* Field responses */}
      {filledFields.length === 0 ? (
        <div className="rounded-lg border border-dashed border-slate-300 bg-white p-8 text-center">
          <p className="text-sm text-slate-500">No responses were saved in this entry.</p>
        </div>
      ) : (
        <div className="space-y-4">
          {filledFields.map((f, idx) => (
            <div key={f.fieldId} className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
              <div className="mb-3 flex items-center gap-2">
                <span className="flex h-6 w-6 flex-shrink-0 items-center justify-center rounded-full bg-slate-900 text-xs font-bold text-white">
                  {idx + 1}
                </span>
                <h2 className="text-base font-semibold text-slate-900">{f.label}</h2>
              </div>
              <ResponseValue type={f.type} value={f.value} />
            </div>
          ))}
        </div>
      )}

      {/* Footer nav */}
      <div className="pb-8">
        <Link
          href="/portfolio"
          className="text-sm text-slate-500 hover:text-slate-800"
        >
          ← Back to Portfolio
        </Link>
      </div>
    </div>
  );
}
