#!/usr/bin/env python3
"""Batch 36: World Adaptation Blueprint, Section VI Era F (The Contractor Years)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'World_Adaptation_Blueprint' (Google Drive fileId "
    "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA, Lore Vault), Section VI "
    "('The Lauris Letitia Chronicle'), Era F ('The Contractor Years') -- her "
    "forty documented Sealbound Directorate contracts across four "
    "operational sub-eras, the Defection Interval, and the Ezio recruitment "
    "meeting. Two renames applied throughout to avoid proper-noun collision "
    "with already-locked canon: the source's 'Jicome' (the Sealbound "
    "Directorate's headquarters city) is renamed Kesmara, distinct from the "
    "already-locked nation of Jicome (Kanja's homeland, MCD-110); the "
    "source's 'Verehimu' (a coastal region/trench/naval authority) is "
    "renamed Voskharen, distinct from House Verehimu (Ozmund's noble "
    "bloodline). Both renames approved by Abad in-conversation before "
    "drafting. The source document's inconsistent 'Karren Highlands' / "
    "'Korren Highlands' spelling (same region) is normalized to Korren "
    "Highlands throughout -- a document-internal spelling drift, not a "
    "canon collision. The source's garbled opening age-arithmetic clause "
    "('departed Kares Prime at approximately age 4,000 minus 2,000 -- "
    "meaning she arrived at age approximately 2,000'), which contradicts "
    "the already-locked MCD-174 departure age of ~4,000, is dropped; only "
    "the unambiguous arrival timing (~2,000 years before present-day "
    "events) is kept. MCD-184 resolves an apparent tension with the "
    "already-locked 'T.D.K.'s 5,000-year dormancy' (Book 1 epilogue, which "
    "Era F falls entirely inside) per Abad's ruling: the engineering "
    "tradition's automated apparatus and subordinate administrators adapt "
    "to and study Lauris across Era F, not Anu Un Ra's own personal "
    "attention -- consistent with the already-locked pattern that the "
    "K-strand decline ran 'on autopilot' without his active involvement."
)

NEW_RULES = [
    {
        "id": "MCD-175",
        "category": "World Mechanics",
        "statement": (
            "Lauris arrived on Cian approximately 2,000 years before the "
            "present-day events of My Rival's Distance, making planetfall "
            "at the orbital descent station of Kesmara, the Sealbound "
            "Directorate's headquartered city (renamed from the source "
            "document's 'Jicome' to avoid collision with the already-locked "
            "nation of Jicome, Kanja's homeland). The Directorate's intake "
            "protocols flagged her unclassified, unprecedented-density "
            "Karesian profile; Operations Director Iyellen Macresh reviewed "
            "the flag, cross-referenced it against centuries of "
            "rumor-network reports stemming from the Vask Olmedrin defense, "
            "and within a month of Lauris's arrival extended her the "
            "Directorate's highest non-employee classification, Tier-1 "
            "External Asset. Lauris accepted without fully understanding "
            "what the Directorate was; the acceptance entered Directorate "
            "records as recruitment of External Asset Designation LL-001."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-176",
        "category": "World Mechanics",
        "statement": (
            "During her first three centuries or so on Cian, Lauris "
            "commissioned the three weapons of her original Forged Triad "
            "from the volcanic forge at Mao (the same forging tradition "
            "that later produces Kanja's Mafesto, Obsidian Malice, and the "
            "Talisman of Mao): the Spine of Dagon (fossilized Dragonbone "
            "infused with molten Drakma, delivered ~78 years after "
            "commission, its spatial-folding sheath built to preserve her "
            "petite-frame deception), the Aristocrat (a rapier from "
            "pre-aligned Drakma, delivered ~31 years after commission), and "
            "the Integrated Variable Phalanx (the three-shield "
            "Night-Glass/Solar-Spire/Phoenix-Guard system with Memory-Plate "
            "Technology, ~247 years in development, its Triad-Lock fusion "
            "mode the longest single component at ~80 years). Attia's "
            "Rite, her fourth weapon, was not part of this original Triad; "
            "it is commissioned ~1,400 years later by Ezio Valcari from "
            "Kanja Rexmar as a gift marking her acceptance of the Attia "
            "role (Era G). On Cian, her four Karth-Sera combat disciplines "
            "(already locked at MCD-170) became known by the weapons that "
            "channel them, cementing weapon and discipline as a single "
            "name by the time she meets Kanja."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-177",
        "category": "World Mechanics",
        "statement": (
            "Lauris's onboarding as External Asset LL-001 was conducted at "
            "the Directorate's External Operations Coordination Center in "
            "Kesmara's Eastern District -- itself an old, repurposed "
            "containment substation from Anu Un Ra's original Era 11-12 "
            "Ionic Rite program, though the Directorate no longer knew "
            "this about its own facility. She completed the standard "
            "fourteen-month contractor curriculum in roughly three months "
            "and was paired for mentored supervision with senior "
            "contractor Vael Korr-Drennen (External Asset MR-014, ~800 "
            "years' Cian experience). Vael's mentorship report at the end "
            "of her ten Apprentice Contracts concluded: 'She does not need "
            "me. She did not need me from the second day. The institution "
            "should plan accordingly.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-178",
        "category": "World Mechanics",
        "statement": (
            "Lauris's first ten Directorate contracts (the Apprentice "
            "Contracts) closed with her upgrade to Senior External Asset. "
            "Three of the ten produced her first encounters with inherited "
            "Ionic Rite architecture, though she did not yet have a "
            "framework to identify it as such: the Iron-Spire (Op. 3, a "
            "malfunctioning resonance node whose defensive subroutines "
            "could not harm Karesian biology), the Black Choir's substation "
            "(Op. 7, a resonance field that had induced collective "
            "vocal-amplification capability in fourteen ungifted women), "
            "and a sealed container excavated from the Velkar riverbed "
            "(Op. 8, of unknown contents, delivered unopened to the "
            "Directorate's senior archive, where it remains sealed in the "
            "present day). Her tenth contract closed the period by ending "
            "it: Operations Director Iyellen Macresh, the same officer who "
            "had recruited her, was exposed for embezzlement and, when "
            "three prior Internal Affairs attempts failed, was terminated "
            "by Lauris herself at Iyellen's private estate in the Kesmara "
            "Eastern Hills."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-179",
        "category": "World Mechanics",
        "statement": (
            "Operations 11 through 22 (the Established Hunter period) "
            "produced the aliases that follow Lauris through her Cian "
            "career -- the Wall That Walks, Heavy-Ordnance Letitia, the "
            "Thing That Won't Move, the Petite Catastrophe, the Compact "
            "Siege -- and the period's first direct evidence that the "
            "engineering tradition beneath the Directorate had been "
            "processing Karesian biology: the Salt-Locked Archive's "
            "guardian construct (Op. 15), an 800-year-old humanoid "
            "combatant built from Karesian genetic substrate and trained "
            "in disciplinary forms drawn from deep Karesian archival "
            "access; and the Drowning Vault (Op. 17), a submerged "
            "Directorate site where Lauris's breach clearance revealed "
            "roughly 200 additional Karesian-derived subjects held in "
            "long-term suspended-development containment behind the "
            "breach she had just resealed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-180",
        "category": "World Mechanics",
        "statement": (
            "During the Established Hunter period, Lauris's Operation 18 "
            "contract targeted a Cian-born-presenting woman using the "
            "alias 'Verith,' who displayed Karesian-class density (~6,000x "
            "static, ~12,000x sustained), cooperative-era Karesian combat "
            "forms, and spontaneous cooperative-era Karesian vocabulary. "
            "Lauris's post-engagement archival assessment concluded Verith "
            "was not Cian-born at all: she was an engineered Karesian, "
            "raised roughly 37 years in an undisclosed containment program "
            "from cooperative-era genetic source material, whose language "
            "and combat training implied that program had access to "
            "living cooperative-era Karesian linguistic and disciplinary "
            "input. Lauris terminated her in the closing engagement rather "
            "than deliver her to Directorate processing, judging a clean "
            "death preferable to what acquisition would have meant; she "
            "recorded this as the most morally complicated decision of her "
            "Directorate career and has deferred the question of whether "
            "it was right to a future conversation with Val Mirel, which "
            "has not yet occurred. Verith was the first engineered "
            "Karesian Lauris encountered alive, and the moment she stopped "
            "considering herself the last of her kind on Cian."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-181",
        "category": "World Mechanics",
        "statement": (
            "Operation 23 sent Lauris into the Iron-Halls of Velkar "
            "(unrelated to Kares Prime's own Iron-Halls of Vask, a naming "
            "coincidence she noted in her archive), where a malfunctioning "
            "polarity-control apparatus carried operational instrumentation "
            "written in cooperative-era Karesian technical language -- a "
            "language never exported outside Karesian internal use. This "
            "is the evidence that let Lauris independently conclude, well "
            "before her later confirmation, that the K-strand decline "
            "(MCD-153 through MCD-157) had been deliberate engineering "
            "rather than natural biological catastrophe, and that whoever "
            "was responsible had obtained Karesian technical and "
            "biological material directly from Kares Prime during the "
            "deep cooperative era."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-182",
        "category": "World Mechanics",
        "statement": (
            "Operation 24 pitted Lauris against a fluctuating-density "
            "entity (Subject AE-001) whose post-mortem biological "
            "structure matched neither Karesian nor Cian-born substrate. "
            "The encounter is Lauris's first direct evidence that the "
            "engineering tradition's source materials were not limited to "
            "Karesian biology -- that other, unidentified species were "
            "being processed by the same apparatus at other facilities "
            "she had not yet located."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-183",
        "category": "World Mechanics",
        "statement": (
            "A second Drowning Vault breach (Op. 25) released 80 of its "
            "secured population; Lauris hunted the dispersed subjects "
            "across 28 months using Karesian-to-Karesian biological "
            "signature detection, then conducted a full site inspection "
            "that revealed the Vault's true nature: a 12,000+ year "
            "continuous-generation and suspended-maintenance facility, "
            "with 120 Karesian-derived subjects (ages 20 to 8,000 years at "
            "generation) still secured within it. Lauris recorded a "
            "personal commitment in her archive to release them once she "
            "was no longer a Directorate contractor. As of the present-day "
            "timeline, the commitment is unfulfilled; the 120 remain "
            "secured in the Drowning Vault, and their release is an "
            "acknowledged, unresolved Lords of Cian operational debt."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-184",
        "category": "World Mechanics",
        "statement": (
            "Operation 26's target, insurgent leader Veth Korr, was found "
            "on Lauris's exit reconnaissance to have been founded and "
            "resourced by the same engineering-tradition apparatus "
            "operating beneath the Directorate -- a movement engineered to "
            "draw the Directorate's highest-capability asset into a "
            "controlled, observable engagement. From this operation "
            "forward, Lauris operated on the understanding that the "
            "apparatus's inherited protocols and facilities were adapting "
            "to and studying her specific combat methodology across her "
            "career, feeding that data back into subsequent facility and "
            "subject designs (see MCD-186, the Operation 28 'Copy'). This "
            "adaptation is the automated apparatus and its subordinate "
            "administrators responding to accumulating operational data, "
            "not Anu Un Ra's own personal attention -- consistent with his "
            "established 5,000-year post-Deposition dormancy; the "
            "Cian-resident program has run on inherited protocol since "
            "long before Lauris's arrival."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-185",
        "category": "World Mechanics",
        "statement": (
            "Operation 27 located and destroyed a Tide-Wraith breeding "
            "substrate in the Voskharen Trench (roughly 14 adults, ~400 "
            "juveniles, plus the generative substrate itself), following "
            "two earlier Tide-Wraith engagements (Op. 11's juvenile, Op. "
            "21's adult). The species was revealed as engineered rather "
            "than naturally evolved -- an Ionic-Rite-derived production "
            "line rather than a natural predator lineage -- and was "
            "believed biologically extinguished on Cian at the time. "
            "Operation 39 (see MCD-191) later disproves this: a second "
            "production substrate exists in the Far Trench."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-186",
        "category": "World Mechanics",
        "statement": (
            "Operation 28 pitted Lauris against a cluster of seven "
            "engineered Karesian subjects, the last of whom fought using "
            "her own Karth-Sera curriculum (MCD-169-170) rather than "
            "cooperative-era or Sister-Hold-era forms. The subject's "
            "combat capability and bearing closely mirrored Lauris's own "
            "development around age 2,400; Lauris's working conclusion, "
            "recorded in her personal archive, is that the engineering "
            "tradition has been observing her Cian operations closely "
            "enough to reverse-engineer Karth-Sera from her operational "
            "behavior alone, rather than possessing an independent copy of "
            "the curriculum from Kares Prime. She terminated the subject "
            "and has never resolved, in writing, how to feel about it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-187",
        "category": "World Mechanics",
        "statement": (
            "Operation 29's target, a fleeing engineered Karesian subject "
            "(Designation CP-414), spoke to Lauris during their "
            "engagement's final minutes: details of additional "
            "engineering-tradition facilities in the Korren Highlands, the "
            "mispronounced name of the tradition's senior coordinator "
            "(which Lauris would not recognize as Anu Un Ra until "
            "Operation 34), and a final statement immediately before "
            "Lauris's terminating strike -- 'You were not the first. You "
            "will not be the last. We are the same. Run.' Lauris "
            "terminated her as contracted, but the message shaped every "
            "operation she conducted afterward."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-188",
        "category": "World Mechanics",
        "statement": (
            "Using Operation 29's intelligence, Lauris began directing her "
            "own contract acceptances toward the Korren Highlands. "
            "Operation 30's Site Recovery contract let her conduct covert "
            "reconnaissance of a nearby facility (later designated Site "
            "K-Theta): ~8 square kilometers, partially subterranean, ~200 "
            "mixed-biology personnel plus contained engineered Karesian "
            "subjects. This is the first direct intelligence the Lords of "
            "Cian's eventual movement would have on the tradition's "
            "primary Cian facilities; Lauris would deliver it to Sephtis "
            "after her defection, and Sephtis independently recognized the "
            "site from his own archives under the same designation."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-189",
        "category": "World Mechanics",
        "statement": (
            "Operation 31's target, Subject IM-099, turned out to be "
            "Kareth-Vassen Aerelin: a Cian-diaspora Kareth War-Order "
            "operative (~80,000 years old, lower Cian-native density "
            "profile) running an autonomous, centrally-unaffiliated 60-year "
            "campaign against the engineering tradition's trafficking "
            "networks under organized-crime cover. Lauris and Aerelin "
            "recognized each other as aligned rather than opposed, formed "
            "an ongoing informal intelligence alliance, and staged "
            "Aerelin's apparent termination to close the Directorate's "
            "contract. Aerelin remains active in the present-day timeline "
            "as an off-page Lords of Cian intelligence source; her contact "
            "is maintained solely by Sephtis, and the wider crew does not "
            "know of her."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-190",
        "category": "World Mechanics",
        "statement": (
            "Operation 32 destroyed a Living-Drakma-adjacent biological "
            "raw-material production substrate off the Voskharen coast -- "
            "the single most damaging act of sabotage against the "
            "engineering tradition in Lauris's contractor career. "
            "Operation 34 cleared Site K-Theta itself (see MCD-188): its "
            "~60 active-duty and ~200 contained engineered Karesian "
            "subjects were engaged, but rather than reseal or destroy the "
            "200 contained subjects, Lauris covertly relocated them to a "
            "concealed cave system roughly 14 kilometers away -- her first "
            "action taken entirely outside Directorate authority. The "
            "facility's central generator documentation, read during its "
            "destruction, named the engineering tradition's senior "
            "coordinator: Anu Un Ra. Lauris recognized the name from "
            "Operation 29's mispronounced hint and would not fully connect "
            "it to T.D.K.'s broader history until Ezio briefed her after "
            "her defection (MCD-194)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-191",
        "category": "World Mechanics",
        "statement": (
            "Across her final six operations before defection, Lauris "
            "used Directorate cover to systematically work against the "
            "apparatus she'd been hired to serve: Operation 35 expanded "
            "her working Kareth War-Order contact from Aerelin alone to "
            "roughly 18 autonomous operatives, while her Directorate "
            "intelligence report on the same activity deliberately "
            "mischaracterized its true nature to protect it. Operation 36 "
            "found and destroyed fourteen smaller redundancy nodes at the "
            "Vask of the Hollow that her earlier Operation 20 clearance "
            "had missed, confirming the tradition built distributed "
            "redundancy into its facilities generally. Operation 37 was "
            "her first openly joint operation with Aerelin's network -- "
            "three coordinated facility clearances, roughly 280 engineered "
            "Karesian subjects rescued to concealment rather than left to "
            "Directorate processing. Operation 38 saw Lauris deliberately "
            "withhold three of seven discovered secondary facilities "
            "(holding roughly 480 subjects) from her Directorate report, "
            "judging the arithmetic favored preserving them for her own "
            "post-defection rescue operations over immediate "
            "Directorate-authorized clearance by other contractors; two of "
            "the three have since been cleared, the third remains an open "
            "Lords of Cian objective as of the present-day timeline. "
            "Operation 39 located and destroyed a second Tide-Wraith "
            "production substrate in the Far Trench, disproving Operation "
            "27's assumption that the species had been fully "
            "extinguished."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-192",
        "category": "World Mechanics",
        "statement": (
            "Lauris's fortieth and final Directorate contract targeted "
            "Hellem Veth-Kovan, a senior Operations Director exposed by "
            "Internal Investigations for embezzlement that was, in fact, "
            "Kareth War-Order operational funding for Aerelin's network "
            "across 80 years of his deep cover. Lauris and Aerelin agreed "
            "his exposure was terminal regardless of Lauris's choice, and "
            "that Lauris executing him herself would mean a clean death "
            "and the chance to receive his compiled intelligence before "
            "the tradition's compromised Internal Investigations assets "
            "could reach him first. She did so at the same Kesmara Eastern "
            "Hills estate where she had terminated Iyellen Macresh in "
            "Operation 10 -- deliberately mirroring her first Directorate "
            "contract with her last, but inverted: Iyellen's termination "
            "served the institution, Veth-Kovan's served the Kareth "
            "War-Order operative he actually was. Lauris's formal "
            "defection began the next morning; the Directorate would "
            "classify her as Reclassified -- Hostile within days."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-193",
        "category": "World Mechanics",
        "statement": (
            "The roughly two months between Operation 40 and Lauris's "
            "recruitment by Ezio Valcari were the only period since her "
            "birth in which she held no institutional affiliation. She "
            "moved between fourteen Aerelin-prepared safe-houses, "
            "terminating three Directorate tracking teams without "
            "incident, and spent the interval securing the relocated "
            "engineered-Karesian cave systems (Site K-Theta's 200, per "
            "MCD-190) for long-term concealment. Knowledge of the cave "
            "systems is staged within the Lords of Cian: Sephtis learns of "
            "them within roughly two years of Lauris's recruitment, Ezio "
            "within roughly five years; Kanja and the wider crew do not "
            "know of them as of the present-day timeline, a detail "
            "reserved for a future book."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-194",
        "category": "World Mechanics",
        "statement": (
            "Ezio Valcari, having observed Lauris's Directorate career "
            "from a distance for roughly two decades, arranged her "
            "recruitment meeting through Aerelin's mediation at a private "
            "coastal residence. Fermand Aurelias accompanied Ezio and "
            "withdrew to a side room, leaving the two to speak alone. "
            "Lauris's biological-signature sense registered Ezio's body as "
            "inconsistent with his public 'non-combatant theorist' "
            "identity -- density and structural-resonance markers she "
            "recognized as Karesian-related -- and the two explicitly "
            "agreed not to discuss it; the arrangement still holds as of "
            "the present-day timeline, and Lauris has never raised what "
            "she has since observed of his hidden capability in the "
            "field. Ezio briefed her on Anu Un Ra's broader operational "
            "history via Sephtis's archives, converting her Operation-34 "
            "discovery into full strategic context, and offered her the "
            "Attia role. She accepted on three conditions, all agreed "
            "without modification: her independent agenda regarding "
            "engineered Karesian subjects (the Drowning Vault's 120, the "
            "withheld Operation 38 facility, her Kares Prime preservation "
            "commitments) takes precedence over Lords of Cian operational "
            "requirements when the two conflict; her relationship with "
            "Aerelin and the Kareth War-Order network stays on terms she "
            "controls rather than the movement's central command; and her "
            "authority over her own combat deployment decisions is "
            "absolute."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation, including both proper-noun renames (Jicome->Kesmara, Verehimu->Voskharen) and the dormancy-conflict resolution (automated apparatus, not T.D.K. personally): "LOCK IT"'


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
            "batch": 36,
            "source_doc": "World_Adaptation_Blueprint (Section VI, Era F: The Contractor Years -- forty operations, the Defection Interval, the Ezio meeting)",
            "source_id": "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 3,
            "conflicts_resolved": 3,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "3.9"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
