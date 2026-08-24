# Interactive Archive App and Studio App — Tech Stack and Build Timing

By Abad Morel. Written 2026-08-23, settling the tech stack and build timing for the interactive archive app and its companion studio app so it survives session loss.

**Superseded for the archive app, 2026-08-23 (same day):** the archive and the studio are two separate apps, focus is on the archive. The full reconciled Game Plan for the archive (`lords-of-cian-archive-game-plan.md`, dated 20 August 2026) is the authoritative plan going forward, built against the real repository (`The-Reaver/My-Rivals-Distance-Archive`) rather than the speculative proposal below. This doc's speculative stack notes hold up (React, TypeScript, Tailwind, Supabase, confirmed by the real System Explanation, with the router corrected to TanStack Router, not Next.js) and the `spoiler_tier` idea below is superseded by the real system's more developed four-level clearance model plus per-item book placement and the `published_books` unlock cascade. Kept below for the record, not as current direction.

## What already exists

A Lords of Cian archive already exists as a Lovable project: `cian-archive-tales`, project ID `36d6dae2-3c41-496b-aaa2-0bfc98fbfb05`, workspace `ipyUKp7cIHPv0JiUyvBe` ("Morel's Lovable"), located 2026-08-04. Lovable's stack is React, TypeScript, Tailwind CSS, and shadcn/ui on the frontend, with Supabase (Postgres, Auth, Storage, Edge Functions) as the backend.

A separate STAG Production Studio system also exists. Ratified 2026-08-04: the archive and the Production Studio stay fully independent for now, with wiring them together left as a future decision.

## Tech stack

Build both the interactive archive app and the studio app on the same stack already proven in `cian-archive-tales`: React, TypeScript, Tailwind, shadcn/ui, Supabase. Extend the existing Lovable project for the reader-facing archive rather than starting a new one.

Add a `spoiler_tier` field to every canon entry synced from `canon-ledger.json` into a Supabase Postgres table (tier 0 for pre-Book-1 world lore with no plot content, higher tiers for each book's reveals), and enforce the gating with Postgres Row-Level Security policies, not just UI hiding, so a reader cannot bypass it through browser developer tools.

The studio app is a private, authenticated admin frontend, on the same stack, that reads and writes the same Supabase tables. It is where canon-ledger batches get imported, tagged with a spoiler tier, and flipped to published. This gives the archive and the studio one shared data source without merging their user-facing codebases.

## Open question

Does sharing one Supabase data source between the archive and the studio reverse the 2026-08-04 independence ruling? A shared datastore with no shared codebase or UI sits in between "fully independent" and "wired together." Needs settling before the studio app's data layer is built, since retrofitting a shared schema onto two separately-provisioned Supabase projects later is real rework, while designing for it up front is not.

## On timing

The canon-ledger holds 510 locked rules as of 2026-08-23, across 21 batches, all world-building (geography, factions, cultures, the full cult network, Ashkeel's founding layer), with the plot-spoiler line (Book 1's opening murder scene onward) still ahead of anything drafted. Direction: start building the schema and the canon-ledger-to-Supabase sync pipeline now, and begin populating tier-0 content from what is already locked immediately, rather than waiting for every remaining pre-Book-1 world-building batch (Domus Inviolate, remaining Ashkeel batches, the Character Codex) to finish first. Those batches feed the pipeline incrementally once it exists.

## Status

Stack choice set. The shared-data-source question above still needs a final ruling.
