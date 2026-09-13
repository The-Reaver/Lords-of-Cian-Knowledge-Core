# Proposed tech stack for the Lords of Cian interactive archive app and its companion studio app: extend the existing cian-archive-tales Lovable project rather than starting a new stack

**SUPERSEDED same day, 2026-08-23** by 2026-08-23-lords-of-cian-archive-tech-stack-superseded-by-real-game-plan.md, once a real archive game plan surfaced. Kept as historical record, not current direction.


- id: 2026-08-23-lords-of-cian-archive-and-studio-tech-stack-proposal
- type: spec
- status: rejected
- rejected: 2026-08-25 — anansi-promote skill run, 3/10 (novelty 0, evidence 1, actionability 0, generality 0, non-contradiction 2). Self-superseded the same day by its own header, and the real reconciled game plan replaced it. Its invented spoiler_tier field is superseded by the real four-level reader-clearance model. Retained in place as historical record of how the real plan was reached, per the no-deletion rule.
- author: Abad Morel
- source: settled 2026-08-23, tech stack and build timing for the interactive archive app and studio app, captured so it is not lost
- tags: lords-of-cian, lovable, archive, studio, tech-stack, spoiler-gating, canon-ledger
- project: lords-of-cian

## Body

The interactive archive for the Lords of Cian world is populated from canon locked in `canon-ledger.json` (510 rules across 21 batches as of 2026-08-23), with all Book-1-plot spoilers hidden. This note settles the stack for that archive and for a companion "studio app," and when coding starts.

This is not a greenfield decision. A Lords of Cian archive already exists as a Lovable project, `cian-archive-tales` (project ID `36d6dae2-3c41-496b-aaa2-0bfc98fbfb05`, workspace `ipyUKp7cIHPv0JiUyvBe`, "Morel's Lovable"), found on 2026-08-04 (see linked note). Lovable's stack is React, TypeScript, Tailwind CSS, and shadcn/ui on the frontend, with Supabase (Postgres, Auth, Storage, Edge Functions) as the backend. A separate STAG Production Studio system also exists, ratified on 2026-08-04 to stay fully independent from the archive for now, with wiring them together left as a future decision.

Direction:

Build both the interactive archive and the studio app on the same stack already proven in `cian-archive-tales` (React, TypeScript, Tailwind, shadcn/ui, Supabase), rather than introducing a third stack. Extend the existing Lovable project for the reader-facing archive instead of starting a new one.

Add a `spoiler_tier` field to every canon entry synced from `canon-ledger.json` into a Supabase Postgres table (tier 0 for pre-Book-1 world lore with no plot content, higher tiers for each book's reveals), and enforce the gating with Postgres Row-Level Security policies, not just UI hiding, so a reader cannot bypass it through browser tools.

The studio app is a private, authenticated admin frontend, on the same stack, that reads and writes the same Supabase tables. It is where canon-ledger batches get imported, tagged with a spoiler tier, and flipped to published. This gives the archive and the studio one shared data source without merging their user-facing codebases, which may or may not satisfy the spirit of the 2026-08-04 independence ruling. Flagged as an open question in the linked note rather than assumed.

On timing: the canon-ledger already holds 510 locked rules, all world-building (geography, factions, cultures, the cult network, Ashkeel's founding layer), with the plot-spoiler line (Book 1's opening murder scene onward) still ahead of anything drafted. Direction: start building the schema and the canon-ledger-to-Supabase sync pipeline now, and begin populating tier-0 content from what is already locked immediately, rather than waiting for every pre-Book-1 world-building batch (Domus Inviolate, remaining Ashkeel batches, the Character Codex) to finish first. Those batches feed the pipeline incrementally once it exists.

## Links

- derived-from: 2026-08-04-lords-of-cian-lovable-archive-located
- derived-from: 2026-08-04-lovable-archive-production-studio-independence-ratified
- relates: 2026-08-23-archive-studio-independence-open-question (the fork this proposal raises but does not resolve)
