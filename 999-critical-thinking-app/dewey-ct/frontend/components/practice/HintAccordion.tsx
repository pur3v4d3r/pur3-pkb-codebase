'use client';

import { useState } from 'react';

interface HintProps {
  id: string;
  title: string;
  content: string;
}

export default function HintAccordion({ hints }: { hints: HintProps[] }) {
  const [openId, setOpenId] = useState<string | null>(null);

  return (
    <div className="space-y-2">
      {hints.map((hint) => (
        <div key={hint.id} className="rounded-lg border border-slate-200 overflow-hidden">
          <button
            onClick={() => setOpenId(openId === hint.id ? null : hint.id)}
            className="flex w-full items-center justify-between px-4 py-3 text-left text-sm font-medium text-slate-700 hover:bg-slate-50"
          >
            <span>{hint.title}</span>
            <span className="text-slate-400">{openId === hint.id ? '▲' : '▼'}</span>
          </button>
          {openId === hint.id && (
            <div className="border-t border-slate-100 bg-amber-50 px-4 py-3 text-sm leading-relaxed text-slate-700">
              {hint.content}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
