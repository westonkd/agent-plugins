# Known Bugs and Unintended Interactions

Hand-maintained, unlike the rest of `references/`, which is generated from the
compendium. Last reviewed 2026-08-31.

Destiny 2's final content update, Monument of Triumph (Update 9.7.0), shipped
2026-06-09. Update 9.7.0.2 was the last gameplay bug-fix pass and 9.7.0.3
(2026-07-07) was the last hotfix of any kind. Bungie's stated policy after that
point is that major issues with abilities, armor sets, bosses, or maps get
**disabled rather than fixed**, because there is no team left to fix them. So an
interaction listed here as live is expected to stay live, and a build may lean on
it. Only entries present in Monument of Triumph or later are listed.

Status vocabulary used below:

- **Live** — working now, in both PvE and PvP unless stated.
- **Live in PvE, disabled in Crucible** — Bungie switched the perk off in PvP only.
  It remains fully functional in strikes, raids, dungeons, and patrol.
- **Patched** — already fixed or removed. Do not build around it.

Numbers in this file come from the compendium files named in each entry; the
narrative claims come from the sources listed at the bottom. Anything marked
"unverified" has not been measured, and should be tested before a build depends
on it.

## Live and worth building around

### Supercyclical counts non-Super damage as Super damage

Iron Battalion (Iron Banner) 4-piece, `armor/set-bonuses.md`. Status: **live**.

Supercyclical has two triggers: kills scored while a Super is active refund Super
energy when the Super ends, and **kills scored with Super damage while not in a
Super refund it directly**. The second trigger is the interesting one, because
"Super damage" is a damage classification, not a check for being in a Super, and
some things carry that classification outside of a Super.

The confirmed case is **Astrocyte Verse** on Warlock. The compendium records that
its free horizontal Dark Blink "releases 4 [2] Seekers that are functionally
identical to Nova Warp's and scale with Super Damage"
(`armor/exotics/warlock.md`). Those Seeker kills satisfy Supercyclical without any
Super being cast; reporting at the time put it at roughly 66% of a Super regenerated
when combined with actually casting one. As of the last community testing this is
the only out-of-Super source players had found that works.

A second candidate the same mechanism predicts, not yet reported by anyone:
**Rime-coat Raiment** on Warlock. Its Bleak Domain perk surrounds a Bleak Watcher
turret with 4 Medium Stasis Crystals, and the compendium states flatly that
**"Stasis Crystals count as Super Ability Damage"** (`armor/exotics/warlock.md`).
Crystals elsewhere do not carry that classification: Glacier Grenade crystals deal
Stasis *Grenade* damage (`subclasses/stasis.md`), and crystals only become Super
damage inside Glacial Quake. Rime-coat is the one source that produces
Super-classified damage continuously outside a Super, and the crystals respawn every
15 seconds, so shatter kills near the turret should feed Supercyclical exactly the
way Dark Blink Seekers do. **Unverified** — no source reports testing it. Test it by
equipping the 4-piece with no Super cast, killing adds purely through crystal
shatters, and watching whether the Super bar moves. Bleak Watcher is available on
Prismatic Warlock as well as Stasis, so it slots into either.

Stacking cases reported alongside it, all in-Super and all live:

- **Shards of Galanor** refunds up to 50%, and Supercyclical's up-to-33% stacks on
  top, for about 83% back per cast.
- **Gathering Storm with Raiju's Harness**, fed close-range kills, lands at roughly
  80–100% refunded.
- **Nova Bomb with Skull of Dire Ahamkara**, detonating one bomb and killing adds
  with the second, can fully refund.

Refund scale is roughly 5% at one kill up to about 33% at six, and the refund cap
resets on each Super cast (`armor/set-bonuses.md`). Any roaming Super that reliably
kills six targets pays out the maximum.

Practical read: on Warlock, Astrocyte Verse plus Iron Battalion is a Super engine
that needs no Super kills at all, and Rime-coat Raiment is the first thing to test
for a second one. On Hunter and Titan, pick the Super that racks up
six kills fastest, then stack an exotic that already refunds.

### Overflowing Coffers massively overtunes Tangle damage

Yearning Echo (Grasp of Avarice) 4-piece, `armor/set-bonuses.md`.
Status: **live in PvE, disabled in Crucible**.

At x5 Untold Greed or higher, the 4-piece gives Strand Tangles **350% increased
damage**, and the compendium notes it affects Whirling Maelstrom too. Bungie
publicly called the Tangle damage "more than intended" and disabled the bonus for
Pantheon on 2026-06-12; the Crucible-wide disable followed on 2026-07-01. The
compendium currently marks it as disabled in Crucible only, so it remains the
strongest Strand damage amplifier available in general PvE.

The same 4-piece also inflates elemental pickups well beyond their normal value:
Firesprites and Void Breaches +120%, Ionic Traces to 21% grenade/melee and 27%
class energy, Stasis Shards from 10% to 36% melee energy (additive with Hunger's
+60%, totalling 42.5% per shard). In Crucible this was the Stasis Titan Super-spam
engine that got it switched off.

### Crystocrene grants Frost Armor in combat

Crystocrene (Europa) 4-piece "From the Storm", `armor/set-bonuses.md`.
Status: **live in PvE, disabled in Crucible**.

The bonus is written to require 12 seconds of neither dealing nor taking damage,
then to stack Frost Armor every 3 seconds up to x5. Players found it proccing in
combat as well, which Bungie confirmed was not intended. Rather than fix it, the
bonus was disabled in Crucible on 2026-08-01 and left alone everywhere else, which
makes it one of the cheapest sources of standing damage resistance in PvE.

### Bountiful Munitions prints Special ammo

Cyberserpent Null (Gambit) 4-piece, `armor/set-bonuses.md`.
Status: **live in PvE, disabled in Crucible**.

Special ammo progress per kill while Adrenal Rush is up: +3% rank-and-file, +16%
elite, +24% elite Taken. The compendium adds that destroyable entities and
Constructs also count for +16%, which is the part that turned into effectively
infinite Special ammo in PvP and got it disabled there on 2026-07-29. In PvE it is
untouched and remains a strong Special-heavy ammo economy.

### Bittersweet heals more than its own table

Duality dungeon 4-piece, `armor/set-bonuses.md`.
Status: **live in PvE, disabled in Crucible**.

Stowing a weapon converts Built Bitter stacks into healing, up to a full heal at x8
or more. The compendium flags outright that "there are some weird inconsistencies
that can result in MUCH higher healing values" than the listed per-stack table. The
Crucible disable landed 2026-07-01; PvE keeps both the intended healing and the
inconsistency.

### Blastwave Striders fires without self-damage

Hoarfrost-Z, `armor/exotics/titan.md`. Status: **live**, unverified as intentional.

Blastwave Striders is documented to trigger on Shiver Strike damage, Howl of the
Storm damage, or explosive **self**-damage at full charge. The compendium notes that
**Explosive Head, Explosive Payload, and Timed Payload trigger it despite not
dealing self-damage**. That turns any legendary weapon with one of those perks into
a free trigger for the wave, the Freeze, and x5 Frost Armor, with no self-harm.

### Zoetic Lockset ignition chain

Sundered Doctrine dungeon final boss. Status: **live**.

A Solar Warlock running Dawn Chorus, Incinerator Snap, Ember of Char, Ember of
Ashes, and the Solar Fulmination artifact perk can start a self-sustaining ignition
chain on the Lockset: the boss ignites, which ignites the adjacent Lockset segment
through stacked Scorch, which ignites back. It one-phases the encounter with the
player behind cover, which makes it a solo AFK farm for Sundered Doctrine loot.
This is a build interaction rather than a geometry exploit, so the fragment and perk
values in `subclasses/solar.md` and `artifact-perks/` apply as written.

## Live, but working against you

These are documented failures where an item does less than its description claims.
Do not credit them in a build.

- **Better Already** (armor mod) does not stack, despite the in-game tooltip
  saying it does. `armor/mods.md`
- **Wraithmetal Mail** (Hunter exotic) grants no Class stat, contrary to its
  description. `armor/exotics/hunter.md`
- **Iron Lord's Vigor** (artifact perk) grants no damage resistance, contrary to
  its description. `artifact-perks/`
- **Spark of Frequency**'s tooltip claims it increases the fragment's effects; it
  does not, at least for the reload bonuses. `subclasses/arc.md`
- **Hypercritical** (activity modifier) does not decrease damage despite stating
  so. `mechanics.md`
- **Disruption** is bugged: disrupted combatants no longer take the 25% damage
  penalty for 5 seconds. Overload stuns still work; the damage debuff does not.
  `mechanics.md`
- **Deterministic Chaos** cannot practically apply Weaken: optimising its ammo
  refill makes the 32nd-shot Weaken unreachable, so its own traits fight each
  other. `weapons/exotics/power-weapons.md`
- **Suspend on bosses** marks them as afflicted without applying the effects, so
  suspend-payoff perks read as active while the boss ignores the suspension.
  `subclasses/strand.md`

## Patched or removed

- **Ward of Dawn boss launching.** Crossbow bolts stuck into the Ward's central
  core turned it into a physical launcher that threw Insurrection Prime, Morgeth,
  and Atheon off the map. Fixed in 9.7.0.2.
- **"The Stackening" artifact stacking.** Queuing into Trials and then slotting one
  artifact perk into every column stacked it, most notoriously Thunderous Retort
  and Pack Tactics, one-shotting bosses with any single-use Super. Fixed in 9.7.0.2.
- **Truth ammo.** Held 14 rockets; reduced to 10 in 9.7.0.2.
- **Divinity in Pantheon.** Divinity could damage Insurrection Prime outside the
  damage phase; the 9.7.0.3 fix removed Divinity from that encounter entirely.
- **Phantom Surge** failing on weakened or tethered targets while Stylish Executioner
  was active, and projectiles passing through Ward of Dawn in PvP, were both fixed
  in 9.7.0.3.
- **Disjunction** was disabled in all Crucible playlists on 2026-08-01. It remains
  in private matches. Not a build concern, but it removes a map from PvP planning.

## Keeping this current

The game receives no further balance patches, so entries move only when Bungie
disables something server-side. Two checks catch that: the compendium marks a
switched-off perk inline with `DISABLED IN CRUCIBLE`, visible via
`grep -rn "DISABLED" references/`, and the @Destiny2Team account announces each
disable. If a perk here stops matching the compendium, trust the compendium.

## Sources

- Bungie, [Monument of Triumph and Update 9.7.0 Support Guide](https://help.bungie.net/hc/en-us/articles/49848696022548-Destiny-2-Monument-of-Triumph-and-Update-9-7-0-Support-Guide)
- Bungie, [Destiny Server and Update Status](https://help.bungie.net/hc/en-us/articles/360049199271-Destiny-Server-and-Update-Status)
- @Destiny2Team, [Overflowing Coffers disabled for Pantheon](https://x.com/Destiny2Team/status/2065239573530112270) and [Crucible set bonus disables](https://x.com/Destiny2Team/status/2072443825445048637)
- Paul Tassi, Forbes, [Players Discover Hugely Overpowered Armor Set Before Closure](https://www.forbes.com/sites/paultassi/2026/07/03/destiny-2-players-discover-hugely-overpowered-armor-set-before-closure/) (2026-07-03)
- Paul Tassi, Forbes, [How To Launch Destiny 2 Raid Bosses Into The Sun](https://www.forbes.com/sites/paultassi/2026/06/16/how-to-launch-destiny-2-raid-bosses-into-the-sun/) (2026-06-16)
- Paul Tassi, Forbes, [The Patch Notes For Destiny 2's Final Hotfix Ever](https://www.forbes.com/sites/paultassi/2026/07/07/the-patch-notes-for-destiny-2s-final-hotfix-ever/) (2026-07-07)
- Boostmatch, [Destiny 2 Final Update: Bugs, Fixes & What to Do Now](https://boostmatch.gg/blog/destiny-2/articles/destiny-2-final-update-monument-of-triumph-bugs-guide) (2026-06-25), for the 9.7.0.2 fix list
- GameRant, [Disabling Two Armor Sets Permanently](https://gamerant.com/destiny-2-disable-armor-sets-grasp-avarice-duality/) (2026-07-01), [Disabling One Armor Set Permanently](https://gamerant.com/destiny-2-armor-set-gambit-crucible-iron-banner-disable/) (2026-07-29), [Disabling Another Armor Set and Map](https://gamerant.com/destiny-2-disable-europe-armor-set-disjunction-crucible-map/) (2026-08-01)
- GameRant, [Players Can Solo AFK Farm a Dungeon Boss](https://gamerant.com/destiny-2-solo-afk-farm-sundered-doctrine-zoetic-lockset/)
- gamer.org, [Disables Two Armor Set Bonuses in Crucible](https://www.gamer.org/destiny-2-disables-monument-of-triumph-armor-sets-pvp/) (2026-07-02) and [Cyberserpent Null Bonus Disabled](https://www.gamer.org/destiny-2-cyberserpent-null-armor-set-bonus-disabled/) (2026-07-30)
