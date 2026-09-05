#!/usr/bin/env python3
"""Batch 65: locks Detroit's five territories and leaders, the fourth
Phase 2 homage-era city (OPEN-011). Same rigor and bundling pattern as
NYC/LA/Chicago: one rule per territory, one rule per leader, 10 rules
total for the five pairs. Kazi/Irin (League of Revolutionary Black
Workers/DRUM), Taifa/Osei (Republic of New Afrika), Hekalu/Adom (Shrine
of the Black Madonna), Nyansa/Adisa (James Boggs), Kiti/Owusu (Coleman
Young). Sourced from research/phase2-homage-source-material/
fourth-city-candidates-research.md, drafted and pasted for Abad's
review before this lock."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Detroit homage-era territories, chat-drafted 2026-09-05, original "
    "invention drawing on real-world research at "
    "research/phase2-homage-source-material/fourth-city-candidates-research.md "
    "(League of Revolutionary Black Workers, Republic of New Afrika, Shrine "
    "of the Black Madonna, James Boggs, Coleman Young). No fictional-name "
    "source document -- homage conversion only, per the Phase 2 naming "
    "convention (PH2-034)."
)

NEW_RULES = [
    {
        "id": "PH2-050",
        "category": "Phase 2 Homage Era",
        "statement": (
            "Kazi is the fourth homage-era city's (Detroit's) first "
            "territory, named for the Swahili word for 'work/labor,' "
            "matching the Swahili register already established in "
            "Chicago (Umoja, Uhuru). Homage to the League of "
            "Revolutionary Black Workers and its DRUM (Dodge "
            "Revolutionary Union Movement) wildcat-strike organizing, "
            "anchored on the auto-plant floor rather than any single "
            "building or neighborhood."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-051",
        "category": "Phase 2 Homage Era",
        "statement": (
            "Irin leads Kazi, homage to General Baker, the League of "
            "Revolutionary Black Workers' central founding organizer. "
            "'Irin' is Yoruba for 'iron.' An assembly-line worker who "
            "turns the plant floor itself into the site of struggle, "
            "refusing to let the line's own leverage go to waste. Two "
            "lieutenants drawn from the real DRUM/League leadership "
            "circle (homage to John Watson, Mike Hamlin, and Ken "
            "Cockrel Sr.) stand as his founding co-organizers, not yet "
            "individually named or detailed. Signature ability, 'The "
            "Line Stops': when Irin calls a halt, everyone bound into "
            "the same production chain feels it and understands why, "
            "instantly, without a word passed hand to hand. Cost: only "
            "works on people already structurally bound into the same "
            "chain of labor -- useless as leverage on anyone standing "
            "outside that relationship."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-052",
        "category": "Phase 2 Homage Era",
        "statement": (
            "Taifa is Detroit's second territory, named for the Swahili "
            "word for 'nation.' Homage to the Republic of New Afrika "
            "(RNA/PGNA), the era's most literal land-sovereignty "
            "project -- a Black nationalist movement that drafted its "
            "own constitution and sought its own claimed territory."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-053",
        "category": "Phase 2 Homage Era",
        "statement": (
            "Osei leads Taifa, homage to Richard Henry (Imari Obadele), "
            "who built and ran the Republic of New Afrika day to day "
            "for decades. 'Osei' is Akan for 'noble one.' His brother "
            "Yaw (Akan, a Thursday-born day-name, matching the "
            "already-established Akan day-name convention used for "
            "Kofi and Kwame Ade) stands beside him as co-founder, "
            "homage to Milton Henry (Gaidi Obadele). The RNA's real "
            "first (exiled, in-absentia) president stays backstory-only "
            "and unnamed on-page, matching the Toussaint Louverture/ "
            "Legbara Kalunga and Al Raby/MLK precedent for major real "
            "figures who don't need a separate locked card. Signature "
            "ability, 'Kin at a Distance': everyone who has sworn "
            "Osei's same oath acts in coordinated concert even scattered "
            "and out of contact, as if still standing in the same room. "
            "Cost: only binds those who already chose the cause "
            "themselves -- cannot compel anyone who hasn't sworn it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-054",
        "category": "Phase 2 Homage Era",
        "statement": (
            "Hekalu is Detroit's third territory, named for the Swahili "
            "word for 'temple/shrine.' Homage to the Shrine of the "
            "Black Madonna (Pan-African Orthodox Christian Church), "
            "which fused radical Black liberation theology with "
            "cooperative economic institution-building -- farms, a "
            "press, self-sustaining cultural complexes."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-055",
        "category": "Phase 2 Homage Era",
        "statement": (
            "Adom leads Hekalu, homage to Rev. Albert Cleage Jr. "
            "'Adom' is Akan for 'grace/mercy.' A pastor who breaks from "
            "his own church's cautious theology toward a liberationist "
            "reading of scripture, then builds it into lived cooperative "
            "economics rather than leaving it as a congregation's "
            "creed. Signature ability, 'The Common Table': anyone who "
            "breaks bread at his table is bound into a mutual-"
            "obligation network that quietly enforces itself, no oath "
            "required. Cost: only holds among people who chose to sit "
            "down together -- cannot be forced on the unwilling."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-056",
        "category": "Phase 2 Homage Era",
        "statement": (
            "Nyansa is Detroit's fourth territory, named for the Akan "
            "word for 'wisdom.' Homage to James Boggs, the "
            "autoworker-turned-theorist whose writing constantly "
            "revised movement doctrine against lived reality rather "
            "than importing it wholesale from elsewhere."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-057",
        "category": "Phase 2 Homage Era",
        "statement": (
            "Adisa leads Nyansa, homage to James Boggs. 'Adisa' is "
            "Yoruba for 'one who makes clear.' His real, deeply "
            "documented lifelong co-theorist and life partner (homage "
            "to Grace Lee Boggs) is referenced as present throughout "
            "his work but is deliberately left backstory-only, not a "
            "separate named or invented character -- the same "
            "technique already used for MLK and the Republic of New "
            "Afrika's exiled first president (PH2-053), applied here "
            "specifically because her real heritage falls outside this "
            "era's Black/brown-diasporic naming palette (PH2-034) and "
            "inventing a name for her would misrepresent rather than "
            "honor that partnership. Signature ability, 'The Long "
            "Correction': a contradiction in a movement's own logic, "
            "once Adisa says it aloud correctly, can't be quietly "
            "un-thought by that movement again. Cost: only surfaces "
            "truths already latent in the group -- can't implant a "
            "belief that isn't already half-formed there."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-058",
        "category": "Phase 2 Homage Era",
        "statement": (
            "Kiti is Detroit's fifth and capstone territory, named for "
            "the Swahili word for 'seat' -- the seat of power, "
            "paralleling Chicago's Uhuru as an electoral/civic capstone "
            "without reusing its name. Homage to the office of Detroit's "
            "mayoralty as broken open by its first Black mayor."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-059",
        "category": "Phase 2 Homage Era",
        "statement": (
            "Owusu leads Kiti, homage to Coleman Young, Detroit's first "
            "Black mayor. 'Owusu' is Akan for 'one who overcomes.' A "
            "labor-and-civil-rights organizer, blacklisted for it "
            "decades earlier, who breaks the political machine's hold "
            "on the city's highest office and holds it for a "
            "generation. Signature ability, 'The Long Tenure': while "
            "Owusu holds the seat, every attempt to wear him down "
            "through attrition instead strengthens his grip, because "
            "he has already outlasted worse. Cost: purely defensive "
            "and purely institutional -- does nothing to expand his "
            "reach beyond the seat itself, and lapses completely the "
            "moment he is out of office."
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

    for o in ledger["open_decisions"]:
        if o["id"] == "OPEN-011":
            o["resolution"] += (
                " Territories/leaders built and locked in Batch 65 "
                "(PH2-050 through PH2-059): Kazi/Irin, Taifa/Osei, "
                "Hekalu/Adom, Nyansa/Adisa, Kiti/Owusu."
            )

    ledger["batches_completed"].append(
        {
            "batch": 65,
            "source_doc": (
                "Detroit's five homage-era territories and leaders "
                "(the fourth Phase 2 city, per OPEN-011), drawing on "
                "the League of Revolutionary Black Workers, the "
                "Republic of New Afrika, the Shrine of the Black "
                "Madonna, James Boggs, and Coleman Young."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "6.8"
    ledger["last_updated"] = "2026-09-05"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
