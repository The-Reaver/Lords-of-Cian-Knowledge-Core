# The fable-review pipeline paired read-only reviewers with fix agents that apply findings verbatim and leave new creative invention untouched

- id: 2026-10-05-b-fable-review-pipeline-division-of-labor
- type: decision
- status: ratified
- ratification: 2026-10-05, same-session independent review, ratified; corrected: source batch range realigned to the ledger's batches_completed numbering (CLAUDE.md's Phase 2-5 review headings run one to two numbers ahead)
- class: confirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batches 337-349
- confidence: high -- same pattern repeated across Phases 4 and 5 in the batch records
- verified: 2026-10-05
- tags: lords-of-cian, process, review, parallel-agents

## Body
Phases 4 and 5 ran the same pipeline: parallel read-only review agents (one per city, or one per rule-prefix family or ID chunk) returned exact findings and fix instructions; matching fix agents then applied mechanical and reconciliation fixes verbatim, editing Chronicle prose files and writing an unexecuted merge script, and leaving anything that required new creative invention untouched. The orchestrating session reviewed each hand-back, verified new rule IDs, renumbered hardcoded batch labels (several agents used a shared placeholder number), ran the script, confirmed zero duplicate IDs, then committed. The fix agents never touched canon-ledger.json or git. Findings requiring a new fact were deliberately left unresolved and accumulated into a running tally for the author, so that review speed never became a channel for inventing canon.

## Links
- related, 2026-10-05-b-ctg-correction-vs-new-fact-split.md, the routing rule the pipeline follows
- related, 2026-10-05-b-parallel-rename-race-batch-343.md, a failure mode of running fix agents in parallel
- related, 2026-10-05-b-batch-citation-drift-from-shared-placeholder.md, another consequence of shared placeholders
