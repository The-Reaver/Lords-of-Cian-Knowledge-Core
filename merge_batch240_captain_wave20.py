#!/usr/bin/env python3
"""Batch 240: Captain Alias Chronicle wave 20 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Captain's twentieth Alias Chronicle wave. \"The Charter They Finally Wrote\" (MCD-1056) pays off "
    "wave 19's deliberately open close (\"The War the Name Outlived,\" MCD-1004): eight months after "
    "the surrender the dispute council reconvenes and writes a genuine but partial charter -- three "
    "settled principles (free membership, the council's war-independent authority, Kanja as one voting "
    "seat among equals) plus a fourth clause on founding-generation mortality left deliberately blank "
    "rather than forced, extending the wave-6 dispute council (MCD-592) and Maret Vos free-departure "
    "precedent (MCD-593). \"What Sera Chose Instead\" (MCD-1057) extends Callum Breck's daughter Sera "
    "(already locked, CC-117) beyond her infancy-era mentions with the sub-series' first entry showing "
    "a founding-crew child deliberately choosing not to join the crew, applying the charter's "
    "free-membership principle in reverse; introduces one new minor, non-recurring mentor figure "
    "(Healer Orenn), collision-checked clean. \"The First Job That Wasn't the War\" (MCD-1058) closes "
    "the wave with a detailed full-Trinity combat showcase, deliberately peacetime and voluntary -- no "
    "chain of command, no campaign, no payment -- demonstrating the charter's unwritten fourth "
    "principle in lived action; new location is a deliberately unnamed fishing settlement, no proper "
    "noun introduced. No new named characters were introduced anywhere in this wave beyond Healer "
    "Orenn; all three entries reuse already-locked crew (Garren Hask, Corren Halst, Efa Gol, Callum "
    "Breck, Pell Ostra). Abad's approval: \"doorway for all the aliases that remain\" (approval of "
    "Bane's individually-presented wave 20 plus blanket authorization to continue the same wave for "
    "the remaining ten aliases)."
)

NEW_RULES = [
    {
        "id": "MCD-1056",
        "category": "alias-chronicle",
        "statement": (
            "\"The Charter They Finally Wrote\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-charter-they-finally-wrote.md), Captain Alias Chronicle "
            "LVIII, wave 20. Direct payoff to wave 19's deliberately open close (\"The War the Name "
            "Outlived,\" MCD-1004): eight months after the Trinity's surrender, Garren Hask reconvenes "
            "the dispute council as promised and it produces the crew's first written charter -- three "
            "settled principles (membership is chosen and free to leave at any time without owing "
            "explanation, extending the already-locked Maret Vos precedent, MCD-593; the dispute "
            "council's authority stands independent of any war, MCD-592; Kanja sits as one voting seat "
            "among equals, no greater formal weight than any other member) plus a fourth clause, on what "
            "happens when the founding generation who remembers why the crew started is gone, "
            "deliberately left blank rather than forced -- a direct, unresolved forward link to the "
            "mortality-succession thread (\"The Promise for After He's Gone,\" MCD-920). No new named "
            "characters -- Garren Hask, Corren Halst, Efa Gol, and Callum Breck all reused. First entry, "
            "wave 20."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1057",
        "category": "alias-chronicle",
        "statement": (
            "\"What Sera Chose Instead\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-sera-chose-instead.md), Captain Alias Chronicle LIX, "
            "wave 20. The sub-series' first entry to dramatize a founding-crew child deliberately "
            "choosing not to join the crew: the summer she turns sixteen, Callum Breck's daughter Sera "
            "(already locked, CC-117, previously mentioned only in infancy) tells Kanja directly that "
            "she is committing to healer's training instead, extending the already-locked charter's "
            "(MCD-1056) free-membership principle to someone who was never a member to begin with -- the "
            "found-family ethos protecting the choice to stay connected without ever serving aboard, a "
            "deliberate inverse of the sub-series' prior inheritance-by-joining entries (Danne Sok's "
            "daughter enlisting, MCD-1002; Garren Hask's grandnephew and great-grandniece). Introduces "
            "one new minor, non-recurring character, Healer Orenn (Sera's mentor), collision-checked "
            "clean against the full live ledger. No crew-roster change. Second entry, wave 20."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1058",
        "category": "alias-chronicle",
        "statement": (
            "\"The First Job That Wasn't the War\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-first-job-that-wasnt-the-war.md), Captain Alias Chronicle "
            "LX, wave 20, closing the wave. A detailed full-Trinity combat showcase, deliberately "
            "peacetime and voluntary: two weeks after the charter (MCD-1056) is written, the crew "
            "answers an unpaid, unordered call for help from a fishing settlement under raid by "
            "post-surrender opportunists, distinct from every prior war-era coordinated engagement in "
            "having no chain of command, no campaign, and no payment behind it. Efa Gol's seaward cutoff, "
            "Pell Ostra's non-explosive capstan-line boarding net, and Callum Breck's silent-signal shore "
            "watch (all already-locked crew, reused) precede Kanja anchoring the pier itself: Mafesto's "
            "Kinetic Transfer System redirects a ramming cutter's shock sideways along the pilings rather "
            "than through sheltering civilians, Obsidian Malice discharges once low and controlled to "
            "scatter a boarding line without damaging the hull the settlement will need back, and Onyx "
            "reads wet-plank footing to land every strike to disarm rather than kill -- eleven raiders "
            "taken alive in eleven minutes. Corren Halst names the connection explicitly: the settlement "
            "receiving help with nothing written or owed in return is the charter's deliberately blank "
            "fourth line, lived rather than worded. New location is a deliberately unnamed fishing "
            "settlement, no proper noun introduced. No new named characters -- Corren Halst, Garren "
            "Hask, Efa Gol, Pell Ostra, and Callum Breck all reused. Closes Captain's twentieth wave."
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
            "batch": 240,
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
