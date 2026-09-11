#!/usr/bin/env python3
"""Batch 156: Lock the Scourge's fourth three-entry Alias Chronicle wave (MCD-491 through MCD-493),
continuing uninterrupted per Abad's authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "work on a fourth Alias wave and a third territory entry continuously uninterrupted '
    'this includes testing, committing, pushing to origin Main."'
)

NEW_RULES = [
    {
        "id": "MCD-491",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The One Who Didn't Want Freedom\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-one-who-didnt-want-freedom.md), the Scourge Alias "
            "Chronicle X, first entry in the fourth wave. Set roughly age 110: a worker under a "
            "legitimately consented debt-bondage contract refuses liberation, forcing Kanja to "
            "recognize the difference between coercion and chosen hardship -- the first genuine "
            "moral-complexity entry testing the limits of his established rescue pattern. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-492",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Crew That Challenged the Crescent\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-crew-that-challenged-the-crescent.md), the Scourge "
            "Alias Chronicle XI. Set roughly age 130: a detailed combat showcase against a rival "
            "pirate captain's three-ship squadron assembled specifically to test the Scourge's "
            "dominance over the Gale Straits, sequencing the full gear system (Forge-Coat, "
            "Sovereign Eyes, Ironhand Gauntlets, Ironfall Boots, Smoke System) with Mafesto and "
            "Obsidian Malice -- Onyx of Oblivion correctly absent per its L9 seal. The rival captain "
            "is disarmed and released rather than killed. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-493",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Ends When the Mask Comes Off\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-ends-when-the-mask-comes-off.md), the Scourge Alias "
            "Chronicle XII, closing the fourth wave. Set roughly age 300: an elderly but still-"
            "active Garren Hask and Kanja reflect on the eventual, deliberately unspecified end of "
            "the Scourge persona and what comes after it, extending Hask's already-locked "
            "ghost-fleet/Scourge-era ledger role (MCD-414). No new named characters beyond the "
            "already-locked Garren Hask. Closes the Scourge's fourth three-Chronicle wave (with 'The "
            "One Who Didn't Want Freedom,' MCD-491, and 'The Crew That Challenged the Crescent,' "
            "MCD-492)."
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
            "batch": 156,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Scourge's fourth three-entry Alias Chronicle wave (MCD-491 through "
                "MCD-493). " + BATCH_NOTE
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
