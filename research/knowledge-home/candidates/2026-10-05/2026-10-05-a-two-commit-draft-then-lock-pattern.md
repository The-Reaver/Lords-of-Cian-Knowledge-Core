# Single-Chronicle drafts are committed first as unlocked or pending with a plain header, and the header is corrected to Locked canon only after approval

- id: 2026-10-05-a-two-commit-draft-then-lock-pattern
- type: decision
- status: ratified
- ratification: 2026-10-05, same-session independent review, ratified
- class: confirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batch 303
- confidence: high -- described repeatedly as 'the same two-commit pattern used throughout the project'
- verified: 2026-10-05
- tags: lords-of-cian, process, draft-then-lock, stop-hook

## Body
Chronicles presented one at a time for approval (Ozmund Chronicle I, Daba's third wave, Lauris waves, Ezio drafts) follow a two-commit pattern: the draft is committed immediately with a header marking it unlocked/pending, because a Stop hook requires a clean working tree; after the author's explicit approval the merge script runs and the header is corrected to "Locked canon". Blanket-authorization runs (for example the large Ozmund and Daba waves, approved with phrases such as "add 19 more" or "go") write directly with Locked headers and merge at the end. The pattern preserves the first non-negotiable rule (draft, approval, lock) while keeping git clean. A consequence appears in Batch 332: Ezio's Chronicles II-IV were drafted as unlocked/pending drafts and reviewed for internal consistency but deliberately not locked, because the author had not yet reviewed them. A pending file with a pending header is a signal to reviewers that it is out of ledger scope.

## Links
- related, 2026-10-05-a-ezio-pending-drafts-ii-iv-not-locked.md, an example of drafts left pending after a review pass
