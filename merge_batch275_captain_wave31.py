#!/usr/bin/env python3
"""Batch 275: Captain Alias Chronicle wave 31 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "Captain's thirty-first Alias Chronicle wave, drafted under Abad's blanket authorization to "
    "continue a 31st wave for all eleven aliases -- the final alias in this run. This wave shows a "
    "founding-crew child (Mira, MCD-1370/1371/1372) taking an active operational role for the first "
    "time in a detailed full-Trinity combat showcase, then pays off the mortality thread running "
    "since MCD-920: Garren Hask dies of old age at his own ledger table (his heart condition from "
    "MCD-1089 finally running its course, consistent with his decline across MCD-1384 and MCD-1389), "
    "and the wave closes on his memorial at the Pier Nine wall, where Mira carves his name as she did "
    "Joran's (MCD-1372). No new named characters anywhere in the wave -- Mira, Efa Gol, Corren Halst, "
    "Callum Breck, Sera, Pell Ostra, and the ledger's already-established unnamed keeper "
    "(MCD-1001/1384) are all reused. Abad's approval: \"let's do a 31st alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1421",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Second Generation Held\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-second-generation-held.md), Captain Alias "
            "Chronicle XCI, wave 31. A detailed full-Trinity combat showcase defending a grain depot "
            "from opportunist raiders in which Mira (MCD-1370/1371/1372), now twenty, takes an "
            "active operational role for the first time -- flagging a structural collapse risk in "
            "time for Mafesto's Kinetic Transfer System to redirect it -- rather than only a council "
            "or memorial-wall function. Efa Gol, Corren Halst, and Pell Ostra reused. No new named "
            "characters. First entry, wave 31."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1422",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Morning the Ledger Went Quiet\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-morning-the-ledger-went-quiet.md), Captain Alias "
            "Chronicle XCII, wave 31. Garren Hask dies of old age at his own ledger table, his heart "
            "condition (MCD-1089) finally running its course, consistent with his decline across "
            "MCD-1384 (wave 28) and MCD-1389 (wave 30). A deliberately quiet, unresolved-into-comfort "
            "death entry directly paying off the founding mortality promise (MCD-920); the ledger's "
            "already-established, deliberately unnamed new keeper (MCD-1001/1384) takes over the "
            "day's accounts. Sera and Efa Gol reused. No new named characters. Second entry, wave 31."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1423",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Name They Carved for Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-name-they-carved-for-him.md), Captain Alias Chronicle "
            "XCIII, wave 31, closing the wave. Garren Hask's memorial at the Pier Nine wall, "
            "deliberately mirroring and contrasting wave 30's warm reunion closer (MCD-1389/1390): "
            "Mira carves his name into the wall she herself established (MCD-1372), paralleling her "
            "carving of Joran's name, and the ledger's new keeper (MCD-1001/1384) reads the crew's "
            "founding entry aloud. Closes the mortality arc opened at MCD-920 and deepened through "
            "MCD-1089/1373/1384/1422. Corren Halst, Callum Breck, and Efa Gol reused. No new named "
            "characters. Closes wave 31."
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
            "batch": 275,
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
