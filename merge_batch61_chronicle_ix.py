#!/usr/bin/env python3
"""Batch 61: locks Chronicle IX ('The Ledger and the Chain') as canon --
the first Kanja Chronicle depicting a Phase 2 homage-era comrade's guest
appearance, per the survival/mainline-integration standing decision
(PH2-048). Extends the already-locked Maw-15 operation (MCD-264, age 165)
with the new scene; the full narrative text lives at
docs/lords-of-cian/chronicles/chronicle-ix-the-ledger-and-the-chain.md,
already drafted in full and pasted for Abad's review before this lock."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Chronicle IX ('The Ledger and the Chain'), chat-drafted 2026-09-05, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/chronicle-ix-the-ledger-and-the-chain.md."
)

NEW_RULES = [
    {
        "id": "MCD-331",
        "category": "World Mechanics",
        "statement": (
            "Chronicle IX ('The Ledger and the Chain') is the first "
            "Kanja Chronicle depicting a Phase 2 homage-era comrade's "
            "guest appearance, per the survival/mainline-integration "
            "standing decision (PH2-048). Slots into the already-locked "
            "Maw-15 operation (MCD-264, age 165): seven days before "
            "Kanja's public-pressure liberation of Maw-15 goes public, "
            "Ogoun Xarey (Xaragua) arrives independently, intending to "
            "burn the facility down immediately. Kanja persuades him to "
            "wait the seven days instead; the liberation succeeds "
            "without violence, 5,100 freed, matching MCD-264's locked "
            "numbers exactly. Ogoun Xarey is never named on-page "
            "(matching the Toussaint Louverture/Legbara Kalunga "
            "backstory-only precedent) -- he departs before the "
            "liberation completes, leaving an untranslated word cut "
            "into the seawall stone as a deliberate, unresolved hook "
            "for future Chronicles once more homage-era comrades "
            "accumulate. Narrated by Onyx of Oblivion per VB-020/021."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full drafted Chronicle text as sent (a shared file) and then said: "lock it"'


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
            "batch": 61,
            "source_doc": (
                "Chronicle IX ('The Ledger and the Chain') -- the first "
                "Kanja Chronicle written under the new survival/mainline-"
                "integration standing decision (PH2-048), depicting Ogoun "
                "Xarey's first guest appearance, slotted into the "
                "already-locked Maw-15 operation (MCD-264, age 165)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "6.4"
    ledger["last_updated"] = "2026-09-05"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
