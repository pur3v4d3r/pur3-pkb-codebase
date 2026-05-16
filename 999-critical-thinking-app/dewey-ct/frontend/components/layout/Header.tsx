import Link from 'next/link';

interface NavLink {
  href: string;
  label: string;
}

const NAV_LINKS: NavLink[] = [
  { href: '/', label: 'Chapters' },
  { href: '/frameworks', label: 'Frameworks' },
  { href: '/templates', label: 'Templates' },
  { href: '/ask', label: 'Ask' },
  { href: '/portfolio', label: 'Portfolio' },
];

export default function Header() {
  return (
    <header className="sticky top-0 z-40 border-b border-slate-200 bg-white/80 backdrop-blur-sm">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-3">
        <Link href="/" className="flex items-center gap-2">
          <span className="rounded bg-slate-900 px-2 py-1 text-sm font-bold text-white">CT</span>
          <span className="text-base font-semibold text-slate-800">DeweyCT</span>
        </Link>

        <nav className="flex items-center gap-1">
          {NAV_LINKS.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="rounded-md px-3 py-1.5 text-sm font-medium text-slate-600 transition hover:bg-slate-100 hover:text-slate-900"
            >
              {link.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
