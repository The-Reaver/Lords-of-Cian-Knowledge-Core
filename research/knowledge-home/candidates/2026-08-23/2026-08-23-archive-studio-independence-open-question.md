# Open question: does sharing one Supabase data source between the archive app and the studio app reverse the 2026-08-04 ruling that the two stay fully independent

- id: 2026-08-23-archive-studio-independence-open-question
- type: question
- status: rejected
- rejected: 2026-08-25 — anansi-promote skill run, 4/10 (novelty 1, evidence 1, actionability 0, generality 0, non-contradiction 2). Premise invalidated the same day it was raised: the superseding note records the operator correcting the assumption this question was framed around (archive and studio are two different applications, not one system with two frontends), and explicitly sets the independence question aside rather than resolving it. Not a live question. Kept in place per the no-deletion rule.
- author: Abad Morel
- source: raised 2026-08-23 while drafting the tech-stack proposal for the archive and studio apps
- tags: lords-of-cian, lovable, archive, studio, governance
- project: lords-of-cian

## Body

On 2026-08-04 the Lovable-hosted Lords of Cian Archive and the STAG Production Studio were ratified as fully independent for now, with wiring them together left as a future decision (Fleet was allowed to suggest it, not decide it).

On 2026-08-23 the interactive archive app and the studio app are named together as two destinations for the same new canon material, which could mean the two are now meant to connect, or could simply mean two separate consumers of the same canon-ledger source that never touch each other's codebase or user-facing surface.

The tech-stack proposal drafted the same day (see linked note) has both apps sharing one Supabase Postgres data source, which sits in between full independence and full wiring: no shared codebase or UI, but a shared datastore and schema. Whether that counts as still-independent or as the wiring the 2026-08-04 ruling deferred still needs a direct ruling, since retrofitting a shared schema onto two already-built, separately-provisioned Supabase projects later is real rework, while designing for it up front is not.

## Links

- relates: 2026-08-23-lords-of-cian-archive-and-studio-tech-stack-proposal
- relates: 2026-08-04-lovable-archive-production-studio-independence-ratified
