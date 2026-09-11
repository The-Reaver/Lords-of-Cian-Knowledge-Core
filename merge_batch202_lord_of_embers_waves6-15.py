#!/usr/bin/env python3
"""Batch 202: Lock the Lord of Embers's sixth through fifteenth Alias Chronicle waves
(MCD-861 through MCD-890, 30 rules / 10 waves). Completes wave 6 through wave 15 for all
eleven aliases."""
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
    'territory everybody that has their own Chronicle entry is in a separate folder entirely." '
    "Completes the run: every alias now has ten full waves (waves 1-15, minus a fixed gap "
    "at none -- waves 1 through 5 were already locked; this batch and its nine siblings "
    "(Batches 192-201) complete waves 6 through 15)."
)

ROMAN = ["XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV",
         "XXVI", "XXVII", "XXVIII", "XXIX", "XXX", "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV",
         "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL", "XLI", "XLII", "XLIII", "XLIV", "XLV"]

ENTRIES = [
    ("the-crew-that-rebuilt-without-him", "The Crew That Rebuilt Without Him", 6,
     "A settlement trained months earlier during an ordinary six-day stop rebuilds itself "
     "after a burning while The Anvil is storm-bound sixteen days away, proving "
     "\"metabolizes punishment\" is a transferable method, not a personal power."),
    ("what-the-floodwater-couldnt-take", "What the Floodwater Couldn't Take", 6,
     "A detailed Trinity showcase: a storm-surge flood at a forge site, exploited by an "
     "opportunistic raid, defeated using the flood itself as both obstacle and weapon."),
    ("the-engineer-who-came-to-disprove-him", "The Engineer Who Came to Disprove Him", 6,
     "A skeptical Trust engineer sent to formally debunk the rebuild-speed reputation "
     "instead confirms it rigorously; his honest report is buried by his own side."),
    ("the-rebuild-that-broke-someone", "The Rebuild That Broke Someone", 7,
     "A rushed reheat under record-chasing pace causes a real injury; Kanja owns the "
     "failure and slows the campaign's pace afterward."),
    ("what-they-chose-to-save-first", "What They Chose to Save First", 7,
     "A detailed Trinity showcase defending grain stores over the forge terrace during a "
     "split-force raid."),
    ("the-mural-on-the-sea-wall", "The Mural on the Sea Wall", 7,
     "Settlement children paint an uncommissioned, inaccurate mural of the campaign; Kanja "
     "lets it stand as-is -- a folk-art legacy entry."),
    ("the-magistrate-who-spent-his-name", "The Magistrate Who Spent His Name", 8,
     "An administrator extorts tribute falsely claiming it funds \"the Lord of Embers\"; "
     "publicly corrected without violence."),
    ("the-pass-that-wouldnt-close", "The Pass That Wouldn't Close", 8,
     "A detailed Trinity showcase: a mountain supply-pass ambush neutralized before the "
     "convoy it protects arrives."),
    ("the-soldier-who-stayed", "The Soldier Who Stayed", 8,
     "A former Trust soldier defects and is absorbed into the crew on pure merit -- an "
     "outsider, former-enemy closer."),
    ("the-fear-that-outlasted-the-flame", "The Fear That Outlasted the Flame", 9,
     "A rumor campaign, fear of being judged too slow, that the ability itself can't touch; "
     "resolved only through patient, honest presence."),
    ("the-foundry-they-turned-around", "The Foundry They Turned Around", 9,
     "A detailed Trinity showcase defending a captured Trust foundry mid-conversion to "
     "campaign use."),
    ("the-apprentice-who-became-the-guildmaster", "The Apprentice Who Became the Guildmaster",
     9, "A former apprentice, decades later, applies the forge's meritocratic ethos as an "
     "institutional ruling."),
    ("the-night-he-almost-didnt-make-the-sixth", "The Night He Almost Didn't Make the Sixth",
     10, "Six simultaneous sites, one more than the established five-site max, pushes the "
     "Trinity to a real, acknowledged near-failure."),
    ("what-held-the-bridge-together", "What Held the Bridge Together", 10,
     "A detailed Trinity showcase defending an unfinished pontoon river crossing."),
    ("two-apprentices-two-roads", "Two Apprentices, Two Roads", 10,
     "Two apprentices from the same lesson diverge into smithing and soldiering, reunited "
     "to find the paths complementary."),
    ("the-pride-that-wouldnt-take-help", "The Pride That Wouldn't Take Help", 11,
     "A prideful district refuses aid until a genuine material trade, quarried stone, "
     "preserves its dignity."),
    ("what-the-quarry-wall-held-back", "What the Quarry Wall Held Back", 11,
     "A detailed Trinity showcase defeating a demolition attack on an active quarry."),
    ("the-alloy-she-wouldnt-share", "The Alloy She Wouldn't Share", 11,
     "A trained smith invents her own proprietary alloy and withholds it; affirmed as the "
     "deeper success of teaching."),
    ("the-diplomat-who-came-to-negotiate-a-surrender",
     "The Diplomat Who Came to Negotiate a Surrender", 12,
     "A Trust diplomat offers formal territorial recognition in exchange for halting the "
     "campaign; countered to secure gains without conceding the advance."),
    ("the-night-the-tide-turned-the-battle", "The Night the Tide Turned the Battle", 12,
     "A detailed Trinity showcase using a tracked tidal schedule as a proactive weapon."),
    ("the-ballad-that-outgrew-the-truth", "The Ballad That Outgrew the Truth", 12,
     "A traveling singer's exaggerated ballad, left deliberately uncorrected -- a "
     "legend-vs-fact closer."),
    ("the-vote-to-turn-back", "The Vote to Turn Back", 13,
     "A genuine crew disagreement over competing priorities, resolved by open deliberation "
     "and a crew-proposed compromise."),
    ("the-site-that-burned-twice", "The Site That Burned Twice", 13,
     "The same district burned twice in one season, rebuilding even faster the second time "
     "from banked lessons."),
    ("the-boy-who-refused-the-forge", "The Boy Who Refused the Forge", 13,
     "A naturally gifted boy chooses healing over smithing, supported rather than "
     "pressured."),
    ("the-grudge-that-outlived-the-war", "The Grudge That Outlived the War", 14,
     "An unrelated, decades-old local feud the campaign explicitly can't and doesn't try to "
     "resolve."),
    ("the-forge-at-the-edge-of-the-map", "The Forge at the Edge of the Map", 14,
     "A detailed Trinity showcase at the campaign's most isolated site, fought with no "
     "possibility of reinforcement."),
    ("what-the-senior-smith-passed-down", "What the Senior Smith Passed Down", 14,
     "The recurring senior smith trains her own successor -- a bookend for that character."),
    ("the-final-burning", "The Final Burning", 15,
     "The tour's last attempted burning, rebuilt almost entirely by the district itself "
     "with minimal crew involvement."),
    ("what-eighteen-months-built", "What Eighteen Months Built", 15,
     "A detailed capstone Trinity showcase repelling a combined naval and shore effort to "
     "end the tour, using every accumulated refinement of the campaign."),
    ("the-anvils-last-anchorage", "The Anvil's Last Anchorage", 15,
     "A closing legacy entry at the tour's final, ordinary stop, reflecting on the full "
     "eighteen-month campaign's cumulative impact, closing the ten-wave run."),
]

assert len(ENTRIES) == 30


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 202, 2026-09-11 (`MCD-{mcd_id}`). The Lord of Embers Alias "
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
    start = 861
    new_rules = []
    for i, (filename, title, wave, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        roman = ROMAN[i]
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The Lord "
                f"of Embers Alias Chronicle {roman}, wave {wave} of ten (waves 6-15). "
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
        "batch": 202,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Lord of Embers's sixth through fifteenth Alias Chronicle waves "
            "(MCD-861 through MCD-890, 30 rules, 10 waves of 3). Completes waves 6-15 "
            "(330 new Chronicles total) across all eleven aliases (Batches 192-202). " +
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
