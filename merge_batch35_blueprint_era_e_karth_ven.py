#!/usr/bin/env python3
"""Batch 35: World Adaptation Blueprint, Section VI Era E (Vask Karth-Ven and the long development)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'World_Adaptation_Blueprint' (Google Drive fileId "
    "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA, Lore Vault), Section VI "
    "('The Lauris Letitia Chronicle'), Era E ('Vask Karth-Ven and the Long "
    "Development'). The four combat disciplines developed here resolve "
    "cleanly onto Lauris's already-locked named weapons (MCD-033, "
    "ARS-220) rather than colliding with them -- weapon and discipline "
    "share a name."
)

NEW_RULES = [
    {
        "id": "MCD-167",
        "category": "World Mechanics",
        "statement": (
            "Vask Karth-Ven (MCD-160), Kares Prime's combat-development "
            "center, added three resident instructors to Lauris's "
            "original five-member Threnarr Sister-Hold, forming an "
            "eight-member Hold for her training: Veska Karth-Ven (senior "
            "combat instructor, keeper of the cooperative-era upper-tier "
            "archives), Tiramen Karth-Ven (adaptive-methodology "
            "specialist), and Voreth Karth-Ven (junior instructor, "
            "closest to Lauris in relative age, who became her primary "
            "sparring partner)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-168",
        "category": "World Mechanics",
        "statement": (
            "Lauris's first century at Karth-Ven (age 14-114) was a "
            "calibration period: her static density rose logarithmically "
            "without a projectable ceiling (4,200x at 20, 5,600x at 30, "
            "8,400x at 50, 11,500x at 100), forcing the Sister-Hold to "
            "abandon ceiling projection and train to whatever density she "
            "currently carried. This period also confirmed her defining "
            "trait -- she does not fatigue. Training sessions stopped "
            "being calibrated around her recovery (she needed none) and "
            "instead around the instructors', who rotated through eight "
            "to twelve substitutions across a single training day."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-169",
        "category": "World Mechanics",
        "statement": (
            "By Lauris's 200th year, no existing Karesian curriculum "
            "could contain her development, so Tiramen spent ~80 years "
            "building the Karth-Sera ('the discipline of the witnessed "
            "last') specifically for her, on three principles: Continuous "
            "Engagement (no scheduled recovery, since she needed none -- "
            "sessions ran on instructor rotation instead); "
            "Density-Progressive Combat (train her to weaponize her "
            "rising density rather than front-load peak strength -- the "
            "foundational logic of every fight she'd later conduct as an "
            "SBD bounty hunter: she wins by lasting longest, not hitting "
            "hardest first); and Lattice-Conscious Movement (training her "
            "to read her own Hexa-Lamellar Lattice configuration in real "
            "time, the biological basis of her precision). Lauris still "
            "carries fragments of the Karth-Sera in her personal archive "
            "aboard the Karkosa; Sephtis, who has read them, has never "
            "asked for the full curriculum and treats it as an external "
            "repository he catalogs but doesn't appropriate."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-170",
        "category": "World Mechanics",
        "statement": (
            "The Karth-Sera curriculum developed the four combat "
            "disciplines already locked as Lauris's named weapons "
            "(MCD-033, ARS-220) -- the weapon and the discipline built "
            "around wielding it share a name: Triad-Lock (age 200-600 "
            "under Veska, the kinetic-anchor stance behind the Phalanx's "
            "Triad-Lock configuration), Spine of Dagon (600-1,100 under "
            "Tiramen, the structural-breach strike keyed to her rising "
            "density), the Aristocrat (1,100-1,800 under Voreth, the "
            "hardest to develop -- a precision strike requiring real-time "
            "lattice-reading to find an opponent's structural failure "
            "point), and Attia's Rite (1,800-2,400, the crowd-control "
            "discipline exploiting her limitless stamina against multiple "
            "soft targets simultaneously)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-171",
        "category": "World Mechanics",
        "statement": (
            "Lauris's first lethal combat came at age 1,247: a mining "
            "collapse at Vask Threnarr trapped three women, and she held "
            "the unstable shaft in sustained Triad-Lock for three hours "
            "while extracting them, absorbing a calculated 2.4 million "
            "metric tons of cumulative pressure-equivalent. An orbital "
            "trade representative who witnessed the aftermath filed a "
            "report that seeded a persistent cross-network rumor about "
            "her -- the same rumor Sephtis encountered in his own "
            "archival research roughly 1,800 years before Lauris "
            "actually arrived on Cian."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-172",
        "category": "World Mechanics",
        "statement": (
            "At age 1,840, Lauris asked Selene directly why she was "
            "different; Selene answered over a fourteen-hour "
            "conversation, laying out the full truth of the K-strand "
            "decline and the synthesis conception. Lauris's response -- "
            "'Then I am a record' -- and Selene's -- 'You are also a "
            "person... we have been waiting to see' -- are both "
            "preserved in Selene's archive. Lauris achieved karth-ven (a "
            "state Karesians normally take decades or centuries to reach "
            "after receiving weighty context-defining information) "
            "within 24 hours, the youngest documented achievement in "
            "Sister-Hold history -- not through visible processing, but "
            "by simply continuing unchanged, which the Sister-Hold "
            "concluded was itself the achievement: her childhood "
            "inheritance of witness (MCD-161) meant she'd effectively "
            "been ready for the conversation since childhood."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-173",
        "category": "World Mechanics",
        "statement": (
            "At age 2,800, Lauris single-handedly defended Vask Olmedrin "
            "against a 400-strong non-Karesian raiding coalition that had "
            "already broken the outer defensive line and killed ~60 "
            "defenders. She engaged alone for 8 hours using Attia's Rite, "
            "reducing the raiding force from 280 to full retreat, and "
            "recorded the highest single-engagement density any Karesian "
            "has ever documented: ~25,000x. She declined formal "
            "acknowledgment from the Olmedrin Iron-Speakers. No further "
            "raids were attempted against the surviving Vasks for the "
            "remainder of her time on Kares Prime, and the orbital-trade "
            "rumor about her hardened into established report -- the "
            "version Sephtis encountered roughly 1,200 years before her "
            "arrival."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-174",
        "category": "World Mechanics",
        "statement": (
            "Lauris decided to leave Kares Prime gradually between ages "
            "3,400-3,580, having exhausted what the civilization's "
            "surviving infrastructure could still offer her and "
            "researched the outside world for ~180 years before settling "
            "on Cian for three specific reasons: it held the only "
            "Karesian-descended population in the archives (the Kareth "
            "War-Order), the only documented institution running "
            "inherited Ionic-Rite-style methodology (the Sealbound "
            "Directorate), and Living Drakma deposits approaching Kares "
            "Prime's own -- the same logic that drew the original Kareth "
            "diaspora there 122,000 years earlier (MCD-151). The "
            "Iron-Speakers deliberated for 380 years before agreeing to "
            "support her departure, asking only that she preserve a "
            "record of what she found. Selene was killed in a Vask "
            "Threnarr defensive action ~28 years before the scheduled "
            "departure, with Lauris fighting at her side and killing her "
            "attacker within 30 seconds of Selene's death -- too late. "
            "Lauris departed Kares Prime at approximately age 4,000, "
            "through the Olmedrin orbital trade-point, with roughly "
            "1,200 Karesian women present to see her off."
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
            "batch": 35,
            "source_doc": "World_Adaptation_Blueprint (Section VI, Era E: Vask Karth-Ven and the long development)",
            "source_id": "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "3.8"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
