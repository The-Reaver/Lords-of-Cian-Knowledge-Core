#!/usr/bin/env python3
"""Batch 318: Ezio Valcari Chronicle I locked.

First entry in Ezio's own Character Chronicle series, dramatizing the
Callas Modrin exposure (CC-156/MCD-1864) -- his Game Plan's picked
Chronicle I candidate. Drafted, presented in full; Abad's approval:
"lock it."
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = (
    "Original invention, chat-drafted 2026-09-30, Ezio Valcari's own "
    "Character Chronicle series launch, per his gate's Game Plan "
    "(docs/lords-of-cian/character-profiles/ezio-valcari.md)."
)

with open(LEDGER_PATH, "r", encoding="utf-8") as f:
    ledger = json.load(f)

existing_ids = {r["id"] for r in ledger["rules"]}

NEW_RULES = [
    {
        "id": "MCD-1876",
        "category": "ezio-character-chronicle",
        "statement": (
            "Ezio Chronicle I, 'The Frequency That Never Failed' (full narrative text at "
            "docs/lords-of-cian/chronicles/ezio-chronicle-i-the-frequency-that-never-failed.md). "
            "The first entry in Ezio Valcari's own Character Chronicle series, opening under the "
            "Character Chronicle Gameplan -- the fourth protagonist (after Ozmund, Lauris, Daba) to "
            "clear the Launch Protocol gate. Narrated by Fermand Aurelias (CC-034/VB-024), matching "
            "the register Lauris Chronicle I set. Dramatizes the Callas Modrin exposure (CC-156/"
            "MCD-1864) directly for the first time: Ezio cross-references three geographically "
            "scattered settlements' extortion payments -- each kept deliberately below the threshold "
            "of institutional attention -- against real Directorate equipment maintenance logs, using "
            "the Archive-Key/Cipher Cane (ARS-404) on the page for the first time to touch-read a "
            "sealed data-plate proving Modrin's 'escalating contamination' reports were fabricated "
            "after the fact. The confrontation is quiet, unarmed, and extracts no forced confession, "
            "extending the Socratic Trap (ARS-405) into a document-led register. Closes exactly as "
            "MCD-1864 already locks it: Modrin's own superiors prosecute him not for extorting the "
            "settlements, which the Trust has no institutional interest in, but for defrauding the "
            "Trust's own equipment-maintenance budget through the same false reports -- a bitterly "
            "ironic, deliberately bureaucratic-judo defeat. No combat, no Kanja, no new named "
            "characters beyond the already-locked Callas Modrin. Strictly pre-Book-1."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

new_ids = [r["id"] for r in NEW_RULES]
assert len(new_ids) == len(set(new_ids)), "duplicate IDs within the new-rules batch"
collisions = existing_ids & set(new_ids)
assert not collisions, f"ID collision with live ledger: {collisions}"

ledger["rules"].extend(NEW_RULES)

batch_note = (
    "Ezio Valcari's Character Chronicle series opens. Chronicle I, 'The Frequency That Never "
    "Failed,' dramatizes the Callas Modrin exposure (CC-156/MCD-1864) -- the ready-made hook the "
    "ledger itself had flagged as queued for exactly this launch. Picked directly from the Game "
    "Plan's three candidates. Narrated by Fermand per CC-034/VB-024, matching Lauris Chronicle I's "
    "established register. No combat, no Kanja, no new named characters, strictly pre-Book-1. "
    "Presented in full; Abad's approval, quoted verbatim: \"lock it.\""
)
ledger["batches_completed"].append(
    {
        "batch": 318,
        "date": str(date.today()),
        "source": "Original invention (Ezio Valcari Character Chronicle I)",
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
