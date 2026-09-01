# Artifact Perks — Implement of Curiosity (Reclamation)

Only one artifact can be equipped at a time. Every artifact perk in a build must come from this one file.

Source: Destiny Data Compendium, `Artifact Perks` tab. Numbers in `[brackets]` are Crucible/PvP values; `↑` marks enhanced perk values.

*Kinetic | Solar | Stasis | Strand ⯁ Bow | Sword | Micro-Missiles*

### Fever and Chill

Upon scoring multiple Precision Hits within 3 seconds of each:
Solar Weapons | Grants Radiant for 10+5 seconds.
Stasis Weapons: Grants a stack of Frost Armor.
Incurs a 1.5s cooldown between triggers.
Additional hits during this time do not count.
Precision Hits trigger:
(25% of Magazine Size) + 1, rounded down
Mag to Crits Requirement:
Bows = 3 Crits | 3 Mag = 1 Crit
4–7 Mag = 2 Crits | 8–11 Mag = 3 Crits
12–15 Mag = 4 Crits | 16–19 Mag = 5 Crits
20–23 Mag = 6 Crits | 24-27 Mag = 7 Crits
28–31 Mag = 8 Crits | 32–35 Mag = 9 Crits
36–39 Mag = 10 Crits | 40–43 Mag = 11 Crits

### Threaded Blast

Upon destroying a Tangle with Strand Damage:
Explosion has an additional damage instance that deals 288 [?] damage, down to 75% damage over a 17 meter radius.
Additional damage counts as Tangle Damage for all interactions.

### Radiant Shrapnel

Upon dealing Weapon Damage equal to 10% of an Enemy's Combined Health+Shields while Radiant, or upon killing a Scorched Combatant with a Weapon:
Target releases 1 Solar Shrapnel that deals 54 [?] Impact Damage and up to 289 [20] Explosive Damage, inflicting x20+0 Scorch over ? meters.
Incurs a 1 second cooldown between Shrapnel spawns.
Shrapnel is slightly homing, and often misses the enemy it spawns on.

### Elemental Benevolence

Upon bestowing an Elemental Buff to allies:
~15?% Class Ability Energy.
Incurs a ? second cooldown PER ALLY after activation.

### Cauterized Darkness

Upon inflicting a Darkness Debuff on a Non-Boss Combatants:
75% Increased Solar Damage dealt.
Indicated by getting Yellow Numbers on Solar Damage.
Stacks with other Weaken sources.
Incurs a 2? second cooldown between additional Darkness Debuffs inflicting the Cauterized Darkness debuff.

### Shieldcrush

While Frost Armor, Void Overshield, or Woven Mail are active:
?% [?%] Additional Base Melee Recharge Rate
50% [5%] Increased Powered Melee Damage.
Also increases Super Melee Damage and Ignition Damage.
While Amplified or Radiant are active:
?% [?%] Additional Base Grenade Recharge Rate
25% [5%] Increased Grenade Damage.
Grapple Melee instead receives 12% Increased Damage for each half of the perk.

### Frost Renewal

On Shield Break from Combatant Damage, while Frost Armor is active:
Releases a Stasis Burst over 10 meters.
Stasis Burst freezes enemies and grants a stack of Frost Armor to the user and allies in range.

### Elemental Daze

Upon stunning a Champion with an Elemental Weapon:
Triggers an Elemental-Matching Explosion that deals up to 315 Elemental Damage and inflicts an Elemental Debuff over 5 meters, down to 0% damage.
Arc: Jolt | Solar: Ignition | Void: Volatile
Stasis: Freeze | Strand: Sever
Has no effect on Kinetic Weapons.

### Elemental Overdrive

Upon picking up a Elemental Pickup:
22% [?%] increased Pickup-Matching Weapon Damage for 7 seconds.
Displays as Weapon Surge despite stacking multiplicatively with it.

### Horde Shuttle

Dealing Weapon Damage equal to 10% [100? HP] of an Unraveled Enemy's Combined Health + Shields spawns a Threadling.
Incurs a 0.5 second cooldown between Threadlings.
Threadlings inflict Sever upon dealing damage.

### Shoulder to Shoulder

Upon dealing sustained Precision Damage while within 15 meters of 2 allies:
25% Damage Resist (Resist x2) for 10? seconds

### Tangled Web

Upon killing a Strand-Debuffed Combatant:
Triggers a Suspending Blast.
Only triggers when a Tangle is created.

### Refresh Threads

Upon picking up a Super-Matching Elemental Pickup:
25% Ability Energy to the least-charged Ability.
Also triggers with Tangles on Strand.
Incurs a 0.3 second cooldown between triggers.
Does not trigger on Abilities that have at least 1 Charge ready.
Does not work while Acrobat Dodge is equipped on Prismatic.

### Elemental Coalescence

Upon scoring a random, Pickup-based amount of kills:
Spawns a Super-Matching Elemental Pickup.
Kills needed to trigger vary per Elemental Pickup.
Firesprites, Void Breaches: 4–7 kills.
Ionic Trace, Stasis Shards, Tangles: 9–11 kills.
Triggers the global cooldown for Firesprites, Void Breaches, and Tangles.
Kills scored during the cooldown do not count for the next pickup.
Matching the Damage Type to the Super Element has no bonus effects.

### Frigid Glare

Upon scoring a Precision Kill with a Stasis Weapon while Frost Armor is active:
Triggers a Freezing Burst on Enemy Death Location.
Freezing Burst affects enemies within 7 meters.

### Pack Tactics

Dealing Threadling Damage grants a stack of Pack Tactic for 10 seconds, up to a maximum of 2 stacks.
Dealing additional Threadling damage refreshes the buff duration.
Pack Tactics x1 | 15% increased Threadling Damage.
Pack Tactics x2 | 30% Increased Threadling Damage.
Threadling Damage stuns Unstoppable Champions.
Each Threadling hit while at x2 stacks will increase Threadling Damage by 1.03x until buff expires.

### That Fresh Bullets Smell

On Ammo Brick Pickup:
Grants Kinetic Weapon Surge for 11 seconds.
Special Brick = x2 Kinetic Weapon Surge.
Heavy Brick = x3 Kinetic Weapon Surge.
Does not overwrite stronger Weapon Surges.

### Iron Lord's Vigor

Upon scoring 3 Sword Kills within 3 seconds of each:
Grants +3 Ammo.
Praxic Blade and Ergo Sum receive +1 Ammo instead.
Does not grant any Damage Resist, contrary to description.

### Semi-Auto Striker

While at <2 Armor Charges:
Upon scoring multiple Precision Hits within 3 seconds of each with Bows, Sniper Rifles, or Scout Rifles:
Grants an Armor Charge.
Precision Hit Requirement:
Scouts = 5 | Bows = 3 | Snipers = 2

### Energy Acceleration

Upon scoring 2 non-simultaneous Micro-Missile damage instances within 3 seconds of each or a Micro-Missile Kill:
Target releases a Kinetic Shockwave that deals 120 [20] Kinetic Damage and stuns Unstoppable Champions over 7 meters.
Shockwave has no falloff.
Incurs a 2 second cooldown between activations.

### Argent Quiver

While Armor Charge is active:
Reloading a bow grants 3 stacks of Godslayer Broadheads.
Stowing removes all stacks.
Upon firing while Godslayer Broadhead is active:
Consumes 1 stack of Godslayer Broadheads to grant increased damage and +? Reload Speed.
Primary = 35% increased damage to Combatants.
Heavy = 25% increased damage to Combatants.
Stacks with everything.
