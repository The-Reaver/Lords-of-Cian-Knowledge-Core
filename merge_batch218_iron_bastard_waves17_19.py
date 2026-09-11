#!/usr/bin/env python3
"""Batch 218: Lock the Iron Bastard's seventeenth through nineteenth Alias Chronicle waves
(MCD-960 through MCD-968, 9 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "three more waves and then we\'ll move on to something else this includes '
    'testing committing and pushing to origin Main." Waves 17-19 (three-per-alias pacing) '
    "for the Iron Bastard."
)

ENTRIES = [
    (17, "the-structure-too-small-to-hear", "The Structure Too Small to Hear", "XLIX",
     "The doctrine's first test at the lower bound of scale: a hair-fine miniature "
     "puzzle-box mechanism, where the difficulty is isolating a whisper-level signature "
     "from the listener's own body noise. Resolved through stillness and patience rather "
     "than power."),
    (17, "the-storm-that-wrote-its-own-signature", "The Storm That Wrote Its Own Signature",
     "L",
     "A lightning storm imposes a constantly shifting false tension signature on a "
     "watchtower's ironwork; Kanja withdraws and waits the storm out instead of forcing an "
     "untrustworthy reading, establishing patience/withheld action as a new doctrine "
     "response."),
    (17, "the-command-vehicle-in-the-formation", "The Command Vehicle in the Formation", "LI",
     "Eight identical-looking Crawlers ring a depot; Kanja identifies the single command "
     "vehicle by a subtly heavier bracing signature and disables only it, collapsing the "
     "whole formation's coordination -- a new signature-discrimination tactic. Closes "
     "wave 17."),
    (18, "the-silence-where-the-talisman-should-have-answered",
     "The Silence Where the Talisman Should Have Answered", "LII",
     "The Aegis-Talisman itself goes fully inert from prior battle damage mid-mission; "
     "Kanja completes a critical read through unaided direct hand contact alone, proving "
     "the core skill is his, not the artifact -- the run's first true device-independence "
     "entry."),
    (18, "two-doctrines-no-common-ancestor", "Two Doctrines, No Common Ancestor", "LIII",
     "A neutral trade enclave's engineers, with zero prior contact with Kanja or the Trust, "
     "have independently developed a near-identical diagnostic-listening craft. A "
     "respectful, non-adversarial comparison and skill exchange -- convergent invention "
     "rather than study, defection, or theft."),
    (18, "the-trial-of-the-falling-roof", "The Trial of the Falling Roof", "LIV",
     "Kanja is personally and falsely accused of an unrelated market-roof collapse; he "
     "uses the doctrine as public testimony before a tribunal to prove his innocence and "
     "the collapse's true cause -- a personal self-defense register. Closes wave 18."),
    (19, "the-zone-he-didnt-have-to-read-alone", "The Zone He Didn't Have to Read Alone",
     "LV",
     "The first true multi-listener team job: Kanja, the second student, and the defected "
     "Trust engineer divide a sprawling harbor complex into zones and read it "
     "simultaneously -- a generational/collaborative scaling entry."),
    (19, "what-the-third-generation-asked", "What the Third Generation Asked", "LVI",
     "The second student's own apprentice, a third generation removed from Kanja, asks why "
     "the doctrine reads only tension and not moral worth, forcing Kanja to articulate that "
     "judgment has always been his, not the method's."),
    (19, "the-building-that-asked-to-be-heard", "The Building That Asked to Be Heard", "LVII",
     "A quiet, non-technical closer: Kanja reads a condemned, empty foundry warehouse with "
     "no operational purpose at all, the day before its demolition -- an elegy for an "
     "ordinary structure. Closes wave 19."),
]

assert len(ENTRIES) == 9


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 218, 2026-09-11 (`MCD-{mcd_id}`). The Iron Bastard Alias "
        f"Chronicle {roman}, wave {wave}. Not a territory Chronicle. Narrated in neutral "
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
    start = 960
    new_rules = []
    for i, (wave, filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The Iron "
                f"Bastard Alias Chronicle {roman}, wave {wave}. {summary}"
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
        "batch": 218,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Iron Bastard's seventeenth through nineteenth Alias Chronicle waves "
            "(MCD-960 through MCD-968, 9 rules). " + BATCH_NOTE
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
