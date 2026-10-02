#!/usr/bin/env python3
"""Batch 325 (filename kept as "batch321" to match the shared naming cohort used for this whole
wave of fable/read-only review correction passes -- merge_batch321_bane/blue_collar_titan/
industrial_myth/trench_monarch/crow_king_fixes.py -- each of which also logs its own true
sequential ledger batch number inside): corrections surfaced by a read-only review pass on the
Storm That Walks Alias Chronicle track (102 entries).

Fixes applied directly to the Chronicle `.md` files (prose + header notes) in a companion pass
*before* this script; this script only amends the matching canon-ledger.json rule statements so
the ledger's own text matches the corrected files. No new creative facts and no new rules are
locked here -- pure reconciliation against already-locked canon, matching the Batch 226/68/320/321
precedent.

Fix categories (see the Chronicle files themselves for the full prose):

C1 -- Sephtis's death reframed as a staged withdrawal, not real. Sephtis (Vrail, `CC-037`, 1,997
      years old) is locked as alive in the present-day/Book-4 era elsewhere in canon, so he cannot
      have genuinely died of old age in this track. MCD-982 (the death itself), MCD-1357
      ("generations after his own death"), and MCD-1513 ("Sephtis... are both deceased") are
      reworded; MCD-983 and MCD-1348 needed no narrative change (983's prose never asserted death
      as fact; 1348's prose line "decades gone now" was fixed in the file but the rule statement
      never asserted it either) but MCD-983's file carries an added consistency note and MCD-1348's
      statement below still gets a short correction clause for the audit trail.

C2 -- Full-Trinity combat staged well within the 284-year Long Mask, after Kanja's locked age-30
      surrender of the Trinity to its sealed vault (`MCD-246`). Standard swap applied throughout:
      Mafesto's Kinetic Transfer System -> the Forge-Coat + Ironfall Boots grounding function;
      Obsidian Malice's "discharge" -> the Ironhand Gauntlets' leverage/plain striking; Onyx of
      Oblivion's named powers / "reading" a fight -> the Rexmar Machete + Kanja's own instinctive
      Rexmar-Mar tactical sense, with the Sovereign Eyes/Smoke System covering perception/stealth
      beats. MCD-588 needed no fix (no Trinity-era gear ever appears in its prose).

C3 -- The fourth-generation apprentice's sex, which flipped mid-track, resolved he/him (the clear
      majority: `MCD-1343`, `1344`, `1345`, `1349`, `1354`, `1357`, `1358`, `1359`, `1360`, `1362`).
      MCD-1505's own title and file embedded the wrong pronoun ("The Miss That Was Only Hers") and
      were renamed to match (`the-miss-that-was-only-his.md`), following the same precedent as the
      Maret Vos/Dol Maren pronoun reconciliation's "the-wind-he-read-better.md" rename (Batch 226).

C4 -- Two internal timeline slips: MCD-1088's "a season ago" corrected to "three years ago" to
      match MCD-1086/1337's own established three-year framing; MCD-1349's "a fifteen-year peace"
      reworded to "a handful of years' peace" to match MCD-1354's "two years earlier" framing.

E1 -- Duplicate Chronicle numerals: MCD-555/556/557 renumbered from the wave-6 duplicate XVI/XVII/
      XVIII (correctly held by MCD-561/562/563) to the correct XIII/XIV/XV.

E5 -- MCD-1352's wrong citation for Ghost Harbor's renaming (MCD-241, the Rolling Foundry Campaign)
      corrected to MCD-235 (the actual Ghost Harbor siege/Ash-Wharf rule).

E2/E3/E4/E6/E7 (writers'-room "wave" leaks, inline rule-ID citations inside narrative sentences,
Obsidian Malice mischaracterized as a blade or attributed to Onyx, an "engine-heat" tech
anachronism, a real-world calendar name) were all pure prose-level fixes -- none of the affected
rule statements themselves contained the flawed language, so no statement amendment was needed for
those beyond what C1-C4/E1/E5 already cover above. A stale Chronicle-count figure (93 -> 102) was
also corrected in `docs/lords-of-cian/chronicle-tracks-status.md`, outside the ledger entirely.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Read-only review pass (Storm That Walks Alias Chronicle corpus), reconciliation pass, 2026-10-02"

with open(LEDGER_PATH) as f:
    ledger = json.load(f)

rules_by_id = {r["id"]: r for r in ledger["rules"]}

# --- Amend rule statements to match the corrected Chronicle prose ---
AMENDMENTS = {
    # --- C1: Sephtis's death reframed as staged, not real ---
    "MCD-982": (
        '"The Sky the Day They Buried Him" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-sky-the-day-they-buried-him.md), The Storm That Walks "
        "Alias Chronicle LIII, wave 18. Sephtis stages his own peaceful death in his sleep, a "
        "withdrawal the entire lineage genuinely believes; his successor alone makes the call "
        "determining whether the sea-burial rites can proceed, understanding it as the one reading "
        "she could not hand to anyone else. First mortality entry specific to this alias's arc. "
        "Corrected Batch 325, 2026-10-02: Sephtis (Vrail, `CC-037`, 1,997 years old) is confirmed "
        "alive elsewhere in canon, so this is reframed as a staged withdrawal he arranges himself -- "
        "a natural-seeming death and sea-burial the lineage genuinely believes, while he continues "
        "on elsewhere in disguise during the Long Mask -- rather than a real death."
    ),
    "MCD-1357": (
        '"The Name They Gave the Second Method" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-name-they-gave-the-second-method.md), Storm That Walks "
        "Alias Chronicle LXXXIV, wave 28, closing the wave. Sailors informally name a "
        "reading-verification practice 'the second reader's watch,' tracing to the "
        "disagreement-resolution protocol the successor helped establish at MCD-979 -- a legacy "
        "entry deliberately distinct from MCD-983's strait named for Sephtis, since the successor, "
        "never given a proper name across her entire arc, receives a named practice rather than a "
        "place. No new named characters. Corrected Batch 325, 2026-10-02: Sephtis is confirmed "
        "alive elsewhere in canon (`CC-037`); the narrative prose's \"generations after his own "
        "death\" is reworded to reflect that he stepped back and let the lineage believe he had "
        "died (`MCD-982`), and an inline rule-ID citation is removed from the prose."
    ),
    "MCD-1513": (
        '"The Second Volume" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-second-volume.md), Storm That Walks Alias Chronicle CII, "
        "wave 34, closing the wave. The written creed begun at MCD-1345 fills its last page after "
        "nine years and a second volume opens; the fourth-generation apprentice's first entry in it "
        "deliberately carries the still-unresolved Titan-class weather gap (MCD-1420) forward "
        "rather than resolving it, closing wave 34 on continuity rather than resolution, consistent "
        "with MCD-1363's established practice of leaving this alias's frontier open. Confirms the "
        "current generational state: Sephtis (believed by the lineage to have died, in truth a "
        "staged withdrawal, MCD-982) and his direct successor (genuinely deceased, MCD-1356) are "
        "both gone from the school's daily life, the third-generation student remains senior "
        "credentialed authority, and the fourth-generation apprentice holds full independent "
        "forecasting authority as acting field forecaster. No new named characters. Corrected "
        "Batch 325, 2026-10-02: \"Sephtis and his direct successor are both deceased\" is reworded "
        "since Sephtis is confirmed alive elsewhere in canon (`CC-037`) -- his own apparent death "
        "is a staged withdrawal the lineage genuinely believes, not a real one."
    ),
    "MCD-1348": (
        '"What the Miss Bought Back" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-miss-bought-back.md), Storm That Walks Alias "
        "Chronicle LXXV, wave 25, closing the wave. Months after the costly false positive, the "
        "transparent handling of the miss draws new harbors to request standing readings "
        "specifically because of it, and the affected merchant returns having decided the school's "
        "honestly-logged failures make its record more trustworthy, not less. No new named "
        "characters. Corrected Batch 325, 2026-10-02: Sephtis is confirmed alive elsewhere in "
        "canon (`CC-037`); the narrative prose's \"Sephtis, decades gone now\" is reworded to "
        "\"decades retired by then,\" consistent with `MCD-982`'s own correction."
    ),

    # --- C2: Long Mask-era gear swap (full-Trinity combat staged after the age-30 surrender) ---
    "MCD-589": (
        '"The Order He Didn\'t Question" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-order-he-didnt-question.md), the Storm That Walks Alias "
        "Chronicle XLIV, wave 15 of ten (waves 6-15). A detailed Long Mask-era gear showcase (the "
        "Forge-Coat and Ironfall Boots, the Ironhand Gauntlets, and the Rexmar Machete) committed "
        "entirely on the successor's unverified forecast -- a trust-test with no safety net. "
        "Corrected Batch 325, 2026-10-02: an earlier draft staged this as a full-Trinity showcase, "
        "despite this Chronicle's placement well within the 284-year Long Mask era, after Kanja's "
        "already-locked age-30 surrender of the Trinity to its sealed vault (`MCD-246`); replaced "
        "with his correct Long-Mask-era kit (the seven-piece post-Mafesto gear system, `ARS-344` "
        "through `ARS-356`, plus the Rexmar Machete and his own instinctive Rexmar-Mar tactical "
        "sense)."
    ),
    "MCD-907": (
        '"The Storm They Read Too Late" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-storm-they-read-too-late.md), The Storm That Walks "
        "Alias Chronicle XLVII, wave 16. With no time to retreat, Kanja reads the incoming storm by "
        "raw observation rather than a forecast and turns his full Long Mask-era kit defensively "
        "against the storm's physical force itself to save the convoy, rather than against an "
        "enemy combatant -- two hulls damaged, none lost, no deaths. Corrected Batch 325, "
        "2026-10-02: an earlier draft staged this as a full-Trinity showcase and mischaracterized "
        "Obsidian Malice as a blade (it is a war club, `ARS-030`, and not one of Onyx of Oblivion's "
        "own named powers); replaced with his correct Long-Mask-era kit (`ARS-344` through "
        "`ARS-356`, plus the Rexmar Machete and his own instinctive Rexmar-Mar tactical sense)."
    ),
    "MCD-984": (
        '"The Calm Bought for a Handshake" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-calm-bought-for-a-handshake.md), The Storm That Walks "
        "Alias Chronicle LV, wave 19. A jointly-called calm window lets two mutually distrustful "
        "delegations cross contested water into a peace negotiation simultaneously and "
        "unthreatened, with Kanja's own Long Mask-era gear present only as a visible, unused "
        "deterrent -- protecting a diplomatic negotiation rather than a fleet or rescue. Corrected "
        "Batch 325, 2026-10-02: an earlier draft had the Trinity present as the visible deterrent, "
        "despite this Chronicle's placement well within the 284-year Long Mask era, after Kanja's "
        "already-locked age-30 surrender of the Trinity to its sealed vault (`MCD-246`); replaced "
        "with his correct Long-Mask-era kit (`ARS-344` through `ARS-356`, plus the Rexmar Machete)."
    ),
    "MCD-1053": (
        '"The Night They Came for the School" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-night-they-came-for-the-school.md), Storm That Walks "
        "Alias Chronicle LVIII, wave 20, first entry in the wave. A smuggling faction whose trade "
        "has been broken by the storm-timing doctrine's growing reach (extending the "
        "institutional-reach thread of MCD-570-575) raids the storm-reading school's (MCD-978) "
        "coastal compound under cover of a storm, the same tactic the doctrine itself has always "
        "denied them. A detailed Long Mask-era gear combat showcase -- the Forge-Coat and Ironfall "
        "Boots grounding a ramming charge's shock back through the attacking hull's own timbers, "
        "the Smoke System closing distance inside the storm's own dark and the Rexmar Machete "
        "timing strikes to gust gaps as a deliberate message, the Ironhand Gauntlets collapsing a "
        "dune face to strand the third landing party in the open, the Sovereign Eyes confirming no "
        "further landing follows -- defends the school and its sleeping students with zero "
        "casualties on either side beyond the raiders taken. The first Storm That Walks entry where "
        "Kanja defends an institution rather than a fleet, vessel, or rescue. Set after Sephtis "
        "stepped back and let the lineage believe he had died (MCD-982), with his successor "
        "(MCD-505) acting as the school's sole senior authority. No new named characters. Corrected "
        "Batch 325, 2026-10-02: an earlier draft staged this as a full-Trinity showcase, despite "
        "this Chronicle's placement well within the 284-year Long Mask era, after Kanja's "
        "already-locked age-30 surrender of the Trinity to its sealed vault (`MCD-246`); replaced "
        "with his correct Long-Mask-era kit, and updated to reflect `MCD-982`'s own correction that "
        "Sephtis's death was staged, not real."
    ),
    "MCD-1087": (
        '"The Truce They Wouldn\'t Honor" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-truce-they-wouldnt-honor.md), Storm That Walks Alias "
        "Chronicle LXII, wave 21. A detailed Long Mask-era gear combat showcase: during a joint "
        "weather-calibration drill between Kanja's fleet and the rival squadron under the "
        "mutual-berth truce established at MCD-985, four holdout ships that never accepted the "
        "truce break formation and attack in the dark, meaning to frame it as proof the truce was a "
        "trap. The Forge-Coat and Ironfall Boots redirect the first ramming run into open water "
        "rather than toward the rival flagship it targeted, deliberately avoiding any appearance of "
        "Kanja's fleet retaliating against the rival squadron; his own instinctive Rexmar-Mar "
        "tactical sense and the Rexmar Machete disable the second holdout's rigging in the storm's "
        "own gust-lulls with zero crew casualties; the Smoke System and the Rexmar Machete board "
        "and disable the third with three precise, bloodless line cuts; the Ironhand Gauntlets "
        "throw a wall of displaced water ahead of the fourth rather than striking its hull. All "
        "four holdouts disabled, no deaths on either side; the rival squadron's own commander takes "
        "the holdouts into her own custody in full view of both fleets. The first Storm That Walks "
        "entry where Kanja defends an agreement between two fleets rather than a single fleet, "
        "vessel, rescue, or institution, with every strike deliberately calibrated to protect the "
        "attacking holdouts' own crews as carefully as the rival squadron's ships. No new named "
        "characters -- the four holdout captains and the rival commander (already established "
        "unnamed at MCD-985) remain unnamed. Corrected Batch 325, 2026-10-02: an earlier draft "
        "staged this as a full-Trinity showcase and used a tech anachronism (\"engine-heat "
        "signature,\" this world having no engines beyond the Hymn-Engine/Meridian Engine); "
        "replaced with his correct Long-Mask-era kit (`ARS-344` through `ARS-356`, plus the Rexmar "
        "Machete) and \"galley-fire signature.\""
    ),
    "MCD-1338": (
        '"The Silence With No Wind In It" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-silence-with-no-wind-in-it.md), Storm That Walks Alias "
        "Chronicle LXV, wave 22. A detailed Long Mask-era gear combat showcase in total windless "
        "fog, the one condition the storm-timing doctrine has no signal to read; the smuggling "
        "faction from MCD-1053 exploits the doctrine's silence, and Kanja's own non-doctrine senses "
        "(hearing, close-range awareness) carry the fight instead, keeping the doctrine's real "
        "limit honest rather than quietly covered. No new named characters. Corrected Batch 325, "
        "2026-10-02: an earlier draft staged this as a full-Trinity showcase, despite this "
        "Chronicle's placement well within the 284-year Long Mask era, after Kanja's already-"
        "locked age-30 surrender of the Trinity to its sealed vault (`MCD-246`); replaced with his "
        "correct Long-Mask-era kit (`ARS-344` through `ARS-356`, plus the Rexmar Machete)."
    ),
    "MCD-1341": (
        '"The Break in the Floe" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-break-in-the-floe.md), Storm That Walks Alias Chronicle "
        "LXVIII, wave 23. A detailed Long Mask-era gear rescue-and-combat showcase freeing three "
        "ships trapped by closing pack ice, using the northern pilot's ice-reading method "
        "(MCD-1340) rather than storm-timing doctrine to time the intervention; the student "
        "credits the rescue in the ledger under the pilot's own name rather than the school's "
        "tradition. No new named characters. Corrected Batch 325, 2026-10-02: an earlier draft "
        "staged this as a full-Trinity showcase and mischaracterized Obsidian Malice as one of "
        "Onyx of Oblivion's own named powers (it is a war club, `ARS-030`, and Kanja's own "
        "weapon); replaced with his correct Long-Mask-era kit (`ARS-344` through `ARS-356`, plus "
        "the Rexmar Machete)."
    ),
    "MCD-1350": (
        '"The Fleet That Went Blind Together" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-fleet-that-went-blind-together.md), Storm That Walks "
        "Alias Chronicle LXXVII, wave 26. A detailed Long Mask-era gear combat showcase: with the "
        "rival forecaster incapacitated by illness during a genuine weather emergency, raiders "
        "exploit both fleets' shared vulnerability; the student reads weather for both fleets "
        "under one shared call, and Kanja defends both together for the first time in active joint "
        "combat rather than one fleet protecting the other's agreement from outside (MCD-1087). No "
        "new named characters. Corrected Batch 325, 2026-10-02: an earlier draft staged this as a "
        "full-Trinity showcase and included a writers'-room \"two waves earlier\" reference in the "
        "narrative prose; replaced with his correct Long-Mask-era kit (`ARS-344` through "
        "`ARS-356`, plus the Rexmar Machete) and in-world phrasing."
    ),
    "MCD-1353": (
        '"What Held the Causeway" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-held-the-causeway.md), Storm That Walks Alias "
        "Chronicle LXXX, wave 27. A detailed Long Mask-era gear showcase defending Ghost Harbor's "
        "main evacuation causeway from storm-surge collapse while it is still crowded with fleeing "
        "civilians, timed against the student's own surge reading; the causeway is held exactly "
        "long enough to clear every crossing before it collapses, with zero casualties. No new "
        "named characters. Corrected Batch 325, 2026-10-02: an earlier draft staged this as a "
        "full-Trinity showcase and mischaracterized Obsidian Malice as one of Onyx of Oblivion's "
        "own named powers (it is a war club, `ARS-030`, and Kanja's own weapon); replaced with his "
        "correct Long-Mask-era kit (`ARS-344` through `ARS-356`, plus the Rexmar Machete)."
    ),
    "MCD-1419": (
        '"The Apprentice\'s First Fleet" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-apprentices-first-fleet.md), Storm That Walks Alias "
        "Chronicle XCII, wave 31. The student formally cedes full forecasting authority to the "
        "fourth-generation apprentice for a major fleet relief engagement -- a deliberate handoff, "
        "not a crisis-forced test -- and a detailed Long Mask-era gear combat showcase (the "
        "Forge-Coat and Ironfall Boots, the Ironhand Gauntlets, the Smoke System, and the Rexmar "
        "Machete) is committed entirely on the apprentice's own unconfirmed call using the new "
        "overlap-window method from MCD-1418. The window opens exactly as called; the garrison "
        "holds and the blockade squadron surrenders. No new named characters. Corrected Batch 325, "
        "2026-10-02: an earlier draft staged this as a full-Trinity showcase, despite this "
        "Chronicle's placement well within the 284-year Long Mask era, after Kanja's already-"
        "locked age-30 surrender of the Trinity to its sealed vault (`MCD-246`); replaced with his "
        "correct Long-Mask-era kit. Also corrects the fourth-generation apprentice's pronouns to "
        "he/him, matching the clear majority usage across this track (`MCD-1343`, `1344`, `1345`, "
        "`1349`, `1354`, `1357`, `1358`, `1359`, `1360`, `1362`)."
    ),
    "MCD-1506": (
        '"What the Ash Choked Off" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-ash-choked-off.md), Storm That Walks Alias "
        "Chronicle XCV, wave 32. A coastal volcanic ash-fall -- a new hazard for this alias -- "
        "fouls the Ironhand Gauntlets mid-engagement against an opportunistic Directorate strike, "
        "the sub-series' first genuine equipment failure for this alias, forcing the Forge-Coat, "
        "Ironfall Boots, Smoke System, and Rexmar Machete to carry the fight without them. No new "
        "named characters. Corrected Batch 325, 2026-10-02: an earlier draft staged this as a "
        "full-Trinity showcase (Mafesto, Obsidian Malice, Onyx of Oblivion), despite this "
        "Chronicle's placement well within the 284-year Long Mask era, after Kanja's already-"
        "locked age-30 surrender of the Trinity to its sealed vault (`MCD-246`); replaced with his "
        "correct Long-Mask-era kit, and the equipment-failure beat transferred from Obsidian "
        "Malice's discharge housing to the Ironhand Gauntlets' plates."
    ),
    "MCD-1510": (
        '"The Window That Ended the Smuggling" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-window-that-ended-the-smuggling.md), Storm That Walks "
        "Alias Chronicle XCIX, wave 33, closing the wave. The smuggling faction that raided the "
        "school (MCD-1053) and exploited total windless fog (MCD-1338) is finally cornered in a "
        "detailed Long Mask-era gear combat showcase -- the Sovereign Eyes exposing decoy hulls, "
        "the Forge-Coat and Ironfall Boots, the Ironhand Gauntlets -- using the overlap-window "
        "method from MCD-1418/1419 to close the last blind spot on the coast; half the faction's "
        "crews are offered legitimate trade routes given the school's growing reach, the rest "
        "handed to the magistrate. Closes a long-dangling recurring antagonist thread. No new "
        "named characters. Corrected Batch 325, 2026-10-02: an earlier draft staged this as a "
        "full-Trinity showcase, despite this Chronicle's placement well within the 284-year Long "
        "Mask era, after Kanja's already-locked age-30 surrender of the Trinity to its sealed vault "
        "(`MCD-246`); replaced with his correct Long-Mask-era kit, and an inline rule-ID citation "
        "is removed from the narrative prose."
    ),
    "MCD-1511": (
        '"The Storm They Read Backward" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-storm-they-read-backward.md), Storm That Walks Alias "
        "Chronicle C, wave 34, first entry in the wave -- the alias's hundredth Chronicle. The "
        "doctrine is used forensically for the first time: the student and the fourth-generation "
        "apprentice reconstruct a storm that already happened, using drift patterns and the "
        "northern pilot's ice-reading method, to locate survivors of an uninvolved vessel that "
        "never consulted the school before it sailed; Kanja conducts the physical rescue using his "
        "own Rexmar-born strength (carried by the Forge-Coat and Ironfall Boots) and the Smoke "
        "System, with no adversary and no combat. No new named characters. Corrected Batch 325, "
        "2026-10-02: an earlier draft staged the rescue using Trinity-era gear and powers, despite "
        "this Chronicle's placement well within the 284-year Long Mask era, after Kanja's "
        "already-locked age-30 surrender of the Trinity to its sealed vault (`MCD-246`); replaced "
        "with his correct Long-Mask-era kit."
    ),
    "MCD-1512": (
        '"The Sky They Ordered Clear" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-sky-they-ordered-clear.md), Storm That Walks Alias "
        "Chronicle CI, wave 34. The doctrine's first purely joyful, zero-peril use: the school "
        "guarantees clear skies for the fourth-generation apprentice's own coming-of-age festival, "
        "with no threat, hostile party, or stake of any kind; Kanja appears without the Rexmar "
        "Machete at his hip for the first time in this alias's run. No new named characters. "
        "Corrected Batch 325, 2026-10-02: \"without Onyx of Oblivion at his hip\" is reworded to "
        "his correct Long-Mask-era weapon, the Rexmar Machete; the fourth-generation apprentice's "
        "pronouns are corrected to he/him, matching the clear majority usage across this track; "
        "and an inline rule-ID citation is removed from the narrative prose."
    ),

    # --- C3: fourth-generation apprentice's pronouns resolved he/him (majority usage) ---
    "MCD-1420": (
        '"The Weather a Titan Leaves Behind" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-weather-a-titan-leaves-behind.md), Storm That Walks "
        "Alias Chronicle XCIII, wave 31, closing the wave. A Titan-class vessel's distant passage "
        "produces slow, pulsing atmospheric and water disturbance that none of the school's three "
        "blended traditions can chart, mirroring MCD-1358's reverse case (Kanja's own senses once "
        "misread a Titan-class vessel's mass as weather; here the vessel's actual passage genuinely "
        "makes weather no tradition recognizes). The fleet holds at anchor rather than sail into "
        "unread water; the apprentice records the gap honestly in the creed's book as an open "
        "question rather than a forced resolution. Closes wave 31 deliberately leaving the "
        "doctrine's frontier open, consistent with MCD-1363. No new named characters. Corrected "
        "Batch 325, 2026-10-02: corrects the fourth-generation apprentice's pronouns to he/him, "
        "matching the clear majority usage across this track, and removes a writers'-room \"Thirty "
        "waves\" reference from the narrative prose."
    ),
    "MCD-1505": (
        '"The Miss That Was Only His" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-miss-that-was-only-his.md), Storm That Walks Alias "
        "Chronicle XCIV, wave 32, first entry in the wave. Months after the fourth-generation "
        "apprentice was ceded full forecasting authority (MCD-1419), he makes his first genuine "
        "independent miscalculation while holding it alone -- an honest, small-stakes miss with no "
        "external cause -- and logs it transparently in the ledger himself, testing what the "
        "authority actually costs now that no one checks it behind him. No new named characters. "
        "Corrected Batch 325, 2026-10-02: the fourth-generation apprentice's pronouns corrected to "
        "he/him throughout, matching the clear majority usage across this track; title and file "
        "renamed from \"The Miss That Was Only Hers\" / `the-miss-that-was-only-hers.md` to match; "
        "and two inline rule-ID citations removed from the narrative prose."
    ),
    "MCD-1509": (
        '"The Trade He Chose Instead" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-trade-he-chose-instead.md), Storm That Walks Alias "
        "Chronicle XCVIII, wave 33. The third-generation student's own grown son tells her he will "
        "not carry the craft forward, having apprenticed instead to a hull-wright -- the "
        "sub-series' first explicit dramatization on the page that the doctrine's continuity was "
        "never a matter of bloodline, only of choosing it, retroactively affirming the "
        "already-unrelated apprentice's own selection (MCD-1343). Purely domestic register, no "
        "combat. No new named characters. Corrected Batch 325, 2026-10-02: corrects the "
        "fourth-generation apprentice's pronouns to he/him (\"the girl who now held full "
        "authority\" -> \"the boy who now held full authority\"), matching the clear majority "
        "usage across this track."
    ),

    # --- C4: internal timeline slips ---
    "MCD-1088": (
        '"What the Trust Wrote Into the Manual" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-trust-wrote-into-the-manual.md), Storm That Walks "
        "Alias Chronicle LXIII, wave 21, closing the wave. The Sovereign Trust formally codifies "
        "the storm-timing doctrine into written naval regulation -- a mandatory 'storm-interval "
        "verification' protocol requiring any officer disputing a certified reading to request the "
        "reader's full record before overriding it -- crediting the school as an institution "
        "rather than Sephtis, the successor, the third-generation student, or Kanja by any name. "
        "The retired successor frames it to the student as the doctrine outliving personal "
        "reputation entirely: 'we were only ever the part that had to be believed until the part "
        "that didn't need believing caught up.' Kanja privately reflects that the doctrine's "
        "growing anonymity mirrors his own aliases' names outlasting or displacing his own (Bane "
        "unclaimed, the Trench Monarch worn by a man who never sanctioned it). The sub-series' "
        "first entry to show the doctrine reach formal, written institutional permanence rather "
        "than only informal reach (MCD-570/572/573/587) or living memory (MCD-978/1053), directly "
        "extending MCD-1086's legitimacy-test outcome into its lasting procedural consequence. "
        "Closes the twenty-first wave (with MCD-1086 and MCD-1087) on a quiet, reflective register "
        "distinct from both prior wave-closing reflections (MCD-986, MCD-1055). No new named "
        "characters. Corrected Batch 325, 2026-10-02: an internal timeline slip in the narrative "
        "prose ('a season ago') is reworded to 'three years ago,' matching MCD-1086/1337's own "
        "established three-year framing for this same handoff."
    ),
    "MCD-1349": (
        '"The Peer Who Had No One Left to Teach" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-peer-who-had-no-one-left-to-teach.md), Storm That Walks "
        "Alias Chronicle LXXVI, wave 26, first entry in the wave. The rival fleet's own "
        "generations-old weather tradition (MCD-985) faces its own succession crisis -- its aging "
        "forecaster has trained no successor in fifteen years; the third-generation student, "
        "drawing on the school's own succession history, suggests looking outside the rival "
        "fleet's own command for a candidate. No new named characters -- the rival forecaster "
        "remains unnamed, consistent with MCD-985. Corrected Batch 325, 2026-10-02: a 'fifteen-year "
        "peace' timeline slip in the narrative prose is reworded to a handful of years' peace, "
        "matching MCD-1354's own 'two years earlier' relative framing, and an inline rule-ID "
        "citation is removed from the prose."
    ),

    # --- E1: duplicate Chronicle numerals renumbered ---
    "MCD-555": (
        '"The Storm That Made Enemies Allies" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-storm-that-made-enemies-allies.md), the Storm That "
        "Walks Alias Chronicle XIII, first entry in the fifth wave. A storm larger than any prior "
        "prediction threatens both the rebel fleet and an engaged Directorate squadron equally; "
        "Kanja offers a storm-duration truce, both fleets surviving the night through genuine "
        "cooperation before the Directorate commander withdraws without resuming the engagement -- "
        "the first entry where the storm endangers both sides at once. No new named characters. "
        "Corrected Batch 325, 2026-10-02: renumbered from the duplicate \"Chronicle XVI\" (which "
        "collided with MCD-561's own correctly-numbered wave 6 entry) to the correct \"Chronicle "
        "XIII.\""
    ),
    "MCD-556": (
        '"The Prediction He Almost Used for Advantage" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-prediction-he-almost-used-for-advantage.md), the Storm "
        "That Walks Alias Chronicle XIV. A single storm prediction could trap a strategically "
        "valuable Directorate supply squadron or warn an unrelated civilian fishing fleet in the "
        "same path; Kanja prioritizes the fishing fleet over available military advantage, "
        "extending the humanitarian-rescue precedent (MCD-459) into an active choice between "
        "competing beneficiaries. No new named characters beyond the already-locked Sephtis. "
        "Corrected Batch 325, 2026-10-02: renumbered from the duplicate \"Chronicle XVII\" (which "
        "collided with MCD-562's own correctly-numbered wave 6 entry) to the correct \"Chronicle "
        "XIV.\""
    ),
    "MCD-557": (
        '"What the Second Sky-Reader Saw Alone" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-second-sky-reader-saw-alone.md), the Storm That "
        "Walks Alias Chronicle XV, closing the fifth wave. Sephtis's successor (already locked, "
        "MCD-505) makes her first fully independent, correct storm prediction under time pressure "
        "without his confirmation, fulfilling the institutional-redundancy purpose of her "
        "training. No new named characters beyond the already-locked Sephtis and his successor. "
        "Closes the Storm That Walks' fifth three-Chronicle wave (with 'The Storm That Made "
        "Enemies Allies,' MCD-555, and 'The Prediction He Almost Used for Advantage,' MCD-556). "
        "Corrected Batch 325, 2026-10-02: renumbered from the duplicate \"Chronicle XVIII\" (which "
        "collided with MCD-563's own correctly-numbered wave 6 entry) to the correct \"Chronicle "
        "XV.\""
    ),

    # --- E5: wrong citation for Ghost Harbor's renaming ---
    "MCD-1352": (
        '"The City That Had Three Days" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-city-that-had-three-days.md), Storm That Walks Alias "
        "Chronicle LXXIX, wave 27, first entry in the wave. A supermassive storm threatens Ghost "
        "Harbor (formerly Ash Harbor, MCD-235, placed on the Atlas at GEO-006); the student brings "
        "the full transparent ledger to the harbor's magistrate, who orders a full evacuation on a "
        "three-day window -- the doctrine's first application at whole-city civilian-evacuation "
        "scale. No new named characters. Corrected Batch 325, 2026-10-02: corrects a wrong "
        "citation for Ghost Harbor's renaming (MCD-241 cited, MCD-235 controls) and removes two "
        "writers'-room \"waves back\"/\"waves earlier\" references from the narrative prose."
    ),
}

for rid, new_statement in AMENDMENTS.items():
    assert rid in rules_by_id, f"Rule {rid} not found in ledger -- check for an ID typo"
    rules_by_id[rid]["statement"] = new_statement

NEW_RULES = []  # no new creative facts -- pure reconciliation, matching Batch 226/68/320/321 precedent

ledger["batches_completed"].append({
    "batch": 325,
    "date": str(date.today()),
    "source": SOURCE,
    "rule_count": len(NEW_RULES),
    "note": (
        "Reconciliation pass following a read-only review of the Storm That Walks Alias Chronicle "
        "corpus (102 entries), matching the pilot-review precedent established on the Bane corpus "
        "(Batch 320) and extended across the Blue-Collar Titan, Industrial Myth, Trench Monarch, "
        "and Crow King corpora (Batches 321-324). Fixed: Sephtis's death reframed as a staged "
        "withdrawal rather than a real one, since he is confirmed alive elsewhere in canon (`CC-037`) "
        "-- MCD-982, MCD-1348, MCD-1357, MCD-1513 reworded, MCD-983 given a consistency note; "
        "full-Trinity combat staged well within the 284-year Long Mask era, after Kanja's "
        "already-locked age-30 surrender of the Trinity (`MCD-246`), swapped for his correct "
        "Long-Mask-era kit across MCD-589, MCD-907, MCD-984, MCD-1053, MCD-1087, MCD-1338, "
        "MCD-1341, MCD-1350, MCD-1353, MCD-1419, MCD-1506, MCD-1510, MCD-1511, MCD-1512 (MCD-588 "
        "needed no fix); the fourth-generation apprentice's pronouns resolved he/him, the clear "
        "majority usage, across MCD-1419, MCD-1420, MCD-1505, MCD-1509, MCD-1512 (MCD-1505's own "
        "title and file, which embedded the wrong pronoun, renamed from \"The Miss That Was Only "
        "Hers\"/the-miss-that-was-only-hers.md to \"The Miss That Was Only His\"/"
        "the-miss-that-was-only-his.md, matching the Maret Vos/Dol Maren rename precedent, Batch "
        "226); two internal timeline slips fixed (MCD-1088's 'a season ago' -> 'three years ago'; "
        "MCD-1349's 'a fifteen-year peace' -> 'a handful of years' peace'); three duplicate "
        "Chronicle numerals renumbered (MCD-555/556/557 from the wave-6 duplicate XVI/XVII/XVIII, "
        "correctly held by MCD-561/562/563, to the correct XIII/XIV/XV); and one wrong citation "
        "fixed (MCD-1352's Ghost Harbor renaming cited MCD-241, corrected to MCD-235). A further "
        "set of pure prose-level fixes was applied directly to the Chronicle files themselves, "
        "outside this script's scope, since the affected rule statements never contained the "
        "flawed language: writers'-room 'wave'/'entries earlier' leaks reworded to in-world "
        "phrasing across MCD-505, MCD-1350, MCD-1359, MCD-1363, MCD-1418, MCD-1420, MCD-1505; "
        "inline rule-ID citations removed from narrative prose across MCD-1349, MCD-1357, "
        "MCD-1505, MCD-1507, MCD-1508, MCD-1510, MCD-1512; Obsidian Malice mischaracterized as a "
        "blade or attributed to Onyx of Oblivion fixed across MCD-907, MCD-1341, MCD-1353 (it is a "
        "war club, `ARS-030`, and Kanja's own weapon); an 'engine-heat signature' tech anachronism "
        "(this world has no engines beyond the Hymn-Engine/Meridian Engine) reworded to "
        "'galley-fire signature' in MCD-1087; and a real-world calendar name ('Tuesdays') removed "
        "from MCD-1361. The stale Chronicle-count tracker figure was also corrected from 93 to 102 "
        "in docs/lords-of-cian/chronicle-tracks-status.md. Pure reconciliation throughout -- no "
        "new creative facts, matching the Batch 226/68/320/321 precedent."
    ),
})

ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
ledger["last_updated"] = str(date.today())

ids = [r["id"] for r in ledger["rules"]]
assert len(ids) == len(set(ids)), "Duplicate rule IDs detected!"

with open(LEDGER_PATH, "w") as f:
    json.dump(ledger, f, indent=2)
    f.write("\n")

print(f"OK: {len(ledger['rules'])} total rules, {len(ledger['batches_completed'])} batches, "
      f"ledger_version {ledger['ledger_version']}, zero duplicate IDs.")
