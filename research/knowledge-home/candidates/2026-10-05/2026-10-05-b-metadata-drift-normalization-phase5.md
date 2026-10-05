# Phase 5 normalized drifting category and status metadata across hundreds of rules without changing any fact

- id: 2026-10-05-b-metadata-drift-normalization-phase5
- type: finding
- status: ratified
- ratification: 2026-10-05, same-session independent review, ratified; corrected: batch numbers realigned to the ledger's batches_completed numbering (CLAUDE.md's Phase 2-5 review headings run one to two numbers ahead); removed an unsupported claim that Batch 349's record mentions MCD-1730
- class: confirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batches 341-349
- confidence: high -- counts reported per batch
- verified: 2026-10-05
- tags: lords-of-cian, ledger-hygiene, metadata, review

## Body
The institutional rule-block reviews found metadata drift beyond statement text: category normalized across 100 CC- rules (Batch 341), 42 PH2/WC/POL/VB/COS rules plus status drift across 30 (Batch 342), 47 CULT/ASH rules (Batch 343), uppercase "LOCKED" statuses lowercased on 72 ARS/MAW/HLD rules (Batch 345), territory-Chronicle category tags on 11 MCD rules (Batch 346; CLAUDE.md heads these five batches 340-345) and 23 more (Batch 349), 52 MCD rules' uppercase statuses, MCD-051/122 composite statuses normalized, MCD-112's "FLAGGED" lowercased and left genuinely open, and a null category on MCD-131/132/133 set to "character-pyro". The earlier MCD-1730 category mis-tag was fixed separately on 2026-09-23 (see the category-tag note). Lesson: category and status values drift when parallel agents invent their own placeholder values; verify them against the established per-track convention before merging.

## Links
- related, 2026-10-05-b-batch-citation-drift-from-shared-placeholder.md, another consequence of agents inventing their own labels
- related, 2026-10-05-b-mcd-core-chunking-needs-cross-chunk-grep.md, the review that found the MCD instances
