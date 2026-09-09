#!/usr/bin/env python3
"""Batch 78: Boriken Chronicle I ("The Fire That Found No Center"), the
first entry in Boriken's own Chronicle series -- protagonist Guani
(PH2-010), Kanja as unnamed guest, matching the established
territory-Chronicle convention (MCD-334/335/336/339/340). Completes the
first Chronicle entry for every one of NYC's five territories."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Boriken Chronicle I ('The Fire That Found No Center'), chat-drafted "
    "2026-09-08, original invention, no external source document. Full "
    "narrative text at "
    "docs/lords-of-cian/chronicles/boriken-chronicle-i-the-fire-that-found-no-center.md."
)

NEW_RULES = [
    {
        "id": "MCD-341",
        "category": "World Mechanics",
        "statement": (
            "Boriken Chronicle I ('The Fire That Found No Center') is the "
            "first entry in Boriken's own Chronicle series, per the "
            "established structure (MCD-334/335/336/339/340): each Phase "
            "2 homage-era territory has its own Chronicles, with its own "
            "leader as protagonist and Kanja appearing only as an unnamed "
            "guest. An unnamed career administrator (the Commissioner), "
            "after five failed raids each capturing only a fragment of "
            "Guani's (PH2-010) distributed authority, shifts strategy from "
            "hunting the man to burning five of his institutions "
            "simultaneously in one night (the hospital wing, the garbage "
            "depot, two rooftop meeting halls, and a church hall). Guani's "
            "signature ability ('No Single Point,' PH2-010) is shown "
            "directly in operation for the first time: no single location "
            "holds the real him, so none of the five strikes ends him. "
            "The ability's stated cost is also dramatized as the story's "
            "actual engine, not just a caveat -- the church hall's six-year "
            "debt ledger burns and cannot be fully rebuilt from the memory "
            "of the forty people who held pieces of it, a real, "
            "uncompensated loss rather than a disguised win. An unnamed "
            "stranger is present at the church-hall raid and helps carry "
            "people to safety, without taking command, credit, or "
            "narrative authorship of the outcome. No new named characters "
            "introduced. Slots into no existing mainline battle -- "
            "original homage-era material set in Boriken itself. Completes "
            "the first Chronicle entry for all five NYC territories "
            "(Xaragua, Areito, Yara, Guanin, Boriken)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "lock it"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 78,
            "source_doc": (
                "Boriken Chronicle I ('The Fire That Found No Center', "
                "MCD-341) -- the fifth and final first-Chronicle entry for "
                "NYC's five territories (Guani/Boriken), continuing the "
                "open-ended Phase 2 territory-Chronicle expansion (alongside "
                "Xaragua I/II, Umoja I, Yara I, Areito I, Guanin I) that was "
                "never gated by the Pre-Book-1 Foundation Complete milestone "
                "(Batch 75)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "8.1"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
