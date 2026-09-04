#!/usr/bin/env python3
"""Batch 53: Phase 1b, third document. The Lauris/Anirak Threat
Development Blueprint -- Lauris's Anomalous Mass/Density Saturation
mechanics and the three Kareth-sister artifacts (the Convergence, the
Gradient, the Patient Stone), Anirak's Fury Variant/Escalation States
mechanics, both characters' four "wrinkles" each, hard constraints for
future drafting, and a combined Lauris+Anirak operational note. 18 new
ARS- rules, one resolving a pre-existing flagged naming conflict."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Lauris_Anirak_Threat_Blueprint.docx (Google Drive fileId "
    "1A3HTRglwNhILAER2GhHRZnyCz9PzwdhtoEmx55MqPpk, the Lore Vault copy "
    "-- a second, non-Lore-Vault .docx copy also exists with identical "
    "content). Third document drafted under Phase 1b of the "
    "pre-Book-1-era roadmap. This document is the original, "
    "never-before-fully-drafted source for the three Kareth-sister "
    "artifacts (the Convergence, the Gradient, the Patient Stone) that "
    "Batch 46 could previously only name via cross-corroboration with "
    "the Complete Structural Outline, plus the source that corroborates "
    "Batch 49's Line-front roster fix (MCD-221) and Batch 46's Ren/"
    "Abyss sibling pairing (CC-114). One pre-existing flagged "
    "contradiction resolved in favor of this document's account, now a "
    "third independent corroborating source: ARS-220's internal Attia's "
    "Rite naming conflict with Ezio's Concealed Arsenal, resolved as a "
    "duplication error on Ezio's side (ARS-359)."
)

NEW_RULES = [
    {
        "id": "ARS-357",
        "category": "avatar-arsenal",
        "statement": (
            "Anomalous Mass: Lauris's Karesian biology decouples density "
            "from weight entirely -- she carries hyper-compressed "
            "cellular mass from Kares Prime's crushing gravity but "
            "registers no corresponding gravitational signature, "
            "striking with kinetic transfer standard instruments can't "
            "attribute to her visible weight. Not a malfunction or "
            "incomplete development; the two properties operate as "
            "independent systems by design."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-358",
        "category": "avatar-arsenal",
        "statement": (
            "Density Saturation: a biological state Lauris enters "
            "through sustained high-intensity engagement, not an "
            "activated ability. Unlike every other density-capable "
            "combatant in the series, who become more detectable as "
            "output climbs, Lauris becomes less detectable the deeper "
            "into saturation she goes -- partial saturation reads as "
            "sensor calibration error, full saturation reads as a "
            "gravitational signature's total absence. Saturation "
            "ceiling: 30 minutes pre-Convergence (Books 1-2), dropping "
            "to 18 minutes post-Convergence (no earlier than Book 3) as "
            "Val Saeryn's gauntlet accelerates accumulation."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-359",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-220: the Attia's Rite naming conflict (Lauris's "
            "breaker blade vs. an identically-named entry in Ezio's "
            "Concealed Arsenal) is resolved in favor of Lauris's "
            "ownership, now corroborated by three independent sources "
            "including this document. Attia's Rite was forged by Kanja "
            "to mark Ezio's promotion to Sergeant-at-Arms but is wielded "
            "by Lauris, not Ezio; the Ezio Concealed Arsenal entry is a "
            "duplication error and is superseded. Lauris's full arsenal: "
            "the Aristocrat (precision rapier, 'the scalpel'), the "
            "Spine of Dagon (6.2ft dragonbone greatsword with the "
            "spatial-folding Swallow sheath), Attia's Rite "
            "(forward-weighted breaker, 'processes crowds'), and the "
            "Phalanx."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-360",
        "category": "avatar-arsenal",
        "statement": (
            "The Phalanx: Lauris's three bio-integrated shields -- "
            "Night-Glass (shadow-wall, left vambrace), Solar-Spire "
            "(spinning deflector, right vambrace), Phoenix-Guard "
            "(hexagonal chest carapace) -- which fuse via Triad-Lock "
            "into a continuous Drakma wall capable of a battering-ram "
            "sprint through structural walls, energy barriers, and "
            "formations."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-361",
        "category": "avatar-arsenal",
        "statement": (
            "The Kareth-sister artifacts (named but undefined since "
            "Batch 46's cross-corroboration, now given full "
            "definitions): the Convergence is Val Saeryn Kareth's Kares "
            "Prime alloy gauntlet, recruiting environmental mass and "
            "amplifying Kinetic Concentration through "
            "gravitational-alignment architecture refined across her "
            "93,179 years -- this is what drops Lauris's saturation "
            "ceiling from 30 to 18 minutes. The Gradient is Val Mirel "
            "Kareth's Kares Prime alloy blade, concentrating cutting "
            "force along a target's internal density-differential seam "
            "before its wielder consciously locates it. The Patient "
            "Stone is Kares Prime core material with a density "
            "null-signature defeating all detection, including Density "
            "Sight and Predictive Oracles, carrying 60,000 years of "
            "encoded command lineage. All three are received by Lauris "
            "no earlier than Book 3."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-362",
        "category": "avatar-arsenal",
        "statement": (
            "Wrinkle 1, the Saturation Inversion (first full expression "
            "Book 3): at full Density Saturation, Lauris's gravitational "
            "signature doesn't suppress, it's simply absent -- Orlok's "
            "Density Sight (which reads every other density-capable "
            "combatant in the series) registers empty space where she "
            "stands. Orlok observes this directly during a Shogunate "
            "war engagement and logs it privately without telling her; "
            "she never learns the mechanism, only that the fight 'feels "
            "complete' at that point."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-363",
        "category": "avatar-arsenal",
        "statement": (
            "Wrinkle 2, the Patient Stone Synergy (identified Book 4): "
            "the Patient Stone's null-signature (ARS-361) compounds with "
            "full Saturation's absent gravitational signature, making "
            "Lauris the series' only genuinely undetectable S-tier "
            "combatant against any density/mass/gravitational-event "
            "detection system, including T.D.K.'s own subterranean "
            "architecture. Fermand identifies the exact-shaped gap in "
            "T.D.K.'s detection network during the Broken Meridian "
            "expedition; Ezio classifies it as an operational advantage "
            "to be kept from the SBD until Book 5."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-364",
        "category": "avatar-arsenal",
        "statement": (
            "Wrinkle 3, the Convergence in the Meridian's geology "
            "(unique peak, Book 5 only): the Convergence's "
            "environmental-mass recruitment produces a qualitatively "
            "different result in the Broken Meridian's substrate "
            "specifically -- 30,000 years of compression from T.D.K.'s "
            "own Warbody presence there, the densest geological material "
            "in the world. This peak cannot be replicated at any other "
            "location; Book 4's outer-approaches use of the Convergence "
            "during the same expedition (extends the already-locked "
            "Book 4 Broken Meridian/Book 5 Gate Battle usage of this "
            "location) is a deliberately weaker baseline reading, not "
            "the full expression."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-365",
        "category": "avatar-arsenal",
        "statement": (
            "Wrinkle 4, the Spine's corridor pressure wave (Book 5, "
            "Meridian interior): at full Saturation in open terrain, the "
            "Spine of Dagon's swing produces a contact-range knockdown "
            "wave; in the Meridian's enclosed stone corridors, the wave "
            "amplifies off the walls instead of dissipating, arriving "
            "ahead of the blade and destabilizing opponents before the "
            "strike lands, with reflected lateral pressure hitting "
            "anyone at the corridor walls."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-366",
        "category": "avatar-arsenal",
        "statement": (
            "Lauris hard constraints, for consistency in future "
            "drafting: her biology is inherited, not manufactured or "
            "lab-produced; she never sinks regardless of density "
            "output; the Convergence's Book 5 Meridian peak (ARS-364) "
            "is environment-specific and must not be written as "
            "available in Book 4 or any other Book 5 location; the "
            "Spine's amplified corridor pressure wave (ARS-365) "
            "requires full Saturation AND enclosed stone architecture "
            "simultaneously -- open terrain at full Saturation produces "
            "only the standard wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-367",
        "category": "avatar-arsenal",
        "statement": (
            "Extends MCD-251/CC-112: Anirak's Fury Variant biology is "
            "built for momentum accumulation without a conventional "
            "ceiling -- impact is fuel, not cost, and her muscles loosen "
            "rather than fatigue under sustained exertion. Her Twin "
            "Fangs (Living Drakma hook-swords) are heart-rate "
            "responsive, warming and increasing in molecular density as "
            "her Fury climbs. Her bioluminescent violet-eyed "
            "gaze-capture (already locked as always-on, CC-112) and her "
            "Siren's Voice neuroacoustic vertigo/nausea emission are "
            "independent baseline capabilities; her acoustic "
            "hydro-sensitivity lets her perceive the ocean (waves, "
            "weather, submersibles) ambiently, before any instrument."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-368",
        "category": "avatar-arsenal",
        "statement": (
            "The Fury Escalation States, extending MCD-251's "
            "momentum-accumulation mechanic: Warm (elevated heart rate, "
            "full fine control, all techniques available), Hot (high "
            "heart rate, reduced reaction time, first involuntary "
            "Voice/gaze synchronization begins -- see ARS-370), White "
            "(combat ceiling as established through Book 4, reduced "
            "fine control, near-forge Fang temperature, involuntary "
            "Voice/gaze synchronization now consistent), and Flood "
            "State (Book 5 Line front only -- see ARS-369 -- fine "
            "control absent entirely, doctrine replaced by pure kinetic "
            "momentum)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-369",
        "category": "avatar-arsenal",
        "statement": (
            "Wrinkle 1, Flood State (Book 5 Line front exclusively -- "
            "the series' longest sustained engagement, extending "
            "MCD-221's Line-front roster): no engagement before Book 5 "
            "lasts long enough to push Anirak past White. At Flood "
            "State the Chain-Strike doctrine's techniques persist only "
            "as biological instinct, no longer intentional choices. "
            "Ren's role shifts correspondingly from finisher to full "
            "aftermath-radius manager, neutralizing what she's "
            "disoriented and clearing targets so she doesn't have to "
            "stop. Red Beard (commanding the Line front per MCD-221) "
            "responds to her reaching Flood State by silently "
            "increasing his own operational distance by 30 meters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-370",
        "category": "avatar-arsenal",
        "statement": (
            "Wrinkle 2, Voice/gaze synchronization (first integration "
            "Book 3, full expression Book 5): distinct from the "
            "always-on baseline gaze-capture (CC-112), this is the "
            "timing coordination between the Voice pulse and direct eye "
            "contact becoming biologically automatic as Fury escalates "
            "-- involuntary at Hot, consistent at White, and a single "
            "inseparable compound effect at Flood State. First "
            "involuntary occurrence (Book 3) unsettles Anirak briefly, "
            "since her own biology acted without her authorization; by "
            "Book 5 she doesn't register it at all."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-371",
        "category": "avatar-arsenal",
        "statement": (
            "Wrinkle 3, active hydro-sensitivity sonar (ambient Books "
            "2-4, active Book 5): Anirak's baseline hydro-sensitivity "
            "(ARS-367) extends into ~300-meter active sonar when her "
            "heat-conducting Twin Fangs chains are running hot (Hot "
            "state or above), making her the Line front's earliest "
            "naval-perimeter warning system -- she reports positions to "
            "Ironbane (extends MCD-221's Ironbane's-fleet Line-front "
            "component) without narrating the mechanism."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-372",
        "category": "avatar-arsenal",
        "statement": (
            "Wrinkle 4, chain thermal transfer at Flood State: the Twin "
            "Fangs run at forge-adjacent temperature at Flood State; "
            "two chain wraps sustained three seconds on the same "
            "contact point structurally weakens (not burns through) the "
            "material there, creating a failure point Ren learns to "
            "target without either of them naming the mechanism "
            "explicitly."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-373",
        "category": "avatar-arsenal",
        "statement": (
            "Anirak hard constraints, for consistency in future "
            "drafting: no stillness, no sniping, no clean kills -- total "
            "engagement is doctrine, not an escalation of last resort. "
            "Flood State occurs only in the Book 5 Line front; any "
            "earlier engagement approaching that duration must be "
            "interrupted rather than allowed to break the ceiling "
            "early. The active sonar (ARS-371) requires Hot state or "
            "above -- the Book 2 seed is ambient only. Siren's Voice has "
            "no effect on undead combatants (extends the already-locked "
            "Crownless Host/undead legions), so living troops must be "
            "routed toward her engagement zone."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-374",
        "category": "avatar-arsenal",
        "statement": (
            "Combined operational note, Lauris and Anirak in shared "
            "engagement (extends MCD-221's Line-front roster): both "
            "become more dangerous the longer a fight runs, but in "
            "opposite detection directions -- Anirak louder and harder "
            "to escape, Lauris quieter and harder to find, which "
            "defeats any instrument trying to track both simultaneously. "
            "In a shared Book 5 engagement, Anirak's Siren's Voice "
            "compounds against opponents already destabilized by the "
            "Spine's pressure wave, and Lauris's Triad-Lock breaches "
            "become structural failure points Anirak's Debt Collection "
            "chain-pulls exploit in the following second."
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
            "batch": 53,
            "source_doc": "Lauris_Anirak_Threat_Blueprint.docx -- Phase 1b, third document: Lauris's Anomalous Mass/Density Saturation mechanics and the three Kareth-sister artifacts, Anirak's Fury Variant/Escalation States mechanics, both characters' four wrinkles each, hard constraints, and a combined operational note",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 1,
            "conflicts_resolved": 1,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "5.6"
    ledger["last_updated"] = "2026-09-04"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
