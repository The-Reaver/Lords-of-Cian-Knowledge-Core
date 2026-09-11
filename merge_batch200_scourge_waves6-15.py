#!/usr/bin/env python3
"""Batch 200: Lock the Scourge's sixth through fifteenth Alias Chronicle waves
(MCD-801 through MCD-830, 30 rules / 10 waves)."""
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
    ("the-town-that-was-already-afraid", "The Town That Was Already Afraid", 6,
     "Age 36, V1 gear. A port militia, primed by wild rumor, nearly attacks freed captives; "
     "the Scourge de-escalates through calm honesty, establishing the legend as a liability "
     "as well as an asset."),
    ("the-caravan-road", "The Caravan Road", 6,
     "Age 44, V2 gear. The first-ever land-based liberation, an inland caravan route, a "
     "full gear showcase off water for the first time."),
    ("the-roads-she-started-mapping", "The Roads She Started Mapping", 6,
     "Age 68, V2 gear. A freed captive from the caravan, grown up, has independently built "
     "a safe-route cartography network with no dependence on him -- a generational "
     "ripple-effect closer."),
    ("the-one-who-didnt-wake-again", "The One Who Didn't Wake Again", 7,
     "Age 95, V3 gear. A rescued captive dies of prior suffering despite a clean, fast "
     "rescue, dramatizing the limits of \"in time.\""),
    ("the-net-built-to-catch-him", "The Net Built to Catch Him", 7,
     "Age 112, V3 gear. A strategist spends years cataloguing his patterns and builds a "
     "six-ship decoy trap; he escapes by having grown unpredictable."),
    ("the-harbor-that-wouldnt-take-them", "The Harbor That Wouldn't Take Them", 7,
     "Age 128, V3 gear. Pure diplomatic negotiation to secure harbor for 206 freed captives, "
     "resolved through leverage and existing trade ties, no combat."),
    ("what-efa-gol-handed-down", "What Efa Gol Handed Down", 8,
     "Age 150, V3 gear. Efa Gol steps back from decoy command as her instincts slow, "
     "handing off cleanly before failure."),
    ("the-blade-at-the-captives-throat", "The Blade at the Captive's Throat", 8,
     "Age 138, V3 gear. A hostage standoff resolved through six minutes of deliberate "
     "patience, not force."),
    ("the-game-the-freed-children-played", "The Game the Freed Children Played", 8,
     "Age 165, V3 gear. Anonymous observation of children reenacting a drifted, distorted "
     "version of the legend as a street game."),
    ("when-the-coat-didnt-answer", "When the Coat Didn't Answer", 9,
     "Age 178, V3 gear. A novel Drakma-charged weapon defeats the Forge-Coat's grounding "
     "weave outright; falls back to plain swordsmanship."),
    ("the-first-night-in-the-new-coat", "The First Night in the New Coat", 9,
     "Age 241, V4 debut. The new gear's rough, unglamorous first deployment, teething "
     "failures included."),
    ("the-reef-he-didnt-know", "The Reef He Didn't Know", 9,
     "Age 255, V4 gear. Matured V4 sensory gear reads a wholly unfamiliar reef system on "
     "the first pass."),
    ("the-weight-the-mask-kept-count-of", "The Weight the Mask Kept Count Of", 10,
     "Age 305, V4 gear. Pure interiority; Kanja alone totals the toll of 283 years under "
     "one persona."),
    ("the-isle-that-stopped-needing-him", "The Isle That Stopped Needing Him", 10,
     "Age 290, V4 gear. A region cleared decades earlier is now fully self-sufficient -- "
     "quiet obsolescence."),
    ("the-last-ledger-line", "The Last Ledger Line", 10,
     "Age 300, V4 gear. Garren Hask's lifetime numeric tally of everyone freed (211,406, "
     "\"a floor, not a ceiling\")."),
    ("the-captain-who-surrendered-nothing", "The Captain Who Surrendered Nothing", 11,
     "Age 70, V2 gear. A defeated captain refuses surrender itself, choosing near-suicide "
     "over capitulation; resolved through restraint."),
    ("the-chain-that-freed-itself", "The Chain That Freed Itself", 11,
     "Age 62, V2 gear. Captives break free mid-raid and fight alongside him as active "
     "combatants, not passive rescued."),
    ("what-the-captains-son-remembered", "What the Captain's Son Remembered", 11,
     "A retrospective set decades later, age 130: the defeated captain's son reflects on "
     "grief and blame; the Scourge is absent from the page."),
    ("the-flag-flown-without-permission", "The Flag Flown Without Permission", 12,
     "Age 55, V2 gear. A resistance camp flies a fabricated banner using his name and "
     "likeness in a strait he's never sailed."),
    ("the-impostors-undoing", "The Impostor's Undoing", 12,
     "Age 133, V3 gear. A false claimant is exposed via careful documentation, not "
     "confrontation."),
    ("the-village-that-never-needed-saving", "The Village That Never Needed Saving", 12,
     "Age 100, V3 gear. A village organizes effective self-defense from rumor alone, with "
     "zero direct involvement from him, ever."),
    ("the-market-that-rebuilt-itself", "The Market That Rebuilt Itself", 13,
     "Age 145, V3 gear. A destroyed slaving hub simply relocates forty miles away, "
     "confronting the limits of force against demand."),
    ("the-convoy-escort-he-couldnt-outpace", "The Convoy Escort He Couldn't Outpace", 13,
     "Age 160, V3 gear. A four-day pursuit and attrition chase ending in partial, not "
     "total, success."),
    ("the-merchant-who-changed-his-trade", "The Merchant Who Changed His Trade", 13,
     "Age 170, V3 gear. A slaver voluntarily converts to legitimate trade under collapsing "
     "economics."),
    ("the-meal-he-ate-as-no-one", "The Meal He Ate as No One", 14,
     "Age 108, V3 gear, unmasked. Anonymous in a tavern, overhearing his own distorted "
     "legend."),
    ("the-storm-he-waited-out-like-anyone-else", "The Storm He Waited Out Like Anyone Else", 14,
     "Age 90, V3 gear, unmasked. Stranded by weather, passes days as an ordinary sailor."),
    ("what-he-taught-without-the-mask-on", "What He Taught Without the Mask On", 14,
     "Age 118, V3 gear, unmasked. Off-duty mentorship teaching knots and wind-reading, no "
     "reference to the persona."),
    ("the-night-he-almost-didnt-go", "The Night He Almost Didn't Go", 15,
     "Age 250, V4 gear. Genuine hesitation from accumulated exhaustion before a mission."),
    ("the-fight-he-fought-angry", "The Fight He Fought Angry", 15,
     "Age 168, V3 gear. A rare loss of composure and fury after captives are murdered to "
     "destroy evidence; a near-overreach checked by his successor."),
    ("the-question-efa-gol-finally-asked", "The Question Efa Gol Finally Asked", 15,
     "Age 180, V3 gear. Efa Gol directly asks if he regrets the persona; left deliberately "
     "unresolved, closing the ten-wave run."),
]

assert len(ENTRIES) == 30


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 200, 2026-09-11 (`MCD-{mcd_id}`). The Scourge Alias Chronicle "
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
    start = 801
    new_rules = []
    for i, (filename, title, wave, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        roman = ROMAN[i]
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The "
                f"Scourge Alias Chronicle {roman}, wave {wave} of ten (waves 6-15). {summary}"
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
        "batch": 200,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Scourge's sixth through fifteenth Alias Chronicle waves (MCD-801 "
            "through MCD-830, 30 rules, 10 waves of 3). " + BATCH_NOTE
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
