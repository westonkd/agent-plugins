---
name: destiny-2-builds
description: Optimize Destiny 2 builds and loadouts using measured in-game values from the Destiny Data Compendium. Use when a player asks what to run, how to improve a build, which fragments, aspects, armor mods, set bonuses, artifact perks, exotic armor, or exotic weapons to pair, how a perk or ability actually works, what stats to hit, or how ability energy, Armor Charge, champions, and combatant scaling behave. Covers Arc, Solar, Void, Stasis, Strand, and Prismatic for Hunter, Titan, and Warlock, in both PvE and PvP, plus the bugs and unintended interactions that are now permanent because the game receives no further balance patches.
license: MIT
metadata:
  source: Destiny Data Compendium
  source-url: https://docs.google.com/spreadsheets/d/1WaxvbLx7UoSZaBqdFr1u32F2uWVLo-CJunJB4nlGUE4/edit
---

# Destiny 2 build optimization

Destiny 2 stopped receiving content updates, so the numbers bundled here are stable.
Every value in `references/` comes from the community-maintained Destiny Data
Compendium. Treat those files as the source of truth and prefer them over recall.

## Finding data

`references/INDEX.md` maps every reference file to what it contains, how many
entries it holds, and which sections it has. Read it first, then open only the
files a question actually needs. Do not load the whole reference tree.

Fastest paths to a specific answer:

- A named perk, mod, fragment, aspect, or exotic: `grep -ril "<name>" references/`
  then read the surrounding `###` block in the file that matches.
- Everything an element can do: `references/subclasses/<element>.md`.
- A number about stats, cooldowns, champions, or combatants: `references/mechanics.md`.
- Bugs and unintended interactions that change what a build is worth:
  `references/known-bugs.md`. Check it whenever a set bonus, exotic, or Super
  economy is central to the answer.
- Anything under `references/archive/` describes past seasons. Never quote it as current.

Fragments are filed under their short name, so Ember of Ashes is `### Ashes` and Facet
of Purpose is `### Purpose`. Search for the short name, and use the file the fragment
belongs to for its full name.

Reading conventions used by the source, which carry into every file:

- `[brackets]` are the Crucible/PvP value; the unbracketed number is PvE.
- `↑` marks the enhanced version of a weapon perk or the tuned (100+) stat benefit.
- `x1`, `x3` are stack counts; `|` separates the values of successive ranks or tiers.
- `?` means the compendium authors could not verify that figure. Pass that uncertainty
  on rather than presenting a `?` value as measured.

## Build legality

A loadout that cannot be equipped in game is worthless no matter how well the synergy
reads. These limits are hard. Decide the class, the subclass, and the artifact before
picking anything else, and check every later pick against them.

**One class.** Hunter, Titan, or Warlock, chosen once. Each subclass file holds all
three classes, so a `###` entry is legal only when it sits under that class's `##`
section. Grenades and fragments are shared by every class; melee abilities, supers,
aspects, and subclass class abilities are not. Exotic armor comes from
`references/armor/exotics/<class>.md` and nowhere else. When in doubt about who owns
an entry, print its enclosing section:

```
awk -v n="Ascension" '/^## /{s=substr($0,4)} $0=="### "n{print FILENAME" -> "s}' \
  references/subclasses/*.md references/armor/exotics/*.md
```

**One subclass.** Aspects, fragments, grenade, melee, super, and class ability all come
from a single `references/subclasses/<element>.md`. No Solar fragment on a Void build.
Prismatic is its own subclass, not a licence to mix: its fragments are the Facets in
`subclasses/prismatic.md`, and its grenades, melees, supers, and aspects are only the
ones listed under that class's section in that same file. An aspect that appears in
`subclasses/arc.md` but not in the Prismatic pool cannot be run on Prismatic.

**Two aspects.** Fragment slots come from those two aspects. The compendium does not
record slot counts, so never list more than five fragments, and say the usable count
depends on the aspects chosen.

**One exotic armor piece.** Exactly one, in one slot. An exotic class item is that one
piece and rules out an exotic helmet, gauntlets, chest, or boots. Its two Spirit perks
are one from `armor/exotic-class-items/first-perk-column.md` and one from
`armor/exotic-class-items/second-perk-column.md`, each either class-agnostic or from
the build's own class section. Two perks from the same column is not a roll that exists.

**One exotic weapon.** At most one across the kinetic, energy, and power slots, and the
other two weapons are legendary. An exotic weapon plus an exotic armor piece is the
limit; a second exotic in either category is not equippable.

**One artifact.** Since Monument of Triumph a player selects a single artifact, so every
artifact perk in a build comes from one file in `references/artifact-perks/`. Name that
artifact in the answer. Never combine perks from two of those files, and never pull from
`references/archive/` for a current build.

**Slot-correct armor mods.** A mod is only equippable in the slot it is filed under in
`armor/mods.md`, and its energy cost has to fit the piece. One set bonus at 4 pieces, or
two at 2 pieces each; with an exotic occupying a slot only four armor pieces remain, so
a 4-piece bonus and a 2-piece bonus cannot both be active.

## Building a loadout

Work in this order, and look up each piece rather than assuming it.

1. **Pin down the request.** Class, subclass or element (or free choice), activity and
   whether it is PvE or PvP, the goal (add clear, boss damage, survivability, ability
   spam, dueling), and any constraint: gear the player owns, an exotic they want to
   build around, a weapon type they enjoy.
2. **Pick the engine.** Choose the one loop the build is built to repeat, for example
   grenade regeneration into detonations, melee cycling, weapon damage windows, or
   Armor Charge economy. State the engine explicitly; every later choice serves it.
3. **Assemble the pieces**, checking each against the references:
   - Aspects and fragments from `references/subclasses/<element>.md`, including the
     fragment stat penalties, which are listed per fragment.
   - Exotic armor from `references/armor/exotics/<class>.md`, or one exotic class item
     perk from each file in `references/armor/exotic-class-items/`.
   - Armor mods from `references/armor/mods.md`, respecting the energy cost per piece.
   - An armor set bonus from `references/armor/set-bonuses.md` when 2 or 4 pieces fit.
   - Weapons: exotic behaviour in `references/weapons/exotics/`, legendary perks and
     origin traits in `references/weapons/perks/`.
   - Artifact perks from one file in `references/artifact-perks/`, chosen for the
     champion-stun options the activity requires. Pick the artifact first, then take
     every perk from that file.
4. **Set the stats.** Stat effects, their tuned 100–200 range, and the ability
   regeneration and cooldown scaling live in `references/mechanics.md` and
   `references/class-abilities.md`. Recommend a stat priority tied to the engine, not
   a generic spread, and say what each point buys.
5. **Verify the interactions.** Confirm each pairing actually triggers: matching
   damage type, the right verb (jolt, scorch, weaken, slow, unravel), ability kill
   versus weapon kill, and cooldowns that keep pace with each other. Ability energy
   rules, chunk scalars, and Armor Charge behaviour are in `references/mechanics.md`.
6. **Check the activity.** For endgame content, cross-check champion coverage,
   activity modifiers, and combatant damage scaling in `references/mechanics.md`.
7. **Check `references/known-bugs.md`.** Destiny 2 gets no further balance patches,
   so its live bugs are permanent and several of them are build-defining: perks that
   pay out far above their tooltip, perks Bungie disabled in Crucible but left
   working in PvE, and perks that quietly do nothing. Fold the ones that help into
   the build, name them as bugs rather than intended behaviour, and drop anything
   the file lists as not working. What is patched there is dead; do not plan around it.
8. **Run the legality check.** Walk the build once more against every rule in
   "Build legality": one class, one subclass, two aspects, at most five fragments, one
   exotic armor piece, at most one exotic weapon, one artifact, mods in the right slots.
   Anything that fails is replaced with a legal pick from the same file, not explained
   away.

## Answering

Deliver a build sheet the player can act on:

- A header line naming the class, the subclass, and the artifact the build assumes.
- Subclass, aspects, fragments (call out any stat penalties).
- Exotic armor and why it is the pick.
- Weapons, with the perks that matter and their role in the loop.
- Armor mods per slot, and the set bonus if one is used.
- Stat priorities.
- Artifact perks worth slotting, all from the named artifact.
- The gameplay loop in two or three sentences: what to do first, what it feeds.

Quote real numbers from the references (durations, percentages, stack counts) instead
of vague claims, and name the file a number came from when it is load-bearing.
Offer variants when the player's constraints leave room, and say plainly when a
requested combination does not work and what to run instead.

This skill advises. It does not edit game files or third-party build tools, and
nothing here needs to be applied anywhere. Produce the recommendation and stop.

## Regenerating the data

`scripts/build_reference.py` at the plugin root rebuilds every file under
`references/` from the compendium spreadsheet. Run it only when asked to refresh
the data, not while answering a build question.
