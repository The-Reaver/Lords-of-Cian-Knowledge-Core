#!/usr/bin/env python3
"""Batch 111: Lock the Scourge's three-entry Alias Chronicle wave (MCD-380 through MCD-382),
continuing uninterrupted through the remaining alias waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-10, no source document."

BATCH_NOTE = (
    'Abad: "continue uninterrupted until completion this includes test, commit, push to main '
    'origin" (covering all ten remaining alias waves).'
)

NEW_RULES = [
    {
        "id": "MCD-380",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What He Chose to Burn\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-he-chose-to-burn.md), the Scourge Alias "
            "Chronicle I. Rebellion era, the morning after the Ash-Wharf Massacre (MCD-235, age "
            "22). Efa Gol (already-locked crew member, CC-130) finds Kanja still wearing his "
            "ruined, smoke-damaged coat at the harbor's edge; he reflects that unlike his other "
            "Directorate- or crew-given aliases, this persona was neither chosen nor given by "
            "anyone, including himself -- it happened by accident, standing still through his "
            "own detonated stockpile, and he does not yet know what it will end up costing before "
            "it's finished. Dramatizes MCD-235's own stated 'unplanned, emergent' origin directly. "
            "First entry in the Scourge's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-381",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Shape the Smoke Remembers\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-shape-the-smoke-remembers.md), the Scourge Alias "
            "Chronicle II. Long Mask era, Pirate Dawn (ages 48-52, MCD-250), a new naval "
            "engagement distinct from the already-locked Boiling Strait (a different character's "
            "battle). A slaver galleon's crew is disabled and 211 captives freed in a detailed "
            "showcase of the early Scourge loadout: the Forge-Coat V1 (ARS-347) venting Terror-"
            "mode smoke (ARS-354), the Sovereign Eyes V1's unintended predator-eyed glow "
            "(ARS-350), the Ironhand Gauntlets V1 (ARS-352) absorbing and returning a boarding-"
            "axe strike, the Ironfall Boots' impact-sole tremor (ARS-353), and the Rexmar Machete "
            "(ARS-260, not a Trinity relic) winning the captain's duel through plain swordsmanship "
            "-- the freed captives' own later account deliberately contrasts the theatrical "
            "smoke-and-eyes reputation against the mundane skill actually doing the work. No new "
            "named characters. Second entry in the Scourge's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-382",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Signal Honest Ships Learned\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-signal-honest-ships-learned.md), the Scourge "
            "Alias Chronicle III, closing the wave. Long Mask era, Pirate Dawn (ages 48-52). A "
            "merchant captain deliberately signals for the Scourge's protection when a suspicious "
            "Gale Straits patrol closes in the dark; a single vessel holds position a half-mile "
            "off until the patrol withdraws rather than risk its own manifest facing the same "
            "scrutiny. Dramatizes MCD-250's 'recognized and surrendered to on sight without "
            "verification' fact from the opposite angle -- protection extended to honest cargo "
            "rather than only judgment against dishonest. No new named characters. Closes the "
            "Scourge's three-Chronicle wave (with 'What He Chose to Burn,' MCD-380, and 'The "
            "Shape the Smoke Remembers,' MCD-381)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 111,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Scourge's three-entry Alias Chronicle wave (MCD-380 through MCD-382), "
                "the fifth of ten remaining alias waves. " + BATCH_NOTE
            ),
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate IDs after merge"
    print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
          f"Batches: {len(ledger['batches_completed'])}.")


if __name__ == "__main__":
    main()
