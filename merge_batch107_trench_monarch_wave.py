#!/usr/bin/env python3
"""Batch 107: Lock the Trench Monarch's three-entry Alias Chronicle wave (MCD-368 through
MCD-370), under Abad's blanket authorization to continue uninterrupted through all remaining
alias waves."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-10, no source document."

BATCH_NOTE = (
    'Abad: "continue uninterrupted until completion this includes test, commit, push to main '
    'origin" (covering all ten remaining alias waves, starting with the Trench Monarch).'
)

NEW_RULES = [
    {
        "id": "MCD-368",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Name He Didn't Choose\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-name-he-didnt-choose.md), Trench Monarch Alias "
            "Chronicle I. Rebellion era, weeks after the Dredge-Line Ambush (MCD-231, CC-118), "
            "where Callum Breck unilaterally chalked the 'Trench Monarch' name on a captured "
            "officer's forehead without Kanja choosing or sanctioning it. At a fresh dredge site "
            "the reputation arrives ahead of any actual confrontation: the foreman surrenders "
            "manifests unprompted rather than call in a garrison to protect a debased-Drakma lie. "
            "Kanja reflects to Breck that he doesn't get to reject a name that's already doing the "
            "work a king is supposed to do -- he only gets to make sure it keeps meaning what the "
            "district thinks it means. Dramatizes CC-118's own stated fact directly. No new named "
            "characters beyond the already-locked Callum Breck. First entry in the Trench "
            "Monarch's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-369",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Sword Remembers\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-sword-remembers.md), Trench Monarch Alias "
            "Chronicle II. Rebellion era, between the Dredge-Line Ambush and the Black Trench "
            "(ages 18-19), a solo-blade showcase of Onyx of Oblivion -- Mafesto remains dormant "
            "and Obsidian Malice undeployed until the Trinity's first combined deployment at the "
            "Black Trench (MCD-232), so no armor or war club appears here. A sixteen-strong "
            "Compliance detachment, sent specifically to counter the Dredge-Line tactics, is "
            "defeated in under four minutes, demonstrating all five of Onyx's already-locked "
            "powers (ARS-020) in named sequence: Cadence Ruin (collapsing a coordinated two-man "
            "timing gap), Whisper of Shadows (nullifying a blind-spot attack), Veil Piercer "
            "(opening a structural seam in an interlocked shield wall), Soulbound Edge (deciding "
            "a mutual killing exchange in Kanja's favor by fractions of an angle), and the Black "
            "Ledger (marking the defeated commanding officer's collar as a closed debt rather "
            "than an erasure, consistent with Onyx's locked moral-absolutist voice, VB-021: "
            "'Mercy is earned. Memory is the receipt.'). No new named characters. Second entry in "
            "the Trench Monarch's three-Chronicle wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-370",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ones Who Called Him That First\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ones-who-called-him-that-first.md), Trench "
            "Monarch Alias Chronicle III, closing the wave alongside 'The Name He Didn't Choose' "
            "(MCD-368) and 'What the Sword Remembers' (MCD-369). An old dredge-site tally worker "
            "explains to a new apprentice why the alias's reputation is grounded in exposing "
            "systemic wage theft through proof rather than violence (MCD-231's own stated "
            "method), not in combat, and that Kanja's own visible discomfort with the title is "
            "precisely what makes it trustworthy. No new named characters -- the tally worker and "
            "apprentice are unnamed and undeveloped beyond this scene."
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
            "batch": 107,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks the Trench Monarch's three-entry Alias Chronicle wave (MCD-368 through "
                "MCD-370), the first of ten remaining alias waves. " + BATCH_NOTE
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
