#!/usr/bin/env python3
"""Batch 274: Storm That Walks Alias Chronicle wave 31 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "The Storm That Walks' thirty-first Alias Chronicle wave, drafted under Abad's blanket "
    "authorization to continue a 31st wave for all eleven aliases. Three genuinely new registers: "
    "the school's self-organizing council resolves its first honest three-way disagreement among all "
    "three formally credited traditions (Sephtis's storm-timing lineage, the rival fleet's tradition, "
    "the northern pilot's ice-reading chapter) with Kanja unreachable and no time to verify by scout, "
    "codifying a new overlap-window principle into the written creed; the student formally cedes full, "
    "unconfirmed forecasting authority to the fourth-generation apprentice for a full Trinity combat "
    "showcase, the alias's first deliberate (rather than crisis-forced) generational handoff; and the "
    "wave closes by mirroring MCD-1358 from the opposite angle -- a Titan-class vessel's actual passage "
    "produces genuine, uncharted atmospheric disturbance no blended tradition can read, documented as an "
    "honest open gap rather than resolved. No new named characters; all three entries reuse already-"
    "locked recurring figures (the student, the apprentice, the dual-tradition sailor, Efa Gol, Kanja), "
    "collision-checked against the full live ledger before drafting. Abad's approval: \"let's do a 31st "
    "alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1418",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Reading With No Tiebreaker\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-reading-with-no-tiebreaker.md), Storm That Walks Alias "
            "Chronicle XCI, wave 31, first entry in the wave. Three formally credited traditions -- "
            "Sephtis's storm-timing lineage, the rival fleet's independent method, and the northern "
            "pilot's ice-reading chapter -- read the same shoulder-season strait and reach three "
            "different, individually sound windows, with Kanja unreachable and no time left to scout "
            "and verify. The student resolves it by codifying a new principle into the written creed: "
            "when honest traditions disagree and time forbids verification, sail the overlap every "
            "tradition agrees is safe rather than any single tradition's own best call. The sub-series' "
            "first entry where the council resolves a genuine multi-tradition disagreement, not a "
            "factual error, entirely on its own. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1419",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Apprentice's First Fleet\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-apprentices-first-fleet.md), Storm That Walks Alias "
            "Chronicle XCII, wave 31. The student formally cedes full forecasting authority to the "
            "fourth-generation apprentice for a major fleet relief engagement -- a deliberate handoff, "
            "not a crisis-forced test -- and a full Trinity combat showcase (Mafesto's Kinetic Transfer "
            "System, Obsidian Malice's discharge, Onyx of Oblivion's Whisper of Shadows) is committed "
            "entirely on the apprentice's own unconfirmed call using the new overlap-window method from "
            "MCD-1418. The window opens exactly as called; the garrison holds and the blockade squadron "
            "surrenders. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1420",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Weather a Titan Leaves Behind\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-weather-a-titan-leaves-behind.md), Storm That Walks "
            "Alias Chronicle XCIII, wave 31, closing the wave. A Titan-class vessel's distant passage "
            "produces slow, pulsing atmospheric and water disturbance that none of the school's three "
            "blended traditions can chart, mirroring MCD-1358's reverse case (Kanja's own senses once "
            "misread a Titan-class vessel's mass as weather; here the vessel's actual passage genuinely "
            "makes weather no tradition recognizes). The fleet holds at anchor rather than sail into "
            "unread water; the apprentice records the gap honestly in the creed's book as an open "
            "question rather than a forced resolution. Closes wave 31 deliberately leaving the doctrine's "
            "frontier open, consistent with MCD-1363. No new named characters."
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
            "batch": 274,
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
