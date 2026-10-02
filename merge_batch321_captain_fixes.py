#!/usr/bin/env python3
"""Batch 321: reconciliation corrections surfaced by a read-only review of the "Captain" Alias
Chronicle track (102 entries), including several post-surrender Trinity anachronisms that Batch 314
missed, a chronology-anchor fix for the Long Mask-era gear system's earliest appearance, a Chronicle
numeral collision resolved by renumbering, pronoun and citation fixes, and several smaller mechanical
errors (leaked rule-ID citations in narrative prose, writers'-room phrasing, a self-contradiction, a
misattributed trait, an invented event contradicting already-locked canon). No new creative facts --
pure reconciliation against already-locked canon, matching the Batch 226/68/320 precedent. Applied
directly to the Chronicle .md files first; this script amends the matching canon-ledger.json rule
statements to keep both in sync. NOT RUN as part of this pass -- prepared for a human/session to run
separately."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Read-only review of the Captain Alias Chronicle track, reconciliation pass, 2026-10-02"

with open(LEDGER_PATH) as f:
    ledger = json.load(f)

rules_by_id = {r["id"]: r for r in ledger["rules"]}

# --- Amend rule statements to match the corrected Chronicle prose ---
AMENDMENTS = {
    # C1: three more post-surrender Trinity entries Batch 314 missed -- MCD-1377 also retitled and
    # the file renamed, since its old title directly named the Kinetic Transfer System.
    "MCD-1377": (
        '"The Beam That Bought Ninety Seconds" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-beam-that-bought-ninety-seconds.md), Captain Alias "
        "Chronicle LXXVII, wave 26. A detailed rescue-engineering showcase with no enemy present: "
        "Kanja's own post-surrender gear (the Forge-Coat and Ironfall Boots working together to "
        "ground a collapsing tenement's structural force into the earth, the Ironhand Gauntlets "
        "bracing the failing joint) is used to hold the structure up rather than deflect an attack, "
        "buying roughly ninety seconds to complete an evacuation -- a genuinely new application of "
        "the gear's established force-grounding mechanic (`ARS-344`/`ARS-349`). No new named "
        "characters. Corrected Batch 321, 2026-10-02 (retitled and the file renamed from \"What the "
        'Kinetic Transfer System Held Up\"): removed a post-surrender Trinity anachronism (Mafesto\'s '
        "Kinetic Transfer System and Obsidian Malice, decades after the Trinity's locked age-30 "
        "surrender, `MCD-246`) and a false claim that Mafesto was built to save one man's life at the "
        "Black Trench (Mafesto was bonded roughly two years before the Black Trench, per "
        "`MCD-232`/`ARS-342`); also corrects Corren Halst's pronoun to he/him per `CC-158`."
    ),
    "MCD-1421": (
        '"What the Second Generation Held" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-second-generation-held.md), Captain Alias Chronicle "
        "XCI, wave 31. A detailed combat showcase, fought with Kanja's own post-surrender gear, "
        "defending a grain depot from opportunist raiders in which Mira (`MCD-1370`/`1371`/`1372`), "
        "now twenty, takes an active operational role for the first time -- flagging a structural "
        "collapse risk in time for the Forge-Coat and Ironfall Boots to redirect it -- rather than "
        "only a council or memorial-wall function. Efa Gol, Corren Halst, and Pell Ostra reused. No "
        "new named characters. First entry, wave 31. Corrected Batch 321, 2026-10-02: removed a "
        "post-surrender Trinity anachronism (Mafesto's Kinetic Transfer System, Obsidian Malice, "
        "Onyx of Oblivion, `MCD-246`) and two leaked inline rule-ID citations from the narrative "
        "prose."
    ),
    # C3 + E4: MCD-1515's impossible "two hundred years of trained swordsmanship" and a wrong
    # cross-reference for Callum Breck's shore-watch craft.
    "MCD-1515": (
        '"The Watch Callum Breck Called" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-watch-callum-breck-called.md), Captain Alias Chronicle "
        "XCV, wave 32. A detailed Long Mask-era gear combat showcase (the Forge-Coat and Ironfall "
        "Boots redirecting a volley's collected force, the Ironhand Gauntlets collapsing loose scree "
        "through leverage rather than any discharge, and the Rexmar Machete wielded through a "
        "lifetime of trained swordsmanship and Kanja's own instinctive Rexmar-Mar tactical sense for "
        "ground and load) defending a resettlement convoy, built around a genuine first for the "
        "sub-series -- Kanja fighting under another crew member's tactical command as the "
        "newly-seated chair. Extends Callum Breck's silent-signal shore-watch craft (`MCD-1378`) "
        "from a naval into a land-defense application, directly testing the private fear his own "
        "silence arc (`CC-119`) still carries. All eleven raiders taken alive. No new named "
        "characters. Second entry, wave 32. Corrected, Batch 314, 2026-09-28: an earlier draft "
        "mistakenly staged this as a full-Trinity showcase, despite this Chronicle's placement well "
        "within the 284-year Long Mask era, after Kanja's already-locked age-30 surrender of the "
        "Trinity to its sealed vault (`MCD-246`); replaced with his correct Long-Mask-era kit (the "
        "seven-piece post-Mafesto gear system, `ARS-344` through `ARS-356`, plus the Rexmar Machete "
        "and his own instinctive Rexmar-Mar tactical sense). Corrected Batch 321, 2026-10-02: fixed "
        'an impossible "two hundred years of trained swordsmanship" claim and a wrong citation '
        "(`MCD-1099` corrected to `MCD-1378`)."
    ),
    # E1: the two ledger statements that were never updated for Corren Halst's he/him pronoun.
    "MCD-1514": (
        '"The Three Years That Ran Out" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-three-years-that-ran-out.md), Captain Alias Chronicle "
        "XCIV, wave 32. The sub-series' first real test of the rotating council-chair structure "
        "(`MCD-1380`): Corren Halst's three-year term reaches its actual end and he declines a "
        "second term on principle, and the council chooses Callum Breck as the second chair-holder, "
        "tying his acceptance to his own already-locked 'Captain' origin (`MCD-397`) and Trench "
        "Monarch naming (`CC-118`). No new named characters. First entry, wave 32. Corrected Batch "
        "321, 2026-10-02: Corren Halst's pronoun fixed to he/him throughout per `CC-158`; Efa Gol's "
        '"thirty years perfecting the discipline" softened to "the better part of twenty years."'
    ),
    "MCD-1379": (
        '"Five Years, As Promised" (full narrative text at '
        "docs/lords-of-cian/chronicles/five-years-as-promised.md), Captain Alias Chronicle LXXIX, "
        "wave 27. The direct, on-schedule payoff to Corren Halst's five-year promise (`MCD-1090`): "
        "Kanja asks him the succession question again, and he argues the question itself was wrong "
        "-- pointing to the self-sufficiency this run's own prior waves demonstrated as evidence the "
        "crew has been training itself not to need any single successor. No new named characters. "
        "First entry, wave 27. Corrected Batch 321, 2026-10-02: Corren Halst's pronoun fixed to "
        "he/him throughout per `CC-158`."
    ),
    # E4: a wrong CC- citation for Tam Sullen (Efa Gol's pair-partner).
    "MCD-1372": (
        '"The Wall at Pier Nine" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-wall-at-pier-nine.md), Captain Alias Chronicle LXXII, "
        "wave 24, closing the wave. Mira's own answer breaks the council's deadlock: a new standing "
        "memorial wall is built at Pier Nine's seawall, open to civilian and crew names alike, "
        "Joran's name carved first by Mira's own hand, with Tam Sullen's name (Efa Gol's Black "
        "Trench-era pair-partner, `CC-131`) added retroactively as its founding-era link, kept "
        "distinct from the separately-established unnamed rigger of `MCD-998`. No new proper nouns. "
        "Closes wave 24. Corrected Batch 321, 2026-10-02: fixed a wrong citation (`CC-130` corrected "
        "to `CC-131`)."
    ),
    # E10: the Sovereign Eyes' perception function reworded from its amber "glow" to its overlay.
    "MCD-1521": (
        '"What They Tried to Erase From the Wall" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-they-tried-to-erase-from-the-wall.md), Captain Alias "
        "Chronicle CI, wave 34. A detailed Long Mask-era gear combat showcase (the Sovereign Eyes' "
        "overlay and Kanja's own instinctive Rexmar-Mar tactical sense finding the attackers first; "
        "the Forge-Coat and Ironfall Boots redirecting a detonation's full force; the Ironhand "
        "Gauntlets breaking the second team's footing through leverage rather than any discharge; "
        "and the flat of the Rexmar Machete, wielded through trained swordsmanship alone, putting "
        "the last two down disarmed) defending the Pier Nine memorial wall (`MCD-1372`) itself from "
        "an attack by unreconciled Trust holdouts aimed at erasing the crew's history rather than "
        "harming its people -- a genuinely new stake for this alias's combat register. All six "
        "attackers taken alive. Mira and Callum Breck (as chair) reused. No new named characters. "
        "Second entry, wave 34. Corrected, Batch 314, 2026-09-28: an earlier draft mistakenly staged "
        "this as a full-Trinity showcase, despite this Chronicle's placement well within the "
        "284-year Long Mask era, after Kanja's already-locked age-30 surrender of the Trinity to its "
        "sealed vault (`MCD-246`); replaced with his correct Long-Mask-era kit (the seven-piece "
        "post-Mafesto gear system, `ARS-344` through `ARS-356`, plus the Rexmar Machete and his own "
        "instinctive Rexmar-Mar tactical sense). Corrected Batch 321, 2026-10-02: reworded the "
        'Sovereign Eyes\' perception function from its amber "glow" (a fear-response signal others '
        "see, per `ARS-350`) to its overlay."
    ),
    "MCD-1374": (
        '"The Boarding in the Blind Dark" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-boarding-in-the-blind-dark.md), Captain Alias Chronicle "
        "LXXIV, wave 25. A detailed Long Mask-era gear boarding-action combat showcase (the "
        "Sovereign Eyes' overlay, the Forge-Coat and Ironfall Boots, the Ironhand Gauntlets, the "
        "Rexmar Machete, and Kanja's own instinctive Rexmar-Mar tactical sense) fought in total "
        "darkness during a moonless storm, the sub-series' first blind-dark engagement for this "
        "alias, with Efa Gol coordinating the operation by sound-count alone. Frees forty-one "
        "captives from a slaver vessel. No new named characters. Corrected, Batch 314, 2026-09-28: "
        "an earlier draft mistakenly staged this as a full-Trinity showcase, despite this "
        "Chronicle's placement well within the 284-year Long Mask era, after Kanja's already-locked "
        "age-30 surrender of the Trinity to its sealed vault (`MCD-246`); replaced with his correct "
        "Long-Mask-era kit (the seven-piece post-Mafesto gear system, `ARS-344` through `ARS-356`, "
        "plus the Rexmar Machete and his own instinctive Rexmar-Mar tactical sense). Corrected Batch "
        "321, 2026-10-02: fixed a misattributed cross-reference (this is the Storm That Walks "
        "alias's own total-darkness precedent, `MCD-426`, \"The Dark Water Ambush\" -- not to be "
        'confused with the Crow King\'s unrelated "The Vault That Held No Light," `MCD-416`) and '
        'reworded the Sovereign Eyes\' perception function from its amber "glow" to its overlay '
        "(`ARS-350`)."
    ),
    # E5/E6: wave 5's Chronicle numerals XVI/XVII/XVIII duplicated wave 6's own MCD-591/592/593;
    # renumbered to the unused X/XI/XII.
    "MCD-558": (
        '"The Nine Days Nobody Slept" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-nine-days-nobody-slept.md), Captain Alias Chronicle X, "
        "first entry in the fifth wave. A detailed nine-day siege endurance showcase: Kanja "
        "deliberately declines to use his biological advantage for extra rest, moving constantly "
        "among the exhausted crew instead so nobody carries the grinding hardship believing "
        "themselves more alone in it than he is. No new named characters. Renumbered Batch 321, "
        "2026-10-02 (from Chronicle XVI, which duplicated wave 6's own `MCD-591`) -- no other file "
        "cross-references this entry by numeral, only by rule ID, so the renumbering is safe. Also "
        "corrected: Kanja's reduced sleep need reattributed from Mafesto's Kinetic Transfer System "
        "(a force-redirect system, not a biology system) to his own biology."
    ),
    "MCD-559": (
        '"The Enemy Who Asked to Stay" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-enemy-who-asked-to-stay.md), Captain Alias Chronicle XI. "
        "A captured Directorate officer asks to join the crew rather than accept parole or custody; "
        "Kanja extends the same gradual, tested trust-building process given to any unproven "
        "newcomer rather than either blanket suspicion or immediate acceptance. No new named "
        "characters. Renumbered Batch 321, 2026-10-02 (from Chronicle XVII, which duplicated wave "
        "6's own `MCD-592`)."
    ),
    "MCD-560": (
        '"What Efa Gol Saw From the Start" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-efa-gol-saw-from-the-start.md), Captain Alias Chronicle "
        "XII, closing the fifth wave. Efa Gol (already locked, present since Warehouse Twelve) "
        "offers a synthesizing reflection across every alias Kanja has carried, explaining why "
        "'Captain' -- the name his own crew chose rather than one assigned by fear or "
        "classification -- means the most to the people who lived every day of the war alongside "
        "him. No new named characters beyond the already-locked Efa Gol. Closes Captain's fifth "
        "three-Chronicle wave (with 'The Nine Days Nobody Slept,' `MCD-558`, and 'The Enemy Who "
        "Asked to Stay,' `MCD-559`). Renumbered Batch 321, 2026-10-02 (from Chronicle XVIII, which "
        "duplicated wave 6's own `MCD-593`)."
    ),
}

# --- E6: MCD-606 through MCD-620, fifteen rule statements carrying a nonsensical "wave N of ten"
# template leftover, fixed to "wave N of the ten-wave run" ---
WAVE_OF_TEN_FIXES = {
    "MCD-606": 11, "MCD-607": 11, "MCD-608": 11,
    "MCD-609": 12, "MCD-610": 12, "MCD-611": 12,
    "MCD-612": 13, "MCD-613": 13, "MCD-614": 13,
    "MCD-615": 14, "MCD-616": 14, "MCD-617": 14,
    "MCD-618": 15, "MCD-619": 15, "MCD-620": 15,
}

for rid, wave_n in WAVE_OF_TEN_FIXES.items():
    old = f"wave {wave_n} of ten (waves 6-15)"
    new = f"wave {wave_n} of the ten-wave run (waves 6-15)"
    stmt = rules_by_id[rid]["statement"]
    assert old in stmt, f"{rid}: expected substring not found: {old!r}"
    rules_by_id[rid]["statement"] = stmt.replace(old, new)

for rid, new_statement in AMENDMENTS.items():
    rules_by_id[rid]["statement"] = new_statement

# Batch number computed dynamically rather than hardcoded: this script was written against an
# earlier snapshot of the ledger (last batch 320 at the time), but the live ledger may have moved on
# by the time this actually runs. Using the file's own next-available number keeps this safe to run
# later without colliding with batches completed in between.
next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1

ledger["batches_completed"].append({
    "batch": next_batch,
    "date": str(date.today()),
    "source": SOURCE,
    "rule_count": 0,
    "note": (
        "Reconciliation pass applying fixes surfaced by a read-only review of the Captain Alias "
        "Chronicle track (102 entries), including several the Batch 314 gear-correction pass missed. "
        "Fixed in both the Chronicle .md files and these matching ledger rule statements: three more "
        "post-surrender Trinity anachronisms (MCD-1377, retitled/file renamed from 'What the Kinetic "
        "Transfer System Held Up' to 'The Beam That Bought Ninety Seconds,' also removing a false "
        "claim that Mafesto was built to save one man's life at the Black Trench; MCD-1421; MCD-1370) "
        "swapped to Kanja's post-surrender gear; a chronology-anchor fix loosening MCD-1058's "
        '"roughly 8.5 months after that surrender" to "roughly five years," and MCD-1376\'s charter '
        'age from "three years old" to "near enough a decade old," so the seven-piece Long Mask-era '
        "gear system (built ages 33-50) reliably falls inside its own existence window across the "
        "later wave run, incidentally also resolving Mira's age-progression math; an impossible "
        '"two hundred years of trained swordsmanship" claim (MCD-1515, fixed to "a lifetime of '
        'trained swordsmanship"); Garren Hask\'s lifespan softened (MCD-597, "well past his hundredth '
        'year" to "well past eighty," "eighty years" to "thirty years") to fit inside his locked '
        "death window (`MCD-1422`, wave 31); the ledger-keeping lineage corrected from Hask's own "
        "blood descendants to the ledger's taught, non-hereditary successive keepers (MCD-618), "
        "matching `MCD-1384`/`1388`/`1422`/`1423`; an invented six-man Iron Shallows rescue "
        "contradicting the locked zero-casualty account reframed as the tense withdrawal of Efa "
        "Gol's own thirty-person decoy force (MCD-598, MCD-599, per `MCD-233`); two mistaken "
        '"Rebellion era" header tags struck (MCD-508, MCD-463, the latter\'s "decades after '
        'Warehouse Twelve" also corrected to "years"); three "thirty years" claims that overshot the '
        'charter\'s own corrected founding timeline softened to "the better part of twenty years" '
        "(MCD-920, MCD-1384, MCD-1514); nine files' Corren Halst pronoun corrected to he/him per "
        "`CC-158` (MCD-1058, MCD-1090, MCD-1364, MCD-1377, MCD-1381, MCD-1382, MCD-1383, MCD-1386, "
        "MCD-1514), plus two ledger statements that were never updated for this (MCD-1379, "
        "MCD-1514); eight leaked inline rule-ID citations stripped from narrative prose (MCD-1519, "
        "which also fixed a wrong citation, MCD-233 corrected to MCD-232 for the Black Trench; "
        "MCD-1517; MCD-1421; MCD-1422; MCD-1423; MCD-1369; MCD-1365; MCD-1520); four writers'-room "
        'phrasing leaks reworded to in-world language (MCD-1423\'s "wave 30" and "ninety-three '
        'Chronicles"; MCD-1390\'s "ninety Chronicles" and a narrator-aside; MCD-1383\'s "combat '
        "showcase\"; MCD-1385's dialogue quoting a Chronicle title verbatim); six wrong rule-ID/CC-ID "
        "citations fixed (MCD-1515: MCD-1099 to MCD-1378; MCD-1378's note: CC-116 to CC-119; "
        "MCD-1372: CC-130 to CC-131; MCD-1366's note: MCD-368 to MCD-401; MCD-1374: a misattributed "
        '"Vault That Held No Light" cross-reference fixed to the correct Storm That Walks precedent, '
        'MCD-426; MCD-591\'s note: an unresolved "(CC- family)" placeholder fixed to CC-159); a '
        "Chronicle-numeral collision resolved by renumbering wave 5's three entries (MCD-558/559/560) "
        "from the duplicated XVI/XVII/XVIII to the previously-unused X/XI/XII; fifteen rule statements "
        '(MCD-606 through MCD-620) with a nonsensical "wave N of ten" template leftover fixed to '
        '"wave N of the ten-wave run"; a dialogue line (MCD-1004) reworded so Kanja says he recovered '
        'and bonded the Trinity rather than "built" it, and clarified the stated uncertainty is about '
        "the crew's own future rather than the Trinity's; a self-contradiction over whether the "
        "Forge-Coat was sealed for impact on arrival (MCD-1518); Obsidian Malice's recharge cycle "
        'given an impossible "40 seconds" framing removed (MCD-429); "the Trinity\'s resting density" '
        "reattributed to Kanja's own biology (MCD-293) rather than a set of gear (MCD-596); the "
        'Sovereign Eyes\' perception function reworded from its amber "glow" (a fear-response signal '
        "others see, per `ARS-350`) to its overlay in two entries (MCD-1374, MCD-1521); stale tracker "
        "and profile-doc figures corrected (`chronicle-tracks-status.md`'s Captain row, 93 to 102; "
        "`character-profiles/alias-captain.md`'s now-resolved era-span contradiction, its stale claim "
        'that the Batch-314-fixed entries are "full-Trinity combat showcases," its stale claim that '
        'Long Mask gear "appears nowhere in the Captain track," its stale claim that Halst/Sok/Vos '
        "all lack a `CC-` dossier (only Vos still does, after `CC-158`/`CC-159`), a pronoun slip for "
        "Halst's own term, and a false XCII-duplicate claim -- the second hit is a different alias's "
        "entry, `MCD-1486`, cross-referencing this track rather than a real duplicate); and a minor "
        'Garren Hask/Callum Breck timing softening ("years after his own recovered voice" to "not '
        'long after," MCD-606). No new creative facts anywhere in this pass -- pure reconciliation '
        "against already-locked canon, matching the Batch 226/68/320 precedent. NOT RUN as part of "
        "this pass -- prepared for separate execution."
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
