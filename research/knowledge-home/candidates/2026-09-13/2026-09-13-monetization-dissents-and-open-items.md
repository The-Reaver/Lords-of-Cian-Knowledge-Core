# Six unresolved items from the fleet monetization review, recorded explicitly rather than smoothed over

- id: 2026-09-13-monetization-dissents-and-open-items
- type: finding
- status: candidate
- class: confirmed
- source: Fleet monetization review, 2026-09-13 (Brain Trust + AJ's independent audit)
- confidence: high -- direct record of dissents and named gaps, not a synthesis
- verified: 2026-09-13
- tags: lords-of-cian, archive-app, monetization, brain-trust
- REVIEW: high-impact

## Body
Recorded explicitly per the review's own discipline against smoothing over disagreement:

1. Whether a $1 price point should exist at all, even as pure cosmetic support. Jasiah's
   standing objection: a $1 charge costs roughly a third of its value in payment-processing
   fees for no real revenue purpose. Not resolved by the carried recommendation, which keeps a
   cheap Supporter tier -- the actual price floor ($1, higher, or pay-what-you-want) is
   Abad's call.
2. Model G (pay-what-you-want, $1 floor, no fixed SKUs) ended in a genuine 3-3 Brain Trust
   deadlock. Not carried into the final recommendation, but never voted down either -- live if
   Abad wants it reconsidered.
3. Whether one-time unlocks and revocable subscriptions are safe to run side by side is
   unevaluated. Sentinel: a permanent one-time purchase carries different refund exposure than
   a lapsing subscription. Oluwole: this would be a third access-control system layered on top
   of clearance_level and a subscription/entitlement table -- wants two stable systems proven
   before adding a third.
4. The free-progression/paid-entitlement unification question is genuinely open: whether the
   still-separately-queued Level 1->2 clearance rule and paid entitlement become one ladder or
   stay two permanent parallel systems. Elijah flagged this as the single largest hidden
   future-rework cost in the whole decision, and it depends directly on how the Level 2 rule
   itself resolves.
5. Downgrade and lapse-notification policy has no design yet -- what happens if a reader
   downgrades mid-story, or is notified a requested Chronicle is ready right as their
   membership lapses. Both tracks flagged this; neither designed an answer.
6. Missing data neither track had access to: current registered-reader count and any prior
   engagement/conversion analog (needed to know whether 100k members would be 10x or 1000x
   growth from today); age-distribution signal on the existing readership (needed to scope any
   minors/compliance precondition on a paid product); and the actual size of the
   leftover-material backlog (depends on the ledger processing finishing -- see
   2026-09-13-leftover-material-mining-preconditions.md).

## Links
- depends_on, 2026-09-13-monetization-carried-recommendation.md, the recommendation these items qualify
- depends_on, 2026-09-13-leftover-material-mining-preconditions.md, item 6's backlog-size gap
