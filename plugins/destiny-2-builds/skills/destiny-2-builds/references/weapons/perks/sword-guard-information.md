# Weapon Perks, Mods, and Traits — Sword Guard Information

Source: Destiny Data Compendium, `Weapon Perks` tab. Numbers in `[brackets]` are Crucible/PvP values; `↑` marks enhanced perk values.

### Sword Guarding

[Guard] projects an energy shield in front of the user that constantly drains over time, the rate of which is determined by Guard Endurance.
Applies a 0.85x Movement Speed Multiplier while guarding.
Attacks that strike the shield deal decreased damage, with the damage resistance being determined by Guard Resistance.
Scales from 82.5% [52.5%] to 95% [65%] Damage Resist based on the Guard Resistance stat.

### Charge Rate

Charge Rate determines the delay before Sword Energy is regenerated, and the rate at which it is regenerated.
Using any Sword Energy restarts Energy Regeneration Delay, regardless of which equipped Sword drained it.
Sword Energy Regeneration Delay, in seconds:
10 CR = 2.65s | 30 CR = 2.45s | 40 CR = 2.25s | 70 CR = 1.65s | 100 CR = 1.05s
Sword Energy Regeneration Rate = 1.35 - (Charge Rate x 0.01)

### Guard Endurance

Sword Guard passively drains Sword Energy. Guarding against any damage pauses passive drain for ? seconds.
Sword Energy Drain, in seconds:
0 GE = 2.5s | 40 GE = 5s | 60 GE = 6.35s | 90 GE = 9s | 100 GE = 12.5s
Stronghold and Infinite Guard Swords do not drain any Sword Energy.

### Guard Resistance

Guard Resistance determines the amount of Damage Resist the Sword Guard provides against blocked attacks.
Internally, this is the Stability stat, which means that effects that increase Stability, such as Rally Barricade, will increase the Damage Resist.
Guard Damage Resist = 82.5% [52.5%] at 0 Resistance to 95% [65%] at 100 Resistance.
Damage Resist = ???????? | 52.5 + (0.125 x Stat)
