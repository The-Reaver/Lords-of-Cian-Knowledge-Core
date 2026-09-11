#!/usr/bin/env python3
"""Batch 201: Lock the Crow King's sixth through fifteenth Alias Chronicle waves
(MCD-831 through MCD-860, 30 rules / 10 waves)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "I want you to do the sixth wave plus nine more waves for all the aliases '
    'continuously, uninterrupted, this includes rigorous testing to ensure no contradictions '
    'or errors, committing and pushing to origin Main, and please make sure that all '
    'Chronicles are styled inside of the Google Drive and organized neatly where every '
    'territory everybody that has their own Chronicle entry is in a separate folder entirely."'
)

ROMAN = ["XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV",
         "XXVI", "XXVII", "XXVIII", "XXIX", "XXX", "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV",
         "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL", "XLI", "XLII", "XLIII", "XLIV", "XLV"]

ENTRIES = [
    ("the-bridge-that-wasnt-there", "The Bridge That Wasn't There", 6,
     "The first river-crossing evasion; establishes water's acoustic-folding as a new "
     "terrain type distinct from marsh, highland, or urban."),
    ("what-the-city-walls-repeated", "What the City Walls Repeated", 6,
     "The first urban, walled-settlement deception, exploiting stone-street echo geometry "
     "rather than pure vocal craft."),
    ("the-old-womans-crow-king", "The Old Woman's Crow King", 6,
     "Closes the wave via an uninvolved civilian's folk-tale account, reflecting on why "
     "exaggerated legend persists."),
    ("the-crown-that-wasnt-his", "The Crown That Wasn't His", 7,
     "A bandit company weaponizes the Crow King symbol itself against villages; resolved "
     "without violence."),
    ("one-voice-one-gate", "One Voice, One Gate", 7,
     "The smallest-scale operation of the run -- one man, one guard, one sentence."),
    ("what-voris-tried-to-become", "What Voris Tried to Become", 7,
     "Commandant Voris personally tests his own \"unpredictability\" doctrine and discovers "
     "its institutional cost."),
    ("the-voice-among-their-own", "The Voice Among Their Own", 8,
     "Trained listening turned toward catching an informant within Kanja's own crew."),
    ("what-she-wouldnt-say", "What She Wouldn't Say", 8,
     "The apprentice singer, captured and interrogated, resists via silence rather than "
     "lies."),
    ("the-students-first-failure", "The Student's First Failure", 8,
     "The apprentice's own student misjudges timing in the field -- the first lineage "
     "mistake, handled through accountability."),
    ("the-one-they-couldnt-warn", "The One They Couldn't Warn", 9,
     "A knowingly-chosen, not accidental, cost to an uninvolved bystander."),
    ("when-the-plan-broke-mid-song", "When the Plan Broke Mid-Song", 9,
     "A wind shift forces real-time improvisation mid-Braid."),
    ("the-voices-that-only-listened", "The Voices That Only Listened", 9,
     "Pure eavesdropping and reconnaissance with zero deception."),
    ("the-man-who-could-not-hear", "The Man Who Could Not Hear", 10,
     "A deaf commander forces adaptation into written and visual deception."),
    ("the-negotiation-without-a-single-lie", "The Negotiation Without a Single Lie", 10,
     "A formal parley won via verified truth as leverage, no deception at all."),
    ("what-the-silence-taught-them", "What the Silence Taught Them", 10,
     "The apprentice synthesizes that the craft was never really vocal at its core."),
    ("before-the-marsh", "Before the Marsh", 11,
     "A flashback to an embarrassing early experiment among Kanja's earliest crew, "
     "predating the Wetlands scarecrow trick."),
    ("what-the-hounds-heard", "What the Hounds Heard", 11,
     "Tracking hounds hear frequencies outside human-calibrated design, nearly exposing an "
     "operation."),
    ("the-story-corren-halst-still-told", "The Story Corren Halst Still Told", 11,
     "Corren Halst's retrospective on why the wave-11 failure story matters more than the "
     "famous marsh trick."),
    ("the-report-that-named-the-wrong-man", "The Report That Named the Wrong Man", 12,
     "An unrelated cell's sabotage gets pinned on him by honest mistake; resolved via "
     "counter-proof."),
    ("the-signal-before-the-storm-of-steel", "The Signal Before the Storm of Steel", 12,
     "Deception and Trinity combat are planned together as one single operation from the "
     "start."),
    ("what-she-taught-him-back", "What She Taught Him Back", 12,
     "The apprentice teaches Kanja a non-deceptive, morale-building use of the same "
     "technique."),
    ("the-village-that-walked-out-singing", "The Village That Walked Out Singing", 13,
     "A civilian evacuation disguised as an open festival procession."),
    ("the-game-neither-of-them-won", "The Game Neither of Them Won", 13,
     "The first genuine draw -- a blanket-skepticism tactician defeats the deception but is "
     "equally blind to real intelligence."),
    ("the-third-voice-she-never-expected", "The Third Voice She Never Expected", 13,
     "The apprentice's student begins teaching her own student -- a third generation of the "
     "craft."),
    ("the-children-who-played-crow-king", "The Children Who Played Crow King", 14,
     "Children's inaccurate reenactment of the legend raises real-world risk."),
    ("the-win-he-wouldnt-take", "The Win He Wouldn't Take", 14,
     "Deliberate restraint against an already-beaten, legitimate target."),
    ("what-voris-heard-secondhand", "What Voris Heard Secondhand", 14,
     "Commandant Voris recognizes restraint, not just cunning, as central to the method."),
    ("the-night-five-provinces-moved-at-once", "The Night Five Provinces Moved at Once", 15,
     "The largest coordinated operation of the run -- five techniques run simultaneously by "
     "five practitioners across five provinces."),
    ("what-the-craft-had-become", "What the Craft Had Become", 15,
     "A quiet valedictory reflection between Kanja and the apprentice on the craft "
     "outgrowing him."),
    ("the-last-scarecrow", "The Last Scarecrow", 15,
     "A full-circle closer -- Commandant Voris receives a final scarecrow and recognizes "
     "the craft has become a discipline larger than any one practitioner, closing the "
     "ten-wave run."),
]

assert len(ENTRIES) == 30


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 201, 2026-09-11 (`MCD-{mcd_id}`). The Crow King Alias "
        f"Chronicle {roman}, wave {wave} of the ten-wave sixth-through-fifteenth run. Not a "
        f"territory Chronicle. Narrated in neutral third-person prose.*"
    )
    new_text, n = pattern.subn(replacement, text, count=1)
    assert n == 1, f"header pattern not found/replaced in {filename}"
    with open(path, "w") as f:
        f.write(new_text)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    start = 831
    new_rules = []
    for i, (filename, title, wave, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        roman = ROMAN[i]
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The Crow "
                f"King Alias Chronicle {roman}, wave {wave} of ten (waves 6-15). {summary}"
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
        "batch": 201,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Crow King's sixth through fifteenth Alias Chronicle waves (MCD-831 "
            "through MCD-860, 30 rules, 10 waves of 3). " + BATCH_NOTE
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
