#!/usr/bin/env python3
"""Batch 309: Soledad Keme's true age, and the Legbara Kalunga dual-seat resolution
for the Astral Archipelago's Council of Crossroads -- closing the last open item
from Batch 307 (the Shattered Kingdoms Political Atlas mining pass).
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-27, no source document."

with open(LEDGER_PATH, "r", encoding="utf-8") as f:
    ledger = json.load(f)

existing_ids = {r["id"] for r in ledger["rules"]}

NEW_RULES = [
    {
        "id": "MCD-1851",
        "category": "World Mechanics",
        "statement": (
            "Soledad Keme (the Singularity, First Seat) is over 150,000 years old -- the "
            "oldest confirmed-aged being in the setting, exceeding even Anu Un Ra/T.D.K. "
            "(30,000+ years, CC-053) and Orlok (76,003 years, CC-058, previously the "
            "second-oldest). This corrects the Shattered Kingdoms Political Atlas source "
            "document's own stated ~4,800 years, which undersold her by a wide margin, per "
            "Abad's explicit ruling. Her extreme age is consistent with, and now explains, her "
            "already-locked firsthand account of Old Dominion-era events roughly 50,000 years "
            "before Book 1's present (MCD-326) -- not oral tradition or secondhand record, but "
            "living memory. It does not conflict with the Astral Archipelago's own much younger "
            "5,000-year founding (POL-104): she predates the nation she now anchors by a wide "
            "margin, having become its First Seat at or after its founding rather than being "
            "native to it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1852",
        "category": "World Mechanics",
        "statement": (
            "Extends MCD-095/POL-103: Legbara Kalunga holds two of the Council of Crossroads' "
            "nine seats simultaneously -- the Second Seat (Master Void-Cusp, domain the dead, "
            "~3,200 years old, Baron Samedi homage, the second most operationally active "
            "Council member -- manages the transition of the deceased, ancestral records, and "
            "the containment of entities that persist beyond biological death, an "
            "Archipelago-native containment tradition predating the SBD by millennia) and the "
            "Fifth Seat (the Event Horizon, domain crossroads -- decision points, trade "
            "negotiations, territorial boundaries -- the Archipelago's ambassador to external "
            "powers and the first Council figure Kanja meets, Elegua homage). This resolves the "
            "Batch 307 open question of whether the Shattered Kingdoms Political Atlas's "
            "presentation of Master Void-Cusp and the Event Horizon as two separate, "
            "distinctly-aged, distinctly-homaged seats contradicts MCD-095's fusion of both "
            "epithets into one person: it does not, since the ages given (~3,200 for Void-Cusp, "
            "none given for the Event Horizon) are consistent with a single figure and the "
            "dual seat reflects his standing as the Singularity's Champion, a rank the "
            "ordinary nine-seats-nine-holders structure doesn't otherwise accommodate. His own "
            "two-part name is not decorative: 'Legbara' (from Legba/Elegua) names the crossroads "
            "seat, 'Kalunga' (the Kikongo threshold between the living and the dead) names the "
            "death seat."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

new_ids = [r["id"] for r in NEW_RULES]
assert len(new_ids) == 2
assert len(set(new_ids)) == len(new_ids)
collisions = existing_ids & set(new_ids)
assert not collisions, f"ID collision: {collisions}"

ledger["rules"].extend(NEW_RULES)

batch_note = (
    "Closes the last open item from Batch 307 (the Shattered Kingdoms Political Atlas mining "
    "pass): whether the Astral Archipelago's Council of Crossroads treats Master Void-Cusp and "
    "the Event Horizon as one seat (MCD-095) or two (the Atlas's own prose). Presented as a "
    "compatible-reading resolution -- Legbara Kalunga is a genuine dual-seat holder, explained "
    "by his standing as the Singularity's Champion -- rather than a rename or an amendment to "
    "either side. Alongside it, Abad directed a correction to Soledad Keme's age: \"Singularity "
    "is way older than everybody else I would say that we need to give Singularity at least "
    "over 150,000 years.\" Locked as the oldest confirmed-aged being in the setting, exceeding "
    "T.D.K. and Orlok, and reconciling cleanly with her already-locked firsthand account of "
    "events 50,000 years before Book 1's present (MCD-326). Abad's approval: \"lock it.\""
)
ledger["batches_completed"].append(
    {
        "batch": 309,
        "date": str(date.today()),
        "source": "Original invention plus Shattered_Kingdoms_Political_Atlas reconciliation",
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
