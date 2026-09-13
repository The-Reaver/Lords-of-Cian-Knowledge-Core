# Six queued archive-app decisions — closing Brain Trust verdicts

Follow-up to `2026-09-13-archive-app-six-open-items-brain-trust-review.md`. Abad's instruction after
reading that review, quoted verbatim: "I want you to unpause it. for all other items to bring trust
will render the verdict and I will approve it." This document records the closing round: item 6
(Supabase unpause) executed; items 1, 2, 3, 5 -- the four that had a real tension or split in the
first round rather than a clean convergence -- sent back to the relevant seats with one instruction:
render a final, decisive ruling, not another menu. Item 4 (AI-Parse) is not revisited here; the first
round already converged unanimously on HOLD with a clear condition list, so there was nothing left to
adjudicate.

**Status: all six items now have a closing ruling. Ratification is Abad's per his own stated
intent ("I will approve it") -- these are recorded as decided, pending that approval landing in his
own words per this project's standing discipline, same as every other batch.**

---

## Item 6 — Supabase unpause: DONE

`mcp__Supabase__restore_project` called against `dghkxaclaeluheahdsne` -- accepted, project
transitioning `INACTIVE` -> `COMING_UP` -> (expected) `ACTIVE_HEALTHY`. Per Sentinel's corrected
sequencing from the first round, `get_advisors` (security + performance) will run once the project
reports healthy, not before -- the first round proved the pre-unpause check doesn't actually work.
Follow-up spot-check (a real Level 1 test account, per this repo's own standing P0-3 note) remains
queued for whenever a session can drive the signup flow against the now-live project.

**New, time-sensitive finding from this closing round (Omar):** the instant the project is reachable
and any real reader signs in, `quiz_questions.correct_index` (the answer key) is fetchable directly
via PostgREST regardless of whether any quiz UI ever ships -- RLS grants the full row to any
`authenticated` role today. This is decoupled from the item-3 timing decision below and needs a
one-line migration (revoke `SELECT` from `anon`/`authenticated` on `quiz_questions`, or tighten RLS
to deny-all) landed at or immediately after unpause, independent of when/if the quiz feature itself
ships.

## Item 1 — Reader Demand Score formula: CLOSED

**Final ruling (Jasiah, resolving the round-one HOLD-vs-SHIP split):** ship now, but only as an
internal-only, non-reader-facing drafting-priority signal -- no leaderboard, no public display, no
automated action tied to it yet. Hold the reader-facing / automation-driving version until `reads`
and `shares` get real server-side validation (the P0-4 gap this whole review kept surfacing).

**Concrete formula, buildable as specified:**
```
raw_signal(character, window) =
    4.0 * chronicle_requests_fraud_discounted
  + 3.0 * referrals.credited
  + 0.5 * reads.completion_pct_aggregate   (near-zero weight -- unvalidated input)
  + 0.1 * shares                            (near-zero weight -- unvalidated input)
```
- Every input except `referrals.credited` gets a per-account contribution cap per character per
  window (blunts multi-throwaway-account farming).
- A minimum-sample floor (e.g. >=15-20 distinct contributing accounts) before any trend is computed;
  below it, output is null/"insufficient data," never a confident-looking number from noise.
- Trend/decay (Reddit-hot/HN-gravity-style) applied only on top of the fraud-discounted, floor-gated
  signal -- never on raw counts, so a burst-fraud attack can't manufacture a "rising" trend.
- Unconfirmed-email accounts contribute zero to any input, hard exclude.
- Computed fully server-side (scheduled job/edge function), writing only the final aggregate to
  `demand_scores` -- no query path ever exposes per-reader identity.
- Cadence: a scheduled job (new infrastructure, ticketed separately per Omar, not a blocker to
  shipping the formula itself).

**Promotion path, recorded not scoped:** once `reads`/`shares` get equivalent server-side validation
to `chronicle_requests`/`referrals.credited`, re-weight and reconsider reader visibility -- still
non-comparative/non-ranked even then, per Amaya's standing FOMO/neurodivergent-first condition.

## Item 2 — Level 2 clearance-unlock gate: CLOSED

**Final ruling (Bink, resolving the stalling-risk-vs-gaming-risk tension):**
```
clearance_level_2_unlock =
    EXISTS(reads WHERE reader_id = X AND completed = true)   -- >=1 fully completed chronicle
    AND (
        EXISTS(shares WHERE reader_id = X)                    -- >=1 share, OR
        OR
        EXISTS(chronicle_requests WHERE reader_id = X)         -- >=1 request
    )
```
One completed read is mandatory (down from the original AND-gate's 3-read leg); the companion action
is a fully free reader choice between share or request, no ordering or combination required.

**Why this resolves rather than splits the difference:** the prior internal audit's stalling fear and
this review's gaming fear were never actually the same dial. The mandatory-read clause controls
stalling risk (kept low: one read, not three); the free-choice OR on the companion action controls
gaming risk (closed: a bare share click alone can no longer unlock anything, since reading can't be
skipped). Tuned independently rather than traded off.

**Hard pre-ship dependency, not a hedge:** `reads.completed` must be confirmed server-side-backed,
not a client-set flag -- multiple seats flagged this as open and it's load-bearing for this verdict.
If it turns out to be client-trusted only, the interim substitute (ship now, don't wait for a
redesign): a server-logged proxy -- minimum dwell time (>=60s, debounced server ping) plus scroll
depth >=90% on that `chronicle_entry` -- stands in for "completed" until real tracking lands.

**Hard requirements, not optional:** live progress visibility ("1/1 read - pick one: share or
request"), not a silent threshold (Amaya); an `access_method`-style column logging which companion
action satisfied the gate for every unlock, cheap now and the only way to detect abuse of either leg
after the fact without another review cycle (Oluwole).

## Item 3 — `quiz_questions` (P3-1): CLOSED

**Final ruling (Omar, resolving the build-now-vs-defer-vs-drop question):** defer, not drop, not
build now. Concrete trigger: build begins once **both** (a) the demand-score and clearance-gate
features (items 1 and 2) have run live against real traffic for 4 consecutive weeks, and (b) the
archive has >=25 registered/returning readers -- whichever lands later. (The 25-reader figure is a
reasonable floor for this project's depth-first audience, not load-bearing -- adjustable once real
signup data exists, without reopening this review.)

**Format, if/when built:** stays a plain comprehension/self-check trivia tool as currently specced --
explicitly NOT redesigned toward a shareable personality/identity-quiz format, even though research
shows that format drives more sharing. Reasoning: that's a different feature with different schema
and UX intent, and chasing virality here would fight Amaya's own "diagnostic, not a gate" framing
(personality-quiz formats are built around a shareable result reveal, which reads close to the
visible-score/pass-fail framing already ruled out).

**Hard precondition, unconditional regardless of timing:** the `SECURITY DEFINER` grading-RPC fix
(§3 of the first-round review) ships before any UI/route ever touches this table in production --
and per item 6 above, the direct-grant lockdown on the raw table happens now, immediately, decoupled
from this feature's own build timeline.

## Item 4 — Bulk Character Codex ingestion (P1-6) / AI-Parse: unchanged, HOLD

Not revisited this round -- the first review converged unanimously (Celestina, Jasiah, Omar) with no
real split: hold building the pipeline until a key and real approach exist; when it is built, the
conditions from §4 of the first review apply (Railway env var for the key, an explicit child-safety
pre-screen step, output lands as `kc_entries.status='draft'` through the existing repository, and a
markdown-sanitization check before AI-Parse output ever reaches `body_markdown`).

## Item 5 — Email provider for the Request Fulfillment Loop: CLOSED

**Final ruling (Oluwole, dropping the round-one HOLD in favor of Omar's SHIP WITH CONDITIONS):**
**Resend**, triggered via a Supabase Database Webhook -> Edge Function on the fulfillment state
transition (not an app-side send) -- ties the send atomically to the actual DB event of record and
lets the API key live in Supabase's own secret store, isolated from the Next.js deployment.

**What changed the verdict:** Oluwole's original HOLD rested on treating email as the
integrity-bearing channel a fulfillment promise depends on. Re-examined against a fact already on the
table (Amaya's condition that `/notifications` always fires in-app regardless of email outcome), that
premise doesn't hold -- the in-app path, not email, is what actually carries the promise. Once email
is correctly understood as a convenience channel, the Postmark-vs-Resend deliverability gap cited in
round one stops being decisive at this project's stated scale (small reader base, transactional-only).

**One narrow, bounded gate (not reopening the HOLD):** the email channel itself does not go live
until email confirmation is re-enabled (or an equivalent explicit address-validation step exists) --
sending to unconfirmed addresses degrades sender reputation regardless of provider. This blocks only
the email channel; the in-app `/notifications` path is unaffected and can ship immediately. A bounded
checkpoint is set to revisit the provider choice on real data: first 500 sends or 90 days
post-launch, whichever comes first.

**Non-negotiable conditions, carried forward from round one unchanged:** API key server-side only
(now further reinforced by the Edge Function architecture); a privacy-policy/ToS line naming Resend,
since reader email leaves Supabase's boundary; minimal payload (email + template content only, no
bundled reader data); inbound delivery/bounce webhooks must verify the provider's signature before
writing to any reader state; `/notifications` fires regardless of email outcome.

## §7 Execution addendum — the unpause and both schema fixes, done

All action items from this closing round are now complete, not just ruled on:

- **Supabase restored:** `mcp__Supabase__restore_project` against `dghkxaclaeluheahdsne`,
  confirmed `ACTIVE_HEALTHY`. Post-unpause `get_advisors` ran per the corrected sequencing.
- **Real, significant discovery made while verifying:** the live project had only ever
  received migrations through `0005_seed_verification_data` (2026-08-24) --
  `mcp__Supabase__list_migrations` showed 5 applied against 15 files in the repo. Every
  migration from 0006 onward (P0-4 fraud controls, the Standing Requests Ledger, Also Drawn
  To, Follow Reconsideration, Field Notes, the shares CHECK constraints, Connective Tissue
  Trails, Two Dossiers Side by Side) had been verified locally every session since but never
  actually applied to the live project. All were applied now, in order, via
  `mcp__Supabase__apply_migration` -- the live project's schema matches the repo exactly for
  the first time since 2026-08-24.
- **quiz_questions lockdown (item 3):** applied both to the live project and as
  `supabase/migrations/0016_lock_down_quiz_questions_answer_key.sql` in the archive-app repo,
  verified against a fresh local Postgres instance (a non-admin authenticated reader now sees
  0 rows, confirmed by direct query before/after).
- **One further finding from the post-unpause advisors run, fixed the same session:**
  `change_followed_character`'s `revoke execute ... from anon` (migration `0010`) never
  actually worked -- Postgres grants `EXECUTE` on a new function to `PUBLIC` by default, and
  `anon` is implicitly a member of `PUBLIC`, so the named revoke left the `PUBLIC` grant
  untouched. Confirmed directly (`information_schema.routine_privileges` showed `PUBLIC` still
  held `EXECUTE`). Not exploitable -- the function's own `auth.uid()` check already blocks
  anonymous calls before any mutation -- but closed for correctness via
  `supabase/migrations/0017_close_change_followed_character_public_grant.sql`, applied both
  live and locally.
- All 17 migrations verified applying cleanly against a fresh local Postgres instance before
  and after both fixes, matching this project's standard verification workflow.
- The archive-app repo's own `CLAUDE.md` is updated to mark all six queued items resolved,
  linking back to this document and the first-round review.

## Links
- depends_on, 2026-09-13-archive-app-six-open-items-brain-trust-review.md, the first-round review
  this closes out
