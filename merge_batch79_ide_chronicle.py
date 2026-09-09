#!/usr/bin/env python3
"""Batch 79: Ide Chronicle I ("What Could Not Be Buried"), the first
entry in Ide's own Chronicle series -- protagonist Ase (PH2-036), Kanja
as unnamed guest, matching the established territory-Chronicle convention
(MCD-334/335/336/339/340/341). Opens Chicago's own run of territory
Chronicles."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Ide Chronicle I ('What Could Not Be Buried'), chat-drafted 2026-09-09, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/ide-chronicle-i-what-could-not-be-buried.md."
)

NEW_RULES = [
    {
        "id": "MCD-342",
        "category": "World Mechanics",
        "statement": (
            "Ide Chronicle I ('What Could Not Be Buried') is the first "
            "entry in Ide's own Chronicle series, per the established "
            "structure (MCD-334/335/336/339/340/341): each Phase 2 "
            "homage-era territory has its own Chronicles, with its own "
            "leader as protagonist and Kanja appearing only as an unnamed "
            "guest. An unnamed local authority (the Magistrate of Ide) "
            "publicly executes an innocent man over a granary theft he did "
            "not commit, deciding guilt within the hour before anyone can "
            "establish the truth. Ase (PH2-036), arriving three streets "
            "away too late to intervene, spends the following days "
            "documenting the dead man's name, every witness, and the "
            "Magistrate's own words with total precision. Ase's signature "
            "ability ('Named and Numbered,' PH2-036) is shown directly in "
            "operation for the first time, honoring both its mechanic and "
            "its stated cost: she has no power to have stopped the "
            "execution (she arrives after, as the ability requires), but "
            "her account, once copied and carried out of Ide by multiple "
            "independent routes before the Magistrate's men can seize the "
            "original plates, becomes permanently impossible to erase or "
            "deny. An unnamed Kanja is present at the execution itself, "
            "equally unable to intervene, and later helps smuggle one copy "
            "of the account out of the city without taking command, "
            "credit, or narrative authorship. No new named characters "
            "introduced. Slots into no existing mainline battle -- "
            "original homage-era material set in Ide itself, and opens "
            "Chicago's own run of territory Chronicles (Umoja already has "
            "one, Umoja Chronicle I, MCD-335; Ide, Kwan, Jibaro, and Uhuru "
            "had none before this entry)."
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
            "batch": 79,
            "source_doc": (
                "Ide Chronicle I ('What Could Not Be Buried', MCD-342) -- "
                "the eighth territory Chronicle overall and Ide's first "
                "(Ase), opening Chicago's own run of territory Chronicles, "
                "continuing the open-ended Phase 2 territory-Chronicle "
                "expansion (alongside Xaragua I/II, Umoja I, Yara I, "
                "Areito I, Guanin I, Boriken I) that was never gated by "
                "the Pre-Book-1 Foundation Complete milestone (Batch 75)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "8.2"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
