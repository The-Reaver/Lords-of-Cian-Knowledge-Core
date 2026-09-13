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

## Partially ratified
2026-09-13. Abad's ruling, quoted verbatim: "I approve of everything and I will drop my idea." This
note's status is left at candidate rather than ratified, deliberately: the six items above are open
questions with multiple live options each, not a single recommendation to approve or reject, and none
of them was individually resolved in Abad's blanket approval. Everything they gate (the carried
recommendation, the vintage-boundary rule, the mining preconditions, the signal-first sequencing) is
now ratified regardless -- these six items were never blockers to that, only unresolved details within
it. Each stays open until Abad rules on it specifically:

1. Whether a $1 price point should exist at all -- unresolved.
2. Model G (pay-what-you-want) -- unresolved, not reconsidered, not closed.
3. Whether one-time unlocks and revocable subscriptions are safe side by side -- moot for now, since
   Idea 1's merge of the two was dropped (2026-09-13-accumulating-unlock-subscription-held.md) and the
   carried recommendation already keeps them as two separate SKUs, which was never itself the specific
   thing this dissent questioned.
4. Free-progression (Level 1->2) / paid-entitlement unification -- unresolved, depends on the
   still-separately-queued Level 2 rule.
5. Downgrade and lapse-notification policy -- unresolved, no design exists yet.
6. Missing data (reader count, age distribution, backlog size) -- unresolved; none of it was supplied
   this round.

## Links
- depends_on, 2026-09-13-monetization-carried-recommendation.md, the recommendation these items qualify
- depends_on, 2026-09-13-leftover-material-mining-preconditions.md, item 6's backlog-size gap
