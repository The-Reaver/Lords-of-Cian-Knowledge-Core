# Lords of Cian Interactive Archive — Roadmap, 2026-10-02

By Abad Morel. Supersedes the Aug-20 game plan (`lords-of-cian-archive-game-plan.md`) as the
operative status reference — that document is kept for its reasoning (the demand-signal design,
the engagement-idea rationale), but its "ground truth" section describes a repo that no longer
exists in that state. This doc is built from a direct, same-session inspection of all three real
systems (the GitHub repo, the live Railway deployment, the live Supabase project), not from prior
docs' claims about them.

## The headline: it's live, not scaffolded

The archive is a working, deployed, populated product today, not a backlog. In order of surprise:

1. **Content population already ran at full scale.** `bulk_import_knowledge_core.py` imported
   **1,198 live Chronicle entries across 24 characters** — all 11 of Kanja's Alias arcs (1,122
   entries) plus all 22 territory-leader characters (76 entries, 20 homage territories + Arturo +
   the Xaragua/Kazi character splits) — straight from the Knowledge Core repo's
   `docs/lords-of-cian/chronicles/` directory. A sibling script then populated **12 World
   Briefings** from the remaining ~515 non-Chronicle canon-ledger rules (GEO/ARS/MAW/ASH/CULT/POL/
   WC/HLD/WGD/SBD/CHAR/COS), one briefing per rule-prefix. Phase 3's old "content-readiness gate" —
   "enough material live that a Level 1 reader can plausibly read three to 90%" — isn't a future
   milestone, it's already true by a wide margin.
   Not yet imported: the Character Chronicle tracks (Lauris, Ozmund, Daba, Ezio — roughly 290
   entries as of Batch 350) and the Kanja-version track. A second bulk-import pass is needed before
   "fully loaded" is literally true.
2. **It's deployed and running.** Railway project `lords-of-cian-archive` has both services
   (`web`, `canon-service`) live, latest deployment `SUCCESS`, matching the repo's current HEAD
   (`05dd3b7`, 2026-09-14). Reachable today at `web-production-8be0b.up.railway.app`. No custom
   domain is connected yet — that's the one real gap in "deployed."
3. **The database schema, RLS, and fraud controls are built and verified**, not just designed —
   17 migrations, RLS on all 18 tables across both schemas, the identity-fraud mechanics from
   P0-4, and all nine of the Aug-20 engagement ideas (§3 1-9: Standing Requests Ledger, Request
   Fulfillment Loop, Field Notes, Also Drawn To, Referral Lineage groundwork, Correspondence
   Checkpoints groundwork, Follow Reconsideration, Connective Tissue Trails, Two Dossiers Side by
   Side) are shipped in code.
4. **The six items flagged for "the real Brain Trust"** (demand-score formula, the Level 2 unlock
   rule, the quiz_questions timing, bulk-ingestion go/no-go, the email provider, the unpause
   timing) all have closing verdicts, resolved 2026-09-13 — see the Knowledge Core repo's
   `2026-09-13-archive-app-six-open-items-final-verdicts.md`. The Level 2 gate those verdicts
   specified (`1 completed read AND (1 share OR 1 request)`, with server-side-verified `completed`)
   is built: `f22b675`.

## What's actually still open, in order

### 1. The Supabase project is paused again — immediate, operational
Checked live just now: `lords-of-cian-archive` (`dghkxaclaeluheahdsne`) status is **INACTIVE**.
It was confirmed `ACTIVE_HEALTHY` after the 2026-09-13 unpause, so this is Supabase's own
free-tier auto-pause after a stretch of no traffic, not a regression. Since `web`'s every
data-driven page depends on it, **the live Railway URL is almost certainly serving broken pages
right now.** This is the first thing to fix, and it's cheap: `mcp__Supabase__restore_project`,
then re-run `get_advisors` once (not a new finding — the auto-pause itself is the event, not a
code change) to confirm nothing drifted.

### 2. Connect a custom domain
Railway shows only the auto-generated `*.up.railway.app` domain, no custom domain. This is the
one genuinely unstarted piece of the original P1-7 ("deploy to production, connect the custom
domain") — deployment happened, the domain connection didn't. Low effort (`generate-domain` /
`update-domain` on Railway once a domain name is chosen), but it's the thing standing between
"live" and "the 6-month demand-collection milestone actually starts counting," since Strategy
§8's success metrics assume a real, shareable, indexable address.

### 3. Re-verify after the pause/unpause cycle
Worth a fresh `get_advisors` security pass and one real signed-in-test-account walk of the four
clearance transitions once the project is back up — not because anything is suspected broken,
but because every prior "verified against the live project" claim in the repo's CLAUDE.md
predates at least one full pause/restore cycle, and that's exactly the kind of state transition
worth confirming rather than assuming survived cleanly.

### 4. Genuinely deferred, by explicit prior decision — not oversights
- **Bulk Character Codex ingestion (P1-6):** unanimous Brain Trust HOLD. No dormant AI-parse
  pipeline exists (the Anthropic SDK dependency is pinned but zero code calls it) — this is
  "build from zero," conditioned on specific triggers already recorded in the first-round Brain
  Trust doc. Separately, the Chronicle/World-Briefing bulk imports that already ran used a
  *different*, simpler path (concatenation from the already-structured canon ledger, not AI
  extraction from raw prose) — that path is done; P1-6's own AI-parse path is the part still on
  hold.
- **`quiz_questions` (P3-1):** deferred behind a concrete trigger (Ideas 1 & 2 live 4+ weeks AND
  ≥25 registered readers) — a real answer-key RLS leak in it was already found and fixed
  (`0016`) independent of the timing decision, so the table itself is safe sitting idle.
- **Email delivery for the Request Fulfillment Loop:** provider decided (Resend, via a Supabase
  Database Webhook → Edge Function), but gated on re-enabling email confirmation — which is
  itself gated on a signup-architecture decision outside any single session's authority (GoTrue's
  frictionless-signup call vs. the demand-signal integrity P0-4 was built to protect). Until that
  lands, the in-app half of the loop (the `/notifications` page, the trigger) works; the email
  half doesn't fire.
- **Referral-pair fraud signals** (`signup_ip_hash`/`signup_ip_hash_match`): stay unpopulated
  because Supabase Auth's signup call goes straight from the browser to GoTrue, bypassing this
  app's own server — populating them needs a custom signup Route Handler, a real architecture
  change, not a migration. Not attempted, correctly not silently skipped either (flagged plainly
  in the repo's own CLAUDE.md).

### 5. The standing SEO/GEO/five-tier charter — not yet ratified
Separate from everything above: the proposed SEO/GEO/gamified-five-tier-unlock charter still needs a Brain Trust review before its concrete schema/tagging decisions can be adopted as
*ratified* rather than draft. Per CLAUDE.md (resolved 2026-09-12), no device bridge is needed: any
session can run the protocol from `structure-notes/brain-trust-on-demand-protocol.md` in this repo. Nothing
built so far depends on this landing first — it only gates that one specific charter.

### 6. Operate the demand engine (Phase 4 from the original plan — open-ended, not a task)
Once the domain is live and traffic exists, the steady-state loop from the original plan still
applies as written: read the Demand panel by trend direction, check clearance distribution,
check referral chain depth, check the anomaly flag. Nothing here changes — it just hasn't started
yet because there's been no real traffic to read.

## Recommended order

1. Unpause Supabase (`restore_project`), confirm `get_advisors` clean, spot-check the live site
   actually renders character/chronicle/world pages correctly post-restore. **Minutes, not hours.**
2. Pick and connect a custom domain on Railway's `web` service.
3. Decide whether to revisit the email-confirmation architecture now (unlocks the Fulfillment
   Loop's email half and the referral-fraud signals together) or defer it — this is the one
   item above that's a real product decision, not a mechanical step.
4. Let the site run and start actually collecting demand data — Phase 4 is the natural next
   state once 1-2 land, not a separate project.
5. Revisit P1-6 (bulk AI-parse ingestion) and `quiz_questions` only when their own
   already-recorded trigger conditions are met.
6. Run the Brain Trust review for the SEO/GEO/five-tier charter from this repo whenever convenient —
   not urgent, nothing else is waiting on it.

## What this doc deliberately does not re-litigate

The Aug-20 game plan's actual design reasoning — why the demand score is shaped the way it is,
why each of the nine engagement ideas earns its place, the adversarial-review corrections — is
still the right reference for *why* the system works the way it does. This doc only replaces its
*ground-truth* section, which has been overtaken by two full sessions of real, verified build
work the Aug-20 doc couldn't have known about.
