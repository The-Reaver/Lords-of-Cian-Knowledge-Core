#!/usr/bin/env python3
"""Batch 120: Lock the Blue-Collar Titan's second three-entry Alias Chronicle wave (MCD-407
through MCD-409), continuing uninterrupted through all remaining alias second waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = 'Abad: "complete all of the Alias drafts continuously uninterrupted."'

NEW_RULES = [
    {
        "id": "MCD-407",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Second Tunnel\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-second-tunnel.md), Blue-Collar Titan Alias "
            "Chronicle IV, first entry in the second wave. A new infrastructure operation in a "
            "different city, distinct from the Sewer War of Killane, where outdated survey maps "
            "nearly derail the crew; Kanja reads a mortar-color shift to identify a later, "
            "unrecorded maintenance passage, recovering three days the operation had nearly lost "
            "-- extending his genuine tradesman competence as a transferable skill rather than a "
            "one-time trick. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-408",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Broke and What He Fixed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-broke-and-what-he-fixed.md), Blue-Collar Titan "
            "Alias Chronicle V. Obsidian Malice's housing cracks under an over-tolerance strike "
            "during an ambush extraction; rather than wait weeks for the Mao forge, Kanja repairs "
            "it himself through genuine smithing technique (controlled reheat, Dead Drakma filing "
            "work, mimicking the original forging sequence), not any Trinity self-regenerative "
            "property. The repair holds through eleven subsequent engagements. No new named "
            "characters; the field armorer is unnamed and one-scene."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-409",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Guild Master's Test\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-guild-masters-test.md), Blue-Collar Titan Alias "
            "Chronicle VI, closing the second wave. A skeptical smiths' guild master, distrustful "
            "of self-styled folk heroes, sets Kanja a genuine journeyman's trade test (a warped "
            "axle housing) before agreeing to cooperate; he passes competently but rushes one "
            "reheat and admits it unprompted, which convinces her of his honesty more than "
            "flawless work would have. The guild's supply routes open within the week. No new "
            "named characters; the guild master is unnamed and one-scene. Closes the Blue-Collar "
            "Titan's second three-Chronicle wave (with 'The Second Tunnel,' MCD-407, and 'What "
            "Broke and What He Fixed,' MCD-408)."
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
            "batch": 120,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Blue-Collar Titan's second three-entry Alias Chronicle wave (MCD-407 "
                "through MCD-409), the fourth of eleven second waves in a continuous run. "
                + BATCH_NOTE
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
