#!/usr/bin/env python3
"""Batch 219: Lock the Lord of Embers's seventeenth through nineteenth Alias Chronicle
waves (MCD-969 through MCD-977, 9 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "three more waves and then we\'ll move on to something else this includes '
    'testing committing and pushing to origin Main." Waves 17-19 (three-per-alias pacing) '
    "for the Lord of Embers."
)

ENTRIES = [
    (17, "what-the-forge-carved-in-memory", "What the Forge Carved in Memory", "XLIX",
     "An apprentice dies of illness, no enemy, no raid, nothing to rebuild. The floor's "
     "method has no answer for a cough; Kanja forges a plain, unmarked hinge in the boy's "
     "memory instead. First entry to confront loss with no adversary at all."),
    (17, "the-settlement-that-was-never-there", "The Settlement That Was Never There", "L",
     "Four fabricated burning reports lure the crew off-schedule toward an ambush; Callum "
     "Breck spots the pattern, and Kanja arrives on the ambush road already knowing it's "
     "bait -- discernment/counter-intelligence rather than a genuine rebuild or defense."),
    (17, "the-ledger-that-wasnt-his", "The Ledger That Wasn't His", "LI",
     "A predatory moneylender exploits frightened, displaced families three districts "
     "ahead of the campaign; Kanja undercuts him with a standing tool/material-credit offer "
     "rather than confronting him directly, and admits the fix is temporary. Closes "
     "wave 17."),
    (18, "the-caravan-that-didnt-know-his-name", "The Caravan That Didn't Know His Name",
     "LII",
     "A foreign trading caravan from beyond the Trust's reach trades fairly with the crew "
     "without ever learning who they are, judging the floor on the trade alone. First "
     "entry where the reputation never enters the picture."),
    (18, "what-the-river-barge-couldnt-outrun", "What the River Barge Couldn't Outrun",
     "LIII",
     "A detailed Trinity showcase defending an ore convoy through white-water rapids, using "
     "the violent current itself as both obstacle and weapon -- new terrain distinct from "
     "prior flood/pontoon/land showcases."),
    (18, "the-burn-he-didnt-let-them-see", "The Burn He Didn't Let Them See", "LIV",
     "Kanja sustains a real forge-accident burn from fatigue and tries to hide it; the "
     "senior smith forces him to accept care in front of the apprentices. First entry "
     "where Kanja himself is the injured, cared-for party. Closes wave 18."),
    (19, "the-boundary-stone-no-one-could-move", "The Boundary Stone No One Could Move",
     "LV",
     "A land-title dispute between two families stalls a forge terrace; Kanja refuses to "
     "adjudicate by his own authority, deferring to the district's elders' circle. First "
     "entry centered on property/legal adjudication."),
    (19, "those-who-came-with-nothing-but-the-road", "Those Who Came With Nothing But the Road",
     "LVI",
     "A detailed Trinity showcase defending roughly four hundred refugees fleeing unrelated "
     "regional conflict, pursued by opportunistic raiders -- first entry extending full "
     "protection to people outside the campaign's own settlements/apprentices."),
    (19, "the-festival-they-built-around-the-forge", "The Festival They Built Around the Forge",
     "LVII",
     "A settlement's harvest festival absorbs the crew into existing local custom; a purely "
     "celebratory, conflict-free closer with no lesson delivered through adversity. Closes "
     "wave 19."),
]

assert len(ENTRIES) == 9


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 219, 2026-09-11 (`MCD-{mcd_id}`). The Lord of Embers Alias "
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
    start = 969
    new_rules = []
    for i, (wave, filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The Lord "
                f"of Embers Alias Chronicle {roman}, wave {wave}. {summary}"
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
        "batch": 219,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Lord of Embers's seventeenth through nineteenth Alias Chronicle "
            "waves (MCD-969 through MCD-977, 9 rules). " + BATCH_NOTE
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
