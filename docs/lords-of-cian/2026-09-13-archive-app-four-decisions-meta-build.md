# Four archive-app product decisions — meta-build recommendations

Addendum to `lords-of-cian-archive-game-plan.md`. Date: 13 September 2026. Status: **RATIFIED
2026-09-13 — all four meta-build recommendations adopted as written below.** Source repository:
The-Reaver/My-Rivals-Distance-Archive / Supabase project `lords-of-cian-archive`.

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

**WORKFLOW:** Event tables (requests, completion-weighted reads, credited referrals) feed a scheduled
recompute job into the existing `demand_scores` table, stamped `last_computed_at`. Full recompute from
source each cycle, never incremental counters (Breaker/Chaos: incremental counters that crash
mid-decrement inflate a trend permanently and never self-correct).

**SPECIFICATION for the reader:** A number that visibly moves with momentum, not raw popularity —
"what's rising," not "what's biggest."

**WHAT THE UI DOES:** Character hero and Character Index show score + trend arrow only, never raw
sub-component counts. Admin's Demand panel shows the decomposition (per-input counts, trend, an
anomaly flag) so an author can see why a number moved before staking a multi-year writing decision on
it.

**HOW IT SERVES:** The reader gets a legible way to signal interest that actually moves the needle
even from a low base (Onyx-shaped characters aren't structurally locked out); the author gets a
number that's honest about its own fraud exposure rather than quietly trusted.

---

## Decision 2 — Level 2 clearance-unlock rule

**Meta-build recommendation:** **OR-gate** (read 3 chronicles fully, OR share once, OR request 2) —
this is the strongest convergence of the four decisions: 10 of 11 investigators independently landed
here, from completely different reasoning paths (product/content-pacing, funnel math, implementation
simplicity, UX legibility, and — critically — even the two seats whose job was to attack it).

- **Oluwole's independent mathematical case:** for any set of independent completion probabilities,
  an OR-gate structurally cannot convert worse than an AND-style gate built from the same components
  — this is arithmetic (Steiner's disjunctive-task logic), not a preference.
- **Amaya/Celestina's UX case:** an OR-gate removes the working-memory burden of tracking partial
  progress across three heterogeneous action types, and doesn't strand a reader on a
  character with fewer than 3 published entries (nine of eighteen characters currently have zero).
- **The security seats did NOT override the product call, but attached a hard precondition:**
  Sentinel and Breaker/Security both confirm the OR-gate is trivially bypassable **as currently
  specified** — a single scripted "request 2 chronicles" call, with no verification, clears it. This
  is not a reason to reject OR-gate (2-of-3 is bypassed almost as cheaply, per Breaker/Security's own
  analysis — it just costs one more scripted call). It is a reason the OR-gate **must not go live**
  before each leg is hardened: "share" must be a verified deep-link click-through opened by a
  different session, never a bare button-click; "request" must be capped at 1-per-user-per-character,
  reusing the same uniqueness rule P0-4 already designs for Level 3.
- **Breaker/Correctness's implementation requirement:** ship this as a **derived, recomputed check**
  (re-evaluated against source tables), not a one-shot event trigger — a trigger-only implementation
  silently strands any reader who already completed one qualifying action *before* this feature
  shipped, since nothing will ever re-fire for them. Backfill existing progress on deploy.
- **Kratos's default-safety requirement:** any bug in the unlock check must **fail closed** (deny),
  never fail open — matches the same default-deny posture already mandated for RLS.

**WORKFLOW:** A trigger/edge function evaluates the OR condition on each qualifying insert
(read-completion, verified share, capped request) and writes `clearance_level` server-side, never
client-trusted. A reconciliation pass runs on deploy (backfill) and periodically thereafter
(self-heals any drift — Breaker/Chaos's fix for the crash-between-check-and-write limbo scenario).

**SPECIFICATION for the reader:** Three independent, low-friction paths to the same unlock; any one
suffices; no combination bookkeeping.

**WHAT THE UI DOES:** Progress shown as three parallel tracks, not a single "2 of 3" counter. Unlock
itself is a quiet Activity Feed line — no confetti, no modal, matching the platform's existing
non-gamified posture.

**HOW IT SERVES:** Fastest plausible route past the exact stall point the game plan already treats as
a diagnosable failure mode, without handing an unauthenticated script a one-call bypass.

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
  already established (§5.4).

**WORKFLOW:** Admin triggers an async batch job (Message Batches API, cached schema/system prefix) →
per-document idempotent processing with a job-tracking table (queued/parsed/written/failed) → each
character record reconciled against existing locked canon before write (new/auto-merge/conflict-queue)
→ conflict-bucket items go to an admin review screen (existing-vs-parsed side by side); everything
else writes straight through to Writer-Reference only, never reader-facing directly.

**SPECIFICATION for the admin (this is an internal tool; readers never interact with it directly):**
Bulk, cost-bounded, auditable processing of the Character Codex corpus that cannot silently reverse a
decision the operator already made by hand.

**WHAT THE UI DOES:** Admin sees job status, a cost estimate before confirming a run, and a
conflict-review queue with accept/reject/edit per field — never a bulk "approve all."

**HOW IT SERVES:** Gets the ~1M-word corpus ingested at real scale without either leaking a live
credential in the codebase's first public history, or mechanically undoing canon decisions the
operator already settled by hand.

---

## Ratified 2026-09-13, and two items independent of these four decisions

All four meta-build recommendations above are ratified as written. Two items are independent of any of
the four decisions and should be actioned regardless:

1. **Rotate/confirm the Anthropic API key is absent from anything entering this codebase's first git
   push** (Breaker/Security's SEVERE finding) — time-sensitive, unrelated to which of the four
   decisions gets built first.
2. The demand-score and clearance-unlock builds both explicitly depend on P0-4 (fraud/identity
   controls) landing first, for the fraud-safety and gate-hardening reasons in Decisions 1 and 2 above
   — this is already sequenced in the game plan, restated here because three independent investigators
   converged on it as a hard precondition, not just a preference.
