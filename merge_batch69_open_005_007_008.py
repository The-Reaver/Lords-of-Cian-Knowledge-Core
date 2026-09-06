#!/usr/bin/env python3
"""Batch 69: closes roadmap Step 1 -- the 3 genuinely-open decisions.

OPEN-005: formally closed, "Session Lock 2" confirmed never existed
as a standalone document.

OPEN-007: locks MCD-338, the structural decision that the Ever Haunt
and Painter chapters are standalone interstitials, not folded into
existing POV chapters. Content itself remains undrafted.

OPEN-008: locks POL-097/098/099, heads for House Marlunar, House
Marvault, and House Marossen (the Astral Archipelago's three founding
families per POL-095, descending from Haku's bride's own line per
POL-096) -- Fleetmaster Ythan Marlunar, Warden of the Vault Cassia
Marvault, Shield-Marshal Doric Marossen, each holding one of the
Council of Crossroads' nine seats hereditarily."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Roadmap Step 1 closeout (OPEN-005/007/008), chat-drafted 2026-09-06, "
    "original invention, no external source document."
)

NEW_RULES = [
    {
        "id": "MCD-338",
        "category": "World Mechanics",
        "statement": (
            "Two interstitial world-phenomena chapters are structurally "
            "confirmed as standalone -- not folded into any POV "
            "character's ongoing chapters: an Ever Haunt chapter "
            "(elaborating the pursuit-phenomenon classification already "
            "locked at WC-019, CULT-197/198) and a Painter chapter "
            "(elaborating the ancient wandering predator already locked "
            "at CHAR-001). Both are atmospheric/phenomena-focused "
            "interludes rather than tied to a single POV character's "
            "arc, slotted between books rather than embedded within "
            "existing chapters. Exact book placement and full chapter "
            "content remain undrafted, reserved for a future dedicated "
            "pass."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "POL-097",
        "category": "Politics",
        "statement": (
            "House Marlunar holds one of the Astral Archipelago's nine "
            "Council of Crossroads seats hereditarily, the other eight "
            "split between two more hereditary seats (Marvault, "
            "Marossen) and six rotating/elected seats from the outer "
            "islands. Marlunar governs the Archipelago's navy and "
            "navigation traditions. Its head, Fleetmaster Ythan "
            "Marlunar, commands the fleet and holds the Council's "
            "maritime-affairs seat."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "POL-098",
        "category": "Politics",
        "statement": (
            "House Marvault holds a second hereditary Council of "
            "Crossroads seat, governing the Astral Archipelago's "
            "treasury, trade tariffs, and the ongoing logistics of "
            "repaying the standing Rexmar debt (POL-050, WC-012) "
            "accrued from Haku's Living Drakma liberation 5,000 years "
            "ago. Its head, Warden of the Vault Cassia Marvault, holds "
            "the Council's commerce seat."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "POL-099",
        "category": "Politics",
        "statement": (
            "House Marossen holds the third hereditary Council of "
            "Crossroads seat, governing the Astral Archipelago's marine "
            "infantry and coastal defense. Its head, Shield-Marshal "
            "Doric Marossen, holds the Council's defense seat."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

OPEN_UPDATES = {
    "OPEN-005": {
        "status": "resolved",
        "note": (
            "RESOLVED 2026-09-06: confirmed never existed as a standalone "
            "document. Reconfirmed dead-end three separate times (the "
            "original search, Batch 39, Batch 40), with Master Canon "
            "Decisions itself repeatedly deferring to this same missing "
            "file without it ever surfacing. Formally closed, not "
            "pursued further."
        ),
    },
    "OPEN-007": {
        "status": "resolved",
        "note": (
            "RESOLVED 2026-09-06, see MCD-338: the Ever Haunt and Painter "
            "chapters are standalone interstitials between books, not "
            "folded into existing POV chapters. Structural decision only "
            "-- full chapter content remains undrafted."
        ),
    },
    "OPEN-008": {
        "status": "resolved",
        "note": (
            "RESOLVED 2026-09-06, see POL-097/098/099: House Marlunar "
            "(Fleetmaster Ythan Marlunar), House Marvault (Warden of the "
            "Vault Cassia Marvault), and House Marossen (Shield-Marshal "
            "Doric Marossen) each have heads locked, one per hereditary "
            "Council of Crossroads seat."
        ),
    },
}

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

    updated = []
    for o in ledger["open_decisions"]:
        if o["id"] in OPEN_UPDATES:
            o["status"] = OPEN_UPDATES[o["id"]]["status"]
            o["note"] = OPEN_UPDATES[o["id"]]["note"]
            updated.append(o["id"])
    assert set(updated) == set(OPEN_UPDATES.keys()), f"expected to update {set(OPEN_UPDATES.keys())}, found {updated}"

    ledger["batches_completed"].append(
        {
            "batch": 69,
            "source_doc": (
                "Roadmap Step 1 closeout: resolves OPEN-005 (Session "
                "Lock 2, confirmed nonexistent), OPEN-007 (Ever Haunt/"
                "Painter interstitial chapter structure, MCD-338), and "
                "OPEN-008 (House Marlunar/Marvault/Marossen heads, "
                "POL-097 through 099)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "7.2"
    ledger["last_updated"] = "2026-09-06"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")
    print(f"Open decisions resolved: {updated}")


if __name__ == "__main__":
    main()
