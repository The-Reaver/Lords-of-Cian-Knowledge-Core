#!/usr/bin/env python3
"""Batch 190: Lock the Storm That Walks' fifth three-entry Alias Chronicle wave (MCD-555 through
MCD-557), continuing uninterrupted per Abad's authorization."""
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
        "id": "MCD-555",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Storm That Made Enemies Allies\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-storm-that-made-enemies-allies.md), the Storm That "
            "Walks Alias Chronicle XVI, first entry in the fifth wave. A storm larger than any "
            "prior prediction threatens both the rebel fleet and an engaged Directorate squadron "
            "equally; Kanja offers a storm-duration truce, both fleets surviving the night through "
            "genuine cooperation before the Directorate commander withdraws without resuming the "
            "engagement -- the first entry where the storm endangers both sides at once. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-556",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Prediction He Almost Used for Advantage\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-prediction-he-almost-used-for-advantage.md), the "
            "Storm That Walks Alias Chronicle XVII. A single storm prediction could trap a "
            "strategically valuable Directorate supply squadron or warn an unrelated civilian "
            "fishing fleet in the same path; Kanja prioritizes the fishing fleet over available "
            "military advantage, extending the humanitarian-rescue precedent (MCD-459) into an "
            "active choice between competing beneficiaries. No new named characters beyond the "
            "already-locked Sephtis."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-557",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Second Sky-Reader Saw Alone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-second-sky-reader-saw-alone.md), the Storm That "
            "Walks Alias Chronicle XVIII, closing the fifth wave. Sephtis's successor (already "
            "locked, MCD-505) makes her first fully independent, correct storm prediction under "
            "time pressure without his confirmation, fulfilling the institutional-redundancy "
            "purpose of her training. No new named characters beyond the already-locked Sephtis and "
            "his successor. Closes the Storm That Walks' fifth three-Chronicle wave (with 'The "
            "Storm That Made Enemies Allies,' MCD-555, and 'The Prediction He Almost Used for "
            "Advantage,' MCD-556)."
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
            "batch": 190,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Storm That Walks' fifth three-entry Alias Chronicle wave (MCD-555 "
                "through MCD-557). " + BATCH_NOTE
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
