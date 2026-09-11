#!/usr/bin/env python3
"""Batch 210: Lock the Sovereign Ghost of the Great Sea's sixteenth Alias Chronicle wave
(MCD-912 through MCD-914, 3 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do the waves per alias x 11 aliases... continue uninterrupted until completion '
    'this includes test, commit, push to main origin." Sixteenth wave (three-per-alias '
    'pacing) for the Sovereign Ghost of the Great Sea.'
)

ENTRIES = [
    ("the-mercy-that-cost-them", "The Mercy That Cost Them", "XLVI",
     "Kanja's standard-practice parole of a captured Trust clerk is followed, weeks later, "
     "by a devastatingly precise reprisal raid on a fleet-aligned fishing settlement that "
     "could only have come from inside knowledge. Guilt is never confirmed or ruled out -- "
     "the alias's first genuine moral-cost failure entry, with Kanja choosing, without "
     "comfort, to keep making the same trade afterward."),
    ("what-the-crew-argued-over", "What the Crew Argued Over", "XLVII",
     "In the raid's aftermath, a grieving young crewman directly challenges the restraint "
     "doctrine aboard The Receipt. Efa Gol and Kanja don't out-argue him into agreement -- "
     "the disagreement is explicitly left open and carried, establishing the doctrine "
     "survives only through active maintenance, not automatic consensus."),
    ("the-flag-that-wasnt-theirs", "The Flag That Wasn't Theirs", "XLVIII",
     "An unrelated faction stages a black-sail atrocity against a village specifically to "
     "defame the ghost fleet's name -- provably not them, but the perpetrators are never "
     "caught. Kanja shows up unarmed with proof and restitution, and some villagers are "
     "convinced while others never will be, establishing a genuine limit of the "
     "reputation-defense playbook. Closes the wave."),
]

assert len(ENTRIES) == 3


def fix_header(filename, mcd_id, roman):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 210, 2026-09-11 (`MCD-{mcd_id}`). Sovereign Ghost of the "
        f"Great Sea Alias Chronicle {roman}, wave 16. Not a territory Chronicle. Narrated "
        f"in neutral third-person prose.*"
    )
    new_text, n = pattern.subn(replacement, text, count=1)
    assert n == 1, f"header pattern not found/replaced in {filename}"
    with open(path, "w") as f:
        f.write(new_text)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    start = 912
    new_rules = []
    for i, (filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), Sovereign "
                f"Ghost of the Great Sea Alias Chronicle {roman}, wave 16. {summary}"
            ),
            "status": "locked",
            "source": SOURCE,
        })

    new_ids = [r["id"] for r in new_rules]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(new_rules)

    ledger["batches_completed"].append({
        "batch": 210,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Sovereign Ghost of the Great Sea's sixteenth Alias Chronicle wave "
            "(MCD-912 through MCD-914, 3 rules). " + BATCH_NOTE
        ),
    })

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
