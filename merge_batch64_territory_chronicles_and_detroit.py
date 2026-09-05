#!/usr/bin/env python3
"""Batch 64: two things.

1. Supersedes MCD-331/332/333 (the withdrawn Chronicle IX/X/XI, which had
   Kanja as protagonist and the homage-era figure as guest -- backwards
   from Abad's actual intent) with three new rules for their replacements:
   Xaragua Chronicle I, Umoja Chronicle I, Yara Chronicle I. Each
   homage-era territory is the protagonist of its own Chronicle series;
   Kanja appears only as a guest. Full narrative text for each lives in
   docs/lords-of-cian/chronicles/.

2. Locks OPEN-011: Detroit selected as the fourth Phase 2 homage-era
   city, per the research at
   research/phase2-homage-source-material/fourth-city-candidates-research.md.
   This locks the CITY CHOICE only -- Detroit's territories/leaders have
   not yet been built (that's the next conversational world-building step,
   same as NYC/LA/Chicago went through before their own PH2- lock)."""
import json

LEDGER_PATH = "canon-ledger.json"

CHRONICLE_SOURCE = (
    "Reworked homage-era territory Chronicles, chat-drafted 2026-09-05, "
    "original invention, no external source document. Full narrative text "
    "in docs/lords-of-cian/chronicles/."
)

NEW_RULES = [
    {
        "id": "MCD-334",
        "category": "World Mechanics",
        "statement": (
            "Xaragua Chronicle I ('The Line That Did Not Break') is the "
            "first entry in Xaragua's own Chronicle series, per the "
            "corrected structure: each Phase 2 homage-era territory has "
            "its own Chronicles, with its own leader as protagonist and "
            "Kanja appearing only as an unnamed guest -- not the reverse. "
            "Ogoun Xarey (Xaragua) holds a coastal redoubt against a "
            "besieging force alongside Mino and Chui (PH2-017), thinning "
            "his own center to hold the gate. An unnamed stranger arrives "
            "partway through, fights in the thinned center as one more "
            "body under Ogoun Xarey's doctrine (no command taken, no "
            "persuasion offered), and the extra eleven minutes he buys "
            "is what lets the gate close on the fleeing settlement's full "
            "eight hundred rather than fewer. He departs before the "
            "battle's aftermath is fully counted, leaving behind only a "
            "rumor among the defenders. Slots into no existing mainline "
            "battle -- original homage-era material set in Xaragua "
            "itself. Supersedes MCD-331 in full."
        ),
        "status": "locked",
        "source": CHRONICLE_SOURCE,
    },
    {
        "id": "MCD-335",
        "category": "World Mechanics",
        "statement": (
            "Umoja Chronicle I ('The Man Who Mapped the Door') is the "
            "first entry in Umoja's own Chronicle series, per the "
            "corrected structure above. Kofi (Umoja) hosts a late-night "
            "meeting; his own chosen head of security -- the secret "
            "informant already established at PH2-040 -- has mapped the "
            "apartment for a raid meant to kill him in his sleep. An "
            "unnamed stranger arrives just ahead of the raid, identifies "
            "the compromised window, and fights off the roof team "
            "without taking command of Kofi's own response (Kofi's own "
            "instinct is to warn his neighbors, not flee). This is the "
            "specific factor that converts Kofi's already-locked close "
            "call into a clean survival. The informant is not confronted "
            "on-page and is gone by dawn, his fate left open for a "
            "future entry. Slots into no existing mainline battle -- "
            "original homage-era material set in Umoja itself. "
            "Supersedes MCD-332 in full."
        ),
        "status": "locked",
        "source": CHRONICLE_SOURCE,
    },
    {
        "id": "MCD-336",
        "category": "World Mechanics",
        "statement": (
            "Yara Chronicle I ('The Seat She Did Not Wait For') is the "
            "first entry in Yara's own Chronicle series, per the "
            "corrected structure above. Yalokona (Yara) is pressured by "
            "her own movement's leadership to defer her candidacy for a "
            "'more electable' figure, per the already-locked detail at "
            "PH2-006; she refuses and announces publicly instead, in a "
            "roofless hall at midday, in front of a crowd. An unnamed "
            "stranger stands among the witnesses, present only as one "
            "more pair of eyes satisfying her own Unbought and Unbossed "
            "ability's witnessed/on-record condition (PH2-006) -- he "
            "offers no advice, no dialogue, and is never identified. She "
            "wins the seat that year on the strength of having refused "
            "to ask permission in public. Slots into no existing "
            "mainline battle -- original homage-era material set in Yara "
            "itself. Supersedes MCD-333 in full."
        ),
        "status": "locked",
        "source": CHRONICLE_SOURCE,
    },
]

SUPERSEDED_NOTES = {
    "MCD-331": (
        "Superseded 2026-09-05 (Batch 64) by MCD-334 (Xaragua Chronicle "
        "I, 'The Line That Did Not Break'). The withdrawn version had "
        "Kanja as protagonist and Ogoun Xarey as guest -- Abad corrected "
        "this: each homage-era territory has its own Chronicles with its "
        "own leader as protagonist and Kanja as guest, not the reverse. "
        "The withdrawn narrative text is kept in "
        "docs/lords-of-cian/chronicles/chronicle-ix-the-ledger-and-the-chain.md, "
        "marked WITHDRAWN, for the project's own record only."
    ),
    "MCD-332": (
        "Superseded 2026-09-05 (Batch 64) by MCD-335 (Umoja Chronicle I, "
        "'The Man Who Mapped the Door'). The withdrawn version had Kanja "
        "as protagonist and Kofi as guest -- Abad corrected this: each "
        "homage-era territory has its own Chronicles with its own leader "
        "as protagonist and Kanja as guest, not the reverse. The "
        "withdrawn narrative text is kept in "
        "docs/lords-of-cian/chronicles/chronicle-x-what-the-ledger-owes.md, "
        "marked WITHDRAWN, for the project's own record only."
    ),
    "MCD-333": (
        "Superseded 2026-09-05 (Batch 64) by MCD-336 (Yara Chronicle I, "
        "'The Seat She Did Not Wait For'). The withdrawn version had "
        "Kanja as protagonist and Yalokona as guest -- Abad corrected "
        "this: each homage-era territory has its own Chronicles with its "
        "own leader as protagonist and Kanja as guest, not the reverse. "
        "The withdrawn narrative text is kept in "
        "docs/lords-of-cian/chronicles/chronicle-xi-what-holds-in-the-light.md, "
        "marked WITHDRAWN, for the project's own record only."
    ),
}

DETROIT_OPEN_DECISION = {
    "id": "OPEN-011",
    "statement": (
        "Which real-world U.S. city should be the fourth Phase 2 "
        "homage-era city, on the same weight class as NYC, LA, and "
        "Chicago?"
    ),
    "status": "resolved",
    "resolution": (
        "RESOLVED 2026-09-05: Detroit. Per background research at "
        "research/phase2-homage-source-material/fourth-city-candidates-research.md: "
        "Detroit is the only city independently corroborated three ways "
        "by the existing source directory (League of Revolutionary Black "
        "Workers, Republic of New Afrika, Shrine of the Black Madonna, "
        "all Detroit-based, none overlapping NYC/LA/Chicago), with a "
        "throughline (industrial labor militancy fused with Black "
        "nationalism, plus the RNA's literal land-sovereignty project) "
        "distinct from the first three cities. Ruled by Abad: \"lock it. "
        "and lock Detroit.\" This resolves the CITY CHOICE only -- "
        "Detroit's five territories/leaders have not yet been built; "
        "that conversational world-building step (matching how NYC/LA/"
        "Chicago were built before their own PH2- lock) is the next "
        "concrete step whenever Abad wants it."
    ),
}

BATCH_NOTE = 'Abad: "lock it. and lock Detroit."'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    superseded_found = set()
    for rule in ledger["rules"]:
        if rule["id"] in SUPERSEDED_NOTES:
            assert rule["status"] == "locked", f"{rule['id']} was not locked before superseding"
            rule["status"] = "superseded"
            rule["note"] = SUPERSEDED_NOTES[rule["id"]]
            superseded_found.add(rule["id"])
    assert superseded_found == set(SUPERSEDED_NOTES.keys()), (
        f"expected to supersede {set(SUPERSEDED_NOTES.keys())}, found {superseded_found}"
    )

    ledger["rules"].extend(NEW_RULES)

    existing_open_ids = {o["id"] for o in ledger["open_decisions"]}
    assert DETROIT_OPEN_DECISION["id"] not in existing_open_ids, "OPEN-011 already exists"
    ledger["open_decisions"].append(DETROIT_OPEN_DECISION)

    ledger["batches_completed"].append(
        {
            "batch": 64,
            "source_doc": (
                "Rework of the withdrawn Chronicle IX/X/XI into the "
                "corrected territory-Chronicle structure (Xaragua "
                "Chronicle I, Umoja Chronicle I, Yara Chronicle I), "
                "superseding MCD-331/332/333, plus OPEN-011: Detroit "
                "selected as the fourth Phase 2 homage-era city."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "6.7"
    ledger["last_updated"] = "2026-09-05"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")
    print(f"Superseded: {sorted(superseded_found)}")
    print(f"Open decisions: {len(ledger['open_decisions'])}")


if __name__ == "__main__":
    main()
