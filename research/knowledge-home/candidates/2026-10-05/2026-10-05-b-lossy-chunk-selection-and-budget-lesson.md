# Selecting review chunks by category plus name is lossy in both directions, and a naive full-corpus review was judged too expensive

- id: 2026-10-05-b-lossy-chunk-selection-and-budget-lesson
- type: finding
- status: ratified
- ratification: 2026-10-05, same-session independent review, ratified; corrected: source batch range realigned to the ledger's batches_completed numbering (CLAUDE.md's Phase 2-5 review headings run one to two numbers ahead)
- class: confirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batch 320 (pilot), applied in Batches 346-349
- confidence: medium -- carried from the pilot record rather than re-measured in this span
- verified: 2026-10-05
- tags: lords-of-cian, process, lesson, review, budget

## Body
The Bane pilot (Batch 320, applied in the span's later chunking) established metrics: about 150-170K tokens for one chunk of roughly 60,500 words of prose plus 9,500 words of rule statements; a naive full run over about 1.01M words of prose and about 457K words of ledger and docs was prohibitively expensive at the time, with roughly 40% of a Max plan remaining. The 108-rule query for Bane was lossy: it missed MCD-365 (Bane's actual Chronicle I, stale category tag) and included six entries from other aliases merely mentioning Bane. Takeaways: build chunk membership from explicit ID or title-substring lists; give every chunk agent repo-wide grep; budget a consolidation pass as a chunk-sized task; run a single pilot before committing a large multi-agent spend.

## Links
- supports, 2026-10-05-b-mcd-core-chunking-needs-cross-chunk-grep.md, the practice this lesson shaped
- related, 2026-10-05-b-fable-review-pipeline-division-of-labor.md, the pipeline used afterward
