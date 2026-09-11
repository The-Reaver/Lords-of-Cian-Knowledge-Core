#!/usr/bin/env python3
"""Batch 122: Lock the Scourge's second three-entry Alias Chronicle wave (MCD-413 through
MCD-415), continuing uninterrupted through all remaining alias second waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = 'Abad: "complete all of the Alias drafts continuously uninterrupted."'

NEW_RULES = [
    {
        "id": "MCD-413",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Golden Terror Left Behind\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-golden-terror-left-behind.md), the Scourge "
            "Alias Chronicle IV, first entry in the second wave. Long Mask era, the Golden Terror "
            "period (ages 80-180, ARS-348). A young crew member who has spent two years studying "
            "the Scourge's documented fights asks how to replicate his technique; Kanja details "
            "the V3 Forge-Coat's triple-layer composite, the Ironhand Gauntlets' convex knuckle "
            "geometry, the Ironfall Boots' impact soles, and the Sovereign Eyes' accidental "
            "predator-glow, framing the loadout as twenty years of accumulated mistakes rather "
            "than a shortcut technique. Onyx remains sealed at L9 throughout and correctly does "
            "not appear. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-414",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ledger Garren Hask Still Kept\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ledger-garren-hask-still-kept.md), the Scourge "
            "Alias Chronicle V. Long Mask era, decades into the persona. An elderly but still "
            "active Garren Hask (already locked, CC-115/CC-116, his continued longevity consistent "
            "with this world's long baseline lifespans) reveals he has privately kept the crew's "
            "'counter' ledger the entire time, tracking ships saved and captives freed beneath the "
            "legend's visible surface; Kanja reflects that he no longer needs the number confirmed "
            "the way he once did, and wonders aloud whether the Trench Monarch and the Scourge are "
            "still entirely the same person. No new named characters beyond the already-locked "
            "Garren Hask."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-415",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Warlord Who Tested the Crescent\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-warlord-who-tested-the-crescent.md), the Scourge "
            "Alias Chronicle VI, closing the second wave. Pirate Dawn (ages 48-52). A rival "
            "warlord sails into the Gale Straits crescent formation's recognized waters to publicly "
            "test whether the black sails' surrender-on-sight reputation (MCD-250) is still real; "
            "Kanja fights him personally, one exchange, disarming rather than killing, proving the "
            "reputation true in front of every watching crew without needing the warlord's death. "
            "His smuggling operation folds within the season. No new named characters; the warlord "
            "is unnamed and one-scene. Closes the Scourge's second three-Chronicle wave (with "
            "'What the Golden Terror Left Behind,' MCD-413, and 'The Ledger Garren Hask Still "
            "Kept,' MCD-414)."
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
            "batch": 122,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Scourge's second three-entry Alias Chronicle wave (MCD-413 through "
                "MCD-415), the sixth of eleven second waves in a continuous run. " + BATCH_NOTE
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
