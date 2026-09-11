#!/usr/bin/env python3
"""Batch 270: The Scourge Alias Chronicle wave 31 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "The Scourge's thirty-first Alias Chronicle wave, drafted under Abad's blanket authorization "
    "to continue a 31st wave for all eleven aliases. All three entries fall within the persona's "
    "final year of the Long Mask (age 313-314), directly extending the throughline opened by "
    "\"The Coat He Almost Didn't Put Back On\" (MCD-1255, age 313): the scouted rescue window that "
    "persuaded Kanja to keep the coat on is fulfilled (age 313, Kanja personally leads for the "
    "first time since handing full trust to Efa Gol's successor); Garren Hask and Sena compile a "
    "person-by-person accounting of freed lives, a register distinct from the sub-series' prior "
    "numeric-tally closers (age 313); and the wave closes on the ordinary, unremarked eve of the "
    "already-locked final mission (MCD-1022, age 314), setting up rather than restaging or "
    "contradicting that entry. No new named characters -- reuses Efa Gol, Garren Hask, Pell Ostra, "
    "Sena, and Efa Gol's established unnamed successor throughout. Abad's approval: \"let's do a "
    "31st alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1406",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Window That Wouldn't Come Twice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-window-that-wouldnt-come-twice.md), The Scourge "
            "Alias Chronicle XCI, wave 31, first entry. Age 313, V4 gear. Direct fulfillment of the "
            "scouted, time-limited rescue window that persuaded Kanja not to end the persona a year "
            "early (\"The Coat He Almost Didn't Put Back On,\" MCD-1255): a tide-cut coastal road "
            "passable only eleven nights a year opens on schedule, and Kanja personally leads the "
            "field operation for the first time in years, freeing eighty-one captives alongside Efa "
            "Gol's successor and Pell Ostra. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1407",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Names the Ledger Kept Track Of\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-names-the-ledger-kept-track-of.md), The Scourge "
            "Alias Chronicle XCII, wave 31. Age 313, V4 gear. Garren Hask and Sena (established "
            "MCD-1043/MCD-1241) compile a person-by-person accounting of specific freed captives' "
            "later lives, a register distinct from the sub-series' prior numeric-tally closers "
            "(MCD-815); Kanja reads it with them, learning the fates of two people from his own "
            "decades-old entries. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1408",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Night Before the Last Coat\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-night-before-the-last-coat.md), The Scourge Alias "
            "Chronicle XCIII, wave 31, closing the wave. Age 314, the eve of the persona's "
            "already-locked final mission (\"The Last Coat He Ever Wore,\" MCD-1022). Efa Gol, "
            "Garren Hask, and Efa Gol's established unnamed successor gather with Kanja on an "
            "ordinary, unremarked night neither they nor he yet know precedes the literal last "
            "mission; the entry sits deliberately adjacent to MCD-1022 without depicting, restaging, "
            "or contradicting it. Closes the Scourge's thirty-first wave at ninety-three total "
            "entries across thirty-one complete waves. No new named characters."
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
            "batch": 270,
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
