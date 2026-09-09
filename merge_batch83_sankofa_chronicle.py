#!/usr/bin/env python3
"""Batch 83: Sankofa Chronicle I ("The Man Who Turned Against Himself"),
the first entry in Sankofa's own Chronicle series -- protagonist Baale
(PH2-021), Kanja as unnamed guest, matching the established
territory-Chronicle convention (MCD-334/335/336/339/340/341/342/343/344/345).
Opens Los Angeles's own run of territory Chronicles."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Sankofa Chronicle I ('The Man Who Turned Against Himself'), "
    "chat-drafted 2026-09-09, original invention, no external source "
    "document. Full narrative text at "
    "docs/lords-of-cian/chronicles/sankofa-chronicle-i-the-man-who-turned-against-himself.md."
)

NEW_RULES = [
    {
        "id": "MCD-346",
        "category": "World Mechanics",
        "statement": (
            "Sankofa Chronicle I ('The Man Who Turned Against Himself') "
            "is the first entry in Sankofa's own Chronicle series, per "
            "the established structure "
            "(MCD-334/335/336/339/340/341/342/343/344/345): each Phase 2 "
            "homage-era territory has its own Chronicles, with its own "
            "leader as protagonist and Kanja appearing only as an unnamed "
            "guest. A rival lieutenant, Kojo (a new named character, "
            "Akan Monday-born day-name per the standing PH2 naming "
            "convention), attacks Baale (PH2-021) face to face in broad "
            "daylight over disputed western-block territory. Baale's "
            "signature ability ('The Turn,' PH2-021) is shown directly in "
            "operation for the first time via this fresh one-on-one "
            "attacker, deliberately distinct from the ability's own "
            "already-locked backstory event (the COINTELPRO-orchestrated "
            "ambush that nearly killed Baale and Kra, which per PH2-021 "
            "remains backstory only and is not restaged here, matching "
            "the Toussaint-Louverture/Ogoun-Xarey precedent for events "
            "referenced rather than dramatized): surviving the direct "
            "exchange, Kojo becomes bound to serve Baale within the week, "
            "exactly matching the ability's stated mechanic. The "
            "ability's cost is honored explicitly and left as live, "
            "unresolved tension rather than a settled fact -- Baale "
            "states plainly that a faceless, coordinated threat, the same "
            "shape as the COINTELPRO conspiracy in his backstory, is "
            "exactly what his gift cannot reach, foreshadowing rather "
            "than restaging that already-locked near-death event. An "
            "unnamed Kanja watches from the crowd's edge, entirely "
            "uninvolved, matching the Umoja/Yara/Areito pure-witness end "
            "of the established range. Kojo is left open as a minor "
            "recurring figure for future entries. Slots into no existing "
            "mainline battle -- original homage-era material set in "
            "Sankofa itself, and opens Los Angeles's own run of territory "
            "Chronicles (Aztlan, Atunbi, Ijoko, and Orin still have "
            "none)."
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
            "batch": 83,
            "source_doc": (
                "Sankofa Chronicle I ('The Man Who Turned Against "
                "Himself', MCD-346) -- the twelfth territory Chronicle "
                "overall and Sankofa's first (Baale), opening Los "
                "Angeles's own run of territory Chronicles, continuing "
                "the open-ended Phase 2 territory-Chronicle expansion "
                "(alongside Xaragua I/II, Umoja I, Yara I, Areito I, "
                "Guanin I, Boriken I, Ide I, Kwan I, Jibaro I, Uhuru I) "
                "that was never gated by the Pre-Book-1 Foundation "
                "Complete milestone (Batch 75)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "8.6"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
