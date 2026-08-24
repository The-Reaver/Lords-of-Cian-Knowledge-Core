# Anansi close-out, pending placement — session of 2026-08-03

## Status
OPEN as of 2026-08-19. The device bridge to the operator's machine (`desktop-4uc2ltp`) was disconnected for the entire 2026-08-03 close-out session, so nothing was written to the real Knowledge Core at `C:\Users\abadm\stag`. Six files exist only as delivered attachments and in this project doc. A nightly reminder checks this doc until the placement below is completed, then stops itself.

**IMPORTANT — structural finding, 2026-08-19:** the nightly reminder runs as a scheduled/cloud task, and scheduled cloud sessions never have desktop-bridge access, regardless of whether the operator's desktop app is open. Tonight's check found the `mcp__remote-devices__*` tools absent entirely (not just erroring "not connected"), confirming this is not a transient desktop-app-closed condition but a structural limitation of cloud-scheduled runs. This nightly trigger cannot complete the placement on its own, no matter how many nights it fires. To finish this close-out, the operator needs to either (a) open a normal (non-scheduled) Cowork/Claude session while the desktop app is open and ask it to pick up this doc, or (b) recreate this reminder as a local/on-device scheduled task if that option is available to them. The nightly cloud reminder should keep running only as a low-cost check-in; it will keep reporting the same "still pending" result until the operator does one of the above.

**Notification log:** operator pushed a notification about this structural block on 2026-08-23 (5 nights unresolved since the 2026-08-19 finding, same result every night). To avoid nightly notification spam on an unresolved, structurally-blocked condition, future nightly runs should re-check silently and only push another notification if either (a) the device connects and the run can proceed/complete, or (b) roughly a week has passed since the last notification with the block still unresolved. Reply briefly in-session every night regardless; that reply is not seen live since this runs unattended.

## Instructions for whichever session picks this up next
1. Call `mcp__remote-devices__get_device_info`. If it errors "not connected to the bridge," the operator's desktop app is still closed. Stop here, tell the operator in that session's reply that the Anansi close-out is still pending and their desktop app needs to be open, and leave this doc's status as OPEN. Do not delete the reminder trigger.
2. If the device is connected: request/confirm access to the `stag` folder, then read `research/knowledge-home/notes` and check whether any of the 5 candidate notes below duplicate something already in the real Core. Link instead of duplicating if so (Step 2 of the `stag-closeout` skill).
3. Write the 6 files below (5 atomic notes + handoff) verbatim into `research/knowledge-home/candidates/2026-08-03/` on the operator's machine, using the exact filenames given.
4. Stage a candidate entry for `research/knowledge-home/structure-notes/artifact-registry.md` covering the 3 artifacts listed below. Do not edit the live registry directly.
5. Hand the operator exact native git commands (to run themselves, in their own terminal — never through the device bridge) that stage only the 5 notes marked RATIFIED below, plus the handoff file. Do not stage the whole candidates folder wholesale.
6. Once steps 2 to 5 are done, update this doc's Status line to CLOSED with today's date, then find this reminder's trigger (list_triggers, name "Anansi close-out nightly reminder") and call delete_trigger on it so it stops firing.
7. Report back in that session's reply: Core count before/after, files placed, ratification outcome, artifacts staged, and confirmation the reminder was cancelled.

## Ratification outcome (already ruled, 2026-08-03)
Same-session ruling, light findings, no build/security/compliance weight, full Brain Trust seat structure not warranted. All 5 notes RATIFIED. This ruling has not yet been checked against the live Core — re-run dedup (step 2 above) before treating them as safe to commit.

## The 6 files, verbatim

### File 1: 2026-08-03-jicome-sovereign-trust-domain-same-territory.md
RATIFIED. (Full body already exists as a delivered attachment in the 2026-08-03 chat; also summarized in `kanja-chronicles-production-roadmap.md` in this project — Jicome and Sovereign Trust Domain are two names, cultural vs. administrative, for one territory.)

### File 2: 2026-08-03-southern-seaboard-theater-definition.md
RATIFIED. Type: decision. REVIEW: high-impact.
Body: The Complete Chronicle and Long Mask Chronicles both use "Southern Seaboard" for Jicome's home coast, but also apply it to Maw-15 (Regional Atlas cell B16, The Prefecture, ~1,600 miles from Jicome) and Stormshelter Cove (cell G15, Sovereign Trust Domain, non-contiguous with Jicome). Fleet verdict, rendered 2026-08-03: "Southern Seaboard" is the coastal campaign theater spanning Jicome/Sovereign Trust Domain territory and reaching into neighboring Prefecture coastline. Resolves both findings with no text changes required.
Links: depends-on File 1; depends-on File 3 (resolves 2 of its 3 contradictions).

### File 3: 2026-08-03-atlas-vs-manuscript-audit-found-3-contradictions.md
RATIFIED. Type: finding.
Body: Full audit of Complete Chronicle Definitive Edition (87,701 words) and Long Mask Chronicles T3 Corrected (~58,000 words) against the Regional Atlas found 3 confirmed contradictions, all in the Complete Chronicle: (1) Jicome's coast called "Eastern Seaboard" once, though the atlas puts Jicome's only two ports in the westmost grid column. (2) Maw-15 grouped into Jicome's "Southern Seaboard" campaign though the atlas places it in The Prefecture, ~1,600 miles away. (3) Stormshelter Cove called part of the same Southern Seaboard though the atlas places it in non-contiguous Sovereign Trust Domain territory. Long Mask Chronicles produced zero confirmed contradictions. Full detail in `geographic-consistency-audit.md`, this project.
Links: caused File 2; see-also File 4.

### File 4: 2026-08-03-atlas-coverage-gap-and-internal-duplicates.md
RATIFIED. Type: finding.
Body: Karkosa and Maw-7 Slab are each listed twice in the Regional Atlas Gazetteer (Sovereign Trust Domain and Lawless Reaches, identical grid cells G16/G17). Fleet verdict resolves both to Sovereign Trust Domain, approved but not yet executed. The World Overview Grid uses region code "RA" in rows 19-21, columns H-K, never defined in the Region Code Key (only "LR" is defined there); likely a typo, needs confirmation against the source workbook. Across ~145,000 words of manuscript, the large majority of named locations (Portside, Ironport, Keldane City, the Gilded Lighthouse, Gale Straits, Fort Gallan, and roughly 30 more) have no Gazetteer entry. Full list in `geographic-consistency-audit.md`, this project.
Links: see-also File 3; blocks File 5.

### File 5: 2026-08-03-canon-lock-docs-found-book1-outline-missing.md
RATIFIED. Type: correction.
Body: An August 1, 2026 session reported the canon-lock decision documents and Book 1 structural outline as missing. A full, unscoped Drive search on 2026-08-03 located MASTER CANON DECISIONS.docx (fileId 1NLOAu4Qh_ICV30Yd9tKVoBpX2GNBRiBb) and Session Lock 3 (fileId 1dslKhXMpe9pI2-Zoc390jLm8yOgfaWsoQ989oovi4zM). The August 1 search was scoped to a single folder, producing a false "missing" finding; future searches should run unscoped first. One genuine gap remains: Book2_Structural_Outline_Champions.docx exists, no equivalent exists anywhere in Drive for Book 1. Open question for the operator, still unanswered: draft a Book 1 outline now, or defer.
Links: corrects an implicit claim in the 2026-08-01 fleet handoff; blocks File 4 (Phase 1 depends on this being resolved or deferred).

### File 6: SESSION_HANDOFF_2026-08-03.md
The full Step 6 handoff document from the 2026-08-03 session. Content already stored in `kanja-chronicles-production-roadmap.md` and `geographic-consistency-audit.md`, this project, plus delivered as an attachment that session.

## Artifacts to register (Step 4/5)
- `geographic-consistency-audit.md` — Claude project doc, this project.
- `kanja-chronicles-production-roadmap.md` — same project, includes the Phase 0 fleet verdict.
- `Lords_of_Cian_Geography_Reconciliation_Handoff.docx` — delivered directly to the operator, 2026-08-03, not in Drive or the stag folder.

## Note (2026-08-24)
This close-out doc is a separate, older thread from the cult-network/canon-ledger work and archive-app planning done this session, and its own nightly reminder trigger's current status was not checked or touched this session. If this reminder is still firing and reporting "still pending," it's worth confirming next time the device bridge is up whether the placement steps above ever actually completed — check `research/knowledge-home/candidates/` for a `2026-08-03/` subfolder, and run `list_triggers` for a trigger named "Anansi close-out nightly reminder" to see if it's still active.
