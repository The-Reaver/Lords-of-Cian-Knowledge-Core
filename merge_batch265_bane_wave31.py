#!/usr/bin/env python3
"""Batch 265: Bane Alias Chronicle wave 31 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "Bane's thirty-first Alias Chronicle wave, drafted under Abad's blanket authorization to "
    "continue a 31st wave for all eleven aliases. Pushes into three registers not yet used across "
    "Bane's prior 90 entries: a whiteout blizzard that strips Sovereign Eyes' visual enhancement to "
    "nothing, forcing a full-Trinity ambush defense to run entirely on sound and vibration through "
    "Cadence Ruin, Mafesto's Kinetic Transfer System, and Obsidian Malice; a genuine trusted-insider "
    "betrayal, discovered from inside the column rather than exposed by an outside enemy, where a "
    "coerced guide's months-long small leaks are met with an extraction rather than retribution; and "
    "a direct payoff to the Toran generational-transmission thread (MCD-1099, MCD-1061), the first "
    "entry where a trained subordinate runs a full operation with neither Corren Halst nor Bane "
    "present at all. No new named characters -- Corren Halst, Danne Sok, Efa Gol, and Toran (already "
    "locked, MCD-1099) reused; collision-checked clean before drafting. Abad's approval: \"let's do a "
    "31st alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1391",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The White That Took the Map Away\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-white-that-took-the-map-away.md), Bane Alias "
            "Chronicle XCI, wave 31. New environmental register: a whiteout blizzard strips "
            "Sovereign Eyes' visual enhancement to nothing against a wall of falling snow, forcing "
            "a detailed full-Trinity ambush defense to run entirely on sound and vibration -- "
            "Cadence Ruin locates twelve ambushers by the wrongness of their stillness, Mafesto's "
            "Kinetic Transfer System redirects arrows by feel, and Obsidian Malice discharges at "
            "sound alone, with zero visual confirmation of any target across the entire engagement. "
            "No new named characters -- Corren Halst and Danne Sok reused. Opens wave 31."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1392",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Guide Who Sold Them an Inch at a Time\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-guide-who-sold-them-an-inch-at-a-time.md), Bane "
            "Alias Chronicle XCII, wave 31. First trusted-insider betrayal entry: a four-month "
            "guide, coerced through a held hostage rather than acting from malice, has fed the "
            "Directorate small operational details, discovered from inside the column by Efa Gol's "
            "pattern-reading rather than exposed by an outside enemy. VB-060's 'Already-Finished "
            "Negotiation' presence trait produces relief rather than fear or capitulation for the "
            "first time, against a man already broken by a burden rather than someone resisting or "
            "defeated. Resolution is an extraction addressing the coercion's root cause, not "
            "punishment. No new named characters -- the guide and his sister are unnamed; Efa Gol "
            "and Corren Halst reused."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1393",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Nights Toran Commanded Alone\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-nights-toran-commanded-alone.md), Bane Alias "
            "Chronicle XCIII, wave 31, closing wave 31. Direct payoff to 'The Lieutenant Corren "
            "Halst Chose' (MCD-1099) and 'The Weight Maret Vos Chose to Carry' (MCD-1061): Toran "
            "requests and runs a full extraction operation with neither Corren Halst nor Bane "
            "present at all, the first fully unsupervised test of the crew's trained discipline. "
            "His own second-set-of-eyes verification practice (extending MCD-1059's standing order) "
            "holds independently, and he talks himself out of sending for confirmation, an explicit, "
            "unforced parallel to VB-060's 'Already-Finished Negotiation' presence trait, framing it "
            "as a teachable discipline rather than a quality unique to Bane. No new named characters "
            "-- Toran (MCD-1099) and Corren Halst reused. Closes wave 31."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)
    assert len(NEW_RULES) == 3, f"expected 3 new rules, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"
    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"
    ledger["rules"].extend(NEW_RULES)
    ledger["batches_completed"].append(
        {
            "batch": 265,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-11, no source document",
            "rule_count": len(NEW_RULES),
            "note": BATCH_NOTE,
        }
    )
    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")
    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs found post-write!"
    print(
        f"OK. Total rules: {len(ledger['rules'])}. "
        f"Ledger version: {ledger['ledger_version']}. "
        f"Batches: {len(ledger['batches_completed'])}."
    )


if __name__ == "__main__":
    main()
