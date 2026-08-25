#!/usr/bin/env python3
"""Batch 37: World Adaptation Blueprint, Section VI Era G (The Lords of Cian and the Attia Role)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'World_Adaptation_Blueprint' (Google Drive fileId "
    "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA, Lore Vault), Section VI "
    "('The Lauris Letitia Chronicle'), Era G ('The Lords of Cian and the "
    "Attia Role') -- her integration into the crew, the Sephtis "
    "Conversation, the Kanja introduction, the Onyx introduction, the "
    "forging and delivery of Attia's Rite, her present-day crew "
    "relationships, the World Adaptation Observation, and her present-day "
    "operational status. Two proper-noun rulings applied per Abad's calls "
    "before drafting: Onyx's predecessor wielder, named 'Yuto Rexmar Haku' "
    "in the source, is locked as 'Yuto Haku' -- dropping 'Rexmar' since "
    "the already-locked timeline (MCD-110/MCD-... Jicome/Rexmar rules) has "
    "the Rexmar line beginning after Haku, not with him; and the source's "
    "claim that Yuto Haku 'defeated T.D.K. in his Era 12 containment "
    "program' is dropped in favor of the already-locked framing (CC-056, "
    "WC-020: Haku forced Anu Un Ra's retreat during the Deposition, ~5,000 "
    "years ago, via overstretch and Verehimu's betrayal), since 'Era 12' "
    "is a separate, much older era and the attribution conflicts with the "
    "locked Deposition mechanism. The source's 'Jicome'/'Verehimu' "
    "geography is kept renamed Kesmara/Voskharen per Batch 36's ruling, "
    "for continuity with the Era F rules. One chronology slip silently "
    "corrected, consistent with the Batch 36 precedent of dropping a "
    "contradictory age clause: the source describes the World Adaptation "
    "pattern recognition as occurring in Lauris's 'second century on Cian' "
    "while also placing it 'roughly a century' into her Lords of Cian "
    "tenure -- inconsistent with her already-locked ~2,000-year "
    "Directorate career preceding her recruitment (MCD-175, MCD-192). "
    "Locked here as 'roughly a century into her Lords of Cian tenure' "
    "only, dropping the contradictory 'second century on Cian' framing."
)

NEW_RULES = [
    {
        "id": "MCD-195",
        "category": "World Mechanics",
        "statement": (
            "Era G (the Lords of Cian and the Attia role) spans roughly "
            "200 years of Cian-time, from Lauris's arrival at the "
            "movement's operational headquarters following the Ezio "
            "meeting to the present-day timeline of My Rival's Distance. "
            "Her integration was procedural rather than cultural: the "
            "calibration of the Attia role against the crew's command "
            "structure and the establishment of working relationships "
            "with the senior crew, not assimilation. At her arrival, the "
            "Lords of Cian's operational core comprised Kanja Rexmar "
            "(Captain), Onyx of Oblivion (Kanja's sentient longsword), "
            "Ezio Valcari (Architect, her principal), Sephtis (Archivist), "
            "and roughly fourteen other senior figures, atop a broader "
            "movement of roughly 200 people across territorial cells. "
            "Ezio personally conducted her staggered introductions to the "
            "senior crew across three weeks: Sephtis on day one, Kanja on "
            "day three, Onyx on day five."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-196",
        "category": "World Mechanics",
        "statement": (
            "Sephtis's introduction to Lauris, conducted alone in the "
            "Karkosa's archive room across a fourteen-hour conversation, "
            "opened with his disclosure that he had known of her existence "
            "since the orbital-trade rumor reports following the Vask "
            "Olmedrin defense -- roughly 1,200 years before her arrival on "
            "Cian -- making him the only being on the planet continuously "
            "aware of her since before she arrived. He then presented "
            "archival records of Anu Un Ra's programs across roughly "
            "76,000 years of Cian history, including the K-strand decline "
            "operation and the Old Dominion's engineered collapse, "
            "substantially exceeding what Ezio had outlined at the "
            "Recruitment Meeting; Lauris assessed this as the single most "
            "operationally valuable disclosure of her integration period."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-197",
        "category": "World Mechanics",
        "statement": (
            "Sephtis confirmed to Lauris, during their introductory "
            "conversation, that he already maintained operational contact "
            "with Kareth-Vassen Aerelin (having learned of the "
            "Lauris-Aerelin alliance from Aerelin herself roughly twelve "
            "years before Lauris's defection), and that this contact "
            "would remain his personally rather than a Lords of Cian "
            "command function -- the wider crew does not know of Aerelin. "
            "Going forward, Lauris coordinates with Aerelin through "
            "Sephtis as the sole channel. Sephtis and Lauris also "
            "established a standing joint archive, cross-referencing her "
            "operational and personal records against his archival "
            "accumulation on the engineering tradition's history; the "
            "joint archive is not disclosed to the wider crew, Ezio knows "
            "of its existence without having requested access, and Kanja "
            "does not know of it at all."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-198",
        "category": "World Mechanics",
        "statement": (
            "Sephtis disclosed that Val Mirel Kareth (Ozmund's mother) "
            "became aware of Lauris's existence roughly six months after "
            "her arrival on Cian, through Kareth War-Order intelligence "
            "intersecting with Directorate contractor records, and had "
            "been tracking her operational profile at a distance for "
            "roughly 1,800 years without initiating contact -- consistent "
            "with War-Order protocol of deliberate non-contact toward "
            "Karesian-substrate operatives outside its direct command "
            "unless the operative requests it. Offered a broker-contact "
            "option, Lauris declined: 'Not yet. The contact will occur "
            "when operational circumstances require it... The operational "
            "reason will eventually arise.' As of the present-day "
            "timeline, that reason has not arisen; Lauris and Val Mirel "
            "remain in parallel operational alignment without direct "
            "contact, with Sephtis holding the broker-contact protocol on "
            "standby."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-199",
        "category": "World Mechanics",
        "statement": (
            "Kanja's introduction to Lauris was conducted in the "
            "Karkosa's primary forge, his own choice of venue so he could "
            "observe how a new crew member moved among his tools; her "
            "proprioceptive accuracy in reading the forge's working state "
            "registered, on his unspoken assessment, as matching his "
            "mother's pattern. He confirmed his command authority and the "
            "Attia role's operational scope, including the three "
            "conditions Lauris had negotiated at the Recruitment Meeting "
            "(MCD-194), without attempting to renegotiate any of them, and "
            "acknowledged that his command authority does not extend to "
            "her independent agenda or her active-combat judgment."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-200",
        "category": "World Mechanics",
        "statement": (
            "Near the end of the Kanja introduction, Kanja asked Lauris "
            "whether the engineering tradition's cooperative-era Karesian "
            "technical materials (MCD-181) had come from his mother's "
            "people (the Kareth War-Order diaspora) or from hers -- a "
            "question precise enough to show he already understood his "
            "mother's biology was Karesian-derived rather than purely "
            "Cian-born, though not yet its full extent. Lauris answered "
            "that the materials originated from Kares Prime itself, "
            "acquired directly from the homeworld during the deep "
            "cooperative era, predating the diaspora that produced his "
            "mother's people. Kanja's response -- 'Your homeworld. Not my "
            "mother's people. The homeworld.' -- registered his "
            "recognition that Lauris was homeworld-native rather than "
            "diaspora-descended. Lauris did not clarify further: "
            "extending the same deferral she'd established with Ezio "
            "(MCD-194), she has not told Kanja that she is the synthesis "
            "evolution, the last of her kind, or the biological source "
            "population his mother's line descends from. As of the "
            "present-day timeline this remains undisclosed; the Codex's "
            "Blueprint Eye ability has not yet performed a reading of her "
            "that would close the gap."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-201",
        "category": "World Mechanics",
        "statement": (
            "Onyx's introduction to Lauris, conducted in the captain's "
            "cabin with Kanja present (Onyx communicates only through "
            "whoever holds its grip), took roughly ninety seconds: Kanja "
            "extended the sword grip-first as a gesture of availability "
            "rather than transfer, and Onyx's silent evaluation of her "
            "biological signature, density profile, and combat history "
            "concluded with a positive judgment -- Operationally Aligned "
            "-- and her permanent addition to the Black Ledger. Onyx then "
            "conveyed, through Kanja, that the Black Ledger had held a "
            "space reserved for her for roughly 1,200 years, a reservation "
            "traced to Onyx's predecessor wielder: Yuto Haku, Kanja's "
            "revered ancestor already locked as the only being to force "
            "Anu Un Ra's retreat (CC-056, WC-020). Yuto had known of her "
            "eventual arrival, via the same orbital-trade rumor network "
            "Sephtis had drawn on, without knowing her name, and had "
            "reserved the space anyway; the reservation survived his "
            "death and every wielder transition since, until Lauris "
            "claimed it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-202",
        "category": "World Mechanics",
        "statement": (
            "Lauris's introductions to the rest of the senior crew across "
            "the following two weeks produced no operational friction. "
            "The crew organically adopted a set of nicknames for her "
            "within her first month aboard -- Little Heavy, the "
            "Anchor-Girl, Gravity's Daughter, the Soft Hammer, Iron "
            "Flower, the Quiet Weight -- which she neither solicited nor "
            "discouraged; her acceptance of them functioned as her "
            "acceptance of the crew's own social structure on its own "
            "terms, and all remain in active, interchangeable informal "
            "use as of the present-day timeline."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-203",
        "category": "World Mechanics",
        "statement": (
            "Roughly fourteen months after Lauris's recruitment, Ezio "
            "commissioned Kanja to forge Attia's Rite: a leaf-shaped "
            "breaker meant to serve simultaneously as the operational "
            "weapon for her crowd-management discipline (already locked "
            "at MCD-170 as the fourth Karth-Sera discipline) and as the "
            "Attia role's symbolic instrument. Kanja forged it in eleven "
            "continuous days at the Karkosa's forge, using pattern-welded "
            "steel infused with Drakma from Mao Volcano's caldera during "
            "an unrelated supply stop. The completed breaker measures "
            "roughly 720mm, leaf-bladed, and weighs roughly three times "
            "what the same design would weigh for a Cian-born wielder -- "
            "calibrated specifically to her grip strength and "
            "combat-progression curve rather than to standard "
            "ergonomics."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-204",
        "category": "World Mechanics",
        "statement": (
            "At the delivery of Attia's Rite, conducted privately between "
            "Kanja and Lauris (Ezio present as nominal commissioner), "
            "Lauris recognized the breaker as more precisely calibrated to "
            "her combat methodology than any weapon she had carried, "
            "including the Spine of Dagon. She told Kanja: 'This breaker "
            "carries the discipline that my Sister-Hold trained me in for "
            "six hundred years... After today, the discipline's name on "
            "Cian will be the breaker's name. The discipline's previous "
            "name on my homeworld is no longer in operational use. I am, "
            "in functional terms, transferring the naming authority to "
            "your forge. The naming authority belongs to you. I accept "
            "the transfer.' Kanja accepted: 'The discipline's name on "
            "Cian is Attia's Rite. The forge accepts the naming "
            "authority. The forge will hold it until you require its "
            "return.' Since the exchange, Kanja has also become her "
            "equipment's primary maintenance authority on Cian, "
            "periodically refining and recalibrating the Spine of Dagon "
            "and the Aristocrat alongside Attia's Rite."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-205",
        "category": "World Mechanics",
        "statement": (
            "Lauris's present-day relationship with Ezio operates through "
            "communication protocols compressed to a single word or "
            "gesture, each reading the other's operational intent without "
            "further specification; he provides strategic direction, she "
            "provides survivable execution, and the Recruitment Meeting's "
            "three conditions (MCD-194) remain inviolate. Her relationship "
            "with Kanja is more complicated: he treats her, per Sephtis's "
            "own assessment, with a deference exceeding standard "
            "Captain-to-Sergeant-at-Arms protocol -- correct in instinct, "
            "incomplete in understanding, since he does not yet know her "
            "biology is the literal source population his mother's line "
            "descends from (MCD-200). He is also, independent of that "
            "unresolved recognition, her primary equipment-maintenance "
            "authority on Cian."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-206",
        "category": "World Mechanics",
        "statement": (
            "Lauris's relationship with Onyx runs entirely through "
            "Kanja's mediation, since she does not wield the blade "
            "herself. Her closest operational alliance aboard the Karkosa "
            "is with Sephtis: their joint archive (MCD-197) is, on "
            "Sephtis's own assessment, the single most comprehensive "
            "understanding of Anu Un Ra's long-cycle programs that exists "
            "outside his own apparatus. Her closest thing to a "
            "Karth-Ven-style sparring partner is Valen (Sinisterblade), "
            "who recognizes her combat methodology as a mirror of his own "
            "and whose Codex-documented alias for her is 'the Other "
            "Patience'; the two spar roughly weekly when ship operations "
            "permit, and it is her primary combat-conditioning "
            "maintenance in the present-day timeline. Her relationships "
            "with the rest of the senior crew are professionally adequate "
            "without being personally substantive -- operationally "
            "integrated, socially distinct, culturally undemanding, on "
            "Sephtis's own characterization."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-207",
        "category": "World Mechanics",
        "statement": (
            "Lauris's first detection of anomalous ground response on "
            "Cian occurred roughly two months after her arrival, during "
            "reconnaissance through Kesmara's harbor district: certain "
            "paving stones responded to her weight with subtle stiffness "
            "traceable to Living Drakma concentrations that should not "
            "have been present in ordinary sedimentary stone. She filed "
            "the observation without reporting it. The count of affected "
            "locations grew from roughly 14 within her first year to "
            "roughly 80 within her first decade to roughly 240 by her "
            "fifth decade, clustering around the major coastal cities of "
            "the Kesmara and Voskharen regions with secondary "
            "concentrations at locations that would later have Lords of "
            "Cian operational presence."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-208",
        "category": "World Mechanics",
        "statement": (
            "Roughly a century into her tenure with the Lords of Cian, "
            "Lauris detected the same anomaly at double magnitude in the "
            "Karkosa's home harbor -- a location with no known history of "
            "engineering-tradition activity. She raised the observation "
            "to Sephtis, whose archives had no direct precedent but did "
            "contain the Talisman of Mao's canonical but previously "
            "untested Stage 2 'Foundry Anvil (planetary structural "
            "repair)' specification. Fourteen weeks of joint research "
            "confirmed the Talisman had been autonomously running Stage 2 "
            "for roughly three centuries, incorporating Living Drakma "
            "into the geological substrate around Kanja's operational "
            "presence -- the mechanism underlying the World Adaptation "
            "phenomena already locked at MCD-146/147. Lauris's continuous "
            "geological observation across Lords of Cian territories, "
            "cross-referenced against Sephtis's archival framework, has "
            "since produced a quantified model of the planet's adaptation "
            "curve (documented in the Blueprint's Section V). The "
            "intelligence is held jointly by Lauris and Sephtis, not "
            "centralized in Lords of Cian command: Ezio knows of its "
            "existence without requesting access, and Kanja -- per the "
            "standing mandate that he not know what his own Talisman has "
            "been doing on his behalf -- does not know of it at all, as "
            "of the present-day timeline."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-209",
        "category": "World Mechanics",
        "statement": (
            "Lauris's present-day combat profile: static density "
            "~14,000x, rising through her combat-progression curve to "
            "~18,000x at one minute, ~22,000x at thirty minutes, "
            "~26,000x at sixty minutes, and approaching ~30,000x past "
            "ninety minutes, with no measurable fatigue threshold. Her "
            "tactical profile (Compact Siege) wins through duration "
            "rather than opening force. Across roughly 4,000 years of "
            "combat she has never been defeated, killed, or surrendered a "
            "fight, though she has been delayed, contained, or fought to "
            "a standstill; her only meaningful moments of risk have come "
            "in engagements resolved in under five minutes, before her "
            "combat-progression curve could activate. Her plausible "
            "theoretical defeat conditions are opponents who could end a "
            "fight in its opening seconds: Anu Un Ra's Warbody at "
            "sustained Sovereign Mass with Predictive Oracle architecture, "
            "Kanja's Density Spike at limitless impact if it connects "
            "immediately, or Orlok at post-enlightenment ~30,000x if he "
            "specifically cultivated a discipline against her profile "
            "(which he has not, having never engaged her). Operation 28's "
            "post-Sister-Hold subject (MCD-186) remains the closest any "
            "opponent has come to matching her specifically, despite that "
            "subject's engineered constraints."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-210",
        "category": "World Mechanics",
        "statement": (
            "Lauris is one of four identified threats to Anu Un Ra's "
            "Warbody platform (alongside Valen, already locked as the "
            "Warbody's worst-case matchup). Her threat methodology denies "
            "the Warbody's reset cycles and accumulates stability debt "
            "through sustained contact, exploiting the fact that her "
            "combat-progression curve can outlast the Warbody's stability "
            "reserves -- contingent on establishing and holding sustained "
            "contact against the Warbody's superior Predictive-Oracle-"
            "driven mobility, which is her operational bottleneck rather "
            "than her raw capability. The Lords of Cian's strategic "
            "planning treats an eventual Lauris-vs-Warbody engagement as "
            "a coordinated multi-asset operation to position her into "
            "sustained contact, not a solo engagement; the coordination's "
            "specific operational details are not part of this "
            "chronicle."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-211",
        "category": "World Mechanics",
        "statement": (
            "Among Lauris's active operational debts (the Drowning "
            "Vault's 120, MCD-183; the third withheld Operation 38 "
            "facility, MCD-191; the relocated cave-system subjects "
            "awaiting revival, MCD-190/193; and the unresolved Verith "
            "question deferred to a future Val Mirel conversation, "
            "MCD-180), one is new to Era G: the Iron-Speakers of Kares "
            "Prime asked, at her departure (MCD-174), that she preserve a "
            "record of what she found beyond the homeworld as the "
            "civilization's sole continuing testimony. That record is her "
            "personal archive aboard the Karkosa -- the same archive this "
            "chronicle draws from -- and its ongoing existence is, in the "
            "chronicle's own framing, the debt's discharge already in "
            "progress rather than a future obligation."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation, including both proper-noun rulings on Yuto Haku (dropping "Rexmar" and the "Era 12" attribution): "lock it"'


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
            "batch": 37,
            "source_doc": "World_Adaptation_Blueprint (Section VI, Era G: The Lords of Cian and the Attia Role)",
            "source_id": "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 2,
            "conflicts_resolved": 2,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "4.0"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
