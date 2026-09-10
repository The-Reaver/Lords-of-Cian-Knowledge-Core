#!/usr/bin/env python3
"""Batch 109: Lock the Blue-Collar Titan's three-entry Alias Chronicle wave (MCD-374 through
MCD-376), continuing uninterrupted through the remaining alias waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-10, no source document."

BATCH_NOTE = (
    'Abad: "continue uninterrupted until completion this includes test, commit, push to main '
    'origin" (covering all ten remaining alias waves).'
)

NEW_RULES = [
    {
        "id": "MCD-374",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Six-Week Silence\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-six-week-silence.md), Blue-Collar Titan Alias "
            "Chronicle I. Rebellion era, during the Sewer War of Killane (MCD-234, age 20). A "
            "burst clay sewer main draws municipal repair crews directly above the tunnel where "
            "the Southern District's Scrip-Registry copy is being transcribed; Kanja surfaces "
            "alone, diagnoses the pipe failure with genuine tradesman's knowledge, and leaves "
            "before either crewman thinks to question a helpful passerby -- avoiding a security "
            "escalation that a stranger's silent disappearance would have triggered. Establishes "
            "the alias's defining trait as genuine working competence, not reputation alone. No "
            "new named characters. First entry in the Blue-Collar Titan's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-375",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Titan Carries\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-titan-carries.md), Blue-Collar Titan Alias "
            "Chronicle II. Rebellion era, the final night of the Sewer War of Killane (MCD-234, "
            "age 20) -- the Trinity's first extended combined-use showcase since its debut at "
            "the Black Trench (MCD-232). A 90-strong rapid-response detachment nearly catches the "
            "extraction at the surface breach; Kanja holds the line alone for the full forty "
            "minutes the crew needs to clear through, demonstrating Mafesto's Kinetic Transfer "
            "System (ARS-010, corrected per MCD-291 to grounding/conductance) absorbing volley "
            "fire, Obsidian Malice (ARS-030) discharging the gathered kinetic charge in a single "
            "shield-breaking strike, and Onyx of Oblivion's Cadence Ruin and Veil Piercer (ARS-020) "
            "covering the club's 3-5 second recharge window -- three systems handing the fight to "
            "each other in sequence rather than one weapon acting alone. A recovered Trust "
            "after-action report is quoted: 'he does not fight like a man carrying three weapons. "
            "He fights like one weapon that happens to be wearing a man.' No new named characters. "
            "Second entry in the Blue-Collar Titan's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-376",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Titan's Own Hands\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-titans-own-hands.md), Blue-Collar Titan Alias "
            "Chronicle III, closing the wave. Rebellion era, during the Sewer War of Killane "
            "(MCD-234, age 20). A conscripted sixty-one-year-old tunnel engineer is startled to "
            "find Kanja personally setting shoring timber alongside the crew, with genuine, "
            "practiced competence rather than performative labor; Kanja states plainly that his "
            "trade came before his war, and that he'd rather stay the kind of titan who remembers "
            "which of the two still feels like work. Grounds the Blue-Collar Titan's dignity-of-"
            "labor theme (VB-061) in a direct physical scene. No new named characters; the "
            "engineer is unnamed and one-scene. Closes the Blue-Collar Titan's three-Chronicle "
            "wave (with 'The Six-Week Silence,' MCD-374, and 'What the Titan Carries,' MCD-375)."
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
            "batch": 109,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Blue-Collar Titan's three-entry Alias Chronicle wave (MCD-374 through "
                "MCD-376), the third of ten remaining alias waves. " + BATCH_NOTE
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
