#!/usr/bin/env python3
"""Batch 133: Lock the Scourge's third three-entry Alias Chronicle wave (MCD-446 through MCD-448),
continuing uninterrupted per Abad's "#1 and #2 now" authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "#1 and #2 now and continue uninterrupted until completion this includes test, commit, '
    'push to main origin."'
)

NEW_RULES = [
    {
        "id": "MCD-446",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Siege of the Salt Keep\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-siege-of-the-salt-keep.md), the Scourge Alias "
            "Chronicle VII, first entry in the third wave. Set roughly age 140, mid-Golden-Terror "
            "period: a detailed combat showcase breaching a three-generation fortified slaving "
            "depot using the Forge-Coat V2/Sovereign Eyes, Mafesto's Kinetic Transfer System, "
            "Obsidian Malice's gate-collapsing discharge, and the Ironhand Gauntlets/Ironfall "
            "Boots, freeing 180 captives -- Onyx of Oblivion correctly absent per its established "
            "L9 seal throughout the Long Mask (MCD-413). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-447",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Surrender That Cost No Blood\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-surrender-that-cost-no-blood.md), the Scourge Alias "
            "Chronicle VIII. Set roughly age 165: a slaving captain strikes his colors and opens his "
            "holds before any shot is fired, purely on the reputation's weight, freeing 41 captives "
            "through psychological pressure alone rather than combat, extending the 'the fear only "
            "works if it's true' principle (MCD-431) into this alias's own register. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-448",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Boy Who Didn't Know His Name\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-boy-who-didnt-know-his-name.md), the Scourge Alias "
            "Chronicle IX, closing the third wave. Set roughly age 210: a cabin boy, born on a ship "
            "the Scourge freed decades before his own birth, unknowingly tells the already-drifted "
            "legend back to the anonymous quartermaster who lived it, who gently redirects the boy "
            "toward the people freed rather than the myth itself, deliberately never revealing his "
            "identity. No new named characters. Closes the Scourge's third three-Chronicle wave "
            "(with 'The Siege of the Salt Keep,' MCD-446, and 'The Surrender That Cost No Blood,' "
            "MCD-447)."
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
            "batch": 133,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Scourge's third three-entry Alias Chronicle wave (MCD-446 through "
                "MCD-448). " + BATCH_NOTE
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
