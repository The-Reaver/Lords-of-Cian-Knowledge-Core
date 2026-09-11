#!/usr/bin/env python3
"""Batch 246: The Scourge Alias Chronicle wave 21 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Scourge's twenty-first Alias Chronicle wave (three entries, LXI-LXIII), continuing the "
    "three-per-wave pacing. Three genuinely new registers not covered in any of the prior 60 "
    "entries: the sub-series' first cold/ice-environment combat showcase, dramatizing the Ironhand "
    "Gauntlets' V4 blood-heating feature and an off-label Mend-Line use for hypothermia rather than "
    "its designed bleeding/structural function (MCD-1074, age 268); the sub-series' first complete "
    "tactical retreat with zero captives freed, a genuine tested limit rather than a partial or "
    "eventual success (MCD-1075, age 75, deliberately left unresolved per the project's established "
    "open-thread practice); and the sub-series' first entry to center Pell Ostra (CC-132/133) the "
    "way earlier waves centered Efa Gol and Garren Hask, a precision-craft moral-complexity entry "
    "with no combat at all (MCD-1076, age 235, closing the wave). Gear-version placement was checked "
    "against ARS-344 through ARS-356 before drafting (Ironhand Gauntlets V1 until age 80, V4 from "
    "age 260; Mend-Line V3 from age 200, V4 from age 270) to avoid contradicting the established "
    "evolution tables. Onyx of Oblivion correctly absent per its L9 seal in all three entries, all "
    "set within the 284-year Long Mask (ages 75, 235, 268). No new named characters in any of the "
    "three -- all reused already-locked crew (Efa Gol, Garren Hask, Pell Ostra). Abad's approval: "
    "\"another alias wave of all aliases\"."
)

NEW_RULES = [
    {
        "id": "MCD-1074",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Strait That Froze Early\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-strait-that-froze-early.md), the Scourge Alias "
            "Chronicle LXI, wave 21, first entry. Age 268, V4 gear (Forge-Coat/Smoke "
            "System/Sovereign Eyes/Ironhand Gauntlets all V4, ARS-347/350/352/354), Mend-Line still "
            "V3 (ARS-355, V4 doesn't begin until age 270). The sub-series' first cold/ice-environment "
            "combat showcase: a northern slaving route freezes eleven days early, trapping a convoy "
            "ship in pack ice. Crossing the floes alone, the Ironhand Gauntlets' V4 blood-heating "
            "keeps his grip functional where cold would otherwise cost it; the Ironfall Boots' "
            "impact-sole tremor, built to destabilize standing opponents, incidentally cracks the ice "
            "under a watch post; Mafesto's Kinetic Transfer System redirects a boarding axe's own "
            "swing at close range; Obsidian Malice is deliberately withheld, since a discharge on "
            "hull ice stressed by freezing water risks opening the ship to the sea before the "
            "forty-one captives below can be freed. A hypothermic child is warmed via an off-label "
            "field use of the Mend-Line's sealed reservoirs (ARS-355) against her core rather than a "
            "wound. Efa Gol and Garren Hask (CC-130, CC-115/116) referenced in established roles, not "
            "staged in new action. Onyx of Oblivion correctly absent per its L9 seal. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1075",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wall He Chose Not to Bleed For\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wall-he-chose-not-to-bleed-for.md), the Scourge "
            "Alias Chronicle LXII, wave 21. Age 75, Forge-Coat/Smoke System/Sovereign Eyes V2 "
            "(ARS-347/350/354, the Pirate Dawn era, ages 40-80), Ironhand Gauntlets still V1 "
            "(ARS-352, V2 doesn't begin until age 80). The sub-series' first entry depicting a "
            "complete tactical retreat with zero captives freed -- a fortified island slaving depot's "
            "sheer sea walls, submerged obstruction chains, and rotating three-tower watch coverage "
            "prove costlier to breach than the rescue would be worth that night; a ninety-second "
            "probing assault confirms it, and Kanja calls a clean withdrawal (no one hit, no one left "
            "behind among his own) rather than press an assault he judges will cost more lives than "
            "it saves. Garren Hask logs the outcome as 'withdrawn' rather than a count of the freed, "
            "the first such entry in years of his ledger; Efa Gol's decoy line covers the retreat. "
            "Deliberately left unresolved -- the stronghold is neither named nor later confirmed "
            "taken, matching the project's established practice for genuinely open threads. Efa Gol "
            "and Garren Hask (CC-130, CC-115/116) in established roles. Onyx of Oblivion correctly "
            "absent per its L9 seal. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1076",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Charge She Measured Twice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-charge-she-measured-twice.md), the Scourge Alias "
            "Chronicle LXIII, wave 21, closing the wave. Age 235, gear generation V3 (ARS-348, ages "
            "80-241, prior to the V4 debut already locked at age 241, MCD-811). The sub-series' "
            "first entry to center Pell Ostra (CC-132/133, the crew's demolitions and chemistry "
            "specialist) the way earlier waves centered Efa Gol (MCD-807) and Garren Hask (MCD-414): "
            "a warehouse slated for a breach raid shares its landward wall with an uninvolved "
            "nursery, and Ostra spends four hours mapping the wall's uneven mortar by ear before "
            "splitting her charge into a smaller lead crack and a larger follow-through timed a "
            "half-second behind it, breaching the warehouse cleanly while leaving the nursery wall's "
            "plaster uncracked. Dramatizes her established signature trait (CC-132) of addressing "
            "materials as requests rather than commands directly on the page for the first time in "
            "this sub-series. A moral-complexity/craft entry with no combat at all, resolved entirely "
            "through precision. Closes with a brief exchange comparing her measured-force philosophy "
            "to Kanja's own, and a light generational-transmission beat with a deliberately unnamed "
            "apprentice. Onyx of Oblivion correctly absent per its L9 seal. No new named characters. "
            "Closes the Scourge's twenty-first wave (with 'The Strait That Froze Early,' MCD-1074, "
            "and 'The Wall He Chose Not to Bleed For,' MCD-1075)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 3, f"expected 3 new rules, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 246,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-11, no source document",
            "rule_count": len(NEW_RULES),
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs found post-write!"

    print(
        f"OK. Total rules: {len(ledger['rules'])}. "
        f"Ledger version: {ledger['ledger_version']}. "
        f"Batches: {len(ledger['batches_completed'])}."
    )


if __name__ == "__main__":
    main()
