# A new rule's category field must follow the track's established convention, as shown by the MCD-1730 mis-tag corrected on 2026-09-23

- id: 2026-10-05-a-category-tag-must-match-track-convention
- type: finding
- status: candidate
- class: confirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batch 303
- confidence: high -- the correction is recorded with exact values
- verified: 2026-10-05
- tags: lords-of-cian, ledger-hygiene, categories, ozmund

## Body
Ozmund Chronicle I (`MCD-1730`) was mistakenly tagged `kanja-alias-chronicle`, the Alias Chronicle track's category, instead of the Character Chronicle convention used for Lauris and Daba (`lauris-character-chronicle`, `daba-character-chronicle`). It was corrected in place to `ozmund-character-chronicle` in both `canon-ledger.json` and `merge_batch303_ozmund_chronicle_i.py`, with no content or version change. This is the same class of fix as the Maret Vos / Dol Maren reconciliation. The recurrence is notable: Batch 230 (alias wave 20) had five agents reuse a template placeholder `alias-chronicle` instead of `kanja-alias-chronicle`, and later phases normalized category drift across hundreds of rules. Lesson for future sessions: state the exact category string in every agent brief and check it in the merge script's assertions, because category drift is cheap to prevent and tedious to repair afterward.

## Links
- related, 2026-10-05-b-metadata-drift-normalization-phase5.md, the later bulk normalization of the same drift
- related, 2026-10-05-b-batch-citation-drift-from-shared-placeholder.md, other merge-script hygiene lessons
