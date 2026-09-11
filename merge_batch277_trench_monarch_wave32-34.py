#!/usr/bin/env python3
"""Batch 277: Trench Monarch Alias Chronicle waves 32-34 (9 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "Continues the Alias Chronicle sub-series' thirty-second, thirty-third, and thirty-fourth "
    "waves for the Trench Monarch, under Abad's direct authorization: \"do 3 more alias wave for "
    "all eleven.\" Wave 32 opens with the alias's first offensive infiltration rather than a "
    "reactive engagement -- a night raid freeing eleven people held under invented debts, detailed "
    "Onyx of Oblivion technique per the standing craft instruction (MCD-1433) -- then a voluntary "
    "peer joint-audit between the tally method and a rival accountant's books, resolved through "
    "mutual credit rather than adversarial exposure (MCD-1434), and closes on the method's first "
    "successful independent replication carried by a trained graduate to a distant town, "
    "deliberately contrasting the earlier failed imitation at MCD-947 (MCD-1435). Wave 33 gives "
    "Callum Breck his first dedicated personal-life register, set before his silence arc, alongside "
    "his established wife and infant daughter Sera (MCD-1436); a detailed combined fire-and-raid "
    "combat showcase, the alias's first fire-environment engagement (MCD-1437); and closes on a "
    "no-fault workplace death whose aftermath produces systemic cross-district safety reform rather "
    "than only grief, extending Dol Maren's engineering role (MCD-1438). Wave 34 opens with the "
    "alias's first genuine capture-and-escape register, establishing quicklime dust as a real "
    "sensory blind spot against Onyx's own combat-read (MCD-1439); a formal outside delegation asks "
    "Kanja to personally expand the method beyond his five districts, and he declines on principle, "
    "sending trained clerks instead and leaving the outcome deliberately open (MCD-1440); and "
    "closes the wave with Kanja directly teaching bladework to his three founding crew members -- "
    "Corren Halst, Danne Sok, and Maret Vos -- for the first time, distinct from his training of "
    "Nev Torr and an unrelated bullied bystander (MCD-1441). No new named characters across any of "
    "the nine entries; every returning figure reuses already-locked crew (Garren Hask, Callum "
    "Breck, Corren Halst, Danne Sok, Maret Vos -- he/him throughout, per the Batch 226 "
    "reconciliation -- Pell Ostra, Dol Maren). Zero proper-noun collisions found on check."
)

NEW_RULES = [
    {
        "id": "MCD-1433",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Debt They Held With Chains\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-debt-they-held-with-chains.md), Trench Monarch "
            "Alias Chronicle XCIV, wave 32, first entry. Rebellion era, pre-Black-Trench -- Onyx of "
            "Oblivion solo, Mafesto dormant and Obsidian Malice undeployed (MCD-232). The alias's "
            "first offensive infiltration rather than a defensive or reactive engagement: Kanja "
            "personally infiltrates a private debt-bondage lockup holding eleven people against "
            "invented debts, freeing them in a detailed combat showcase (Whisper of Shadows for "
            "infiltration, Veil Piercer used on a barred door rather than a person, Cadence Ruin "
            "reading the freed group's own panic risk) per the standing craft instruction. No new "
            "named characters -- the guards and the owner are unnamed. First entry in the Trench "
            "Monarch's thirty-second wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1434",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Audit They Both Signed\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-audit-they-both-signed.md), Trench Monarch Alias "
            "Chronicle XCV, wave 32. Rebellion era, pre-Black-Trench. A new peer-accountability "
            "register distinct from the already-locked fraud (MCD-1126), coercion-litigation "
            "(MCD-1130), and hostile Trust-audit (MCD-1145) threads: a rival accountant who calls "
            "the tally method sloppy rather than dishonest is answered with a voluntary joint audit "
            "of the same three sites, each method checked against the other's findings; the tally "
            "method catches wage theft the accountant's method wouldn't, his sharper arithmetic "
            "catches a shipping discrepancy the tally method missed, and both men credit the other "
            "honestly rather than claim sole vindication. No new named characters -- the accountant "
            "is unnamed. Second entry in the Trench Monarch's thirty-second wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1435",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ledger He Taught Somewhere Else\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ledger-he-taught-somewhere-else.md), Trench Monarch "
            "Alias Chronicle XCVI, wave 32, closing the wave. Rebellion era, pre-Black-Trench. The "
            "tally method's first successful independent replication: a trained graduate of "
            "Warehouse Twelve's classes (first named in MCD-1031) carries the verification "
            "discipline, deliberately stripped of the Trench Monarch name and reputation, to a "
            "distant granary town on her own initiative and with Kanja's blessing, succeeding where "
            "MCD-947's earlier distant imitation (which copied the method's form without its "
            "rigor) failed and ruined an innocent owner. No new named characters -- the graduate, "
            "her cousin's husband, and the granary owner are all unnamed. Closes the Trench "
            "Monarch's thirty-second wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1436",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Callum Breck Carried Home at Night\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-callum-breck-carried-home-at-night.md), Trench "
            "Monarch Alias Chronicle XCVII, wave 33, first entry. Rebellion era, pre-Black-Trench, "
            "before Breck's silence arc (CC-119). A dedicated Callum Breck personal-life register, "
            "distinct from his already-locked coining-the-name origin (MCD-368) and his later "
            "reflection entries: Kanja walks Breck's nightly route home and witnesses the plain, "
            "unremarkable domestic life -- his established wife (unnamed, CC-117) and infant "
            "daughter Sera (CC-117) -- that the war and the name he coined have nothing to do with. "
            "No new named characters -- Breck's wife is deliberately kept unnamed, matching CC-117. "
            "First entry in the Trench Monarch's thirty-third wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1437",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Night the Warehouse Burned Twice\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-night-the-warehouse-burned-twice.md), Trench "
            "Monarch Alias Chronicle XCVIII, wave 33. Rebellion era, pre-Black-Trench -- Onyx of "
            "Oblivion solo, Mafesto dormant and Obsidian Malice undeployed (MCD-232). A detailed, "
            "battle-intense combat showcase per the standing craft instruction: a decoy fire draws "
            "the crew away while raiders set a real, oil-fed fire at the ledger-room gate; Kanja "
            "fights four coordinated raiders half-blind through smoke (Whisper of Shadows for "
            "navigation, Cadence Ruin dismantling their trained formation, Veil Piercer opening the "
            "last man's guard as a ceiling beam gives way). The alias's first combined fire-and-raid "
            "combat register. No new named characters -- the raiders are unnamed. Second entry in "
            "the Trench Monarch's thirty-third wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1438",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What They Built After the Rope Broke\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-they-built-after-the-rope-broke.md), Trench "
            "Monarch Alias Chronicle XCIX, wave 33, closing the wave. Rebellion era, "
            "pre-Black-Trench. A no-fault accidental workplace death -- a hoist rope failing under "
            "ordinary load, killing a worker the tally method had no way to protect -- produces "
            "systemic cross-district safety reform rather than only grief: Dol Maren (CC-121, "
            "MCD-1123) audits load-rating standards across all five districts and finds four "
            "running closer to failure than necessary, leading to a single cross-checked standard "
            "adopted district-wide. Distinct from the elder's peaceful natural-causes death "
            "(MCD-902) and the torture-retaliation death that first cracked Kanja's composure "
            "(MCD-901). No new named characters -- the dead man and his widow are unnamed. Closes "
            "the Trench Monarch's thirty-third wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1439",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Night They Took Him Instead\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-night-they-took-him-instead.md), Trench Monarch "
            "Alias Chronicle C, wave 34, first entry. Rebellion era, pre-Black-Trench -- Onyx of "
            "Oblivion solo, Mafesto dormant and Obsidian Malice undeployed (MCD-232). The alias's "
            "first genuine capture-and-escape register: a thrown sack of quicklime dust defeats "
            "Onyx's own combat-read and Kanja is knocked out, bound, and blindfolded in a shuttered "
            "tannery by two captors debating ransom versus killing him outright; he escapes using "
            "Whisper of Shadows on the door hinge itself since his hands are bound, then defeats "
            "both captors before they realize the door failed from the inside. Establishes "
            "quicklime dust as a genuine, narrow sensory blind spot. No new named characters -- the "
            "captors are unnamed. First entry in the Trench Monarch's thirty-fourth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1440",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The District That Asked to Be Next\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-district-that-asked-to-be-next.md), Trench Monarch "
            "Alias Chronicle CI, wave 34. Rebellion era, pre-Black-Trench. A formal, voluntary "
            "expansion request tested constructively: three foremen from a distant river-trade "
            "district ask Kanja to personally bring the tally method to their own docks; he "
            "declines on principle (\"if it only works with me in the room, it was never actually "
            "built right\"), sending two trained clerks with the verification discipline but no "
            "name or reputation attached instead, leaving the outcome deliberately unresolved -- "
            "distinct from MCD-947's failed distant imitation and MCD-1435's single "
            "independently-motivated graduate. No new named characters -- the delegation's three "
            "foremen and the two departing clerks are unnamed. Second entry in the Trench Monarch's "
            "thirty-fourth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1441",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The First Time He Taught Them to Fight\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-first-time-he-taught-them-to-fight.md), Trench "
            "Monarch Alias Chronicle CII, wave 34, closing the wave. Rebellion era, "
            "pre-Black-Trench. Kanja directly and deliberately teaches ordinary bladework (no Onyx "
            "of Oblivion powers invoked) to his three earliest crew members -- Corren Halst, Danne "
            "Sok, and Maret Vos (he/him throughout, per the Batch 226 reconciliation) -- for the "
            "first time, prompted narratively by the capture in MCD-1439 though not framed as a "
            "direct response to it. Distinct from his training of the already-locked Nev Torr "
            "(MCD-1063) and of an unrelated bullied bystander (MCD-948), both strangers to the crew "
            "at the time. No new named characters. Closes the Trench Monarch's thirty-fourth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)
    assert len(NEW_RULES) == 9, f"expected 9 new rules, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"
    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"
    ledger["rules"].extend(NEW_RULES)
    ledger["batches_completed"].append(
        {
            "batch": 277,
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
