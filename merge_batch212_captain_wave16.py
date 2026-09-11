#!/usr/bin/env python3
"""Batch 212: Lock Captain's sixteenth Alias Chronicle wave
(MCD-918 through MCD-920, 3 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do the waves per alias x 11 aliases... continue uninterrupted until completion '
    'this includes test, commit, push to main origin." Sixteenth wave (three-per-alias '
    'pacing) for Captain, completing wave 16 for all eleven aliases.'
)

ENTRIES = [
    ("the-secret-he-should-have-told-them", "The Secret He Should Have Told Them", "XLVI",
     "Kanja privately sits on an unconfirmed intelligence shift to spare the crew worry, a "
     "skiff nearly pays for it, and Garren Hask calls him on the paternalism directly. "
     "Kanja admits fault publicly, and a new standing crew norm is born: unconfirmed "
     "information gets shared the moment he has it, full stop."),
    ("the-wedding-he-was-asked-to-witness", "The Wedding He Was Asked to Witness", "XLVII",
     "The wave's first purely celebratory, conflict-free entry. Two crew members ask Kanja "
     "to stand witness, not officiant, at their wedding, so it reads as belonging to the "
     "crew's custom rather than to him -- warm, unguarded, closing on him simply sitting "
     "at ease with his boots off."),
    ("the-promise-for-after-hes-gone", "The Promise for After He's Gone", "XLVIII",
     "The first entry to directly confront the mortality asymmetry between Kanja's long "
     "lifespan and his crew's ordinary one: an aging Garren Hask keeps a private notebook "
     "about what happens to the \"Captain\" institution after the founding generation is "
     "gone. Kanja commits to eventually becoming the one who remembers and hands the "
     "tradition forward. Closes the wave."),
]

assert len(ENTRIES) == 3


def fix_header(filename, mcd_id, roman):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 212, 2026-09-11 (`MCD-{mcd_id}`). Captain Alias Chronicle "
        f"{roman}, wave 16. Not a territory Chronicle. Narrated in neutral third-person "
        f"prose.*"
    )
    new_text, n = pattern.subn(replacement, text, count=1)
    assert n == 1, f"header pattern not found/replaced in {filename}"
    with open(path, "w") as f:
        f.write(new_text)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    start = 918
    new_rules = []
    for i, (filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), Captain "
                f"Alias Chronicle {roman}, wave 16. {summary}"
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
        "batch": 212,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks Captain's sixteenth Alias Chronicle wave (MCD-918 through MCD-920, "
            "3 rules), completing wave 16 for ten of eleven aliases (Lord of Embers still "
            "pending in Batch 213). " + BATCH_NOTE
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
