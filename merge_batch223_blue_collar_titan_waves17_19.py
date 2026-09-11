#!/usr/bin/env python3
"""Batch 223: Lock the Blue-Collar Titan's seventeenth through nineteenth Alias Chronicle
waves (MCD-1005 through MCD-1013, 9 rules)."""
import json
import re
from datetime import date

LEDGER_PATH = "canon-ledger.json"
CHRON_DIR = "docs/lords-of-cian/chronicles/"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "three more waves and then we\'ll move on to something else this includes '
    'testing committing and pushing to origin Main." Waves 17-19 (three-per-alias pacing) '
    "for the Blue-Collar Titan. Note: the drafting agent flagged a pre-existing, "
    "unresolved ledger inconsistency on Maret Vos's pronouns (MCD-533 uses \"his\", "
    "MCD-593 uses \"her\") while drafting Chronicle LVII -- worked around by avoiding "
    "pronouns for that character in the new text; the underlying contradiction is not "
    "resolved by this batch and remains open for a future pass."
)

ENTRIES = [
    (17, "the-man-carrying-two-masters", "The Man Carrying Two Masters", "XLIX",
     "Kanja discovers a coerced crew informant (his sister held hostage) passing "
     "schedules to a Directorate handler, and resolves it through quiet counter-"
     "intelligence and a separate-channel rescue rather than exposure or punishment. "
     "First internal-betrayal register for this alias."),
    (17, "the-six-hours-they-held-him", "The Six Hours They Held Him", "L",
     "A routine patrol stop escalates into a six-hour formal interrogation; Kanja's cover "
     "holds purely on the strength of genuine, verifiable trade knowledge under sustained "
     "pressure. First sustained-custody/interrogation register."),
    (17, "the-quartermasters-price", "The Quartermaster's Price", "LI",
     "Kanja negotiates a legitimate labor-for-timber trade directly with a Trust "
     "requisition officer to dodge a punitive new war tariff, without fraud or bribery. "
     "First direct bureaucratic-negotiation register. Closes wave 17."),
    (18, "the-dust-that-took-years-to-kill", "The Dust That Took Years to Kill", "LII",
     "Kanja identifies chronic occupational lung damage among veteran dry-stone cutters "
     "and engineers ventilation to protect future workers, explicitly unable to undo harm "
     "already done. First slow/cumulative-harm register."),
    (18, "the-order-he-wouldnt-carry-out", "The Order He Wouldn't Carry Out", "LIII",
     "Kanja refuses his own resistance command's demolition order because sheltering "
     "civilians haven't been safely evacuated, accepting real strategic cost for the "
     "delay. First conflict-with-his-own-command register."),
    (18, "the-signal-from-the-other-tunnel", "The Signal From the Other Tunnel", "LIV",
     "An unplanned tunnel breakthrough connects Kanja's crew with an independent "
     "resistance cell's own field engineer; the two combine plans as peers rather than "
     "merging chains of command. First inter-cell peer-collaboration register. Closes "
     "wave 18."),
    (19, "the-siege-that-never-came", "The Siege That Never Came", "LV",
     "A full day of correctly-reasoned defensive preparation for an attack that never "
     "materializes. First pure-anticlimax entry, dramatizing the tedium/cost of sustained "
     "readiness itself."),
    (19, "what-efa-gol-watched-from-above", "What Efa Gol Watched From Above", "LVI",
     "Efa Gol runs a staged surface diversion timed against Kanja's below-ground breach "
     "with no real-time confirmation between the two teams. First paired above-ground/"
     "below-ground remote-coordination register, and Efa Gol's first appearance in this "
     "alias's run."),
    (19, "the-question-maret-vos-never-had-to-ask", "The Question Maret Vos Never Had to Ask",
     "LVII",
     "Maret Vos offers Kanja a genuine refinement to his own engineering method (redundant "
     "margin against a ground that \"lies\"), rather than reflecting on his reputation. "
     "Closes wave 19."),
]

assert len(ENTRIES) == 9


def fix_header(filename, mcd_id, roman, wave):
    path = CHRON_DIR + filename + ".md"
    with open(path) as f:
        text = f.read()
    pattern = re.compile(r"\*\[DRAFT — awaiting batch/rule-ID assignment\]\..*?\*", re.DOTALL)
    replacement = (
        f"*Locked canon, Batch 223, 2026-09-11 (`MCD-{mcd_id}`). The Blue-Collar Titan "
        f"Alias Chronicle {roman}, wave {wave}. Not a territory Chronicle. Narrated in "
        f"neutral third-person prose.*"
    )
    new_text, n = pattern.subn(replacement, text, count=1)
    assert n == 1, f"header pattern not found/replaced in {filename}"
    with open(path, "w") as f:
        f.write(new_text)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    start = 1005
    new_rules = []
    for i, (wave, filename, title, roman, summary) in enumerate(ENTRIES):
        mcd_id = f"MCD-{start + i}"
        fix_header(filename, start + i, roman, wave)
        new_rules.append({
            "id": mcd_id,
            "category": "kanja-alias-chronicle",
            "statement": (
                f"\"{title}\" (full narrative text at {CHRON_DIR}{filename}.md), The "
                f"Blue-Collar Titan Alias Chronicle {roman}, wave {wave}. {summary}"
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
        "batch": 223,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": len(new_rules),
        "note": (
            "Locks the Blue-Collar Titan's seventeenth through nineteenth Alias Chronicle "
            "waves (MCD-1005 through MCD-1013, 9 rules). " + BATCH_NOTE
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
