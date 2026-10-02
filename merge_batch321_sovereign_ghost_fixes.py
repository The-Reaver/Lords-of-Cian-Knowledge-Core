#!/usr/bin/env python3
"""Batch 321: reconciliation corrections surfaced by a read-only review of the Sovereign Ghost of
the Great Sea Alias Chronicle corpus (102 entries). This alias is Rebellion-era (age 21, acquired at
Ghost Harbor, MCD-230), running up through the Trinity's own age-30 surrender (MCD-246) -- so full
Trinity use is CORRECT across nearly this entire corpus, not an anachronism. The actual problems were
the reverse: (1) four entries used Book-2-onward Moonvault gifts (the Foldtide, Undertow, the
Lodestone Lens, the Whalebone Tether -- ARS-378/382/383/388) that don't exist for centuries after this
alias's own window; (2) five entries mixed Long-Mask-era post-Mafesto gear (the Sovereign Eyes, Breath
Collar, Forge-Coat, Ironhand/Ironfall -- ARS-344-356) into scenes with the still-live Trinity, an
impossible pairing since that gear is only built after the Trinity's surrender; (3) several entries
implied decades of elapsed fleet history inside a nine-year window (ages 21-30); (4) a cross-track
fleet-naming collision with the Captain alias's own third-ship-naming scene; (5) a low-severity
black-sails/Night-of-Black-Sails (age 48) terminology overlap; plus a set of mechanical citation,
pronoun, and writers'-room-leak errors. All narrative-prose fixes were applied directly to the
Chronicle files themselves (headers, body text, continuity-note footers) -- this script applies only
the resulting rule-statement-level amendments, plus two small amendments to Captain-track rules
(MCD-607, MCD-788) that the cross-track naming-collision fix required, and a reconciling clause added
to MCD-250. No new creative facts, no new rules -- pure reconciliation against already-locked canon,
matching the Batch 226/68/320 precedent.

NOT YET RUN. The batch number (321) and ledger_version bump below assume this is the next merge
applied to canon-ledger.json; if other batches have landed first, renumber `batch` below and re-derive
`ledger_version` from the live file before running."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Read-only review of the Sovereign Ghost of the Great Sea Alias Chronicle corpus (102 entries), "
    "reconciliation pass, 2026-10-02"
)

with open(LEDGER_PATH) as f:
    ledger = json.load(f)

rules_by_id = {r["id"]: r for r in ledger["rules"]}

# --- Amend existing rule statements to match the corrected Chronicle prose ---

# C1: MCD-1462 isn't itself amended here (its own statement carries no gear-name claim), but the
# three gear-era fixes below (MCD-1071/1211/1403) are the C2 statement-level amendments explicitly
# called for. MCD-951/1465/959/1213/958/1215/1219/1228/784/1216/775/1038 all needed only prose-level
# fixes -- their own ledger statements carried no claim that contradicted the corrected prose, so
# they are intentionally left unamended here (verified individually before this script was written).

# C2: MCD-1071 -- remove the Sovereign Eyes/Breath Collar/Ironfall Boots (Long-Mask-era gear),
# replace with Mafesto's own built-in HUD/armor/boots framing.
rules_by_id["MCD-1071"]["statement"] = (
    "\"The Night the Water Burned\" (full narrative text at "
    "docs/lords-of-cian/chronicles/the-night-the-water-burned.md), Sovereign Ghost of the Great Sea "
    "Alias Chronicle LXI, wave 21, first entry in the wave. A detailed naval Trinity combat showcase "
    "against a fireship ambush -- six burning, pitch-packed hulks released on a timed tide into a "
    "narrow strait to trap the convoy The Ledger is escorting -- combining Mafesto's Kinetic Transfer "
    "System (redirecting a collapsing burning spar off a convoy deck), Obsidian Malice (severing two "
    "staged tow-cables to break one converging trap into six separate, survivable problems), "
    "Mafesto's own built-in helm overlay (MCD-289 locks Blueprint Eye as surfaced through Mafesto's "
    "HUD in this Rebellion-era window, rendering six drift vectors clean through smoke and glare "
    "faster than unaided sight could track them), Mafesto's own sealed plating (holding smoke out of "
    "Kanja's lungs through the boarding), a stomp-tremor through Mafesto's own boots (downing two "
    "boarders exploiting the chaos), and Onyx of Oblivion's Whisper of Shadows and Soulbound Edge "
    "(boarding the nearest hulk through smoke to cut its lashed tiller and haul it off heading by "
    "hand). The convoy survives scorched but whole, no lives lost either side; the fireships' "
    "attackers are deliberately left unidentified, a loose thread rather than resolved here. Not a "
    "territory Chronicle. Corrected Batch 321, 2026-10-02: removed the Sovereign Eyes, Breath "
    "Collar, and Ironfall Boots (ARS-350/351/353), all Long-Mask-era gear that cannot appear "
    "alongside the still-live Trinity in this Rebellion-era entry, replaced with Mafesto's own "
    "built-in HUD/armor/boots."
)

# C2: MCD-1211 -- remove "the Sovereign Eyes' overlay," replace with Mafesto's own built-in overlay.
rules_by_id["MCD-1211"]["statement"] = (
    "\"The Squall That Broke the Line\" (full narrative text at "
    "docs/lords-of-cian/chronicles/the-squall-that-broke-the-line.md), Sovereign Ghost of the Great "
    "Sea Alias Chronicle LXXIII, wave 25, first entry in the wave. A detailed battle-intense "
    "full-Trinity combat showcase fought through active storm conditions rather than around them, "
    "against a Trust flotilla commander exploiting the weather -- Mafesto's own built-in overlay, "
    "Mafesto's grounding tested against combined wave and cannon impact, Obsidian Malice's "
    "sound-targeting, and Onyx of Oblivion's Whisper of Shadows and Soulbound Edge disarming rather "
    "than killing the commander. No new named characters. Corrected Batch 321, 2026-10-02: removed "
    "\"the Sovereign Eyes' overlay\" (Long-Mask-era gear that cannot appear alongside the still-live "
    "Trinity in this Rebellion-era entry), replaced with Mafesto's own built-in overlay."
)

# C2: MCD-1403 -- remove "the Sovereign Eyes/Blueprint Eye" and the ungrounded "Ironfall Boots'
# grip-plating" claim, replace with Mafesto's own helm overlay and grounded footing.
rules_by_id["MCD-1403"]["statement"] = (
    "\"The Channel the Ice Sealed Shut\" (full narrative text at "
    "docs/lords-of-cian/chronicles/the-channel-the-ice-sealed-shut.md), Sovereign Ghost of the Great "
    "Sea Alias Chronicle XCI, wave 31, first entry in the wave. A new environmental register: a "
    "detailed full-Trinity combat showcase fought entirely on foot across refrozen pack ice rather "
    "than ship-to-ship, when raiders exploit an early freeze trapping The Receipt and a supply "
    "tender in a sealed channel -- Mafesto's Kinetic Transfer System reading hull vibration through "
    "ice, Mafesto's own helm overlay mapping ice thickness, its own grounded footing, a precision "
    "Obsidian Malice application fracturing ice underfoot, and Onyx of Oblivion's Whisper of Shadows "
    "and Soulbound Edge. Zero deaths on either side. No new named characters. Corrected Batch 321, "
    "2026-10-02: removed the Sovereign Eyes/Blueprint Eye (Long-Mask-era gear that cannot appear "
    "alongside the still-live Trinity in this Rebellion-era entry) and an \"Ironfall Boots' "
    "grip-plating\" claim that was never an established ARS-353 feature anyway, both replaced with "
    "Mafesto's own helm overlay and grounded footing."
)

# C4: MCD-607 (Captain-track) -- reframed from naming the fleet's "third" ship (which collided with
# MCD-788's own, separately locked third-flagship naming) to the fourth vessel, a non-flagship
# transport, The Second Chance -- folded into the Sovereign Ghost track's own fleet count below.
rules_by_id["MCD-607"]["statement"] = (
    "\"The Vote That Named the Third Ship\" (full narrative text at "
    "docs/lords-of-cian/chronicles/the-vote-that-named-the-third-ship.md), Captain Alias Chronicle "
    "XXXII, wave 11 of ten (waves 6-15). Garren Hask, having already named the fleet's first three "
    "flagships himself (The Audit, The Receipt, The Ledger), deliberately hands the naming of the "
    "fleet's fourth vessel -- a non-flagship transport -- to a crew vote instead of keeping it as his "
    "own honor; the crew names her The Second Chance. Corrected Batch 321, 2026-10-02: originally "
    "framed as the fleet's third ship, colliding with the Sovereign Ghost of the Great Sea alias's "
    "own, separately locked third-flagship naming scene (MCD-788, The Ledger); reframed as the "
    "fourth vessel, resolving the cross-track collision. Hask's own line changed from \"I've had my "
    "say twice\" to \"I've had my say three times.\""
)

# C4: MCD-788 (Sovereign Ghost track) -- "every one of them" -> "every flagship" (acknowledging The
# Second Chance, which Hask deliberately did not name himself); elapsed-time reference corrected.
rules_by_id["MCD-788"]["statement"] = (
    "\"The Third Ship Garren Hask Named\" (full narrative text at "
    "docs/lords-of-cian/chronicles/the-third-ship-garren-hask-named.md), Sovereign Ghost of the "
    "Great Sea Alias Chronicle XXXIII, wave 11 of ten (waves 6-15). Garren Hask names the fleet's "
    "third flagship, The Ledger -- distinct from the Captain-track transport The Second Chance "
    "(MCD-607), which the crew voted to name instead, four years into the war (matching The "
    "Receipt's own capture at age 22, MCD-242). Corrected Batch 321, 2026-10-02: Kanja's line "
    "\"You've named every one of them\" corrected to \"You've named every flagship,\" since The "
    "Second Chance was deliberately not named by Hask; \"three years into a war\" corrected to "
    "\"four years\" for consistency with MCD-242."
)

# C5: MCD-250 -- add a reconciling clause (amendment, not a rewrite) distinguishing this Pirate-Dawn
# (age 48) innovation from Rebellion-era "black sails" imagery in the Sovereign Ghost track (ages
# 21-30), per the low-severity item in the review.
rules_by_id["MCD-250"]["statement"] = (
    "Pirate Dawn opens (ages 48-52): the Night of Black Sails (48) is the origin of the Scourge as a "
    "literal commercial/visual brand -- black Dead-Drakma-thread sailcloth flown in the Gale Straits "
    "crescent formation, recognized and surrendered to on sight without verification. The Boiling "
    "Strait (52) is Bloodreaver's first major naval engagement, reverse-venting his Furnace Harness "
    "to raise a steam plume that overheats an enemy Blight projector -- establishing 'fight the "
    "environment, not the enemy' as explicit crew doctrine. Amended Batch 321, 2026-10-02: this "
    "Pirate-Dawn-era innovation is distinct from, and doesn't contradict, any Rebellion-era 'black "
    "sails' imagery in the Sovereign Ghost of the Great Sea alias's own Chronicle corpus (ages "
    "21-30) -- those are ordinary soot/tar-darkened canvas, recognized by reputation alone; this "
    "innovation is specifically the Dead-Drakma-thread sailcloth plus the Gale Straits crescent "
    "formation as a unified visual doctrine, introduced here for the first time and never claimed "
    "earlier."
)

# E6: MCD-1466 -- Wren Calder renumbered from the fleet's "third" hull-reader to its "second,"
# matching MCD-1039's own establishment of Wren as Dol Maren's first apprentice (Dol Maren himself
# is the first hull-reader, Wren the second).
rules_by_id["MCD-1466"]["statement"] = (
    "\"The Hand That Asked to Stay\" (full narrative text at "
    "docs/lords-of-cian/chronicles/the-hand-that-asked-to-stay.md), Sovereign Ghost of the Great Sea "
    "Alias Chronicle C, wave 34, first entry in the wave. A payoff to the previously-unnamed "
    "apprentice from \"What Dol Maren Passed Down\" (`MCD-1039`, wave 20), naming him for the first "
    "time -- Wren Calder, collision-checked clean against the full ledger -- and extending his "
    "training arc into full, permanent, informed-consent crew membership as the fleet's second "
    "hull-reader, a new register distinct from the informal stowaway-fostering practice "
    "(`MCD-1210`) and from `MCD-1461`'s quiet-release register earlier in this run. Dramatizes the "
    "mortality-gap conversation as an explicit condition of joining, consistent with `MCD-958`/"
    "`MCD-1227`. Reuses Dol Maren and Garren Hask. New minor named character: Wren Calder. First "
    "entry in wave 34. Corrected Batch 321, 2026-10-02: renumbered from \"third hull-reader\" to "
    "\"second,\" matching MCD-1039's own establishment of Wren as Dol Maren's first apprentice (Dol "
    "Maren himself being the fleet's first hull-reader)."
)

ledger["batches_completed"].append({
    "batch": 327,
    "date": str(date.today()),
    "source": SOURCE,
    "rule_count": 0,
    "note": (
        "Reconciliation pass following a read-only review of the Sovereign Ghost of the Great Sea "
        "Alias Chronicle corpus (102 entries). This alias is Rebellion-era (age 21, acquired at "
        "Ghost Harbor, MCD-230), running through the Trinity's own age-30 surrender (MCD-246) -- so "
        "full Trinity use is correct across nearly the whole corpus, not an anachronism. Fixed the "
        "reverse problem instead: (C1) four entries (MCD-951, MCD-1462, MCD-1465, plus a line in "
        "MCD-959) used Book-2-onward Moonvault gifts (the Foldtide, Undertow, the Lodestone Lens, "
        "the Whalebone Tether -- ARS-378/382/383/388) centuries before they exist, swapped for "
        "Kanja's own unaided Mar-bloodline tide-sense (MCD-295) and ordinary anchor-chain/hawser "
        "work; the character-profile doc (`docs/lords-of-cian/character-profiles/"
        "alias-sovereign-ghost.md`) was updated to match, including its stale 'era anchoring' "
        "open-question section, now resolved. (C2) Five entries (MCD-1071, MCD-1211, MCD-1220, "
        "MCD-1403, MCD-1460) mixed Long-Mask-era post-Mafesto gear (the Sovereign Eyes, Breath "
        "Collar, Forge-Coat, Ironhand/Ironfall Boots -- ARS-344-356) into scenes with the still-live "
        "Trinity, an impossible pairing since that gear is only built after the Trinity's age-30 "
        "surrender; swapped for Mafesto's own built-in HUD/armor/boots (MCD-289 locks Blueprint Eye "
        "as surfaced through Mafesto's HUD in this era) -- MCD-1460's Ironhand Gauntlets reference "
        "was removed and reworded to Mafesto/Obsidian Malice left aboard, Onyx carried alone, "
        "preserving the duel's own Onyx-powers showcase. Three of these five entries' own rule "
        "statements needed matching amendments (MCD-1071, MCD-1211, MCD-1403); MCD-1220 and "
        "MCD-1460's statements carried no gear-name claim and needed no amendment. (C3) Several "
        "entries implied decades of elapsed fleet history inside this alias's actual nine-year "
        "Rebellion-era window (ages 21-30): MCD-958's old hand reworked to have signed on already "
        "forty-five, his own two marriages and decades of life behind him before ever reaching the "
        "fleet, rather than joining 'nearly the same age' as a 21-year-old Kanja and aging forty "
        "years aboard; MCD-1213 lost a contradictory 'never once held a funeral' claim (MCD-958 "
        "already shows one) and a 'longer than most of this crew has been alive' line; 'a decade' "
        "trimmed to 'years' in MCD-1202, MCD-1207, MCD-1208, MCD-1215, and MCD-1221. (C4) The "
        "cross-track fleet-naming collision with the Captain alias was resolved: the Captain-track's "
        "own 'third ship' vote-naming scene (MCD-607) is reframed as the fleet's fourth vessel, a "
        "non-flagship transport named The Second Chance by crew vote, distinct from Garren Hask's "
        "own third-flagship naming of The Ledger (MCD-788, amended to read 'every flagship' rather "
        "than 'every one of them'); the three Sovereign-Ghost-track entries describing the fleet's "
        "'fourth, still-unnamed hull' (MCD-1215, MCD-1219, MCD-1228) were each renumbered to 'fifth' "
        "to fold The Second Chance in as the genuine fourth hull. (C5) MCD-250 amended with a "
        "reconciling clause distinguishing its age-48 Dead-Drakma-thread-sailcloth/crescent-"
        "formation innovation from ordinary soot-darkened 'black sails' imagery used in this alias's "
        "own Rebellion-era corpus -- compatible, not contradictory. Mechanical fixes (E1-E7), all "
        "applied directly to the Chronicle files' prose/headers/footers, not through this script: a "
        "she/her pronoun for Danne Sok fixed to he/him in MCD-1038 (matching CC-159); three literal "
        "unresolved placeholder citations fixed (MCD-782 -> MCD-779, MCD-794 -> MCD-793, MCD-800 -> "
        "MCD-797); a wrong rule-ID citation fixed in MCD-1038 (MCD-497 -> MCD-790) and CC- citations "
        "corrected throughout for Danne Sok/Corren Halst/Maret Vos/Pell Ostra/Callum Breck (MCD-779, "
        "782, 785, 776, 542, 1404); eight writers'-room leaks (Chronicle-title-as-dialogue, 'wave'/"
        "'run'/'Trinity showcase'/'combat showcase' phrasing) reworded to in-world language across "
        "MCD-795, MCD-1224, MCD-1040, MCD-1039, MCD-1038, MCD-791, MCD-796, MCD-1208, and MCD-1223; "
        "Obsidian Malice's mischaracterization as a cutting/bladed weapon fixed in MCD-775 (reassigned "
        "to Onyx's own blade, ARS-030 locks it as a war club); the Fleet-Marshal's "
        "command-status contradiction between MCD-952 ('a junior officer aboard her') and MCD-957 "
        "('my own judgment') resolved in favor of MCD-957's account (he was the commanding officer); "
        "MCD-1466's apprentice-count contradiction with MCD-1039 resolved (Wren Calder renumbered "
        "'third' -> 'second' hull-reader); a misplaced 'off the Sovereign Coast' location reference "
        "removed from MCD-1216 (that location belongs to the unrelated duel at MCD-799); 'Kothrane "
        "Strait' corrected to the locked 'Kothrane Narrows' in MCD-784 (per MCD-242); and the stale "
        "Chronicle-count tracker figure corrected from 93 to 102 in chronicle-tracks-status.md. This "
        "script applies only the seven rule-statement-level amendments above (MCD-1071, MCD-1211, "
        "MCD-1403, MCD-607, MCD-788, MCD-250, MCD-1466); every other fix was applied directly to the "
        "Chronicle files and the character-profile/tracker docs, outside this script's scope. Pure "
        "reconciliation throughout -- no new creative facts, no new rules, matching the Batch "
        "226/68/320 precedent."
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
