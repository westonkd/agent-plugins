# destiny-2-builds

A plugin that turns an agent into a Destiny 2 build advisor, working from measured
in-game values rather than recall.

> **Provenance:** every reference file is generated from the community-maintained
> [Destiny Data Compendium](https://docs.google.com/spreadsheets/d/1WaxvbLx7UoSZaBqdFr1u32F2uWVLo-CJunJB4nlGUE4/edit),
> a spreadsheet of measured Destiny 2 numbers. All 21 tabs are pulled, including the
> archived ones. See [`NOTICE`](NOTICE) for attribution. Unofficial; not affiliated
> with Bungie.

Destiny 2 no longer receives content updates, so the data is stable. The skill advises
on loadouts and explains interactions; it does not apply changes anywhere.

## Layout

```
plugin.json                          Agent Plugins 1.0.0 manifest
.claude-plugin/plugin.json           Claude Code manifest (same metadata)
scripts/build_reference.py           Deterministic converter (Python stdlib only)
curated/known-bugs.md                Hand-maintained; copied into references/ on build
scripts/.cache/                      Downloaded CSVs — gitignored
skills/destiny-2-builds/
  SKILL.md                           Entrypoint: lookup routes and the build workflow
  references/
    INDEX.md                         Every file, its blurb, entry count, and sections
    known-bugs.md                    Bugs and unintended interactions, MoT onward
    compendium-overview.md           Compendium front page: credits and errata
    subclasses/<element>.md          Arc, Solar, Void, Stasis, Strand, Prismatic
    class-abilities.md               Dodges, barricades, rifts, and their cooldowns
    weapons/perks/<section>.md       Traits, mods, intrinsic frames, origin traits
    weapons/exotics/<slot>.md        Exotic weapons by ammo slot
    armor/mods.md                    Armor mods by slot, with energy costs
    armor/set-bonuses.md             2-piece and 4-piece armor set bonuses
    armor/exotics/<class>.md         Exotic armor by class
    armor/exotic-class-items/        Spirit of ... perks, one file per perk column
    artifact-perks/<artifact>.md     One file per selectable artifact
    mechanics.md                     Stats, ability energy, Armor Charge, champions
    archive/                         Superseded seasons and pre-rework mechanics
```

## Progressive disclosure

The compendium is roughly 900 KB of dense text, so the skill never loads it whole.
`SKILL.md` is small and always in context; it routes to `references/INDEX.md`, which
lists each file with a one-line blurb, its entry count, and its section names; only
the files a question needs get opened. Reference entries are `###`-headed by name, so
a single `grep -ril "<perk name>" references/` lands on the right block.

## Regenerating

```shell
python3 scripts/build_reference.py            # fetch all tabs, rebuild references/
python3 scripts/build_reference.py --offline  # rebuild from scripts/.cache/
```

`references/` is cleared on every run, so hand-written material lives in `curated/`
and is copied back in and indexed after the generated files are written.
`curated/known-bugs.md` is the one such file today; it is researched by hand from
Bungie announcements and community reporting, and carries its own sources and
review date.

The script reads each tab through the spreadsheet's public CSV endpoint. Because the
tabs are hand-laid-out grids rather than normalized tables, each one carries a small
layout description in `SHEETS` that names the columns holding entry names and text.
If a tab is re-laid-out upstream, that entry is what needs updating.

## Install

```shell
/plugin marketplace add westonkd/agent-plugins
/plugin install destiny-2-builds@agent-plugins
```
