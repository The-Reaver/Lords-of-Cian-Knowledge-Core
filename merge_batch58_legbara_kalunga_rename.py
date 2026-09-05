#!/usr/bin/env python3
"""Batch 58: rename the mainline Cian character "Toussaint Louverture"
(the Event Horizon / Master Void-Cusp, the Singularity's Champion) to
"Legbara Kalunga". This surfaced as a naming collision when real-world
Haitian Revolution research was pasted for Phase 2 homage-era
world-building: the Phase 2 naming convention (locked 2026-09-05) holds
that real-world historical figures never appear directly as in-world
names, and Abad asked that this pre-existing character be brought into
alignment with that stricter rule. Amends five already-locked rules in
place (MCD-095, MCD-098, MCD-142, MCD-220, MCD-221, CC-128) and adds one
new rule documenting the rename itself. Epithets (the Event Horizon,
Master Void-Cusp), role, age, and density are all unchanged -- only the
true name changes."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-05, no source document"

OLD_NAME = "Toussaint Louverture"
OLD_SHORT = "Toussaint"
NEW_NAME = "Legbara Kalunga"
NEW_SHORT = "Legbara"


def amend_full_name(rule):
    rule["statement"] = rule["statement"].replace(OLD_NAME, NEW_NAME)


def amend_short_name(rule):
    rule["statement"] = rule["statement"].replace(
        f"{OLD_SHORT}'s", f"{NEW_SHORT}'s"
    ).replace(OLD_SHORT, NEW_SHORT)


AMENDMENTS = {
    "MCD-095": amend_full_name,
    "MCD-098": amend_full_name,
    "MCD-142": amend_short_name,
    "MCD-220": amend_full_name,
    "MCD-221": amend_short_name,
    "CC-128": amend_full_name,
}

NEW_RULES = [
    {
        "id": "CC-129",
        "category": "character-crew",
        "statement": (
            "The Event Horizon / Master Void-Cusp's true name was "
            "renamed from 'Toussaint Louverture' to 'Legbara Kalunga' "
            "to align with the Phase 2 homage-era naming convention "
            "(locked 2026-09-05) that real-world historical figures' "
            "names are never used directly in-world. 'Legbara' derives "
            "from Elegbara/Legba, the Vodou and Yoruba orisha/lwa of "
            "the crossroads who governs the threshold between the "
            "living and spirit worlds; 'Kalunga' is the Kikongo term "
            "for the sacred boundary between the world of the living "
            "and the dead, historically the root of the term for the "
            "Middle Passage crossing point. His epithets (the Event "
            "Horizon, Master Void-Cusp), role as the Singularity's "
            "Champion, age (3,181 years), and resting density (14,000x) "
            "are all unchanged -- only the true name changes."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the name in-conversation: "approved"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    by_id = {r["id"]: r for r in ledger["rules"]}
    for rule_id, amend_fn in AMENDMENTS.items():
        assert rule_id in by_id, f"missing rule to amend: {rule_id}"
        before = by_id[rule_id]["statement"]
        assert OLD_SHORT in before, f"{rule_id} does not mention {OLD_SHORT!r}"
        amend_fn(by_id[rule_id])
        after = by_id[rule_id]["statement"]
        assert OLD_NAME not in after, f"{rule_id} still contains old full name"
        assert after != before, f"{rule_id} unchanged after amendment"

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 58,
            "source_doc": (
                "Original invention -- renamed the mainline character "
                "'Toussaint Louverture' (the Event Horizon / Master "
                "Void-Cusp) to 'Legbara Kalunga' to resolve a naming "
                "collision with real-world Haitian Revolution research "
                "pasted for Phase 2 homage-era work, aligning him with "
                "the stricter Phase 2 naming convention. Amended "
                "MCD-095, MCD-098, MCD-142, MCD-220, MCD-221, and "
                "CC-128 in place; added CC-129 documenting the rename "
                "and its etymology."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "6.1"
    ledger["last_updated"] = "2026-09-05"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")

    remaining = [
        r["id"] for r in ledger["rules"]
        if r["id"] != "CC-129" and (OLD_NAME in r["statement"] or OLD_SHORT in r["statement"])
    ]
    assert not remaining, f"old name still present in: {remaining}"
    print("Verified: no remaining references to the old name outside CC-129's historical note.")


if __name__ == "__main__":
    main()
