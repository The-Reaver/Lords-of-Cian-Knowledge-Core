# Large Chronicle waves run as parallel agents with disjoint IDs, progressive commits, and a ledger merge only after a cross-agent name-collision sweep

- id: 2026-10-05-a-parallel-strand-agents-commit-progressively-merge-after-sweep
- type: decision
- status: ratified
- ratification: 2026-10-05, same-session independent review, ratified; corrected: batch number realigned to the ledger's batches_completed numbering (CLAUDE.md's Phase 2-5 review headings run one to two numbers ahead)
- class: confirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batch 304
- confidence: high -- the same procedure is described across Batches 304, 305 and 306 and reused later
- verified: 2026-10-05
- tags: lords-of-cian, process, parallel-agents, collision-check, ozmund

## Body
The procedure for Ozmund waves (Batches 304-306), also used for Daba and Lauris waves: each agent drafts one strand with a fixed, non-overlapping Chronicle numeral range and `MCD-` ID range; each reads its own strand's prior entries and the full profile first; each collision-checks every new proper noun against the live ledger before use; agents are barred from touching `canon-ledger.json` or git. Files are committed as each strand completes, which satisfies the Stop hook's clean-working-tree requirement. The ledger merge runs only after all agents report and a full cross-strand collision sweep is done. The sweep is where real collisions surface because each agent can only see its own names. Examples: a servant first drafted as "Corwen" was renamed "Bevin" because the Aethelgard strand's unrelated dike-warden is Corwen Dask (Batch 304); a "Commander Rell" collided with the Rell/Tamsy fen-household family and was later renamed "Welk" (Batch 334, headed Batch 336 in CLAUDE.md). Batch 305's sweep over 17 new names found zero collisions; Batch 306's sweep over 14 new names likewise, noting that 15 substring hits for "rell" were unrelated words (Arellanes, Mirella, Umbrella), a reminder to read substring hits before declaring a collision.

## Links
- related, 2026-10-05-b-parallel-rename-race-batch-343.md, what goes wrong when parallel agents rename the same noun
- related, 2026-10-05-a-two-commit-draft-then-lock-pattern.md, the other commit pattern in use
