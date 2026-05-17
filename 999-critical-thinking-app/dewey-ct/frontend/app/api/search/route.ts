import { getChapterSummaries, getAllFrameworks, getMentalModelsData, getAllTemplates } from '@/lib/content';
import { NextResponse } from 'next/server';

export interface SearchItem {
  id: string;
  title: string;
  subtitle?: string;
  href: string;
  type: 'chapter' | 'framework' | 'mental-model' | 'template';
}

export function GET() {
  const items: SearchItem[] = [];

  // Chapters
  for (const ch of getChapterSummaries()) {
    items.push({
      id: `ch-${ch.chapter}`,
      title: `Ch. ${ch.chapter}: ${ch.title}`,
      subtitle: ch.abstract?.slice(0, 100),
      href: `/chapter/${ch.chapter}`,
      type: 'chapter',
    });
  }

  // Frameworks
  for (const fw of getAllFrameworks()) {
    const desc = typeof fw.description === 'string' ? fw.description : undefined;
    items.push({
      id: `fw-${fw.id}`,
      title: fw.name,
      subtitle: desc?.slice(0, 100),
      href: `/frameworks/${fw.id}`,
      type: 'framework',
    });
  }

  // Mental models
  const { models } = getMentalModelsData();
  for (const m of models) {
    items.push({
      id: `mm-${m.id}`,
      title: m.name,
      subtitle: m.category,
      href: `/mental-models/${m.id}`,
      type: 'mental-model',
    });
  }

  // Templates
  for (const tpl of getAllTemplates()) {
    items.push({
      id: `tpl-${tpl.id}`,
      title: tpl.name,
      subtitle: tpl.description?.slice(0, 100),
      href: `/templates/${tpl.id}`,
      type: 'template',
    });
  }

  return NextResponse.json(items, {
    headers: {
      'Cache-Control': 'public, max-age=3600, stale-while-revalidate=86400',
    },
  });
}
