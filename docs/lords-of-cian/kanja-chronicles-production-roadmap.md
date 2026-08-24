# Kanja Chronicles Production Roadmap — Reconciliation Plan + Phased Build

Written: 2026-08-03. Updated: 2026-08-03, Phase 0 verdict rendered. Updated: 2026-08-08, production kickoff decision + Phase 1 verification. Updated: 2026-08-08, Phase 1 execution (partial) + Kanja profile delivered. Updated: 2026-08-08, Kanja profile corrected against real Book 1 canon. Updated: 2026-08-09, scope narrowed to Chronicle 1 only. Updated: 2026-08-15, Jicome/Rexmar reading changed, uncle character role confirmed.

Depends on: `claude/geographic-consistency-audit.md` (the full audit this plan resolves).
Also depends on: `Lords_of_Cian_Writing_Agent_Fleet_Recommendation.docx` (2026-08-01, Google Drive, fileId 1_G9Zk2cgkzPX4jORUKTup3KmPR5rVIU9) — the already-approved Corvin/Isolde writing-agent plan this roadmap's Phase 3 builds on, not replaces.
Also depends on: `claude/canon-ledger.json` (this Claude Project) — the structured canon-rules ledger built in a parallel session starting 2026-08-13. CONFLICT-004 in that ledger directly overrides Phase 0 item 1 and Phase 1 item 7 below; read that entry before touching Jicome, Sovereign Trust Domain, or Southern Seaboard material.

## 2026-08-15 — Jicome/Rexmar reading changed (supersedes Phase 0 item 1); uncle character role confirmed

Two decisions from the canon-ledger session, both confirmed by Abad, both affecting open items in this roadmap directly.

**Jicome definition changed.** Phase 0 item 1 below ("Jicome / Sovereign Trust Domain naming — DECIDED... same territory, two names") is superseded. Abad chose the richer Rexmar material instead: Jicome is Haku's unified kingdom, a Rex mainland (the Regional Atlas's original JI region, capital Rexhaven) plus a Mar archipelago (a separate archipelago, not the Astral Archipelago), held by the Rexmar line after Haku. The Sovereign Trust Domain (Karkosa, Stormshelter Cove, Maw-7 Slab) is now a **separate, distinct territory**, not Jicome under another name. Full resolution logged as CONFLICT-004 in `claude/canon-ledger.json`; MCD-110 and MCD-111 corrected there, original text preserved inline as superseded.

This directly reopens Phase 1 item 7 below (the Jicome canon note that was supposed to go into Master Canon Decisions) — the note that gets written now needs to reflect this corrected reading, not the original Phase 0 verdict.

It also puts Phase 1 item 5 (Southern Seaboard theater definition) in question, not resolved. The original definition assumed Jicome and the Sovereign Trust Domain were the same place; now that they're separate, it's unclear whether "Southern Seaboard" means Jicome's coastline, the Sovereign Trust Domain's coastline, or both together. Flagged as MCD-112 (FLAGGED status, not LOCKED) in the ledger. Needs Abad's direct ruling before Phase 1 item 5 proceeds — this blocks Chronicle 1 per this roadmap's own dependency chain.

**Uncle character, role confirmed.** The "uncle" character flagged as an open item below (a Rexmar-line figure, secretly allied with Kanja but a bitter rival on the surface) is Kanja's co-conspirator, revealed in a specific chapter timed just before "someone big" dies. Confirmed by Abad 2026-08-15, logged as CHAR-002 in the ledger. Still undeveloped beyond this: no name, no physical description, no specific chapter placement, no identity for the "someone big," no established relationship to Maro Rexmar. Only urgent to build out now if he appears in Chronicle 1 specifically — same conditional as before, the role is settled but the character isn't built.

## 2026-08-09 — Scope narrowed to Chronicle 1 (Chronicle XXIII) only

Abad's instruction: focus exclusively on Chronicle 1. Everything else set aside until further notice.

This does not remove the Phase 1 canon-lock prerequisites — the atlas dedup, RA grid code, Southern Seaboard definition, and Jicome/Sovereign Trust Domain canon note are still needed before Corvin drafts Chronicle 1, since they were never chronicle-specific fixes. What changes: Chronicles XXIV and XXV, the ~35-location Gazetteer expansion, and any work not directly required to get Chronicle 1 to a draftable state are paused, not abandoned. They resume once Chronicle 1 is through Isolde and in Abad's hands.

Still open and specific to getting Chronicle 1 draftable:
- Phase 1 items 2-7 (atlas dedup, RA grid code, Southern Seaboard definition, Jicome canon note) — blocked on browser bridge access, and items 5/7 now additionally depend on the 2026-08-15 Jicome reading change above.
- The uncle character decision — role now confirmed (see 2026-08-15 update above); only blocking if the character appears in Chronicle 1 specifically, and only the full build-out (name, description, placement) remains undone.
- Book 1 structural outline scoping — relevant if Chronicle 1's events overlap Book 1's opening (the Fulfillment Ceremony falls at the end of the Long Mask era, so this needs checking against where Chronicle XXIII actually falls in the timeline).

## 2026-08-08, later — Kanja profile origin corrected. Read this before touching Kanja's backstory again.

The first delivered cut of the Kanja Personality Bible invented an origin (a dockworker's epiphany at eighteen, a 750-year-old uncle explaining the family's decline at a birthday feast) instead of using the real Book 1 canon, which already existed in Drive and answers this completely. Abad caught it and pointed back to the Lore Vault folder (`1ju89lRxrCXhnjFEcZip9Hse3r2QogcDe`). Corrected. The real material, confirmed across `MASTER CANON DECISIONS.docx`, the Session Locks section within it, `--THE PITCH COLLECTION- MY RIVAL'S DISTANCE--`, `Pitch Bible`, and `Beloved_and_Blade_Ronin_Victims.docx`:

- Kanja is a prince. His father, Maro Rexmar, is a king. Kanja's Rebellion (ages 18-30, against the Sovereign Trust, not the SBD) was winning: 22 victories in 12 years, 6 of them battles the Directorate itself classified as unwinnable.
- **The Sovereign Pier Accords**, negotiated in secret roughly 296 years before Book 1 opens: Maro Rexmar and Aethelgard Verehimu (Ozmund's father) traded the end of Kanja's rebellion for Aethelgard's future recognition of Maro as sovereign King of Jicome, plus an alliance against the Shattered Kingdoms. This, not a birthday lecture, is why Kanja's father was able to convince him to stand down from a war he was winning. Kanja surrendered the Trinity (Mafesto, Onyx, Obsidian Malice) into L9 and put on the Long Mask to wait out the deal.
- **The Fulfillment Ceremony is Book 1's opening event** (per Master Canon's own "BOOK 1 STRUCTURE: THE DEPOSED KING" section: "Opening: Murder scene. Two kings dead."). Aethelgard, king for one month, was about to crown Maro sovereign King of Jicome, fulfilling the Accords 284 years after Kanja put on the mask. At the ceremony, three contracted assassins, the Three Ronin, killed both kings: Decimus Korr ("the Silence") cleared the guards, an unnamed infiltrator ("the Ghost") had already been inside for weeks, and Serai Noth ("the Blade") killed both kings in 1.6 seconds. An SBD wet-work team sanitized the scene within four minutes. Ozmund rejects the crown the murder leaves him, hires Ezio to investigate, this is Book 1.
- The pitch material's own line for Kanja: "The 284-year performance was the longest undercover operation in history, and it ended one day too late."
- Kanja and Ozmund are cousins through their mothers, Val Saeryn Kareth and Val Mirel Kareth (Karesian war-sisters), not through their fathers. Their fathers' shared murder is the origin wound both sons carry into Book 3's confrontation ("You are becoming the thing our fathers died to prevent" / "Our fathers' way got them both killed," Master Canon's own locked line, both right, both wrong).

Corrected sections III and IV of `00_Kanja_Psychological_Profile.docx` to run on this material, retitled Section IV from "The Interrupted Boy" to "One Day Too Late," enriched the Ozmund passage in Section IX with the shared-murder/Book-3-rift material, and updated Rule 6 and the "What Kanja Wants" closing to match. Rendered to PDF and checked page by page before redelivering. This is now the second time this session that not searching the Lore Vault folder thoroughly enough produced work that had to be redone — the geography audit undercounted the manuscript's actual "Eastern Seaboard" instances earlier the same day, and this profile invented an origin that Drive already had an answer for. Both times the fix was to go back to source documents already sitting in the folder rather than infer or invent. Treat the Lore Vault folder as the source of truth before drafting anything else for this project, including future chronicle drafts.

**Uncle character, role now confirmed** — see the 2026-08-15 update at the top of this document. The paragraph that used to sit here describing this as fully open is superseded; the narrative role is settled, only the full character build-out remains.

## 2026-08-08 — Phase 1 execution (partial) + Kanja profile delivered (first pass, superseded by the correction above)

Abad instructed: "execute phase 1 and then kanjas personality bible." Both were started this session. Status below.

**Phase 1, item 1 — DONE.** Complete Chronicle Definitive Edition (fileId 1vDbolYZITr7Em066Km2q27T3J7jd1jvWv64JkD8orLg) edited directly in the live Google Doc via Find & Replace. The audit had flagged one instance of "Jicome Eastern Seaboard," the live document actually contained **four** instances of the same underlying error, not one. Read the surrounding context on each before changing it to confirm all four referred to the same place. All four corrected to "Southern Seaboard," verified via repeated Find & Replace searches returning zero remaining matches. Google Docs auto-saved.

**Phase 1, items 2-7 — BLOCKED, not done.** The Regional Atlas Gazetteer dedup (Karkosa, Maw-7 Slab), the "RA" grid code confirmation, the Southern Seaboard theater definition, the ~35-location Gazetteer expansion, and the Master Canon Decisions canon note all require live browser editing. The browser bridge (Claude in Chrome) disconnected mid-session and did not reconnect on two further attempts. No edits were made to the Atlas workbook. Items 5 and 7 additionally now depend on the 2026-08-15 Jicome reading change (see top of this document).

**Cross-check against the fleet's own decision document.** Read `Lords_of_Cian_Writing_Agent_Fleet_Recommendation.docx` in full. Architecture locked at two agents, Corvin (writer) and Isolde (continuity), both starting at Seed. Sonnet 5 primary inside Claude Code sessions, Opus 4.8 fallback, Fable 5 in reserve. Isolde's first proof: plant a contradiction, confirm the flag fires, fix it, confirm it clears.

**Confirmed by Abad, 2026-08-08:** "Chronicles 1, 2, 3" means Chronicle XXIII, XXIV, XXV, the first three chronicles of the Long Mask era.

## PHASE 0 VERDICT — rendered 2026-08-03, per Mandate 1

None of the five Phase 0 items touch money, a live deploy, or DNS, so these are decided and logged rather than left open. Mandate 1 still reserves final override to Abad; nothing here needed to wait on him to move.

1. **Jicome / Sovereign Trust Domain naming — SUPERSEDED 2026-08-15, see the update at the top of this document.** Originally decided as same territory, two names. Abad has since chosen the richer Rexmar material instead (CONFLICT-004 in `claude/canon-ledger.json`): Jicome is Haku's unified Rex-mainland-plus-Mar-archipelago kingdom, and the Sovereign Trust Domain is a separate territory. The canon note still needs writing into Master Canon Decisions — Phase 1 item 7, still open — but it now needs to reflect this corrected reading, not the original verdict.
2. **Southern Seaboard scope — REOPENED 2026-08-15, see the update at the top of this document.** Originally defined as the coastal campaign theater spanning Jicome/Sovereign Trust Domain territory and reaching into neighboring Prefecture coastline. That definition assumed Jicome and the Sovereign Trust Domain were the same place; now that they're separate, this needs a fresh ruling from Abad before Phase 1 item 5 can proceed. **Formal definition not yet written into the atlas or Master Canon Decisions — Phase 1 item 5, still open, now blocked on this ruling rather than just browser access.**
3. **"Jicome Eastern Seaboard" line (C1) — DONE.** Executed 2026-08-08; turned out to be 4 instances, not 1.
4. **Atlas duplicate listings — DECIDED, approved for fix, not yet executed.** Karkosa row 48, Maw-7 Slab row 49 (both Sovereign Trust Domain side), located but not edited. Phase 1 items 2-3.
5. **Canon-lock documents and Book 1 structural outline — PARTIALLY RESOLVED, and now further clarified.** Master Canon Decisions and the Session Locks are not missing, a full-Drive search located them. Master Canon Decisions itself contains a "BOOK 1 STRUCTURE: THE DEPOSED KING" section: opening murder scene (the Fulfillment Ceremony), three acts (Investigation → 10-Day Interregnum → Karkosa Heist), epilogue (The Great Breach, SBD uncovered). This may mean the Book 1 structural outline is less "missing" than "not yet assembled into a single standalone outline document" — the beats already exist across Master Canon Decisions and the Session Locks. Worth re-checking before treating this as a from-scratch draft.

## Phase 1 — Canon lock and atlas update (needed for Chronicle 1)

1. ✅ **DONE.** Change "Eastern" to "Southern" in Complete Chronicle Definitive Edition. 4 instances fixed.
2. ⬜ **BLOCKED.** De-duplicate Karkosa (row 48 located, not edited).
3. ⬜ **BLOCKED.** De-duplicate Maw-7 Slab (row 49 located, not edited).
4. ⬜ **NOT STARTED.** Confirm the "RA" grid code against source workbook tabs.
5. ⬜ **BLOCKED ON A NEW RULING, not just access.** Add a Southern Seaboard theater definition to the atlas or Master Canon Decisions — needs Abad's ruling on what "Southern Seaboard" means now that Jicome and the Sovereign Trust Domain are separate territories (see 2026-08-15 update).
6. ⬜ **PAUSED, not needed for Chronicle 1 alone.** Expand the Gazetteer with ~35 recurring unlisted locations.
7. ⬜ **NOT STARTED, and reading changed.** Add a canon note to Master Canon Decisions resolving Jicome / Sovereign Trust Domain naming — the note now needs to reflect the corrected Rex-mainland-plus-Mar-archipelago reading, not the original same-territory verdict.
8. ⬜ **NEEDS RE-SCOPING, see item 5 above.** Book 1 structural outline: may already exist in fragments across Master Canon Decisions and Session Locks rather than needing a from-scratch draft.

## Phase 2 — Continuity infrastructure

Feed the reconciled atlas, gazetteer, and canon-lock documents into the shared knowledge graph Isolde checks new drafts against. Isolde's first proof: the Stormshelter Cove distance claim as planted test case.

## Phase 3 — Production (Chronicle 1 only, for now)

Corvin drafts Chronicle XXIII (Chronicle 1) against the reconciled canon; the draft passes through Isolde before reaching Abad for review. Chronicles XXIV and XXV are paused until Abad reopens them. Kanja's corrected personality bible (`00_Kanja_Psychological_Profile.docx`) should be fed to Corvin alongside the Sovereign Pier Accords / Fulfillment Ceremony material once Phase 1 finishes — Corvin needs the real origin, not the invented one, or the chronicle will need the same correction this profile just went through.

## Phase 4 — Maintenance (paused with the rest of the multi-chronicle scope)

A geography check every 5-10 chronicles instead of one audit at the end. Gazetteer stays a living document. Resumes once Chronicle 2 production reopens.

## Open items for the next session

- Get Abad's ruling on Southern Seaboard scope now that Jicome and the Sovereign Trust Domain are separate territories (new, 2026-08-15) — this blocks Phase 1 item 5 and, through it, Chronicle 1.
- Write the corrected Jicome/Sovereign Trust Domain canon note into Master Canon Decisions (Phase 1 item 7), reflecting the 2026-08-15 reading, not the original Phase 0 verdict.
- ~~Get Abad's direction on the new uncle character~~ — role confirmed 2026-08-15 (co-conspirator, secretly allied, revealed before a major death). Still needs a name, description, and chapter placement if he appears in Chronicle 1.
- Reconnect the browser bridge and finish Phase 1 items 2-4 and 6.
- Save `00_Kanja_Psychological_Profile.docx` into the Drive folder alongside the other eight profiles.
- Re-check whether the Book 1 structural outline genuinely needs a from-scratch draft or an assembly pass over existing Master Canon material, and whether Chronicle 1 overlaps it at all.
- Gazetteer expansion, Chronicles 2 and 3: paused, resume when Abad reopens the wider scope.
- Before drafting Chronicle 1, read `MASTER CANON DECISIONS.docx`, `--THE PITCH COLLECTION- MY RIVAL'S DISTANCE--`, `Pitch Bible`, and `Beloved_and_Blade_Ronin_Victims.docx` in full — this is where the Fulfillment Ceremony, the Three Ronin, and the Sovereign Pier Accords live.
- Read `claude/canon-ledger.json` before drafting anything Jicome, Rexmar-lineage, or Astral-Archipelago related — that's now the authoritative discrete fact list for this material, not this roadmap alone.

**Note (2026-08-24): this roadmap is unrelated to the cult-network/canon-ledger cult work and to the interactive archive app, kept here for full context. As of this date, canon-ledger.json is at 510 rules across 21 batches — check it directly for the current status of any Jicome/Rexmar/Southern-Seaboard question raised above rather than assuming this doc's 2026-08-15 update is still the latest word.**
