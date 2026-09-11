#!/usr/bin/env python3
"""Batch 211: Lock the Crow King's sixteenth Alias Chronicle wave
(MCD-915 through MCD-917, 3 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do the waves per alias x 11 aliases... continue uninterrupted until completion '
    'this includes test, commit, push to main origin." Sixteenth wave (three-per-alias '
    'pacing) for the Crow King.'
)

ENTRIES = [
    ("the-voice-he-couldnt-trust", "The Voice He Couldn't Trust", "XLVI",
     "Kanja takes a throat wound mid-operation and loses his own voice -- the first entry "
     "to land a genuine physical limit of the Hymn-Engine on Kanja personally. The "
     "apprentice carries a full deception pattern alone for the first time while Kanja "
     "falls back on the craft's older percussive tap-signal channel, establishing a new "
     "standing rule: every operation now requires a rehearsed backup voice."),
    ("what-the-third-generation-refused", "What the Third Generation Refused", "XLVII",
     "The third-generation practitioner refuses a sound, workable deception plan because "
     "the \"opening\" it exploits is a grieving father's lapse, not carelessness -- the "
     "first entry built around a genuine ethical disagreement within the three-generation "
     "lineage itself. Kanja deliberately declines to arbitrate by fiat."),
    ("the-school-that-had-no-name", "The School That Had No Name", "XLVIII",
     "A regional commander asks for twenty of her own scouts to be taught the craft "
     "directly, forcing the apprentice and Kanja to run it for the first time as a "
     "structured six-week curriculum rather than personal, need-driven mentorship -- the "
     "Hymn-Engine's shift toward an institutional discipline while staying unnamed and "
     "unbranded. Closes the wave."),
]

assert len(ENTRIES) == 3


def fix_header(filename, mcd_id, roman):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 211, 2026-09-11 (`MCD-{mcd_id}`). The Crow King Alias "
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
    start = 915
    new_rules = []
    for i, (filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The Crow "
                f"King Alias Chronicle {roman}, wave 16. {summary}"
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
        "batch": 211,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Crow King's sixteenth Alias Chronicle wave (MCD-915 through "
            "MCD-917, 3 rules). " + BATCH_NOTE
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
