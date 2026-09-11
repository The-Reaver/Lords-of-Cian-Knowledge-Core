#!/usr/bin/env python3
"""Batch 217: Lock the Sovereign Ghost of the Great Sea's seventeenth through nineteenth
Alias Chronicle waves (MCD-951 through MCD-959, 9 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "three more waves and then we\'ll move on to something else this includes '
    'testing committing and pushing to origin Main." Waves 17-19 (three-per-alias pacing) '
    "for the Sovereign Ghost of the Great Sea."
)

ENTRIES = [
    (17, "the-debt-the-sea-called-in", "The Debt the Sea Called In", "XLIX",
     "First dramatized use of Undertow (`ARS-388`), the last previously-undetailed "
     "Captain's-Five treasure -- a Titan-scale natural sea creature threatens a grain "
     "convoy, and Kanja drags it under with the net-line rather than kill it in open water "
     "near crewed hulls. First entirely natural, non-human threat for this alias."),
    (17, "the-marshal-who-took-it-personally", "The Marshal Who Took It Personally", "L",
     "Introduces a new recurring antagonist, an unnamed Trust Fleet-Marshal whose grudge "
     "(a command lost at Ghost Harbor) is personal rather than institutional, and whose "
     "patient roving-reconnaissance method is the first to genuinely study the fleet's "
     "patterns rather than just react to them."),
    (17, "what-went-without-so-others-could-have", "What Went Without, So Others Could Have",
     "LI",
     "A pure logistics/rationing entry -- an ice-locked winter and three lost supply ports "
     "force the fleet into six weeks of even rationing, resolved through Dol Maren's trade "
     "and Danne Sok's charting rather than combat or rescue. Closes wave 17."),
    (18, "the-trap-built-from-mercy-itself", "The Trap Built From Mercy Itself", "LII",
     "The Fleet-Marshal escalates by weaponizing the restraint doctrine directly -- a "
     "staged distress call rigged as an ambush -- costing the crew real blood for the first "
     "time from answering a distress call."),
    (18, "the-hand-that-chose-to-leave", "The Hand That Chose to Leave", "LIII",
     "A veteran hand peacefully departs the fleet over genuine, respectful disagreement "
     "with the mercy doctrine -- a new register distinct from an earlier unresolved-but-"
     "stayed internal dissent entry."),
    (18, "the-line-they-ran-through-fire", "The Line They Ran Through Fire", "LIV",
     "The fleet deliberately breaches a Trust blockade picket to deliver grain to a "
     "starving port -- active humanitarian blockade-running, distinct from prior "
     "passive/reactive rescue entries. Closes wave 18."),
    (19, "what-the-marshal-couldnt-take-back", "What the Marshal Couldn't Take Back", "LV",
     "Closes the Fleet-Marshal arc: he comes alone and unarmed to confess and request "
     "reassignment rather than being defeated in combat -- resolution through the enemy's "
     "own voluntary change of heart."),
    (19, "the-last-watch-of-an-old-hand", "The Last Watch of an Old Hand", "LVI",
     "First entry to directly dramatize the mortality gap between Kanja's ageless nature "
     "and an original crew member's natural aging and eventual death for this alias."),
    (19, "what-the-sea-kept-between-them", "What the Sea Kept Between Them", "LVII",
     "A reflective ensemble closer synthesizing this run's threads against Garren Hask's "
     "true-record ledger and the legend-vs-truth theme. Closes wave 19."),
]

assert len(ENTRIES) == 9


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 217, 2026-09-11 (`MCD-{mcd_id}`). Sovereign Ghost of the "
        f"Great Sea Alias Chronicle {roman}, wave {wave}. Not a territory Chronicle. "
        f"Narrated in neutral third-person prose.*"
    )
    new_text, n = pattern.subn(replacement, text, count=1)
    assert n == 1, f"header pattern not found/replaced in {filename}"
    with open(path, "w") as f:
        f.write(new_text)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    start = 951
    new_rules = []
    for i, (wave, filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), Sovereign "
                f"Ghost of the Great Sea Alias Chronicle {roman}, wave {wave}. {summary}"
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
        "batch": 217,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Sovereign Ghost of the Great Sea's seventeenth through nineteenth "
            "Alias Chronicle waves (MCD-951 through MCD-959, 9 rules). " + BATCH_NOTE
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
