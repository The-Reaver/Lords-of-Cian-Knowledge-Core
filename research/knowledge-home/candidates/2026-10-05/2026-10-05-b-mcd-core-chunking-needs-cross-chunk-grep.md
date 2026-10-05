# The MCD core was split by ID range into four chunks, and the highest-value findings were cross-chunk, so reviewers need full-ledger grep access

- id: 2026-10-05-b-mcd-core-chunking-needs-cross-chunk-grep
- type: finding
- status: candidate
- class: confirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batches 345-349 (and pilot note)
- confidence: high -- stated in the batch record and the pilot metrics it cites
- verified: 2026-10-05
- tags: lords-of-cian, process, lesson, review, chunking

## Body
Phase 5 deferred the MCD core (about 1,877 rules, the largest single prefix) for scale, then picked it up as a self-initiated continuation of the same standing review mandate. With no natural thematic grouping at that scale it was split by pure ID range: MCD-1351-1877, 451-900, 901-1350, 1-450, each reviewed by an agent given full-ledger grep access, because the highest-value findings were consistently cross-chunk (stale references into the Lauris and Chronicle-track material, or into CC-, ARS-, MAW- rules). The pilot that preceded this (Bane, Batch 320) had flagged that category-plus-name selection is lossy both ways (it missed Bane's actual Chronicle I over a stale category tag and pulled in six other aliases' entries), so chunk lists must be built from title-substring or explicit-ID lists, with a dedicated consolidation pass budgeted as its own task.

## Links
- related, 2026-10-05-b-fable-review-pipeline-division-of-labor.md, the wider pipeline
- related, 2026-10-05-b-fulfillment-ceremony-284-vs-296-years.md, a cross-chunk finding the fourth chunk produced
