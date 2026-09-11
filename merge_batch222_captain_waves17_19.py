#!/usr/bin/env python3
"""Batch 222: Lock Captain's seventeenth through nineteenth Alias Chronicle waves
(MCD-996 through MCD-1004, 9 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "three more waves and then we\'ll move on to something else this includes '
    'testing committing and pushing to origin Main." Waves 17-19 (three-per-alias pacing) '
    "for Captain."
)

ENTRIES = [
    (17, "the-prank-pell-ostra-spent-a-year-planning",
     "The Prank Pell Ostra Spent a Year Planning", "XLIX",
     "Pell Ostra spends eleven months deliberately corrupting Kanja's read on her "
     "demolition timing so a simple bilge-water prank actually lands. First purely "
     "comedic/levity entry in the entire Captain run."),
    (17, "the-ledger-line-he-made-them-correct", "The Ledger Line He Made Them Correct", "L",
     "Kanja catches Garren Hask quietly paying him an inflated \"command differential\" "
     "share and makes him publicly rewrite the crew's ledger to a standing equal-risk-"
     "equal-share policy. First entry about Kanja's own economic treatment."),
    (17, "the-funeral-efa-gol-asked-him-to-speak-at",
     "The Funeral Efa Gol Asked Him to Speak At", "LI",
     "A founding-era rigger dies of old age; Kanja delivers a eulogy at the crew's own "
     "unceremonious sea-burial. First full funeral/eulogy scene. Closes wave 17."),
    (18, "the-mother-who-asked-him-to-say-the-name",
     "The Mother Who Asked Him to Say the Name", "LII",
     "A bereaved mother of a conscripted enemy soldier asks Kanja to help find and speak "
     "her son's name; Hask's cross-checked casualty ledger locates him. First direct "
     "accountability scene with an outsider/victim, deliberately unresolved into comfort."),
    (18, "the-council-that-told-him-no", "The Council That Told Him No", "LIII",
     "The crew dispute council votes 3-2 against a rescue operation Kanja personally "
     "proposed, and he accepts it. First time his own preference is formally overruled by "
     "an institution he built."),
    (18, "the-deckhand-who-learned-to-read-the-ledger",
     "The Deckhand Who Learned to Read the Ledger", "LIV",
     "Kanja personally teaches an illiterate young deckhand to read using Hask's old "
     "ledgers. First ordinary-skill mentorship entry; establishes a teaching lineage. "
     "Closes wave 18."),
    (19, "the-girl-who-grew-up-visiting-the-ship", "The Girl Who Grew Up Visiting the Ship",
     "LV",
     "Danne Sok's daughter is followed from age six to sixteen, culminating in her "
     "enlisting and earning trust the ordinary slow way. First entry spanning years as one "
     "continuous relationship arc."),
    (19, "the-jealousy-nobody-would-name", "The Jealousy Nobody Would Name", "LVI",
     "A junior crew member resents being passed over in favor of Callum Breck; Kanja names "
     "the festering envy directly and addresses it without favoritism. First entry on "
     "internal rivalry/perceived favoritism."),
    (19, "the-war-the-name-outlived", "The War the Name Outlived", "LVII",
     "Set at the Rebellion's close, the dispute council asks what the \"Captain\" "
     "institution is for now that the war that birthed it is over; Kanja admits he doesn't "
     "know. Closes the wave and the three-wave run on a deliberately open note."),
]

assert len(ENTRIES) == 9


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 222, 2026-09-11 (`MCD-{mcd_id}`). Captain Alias Chronicle "
        f"{roman}, wave {wave}. Not a territory Chronicle. Narrated in neutral third-person "
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
    start = 996
    new_rules = []
    for i, (wave, filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), Captain "
                f"Alias Chronicle {roman}, wave {wave}. {summary}"
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
        "batch": 222,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks Captain's seventeenth through nineteenth Alias Chronicle waves "
            "(MCD-996 through MCD-1004, 9 rules). " + BATCH_NOTE
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
