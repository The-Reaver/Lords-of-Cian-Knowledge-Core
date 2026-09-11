#!/usr/bin/env python3
"""Batch 220: Lock the Storm That Walks' seventeenth through nineteenth Alias Chronicle
waves (MCD-978 through MCD-986, 9 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "three more waves and then we\'ll move on to something else this includes '
    'testing committing and pushing to origin Main." Waves 17-19 (three-per-alias pacing) '
    "for the Storm That Walks."
)

ENTRIES = [
    (17, "the-school-sephtis-never-meant-to-start", "The School Sephtis Never Meant to Start",
     "XLIX",
     "Sephtis and his successor's one-to-one apprenticeship grows into a small "
     "multi-student school -- the first entry to move the doctrine's transmission from a "
     "single lineage into a real institution, with the successor exercising her first "
     "independent authority."),
    (17, "the-two-readings-that-disagreed", "The Two Readings That Disagreed", "L",
     "Sephtis and his successor read the same weather system and reach opposite "
     "conclusions for the first time; Kanja refuses to arbitrate, and they resolve it by "
     "holding the fleet at anchor and sending a scout to verify directly -- a doctrine-"
     "level disagreement protocol."),
    (17, "the-student-who-walked-away", "The Student Who Walked Away", "LI",
     "One of the school's most naturally talented students washes out after his first "
     "honest miss, unable to bear being visibly wrong with lives at stake -- the craft's "
     "real bottleneck is emotional, not mathematical. Closes wave 17."),
    (18, "the-reading-he-could-no-longer-make-alone",
     "The Reading He Could No Longer Make Alone", "LII",
     "An elderly Sephtis, his hand unsteadied by a fever, can still read the sky but can no "
     "longer chart it himself; he dictates a call to his successor in full view of the "
     "fleet rather than hide the decline -- the first physical-limits entry for him."),
    (18, "the-sky-the-day-they-buried-him", "The Sky the Day They Buried Him", "LIII",
     "Sephtis dies peacefully in his sleep; his successor alone makes the call determining "
     "whether the sea-burial rites can proceed, understanding it as the one reading she "
     "could not hand to anyone else. First mortality entry specific to this alias's arc."),
    (18, "the-strait-they-named-for-a-man-who-read-it",
     "The Strait They Named for a Man Who Read It", "LIV",
     "Generations later, sailors have informally named a strait after Sephtis; his now-"
     "elderly successor teaches her own student, a third generation of the craft, closing "
     "the institutional cycle. Closes wave 18."),
    (19, "the-calm-bought-for-a-handshake", "The Calm Bought for a Handshake", "LV",
     "A jointly-called calm window lets two mutually distrustful delegations cross "
     "contested water into a peace negotiation simultaneously and unthreatened, with the "
     "Trinity present only as a visible, unused deterrent -- protecting a diplomatic "
     "negotiation rather than a fleet or rescue."),
    (19, "the-ones-who-read-the-same-sky", "The Ones Who Read the Same Sky", "LVI",
     "An enemy squadron reads the same dangerous water independently and breaks off "
     "unharmed, revealed to have its own generations-old weather tradition; the successor "
     "meets her enemy counterpart under truce, and both fleets begin giving each other's "
     "ships a berth around dangerous weather -- a rival tradition treated as a legitimate "
     "peer."),
    (19, "what-the-storm-never-took-from-him", "What the Storm Never Took From Him", "LVII",
     "On a quiet evening with nothing to forecast, Kanja reflects privately with Efa Gol on "
     "what this alias has meant to him -- not combat or command, but what he learned from "
     "Sephtis's and his successor's courage in being visibly wrong. Closes wave 19."),
]

assert len(ENTRIES) == 9


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 220, 2026-09-11 (`MCD-{mcd_id}`). The Storm That Walks "
        f"Alias Chronicle {roman}, wave {wave}. Not a territory Chronicle. Narrated in "
        f"neutral third-person prose.*"
    )
    new_text, n = pattern.subn(replacement, text, count=1)
    assert n == 1, f"header pattern not found/replaced in {filename}"
    with open(path, "w") as f:
        f.write(new_text)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    start = 978
    new_rules = []
    for i, (wave, filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The "
                f"Storm That Walks Alias Chronicle {roman}, wave {wave}. {summary}"
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
        "batch": 220,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Storm That Walks' seventeenth through nineteenth Alias Chronicle "
            "waves (MCD-978 through MCD-986, 9 rules). " + BATCH_NOTE
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
