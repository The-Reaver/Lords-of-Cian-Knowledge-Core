#!/usr/bin/env python3
"""Batch 232: Industrial Myth Alias Chronicle wave 20 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Industrial Myth's twentieth wave (three entries: 'The Two Who Both Went First,' "
    "'The Debt He Paid Before Being Asked,' 'The Workshop That Couldn't Afford to Owe'), all strictly "
    "unarmed and non-combat per the alias's standing ethos. Each explores a genuinely new register not "
    "shown in the prior nineteen waves: the worst-off-first discipline creating real, unhealed social "
    "friction between two equally deserving claimants; an administrator's preemptive, possibly "
    "self-interested wage reform tested for durability rather than credibility; and the method's first "
    "survival-paced settlement against a small, sympathetic employer genuinely unable to pay in full "
    "without destroying the jobs the debt exists to protect. No new named characters were introduced -- "
    "every antagonist and claimant is unnamed and one-scene, consistent with the sub-series' established "
    "case-of-the-week pattern. Zero proper-noun collisions to check, since no new names were coined. "
    "Abad's approval: \"doorway for all the aliases that remain\" (approval of Bane's "
    "individually-presented wave 20 plus blanket authorization to continue the same wave for the "
    "remaining ten aliases)."
)

NEW_RULES = [
    {
        "id": "MCD-1032",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Two Who Both Went First\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-two-who-both-went-first.md), The Industrial Myth Alias "
            "Chronicle LVIII, wave 20. The worst-off-first discipline (MCD-371) forces a real, "
            "on-the-spot triage between two equally desperate claimants -- an injured loom-tender and a "
            "debt-inheriting boy -- and the one documented second never fully forgives being ranked "
            "behind the other, even though she agrees the call was right. Establishes that the method's "
            "own founding ranking principle carries a genuine, unhealed social cost the ledger has no "
            "column to record. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1033",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Debt He Paid Before Being Asked\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-debt-he-paid-before-being-asked.md), The Industrial Myth "
            "Alias Chronicle LIX, wave 20. A district administrator raises every wage to fair rates and "
            "issues back pay three days before the crew arrives, and Ezio's instinct to call the case "
            "closed is overridden by a delayed second audit, four months later, testing whether the "
            "reform survives after its likely motive (a Trust supply contract weighed partly on labor "
            "record) has already been settled. The raises hold, and the ledger records the outcome as "
            "genuine without ever resolving the administrator's true intent. First entry to test a "
            "preemptive, possibly self-interested compliance rather than hostility, collusion, or staged "
            "deception. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1034",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Workshop That Couldn't Afford to Owe\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-workshop-that-couldnt-afford-to-owe.md), The Industrial "
            "Myth Alias Chronicle LX, wave 20, closing the wave. A small cabinetmaker's workshop "
            "genuinely owes its three journeymen back wages it cannot pay in full without closing the "
            "shop and costing all three their jobs; unlike prior vertical-debt cases with a culpable "
            "party able to absorb the finding (MCD-927), there is no one above this owner to trace the "
            "debt to. The full amount is recorded exactly as owed, per the method's never-adjust-the-"
            "numbers discipline (MCD-747), but the settlement is the method's first survival-paced "
            "repayment schedule, timed to the workshop's own survival and set by the three journeymen "
            "themselves rather than a fixed timetable. No new named characters. Closes the Industrial "
            "Myth's twentieth wave (with MCD-1032 and MCD-1033)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 3, f"expected 3 new rules, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 232,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-11, no source document",
            "rule_count": len(NEW_RULES),
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs found post-write!"

    print(
        f"OK. Total rules: {len(ledger['rules'])}. "
        f"Ledger version: {ledger['ledger_version']}. "
        f"Batches: {len(ledger['batches_completed'])}."
    )


if __name__ == "__main__":
    main()
