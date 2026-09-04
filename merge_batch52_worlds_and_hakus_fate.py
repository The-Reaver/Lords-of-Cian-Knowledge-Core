#!/usr/bin/env python3
"""Batch 52: lock two standing creative decisions Abad made directly
in-conversation, both previously tracked only as open questions in
CLAUDE.md's roadmap, not yet in the ledger itself -- the Phase 2
homage era's World/Dimension structure, and Haku the Unifier's fate
(confirmed alive, held for a mainline-book reveal)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-04, no source document -- "
    "both items were raised as open questions in CLAUDE.md's roadmap on "
    "2026-09-04 (World/Dimension structure logged alongside the Phase 2 "
    "source-material addition; Haku's fate logged during Batch 51's "
    "Rexmar Civilization Codex Entry close-out) and resolved by Abad's "
    "direct ruling in the same session, not extracted from any Lore "
    "Vault document."
)

NEW_RULES = [
    {
        "id": "MCD-313",
        "category": "World Mechanics",
        "statement": (
            "The Phase 2 pre-Book-1 homage era (per Abad's 2026-09-03 "
            "roadmap) is structured as a separate World within the same "
            "universe as Cian -- not a Dimension, and not a region of "
            "Cian itself. This follows the same precedent already "
            "established for Kares Prime (Lauris's homeworld, "
            "MCD-149/151): a distinct, physically reachable planet with "
            "its own conditions, not a sealed-off alternate reality. "
            "Travel between worlds is available as an in-fiction "
            "mechanism, as it already is for Lauris, which lets the "
            "real-world Great Migration theme this era is built to "
            "homage be expressed literally -- migration between worlds "
            "-- rather than only thematically. Per Abad's explicit "
            "ruling (2026-09-04), this is the adopted structure; "
            "letting the drafted Phase 2 content itself determine "
            "structure instead remains the fallback if he later decides "
            "the content should lead."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-314",
        "category": "World Mechanics",
        "statement": (
            "Haku the Unifier is alive, confirmed per Abad's explicit "
            "ruling (2026-09-04): a non-Titan surviving roughly 5,000+ "
            "years purely through indomitable will and spirit (extends "
            "MCD-309's Rexmar-longevity-through-will principle), "
            "paralleling the Titans' own longevity by a wholly "
            "different mechanism. This fact is deliberately held back "
            "from any narrative reveal until a mainline-book beat -- "
            "Abad's target placement is Book 5 or a late-book moment, "
            "timed to land when Titan-scale stakes peak, so the "
            "indomitable-will-vs-Titan-longevity comparison carries "
            "maximum weight. Until that reveal, no other drafted "
            "material should assert or imply Haku's death or a "
            "confirmed absence; in-world ambiguity about his fate is "
            "intentional and should be preserved in anything drafted "
            "before the reveal."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

NEW_OPEN_DECISIONS = [
    {
        "id": "OPEN-009",
        "statement": (
            "Whether the Phase 2 pre-Book-1 homage era should be "
            "structured as its own separate World or Dimension within a "
            "larger multi-setting universe, rather than a region of "
            "Cian itself -- raised 2026-09-04 given the setting already "
            "has precedent for multiple worlds (Lauris's Kares Prime)."
        ),
        "status": "resolved",
        "resolution": (
            "RESOLVED 2026-09-04, see MCD-313. A separate World within "
            "the same universe as Cian, following the Kares Prime "
            "precedent, not a Dimension. Ruled by Abad: \"go with 2, "
            "with 4 as the fallback if I want the content to lead\" "
            "(2 = separate World/same universe; 4 = let drafted content "
            "determine structure later)."
        ),
    },
    {
        "id": "OPEN-010",
        "statement": (
            "Whether Haku the Unifier is still alive -- floated by Abad "
            "2026-09-04 during Batch 51's close-out; no source document "
            "anywhere states how or whether he died."
        ),
        "status": "resolved",
        "resolution": (
            "RESOLVED 2026-09-04, see MCD-314. Confirmed alive, the "
            "reveal held for a mainline-book beat (Book 5 or a "
            "late-book moment) rather than Phase 2. Ruled by Abad: "
            "\"Confirmed alive, held for a mainline-book reveal (Book "
            "5, or a late-book beat) -- biggest possible payoff, lands "
            "right when Titan-scale stakes peak, pairs 'indomitable "
            "will' against the Titans' own longevity at the moment "
            "that comparison means the most.\""
        ),
    },
]

BATCH_NOTE = (
    'Abad ruled on both items directly in-conversation. World/Dimension '
    'structure: "go with 2, with 4 as the fallback if I want the '
    'content to lead." Haku\'s fate: "Confirmed alive, held for a '
    'mainline-book reveal (Book 5, or a late-book beat) -- biggest '
    'possible payoff, lands right when Titan-scale stakes peak, pairs '
    '\'indomitable will\' against the Titans\' own longevity at the '
    'moment that comparison means the most. Costs me patience -- it\'s '
    'a long hold."'
)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    existing_open_ids = {o["id"] for o in ledger["open_decisions"]}
    new_open_ids = [o["id"] for o in NEW_OPEN_DECISIONS]
    open_collisions = existing_open_ids.intersection(new_open_ids)
    assert not open_collisions, f"OPEN-ID collision(s): {open_collisions}"
    ledger["open_decisions"].extend(NEW_OPEN_DECISIONS)

    ledger["batches_completed"].append(
        {
            "batch": 52,
            "source_doc": "Two standing creative decisions ruled on directly in-conversation: the Phase 2 homage era's World/Dimension structure, and Haku the Unifier's fate",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "5.5"
    ledger["last_updated"] = "2026-09-04"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
