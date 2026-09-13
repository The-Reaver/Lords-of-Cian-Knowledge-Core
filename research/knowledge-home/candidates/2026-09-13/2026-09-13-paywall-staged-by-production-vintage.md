# Paywall staging is set by production vintage (everything already free stays free forever), not by narrative position

- id: 2026-09-13-paywall-staged-by-production-vintage
- type: decision
- status: candidate
- class: confirmed
- source: Fleet monetization review, 2026-09-13 (Brain Trust + AJ's independent audit, converged answer to review question (c))
- confidence: medium -- directionally agreed by both tracks, not yet ratified by Abad; one live dissent recorded
- verified: 2026-09-13
- tags: lords-of-cian, archive-app, monetization, brain-trust, storage_mode
- REVIEW: high-impact

## Body
Both review tracks converged on a single explicit, instrumented staging rule for when a
paywall applies, rather than a vague "decide per piece later": everything already free and
indexed as of the paywall's launch stays free and indexable forever; the wall sits only in
front of new production and newly-mined premium content going forward. This maps cleanly onto
the archive app's existing `storage_mode` field.

Rationale, both tracks: never re-gates a page already indexed by search engines (protects the
SEO/GEO strategy the whole archive is built around); never interrupts a reader mid-story; keeps
the free tier large and credible, matching Abad's own stated intent that most of the archive
stay free; and still gives paying readers something genuinely new rather than access to
content that was always going to be free anyway.

AJ's independent audit warned specifically that an undefined "hybrid" staging approach
defaults to an unreachable-wall failure mode (readers can always find some free path around an
ambiguous gate) unless it resolves to exactly one measurable trigger -- the vintage boundary is
that trigger.

Live dissent: Jasiah (Brain Trust) does not oppose the vintage-boundary rule itself but wants
at least a small experiment gating something closer to the front door of the reader journey,
rather than assuming late-only staging proves real willingness to pay. Not resolved by this
note.

## Links
- depends_on, 2026-09-13-monetization-carried-recommendation.md, the tier structure this staging rule applies to
