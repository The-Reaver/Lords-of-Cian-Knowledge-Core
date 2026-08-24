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

This is a scaffold, not a completed sync. What this repo does *not* yet have: the operator's
full existing Core (whatever already lives in `notes/` and `candidates/` on the device),
`structure-notes/brain-trust-on-demand-protocol.md`, the ADR referenced by the `stag-closeout`
skill (`docs/adr/0005-two-store-memory-archive-and-core.md`), and `scripts/knowledge_home/archive_writer.py`.
None of those were available to the session that initialized this repo — they exist only on the
operator's machine as far as this repo currently knows. A future session with device-bridge
access should treat this repo and the device Core as two copies of the same thing needing a real
merge (dedup notes, don't just overwrite), not assume this repo is already the complete picture.

Two live, unrelated threads both still need attention and are tracked in their own docs above,
not here: the Anansi close-out from 2026-08-03 (still OPEN), and the interactive archive app's
Phase 0 blockers (the connected GitHub repo has zero commits; RLS/email-confirmation status may
be leaving reader data exposed on a live public URL).
