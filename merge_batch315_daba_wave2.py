#!/usr/bin/env python3
"""Batch 315: Daba's Character Chronicle gate closes (Psychological Profile
approved, Game Plan closed), and his second wave (Chronicles LI-LIII) locks --
the three next-wave candidates offered in his Game Plan, all picked by Abad
to run "as a wave": the open "what does he want for himself" psychological
question tested directly (LI), the corpus's first genuine physical threat to
his S-tier rating (LII), and a pure texture entry showing 1804's semi-dormant
present (LIII, deliberately touching nothing about MCD-1569's unspecified
Book 1 trigger).
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = (
    "Original invention, chat-drafted 2026-09-28, extending Daba's own "
    "50-Chronicle launch wave (Batch 296) and his gate profile "
    "(docs/lords-of-cian/character-profiles/daba.md)."
)

with open(LEDGER_PATH, "r", encoding="utf-8") as f:
    ledger = json.load(f)

existing_ids = {r["id"] for r in ledger["rules"]}

NEW_RULES = [
    {
        "id": "MCD-1869",
        "category": "daba-character-chronicle",
        "statement": (
            "Daba Chronicle LI, 'The Day With No Name in It' (full text at "
            "docs/lords-of-cian/chronicles/daba-chronicle-li-the-day-with-no-name-in-it.md). "
            "First entry of Daba's second Character Chronicle wave, developing the "
            "psychological question flagged as genuinely open in his gate profile -- whether he "
            "wants anything for himself distinct from 1804's survival. Mika (present since "
            "Chronicle I) tells him she has bought a house, half a day's walk from the coast "
            "road, for no operational reason -- simply asking him to come see it. Pressed to "
            "articulate a want he has never had practice naming, Daba arrives at one certain, "
            "specific answer: the only thing he has ever wanted for himself is for the list of "
            "names 1804's doctrine exists to answer to stop growing. He does not go see the "
            "house by the entry's close, but does not decline either -- the door stays "
            "deliberately, genuinely open, a first real data point on an otherwise-unresolved "
            "question rather than a resolution of it. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1870",
        "category": "daba-character-chronicle",
        "statement": (
            "Daba Chronicle LII, 'The Ground That Almost Wasn't Enough' (full text at "
            "docs/lords-of-cian/chronicles/daba-chronicle-lii-the-ground-that-almost-wasnt-enough.md). "
            "Second entry of the wave -- the first Chronicle in the entire 53-entry corpus to put "
            "Daba's S-tier rating (CC-135) under genuine physical threat, since he holds no "
            "variant biology or density scaling and his rating comes entirely from guerrilla "
            "mastery and tactical discipline. Closing a safehouse at Threnfall personally after "
            "it is traced by a patient, unnamed Trust Compliance captain and eleven enforcers, "
            "Daba survives only by applying his own core doctrine (density is not power if the "
            "terrain neutralizes it, MCD-1567/1568) to save his own life for the first time, "
            "escaping through a disused well and drainage culvert rather than confronting the "
            "perimeter directly. He is genuinely wounded -- an injury decided by luck, not "
            "skill, the first time in his own life that distinction has applied -- and is saved "
            "on arrival at a second safehouse by Wrenna's counting-as-containment response, a "
            "discipline he built into her without ever fully explaining why. Reuses Bren and "
            "Wrenna. No new named characters; the antagonist captain and his enforcers are "
            "deliberately unnamed. Does not touch or dramatize the separate, still-undramatized "
            "Harek Vondel defeat reserved at MCD-1855."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1871",
        "category": "daba-character-chronicle",
        "statement": (
            "Daba Chronicle LIII, 'What a Quiet Year Looks Like' (full text at "
            "docs/lords-of-cian/chronicles/daba-chronicle-liii-what-a-quiet-year-looks-like.md). "
            "Third entry of the wave, closing it -- a deliberate pure-texture entry with no "
            "threat and no plot advance, showing 1804's mature, semi-dormant present day to day: "
            "Kether's refined seven-day recruit vetting, Wrenna running two cells and keeping an "
            "unprompted personal margin-note habit in her reports, Deryn Kettel's ordinary "
            "stable work, and Tessin teaching a new intake the same terrain-as-weapon lesson Daba "
            "once taught Kanja. Daba reads his annual list of names aloud and finds nothing new "
            "to add to it for the first time in years, a rare quiet accounting. Closes on a soft, "
            "deliberately unresolved callback to Chronicle LI's still-open house/Mika thread -- "
            "he does not go that night either, but for the first time thinks he might. Reuses "
            "Kether, Wrenna, Deryn Kettel, and Tessin. No new named characters. Does not name or "
            "imply MCD-1569's unspecified Book 1 trigger for 1804."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

new_ids = [r["id"] for r in NEW_RULES]
assert len(new_ids) == 3
assert len(set(new_ids)) == len(new_ids), "duplicate IDs within the new-rules batch"
collisions = existing_ids & set(new_ids)
assert not collisions, f"ID collision with live ledger: {collisions}"

ledger["rules"].extend(NEW_RULES)

batch_note = (
    "Closes Daba's Character Chronicle Launch Protocol gate for a second wave: the "
    "Psychological Profile drafted last batch was approved as drafted ('Approve as drafted, "
    "keep going'), and the Game Plan's three next-wave candidates -- testing the open 'what "
    "does he want for himself' question, the corpus's first genuine physical threat to his "
    "S-tier rating, and a pure semi-dormant-present texture entry -- were all picked by Abad to "
    "run together: 'All three -- do them as a wave.' Chronicles LI-LIII drafted, presented in "
    "full, and locked on 'lock it.' No new named characters across the wave; Mika, Bren, "
    "Wrenna, Kether, Deryn Kettel, and Tessin all reused from the existing 50-entry corpus. "
    "Daba's row in chronicle-tracks-status.md moves from 'not started (backfill)' to a cleared "
    "gate with 53 total Chronicles."
)
ledger["batches_completed"].append(
    {
        "batch": 315,
        "date": str(date.today()),
        "source": "Original invention (Daba Character Chronicle second wave)",
        "rule_count": len(NEW_RULES),
        "note": batch_note,
    }
)

ledger["ledger_version"] = f"{round(float(ledger['ledger_version']) + 0.1, 1):.1f}"
ledger["last_updated"] = str(date.today())

with open(LEDGER_PATH, "w", encoding="utf-8") as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
      f"Batches: {len(ledger['batches_completed'])}.")
