# Four archive-app product decisions — meta-build recommendations

Addendum to `lords-of-cian-archive-game-plan.md`. Date: 13 September 2026. Status: **RATIFIED
2026-09-13, then RECONCILED same day against a parallel real Brain Trust review** run with live
access to the actual app repo and Supabase project (`2026-09-13-archive-app-six-open-items-brain-trust-review.md`
in the Knowledge Core) — see the correction notes inline below, most substantially on Decision 2.
Source repository: The-Reaver/My-Rivals-Distance-Archive / Supabase project `lords-of-cian-archive`.

**Why two reviews, and how they relate:** this review's 11 investigators worked from
`lords-of-cian-archive-game-plan.md` and `canon-ledger.json` — no code or live-database access (every
investigator disclosed this). The parallel review had exactly the access this one lacked, and found
real, code-verified facts this review could only reason about from prose. Where they conflict, the
live-verified review controls; where this review found something the code-only review couldn't have
(the canon-ledger-specific findings in Decisions 1, 3, and 4 below), those stand as this review's own
contribution. Neither review is discarded — this document now states the reconciled position.

## Process

11 independent investigators — Celestina, Jasiah, Oluwole, Amaya, Omar, Bink, Sentinel (the 7 Brain
Trust seats), Augustine, Kratos, and all 4 Breakers (Security, Correctness, Scale, Chaos) — each
researched all four decisions on their own, with no visibility into the others' work. None defaulted
to a prior session's suggestion; several reached conclusions no earlier pass had considered. All are
real, actively-invoked fleet seats (confirmed via same-day and prior sealed verdict reports across
this fleet — see `2026-09-13-brain-trust-seats-are-invoked-by-grounded-persona-prompt-not-a-registered-tool.md`
in the Knowledge Core), not disclosed stand-ins.

---

## Decision 1 — Reader Demand Score formula

**Meta-build recommendation:** A trend-based score (7-day/30-day window, or an EMA-style momentum
measure), computed server-side on a schedule (not live-per-request), built from **reader-behavior
signals only** — never content-volume signals.

- **Convergence (near-unanimous):** raw cumulative count is rejected by every investigator who
  addressed formula shape. The score must show momentum, matching the game plan's own stated bar
  ("150-rising outranks 200-flat").
- **The sharpest new finding (Breaker/Correctness, verified against real ledger data):** Onyx — the
  narrator credited on every recent Chronicle, with 156 mentions across the ledger — has exactly
  **one** dedicated rule under his own identity, because extraction (P1-3) hasn't shipped yet. Any
  formula using content-supply as an input or normalizer would rank him last on the exact metric
  meant to decide who gets written next. **The formula must never use rule count, document count, or
  word count as an input — demand is a reader-side fact, not a producer-side one.**
- **Fraud gate (Celestina, Bink, Augustine, Kratos, Breaker/Security, independently):** the demand
  signal is provably fraud-prone today (email confirmation disabled, zero uniqueness/rate-limit
  controls per the game plan's own P0-4). **No formula shape fixes this.** Build and test the formula
  now, admin-only, unranked, not publicly displayed or sort-driving until P0-4's verified-identity
  controls land.
- **Bink's refinement:** discount or exclude `shares` (a one-click action, possibly an inverse
  indicator) and referral-chain-derived inputs specifically — referrals are already the load-bearing
  fraud vector for Level 3 abuse; feeding the same vector into drafting-priority doubles one root
  cause across two systems.
- **Sentinel's requirement:** served only through a `SECURITY DEFINER` view/function with a
  publicly-listed-only filter and either a materialized/cached refresh or rounded scores — never a
  live per-request aggregate, which would let an attacker reconstruct the raw event stream by polling
  and differencing.
- **Correction from the live-verified parallel review, replacing an assumption this review had no way
  to check:** this review assumed all four candidate inputs were equally unvalidated. Direct grep
  against the real repo (Jasiah, that review) found `chronicle_requests` and `referrals.credited`
  **already carry server-side validation** (confirmed-email gate, unique constraint, rate limit) —
  `reads.completion_pct` and `shares` have **none**. The formula should weight accordingly now, not
  wait for uniform hardening: `chronicle_requests` and `referrals.credited` highest, `reads` and
  `shares` at near-zero weight until they get equivalent server-side backing. That review's synthesis
  (Bink + Jasiah) is the sharper sequencing call and is adopted here: ship `demand_scores` **display-
  only, feeding no automated drafting-priority decision**, until input-hardening is complete — matching
  this project's own RICE item already ratified in the SEO/GEO charter review (§6 item 5 of that
  document). Also adopted: a minimum-sample floor before any trend is computed or trusted (this
  product's real per-character volume is far below the scale the trend-weighting precedent — Reddit/HN
  — comes from), a per-reader contribution cap per character independent of per-input weighting, and
  **no reader-facing ranking or leaderboard, ever** — not "until hardening lands." A public
  rising/falling rank-against-others display is a FOMO mechanic regardless of input quality, per the
  same neurodivergent-first finding Amaya made independently in both reviews. A soft, single-character
  "readers have asked for this" note is fine; a ranked list is not.

**WORKFLOW:** Event tables (requests, completion-weighted reads, credited referrals) feed a scheduled
recompute job into the existing `demand_scores` table, stamped `last_computed_at`. Full recompute from
source each cycle, never incremental counters (Breaker/Chaos: incremental counters that crash
mid-decrement inflate a trend permanently and never self-correct).

**SPECIFICATION for the reader:** A number that visibly moves with momentum, not raw popularity —
"what's rising," not "what's biggest."

**WHAT THE UI DOES:** Character hero shows a soft, single-character "readers have asked for this" style
signal with a trend indicator — never a Character-Index-wide ranked list or leaderboard, and never
displayed at all (reader-facing) until display-only ships and input-hardening lands. Admin's Demand
panel shows the full decomposition (per-input counts, trend, an anomaly flag) so an author can see why
a number moved before staking a multi-year writing decision on it — and, until hardening lands, sees
it feeding no automated decision at all.

**HOW IT SERVES:** The reader gets a legible way to signal interest that actually moves the needle
even from a low base (Onyx-shaped characters aren't structurally locked out); the author gets a
number that's honest about its own fraud exposure rather than quietly trusted.

---

## Decision 2 — Level 2 clearance-unlock rule

**CORRECTED 2026-09-13.** This review originally recommended a pure OR-gate, hardened per-leg. The
parallel live-verified review found that doesn't hold: against the actual real schema, "share" is
fundamentally a single unverified click today, with no rate limit and no realistic way to harden it
into a real barrier — a hardened-OR design still has a one-click bypass at its weakest leg no matter
how the strongest leg (`request`, which does have real backing — see below) is treated. **Meta-build
recommendation, reconciled: "read, plus one of {share, request}" — a completed read is mandatory, not
one of three interchangeable options.**

- **Why this review's original OR-gate reasoning wasn't wrong, just incomplete:** the funnel-math case
  (Oluwole, this review) for OR over strict 2-of-3 — an OR-shaped gate structurally converts at least
  as well as an AND-shaped one built from the same components — still holds and is *why* the
  reconciled design isn't strict 2-of-3 either. Oluwole's parallel-review counterpart independently
  reached the same read: a multi-path gate's real behavioral cost is set by its cheapest path, so
  *some* path must be hardened to a real floor, or the whole gate is only as strong as its weakest
  link. "Read, plus one of {share, request}" keeps two real paths to the optional half (satisfying
  the funnel-math preference for choice) while making the one path with actual engagement cost
  (reading) non-optional.
- **Confirmed against real code (the parallel review, Bink):** `chronicle_requests` already has
  server-side validation (confirmed-email gate, unique constraint, rate limit) — it is the stronger of
  the two optional companions and should be treated as such. `share` remains the weaker one, worth
  flagging as still-soft even inside this hardened design, per this review's own original finding
  that a share event has no backend verification that it reached anyone.
- **Confirmed against real code (the parallel review, Sentinel):** direct client self-promotion of
  `clearance_level` is already structurally impossible today — table-level `UPDATE` on
  `reader_profiles` was fully revoked when an earlier feature closed the same class of gap. Whichever
  design ships must go through a `SECURITY DEFINER` RPC, matching the pattern this codebase already
  uses successfully (`change_followed_character()`), never a direct client `UPDATE`, and must not
  re-open a table-wide `UPDATE` grant to fix some unrelated column later.
- **Amaya/Celestina's UX case, still valid, adapted to the corrected design:** show live, passive
  progress feedback ("read: 2/3, plus one of share/request") rather than a silent threshold — an
  invisible gate feels arbitrary regardless of the logic underneath, and this matters more, not less,
  now that reading is mandatory rather than one of three equal options.
- **Real, unresolved product tension, not smoothed over (both reviews independently surfaced it):**
  this project's own prior internal audit (game plan P0-2) wanted a permissive OR specifically to
  avoid Level-1 stalling; the fraud-conscious finding above wants a stricter, read-mandatory gate.
  "Read, plus one of {share, request}" is offered as the middle path — harder to game than pure OR,
  meaningfully easier to reach than strict 2-of-3 — but this remains a real product call the operator
  should confirm explicitly, not something either review can fully rule past.
- **Breaker/Correctness's implementation requirement (this review), still adopted:** ship as a
  **derived, recomputed check** (re-evaluated against source tables), not a one-shot event trigger — a
  trigger-only implementation silently strands any reader who already completed a qualifying action
  *before* this feature shipped. Backfill existing progress on deploy.
- **Kratos's default-safety requirement (this review), still adopted:** any bug in the unlock check
  must **fail closed** (deny), never fail open.
- **New, adopted from the parallel review (Oluwole):** tag `access_method` (which path satisfied the
  gate) at write time — cheap now, hard to retrofit, and the only way to later detect if Level 2
  "stops meaning anything."

**WORKFLOW:** A `SECURITY DEFINER` RPC evaluates "read ≥3 AND (verified-share OR rate-limited-request)"
on each qualifying insert and writes `clearance_level` server-side, tagging `access_method`. A
reconciliation pass runs on deploy (backfill) and periodically thereafter, self-healing any drift from
a crash between check and write.

**SPECIFICATION for the reader:** Reading three chronicles is always required; whichever of share or
request the reader also does completes the unlock — not three interchangeable options, and not a rigid
2-of-3 tally across unrelated action types.

**WHAT THE UI DOES:** Progress shown as "reading: 2/3" plus a secondary "and one of: share or request"
track — not a single opaque counter. Unlock itself is a quiet Activity Feed line — no confetti, no
modal, matching the platform's existing non-gamified posture.

**HOW IT SERVES:** Keeps a real, low-friction path to Level 2 that a reader who "just reads" can
complete on their own terms, while closing the one-click bypass a pure OR-gate would have handed to an
unauthenticated script.

---

## Decision 3 — `quiz_questions` (P3-1)

**Meta-build recommendation:** **Defer the full build**, but the design is already resolved and should
ship exactly as specified whenever it does: an ungated diagnostic, first-attempt-only scoring,
unlimited retries, sourced **only** from already-published, locked, reader-facing content.

- **Why defer, not drop:** two independent seats (Omar, Celestina) found the same real bottleneck —
  only ~10 chronicle entries exist across 18 characters, nine with zero. Most quiz value is blocked on
  content volume the feature itself can't fix. Dropping it discards a working `quiz_attempts` table
  and the one diagnostic (per-question first-try pass rate) nothing else provides; building it now
  competes for effort against the actual bottleneck (chronicle-writing throughput, P1-4).
- **The sharpest finding, and the reason "build now" would be actively unsafe as a naive
  implementation (Breaker/Correctness, verified against the real ledger):** `CONFLICT-005` documents
  that the Character Codex **deliberately** states Pyro's mother was "killed," while the actual locked
  canon (`MCD-131`/`MCD-132`) is that she survived — the misdirection is intentional in-world
  narrative, not an error. A quiz question generated naively from source text would confidently teach
  readers the false answer as fact. Three additional rules are formally superseded in the live ledger
  right now (`WC-008`, `WC-023`) — a keyword-scraped generator would surface a wrong "correct answer"
  from these today, not hypothetically.
- **Required design constraint, therefore:** generate candidate questions only from `status: locked`
  rows, explicitly excluding anything flagged in `conflicts[]` or superseded, and route every
  generated question through one-time human approval before it enters the live bank. Never generate
  from raw `canon-ledger.json` directly to a reader-facing table — same principle the ratified SEO/GEO
  charter review already established for the six-field schema (§5.4 of that review).
- **Security requirements (Sentinel, Breaker/Security):** correct-answer validation server-side only,
  never shipped to the client pre-answer; first-attempt flag set server-side and immutable, so no
  client-side reset can manufacture a fake "first attempt."
- **Bink's boundary:** quiz performance must never feed the demand score or any clearance gate — it
  measures comprehension, not desire for more content; conflating the two misdirects whatever response
  a low signal calls for.
- **Chaos-safety (Breaker/Chaos):** write each attempt as one atomic row at completion, not
  per-question — a crash mid-quiz then just means a redo, with no ambiguous partial state to reconcile.
- **Real, already-shipped vulnerability, confirmed by the parallel live-verified review (Sentinel) —
  lands regardless of the build/defer timing call:** `quiz_questions_select`'s RLS policy grants the
  entire row, including `correct_index` (the answer key), to any signed-in reader before they've
  answered — Postgres RLS is row-level only, not column-level. No UI exists yet so nothing is
  exploited today, but the schema as currently committed is unsafe to build a client feature directly
  against. Fix, matching a pattern this codebase already uses twice: a `SECURITY DEFINER` grading RPC
  (`submit_quiz_answer(question_id, selected_index)` returning `{is_correct, explanation}`, writing
  `quiz_attempts` server-side) plus a public fetch view that omits `correct_index` and `explanation`
  entirely. This fix should land whenever the table is first touched by real application code,
  independent of whether the feature ships this quarter or later.
- **Oluwole's counterpart in the parallel review, on value if this ever ships:** published engagement
  data (BuzzFeed) shows identity/personality quizzes drive sharing, not trivia-with-a-score — the
  per-character trivia format as specced here won't behave like a viral growth mechanic even built
  well, though it remains a genuine utility for power readers navigating an already-large canon
  (2,197+ locked rules) as a self-check. Don't oversell this as an engagement/growth feature in
  planning documents; it's a comprehension aid.

**WORKFLOW:** After a reader finishes a character's arc, an optional "Correspondence" prompt appears;
first attempt logs pass/fail per question (server-validated) to `quiz_attempts`; unlimited retries are
allowed but excluded from the diagnostic.

**SPECIFICATION for the reader:** An in-world correspondence, not a test — no grade, no percentage,
no pass/fail badge visible to them beyond the immediate narrative reply.

**WHAT THE UI DOES:** Text-only, reply-letter framing; results route silently to an admin-facing
per-question pass-rate dashboard, never displayed to the reader as a score.

**HOW IT SERVES:** Delivers a genuine, well-evidenced retrieval-practice benefit (repeated testing
measurably improves retention versus rereading) without the evaluation-apprehension risk gamified
assessment research documents, and without ever risking teaching a reader something false as canon.

---

## Decision 4 — Bulk Character Codex ingestion (P1-6)

**Meta-build recommendation:** **Build the pipeline architecture now**, as a dormant, mock-testable
scaffold — every investigator who addressed this converged here, though several split the "build now"
claim into what's genuinely buildable pre-key versus what isn't.

- **What's buildable and testable without a key (Omar, Augustine, Breaker/Scale, Breaker/Chaos):**
  batching/chunking logic, the Message Batches API request shape with prompt-caching on the repeated
  schema prefix, DB write-path transactionality, and — the two sharpest, concrete requirements below —
  reconciliation logic and idempotency. All of this is testable against a mocked client or real
  existing ledger rows as fixtures, not just code that "looks done."
- **The sharpest finding (Breaker/Correctness, verified against real ledger history):** `CC-025` and
  its resolution `MCD-134` document a real, already-occurred case where the Character Codex source
  contained two incompatible profiles for the same character (Lilith Cyzak) — resolved by hand, with
  one profile explicitly discarded as non-canon. **A naive bulk-insert ingestion job has no way to
  know that fight already happened and would silently re-litigate or overwrite the resolved canon by
  pure mechanical order-of-operations.** The pipeline must be reconcile-then-merge: look up every
  ingested character against existing locked rules before writing; new characters auto-insert,
  consistent matches auto-merge, **conflicting matches route to an admin review queue** — reusing the
  exact review pattern that already resolved `MCD-134` once by hand.
- **The second sharpest, independent finding (Breaker/Chaos):** without a unique/idempotency key per
  source-document-plus-section, a crash mid-batch followed by a naive retry duplicates already-written
  records rather than resuming — this scaffolding is cheap to build correctly now and expensive to
  retrofit after ambiguous partial rows already exist.
- **What's genuinely NOT buildable pre-key (Jasiah, Augustine, Oluwole):** extraction-quality
  validation — prompt/schema tuning, hallucination rate, real chunking behavior — is model-and-prompt
  sensitive (a 2026 clinical-extraction sensitivity study is cited as real evidence this doesn't
  transfer cleanly across model swaps). Do not claim the pipeline "works" pre-key; that claim is
  structurally unverifiable until a real run happens.
- **Security requirements, and the one item independent of this decision's timing entirely
  (Sentinel, Kratos, Breaker/Security — all three, independently, treat this as the sharpest finding
  across all four decisions):** the game plan itself already names the Anthropic key as a
  rotate-before-second-platform hygiene item. Breaker/Security's finding sharpens it: this codebase
  has never been through a git-history secret scan and is about to receive its first-ever push — **if
  a key is sitting in any file today, that push is the exposure moment, and it's not reversible once
  forks/clones exist.** Rotate and confirm the key is absent from anything entering version control
  **before** the first push, independent of whether the ingestion pipeline itself ships this quarter.
- **Isolation requirements once live (Sentinel, Bink, Breaker/Security):** admin-only trigger, never a
  public route; fail closed if no key is configured (explicit error, never a silent no-op); every
  newly-ingested row defaults to the most restrictive clearance/publish state available; output always
  lands in Writer-Reference only, staged behind mandatory human review before any promotion to
  reader-facing tables — the same never-auto-publish boundary the ratified SEO/GEO charter review
  already established (§5.4 of that document, corrected 2026-09-13 same day: see below).
- **Correction from the parallel live-verified review, strengthening rather than weakening this
  decision:** the extraction/ratification machinery this decision and the SEO/GEO charter both assume
  is "not yet built" **already exists and is tested** — the `knowledge_core` migration, `extraction.py`,
  `ratification.py`, `routes_knowledge_core.py`, and a full `draft → under_review → ratified → locked`
  state machine. The reconcile-then-merge requirement above is not a design to build from scratch — it
  should plug into this existing, tested state machine (AI-Parse output enters as `status='draft'`
  through the existing repository layer, never a new, less-guarded write path). This makes "build the
  pipeline now" a narrower task than originally scoped: only the AI-Parse auto-population step is
  actually missing, not the review/promotion machinery around it.
- **Additional converged conditions from the parallel review, adopted here:** the Anthropic key belongs
  as a Railway environment variable on canon-service, matching the existing `DATABASE_URL` pattern —
  never Supabase Vault (a separate system requiring a needless network fetch) and never client-exposed.
  An explicit child-safety pre-screen must run before any extraction output is shown for human review,
  matching this project's own zero-exception standing hard-stop rule, already invoked once for real.
  Before AI-Parse output ever reaches rendered markdown: confirm the frontend's markdown renderer stays
  configured without raw-HTML passthrough for AI-generated content, or add explicit sanitization at the
  ingestion boundary — its current "never end-user input" trust comment is true today and becomes false
  the moment this feature ships, a genuinely new finding neither review would have made without
  checking the actual render path. Visually distinguish AI-parsed reference entries from hand-drafted
  Chronicles in the reader UI, so auto-extracted text isn't judged against hand-crafted prose by the
  same bar.

**WORKFLOW:** Admin triggers an async batch job (Message Batches API, cached schema/system prefix) →
per-document idempotent processing with a job-tracking table (queued/parsed/written/failed) → each
character record reconciled against existing locked canon before write (new/auto-merge/conflict-queue)
→ conflict-bucket items go to an admin review screen (existing-vs-parsed side by side); everything
else writes as `status='draft'` through the *existing* `extraction.py`/`ratification.py` state machine,
never a new write path, and never reader-facing until it clears that machinery's own review step.

**SPECIFICATION for the admin (this is an internal tool; readers never interact with it directly):**
Bulk, cost-bounded, auditable processing of the Character Codex corpus that cannot silently reverse a
decision the operator already made by hand.

**WHAT THE UI DOES:** Admin sees job status, a cost estimate before confirming a run, and a
conflict-review queue with accept/reject/edit per field — never a bulk "approve all."

**HOW IT SERVES:** Gets the ~1M-word corpus ingested at real scale without either leaking a live
credential in the codebase's first public history, or mechanically undoing canon decisions the
operator already settled by hand.

---

## Cross-cutting note

Both reviews, independently, converged on the same underlying observation: the demand-score formula,
the clearance gate, and (per the parallel review) the email-provider choice all draw on the same
handful of raw signal tables and the same unresolved identity/fraud gap (P0-4). This isn't four (or
six) independent risks — it's one risk wearing several outfits. Landing P0-4 once unblocks more of this
review than any single decision above does on its own.

## Ratified 2026-09-13, reconciled same day, and two items independent of these four decisions

All four meta-build recommendations above are ratified as reconciled (Decision 2 corrected from its
original pure-OR-gate form; Decisions 1, 3, and 4 refined against live-verified facts the original
11-investigator pass didn't have access to). Two items are independent of any of the four decisions
and should be actioned regardless:

1. **Rotate/confirm the Anthropic API key is absent from anything entering this codebase's first git
   push** (Breaker/Security's SEVERE finding) — time-sensitive, unrelated to which of the four
   decisions gets built first.
2. The demand-score and clearance-unlock builds both explicitly depend on P0-4 (fraud/identity
   controls) landing first, for the fraud-safety and gate-hardening reasons in Decisions 1 and 2 above
   — this is already sequenced in the game plan, restated here because multiple independent
   investigators across both reviews converged on it as a hard precondition, not just a preference.

**Out of scope for this document, handled in the parallel review instead:** the email-provider choice
(Resend vs. holding for confirmed-email re-enablement) and the Supabase unpause go/no-go are real,
live decisions that document covers — this document doesn't duplicate them, since they were never part
of the four decisions this investigation was scoped to.
