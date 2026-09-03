#!/usr/bin/env python3
"""Batch 48: lock Garren Hask, Callum Breck, and Dol Maren -- three
recurring, named crew members with real characterization across all 8
written Chronicle chapters, surfaced as a gap during the Batches 46-47
compliance pass but with zero prior ledger presence."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Compiled from the written manuscript, Chronicle_I through "
    "Chronicle_VIII (Google Drive, 'My Rivals Distance' folder), via "
    "three parallel background-agent full-text passes (one per "
    "character), each independently confirming zero prior ledger "
    "presence via grep. Garren Hask's stated age (53) does not increment "
    "between the age-18 (Chronicle I) and age-19 (Chronicle III) "
    "chapters -- a manuscript-internal inconsistency, not resolved here, "
    "added to Abad's editing punch list alongside the four items from "
    "Batch 47. Callum Breck's role in coining the already-locked 'Trench "
    "Monarch' alias (MCD-230) is an extension, not a contradiction: "
    "MCD-230 only states the alias belongs to Kanja in the sense the "
    "world uses it, not who invented it."
)

NEW_RULES = [
    {
        "id": "CC-115",
        "category": "character-crew",
        "statement": (
            "Garren Hask: a dock-smith on Dock-Row Six/Lower Portside "
            "with 31 years' tenure, recruited into the rebellion at its "
            "founding when his wife's years of suspecting Scrip fraud "
            "are confirmed by the Forge-7 evidence. Becomes the crew's "
            "'counter' -- tallying casualties (Black Trench: 93 of 120 "
            "survive) and later the 12,006 Cestari freed at Maw-9 -- and "
            "its ledger-keeper, a role the text frames as the form his "
            "loyalty takes. Personally named both of the fleet's "
            "flagship-class vessels, The Audit and The Receipt."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-116",
        "category": "character-crew",
        "statement": (
            "Garren Hask, relationships: the first person shown calling "
            "Kanja by his bare name rather than 'boy' or 'son' "
            "(Dredge-Line Ambush, age 18) -- narration frames this as "
            "recognition, not familiarity. Explicitly compared in-text "
            "to Sephtis as a parallel 'ledger' figure. Serves as a "
            "rear-base caretaking conduit alongside his logistics role, "
            "relaying news of Callum Breck's recovery and his daughter "
            "Sera's milestones to Breck in the field."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-117",
        "category": "character-crew",
        "statement": (
            "Callum Breck: a 22-year-old dockhand on Pier Nine's night "
            "shift at recruitment (four years older than Kanja), with a "
            "wife (unnamed throughout) and an infant daughter, Sera, "
            "born roughly four months before the Scrip-Forge Raid. "
            "Recruited on the eve of Sera's naming ceremony, which he "
            "misses to execute the raid."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-118",
        "category": "character-crew",
        "statement": (
            "Extends MCD-230: the 'Trench Monarch' alias (already "
            "locked as one of Kanja's names) was personally and "
            "unilaterally coined by Callum Breck during the Dredge-Line "
            "Ambush (age 18) -- he chalked 'THE TRENCH MONARCH' on "
            "captured Compliance Officer Tavin Greer's forehead "
            "unprompted, while thinking of his own daughter, without "
            "asking or informing Kanja beforehand. Kanja did not choose "
            "or sanction the name; it reached him already given by the "
            "district."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-119",
        "category": "character-crew",
        "statement": (
            "Callum Breck's silence arc: his assigned pair-partner, "
            "16-year-old Nev Torr, dies under his watch at the Black "
            "Trench (age 19), and Breck goes four months without "
            "speaking to anyone but his infant daughter. He breaks his "
            "silence only to confirm Iron Shallows' zero-casualty "
            "headcount ('Two hundred'), then rebuilds his voice "
            "gradually through purely functional, navigational speech "
            "across the following battles, culminating in a 26-word "
            "channel-navigation call that personally guides the fleet's "
            "escape at Ghost Harbor (age 21)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-120",
        "category": "character-crew",
        "statement": (
            "Dol Maren: a crane operator at recruitment (mid-30s), "
            "following his father's 34-year career operating 'Crane "
            "Six.' Marked by near-total verbal economy and a fixed "
            "reporting format -- a number, a material, and a conclusion "
            "-- with trust expressed only through verified calculation, "
            "never faith. Coincidentally shares a name with the "
            "unrelated, much-later Trust Governor Maren Tallis "
            "(MCD-260, appears roughly 178 years afterward in a "
            "different role); no connection between them."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-121",
        "category": "character-crew",
        "statement": (
            "Dol Maren's arc: builds and load-tests 17 plank-bridges at "
            "the Dredge-Line Ambush (age 18); disassembles eight "
            "captured siege guns into four working ones after the Black "
            "Trench (age 19); verifies the no-kill demolition math at "
            "Maw-9 (age 20); maps structural load points during the "
            "Killane tunnel infiltration (age 20); becomes the fleet's "
            "shipwright from Ghost Harbor onward (ages 21-22), assessing "
            "and repairing vessels under the same materials-competence "
            "framework he's applied to bridges, guns, and tunnels "
            "throughout."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation: "lock it"'


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
            "batch": 48,
            "source_doc": "Chronicles I-VIII (written manuscript) -- three recurring named crew members (Garren Hask, Callum Breck, Dol Maren) surfaced during the compliance pass with zero prior ledger presence",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "5.1"
    ledger["last_updated"] = "2026-09-02"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
