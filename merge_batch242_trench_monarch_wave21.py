#!/usr/bin/env python3
"""Batch 242: Trench Monarch Alias Chronicle wave 21 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "A twenty-first Trench Monarch Alias Chronicle wave (three entries), all set within the "
    "already-established pre-Black-Trench window (Onyx of Oblivion solo, Mafesto dormant and "
    "Obsidian Malice undeployed per MCD-232), none contradicting the wave-15 closure at MCD-650. "
    "\"What He Owed Outside the Ledger\" (MCD-1062) holds Kanja accountable for collateral cost "
    "from the alias's own founding battle, the Dredge-Line Ambush flood (MCD-231), for the first "
    "time -- a loss the tally-verification method cannot repair, closing on honest record-keeping "
    "rather than restitution. \"The Boy He Trained Like He Meant It\" (MCD-1063) is the first entry "
    "showing Kanja train an existing crew member (the already-locked Nev Torr, Callum Breck's "
    "pair-partner, CC-118/CC-119) at full intensity with no Onyx powers invoked, detailed stance-"
    "and-technique choreography per the standing craft note; his established Black Trench fate is "
    "not referenced or altered. \"The Method the Trust Wanted to Own\" (MCD-1064) closes the wave "
    "with a new institutional register -- the Sovereign Trust seeking to formally adopt and scale "
    "the method rather than suppress, investigate, or imitate it -- left deliberately unresolved. "
    "No new named characters were introduced; Garren Hask, Callum Breck, and Nev Torr (all already "
    "locked) were reused. One new place name, the Kessic flats (a flood-zone location consistent "
    "with MCD-231's canal-flooding mechanics), collision-checked clean. Abad's approval: \"another "
    "alias wave of all aliases\"."
)

NEW_RULES = [
    {
        "id": "MCD-1062",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What He Owed Outside the Ledger\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-he-owed-outside-the-ledger.md), The Trench Monarch "
            "Alias Chronicle LXI, wave 21, first entry. Rebellion era, pre-Black-Trench. Months "
            "after the Dredge-Line Ambush (MCD-231) -- the flood that drowned a 200-soldier punitive "
            "column and founded the alias -- a woman whose family's sixty-year grafted orchard on "
            "the Kessic flats was salt-killed by the same flood comes to Warehouse Twelve, not "
            "disputing that the flood was necessary, but pointing out that unlike every wage theft "
            "the tally method has ever corrected, her loss was never entered on any ledger at all. "
            "The established restitution method finds no purchase -- there is no owner to charge and "
            "no coin figure that restores sixty years of root stock -- so Kanja offers his crew's "
            "labor toward reclamation across seasons while explicitly naming it insufficient, and "
            "writes the loss down himself on a page with no owner's name and no repayment schedule, "
            "signed with his own name rather than the alias. First entry in the sub-series to hold "
            "the founding battle itself accountable for collateral cost, and the first to close "
            "without the tally-verification method (MCD-231) providing a clean resolution. No new "
            "named characters -- the woman is unnamed; Garren Hask (already locked) appears in his "
            "established role."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1063",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Boy He Trained Like He Meant It\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-boy-he-trained-like-he-meant-it.md), The Trench "
            "Monarch Alias Chronicle LXII, wave 21. Rebellion era, pre-Black-Trench -- Mafesto "
            "dormant and Obsidian Malice undeployed until the Black Trench (MCD-232). Callum Breck "
            "brings sixteen-year-old Nev Torr (both already locked, CC-118/CC-119) to Kanja for "
            "combat training beyond what Breck's own footwork lessons can cover. A detailed "
            "hand-to-hand and bladed sparring sequence, built entirely from stance-correction, "
            "weight transfer, and technique rather than any of Onyx of Oblivion's named powers -- "
            "Cadence Ruin is explicitly stated to stay unused throughout, Kanja winning the "
            "full-intensity exchange on trained skill alone against an untrained but genuinely fast "
            "opponent. First entry in the sub-series showing Kanja personally train an existing "
            "crew member's combat capability at full intensity with no powers invoked, distinct from "
            "declining to recruit an uninvolved bystander (MCD-948). Nev Torr's already-established "
            "fate at the Black Trench (dying under Breck's watch, age 19) is not referenced, "
            "foreshadowed on the page, or altered -- the scene sits entirely within his established "
            "pre-Black-Trench timeline. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1064",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Method the Trust Wanted to Own\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-method-the-trust-wanted-to-own.md), The Trench "
            "Monarch Alias Chronicle LXIII, wave 21, closing the wave. Rebellion era, "
            "pre-Black-Trench. An unnamed Sovereign Trust registrar, acting on the Canal House "
            "inquest's (MCD-645) quiet institutional conclusions, proposes formally chartering and "
            "scaling the tally-verification method Trust-wide as standardized dispute-resolution "
            "practice -- a genuinely new register for the sub-series, the Trust seeking to adopt and "
            "co-opt the method rather than suppress (MCD-621), investigate (MCD-645/647), bribe "
            "around (MCD-943/949), or have it badly imitated (MCD-947). Kanja weighs the honest "
            "arithmetic of the method's reach (Garren Hask's own figures: sixteen trained students "
            "against four hundred districts) against the risk of losing the method's independence, "
            "and sets a hard condition -- verification stays answerable to the districts being "
            "counted for, never to Trust-appointed auditors, and figures stay open to any worker who "
            "wants to check them -- without knowing whether the charter that reaches him will honor "
            "it. Closes deliberately unresolved, echoing MCD-947's legend-outrunning-control tension "
            "at an institutional rather than grassroots scale. No new named characters -- the "
            "registrar is unnamed; Garren Hask (already locked) appears in his established role. "
            "Closes the Trench Monarch's twenty-first wave (with MCD-1062, MCD-1063)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 3, f"expected 3 new rules, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 242,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-11, no source document",
            "rule_count": len(NEW_RULES),
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs found post-write!"

    print(
        f"OK. Total rules: {len(ledger['rules'])}. "
        f"Ledger version: {ledger['ledger_version']}. "
        f"Batches: {len(ledger['batches_completed'])}."
    )


if __name__ == "__main__":
    main()
