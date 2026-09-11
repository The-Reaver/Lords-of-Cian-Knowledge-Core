#!/usr/bin/env python3
"""Batch 247: Crow King Alias Chronicle wave 21 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Crow King's twenty-first Alias Chronicle wave (three entries). \"The Boy Who Counted "
    "Instead of Sang\" (MCD-1077) opens the wave with the fourth generation's (introduced MCD-1046, "
    "wave 20) first independent field use -- a falsified supply-requisition trail built entirely on "
    "exact numeric recall rather than any vocal, musical, or percussive method, the first entry "
    "across all twenty-one waves grounded in bureaucratic/logistics deception rather than battlefield "
    "evasion. \"What the Chase Could Not Outrun\" (MCD-1078) is a detailed full-Trinity combat "
    "showcase fought entirely at a dead run -- a mounted causeway pursuit, the first entry to combine "
    "a false signal with Trinity combat in continuous motion rather than a static setting. \"What Efa "
    "Gol Recognized\" (MCD-1079) closes the wave with a quiet reflective entry narrated by "
    "already-locked crew member Efa Gol (CC-130), who recognizes her own long-standing decoy/diversion "
    "specialty and the Hymn-Engine lineage as the same underlying discipline in different forms. No "
    "new named characters across any of the three entries; the fourth generation remains deliberately "
    "unnamed per this alias's established convention, and Efa Gol is reused rather than introduced. "
    "Zero new proper nouns -- all locations, garrisons, and one-off Directorate-adjacent figures stay "
    "unnamed, consistent with this alias's established pattern. Abad's approval: \"another alias wave "
    "of all aliases\"."
)

NEW_RULES = [
    {
        "id": "MCD-1077",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Boy Who Counted Instead of Sang\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-boy-who-counted-instead-of-sang.md), Crow King Alias "
            "Chronicle LXI, wave 21, opening it. The fourth generation (introduced MCD-1046, \"The "
            "Fourth Voice,\" wave 20) runs his first independent field test, building a deception "
            "entirely unlike either of his two teachers' methods: a falsified supply-requisition "
            "trail for a phantom garrison, made internally consistent across multiple independent "
            "audits purely through his own flawless numeric recall, with no voice, song, rhythm, or "
            "signal involved at all. It holds for eleven days, quietly starving an active Directorate "
            "position of two requisition convoys and letting the crew take it without a fight. The "
            "third generation deliberately withholds calling it a success until he can explain the "
            "full chain of reasoning back to her himself. Extends the already-locked \"the craft was "
            "never really vocal at its core\" synthesis (Chronicle XXX, MCD-845) into a genuinely new "
            "register: bureaucratic/logistics camouflage rather than battlefield evasion. No new named "
            "characters; the fourth generation and the records auditor are both unnamed, consistent "
            "with this alias's established convention. No new proper nouns."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1078",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Chase Could Not Outrun\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-chase-could-not-outrun.md), Crow King Alias "
            "Chronicle LXII, wave 21. A detailed full-Trinity combat showcase fought entirely at a "
            "dead run: a mounted Directorate courier company closes on a supply convoy along a "
            "causeway with no ground left to choose and no stillness available to exploit. A false "
            "signal (a claim that the border garrison's outriders already hold the crossing) buys "
            "three riders' hesitation; Mafesto's Kinetic Transfer System redirects the lead rider's "
            "own momentum sideways into a second mount rather than through the convoy; Obsidian Malice "
            "discharges once to break the company's tight formation; Onyx of Oblivion's Cadence Ruin "
            "and Veil Piercer track a moving target and a failing causeway span in real time rather "
            "than mapping a fixed space. The company reins up not from a trick alone but from three "
            "downed mounts and a collapsing span. The first entry across all twenty-one waves to "
            "combine a false signal with full-Trinity combat in continuous motion rather than any "
            "static setting (checkpoints, vaults, garrisons, sieges). Efa Gol (CC-130, already locked) "
            "reused for continuity. No new named characters and no new proper nouns -- the causeway, "
            "border crossing, and courier company all stay unnamed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1079",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Efa Gol Recognized\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-efa-gol-recognized.md), Crow King Alias Chronicle "
            "LXIII, wave 21, closing it. A quiet, non-combat reflective closer narrated from "
            "already-locked crew member Efa Gol's (CC-130) own perspective: hearing the account of "
            "the fourth generation's voiceless phantom-garrison deception (MCD-1077), she recognizes "
            "her own long-standing, independently developed decoy/diversion specialty (Iron Shallows, "
            "CC-130/MCD-233) as the same underlying discipline -- patience and restraint rather than "
            "any particular performance -- wearing a different form, extending the already-locked "
            "\"the craft was never really vocal at its core\" synthesis (Chronicle XXX, MCD-845) one "
            "step further. The first closer in this alias's run voiced by a crew member whose own "
            "established competency, rather than her relationship to Kanja or the lineage, is the "
            "lens, distinct from the prior closers narrated by Corren Halst (Chronicle XXXIII), the "
            "apprentice and Kanja together (Chronicle XLIV), and Commandant Voris (Chronicle XLV). No "
            "new named characters. Closes wave 21 (with \"The Boy Who Counted Instead of Sang,\" "
            "MCD-1077, and \"What the Chase Could Not Outrun,\" MCD-1078)."
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
            "batch": 247,
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
