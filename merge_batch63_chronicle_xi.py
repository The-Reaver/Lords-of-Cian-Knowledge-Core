#!/usr/bin/env python3
"""Batch 63: locks Chronicle XI ('What Holds in the Light') as canon --
the third Kanja Chronicle depicting a Phase 2 homage-era comrade's guest
appearance, per the survival/mainline-integration standing decision
(PH2-048). Extends the already-locked Second Century Mark (MCD-260,
age 200) with the new scene; the full narrative text lives at
docs/lords-of-cian/chronicles/chronicle-xi-what-holds-in-the-light.md,
already drafted in full and pasted for Abad's review before this lock."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Chronicle XI ('What Holds in the Light'), chat-drafted 2026-09-05, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/chronicle-xi-what-holds-in-the-light.md."
)

NEW_RULES = [
    {
        "id": "MCD-333",
        "category": "World Mechanics",
        "statement": (
            "Chronicle XI ('What Holds in the Light') is the third Kanja "
            "Chronicle depicting a Phase 2 homage-era comrade's guest "
            "appearance, per the survival/mainline-integration standing "
            "decision (PH2-048). Slots into the already-locked Second "
            "Century Mark (MCD-260, age 200, Long Mask era): during Trust "
            "Governor Maren Tallis's twelve-year truce negotiation, "
            "Yalokona (Yara) arrives unannounced and blocks Tallis's "
            "attempt to append a private, unsigned side-agreement, "
            "forcing all terms to be stated once, aloud, in the light and "
            "witnessed -- her canonical Caucus (any alliance she "
            "personally brokers becomes binding in a way neither side "
            "can secretly break) and Unbought and Unbossed (immune to "
            "being made to comply, stop, or disappear through money, "
            "threat, or force so long as it happens witnessed or on "
            "record) abilities, both shown in effect but never named on "
            "the page. The negotiation resolves exactly as MCD-260 "
            "already records (the twelve-year truce, the Governor's "
            "Shackle named, the 114-year Pi-Awakening countdown set). "
            "She is never named on-page (matching the Chronicle IX/X "
            "precedent) -- she departs before the formal signing, "
            "leaving behind an unidentified ledger filing recording only "
            "that the accord was witnessed, a third unresolved hook "
            "alongside Chronicle IX's carved word and Chronicle X's folk "
            "phrase, for a future Chronicle to draw together once more "
            "homage-era comrades accumulate. Narrated by Onyx of "
            "Oblivion per VB-020/021."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full drafted Chronicle text as sent (a shared file) and then said: "locked"'


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
            "batch": 63,
            "source_doc": (
                "Chronicle XI ('What Holds in the Light') -- the third "
                "Kanja Chronicle written under the survival/mainline-"
                "integration standing decision (PH2-048), depicting "
                "Yalokona's first guest appearance, slotted into the "
                "already-locked Second Century Mark (MCD-260, age 200)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "6.6"
    ledger["last_updated"] = "2026-09-05"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
