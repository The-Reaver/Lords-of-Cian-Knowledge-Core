# The $1/$2/$3-on-clearance_level membership proposal as originally stated was rejected by both independent fleet review tracks

- id: 2026-09-13-membership-tiers-as-stated-rejected
- type: decision
- status: ratified
- class: confirmed
- source: Fleet monetization review, 2026-09-13 (7-seat Brain Trust + Elijah's feasibility interviews, and AJ's independent 4-Breaker audit, run blind to each other)
- confidence: high -- both independently-run tracks converged on the same three problems without seeing each other's reasoning; treat the convergence itself as the strongest signal, not either track's internal vote count alone
- verified: 2026-09-13
- tags: lords-of-cian, archive-app, monetization, brain-trust, clearance-level
- REVIEW: high-impact

## Body
Abad's proposal -- three membership tiers ($1/$2/$3 per month) mapped directly onto the
archive app's existing `clearance_level` column, with "unlocking and keeping access" implying
a lapsing subscription -- was put to both the 7-seat Brain Trust (Celestina, Jasiah, Oluwole,
Amaya, Omar, Bink, Sentinel, Omar recording NO CONFIDENCE as out-of-lane) and AJ's independent
4-Breaker adversarial audit. Both tracks returned HOLD, reached independently by different
methods, converging on the same three problems:

1. Mapping tiers directly onto `clearance_level` collides with the still-separately-open Level
   1->2 free-promotion rule (queued for the same Brain Trust, unresolved as of this review) --
   a free reader could end up outranking a paying one under some readings of that rule.
2. "Keeping access" was described as revocable, but no re-lock-on-lapse mechanism exists
   anywhere in the archive app's codebase today. As specified, what would actually ship is a
   disguised one-time unlock, not a real subscription.
3. The 100,000-paying-member target has no funnel or economics grounding -- realistic card
   fees, chargebacks, and churn-cycling on sub-$2 recurring charges could plausibly cut real
   net revenue to 40-60% of the naive gross figure.

The proposal as literally stated is not being implemented. See
2026-09-13-monetization-carried-recommendation.md for what both tracks converged on instead.

## Ratified
2026-09-13. Abad's ruling, quoted verbatim, given as one blanket approval covering all eight of
this date's monetization candidate notes: "I approve of everything and I will drop my idea." Applied
here as: Model A's rejection stands as final.

## Links
- depends_on, 2026-09-13-monetization-carried-recommendation.md, the alternative both tracks converged toward
