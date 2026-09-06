#!/usr/bin/env python3
"""Batch 66: locks Xaragua Chronicle II ('The Man at the Head of the
Table') and the three new characters/structures it introduces --
Arturo "de la Muerte" Salvatierra Duho, the Five Families, and Yaisa.
Chronologically the first Xaragua Chronicle (precedes Chronicle I),
establishing the mechanism that let Kanja move through NYC's
territories unchallenged. Full narrative text at
docs/lords-of-cian/chronicles/
xaragua-chronicle-ii-the-man-at-the-head-of-the-table.md, drafted
and revised across several rounds of Abad's direction before this
lock (two surnames, Kanja staying unnamed to Arturo too, the
tormented-past backstory, and Yaisa's introduction)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Xaragua Chronicle II ('The Man at the Head of the Table') and its new "
    "characters (Arturo, the Five Families, Yaisa), chat-drafted 2026-09-06, "
    "original invention, no external source document. Full narrative text at "
    "docs/lords-of-cian/chronicles/"
    "xaragua-chronicle-ii-the-man-at-the-head-of-the-table.md."
)

NEW_RULES = [
    {
        "id": "PH2-060",
        "category": "Phase 2 Homage Era",
        "statement": (
            "The Five Families are NYC's citywide organized-crime and "
            "internal-peacekeeping structure, layered above (not "
            "replacing) the five territories' own political movements "
            "(Xaragua/Ogoun Xarey, Areito/Kwame Ade, Yara/Yalokona, "
            "Guanin/Eri Kotoko, Boriken/Guani) -- one family per "
            "territory, each operating within its own turf. This is a "
            "separate register from the territories' liberation "
            "politics: underworld economy, protection, and internal "
            "dispute resolution, extending the underworld texture "
            "already established at Areito (Kwasi Owolabi's Policy-era "
            "operation, PH2-011), which becomes one of the five "
            "families under this structure. A single citywide "
            "figurehead sits above all five as peacekeeper and arbiter "
            "rather than as any one family's own boss -- see Arturo "
            "Salvatierra Duho, PH2-061."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-061",
        "category": "Phase 2 Homage Era",
        "statement": (
            "Arturo 'de la Muerte' Salvatierra Duho leads the Five "
            "Families (PH2-060), a Xaragua native and the fourth "
            "homage-era comrade to guest-relate to Kanja, but in a "
            "structurally distinct role: not a one-off guest in a "
            "Kanja battle, but Kanja's standing point of contact across "
            "all five NYC territories. Two surnames per Abad's "
            "direction: Salvatierra (Spanish) kept alongside Duho added "
            "to it (the real Taino word for a cacique's ceremonial seat "
            "of judgment), reflecting the double Spanish/Taino heritage "
            "common to Dominican identity. His nickname is a reputation, "
            "not a description -- earned by what happens to people who "
            "threaten what's his, not by how he treats his own. "
            "Physics: a biochemical branch (per VB-005's mass/sound/"
            "pressure/chemistry backbone), not density-scaling -- his "
            "signature ability, 'Blood Debt,' has three faces: "
            "protective (wounds seal, toxins break down, bleeding stops "
            "near him or on anyone he's personally claimed), its dark "
            "reverse (catastrophic hemorrhage or organ failure on "
            "someone he's decided is finished, almost never used), and "
            "turned inward (his own aging arrested at a chosen point, "
            "explaining why a much older man still looks mid-40s). Cost: "
            "only works at close range -- a hand on a shoulder, a "
            "shared table -- not a battlefield-wide aura, meaning "
            "grievances get settled at his table because that's the "
            "only place his protection holds; and every true use of the "
            "reverse face visibly ages him, since his youth is a "
            "resource he spends, not a fact about him. Personality: a "
            "force of nature, very rarely outwitted, unflappable and "
            "commanding without ever being boastful; the one exception "
            "is playful banter with those who've earned it, which as of "
            "Xaragua Chronicle II is only Yaisa (PH2-062). Backstory: a "
            "tormented past that is the actual source of his authority "
            "-- as a young man in Xaragua he was one of a tight cohort "
            "of dock boys who were each other's real family; war took "
            "several overseas, and Xaragua's own street war took most "
            "of the rest while he was gone, until only he and Yaisa "
            "remained from that generation. He did not study the "
            "criminal world from above; he survived every rung of it in "
            "sequence on the way up, which is why he understands it "
            "better than anyone. The Five Families, and 'No Blood at My "
            "Table' specifically, are his direct answer to that decade "
            "-- a debt he is still paying, not resolved grief. First "
            "appears in Xaragua Chronicle II ('The Man at the Head of "
            "the Table'), granting the still-unnamed Kanja passage "
            "through all five NYC territories on tested behavior alone "
            "-- Kanja declines to give his name even here, and Arturo "
            "does not press, consistent with the unnamed-guest pattern "
            "across Ogoun Xarey's and Yalokona's own Chronicles. Flagged "
            "for future payoff, not yet dramatized: per Abad's explicit "
            "direction, Kanja eventually earns a place among Arturo's "
            "small circle capable of unguarded banter with him -- a "
            "long-arc thread across future Xaragua Chronicles, not "
            "resolved in this one."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-062",
        "category": "Phase 2 Homage Era",
        "statement": (
            "Yaisa is the sole other survivor of Arturo Salvatierra "
            "Duho's (PH2-061) original dock-boy cohort, the generation "
            "lost to war and Xaragua's own street war. Now his "
            "second-in-command, running the Five Families' day-to-day "
            "business while he handles what only he can. The only "
            "person alive who remembers him before he became 'de la "
            "Muerte,' and the one person whose opinion of him predates "
            "the reputation -- which is why she is currently the only "
            "one who can banter with him unguarded, per Abad's "
            "direction on Arturo's personality. Appears silently in "
            "Xaragua Chronicle II, present at the room's edge, unnamed "
            "to the stranger and given no dialogue in that scene -- her "
            "role is established for the reader, not yet for the "
            "story's other occupant."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-337",
        "category": "World Mechanics",
        "statement": (
            "Xaragua Chronicle II ('The Man at the Head of the Table') "
            "is the fourth Phase 2 homage-era guest-relation Chronicle, "
            "but chronologically the first in-universe -- it precedes "
            "Xaragua Chronicle I (MCD-334) and Yara Chronicle I "
            "(MCD-336), establishing the mechanism that let Kanja "
            "already be trusted enough to appear, unchallenged, in "
            "both. Arturo Salvatierra Duho (PH2-061), leader of NYC's "
            "Five Families (PH2-060), tests the still-unnamed Kanja "
            "over three unwatched days in Xaragua, then grants him "
            "passage through all five NYC territories (Xaragua, Areito, "
            "Yara, Guanin, Boriken) on tested behavior alone, never "
            "learning his name -- Kanja declines the one opening to "
            "give it, and Arturo does not press, consistent with the "
            "unnamed-guest pattern in Ogoun Xarey's and Yalokona's own "
            "Chronicles. Arturo's Blood Debt ability is shown small and "
            "controlled (a self-inflicted cut, sealed instantly), not "
            "at full extent. Yaisa (PH2-062) appears silently in the "
            "scene. Slots into no existing mainline battle -- original "
            "homage-era material set in Xaragua itself."
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
            "batch": 66,
            "source_doc": (
                "Xaragua Chronicle II ('The Man at the Head of the "
                "Table') -- chronologically the first Xaragua "
                "Chronicle, introducing Arturo Salvatierra Duho, the "
                "Five Families, and Yaisa."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "6.9"
    ledger["last_updated"] = "2026-09-06"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
