# The Connective-Tissue Gate has four ordered steps: mechanical check, independent review, propagation, presentation

- id: 2026-10-05-b-ctg-four-step-gate-mechanics
- type: decision
- status: ratified
- ratification: 2026-10-05, same-session independent review, ratified
- class: confirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batch 362
- confidence: high -- written into CLAUDE.md as the third non-negotiable rule
- verified: 2026-10-05
- tags: lords-of-cian, connective-tissue, gate, process
REVIEW: high-impact

## Body
Every entry, rule draft, correction, profile section, and merge must pass this gate before it is shown to the author (CLAUDE.md, third non-negotiable rule; also lives in docs/lords-of-cian/character-profiles/_TEMPLATE.md):

1. Mechanical check. Run `python3 scripts/connective_tissue_check.py <draft>`; it must exit 0, meaning every cited rule ID exists and is locked. Its output is the checklist: every proper noun with the rules and entries already using it, every new name with near-collisions, every number (age, year, count, density, distance) in the narrative.
2. Independent review. A fresh-context reviewer who did not write the draft reads it beside every listed rule and tries to break it: ages and dates against each character's timeline, gear against era (Trinity before the age-30 surrender, post-Mafesto kit after, Book-2 Moonvault gifts never before Book 2), who knows what and since when, places against the Atlas, voice against the narrator's sheet, kills against CC-161/CC-162/MCD-1882, reserved threads against the profile. Every finding is fixed and the draft re-checked before presentation.
3. Propagation. A change to a locked fact is carried in the same batch to every rule statement, entry, profile, and tracker row stating it, found by repo-wide grep. A fact corrected in one place and left stale in another is a gate failure.
4. Presentation. Each draft carries a short connective-tissue note: what it agrees with, extends, touches, and which new names were collision-checked. Approval and lock then follow the first non-negotiable rule.

## Links
- depends_on, 2026-10-05-b-ctg-number-one-priority-ruling.md, the ruling this gate implements
- related, 2026-10-05-b-half-applied-fix-propagation-lesson.md, a concrete propagation failure that motivated step 3
