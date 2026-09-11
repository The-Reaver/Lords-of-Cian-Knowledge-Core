#!/usr/bin/env python3
"""Batch 199: Lock the Sovereign Ghost of the Great Sea's sixth through fifteenth Alias
Chronicle waves (MCD-771 through MCD-800, 30 rules / 10 waves)."""
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
    ("the-storm-they-didnt-make", "The Storm They Didn't Make", 6,
     "Fisherfolk credit the fleet with taming storms; Kanja corrects the myth and gives Dol "
     "Maren's real weather-reading method away rather than let false hope get someone "
     "killed."),
    ("what-the-reef-wanted-to-take", "What the Reef Wanted to Take", 6,
     "False channel markers lure the fleet toward a reef ambush; Dol Maren's hull-reading "
     "escapes it, then they turn the trap on the Trust force that set it."),
    ("ten-ships-that-were-one", "Ten Ships That Were One", 6,
     "Efa Gol rigs a single hull to read as a ten-ship squadron, deterring a raid on a "
     "merchant convoy with zero combat."),
    ("the-captain-who-didnt-believe-in-ghosts", "The Captain Who Didn't Believe in Ghosts", 7,
     "A skeptical Trust captain refuses the reputation and forces real, openly-fought "
     "combat -- the alias's first reputation failure."),
    ("air-enough-for-six", "Air Enough for Six", 7,
     "A pure technical rescue: six sailors freed from a sinking merchant hull's shrinking "
     "air pocket, no combat."),
    ("what-pell-ostra-cleared", "What Pell Ostra Cleared", 7,
     "Pell Ostra clears eleven scuttled hulks strangling a fishing harbor, including a live "
     "mid-operation correction."),
    ("terms-without-blood", "Terms Without Blood", 8,
     "A neutral privateer coalition negotiates safe passage through witnessed spoken terms, "
     "no paper, no combat."),
    ("the-wind-she-read-better", "The Wind She Read Better", 8,
     "A pure sailing duel with zero Trinity powers: Dol Maren out-navigates a faster Trust "
     "courier ship."),
    ("what-danne-sok-charted", "What Danne Sok Charted", 8,
     "Danne Sok's patient route and patrol-pattern charting, the unglamorous logistics "
     "sustaining the fleet's elusiveness."),
    ("the-toll-he-refused-to-take", "The Toll He Refused to Take", 9,
     "The fleet lets a legitimate Trust humanitarian convoy pass untouched rather than "
     "validate propaganda by seizing it."),
    ("the-night-the-coast-held", "The Night the Coast Held", 9,
     "A full combined Trinity showcase defending an undefended civilian town from "
     "non-Trust raiders."),
    ("the-chart-the-enemy-couldnt-steal", "The Chart the Enemy Couldn't Steal", 9,
     "Corren Halst thwarts an infiltrator trying to steal Danne Sok's charts."),
    ("what-the-rumor-cost-them", "What the Rumor Cost Them", 10,
     "The reputation's first unintended harm: an innocent ship mistaken for the fleet and "
     "fired on by a panicked patrol."),
    ("the-strait-that-ate-the-light", "The Strait That Ate the Light", 10,
     "A three-day fog-bound running engagement won through environmental attrition rather "
     "than a decisive battle."),
    ("where-the-captives-went", "Where the Captives Went", 10,
     "Maret Vos, years later, visits the settlement built by the slaver-ship captives freed "
     "in an earlier wave."),
    ("the-ships-that-borrowed-his-name", "The Ships That Borrowed His Name", 11,
     "A fishing village borrows the ghost-fleet mythology for its own protection; Kanja "
     "lets it stand."),
    ("the-convoy-caught-between-two-flags", "The Convoy Caught Between Two Flags", 11,
     "Extracting civilians from crossfire between two unrelated warring powers."),
    ("the-third-ship-garren-hask-named", "The Third Ship Garren Hask Named", 11,
     "Garren Hask names the fleet's third flagship, The Ledger."),
    ("the-officer-who-read-every-report", "The Officer Who Read Every Report", 12,
     "A Directorate analyst nearly out-predicts the fleet through patient pattern study "
     "alone."),
    ("what-fell-when-the-tower-did", "What Fell When the Tower Did", 12,
     "A vertical assault on a coastal watchtower, full gear/Trinity combination against a "
     "fixed structure."),
    ("the-decoys-efa-gol-never-used", "The Decoys Efa Gol Never Used", 12,
     "Efa Gol's notebook of decoy plans she deliberately chose never to use."),
    ("the-night-he-let-them-see-everything", "The Night He Let Them See Everything", 13,
     "The fleet abandons concealment entirely to reassure a terrorized village in full "
     "daylight."),
    ("the-thing-the-directorate-built-to-hunt-them",
     "The Thing the Directorate Built to Hunt Them", 13,
     "First non-human adversary: a fear-immune mechanical war-construct engineered to "
     "counter the anchor-chain weapon."),
    ("the-hull-dol-maren-wasnt-finished-with", "The Hull Dol Maren Wasn't Finished With", 13,
     "Dol Maren studies the captured construct's engineering into a genuine hull advance "
     "for The Ledger."),
    ("the-officer-the-ghost-cost-his-commission", "The Officer the Ghost Cost His Commission",
     14, "A Trust officer stripped of rank for truthfully reporting an earlier sighting; "
     "Kanja confirms it to him directly."),
    ("the-passenger-nobody-could-know-they-carried",
     "The Passenger Nobody Could Know They Carried", 14,
     "A silent stealth extraction of a political dissident through a Directorate blockade, "
     "no combat."),
    ("what-they-did-before-every-sailing", "What They Did Before Every Sailing", 14,
     "The crew's wordless pre-sailing ritual, traced to its origin after the Black Trench."),
    ("what-the-scholar-wasnt-allowed-to-prove", "What the Scholar Wasn't Allowed to Prove", 15,
     "A historian's accurate manuscript on the fleet, confirmed by Kanja, voluntarily "
     "shelved unpublished."),
    ("the-duel-off-the-sovereign-coast", "The Duel Off the Sovereign Coast", 15,
     "A formal flagship-vs-flagship duel decided by pure seamanship, zero Trinity powers."),
    ("the-gathering-at-the-ghost-fleets-anchorage",
     "The Gathering at the Ghost Fleet's Anchorage", 15,
     "A warm ensemble closer, all three flagships and the full established crew at anchor "
     "together, closing the ten-wave run."),
]

assert len(ENTRIES) == 30


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 199, 2026-09-11 (`MCD-{mcd_id}`). Sovereign Ghost of the "
        f"Great Sea Alias Chronicle {roman}, wave {wave} of the ten-wave "
        f"sixth-through-fifteenth run. Not a territory Chronicle. Narrated in neutral "
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
    start = 771
    new_rules = []
    for i, (filename, title, wave, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        roman = ROMAN[i]
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), Sovereign "
                f"Ghost of the Great Sea Alias Chronicle {roman}, wave {wave} of ten (waves "
                f"6-15). {summary}"
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
        "batch": 199,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Sovereign Ghost of the Great Sea's sixth through fifteenth Alias "
            "Chronicle waves (MCD-771 through MCD-800, 30 rules, 10 waves of 3). " +
            BATCH_NOTE
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
