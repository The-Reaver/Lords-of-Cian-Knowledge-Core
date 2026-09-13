# Fleet-carried monetization recommendation: perks-only Supporter tier + per-content unlock + vintage-boundary paywall, entitlement kept separate from clearance_level

- id: 2026-09-13-monetization-carried-recommendation
- type: decision
- status: ratified
- class: confirmed
- source: Fleet monetization review, 2026-09-13 (chair's synthesis of independently-converging Brain Trust and AJ-audit output; not itself re-voted by either track -- presented for Abad's ratification, not a fixed conclusion)
- confidence: medium -- directionally strong (both tracks converged toward the same shape independently: AJ's audit reached essentially Models D+E combined from the opposite direction), but real open items remain (see 2026-09-13-monetization-dissents-and-open-items.md) and this has not been ratified by Abad
- verified: 2026-09-13
- tags: lords-of-cian, archive-app, monetization, brain-trust, clearance-level, entitlement
- REVIEW: high-impact

## Body
Not yet ratified -- staged here as the fleet's carried recommendation pending Abad's own
explicit approval, per this project's standing draft-then-approval discipline. The shape both
independent review tracks converged toward, replacing the rejected $1/$2/$3-on-clearance_level
proposal (2026-09-13-membership-tiers-as-stated-rejected.md):

- A cheap perks-only "Supporter" tier that never gates or revokes content already visible to a
  reader -- early access, priority on requested Chronicles, cosmetic recognition only.
- A per-content one-time "unlock forever" purchase for specific Chronicles/territories -- real
  ownership, framed as the natural home for premium content later mined from material that
  didn't make canon-ledger.json (see 2026-09-13-leftover-material-mining-preconditions.md).
- Paywall boundary set by production vintage, one explicit instrumented rule, not narrative
  position: everything currently free and indexed stays free and indexable forever; new work
  going forward carries the price. Maps cleanly onto the archive app's existing `storage_mode`
  field. AJ's audit independently warned an undefined "hybrid" staging rule defaults to an
  unreachable-wall failure mode unless it is exactly one measurable trigger like this.
- Entitlement lives in its own table, ANDed against `clearance_level`/`storage_mode` in RLS --
  never overloads `clearance_level` itself, and is deliberately built senior to whatever the
  still-separately-queued Level 1->2 rule ends up being, rather than colliding with it.
- The 100,000-member target is replaced by a net-of-fees, churn-adjusted conversion-rate
  ladder, instrumented from day one, rather than a single headline subscriber count.

Jasiah (Brain Trust) does not oppose the vintage-boundary rule itself but wants at least a
small experiment gating something closer to the front door, rather than assuming late-only
staging proves willingness to pay -- a live dissent, not resolved by this recommendation.

## Ratified
2026-09-13. Abad's ruling, quoted verbatim: "I approve of everything and I will drop my idea." The
carried recommendation is adopted as the standing monetization shape: perks-only Supporter tier +
per-content one-time unlock (kept as two separate SKUs, not merged -- see
2026-09-13-accumulating-unlock-subscription-held.md) + vintage-boundary paywall + entitlement in its
own table + conversion-rate ladder replacing the 100k target. This is now decided project direction,
not a pending recommendation. Real preconditions before build remains: the archive app's own tier/
perk design should sequence after real reader-loop signal, per
2026-09-13-signal-first-tier-design-carried.md.

## Links
- depends_on, 2026-09-13-membership-tiers-as-stated-rejected.md, the proposal this replaces
- depends_on, 2026-09-13-monetization-dissents-and-open-items.md, unresolved items this recommendation does not settle
- depends_on, 2026-09-13-leftover-material-mining-preconditions.md, where the per-content-unlock premium supply is meant to come from
