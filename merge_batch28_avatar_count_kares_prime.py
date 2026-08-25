#!/usr/bin/env python3
"""Batch 28: resolve the Avatar count (19, not 16/17) and the Kares Prime/
Kareth War-Matriarchy reconciliation for MCD-034. Also promotes WC-014 from
draft to locked with its Avatar count corrected.
"""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'World_Adaptation_Blueprint' (Google Drive fileId "
    "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA, Lore Vault), Section III "
    "(the Stress Profile Table) and the 'CANON RECONCILIATION -- KARES PRIME "
    "AND THE KARETH WAR-MATRIARCHY' preface. Resolves the inconsistency "
    "documented at CC-075 (16 vs 17 Avatars) and the missing world qualifier "
    "in MCD-034, both per Abad's rulings, 2026-08-25."
)

WC_014_REVISED = (
    "The Talisman of Mao is a shifting Living Drakma sphere functioning as a "
    "synchronization server for 19 Avatars (corrected from an earlier 17 "
    "figure; see MCD-140), with a Triple-Tiered Cascade: Sovereign Umbrella "
    "(crew-level) -> Grounded Bastion (planetary) -> Internal Quench (Kanja, "
    "currently 99.9% capacity). Stage 2 (Grounded Bastion) channels Kanja's "
    "radiance into the planet's crust as Architectural Reinforcement; Stage "
    "3's Governor's Shackle uses the Gravity-Fetter pendant as its physical "
    "interface, and severing it triggers the Pi-Awakening."
)

NEW_RULES = [
    {
        "id": "MCD-140",
        "category": "World Mechanics",
        "statement": (
            "The Talisman of Mao's Sovereign Umbrella protects nineteen "
            "Avatars, not sixteen or seventeen as various source documents "
            "state -- those figures are undercounts. The confirmed roster, "
            "per the World Adaptation Blueprint's own Stress Profile Table: "
            "Kanja Rexmar, Ozmund Verehimu, Valen, Sephtis, Bloodreaver "
            "(Torian), Ironbane (Darius), Anansi (Shadowforge), Stormbreaker "
            "(Kaelen), Blades Fury (Anirak), Dreadlord (Azar), Drown-Warden "
            "Varkul, Sorya, Varruk, Pyro (Ignis Rexmar), Voidbreaker (Jax), "
            "Stormreaver (Kairo), Soulreaver Zora, Ghostwind (Sylas), and "
            "Abyss (Ren). Onyx of Oblivion appears in the same table but is "
            "explicitly excluded from the count: it is a sentient weapon, "
            "not a person, and the table itself describes it as 'a node in "
            "the planetary lattice' rather than a stress source the "
            "Talisman protects against. This resolves the inconsistency "
            "documented at CC-075 and supersedes the '17 Avatars' figure "
            "formerly in draft WC-014."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-141",
        "category": "World Mechanics",
        "statement": (
            "MCD-034 ('Lauris Letitia is the last born pure-blood Karesian "
            "before the men died and the women ruled alone') is amended to "
            "specify a world: this happened on Kares Prime, Lauris's "
            "homeworld, classified High-Gravity Warborn, not on Cian. The "
            "Kareth War-Matriarchy on Cian (the institution behind Val "
            "Saeryn Kareth and Val Mirel Kareth) is a separate, distant "
            "descendant institution: the surviving line of a Karesian "
            "colonial expedition that left Kares Prime roughly 122,000 "
            "years ago during a period of catastrophic decline. The split "
            "is old enough that neither branch recognizes the other as the "
            "same people anymore -- the Kareth on Cian remember themselves "
            "as an independent War-Order; what remains on Kares Prime "
            "remembers itself as a dying root population. Lauris carries "
            "the source population's biology; the Kareth sisters carry the "
            "descended, diluted version. MCD-034's substance (last "
            "pure-blood, biological ceiling, the men-died/women-ruled "
            "history) is otherwise unchanged."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Abad resolved the Avatar count in two follow-up passes after the initial '
    '"17, Kanja included" ruling didn\'t match the Blueprint\'s 20-entry table: '
    'confirmed Onyx isn\'t an Avatar ("20 is a broader list than \'Avatars\'"), '
    'then confirmed the resulting 19 is the real count ("19 is the real '
    'count"), superseding the earlier 17 ruling. The Kares Prime reconciliation '
    'and the full draft were then approved together: "lock it"'
)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"

    ledger["rules"].extend(NEW_RULES)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}
    assert rules_by_id["WC-014"]["status"] == "draft"
    rules_by_id["WC-014"]["statement"] = WC_014_REVISED
    rules_by_id["WC-014"]["status"] = "locked"

    ledger["batches_completed"].append(
        {
            "batch": 28,
            "source_doc": "World_Adaptation_Blueprint (Avatar count + Kares Prime reconciliation only; full document not yet extracted)",
            "source_id": "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 1,
            "conflicts_resolved": 1,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "3.1"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")
    print(f"WC-014 status: {rules_by_id['WC-014']['status']}")


if __name__ == "__main__":
    main()
