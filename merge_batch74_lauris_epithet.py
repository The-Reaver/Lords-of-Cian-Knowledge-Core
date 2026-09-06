#!/usr/bin/env python3
"""Batch 74: Lauris Letitia's epithet and psychology (roadmap Step 4,
part 3/4 -- closes the backlog triage).

Sourced from 04_Lauris_Psychological_Profile.docx ("The Joyful
Weight"), confirmed NOT redundant with prior extractions during the
Step 4 confirm-redundant pass -- every other major character has a
locked epithet, Lauris didn't. The sibling document,
Five_Book_Construction.docx, was confirmed fully redundant with the
already-extracted MRD Five Book Arcs/Complete Structural Outline
(Batches 55-56) in the same pass; no rules drafted from it."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "04_Lauris_Psychological_Profile.docx ('The Joyful Weight', Google "
    "Drive fileId 1jukjjvzgjgkmtfEEUuCn0TBsy5wihnst), roadmap Step 4 "
    "backlog triage confirm-redundant pass, 2026-09-06."
)

NEW_RULES = [
    {
        "id": "CC-134",
        "category": "character-crew",
        "statement": (
            "Lauris Letitia's epithet and psychology: 'She Who is "
            "Crowned with Joy' / 'The Joyful Victor' -- her defining "
            "trait is combat-joy, not bloodlust or arrogance: an "
            "empirical confidence born of a body operating at full "
            "design capacity in Cian's comparatively low gravity "
            "(extends MCD-143/MCD-149's Hexa-Lamellar/Gravimetabolic/"
            "Ironstorm Blood biology). Positioned by the source as the "
            "series' emotional counterweight to the other leads' "
            "burdens: where Kanja carries grief, Ozmund carries doubt, "
            "Ezio carries deception, Anansi carries rage, Valeria "
            "carries perception's burden, and Sephtis carries time, "
            "Lauris carries joy."
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

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 74,
            "source_doc": (
                "Roadmap Step 4 backlog triage, part 3/4 (closes the "
                "triage): Lauris Letitia's epithet/psychology (CC-134), "
                "sourced from 04_Lauris_Psychological_Profile.docx, "
                "confirmed not redundant. Five_Book_Construction.docx, "
                "checked in the same pass, confirmed fully redundant "
                "with MRD Five Book Arcs/Complete Structural Outline "
                "(Batches 55-56) -- no rules drafted from it."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "7.7"
    ledger["last_updated"] = "2026-09-06"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
