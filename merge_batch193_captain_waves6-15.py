#!/usr/bin/env python3
"""Batch 193: Lock Captain's sixth through fifteenth Alias Chronicle waves
(MCD-591 through MCD-620, 30 rules / 10 waves)."""
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
    ("the-family-waiting-at-the-dock", "The Family Waiting at the Dock", 6,
     "Danne Sok brings his wife and daughter to meet Kanja, establishing that crew families "
     "form their own independent impression of him, distinct from battlefield reputation."),
    ("the-dispute-he-let-them-settle", "The Dispute He Let Them Settle", 6,
     "Kanja refers a crew quarrel to a newly-founded crew dispute council rather than ruling "
     "himself, deliberately building institutional trust that doesn't depend on his presence."),
    ("the-night-maret-vos-almost-walked", "The Night Maret Vos Almost Walked", 6,
     "Maret Vos tries to leave for good out of guilt/debt; Kanja lets her go freely, refusing "
     "to convert loyalty into obligation."),
    ("the-call-he-got-wrong", "The Call He Got Wrong", 7,
     "Kanja overrides Corren Halst's tidal read, gets it wrong, and publicly institutes a "
     "self-correction rule (\"say so twice\") rather than letting pride stand."),
    ("the-hand-that-never-opened-to-him", "The Hand That Never Opened to Him", 7,
     "A years-long crew member who never converts to warmth despite fair treatment, "
     "establishing the honest limit of the \"earned trust\" ethos."),
    ("the-day-they-carried-him", "The Day They Carried Him", 7,
     "First inversion: the crew physically cares for an exhausted, depleted Kanja instead of "
     "the reverse."),
    ("the-grandchild-who-wanted-the-old-stories", "The Grandchild Who Wanted the Old Stories", 8,
     "An elderly Garren Hask's great-grandniece hears the origin story firsthand, showing the "
     "legend passing to a third generation."),
    ("the-defector-who-chose-the-name", "The Defector Who Chose the Name", 8,
     "A Trust sailor defects specifically because of the Iron Shallows rescue story, then is "
     "slow-proven like any recruit."),
    ("the-ship-they-laid-to-rest", "The Ship They Laid to Rest", 8,
     "The Audit is ceremonially decommissioned rather than scrapped, with Hask, Efa Gol, and "
     "Breck each contributing a memory."),
    ("the-winter-the-stores-ran-thin", "The Winter the Stores Ran Thin", 9,
     "A supply crisis is solved through crew ideas and accumulated community goodwill, with "
     "Kanja deliberately not deciding anything himself."),
    ("the-fever-that-took-the-night-watch", "The Fever That Took the Night Watch", 9,
     "Kanja does ordinary nursing labor through the night for a sick sailor -- no Trinity "
     "function applies."),
    ("the-table-where-the-crew-spoke-for-themselves",
     "The Table Where the Crew Spoke for Themselves", 9,
     "Kanja lets three crew members negotiate a settlement alliance while he stays silent, "
     "building their standing rather than his own."),
    ("the-accusation-he-let-them-judge", "The Accusation He Let Them Judge", 10,
     "A merchant falsely accuses the crew of skimming relief supplies; the crew's own council "
     "and ledger clear it, not Kanja's word."),
    ("the-voice-that-wasnt-who-it-claimed", "The Voice That Wasn't Who It Claimed", 10,
     "A trusted crew member is found passing information under duress (family held hostage); "
     "resolved with mercy and rescue rather than punishment."),
    ("the-trade-he-offered-himself-for", "The Trade He Offered Himself For", 10,
     "Kanja becomes an unguarded hostage himself to secure three captured crew members' "
     "release, and honors the terms even though he could break them."),
    ("the-day-they-named-for-remembering", "The Day They Named for Remembering", 11,
     "The crew founds an annual remembrance day for the Black Trench dead, becoming a lasting "
     "tradition."),
    ("the-vote-that-named-the-third-ship", "The Vote That Named the Third Ship", 11,
     "Garren Hask deliberately hands ship-naming to a crew vote instead of keeping it as his "
     "own honor."),
    ("the-officers-who-didnt-need-him-there", "The Officers Who Didn't Need Him There", 11,
     "Kanja formally trains non-Trinity crew in independent command; Corren Halst successfully "
     "leads a split engagement without him."),
    ("the-grief-he-kept-until-morning", "The Grief He Kept Until Morning", 12,
     "Efa Gol finds Kanja's private grief after he held composure for the crew all day."),
    ("the-question-he-couldnt-answer-for-her", "The Question He Couldn't Answer for Her", 12,
     "Kanja sits with a crew member's moral injury after a kill, offering presence rather than "
     "resolution."),
    ("the-anniversary-callum-breck-still-kept", "The Anniversary Callum Breck Still Kept", 12,
     "Decades later, Breck invites Kanja to his private, individual Nev Torr remembrance for "
     "the first time."),
    ("the-mission-he-said-she-wasnt-ready-for", "The Mission He Said She Wasn't Ready For", 13,
     "Kanja repeatedly refuses to assign an eager, qualified crew member to a high-risk "
     "mission over a safety concern, until she proves it resolved."),
    ("the-order-he-reversed-in-front-of-everyone",
     "The Order He Reversed in Front of Everyone", 13,
     "A junior sailor publicly corrects a live tactical order; Kanja reverses instantly and "
     "without defensiveness."),
    ("the-old-hand-who-refused-to-stop", "The Old Hand Who Refused to Stop", 13,
     "An aging, wounded veteran insists on keeping a real duty rotation; Kanja respects his "
     "autonomy over his own safety concerns."),
    ("the-child-nobody-else-went-back-for", "The Child Nobody Else Went Back For", 14,
     "Kanja personally wades out to save one drowning child at a settlement, unconnected to "
     "any campaign."),
    ("the-ordinary-day-the-manifest-remembered", "The Ordinary Day the Manifest Remembered", 14,
     "A mundane resupply day spent hauling crates and fixing a ledger error, showing "
     "consistency without an audience."),
    ("the-storm-with-no-enemy-in-it", "The Storm With No Enemy in It", 14,
     "The crew does pure disaster-relief labor, no Trinity, during a natural storm with no "
     "combat involved."),
    ("everyone-who-ever-sailed-under-the-name", "Everyone Who Ever Sailed Under the Name", 15,
     "A formal census reveals thousands have served under the name across the decades, a "
     "scale reflection using the crew's ledger tradition."),
    ("the-word-they-wouldnt-let-him-mock", "The Word They Wouldn't Let Him Mock", 15,
     "A captured Directorate officer mocks the name; the crew, not Kanja, collectively "
     "defends and defines what it means."),
    ("what-efa-gol-told-the-newest-ones", "What Efa Gol Told the Newest Ones", 15,
     "An elderly Efa Gol inducts a new recruit generation into the alias's meaning, closing "
     "the ten-wave run on a self-perpetuating, unresolved note."),
]

assert len(ENTRIES) == 30


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 193, 2026-09-11 (`MCD-{mcd_id}`). Captain Alias Chronicle "
        f"{roman}, wave {wave} of the ten-wave sixth-through-fifteenth run. Not a territory "
        f"Chronicle. Narrated in neutral third-person prose.*"
    )
    new_text, n = pattern.subn(replacement, text, count=1)
    assert n == 1, f"header pattern not found/replaced in {filename}"
    with open(path, "w") as f:
        f.write(new_text)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    start = 591
    new_rules = []
    for i, (filename, title, wave, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        roman = ROMAN[i]
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), Captain "
                f"Alias Chronicle {roman}, wave {wave} of ten (waves 6-15). {summary}"
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
        "batch": 193,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks Captain's sixth through fifteenth Alias Chronicle waves (MCD-591 through "
            "MCD-620, 30 rules, 10 waves of 3). " + BATCH_NOTE
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
