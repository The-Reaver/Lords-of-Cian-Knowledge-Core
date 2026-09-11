#!/usr/bin/env python3
"""Batch 205: Lock the Iron Bastard's sixteenth Alias Chronicle wave
(MCD-897 through MCD-899, 3 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do the waves per alias x 11 aliases... continue uninterrupted until completion '
    'this includes test, commit, push to main origin." Sixteenth wave (three-per-alias '
    'pacing) for the Iron Bastard.'
)

ENTRIES = [
    ("the-gate-the-river-swallowed", "The Gate the River Swallowed", "XLVI",
     "The doctrine's first submerged/underwater application: reading a fully water-covered "
     "sluice gate from the bank fails outright because the current's noise masks the "
     "tension signature at any distance. Resolved via direct physical contact with a "
     "partially-submerged anchor chain, extending the direct-contact fallback into a medium "
     "never used before."),
    ("the-dam-he-built-instead-of-broke", "The Dam He Built Instead of Broke", "XLVII",
     "The doctrine's first fully constructive, non-adversarial use: no enemy, no military "
     "objective -- Kanja diagnoses and reinforces a failing civilian dam to keep it "
     "standing, establishing the doctrine can serve as pure civil aid."),
    ("the-men-who-sold-his-own-ear", "The Men Who Sold His Own Ear", "XLVIII",
     "The doctrine's first corruption by non-institutional profiteers -- freelance "
     "mercenaries with no real grasp of the technique trade on the Iron Bastard's name and "
     "a crude fake of the method to settle private disputes for hire. Kanja's response is "
     "corrective, stopping a false \"collapse\" to save the structure, rather than combat. "
     "Closes the wave."),
]

assert len(ENTRIES) == 3


def fix_header(filename, mcd_id, roman):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 205, 2026-09-11 (`MCD-{mcd_id}`). The Iron Bastard Alias "
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
    start = 897
    new_rules = []
    for i, (filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The Iron "
                f"Bastard Alias Chronicle {roman}, wave 16. {summary}"
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
        "batch": 205,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Iron Bastard's sixteenth Alias Chronicle wave (MCD-897 through "
            "MCD-899, 3 rules). " + BATCH_NOTE
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
