# Why the PRD / DESIGN / ADR pattern is shaped this way

This is the rationale behind the scaffold `init_skill.sh` produces. Read it before filling
in a scaffold or explaining the pattern to someone — the goal is to apply the shape
correctly, not just to have the right files on disk.

## Why SKILL.md stays thin

SKILL.md is the thing loaded into context every time the skill is invoked. Anything written
there is a permanent context-budget tax paid on every use, regardless of whether that
particular task needed it. Putting the problem statement, architecture, and decision
history in `references/` instead means the agent pays for them only when it actually opens
those files — progressive disclosure, not a wall of upfront text. A thin SKILL.md is also a
single-source-of-truth device: if the mission statement lived in two places (SKILL.md and
PRD.md), they would drift the first time one got updated and not the other. SKILL.md states
the mission once and points elsewhere for everything else.

## Why PRD.md carries a status blockquote

A PRD that accumulates edits over months turns into a document where the "current truth" is
buried somewhere in a long scroll, indistinguishable from superseded reasoning unless you
diff the whole history. The status blockquote at the top is a deliberate exception to
"don't repeat yourself": it exists specifically so a reader — human or agent — never has to
reconstruct current state from the full document. It should name the load-bearing decisions
made so far and flag which earlier assumptions in the body are now stale, rather than
silently deleting or rewriting them out of the narrative sections below.

## Why DESIGN.md starts as a stub

Problem statements can usually be written on day one; architecture generally can't — it's
discovered while building. Filling DESIGN.md in prematurely produces a document with false
authority that gets ignored or actively misleads once reality diverges from the plan.
Leaving it as a one-line stub is intentional: its presence signals "architecture notes
belong here," and it costs nothing to leave empty until there's something true to say.
Don't delete it for being empty, and don't feel obligated to pad it before that point.

## Why ADRs are append-only — superseded, never deleted

The point of an ADR log is to answer "why is it built this way?" and "did we already try
that?" for someone arriving later. Deleting an old ADR when a decision changes erases
exactly the information future readers need most: that the rejected approach was in fact
tried, and why it didn't work out. Instead, a superseding ADR is added and the old one gets
a note under its title pointing at the new file — the old reasoning stays legible, just
marked as no longer current. This turns the ADR directory into a genuine historical log
instead of a mutable "current state" document (that's what DESIGN.md is for).

## Why filenames are timestamp-prefixed slugs

`<YYYYMMDDHHMMSS>_<slug>.md` gives correct chronological ordering for free in any file
listing, in any tool, without a separate index file that could go stale or need merging
across branches. It also sidesteps filename collisions between similarly-titled decisions
and decouples ordering from the title text, so renaming a decision's title later doesn't
reshuffle history. The generator script (`new_adr.sh`) computes the timestamp and slug
mechanically rather than asking an agent or human to compute them by hand, which is what
actually makes "always timestamp-prefixed, always consistently formatted" hold up over
time.

## Why a script generates ADRs instead of writing the file by hand

A script guarantees every ADR has the same fields in the same order regardless of who or
what is writing it, guarantees the timestamp is actually correct (not guessed by an LLM),
and gives you exactly one place to fix the template if the schema ever needs to change. It
also makes the "never delete, only supersede" convention easy to follow correctly, since the
collision guard means you can never accidentally overwrite a prior record just by picking a
similar title.

## Applying the pattern well, not just mechanically

- Keep the PRD status blockquote current — treat it as maintenance work, not optional
  polish.
- Use ADRs for narrow, dated, "we chose X over Y because Z" decisions. Use DESIGN.md for
  the connective narrative that ties multiple decisions together into an overall picture.
- Respect `Status`: `Proposed` means still under discussion, `Accepted` means settled,
  `Superseded by <file>` means kept only for history. Don't treat a `Proposed` ADR as
  binding, and don't quietly flip a superseded ADR's status without adding the superseding
  note.
- This scaffold is a starting shape, not a one-time artifact — whichever agent or person is
  working in the repo later is expected to keep editing `references/PRD.md`, filling in
  `references/DESIGN.md`, and adding ADRs as work continues.
