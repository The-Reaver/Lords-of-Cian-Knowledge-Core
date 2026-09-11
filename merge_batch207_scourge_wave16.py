#!/usr/bin/env python3
"""Batch 207: Lock the Scourge's sixteenth Alias Chronicle wave
(MCD-903 through MCD-905, 3 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do the waves per alias x 11 aliases... continue uninterrupted until completion '
    'this includes test, commit, push to main origin." Sixteenth wave (three-per-alias '
    'pacing) for the Scourge.'
)

ENTRIES = [
    ("the-shrine-they-built-without-asking", "The Shrine They Built Without Asking", "XLVI",
     "Age 172, V3 gear. A settlement he freed eleven years earlier has built a literal "
     "shrine to him. He confronts the community's elder anonymously and pushes back "
     "against the deification, redirecting credit toward the self-built watch chain and "
     "trade compact that actually kept them safe, without tearing the shrine down himself."),
    ("the-raid-he-watched-from-the-rigging", "The Raid He Watched From the Rigging", "XLVII",
     "Age 265, V4 gear. Kanja hands full command of an entire liberation raid, including a "
     "tense hostage standoff, to Efa Gol's already-established unnamed successor, staying "
     "aboard only as an unused failsafe. She resolves it exactly as he would have, proving "
     "the doctrine and reputation function institutionally without him physically leading."),
    ("the-boy-he-once-cut-free", "The Boy He Once Cut Free", "XLVIII",
     "Age 122, V3 gear, minimal use. A man he personally freed as a nine-year-old captive "
     "decades earlier is found running his own small trafficking operation. Kanja frees "
     "the man's captives but hands him over to Garren Hask's ledger-keeping rather than "
     "punishing or absolving him -- a deliberately unresolved confrontation with the limit "
     "of \"freedom redeems.\" Closes the wave."),
]

assert len(ENTRIES) == 3


def fix_header(filename, mcd_id, roman):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 207, 2026-09-11 (`MCD-{mcd_id}`). The Scourge Alias Chronicle "
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
    start = 903
    new_rules = []
    for i, (filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The "
                f"Scourge Alias Chronicle {roman}, wave 16. {summary}"
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
        "batch": 207,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Scourge's sixteenth Alias Chronicle wave (MCD-903 through MCD-905, "
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
