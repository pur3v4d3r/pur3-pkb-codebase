'use client';

import type {
  Callout,
  QuoteCallout,
  ConceptCallout,
  WarningCallout,
  TipCallout,
  SynthesisCallout,
} from '@/types/chapter';

interface CalloutRendererProps {
  callout: Callout;
}

export default function CalloutRenderer({ callout }: CalloutRendererProps) {
  switch (callout.type) {
    case 'quote':
      return <QuoteBlock callout={callout} />;
    case 'concept':
      return <ConceptBlock callout={callout} />;
    case 'warning':
      return <WarningBlock callout={callout} />;
    case 'tip':
      return <TipBlock callout={callout} />;
    case 'synthesis':
      return <SynthesisBlock callout={callout} />;
  }
}

function QuoteBlock({ callout }: { callout: QuoteCallout }) {
  return (
    <aside className="my-6 rounded-lg border-l-4 border-amber-400 bg-amber-50 p-5">
      <blockquote className="mb-3 text-base italic leading-relaxed text-slate-800">
        &ldquo;{callout.quote}&rdquo;
      </blockquote>
      <p className="text-sm leading-relaxed text-slate-600">{callout.insight}</p>
    </aside>
  );
}

function ConceptBlock({ callout }: { callout: ConceptCallout }) {
  return (
    <aside className="my-6 rounded-lg border border-blue-200 bg-blue-50 p-5">
      <div className="mb-1 flex items-center gap-2">
        <span className="rounded bg-blue-700 px-2 py-0.5 text-xs font-bold uppercase tracking-wide text-white">
          Concept
        </span>
        <h3 className="font-semibold text-slate-900">{callout.concept_name}</h3>
      </div>
      <p className="mb-3 text-sm leading-relaxed text-slate-700">{callout.definition}</p>
      <div className="mb-2">
        <span className="text-xs font-semibold uppercase tracking-wide text-blue-700">Why it matters</span>
        <p className="mt-1 text-sm leading-relaxed text-slate-600">{callout.why_it_matters}</p>
      </div>
      <div>
        <span className="text-xs font-semibold uppercase tracking-wide text-blue-700">Modern echo</span>
        <p className="mt-1 text-sm italic leading-relaxed text-slate-500">{callout.modern_echo}</p>
      </div>
    </aside>
  );
}

function WarningBlock({ callout }: { callout: WarningCallout }) {
  return (
    <aside className="my-6 rounded-lg border border-red-200 bg-red-50 p-5">
      <div className="mb-3 flex items-center gap-2">
        <span className="rounded bg-red-600 px-2 py-0.5 text-xs font-bold uppercase tracking-wide text-white">
          Common Misconception
        </span>
      </div>
      <p className="mb-2 text-sm font-medium text-red-800">{callout.misconception}</p>
      <div className="mb-2">
        <span className="text-xs font-semibold uppercase tracking-wide text-red-700">Correction</span>
        <p className="mt-1 text-sm leading-relaxed text-slate-700">{callout.correction}</p>
      </div>
      <div className="rounded bg-red-100 p-2 text-xs text-red-700">
        <strong>Still relevant:</strong> {callout.still_relevant}
      </div>
    </aside>
  );
}

function TipBlock({ callout }: { callout: TipCallout }) {
  return (
    <aside className="my-6 rounded-lg border border-emerald-200 bg-emerald-50 p-5">
      <div className="mb-2 flex items-center gap-2">
        <span className="rounded bg-emerald-700 px-2 py-0.5 text-xs font-bold uppercase tracking-wide text-white">
          Practical Tip
        </span>
      </div>
      <p className="mb-3 text-sm font-semibold leading-relaxed text-slate-800">{callout.principle}</p>
      <div>
        <span className="text-xs font-semibold uppercase tracking-wide text-emerald-700">In practice</span>
        <p className="mt-1 text-sm leading-relaxed text-slate-600">{callout.in_practice}</p>
      </div>
    </aside>
  );
}

function SynthesisBlock({ callout }: { callout: SynthesisCallout }) {
  return (
    <aside className="my-8 rounded-lg border-2 border-slate-300 bg-slate-50 p-6">
      <div className="mb-3 flex items-center gap-2">
        <span className="rounded bg-slate-800 px-2 py-0.5 text-xs font-bold uppercase tracking-wide text-white">
          Chapter Synthesis
        </span>
      </div>
      <p className="mb-4 text-sm leading-relaxed text-slate-700">{callout.central_argument}</p>
      {callout.logical_progression.length > 0 && (
        <div className="mb-4">
          <span className="text-xs font-semibold uppercase tracking-wide text-slate-500">Logical Progression</span>
          <ol className="mt-2 list-decimal pl-5 space-y-1">
            {callout.logical_progression.map((step, i) => (
              <li key={i} className="text-sm leading-relaxed text-slate-600">{step}</li>
            ))}
          </ol>
        </div>
      )}
      {callout.bridge_to_next && (
        <div className="rounded bg-slate-200 p-3 text-sm italic text-slate-600">
          <strong>Next:</strong> {callout.bridge_to_next}
        </div>
      )}
    </aside>
  );
}
