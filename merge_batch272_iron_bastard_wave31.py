#!/usr/bin/env python3
"""Batch 272: Iron Bastard Alias Chronicle wave 31 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "The Iron Bastard's thirty-first Alias Chronicle wave, drafted under Abad's blanket "
    "authorization to continue a 31st wave for all eleven aliases. Three new registers: a "
    "forensic-investigation entry (no combat) examining recovered wreckage from a second Crawler "
    "of the depot's unresolved design (`MCD-1308`), narrowing the mechanism's likely origin to "
    "reverse-engineering of the scholar's own openly published research rather than the old corps "
    "or the rival diagnostician -- a new thematic register questioning the free-teaching principle's "
    "own openness as a genuine cost for the first time, left unresolved as to the culprit's identity; "
    "a detailed full-Trinity combat showcase isolating a war-engine camouflaged inside a running "
    "tide-mill's own legitimate rotational machinery noise, a new dynamic-camouflage register distinct "
    "from every prior static or environmental countermeasure, resolved non-destructively with the mill "
    "left running; and a closing entry refusing a foreign sovereign's throne-level offer of exclusive "
    "weaponized teaching against civilian housing, the highest-stakes ethical refusal yet, explicitly "
    "engaging the openness-as-vulnerability question the first entry raised. No new named characters -- "
    "all recurring roles (the Trust scholar, the third-generation apprentice, the envoy) follow this "
    "alias's established convention of unnamed recurring figures. Abad's approval: \"let's do a 31st "
    "alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1412",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Bones of the Machine That Lied\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-bones-of-the-machine-that-lied.md), Iron Bastard "
            "Alias Chronicle XCI, wave 31, first entry. Wreckage from a second Crawler of the "
            "depot's unresolved design (`MCD-1308`) is recovered after conventional destruction "
            "unrelated to the doctrine and studied by Kanja, the Trust scholar (`MCD-421`/`551`/"
            "`1307`), and the third-generation apprentice (`MCD-967`/`1289`); the mechanism is "
            "traced to reverse-engineering of the academy's own openly published research rather "
            "than the defected engineer's old corps (`MCD-716`) or the rival diagnostician "
            "(`MCD-1286`-`1288`), both explicitly ruled out -- the culprit's identity remains "
            "unresolved. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1413",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Mill That Turned Against Itself\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-mill-that-turned-against-itself.md), Iron Bastard "
            "Alias Chronicle XCII, wave 31. A detailed, battle-intense full-Trinity combat "
            "showcase: a war-engine is rigged into a running tide-mill's own drivetrain, "
            "camouflaged by the mill's legitimate rotational vibration rather than hidden or "
            "falsified; Mafesto's Kinetic Transfer System, Obsidian Malice, and Onyx of "
            "Oblivion's Cadence Ruin are used together as a real-time baseline-and-isolation "
            "network to find the one beat that doesn't belong, extending the three-voice "
            "diagnostic method (`MCD-721`) to a continuously operating civilian structure for "
            "the first time. Doubled verification (`MCD-497`) and the standing-alone check "
            "(`MCD-1081`) both confirm before discharge; the device is severed without stopping "
            "the mill or damaging its gearwork. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1414",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What He Would Not Teach a Crown\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-he-would-not-teach-a-crown.md), Iron Bastard "
            "Alias Chronicle XCIII, wave 31, closing the wave. A foreign sovereign's envoy offers "
            "land, title, and exclusive teaching rights in exchange for training a royal corps to "
            "weaponize diagnostic listening against occupied civilian housing, explicitly citing "
            "the depot mystery's revealed openness-as-vulnerability (`MCD-1412`) as leverage; "
            "Kanja refuses outright, extending the free-teaching principle (`MCD-499`/`551`/`719`/"
            "`967`/`1048`) and the prior declined licensing offer (`MCD-1082`) and honorary chair "
            "(`MCD-1307`) into a refusal of exclusivity and material power at their largest scale "
            "yet, distinct from the freelance-mercenary corruption of `MCD-899`. Closes wave 31 "
            "without resolving the depot mystery's culprit. No new named characters."
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
            "batch": 272,
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
