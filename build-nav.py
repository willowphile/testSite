#!/usr/bin/env python3
"""
Regenerates navbar.html from nav-config.json.

Usage:
    python3 build-nav.py

Any .html files in the directory that aren't listed in nav-config.json
(and aren't in the skip list) show up in an "Uncategorized" dropdown.
To categorize them, add them to nav-config.json and re-run.
"""
import json
import re
from pathlib import Path

CONFIG_FILE = Path('nav-config.json')
NAVBAR_FILE = Path('navbar.html')


def get_title(path: Path) -> str:
    try:
        content = path.read_text(encoding='utf-8', errors='ignore')
        match = re.search(r'<title[^>]*>([^<]+)</title>', content, re.IGNORECASE)
        if match:
            t = match.group(1).strip()
            if t and t != 'Page Title':
                return t
    except Exception:
        pass
    return path.name


def render_link(href: str, label: str) -> str:
    return f'  <a href="{href}">{label}</a>'


def render_dropdown(label: str, items: list[dict]) -> str:
    links = '\n'.join(f'      <a href="{i["href"]}">{i["label"]}</a>' for i in items)
    return (
        f'  <div class="dropdown">\n'
        f'    <button class="dropbtn">{label}</button>\n'
        f'    <div class="dropdown-content">\n'
        f'{links}\n'
        f'    </div>\n'
        f'  </div>'
    )


def main():
    if not CONFIG_FILE.exists():
        print(f'Error: {CONFIG_FILE} not found. Run from the testSite directory.')
        return

    config = json.loads(CONFIG_FILE.read_text())
    skip = set(config.get('skip', []))

    # Collect every href already accounted for in the config
    known = set()
    for item in config.get('left', []):
        if item.get('type') == 'dropdown':
            for i in item.get('items', []):
                known.add(i.get('href', ''))
        else:
            known.add(item.get('href', ''))
    known |= skip

    # Find uncategorized files
    all_html = sorted(p.name for p in Path('.').glob('*.html'))
    uncategorized = [
        {'href': name, 'label': get_title(Path(name))}
        for name in all_html
        if name not in known
    ]

    # Build navbar
    parts = []
    for item in config.get('left', []):
        if item.get('type') == 'dropdown':
            parts.append(render_dropdown(item['label'], item['items']))
        else:
            parts.append(render_link(item['href'], item['label']))

    if uncategorized:
        parts.append(render_dropdown('Uncategorized', uncategorized))

    navbar = '<div class="navbar">\n' + '\n'.join(parts) + '\n</div>\n'
    NAVBAR_FILE.write_text(navbar)

    print(f'Wrote {NAVBAR_FILE} ({len(config.get("left", []))} items, '
          f'{len(uncategorized)} uncategorized)')
    if uncategorized:
        print('\nUncategorized files (add these to nav-config.json to organize them):')
        for f in uncategorized:
            print(f'  {f["href"]:40s}  {f["label"]}')


if __name__ == '__main__':
    main()
