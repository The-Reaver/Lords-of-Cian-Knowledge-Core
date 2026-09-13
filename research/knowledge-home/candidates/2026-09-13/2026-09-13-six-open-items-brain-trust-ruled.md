# Brain Trust ruled directly on all six remaining monetization open items, per Abad's delegation

- id: 2026-09-13-six-open-items-brain-trust-ruled
- type: decision
- status: ratified
- class: confirmed
- source: Brain Trust ruling pass, 2026-09-13 (Celestina, Jasiah, Oluwole, Bink, Sentinel), run per
  structure-notes/brain-trust-on-demand-protocol.md, each seat working independently against a shared
  brief and instructed to give a decisive ruling per item rather than a hedge, since Abad delegated the
  ruling itself rather than asking for a recommendation to bring back to him.
- confidence: high -- every item below drew either unanimous or clearly-converged rulings from the
  seats actually in-lane for it; no split votes, no seat dissenting from another in-lane seat's ruling
- verified: 2026-09-13
- tags: lords-of-cian, archive-app, monetization, brain-trust, pricing, entitlement
- REVIEW: high-impact

## Body
Abad's instruction, quoted verbatim: "Let Brain Trust rule on the six open items now." Per the
protocol's own Mandate 1 ("a carried vote is a recommendation, Abad ratifies"), this delegation is
itself Abad's act of ratification for whatever the panel converges on below -- he is not being asked
to re-approve each individual ruling separately, having already handed the decision to the Brain
Trust for this specific batch of six items. If he wants to override any single ruling, that stays his
call at any time.

**1. Should a $1 price point exist at all?**
**Ruled: no. Price floor set at $3, no SKU below that.** Both in-lane seats (Jasiah, business
economics; Sentinel, risk/compliance) independently converged on the same number for different
reasons: Jasiah found sub-$3 units structurally negative-to-marginal once payment-processing fees
(~33% of a $1 charge) and support overhead are counted; Sentinel found $1 digital-goods transactions
disproportionately attract card-network dispute-ratio risk on a new, unproven merchant account with
no established payment history. Celestina (reader experience) had no objection to the floor itself,
only a constraint on shape if it moves: whatever replaces $1 should still map to one legible unit
("$3 unlocks this Chronicle"), not a bundle the reader has to do math on.

**2. Model G (pay-what-you-want) — reconsider or close for good?**
**Ruled: closed for good.** Unanimous across all five seats, the strongest consensus of this whole
ruling pass. Celestina: PWYW reintroduces decision friction at the exact moment a one-tap impulse
action is wanted, and creates visible inequity between readers of identical canon content. Jasiah:
unforecastable economics, no floor above processing cost, complicates the entitlement/RLS model for
no demonstrated demand upside. Oluwole: architecturally free either way (the entitlement table only
checks "does a row exist," not the amount paid) but pushes real complexity into payment-integration
and reporting for zero platform-fit benefit. Bink: destroys the clean, benchmarkable "conversion rate
at price X" per SKU the review just built the two-SKU model to support. Sentinel: compounds the
dispute-ratio problem from item 1, and arbitrary reader-chosen amounts are unfamiliar territory for
chargeback-reason-code frameworks. If Abad still wants a PWYW *feel*, the unanimous suggestion is a
small set of fixed price tiers, or a fixed floor plus an optional tip -- not true PWYW.

**3. Is it safe to run one-time unlocks and revocable subscriptions side by side as two SKUs?**
**Ruled: yes, safe -- with conditions.** Oluwole (architecture): yes without qualification, and
architecturally simpler than a merged system, since Supporter never gates content so the two systems
never need to interact in one RLS policy. The other seats attach real conditions rather than
disagreeing: Celestina requires the UI to always show "owned" (permanent) status as visually distinct
from "Supporter-active" status, everywhere, with zero flicker during a state change. Jasiah requires a
bounded refund window on the one-time unlock (14-30 days, standard digital-goods practice), after
which it's treated as permanently non-refundable with no soft support-precedent exceptions. Sentinel
sets four conditions: subscription perks must never include a permanent unlock as a benefit (the
exact abuse path Abad's dropped merge idea would have reopened under a different label); a one-time
unlock is revoked only by a chargeback/refund on its own transaction, never by an unrelated
subscription lapsing; separate webhook and entitlement-grant logic per SKU type, so a subscription
cancellation can't cascade into revoking a purchase through shared code; dispute-ratio tracking
segmented by SKU type. Bink adds a metrics condition: track two distinct funnels (subscription
conversion/churn, unlock conversion/repeat-rate), with a combined "any paying customer" figure
reported only as a secondary, labeled rollup, never the primary KPI.

**4. Free-progression (Level 1->2) vs. paid entitlement -- unify eventually, or stay parallel forever?**
**Ruled: stay two permanent, structurally separate systems -- do not plan a future unification.**
Jasiah: the net-present-cost case is clear -- a small amount of ongoing duplication now is cheaper
than an uncertain, deferred large rework bill later, and unifying them risks re-deriving a
monetization rule from a growth mechanic (or vice versa) under production pressure. Oluwole agrees on
keeping them separate now (don't overload `clearance_level` with commercial state, don't couple an
unresolved free-progression rule to a shipped payment system prematurely) but adds a cheap design
requirement: the access-check evaluation layer should already treat `clearance_level` and
entitlement-ledger membership as alternative satisfying conditions (an OR, not a merge), so any future
optionality is a change to one function's inputs, not a data migration. Bink adds a reporting
requirement: every level-attainment record gets an `access_method` tag (`free_progression` |
`paid_entitlement`) at write time, since retrofitting that attribution later is much harder. Celestina
adds a reader-facing requirement: the two backends should present as one unified "you have access"
status to the reader, who should never have to reason about which system unlocked something --
and flags that the still-unresolved Level 1->2 rule itself should be settled before more paywalled
content ships, since until it is, there's a real risk of a free-earned and a paid-purchased item
visually colliding and creating a "did I pay for this or earn it?" moment. Sentinel flags a narrower
compliance condition: if free-progression engagement data is ever used to determine what offer or
price a reader is later shown (as opposed to just what's unlocked for free), that edges toward
targeted pricing and should be disclosed in the privacy policy/ToS if it happens.

**5. Downgrade and lapse-notification policy.**
**Ruled: adopt the following as the minimum-viable policy before subscriptions go live -- not
optional, cheap enough that deferring it isn't worth the risk.** The five seats' rulings compound
cleanly rather than conflict: (a) nothing a reader has permanently unlocked is ever re-locked, under
any subscription-state change, ever (Celestina, Jasiah); (b) content already committed/queued for
delivery at the exact moment a membership lapses is grace-delivered anyway, treated as already earned
(Celestina, Jasiah); (c) full notification lifecycle -- a signup confirmation with price/cadence/
cancellation link, a pre-renewal reminder a few days ahead of each charge, payment-failure dunning
with a grace period (3-14 days, a few retries) before downgrading rather than a same-day cutoff, and a
lapse/downgrade confirmation explicitly stating that separately-purchased one-time unlocks are
unaffected (Sentinel, who ties this directly to US auto-renewal law and EU Consumer Rights/Omnibus
Directive norms, and to reducing the confusion-driven disputes that erode the same dispute ratio items
1-2 are trying to protect); (d) architecturally, this cannot be pure RLS state-checking -- it requires
a webhook-fed status-change event log as the sole legal writer to subscription status (mirroring the
existing SECURITY DEFINER RPC pattern), plus a scheduled or event-triggered dispatch job, the first
genuinely event-driven component the stack would need (Oluwole); (e) churn must be timestamped from
the server-side lapse event itself, never from a notification-sent or reader-acknowledged event, to
avoid systematically distorting the churn-adjusted conversion-rate ladder's underlying data (Bink).

**6. Missing data (reader count, conversion analog, age distribution, backlog size) -- proceed or
block?**
**Ruled: proceed now on stated, conservative assumptions. Do not block this ruling pass or the
broader launch on any of the four.** All five seats converged on a proceed-don't-block posture, with
each flagging exactly what narrower, later step each data point actually gates rather than treating
all four as blanket blockers: registered-reader count is trivially fetchable once the paused Supabase
project wakes up and isn't a real data-gathering problem, but it does need to exist before the
already-ratified conversion-rate ladder's absolute numeric targets are finalized -- not before today's
rulings (Bink). A prior engagement/conversion analog doesn't exist yet because no monetization has
ever run on this archive; use conservative industry-benchmark priors for niche-fiction/serialized
subscription conversion as an explicitly low-confidence placeholder, to be superseded by the
already-ratified pledge/waitlist pay-intent test rather than waited on as a separate data source
(Bink). Age-distribution data is not a launch blocker per se (Sentinel: COPPA turns on whether the
service is directed to children or has actual knowledge of underage users, not on an unknown fraction
of an adult-oriented readership, and this project's own standing child-safety hard-stop already
supports a general/adult-oriented posture) -- but regardless of what the real distribution turns out
to be, the payment step specifically should carry an explicit age/date-of-birth confirmation, not
just a bundled ToS checkbox, since "my child subscribed without authorization" is a high-success
chargeback narrative (Sentinel). Content-backlog size is the one figure worth an actual count before
the *next* step, not before today's six rulings -- it's needed to set the timebox/trigger for the
already-ratified signal-first paywall experiment and to judge whether the paid layer's unit economics
clear the fixed cost of building the SKU infrastructure in item 3 at all (Jasiah, Bink). Oluwole
confirmed there's no cardinality cliff in the entitlement design -- the same indexed-lookup schema
shape works whether the reader base is 100 or 100,000, so none of this blocks architecture work either.

## Links
- depends_on, 2026-09-13-monetization-dissents-and-open-items.md, the six items this note resolves
- depends_on, 2026-09-13-monetization-carried-recommendation.md, the standing shape these rulings refine
- depends_on, 2026-09-13-accumulating-unlock-subscription-held.md, item 3's conditions directly guard against this dropped idea's abuse path resurfacing through implementation
- depends_on, 2026-09-13-leftover-material-mining-preconditions.md, item 6's backlog-size figure feeds directly into that note's own precondition 1
