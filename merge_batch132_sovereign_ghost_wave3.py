#!/usr/bin/env python3
"""Batch 132: Lock the Sovereign Ghost of the Great Sea's third three-entry Alias Chronicle wave
(MCD-443 through MCD-445), continuing uninterrupted per Abad's "#1 and #2 now" authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "#1 and #2 now and continue uninterrupted until completion this includes test, commit, '
    'push to main origin."'
)

NEW_RULES = [
    {
        "id": "MCD-443",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Task Force Built to Hunt a Ghost\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-task-force-built-to-hunt-a-ghost.md), the Sovereign "
            "Ghost of the Great Sea Alias Chronicle VII, first entry in the third wave. A "
            "Directorate task force of five ironclad hunters built specifically to counter the "
            "already-locked anchor-chain weapon is defeated by Kanja deliberately not repeating "
            "that tactic -- Mafesto's hull-displacement sensing, Obsidian Malice disabling a "
            "rudder assembly, and Onyx of Oblivion's Whisper of Shadows/Cadence Ruin breaking the "
            "hunters' coordinated doctrine -- with Dol Maren (already locked) present in a "
            "supporting role. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-444",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Sails That Weren't His\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-sails-that-werent-his.md), the Sovereign Ghost of "
            "the Great Sea Alias Chronicle VIII. An ordinary privateer deliberately mimics the "
            "ghost fleet's black-sail reputation to cover his own plunder; Kanja tracks him down "
            "and resolves it through forced public confession port by port rather than combat, "
            "protecting the reputation's truth over its fear factor. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-445",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Quartermaster Kept Account Of\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-quartermaster-kept-account-of.md), the "
            "Sovereign Ghost of the Great Sea Alias Chronicle IX, closing the third wave. Garren "
            "Hask (already locked) presents a year-long ledger of every ship the fleet encountered, "
            "revealing a consistent pattern of disabling rather than sinking and rescuing rather "
            "than plundering; Kanja confirms he keeps his own private count and asks Hask to "
            "preserve the true record beneath whatever legend eventually drifts from it. No new "
            "named characters beyond the already-locked Garren Hask. Closes the Sovereign Ghost's "
            "third three-Chronicle wave (with 'The Task Force Built to Hunt a Ghost,' MCD-443, and "
            "'The Sails That Weren't His,' MCD-444)."
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
            "batch": 132,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Sovereign Ghost of the Great Sea's third three-entry Alias Chronicle "
                "wave (MCD-443 through MCD-445). " + BATCH_NOTE
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
