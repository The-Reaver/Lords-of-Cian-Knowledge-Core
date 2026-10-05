# A fix applied in one rule left its dependent rule stale, which is the failure mode the gate's propagation step exists to prevent

- id: 2026-10-05-b-half-applied-fix-propagation-lesson
- type: finding
- status: candidate
- class: confirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batch 340
- confidence: high -- the batch record names the specific rules
- verified: 2026-10-05
- tags: lords-of-cian, process, lesson, propagation

## Body
Batch 340 found a half-applied earlier fix: after Batch 321, Danne Sok's memory still described Kanja as "freed" rather than "found alongside" in CC-159, MCD-530, and MCD-234, even though the Corren Halst/Danne Sok/Maret Vos "found each other on the docks" facts had been reconciled elsewhere. It was reconciled in Batch 340 together with other drift (Abyss's "crew's youngest member" claim against Pyro's own age at CC-101/MCD-1715; a stale age ranking at CC-058 after MCD-1851). Lesson: a correction to a locked fact must be propagated in the same batch to every copy, which became gate step 3 (repo-wide grep) in Batch 362.

## Links
- supports, 2026-10-05-b-ctg-four-step-gate-mechanics.md, evidence for step 3
- related, 2026-10-05-b-parallel-rename-race-batch-343.md, a related race failure
