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
   **1,198 live Chronicle and Annals entries across 24 characters** — all 11 of Kanja's Alias
   arcs (1,122 entries) plus all 22 territory-leader characters (76 entries, 20 homage territories
   + Arturo + the Xaragua/Kazi character splits) — straight from the Knowledge Core repo's
   `docs/lords-of-cian/chronicles/` directory. A sibling script then populated **12 World
   Briefings** from the remaining ~515 non-Chronicle canon-ledger rules (GEO/ARS/MAW/ASH/CULT/POL/
   WC/HLD/WGD/SBD/CHAR/COS), one briefing per rule-prefix. Phase 3's old "content-readiness gate" —
   "enough material live that a Level 1 reader can plausibly read three to 90%" — isn't a future
   milestone, it's already true by a wide margin.
   Not yet imported: the character Series tracks (Lauris, Ozmund, Daba, Ezio — roughly 290
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

## Readiness and the first upload, 2026-10-07

Added after Batch 379 (ledger 38.1, 2,729 rules, 379 batches). Writing continues in the Knowledge
Core; this section only tracks what the archive will take from it.

### Is there enough material? Yes.

| Series | Locked entries | Book 1 unlock tier (`VB-069`) |
|---|---|---|
| Kanja: Alias Chronicles (11 aliases x 102) | 1,122 | 172 |
| Kanja: the Kanja-version track | 7 | 7 |
| Kanja: manuscript Chronicles I-VIII | 8 | 8 |
| Ozmund: the Testaments | 121 | 0 |
| Lauris: the Records | 110 | 0 |
| Daba: the Rolls | 59 | 0 |
| Territory Annals (20 territories, plus Arturo) | 76 | 0 |
| Anirak: the Collections | 3 | 0 |
| Ezio: the Exhibits | 1 (3 more drafted, not locked) | 0 |

About 1,507 locked entries and 1.1 million words. All 188 gated entries are Kanja's (172 alias
entries showing the Trinity in use, plus the whole Kanja-version track and the manuscript, and the
one undecidable entry, `MCD-729`, which counts among the 172).

### Proposed upload plan (Abad, 2026-10-07; under discussion, not final)

- **Kanja, Lauris and Ozmund: every entry uploaded.** For Kanja that means 949 open at launch and
  188 uploaded into the vault, locked until Book 1 is published (`VB-069`).
- **Everyone else, including Daba's 1804: five entries each at launch.** Abad, 2026-10-07: "Every
  other entry for 1808 will have five entries" ("1808" read as 1804, to be confirmed).
- **Then release by demand.** Readers' requests show which characters and which parts of the world
  they want. The rest of the already-written backlog is released in answer to those requests. Abad:
  "I will upload those as if they are waiting for something to be written and they request it and
  then I upload it but I've already written it". This runs on the Standing Requests Ledger and the
  Request Fulfillment Loop the archive already ships (engagement ideas 1 and 2).
- **Writing needed to reach five:** 17 territories hold three Annals each (+34). Anirak holds three
  Collections (+2). Ezio holds one locked Exhibit with three drafted (+1 if the drafts are approved).
  Xaragua's six are Ogoun Xarey's one and Arturo's five (+4 if counted per leader). Kazi (13) and
  Sankofa (6) already have five or more. Daba has 59.

### What the live archive needs before that upload

1. **The live database already holds the 188 gated entries.** The 2026-09-14 import loaded all
   1,122 alias entries, before `VB-069` existed. They must be hidden or vaulted before the site is
   unpaused for readers.
2. **The live copies are stale.** They predate Batches 320-379: the fable-review corrections, the
   Batch 375 series renames, and the Batch 378 timeline. Every uploaded entry is re-imported from
   the current files, not patched.
3. **The importer needs a release flag per entry** (open, vault, or not released), driven by the
   manifest and the upload plan, so the selection is data and can change without code.
4. **Approval-list items that touch released entries should be ruled first,** or the
   contradiction goes public. Highest stakes: item 2 (Garren Hask dies at 50-55 on the Captain
   track but lives to 313 on the Scourge and Lauris tracks), item 31 (three Lauris Records that
   cannot be set before Book 1), item 21 ("the Karkosa" as the crew's ship in the Records), item 39
   (Lauris Record VIII against `MCD-193`), and item 38 (Sephtis's staged death against his open
   place in the crew).

### How much more pre-Book-1 material can be written

The story room is large; review bandwidth is the real limit. Open ground, roughly in order of value:

- **Tier 1 launches never started:** Fermand, Valen, Sephtis, Anansi and Orlok have no series. Pyro
  and the Triad gates are in progress. Ezio has three drafts awaiting review. A Red Beard series
  would also unblock villain defeats already locked as rules (`MCD-1859`, `MCD-1862`).
- **Account types barely used:** Comrade Accounts, Adversary Accounts, Dossiers and Hearsay
  (`VB-067`, `VB-068`) are new formats. They are also the main way to tell the Trinity's
  Rebellion legend in the open archive without breaking `VB-069`.
- **Kanja's Long Mask (ages 30-313)** is open-eligible, since the Trinity is sealed. New
  Kanja-version entries are always vault-only.
- **Near saturation:** the Alias tracks (102 each) and Ozmund's pre-Ceremony window (121) show
  repetition risk. Abad's standing pacing rule already says to hold the Alias waves until the
  archive is loaded.

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
