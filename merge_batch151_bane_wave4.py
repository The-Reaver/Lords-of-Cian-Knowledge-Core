#!/usr/bin/env python3
"""Batch 151: Lock Bane's fourth three-entry Alias Chronicle wave (MCD-476 through MCD-478),
starting a new continuous run per Abad's authorization: "work on a fourth Alias wave and a third
territory entry continuously uninterrupted this includes testing, committing, pushing to origin
Main."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "work on a fourth Alias wave and a third territory entry continuously uninterrupted '
    'this includes testing, committing, pushing to origin Main." Starts a fourth Alias Chronicle '
    'wave, beginning with Bane.'
)

NEW_RULES = [
    {
        "id": "MCD-476",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fight He Couldn't Walk Away From\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fight-he-couldnt-walk-away-from.md), Bane Alias "
            "Chronicle X, first entry in the fourth wave. A Directorate duelist trained outside "
            "conventional doctrine, unafraid of the reputation, forces the first genuine peer-level "
            "single combat of Bane's run -- Onyx of Oblivion's Cadence Ruin finds nothing to "
            "disrupt until the duelist's own improvisational pattern repeats a third time, Veil "
            "Piercer closing a fight neither side's equipment decided. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-477",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Delay Cost\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-delay-cost.md), Bane Alias Chronicle XI. Bane's "
            "cautious extra-day verification before a prisoner liberation -- the same caution that "
            "keeps his reputation honest -- costs two prisoners their lives to an informant embedded "
            "among the guards rather than the captives, a genuine failure Bane does not excuse or "
            "resolve, the first entry to dramatize a real cost of his own decision-making rather "
            "than an external limit. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-478",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Child Who Wasn't Afraid\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-child-who-wasnt-afraid.md), Bane Alias Chronicle "
            "XII, closing the fourth wave. A freed child too young to know the stories tells Bane "
            "plainly that he isn't scary, just tired -- a quiet, humanizing closer stripping the "
            "reputation away entirely and showing VB-060's presence trait by its total absence for "
            "the first time. No new named characters. Closes Bane's fourth three-Chronicle wave "
            "(with 'The Fight He Couldn't Walk Away From,' MCD-476, and 'What the Delay Cost,' "
            "MCD-477)."
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
            "batch": 151,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks Bane's fourth three-entry Alias Chronicle wave (MCD-476 through MCD-478), "
                "the first of a new continuous run covering both a fourth Alias Chronicle wave and "
                "a third territory-Chronicle entry. " + BATCH_NOTE
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
