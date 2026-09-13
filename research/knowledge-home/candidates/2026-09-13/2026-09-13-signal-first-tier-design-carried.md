# Abad's "design tiers after reader-loop signal, not before" idea was carried by a scoped 5-seat Brain Trust reaction pass -- SHIP WITH CONDITIONS, strongest consensus of the whole review process so far

- id: 2026-09-13-signal-first-tier-design-carried
- type: decision
- status: candidate
- class: confirmed
- source: Scoped 5-seat Brain Trust reaction pass, 2026-09-13 (Celestina, Jasiah, Oluwole, Bink, Sentinel), reacting to an idea Abad proposed after reading the carried recommendation in 2026-09-13-monetization-carried-recommendation.md. Run per the now-unblocked structure-notes/brain-trust-on-demand-protocol.md, seat-by-seat via the Agent tool from inside this session.
- confidence: high -- 5/5 seats support shipping in some form (1 SHIP, 4 SHIP WITH CONDITIONS); not yet ratified by Abad
- verified: 2026-09-13
- tags: lords-of-cian, archive-app, monetization, brain-trust, metrics, demand-scores
- REVIEW: high-impact

## Body
Abad's idea: rather than finalizing what content/perks sit behind which tier now and adding
instrumentation at launch to measure conversion afterward (the carried recommendation's
implicit order), hold off on locking the tier/perk structure until the archive's own
already-live engagement signals (demand_scores, chronicle_requests, character_comparisons,
also_drawn_to, field_notes, shares) show what readers actually gravitate to. Reverses
design-then-measure into measure-then-design.

Tally: 1 SHIP (Celestina), 4 SHIP WITH CONDITIONS (Jasiah, Oluwole, Bink, Sentinel) -- the
strongest cross-seat agreement of any question put to this or the prior review (which itself
had already identified this same instinct as Model F, its own strongest-consensus item).
Carried, with real conditions attached:

- **Jasiah:** as stated, "wait for signal" has no stopping condition and can quietly become
  "monetize never" by drift rather than decision. Wants an explicit trigger (a date or a volume
  threshold on chronicle_requests) plus one genuine real-money or pledge-style signal running
  alongside the free engagement data -- clicks show what readers want, a pledge shows what
  they'd pay.
- **Bink (the sharpest critique, central to this seat's own lens):** none of the six signals
  have ever been validated against real payment behavior -- at zero price they measure
  engagement/curiosity, a related but distinct construct from willingness-to-pay. Flags two
  signals as actively risky to use this way: `shares` is likely an *inverse* indicator (exactly
  the top-of-funnel acquisition content that should stay free, not get paywalled), and
  `field_notes` skews toward the most engaged existing free power-users, the classic
  freemium-paradox segment least likely to convert. Also flags that `chronicle_requests` is
  already spoken for as a free perk in the carried recommendation -- reusing the same signal to
  decide what gets locked behind a paywall risks a reader feeling misled ("I asked for this and
  you charged me for it"). Raises a specific Goodhart's-law risk when asked directly: if readers
  suspect that requesting/comparing/favoriting too visibly gets something paywalled, the
  highest-value signal gets suppressed and lower-awareness signals become vulnerable to
  organized brigading by small fan clusters -- mitigate by not disclosing the signal-to-paywall
  linkage and manually reviewing suspicious pre-decision spikes rather than automating on them.
- **Oluwole:** architecturally cheap to defer, since the engagement tables are already
  decoupled from any entitlement/paywall table -- but only if the eventual gating logic stays
  data-driven (a mapping table, not hardcoded content IDs) and reuses the already-proposed
  `storage_mode` field rather than inventing a new classification column, which would itself
  become an unplanned third system.
- **Sentinel:** poses no new payment/chargeback exposure since no money changes hands during
  the observation period, and is compatible with every open dissent from the prior review
  without needing to resolve any of them first. Two conditions: honor the already-agreed
  free-content vintage boundary (don't let a later tier decision retroactively reclassify
  content a reader already engaged with as free -- a bait-and-switch risk), and check whether
  the engagement signals are account-linked; if so, flag for a privacy/purpose-limitation
  language review before using free-era behavioral data to drive a monetization decision.
- **Celestina:** content interest and willingness-to-pay are not the same thing -- paywalling
  the most-beloved content on a high demand_scores reading risks exactly the reader-trust
  backlash the archive's free-first culture is built to avoid. Also flags that given the
  project's existing content volume, there may already be enough accumulated signal to act on
  soon rather than facing a long wait -- worth a metrics-seat read on actual signal volume
  before assuming this means a long delay.

## Links
- depends_on, 2026-09-13-monetization-carried-recommendation.md, the recommendation this idea resequences
- depends_on, 2026-09-13-monetization-dissents-and-open-items.md, confirmed compatible with every open item there without resolving them
- relates, 2026-09-13-accumulating-unlock-subscription-held.md, the companion idea from the same reaction pass, which held
