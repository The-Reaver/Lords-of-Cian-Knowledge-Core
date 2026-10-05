# The Batch 378 draft passed the mechanical check but still owes the independent review gate step before it can be presented for approval.
- id: 2026-10-05-c-pending-batch-378-owes-independent-review
- type: finding
- status: candidate
- class: believed-unconfirmed
- source: Canon session 2026-09-20 to 2026-10-05 (raw archive research/knowledge-home/raw/2026-10-05-canon-session-batches-303-377.jsonl), Batch 378
- confidence: high, the draft states this plainly about itself
- verified: 2026-10-05
- tags: lords-of-cian, batch-378-pending, connective-tissue, gate, process
## Body
This item is a draft and is pending the author's approval; nothing in it is locked canon. The draft's own closing line (docs/lords-of-cian/drafts/2026-10-05-pact-and-long-mask-timeline.md): 'python3 scripts/connective_tissue_check.py on this draft exits 0. The independent review (step 2 of the gate) is still owed before this draft is presented.' Under the Connective-Tissue Gate, a fresh-context reviewer who did not write the draft must read it beside every rule the script listed and try to break it, with every finding fixed and the draft re-checked, before presentation. Earlier batches in this session needed several review rounds before the gate came back clean (see the review-rounds note), so a first review of a 49-rule, 60-entry batch should be expected to find things. The merge script merge_batch378_pact_long_mask_timeline.py had a clean dry run, and the propagation diff is at docs/lords-of-cian/drafts/2026-10-05-batch378-propagation-full-text.diff. Approval then locks it under the first non-negotiable rule.
## Links
- related, 2026-10-05-c-review-rounds-before-a-clean-gate.md, how many rounds earlier batches needed
- related, 2026-10-05-c-approval-item-1-offset-now-batch-378-draft.md, the draft itself
