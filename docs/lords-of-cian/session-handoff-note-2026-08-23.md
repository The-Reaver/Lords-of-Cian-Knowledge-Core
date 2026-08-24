# Session Handoff Note — 2026-08-23

Written for the next session picking this up, since this session's context window has grown very large (21 canon-ledger batches plus a full archive-strategy review). Everything durable is saved to project docs; this note is the map to it.

## Current focus: the interactive archive app

The archive and the "studio app" are two separate apps. Focus is on the archive. The studio app is parked, not abandoned, revisit later.

**The authoritative plan is `lords-of-cian-archive-game-plan.md`** (dated 20 August 2026, "Reconciled final"), a fleet-reviewed strategy deliverable covering the real repository (`The-Reaver/My-Rivals-Distance-Archive`), a Lovable project already substantially built (React, TypeScript, Tailwind, shadcn/ui, Supabase, TanStack Router). Read this doc first before doing anything else archive-related. It contains a six-phase game plan (P0 through P3 backlog items), an engagement-feature roadmap, and a full adversarial-findings log.

**`archive-studio-tech-stack-decision.md` is superseded** for the archive by the doc above (it was a speculative proposal written before the real plan surfaced). Its stack guess held up in substance; its `spoiler_tier` idea is superseded by the real system's four-level clearance model and `published_books` unlock cascade. Kept for the record, not current direction.

### Two urgent flags from the real plan, unresolved

1. **The connected GitHub repo is empty.** Zero commits, zero branches, no `src/`, no `package.json`. Every "Complete" claim inside the Lovable workspace is unverified by anyone but Lovable's own agent. This is P0-1 in the game plan and blocks everything else.
2. **Possible live security exposure right now.** The archive is already reachable at a `lovable.app` URL. The source documents contradict themselves on whether Row Level Security is actually enabled, and email confirmation is disabled by design. If RLS is off, reader emails, engagement rows, and the referral graph may be readable by anyone with the link today, not at launch. This is P0-3/P0-4 in the game plan.

Next action was framed as a choice: P0-1 (push to GitHub) first since it blocks everything else, or the security audit in parallel if repo access exists some other way. Not yet answered when this session handed off.

### Connection worth carrying forward

P1-3 in the game plan (the missing tool that extracts Writer-Reference material into reader-facing content) is functionally what `canon-ledger.json` has been doing by hand all session: 510 locked, cross-checked, source-cited atomic facts pulled from Writer-Reference documents (Character Codex, Arsenal of Cian, Maw Codex, and more). Once P0-1 and P1-3 land, that ledger is a ready-made seed set for World Briefings and Archive Documents, not something to build from zero.

## Canon-ledger status (separate, parallel thread, not blocking the archive)

`canon-ledger.json` (synced as a project doc) sits at **version 2.4, 510 rules, 21 batches, zero duplicate IDs**, as of 2026-08-23. This session completed the full cult-network execution plan (five source dossiers plus three full-expansion-from-scratch cults: the Slab Compact, the Null Caucus, the Frequency Vigil) and the Ashkeel founding/governance batch (renamed from the uploaded "Guild of the Extraordinary" document under full creative autonomy).

Still queued, not urgent: the Domus Inviolate Dossier deep-read, the remaining Ashkeel batches (Seven High Arts, collar/legal hierarchy, geography and guilds, named characters), the 173-file Character Codex zip, the World Adaptation Blueprint, C-001 through C-023 Codex-text corrections, the Tier 4 Preparation Checklist cross-check, and three open items (OPEN-005, OPEN-007, OPEN-008).

**`master-to-do-list.md` is stale** (last updated 2026-08-13, predates all 21 batches). Treat `canon-ledger.json` as the live source of truth for canon status, not that file, until it gets a refresh pass.

## Standing convention, this session

Documents in this project read as authored by Abad, with no AI-attribution language. This was corrected retroactively in `canon-ledger.json` (12 fields that had said "Claude" were fixed) and applied going forward to every doc written since. Abad has not yet confirmed whether this is permanent standing practice or a one-time fix, worth a quick check if it comes up again.

## Anansi

Two candidate notes (not yet ratified) sit in `research/knowledge-home/candidates/2026-08-23/` on the operator's machine, covering the now-superseded tech-stack proposal and the archive/studio independence question. They predate the real game plan surfacing and may need a follow-up note once the real plan is reconciled against the 2026-08-04 independence ruling (does a shared Supabase data source between the archive and studio count as still-independent, still open).

## Where things are saved

- `claude/canon-ledger.json` — canon, 510 rules, 21 batches
- `claude/lords-of-cian-archive-game-plan.md` — the authoritative archive plan (read this first)
- `claude/archive-studio-tech-stack-decision.md` — superseded, kept for record
- `claude/master-to-do-list.md` — stale, canon-ledger.json supersedes it for canon status
- `claude/geographic-consistency-audit.md`, `claude/kanja-chronicles-production-roadmap.md`, `claude/anansi-closeout-2026-08-03.md` — untouched this session, unrelated threads
