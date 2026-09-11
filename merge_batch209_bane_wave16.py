#!/usr/bin/env python3
"""Batch 209: Lock Bane's sixteenth Alias Chronicle wave
(MCD-909 through MCD-911, 3 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do the waves per alias x 11 aliases... continue uninterrupted until completion '
    'this includes test, commit, push to main origin." Sixteenth wave (three-per-alias '
    'pacing) for Bane.'
)

ENTRIES = [
    ("the-line-he-drew-inside-his-own-column", "The Line He Drew Inside His Own Column",
     "XLVI",
     "A recruit beats a captured, already-cooperative Directorate clerk out of cruelty "
     "rather than necessity. Bane holds a formal reckoning inside his own column, "
     "expelling the recruit rather than killing him, grounding the choice in \"the fear "
     "only works if it's true\": cruelty from inside breaks the mechanism as surely as "
     "cruelty from outside would."),
    ("the-surrender-that-wasnt-one", "The Surrender That Wasn't One", "XLVII",
     "A garrison stages a fake surrender using \"wounded\" soldiers on stretchers as cover "
     "for an ambush. Onyx's Veil Piercer power gets its first dedicated showcase -- reading "
     "what things actually are beneath how they're arranged to look -- completing a "
     "trilogy with the already-locked Black Ledger and Soulbound Edge showcases. Bane "
     "exposes the ruse without violence beyond forcing the ambushers to reveal themselves."),
    ("the-fire-he-chose-over-the-ambush", "The Fire He Chose Over the Ambush", "XLVIII",
     "Mid-campaign, with three days invested in positioning an ambush on a supply convoy, "
     "a wildfire set as scorched-earth denial threatens a small neutral herding "
     "settlement. Bane abandons the ambush entirely to save the settlement -- a deliberate "
     "forfeiture of a major tactical investment as a clear-eyed choice, carried entirely by "
     "ordinary physical labor since no Trinity ability applies to a fire. Closes the wave."),
]

assert len(ENTRIES) == 3


def fix_header(filename, mcd_id, roman):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 209, 2026-09-11 (`MCD-{mcd_id}`). Bane Alias Chronicle "
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
    start = 909
    new_rules = []
    for i, (filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), Bane "
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
        "batch": 209,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks Bane's sixteenth Alias Chronicle wave (MCD-909 through MCD-911, "
            "3 rules). " + BATCH_NOTE
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
