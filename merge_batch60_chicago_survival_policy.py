#!/usr/bin/env python3
"""Batch 60: locks Chicago (the third homage-era city) into canon-ledger.json
under the PH2- prefix, plus the new survival/mainline-integration standing
decision, the world-tech-level reconfirmation, Sauti (LA), and the standalone
Duro/Doss "what if." Also amends two already-locked Batch 59 rules (PH2-021,
PH2-030) in place: Baale, Kra, and Ohun now survive their real-world-mirrored
close calls, per Abad's explicit 2026-09-05 direction. Every piece here was
drafted in full and explicitly approved in-conversation before this batch
converts it into the ledger, same pattern as Batch 59."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Phase 2 pre-Book-1 homage-era conversational development, chat-drafted "
    "2026-09-05, no external source document -- original invention. Fully "
    "tracked at docs/lords-of-cian/phase2-homage-era-development.md. Chicago, "
    "the survival/mainline-integration standing decision, the world-tech-"
    "level reconfirmation, Sauti, and Duro/Doss were each drafted in full and "
    "explicitly approved in-conversation before this batch converted them "
    "into the ledger."
)

# ---------------------------------------------------------------------------
# Amendments to already-locked Batch 59 rules: Baale/Kra/Ohun now survive.
# ---------------------------------------------------------------------------

PH2_021_OLD_TAIL = (
    "Assassinated alongside his co-founder Kra (homage: John Huggins) "
    "during a Panther/US-Organization conflict a real, documented FBI "
    "COINTELPRO campaign deliberately inflamed with forged letters and "
    "cartoons. Commands total loyalty from men who used to answer to no "
    "one -- not through force, but because everyone who's raised a hand "
    "against him ends up serving him afterward; dies not in open combat "
    "but ambushed by a conflict manufactured by people who never once "
    "confronted him directly. Signature ability, 'The Turn': anyone who "
    "attacks Baale directly, if they survive the exchange, becomes bound "
    "to serve him from that point on -- charisma at an almost physical "
    "intensity. Cost: only works in person, one at a time, face to face; "
    "cannot reach across distance, through intermediaries, or through a "
    "conspiracy that never shows its face."
)
PH2_021_NEW_TAIL = (
    "Survives, per Abad's 2026-09-05 ruling (revised from an earlier "
    "version where he and his co-founder Kra, homage: John Huggins, were "
    "both killed the way the real men were): a Panther/US-Organization "
    "conflict a real, documented FBI COINTELPRO campaign deliberately "
    "inflamed with forged letters and cartoons nearly kills them both -- "
    "the ambush fails. Commands total loyalty from men who used to "
    "answer to no one -- not through force, but because everyone who's "
    "raised a hand against him ends up serving him afterward. Signature "
    "ability, 'The Turn': anyone who attacks Baale directly, if they "
    "survive the exchange, becomes bound to serve him from that point on "
    "-- charisma at an almost physical intensity. Cost: only works in "
    "person, one at a time, face to face; cannot reach across distance, "
    "through intermediaries, or through a conspiracy that never shows "
    "its face -- exactly the kind of threat that nearly killed him."
)

PH2_030_OLD_TAIL = (
    "Ohun (homage: Ruben Salazar), Yoruba for 'voice/sound' -- a "
    "journalist covering Aztlan's rise from inside the community, "
    "killed mid-sentence in a bar by a projectile fired into a crowd he "
    "was only documenting, on the same day the Moratorium he covered "
    "turned violent. Iya (homage: Gloria Arellanes), Yoruba for "
    "'mother' -- Aztlan's first woman minister (see PH2-023 for the "
    "walkout she led). Kra (homage: John Huggins), Akan for 'soul' -- "
    "Baale's co-founder and equal partner in Sankofa (see PH2-021), "
    "killed alongside him; his widow carries the work forward as a real, "
    "ongoing legacy."
)
PH2_030_NEW_TAIL = (
    "Ohun (homage: Ruben Salazar), Yoruba for 'voice/sound' -- a "
    "journalist covering Aztlan's rise from inside the community. "
    "Survives, per Abad's 2026-09-05 ruling (revised from an earlier "
    "version where a stray projectile killed him mid-sentence in a bar "
    "the day the Moratorium he covered turned violent): the projectile "
    "finds the wall beside him instead. Built as a 'regular person' per "
    "PH2-048's design principle -- no combat ability, survives on "
    "caution, sourcing instincts, and real luck. Iya (homage: Gloria "
    "Arellanes), Yoruba for 'mother' -- Aztlan's first woman minister "
    "(see PH2-023 for the walkout she led). Kra (homage: John Huggins), "
    "Akan for 'soul' -- Baale's co-founder and equal partner in Sankofa "
    "(see PH2-021, also amended 2026-09-05 to survive alongside him); "
    "his marriage and partnership continue as an ongoing thread rather "
    "than a legacy left to his widow."
)

AMENDMENTS = [
    ("PH2-021", PH2_021_OLD_TAIL, PH2_021_NEW_TAIL),
    ("PH2-030", PH2_030_OLD_TAIL, PH2_030_NEW_TAIL),
]

# ---------------------------------------------------------------------------
# New rules: Chicago (5 territories/leaders), Meji/Oluso, Sauti, Duro/Doss,
# the survival-policy standing decision, and the world-tech-level rule.
# ---------------------------------------------------------------------------

NEW_RULES = [
    {
        "id": "PH2-035",
        "category": "phase2-homage-chicago-territory",
        "statement": (
            "Chicago is the third homage-era city (after NYC and LA). Ide "
            "is the Bronzeville-equivalent territory, named for the "
            "Yoruba word for 'bronze,' honoring Bronzeville's real "
            "self-given community nickname born of skin-tone pride."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-036",
        "category": "phase2-homage-chicago-leader",
        "statement": (
            "Ase leads Ide, homage to Ida B. Wells -- born enslaved, "
            "became an anti-lynching investigative journalist after "
            "being forced off a train in Memphis, moved to Chicago in "
            "1893, co-founded the Negro Fellowship League and the Alpha "
            "Suffrage Club (Illinois's first Black women's suffrage "
            "organization), documented lynchings by name, date, and "
            "witness against white newspapers' own reporting. Name is "
            "Yoruba for the life-force/power that makes a spoken or "
            "written thing binding and real. Refuses to be moved from a "
            "train seat and turns that refusal into a life's method: "
            "document everything, make the truth impossible to take "
            "back. Steps into the front of a suffrage parade after being "
            "told to march at the back (the real 1913 Washington march). "
            "Signature ability, 'Named and Numbered': any atrocity Ase "
            "personally documents becomes permanently impossible to "
            "erase, deny, or cover up. Cost: only works after the fact -- "
            "no power to stop violence in the moment, only to make its "
            "truth unkillable afterward. Built per the 'regular person' "
            "design principle (PH2-048): no combat ability."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-037",
        "category": "phase2-homage-chicago-territory",
        "statement": (
            "Kwan is the West Side-equivalent territory, named for the "
            "Akan word for 'road/path.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-038",
        "category": "phase2-homage-chicago-leader",
        "statement": (
            "Kasa leads Kwan, homage to Al Raby -- a self-taught school "
            "dropout turned teacher who became chief organizer/spokesman "
            "of the coalition that invited Martin Luther King Jr. to "
            "Chicago in 1966, co-led the Chicago Freedom Movement's "
            "open-housing marches into hostile white neighborhoods, and "
            "returned in 1982 to personally run Harold Washington's "
            "mayoral campaign. Name is Akan for 'speak/voice.' Quietly "
            "builds the coalition that talks a legendary outside leader "
            "(shaped by the real Martin Luther King Jr., referenced in "
            "backstory only, not a separate character, matching Ogoun "
            "Xarey's Toussaint-Louverture precedent) into coming north, "
            "then marches at the front of it into a mob throwing rocks. "
            "Wins an agreement that looks like victory on paper and "
            "delivers far less in practice. Signature ability, 'The "
            "Invitation': anyone Kasa personally invites into a cause "
            "gains real, almost binding legitimacy and national "
            "attention they couldn't generate alone. Cost: purely "
            "reputational, not physical -- doesn't stop a thrown rock or "
            "a mob."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-039",
        "category": "phase2-homage-chicago-territory",
        "statement": (
            "Umoja is the West Garfield Park-equivalent territory, named "
            "for the Swahili word for 'unity' (a real Kwanzaa "
            "principle)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-040",
        "category": "phase2-homage-chicago-leader",
        "statement": (
            "Kofi leads Umoja, homage to Fred Hampton -- NAACP Youth "
            "Council organizer turned, at 20, chairman of the Illinois "
            "Black Panther Party; personally built the real original "
            "Rainbow Coalition alliance with the Young Lords (Omoba) and "
            "the Young Patriots Organization; ran free breakfast and "
            "medical-clinic survival programs. Name is an Akan "
            "Friday-born day-name. A magnetic 21-year-old who personally "
            "sits down with leaders of groups Chicago's own segregation "
            "was built to keep apart and welds them into one alliance "
            "through sheer conviction. Survives, per Abad's explicit "
            "direction: his own chosen head of security is secretly the "
            "informant who maps his apartment for the raid meant to kill "
            "him in his sleep -- he survives it, the closest of several "
            "close calls. Signature ability, 'One Fire': Kofi can "
            "permanently bind two or more separate groups into a genuine "
            "shared cause simply by standing between them and speaking -- "
            "the bond holds on its own afterward. Cost: his power runs on "
            "trust and proximity, meaning the person he's let closest is "
            "always his single greatest point of failure -- no defense "
            "exists against betrayal from someone let all the way in; "
            "this time, it's not the thing that finally gets him."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-041",
        "category": "phase2-homage-chicago-territory",
        "statement": (
            "Jibaro is the Lincoln Park-equivalent territory, named for "
            "a real, proud Puerto Rican folk-identity term for the "
            "island's rural mountain people."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-042",
        "category": "phase2-homage-chicago-leader",
        "statement": (
            "Omoba leads Jibaro, homage to Jose 'Cha Cha' Jimenez -- "
            "founded the original Young Lords Organization in Chicago's "
            "Lincoln Park in 1968, predating and directly inspiring the "
            "later NYC chapter (Guani, PH2-010); occupied a seminary and "
            "a church, running free breakfast, health, and daycare "
            "programs from the latter; personally co-founded the Rainbow "
            "Coalition with Kofi in 1969; later helped build the Latino "
            "coalition that elected Ofin in 1983. Name is Yoruba for "
            "'prince.' A gang leader who reads himself into a different "
            "person during solitary confinement, turns his own street "
            "organization into a political one overnight, then takes "
            "over a church and a seminary building by simply walking in "
            "and staying. Signature ability, 'The Occupation': wherever "
            "Omoba and those loyal to him physically hold a space for "
            "more than a day, it permanently becomes a sanctuary no "
            "outside authority can reclaim by force. Cost: only works on "
            "space belonging to an institution he can shame into "
            "complicity; doesn't work on open ground or purely private "
            "property."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-043",
        "category": "phase2-homage-chicago-territory",
        "statement": (
            "Uhuru is the citywide/City Hall-equivalent territory, named "
            "for the Swahili word for 'freedom' -- the capstone "
            "territory, representing institutional political power "
            "rather than one neighborhood."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-044",
        "category": "phase2-homage-chicago-leader",
        "statement": (
            "Ofin leads Uhuru, homage to Harold Washington -- lawyer and "
            "legislator who broke from Chicago's Democratic Machine, "
            "elected the city's first Black mayor in 1983 on a coalition "
            "Al Raby personally managed and Cha Cha Jimenez helped build "
            "the Latino vote for; spent 1983-1986 blocked by a hostile "
            "29-alderman council bloc ('Council Wars') before a "
            "court-ordered redistricting broke the deadlock; died "
            "suddenly of a heart attack at his City Hall desk in 1987, "
            "less than a year into his second term. Name is Yoruba for "
            "'law.' Elected on the exact coalition Kasa personally "
            "organizes and Omoba personally delivers, then blocked "
            "appointment by appointment for years before the wall "
            "finally, completely breaks. Dies suddenly at his own desk "
            "at the height of his power -- the one death in the Chicago "
            "build kept as-built, not flipped, landing as the capstone's "
            "own real cost rather than an assassination 'what if.' "
            "Signature ability, 'The Override': any single act of "
            "obstruction against Ofin eventually breaks if he simply "
            "refuses to stop pushing, and once it breaks it breaks "
            "completely and permanently. Cost: runs on time and "
            "endurance, not force -- the same engine that breaks every "
            "wall against him burns him from the inside, with a real, "
            "foreshadowed limit to how long he can keep paying for it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-045",
        "category": "phase2-homage-chicago-underworld",
        "statement": (
            "Meji and Oluso, Chicago's twist-character thread (the "
            "Blackstone Rangers/TWO saga), kept genuinely disputed "
            "rather than resolved into a clean hero or villain, matching "
            "the real historical record's own unresolved dual readings. "
            "Meji (homage: Jeff Fort), Yoruba for 'two/twin,' reflecting "
            "a man simultaneously courted by City Hall and under federal "
            "investigation in the same year (1968); composite skeleton "
            "of Thomas Shelby's tightrope-walk between legitimate and "
            "outlaw power, Michael Corleone's tragedy of a real chance "
            "at legitimacy (the real 1967 federal OEO anti-poverty grant "
            "funneled through his organization) that corrupts rather "
            "than redeems, and a late-life Gyp-Rosetti-flavored turn "
            "toward paranoid insularity mirroring the real 1970s-80s "
            "El Rukns/Libya-terrorism trajectory. Oluso (homage: Rev. "
            "Arthur Brazier), Yoruba for 'shepherd/guardian' -- a "
            "genuine good-faith community organizer (the real Woodlawn "
            "Organization) who brokers the funding-for-transformation "
            "deal with Meji's organization, his real intentions "
            "complicated by an outcome he never controls."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-046",
        "category": "phase2-homage-la-underworld",
        "statement": (
            "Sauti, 'the Whistleblower,' added to Sankofa's crack-era "
            "saga (Kasi/Doyle/Moto, PH2-031/032/033). Homage to Gary "
            "Webb, the real journalist whose 1996 'Dark Alliance' "
            "reporting is the actual source of the CIA-Contra allegation "
            "Doyle's thread is built from -- real Webb's story ends in "
            "professional destruction and a disputed death, rewritten "
            "here as survival. Name is Swahili for 'voice.' An "
            "investigative reporter who won't let the story die even "
            "after his own paper backs away from it and his career takes "
            "the hit the real man's did. Built per the 'regular person' "
            "design principle (PH2-048): no combat ability, survives on "
            "caution and sourcing. Signature ability, 'The Nuisance': "
            "once Sauti has personally confirmed three independent "
            "sources for a claim, it can't be fully suppressed. Cost: "
            "protects the story, never the man -- no personal "
            "protection, no combat capability."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-047",
        "category": "phase2-homage-standalone",
        "statement": (
            "Duro and Doss, a standalone 'what if' not tied to any built "
            "territory, set in a small-town setting adjacent to the NYC "
            "cluster. Homage to Clay Tiffany, a real citizen journalist "
            "and public-access cable host broadcasting out of two small "
            "Westchester County, NY towns in the late 1990s/early 2000s, "
            "who spent years accusing a violent local police officer of "
            "corruption; the officer retaliated with real, escalating "
            "violence (1997-1999) including a beating that broke "
            "Tiffany's ribs and an orbital bone. Tiffany won an FBI "
            "investigation and a real $200,000 settlement but died alone "
            "in March 2015, months before the officer was revealed in "
            "2016 as a quadruple murderer (later a real Jeffrey Epstein "
            "cellmate), convicted 2023 and sentenced to four consecutive "
            "life terms in 2024. Rebuilt for this world's confirmed "
            "pre-industrial tech level (no broadcast media, PH2-049) as "
            "Duro, a public crier and pamphleteer -- Yoruba for "
            "'stand/persist/hold firm' -- who stands in the same market "
            "square reciting his findings and pressing hand-copied "
            "broadsheets ('Last Rites for Liars') into people's hands. "
            "The actual 'what if': Duro survives long enough, and pushes "
            "hard enough, that the reckoning he forces removes Doss from "
            "power years before Doss ever gets the chance to become a "
            "killer -- the real quadruple murder never happens here. "
            "Signature ability, 'The Copy That Survives': once spoken "
            "and written down, copies multiply faster than anyone can "
            "burn or confiscate them all. Cost: protects the words, "
            "never the man -- no combat capability, only stubbornness, "
            "luck, and Doss stopping just short of killing him. Doss "
            "(homage: Nicholas Tartaglione) is built on Gyp Rosetti's "
            "exact psychology -- a fragile ego that treats public "
            "exposure as a mortal insult and answers with brutal, "
            "escalating violence, matching the real 'you can't tell lies "
            "about me' line (rebuilt as 'in the square')."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-048",
        "category": "phase2-homage-standing-decision",
        "statement": (
            "Survival, mainline integration, and the 'what if' "
            "principle (standing decision, per Abad's explicit "
            "direction): the homage era is not sealed off from mainline "
            "Cian. Every homage-era character, across every city, is a "
            "comrade of Kanja's. This world's baseline lifespans already "
            "run hundreds to tens of thousands of years -- a character "
            "who survives their own origin-era conflict, rather than "
            "dying the way the real person did, has the intervening time "
            "to grow into an extraordinarily skilled, ancient veteran by "
            "Kanja's own era. New Chronicles will be written featuring "
            "Kanja himself, spanning both his Rebellion (ages 18-30) and "
            "his post-Rebellion/Long Mask era, with guest appearances by "
            "these now-ancient figures. The growing, accumulating number "
            "of them bleeds into Book 1 and becomes the reinforcement "
            "that turns the tide roughly midway through the five-book "
            "series. Survival is hand-picked by Abad case by case, not "
            "automatic -- reserved especially for figures whose real "
            "deaths left a genuine 'what if' feeling. Already applied: "
            "Kofi (PH2-040), Baale and Kra (PH2-021, amended), and Ohun "
            "(PH2-030, amended). Everything else built before this "
            "ruling stays exactly as written. Journalists and "
            "whistleblowers specifically get their own design principle: "
            "written as 'regular people,' not combat-tier leaders -- "
            "their signature traits keep them alive and effective in "
            "their own domain (documentation, sourcing, credibility, "
            "persistence) rather than granting physical combat power."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-049",
        "category": "phase2-homage-standing-decision",
        "statement": (
            "World tech level, reconfirmed for the homage era (standing "
            "decision): this world is firmly pre-industrial (Norse/"
            "Gothic and Roman/Imperial-styled nations per WC-012, "
            "ritual-forged Drakma weapons that explicitly cannot be "
            "industrialized per WC-013, no engines beyond the "
            "Drakma-resonance Hymn-Engine and the ancient Meridian "
            "Engine, no firearms, no electronic or broadcast media of "
            "any kind -- CULT-199 bans modern-tech metaphors outright). "
            "Homage-era characters whose real anchors used period tech "
            "that doesn't exist here (broadcast television, radios, "
            "etc.) get translated to period-appropriate in-world "
            "equivalents (public criers, hand-copied broadsheets and "
            "pamphlets) rather than keeping the real mechanism -- see "
            "PH2-047 (Duro and Doss). A possible future addition, "
            "floated but not yet drafted: early firearms (draftable/"
            "armor-piercing bullets), which if ever introduced would "
            "need to be culturally framed as cowardly by this world's "
            "own standards AND mechanically incapable of harming a "
            "density-scaled combatant regardless of sophistication."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Every piece in this batch was drafted in full and explicitly approved '
    'in-conversation across the same 2026-09-05 session. Kofi/Hampton\'s '
    'survival: "this will be along with New York City and LA Kanja\'s '
    'comrades... that\'s what we\'ll bleed into book one and start turning '
    'the tide Midway through the series." Scope of the survival principle: '
    '"Hampton now, a default going forward" (existing deaths elsewhere stay '
    'as built). Expanding it to Salazar and Huggins, and the journalist '
    'design principle: "I think that Salazar and Huggins will live and '
    'journalists will live cuz I want a regular person people can connect '
    'with on a human level... they will have attributes that will Aid in '
    'their survival but they will not be World beating Crushers in the '
    'physical sense... especially the journalists and The Whistleblower." '
    'Confirming survival is hand-picked, not automatic: "not every '
    'journalist will be able to survive but I will hand-pick those that '
    'will as we go." The Duro/Doss world-tech correction: "there are no on '
    'air or broadcasts here... this world should [not] have those type of '
    'communications because of its if you see my world there are no '
    'engines or anything like that." Final confirmation: "confirmed."'
)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    by_id = {r["id"]: r for r in ledger["rules"]}
    for rule_id, old_tail, new_tail in AMENDMENTS:
        assert rule_id in by_id, f"missing rule to amend: {rule_id}"
        statement = by_id[rule_id]["statement"]
        assert old_tail in statement, f"{rule_id}: expected old text not found"
        by_id[rule_id]["statement"] = statement.replace(old_tail, new_tail)
        assert new_tail in by_id[rule_id]["statement"], f"{rule_id}: amendment didn't apply"

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 60,
            "source_doc": (
                "Phase 2 pre-Book-1 homage-era conversational development "
                "(docs/lords-of-cian/phase2-homage-era-development.md) -- "
                "locks Chicago (the third homage-era city: 5 territories/"
                "leaders plus the Meji/Oluso twist thread), the new "
                "survival/mainline-integration standing decision, the "
                "world-tech-level reconfirmation, Sauti (LA), and the "
                "standalone Duro/Doss 'what if.' Amends PH2-021 and "
                "PH2-030 in place: Baale, Kra, and Ohun now survive their "
                "real-world-mirrored close calls."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "6.3"
    ledger["last_updated"] = "2026-09-05"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
