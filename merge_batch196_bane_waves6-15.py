#!/usr/bin/env python3
"""Batch 196: Lock Bane's sixth through fifteenth Alias Chronicle waves
(MCD-681 through MCD-710, 30 rules / 10 waves)."""
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
    ("the-rumor-he-never-corrected", "The Rumor He Never Corrected", 6,
     "A false story of a massacre attributed to Bane (actually a fever outbreak) is spreading "
     "and helping recruitment; Bane insists on correcting it publicly even at real "
     "recruitment cost, establishing his reputation only holds if every claim is literally "
     "true."),
    ("what-the-bad-map-cost", "What the Bad Map Cost", 6,
     "Bane acts on stale, unverified intelligence and nearly walks a 40-person column into "
     "an ambush; he catches it in time but owns the mistake, instituting mandatory "
     "independent cross-checking of intelligence -- his first genuine tactical misjudgment."),
    ("the-archivist-who-couldnt-make-him-match", "The Archivist Who Couldn't Make Him Match", 6,
     "A Directorate records clerk trying to compile a standard physical description of Bane "
     "finds eyewitness accounts hopelessly, suspiciously contradictory -- the myth's own "
     "inconsistency is part of what makes him impossible to pin down."),
    ("the-column-he-didnt-lead", "The Column He Didn't Lead", 7,
     "Bane deliberately stays unreachable and hands Efa Gol full, unsupervised command of a "
     "raid for the first time; she adapts alone when the plan breaks and succeeds."),
    ("six-hours-in-a-cage", "Six Hours in a Cage", 7,
     "Bane deliberately allows himself to be \"captured\" as a calculated infiltration "
     "tactic to reach a records room, sitting restrained for six hours until an ally frees "
     "the way -- captivity as a chosen tool rather than only a failure state."),
    ("what-the-cook-remembered", "What the Cook Remembered", 7,
     "An unnamed camp cook's intimate account of Bane's ordinary domestic habits -- mending "
     "his own clothes, rationing himself least when supplies run short."),
    ("the-pass-that-wanted-him-dead-first", "The Pass That Wanted Him Dead First", 8,
     "A pure survival showcase -- Bane and four others cross a lethal mountain pass in a "
     "storm to resupply a besieged post, no enemy involved, establishing his ordinary human "
     "vulnerability to cold and altitude."),
    ("the-man-who-didnt-flinch", "The Man Who Didn't Flinch", 8,
     "The first negotiation where the \"Already-Finished Negotiation\" presence trait "
     "(`VB-060`) simply fails -- a disciplined garrison commander refuses to feel it and "
     "fights anyway, losing badly, establishing the trait isn't universal."),
    ("the-soldier-who-almost-didnt-come-back", "The Soldier Who Almost Didn't Come Back", 8,
     "A Directorate conscript sneaks to Bane's camp at night to confess a cover-up he "
     "witnessed, testing trust-building initiated from the enemy's side; the outcome is left "
     "deliberately unresolved."),
    ("what-the-black-ledger-remembers", "What the Black Ledger Remembers", 9,
     "First deep showcase of Onyx of Oblivion's Black Ledger power, used to forensically "
     "read a burned settlement and expose a false-flag atrocity actually committed by Trust "
     "forces, not border raiders as believed."),
    ("the-village-he-didnt-burn", "The Village He Didn't Burn", 9,
     "A pure non-combat restorative-labor entry -- Bane and crew spend five days physically "
     "rebuilding a contested, unprotected village's well and granary with no fight involved "
     "at all."),
    ("the-story-told-for-coin", "The Story Told for Coin", 9,
     "A traveling storyteller profits off a wildly embellished account of the Black Trench; "
     "Bane confronts him but ultimately lets the exaggeration stand once he confirms the man "
     "knows where the line is."),
    ("what-he-didnt-say-out-loud", "What He Didn't Say Out Loud", 10,
     "A private, unguarded late-night conversation with Garren Hask reveals Bane's real, "
     "undiminished emotional weight over every death, and his fear of ever becoming numb to "
     "it -- the first direct interior/psychological entry."),
    ("the-twelve-he-couldnt-wait-for", "The Twelve He Couldn't Wait For", 10,
     "A high-stakes, underprepared overnight extraction of 12 captives runs dangerously close "
     "to failure; Bane openly names it as a bad-odds gamble he'd make again rather than let "
     "it read as another clean victory."),
    ("the-numbers-bane-left-behind", "The Numbers Bane Left Behind", 10,
     "Garren Hask tallies the full mixed ledger of the Bane era -- garrisons stood down, "
     "wells rebuilt, rumors corrected -- deliberately weighting combat and non-combat entries "
     "equally, foreshadowing the alias's eventual transition."),
    ("what-the-soulbound-edge-bound", "What the Soulbound Edge Bound", 11,
     "First deep showcase of Onyx's Soulbound Edge power, used to detect an unwilling "
     "informant planted among freed refugees; Bane resolves it through mercy -- freeing the "
     "informant's coerced sister -- rather than punishment."),
    ("the-water-that-wouldnt-carry-the-current", "The Water That Wouldn't Carry the Current", 11,
     "Mafesto's Kinetic Transfer System fails to function properly in marsh/silt terrain -- "
     "no solid ground to conduct force through -- the first genuine mechanical limitation of "
     "the Trinity shown in the field, discovered by an enemy studying his tactics."),
    ("the-commander-who-wanted-the-name-for-himself",
     "The Commander Who Wanted the Name for Himself", 11,
     "A rebellion company commander resents having his own hard-won victory folded into the "
     "Bane legend; Bane spends a week personally correcting the record to credit the man by "
     "name -- friction from his own side rather than the enemy."),
    ("what-he-taught-before-they-ever-fought", "What He Taught Before They Ever Fought", 12,
     "Bane personally trains six new recruits in basic unglamorous combat fundamentals "
     "before their first battle, deliberately de-mythologizing his own reputation to "
     "prioritize their survival."),
    ("the-grain-that-never-reached-the-garrison", "The Grain That Never Reached the Garrison",
     12, "An eleven-week bloodless siege-by-starvation via deniable, patient supply-chain "
     "sabotage forces a 400-man garrison to surrender without a single casualty on either "
     "side."),
    ("the-medic-who-finally-got-to-treat-him", "The Medic Who Finally Got to Treat Him", 12,
     "After a year of Bane refusing treatment to preserve crew morale, a serious wound forces "
     "him to finally let the column medic treat him -- first vulnerability/self-care entry."),
    ("the-ground-he-chose-to-give-up", "The Ground He Chose to Give Up", 13,
     "Facing overwhelming numbers, Bane deliberately withdraws from a contested overlook "
     "rather than making a costly last stand -- the first genuine tactical retreat framed as "
     "choice, not defeat."),
    ("the-fight-that-went-straight-up", "The Fight That Went Straight Up", 13,
     "A detailed vertical battlement/siege-tower combat showcase on a narrow sixty-foot-high "
     "walkway, where Mafesto's grounded footwork doesn't fully apply and Onyx's Whisper of "
     "Shadows/Veil Piercer carry the fight instead."),
    ("the-dispute-they-brought-to-him-instead", "The Dispute They Brought to Him Instead", 13,
     "Freed captives ask Bane to judge an internal informant dispute; he declines to rule "
     "and instead facilitates a community-led truth-finding process."),
    ("the-officer-who-chose-to-talk", "The Officer Who Chose to Talk", 14,
     "A captured officer who expected brutal treatment instead witnesses a week of plain "
     "decency toward prisoners and voluntarily discloses how distorted the Directorate's "
     "internal casualty reports about Bane have become."),
    ("the-promise-he-couldnt-keep", "The Promise He Couldn't Keep", 14,
     "A specific date-certain promise to defend a settlement is broken due to an unavoidable "
     "crisis elsewhere, costing four lives; Bane owns it fully and permanently changes how "
     "he frames future assurances -- the presence trait's failure from his own side."),
    ("what-callum-breck-handed-him-instead-of-words",
     "What Callum Breck Handed Him Instead of Words", 14,
     "During Breck's still-ongoing silent period after Nev Torr's death, he wordlessly gives "
     "Bane a hand-carved marker acknowledging the broken promise doesn't erase a pattern of "
     "kept ones -- a gesture-only comfort scene predating Breck's full voice recovery."),
    ("the-threat-file-that-finally-closed", "The Threat File That Finally Closed", 15,
     "The Directorate formally retires the \"Bane\" threat classification, concluding his "
     "behavior no longer fits the fear-based profile it was built around."),
    ("the-last-night-the-ravine-remembered", "The Last Night the Ravine Remembered", 15,
     "The most detailed, high-intensity full-Trinity combat showcase of the run -- five "
     "companies and two reinforced Crawlers thrown at a ravine deliberately echoing the "
     "Black Trench, all defeated in a single grinding night."),
    ("what-the-name-cost-him-to-set-down", "What the Name Cost Him to Set Down", 15,
     "Bane's own private recognition, in conversation with Garren Hask, that the alias has "
     "done what it was for and is ready to be set down -- closes the full fifteen-wave arc "
     "without naming a successor persona."),
]

assert len(ENTRIES) == 30


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 196, 2026-09-11 (`MCD-{mcd_id}`). Bane Alias Chronicle "
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
    start = 681
    new_rules = []
    for i, (filename, title, wave, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        roman = ROMAN[i]
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), Bane Alias "
                f"Chronicle {roman}, wave {wave} of ten (waves 6-15). {summary}"
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
        "batch": 196,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks Bane's sixth through fifteenth Alias Chronicle waves (MCD-681 through "
            "MCD-710, 30 rules, 10 waves of 3). " + BATCH_NOTE
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
