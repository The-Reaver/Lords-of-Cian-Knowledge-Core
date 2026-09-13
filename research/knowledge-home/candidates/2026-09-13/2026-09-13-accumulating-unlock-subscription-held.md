# Abad's single-mechanism "subscription with accumulating unlocks" idea was HELD by a scoped 5-seat Brain Trust reaction pass -- it doesn't collapse to one system, it relabels a chargeback risk

- id: 2026-09-13-accumulating-unlock-subscription-held
- type: decision
- status: candidate
- class: confirmed
- source: Scoped 5-seat Brain Trust reaction pass, 2026-09-13 (Celestina, Jasiah, Oluwole, Bink, Sentinel), reacting to an idea Abad proposed after reading the carried recommendation in 2026-09-13-monetization-carried-recommendation.md. Run per the now-unblocked structure-notes/brain-trust-on-demand-protocol.md, seat-by-seat via the Agent tool from inside this session, following that protocol's own precedent (rule 1) that this is the same process, not a lighter substitute.
- confidence: medium-high -- direct seat verdicts, tallied 3 HOLD / 2 SHIP WITH CONDITIONS on a 5-seat panel; not yet ratified by Abad
- verified: 2026-09-13
- tags: lords-of-cian, archive-app, monetization, brain-trust, entitlement, clearance-level
- REVIEW: high-impact

## Body
Abad's idea: instead of the carried recommendation's two separate SKUs (a perks-only
Supporter subscription, plus a separate per-content one-time "unlock forever" purchase), fold
permanence into the subscription itself -- while actively subscribed, each billing period
unlocks specific content; once unlocked, it stays permanently accessible even after the
subscription lapses; new unlocks stop the moment the subscriber isn't active. Offered as a fix
for two open dissents: Oluwole's "no third access-control system" objection and Sentinel's
refund-exposure concern about a permanent one-time sale.

Tally: 3 HOLD (Celestina, Jasiah, Sentinel), 2 SHIP WITH CONDITIONS (Oluwole, Bink). Majority
HOLD -- not carried as stated. Both premises the idea was pitched on were directly challenged:

- **Oluwole:** the "avoids a third access-control system" claim doesn't hold up architecturally.
  A permanently-held, never-revoked unlock grant has different lifecycle semantics than mutable
  subscription status and needs its own append-only ledger table regardless. What the idea
  actually eliminates is the second purchase/checkout SKU, not the third data structure --
  worth shipping for that reason, with the ledger built as its own table from day one rather
  than forced into the subscription row.
- **Sentinel (sharpest rebuttal):** framing an unlock as "benefit consumption" rather than "a
  sale" has no binding effect on how a card issuer evaluates a dispute -- it doesn't reduce
  chargeback exposure, it relabels it. Worse, it creates a new subscribe-grab-cancel abuse
  incentive the two-SKU design didn't have, and stacks subscription-disclosure obligations on
  top of the digital-goods obligations the permanent unlock already carries -- a superset of
  compliance surface, not a simplification. Recommends keeping the two SKUs separate as the
  carried recommendation already had them.
- **Celestina and Jasiah, independently:** the unlock cadence/allotment mechanism (how content
  gets chosen for unlocking each period) is unspecified, and both flagged this as the actual
  load-bearing detail -- Celestina from a fairness/reader-trust angle (system-assigned vs.
  reader-chosen changes whether it feels like a gift or a lottery), Jasiah from an
  unit-economics angle (undefined cadence makes churn/LTV unmodelable and creates a
  structural incentive to subscribe once, grab the allotment, and cancel).
- **Bink:** flags a metrics-integrity risk independent of the above -- this design creates two
  permanently-diverging populations (active subscribers vs. cumulative unlock-holders), and
  the prior review's strongest-consensus item (Model F, the churn-adjusted conversion ladder)
  only stays trustworthy if it's built off active billing status, not cumulative unlocks.

Real value the panel did credit: fewer integration paths (one purchase/billing flow instead of
two, Oluwole/Jasiah), and no runtime re-lock-on-lapse check needed since access is designed
never to be revoked (Bink) -- a genuine answer to the original review's blocking finding #2.

## Links
- depends_on, 2026-09-13-monetization-carried-recommendation.md, the two-SKU design this idea proposed replacing
- depends_on, 2026-09-13-monetization-dissents-and-open-items.md, Oluwole's and Sentinel's standing objections this idea was pitched against
- relates, 2026-09-13-signal-first-tier-design-carried.md, the companion idea from the same reaction pass, which carried
