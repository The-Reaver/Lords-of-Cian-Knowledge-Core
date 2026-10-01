#!/usr/bin/env python3
"""Batch 320: reconciliation corrections surfaced by the pilot fable-review pass on the Bane
Alias Chronicle corpus. Mechanical fixes (anachronisms, broken cross-references, misattributed
place names, a category-tag error) plus two pragmatic judgment calls: the Corren Halst/Danne Sok
pronoun split resolved he/him (matching majority usage, the same resolution pattern as Maret
Vos/Dol Maren, Batch 226), and the Kessic Overwatch naming collision resolved by renaming the
second, contradictory installation. No new creative facts -- pure reconciliation against
already-locked canon, matching the Batch 226/68 precedent."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Pilot fable-review pass (Bane Alias Chronicle corpus), reconciliation pass, 2026-10-01"

with open(LEDGER_PATH) as f:
    ledger = json.load(f)

rules_by_id = {r["id"]: r for r in ledger["rules"]}

# --- E1: fix MCD-365's category tag ---
rules_by_id["MCD-365"]["category"] = "kanja-alias-chronicle"

# --- Amend rule statements to match the corrected Chronicle prose ---
AMENDMENTS = {
    "MCD-1391": (
        '"The White That Took the Map Away" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-white-that-took-the-map-away.md), Bane Alias Chronicle "
        "XCI, wave 31. New environmental register -- a whiteout blizzard strips Mafesto's own helm "
        "overlay of its visual advantage, forcing a detailed full-Trinity ambush defense to run "
        "entirely on sound, vibration, and Cadence Ruin. Corrected Batch 320, 2026-10-01: the "
        'original draft used an anachronistic "Sovereign Eyes" reference (that gear is built at age '
        "33, after the Trinity's own age-30 surrender, `ARS-350`, and cannot appear in a scene with "
        "Mafesto, Onyx, and Obsidian Malice all live)."
    ),
    "MCD-1425": (
        '"The Duel That Would Cost Nothing But Him" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-duel-that-would-cost-nothing-but-him.md), Bane Alias "
        "Chronicle XCV, wave 32. First entry to stage an entire engagement with the Trinity excluded "
        "from the terms before it begins rather than merely unused or malfunctioning: a garrison "
        "commander offers formal single combat, plain blade only, to decide an entire siege's "
        "outcome and spare both sides further casualties. Bane accepts on those exact terms -- Onyx "
        "sheathed, Mafesto and Obsidian Malice left with the column -- and wins through patience and "
        "Valen Sinisterblade's own in-Rebellion training as Master-at-Arms (`ARS-344`) rather than "
        "any augmented power, isolating his raw swordsmanship as the sole deciding factor for the "
        "first time since 'The Fight He Couldn't Walk Away From' (MCD-476), which still involved "
        "Onyx. The garrison surrenders whole per the wager's terms. No new named characters -- the "
        "commander is unnamed and one-scene; Corren Halst reused. Corrected Batch 320, 2026-10-01: "
        "the original draft claimed pre-Rebellion training, conflicting with `MCD-311`'s lock that "
        "Kanja's early Rebellion results came from no formal training at all, and cited the wrong "
        "rules (`MCD-291`/`292`, unrelated)."
    ),
    "MCD-1426": (
        '"What the Enemy\'s Own Children Were Owed" (full narrative text at '
        "docs/lords-of-cian/chronicles/what-the-enemys-own-children-were-owed.md), Bane Alias "
        "Chronicle XCVI, wave 32, closing wave 32. First entry to extend 'the fear only works if "
        "it's true' (MCD-431) to the dependents of enemy soldiers rather than to enemies, civilians, "
        "or captives themselves: the same supply-chain sabotage that starved the Kessic Wardline "
        "garrison into surrender (MCD-700) is found to be reaching a garrison town's own military "
        "families, and Bane redirects captured grain to the civilian quarter over Corren Halst's "
        "strategic objection, stating the campaign's target was the garrison's capacity to fight, "
        "not its children's next meal. No new named characters -- the woman and her family are "
        "unnamed; Corren Halst and Danne Sok reused. Closes wave 32. Corrected Batch 320, 2026-10-01: "
        'the original draft misattributed the method to "the Threshbend depot," which fell to nine '
        "days of psychological pressure (`MCD-529`), not starvation."
    ),
    "MCD-432": (
        '"The Full Weight of the Trinity" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-full-weight-of-the-trinity.md), Bane Alias Chronicle "
        "VIII. A detailed single-combat Trinity showcase against the fortified Kessic Overwatch "
        "garrison: Mafesto's Kinetic Transfer System absorbing a six-impact volley into stored "
        "charge, Obsidian Malice discharging at full charge to breach the inner gate in one strike, "
        "and Onyx of Oblivion's Cadence Ruin/Veil Piercer breaking a trained formation into six "
        "isolated fighters, ending with the garrison's surrender and the Trinity's remaining charge "
        "deliberately left unspent. No new named characters. Corrected Batch 320, 2026-10-01: the "
        'original draft specified a "two years of dormant charge" figure for Obsidian Malice that '
        "duplicates the bank already spent at the Black Trench weeks earlier (`ARS-342`); reworded "
        "to a plain full discharge."
    ),
    "MCD-1060": (
        '"The Twelve Miles That Never Stopped Moving" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-twelve-miles-that-never-stopped-moving.md), Bane Alias "
        "Chronicle LXII, wave 21. Rebellion era, within the \"Bane\" window -- not a territory "
        "Chronicle. A detailed full-Trinity combat showcase built around continuous motion rather "
        "than a held position: a six-hundred-refugee convoy, a wounded rearguard, and a pursuing "
        "Directorate cavalry screen force a twelve-mile defense across three changing terrains "
        "without the column's pace ever dropping below a walk. Across open grassland, Mafesto's "
        "Kinetic Transfer System redirects charging cavalry's own momentum sideways through Bane's "
        "footing mid-stride. Through a close pine stand, Onyx of Oblivion's Cadence Ruin folds an "
        "infantry bottleneck attempt apart while Veil Piercer picks two disguised scouts out of a "
        "civilian-looking knot mid-stride. Along a final exposed causeway, Obsidian Malice is "
        "released at full discharge in one arcing blast timed to the pursuing commander's committed "
        "final push, delivered without Bane breaking stride to aim it. The column crosses the "
        "border zone an hour before dusk having never once formed up to fight from fixed ground. "
        "Distinguished from every prior full-Trinity showcase (the fortified-garrison assault, "
        "MCD-432; the multi-day siege, MCD-529; the vertical battlement fight, MCD-703; the "
        "precision-constrained bridge defense, MCD-1026; and the most-intense ravine battle, "
        "MCD-709) by its continuous-motion constraint. No new named characters -- Efa Gol reused; "
        "the pursuing Directorate commander is unnamed and one-scene. Second entry in wave 21. "
        "Corrected Batch 320, 2026-10-01: the original draft specified a duplicate 'two years of "
        "dormant charge' figure for Obsidian Malice; reworded to a plain full discharge."
    ),
}

for rid, new_statement in AMENDMENTS.items():
    rules_by_id[rid]["statement"] = new_statement

# --- C5: new CC- dossiers for Corren Halst and Danne Sok (he/him pronoun reconciliation) ---
NEW_RULES = [
    {
        "id": "CC-158",
        "category": "character-crew",
        "statement": (
            "Corren Halst: he/him (reconciled Batch 320, 2026-10-01, resolving a real pronoun "
            "split -- he/him throughout the Bane Alias Chronicle corpus, but she/her in a number of "
            "Captain and Blue-Collar Titan entries -- in favor of the clear majority usage, the same "
            "resolution pattern as Maret Vos/Dol Maren, Batch 226). One of the three earliest crew "
            "members freed independently before Maw-9, by the Black Trench (age 19, `MCD-234`), "
            "alongside Danne Sok and Maret Vos, forming the nucleus of Kanja's earliest crew before "
            "the mass liberation. Serves as Bane's second and most heavily recurring confidant across "
            "the Bane Alias Chronicle corpus (34+ waves), later taking a rotating dispute-council "
            "chair term under the Captain-era charter (`MCD-1056`/`1380`) and, decades on, a "
            "dock-era leg injury forces a graceful transition from front-line rotation to training "
            "the crew's recruits (`MCD-1459`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-159",
        "category": "character-crew",
        "statement": (
            "Danne Sok: he/him (reconciled Batch 320, 2026-10-01, same resolution as `CC-158`). One "
            "of the three earliest crew members freed independently before Maw-9, by the Black "
            "Trench (age 19, `MCD-234`), alongside Corren Halst and Maret Vos. Runs an "
            "intelligence/verification network referenced extensively across the Bane Alias "
            "Chronicle corpus (e.g. independently confirming a Directorate defector's account over "
            "six weeks, `MCD-1027`). Privately kept, for the whole of the war, a memory of the young "
            "Kanja's hands shaking for an hour after freeing him, before any alias existed (`MCD-530`). "
            "Has a daughter (deliberately kept unnamed) who grows up visiting the crew's ships and "
            "eventually enlists, leading her own first independent operation a generation after "
            "Corren Halst's own comparable growth (`MCD-1002`/`1517`)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

existing_ids = set(rules_by_id.keys())
for r in NEW_RULES:
    assert r["id"] not in existing_ids, f"ID collision: {r['id']}"
    ledger["rules"].append(r)

ledger["batches_completed"].append({
    "batch": 320,
    "date": str(date.today()),
    "source": SOURCE,
    "rule_count": len(NEW_RULES),
    "note": (
        "Reconciliation pass following the pilot fable-review of the Bane Alias Chronicle corpus "
        "(the pilot chunk for a much larger proposed corpus-wide review, which the pilot's own "
        "measured cost -- ~150-170K tokens for one 108-file chunk -- showed would be prohibitively "
        "expensive to run in full without first fixing the chunking methodology). Fixed: a "
        "Trinity-era anachronism (Sovereign Eyes appearing before it's built, MCD-1391), an "
        "Iron-Bastard-doctrine anachronism (MCD-709), Obsidian Malice's 'two years of dormant "
        "charge' claimed redundantly within 18 months of the Black Trench across three entries "
        "(MCD-432, MCD-709, MCD-1060), a mislabeled pre-Rebellion Valen-training claim and wrong "
        "citation (MCD-1425), a misattributed broken-promise settlement name (MCD-939), a "
        "misattributed siege method plus a leaked inline rule-ID citation (MCD-1426), a grief "
        "reference pointed at a battle already locked as zero-casualty (MCD-693), a Dol Maren trait "
        "bled onto Maret Vos (MCD-1061), a mis-tagged category on Bane's actual Chronicle I "
        "(MCD-365), two Voice-Bible characterization labels leaking into narrative prose as quoted "
        "in-world phrases (MCD-706, MCD-1027), a writers'-room 'wave' reference leaking into prose "
        "(MCD-1393), Obsidian Malice described as a bladed/sheathed weapon twice (MCD-1100, "
        "MCD-1113), a misattributed waystation-song callback (MCD-1432), stale Chronicle-count "
        "figures and a stale citation in the Bane profile doc and tracker. Two pragmatic judgment "
        "calls made directly per Abad's 'proceeding a pragmatic order' direction rather than "
        "blocking on separate rulings: (1) Corren Halst and Danne Sok's real pronoun split "
        "(confirmed by corpus-wide grep: he/him in all of Bane, but she/her in 7 Captain/"
        "Blue-Collar Titan entries) resolved he/him for both, the clear majority usage, with new "
        "dossiers locked at CC-158/159 and every affected file swept; (2) the Kessic Overwatch "
        "naming collision (one entry has it taken by a violent full-Trinity assault, MCD-432; "
        "another has the same name surrender cleanly on amnesty terms six weeks earlier, MCD-1102) "
        "resolved by renaming the second, contradictory installation to a distinct garrison, "
        "Hallmere, rather than forcing either account to fit the other -- the same resolution "
        "pattern already used elsewhere in the project for this exact class of collision. Pure "
        "reconciliation throughout -- no new creative facts beyond the two dossiers, matching the "
        "Batch 226/68 precedent."
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
