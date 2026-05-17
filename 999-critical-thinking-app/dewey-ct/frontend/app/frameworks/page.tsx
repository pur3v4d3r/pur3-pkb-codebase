import Link from 'next/link';

export default function FrameworksPage() {
  const frameworks = [
    { id: 'paul-elder', name: 'Paul-Elder', desc: 'Elements of Reasoning and Intellectual Standards' },
    { id: 'blooms-taxonomy', name: "Bloom's Taxonomy", desc: 'Revised cognitive taxonomy with 6 levels' },
    { id: 'socratic-questioning', name: 'Socratic Questioning', desc: 'Six types of probing questions for deep inquiry' },
    { id: 'toulmin-argument', name: 'Toulmin Argument', desc: 'Claim, Data, Warrant, Backing, Qualifier, Rebuttal' },
    { id: 'mental-models', name: 'Mental Models', desc: 'Latticework of multi-disciplinary thinking tools' },
    { id: 'logical-fallacies', name: 'Logical Fallacies', desc: 'Formal and informal fallacy catalogue' },
    { id: 'dewey-five-phases', name: "Dewey's Five Phases", desc: 'Complete reflective thinking process model' },
    { id: 'ennis-framework', name: 'Ennis FRISCO', desc: 'Streamlined conception with 12 abilities and 14 dispositions' },
    { id: 'delphi-consensus', name: 'Delphi / Facione', desc: 'APA consensus model: 6 core skills + CCTDI dispositions' },
    { id: 'dual-process-theory', name: 'Dual-Process Theory', desc: 'System 1 / System 2 with Stanovich tripartite model' },
    { id: 'habits-of-mind', name: "Costa & Kallick's Habits of Mind", desc: '16 intelligent behaviors for disciplined thinking' },
    { id: 'browne-keeley', name: 'Browne-Keeley 10 Questions', desc: 'Practical critical reading protocol' },
    { id: 'paul-elder-enrichments', name: 'Paul-Elder Enrichments', desc: 'SEE-I method, 7 stages of development, Socratic question banks' },
    { id: 'acer-critical-thinking', name: 'ACER Critical Thinking', desc: 'Australian standards-based assessment framework' },
    { id: 'acer-metacognitive', name: 'ACER Metacognitive', desc: 'Metacognitive skills and self-regulation framework' },
    { id: 'developmental-models', name: 'Developmental Models', desc: "Perry's Scheme, King-Kitchener's Reflective Judgment, and Kuhn's Epistemological Levels" },
    { id: 'cognitive-biases', name: 'Cognitive Biases', desc: 'Systematic reasoning errors with counter-strategies; grounded in dual-process theory' },
    { id: 'cross-framework-synthesis', name: 'Cross-Framework Synthesis', desc: 'Convergence and divergence analysis across all major CT frameworks, with developmental mapping' },
    { id: 'siegel-reasons-conception', name: "Siegel's Reasons Conception", desc: 'Two-component model: reason assessment + critical spirit; philosophy-grounded CT definition' },
    { id: 'halpern-critical-thinking', name: "Halpern's Four-Component Framework", desc: 'Dispositions, structural knowledge, skill, metacognition; designed for transfer' },
    { id: 'webbs-depth-of-knowledge', name: "Webb's Depth of Knowledge (DOK)", desc: 'Four levels of cognitive demand for task and assessment alignment' },
    { id: 'marzano-new-taxonomy', name: "Marzano's New Taxonomy", desc: 'Self-System, Metacognitive System, and Cognitive System; explains why skills are not deployed' },
    { id: 'solo-taxonomy', name: 'SOLO Taxonomy', desc: 'Five levels of response complexity: pre-structural through extended abstract' },
    { id: 'watson-glaser', name: 'Watson-Glaser Appraisal', desc: 'Five CT subtests + RED model; oldest validated CT assessment' },
    { id: 'cctdi', name: 'CCTDI Disposition Inventory', desc: 'Seven CT dispositions: truth-seeking, open-mindedness, analyticity, systematicity, and more' },
    { id: 'walton-argumentation-schemes', name: "Walton's Argumentation Schemes", desc: 'Presumptive reasoning patterns with critical questions for evaluation' },
    { id: 'lipman-community-of-inquiry', name: "Lipman's Community of Inquiry", desc: 'Multidimensional thinking (critical + creative + caring) and P4C pedagogy' },
    { id: 'brookfield-critical-thinking', name: "Brookfield's Assumption Hunting", desc: 'CT as surfacing paradigmatic, prescriptive, and causal assumptions; emancipatory approach' },
    { id: 'dikw-pyramid', name: 'DIKW Pyramid', desc: 'Data → Information → Knowledge → Wisdom hierarchy; CT operates at each transition' },
    { id: 'bailin-reconception', name: "Bailin's Reconception of CT", desc: 'Against domain-general skills; CT requires background knowledge, critical concepts, and standards' },
  ];

  return (
    <div className="space-y-6">
      <div className="space-y-1">
        <h1 className="text-2xl font-bold tracking-tight text-slate-900">Critical Thinking Frameworks</h1>
        <p className="text-sm text-slate-500">
          {frameworks.length} frameworks &mdash; each a different lens for developing and evaluating thought
        </p>
      </div>

      <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {frameworks.map((fw) => (
          <Link
            key={fw.id}
            href={`/frameworks/${fw.id}`}
            className="group rounded-lg border border-slate-200 bg-white dark:bg-slate-700 dark:border-slate-600 p-4 shadow-sm transition-[box-shadow,border-color] duration-150 ease-in-out hover:border-slate-400 hover:shadow-md dark:hover:bg-slate-600"
          >
            <h2 className="mb-1 text-sm font-semibold text-slate-900 group-hover:text-blue-700 dark:text-slate-100 dark:group-hover:text-blue-400">{fw.name}</h2>
            <p className="text-xs leading-relaxed text-slate-600">{fw.desc}</p>
            <p className="mt-2 text-xs text-slate-400 group-hover:text-blue-600 dark:group-hover:text-blue-400">Read more →</p>
          </Link>
        ))}
      </div>
    </div>
  );
}
