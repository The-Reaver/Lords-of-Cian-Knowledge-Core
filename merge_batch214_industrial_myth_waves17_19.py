#!/usr/bin/env python3
"""Batch 214: Lock the Industrial Myth's seventeenth through nineteenth Alias Chronicle
waves (MCD-924 through MCD-932, 9 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "three more waves and then we\'ll move on to something else this includes '
    'testing committing and pushing to origin Main." Waves 17-19 (three-per-alias '
    "pacing) for the Industrial Myth."
)

ENTRIES = [
    (17, "the-ledger-that-named-the-wrong-man", "The Ledger That Named the Wrong Man", "XLIX",
     "A testifier weaponizes the ledger process, falsely accusing an innocent junior clerk "
     "to settle a personal grudge; Ezio's cross-checking catches the fabricated dates, and "
     "Kanja refuses the claim even at cost to the crew's standing. Establishes the ledger "
     "protects the innocent from itself, not just advocates for whoever testifies."),
    (17, "what-ezio-refused-to-enter", "What Ezio Refused to Enter", "L",
     "The first real disagreement between Kanja and Ezio: Ezio wants to use a "
     "true-but-unrelated personal scandal as fast leverage against a stalling "
     "administrator; Kanja refuses, defining a hard boundary (wages/hours/production only, "
     "never personal leverage) and leaving Ezio genuinely unpersuaded in the moment."),
    (17, "the-debt-with-no-one-left-to-pay-it", "The Debt With No One Left to Pay It", "LI",
     "An elderly worker's decades-old wage debt traces to a dissolved firm and a long-dead "
     "owner -- totally unrecoverable. Introduces \"Recorded. Unrecoverable. True.\" as a new "
     "documentation category for cases beyond any possible restitution. Closes wave 17."),
    (18, "the-man-above-the-man-who-owed-her", "The Man Above the Man Who Owed Her", "LII",
     "The first vertical debt-tracing entry: a wage shortfall is followed up through four "
     "honest, non-fabricating intermediary layers to an absentee financier at the top, "
     "establishing that responsibility settles at the top of a chain even when every layer "
     "beneath is individually blameless."),
    (18, "the-night-he-didnt-get-up", "The Night He Didn't Get Up", "LIII",
     "Kanja oversleeps a scheduled testimony morning after weeks of unsustainable "
     "back-to-back districts -- pure physical exhaustion, no external threat -- humanizing "
     "him and surfacing the campaign's real toll on him personally for the first time."),
    (18, "the-compact-of-silence", "The Compact of Silence", "LIV",
     "A province-wide administrator collusion denies the crew entry outright; resolved when "
     "a district's own workers break the blockade from inside after watching Kanja wait "
     "patiently at a locked gate for three days without forcing it. Closes wave 18."),
    (19, "the-blow-he-let-land", "The Blow He Let Land", "LV",
     "The first live, real-time test of the unarmed ethos: an overseer strikes an old "
     "worker directly in front of Kanja, well within intervention range, and Kanja "
     "documents the assault on the spot instead of stopping it -- dramatizing the "
     "restraint's real personal cost in the moment it's hardest to hold."),
    (19, "the-ledgers-second-generation", "The Ledger's Second Generation", "LVI",
     "The method propagates a second generation removed from Kanja and Ezio: the quarry "
     "district's own trained auditors independently teach a further, previously untouched "
     "district -- escalating the self-sustaining-method theme beyond any direct lineage."),
    (19, "the-first-book-he-filled", "The First Book He Filled", "LVII",
     "A legacy closer from Kanja's own perspective: his original, worn-out first ledger "
     "book finally falls apart; he has it carefully copied rather than discarded, "
     "reflecting on the campaign's full two-year arc through the physical artifact itself. "
     "Closes wave 19."),
]

assert len(ENTRIES) == 9


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 214, 2026-09-11 (`MCD-{mcd_id}`). The Industrial Myth Alias "
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
    start = 924
    new_rules = []
    for i, (wave, filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The "
                f"Industrial Myth Alias Chronicle {roman}, wave {wave}. {summary}"
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
        "batch": 214,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Industrial Myth's seventeenth through nineteenth Alias Chronicle "
            "waves (MCD-924 through MCD-932, 9 rules). " + BATCH_NOTE
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
