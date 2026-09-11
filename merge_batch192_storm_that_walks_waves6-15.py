#!/usr/bin/env python3
"""Batch 192: Lock the Storm That Walks' sixth through fifteenth Alias Chronicle waves
(MCD-561 through MCD-590, 30 rules / 10 waves), under Abad's blanket authorization to
continue uninterrupted through ten more waves for every alias."""
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

# (filename, title, wave, one-paragraph summary)
ENTRIES = [
    ("the-days-without-wind", "The Days Without Wind", 6,
     "A two-week dead calm gives Sephtis nothing to forecast; a blockade-runner interception "
     "is decided by pure rowed endurance instead of any storm-timing edge, establishing the "
     "doctrine's core limit: it needs weather to exist."),
    ("the-fight-with-nowhere-to-hide", "The Fight With Nowhere to Hide", 6,
     "Full daylight, no storm cover -- Onyx adapts Whisper of Shadows to stillness instead of "
     "rain, Mafesto and Obsidian Malice fight fully visible, proving the Trinity isn't "
     "dependent on weather to be dangerous."),
    ("what-she-called-before-the-silence", "What She Called Before the Silence", 6,
     "Sephtis's successor makes her first forecast of an absence of weather -- a genuinely new "
     "kind of call, deepening her arc as his trained successor."),
    ("the-man-who-called-him-a-liar", "The Man Who Called Him a Liar", 7,
     "A Trust weather-service director publicly disputes the doctrine's legitimacy; settled by "
     "a verified public wager rather than combat."),
    ("the-tide-that-turned-twice", "The Tide That Turned Twice", 7,
     "A Trinity showcase using a predicted tidal surge, not a storm, at a river-mouth garrison "
     "-- a new coastal environment for the doctrine."),
    ("what-the-rival-came-back-to-learn", "What the Rival Came Back to Learn", 7,
     "The defeated rival forecaster returns to genuinely study the method, extending its "
     "institutional reach for the first time."),
    ("the-fleet-built-to-ignore-the-sky", "The Fleet Built to Ignore the Sky", 8,
     "A Trust squadron purpose-built and drilled to neutralize storm-timing outright -- the "
     "first full repulsion of the core tactic."),
    ("what-the-hardened-crews-stopped-fearing", "What the Hardened Crews Stopped Fearing", 8,
     "A Trinity showcase exploiting the storm-hardened squadron's own overconfidence: their "
     "storm-hardening made them stop watching for a threat, not just weather."),
    ("the-captain-who-trusted-his-ballast", "The Captain Who Trusted His Ballast", 8,
     "The defeated commander's reflective account distinguishing his engineering success from "
     "his tactical defeat."),
    ("the-village-that-listened-to-the-sky", "The Village That Listened to the Sky", 9,
     "A fishing settlement outside any conflict receives the same forecasting service, "
     "establishing pure civilian-protection use of the doctrine."),
    ("the-boats-that-didnt-come-in", "The Boats That Didn't Come In", 9,
     "A rescue showcase using Mafesto during the storm itself, with a real, uncompensated loss "
     "-- one fisherman -- rather than a clean save."),
    ("the-old-woman-who-read-the-gulls", "The Old Woman Who Read the Gulls", 9,
     "A village elder's independent folk-forecasting method is integrated as a genuine "
     "complementary practice, seeding a bottom-up forecasting network."),
    ("the-envoy-who-asked-the-wrong-price", "The Envoy Who Asked the Wrong Price", 10,
     "A foreign delegation tries to buy exclusive rights to the storm-timing method, then "
     "attempts espionage when refused."),
    ("what-the-storm-exposed", "What the Storm Exposed", 10,
     "A Trinity showcase foiling the embedded agent's theft attempt during an actual "
     "predicted storm."),
    ("what-he-chose-to-share", "What He Chose to Share", 10,
     "Sephtis and Kanja settle on a case-by-case sharing policy for a second, non-hostile "
     "delegation."),
    ("the-season-without-a-single-storm", "The Season Without a Single Storm", 11,
     "A three-month blockade with no forecastable storm strains crew morale and discipline."),
    ("what-three-months-bought-in-one-night", "What Three Months Bought in One Night", 11,
     "A full Trinity showcase when the storm finally arrives, resolving the siege in one "
     "night."),
    ("what-the-waiting-cost-the-ones-who-held-the-line",
     "What the Waiting Cost the Ones Who Held the Line", 11,
     "The doubting officer's reconciliation, honoring the real cost of the three-month wait "
     "rather than erasing it."),
    ("the-storm-he-chose-not-to-use", "The Storm He Chose Not to Use", 12,
     "Two simultaneous storms, only one usable; Kanja must choose which allied fleet gets the "
     "advantage."),
    ("the-storm-nobody-called", "The Storm Nobody Called", 12,
     "The unchosen allied squadron fights the same storm unaided and takes real losses."),
    ("what-they-chose-between-two-fleets", "What They Chose Between Two Fleets", 12,
     "Sephtis's successor builds a formal triage framework in response to the two-storm "
     "dilemma, a genuine doctrine-building contribution of her own."),
    ("what-the-rain-was-timed-to-cover", "What the Rain Was Timed to Cover", 13,
     "The doctrine's first inland application: predicted river flooding enables a stalled "
     "siege crossing."),
    ("the-ground-that-moved-with-the-water", "The Ground That Moved With the Water", 13,
     "A Trinity showcase exploiting rising floodwater against a garrison's fixed earthworks."),
    ("the-engineer-who-learned-to-read-weather-like-ground",
     "The Engineer Who Learned to Read Weather Like Ground", 13,
     "Sephtis and a siege engineer cross-pollinate weather-reading and structural engineering."),
    ("the-officer-who-refused-to-sail-into-it", "The Officer Who Refused to Sail Into It", 14,
     "A veteran officer within Kanja's own fleet formally refuses a storm-timed order."),
    ("what-the-chart-didnt-show", "What the Chart Didn't Show", 14,
     "A Trinity showcase recovering from a genuine forecast blind spot: a storm-shifted shoal "
     "no chart showed."),
    ("what-they-added-to-the-method", "What They Added to the Method", 14,
     "Local pilotage knowledge is formally folded into the doctrine, reconciling with the "
     "officer who refused the earlier order."),
    ("the-fleet-she-called-alone", "The Fleet She Called Alone", 15,
     "Decades later, an elderly Sephtis retires; his successor forecasts an entire fleet "
     "action alone for the first time."),
    ("the-order-he-didnt-question", "The Order He Didn't Question", 15,
     "A full Trinity showcase committed entirely on the successor's unverified forecast -- a "
     "trust-test with no safety net."),
    ("what-the-fleet-learned-from-a-man-who-read-the-sky",
     "What the Fleet Learned From a Man Who Read the Sky", 15,
     "A generations-later retrospective: the storm-timing doctrine has become permanent "
     "institutional naval practice, closing the ten-wave run."),
]

assert len(ENTRIES) == 30


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 192, 2026-09-11 (`MCD-{mcd_id}`). The Storm That Walks Alias "
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
    start = 561
    new_rules = []
    for i, (filename, title, wave, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        roman = ROMAN[i]
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), the Storm "
                f"That Walks Alias Chronicle {roman}, wave {wave} of ten (waves 6-15). "
                f"{summary}"
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
        "batch": 192,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Storm That Walks' sixth through fifteenth Alias Chronicle waves "
            "(MCD-561 through MCD-590, 30 rules, 10 waves of 3). " + BATCH_NOTE
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
