#!/usr/bin/env python3
"""Batch 62: locks Chronicle X ('What the Ledger Owes') as canon -- the
second Kanja Chronicle depicting a Phase 2 homage-era comrade's guest
appearance, per the survival/mainline-integration standing decision
(PH2-048). Extends the already-locked Furnace District Strike (MCD-244,
age 21) with the new scene; the full narrative text lives at
docs/lords-of-cian/chronicles/chronicle-x-what-the-ledger-owes.md,
already drafted in full and pasted for Abad's review before this lock."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Chronicle X ('What the Ledger Owes'), chat-drafted 2026-09-05, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/chronicle-x-what-the-ledger-owes.md."
)

NEW_RULES = [
    {
        "id": "MCD-332",
        "category": "World Mechanics",
        "statement": (
            "Chronicle X ('What the Ledger Owes') is the second Kanja "
            "Chronicle depicting a Phase 2 homage-era comrade's guest "
            "appearance, per the survival/mainline-integration standing "
            "decision (PH2-048). Slots into the already-locked Furnace "
            "District Strike (MCD-244, age 21, Rebellion era): during the "
            "four days Kanja spends asking 4,000 smelting-district workers "
            "how much they are owed, Kofi (Umoja) is present among the "
            "hauler-line workers and welds the district's two mutually "
            "distrustful factions (tenders and haulers) into one unified "
            "strike front by standing at the seam between them and "
            "speaking -- his canonical One Fire ability (PH2-040), shown "
            "in effect but never named on the page. The strike proceeds "
            "and resolves exactly as MCD-244 already records (4,000 "
            "workers, Ezio's documented 340%-average debt structure, the "
            "workers striking on their own initiative, eleven days at the "
            "gate, the twenty-first victory without a blow struck). Kofi's "
            "stated age (21) matches Kanja's age at this battle exactly, "
            "a deliberate mirror left as subtext. He is never named "
            "on-page (matching the Chronicle IX/Ogoun Xarey precedent) -- "
            "he departs before the terms are signed, leaving behind a "
            "folk phrase ('same fire, different hands') that outlives the "
            "strike, a second unresolved hook alongside Chronicle IX's "
            "carved word for a future Chronicle to draw together once "
            "more homage-era comrades accumulate. Narrated by Onyx of "
            "Oblivion per VB-020/021."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full drafted Chronicle text as sent (a shared file) and then said: "approved"'


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
            "batch": 62,
            "source_doc": (
                "Chronicle X ('What the Ledger Owes') -- the second Kanja "
                "Chronicle written under the survival/mainline-"
                "integration standing decision (PH2-048), depicting "
                "Kofi's first guest appearance, slotted into the "
                "already-locked Furnace District Strike (MCD-244, age "
                "21)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "6.5"
    ledger["last_updated"] = "2026-09-05"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
