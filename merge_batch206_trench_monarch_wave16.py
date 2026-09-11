#!/usr/bin/env python3
"""Batch 206: Lock the Trench Monarch's sixteenth Alias Chronicle wave
(MCD-900 through MCD-902, 3 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do the waves per alias x 11 aliases... continue uninterrupted until completion '
    'this includes test, commit, push to main origin." Sixteenth wave (three-per-alias '
    'pacing) for the Trench Monarch.'
)

ENTRIES = [
    ("the-wall-that-wouldnt-hold-itself", "The Wall That Wouldn't Hold Itself", "XLVI",
     "A storm collapses a canal retaining wall above forty families' homes at Warrow Bend. "
     "Pure disaster relief with no adversary and no Onyx use at all -- Kanja and the "
     "earliest crew spend two days doing raw physical labor to shore the wall by hand, "
     "extending the \"digging his own crown\" ethos to nature and exhaustion, not just "
     "human opposition."),
    ("the-anger-he-almost-let-win", "The Anger He Almost Let Win", "XLVII",
     "A cooperating tally worker is brutally tortured as retaliation. For the first time "
     "Kanja's composure genuinely cracks -- Onyx's Soulbound Edge responds to raw rage "
     "rather than trained intention-reading, and he comes within a breath of a killing "
     "stroke he can't fully claim was a deliberate choice, leaving him shaken and honest "
     "about it with the crew afterward."),
    ("the-elder-they-buried-at-the-canal", "The Elder They Buried at the Canal", "XLVIII",
     "An unnamed old dredge hand, older than the alias itself, dies quietly of natural "
     "causes. Kanja attends the small, unceremonial burial uninvited and unneeded, speaks "
     "briefly, and helps finish the grave marker by hand -- a mourning/mortality register "
     "centering an ordinary community elder's death. Closes the wave."),
]

assert len(ENTRIES) == 3


def fix_header(filename, mcd_id, roman):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 206, 2026-09-11 (`MCD-{mcd_id}`). The Trench Monarch Alias "
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
    start = 900
    new_rules = []
    for i, (filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The "
                f"Trench Monarch Alias Chronicle {roman}, wave 16. {summary}"
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
        "batch": 206,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Trench Monarch's sixteenth Alias Chronicle wave (MCD-900 through "
            "MCD-902, 3 rules). " + BATCH_NOTE
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
