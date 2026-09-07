#!/usr/bin/env python3
"""Batch 76: Areito Chronicle I ("What Doesn't Land"), the first entry in
Areito's own Chronicle series -- protagonist Kwame Ade (PH2-004), Kanja as
unnamed guest, matching the established territory-Chronicle convention
(MCD-334/335/336)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Areito Chronicle I ('What Doesn't Land'), chat-drafted 2026-09-07, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/areito-chronicle-i-what-doesnt-land.md."
)

NEW_RULES = [
    {
        "id": "MCD-339",
        "category": "World Mechanics",
        "statement": (
            "Areito Chronicle I ('What Doesn't Land') is the first entry in "
            "Areito's own Chronicle series, per the established structure "
            "(MCD-334/335/336): each Phase 2 homage-era territory has its "
            "own Chronicles, with its own leader as protagonist and Kanja "
            "appearing only as an unnamed guest. Kwame Ade (PH2-004), eleven "
            "days after the public break that marks his second reinvention, "
            "sits unguarded in a barbershop back room awaiting retaliation "
            "from three former allies. An unnamed stranger arrives an hour "
            "ahead of them and stands aside, present but uninvolved. When "
            "the three arrive, Kwame Ade's signature ability ('conviction as "
            "armor,' PH2-004) is shown directly in operation: two honest "
            "blows thrown by a man still torn by love and betrayal simply "
            "don't land, a drawn blade is sheathed unused, and the third man "
            "leaves without striking at all -- Kwame Ade never raises a "
            "hand. The stranger departs afterward, leaving one line as a "
            "deliberate forward reference to PH2-004's own stated "
            "vulnerability: the one man who will eventually land a blow on "
            "Kwame Ade is someone who shares his exact certainty, not his "
            "doubt -- left as foreshadowing, unresolved here. No new named "
            "characters introduced. Slots into no existing mainline "
            "battle -- original homage-era material set in Areito itself."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "lock it"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 76,
            "source_doc": (
                "Areito Chronicle I ('What Doesn't Land', MCD-339) -- the "
                "first territory Chronicle for Areito/Kwame Ade, continuing "
                "the open-ended Phase 2 territory-Chronicle expansion "
                "(alongside Xaragua I/II, Umoja I, Yara I) that was never "
                "gated by the Pre-Book-1 Foundation Complete milestone "
                "(Batch 75)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "7.9"
    ledger["last_updated"] = "2026-09-07"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
