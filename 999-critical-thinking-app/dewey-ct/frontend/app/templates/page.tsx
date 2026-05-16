export default function TemplatesPage() {
  const templates = [
    { id: 'dewey-reflective-v1', name: 'Dewey Reflective Thinking', desc: 'Five-phase inquiry scaffold based on Chapter 6 of How We Think' },
    { id: 'argument-analysis-v1', name: 'Argument Analysis', desc: 'Toulmin-based structure for dissecting arguments' },
    { id: 'blooms-scaffold-v1', name: "Bloom's Scaffold", desc: 'Progressive questioning from recall to synthesis and evaluation' },
    { id: 'socratic-questioning-v1', name: 'Socratic Questioning', desc: 'Six-type question protocol for guided inquiry' },
    { id: 'paul-elder-analysis-v1', name: 'Paul-Elder Analysis', desc: 'Eight elements of reasoning with intellectual standards' },
  ];

  return (
    <div className="space-y-6">
      <div className="space-y-1">
        <h1 className="text-2xl font-bold tracking-tight text-slate-900">Thinking Templates</h1>
        <p className="text-sm text-slate-500">
          Structured worksheets for applying critical-thinking frameworks to real problems
        </p>
      </div>

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
        {templates.map((t) => (
          <div key={t.id} className="rounded-lg border border-slate-200 bg-white p-5 shadow-sm">
            <h2 className="mb-1 text-base font-semibold text-slate-900">{t.name}</h2>
            <p className="text-sm leading-relaxed text-slate-600">{t.desc}</p>
            <p className="mt-3 text-xs text-slate-400">Interactive form coming soon</p>
          </div>
        ))}
      </div>
    </div>
  );
}
