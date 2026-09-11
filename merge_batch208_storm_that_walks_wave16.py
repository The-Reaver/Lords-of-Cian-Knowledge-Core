#!/usr/bin/env python3
"""Batch 208: Lock the Storm That Walks' sixteenth Alias Chronicle wave
(MCD-906 through MCD-908, 3 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do the waves per alias x 11 aliases... continue uninterrupted until completion '
    'this includes test, commit, push to main origin." Sixteenth wave (three-per-alias '
    'pacing) for the Storm That Walks.'
)

ENTRIES = [
    ("the-calm-that-was-made-not-found", "The Calm That Was Made, Not Found", "XLVI",
     "The sub-series' first genuine deception of the forecasting method itself: a "
     "Directorate defector infiltrates the successor's relay network and falsifies "
     "confirmation signals, feeding her a fabricated \"clean\" six-hour calm window while "
     "withholding knowledge of a real, fast-approaching storm, exposing supply hulls in "
     "open water."),
    ("the-storm-they-read-too-late", "The Storm They Read Too Late", "XLVII",
     "With no time to retreat, Kanja reads the incoming storm by raw observation rather "
     "than a forecast and turns all three Trinity pieces defensively against the storm's "
     "physical force itself to save the convoy, rather than against an enemy combatant -- "
     "two hulls damaged, none lost, no deaths."),
    ("what-the-second-sky-reader-doubted-after",
     "What the Second Sky-Reader Doubted After", "XLVIII",
     "Unable to \"study\" a deliberate deception the way she could study an honest "
     "miscalculation, Sephtis's successor works through her own doubt with him and "
     "institutes a permanent new safeguard -- an independent \"second watch\" verification "
     "line across the relay network. Closes the wave."),
]

assert len(ENTRIES) == 3


def fix_header(filename, mcd_id, roman):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 208, 2026-09-11 (`MCD-{mcd_id}`). The Storm That Walks "
        f"Alias Chronicle {roman}, wave 16. Not a territory Chronicle. Narrated in neutral "
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
    start = 906
    new_rules = []
    for i, (filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The "
                f"Storm That Walks Alias Chronicle {roman}, wave 16. {summary}"
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
        "batch": 208,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Storm That Walks' sixteenth Alias Chronicle wave (MCD-906 through "
            "MCD-908, 3 rules). " + BATCH_NOTE
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
