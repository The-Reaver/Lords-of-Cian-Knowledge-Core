# Merging this repo with the real Core at `C:\Users\abadm\stag`

Written 2026-08-24, by the session that first scaffolded this repo. This repo
(`Lords-of-Cian-Knowledge-Core`) and the operator's device Core are currently **two separate,
unmerged copies of overlapping material**. This repo has no device-bridge access and could not
verify anything against the live folder — everything below is a procedure for the next session
that *does* have a working bridge (an interactive Cowork/Claude session with
`mcp__remote-devices__*` tools present, desktop app open, `desktop-4uc2ltp` connected), not a
merge that has already happened.

**A cloud/scheduled session cannot do this.** Per `docs/lords-of-cian/anansi-closeout-2026-08-03.md`'s
own structural finding, `mcp__remote-devices__*` tools are structurally absent from scheduled and
Claude Code Remote sessions, not just erroring "not connected." Confirm the tools are actually
present (`ToolSearch` or check the tool list directly) before starting; if they're absent, stop
and say so rather than guessing at device state.

## Baseline: what this repo has, as of 2026-08-24

- `notes/` — **empty** except `.gitkeep`. Nothing has been imported from the device Core's ratified
  notes.
- `candidates/` — **empty** except `.gitkeep`. Nothing has been imported from any date-folder on
  the device.
- `raw/` — **one file**: `2026-08-23-canon-ledger-cult-network-and-archive-strategy.jsonl` (96
  turns, 2026-08-22T19:12Z through 2026-08-24T01:37Z), imported from a chat upload, not read from
  the device. The device almost certainly has this same session's raw archive already, plus many
  more sessions this repo has never seen.
- `structure-notes/artifact-registry.md` — **empty stub**, header/format only, no entries. The
  device Core's real registry has entries; this repo's copy does not.
- `structure-notes/brain-trust-on-demand-protocol.md` — **does not exist in this repo.** The
  `stag-closeout` skill references it as the standing ratification-process doc. Pull it from the
  device as-is; do not reconstruct it from memory or invent one.
- No `docs/adr/0005-two-store-memory-archive-and-core.md`, no `scripts/knowledge_home/archive_writer.py`.
  Both are referenced by `stag-closeout` and both are unknown to this repo. Pull verbatim from the
  device; if `archive_writer.py` isn't there either, say so rather than writing a new one that
  might not match the device's actual append-only guarantees (ADR-0005).

Treat this repo's copy as strictly behind the device on all four `research/knowledge-home/`
subfolders, and the device as strictly behind this repo on everything else (`CLAUDE.md`,
`canon-ledger.json`, `docs/lords-of-cian/*`) unless a device session has independently written
newer versions of those since 2026-08-23 — check dates before assuming either direction.

## Merge procedure

### 1. `notes/` — the ratified Core

This repo's `notes/` is empty, so there is nothing here that could conflict with the device's
copy. Copy the device's `research/knowledge-home/notes/*.md` into this repo's `notes/` verbatim,
one file per note, no edits. This is an import, not a merge — skip straight to committing it
(see Git operations, below). Do not re-ratify anything already `status: ratified` (or equivalent)
on the device; ratification already happened there.

### 2. `candidates/` — check two specific outstanding items first

Before a generic folder copy, resolve these two known items, both already documented in this
repo and both possibly still unresolved on the device:

**a. The 2026-08-03 Anansi close-out** (`docs/lords-of-cian/anansi-closeout-2026-08-03.md`).
Check whether `research/knowledge-home/candidates/2026-08-03/` already exists on the device.
- **If it exists:** a later session already completed this close-out. Read its `Status` line —
  if `CLOSED`, this repo's copy of the close-out doc is just history; update this repo's copy
  to note the closure date, and check whether the "Anansi close-out nightly reminder" trigger
  was actually deleted (`list_triggers`) — the doc's own step 6 says to delete it, and per the
  doc's 2026-08-24 note this was never confirmed done.
- **If it does not exist:** this close-out is still genuinely OPEN. The doc already contains the
  full verbatim text of all 6 files (5 atomic notes + 1 handoff) that were supposed to be written
  — do not re-draft them, copy them out of the doc's "File 1" through "File 6" sections exactly
  as given, run the dedup check the close-out's own Step 2 requires (read `notes/` — now imported
  per step 1 above — and check none of the 5 notes duplicate something already there), then write
  the 6 files into `research/knowledge-home/candidates/2026-08-03/` on the device using the exact
  filenames the doc specifies. Also stage the artifact-registry entry for the 3 artifacts listed
  in that doc (into the device's registry as a candidate, not a direct edit — ratification still
  gates it per Step 4 below). Then follow the doc's own steps 5-7 for git commands and closing
  the doc out, and confirm the nightly trigger deletion this time.

**b. The 2026-08-23 candidates** referenced in `docs/lords-of-cian/session-handoff-note-2026-08-23.md`:
two notes in `research/knowledge-home/candidates/2026-08-23/` on the device, covering the
now-superseded tech-stack proposal and the archive/studio independence question. Pull this
date-folder into this repo as-is (still `status: candidate` — do not ratify them in this pass
just because they're being copied). The handoff note itself flags they may need a follow-up
note reconciling them against `lords-of-cian-archive-game-plan.md`, which is already in this
repo — that follow-up is separate work, not part of the merge itself.

**c. Everything else in `candidates/`** on the device (any other date folders): copy verbatim.
Do not ratify anything as part of this merge — ratification is a separate, explicit step (see
`stag-closeout` Step 4) that needs the operator's Brain Trust review, not something a merge pass
should do implicitly.

### 3. `raw/` — append-only transcripts, dedup by content not filename

The device's `raw/` folder almost certainly already contains an archive file covering the same
2026-08-22→24 session as this repo's `2026-08-23-canon-ledger-cult-network-and-archive-strategy.jsonl`,
very possibly under a different filename (the close-out skill derives filenames from a
session slug, which this repo's import guessed at rather than read from the device).

- Before copying anything, check for an existing device file covering the same date range and
  turn content (compare first/last `ts` values, turn count, and a text snippet) rather than
  matching on filename.
- If a matching file already exists on the device: this repo's copy is redundant. Do not write
  it again under a different name. Note in the merge report which device file it corresponds to
  and remove or clearly mark this repo's copy as a duplicate-of.
- If no matching file exists on the device: this repo's copy may be the only surviving record of
  that session's raw transcript. Write it into the device's `raw/` folder under the device's
  actual naming convention (check a few existing filenames there first) rather than this repo's
  guessed name, since `archive_writer.py`/ADR-0005 govern the real format and this repo's copy
  was hand-derived from a chat upload, not written by that script.
- For every other raw file already on the device that this repo doesn't have: copy verbatim, no
  edits — these are append-only source records, never rewrite a line that's already there.

### 4. `structure-notes/`

Copy `brain-trust-on-demand-protocol.md` and any other files present on the device but not in
this repo verbatim. For `artifact-registry.md`: this repo's copy is an empty stub; the device's
copy is presumably the real, populated registry. Replace this repo's stub with the device's
version rather than trying to merge entries by hand — check first that this repo's stub hasn't
picked up any real entries in the meantime (it shouldn't have, since nothing has ratified into
it yet, but confirm rather than assume).

## Also pull, not yet in this repo

- `docs/adr/0005-two-store-memory-archive-and-core.md` (referenced by `stag-closeout`, governs
  the raw-archive append-only guarantee) — copy verbatim into this repo's `docs/adr/`.
- `scripts/knowledge_home/archive_writer.py` (the script `stag-closeout` Step 0 calls) — copy
  verbatim into this repo's `scripts/knowledge_home/`. If it references other local modules,
  pull those too rather than a partial copy.

## Git operations — read before touching git

Per `stag-closeout`'s own Step 7, **never run git through the device bridge** — it leaves a stale
`.git/index.lock` (sometimes `.git/HEAD.lock`) the sandbox can't clean up. The device-bridge
session's job is to *read* files from the device and *write* them into this repo's working tree
(which lives in the Claude Code Remote sandbox, not on the device); committing and pushing happens
normally from there, the same way this repo's first commit was made. Nothing about this merge
changes that rule — it applies to reading `stag`, not to committing the results.

Stage only what step 1-4 above actually determined should move: the full `notes/` import,
resolved `candidates/` folders, deduped `raw/` files, and the real `structure-notes/`,
`docs/adr/`, and `scripts/knowledge_home/` content. Do not run a blanket `git add -A` on faith —
review `git status` against this checklist before committing, per this project's own standing
review-before-commit practice.

## Report back

When this merge runs, report: note count before/after in `notes/`; which `candidates/` date
folders were pulled in and whether the 2026-08-03 close-out was found already-closed or was
completed as part of this pass (and whether its nightly trigger was confirmed deleted); how many
`raw/` files were deduped vs. newly copied, and the resolution for this repo's own
2026-08-23 transcript file; and confirmation that `structure-notes/`, `docs/adr/`, and
`scripts/knowledge_home/` now match the device. Update this repo's root `README.md` "Status"
section to drop the "not yet a full sync" caveat once all four subfolders are confirmed merged.
