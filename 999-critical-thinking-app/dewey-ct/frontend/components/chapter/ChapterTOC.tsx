'use client';

import { useEffect, useState } from 'react';

const ALL_SECTIONS = [
  { id: 'ch-overview', label: 'Overview' },
  { id: 'ch-concepts', label: 'Key Concepts' },
  { id: 'ch-annotations', label: 'Annotations' },
  { id: 'ch-connections', label: 'Connections' },
  { id: 'ch-crosswalk', label: 'Crosswalk' },
  { id: 'ch-models', label: 'Mental Models' },
] as const;

/** Sticky TOC sidebar for chapter pages with IntersectionObserver scroll-spy. */
export default function ChapterTOC() {
  const [activeId, setActiveId] = useState('');
  // Discover which section ids are actually rendered on this page.
  const [present, setPresent] = useState<string[]>([]);

  useEffect(() => {
    const found = ALL_SECTIONS
      .filter((s) => document.getElementById(s.id) !== null)
      .map((s) => s.id);
    setPresent(found);
  }, []);

  // Scroll-spy: highlight whichever section is closest to the top of the viewport.
  useEffect(() => {
    if (present.length === 0) return;

    const els = present
      .map((id) => document.getElementById(id))
      .filter((el): el is HTMLElement => el !== null);

    const obs = new IntersectionObserver(
      (entries) => {
        const intersecting = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (intersecting.length > 0) {
          setActiveId(intersecting[0].target.id);
        }
      },
      { rootMargin: '-10% 0px -80% 0px', threshold: 0 },
    );

    els.forEach((el) => obs.observe(el));
    return () => obs.disconnect();
  }, [present]);

  const sections = ALL_SECTIONS.filter((s) => present.includes(s.id));
  if (sections.length === 0) return null;

  return (
    <nav aria-label="Page sections" className="sticky top-24 space-y-0.5 text-sm">
      <p className="mb-3 px-3 text-[10px] font-semibold uppercase tracking-widest text-slate-400">
        On this page
      </p>
      {sections.map((s) => (
        <a
          key={s.id}
          href={`#${s.id}`}
          className={`block rounded-md px-3 py-1.5 text-xs transition ${
            activeId === s.id
              ? 'bg-slate-100 font-semibold text-slate-900 dark:bg-slate-800 dark:text-slate-100'
              : 'text-slate-500 hover:bg-slate-50 hover:text-slate-700 dark:hover:bg-slate-800 dark:hover:text-slate-300'
          }`}
        >
          {s.label}
        </a>
      ))}
    </nav>
  );
}
