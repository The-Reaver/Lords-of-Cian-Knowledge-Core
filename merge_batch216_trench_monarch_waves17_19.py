#!/usr/bin/env python3
"""Batch 216: Lock the Trench Monarch's seventeenth through nineteenth Alias Chronicle
waves (MCD-942 through MCD-950, 9 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "three more waves and then we\'ll move on to something else this includes '
    'testing committing and pushing to origin Main." Waves 17-19 (three-per-alias pacing) '
    "for the Trench Monarch."
)

ENTRIES = [
    (17, "the-fever-that-wouldnt-break", "The Fever That Wouldn't Break", "XLIX",
     "Kanja is struck down by a canal-borne cistern fever and spends days fully dependent "
     "on Corren Halst, Danne Sok, and Maret Vos for care -- the alias's first "
     "illness/physical-vulnerability register. Once recovered, he institutes a permanent "
     "water-boiling sanitation rule."),
    (17, "the-man-who-sold-the-hour", "The Man Who Sold the Hour", "L",
     "A trusted runner inside Kanja's own network sells advance raid timing for a small "
     "bribe. Pell Ostra traces the leak; rather than punishing the runner, Kanja lets him "
     "earn back trust through six months of unpaid verification work -- the first internal-"
     "betrayal/restorative-justice register."),
    (17, "the-two-weeks-he-wasnt-there", "The Two Weeks He Wasn't There", "LI",
     "Reframes the two prior entries as one fortnight in which Halst, Sok, and Vos ran "
     "three sites entirely independently while Kanja was incapacitated -- the first "
     "dramatization of the method surviving its own originator's total absence. Closes "
     "wave 17."),
    (18, "the-debt-owed-to-no-one-living", "The Debt Owed to No One Living", "LII",
     "Kanja mediates a grieving daughter-and-uncle inheritance dispute over a dead worker's "
     "small estate -- a purely civil/domestic register with no owner, no tally figure, and "
     "no institutional wrongdoing to correct."),
    (18, "the-crowd-that-came-to-see-a-king", "The Crowd That Came to See a King", "LIII",
     "Two hundred pilgrims and onlookers descend on a site with no grievance at all, "
     "halting real work; Kanja publicly demystifies himself to disperse them, revealing six "
     "genuine grievances hidden inside the crowd -- dramatizing fame's logistical burden."),
    (18, "the-copy-that-broke-what-it-borrowed", "The Copy That Broke What It Borrowed", "LIV",
     "A distant region's workers badly imitate the tally method without its verification "
     "discipline, wrongly ruining an innocent owner and costing forty jobs; Kanja travels "
     "three weeks to teach the slow, real method -- his legend outrunning his control over "
     "its execution. Closes wave 18."),
    (19, "the-boy-who-wouldnt-stay-down", "The Boy Who Wouldn't Stay Down", "LV",
     "Kanja personally trains a bullied fourteen-year-old dredge-site bystander in footwork "
     "and self-defense over six weeks, deliberately declining to recruit him into the crew "
     "-- direct mentorship that doesn't convert into reputation or crew membership."),
    (19, "the-trade-he-wouldnt-make", "The Trade He Wouldn't Make", "LVI",
     "A Compliance officer offers real, valuable raid-warning intelligence in exchange for "
     "Kanja's silence about an unrelated smuggling operation. Kanja refuses at acknowledged "
     "real cost -- the alias's first temptation-toward-profitable-compromise register."),
    (19, "what-the-canal-remembered-by-itself", "What the Canal Remembered By Itself", "LVII",
     "An uninvolved longtime shopkeeper gives an outsider's historical account of how wage "
     "theft went from routine to rare along the canal, concluding the change no longer "
     "depends on Kanja's presence. Closes wave 19."),
]

assert len(ENTRIES) == 9


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 216, 2026-09-11 (`MCD-{mcd_id}`). The Trench Monarch Alias "
        f"Chronicle {roman}, wave {wave}. Not a territory Chronicle. Narrated in neutral "
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
    start = 942
    new_rules = []
    for i, (wave, filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The "
                f"Trench Monarch Alias Chronicle {roman}, wave {wave}. {summary}"
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
        "batch": 216,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Trench Monarch's seventeenth through nineteenth Alias Chronicle "
            "waves (MCD-942 through MCD-950, 9 rules). " + BATCH_NOTE
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
