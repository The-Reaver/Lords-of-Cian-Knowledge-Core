#!/usr/bin/env python3
"""Batch 165: Lock Borikén Chronicle III (MCD-512), continuing the territory-Chronicle third-entry
run per Abad's authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "work on a fourth Alias wave and a third territory entry continuously uninterrupted '
    'this includes testing, committing, pushing to origin Main."'
)

NEW_RULES = [
    {
        "id": "MCD-512",
        "category": "phase2-territory-chronicle",
        "statement": (
            "Borikén Chronicle III, \"The Men Who Claimed His Name\" (full narrative text at "
            "docs/lords-of-cian/chronicles/boriken-chronicle-iii-the-men-who-claimed-his-name.md). "
            "Three unconnected impostors exploit 'No Single Point' (PH2-010)'s own ambiguity to run "
            "extortion under Guaní's name; he defeats the scheme through quiet, patient questioning "
            "of the impostors rather than ever revealing himself, deliberately preserving the "
            "mechanic that protects him from real threats. An unnamed Kanja helps brief residents "
            "on the questions to ask, uninvolved otherwise. No new named characters. Third Borikén "
            "territory Chronicle."
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
            "batch": 165,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": "Locks Borikén Chronicle III (MCD-512). " + BATCH_NOTE,
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
