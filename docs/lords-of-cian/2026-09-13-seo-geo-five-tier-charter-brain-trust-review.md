# SEO/GEO/gamified-five-tier-unlock charter — real Brain Trust review

Addendum to `lords-of-cian-archive-game-plan.md`. Date: 13 September 2026. Status: **RATIFIED
2026-09-13 — all four open questions ruled on (see §5).** Source repository under review:
The-Reaver/My-Rivals-Distance-Archive / Supabase project `lords-of-cian-archive`.

---

## §0 What this replaces

On 2026-09-03, a Claude Code Remote (cloud) session — structurally unable to reach the real Brain
Trust process, per `docs/lords-of-cian/anansi-closeout-2026-08-03.md`'s own finding — improvised an
**unratified 4-seat stand-in panel** (SEO Architecture, GEO Strategy, Gamification/Engagement Design,
Continuity/Workflow-Fit) and produced a draft charter. The operator caught this before it was treated
as settled (see `research/knowledge-home/candidates/2026-09-03/2026-09-03-stand-in-panel-must-be-flagged-before-not-after.md`)
and the device-Core merge needed to run the real process was completed 2026-09-12 (see CLAUDE.md's
"Standing blocker" section, now resolved).

This document is the **real** Brain Trust review: 7 named seats (Celestina, Jasiah, Oluwole, Amaya,
Omar, Bink, Sentinel), each investigating independently with no visibility into the others, using the
fixed verdict schema and process defined in `research/knowledge-home/structure-notes/brain-trust-on-demand-protocol.md`.
The 2026-09-03 stand-in panel's draft was given to every seat as one input among several to react to,
explicitly not as something to converge on by default. No seat defaulted to it; two seats (Oluwole,
Sentinel) surfaced findings the stand-in panel never raised at all.

## §1 The charter under review

Six proposed optional fields on future `canon-ledger.json` rules (additive-only, not backfilled onto
already-locked rules), meant to be generated mechanically from each rule's approved `statement` text:
`citable`, `subject` (never defined), `slug`, `related_ids`, `world_briefing_category`,
`disambiguates_from`. Plus a five-tier thematic mapping for the Phase 2 pre-Book-1 era (T0 Arrival, T1
Organizing, T2 Confrontation, T3 Fracture, T4 Legacy/Bleed-Through) tied to `demand_scores`/
`chronicle_requests` as a drafting-priority signal.

## §2 The verdict tally

| Seat | Lane | Verdict | Confidence |
|---|---|---|---|
| Celestina, Architect | Is the schema sound enough to build on? | HOLD | high |
| Jasiah, QA/Validator | What does the evidence actually prove? | HOLD | high |
| Oluwole, Research/Validation | Is the product theory true? | SHIP WITH CONDITIONS | medium |
| Amaya, UX/UI | Does this serve the reader or just the metrics? | HOLD | medium |
| Omar, DevOps | Can this actually be shipped and run? | HOLD | medium |
| Bink, GEO Calibration | Does the score/signal mean anything? | HOLD | high |
| Sentinel, Security | What happens when this is exposed? | HOLD | high |

**6 of 7 HOLD, 1 SHIP WITH CONDITIONS. No dissent filed — a genuine, high-confidence convergence, not
a contested vote.** Per the protocol, simple majority carries; a unanimous-direction HOLD needs no
tie-break. The operator holds the veto per Mandate 1 regardless.

## §3 Findings, by seat (condensed; full verdicts held in this review session's record)

- **Celestina:** the five-tier language collides with the archive's own already-ratified four-level
  `clearance_level` model (0-3) — the game plan explicitly killed an earlier five-value `spoiler_tier`
  idea already. No sync contract exists between `canon-ledger.json` (source of truth) and Supabase's
  `knowledge_core` schema (consumer). Confirmed additive-only is schema-safe: none of the 6 field names
  collide with the real ledger today (2,197 rules, checked directly, zero duplicate IDs).
- **Jasiah:** zero code anywhere implements "generated mechanically from statement text" — a design
  proposal being handled as a decided mechanism. "Additive-only, no backfill" has no enforcing gate (no
  CI, no hook). The four-vs-five-tier drift already happened once with no repeatable check to catch a
  recurrence.
- **Oluwole:** `citable`'s premise is genuinely research-backed (Aggarwal et al., "GEO: Generative
  Engine Optimization," KDD 2024). But gated content is empirically invisible to AI answer engines (a
  2026 study found 0% AI-citation share for paywalled content vs. 91.3% open-web) — the charter never
  states which tier(s) are meant to carry the SEO/GEO weight it's built for.
- **Amaya:** a five-tier reader narrative on a four-value schema strands readers at the seam. A
  referral-gated top tier (per the game plan's own P0-4) structurally excludes "just here to read"
  users from ever reaching top-tier content. A public demand-score leaderboard plus "vote for what's
  written next" risks FOMO mechanics against the operator's standing neurodivergent-first requirement.
- **Omar:** every piece of infrastructure this needs (live Supabase, a real ledger-to-Supabase sync, a
  field-generation job) is paused, unbuilt, or a bare scaffold. The charter's own numbers (750 rules,
  49 batches) are ~3x stale against the live ledger (2,197 rules, 289 batches as of 2026-09-12).
- **Bink:** no measurement mechanism exists for the citability claim. The demand signal proposed to
  drive drafting priority is already flagged, unfixed, as fraud-prone in the archive's own game plan
  (P0-4, one person with two throwaway accounts can inflate it) — not fit to drive creative decisions
  as-is.
- **Sentinel:** the most severe, novel finding. `canon-ledger.json` carries no clearance/tier/spoiler
  field at all. Generating reader-facing `citable` text mechanically from the raw ledger — rather than
  from content that has already passed the archive's own extraction/clearance step (game plan P1-3) —
  is a designed spoiler-leak path, not a hypothetical one. Sequential IDs (`MCD-001`...`MCD-1459` etc.)
  make `related_ids`/`disambiguates_from` an ID-enumeration leak if exposed under the same public-RLS
  pattern already used for `demand_scores`.

## §4 The real disagreement map

No head-on contradiction. The seven verdicts compound rather than conflict. The one genuine framing
difference: Oluwole's fix is "decide which tier is the SEO surface" (T0, or T0+T1 via a teaser-wall);
Sentinel's fix is stricter — never generate from raw `canon-ledger.json` at all, only from
already-extracted, clearance-assigned content. These are compatible: Sentinel's constraint holds
regardless of which tier Oluwole's question resolves to.

**Scope-creep check:** none of the seven verdicts asks to expand the charter. Every finding either
demands proof before adopting a claim, or points at a mechanism the fleet already built once (the
extraction step, the `demand_scores` public-aggregate pattern) that this charter currently routes
around instead of through. Fixing this makes the charter smaller and safer, not bigger.

## §5 Ratified 2026-09-13 — the operator's ruling on all four questions

Four questions, asked directly of the operator on 2026-09-13, researched twice over (§8, §9), then
ratified as follows. Per the protocol's Mandate 1, a carried Brain Trust vote is a recommendation, not
an instruction — the operator's ruling below adopts the converged recommendation on each, which is a
real ratification, not a rubber stamp: the recommendations were reached independently, twice, by real
and disclosed-stand-in seats before the operator ruled on them.

1. **T0–T4 access-gate vs. content-classification — RATIFIED: content classification, independent of
   `clearance_level`. No schema migration.** Adopts the unanimous §8/§9 recommendation. Per Augustine's
   §9 refinement, T0–T4 must not simply move onto `canon-ledger.json` instead — it lives wherever the
   (not-yet-built) extraction step's output lives, same as the six charter fields.
2. **Which tier(s) are the deliberate SEO/GEO surface — RATIFIED: Tier 0 + Tier 1 via a teaser-wall**
   (public excerpt, full text gated behind Tier 1+). Adopts Oluwole's and Augustine's recommendation:
   Augustine's build lens found this is not new infrastructure on the current scaffold, reusing the
   already-scoped public-aggregate-view (P1-1) and reader-route (P1-2) work. The caching-safety half of
   this question was already resolved as a hard requirement in §9 (force-dynamic rendering on every
   T1+ route), independent of and prior to this tier ruling.
3. **What `subject` means — RATIFIED: `entity[] | none`, computed at read time, never stored on
   `canon-ledger.json`.** Adopts the unanimous §8/§9 recommendation (Augustine and Breaker/Correctness
   reached it independently, before either saw the other's reasoning).
4. **Whether field-generation may run against raw `canon-ledger.json` — RATIFIED: never.** Generation
   is permanently scoped to run only inside the (not-yet-built) extraction step, against
   already-extracted, clearance-assigned content. Adopts Sentinel's original hard constraint, sharpened
   by every subsequent round (§8, §9) into a build requirement, not a policy statement to be trusted on
   discipline alone.

## §6 Handoff — RICE-ordered fix list

| Priority | Item | Status | Owner |
|---|---|---|---|
| 1 | T0–T4 is a content classification, independent of `clearance_level`; no schema migration | **Ratified §5.1** | Design constraint |
| 2 | Never generate from raw `canon-ledger.json` — only from already-extracted, clearance-assigned content | **Ratified §5.4** | Design constraint |
| 3 | `subject` is `entity[] \| none`, computed at read time, never stored on the ledger | **Ratified §5.3** | Design constraint |
| 4 | Tier 0 + Tier 1 (teaser-wall) is the SEO/GEO surface | **Ratified §5.2** | Design constraint |
| 5 | Gate any demand-driven drafting priority behind the game plan's own P0-4 fraud controls (currently unbuilt) | Sequenced after P0-4 | Implementation |
| 6 | Small proof-of-concept: generate `citable`/`slug`/`related_ids` for ~10 seed **`chronicle_entries`** rows in the archive app's own Supabase DB — corrected 2026-09-13 per Augustine's finding below; the original wording ("10 real locked rules") named `canon-ledger.json` rows, directly contradicting item 2 two rows above | Non-blocking, precedes scale-up | Implementation |
| 7 | Add a repeatable check that any doc's asserted tier-count matches the live schema constraint, so the four-vs-five drift can't recur silently | Non-blocking | Implementation |
| 8 | **Resolved, not open — force dynamic rendering on every clearance-gated (T1+) route** (`export const dynamic = 'force-dynamic'` or equivalent no-store fetch); only the public T0 surface / aggregate views may be statically generated or cached. Confirmed by both Celestina and Sentinel as a real, non-hypothetical Next.js App Router default-caching gap | Ratified, folds into Phase 1's P0-3 done-when criteria | Implementation |

**Do adopt the six-field schema and the five-tier mapping — but only as ratified in §5, not as
originally drafted.** The charter's underlying ideas (a clean, quotable `citable` field; structured
reader-facing categorization; a demand-aware drafting signal) are ratified in the corrected shape §5
and this table describe: `subject` as a derived, unstored field; generation permanently scoped inside
the not-yet-built extraction step; T0–T4 as a content classification; Tier 0+1 as the SEO surface. None
of the six fields or the tier mapping should be built until the extraction step (P1-3) itself exists —
that remains a real, unremoved precondition, not a ratification of "build it now."

## §8 Second research round, 2026-09-13 — operator-requested, on the 4 open questions

The operator asked for a further round specifically on §5's 4 questions, naming Kratos, Augustin, and
the 4 Breakers as participants. None of the six are invokable as distinct sessions in this environment
(Kratos and Augustin are not registered subagent types; the Breakers' ratified charter requires
attacking an *existing build* with a different AI family, and no build exists yet). This round ran as
6 generic stand-ins under those analytical lenses, disclosed as such up front in every dispatch, per
the "flag before, not after" lesson from `2026-09-03-stand-in-panel-must-be-flagged-before-not-after.md`.
Each investigated independently, blind to the others and to this document's §1–§7.

**New finding, unrelated to this charter's fate, flagged as urgent on its own:** Breaker/Chaos verified
directly (grep across all 268 `merge_batch*.py` scripts) that every one writes `canon-ledger.json` via
`json.load` → mutate → `open(path, "w")` → `json.dump()` on the same path, truncating before writing —
zero uses of atomic temp-file-plus-rename anywhere in the codebase's history. A crash mid-write
corrupts the **entire ledger** (all 2,197 rules), not just the batch in flight. This is a present-day
defect in the existing canon-writing workflow, independent of whether this charter is ever built.
211 git commits touching the file provide an undocumented manual recovery path (`git checkout --`), but
nothing detects corruption automatically. Recommend fixing this regardless of the charter's outcome.

**Q1 (tier meaning) — research converges on: keep separate.** Augustin's builder analysis: coupling
`clearance_level` (an RLS access gate) to T0–T4 (a content/drafting-priority label) means every future
change to either forces touching both; decoupling is genuinely less total work, not just lower-risk.
Breaker/Correctness found the concrete reason coupling is dangerous: readers already at Level 3 via a
one-time referral event (some predating the P0-4 fraud fix) would either get silently promoted into a
new top tier — reopening the exact self-referral hole P0-4 was built to close — or silently demoted in
*meaning* if left numerically unchanged. Kratos's incident lens rates a botched migration HIGH severity
if it happens, though near-zero likelihood today (nothing live). **Converged recommendation: T0–T4 is a
content classification, independent of `clearance_level`. No schema migration.**

**Q2 (SEO surface tier) — research adds a structural risk beyond "pick a tier."** Kratos identified a
failure mode none of the 7 original seats raised: RLS is a database-layer control, but an SEO/GEO
strategy pushes toward static generation and CDN caching — if a gated page is ever cached without
varying the cache key by clearance, it can be served to anonymous crawlers and low-tier readers
regardless of what the database policy says, because the request never reaches the database at all.
Rated MEDIUM–HIGH: elevated likelihood precisely because the charter's whole purpose pushes toward
cacheable rendering. **This holds regardless of which tier is chosen as the SEO surface** — whatever
the answer to "which tier is public," caching/CDN behavior needs its own explicit audit alongside RLS,
not folded into it.

**Q3 (`subject` field) — research converges on: don't persist it as designed.** Breaker/Correctness
found two real ledger rules that break every candidate definition: `CC-106` (a genuinely
symmetric two-character mutual-stalemate rule, no single "the" subject) and `PH2-034` /`OPEN-012`
(author-process rules and a literally-undefined open question, no in-world entity at all). Augustin's
independent recommendation, reached before seeing Breaker/Correctness's examples: don't store `subject`
on the ledger at all — derive it at read-time in the extraction/generator layer from `category` plus
existing ID cross-references, output-only, never written back onto the additive-only source. Breaker/
Security adds: if `subject` is ever populated via an AI-parse ingestion step, it's a content-integrity
attack surface (misattribution, prompt-injection-via-source-document) with no proposed review gate.
**Converged recommendation: `subject` as `entity[] | none`, computed at read time, never stored on
`canon-ledger.json` — or dropped from the charter entirely if that's simpler.**

**Q4 (generation source) — research strengthens Sentinel's original constraint to a hard requirement.**
Every one of the 6 stand-ins that touched this question agrees with Sentinel's original finding and
sharpens it. Breaker/Security: the precondition (the extraction step, P1-3, doesn't exist yet) makes
violating the constraint the *default* outcome, not an edge case — "process discipline with no
enforceable technical control." Breaker/Correctness supplies two concrete failure cases: `MCD-314`
(a rule that reads as safe early-tier content but is actually a deliberately embargoed endgame reveal —
a mechanical classifier reading only `statement` text would leak it) and `MCD-331`→`MCD-334` (a real,
already-executed supersession that inverts which character is the protagonist — a field generated
before the correction would assert the exact fact the correction reversed, with no version pointer or
re-trigger to catch it). Augustin's build recommendation: implement the six-field generator as a
function called *inside* the extraction step itself, so pointing it at the raw ledger is structurally
impossible rather than a rule a separate batch job could accidentally break. **Converged recommendation:
build the generator only as part of the (not-yet-built) extraction step; treat "generate from raw
canon-ledger.json" as permanently out of scope, not a temporary shortcut.**

## §9 Third round, 2026-09-13 — Augustine (real seat, corrected) and the caching finding, brought to the Brain Trust

The operator corrected an error in §8: Augustine is a real, actively-used Brain Trust seat (confirmed
from same-day verdicts elsewhere in the fleet, `reports/BT_S37_SCOPE_AUGUSTINE_2026-09-13.md` and
`reports/BT_KPI_Q3Q6_VERDICT_AUGUSTINE_2026-09-13.md`), invoked the same way every other seat is — a
grounded persona prompt dispatched as a subagent — not a special registered tool. The earlier §8
Augustin stand-in was withdrawn and replaced with a properly-grounded Augustine verdict below. The
operator also asked that Kratos's caching finding be brought to the real Brain Trust rather than ruled
on directly — Celestina and Sentinel each gave a supplemental ruling on it specifically.

**Augustine, delivery-velocity lens — VERDICT: HOLD, confidence high.** Agrees with the §8 convergence
on all four questions but found one real defect in this document itself: RICE item #6 (now corrected
above) told a future implementer to pilot the generator against "10 real locked rules" — read plainly,
that means `canon-ledger.json` rows, directly contradicting item #2's hard constraint two rows above.
Recommends re-scoping the POC to the archive app's own `chronicle_entries` seed rows (already
reader-facing, never extracted from the raw ledger), and requiring any pre-P1-3 POC script to hard-fail
on any input row lacking a clearance field, turning Sentinel's "process discipline with no enforceable
technical control" into an actual control now rather than a promise. Also flags that T0–T4, once
decoupled from `clearance_level`, must not simply move to `canon-ledger.json` instead — it should live
wherever the (not-yet-built) extraction step's output lives, or it becomes a second raw-ledger
reader-facing field violating the same Q4 constraint it's meant to respect.

**Celestina, supplemental ruling — CONFIRMED REAL RISK, not hypothetical.** The game plan never
mentions SSG/ISR/CDN anywhere, but Next.js App Router defaults to static rendering for any route
without an explicit dynamic directive — the risk activates the moment the character/chronicle detail
route (P1-2) is built, by the framework's own default behavior, not a remote scenario. Constraint:
`export const dynamic = 'force-dynamic'` (or `cache: 'no-store'`) on every clearance-gated (T1+) route,
reading clearance server-side per request; only the public T0 aggregate views may be statically
generated. Does not reopen her original HOLD — additive, folds into Phase 1's done-when criteria.

**Sentinel, supplemental ruling — CONFIRMED REAL RISK**, specific to Next.js App Router's documented
default caching model (Full Route Cache + Data Cache bypass RLS entirely once a page is cached — RLS
only fires on the Supabase query, which a cache hit never makes). Concrete test once deployed: request
the same gated route as two different clearance levels, diff the bodies; check `next build`'s route
manifest for `λ (Dynamic)` vs `○ (Static)` on every gated route. Tracked as a Phase 1/P0-3 "done when"
criterion and a Phase 3 launch-QA checklist item — **not** a §5 open question, since it's a resolved
engineering requirement, not a product judgment call.

**Net effect on §5:** Q2's caching-safety half was resolved here (force-dynamic on T1+, confirmed by
two real seats) independent of which tier is chosen as the SEO surface. Q1, Q3, Q4 stand as the §8
convergence described, corroborated rather than superseded by a real seat's independent pass. **The
operator ratified all four questions on 2026-09-13 — see §5 for the rulings.**

## §7 Process note

Ran per `research/knowledge-home/structure-notes/brain-trust-on-demand-protocol.md`, from a local
Claude Code session already running inside `C:\Users\abadm\stag` with ordinary filesystem/git access —
no `mcp__remote-devices__*` device-bridge tool was available or needed. Each of the 7 seats ran as an
isolated subagent with a self-contained brief (the charter, the verified real state of the archive app,
and a local read-only clone of this repo) and no visibility into any other seat's output, matching the
protocol's independence requirement. Elijah's interview, the table, and the vote were synthesized by
the orchestrating session directly (itself a Sonnet session holding all seven verdicts, matching the
protocol's "one chat, all seven verdicts pasted in" shape) rather than run as additional subagent
calls.
