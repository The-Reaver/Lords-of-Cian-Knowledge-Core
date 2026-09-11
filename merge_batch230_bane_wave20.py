#!/usr/bin/env python3
"""Batch 230: Bane Alias Chronicle wave 20 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Bane's twentieth Alias Chronicle wave, drafted and presented individually first per the "
    "established wave-5 precedent, then approved. \"The Bridge He Refused to Blow\" (MCD-1026) is a "
    "detailed full-Trinity combat showcase built around a precision constraint -- taking a bridge "
    "intact under fire rather than through it -- distinct from every prior demolition-driven or "
    "natural-disaster crossing entry. \"The Officer Who Wasn't Lying\" (MCD-1027) extends VB-060's "
    "\"Already-Finished Negotiation\" presence trait in reverse: a genuinely sincere Directorate "
    "defector unsettles Bane precisely because there is no deception underneath to read. \"What the "
    "Council Decided\" (MCD-1028) pays off wave 19's tribunal entry (MCD-939) with a real evidentiary "
    "precedent that doesn't reach the districts still circulating the Directorate's original "
    "fabricated claims, deliberately not a clean win, closing wave 20. New location, Drennock Bridge, "
    "collision-checked clean; no new named characters across all three entries. Abad's approval: "
    "\"doorway for all the aliases that remain\" (read as approval of this wave plus authorization to "
    "continue the same wave for the remaining ten aliases)."
)

NEW_RULES = [
    {
        "id": "MCD-1026",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Bridge He Refused to Blow\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-bridge-he-refused-to-blow.md), Bane Alias Chronicle "
            "LVIII, wave 20. A detailed full-Trinity combat showcase built around a precision "
            "constraint: Drennock Bridge (new location, collision-checked clean) is the only crossing "
            "wide enough for nine hundred refugees before seasonal floods close the lower fords, held "
            "by a Directorate garrison under orders to burn it rather than lose it. Bane fights to "
            "take the bridge intact rather than through it -- Onyx's Cadence Ruin metered down, "
            "Mafesto's kinetic transfer redirected sideways off the span instead of through it, "
            "Obsidian Malice aimed away from the piers, charge-runners intercepted blade-first rather "
            "than by ranged Trinity ability -- distinct from every prior demolition-driven or "
            "natural-disaster crossing entry. The bridge stands undamaged; all nine hundred refugees "
            "cross safely. No new named characters -- Danne Sok, Corren Halst, and Efa Gol reused. "
            "Opens wave 20."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1027",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Officer Who Wasn't Lying\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-officer-who-wasnt-lying.md), Bane Alias Chronicle LIX, "
            "wave 20. Extends VB-060's \"Already-Finished Negotiation\" presence trait in reverse: an "
            "unnamed Directorate captain approaches Bane alone and unarmed to genuinely defect, and "
            "Bane -- who has spent years reading rooms for hidden deception -- finds none, which "
            "unsettles him more than any trap would have. Verified over six weeks through Danne Sok's "
            "network before being taken in, but believed from the first sentence. First entry to test "
            "the presence trait against sincerity rather than performance. No new named characters -- "
            "Danne Sok and Callum Breck referenced consistently with their already-locked roles; the "
            "defecting captain deliberately left unnamed. Second entry in wave 20."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1028",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Council Decided\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-council-decided.md), Bane Alias Chronicle LX, "
            "wave 20. Direct payoff to wave 19's institutional/tribunal entry, \"The Council That "
            "Asked Him to Speak Plainly\" (MCD-939): six weeks later, the arbiter council rules "
            "against the Directorate's fabricated atrocity claims on every point Bane refused to "
            "concede and against him on every point he honestly volunteered, producing the arbiter "
            "system's first citable evidentiary precedent of its kind -- while the Directorate's "
            "original propaganda keeps circulating unchanged in districts the ruling never reaches, "
            "deliberately not framed as a clean win. No new named characters -- Corren Halst and Efa "
            "Gol reused. Closes wave 20."
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
            "batch": 230,
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
