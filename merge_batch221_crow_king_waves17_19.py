#!/usr/bin/env python3
"""Batch 221: Lock the Crow King's seventeenth through nineteenth Alias Chronicle waves
(MCD-987 through MCD-995, 9 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "three more waves and then we\'ll move on to something else this includes '
    'testing committing and pushing to origin Main." Waves 17-19 (three-per-alias pacing) '
    "for the Crow King."
)

ENTRIES = [
    (17, "the-storm-that-swallowed-every-word", "The Storm That Swallowed Every Word",
     "XLIX",
     "A multi-day downpour makes vocal projection categorically impossible; the crew "
     "converts the percussive tap-signal channel into a full multi-person relay chain and "
     "runs an entire evacuation without a single spoken word."),
    (17, "what-the-blind-commander-heard-first", "What the Blind Commander Heard First", "L",
     "A blind garrison commander with trained hyperacute hearing catches the crew's "
     "flawless false signal precisely because it's too rhythmically perfect for real fear "
     "-- forcing the craft to deliberately engineer imperfection for the first time."),
    (17, "the-first-quiet-performance", "The First Quiet Performance", "LI",
     "Set shortly after age 30: the craft's first post-Rebellion deployment, shrunk from "
     "army-scale deception to getting one bored checkpoint guard to overlook one disguised "
     "traveler -- marking the Hymn-Engine's transition into the Long Mask era. Closes "
     "wave 17."),
    (18, "what-one-of-the-twenty-carried-away", "What One of the Twenty Carried Away", "LII",
     "One of the twenty outsider scouts trained in a prior wave, captured and coerced, "
     "teaches a fragment of the craft to a hostile raiding company. The response is "
     "non-punitive: a new private authentication phrase to distinguish genuine lineage "
     "practitioners from imitators."),
    (18, "the-delegation-that-never-saw-a-soldier", "The Delegation That Never Saw a Soldier",
     "LIII",
     "The craft is used for the first time in a purely diplomatic register -- projecting "
     "false military strength to a neutral foreign delegation to win material support, "
     "with zero combat and zero intended harm to anyone."),
    (18, "the-lie-their-own-side-believed", "The Lie Their Own Side Believed", "LIV",
     "A false signal meant for the enemy is misread by an allied militia, nearly causing "
     "friendly fire -- prompting a second authentication marker built specifically to "
     "prevent allies from misreading the crew's own deceptions. Closes wave 18."),
    (19, "the-flood-that-needed-no-enemy", "The Flood That Needed No Enemy", "LV",
     "A catastrophic dam failure with no adversary at all; the coordination discipline "
     "underneath the Hymn-Engine is used with zero deception to evacuate a flooding "
     "settlement, at a real, unsoftened cost of twelve lives."),
    (19, "the-third-generations-first-command", "The Third Generation's First Command", "LVI",
     "The third-generation practitioner runs a full operation entirely alone for the first "
     "time, completing the generational structure as a direct counterpart to the original "
     "apprentice's own solo debut."),
    (19, "what-they-couldnt-take-back", "What They Couldn't Take Back", "LVII",
     "The craft's first genuine, unrecovered regional breach -- two deaths, a burned "
     "regional variant, no clever counter -- closing on all three generations together "
     "processing the method's real limits. Closes wave 19."),
]

assert len(ENTRIES) == 9


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 221, 2026-09-11 (`MCD-{mcd_id}`). The Crow King Alias "
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
    start = 987
    new_rules = []
    for i, (wave, filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The Crow "
                f"King Alias Chronicle {roman}, wave {wave}. {summary}"
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
        "batch": 221,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Crow King's seventeenth through nineteenth Alias Chronicle waves "
            "(MCD-987 through MCD-995, 9 rules). " + BATCH_NOTE
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
