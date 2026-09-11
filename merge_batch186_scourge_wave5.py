#!/usr/bin/env python3
"""Batch 186: Lock the Scourge's fifth three-entry Alias Chronicle wave (MCD-543 through MCD-545),
continuing uninterrupted per Abad's authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do a wave through all the aliases. do this continuously, uninterrupted, this includes '
    'rigorous testing, committing, and pushing to origin Main."'
)

NEW_RULES = [
    {
        "id": "MCD-543",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Armada at Dead Reckoning\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-armada-at-dead-reckoning.md), the Scourge Alias "
            "Chronicle XIII, first entry in the fifth wave. Set roughly age 150: a detailed "
            "large-scale fleet battle, eight ships against a twelve-ship Directorate armada near the "
            "shoals of Dead Reckoning, using the full gear system (Forge-Coat, Sovereign Eyes, "
            "Ironhand Gauntlets, Ironfall Boots) and local navigational knowledge to ground three "
            "enemy ships and disable the flagship -- Onyx of Oblivion correctly absent per its L9 "
            "seal. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-544",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Sea Took Anyway\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-sea-took-anyway.md), the Scourge Alias "
            "Chronicle XIV. Set roughly age 160: a cornered slaving captain deliberately scuttles "
            "his own ship rather than surrender it, drowning eleven captives before the Scourge can "
            "reach them despite freeing sixty-one -- the first genuine, unprevented rescue failure "
            "of the alias's run, recorded honestly in Garren Hask's private ledger rather than "
            "smoothed into the legend. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-545",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Grandchildren of the Freed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-grandchildren-of-the-freed.md), the Scourge Alias "
            "Chronicle XV, closing the fifth wave. Set roughly age 200: the Scourge visits, "
            "unrecognized, a settlement founded by Salt Keep survivors (MCD-446) generations "
            "earlier, finding the accurate account preserved intact across generations and "
            "deliberately leaving without revealing his identity. No new named characters. Closes "
            "the Scourge's fifth three-Chronicle wave (with 'The Armada at Dead Reckoning,' "
            "MCD-543, and 'What the Sea Took Anyway,' MCD-544)."
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
            "batch": 186,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Scourge's fifth three-entry Alias Chronicle wave (MCD-543 through "
                "MCD-545). " + BATCH_NOTE
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
