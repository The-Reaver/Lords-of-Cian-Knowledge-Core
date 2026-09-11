#!/usr/bin/env python3
"""Batch 213: Lock the Lord of Embers's sixteenth Alias Chronicle wave
(MCD-921 through MCD-923, 3 rules). Completes wave 16 for all eleven aliases."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do the waves per alias x 11 aliases... continue uninterrupted until completion '
    'this includes test, commit, push to main origin." Sixteenth wave (three-per-alias '
    'pacing) for the Lord of Embers, completing wave 16 across all eleven aliases '
    "(Batches 203-213, 33 new Chronicles, MCD-891 through MCD-923)."
)

ENTRIES = [
    ("the-smith-who-came-to-judge-him", "The Smith Who Came to Judge Him", "XLVI",
     "An itinerant master smith walks four weeks to expose the Lord of Embers' reputation "
     "as a lie and challenges him to a formal, judged craft contest -- no Trinity gear, no "
     "combat. The master's faster work cracks under stress test; Kanja's slower, more "
     "deliberate work holds, proving the reputation was never about supernatural speed but "
     "patient, teachable technique."),
    ("what-the-enemy-learned-to-rebuild", "What the Enemy Learned to Rebuild", "XLVII",
     "A Directorate garrison rebuilds in 19 days instead of the usual 9 weeks, using "
     "methods lifted from Kanja's own openly-taught rebuild doctrine via an escaped "
     "captured smith. Kanja confronts the double-edged cost of an open method being "
     "weaponized by forced-labor conscription, resolved only partially by recognizing that "
     "consent and ownership, not the technique itself, are the method's real load-bearing "
     "element."),
    ("the-fire-that-asked-for-no-enemy", "The Fire That Asked for No Enemy", "XLVIII",
     "A lightning-sparked wildfire with no Trust involvement threatens a settlement; the "
     "senior smith's already-established successor takes independent command for the "
     "first time, forging firebreak-cutting tools while Kanja works as one more hand under "
     "her plan -- the first test of \"metabolizes punishment\" against nature rather than "
     "any enemy action. Closes the wave."),
]

assert len(ENTRIES) == 3


def fix_header(filename, mcd_id, roman):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 213, 2026-09-11 (`MCD-{mcd_id}`). The Lord of Embers Alias "
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
    start = 921
    new_rules = []
    for i, (filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The Lord "
                f"of Embers Alias Chronicle {roman}, wave 16. {summary}"
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
        "batch": 213,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Lord of Embers's sixteenth Alias Chronicle wave (MCD-921 through "
            "MCD-923, 3 rules). Completes wave 16 (33 new Chronicles, Batches 203-213) "
            "across all eleven aliases. " + BATCH_NOTE
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
