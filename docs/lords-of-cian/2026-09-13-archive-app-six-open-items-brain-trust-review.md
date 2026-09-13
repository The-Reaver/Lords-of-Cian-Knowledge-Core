# Six queued archive-app decisions — real Brain Trust review

Addendum to the archive-app repo's own CLAUDE.md ("Six decisions queued for the real Brain Trust,
2026-09-13"). Date: 13 September 2026. Status: **REVIEWED, awaiting operator ratification on items
1, 2, 4, 5 and a go/no-go on the live action in item 6. Items 3's security fix and item 4's
"dormant" correction are findings, not choices, and stand regardless of ratification.**

---

## §0 Process

Run per `research/knowledge-home/structure-notes/brain-trust-on-demand-protocol.md`, the same real
process used for the 2026-09-13 SEO/GEO/five-tier charter review. Seven seats (Celestina, Jasiah,
Oluwole, Amaya, Omar, Bink, Sentinel), each investigating independently via the Agent tool, no
visibility into the others, each instructed to verify claims against the live repo
(`The-Reaver/My-Rivals-Distance-Archive`, HEAD `a5516a4`) and the live Supabase project directly
rather than trust the brief's paraphrase — every seat did exactly that, and several findings below
exist only because a seat caught the brief's own framing overstating or understating what's actually
built.

## §1 Item 1 — Reader Demand Score formula (P1-1)

**Verdict tally:** 5 SHIP WITH CONDITIONS (Celestina, Oluwole, Amaya, Bink, Sentinel), 1 HOLD
(Jasiah), Omar outside lane with a flag.

**Confirmed fact, not opinion (Jasiah, grepped):** zero computation writes to `demand_scores` beyond
a seed migration's placeholder zeros. Of the four candidate inputs, only `referrals.credited` and
`chronicle_requests` have any server-side validation (confirmed-email gate, unique constraint +
rate limit); `reads.completion_pct` and `shares` have **no** validation at all — both are bare
client-set inserts a reader's own account can spam freely.

**Converged design, if/when built:**
- Trend computed only over fraud-discounted inputs, never raw counts — a burst-fraud attack is
  *cheaper* against a naive trend derivative than against a raw total (Bink).
- `shares` gets near-zero weight (unverified click, no confirmed reach); `chronicle_requests` and
  `referrals.credited` weighted highest; `reads` only counted meaningfully once/if it gets
  server-side backing — until then, treat it like `shares` (Bink, Jasiah).
- A minimum-sample floor before any trend is computed/trusted, since this product's real per-character
  volume is far below the scale (Reddit/HN) the trend-weighting precedent comes from (Oluwole, Bink).
- A per-reader contribution cap per character, independent of per-input weighting, to blunt a
  multi-throwaway-account farming pattern (Bink).
- Exclude/downweight unconfirmed-email accounts explicitly in the formula spec (Celestina).
- Displayed to readers, if at all, as non-comparative and non-ranked — never a leaderboard or visible
  rank-against-others; a public "rising/falling" ranking signal is a FOMO mechanic that conflicts with
  the operator's standing neurodivergent-first requirement, the same finding Amaya made in the SEO/GEO
  review. A soft, single-character "readers have asked for this" note is fine; a ranked list is not.
- The aggregation must happen fully server-side (canon-service, which holds a service-role connection)
  with no intermediate per-reader join ever exposed via a `GRANT` to `anon`/`authenticated` (Sentinel).
- No scheduled-job/cron mechanism exists anywhere in the repo to actually recompute this periodically
  — an unscoped follow-on task once a formula is chosen, not a blocker to choosing one (Omar).

**Jasiah's dissent, recorded, not overridden:** given two of four inputs are currently wide open to
inflation, formalizing any formula today "bakes the gap in rather than fixing it." Bink's own
suggestion threads this: ship demand_scores as **display-only, feeding no automated drafting-priority
decision**, until the input-hardening above lands — matching this project's own already-ratified RICE
item from the SEO/GEO review ("gate any demand-driven drafting priority behind P0-4 fraud controls").

**Awaiting operator ratification:** the formula shape and weighting above, and whether it ships
display-only first per Bink/Jasiah's condition.

## §2 Item 2 — The Level 2 clearance-unlock rule

**Verdict tally:** Jasiah HOLD (nothing built, correctly routed as pure decision); the rest converge
on a synthesis below rather than picking either of the two originally-framed readings cleanly.

**Confirmed fact (Sentinel, verified against migration `0010`):** direct client self-promotion of
`clearance_level` is **already structurally impossible today** — table-level `UPDATE` on
`reader_profiles` was fully revoked when the follow-reconsideration feature closed the same class of
row-level-policy gap reactively. Whichever gate design ships must use a `SECURITY DEFINER` RPC
(matching `change_followed_character()`'s already-proven pattern), never a direct client `UPDATE` —
and must not "fix" some future unrelated column's missing grant by re-adding a table-wide `UPDATE`
grant, which would silently reopen this for `clearance_level` too. (Celestina's brief separately
described this as still-open; Sentinel's direct code citation is the more specific and verified
finding and controls here.)

**The real finding: neither original reading, as literally worded, is safe.**
- Bink: the OR-gate as stated ("read 3 fully, OR share once, OR request 2") is **not a real gate** —
  "share once" is a single unverified click with no rate limit, a complete standalone unlock path any
  script clears in under a second per throwaway account. This reading should not ship in any form.
- Bink: the 2-of-3 AND-gate is real progress but still has a hole as worded — "any two of three"
  admits `share + request` (the two cheapest actions) as a complete, valid pair, without ever
  requiring an actual read.
- Oluwole, independently: basic satisficing logic says a multi-path gate's real behavioral cost is
  the *minimum* of its paths — whichever design ships, the cheapest path (`request`, two clicks, no
  elapsed time, no verification) will dominate unless specifically hardened. Separately surfaces
  this project's own prior internal audit (`lords-of-cian-archive-game-plan.md`, P0-2) already
  recommending OR over AND pre-launch, reasoning that an AND-gate risks *nobody* reaching Level 2
  ("stalling"), which is a worse failure than being briefly too easy — a real, cited tension against
  Bink's finding, not resolved by either seat alone.

**Converged design (from Bink + Oluwole together, not either alone):** a completed read is a
**mandatory** component of the gate — "read, plus one of {share, request}" — not any two of three
interchangeably, and not a pure OR. This closes both flagged holes at once: the OR-gate's single-click
unlock, and the AND-gate's share+request-without-reading loophole. Request should count as the
stronger of the two optional companions (already rate-limited + unique-constrained); share as the
weaker, worth flagging even inside the hardened design (Bink).

**Also converged:** whichever gate design ships needs live, passive progress feedback ("2 of 3
toward next tier"), not a silent threshold that fires with no visible cause — Amaya's finding that an
invisible gate feels arbitrary regardless of its underlying logic, and that an AND-gate demanding
specific action *types* (rather than rewarding however a reader already engages) is an unnecessary
imposed-procedure tax worth avoiding if the hardened design can reward natural behavior instead.
Oluwole also recommends `access_method`-style provenance tagging (which path satisfied the gate) at
write time, cheap now, hard to retrofit, and the only way to later detect if Level 2 "stops meaning
anything."

**Real, unresolved tension flagged for the operator, not smoothed over:** the project's own prior
internal audit (P0-2) wanted a permissive OR specifically to avoid a stalling failure mode; this
review's fraud-conscious seats want read to be mandatory, which is stricter than pure OR. The
"read + one of {share, request}" synthesis is offered as a middle path that's harder to game than
pure OR while remaining meaningfully easier to reach than a strict 2-of-3, but it is a genuine
product call, not something the panel can rule past.

**Awaiting operator ratification:** the "read + one of {share, request}" gate design, or an
explicit override if the operator wants pure OR (with its known single-click hole) or strict 2-of-3
(with its known no-read hole) instead.

## §3 Item 3 — `quiz_questions` (P3-1)

**Verdict tally:** HOLD on building now (Amaya, Omar), unanimous zero-cost-to-defer (Celestina,
Jasiah, Bink), one real security bug found regardless of timing (Sentinel).

**Real, confirmed vulnerability in already-committed schema (Sentinel):** `quiz_questions_select`'s
RLS policy (`auth.role() = 'authenticated'`) grants the **entire row** — including `correct_index`,
the answer key — to any signed-in reader before they've answered, because Postgres RLS is row-level
only, not column-level. No UI exists yet so nothing is exploited today, but the schema as committed
is unsafe to build a client feature directly against: the moment any frontend does a plain `select`
against this table, the answer key ships in the response regardless of what the UI chooses to render.
`explanation` is exposed under the same policy and risks restating the answer.

**Fix, matching this project's own established pattern (Sentinel):** a `SECURITY DEFINER` grading RPC
(`submit_quiz_answer(question_id, selected_index)` returning `{is_correct, explanation}`, writing
`quiz_attempts` server-side) plus a public question-fetch view that omits `correct_index` entirely —
the same shape as `change_followed_character()` and the `chronicle_request_ledger` view this codebase
already uses twice.

**On timing:** confirmed zero UI, zero routes, zero references outside the schema file and two
passing comments (Jasiah, Bink independently). Amaya: don't stack a third unproven engagement
mechanic (after demand score and the clearance gate) before either of the first two has been watched
against real readers — sequencing risk, not a correctness one. Omar: zero live readers exist yet
regardless (Supabase still paused), so there's no traffic to validate the diagnostic's value against
today. Oluwole, on value if it ever ships: research on quiz engagement (BuzzFeed's own published
completion data) shows *identity/personality* quizzes drive sharing, not trivia-with-a-score — a
per-character trivia format as specced won't behave like a viral growth mechanic even if built
well, though it's a genuine, real utility for power readers navigating this project's now-enormous
canon depth (2,197 rules, ~1,122 Alias Chronicles) as a self-check, distinct from growth. Amaya
separately: "diagnostic, not a gate" must be enforced through UI framing too (reveal/flavor tone,
never a visible numeric score or pass/fail state), not just through the absence of a content gate.

**Awaiting operator ratification:** whether the quiz ships at all, and if so, on what timeline and
which framing (reader utility vs. growth mechanic — Oluwole's finding is that these need different
formats). **Not awaiting ratification:** the RLS fix, which should land whenever this table is first
touched by real application code, regardless of the build/defer/drop timing call.

## §4 Item 4 — Bulk Character Codex ingestion (P1-6) / AI-Parse

**Verdict tally:** HOLD on building the pipeline now (Celestina, Jasiah, Omar, converged), with
conditions attached for whenever it does ship (Oluwole, Sentinel).

**Correction to the operator's own framing (Celestina, Jasiah, Omar, independently converged):**
"dormant, no key set" overstates what exists. There is no paused pipeline — only `anthropic==1.0.0`
pinned as a dependency and one aspirational line in a module docstring claiming ownership of AI-Parse.
Zero lines of code anywhere instantiate a client, read a key, or define a route. This changes the
actual decision: it's not "flip a key on for a built system," it's "build the pipeline from zero" —
worth knowing before scoping effort against it.

**Cross-cutting correction, more significant, surfaced by Celestina and independently worth flagging
to whoever next touches the SEO/GEO charter:** that already-ratified 2026-09-13 review's §5/§8
repeatedly treats "the extraction step (P1-3)" as not-yet-built and bases a hard ratified constraint
on that premise. Direct inspection here found the extraction/ratification machinery — the
`knowledge_core` migration, `extraction.py`, `ratification.py`, `routes_knowledge_core.py`, full test
coverage, the `draft → under_review → ratified → locked` state machine — already exists and is
tested. This doesn't weaken that charter's ratified constraint (if anything the enforcement is
stronger than assumed, since it's real code, not a policy promise) — but the charter's own wording is
stale and should be corrected so a future session doesn't try to rebuild P1-3 from scratch. What's
actually still missing is only the upstream AI-Parse auto-population step (this item), which is a
narrower gap than the charter's text implies.

**Converged conditions for when this is built:**
- Anthropic API key as a Railway environment variable on canon-service, matching the existing
  `DATABASE_URL` pattern exactly — never Supabase Vault (a separate system canon-service would need
  to fetch over the network for zero benefit), never client-exposed (Omar, Sentinel).
- An explicit child-safety pre-screen step before extraction output is ever shown for review,
  matching this project's own zero-exception standing hard-stop rule — general extraction-pipeline
  practice already recommends upstream content-safety screening, and this project has already had to
  invoke that hard stop once for real (Oluwole).
- AI-Parse output must land as `kc_entries.status='draft'` through the existing
  `PostgresKnowledgeCoreRepository`, never a new, less-guarded write path into the same tables
  (Celestina) — feeding the same draft-then-human-approval gate this project has already run
  successfully 289 times (Oluwole).
- Before AI-Parse output ever reaches `body_markdown`: confirm `react-markdown` stays configured
  without raw-HTML passthrough for AI-generated content, or add explicit sanitization at the
  ingestion boundary. `Markdown.tsx`'s current comment ("never end-user input... the usual
  markdown-injection concerns don't apply") is true today and becomes false the moment this feature
  ships — nothing currently re-examines that premise (Sentinel, a genuinely new finding, not
  previously flagged anywhere in this project).
- Visually/structurally distinguish AI-parsed reference entries from hand-drafted Chronicles in the
  reader UI, so auto-extracted text isn't judged against hand-crafted narrative prose by the same bar
  (Amaya).

**Awaiting operator ratification:** none of this blocks anything else — it's a hold, not a live
decision needing a yes/no. Worth the operator's attention only to confirm the conditions above before
whoever eventually builds this starts.

## §5 Item 5 — Email provider for the Request Fulfillment Loop

**Verdict tally:** Oluwole HOLD, Omar SHIP WITH CONDITIONS — a real, evidence-based split, not
smoothed into a false consensus.

**Oluwole's case, with real external data:** current 2026 comparative testing shows Postmark leading
structured inbox-placement testing (83.3%) over Amazon SES (77.1%), with Resend leading on developer
experience specifically (first-class React Email support, a genuine fit for this Next.js/App-Router
stack — not picked arbitrarily). But Resend was suggested on DX grounds, and deliverability should
outweigh DX for this specific use case: these are trust/integrity-bearing transactional sends
(confirmation, fulfillment notices) where a message silently landing in spam breaks the same
referral-credit and demand-signal integrity model the rest of this review keeps returning to.
Separately, and this is the harder blocker: this project's own game plan records that email
confirmation is currently disabled system-wide, and P0-4's referral-crediting/demand-signal design
already requires confirmed email — choosing an ESP is premature ahead of that re-enablement decision,
and once made, the ESP choice should be evaluated against real, measured deliverability for the
project's actual expected volume, not decided in the abstract now.

**Omar's case:** Resend is operationally sound for the stated scope specifically (small reader base,
transactional-only, no marketing-blast use case) — comfortable free tier, official SDK with
first-class Next.js/Vercel examples matching this exact stack, standard reputation practice
(verified domain + DKIM/SPF) sufficient at this scale. Flags a real architectural entanglement: where
the send is actually triggered from (a Database Webhook/Edge Function vs. app-side send) determines
where the secret is provisioned, and that trigger-mechanism decision is itself blocked on item 6
(the project needs to be live to build a Database Webhook at all) — so the two decisions can't be
fully separated.

**Converged security conditions, regardless of which provider or timing wins (Sentinel):** API key
lives server-side only, never a `NEXT_PUBLIC_*` variable; reader email leaving Supabase's boundary to
a third-party subprocessor needs a plain disclosure line in the privacy policy/ToS naming the
provider and purpose; minimize payload (email + minimal templated content only, never bundling
referral graph/clearance level/reading history into the API call); any inbound delivery/bounce
webhook from the provider must verify the provider's signature before writing to `notifications` or
reader state, since an unverified inbound webhook is a spoofable write path. Amaya, separately: the
in-app `/notifications` path (already fully built) should always fire regardless of email outcome —
email is a supplementary channel, not the mechanism the "your story is ready" promise depends on.

**Awaiting operator ratification:** whether to re-enable confirmed email first and revisit the ESP
choice against real deliverability data (Oluwole's recommendation), or proceed with Resend now under
Sentinel's security conditions and Omar's operational read (Omar's recommendation). Both are live
options; this review did not converge on one.

## §6 Item 6 — When to unpause `lords-of-cian-archive`

**Verdict tally:** Omar SHIP (unpause now), Sentinel SHIP WITH CONDITIONS (unpause now, but correct
the verification sequencing) — the two in-lane seats converge tightly, both independently verified
against the live project rather than assumed.

**Confirmed live, not stale (both seats, separately):** the project (`dghkxaclaeluheahdsne`) is
`INACTIVE` right now. This account already runs one project `ACTIVE_HEALTHY` alongside four paused
ones — unpausing is a routine, already-practiced, reversible action for this operator, not a novel
or high-stakes one (Omar).

**A real flaw found in the operator's own planned verification sequence, reproduced directly, not
inferred (Sentinel):** the standing plan (this repo's own CLAUDE.md) was to run `get_advisors` before
deciding to unpause. Sentinel ran it against the paused project and got a clean, empty result — then
ran an actual SQL query (`list_tables`) against the same project and it failed outright ("Connection
terminated due to connection timeout"), proving the database is genuinely unreachable while paused.
The clean advisors result is not evidence of anything; it's an advisors service failing soft against
a database it can't actually inspect, not a confirmed zero-warning state. **The planned
check-before-unpausing sequence is not achievable as originally stated — advisors cannot meaningfully
run pre-unpause.**

**Grounded in direct migration review instead (Sentinel, all 15 files read):** every table across
both schemas has RLS enabled with explicit policies; `knowledge_core` additionally has both schemas
fully revoked from `anon`/`authenticated` on top of RLS. No table found with RLS enabled-but-no-
policies or RLS disabled outright. On that basis, unpausing itself is safe now — but a real advisors
run should happen **immediately after** unpause (when it can actually reach the database), not
before, and even then a clean advisors result isn't sufficient on its own: it would not have caught
item 3's `quiz_questions` answer-key leak, since that's a policy-scoping bug, not a missing-policy
gap advisors checks for.

**Confirmed by Celestina, independently, from the schema side:** across all 15 migrations reviewed,
no blocking schema/RLS defect exists that unpausing would expose — the open items from this whole
review (the demand-score formula, the clearance gate, AI-Parse) are formula/pipeline gaps, not
reasons the schema itself is unsafe to go live against.

**This is the one item in this review that is a live action on the operator's real external
infrastructure, not a design/spec decision** — it needs the operator's explicit go-ahead before
anyone actually restores the project, distinct from the other five items, which are specification
decisions with no external side effect until someone builds against them.

**Awaiting operator go/no-go:** restore the project now (both in-lane seats' converged
recommendation), then run `get_advisors` (security + performance) immediately after, followed by a
real Level 1 test-account spot-check per this repo's own standing P0-3 note — closing that
verification properly, in the correct order, for the first time.

## §7 Cross-cutting notes

- Multiple seats independently converged on the same underlying tension this whole review keeps
  surfacing: several of these six items (the demand-score formula, the clearance gate, the email
  provider) all draw on the same handful of raw signal tables (`chronicle_requests`, `reads`,
  `shares`, confirmed email), and this project's own prior internal audit already named the fix
  (P0-4 identity/fraud controls) without it having landed yet. Jasiah's framing: "this isn't six
  independent risks, it's one risk wearing six outfits."
- Two factual corrections to this project's own prior documentation surfaced along the way, both
  worth fixing at the source rather than just noting here: the "dormant AI-Parse pipeline" framing in
  the archive app's CLAUDE.md (§4 above), and the SEO/GEO charter's stale "extraction step not yet
  built" premise (§4 above).
- One genuinely new security finding with no prior flag anywhere in the project: the `Markdown.tsx`
  "never end-user input" trust assumption that AI-Parse (item 4) will invalidate the moment it ships
  (Sentinel).

## Links
- depends_on, [Knowledge Core] 2026-09-13-seo-geo-five-tier-charter-brain-trust-review.md, the P1-3
  staleness correction in §4 above concerns that document
- relates, [archive-app repo] CLAUDE.md, "Six decisions queued for the real Brain Trust, 2026-09-13"
  — the section this review resolves
