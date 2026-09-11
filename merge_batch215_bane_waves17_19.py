#!/usr/bin/env python3
"""Batch 215: Lock Bane's seventeenth through nineteenth Alias Chronicle waves
(MCD-933 through MCD-941, 9 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "three more waves and then we\'ll move on to something else this includes '
    'testing committing and pushing to origin Main." Waves 17-19 (three-per-alias pacing) '
    "for Bane."
)

ENTRIES = [
    (17, "the-silence-they-built-to-blind-him", "The Silence They Built to Blind Him", "XLIX",
     "A Directorate engineering corps builds a sound-deadened depot chamber specifically to "
     "defeat Onyx of Oblivion's non-visual sensing; Bane falls back on plain physical "
     "tracking to free forty prisoners. First entry to show the enemy successfully "
     "targeting and partially neutralizing an established Trinity sensory ability."),
    (17, "the-name-they-wanted-to-borrow", "The Name They Wanted to Borrow", "L",
     "A settlement asks Bane for permission to invoke his name/reputation as a standing "
     "deterrent against a separate bandit threat, with no guarantee he'll be present if "
     "tested -- a genuine consent-and-control question about who gets to use his legend."),
    (17, "the-night-they-came-for-the-blade", "The Night They Came for the Blade", "LI",
     "Infiltrators attempt to steal Onyx of Oblivion while Bane sleeps; the theft is "
     "thwarted entirely by Garren Hask's own unassigned habit of walking the tent line at "
     "night, no Trinity ability involved. First entry to dramatize the Trinity's literal "
     "physical vulnerability during rest. Closes wave 17."),
    (18, "the-crossing-they-almost-didnt-make", "The Crossing They Almost Didn't Make", "LII",
     "A flash flood turns a safe ford into a torrent mid-evacuation of ninety refugees with "
     "a Directorate company in pursuit. Mafesto's Kinetic Transfer System proves useless "
     "against unstable moving water; the crossing succeeds through rope-work, crew "
     "coordination, and Bane's own swimming."),
    (18, "what-stays-after-the-first-one", "What Stays After the First One", "LIII",
     "A seventeen-year-old recruit kills for the first time and is left numb; Bane counsels "
     "him privately, drawing on his own remembered first kill. First dedicated first-kill "
     "trauma/mentorship entry for this alias."),
    (18, "what-he-couldnt-be-in-two-places-for", "What He Couldn't Be in Two Places For", "LIV",
     "Two crises break simultaneously -- a poisoned well and an imminent ambush on a "
     "refugee column. Bane splits the column, trusting Maret Vos to run the interception "
     "alone; both succeed, but he admits the numbers won't always favor a split this "
     "cleanly. First genuine parallel dual-crisis dilemma. Closes wave 18."),
    (19, "the-council-that-asked-him-to-speak-plainly",
     "The Council That Asked Him to Speak Plainly", "LV",
     "A neutral cross-faction arbiter council summons Bane to answer fabricated and "
     "exaggerated atrocity claims; he testifies disarmed, answering honestly for real "
     "failures while refusing accusations the record doesn't support. First formal "
     "institutional/legal-tribunal register for this alias."),
    (19, "the-one-who-didnt-need-him-anymore", "The One Who Didn't Need Him Anymore", "LVI",
     "Passing through Threndale, the column discovers a thriving relief operation run by a "
     "woman freed two years earlier in an operation Bane barely remembers. She tells him "
     "plainly she doesn't need thanking or owing. A single-thread legacy/ripple-effect "
     "entry."),
    (19, "the-argument-halst-won", "The Argument Halst Won", "LVII",
     "Corren Halst openly and publicly opposes Bane's plan to strike a weakened garrison; "
     "the disagreement is settled by a polled vote among senior members rather than Bane's "
     "authority. Halst turns out to be right, establishing Bane's command isn't absolute. "
     "Closes wave 19."),
]

assert len(ENTRIES) == 9


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 215, 2026-09-11 (`MCD-{mcd_id}`). Bane Alias Chronicle "
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
    start = 933
    new_rules = []
    for i, (wave, filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), Bane "
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
        "batch": 215,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks Bane's seventeenth through nineteenth Alias Chronicle waves (MCD-933 "
            "through MCD-941, 9 rules). " + BATCH_NOTE
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
