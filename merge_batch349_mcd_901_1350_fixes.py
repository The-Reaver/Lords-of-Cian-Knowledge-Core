#!/usr/bin/env python3
"""Batch 349: Fable-model read-only review of MCD-901 through MCD-1350 --
mechanical fixes only (contradictions/errors flagged NEEDS ABAD left untouched).

Covers:
  - C1: MCD-951 (Undertow anachronism -> Mar-bloodline tide-sense/anchor-chain work)
  - C2: MCD-1215 (fourth -> fifth working ship, The Second Chance cross-ref)
  - C3: MCD-1241, MCD-1247 (Forge-Coat V3 -> V4 gear at ages 235/180)
  - C4: MCD-1054, MCD-1055, MCD-981 (Sephtis's "death" -> staged withdrawal, MCD-982)
  - C6: MCD-1135 ("two years of cross-district trust" -> built-since-Dredge-Line)
  - E1: batch-citation renumbering, "Corrected Batch 321" -> the real batch number
        for each alias track (Trench Monarch 323, Crow King 324, Iron Bastard 326,
        Sovereign Ghost 327, Lord of Embers 330)
  - E2: category normalization, MCD-1024/MCD-1093 territory-chronicle ->
        phase2-territory-chronicle
  - E3: MCD-1137 ("found Halst and Sok" -> "found Danne Sok and Maret Vos")
  - E4: MCD-1074 (ARS-347 -> ARS-348 in a V4-gear citation list)
  - E5: MCD-958 ("Kanja's ageless nature and an original crew member's" ->
        "Kanja's long lifespan and a veteran hand's (already forty-five when he
        signed on)")
  - E6: MCD-1311/1314/1326/1329/1332 (Mafesto's own "grounding mechanism/function"
        -> Kanja's own grounding conductance (MCD-291) working through Mafesto's
        Kinetic Transfer System, ARS-010)
  - E7: MCD-1071 (stomp-tremor -> stamp, Ironfall-Boots-vs-Mafesto fix),
        MCD-1038 (Mafesto's KTS reading rigging tension -> Kanja reading it,
        tension-reading is Iron Bastard doctrine not KTS)
  - E8: MCD-1244 ("unseal Onyx" -> "go back for Onyx"; Onyx is vaulted at Karkosa,
        not carried sealed on his person)

Deliberately NOT touched (NEEDS ABAD / out of scope for this batch): C5 (the
Garren Hask/Efa Gol/Pell Ostra cross-track mortality contradiction -- MCD-920,
1089, 1090, 1243, 1246, 1252, 1253, 1254, 1255, 1076), E9 (the naval-cannon
tech-level question itself, beyond the unrelated fixes already applied to
MCD-1038/MCD-1211), and all ENRICHMENT/optional items (MCD-1045/1078 Trinity-era
clarifiers, MCD-1258's runner's-son clarifier, near-collision renames, new Atlas
placements).

Companion prose fixes applied directly to the affected Chronicle .md files
(docs/lords-of-cian/chronicles/): senas-own-student.md and
the-forge-that-bought-its-own-freedom.md (V3 -> V4 gear, matching MCD-1241/1247);
the-reading-the-third-student-made-alone.md, what-outlived-the-woman-who-carried-it.md,
and the-reading-he-could-no-longer-make-alone.md (Sephtis's "death"/"decline" ->
staged withdrawal, matching MCD-1054/1055/981). the-debt-the-sea-called-in.md
(MCD-951's own Chronicle file) was checked and found already corrected in a prior
pass -- no further prose edit needed there, only its stale ledger statement.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Fable-model (background agent) read-only review of canon-ledger.json MCD "
    "rules 901-1350 against the full ledger and Chronicle corpus, 2026-10-02."
)

# ---------------------------------------------------------------------------
# AMENDMENTS: full corrected statement text per rule ID.
# ---------------------------------------------------------------------------
AMENDMENTS = {
    # C1 -- MCD-951: Undertow (ARS-388, a Book-2-onward Moonvault gift) is
    # anachronistic in this Rebellion-era entry.
    "MCD-951": (
        "\"The Debt the Sea Called In\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-debt-the-sea-called-in.md), Sovereign "
        "Ghost of the Great Sea Alias Chronicle XLIX, wave 17. A Titan-scale "
        "natural sea creature threatens a grain convoy, and Kanja drives it "
        "under and away using his own Mar-bloodline tide-sense (MCD-295) and "
        "ordinary anchor-chain/hawser work rather than kill it in open water "
        "near crewed hulls (corrected Batch 327: an earlier draft used Undertow, "
        "ARS-388, a Book-2-onward Moonvault gift that does not exist in this "
        "Rebellion-era window). First entirely natural, non-human threat for "
        "this alias."
    ),
    # C2 -- MCD-1215: the fleet already has an unnamed fourth ship (The Second
    # Chance, MCD-607); this surrendered vessel is the fifth, not the fourth.
    "MCD-1215": (
        "\"The Captain Who Gave Up His Ship\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-captain-who-gave-up-his-ship.md), "
        "Sovereign Ghost of the Great Sea Alias Chronicle LXXVII, wave 26. A new "
        "register: a dismasted Trust corvette captain voluntarily surrenders his "
        "ship whole, cargo and commission, rather than be captured -- the crew "
        "is freed per standard practice and the vessel becomes the fleet's "
        "unnamed fifth working ship (the fourth being the crew-named transport "
        "The Second Chance, MCD-607). No new named characters."
    ),
    # C3 -- MCD-1241/MCD-1247: age 235 and age 180 both fall in the Forge-Coat's
    # V4 era (ages 180-284) per ARS-348, not V3 (ages 80-180).
    "MCD-1241": (
        "\"Sena's Own Student\" (full narrative text at "
        "docs/lords-of-cian/chronicles/senas-own-student.md), The Scourge Alias "
        "Chronicle LXXVI, wave 26, first entry. Age 235, V4 gear. Direct "
        "generational-transmission payoff to \"The Blade She Almost Didn't "
        "Sheathe\" (MCD-1043, age 190): forty-five years later, Sena "
        "(established minor crew member) talks down a newer, younger crew "
        "member's near-lethal impulse against an already-surrendered guard "
        "using the same words and doctrine Kanja once used on her, with Kanja "
        "present but not needing to intervene. No new named characters beyond "
        "the already-established Sena."
    ),
    "MCD-1247": (
        "\"The Forge That Bought Its Own Freedom\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-forge-that-bought-its-own-freedom.md), "
        "The Scourge Alias Chronicle LXXXII, wave 28, first entry. Age 180, V4 "
        "gear. Extends \"The Merchant Who Changed His Trade\" (MCD-824) into a "
        "new proactive register: an unnamed forge-town owner, acting on "
        "secondhand, unconfirmed reputation alone rather than any direct visit "
        "or pressure, spends two years voluntarily converting his "
        "slave-trade-linked ore operation before the crew ever arrives, "
        "discovered only by coincidence on an unrelated supply run. No new "
        "named characters."
    ),
    # C4 -- MCD-1054/1055/981: Sephtis's exit is a staged withdrawal (MCD-982),
    # not a death or genuine physical decline.
    "MCD-1054": (
        "\"The Reading the Third Student Made Alone\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-reading-the-third-student-made-alone.md), "
        "Storm That Walks Alias Chronicle LIX, wave 20. With Sephtis's successor "
        "(MCD-505) three days away on legitimate institutional business, the "
        "third-generation student (first introduced MCD-983) makes her first "
        "fully independent, unconfirmed storm call under real stakes -- "
        "correctly overriding forty years of seasonal almanac pattern to move a "
        "harbor fleet early, with the storm arriving two hours ahead of even "
        "her own revised number and the early-moved fleet losing nothing. "
        "Kanja, present by coincidence rather than as her teacher or tester, "
        "tells her afterward that she inherited not Sephtis's gift but three "
        "generations' accumulated courage in being visibly wrong. The first "
        "entry to individually center the third-generation student's own "
        "independent judgment, distinct from MCD-557's second-generation "
        "first-solo-call entry by testing institutional depth one generation "
        "further, with the successor's absence circumstantial rather than a "
        "designed test. Set after Sephtis's staged withdrawal (MCD-982) and the "
        "school's founding (MCD-978); the successor remains alive and active "
        "elsewhere. No new named characters."
    ),
    "MCD-1055": (
        "\"What Outlived the Woman Who Carried It\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-outlived-the-woman-who-carried-it.md), "
        "Storm That Walks Alias Chronicle LX, wave 20, closing the wave. Now "
        "elderly, Sephtis's successor (MCD-505) formally and undramatically "
        "retires from making storm calls herself, telling the third-generation "
        "student (MCD-983) that the real risk was no longer her hands but "
        "being trusted past the point of being checked, and hands over her "
        "full running ledger of calls -- successes and honest misses alike -- "
        "as the doctrine's actual inheritance rather than the gift itself. "
        "Confirms the storm-timing doctrine's institutional continuity now "
        "runs three generations deep and does not depend on any single living "
        "person, echoing and extending MCD-986's closing reflection from an "
        "institutional rather than personal angle. Distinct from Sephtis's own "
        "staged-withdrawal-and-succession arc (MCD-981-983): a chosen "
        "stepping-back, not decline or death; does not assert or imply the "
        "successor's death. Kanja present throughout as a quiet witness, no "
        "command or resolution authorship. Closes the Storm That Walks' "
        "twentieth three-Chronicle wave (with 'The Night They Came for the "
        "School,' MCD-1053, and 'The Reading the Third Student Made Alone,' "
        "MCD-1054). No new named characters."
    ),
    "MCD-981": (
        "\"The Reading He Could No Longer Make Alone\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-reading-he-could-no-longer-make-alone.md), "
        "The Storm That Walks Alias Chronicle LII, wave 18. Sephtis, apparently "
        "weakened by a fever, can still read the sky but can no longer chart it "
        "himself; he dictates a call to his successor in full view of the "
        "fleet rather than hide the decline -- the first visible step of the "
        "withdrawal he stages at MCD-982."
    ),
    # C6 -- MCD-1135: "two years" was an uncited chronology figure; reworded to
    # the established, undated "trust built since the Dredge-Line."
    "MCD-1135": (
        "\"What the Bad Harvest Left Behind\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-the-bad-harvest-left-behind.md), "
        "Trench Monarch Alias Chronicle LXXVIII, wave 26, closing the wave. "
        "Rebellion era, pre-Black-Trench. A blight-driven regional grain "
        "shortfall across three upriver districts gives the tally method "
        "nothing to verify and no owner to correct; Kanja instead uses the "
        "cross-district trust built since the Dredge-Line to organize a "
        "voluntary, honest accounting and redistribution of scarce grain, with "
        "Efa Gol running the logistics. Two districts refuse and are not "
        "coerced; nobody starves, but no district is made whole either -- the "
        "method's real institutional legacy paying off in a form it was never "
        "built to produce. No new named characters. Closes the Trench "
        "Monarch's twenty-sixth wave (with \"The Duel Fought to Its Own "
        "Rhythm,\" MCD-1133, and \"The Men Who Fought in His Name,\" "
        "MCD-1134)."
    ),
    # E3 (+ E1 batch renumber) -- MCD-1137: the correction note itself had a
    # leftover self-referential error ("found Halst and Sok" -- Corren Halst
    # can't find himself); should name the other two founding members.
    "MCD-1137": (
        "\"What Corren Halst Never Told the Others\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-corren-halst-never-told-the-others.md), "
        "Trench Monarch Alias Chronicle LXXX, wave 27. Rebellion era, "
        "pre-Black-Trench. Corren Halst's own dedicated origin entry -- the "
        "last of the founding four without one. Reveals he was freed once "
        "before, from one of the Maws, by a rebellion cell that collapsed to "
        "internal betrayal; made his way to the docks afterward, found Danne "
        "Sok and Maret Vos there (two other Maw survivors with the same "
        "hard-earned caution), and the three of them together observed "
        "Kanja's crew for three weeks before approaching, ultimately trusting "
        "Garren Hask's meticulous, cross-witnessed ledger before trusting "
        "Kanja himself. No new named characters beyond the already-locked "
        "Corren Halst. Second entry in the Trench Monarch's twenty-seventh "
        "wave. Corrected Batch 321, 2026-10-02: the original draft said he was "
        "freed from a 'work-camp' and placed his three-weeks observation of "
        "the crew before he'd found Danne Sok and Maret Vos on the docks -- "
        "reworded so the prior rescue is from one of the Maws (matching "
        "`MCD-234`'s Maw-survivor framing) and the observation period happens "
        "after the three of them had already found each other there, matching "
        "the manuscript's own locked account (Chronicle III, Batch 70)."
    ),
    # E4 -- MCD-1074: ARS-347 is V1/V2, not V4; the V4 citation list should
    # read ARS-348.
    "MCD-1074": (
        "\"The Strait That Froze Early\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-strait-that-froze-early.md), the "
        "Scourge Alias Chronicle LXI, wave 21, first entry. Age 268, V4 gear "
        "(Forge-Coat/Smoke System/Sovereign Eyes/Ironhand Gauntlets all V4, "
        "ARS-348/350/352/354), Mend-Line still V3 (ARS-355, V4 doesn't begin "
        "until age 270). The sub-series' first cold/ice-environment combat "
        "showcase: a northern slaving route freezes eleven days early, "
        "trapping a convoy ship in pack ice. Crossing the floes alone, the "
        "Ironhand Gauntlets' V4 blood-heating keeps his grip functional where "
        "cold would otherwise cost it; the Ironfall Boots' impact-sole "
        "tremor, built to destabilize standing opponents, incidentally cracks "
        "the ice under a watch post, and he deliberately doesn't risk a "
        "second use near the hull itself, since a tremor strong enough "
        "against ice stressed by freezing water risks opening the ship to the "
        "sea before the forty-one captives below can be freed; the "
        "Forge-Coat's grounding weave redirects a boarding axe's own swing at "
        "close range. A hypothermic child is warmed via an off-label field "
        "use of the Mend-Line's sealed reservoirs (ARS-355) against her core "
        "rather than a wound. Efa Gol's own successor and Garren Hask "
        "(CC-130, CC-115/116) referenced in established roles, not staged in "
        "new action -- Efa Gol herself has already stepped back by this age "
        "(268), well past her age-150 handoff (`MCD-807`). Onyx of Oblivion, "
        "Mafesto, and Obsidian Malice correctly absent per the Trinity's "
        "age-30 surrender (`MCD-246`). No new named characters."
    ),
    # E5 -- MCD-958: Kanja is long-lived, not literally ageless; the crew
    # member was already an adult (forty-five) when he joined, not "original"
    # in the sense of having aged alongside Kanja from youth.
    "MCD-958": (
        "\"The Last Watch of an Old Hand\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-last-watch-of-an-old-hand.md), "
        "Sovereign Ghost of the Great Sea Alias Chronicle LVI, wave 19. First "
        "entry to directly dramatize the mortality gap between Kanja's long "
        "lifespan and a veteran hand's (already forty-five when he signed on) "
        "natural aging and eventual death for this alias."
    ),
    # E6 -- MCD-1311/1314/1326/1329/1332: the grounding/conductance mechanic
    # (MCD-291) belongs to Kanja's own Bio-Drakma skeleton, channeled through
    # Mafesto's Kinetic Transfer System (ARS-010) -- not a standalone "function"
    # of Mafesto's own.
    "MCD-1311": (
        "\"The Frost That Didn't Wait for Spring\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-frost-that-didnt-wait-for-spring.md), "
        "Lord of Embers Alias Chronicle LXV, wave 22. A detailed, "
        "battle-intense Trinity combat showcase in the alias's first "
        "deep-cold/frost environmental register: a Directorate patrol "
        "exploits an unseasonable freeze at a highland terrace, and Kanja "
        "discovers that his own grounding conductance (MCD-291) working "
        "through Mafesto's Kinetic Transfer System (ARS-010) requires "
        "actively retaining heat before it can be redirected, a genuine "
        "cold-weather limit not previously shown. Obsidian Malice used for "
        "steam-based blinding rather than direct damage. No new named "
        "characters."
    ),
    "MCD-1314": (
        "\"The Storm That Nearly Took the Anvil\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-storm-that-nearly-took-the-anvil.md), "
        "Lord of Embers Alias Chronicle LXVIII, wave 23. A detailed, "
        "battle-intense Trinity combat showcase: a genuine open-sea storm "
        "nearly capsizes The Anvil itself while a Directorate cutter uses the "
        "weather as cover for a boarding strike; Kanja's own grounding "
        "conductance (MCD-291) working through Mafesto's Kinetic Transfer "
        "System (ARS-010) is used to brace the ship's own straining structure "
        "and Obsidian Malice's discharge performs emergency mid-battle "
        "structural repair, both new applications of established gear "
        "mechanics. Kanja pulls enemy sailors from the water after the fight, "
        "extending established restraint. No new named characters."
    ),
    "MCD-1326": (
        "\"What the Canyon Carried Sound Of\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-the-canyon-carried-sound-of.md), "
        "Lord of Embers Alias Chronicle LXXX, wave 27. A detailed, "
        "battle-intense Trinity combat showcase in the alias's first "
        "arid/desert canyon environmental register: an ore convoy ambush is "
        "broken by turning the canyon's own dry-air acoustics against dug-in "
        "Directorate positions, with Cadence Ruin detecting repositioning "
        "through bare rock and Kanja's own grounding conductance (MCD-291) "
        "working through Mafesto's Kinetic Transfer System (ARS-010) shown "
        "behaving differently against parched, heat-radiating stone than wet "
        "or frozen ground. No new named characters."
    ),
    "MCD-1329": (
        "\"What He Came Back to Finish\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-he-came-back-to-finish.md), Lord "
        "of Embers Alias Chronicle LXXXIII, wave 28, direct sequel to "
        "MCD-1328. A detailed, battle-intense Trinity combat showcase fought "
        "under genuine, still-healing physical limitation: Kanja fights the "
        "most tactically careful, restraint-driven engagement of the tour, "
        "leaning on Onyx of Oblivion to carry a larger share of the active "
        "fighting while Kanja's own grounding conductance (MCD-291) working "
        "through Mafesto's Kinetic Transfer System (ARS-010) does more "
        "defensive work than usual, successfully defending three settlements "
        "targeted specifically because word of his injury reached the "
        "Directorate. No new named characters."
    ),
    "MCD-1332": (
        "\"What the Pilgrims Never Saw Coming\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-the-pilgrims-never-saw-coming.md), "
        "Lord of Embers Alias Chronicle LXXXVI, wave 29. A detailed, "
        "battle-intense Trinity combat showcase protecting a "
        "four-thousand-person pilgrimage crowd from a Directorate strike "
        "using the procession as cover; Kanja's own grounding conductance "
        "(MCD-291) working through Mafesto's Kinetic Transfer System "
        "(ARS-010) is repurposed for physically shepherding bystanders and "
        "Obsidian Malice's discharge is shaped into narrow containment "
        "lanes, prioritizing crowd safety and minimal disruption over speed "
        "for the first time. No new named characters."
    ),
    # E7 (+ E1 batch renumber) -- MCD-1071: the stomp-tremor function belongs
    # to the Ironfall Boots, not Mafesto's own boots.
    "MCD-1071": (
        "\"The Night the Water Burned\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-night-the-water-burned.md), "
        "Sovereign Ghost of the Great Sea Alias Chronicle LXI, wave 21, first "
        "entry in the wave. A detailed naval Trinity combat showcase against "
        "a fireship ambush -- six burning, pitch-packed hulks released on a "
        "timed tide into a narrow strait to trap the convoy The Ledger is "
        "escorting -- combining Mafesto's Kinetic Transfer System "
        "(redirecting a collapsing burning spar off a convoy deck), Obsidian "
        "Malice (severing two staged tow-cables to break one converging trap "
        "into six separate, survivable problems), Mafesto's own built-in helm "
        "overlay (MCD-289 locks Blueprint Eye as surfaced through Mafesto's "
        "HUD in this Rebellion-era window, rendering six drift vectors clean "
        "through smoke and glare faster than unaided sight could track them), "
        "Mafesto's own sealed plating (holding smoke out of Kanja's lungs "
        "through the boarding), a stamp through Mafesto's armored boots "
        "(downing two boarders exploiting the chaos), and Onyx of Oblivion's "
        "Whisper of Shadows and Soulbound Edge (boarding the nearest hulk "
        "through smoke to cut its lashed tiller and haul it off heading by "
        "hand). The convoy survives scorched but whole, no lives lost either "
        "side; the fireships' attackers are deliberately left unidentified, a "
        "loose thread rather than resolved here. Not a territory Chronicle. "
        "Corrected Batch 327, 2026-10-02: removed the Sovereign Eyes, Breath "
        "Collar, and Ironfall Boots (ARS-350/351/353), all Long-Mask-era gear "
        "that cannot appear alongside the still-live Trinity in this "
        "Rebellion-era entry, replaced with Mafesto's own built-in "
        "HUD/armor/boots."
    ),
    # E7 -- MCD-1038: tension-reading is Iron Bastard doctrine (Kanja's own
    # skill), not a function of Mafesto's Kinetic Transfer System.
    "MCD-1038": (
        "\"The Ship They Meant to Sink\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-ship-they-meant-to-sink.md), "
        "Sovereign Ghost of the Great Sea Alias Chronicle LVIII, wave 20. A "
        "detailed naval Trinity combat showcase with a new objective for this "
        "alias -- stopping a panicked Trust cordon from scuttling a "
        "becalmed, fever-stricken merchant hauler under standing quarantine "
        "regulation, rather than defeating raiders, hunters, or slavers. "
        "Kanja reads the cordon's rigging tension ahead of the fire order, "
        "Obsidian Malice disables two mounted cannons without harming their "
        "gunners, and Onyx of Oblivion's Whisper of Shadows, Cadence Ruin, "
        "and Veil Piercer break a boarding-repulsion line and read the third "
        "captain's hesitation clean, ending the engagement with no deaths on "
        "either side. Efa Gol organizes a genuine eleven-day quarantine with "
        "volunteer fever-resistant crew rather than a rescue; sixty-one of a "
        "hundred and four aboard survive, and Garren Hask logs every name, "
        "living and dead. Extends the coercion-versus-enmity distinction "
        "(MCD-542) into institutional panic rather than conscription. No new "
        "named characters. First entry in the twentieth wave."
    ),
    # E8 -- MCD-1244: Onyx is vaulted at Karkosa during the Long Mask (L9 seal),
    # not carried sealed on Kanja's person.
    "MCD-1244": (
        "\"The Duel He Didn't Need Onyx For\" (full narrative text at "
        "docs/lords-of-cian/chronicles/the-duel-he-didnt-need-onyx-for.md), "
        "The Scourge Alias Chronicle LXXIX, wave 27, first entry. Age 215, V4 "
        "gear. A near-miss discipline entry distinct from MCD-810's gear "
        "failure: a bodyguard trained specifically to counter Onyx of "
        "Oblivion's known techniques nearly wins an extended forty-minute "
        "duel, and the temptation to go back for Onyx arises purely "
        "internally under pressure; the seal holds by choice, and plain "
        "Rexmar Machete swordsmanship and endurance -- the same craft "
        "underlying the whole legend, already present (if less refined) when "
        "it freed two hundred and eleven captives off a slaver galleon "
        "decades earlier (`MCD-381`) -- wins instead. No new named "
        "characters."
    ),
}

# ---------------------------------------------------------------------------
# E1 -- batch-citation renumbering: "Corrected Batch 321" -> the real batch
# number for that alias track. Applied as a targeted substring replace (not
# hand-retyped) to avoid transcription error across ~25 long statements.
# MCD-1137 and MCD-1071 are included here too (on top of their AMENDMENTS
# content fixes above, which still carry the original "Corrected Batch 321"
# text for this loop to find and renumber).
# ---------------------------------------------------------------------------
BATCH_RENUMBER = {
    # Trench Monarch -> 323
    "MCD-944": 323, "MCD-1029": 323, "MCD-1062": 323, "MCD-1123": 323,
    "MCD-1127": 323, "MCD-1129": 323, "MCD-1137": 323, "MCD-1147": 323,
    # Crow King -> 324
    "MCD-1261": 324, "MCD-1262": 324,
    # Iron Bastard -> 326
    "MCD-1047": 326, "MCD-1080": 326, "MCD-1284": 326, "MCD-1287": 326,
    "MCD-1290": 326, "MCD-1293": 326, "MCD-1296": 326, "MCD-1301": 326,
    "MCD-1302": 326,
    # Sovereign Ghost -> 327 (MCD-1071 is renumbered directly within its own
    # AMENDMENTS content fix above, since that text already needed editing
    # for E7; only MCD-1211 needs the renumber-only loop)
    "MCD-1211": 327,
    # Lord of Embers -> 330
    "MCD-969": 330, "MCD-1050": 330, "MCD-1052": 330, "MCD-1084": 330,
    "MCD-1322": 330, "MCD-1328": 330, "MCD-1330": 330, "MCD-1333": 330,
    "MCD-1334": 330,
}

# ---------------------------------------------------------------------------
# E2 -- category-field normalization.
# ---------------------------------------------------------------------------
CATEGORY_FIXES = {
    "MCD-1024": ("territory-chronicle", "phase2-territory-chronicle"),
    "MCD-1093": ("territory-chronicle", "phase2-territory-chronicle"),
}


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}

    # --- content amendments ---
    amended = []
    for rid, new_statement in AMENDMENTS.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        rules_by_id[rid]["statement"] = new_statement
        amended.append(rid)

    # --- batch-citation renumbering (separate, scriptable loop) ---
    renumbered = []
    for rid, correct_batch in BATCH_RENUMBER.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        stmt = rules_by_id[rid]["statement"]
        assert "Batch 321" in stmt, f"{rid}: expected 'Batch 321' not found"
        new_stmt = stmt.replace("Batch 321", f"Batch {correct_batch}")
        assert "Batch 321" not in new_stmt, f"{rid}: 'Batch 321' still present after replace"
        rules_by_id[rid]["statement"] = new_stmt
        renumbered.append(rid)

    # --- category normalization (separate loop) ---
    category_fixed = []
    for rid, (old_cat, new_cat) in CATEGORY_FIXES.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        cur = rules_by_id[rid].get("category")
        assert cur == old_cat, f"{rid}: expected category '{old_cat}', found '{cur}'"
        rules_by_id[rid]["category"] = new_cat
        category_fixed.append(rid)

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs found"

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": 0,
        "note": (
            "Mechanical fixes only from a Fable-model read-only review of "
            "MCD-901 through MCD-1350: amends 19 rule statements (MCD-951 "
            "Undertow/ARS-388 anachronism -> Mar-bloodline tide-sense; "
            "MCD-1215 fourth -> fifth unnamed ship, cross-referencing The "
            "Second Chance/MCD-607; MCD-1241/MCD-1247 Forge-Coat V3 -> V4 gear "
            "at ages 235/180 per ARS-348; MCD-1054/1055/981 Sephtis's 'death' "
            "-> staged withdrawal per MCD-982; MCD-1135 an uncited 'two years' "
            "figure -> 'the cross-district trust built since the Dredge-Line'; "
            "MCD-1137 a self-referential error in its own correction note, "
            "'found Halst and Sok' -> 'found Danne Sok and Maret Vos'; "
            "MCD-1074 ARS-347 -> ARS-348 in a V4-gear citation list; MCD-958 "
            "'Kanja's ageless nature and an original crew member's' -> "
            "'Kanja's long lifespan and a veteran hand's (already forty-five "
            "when he signed on)'; MCD-1311/1314/1326/1329/1332 Mafesto's own "
            "'grounding mechanism/function' -> Kanja's own grounding "
            "conductance (MCD-291) working through Mafesto's Kinetic Transfer "
            "System (ARS-010); MCD-1071 a stomp-tremor wrongly attributed to "
            "Mafesto's own boots -> a stamp through Mafesto's armored boots "
            "(the tremor function belongs to the Ironfall Boots); MCD-1038 "
            "tension-reading wrongly attributed to Mafesto's Kinetic Transfer "
            "System -> Kanja's own Iron Bastard doctrine; MCD-1244 'unseal "
            "Onyx' -> 'go back for Onyx,' since Onyx is vaulted at Karkosa "
            "during the Long Mask, not carried sealed on his person). Also "
            "renumbers a shared placeholder batch citation, 'Corrected Batch "
            "321,' to the real batch number for each alias track across 21 "
            "rules (Trench Monarch -> 323: MCD-944/1029/1062/1123/1127/1129/"
            "1137/1147; Crow King -> 324: MCD-1261/1262; Iron Bastard -> 326: "
            "MCD-1047/1080/1284/1287/1290/1293/1296/1301/1302; Sovereign Ghost "
            "-> 327: MCD-1071/1211; Lord of Embers -> 330: MCD-969/1050/1052/"
            "1084/1322/1328/1330/1333/1334), and normalizes two stray "
            "category fields, MCD-1024/MCD-1093, from 'territory-chronicle' "
            "to the correct 'phase2-territory-chronicle'. Companion prose "
            "fixes applied directly to the matching Chronicle .md files for "
            "MCD-1241/1247 (V3 -> V4 gear) and MCD-1054/1055/981 (Sephtis's "
            "death/decline -> staged withdrawal); MCD-951's own Chronicle file "
            "was checked and found already correct from a prior pass. "
            "Deliberately left untouched: the Garren Hask/Efa Gol/Pell Ostra "
            "cross-track mortality contradiction (MCD-920, 1089, 1090, 1243, "
            "1246, 1252, 1253, 1254, 1255, 1076) and the naval-cannon "
            "tech-level question, both flagged NEEDS ABAD, plus all "
            "ENRICHMENT/optional items from the same review."
        ),
    })

    old_version = float(ledger["ledger_version"])
    ledger["ledger_version"] = str(round(old_version + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(
        f"OK: {len(ledger['rules'])} total rules, {len(ledger['batches_completed'])} "
        f"batches, ledger_version {ledger['ledger_version']}, zero duplicate IDs.\n"
        f"{len(amended)} rule statements amended: {', '.join(amended)}.\n"
        f"{len(renumbered)} batch citations renumbered: {', '.join(renumbered)}.\n"
        f"{len(category_fixed)} category fields normalized: {', '.join(category_fixed)}."
    )


if __name__ == "__main__":
    main()
