# [ADR-0005] Two-store memory: an append-only archive and a curated, embedded Core

* Status: Accepted. Operator directive, 2026-08-10, binding from this date with no end date.
* Deciders: operator (Abad)
* Implements: `scripts/knowledge_home/archive_writer.py`, `scripts/knowledge_home/note_schema.py`,
  `scripts/gates/archive_notes_separation_gate.py`, wired into `verify.py`.
* Proving test: `tests/test_archive_notes_separation_gate.py` (standalone, no pytest, per
  AGENTS.md law 3).

## Context and problem statement

Every session produces a transcript. Some small fraction of a transcript is a durable lesson
worth keeping; the rest is scaffolding, exploration, and near-duplicate phrasing. Before this
ADR, `research/knowledge-home/notes/` held both jobs at once: it was the only place a lesson
could be written down, and nothing preserved the full transcript a lesson came from. If notes
had ever been embedded and retrieved directly against a growing pile of raw transcript, retrieval
quality would degrade as the corpus grew, and there was no way to trace a note back to the exact
turns it was drawn from.

## Decision

Two stores, one write path, one pointer between them.

**Store 1, the archive.** Append-only. One file per session, JSONL, one object per turn:
`{ts, role, text, tool_calls}`. Never embedded, never in the vector index. Searched by grep or
Postgres full-text only. Nothing is ever deleted or edited. This is the record.

**Store 2, the Core.** One markdown file per atomic note, real YAML front matter (open and close
`---` fences), one lesson each. Embedded and indexed for hybrid vector plus lexical search when
the Living Knowledge Core (`specs/SPEC_KNOWLEDGE_CORE.md`) goes live. Small, clean, curated.

**The pointer.** Every note carries provenance back into the archive, so nothing is orphaned from
its origin:

```yaml
id: cand-2026-08-10-057
type: ruling
risk_class: A
evidence_state: SETTLED
next_review: 2026-11-08
sources:
  - ref: Operator ruling, 2026-08-10
    reliability: A
    credibility: 1
    origin: operator-ruling-2026-08-10
provenance:
  archive: research/knowledge-home/raw/2026-08-10-curriculum.jsonl
  turns: [188, 191]
```

```
knowledge-home/
  raw/     2026-08-10-curriculum.jsonl      append-only, not indexed
  notes/   cand-2026-08-10-057.md           atomic, indexed
  index/   embeddings + HNSW                built from notes/ only (not yet live, see Phase 2 note below)
```

**Write path.** Session ends. Transcript appends to `raw/`. A distillation pass reads that file
and emits candidate notes with provenance ranges. Operator reviews. Approved notes land in
`notes/`. This step is the existing `core_ratification_gate.py` / Brain Trust + AJ ratification
gate already in place, unchanged by this ADR, and get embedded once the Core's embedding pipeline
is live. The archive is never touched again.

**Why separate, in one line of arithmetic.** Recall at fixed k is monotonically non-increasing in
corpus size, because adding documents can only add competitors for the top k slots. A session
transcript is roughly two to three orders of magnitude larger than the notes it yields, and it is
mostly filler and near-duplicates. Indexing it would push the signal below the cut for every
query. Separation keeps the retrievable corpus at the size where precision holds while losing
nothing, because the provenance pointer means any note resolves to its exact origin in the
archive.

**Retention differs too.** Notes can be superseded and their state can decay on the review clock.
Archive entries have no state and no expiry. They are facts about what was said, not claims about
the world.

## What this ADR changes on the ground, today

- New directory `research/knowledge-home/raw/`, append-only, one JSONL file per session.
- New, stricter note front matter: real delimited YAML (`---`...`---`), fields `id`, `type`,
  `sources[]` (each with `ref`, `reliability`, `origin`), `provenance.archive`,
  `provenance.turns`. This supersedes the informal `- key: value` bullet-list convention every
  pre-2026-08-10 note in `notes/` uses.
- `.legacy-notes-allowlist.txt` grandfathers every note that existed in `notes/` before this ADR
  (the frozen snapshot taken 2026-08-10, same pattern `.ratified-allowlist.txt` already
  established for `core_ratification_gate.py`). Nothing is retroactively rewritten. Every note
  created from now on is held to the new schema.
- `archive_notes_separation_gate.py`, wired into `verify.py`, enforces: the extension boundary
  (no `.md` in `raw/`, no `.jsonl` in `notes/`), the schema on non-legacy notes, and, best-effort
  where git is available, that a committed archive file's prior content is never altered, only
  appended to.

## What this ADR does NOT change

- `specs/SPEC_KNOWLEDGE_CORE.md`'s Phase 2 build (the pgvector store, the embedding model, the
  `write_note()`/`link()`/`retrieve()` seams) is still not started and still gated on the
  operator's word after Phase 1 is clear. This ADR is the store/retention architecture that Phase
  2 must build against; it is not itself the Phase 2 implementation.
- The 8-field note model in `SPEC_KNOWLEDGE_CORE.md` section 2 (id, type, body, source, status,
  created_at, refs, links) and this ADR's front-matter fields are not identical field-for-field.
  Reconciling them (does `sources[]` replace `source`, does `risk_class`/`evidence_state` become
  part of `status`, and so on) is Celestina's ARCHITECT-phase job before `SPEC_KC_FOUNDATION`
  starts, flagged in `SPEC_KNOWLEDGE_CORE.md` section 3 as an open item this ADR creates.
- The embedding dimension: `SPEC_KNOWLEDGE_CORE.md` section 3 settles on
  `text-embedding-3-small`, 1,536 dimensions, pending `SPEC_KC_EMBEDDING_BENCHMARK`. This ADR's
  own example diagram says 768 dimensions, matching a different embedding family (e.g. a
  voyage-lite or a local sentence-transformer model). This is a real, unresolved conflict between
  a settled decision and this ADR's illustrative number, not silently picked one way. Flagged in
  `SPEC_KNOWLEDGE_CORE.md` section 3; `SPEC_KC_EMBEDDING_BENCHMARK` is the batch that must settle
  it, on the recall-at-10 evidence the benchmark spec already requires, not on this ADR's example.

## Consequences

Positive: every future note is traceable to its exact origin turns, and the archive gives the
fleet an append-only record no promotion or ratification pass can accidentally lose or overwrite.
The retrievable Core stays small and precise as the archive grows.

Negative / risk: two stores are more to maintain than one. The archive can grow large with no
pruning (by design, it is a record, not a working set); a future batch should decide a storage
policy (e.g. compression or cold storage past some age) once real volume exists, but that is an
operations decision, not a reason to index the archive itself.

## Sources

- Recall-at-fixed-k degrades monotonically as corpus size grows for a fixed retrieval depth. This is the
  standard precision/recall-at-k tradeoff in information retrieval (more competing documents for
  the same top-k slots lowers the odds any one relevant document is still in the top k). This is
  the same class of reasoning `SPEC_KC_EMBEDDING_BENCHMARK` already applies via recall-at-10.
