# The Lords-of-Cian-Knowledge-Core repo's research/knowledge-home/ scaffold is still missing three files the device merge is supposed to bring over

- id: 2026-09-03-knowledge-home-scaffold-still-missing-three-files
- type: finding
- status: candidate
- class: confirmed
- source: Lords-of-Cian-Knowledge-Core session, 2026-09-03, "Batch 49 and the Brain Trust gap"
- confidence: high -- verified directly by listing the actual directories in this session
- verified: 2026-09-03
- tags: lords-of-cian, fleet, infrastructure, brain-trust

## Body
As of 2026-09-03, `research/knowledge-home/structure-notes/core-merge-instructions.md` (written
2026-08-24) still accurately describes this repo's gaps -- nothing has changed in the 10 days
between. Confirmed absent: `scripts/knowledge_home/archive_writer.py` (directory does not exist
at all), `docs/adr/0005-two-store-memory-archive-and-core.md` (the `docs/adr/` directory exists
but is completely empty), and `structure-notes/brain-trust-on-demand-protocol.md` (not present
among the two files that do exist in `structure-notes/`: `artifact-registry.md` and
`core-merge-instructions.md` itself). `research/knowledge-home/notes/` and `.../candidates/` are
both still empty except `.gitkeep`.

Practical consequence, reconfirmed: no cloud session can perform real Brain Trust ratification or
write an ADR-0005-certified raw archive until a device-bridge session runs the merge procedure
already sitting in `core-merge-instructions.md`. This note exists so a future session doesn't have
to re-verify absence from scratch -- but should still re-check with a fresh `ls` before relying on
it, since the whole point of the pending merge is that this will change.

## Links
- extends, 2026-09-03-cloud-sessions-lack-device-bridge.md, this is the concrete file-level
  consequence of that structural gap
