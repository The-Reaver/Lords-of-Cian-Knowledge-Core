#!/usr/bin/env python3
"""Batch 110: Lock the Sovereign Ghost of the Great Sea's three-entry Alias Chronicle wave
(MCD-377 through MCD-379), continuing uninterrupted through the remaining alias waves."""
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
        "id": "MCD-377",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"A Ship That Was Already Gone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/a-ship-that-was-already-gone.md), Sovereign Ghost of "
            "the Great Sea Alias Chronicle I. Rebellion era, weeks after the Siege of the Ghost "
            "Harbor (MCD-235, age 21). A Trust patrol boat's lookout spots The Audit running dark "
            "and low-draft at half a mile; by the time the patrol closes to investigate she is "
            "gone without trace, and the sighting is never officially reported for fear of "
            "reading as incompetence or superstition. Kanja deliberately allows the sighting and "
            "then deliberately vanishes rather than fight, reasoning that a witnessed-then-"
            "unfindable ghost spreads further than an unseen rumor. References Dol Maren's "
            "already-locked shipwright role (CC-121) without restaging it. No new named "
            "characters. First entry in the Sovereign Ghost's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-378",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Chains That Remembered the Anchor\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-chains-that-remembered-the-anchor.md), Sovereign "
            "Ghost Alias Chronicle II. Rebellion era, a new naval engagement distinct from the "
            "Siege of the Ghost Harbor (MCD-235). A convoy escort gunship is disabled at range by "
            "the anchor-chain magnetic-interference weapon (MCD-235, captured Iron Shallows "
            "chain reforged into the housing), seizing every iron fitting aboard; Kanja boards "
            "personally during the paralysis, demonstrating Mafesto's Kinetic Transfer System "
            "absorbing the drop's impact, Onyx's Whisper of Shadows in close multi-attacker "
            "quarters, and Obsidian Malice's stored-charge discharge clearing the deck in one "
            "motion. The gunship surrenders without a hull breach. No new named characters; the "
            "surrendering captain is unnamed and one-scene. Second entry in the Sovereign Ghost's "
            "three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-379",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Lantern Watch Prayed For\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-lantern-watch-prayed-for.md), Sovereign Ghost "
            "Alias Chronicle III, closing the wave. A young Trust supply-vessel lantern watchman, "
            "who never once sights The Audit across an entire season of night watches, learns "
            "from an older hand that the legend now does the ghost's work without her needing to "
            "appear again -- the Ghost Harbor casualty list is real, but every quiet watch since "
            "has been the fear doing the rest on its own. Extends VB-060's presence doctrine to "
            "reputation alone, absent any actual appearance. No new named characters. Closes the "
            "Sovereign Ghost of the Great Sea's three-Chronicle wave (with 'A Ship That Was "
            "Already Gone,' MCD-377, and 'The Chains That Remembered the Anchor,' MCD-378)."
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
            "batch": 110,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Sovereign Ghost of the Great Sea's three-entry Alias Chronicle wave "
                "(MCD-377 through MCD-379), the fourth of ten remaining alias waves. " + BATCH_NOTE
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
