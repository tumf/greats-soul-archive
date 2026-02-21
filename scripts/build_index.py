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
    category: str | None = None
    tags: set[str] | None = None


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


def read_meta_key(folder: Path, key: str) -> str | None:
    meta = folder / "meta.yml"
    if not meta.exists():
        return None
    txt = meta.read_text(encoding="utf-8")
    m = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", txt, flags=re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def read_meta_tags(folder: Path) -> set[str]:
    meta = folder / "meta.yml"
    if not meta.exists():
        return set()
    txt = meta.read_text(encoding="utf-8")
    tags: set[str] = set()

    # very small YAML subset parser:
    # tags:
    #   - assistant
    in_tags = False
    for raw in txt.splitlines():
        line = raw.rstrip()
        if re.match(r"^tags:\s*$", line):
            in_tags = True
            continue
        if in_tags:
            if re.match(r"^[a-zA-Z0-9_-]+:\s*", line):
                in_tags = False
                continue
            m = re.match(r"^\s*-\s*([a-zA-Z0-9_-]+)\s*$", line)
            if m:
                tags.add(m.group(1).lower())

    return tags


def read_category(folder: Path) -> str | None:
    v = read_meta_key(folder, "category")
    return v.lower() if v else None


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
        cat = read_category(d)
        tags = read_meta_tags(d)
        out.append(Entry(name=name, link=f"people/{d.name}/", category=cat, tags=tags))
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
        if d.name.startswith("_"):
            continue
        identity = d / "IDENTITY.md"
        if not identity.exists():
            continue
        name = parse_name(identity)
        genre = read_meta_key(d, "genre")
        cat = genre.lower() if genre else None
        tags = read_meta_tags(d)
        out.append(Entry(name=name, link=f"fiction/{kind}/{d.name}/", category=cat, tags=tags))
    out.sort(key=lambda e: e.name.lower())
    return out


CATEGORY_ORDER = [
    "business",
    "politics",
    "strategy",
    "philosophy",
    "science",
    "computing",
    "economics",
    "art",
    "uncategorized",
]

CATEGORY_LABELS_EN = {
    "business": "Builders / Business",
    "politics": "Politics / Statecraft",
    "strategy": "Military / Strategy",
    "philosophy": "Philosophy",
    "science": "Science / Math",
    "computing": "Computing / Software",
    "economics": "Economics / Social Science",
    "art": "Art / Literature",
    "uncategorized": "Uncategorized",
}

CATEGORY_LABELS_JA = {
    "business": "ビルダー / ビジネス",
    "politics": "政治 / 統治",
    "strategy": "軍略 / 戦略",
    "philosophy": "哲学",
    "science": "科学 / 数学",
    "computing": "計算機 / ソフトウェア",
    "economics": "経済 / 社会科学",
    "art": "芸術 / 文学",
    "uncategorized": "未分類",
}


def group_people(people: list[Entry]) -> dict[str, list[Entry]]:
    grouped: dict[str, list[Entry]] = {k: [] for k in CATEGORY_ORDER}
    for e in people:
        key = e.category or "uncategorized"
        if key not in grouped:
            key = "uncategorized"
        grouped[key].append(e)
    for k in grouped:
        grouped[k].sort(key=lambda e: e.name.lower())
    return grouped


def render_assistants_section_en(people: list[Entry], fiction: list[Entry]) -> str:
    assistants: list[Entry] = []
    for e in people + fiction:
        if e.tags and "assistant" in e.tags:
            assistants.append(e)
    assistants.sort(key=lambda e: e.name.lower())

    lines: list[str] = []
    lines.append("### Assistants / Sidekicks")
    lines.append("")
    if not assistants:
        lines.append("(None tagged yet)")
        return "\n".join(lines) + "\n"

    for e in assistants:
        lines.append(f"- [{e.name}]({e.link})")

    return "\n".join(lines) + "\n"


def render_index_en() -> str:
    people = list_people()
    pub = list_fiction("public-domain")
    insp = list_fiction("inspired")

    grouped = group_people(people)

    lines: list[str] = []
    lines.append("### People")
    lines.append("")

    for cat in CATEGORY_ORDER:
        entries = grouped.get(cat, [])
        if not entries:
            continue
        lines.append(f"**{CATEGORY_LABELS_EN.get(cat, cat)}**")
        for e in entries:
            lines.append(f"- [{e.name}]({e.link})")
        lines.append("")

    # Curated tag-based sections
    lines.append(render_assistants_section_en(people, pub + insp).rstrip())
    lines.append("")

    lines.append("### Fiction")
    lines.append("")

    def render_fiction_group(title: str, entries: list[Entry]) -> None:
        if not entries:
            lines.append(f"- {title}: `fiction/{title.lower().replace(' ', '-')}/` (no profiles yet)")
            return
        lines.append(f"**{title}**")
        # group by genre (Entry.category)
        genres: dict[str, list[Entry]] = {}
        for e in entries:
            g = e.category or "other"
            genres.setdefault(g, []).append(e)
        for g in sorted(genres.keys()):
            lines.append(f"- *{g}*")
            for e in sorted(genres[g], key=lambda x: x.name.lower()):
                lines.append(f"  - [{e.name}]({e.link})")

        lines.append("")

    if pub:
        render_fiction_group("Public domain", pub)
    else:
        lines.append("- Public domain: `fiction/public-domain/` (no profiles yet)")
        lines.append("")

    if insp:
        render_fiction_group("Inspired-by (modern works)", insp)
    else:
        lines.append("- Inspired-by (modern works): `fiction/inspired/` (no profiles yet)")

    return "\n".join(lines).rstrip() + "\n"


def render_assistants_section_ja(people: list[Entry], fiction: list[Entry]) -> str:
    assistants: list[Entry] = []
    for e in people + fiction:
        if e.tags and "assistant" in e.tags:
            assistants.append(e)
    assistants.sort(key=lambda e: e.name.lower())

    lines: list[str] = []
    lines.append("### 助手 / 相棒")
    lines.append("")
    if not assistants:
        lines.append("（まだなし）")
        return "\n".join(lines) + "\n"

    for e in assistants:
        lines.append(f"- [{e.name}]({e.link})")

    return "\n".join(lines) + "\n"


def render_index_ja() -> str:
    people = list_people()
    pub = list_fiction("public-domain")
    insp = list_fiction("inspired")

    grouped = group_people(people)

    lines: list[str] = []
    lines.append("### People（実在）")
    lines.append("")

    for cat in CATEGORY_ORDER:
        entries = grouped.get(cat, [])
        if not entries:
            continue
        lines.append(f"**{CATEGORY_LABELS_JA.get(cat, cat)}**")
        for e in entries:
            lines.append(f"- [{e.name}]({e.link})")
        lines.append("")

    # Curated tag-based sections
    lines.append(render_assistants_section_ja(people, pub + insp).rstrip())
    lines.append("")

    lines.append("### Fiction（架空）")
    lines.append("")

    def render_fiction_group(title: str, entries: list[Entry]) -> None:
        if not entries:
            lines.append(f"- {title}: （まだなし）")
            return
        lines.append(f"**{title}**")
        genres: dict[str, list[Entry]] = {}
        for e in entries:
            g = e.category or "other"
            genres.setdefault(g, []).append(e)
        for g in sorted(genres.keys()):
            lines.append(f"- *{g}*")
            for e in sorted(genres[g], key=lambda x: x.name.lower()):
                lines.append(f"  - [{e.name}]({e.link})")
        lines.append("")

    if pub:
        render_fiction_group("Public domain", pub)
    else:
        lines.append("- Public domain: `fiction/public-domain/`（まだなし）")
        lines.append("")

    if insp:
        render_fiction_group("Inspired-by（現行作品）", insp)
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
