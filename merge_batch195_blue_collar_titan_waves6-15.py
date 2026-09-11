#!/usr/bin/env python3
"""Batch 195: Lock the Blue-Collar Titan's sixth through fifteenth Alias Chronicle waves
(MCD-651 through MCD-680, 30 rules / 10 waves)."""
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
    ("the-repair-order-that-wasnt", "The Repair Order That Wasn't", 6,
     "A forged maintenance order is used as bait to lure the crew into an ambush; Kanja "
     "catches the forgery through a factual error only genuine clay-main expertise would "
     "notice, and the trap expires unsprung with zero confrontation."),
    ("what-the-dark-couldnt-hide", "What the Dark Couldn't Hide", 6,
     "A collapse kills every light source mid-fight; the full Trinity fights entirely through "
     "touch, vibration, and sound rather than sight -- the alias's first total-darkness "
     "combat showcase."),
    ("the-boy-who-wanted-the-blade-instead", "The Boy Who Wanted the Blade Instead", 6,
     "A grieving orphaned boy demands to be taught to kill; Kanja redirects him into trade "
     "competence instead, a generational-transmission mentorship register."),
    ("the-weight-of-a-false-ledger", "The Weight of a False Ledger", 7,
     "Kanja detects a quartermaster skimming seasoned timber by literally weighing bundles "
     "against grain and moisture, resolving supply-chain fraud without violence."),
    ("the-tunnel-he-cut-through-stone", "The Tunnel He Cut Through Stone", 7,
     "Obsidian Malice is used as a quarrying tool -- controlled strikes reading rock grain -- "
     "to cut forty feet of fresh tunnel through solid bedrock in six hours, interleaved with "
     "a brief defensive skirmish."),
    ("the-one-he-couldnt-dig-out-in-time", "The One He Couldn't Dig Out in Time", 7,
     "The alias's first loss to the work itself rather than combat -- a flawless, forty-minute "
     "rescue effort still arrives too late."),
    ("the-lesson-before-the-tools", "The Lesson Before the Tools", 8,
     "Kanja institutes mandatory structural-safety training before any new recruit touches a "
     "tool -- an institution-building entry distinct from one-on-one mentorship."),
    ("the-walk-no-one-heard", "The Walk No One Heard", 8,
     "A purely non-combat Trinity showcase -- Onyx's Whisper of Shadows used for silent "
     "reconnaissance through an occupied garrison with zero engagement."),
    ("the-choice-between-the-roof-and-the-man", "The Choice Between the Roof and the Man", 8,
     "Two simultaneous crises (a collapsing ceiling threatening nine, a pinned courier) force "
     "a triage decision resolved by matching each crisis to who's actually equipped to answer "
     "it."),
    ("what-moved-through-his-tunnels-at-night", "What Moved Through His Tunnels at Night", 9,
     "Opportunist smugglers exploiting the crew's cleared tunnels are talked out of the "
     "practice through shared-risk reasoning rather than force."),
    ("what-stood-while-it-was-falling", "What Stood While It Was Falling", 9,
     "Engineering and Trinity combat performed simultaneously and interdependently -- shoring "
     "a collapsing ceiling with one hand while fighting off an ambush with the other."),
    ("the-guild-that-grew-from-a-siege", "The Guild That Grew From a Siege", 9,
     "Tunnel workers found a new standing tradesmen's association inspired by his teaching; "
     "Kanja insists it carry no trace of his own name so it outlasts his reputation."),
    ("the-report-no-one-wanted-read", "The Report No One Wanted Read", 10,
     "A formal, redundant-copy structural-defect report forces a negligent labor foreman into "
     "institutional accountability without direct confrontation."),
    ("the-cut-that-freed-them", "The Cut That Freed Them", 10,
     "Precision structural-diagnosis identifies the one non-load-bearing seam in a "
     "purpose-built \"unbreachable\" wall, freeing eleven prisoners with a single surgical "
     "strike."),
    ("the-wall-he-got-wrong", "The Wall He Got Wrong", 10,
     "The alias's first real technical mistake with actual injury -- a rushed assessment "
     "fails, and Kanja publicly owns and corrects it in full."),
    ("what-the-square-could-not-hold", "What the Square Could Not Hold", 11,
     "The alias's first entirely civilian, non-military crisis -- a market undercroft "
     "collapses with no enemy involved, and nineteen people are pulled out alive."),
    ("the-bridge-that-bought-them-time", "The Bridge That Bought Them Time", 11,
     "A surface/outdoor infrastructure showcase featuring Dol Maren's engineering paired with "
     "Trinity combat defense of a supply bridge."),
    ("the-engineer-who-built-against-him", "The Engineer Who Built Against Him", 11,
     "A skilled Trust fortification engineer who designed traps against Kanja defects after "
     "his own craftsmanship-driven integrity is recognized."),
    ("the-plans-that-were-never-true", "The Plans That Were Never True", 12,
     "A forged blueprint's internal elevation/spacing inconsistencies expose it as bait "
     "before anyone walks into the ambush it was built to spring."),
    ("the-engineer-who-fought-like-one", "The Engineer Who Fought Like One", 12,
     "The alias's first genuine skill-versus-skill duel -- a Trust combat engineer who reads "
     "structure the same way Kanja does, ending in mutual recognition rather than a kill."),
    ("what-pell-ostra-said-about-the-quiet-ones", "What Pell Ostra Said About the Quiet Ones",
     12, "Pell Ostra's reflective closer on what distinguishes this alias from Bane and the "
     "others."),
    ("the-bid-he-refused-to-win-cheaply", "The Bid He Refused to Win Cheaply", 13,
     "Post-siege, Kanja deliberately loses a rebuilding contract bid rather than match a "
     "corrupt competitor's dishonestly low price."),
    ("the-junction-that-wouldnt-fall", "The Junction That Wouldn't Fall", 13,
     "A four-day attrition siege against a critical tunnel junction, held through crew "
     "rotation rather than one man's endurance -- a new tempo register."),
    ("the-first-day-no-one-warned-him-about", "The First Day No One Warned Him About", 13,
     "A new recruit expecting glory gets a bucket and measuring cord instead, correcting "
     "romanticized expectation."),
    ("what-the-wreckage-actually-said", "What the Wreckage Actually Said", 14,
     "Forensic reading of fracture patterns determines a collapse was sabotage, not accident, "
     "tracing to a coerced, not malicious, laborer."),
    ("air-enough-for-four", "Air Enough for Four", 14,
     "A purely humanitarian mining-accident rescue with zero enemy and zero combat, racing an "
     "unknown air-supply deadline."),
    ("the-widow-who-wouldnt-thank-him", "The Widow Who Wouldn't Thank Him", 14,
     "A grieving widow confronts Kanja directly and refuses reconciliation -- the alias's "
     "first entry testing his composure under personal blame with no resolution offered."),
    ("the-tunnels-he-sealed-behind-him", "The Tunnels He Sealed Behind Him", 15,
     "After the siege, Kanja chooses to seal most of the tunnel network rather than preserve "
     "it as a monument, prioritizing future safety over legacy."),
    ("the-district-held-on-every-front", "The District Held on Every Front", 15,
     "The alias's largest-scale Trinity set-piece -- a simultaneous five-front district "
     "defense won through superior tunnel-network knowledge, not brute force."),
    ("what-garren-hask-wrote-in-the-margins", "What Garren Hask Wrote in the Margins", 15,
     "Garren Hask's closing cost-accounting ledger tallies the alias's true toll, failures "
     "included, as a grounding counterweight to the legend, closing the ten-wave run."),
]

assert len(ENTRIES) == 30


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 195, 2026-09-11 (`MCD-{mcd_id}`). The Blue-Collar Titan Alias "
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
    start = 651
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
                f"Blue-Collar Titan Alias Chronicle {roman}, wave {wave} of ten (waves 6-15). "
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
        "batch": 195,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Blue-Collar Titan's sixth through fifteenth Alias Chronicle waves "
            "(MCD-651 through MCD-680, 30 rules, 10 waves of 3). " + BATCH_NOTE
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
