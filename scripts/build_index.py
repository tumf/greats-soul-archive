#!/usr/bin/env python3
"""Build README index sections from repo contents.

Updates:
- README.md between <!-- INDEX:START --> and <!-- INDEX:END -->
- README_ja.md between <!-- INDEX_JA:START --> and <!-- INDEX_JA:END -->

Run:
  python3 scripts/build_index.py
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Entry:
    name: str
    link: str


def parse_name(identity_path: Path) -> str:
    # Look for: - **Name:** ...
    txt = identity_path.read_text(encoding="utf-8")
    m = re.search(r"^-\s*\*\*Name:\*\*\s*(.+?)\s*$", txt, flags=re.MULTILINE)
    if m:
        return m.group(1).strip()
    # Fallback: title line '# X — IDENTITY.md'
    m = re.search(r"^#\s+(.+?)\s+—\s+IDENTITY\.md\s*$", txt, flags=re.MULTILINE)
    if m:
        return m.group(1).strip()
    return identity_path.parent.name


def list_people() -> list[Entry]:
    base = ROOT / "people"
    out: list[Entry] = []
    for d in sorted(base.iterdir()):
        if not d.is_dir():
            continue
        if d.name.startswith("_"):
            continue
        identity = d / "IDENTITY.md"
        if not identity.exists():
            continue
        name = parse_name(identity)
        out.append(Entry(name=name, link=f"people/{d.name}/"))
    out.sort(key=lambda e: e.name.lower())
    return out


def list_fiction(kind: str) -> list[Entry]:
    base = ROOT / "fiction" / kind
    if not base.exists():
        return []
    out: list[Entry] = []
    for d in sorted(base.iterdir()):
        if not d.is_dir():
            continue
        identity = d / "IDENTITY.md"
        if not identity.exists():
            continue
        name = parse_name(identity)
        out.append(Entry(name=name, link=f"fiction/{kind}/{d.name}/"))
    out.sort(key=lambda e: e.name.lower())
    return out


def render_index_en() -> str:
    people = list_people()
    pub = list_fiction("public-domain")
    insp = list_fiction("inspired")

    lines: list[str] = []
    lines.append("### People")
    lines.append("")
    for e in people:
        lines.append(f"- [{e.name}]({e.link})")

    lines.append("")
    lines.append("### Fiction")
    lines.append("")

    if pub:
        lines.append("**Public domain**")
        for e in pub:
            lines.append(f"- [{e.name}]({e.link})")
        lines.append("")
    else:
        lines.append("- Public domain: `fiction/public-domain/` (no profiles yet)")

    if insp:
        lines.append("- Inspired-by (modern works):")
        for e in insp:
            lines.append(f"  - [{e.name}]({e.link})")
    else:
        lines.append("- Inspired-by (modern works): `fiction/inspired/` (no profiles yet)")

    return "\n".join(lines).rstrip() + "\n"


def render_index_ja() -> str:
    people = list_people()
    pub = list_fiction("public-domain")
    insp = list_fiction("inspired")

    lines: list[str] = []
    lines.append("### People（実在）")
    lines.append("")
    for e in people:
        lines.append(f"- [{e.name}]({e.link})")

    lines.append("")
    lines.append("### Fiction（架空）")
    lines.append("")

    if pub:
        lines.append("**Public domain**")
        for e in pub:
            lines.append(f"- [{e.name}]({e.link})")
        lines.append("")
    else:
        lines.append("- Public domain: `fiction/public-domain/`（まだなし）")

    if insp:
        lines.append("- Inspired-by（現行作品）:")
        for e in insp:
            lines.append(f"  - [{e.name}]({e.link})")
    else:
        lines.append("- Inspired-by（現行作品）: `fiction/inspired/`（まだなし）")

    return "\n".join(lines).rstrip() + "\n"


def replace_block(path: Path, start: str, end: str, replacement: str) -> None:
    txt = path.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"({re.escape(start)}\n)(.*?)(\n{re.escape(end)})",
        flags=re.DOTALL,
    )
    m = pattern.search(txt)
    if not m:
        raise SystemExit(f"Markers not found in {path}")

    new_txt = txt[: m.start(2)] + replacement.rstrip("\n") + txt[m.end(2) :]
    path.write_text(new_txt, encoding="utf-8")


def main() -> None:
    readme = ROOT / "README.md"
    readme_ja = ROOT / "README_ja.md"

    replace_block(
        readme,
        "<!-- INDEX:START -->",
        "<!-- INDEX:END -->",
        "\n" + render_index_en() + "\n",
    )
    replace_block(
        readme_ja,
        "<!-- INDEX_JA:START -->",
        "<!-- INDEX_JA:END -->",
        "\n" + render_index_ja() + "\n",
    )


if __name__ == "__main__":
    main()
