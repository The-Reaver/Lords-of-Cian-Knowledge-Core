#!/usr/bin/env python3
"""Batch 31: World Adaptation Blueprint, Section VI Era A (Kares Prime civilization)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'World_Adaptation_Blueprint' (Google Drive fileId "
    "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA, Lore Vault), Section VI "
    "('The Lauris Letitia Chronicle'), Era A ('The Karesian Civilization of "
    "Kares Prime'). The document's own claim that Val Saeryn Kareth 'was "
    "killed' during Kanja's youth directly contradicted the already-locked "
    "MCD-137 (both Kareth sisters alive, in deep cover); Abad ruled "
    "MCD-137 stands, so that claim is dropped entirely, not carried into "
    "any rule below. Era A's age/biology material about Val Saeryn is "
    "otherwise unaffected."
)

NEW_RULES = [
    {
        "id": "MCD-148",
        "category": "World Mechanics",
        "statement": (
            "Kares Prime is a high-gravity world (~4.7x Cian's surface "
            "gravity) orbiting in the inner ring of a binary star system, "
            "with dense, mineral-heavy atmosphere and constant tectonic "
            "activity -- mountains rise and fall across generations, not "
            "millennia. Karesians evolved under this instability and "
            "developed a proprioceptive habit of reading ground motion "
            "from infancy, since the surface can't be assumed stable. "
            "This same habit is what lets Lauris detect the Foundry "
            "Anvil's planetary hardening on Cian (MCD-142) long before "
            "anyone else notices -- she was trained by her homeworld to "
            "read exactly this kind of signal."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-149",
        "category": "World Mechanics",
        "statement": (
            "Karesian biology (Hexa-Lamellar Lattice, Gravimetabolic "
            "Architecture, Ironstorm Blood) gives a baseline lifespan of "
            "roughly 100,000 years with no meaningful aging -- cellular "
            "integrity holds indefinitely, and a Karesian in their "
            "twentieth millennium is biologically indistinguishable from "
            "one in their first except for accumulated experience. "
            "Karesians die from being killed (rare, generally requiring an "
            "opponent at or above peak S-tier), catastrophic geological "
            "events, or a small set of uncharacterized pathologies -- not "
            "from age. Adult biology runs four phases keyed to this "
            "lifespan: first adulthood (~6,000-24,000 years, peak "
            "trainable plasticity), second adulthood (~24,000-60,000, "
            "operational mastery -- this is where most Karesian combat "
            "masters and Iron-Speakers built their reputations), third "
            "adulthood (~60,000-90,000, accumulated synthesis), and "
            "fourth adulthood (~90,000-100,000+, treated as living "
            "archives). Val Saeryn Kareth (93,179 years) sits in late "
            "second adulthood; Val Mirel Kareth (89,003) in mature second "
            "adulthood -- both currently alive and in deep cover per "
            "MCD-137, not late in life by Karesian standards at all."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-150",
        "category": "World Mechanics",
        "statement": (
            "For ~31,000 years, Karesian society ran on a cooperative "
            "Pair-Hold structure: adult partnerships (formed at first "
            "adulthood, ~age 6,000) that functioned as operational units "
            "owning land and infrastructure, with children raised "
            "collectively across neighboring Holds. Governance was "
            "distributed across ~40 city-republics called Vasks, each run "
            "by a council of Iron-Speakers who resolved disputes through "
            "non-lethal procedural duels rather than debate. Karesian "
            "gestation runs ~14 Cian months; childhood runs ~6,000 years "
            "before first adulthood begins."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-151",
        "category": "World Mechanics",
        "statement": (
            "Approximately 122,000 years before the present, ~4,000 "
            "Karesians (mixed-gender, departing before any biological "
            "decline had begun) left Kares Prime in a colonial expedition "
            "and settled on Cian, becoming the ancestors of the Kareth "
            "War-Order (MCD-141). Over 122,000 years of lower-gravity "
            "adaptation, their descendants' static density dropped to "
            "roughly 60% of a homeworld Karesian's, with a lifespan "
            "ceiling extended to ~150,000 years. Val Saeryn and Val Mirel "
            "Kareth descend directly from this expedition, carrying "
            "uncorrupted pre-decline biology -- which is specifically why "
            "the Density Spike works in Kanja and Ozmund: their maternal "
            "inheritance traces to a genome that never encountered the "
            "decline that ended active civilization on the homeworld."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-152",
        "category": "World Mechanics",
        "statement": (
            "T.D.K. catalogued Kares Prime during his pre-Era-12 "
            "reconnaissance and assessed it as a low priority: the gravity "
            "well made direct Ionic Rite operations prohibitively "
            "expensive, the Karesians' cooperative structure had no "
            "exploitable central leverage point, and he calculated he'd "
            "eventually gain access to the biology anyway, through "
            "diaspora or the homeworld's own eventual decline. He was "
            "right -- the Cian diaspora delivered it to him, and he has "
            "spent tens of thousands of years processing the Kareth "
            "War-Order on Cian as a result (killing and containing them "
            "down to a small fraction of their original strength), never "
            "needing to touch Kares Prime directly. He has not yet "
            "recognized what Lauris is; that recognition is held in "
            "reserve for later in the series, not Book 1 or 2."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad resolved the Val Saeryn conflict ("MCD-137 stands, she\'s alive"), then approved the full draft as pasted in-conversation: "lock it"'


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
            "batch": 31,
            "source_doc": "World_Adaptation_Blueprint (Section VI, Era A: Kares Prime civilization)",
            "source_id": "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 1,
            "conflicts_resolved": 1,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "3.4"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
