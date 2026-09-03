# The archive app's "zero commits" and RLS-exposure flags from 2026-08-23 are stale as of 2026-09-03

- id: 2026-09-03-archive-app-zero-commits-and-rls-flags-are-stale
- type: finding
- status: candidate
- class: confirmed
- source: Lords-of-Cian-Knowledge-Core session, 2026-09-03, "Batch 49 and the Brain Trust gap"
- confidence: high -- verified by reading the actual repo and migration files, plus mcp__Supabase__list_projects
- verified: 2026-09-03
- tags: lords-of-cian, archive-app

## Body
`lords-of-cian-archive-game-plan.md` (reconciled 2026-08-23) carried two open flags: the connected
GitHub repo (`The-Reaver/My-Rivals-Distance-Archive`) had zero commits, and RLS/email-confirmation
status might be leaving reader data exposed on a live public URL. As of 2026-09-03: the repo now
has one real commit ("Scaffold Next.js + Python canon-service + Supabase Knowledge Core") with a
genuine Next.js App Router + Supabase build (a landing page, a character-index page querying
`demand_scores`). Its Supabase migrations (`0001_operational_schema.sql`, `0002_knowledge_core_schema.sql`)
implement comprehensive row-level security on every table, with the sensitive `knowledge_core`
schema fully revoked (not merely RLS-denied) from `anon`/`authenticated`, and
`reader_profiles.email_confirmed_at` synced from `auth.users` via trigger. This was NOT verified
against the live deployed project -- `mcp__Supabase__list_projects` shows the project
(`lords-of-cian-archive`, id `dghkxaclaeluheahdsne`) as currently paused/inactive, so nothing is
publicly reachable right now regardless of what the migration files say. `mcp__Supabase__get_advisors`
should be run once the project is unpaused before fully closing the RLS flag with live confidence.

Also found: the schema already contains most of the gamification/engagement primitives the
operator asked about for the "game of five" unlock system -- `reader_profiles.clearance_level`
(currently 0-3, four tiers, not yet five), `chronicle_requests` (readers requesting/voting on
which character's story develops next), a public `demand_scores` leaderboard, `reads`
(completion-percent tracking), `shares`, `referrals` with referral codes, `quiz_attempts`. This is
further along than the CLAUDE.md status implied and should ground any future planning rather than
starting from a blank-slate assumption.

## Links
- none
