'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import SearchTrigger from './SearchTrigger';
import ThemeToggle from './ThemeToggle';

interface NavLink {
  href: string;
  label: string;
}

const NAV_LINKS: NavLink[] = [
  { href: '/dashboard', label: 'Dashboard' },
  { href: '/', label: 'Chapters' },
  { href: '/frameworks', label: 'Frameworks' },
  { href: '/mental-models', label: 'Mental Models' },
  { href: '/cheat-sheets', label: 'Cheat Sheets' },
  { href: '/templates', label: 'Templates' },
  { href: '/practice', label: 'Practice' },
  { href: '/detect', label: 'Detect' },
  { href: '/ask', label: 'Ask' },
  { href: '/review', label: 'Review' },
  { href: '/assess', label: 'Assess' },
  { href: '/portfolio', label: 'Portfolio' },
  { href: '/settings', label: 'Settings' },
];

function isActive(href: string, pathname: string): boolean {
  if (href === '/') return pathname === '/';
  return pathname === href || pathname.startsWith(href + '/');
}

export default function Header() {
  const pathname = usePathname();

  return (
    <header className="sticky top-0 z-40 border-b border-slate-200 bg-white/80 backdrop-blur-sm dark:border-slate-800 dark:bg-slate-900/80">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-3">
        <Link href="/" className="flex items-center gap-2">
          <span className="rounded bg-slate-900 px-2 py-1 text-sm font-bold text-white dark:bg-slate-100 dark:text-slate-900">CT</span>
          <span className="text-base font-semibold text-slate-800 dark:text-slate-100">DeweyCT</span>
        </Link>

        <nav className="flex items-center gap-1">
          {NAV_LINKS.map((link) => {
            const active = isActive(link.href, pathname);
            return (
              <Link
                key={link.href}
                href={link.href}
                className={
                  active
                    ? 'rounded-md px-3 py-1.5 text-sm font-medium bg-indigo-50 text-indigo-700 ring-1 ring-indigo-200 dark:bg-indigo-950/60 dark:text-indigo-300 dark:ring-indigo-800'
                    : 'rounded-md px-3 py-1.5 text-sm font-medium text-slate-600 transition hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-slate-100'
                }
                aria-current={active ? 'page' : undefined}
              >
                {link.label}
              </Link>
            );
          })}
          <SearchTrigger />
          <ThemeToggle />
        </nav>
      </div>
    </header>
  );
}
