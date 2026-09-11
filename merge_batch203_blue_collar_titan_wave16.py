#!/usr/bin/env python3
"""Batch 203: Lock the Blue-Collar Titan's sixteenth Alias Chronicle wave
(MCD-891 through MCD-893, 3 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "do the waves per alias x 11 aliases... continue uninterrupted until completion '
    'this includes test, commit, push to main origin." Sixteenth wave (three-per-alias '
    'pacing) for the Blue-Collar Titan.'
)

ENTRIES = [
    ("the-wall-he-built-to-come-down", "The Wall He Built to Come Down", "XLVI",
     "Kanja is ordered to personally demolish a reinforced causeway crossing he himself "
     "built earlier in the Sewer War of Killane, to deny it to a Trust relief column. "
     "Establishes the alias's first identity-reversal register: the same structural-reading "
     "discipline used to build and repair applied to precise, minimal-collateral controlled "
     "demolition of his own completed work."),
    ("what-the-inspector-never-found", "What the Inspector Never Found", "XLVII",
     "A surprise Directorate structural inspector audits the section Kanja has covertly "
     "reinforced for defensive purposes. He passes the inspection entirely on genuine, "
     "verifiable tradesman competence and true, if incomplete, answers -- no lies, no "
     "evasion, no Trinity -- establishing cover held by real craftsmanship surviving real "
     "interrogation."),
    ("the-numbers-that-forgave-no-one", "The Numbers That Forgave No One", "XLVIII",
     "Two workers die from a support-timber failure that turns out, after two days of "
     "rigorous investigation, to be nobody's fault at all -- a genuinely undetectable "
     "material flaw. Establishes the alias's first no-fault forensic register: Kanja "
     "delivers the hardest kind of true account to grieving families, refusing to "
     "manufacture a villain or a preventable lesson. Closes the wave."),
]

assert len(ENTRIES) == 3


def fix_header(filename, mcd_id, roman):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 203, 2026-09-11 (`MCD-{mcd_id}`). The Blue-Collar Titan Alias "
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
    start = 891
    new_rules = []
    for i, (filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The "
                f"Blue-Collar Titan Alias Chronicle {roman}, wave 16. {summary}"
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
        "batch": 203,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Blue-Collar Titan's sixteenth Alias Chronicle wave (MCD-891 through "
            "MCD-893, 3 rules). " + BATCH_NOTE
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
