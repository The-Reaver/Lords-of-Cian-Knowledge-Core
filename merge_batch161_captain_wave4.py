#!/usr/bin/env python3
"""Batch 161: Lock Captain's fourth three-entry Alias Chronicle wave (MCD-506 through MCD-508),
completing a fourth wave for all eleven aliases in this continuous run."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "work on a fourth Alias wave and a third territory entry continuously uninterrupted '
    'this includes testing, committing, pushing to origin Main" -- completes fourth waves for all '
    'eleven aliases (Bane, Trench Monarch, Industrial Myth, Blue-Collar Titan, Sovereign Ghost of '
    'the Great Sea, the Scourge, the Crow King, the Iron Bastard, the Lord of Embers, the Storm '
    'That Walks, and Captain).'
)

NEW_RULES = [
    {
        "id": "MCD-506",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Choice Between Two\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-choice-between-two.md), Captain Alias Chronicle "
            "XIII, first entry in the fourth wave. Two crew elements come under attack "
            "simultaneously, miles apart; Kanja must choose which to save, saving the smaller group "
            "facing certain death while the larger group loses two on its own -- the first genuine "
            "no-clean-answer command dilemma of Captain's run. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-507",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Man Who Was Forced to Betray Them\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-man-who-was-forced-to-betray-them.md), Captain Alias "
            "Chronicle XIV. A trusted crew member has been feeding minor intelligence to a "
            "Directorate handler under coercion (his sister held as leverage); rather than punish "
            "him, Kanja leads a detailed Trinity strike on the handler's safehouse to free the "
            "sister and remove the leverage, keeping the crew member in the crew afterward. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-508",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Name Carried Forward\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-name-carried-forward.md), Captain Alias "
            "Chronicle XV, closing the fourth wave. Garren Hask's grandnephew joins the crew and "
            "asks what the name 'Captain' actually means to inherit rather than simply hear about; "
            "Kanja frames it as a living thing to maintain rather than a finished monument, closing "
            "not only Captain's fourth wave but the full eleven-alias fourth-wave run. No new named "
            "characters. Closes Captain's fourth three-Chronicle wave (with 'The Choice Between "
            "Two,' MCD-506, and 'The Man Who Was Forced to Betray Them,' MCD-507)."
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
            "batch": 161,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks Captain's fourth three-entry Alias Chronicle wave (MCD-506 through MCD-508), "
                "completing a fourth wave for all eleven aliases. " + BATCH_NOTE
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
