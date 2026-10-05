# Two parallel agents renamed the same ability differently, so renames that touch one proper noun must be serialized or reconciled

- id: 2026-10-05-b-parallel-rename-race-batch-343
- type: finding
- status: candidate
- class: confirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batches 340-343
- confidence: high -- the batch record names the cause and the fix
- verified: 2026-10-05
- tags: lords-of-cian, process, lesson, parallel-agents, renames

## Body
The Batch 342 Varruk rename ran against a slightly earlier ledger snapshot than Batch 340's independent rename of the same ability: Batch 340 chose "the Riptide Break", Batch 342 chose "Cadence Break" without seeing it, leaving CC-099 referencing a name that no longer existed in CC-098. Batch 343 standardized on "Cadence Break"/"Cadence Saturation" and corrected CC-099's cross-reference. Context: the name "Cadence Ruin" had collided three ways (Onyx's blade power, Varruk's ability, Sereth Vaul's Green Mark aura), later resolved at ARS-395 as "the Void Wake". The recorded lesson for any future parallel-rename pass: serialize renames touching the same proper noun, or add a consolidation step that reconciles them, as was done here.

## Links
- extends, 2026-10-05-b-fable-review-pipeline-division-of-labor.md, the pipeline in which the race happened
- related, 2026-10-05-b-half-applied-fix-propagation-lesson.md, a sibling failure of fixes not reaching every copy
