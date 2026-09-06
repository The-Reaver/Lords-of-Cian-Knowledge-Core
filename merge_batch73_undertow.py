#!/usr/bin/env python3
"""Batch 73: Undertow, the last undetailed Captain's-Five treasure
(roadmap Step 4, part 2). Original invention, following the same
Norse-artifact homage pattern established in Batch 54 (Bastion/Svalinn,
King's Mantle/Brisingamen, Lodestone Lens/Heimdall's sight, Whalebone
Tether/Gleipnir)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-06, no source document -- "
    "roadmap Step 4 backlog triage, filling in ARS-340's last named-only "
    "slot, following the source document's own Norse-artifact homage "
    "pattern established in Batch 54."
)

NEW_RULES = [
    {
        "id": "ARS-388",
        "category": "avatar-arsenal",
        "statement": (
            "Undertow (Kanja, Captain's Five): homage to Ran, the Norse "
            "sea-goddess whose net drags drowned sailors down to her "
            "hall. A Living Drakma net-line, deployable by hand or "
            "from the Foldtide, that generates a violent localized "
            "downward current on contact with open water -- capable of "
            "capsizing, grounding, or dragging under an enemy vessel, "
            "or briefly pulling down a Titan-class target caught in "
            "open water. The offensive/naval-denial counterpart to the "
            "Whalebone Tether's restraint function (ARS-383): where "
            "the Tether holds, the Undertow takes."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "confirmed"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 73,
            "source_doc": (
                "Roadmap Step 4 backlog triage, part 2: Undertow "
                "(ARS-388), the last undetailed Captain's-Five "
                "treasure, filling ARS-340's remaining named-only slot."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "7.6"
    ledger["last_updated"] = "2026-09-06"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
