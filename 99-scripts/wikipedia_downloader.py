#!/usr/bin/env python3
"""
wikipedia_downloader.py
─────────────────────────────────────────────────────────────────────────────
Download a Wikipedia article and convert it into a structured Obsidian
reference note with rich YAML frontmatter, wiki-links, and citation block.

FEATURES
  - Fetches article via Wikipedia REST API + Action API (no scraping)
  - Builds full frontmatter: title, aliases, url, lang, doc_created,
    doc_modified (article last revision), authors (top contributors),
    categories → tags, summary, page_id, wikidata_id, references count
  - Converts wiki HTML → clean Markdown with section headings preserved
  - Internal Wikipedia links converted to [[Wiki-Links]] (ghost links)
  - Saves to chosen folder with sanitised filename
  - Handles disambiguation, redirects, missing articles
  - Prompts (or accepts CLI flags) for missing optional metadata

USAGE
  python wikipedia_downloader.py "Albert Einstein"
  python wikipedia_downloader.py "Quantum entanglement" --output 04-library/wikipedia
  python wikipedia_downloader.py "Stoicism" --lang en --sections 5 --no-prompt
  python wikipedia_downloader.py --url https://en.wikipedia.org/wiki/Logic

REQUIREMENTS
  pip install requests beautifulsoup4 markdownify python-slugify rich

@author   PKB Scripting Architect
@version  1.0.0
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    from markdownify import markdownify as md
    from slugify import slugify
    from rich.console import Console
    from rich.prompt import Prompt, Confirm
except ImportError:
    sys.exit(
        "Missing dependencies. Run:\n"
        "  pip install requests beautifulsoup4 markdownify python-slugify rich"
    )

console = Console()

# ── CONFIGURATION ─────────────────────────────────────────────────────────
CONFIG = {
    "default_output_folder": "04-library/wikipedia",
    "default_lang": "en",
    "user_agent": "PKB-WikipediaDownloader/1.0 (Obsidian PKB; contact: local)",
    "max_sections": 0,            # 0 = all sections; otherwise truncate
    "include_references": True,   # include References section
    "convert_internal_links": True,  # /wiki/Foo → [[Foo]]
    "tag_prefix": "wikipedia",    # all generated category tags get this prefix
    "max_categories_as_tags": 8,
    "max_contributors": 5,
    "default_status": "seedling",
    "default_certainty": "moderate",
}
# ──────────────────────────────────────────────────────────────────────────


# ═══════════════════════════════════════════════════════════════════════════
# Wikipedia API client
# ═══════════════════════════════════════════════════════════════════════════

class WikipediaClient:
    """Thin wrapper around the Wikipedia REST + Action APIs."""

    def __init__(self, lang: str = "en"):
        self.lang = lang
        self.rest_base = f"https://{lang}.wikipedia.org/api/rest_v1"
        self.action_base = f"https://{lang}.wikipedia.org/w/api.php"
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": CONFIG["user_agent"]})

    def _get(self, url: str, **kwargs) -> requests.Response:
        r = self.session.get(url, timeout=30, **kwargs)
        r.raise_for_status()
        return r

    def summary(self, title: str) -> dict[str, Any]:
        """REST /page/summary/{title} — short description, thumbnail, IDs."""
        url = f"{self.rest_base}/page/summary/{requests.utils.quote(title, safe='')}"
        return self._get(url).json()

    def html(self, title: str) -> str:
        """REST /page/html/{title} — full parsed article HTML."""
        url = f"{self.rest_base}/page/html/{requests.utils.quote(title, safe='')}"
        return self._get(url).text

    def metadata(self, title: str) -> dict[str, Any]:
        """Action API: categories, contributors, revision info."""
        params = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "categories|contributors|revisions|info|pageprops",
            "cllimit": "max",
            "pclimit": str(CONFIG["max_contributors"]),
            "rvprop": "timestamp|user",
            "rvlimit": "1",
            "inprop": "url",
            "redirects": 1,
        }
        data = self._get(self.action_base, params=params).json()
        pages = data.get("query", {}).get("pages", {})
        if not pages:
            return {}
        return next(iter(pages.values()))


# ═══════════════════════════════════════════════════════════════════════════
# HTML → Markdown conversion
# ═══════════════════════════════════════════════════════════════════════════

def clean_html(html: str, max_sections: int = 0) -> tuple[str, int]:
    """Strip Wikipedia chrome, optionally truncate sections, return cleaned HTML.

    Returns (cleaned_html, references_count).
    """
    soup = BeautifulSoup(html, "html.parser")

    # Remove edit links, references markers, infobox tables, navboxes
    selectors_to_strip = [
        ".mw-editsection",
        ".reference",          # inline [1] markers
        ".noprint",
        ".navbox",
        ".infobox",
        ".sistersitebox",
        ".metadata",
        "style",
        "script",
        ".mw-empty-elt",
        ".hatnote",
    ]
    for sel in selectors_to_strip:
        for node in soup.select(sel):
            node.decompose()

    # Count references before potentially removing them
    ref_count = len(soup.select("ol.references li, .references li"))

    if not CONFIG["include_references"]:
        for node in soup.select(".references, ol.references, #References"):
            node.decompose()

    # Truncate to N top-level sections if requested
    if max_sections and max_sections > 0:
        sections = soup.find_all("section", recursive=False)
        if not sections:
            sections = soup.find_all("section")
        for extra in sections[max_sections:]:
            extra.decompose()

    return str(soup), ref_count


def html_to_markdown(html: str) -> str:
    """Convert cleaned HTML to Markdown."""
    body = md(
        html,
        heading_style="ATX",
        bullets="-",
        strip=["span"],
        escape_asterisks=False,
        escape_underscores=False,
    )
    # Collapse 3+ blank lines
    body = re.sub(r"\n{3,}", "\n\n", body)
    # Strip leading/trailing whitespace per line
    body = "\n".join(line.rstrip() for line in body.splitlines())
    return body.strip()


def convert_internal_links(markdown_text: str) -> str:
    """Convert [text](/wiki/Article_Name) → [[Article Name|text]] ghost links."""
    if not CONFIG["convert_internal_links"]:
        return markdown_text

    def repl(m: re.Match) -> str:
        text = m.group(1).strip()
        target_raw = m.group(2)
        # Skip non-/wiki/ links (external, file, etc.)
        if not target_raw.startswith("/wiki/"):
            return m.group(0)
        # Skip special namespaces
        target = unquote(target_raw[len("/wiki/"):])
        if ":" in target.split("#")[0]:
            return text  # collapse File:, Help:, Category: links to plain text
        target = target.replace("_", " ")
        # Strip fragments
        if "#" in target:
            target = target.split("#")[0]
        if not target:
            return text
        if text.lower() == target.lower():
            return f"[[{target}]]"
        return f"[[{target}|{text}]]"

    return re.sub(r"\[([^\]]+?)\]\((/wiki/[^)]+)\)", repl, markdown_text)


# ═══════════════════════════════════════════════════════════════════════════
# Frontmatter assembly
# ═══════════════════════════════════════════════════════════════════════════

def slugify_tag(text: str) -> str:
    """Tag-safe slug: lowercase, hyphenated."""
    return slugify(text, separator="-", lowercase=True)


def build_frontmatter(
    summary: dict[str, Any],
    meta: dict[str, Any],
    *,
    lang: str,
    ref_count: int,
    extra: dict[str, Any] | None = None,
) -> str:
    """Build YAML frontmatter from API responses + user extras."""
    extra = extra or {}
    today = dt.date.today().isoformat()

    title = summary.get("title", "Untitled")
    description = summary.get("description") or extra.get("description", "")
    extract = (summary.get("extract") or "").strip()
    page_url = summary.get("content_urls", {}).get("desktop", {}).get("page", "")
    page_id = summary.get("pageid") or meta.get("pageid", "")
    wikidata_id = summary.get("wikibase_item", "")

    # Last revision timestamp (from Action API)
    revs = meta.get("revisions") or []
    last_modified = today
    if revs:
        ts = revs[0].get("timestamp", "")
        if ts:
            last_modified = ts.split("T")[0]

    # Top contributors
    contributors = [c.get("name", "") for c in (meta.get("contributors") or [])]
    contributors = [c for c in contributors if c][: CONFIG["max_contributors"]]

    # Categories → tags
    raw_categories = [
        c.get("title", "").replace("Category:", "")
        for c in (meta.get("categories") or [])
    ]
    raw_categories = [c for c in raw_categories if c]
    tag_categories = [
        f"{CONFIG['tag_prefix']}/{slugify_tag(c)}"
        for c in raw_categories[: CONFIG["max_categories_as_tags"]]
    ]
    base_tags = [
        CONFIG["tag_prefix"],
        "reference-note",
        "external-source",
    ]
    all_tags = base_tags + tag_categories + extra.get("extra_tags", [])

    # Aliases — short title variants
    aliases = [title]
    if "(" in title:
        aliases.append(title.split("(")[0].strip())
    aliases = list(dict.fromkeys(a for a in aliases if a))

    # YAML — manual emit for tight control over ordering
    def yaml_list(items: list[str], indent: int = 2) -> str:
        if not items:
            return " []"
        pad = " " * indent
        return "\n" + "\n".join(f"{pad}- {x}" for x in items)

    def yaml_str(value: str) -> str:
        # Quote if contains colon, hash, leading dash, etc.
        if not value:
            return '""'
        if re.search(r'[:#\[\]{}|>!*&%@`"\'\n]', value) or value.lstrip().startswith("-"):
            escaped = value.replace('"', '\\"')
            return f'"{escaped}"'
        return value

    fm_lines = [
        "---",
        f"title: {yaml_str(title)}",
        f"aliases:{yaml_list(aliases)}",
        f"doc_type: reference-note",
        f"source: wikipedia",
        f"source_url: {yaml_str(page_url)}",
        f"source_lang: {lang}",
        f"page_id: {page_id}",
        f"wikidata_id: {yaml_str(wikidata_id)}",
        f"description: {yaml_str(description)}",
        f"doc_created: {today}",
        f"doc_modified: {last_modified}",
        f"status: {extra.get('status', CONFIG['default_status'])}",
        f"certainty: {extra.get('certainty', CONFIG['default_certainty'])}",
        f"knowledge_level: {yaml_str(extra.get('knowledge_level', 'reference'))}",
        f"authors:{yaml_list(contributors)}",
        f"references_count: {ref_count}",
        f"tags:{yaml_list(all_tags)}",
        f"related:{yaml_list(extra.get('related', []))}",
        "---",
    ]
    return "\n".join(fm_lines)


# ═══════════════════════════════════════════════════════════════════════════
# Note assembly
# ═══════════════════════════════════════════════════════════════════════════

def build_note(
    frontmatter: str,
    summary: dict[str, Any],
    body_md: str,
    page_url: str,
) -> str:
    """Compose final Markdown note."""
    title = summary.get("title", "Untitled")
    extract = (summary.get("extract") or "").strip()
    description = summary.get("description") or ""
    today = dt.date.today().isoformat()

    sections = [frontmatter, "", f"# {title}", ""]

    if description:
        sections.append(f"> [!abstract] {description}")
        if extract:
            for line in extract.split("\n"):
                sections.append(f"> {line}")
        sections.append("")

    sections.extend([
        "## Overview",
        "",
        extract or "*(No summary extract available — see body below.)*",
        "",
        "---",
        "",
        "## Article Content",
        "",
        body_md,
        "",
        "---",
        "",
        "## Source & Citation",
        "",
        f"- **Source:** [Wikipedia — {title}]({page_url})",
        f"- **Retrieved:** {today}",
        f"- **License:** Content available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)",
        "",
        "## Related Notes",
        "",
        "- *(Add wiki-links to related notes in your vault here.)*",
        "",
    ])
    return "\n".join(sections)


# ═══════════════════════════════════════════════════════════════════════════
# Orchestration
# ═══════════════════════════════════════════════════════════════════════════

def parse_title_from_url(url: str) -> tuple[str, str]:
    """Extract (title, lang) from a Wikipedia URL."""
    parsed = urlparse(url)
    host = parsed.netloc  # e.g. en.wikipedia.org
    lang = host.split(".")[0] if host.endswith("wikipedia.org") else "en"
    path = unquote(parsed.path)
    if path.startswith("/wiki/"):
        title = path[len("/wiki/"):].replace("_", " ")
    else:
        title = path.strip("/").replace("_", " ")
    return title, lang


def prompt_for_extras(no_prompt: bool, defaults: dict[str, Any]) -> dict[str, Any]:
    """Interactively collect optional metadata, unless --no-prompt was passed."""
    if no_prompt:
        return defaults

    console.print("\n[bold cyan]Optional metadata[/bold cyan] [dim](press Enter to accept default)[/dim]")
    extra = {}
    extra["status"] = Prompt.ask(
        "  Status",
        choices=["seedling", "budding", "evergreen", "wilting"],
        default=defaults.get("status", CONFIG["default_status"]),
    )
    extra["certainty"] = Prompt.ask(
        "  Certainty",
        choices=["speculative", "provisional", "moderate", "established", "verified"],
        default=defaults.get("certainty", CONFIG["default_certainty"]),
    )
    extra["knowledge_level"] = Prompt.ask(
        "  Knowledge level", default=defaults.get("knowledge_level", "reference")
    )
    extra_tags_raw = Prompt.ask(
        "  Extra tags (comma-separated, optional)", default=""
    )
    extra["extra_tags"] = [t.strip() for t in extra_tags_raw.split(",") if t.strip()]
    related_raw = Prompt.ask(
        "  Related notes (comma-separated wiki-links, optional)", default=""
    )
    extra["related"] = [r.strip() for r in related_raw.split(",") if r.strip()]
    return extra


def safe_filename(title: str) -> str:
    """Vault-safe markdown filename."""
    slug = slugify(title, separator="-", lowercase=True, max_length=120)
    return f"{slug}.md"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Download a Wikipedia article into a structured Obsidian reference note.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("title", nargs="?", help='Article title (e.g. "Albert Einstein")')
    parser.add_argument("--url", help="Full Wikipedia URL (overrides --title and --lang)")
    parser.add_argument("--lang", default=CONFIG["default_lang"], help="Language code (default: en)")
    parser.add_argument(
        "--output",
        default=CONFIG["default_output_folder"],
        help=f"Output folder (default: {CONFIG['default_output_folder']})",
    )
    parser.add_argument(
        "--sections", type=int, default=CONFIG["max_sections"],
        help="Max top-level sections to include (0 = all)",
    )
    parser.add_argument("--no-references", action="store_true", help="Strip References section")
    parser.add_argument("--no-links", action="store_true", help="Do not convert wiki links to [[wiki-links]]")
    parser.add_argument("--no-prompt", action="store_true", help="Skip interactive metadata prompts")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite if output file exists")
    args = parser.parse_args()

    # Resolve title and language
    if args.url:
        title, lang = parse_title_from_url(args.url)
    elif args.title:
        title, lang = args.title, args.lang
    else:
        parser.error("Provide a TITLE or --url")
        return 2

    # Apply CLI overrides to CONFIG
    if args.no_references:
        CONFIG["include_references"] = False
    if args.no_links:
        CONFIG["convert_internal_links"] = False
    CONFIG["max_sections"] = args.sections

    console.print(f"\n[bold]📚 Wikipedia Downloader[/bold]")
    console.print(f"  Title : [cyan]{title}[/cyan]")
    console.print(f"  Lang  : [cyan]{lang}[/cyan]")

    client = WikipediaClient(lang=lang)

    # Step 1: summary (validates article exists)
    try:
        summary = client.summary(title)
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            console.print(f"[red]❌ Article not found: {title}[/red]")
            return 1
        console.print(f"[red]❌ HTTP error: {e}[/red]")
        return 1

    if summary.get("type") == "disambiguation":
        console.print(f"[yellow]⚠️  '{title}' is a disambiguation page.[/yellow]")
        console.print(f"   See: {summary.get('content_urls', {}).get('desktop', {}).get('page', '')}")
        if not args.no_prompt and not Confirm.ask("Continue anyway?", default=False):
            return 1

    # Resolve canonical title (handles redirects)
    canonical = summary.get("title", title)
    if canonical != title:
        console.print(f"  [dim]Resolved → {canonical}[/dim]")

    # Step 2: metadata (categories, contributors, revisions)
    console.print("  Fetching metadata...")
    try:
        meta = client.metadata(canonical)
    except requests.HTTPError as e:
        console.print(f"[yellow]⚠️  Metadata fetch failed: {e}. Continuing with defaults.[/yellow]")
        meta = {}

    # Step 3: HTML body
    console.print("  Fetching article HTML...")
    html = client.html(canonical)
    cleaned_html, ref_count = clean_html(html, max_sections=CONFIG["max_sections"])
    body_md = html_to_markdown(cleaned_html)
    body_md = convert_internal_links(body_md)

    # Step 4: optional user extras
    extras = prompt_for_extras(args.no_prompt, defaults={})

    # Step 5: assemble
    page_url = summary.get("content_urls", {}).get("desktop", {}).get("page", "")
    frontmatter = build_frontmatter(
        summary, meta, lang=lang, ref_count=ref_count, extra=extras
    )
    note = build_note(frontmatter, summary, body_md, page_url)

    # Step 6: write
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / safe_filename(canonical)

    if out_path.exists() and not args.overwrite:
        if args.no_prompt or not Confirm.ask(
            f"\n[yellow]File exists: {out_path}. Overwrite?[/yellow]", default=False
        ):
            console.print("[red]✗ Aborted (file exists).[/red]")
            return 1

    out_path.write_text(note, encoding="utf-8")
    console.print(f"\n[green]✅ Saved → [bold]{out_path}[/bold][/green]")
    console.print(f"   {len(body_md):,} chars · {ref_count} references · {len(meta.get('categories') or [])} categories")
    return 0


if __name__ == "__main__":
    sys.exit(main())
