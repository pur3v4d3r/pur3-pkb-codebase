/**
 * CSS-only Toulmin argument diagram.
 * Renders the classic DATA → WARRANT → CLAIM flow with BACKING below WARRANT
 * and REBUTTAL / QUALIFIER at bottom.
 */

interface ToulminDiagramProps {
  claim?: string;
  data?: string;
  warrant?: string;
  backing?: string;
  qualifier?: string;
  rebuttal?: string;
}

const CELL_COLORS: Record<string, string> = {
  claim:    'border-indigo-300 bg-indigo-50',
  data:     'border-teal-300 bg-teal-50',
  warrant:  'border-amber-300 bg-amber-50',
  backing:  'border-orange-300 bg-orange-50',
  qualifier:'border-violet-300 bg-violet-50',
  rebuttal: 'border-rose-300 bg-rose-50',
};

const LABEL_COLORS: Record<string, string> = {
  claim:    'text-indigo-700',
  data:     'text-teal-700',
  warrant:  'text-amber-700',
  backing:  'text-orange-700',
  qualifier:'text-violet-700',
  rebuttal: 'text-rose-700',
};

function Cell({
  id,
  label,
  value,
}: {
  id: string;
  label: string;
  value?: string;
}) {
  if (!value) return null;
  return (
    <div className={`rounded-lg border-2 p-3 ${CELL_COLORS[id] ?? 'border-slate-200 bg-white'}`}>
      <p className={`mb-1 text-[10px] font-bold uppercase tracking-widest ${LABEL_COLORS[id] ?? 'text-slate-500'}`}>
        {label}
      </p>
      <p className="text-xs leading-relaxed text-slate-800">{value}</p>
    </div>
  );
}

// Horizontal arrow connector
function Arrow({ label }: { label?: string }) {
  return (
    <div className="flex flex-col items-center justify-center text-slate-400" aria-hidden="true">
      <div className="h-px w-8 bg-slate-300" />
      <div className="relative -mt-1.5 text-xs">▶</div>
      {label && <span className="mt-0.5 text-[9px] text-slate-400">{label}</span>}
    </div>
  );
}

export default function ToulminDiagram({
  claim,
  data,
  warrant,
  backing,
  qualifier,
  rebuttal,
}: ToulminDiagramProps) {
  const hasBacking = !!backing;
  const hasExtended = !!(qualifier || rebuttal);

  return (
    <div className="space-y-4">
      {/* Main row: DATA → WARRANT → CLAIM */}
      <div className="flex flex-wrap items-center gap-2">
        <div className="min-w-[160px] flex-1">
          <Cell id="data" label="Data / Grounds" value={data} />
        </div>
        <Arrow />
        <div className="min-w-[160px] flex-1">
          <Cell id="warrant" label="Warrant" value={warrant} />
        </div>
        <Arrow label="therefore" />
        <div className="min-w-[160px] flex-1">
          <Cell id="claim" label="Claim" value={claim} />
        </div>
      </div>

      {/* Backing below warrant */}
      {hasBacking && (
        <div className="flex items-start gap-2 pl-[calc(50%-80px)] sm:pl-[188px]">
          <div className="flex flex-col items-center">
            <div className="h-4 w-px bg-slate-300" />
            <div className="text-xs text-slate-400">▲</div>
          </div>
          <div className="min-w-[160px] flex-1 max-w-xs">
            <Cell id="backing" label="Backing" value={backing} />
          </div>
        </div>
      )}

      {/* Qualifier and Rebuttal */}
      {hasExtended && (
        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
          <Cell id="qualifier" label="Qualifier (Unless…)" value={qualifier} />
          <Cell id="rebuttal" label="Rebuttal" value={rebuttal} />
        </div>
      )}
    </div>
  );
}
