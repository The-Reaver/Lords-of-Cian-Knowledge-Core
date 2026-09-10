#!/usr/bin/env python3
"""Batch 100: Kazi's two lieutenants named (PH2-063, PH2-064) and Kazi Chronicle II (MCD-363)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-10, no source document. Names and details the two "
    "Kazi lieutenants PH2-051 flags but leaves undetailed ('homage to John Watson, Mike Hamlin, "
    "and Ken Cockrel Sr. ... not yet individually named or detailed'), and dramatizes them "
    "directly in Kazi Chronicle II. Full narrative text at "
    "docs/lords-of-cian/chronicles/kazi-chronicle-ii-the-names-beside-his.md."
)

NEW_RULES = [
    {
        "id": "PH2-063",
        "category": "phase2-homage-detroit-supporting-cast",
        "statement": (
            "Kunle, homage to Ken Cockrel Sr., one of Irin's (PH2-051) two founding Kazi "
            "co-organizers. Yoruba, 'home is filled with honor.' A radical defense lawyer who "
            "treats the courtroom itself as a site of struggle, working the plant's legal "
            "retaliation against individual strikers as directly as Irin works the line itself. "
            "First dramatized in Kazi Chronicle II (MCD-363), securing Bakari's release from a "
            "trumped-up charge filed in retaliation for the events of Kazi Chronicle I (MCD-351)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-064",
        "category": "phase2-homage-detroit-supporting-cast",
        "statement": (
            "Kalamu, a composite homage to John Watson and Mike Hamlin (the real newspaper editor "
            "and labor strategist of the League of Revolutionary Black Workers/DRUM), Irin's "
            "(PH2-051) other founding Kazi co-organizer. Swahili, 'pen.' A journalist/organizer "
            "whose printed sheets, distributed by the world's established pre-industrial crier/"
            "pamphlet network (PH2-049, WC-012/WC-013), turn individual legal cases and labor "
            "actions into documented, citywide public accountings. First dramatized in Kazi "
            "Chronicle II (MCD-363), publicizing Bakari's retaliatory prosecution ahead of trial."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-363",
        "category": "phase2-homage-chronicle",
        "statement": (
            "Kazi Chronicle II, \"The Names Beside His\" (full narrative text at "
            "docs/lords-of-cian/chronicles/kazi-chronicle-ii-the-names-beside-his.md), the second "
            "entry in Kazi's own Chronicles, protagonist Irin (PH2-051), not a Kanja Chronicle -- "
            "Kanja appears only as an unnamed guest, present at the jailhouse and helping "
            "distribute printed sheets before dawn, granted no command, intervention, or "
            "resolution credit. Names and dramatizes the two lieutenants PH2-051 already flags: "
            "Kunle (PH2-063) and Kalamu (PH2-064). Eleven days after the events of Kazi Chronicle "
            "I (MCD-351), the plant retaliates against a single striker, Bakari (a new minor named "
            "character), with a trumped-up charge over a torn gate. Kunle mounts his legal defense "
            "while Kalamu publicizes the retaliatory timing to four thousand readers ahead of "
            "trial; the charge does not hold. Irin explicitly reflects that 'The Line Stops' "
            "(PH2-051) has its own stated limits -- it moves men bound into the same chain of "
            "labor but cannot catch a single man isolated in a room with no one watching -- and "
            "that Kunle's and Kalamu's distinct gifts are not a deficiency in his own but a "
            "genuinely different kind of power the movement needs alongside it. Bakari and the "
            "unnamed plant management are deliberately left minor/undetailed. All three new names "
            "(Kunle, Kalamu, Bakari) collision-checked against the full live ledger before "
            "drafting, zero prior hits. Seventh territory overall (after Xaragua, Areito, Guanin, "
            "Uhuru, Aztlan, and Sankofa) to receive a second Chronicle entry, and the first Detroit "
            "territory to do so."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "lock it."'


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
            "batch": 100,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-10, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Kunle (PH2-063) and Kalamu (PH2-064), Kazi's two founding lieutenants PH2-051 "
                "flagged but left undetailed, dramatized directly in Kazi Chronicle II (MCD-363), "
                "'The Names Beside His.' " + BATCH_NOTE
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
