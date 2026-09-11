#!/usr/bin/env python3
"""Batch 136: Lock the Lord of Embers' third three-entry Alias Chronicle wave (MCD-455 through
MCD-457), continuing uninterrupted per Abad's "#1 and #2 now" authorization."""
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
        "id": "MCD-455",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Convoy That Wouldn't Stop Moving\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-convoy-that-wouldnt-stop-moving.md), the Lord of "
            "Embers Alias Chronicle VII, first entry in the third wave. A detailed Trinity combat "
            "showcase defending the mobile Anvil convoy during mid-transit relocation between "
            "sites, distinct from prior static defenses -- Mafesto, Obsidian Malice, and Onyx of "
            "Oblivion in sequence keep the column moving rather than stopping it, ending with two "
            "apprentices who kept a casting pouring through the ambush rather than abandon it. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-456",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Embargo Couldn't Starve\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-embargo-couldnt-starve.md), the Lord of Embers "
            "Alias Chronicle VIII. A coordinated Directorate ore/coal embargo threatens to starve "
            "the Rolling Foundry Campaign where raids and burning couldn't stop it; Kanja "
            "'metabolizes' the pressure by shifting to salvaged war material and marginal "
            "reopened mine workings, extending the alias's core ethos beyond fire and combat into "
            "economic warfare for the first time. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-457",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Settlement That Kept the Forge Lit\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-settlement-that-kept-the-forge-lit.md), the Lord of "
            "Embers Alias Chronicle IX, closing the third wave. Years after 'An Apprenticeship That "
            "Outlasted the War' (MCD-391), Kanja returns to find the settlement running its own "
            "independent forge, the hinge-truing technique passed through three generations of "
            "apprentices who never met him -- a legacy closer distinct from the wave's combat and "
            "economic-warfare entries. No new named characters. Closes the Lord of Embers' third "
            "three-Chronicle wave (with 'The Convoy That Wouldn't Stop Moving,' MCD-455, and 'What "
            "the Embargo Couldn't Starve,' MCD-456)."
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
            "batch": 136,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Lord of Embers' third three-entry Alias Chronicle wave (MCD-455 "
                "through MCD-457). " + BATCH_NOTE
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
