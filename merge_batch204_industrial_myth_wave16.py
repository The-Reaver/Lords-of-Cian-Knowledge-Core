#!/usr/bin/env python3
"""Batch 204: Lock the Industrial Myth's sixteenth Alias Chronicle wave
(MCD-894 through MCD-896, 3 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do the waves per alias x 11 aliases... continue uninterrupted until completion '
    'this includes test, commit, push to main origin." Sixteenth wave (three-per-alias '
    'pacing) for the Industrial Myth.'
)

ENTRIES = [
    ("what-his-hands-remembered", "What His Hands Remembered", "XLVI",
     "A brick-kiln district distrusts outside \"soft hands\" investigators. Kanja works the "
     "worst barrow rotation in the yard for four days, splitting his hands and falling "
     "behind the pace like any new hauler, before ever asking a single wage question -- "
     "trust earned through failed, unglamorous physical labor rather than the ledger "
     "method."),
    ("what-the-proof-couldnt-undo", "What the Proof Couldn't Undo", "XLVII",
     "A woman's wage-debt testimony is proven cleanly, but the district overseer retaliates "
     "by evicting her on an unrelated tenancy pretext before the ledger can act as "
     "protection. Establishes a new standing practice: the campaign now arranges concrete "
     "relief for anyone who testifies, not just recording their debt, without pretending "
     "the gap is fully closed."),
    ("the-district-that-kept-its-own-books", "The District That Kept Its Own Books", "XLVIII",
     "A quarry-district worker asks who protects the next crew once the tally team moves "
     "on. The crew stays four extra days training a dozen local workers in Ezio's "
     "corrective auditing method, then leaves the district's ledger in their own keeping -- "
     "scaling knowledge-transfer from individual mentorship to district-wide "
     "self-sufficiency as a repeatable standing policy. Closes the wave."),
]

assert len(ENTRIES) == 3


def fix_header(filename, mcd_id, roman):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 204, 2026-09-11 (`MCD-{mcd_id}`). The Industrial Myth Alias "
        f"Chronicle {roman}, wave 16. Not a territory Chronicle. Narrated in neutral "
        f"third-person prose.*"
    )
    new_text, n = pattern.subn(replacement, text, count=1)
    assert n == 1, f"header pattern not found/replaced in {filename}"
    with open(path, "w") as f:
        f.write(new_text)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    start = 894
    new_rules = []
    for i, (filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The "
                f"Industrial Myth Alias Chronicle {roman}, wave 16. {summary}"
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
        "batch": 204,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Industrial Myth's sixteenth Alias Chronicle wave (MCD-894 through "
            "MCD-896, 3 rules). " + BATCH_NOTE
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
