#!/usr/bin/env python3
"""Batch 185: Lock the Sovereign Ghost of the Great Sea's fifth three-entry Alias Chronicle wave
(MCD-540 through MCD-542), continuing uninterrupted per Abad's authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do a wave through all the aliases. do this continuously, uninterrupted, this includes '
    'rigorous testing, committing, and pushing to origin Main."'
)

NEW_RULES = [
    {
        "id": "MCD-540",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Captains Who Chose a Side\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-captains-who-chose-a-side.md), the Sovereign Ghost "
            "of the Great Sea Alias Chronicle XIII, first entry in the fifth wave. A detailed, "
            "large-scale coalition naval battle: three Trust-commissioned captains defect mid-"
            "engagement to fight alongside the ghost fleet against a raiding squadron, their crews "
            "coordinated in real time through Mafesto's reading rather than any shared command "
            "structure, capturing six vessels and saving the merchant convoy. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-541",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Conscripts Who Never Wanted the Fight\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-conscripts-who-never-wanted-the-fight.md), the "
            "Sovereign Ghost of the Great Sea Alias Chronicle XIV. A boarded Directorate warship "
            "turns out to be crewed by coerced coastal-village conscripts rather than willing "
            "combatants; Kanja releases them with safe passage home instead of holding them as "
            "prisoners, distinguishing coercion from enmity even against the fleet's own military "
            "adversaries. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-542",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Callum Breck Remembered of the Water\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-callum-breck-remembered-of-the-water.md), the "
            "Sovereign Ghost of the Great Sea Alias Chronicle XV, closing the fifth wave. Callum "
            "Breck (already locked) shares the previously untold private context behind his "
            "voice-recovery at Ghost Harbor -- months spent silently at the same rail, the sea "
            "itself holding his silence until he no longer needed it -- extending his already-"
            "locked arc (CC-116, MCD-397). No new named characters beyond the already-locked Callum "
            "Breck. Closes the Sovereign Ghost's fifth three-Chronicle wave (with 'The Captains Who "
            "Chose a Side,' MCD-540, and 'The Conscripts Who Never Wanted the Fight,' MCD-541)."
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
            "batch": 185,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Sovereign Ghost of the Great Sea's fifth three-entry Alias Chronicle "
                "wave (MCD-540 through MCD-542). " + BATCH_NOTE
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
