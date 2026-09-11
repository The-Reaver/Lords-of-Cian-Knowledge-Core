#!/usr/bin/env python3
"""Batch 243: Industrial Myth Alias Chronicle wave 21 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Industrial Myth Alias Chronicle wave 21 (LXI-LXIII), continuing the alias's strictly unarmed, "
    "non-combat run. Three genuinely new registers never shown across the prior twenty waves: the "
    "method's first finding that runs against a worker rather than an employer, proving its "
    "impartiality cuts both ways (MCD-1065); its first application outside an industrial setting "
    "entirely, an orchard harvest forcing the established four-day documentation pacing to compress "
    "against a hard natural deadline rather than an administrator's stalling (MCD-1066); and its "
    "first internal solidarity dispute with no administrator or villain at all, where the ledger "
    "supplies shared facts for a settlement's own recipients to divide themselves rather than a "
    "verdict handed down (MCD-1067). No new named characters introduced; every claimant, "
    "administrator, and worker across all three entries is unnamed and one-scene, and Ezio Valcari "
    "(already locked) reused for continuity. Collision-checked before drafting: no existing rule or "
    "Chronicle uses an orchard/harvest-estate setting or an internal worker-vs-worker distribution "
    "dispute; zero new proper nouns invented. Abad's approval: \"another alias wave of all aliases\"."
)

NEW_RULES = [
    {
        "id": "MCD-1065",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Numbers Owed Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-numbers-owed-him.md), The Industrial Myth Alias "
            "Chronicle LXI, wave 21. A worker certain he's owed three years' back wages instead has "
            "the fully cross-referenced ledger find, once eighteen months of quiet off-the-books fever "
            "advances from the administrator are run against his true hours, that he owes a small "
            "balance back the other way. The first entry where a finding runs against a worker rather "
            "than an employer, and the crew records it with the same unflinching rigor as any case "
            "against a hostile administrator -- the administrator's other conduct elsewhere in the "
            "district stays exactly as damning as it was, but this one column runs the other direction "
            "and the ledger, per MCD-747's never-adjust-the-numbers discipline, doesn't flinch either "
            "way. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1066",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Harvest That Wouldn't Wait\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-harvest-that-wouldnt-wait.md), The Industrial Myth "
            "Alias Chronicle LXII, wave 21. The method's first application outside an industrial "
            "setting: a stone-fruit orchard estate three days from its crop turning forces the crew to "
            "compress its established four-day patient-documentation pacing into a single rapid field "
            "pass, testimony taken between picking rows and cross-checked against the estate's own "
            "harvest-quota boards rather than separately gathered corroboration. Ezio calls the pass "
            "less rigorous than any tally the crew has put its name to, and it holds anyway because "
            "the underpayment is a flat, visible quota shortfall with no time for anyone to doctor the "
            "books before the crop comes in -- the settlement paid out of that season's own sale. "
            "Establishes the method bending its own pacing against a hard natural deadline rather than "
            "an administrator's artificial stalling, honestly acknowledged as a deliberate shortcut, "
            "not a permanent lowering of the standard. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1067",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Settlement They Couldn't Agree How to Split\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-settlement-they-couldnt-agree-how-to-split.md), The "
            "Industrial Myth Alias Chronicle LXIII, wave 21, closing the wave. A won settlement for a "
            "forty-one-person hauling gang splits the gang itself along a tenure line once the payout "
            "is in hand -- senior haulers wanting tenure-weighted division, newer hands wanting a flat "
            "split -- with no administrator or villain on the other side of the dispute at all. Ezio "
            "can produce a defensible formula outright; Kanja refuses to let him, laying the full "
            "cross-referenced hours out as a shared table instead and declining to steer the two days "
            "of argument that follow, letting the forty-one workers reach their own compromise from "
            "the same facts. The method's first internal solidarity dispute, establishing that the "
            "ledger supplies shared facts for a group to divide among itself rather than a ruling "
            "handed down, even when a ruling would be faster. No new named characters. Closes the "
            "Industrial Myth's twenty-first wave (with \"What the Numbers Owed Him,\" MCD-1065, and "
            "\"The Harvest That Wouldn't Wait,\" MCD-1066)."
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
            "batch": 243,
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
