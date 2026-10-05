# A cross-block rename in the Daba corpus left a stray "Wrenna" in three rules because the rename sweep was never repo-wide

- id: 2026-10-05-b-stale-rename-never-swept-daba-wrenna
- type: finding
- status: ratified
- ratification: 2026-10-05, same-session independent review, ratified; corrected: batch number realigned to the ledger's batches_completed numbering (CLAUDE.md's Phase 2-5 review headings run one to two numbers ahead)
- class: confirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batch 333 (headed Batch 335 in CLAUDE.md)
- confidence: high -- named rules in the batch record
- verified: 2026-10-05
- tags: lords-of-cian, daba, process, lesson, renames

## Body
In the Daba review (Batch 333, headed Batch 335 in CLAUDE.md), the Batch-296 cross-block rename of "Wrenna" to "Tessin" (to avoid colliding with Chronicle XXIX's Isolde Wrenna) was never swept from MCD-1870, MCD-1871, and MCD-1873, so the stale name survived in locked statements. The same batch fixed other collisions by rename: "Corrow" to "Sarrow" (collision with the Bane-track Corrow ravine network, MCD-1581), "Elowen Marn" to "Elowen Sarn" (Marn family, MCD-1613), "Sarel Doune" to "Lisbet Doune" (collision with "Serel", MCD-1874), a runner "Ossa" to "Tova" (collision with villain Ossa Drem, CC-154), and Deryn Kettel's pronouns to she/her. Lesson: every rename needs a repo-wide grep for the old name afterward.

## Links
- supports, 2026-10-05-b-ctg-four-step-gate-mechanics.md, evidence for the propagation step
- related, 2026-10-05-b-near-collision-names-open-tally.md, names flagged but not renamed
