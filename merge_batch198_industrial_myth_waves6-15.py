#!/usr/bin/env python3
"""Batch 198: Lock the Industrial Myth's sixth through fifteenth Alias Chronicle waves
(MCD-741 through MCD-770, 30 rules / 10 waves)."""
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
    ("the-number-she-wouldnt-give", "The Number She Wouldn't Give", 6,
     "A weaver won't state her true wage debt because it would expose a friend she's "
     "secretly subsidizing; Kanja documents an acknowledged gap rather than forcing "
     "disclosure."),
    ("the-ledger-against-the-ledger", "The Ledger Against the Ledger", 6,
     "The first head-to-head \"ledger vs. ledger\" contest: a debt-bondage moneylender's "
     "fraudulent book collapses under cross-verification against Kanja's, and the "
     "moneylender's own scribe breaks first."),
    ("what-danne-sok-didnt-believe", "What Danne Sok Didn't Believe", 6,
     "Skeptical fighter Danne Sok, assigned unarmed guard duty, watches Kanja talk an armed "
     "mob out of burning a warehouse; stays unconvinced in principle but keeps the post "
     "anyway."),
    ("the-youngest-hand-in-the-yard", "The Youngest Hand in the Yard", 7,
     "A child laborer's testimony is recorded with full rigor; he asks for reading time "
     "instead of extra coin, the ledger's first non-monetary demand."),
    ("the-ledger-read-aloud", "The Ledger Read Aloud", 7,
     "The first formal tribunal entry: the ledger survives hostile cross-examination in a "
     "Trust magistrate's chamber but wins no immediate remedy."),
    ("the-widow-who-asked-for-blood", "The Widow Who Asked for Blood", 7,
     "A widow demands violent retribution for her husband's negligent death; Kanja refuses, "
     "documents the negligence instead, and the overseer is later removed -- she remains "
     "unsatisfied."),
    ("the-man-who-padded-his-own-page", "The Man Who Padded His Own Page", 8,
     "A desperate worker inflates his own claim; Ezio corrects it privately and the crew "
     "quietly covers his real emergency off-ledger."),
    ("the-district-that-wouldnt-speak", "The District That Wouldn't Speak", 8,
     "Worst-off-first fails against generational apathy; Kanja leaves the ledger unattended "
     "for three days until the district fills it on its own initiative."),
    ("everything-said-by-letter", "Everything Said by Letter", 8,
     "A fully epistolary campaign: Ezio traps an evasive distant administrator using only "
     "the administrator's own prior letters, no in-person meeting ever occurs."),
    ("what-the-flood-interrupted", "What the Flood Interrupted", 9,
     "A flash flood interrupts testimony; Kanja spends a night on rescue and relief labor, "
     "and credibility for the ledger that follows is earned through that unarmed physical "
     "aid."),
    ("the-crane-operators-other-ledger", "The Crane Operator's Other Ledger", 9,
     "Maret Vos runs a parallel hazard ledger revealing unsafe conditions and wage theft are "
     "causally linked, forcing a combined settlement."),
    ("the-flagships-numbers-didnt-match", "The Flagship's Numbers Didn't Match", 9,
     "Garren Hask flags a provisions discrepancy in the crew's own books; the method is "
     "turned inward and resolves as an honest clerical error."),
    ("the-last-district-before-the-strike", "The Last District Before the Strike", 10,
     "Immediately before the Furnace District Strike, Kanja steps back and lets two trained "
     "local workers run the ledger-taking unaided."),
    ("the-archivist-who-called-it-fiction", "The Archivist Who Called It Fiction", 10,
     "A Trust archivist calls the ledgers propaganda; given full unrestricted access to "
     "audit, his own report ends up corroborating them."),
    ("what-efa-gol-learned-about-waiting", "What Efa Gol Learned About Waiting", 10,
     "Efa Gol manages a peaceful four-thousand-person queue over three days, a "
     "logistics-of-scale entry distinct from combat crowd-control."),
    ("the-ledger-that-couldnt-cross-the-border", "The Ledger That Couldn't Cross the Border",
     11, "A border-strip debt is undisputed but unenforced because neither the Trust nor a "
     "Shattered Kingdoms hold will claim jurisdiction -- left genuinely unresolved."),
    ("the-man-who-wanted-to-be-owed-nothing", "The Man Who Wanted to Be Owed Nothing", 11,
     "A proud senior craftsman refuses to be listed; weeks later, on his own initiative, "
     "asks to be added after all."),
    ("what-corren-halst-carried-instead-of-a-blade",
     "What Corren Halst Carried Instead of a Blade", 11,
     "Corren Halst physically shields the ledger office from hired intimidators using only "
     "his unarmed presence."),
    ("the-impostor-who-wore-the-name-badly", "The Impostor Who Wore the Name Badly", 12,
     "A grifter extorts payment using the Industrial Myth's name; the real Kanja "
     "distinguishes himself through total transparency, not confrontation. The impostor is "
     "never caught."),
    ("the-numbers-that-made-him-famous-and-feared", "The Numbers That Made Him Famous and "
     "Feared", 12,
     "Administrators learn to stage fake \"worst-off\" testimony to fool the tactic; the "
     "method adapts by cross-referencing the least-visible workers instead."),
    ("the-ledger-he-couldnt-finish", "The Ledger He Couldn't Finish", 12,
     "Called away mid-campaign, Kanja leaves a district ledger unfinished; Ezio and Pell "
     "Ostra complete it without him, proving the method doesn't depend on his presence."),
    ("the-first-district-to-ask-for-him-by-name", "The First District to Ask for Him by Name",
     13, "A district formally invites the Industrial Myth rather than him arriving unbidden; "
     "he refuses to let the invitation change the method's caution."),
    ("the-ledger-the-owner-wrote-himself", "The Ledger the Owner Wrote Himself", 13,
     "A mill owner preemptively writes and submits his own honest ledger for verification -- "
     "the audit still finds errors, all against his own interest."),
    ("what-the-numbers-couldnt-measure", "What the Numbers Couldn't Measure", 13,
     "A dockhand's real grievance, missing his mother's death for overtime, can't fit a wage "
     "column; Ezio creates a second, unmonetized entry type."),
    ("the-day-the-ledger-filled-faster-than-he-could-write",
     "The Day the Ledger Filled Faster Than He Could Write", 14,
     "A six-thousand-worker district overwhelms two scribes; Pell Ostra and Efa Gol "
     "improvise as emergency scribes, proving the method scales via cross-referencing."),
    ("the-boy-who-tried-to-take-ezios-place", "The Boy Who Tried to Take Ezio's Place", 14,
     "Ezio confronts his own reluctance to share the corrective method, then rigorously "
     "tests and trains an apprentice scribe."),
    ("what-he-told-the-ones-who-wanted-to-follow-him",
     "What He Told the Ones Who Wanted to Follow Him", 14,
     "Kanja refuses to let seven workers abandon their district to join his crew, "
     "articulating the method's whole design directly."),
    ("the-night-he-wrote-nothing-down", "The Night He Wrote Nothing Down", 15,
     "A dying worker asks not to be documented, only heard; Kanja sets the ledger aside "
     "entirely for one night."),
    ("the-debt-that-was-never-about-money", "The Debt That Was Never About Money", 15,
     "A mother asks the ledger method to find her fraudulently indentured son; the fraud is "
     "proven but the search for the boy ends without recovery."),
    ("pell-ostras-last-watch-of-the-campaign", "Pell Ostra's Last Watch of the Campaign", 15,
     "The night before the Furnace District Strike, Pell Ostra reflects on the full arc of "
     "what his unarmed guard duty actually accomplished, closing the ten-wave run."),
]

assert len(ENTRIES) == 30


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 198, 2026-09-11 (`MCD-{mcd_id}`). The Industrial Myth Alias "
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
    start = 741
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
                f"Industrial Myth Alias Chronicle {roman}, wave {wave} of ten (waves 6-15). "
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
        "batch": 198,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Industrial Myth's sixth through fifteenth Alias Chronicle waves "
            "(MCD-741 through MCD-770, 30 rules, 10 waves of 3). " + BATCH_NOTE
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
