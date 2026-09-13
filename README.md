# Lords of Cian — Knowledge Core

Git-tracked home for the *My Rival's Distance: The Lords of Cian* canon-locking work and its
project history. Initialized 2026-08-24 from documents that previously existed only as Claude
Project docs, chat attachments, and files on the operator's own machine — several close-out
sessions were blocked for days because the only bridge to that machine (`C:\Users\abadm\stag`)
was a flaky device connection. This repo exists so the durable material survives session loss
and bridge outages without depending on that connection.

## Layout

- **`CLAUDE.md`** — how a Claude Code session should continue the canon-locking work: the
  draft-then-approve-then-lock process, rule-ID prefixes, the merge-script pattern, and standing
  conventions (no AI attribution, the child-safety hard stop, this world's long baseline
  lifespans). Read this first.
- **`canon-ledger.json`** — the authoritative canon-rules ledger. Flat list of atomic,
  source-cited rules (`rules`), a log of every extraction/invention pass (`batches_completed`),
  and open questions (`open_decisions`). As imported: `ledger_version` 2.4, 510 rules, 21
  batches, zero duplicate rule IDs.
- **`docs/lords-of-cian/`** — project history and planning docs, imported verbatim:
  - `session-handoff-note-2026-08-23.md` — the map to everything else here; read after CLAUDE.md.
  - `master-to-do-list.md` — stale as of 2026-08-13; kept for its record of resolved questions
    and corrections, not for current canon status (use `canon-ledger.json` for that).
  - `lords-of-cian-archive-game-plan.md` — the authoritative plan for the separate interactive
    archive app (repo `The-Reaver/My-Rivals-Distance-Archive`), reconciled 20 August 2026.
  - `archive-studio-tech-stack-decision.md` — superseded by the game plan above; kept for record.
  - `geographic-consistency-audit.md`, `kanja-chronicles-production-roadmap.md` — an older,
    separate thread (geography vs. the Regional Atlas, Chronicle 1 production) that predates and
    is unrelated to the cult-network/canon-ledger and archive-app work.
  - `anansi-closeout-2026-08-03.md` — a close-out session left OPEN because the device bridge
    never connected; its placement steps target `research/knowledge-home/` below and have not
    been confirmed as completed.
- **`research/knowledge-home/`** — the Anansi Knowledge Core layout (see the `anansi` and
  `stag-closeout` skills), scaffolded but not yet populated from the operator's machine:
  - `notes/` — ratified atomic notes. Empty; nothing has been synced from the device Core yet.
  - `candidates/<date>/` — candidate notes pending Brain Trust ratification before they merge
    into `notes/`. Empty here; see `anansi-closeout-2026-08-03.md` for candidates already
    approved in conversation but never written to any Core.
  - `raw/` — append-only raw session transcripts, one JSONL file per session, one line per turn.
    Contains one imported transcript: `2026-08-23-canon-ledger-cult-network-and-archive-strategy.jsonl`
    (96 turns, 2026-08-22T19:12Z through 2026-08-24T01:37Z — the session that produced the
    current canon-ledger.json and session-handoff-note).
  - `structure-notes/artifact-registry.md` — registry of ratified lasting artifacts. Created
    empty; nothing has been ratified into it yet.

## Status

**Updated 2026-09-12 — not a full sync, but the merge blocker is resolved.** `structure-notes/brain-trust-on-demand-protocol.md`,
`docs/adr/0005-two-store-memory-archive-and-core.md`, `scripts/knowledge_home/archive_writer.py`, and
the real, populated `structure-notes/artifact-registry.md` are now present in this repo, copied
verbatim from the operator's device (`C:\Users\abadm\stag`). `candidates/2026-08-23/` is now
populated (2 files, still unratified) from the device. The 2026-08-03 Anansi close-out
(`docs/lords-of-cian/anansi-closeout-2026-08-03.md`) is CLOSED — its 6 files were written into the
device's own `research/knowledge-home/candidates/2026-08-03/`, not into this repo (they belong on
the device, per the close-out doc's own instructions). This repo's `raw/2026-08-23-canon-ledger-cult-network-and-archive-strategy.jsonl`
is a confirmed content-duplicate of a file already on the device; left in place and documented, not
deleted.

**Deliberately still not done:** this repo's own `notes/` remains empty. The device's real `notes/`
(846 files as of 2026-09-12) is almost entirely unrelated GEO Suite/compliance/Anansi-tooling
material with nothing yet reviewed for relevance to Lords of Cian — bulk-copying it into this
fiction repo was assessed as scope creep and held pending an explicit operator decision, not done as
part of this merge.

No device bridge (`mcp__remote-devices__*`) was available or needed to do any of the above — a
local Claude Code session already running inside `C:\Users\abadm\stag` has ordinary filesystem/git
access to both this repo (via a plain clone) and the device Core directly. See CLAUDE.md's "Standing
blocker" section (now marked RESOLVED) for the full account.

One live, unrelated thread still needs attention and is tracked in its own doc above, not here: the
interactive archive app (see CLAUDE.md's "Separate, unrelated thread" section for its updated
2026-09-03 status -- the zero-commits and RLS flags from 2026-08-23 are largely resolved on
inspection, not independently verified live).
