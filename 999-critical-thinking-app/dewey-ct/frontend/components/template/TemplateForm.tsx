'use client';

import { useState, useCallback } from 'react';
import { savePortfolioEntry, generateId } from '@/lib/storage';
import { requestFeedback, type FeedbackResponse } from '@/lib/api';
import type { PortfolioEntry } from '@/types/framework';

// ---- Local types that match the actual JSON schema ----

export interface RawTemplateField {
  field_id: string;
  phase?: number;
  label: string;
  type: 'textarea' | 'text' | 'select' | 'multiselect' | 'scale' | 'checklist';
  placeholder?: string;
  example?: string;
  minimum_words?: number;
  hint?: string;
  options?: string[];
  required?: boolean;
  min?: number;
  max?: number;
  llm_evaluation_criterion?: string;
}

export interface RawTemplate {
  template_id: string;
  name: string;
  description: string;
  framework?: string;
  difficulty?: string;
  estimated_time_minutes?: number;
  recommended_chapter?: number;
  print_template_available?: boolean;
  fields?: RawTemplateField[];
  // Some templates may use sections instead
  sections?: Array<{ id: string; title: string; description?: string; fields: RawTemplateField[] }>;
}

// ---- Field renderer sub-components ----

function wordCount(text: string): number {
  return text.trim() === '' ? 0 : text.trim().split(/\s+/).length;
}

interface TextAreaFieldProps {
  field: RawTemplateField;
  value: string;
  onChange: (v: string) => void;
}

function TextAreaField({ field, value, onChange }: TextAreaFieldProps) {
  const wc = wordCount(value);
  const min = field.minimum_words;
  const tooShort = min !== undefined && value.trim() !== '' && wc < min;

  return (
    <div className="space-y-1.5">
      <textarea
        id={field.field_id}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={field.placeholder ?? ''}
        rows={7}
        className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2.5 text-sm leading-relaxed text-slate-800 shadow-sm placeholder:text-slate-400 focus:border-slate-500 focus:outline-none focus:ring-2 focus:ring-slate-200"
      />
      {min !== undefined && (
        <p className={`text-xs ${tooShort ? 'text-amber-600' : 'text-slate-400'}`}>
          {wc} / {min} words minimum
          {!tooShort && wc > 0 && ' ✓'}
        </p>
      )}
    </div>
  );
}

interface TextFieldProps {
  field: RawTemplateField;
  value: string;
  onChange: (v: string) => void;
}

function TextField({ field, value, onChange }: TextFieldProps) {
  return (
    <input
      id={field.field_id}
      type="text"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={field.placeholder ?? ''}
      className="w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm text-slate-800 shadow-sm placeholder:text-slate-400 focus:border-slate-500 focus:outline-none focus:ring-2 focus:ring-slate-200"
    />
  );
}

interface ScaleFieldProps {
  field: RawTemplateField;
  value: string;
  onChange: (v: string) => void;
}

function ScaleField({ field, value, onChange }: ScaleFieldProps) {
  const min = field.min ?? 1;
  const max = field.max ?? 5;
  const options = Array.from({ length: max - min + 1 }, (_, i) => min + i);
  const selected = parseInt(value, 10);

  return (
    <div className="flex items-center gap-2">
      {options.map((n) => (
        <button
          key={n}
          type="button"
          onClick={() => onChange(String(n))}
          className={`h-9 w-9 rounded-full border text-sm font-medium transition ${
            selected === n
              ? 'border-slate-900 bg-slate-900 text-white'
              : 'border-slate-300 bg-white text-slate-600 hover:border-slate-500'
          }`}
        >
          {n}
        </button>
      ))}
    </div>
  );
}

interface SelectFieldProps {
  field: RawTemplateField;
  value: string;
  onChange: (v: string) => void;
}

function SelectField({ field, value, onChange }: SelectFieldProps) {
  return (
    <select
      id={field.field_id}
      value={value}
      onChange={(e) => onChange(e.target.value)}
      className="rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm text-slate-800 shadow-sm focus:border-slate-500 focus:outline-none focus:ring-2 focus:ring-slate-200"
    >
      <option value="">Select…</option>
      {field.options?.map((opt) => (
        <option key={opt} value={opt}>{opt}</option>
      ))}
    </select>
  );
}

interface ChecklistFieldProps {
  field: RawTemplateField;
  value: string; // JSON array of selected items
  onChange: (v: string) => void;
}

function ChecklistField({ field, value, onChange }: ChecklistFieldProps) {
  const selected: string[] = (() => {
    try { return JSON.parse(value) as string[]; } catch { return []; }
  })();

  function toggle(opt: string) {
    const next = selected.includes(opt)
      ? selected.filter((s) => s !== opt)
      : [...selected, opt];
    onChange(JSON.stringify(next));
  }

  return (
    <div className="space-y-2">
      {field.options?.map((opt) => (
        <label key={opt} className="flex cursor-pointer items-start gap-2.5">
          <input
            type="checkbox"
            checked={selected.includes(opt)}
            onChange={() => toggle(opt)}
            className="mt-0.5 h-4 w-4 flex-shrink-0 rounded border-slate-300 text-slate-900 focus:ring-slate-200"
          />
          <span className="text-sm leading-relaxed text-slate-700">{opt}</span>
        </label>
      ))}
    </div>
  );
}

// ---- AI Feedback display ----

interface FeedbackPanelProps {
  feedback: FeedbackResponse;
  onDismiss: () => void;
}

function FeedbackPanel({ feedback, onDismiss }: FeedbackPanelProps) {
  return (
    <div className="mt-3 rounded-lg border border-blue-200 bg-blue-50 p-4 text-sm">
      <div className="flex items-center justify-between gap-2">
        <span className="font-semibold text-blue-900">AI Feedback</span>
        <div className="flex items-center gap-3">
          {feedback.score !== undefined && (
            <span className="rounded-full bg-blue-200 px-2.5 py-0.5 text-xs font-semibold text-blue-900">
              {feedback.score}/10
            </span>
          )}
          <button
            type="button"
            onClick={onDismiss}
            className="text-xs text-blue-500 hover:text-blue-700"
          >
            dismiss
          </button>
        </div>
      </div>
      <p className="mt-2 leading-relaxed text-blue-900">{feedback.feedback}</p>
      {feedback.suggestions.length > 0 && (
        <ul className="mt-3 space-y-1">
          {feedback.suggestions.map((s, i) => (
            <li key={i} className="flex items-start gap-2 text-blue-800">
              <span className="mt-0.5 flex-shrink-0 text-blue-400">→</span>
              <span>{s}</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

// ---- Main TemplateForm component ----

interface TemplateFormProps {
  template: RawTemplate;
}

export default function TemplateForm({ template }: TemplateFormProps) {
  // Normalise: support both top-level `fields` and `sections[].fields`
  const allFields: RawTemplateField[] = (() => {
    if (template.fields && template.fields.length > 0) return template.fields;
    if (template.sections) {
      return template.sections.flatMap((s) => s.fields ?? []);
    }
    return [];
  })();

  const [responses, setResponses] = useState<Record<string, string>>(() =>
    Object.fromEntries(allFields.map((f) => [f.field_id, '']))
  );
  const [showExample, setShowExample] = useState<Record<string, boolean>>({});
  const [feedbackMap, setFeedbackMap] = useState<Record<string, FeedbackResponse>>({});
  const [loadingField, setLoadingField] = useState<string | null>(null);
  const [saved, setSaved] = useState(false);
  const [saveError, setSaveError] = useState<string | null>(null);
  const [apiError, setApiError] = useState<Record<string, string>>({});

  const handleChange = useCallback((fieldId: string, value: string) => {
    setResponses((prev) => ({ ...prev, [fieldId]: value }));
    setSaved(false);
  }, []);

  const toggleExample = (fieldId: string) => {
    setShowExample((prev) => ({ ...prev, [fieldId]: !prev[fieldId] }));
  };

  const handleFeedback = async (field: RawTemplateField) => {
    const text = responses[field.field_id] ?? '';
    if (text.trim().length < 20) {
      setApiError((prev) => ({ ...prev, [field.field_id]: 'Write at least a few sentences before requesting feedback.' }));
      return;
    }
    setLoadingField(field.field_id);
    setApiError((prev) => ({ ...prev, [field.field_id]: '' }));
    try {
      const result = await requestFeedback({
        template_id: template.template_id,
        field_id: field.field_id,
        response_text: text,
        framework_context: field.llm_evaluation_criterion,
      });
      setFeedbackMap((prev) => ({ ...prev, [field.field_id]: result }));
    } catch {
      setApiError((prev) => ({
        ...prev,
        [field.field_id]: 'Could not reach the AI backend. Is the server running at localhost:8000?',
      }));
    } finally {
      setLoadingField(null);
    }
  };

  const dismissFeedback = (fieldId: string) => {
    setFeedbackMap((prev) => {
      const next = { ...prev };
      delete next[fieldId];
      return next;
    });
  };

  const handleSave = () => {
    try {
      const entry: PortfolioEntry = {
        id: generateId(),
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        type: 'template',
        title: `${template.name} — ${new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}`,
        templateId: template.template_id,
        chapterRef: template.recommended_chapter,
        responses,
        tags: template.framework ? [template.framework.toLowerCase().replace(/\s+/g, '-')] : [],
      };
      savePortfolioEntry(entry);
      setSaved(true);
      setSaveError(null);
    } catch {
      setSaveError('Failed to save. Check browser storage permissions.');
    }
  };

  const filledCount = allFields.filter((f) => (responses[f.field_id] ?? '').trim() !== '').length;
  const progressPct = allFields.length > 0 ? Math.round((filledCount / allFields.length) * 100) : 0;

  const difficultyColors: Record<string, string> = {
    beginner: 'bg-green-100 text-green-800',
    intermediate: 'bg-yellow-100 text-yellow-800',
    advanced: 'bg-red-100 text-red-800',
  };

  return (
    <div className="space-y-8">
      {/* Template meta header */}
      <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
        <div className="flex flex-wrap items-center gap-2 text-xs text-slate-500">
          {template.framework && (
            <span className="rounded-full bg-slate-100 px-2.5 py-0.5 font-medium text-slate-700">
              {template.framework}
            </span>
          )}
          {template.difficulty && (
            <span className={`rounded-full px-2.5 py-0.5 font-medium ${difficultyColors[template.difficulty] ?? 'bg-slate-100 text-slate-700'}`}>
              {template.difficulty}
            </span>
          )}
          {template.estimated_time_minutes && (
            <span>~{template.estimated_time_minutes} min</span>
          )}
          {template.recommended_chapter && (
            <span>Recommended after Chapter {template.recommended_chapter}</span>
          )}
        </div>
        <p className="mt-4 text-sm leading-relaxed text-slate-600">{template.description}</p>

        {/* Progress bar */}
        <div className="mt-5">
          <div className="flex items-center justify-between text-xs text-slate-400">
            <span>{filledCount} of {allFields.length} fields filled</span>
            <span>{progressPct}%</span>
          </div>
          <div className="mt-1.5 h-1.5 w-full rounded-full bg-slate-200">
            <div
              className="h-1.5 rounded-full bg-slate-700 transition-all duration-300"
              style={{ width: `${progressPct}%` }}
            />
          </div>
        </div>
      </div>

      {/* Fields */}
      {allFields.map((field, idx) => (
        <fieldset key={field.field_id} className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
          <legend className="sr-only">{field.label}</legend>

          {/* Field header */}
          <div className="mb-4 flex items-start justify-between gap-3">
            <div>
              <div className="flex items-center gap-2">
                {field.phase !== undefined && (
                  <span className="flex h-6 w-6 flex-shrink-0 items-center justify-center rounded-full bg-slate-900 text-xs font-bold text-white">
                    {field.phase}
                  </span>
                )}
                <label htmlFor={field.field_id} className="text-base font-semibold text-slate-900 cursor-pointer">
                  {field.label}
                </label>
              </div>
            </div>
            <span className="flex-shrink-0 text-xs text-slate-400">
              Field {idx + 1} of {allFields.length}
            </span>
          </div>

          {/* Hint */}
          {field.hint && (
            <div className="mb-4 rounded-md border-l-2 border-slate-300 bg-slate-50 px-4 py-2.5 text-xs leading-relaxed text-slate-600">
              {field.hint}
            </div>
          )}

          {/* Input */}
          {(field.type === 'textarea' || field.type === undefined) && (
            <TextAreaField
              field={field}
              value={responses[field.field_id] ?? ''}
              onChange={(v) => handleChange(field.field_id, v)}
            />
          )}
          {field.type === 'text' && (
            <TextField
              field={field}
              value={responses[field.field_id] ?? ''}
              onChange={(v) => handleChange(field.field_id, v)}
            />
          )}
          {field.type === 'scale' && (
            <ScaleField
              field={field}
              value={responses[field.field_id] ?? ''}
              onChange={(v) => handleChange(field.field_id, v)}
            />
          )}
          {field.type === 'select' && (
            <SelectField
              field={field}
              value={responses[field.field_id] ?? ''}
              onChange={(v) => handleChange(field.field_id, v)}
            />
          )}
          {(field.type === 'checklist' || field.type === 'multiselect') && (
            <ChecklistField
              field={field}
              value={responses[field.field_id] ?? ''}
              onChange={(v) => handleChange(field.field_id, v)}
            />
          )}

          {/* Action row */}
          <div className="mt-3 flex flex-wrap items-center gap-3">
            {field.example && (
              <button
                type="button"
                onClick={() => toggleExample(field.field_id)}
                className="text-xs font-medium text-slate-500 underline-offset-2 hover:text-slate-800 hover:underline"
              >
                {showExample[field.field_id] ? 'Hide example' : 'Show example'}
              </button>
            )}
            {field.llm_evaluation_criterion && (
              <button
                type="button"
                onClick={() => handleFeedback(field)}
                disabled={loadingField === field.field_id}
                className="inline-flex items-center gap-1.5 rounded-md border border-blue-200 bg-blue-50 px-3 py-1 text-xs font-medium text-blue-700 transition hover:bg-blue-100 disabled:opacity-50"
              >
                {loadingField === field.field_id ? (
                  <>
                    <svg className="h-3 w-3 animate-spin" viewBox="0 0 24 24" fill="none">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z" />
                    </svg>
                    Thinking…
                  </>
                ) : (
                  'Get AI Feedback'
                )}
              </button>
            )}
          </div>

          {/* Example block */}
          {showExample[field.field_id] && field.example && (
            <div className="mt-4 rounded-lg border border-slate-200 bg-slate-50 px-4 py-3">
              <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-slate-400">Example</p>
              <p className="whitespace-pre-line text-xs leading-relaxed text-slate-600">{field.example}</p>
            </div>
          )}

          {/* API error */}
          {apiError[field.field_id] && (
            <p className="mt-2 text-xs text-red-600">{apiError[field.field_id]}</p>
          )}

          {/* AI feedback */}
          {feedbackMap[field.field_id] && (
            <FeedbackPanel
              feedback={feedbackMap[field.field_id]}
              onDismiss={() => dismissFeedback(field.field_id)}
            />
          )}
        </fieldset>
      ))}

      {/* Save button */}
      <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <p className="text-sm font-medium text-slate-700">Save to Portfolio</p>
            <p className="text-xs text-slate-400">
              Saves your responses to your browser&apos;s local storage.
            </p>
          </div>
          <button
            type="button"
            onClick={handleSave}
            className="inline-flex items-center gap-2 rounded-lg bg-slate-900 px-4 py-2 text-sm font-semibold text-white transition hover:bg-slate-700 active:scale-95"
          >
            {saved ? (
              <>
                <svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                </svg>
                Saved
              </>
            ) : (
              'Save to Portfolio'
            )}
          </button>
        </div>
        {saveError && <p className="mt-2 text-xs text-red-600">{saveError}</p>}
        {saved && (
          <p className="mt-2 text-xs text-slate-500">
            Entry saved to your portfolio. <a href="/portfolio" className="font-medium text-slate-800 underline">View portfolio →</a>
          </p>
        )}
      </div>
    </div>
  );
}
