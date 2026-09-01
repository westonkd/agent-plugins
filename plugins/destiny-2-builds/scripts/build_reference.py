#!/usr/bin/env python3
"""Rebuild the destiny-2-builds skill references from the Destiny Data Compendium.

The compendium is a public Google Sheet whose tabs are hand-laid-out grids, not
normalized tables, so every tab needs a small layout description (below) that
says which columns hold entry names and which hold their text.

Usage (from anywhere):
    python3 scripts/build_reference.py            # fetch + rebuild
    python3 scripts/build_reference.py --offline  # rebuild from cached CSVs

Cached CSVs live in scripts/.cache/ and are not committed.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import shutil
import sys
import urllib.request

SHEET_ID = "1WaxvbLx7UoSZaBqdFr1u32F2uWVLo-CJunJB4nlGUE4"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit"

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN_ROOT = os.path.dirname(HERE)
REFERENCES = os.path.join(PLUGIN_ROOT, "skills", "destiny-2-builds", "references")
CACHE = os.path.join(HERE, ".cache")
CURATED = os.path.join(PLUGIN_ROOT, "curated")

# Hand-maintained files copied into references/ and listed in the index. They are
# not generated from the spreadsheet, so they survive the rebuild by being copied
# back in after it clears the directory.
STATIC = [
    {
        "source": "known-bugs.md", "out": "known-bugs.md", "area": "Bugs",
        "tab": "hand-maintained",
        "blurb": ("Bugs and unintended interactions present in Monument of Triumph or later, "
                  "which ones still favour a build, which are disabled in Crucible but live in "
                  "PvE, and which are already patched."),
    },
]

# Layout of every tab in the compendium.
#   pairs            entry name in column n, its text in column n + 2
#   stacked_right    entry name in column n, its text in column n - 1, next row
#   stacked_below    entry name in column n, its text in the same column, next row
#   grid             free-form; rows are emitted as they are laid out
SHEETS = [
    {
        "gid": "1038486120", "tab": "Landing", "area": "Overview", "out": "compendium-overview.md",
        "title": "Compendium Overview", "layout": "grid",
        "blurb": "Front page of the compendium: credits, damage-scaling notes, and errata.",
    },
    {
        "gid": "1662574278", "tab": "Weapon Perks", "area": "Weapons", "out": "weapons/perks",
        "title": "Weapon Perks, Mods, and Traits", "layout": "pairs",
        "groups": [(0, 2)], "split": "section", "start_row": 4,
        "blurb": "Every weapon trait, weapon mod, intrinsic frame trait, and origin trait, with exact numbers.",
    },
    {
        "gid": "1287885342", "tab": "Armor Perks", "area": "Armor", "out": "armor/set-bonuses.md", "start_row": 2,
        "title": "Armor Set Bonuses", "layout": "pairs", "groups": [(0, 2)],
        "blurb": "2-piece and 4-piece bonuses for every armor set.",
    },
    {
        "gid": "473308249", "tab": "Artifact Perks", "area": "Artifact", "out": "artifact-perks",
        "title": "Artifact Perks", "layout": "stacked_right",
        "name_cols": [2, 5, 8], "section_col": 3, "split": "section",
        "preamble": ("Only one artifact can be equipped at a time. Every artifact perk in a build "
                     "must come from this one file."),
        "blurb": "Perks for this artifact only.",
    },
    {
        "gid": "1934379638", "tab": "Armor Mods", "area": "Armor", "out": "armor/mods.md",
        "title": "Armor Mods", "layout": "pairs", "header_row": 0,
        "groups": [(1, 3), (4, 6), (7, 9), (10, 12), (13, 15), (17, 19), (20, 22), (23, 25)],
        "blurb": "Helmet, arms, chest, legs, and class item mods with energy costs, plus raid and activity mods.",
    },
    {
        "gid": "618967225", "tab": "Arc", "area": "Subclasses", "out": "subclasses/arc.md",
        "start_row": 2, "section_col": 0,
        "title": "Arc Subclasses", "layout": "pairs", "groups": [(1, 3)],
        "extras": {13: "Stat changes"},
        "blurb": "Arc keywords, fragments, aspects, grenades, melees, and supers for all three classes.",
    },
    {
        "gid": "1186062409", "tab": "Solar", "area": "Subclasses", "out": "subclasses/solar.md",
        "start_row": 2, "section_col": 0,
        "title": "Solar Subclasses", "layout": "pairs", "groups": [(1, 3)],
        "extras": {13: "Stat changes"},
        "blurb": "Solar keywords, fragments, aspects, grenades, melees, and supers for all three classes.",
    },
    {
        "gid": "1907852650", "tab": "Void", "area": "Subclasses", "out": "subclasses/void.md",
        "start_row": 2, "section_col": 0,
        "title": "Void Subclasses", "layout": "pairs", "groups": [(1, 3)],
        "extras": {13: "Stat changes"},
        "blurb": "Void keywords, fragments, aspects, grenades, melees, and supers for all three classes.",
    },
    {
        "gid": "1088259962", "tab": "Stasis", "area": "Subclasses", "out": "subclasses/stasis.md",
        "start_row": 2, "section_col": 0,
        "title": "Stasis Subclasses", "layout": "pairs", "groups": [(1, 3)],
        "extras": {13: "Stat changes"},
        "blurb": "Stasis keywords, fragments, aspects, grenades, melees, and supers for all three classes.",
    },
    {
        "gid": "1870531554", "tab": "Strand", "area": "Subclasses", "out": "subclasses/strand.md",
        "start_row": 2, "section_col": 0,
        "title": "Strand Subclasses", "layout": "pairs", "groups": [(1, 3)],
        "extras": {13: "Stat changes"},
        "blurb": "Strand keywords, fragments, aspects, grenades, melees, and supers for all three classes.",
    },
    {
        "gid": "1918152785", "tab": "Prismatic", "area": "Subclasses", "out": "subclasses/prismatic.md",
        "start_row": 2, "section_col": 0,
        "title": "Prismatic Subclasses", "layout": "pairs", "groups": [(1, 3)],
        "list_cols": [3, 5, 7, 9, 11],
        "extras": {13: "Stat changes"},
        "blurb": "Prismatic fragments, Transcendence, and the aspect/ability pool each class can mix.",
    },
    {
        "gid": "20898389", "tab": "Exotic Class", "area": "Armor", "out": "armor/exotic-class-items", "start_row": 1,
        "title": "Exotic Class Item Perks", "layout": "pairs", "groups": [(0, 2), (3, 5)],
        "group_labels": ["First Perk Column", "Second Perk Column"], "split": "group",
        "section_col": 0, "section_lone": True,
        "preamble": ("An exotic class item rolls one perk from the first column and one from the "
                     "second. Both perks must be legal for the class: class-agnostic, or from that "
                     "class's own section."),
        "blurb": "Spirit of ... perks in this column of the exotic class item, by class.",
    },
    {
        "gid": "527596209", "tab": "Class Abilities", "area": "Subclasses", "out": "class-abilities.md", "start_row": 1, "section_col": 0,
        "title": "Class Abilities and Passive Traits", "layout": "pairs", "groups": [(1, 3)],
        "extras": {13: "Cooldowns"},
        "blurb": "Dodges, barricades, and rifts with base cooldowns and class passives.",
    },
    {
        "gid": "441434520", "tab": "Exotic Weapons", "area": "Weapons", "out": "weapons/exotics",
        "title": "Exotic Weapons", "layout": "pairs", "groups": [(0, 3)], "split": "section",
        "blurb": "Every exotic weapon with its frame, perks, catalyst, and measured behaviour.",
    },
    {
        "gid": "1500097863", "tab": "Exotic Armors", "area": "Armor", "out": "armor/exotics", "start_row": 3, "attach_label": "Exotic perk",
        "title": "Exotic Armor", "layout": "pairs",
        "groups": [(0, 2), (3, 5), (6, 8)], "group_labels": ["Hunter", "Titan", "Warlock"],
        "split": "group",
        "blurb": "Every exotic armor piece and its exotic perk, by class.",
    },
    {
        "gid": "1800463143", "tab": "Game Mechanics", "area": "Mechanics", "out": "mechanics.md",
        "title": "Game Mechanics", "layout": "grid", "start_row": 10,
        "blurb": "Ability energy tiers, activity modifiers, Armor Charge, stats, champions, combatant data, and super energy.",
    },
    {
        "gid": "715236319", "area": "Archive", "tab": "OLD Episodic Artifact Perks",
        "out": "archive/episodic-artifact-perks.md",
        "title": "Archived Episodic Artifact Perks", "layout": "stacked_right",
        "name_cols": [2, 5, 8, 11, 14], "section_col": 1,
        "blurb": "Artifact perks from the Episode artifacts, still equippable from past seasons.",
    },
    {
        "gid": "70425171", "area": "Archive", "tab": "OLD Seasonal Artifact Perks",
        "out": "archive/seasonal-artifact-perks.md",
        "title": "Archived Seasonal Artifact Perks", "layout": "stacked_below",
        "name_cols": [1, 4, 7, 10, 13],
        "blurb": "Artifact perks from seasons 15 through 23.",
    },
    {
        "gid": "333521426", "area": "Archive", "tab": "OLD Nether Mechanics", "out": "archive/nether-mechanics.md",
        "title": "Archived Nether Mechanics", "layout": "grid", "start_row": 2,
        "blurb": "Mechanics specific to the Nether activity from Episode: Heresy.",
    },
    {
        "gid": "1925335732", "area": "Archive", "tab": "OLD Armor Mods", "out": "archive/armor-mods.md",
        "title": "Archived Armor Mods", "layout": "pairs", "header_row": 1,
        "groups": [(2, 4), (5, 7), (8, 10), (11, 13), (14, 16), (17, 19), (20, 22),
                   (23, 25), (26, 28), (29, 31), (32, 34), (35, 37), (38, 40)],
        "blurb": "Pre-Edge of Fate armor mods, Charged With Light, Warmind Cells, and Elemental Wells.",
    },
    {
        "gid": "135237481", "area": "Archive", "tab": "OLD Game Mechanics", "out": "archive/game-mechanics.md",
        "title": "Archived Game Mechanics", "layout": "grid", "start_row": 10,
        "blurb": "Mechanics superseded by the Edge of Fate stat and difficulty rework.",
    },
]


def csv_url(gid: str) -> str:
    return (
        f"https://docs.google.com/spreadsheets/d/{SHEET_ID}"
        f"/gviz/tq?tqx=out:csv&headers=0&gid={gid}"
    )


def fetch(gid: str) -> str:
    with urllib.request.urlopen(csv_url(gid), timeout=60) as response:
        return response.read().decode("utf-8")


def load_rows(sheet: dict, offline: bool) -> list[list[str]]:
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f"{sheet['gid']}.csv")
    if not offline:
        text = fetch(sheet["gid"])
        if text.lstrip().startswith("<!DOCTYPE"):
            raise SystemExit(f"{sheet['tab']}: sheet returned HTML, not CSV")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
    with open(path, encoding="utf-8") as handle:
        return list(csv.reader(handle))


NOISE = ("HTMLView", "Go back to the top", "Support the Data Compendium")


def cell(row: list[str], index: int) -> str:
    if index >= len(row):
        return ""
    value = (row[index] or "").replace("\r\n", "\n").strip()
    if value == "-" or any(marker in value for marker in NOISE):
        return ""
    return value


def clean(text: str) -> str:
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    lines = [line.lstrip("#>").strip() if line.startswith(("#", ">")) else line for line in lines]
    return "\n".join(line for line in lines if line)


def is_lone(row: list[str], index: int) -> bool:
    return all(not cell(row, j) for j in range(len(row)) if j != index)


class Section:
    def __init__(self, title: str) -> None:
        self.title = title
        self.notes: list[str] = []
        self.entries: list[dict] = []


HEADER_LABELS = {"information", "description", "effect", "notes", "perk"}


def is_heading(row: list[str], index: int, value: str) -> bool:
    return (
        is_lone(row, index)
        and "\n" not in value
        and len(value) <= 60
        and len(value.split()) <= 6
        and value[-1] not in ".!?"
    )


def parse_pairs(rows: list[list[str]], sheet: dict) -> list[list[Section]]:
    groups = sheet["groups"]
    labels = sheet.get("group_labels")
    header_row = sheet.get("header_row")
    if labels is None and header_row is not None:
        labels = [cell(rows[header_row], name_col) or f"Group {i + 1}"
                  for i, (name_col, _) in enumerate(groups)]

    start_row = sheet.get("start_row", 0)
    section_col = sheet.get("section_col")
    list_cols = sheet.get("list_cols") or []
    per_group: list[list[Section]] = []
    for index, (name_col, text_col) in enumerate(groups):
        sections = [Section(labels[index] if labels else "")]
        prefix = ""
        for row_index, row in enumerate(rows):
            if row_index < start_row or row_index == header_row:
                continue
            if section_col is not None:
                banner = cell(row, section_col)
                if sheet.get("section_lone") and not is_lone(row, section_col):
                    banner = ""
                if banner and "\n" not in banner and len(banner) < 40:
                    prefix = banner
                    sections.append(Section(prefix))
                    continue
            name, text = cell(row, name_col), cell(row, text_col)
            if name and text.lower() in HEADER_LABELS:
                sections.append(Section(f"{prefix} — {name}" if prefix else name))
                continue
            if list_cols and not name:
                items = [cell(row, col) for col in list_cols]
                items = [item for item in items if item and "\n" not in item and len(item) < 60]
                if len(items) > 2 and sections[-1].entries:
                    sections[-1].entries[-1]["body"].append(" · ".join(items))
                    continue
            if name and text:
                sections[-1].entries.append({"name": name, "body": [text], "extras": []})
            elif name and not text:
                if is_heading(row, name_col, name):
                    sections.append(Section(f"{prefix} — {name}" if prefix else name))
                elif not sections[-1].entries:
                    sections[-1].notes.append(name)
                elif sections[-1].entries:
                    label = sheet.get("attach_label")
                    sections[-1].entries[-1]["extras"].append(
                        f"{label}: {name}" if label else name)
                else:
                    sections[-1].entries.append({"name": name, "body": [], "extras": []})
            elif text and sections[-1].entries:
                sections[-1].entries[-1]["body"].append(text)
            for extra_col, label in (sheet.get("extras") or {}).items():
                value = cell(row, int(extra_col))
                if value and sections[-1].entries:
                    sections[-1].entries[-1]["extras"].append(f"{label}: {value}")
        per_group.append([s for s in sections if s.entries or s.notes])
    return per_group


def parse_stacked(rows: list[list[str]], sheet: dict, below: bool) -> list[list[Section]]:
    sections = [Section("")]
    seen: set[tuple[int, int]] = set()
    section_col = sheet.get("section_col")
    for row_index, row in enumerate(rows):
        if section_col is not None:
            banner = cell(row, section_col)
            if banner and is_lone(row, section_col):
                if ("\n" not in banner and len(banner) <= 60
                        and not set("|⯁") & set(banner)):
                    sections.append(Section(banner))
                else:
                    sections[-1].notes.append(banner)
                continue
        for name_col in sheet["name_cols"]:
            if (row_index, name_col) in seen:
                continue
            name = cell(row, name_col)
            if not name:
                continue
            if is_heading(row, name_col, name):
                sections.append(Section(name))
                continue
            text_col = name_col if below else name_col - 1
            text = cell(rows[row_index + 1], text_col) if row_index + 1 < len(rows) else ""
            if below:
                seen.add((row_index + 1, name_col))
            if len(name) > 120 and not text:
                continue
            sections[-1].entries.append({"name": name, "body": [text] if text else [], "extras": []})
    return [[s for s in sections if s.entries or s.notes]]


def flatten(value: str) -> str:
    return " ".join(value.split())


def parse_grid(rows: list[list[str]], sheet: dict) -> list[list[Section]]:
    sections = [Section("")]
    for row in rows[sheet.get("start_row", 0):]:
        values = [cell(row, index) for index in range(len(row))]
        values = [value for value in values if value]
        if not values:
            continue
        head, rest = values[0], values[1:]
        head_flat = flatten(head)
        compact = len(head_flat) < 70
        if not rest:
            if (compact and head_flat[-1] not in ".!?" and len(head_flat.split()) <= 8
                    and not set("|▲▼") & set(head_flat)):
                sections.append(Section(head_flat))
            else:
                sections[-1].entries.append(
                    {"kind": "block", "name": "", "body": [head], "extras": []})
            continue
        if compact and all(len(flatten(value)) < 70 for value in rest):
            sections[-1].entries.append(
                {"kind": "row", "name": head_flat,
                 "body": [flatten(value) for value in rest], "extras": []})
        else:
            sections[-1].entries.append({
                "kind": "block", "name": head_flat if compact else "",
                "body": rest if compact else values, "extras": [],
            })
    return [[section for section in sections if section.entries]]


def parse(rows: list[list[str]], sheet: dict) -> list[list[Section]]:
    layout = sheet["layout"]
    if layout == "pairs":
        return parse_pairs(rows, sheet)
    if layout == "stacked_right":
        return parse_stacked(rows, sheet, below=False)
    if layout == "stacked_below":
        return parse_stacked(rows, sheet, below=True)
    return parse_grid(rows, sheet)


def render(title: str, sheet: dict, sections: list[Section], note: str = "") -> str:
    out = io.StringIO()
    out.write(f"# {title}\n\n")
    if note:
        out.write(f"{note}\n\n")
    out.write(
        f"Source: Destiny Data Compendium, `{sheet['tab']}` tab. "
        "Numbers in `[brackets]` are Crucible/PvP values; `↑` marks enhanced perk values.\n\n"
    )
    named = [s for s in sections if s.title]
    if len(named) > 1:
        out.write("Contents: " + " · ".join(s.title for s in named) + "\n\n")
    for section in sections:
        if section.title:
            out.write(f"## {clean(section.title)}\n\n")
        for note in section.notes:
            out.write(f"*{clean(note)}*\n\n")
        for entry in section.entries:
            if entry.get("kind") == "row":
                cells = " | ".join(clean(value) for value in entry["body"])
                out.write(f"- **{clean(entry['name'])}** — {cells}\n")
                continue
            name = clean(entry["name"])
            if name:
                out.write(f"### {name.splitlines()[0]}\n\n")
                trailing = name.splitlines()[1:]
                if trailing:
                    out.write("*" + " · ".join(trailing) + "*\n\n")
            if entry.get("kind") == "block" and not name:
                out.write("\n")
            for body in entry["body"]:
                out.write(clean(body) + "\n\n")
            for extra in entry["extras"]:
                out.write(f"- {clean(extra)}\n")
            if entry["extras"]:
                out.write("\n")
    text = re.sub(r"\n{3,}", "\n\n", out.getvalue())
    text = re.sub(r"(- \*\*[^\n]*)\n\n(?=- \*\*)", r"\1\n", text)
    return text.strip() + "\n"


def write(path: str, text: str) -> int:
    full = os.path.join(REFERENCES, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as handle:
        handle.write(text)
    return len(text)


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "section"


AREA_ORDER = ["Overview", "Bugs", "Subclasses", "Weapons", "Armor", "Artifact", "Mechanics", "Archive"]

AREA_NOTES = {
    "Overview": "Start here only for provenance and compendium-wide caveats.",
    "Bugs": ("Read this before finalizing a build. The game receives no further balance "
             "patches, so these interactions are permanent."),
    "Subclasses": ("Keywords, fragments, aspects, grenades, melees, and supers, one file per "
                   "element. Fragments are filed under their short name: Ember of Ashes is "
                   "`Ashes`, Facet of Purpose is `Purpose`."),
    "Weapons": "Perk and exotic behaviour, including exact damage and buff numbers.",
    "Armor": "Mods, set bonuses, exotic armor, and exotic class item perks.",
    "Artifact": ("One file per selectable artifact. Only one artifact can be equipped at a "
                 "time, so every artifact perk in a build must come from a single file here."),
    "Mechanics": "Stat tiers, ability energy, Armor Charge, champions, and combatant data.",
    "Archive": "Superseded data kept for older seasons and artifacts. Do not quote as current.",
}


def write_index(manifest: list[dict]) -> None:
    out = io.StringIO()
    out.write("# Reference Index\n\n")
    out.write(
        "Generated from the Destiny Data Compendium by `scripts/build_reference.py`. "
        "Read this file first, then open only the reference files a question needs.\n\n"
        "Conventions used throughout: `[brackets]` are Crucible/PvP values, `↑` marks the "
        "enhanced version of a perk, `x1`/`x2` are stack counts, and `|` separates the "
        "values of successive tiers or ranks.\n\n"
    )
    for area in AREA_ORDER:
        files = [item for item in manifest if item["area"] == area]
        if not files:
            continue
        out.write(f"## {area}\n\n{AREA_NOTES[area]}\n\n")
        for item in files:
            out.write(f"- `{item['path']}` — {item['blurb']} ({item['entries']} entries, "
                      f"{item['bytes'] // 1024} KB)\n")
            if item["sections"] and (item["bytes"] > 20000 or item["area"] == "Bugs"):
                out.write("  - Sections: " + " · ".join(item["sections"]) + "\n")
        out.write("\n")
    write("INDEX.md", out.getvalue().strip() + "\n")


def build(sheet: dict, offline: bool) -> list[tuple[str, int, int, list[str], str]]:
    rows = load_rows(sheet, offline)
    per_group = parse(rows, sheet)
    written: list[tuple[str, int, int, list[str], str]] = []
    split = sheet.get("split")
    preamble = sheet.get("preamble", "")

    if split == "group":
        for index, sections in enumerate(per_group):
            label = (sheet.get("group_labels") or [])[index]
            path = f"{sheet['out']}/{slugify(label)}.md"
            title = f"{sheet['title']} — {label}"
            written.append((path, write(path, render(title, sheet, sections, preamble)),
                            sum(len(s.entries) for s in sections),
                            [s.title for s in sections if s.title],
                            f"{label}. {sheet['blurb']}"))
        return written

    flat = [section for sections in per_group for section in sections]
    if split == "section":
        carried: list[str] = []
        for section in flat:
            if not section.entries:
                carried.extend(section.notes)
                continue
            path = f"{sheet['out']}/{slugify(section.title)}.md"
            title = f"{sheet['title']} — {section.title}" if section.title else sheet["title"]
            plain = Section("")
            plain.entries = section.entries
            plain.notes = carried + section.notes
            carried = []
            written.append((path, write(path, render(title, sheet, [plain], preamble)),
                            len(section.entries), [],
                            f"{section.title}. {sheet['blurb']}"))
        return written

    written.append((sheet["out"], write(sheet["out"], render(sheet["title"], sheet, flat, preamble)),
                    sum(len(s.entries) for s in flat),
                    [s.title for s in flat if s.title], sheet["blurb"]))
    return written


def copy_static() -> list[dict]:
    copied = []
    for item in STATIC:
        with open(os.path.join(CURATED, item["source"]), encoding="utf-8") as handle:
            text = handle.read()
        sections = re.findall(r"^## (.+)$", text, re.M)
        copied.append({
            "path": item["out"], "bytes": write(item["out"], text),
            "entries": len(re.findall(r"^### ", text, re.M)),
            "tab": item["tab"], "area": item["area"], "blurb": item["blurb"],
            "sections": sections,
        })
    return copied


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="rebuild from cached CSVs")
    args = parser.parse_args(argv[1:])

    if os.path.isdir(REFERENCES):
        shutil.rmtree(REFERENCES)

    manifest = []
    for sheet in SHEETS:
        for path, size, entries, sections, blurb in build(sheet, args.offline):
            manifest.append({"path": path, "bytes": size, "entries": entries,
                             "tab": sheet["tab"], "area": sheet["area"],
                             "blurb": blurb, "sections": sections})
            print(f"  {path:52} {size:7} bytes  {entries:4} entries")

    for item in copy_static():
        manifest.append(item)
        print(f"  {item['path']:52} {item['bytes']:7} bytes  {item['entries']:4} entries")

    write_index(manifest)
    with open(os.path.join(CACHE, "manifest.json"), "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
    print(f"\n{len(manifest)} file(s) written to {os.path.relpath(REFERENCES, PLUGIN_ROOT)}")
    print(f"Source: {SHEET_URL}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
