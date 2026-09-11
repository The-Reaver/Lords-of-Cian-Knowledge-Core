#!/usr/bin/env python3
"""Batch 231: Trench Monarch Alias Chronicle wave 20 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Trench Monarch Alias Chronicle wave 20 (LVIII-LX), three entries. \"The Lie Told in His Name\" "
    "(MCD-1029) explores a false confession offered out of love rather than malice -- a young clerk "
    "invokes the name to shield his mother, resolved through the established tally-verification "
    "method rather than punishment, a genuinely new register distinct from the alias's prior "
    "malicious impersonators and slander campaigns. \"What the Black Ledger Was Owed\" (MCD-1030) "
    "extends the Black Ledger power into an ongoing social/psychological pressure mechanism -- marked "
    "administratively on a debtor who evades combat entirely rather than closed once on a defeated "
    "opponent, and shown being lifted for the first time -- with detailed solo-blade Onyx choreography "
    "per the standing craft note. \"The First Class at Warehouse Twelve\" (MCD-1031) closes the wave: "
    "the tally method is formalized into a structured multi-district curriculum for the first time, "
    "the origin point for the method's later independence from Kanja's own presence (MCD-950), "
    "reusing already-locked crew (Garren Hask, Efa Gol, Pell Ostra) for continuity depth. No new "
    "named characters introduced across any of the three entries; zero proper-noun collisions found "
    "on check. Abad's approval: \"doorway for all the aliases that remain\" (approval of Bane's "
    "individually-presented wave 20 plus blanket authorization to continue the same wave for the "
    "remaining ten aliases)."
)

NEW_RULES = [
    {
        "id": "MCD-1029",
        "category": "alias-chronicle",
        "statement": (
            "\"The Lie Told in His Name\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-lie-told-in-his-name.md), The Trench Monarch Alias "
            "Chronicle LVIII, wave 20. A seventeen-year-old clerk at a rival tally operation falsely "
            "confesses to skimming wages, invoking the Trench Monarch's name and claiming the crew's "
            "protection, to shield his mother -- the actual, desperate skimmer -- from an owner's "
            "retaliation. Garren Hask's tally records disprove the confession's shift pattern and "
            "trace the true source; Kanja resolves it through the established method, negotiating "
            "restitution through labor rather than punishment once the shortfall is shown to match "
            "exactly the cost of medicine. Tells the boy the impulse to protect his mother needs no "
            "apology, but that the name isn't a coat to be borrowed without asking. First genuinely "
            "sympathetic (rather than malicious or profit-driven) misuse of the reputation shown in "
            "the sub-series. No new named characters -- the clerk, his mother, and the owner are "
            "unnamed. First entry in the Trench Monarch's twentieth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1030",
        "category": "alias-chronicle",
        "statement": (
            "\"What the Black Ledger Was Owed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-black-ledger-was-owed.md), The Trench Monarch "
            "Alias Chronicle LIX, wave 20. Rebellion era, pre-Black-Trench (Onyx of Oblivion solo, "
            "Mafesto dormant and Obsidian Malice undeployed per MCD-232). A chronically evasive owner "
            "who has fled formal tally negotiation across four districts is finally cornered at a "
            "dockside grain warehouse; a detailed solo-blade combat sequence against six hired guards "
            "puts Cadence Ruin and Whisper of Shadows back on the page in named use without restaging "
            "Chronicle II's full five-power sequence (MCD-369). Rather than closing a defeated "
            "opponent's debt after a duel to the death, Onyx's Black Ledger is placed administratively "
            "on the still-living debtor as an open, visible mark of unpaid wages -- extending the "
            "power into an ongoing social/psychological pressure mechanism. Five months later the man "
            "returns unescorted with full repayment ahead of schedule and asks for the mark closed; "
            "Kanja verifies the figures against Hask's ledger and lifts it, the Black Ledger shown "
            "being removed for the first time. No new named characters -- the debtor and his guards "
            "are unnamed. Second entry in the Trench Monarch's twentieth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1031",
        "category": "alias-chronicle",
        "statement": (
            "\"The First Class at Warehouse Twelve\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-first-class-at-warehouse-twelve.md), The Trench "
            "Monarch Alias Chronicle LX, wave 20, closing the wave. Garren Hask, tracking fourteen "
            "separate requests from five districts to learn the tally-verification method directly, "
            "convinces Kanja to formalize it into a structured four-day, multi-district curriculum for "
            "the first time, rather than the one-to-one mentorship (MCD-948) or single institutional "
            "handoff (MCD-644, Tavin Greer to his replacement clerk) previously shown. Held at "
            "Warehouse Twelve for sixteen students from multiple districts: Hask teaches "
            "cross-witnessed documentation discipline, Efa Gol teaches misdirection as a repeatable "
            "sequence rather than instinct, Pell Ostra teaches physical record protection, and Kanja "
            "himself teaches last and least, insisting the method must work whether or not his name is "
            "ever invoked and must be strong enough to survive districts getting it wrong without him "
            "present to correct them. Establishes the deliberate systemization that is the origin "
            "point for the method's later independence from his presence (MCD-950). No new named "
            "characters -- reuses already-locked crew (Garren Hask, Efa Gol, Pell Ostra) for "
            "continuity depth. Closes the Trench Monarch's twentieth wave (with 'The Lie Told in His "
            "Name,' MCD-1029, and 'What the Black Ledger Was Owed,' MCD-1030)."
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
            "batch": 231,
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
