'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { generateId, savePortfolioEntry } from '@/lib/storage';

// ---- Toulmin field definitions ----

const FIELDS: Array<{
  id: string;
  label: string;
  question: string;
  placeholder: string;
  required: boolean;
  color: string;
}> = [
  {
    id: 'claim',
    label: 'Claim',
    question: 'What is being asserted?',
    placeholder: 'e.g. "We should adopt a four-day work week."',
    required: true,
    color: 'border-indigo-300 bg-indigo-50 focus:ring-indigo-400',
  },
  {
    id: 'data',
    label: 'Data / Grounds',
    question: 'What evidence supports the claim?',
    placeholder: 'e.g. "Studies show 32-hr employees report 20% higher productivity…"',
    required: true,
    color: 'border-teal-300 bg-teal-50 focus:ring-teal-400',
  },
  {
    id: 'warrant',
    label: 'Warrant',
    question: 'Why does the data logically lead to the claim?',
    placeholder: 'e.g. "If productivity rises, reducing hours is cost-neutral for employers."',
    required: true,
    color: 'border-amber-300 bg-amber-50 focus:ring-amber-400',
  },
  {
    id: 'backing',
    label: 'Backing',
    question: 'What supports the warrant itself?',
    placeholder: 'e.g. "Multiple meta-analyses confirm the productivity–hours relationship across industries."',
    required: false,
    color: 'border-orange-300 bg-orange-50 focus:ring-orange-400',
  },
  {
    id: 'qualifier',
    label: 'Qualifier',
    question: 'How strong is the claim? (Unless…)',
    placeholder: 'e.g. "Probably, for knowledge workers — unless roles require continuous coverage."',
    required: false,
    color: 'border-violet-300 bg-violet-50 focus:ring-violet-400',
  },
  {
    id: 'rebuttal',
    label: 'Rebuttal',
    question: 'What are the strongest objections?',
    placeholder: 'e.g. "Some industries (healthcare, manufacturing) require shift coverage that cannot be compressed."',
    required: false,
    color: 'border-rose-300 bg-rose-50 focus:ring-rose-400',
  },
];

export default function ArgumentMapNewPage() {
  const router = useRouter();
  const [title, setTitle] = useState('');
  const [values, setValues] = useState<Record<string, string>>({});
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');

  function handleChange(id: string, value: string) {
    setValues((v) => ({ ...v, [id]: value }));
  }

  function handleSave() {
    // Validate required fields
    const missing = FIELDS.filter((f) => f.required && !values[f.id]?.trim());
    if (missing.length > 0) {
      setError(`Required: ${missing.map((f) => f.label).join(', ')}`);
      return;
    }
    if (!title.trim()) {
      setError('Please add a title for this argument map.');
      return;
    }
    setError('');
    setSaving(true);

    const now = new Date().toISOString();
    const id = generateId();
    savePortfolioEntry({
      id,
      createdAt: now,
      updatedAt: now,
      type: 'template',
      title: title.trim(),
      templateId: 'toulmin-map',
      responses: { ...values },
      tags: ['argument-map', 'toulmin'],
    });

    router.push(`/portfolio/${id}`);
  }

  return (
    <div className="mx-auto max-w-2xl space-y-8">
      {/* Header */}
      <div>
        <nav className="mb-2 text-xs text-slate-400">
          <a href="/practice" className="hover:text-slate-700">Practice</a>
          <span className="mx-1">/</span>
          <span className="text-slate-700">Argument Map</span>
        </nav>
        <h1 className="text-2xl font-bold text-slate-900">Argument Map Builder</h1>
        <p className="mt-1 text-sm text-slate-500">
          Build a Toulmin argument structure — fill in Claim, Data, and Warrant (required).
          Backing, Qualifier, and Rebuttal deepen the analysis. Saved to your portfolio.
        </p>
      </div>

      {/* Title */}
      <div>
        <label className="mb-1 block text-xs font-semibold uppercase tracking-wide text-slate-500">
          Map title
        </label>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder='e.g. "Argument for four-day work week"'
          className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm text-slate-900 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-400"
        />
      </div>

      {/* Fields */}
      {FIELDS.map((field) => (
        <div key={field.id}>
          <div className="mb-1 flex items-center justify-between">
            <label className="text-sm font-semibold text-slate-800">
              {field.label}
              {field.required && <span className="ml-0.5 text-red-500">*</span>}
            </label>
            <span className="text-xs text-slate-400 italic">{field.question}</span>
          </div>
          <textarea
            value={values[field.id] ?? ''}
            onChange={(e) => handleChange(field.id, e.target.value)}
            placeholder={field.placeholder}
            rows={3}
            className={`w-full rounded-lg border px-3 py-2 text-sm text-slate-900 placeholder-slate-400 focus:outline-none focus:ring-2 ${field.color}`}
          />
        </div>
      ))}

      {/* Error */}
      {error && (
        <p className="rounded-lg border border-red-200 bg-red-50 px-4 py-2 text-sm text-red-700">
          {error}
        </p>
      )}

      {/* Actions */}
      <div className="flex items-center gap-3 border-t border-slate-200 pt-4">
        <button
          type="button"
          onClick={handleSave}
          disabled={saving}
          className="rounded-lg bg-indigo-600 px-5 py-2 text-sm font-semibold text-white transition hover:bg-indigo-700 disabled:opacity-60"
        >
          {saving ? 'Saving…' : 'Save to Portfolio'}
        </button>
        <a
          href="/practice"
          className="text-sm font-medium text-slate-500 hover:text-slate-800"
        >
          Cancel
        </a>
        <span className="ml-auto text-xs text-slate-400">Claim, Data, Warrant required</span>
      </div>
    </div>
  );
}
