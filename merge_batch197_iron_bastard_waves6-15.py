#!/usr/bin/env python3
"""Batch 197: Lock the Iron Bastard's sixth through fifteenth Alias Chronicle waves
(MCD-711 through MCD-740, 30 rules / 10 waves)."""
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
    ("the-ear-under-the-ice", "The Ear Under the Ice", 6,
     "First cold-climate application: ice muffles the resonance read; solved by cutting "
     "through to direct contact rather than fighting the interference."),
    ("the-vault-that-answered-nothing", "The Vault That Answered Nothing", 6,
     "A genuine doctrine-limit: an acoustically-deadened vault (felt/timber lining) defeats "
     "the read itself, resolved by falling back to plain siegecraft."),
    ("what-the-keeper-of-the-talisman-remembered", "What the Keeper of the Talisman Remembered",
     6, "Reflective closer: the Aegis-Talisman's original artificer recalls its "
     "calibration; no new mechanics asserted."),
    ("the-gate-that-was-also-a-door", "The Gate That Was Also a Door", 7,
     "A precision showcase distinguishing a tension-bearing gate from an adjacent "
     "non-tension archway during a refugee evacuation."),
    ("what-stood-between-him-and-the-metal", "What Stood Between Him and the Metal", 7,
     "A tactical countermeasure: the enemy builds a rubble screen to deny physical access; "
     "solved via a Trinity-covered approach."),
    ("the-engineer-who-changed-sides", "The Engineer Who Changed Sides", 7,
     "A Trust engineer defects, offering countermeasure schematics -- the first crack in "
     "institutional resistance to the doctrine."),
    ("the-weight-of-three-towers", "The Weight of Three Towers", 8,
     "A detailed siege-tower combat showcase using rope and timber tension, not pure metal."),
    ("the-room-he-wouldnt-bring-down", "The Room He Wouldn't Bring Down", 8,
     "An ethical-restraint entry: surgical targeting spares hostages and prisoners housed "
     "below an ammunition store."),
    ("the-second-student", "The Second Student", 8,
     "Generational transmission: the wave-4 student works solo successfully, confirming the "
     "doctrine's lasting growth beyond Kanja himself."),
    ("what-the-crawler-graveyard-taught-him", "What the Crawler Graveyard Taught Him", 9,
     "A near-miss entry: an ambush hidden among derelict Crawler wrecks is caught via "
     "doubled verification."),
    ("the-three-voices-in-one-hand", "The Three Voices in One Hand", 9,
     "A mechanic-deepening showcase: Mafesto, Obsidian Malice, and Onyx used as one "
     "simultaneous diagnostic network."),
    ("what-the-smith-heard-in-the-quiet", "What the Smith Heard in the Quiet", 9,
     "A warm closer: an anonymous civilian smith shares the same listening intuition the "
     "doctrine formalized."),
    ("the-doctrine-they-taught-their-own-engineers",
     "The Doctrine They Taught Their Own Engineers", 10,
     "A legacy entry: the general's report becomes standard Trust academy curriculum."),
    ("the-structure-that-wasnt-there-yet", "The Structure That Wasn't There Yet", 10,
     "A new technical case: diagnosing an unfinished, still-shifting bridge under "
     "construction."),
    ("what-the-wind-carried-instead-of-sound", "What the Wind Carried Instead of Sound", 10,
     "A sensory-limit entry: desert wind defeats airborne reading, solved via a direct-"
     "contact technique."),
    ("the-chain-that-held-two-ships-together", "The Chain That Held Two Ships Together", 11,
     "A naval-precision entry distinguishing two functionally identical boarding chains by "
     "role, not material."),
    ("the-failure-he-didnt-catch-in-time", "The Failure He Didn't Catch in Time", 11,
     "A dark-cost entry: the first fatal misdiagnosis, establishing a permanent new "
     "verification protocol."),
    ("what-the-widow-asked-him", "What the Widow Asked Him", 11,
     "A heavy aftermath entry: the victim's widow confronts him; deliberately unresolved, no "
     "forgiveness granted."),
    ("the-twelve-locks-of-the-vault-door", "The Twelve Locks of the Vault Door", 12,
     "The first non-destructive use of the doctrine: precision extraction opening a "
     "multi-lock vault intact."),
    ("the-council-that-wanted-the-method-banned", "The Council That Wanted the Method Banned",
     12, "An institutional/political entry: the general defends the doctrine's legitimacy "
     "before a Trust council."),
    ("the-apprentice-who-heard-too-much", "The Apprentice Who Heard Too Much", 12,
     "A new limit: the doctrine's real cognitive/sensory toll on a hastily-taught "
     "volunteer."),
    ("the-fortress-with-no-metal-at-all", "The Fortress With No Metal At All", 13,
     "A full-scale test of the beyond-metal generalization against an all-rope/timber/stone "
     "fortress."),
    ("the-crawler-that-listened-back", "The Crawler That Listened Back", 13,
     "A real-risk escalation: a feedback-emitter Crawler injures Kanja through the Talisman "
     "itself."),
    ("what-the-generals-successor-inherited", "What the General's Successor Inherited", 13,
     "A legacy-continuity closer: the general dies of natural causes; his successor carries "
     "the report forward."),
    ("the-nine-bridges-in-one-night", "The Nine Bridges in One Night", 14,
     "A large-scale logistics entry: nine coordinated bridge collapses, six executed by "
     "trained sappers working from written notes."),
    ("the-one-who-faked-the-sound", "The One Who Faked the Sound", 14,
     "A deception-by-bait entry: an ambush fakes structural distress sounds, caught via "
     "experiential judgment rather than instrumentation."),
    ("what-the-boy-understood-before-the-words-came",
     "What the Boy Understood Before the Words Came", 14,
     "A small warm closer: an unnamed child shows an unexplained intuitive sensitivity to "
     "structures."),
    ("the-last-wall-of-the-old-foundry", "The Last Wall of the Old Foundry", 15,
     "A new technical register: stabilizing and guiding an already-collapsing structure to "
     "safely free trapped laborers."),
    ("the-doctrine-he-never-finished-teaching", "The Doctrine He Never Finished Teaching", 15,
     "A bittersweet reflection: the student asks why the doctrine exists; Kanja admits the "
     "reasoning was never fully finished, even for himself."),
    ("what-the-ear-remembers-after-the-war", "What the Ear Remembers After the War", 15,
     "A capstone closer: the Trust scholar and Kanja survey the doctrine's whole ten-wave "
     "arc together."),
]

assert len(ENTRIES) == 30


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 197, 2026-09-11 (`MCD-{mcd_id}`). The Iron Bastard Alias "
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
    start = 711
    new_rules = []
    for i, (filename, title, wave, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        roman = ROMAN[i]
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The Iron "
                f"Bastard Alias Chronicle {roman}, wave {wave} of ten (waves 6-15). {summary}"
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
        "batch": 197,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Iron Bastard's sixth through fifteenth Alias Chronicle waves "
            "(MCD-711 through MCD-740, 30 rules, 10 waves of 3). " + BATCH_NOTE
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
