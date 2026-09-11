#!/usr/bin/env python3
"""Batch 194: Lock the Trench Monarch's sixth through fifteenth Alias Chronicle waves
(MCD-621 through MCD-650, 30 rules / 10 waves)."""
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
    ("the-handshake-that-wasnt-kept", "The Handshake That Wasn't Kept", 6,
     "An owner reneges on a verbal wage settlement after the crew withdraws in good faith; "
     "Kanja counters not with force but with independent cross-witnessed documentation, "
     "establishing the patience-and-evidence method survives bad faith."),
    ("the-ledger-he-corrected-in-front-of-everyone",
     "The Ledger He Corrected in Front of Everyone", 6,
     "Kanja discovers his own crew's tally erred in the workers' favor and publicly corrects "
     "it unprompted, showing the reputation's honesty applies against his own side's interest "
     "too."),
    ("what-garren-hask-wrote-down-first", "What Garren Hask Wrote Down First", 6,
     "Origin vignette: Garren Hask, then just a dock-smith, independently cross-checks the "
     "Trench Monarch's figures and is recruited on the spot -- the founding moment of his "
     "ledger-keeper role."),
    ("the-rumor-that-traveled-faster-than-the-truth",
     "The Rumor That Traveled Faster Than the Truth", 7,
     "A slander campaign (a bribery accusation) is defeated through public checkable evidence "
     "rather than anger or violence."),
    ("the-flooded-dark", "The Flooded Dark", 7,
     "A total-darkness, flooded-tunnel ambush tests Onyx's Whisper of Shadows against an "
     "environmental extreme rather than a swordsman -- a near-thing, distinct from the "
     "wave-2 duelist-limit entry."),
    ("what-efa-gol-learned-to-read", "What Efa Gol Learned to Read", 7,
     "Origin vignette: Efa Gol's first, unrehearsed use of misdirection to protect a meeting "
     "from a stray patrol."),
    ("the-old-hand-who-wouldnt-kneel-to-a-boy", "The Old Hand Who Wouldn't Kneel to a Boy", 8,
     "A veteran's doubt about following \"a boy\" is won over through humility and public "
     "self-correction, not authority."),
    ("the-duel-he-was-too-young-to-win", "The Duel He Was Too Young to Win", 8,
     "An opponent using net-and-trident gear neutralizes Onyx's intention-reading entirely; "
     "the fight is won by ordinary youthful strength and grappling, not swordcraft."),
    ("what-pell-ostra-kept-safe", "What Pell Ostra Kept Safe", 8,
     "Origin vignette: Pell Ostra's first self-directed use of fire/materials instinct to "
     "save records from a raid."),
    ("five-foremen-at-one-table", "Five Foremen at One Table", 9,
     "Kanja brokers trust among five competing district foremen into one shared tally "
     "standard -- a collaborative peer-diplomacy register, distinct from the wave-5 "
     "adversarial owner negotiation."),
    ("the-water-that-wasnt-safe-to-drink", "The Water That Wasn't Safe to Drink", 9,
     "An attempted slow poisoning is solved through documentation-based investigation, a "
     "detective register."),
    ("what-callum-breck-carried-after", "What Callum Breck Carried After", 9,
     "Breck's later reflection on the guilt and awe of watching the name he coined outgrow "
     "any single moment."),
    ("the-site-they-couldnt-hold", "The Site They Couldn't Hold", 10,
     "First tactical retreat: overwhelming conventional force in open ground defeats both "
     "Onyx and the tally method, and Kanja orders withdrawal."),
    ("two-sites-one-night", "Two Sites, One Night", 10,
     "A command dilemma: two simultaneous threats force a choice, saving one site's hostages "
     "while the other burns -- a real, unresolved cost."),
    ("what-the-ledger-recorded-that-night", "What the Ledger Recorded That Night", 10,
     "Garren Hask records both outcomes honestly, refusing to soften the loss into a cleaner "
     "story."),
    ("what-the-blade-cut-free", "What the Blade Cut Free", 11,
     "Onyx's Veil Piercer used for the first time on inert collapsed material, not an "
     "opponent, to rescue nine trapped miners."),
    ("the-challenge-he-wouldnt-answer-with-steel", "The Challenge He Wouldn't Answer With Steel",
     11, "An honest rival's dominance-duel challenge is declined in favor of a public "
     "transparency contest, subverting genre expectation."),
    ("the-first-sheet-ever-printed", "The First Sheet Ever Printed", 11,
     "The first independently-produced pamphlet about the Trench Monarch circulates via the "
     "crier/pamphlet network, and Kanja establishes the practice of printing corrections "
     "alongside claims."),
    ("what-he-didnt-say-to-corren-halst", "What He Didn't Say to Corren Halst", 12,
     "Private doubt about whether he believes his own growing reputation, confided quietly "
     "to Halst."),
    ("the-boy-who-expected-a-giant", "The Boy Who Expected a Giant", 12,
     "A child, disappointed the \"king\" looks ordinary and tired, is given an honest, "
     "unglamorized account of the work."),
    ("the-blow-danne-sok-took-without-a-word", "The Blow Danne Sok Took Without a Word", 12,
     "Danne Sok silently takes a chain-strike meant for Kanja, a wordless-loyalty register "
     "complementing his separately-closed spoken account."),
    ("the-manifest-that-never-arrived", "The Manifest That Never Arrived", 13,
     "A supply-starvation tactic against the five districts is defeated by tracing and "
     "publicly exposing the reroute rather than raiding it."),
    ("the-duel-fought-with-borrowed-steel", "The Duel Fought With Borrowed Steel", 13,
     "Onyx is knocked out of reach mid-fight; the engagement is finished with a stevedore's "
     "pry-bar, proving skill underneath the sword's gifts."),
    ("what-tavin-greer-taught-the-next-clerk", "What Tavin Greer Taught the Next Clerk", 13,
     "Greer passes the founding instinct behind trust-verification to a new clerk as the "
     "method institutionalizes."),
    ("the-hearing-at-canal-house", "The Hearing at Canal House", 14,
     "A formal Trust inquest summons Kanja; he attends unarmed and the tally records survive "
     "six hours of hostile examination, ending in a non-finding."),
    ("the-ambush-meant-for-the-hearing", "The Ambush Meant for the Hearing", 14,
     "A crowded-market assassination attempt forces Onyx's gifts to be used with "
     "bystander-safety restraint for the first time."),
    ("what-the-court-clerk-recorded", "What the Court Clerk Recorded", 14,
     "An unnamed Trust clerk's private marginal note reveals the institution itself came away "
     "quietly convinced."),
    ("the-last-site-before-the-trench", "The Last Site Before the Trench", 15,
     "The final ordinary dredge-site correction before the Black Trench, with both Kanja and "
     "crew sensing an unnamed coming shift."),
    ("what-onyx-chose-not-to-do", "What Onyx Chose Not to Do", 15,
     "A defector officer and a real duel end with Kanja deliberately withholding a killing "
     "stroke, closing the era's Onyx material on mercy rather than lethality."),
    ("the-name-they-carried-into-the-water", "The Name They Carried Into the Water", 15,
     "Efa Gol and Pell Ostra's joint reflection on the eve of the Black Trench closes the "
     "full fifteen-wave, forty-five-Chronicle run."),
]

assert len(ENTRIES) == 30


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 194, 2026-09-11 (`MCD-{mcd_id}`). The Trench Monarch Alias "
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
    start = 621
    new_rules = []
    for i, (filename, title, wave, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        roman = ROMAN[i]
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The Trench "
                f"Monarch Alias Chronicle {roman}, wave {wave} of ten (waves 6-15). {summary}"
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
        "batch": 194,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Trench Monarch's sixth through fifteenth Alias Chronicle waves "
            "(MCD-621 through MCD-650, 30 rules, 10 waves of 3). " + BATCH_NOTE
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
