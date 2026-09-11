#!/usr/bin/env python3
"""Batch 159: Lock the Lord of Embers' fourth three-entry Alias Chronicle wave (MCD-500 through
MCD-502), continuing uninterrupted per Abad's authorization."""
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
        "id": "MCD-500",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Didn't Come Back This Time\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-didnt-come-back-this-time.md), the Lord of Embers "
            "Alias Chronicle XIII, first entry in the fourth wave. A third punitive burning finally "
            "outpaces the campaign's stretched salvage and marginal-ore resources; the settlement "
            "forge is not rebuilt and the settlement relocates instead, the first genuine, honestly "
            "acknowledged limit of 'metabolizes punishment' across every prior register. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-501",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Saboteur Among the Apprentices\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-saboteur-among-the-apprentices.md), the Lord of "
            "Embers Alias Chronicle XIV. A detailed detection-and-combat showcase: a Directorate "
            "infiltrator embedded among The Anvil's apprentices plants a slow structural sabotage; "
            "Kanja catches the wrongness in the beam's resonance and patiently traces it to its "
            "source over a full day before confronting and restraining the infiltrator, the threat "
            "coming from within the cohort rather than an external raid. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-502",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Smith They Said Couldn't Be One\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-smith-they-said-couldnt-be-one.md), the Lord of "
            "Embers Alias Chronicle XV, closing the fourth wave. A woman rejected by every "
            "conventional smithing guild purely on grounds of sex finds work judged on merit alone "
            "at The Anvil, extending the forge's meritocratic ethos into active confrontation with "
            "exclusionary guild practice. No new named characters. Closes the Lord of Embers' "
            "fourth three-Chronicle wave (with 'What Didn't Come Back This Time,' MCD-500, and 'The "
            "Saboteur Among the Apprentices,' MCD-501)."
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
            "batch": 159,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Lord of Embers' fourth three-entry Alias Chronicle wave (MCD-500 "
                "through MCD-502). " + BATCH_NOTE
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
