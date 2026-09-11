#!/usr/bin/env python3
"""Batch 278: Industrial Myth Alias Chronicle waves 32, 33, and 34 (9 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "Continues the Alias Chronicle sub-series' thirty-second, thirty-third, and thirty-fourth "
    "waves for the Industrial Myth, under Abad's direct authorization: \"do 3 more alias wave for "
    "all eleven.\" Wave 32: the worst-off-first discipline (MCD-371) run for the first time against "
    "a claimant's own pride-driven self-understatement rather than an administrator's staging "
    "(\"The Man Who Wouldn't Claim His Own Debt,\" MCD-1442); Kanja begins training a field "
    "successor -- Maret Vos, already locked -- for his own testimony-gathering role, extending "
    "MCD-483's 'replicable rather than personal' theme to the interview side of the method for the "
    "first time (\"The Second Pair of Hands,\" MCD-1443); and the method's first formal public "
    "debate contesting the crew's right to operate at all, won through structured persuasion in "
    "front of a neutral audience rather than documentation, closing the wave (\"The Debate They "
    "Couldn't Silence,\" MCD-1444). Wave 33: a dishonest copycat runs a corrupted imitation of the "
    "method itself for profit, distinct from the earlier identity-impostor case (\"The Copy That "
    "Wasn't His,\" MCD-1445); the crew's internal-transparency discipline tested from Ezio's own "
    "side for the first time when he is personally offered a bribe (\"The Bribe Ezio Almost Kept,\" "
    "MCD-1446); and the method's first genuinely blameless fatality finding, with no negligence and "
    "no debt to record, only six names worth preserving, closing the wave (\"What No One Owed,\" "
    "MCD-1447). Wave 34: an administrator stages coerced testimony openly in Kanja's own presence, "
    "resolved through private follow-up re-interviews rather than confrontation (\"The Testimony "
    "Coerced in Plain Sight,\" MCD-1448); the method's first wage-tier discrimination case, "
    "eliminating a formal reduced-capacity pay scale for disabled workers once output proves it "
    "false (\"The Tier They Called Reduced,\" MCD-1449); and the method's first request to erase "
    "rather than soften a finding, from a reformed wrongdoer years after restitution, resolved with "
    "a new standing practice -- an unaltered original finding plus a truthful dated addendum -- "
    "closing the wave and this three-wave run (\"The Record He Asked Them to Erase,\" MCD-1450). No "
    "new named characters were introduced across any of the nine entries; Maret Vos (already "
    "locked) is reused for continuity. Strictly unarmed and non-combat throughout, per MCD-244's "
    "established ethos. Abad's approval: \"do 3 more alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1442",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Man Who Wouldn't Claim His Own Debt\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-man-who-wouldnt-claim-his-own-debt.md), Industrial "
            "Myth Alias Chronicle XCIV, wave 32, first entry. The worst-off-first discipline "
            "(MCD-371) and the 'numbers don't flinch either way' impartiality theme (MCD-1065) "
            "applied for the first time against a claimant's own pride-driven self-understatement: "
            "a veteran loom-fitter deliberately understates his own unpaid overtime by more than "
            "half so as not to seem needier than younger workers; Ezio's cross-referencing corrects "
            "the figure upward against the man's own stated wishes once the attendance records show "
            "more is truly owed. No new named characters; the loom-fitter is a new one-scene, "
            "unarmed, non-combat figure. Strictly unarmed and non-combat throughout."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1443",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Second Pair of Hands\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-second-pair-of-hands.md), Industrial Myth Alias "
            "Chronicle XCV, wave 32. Kanja begins training a field successor for his own "
            "testimony-gathering role, extending MCD-483's 'replicable rather than personal' theme "
            "to the interview side of the method for the first time, distinct from Ezio's "
            "already-established training of arithmetic auditors. Maret Vos (already locked, one of "
            "the three earliest crew members freed before the Black Trench) is chosen and proves "
            "capable, his own freed-Cestari background cited as the basis for his patience and "
            "aptitude. No new named characters. Strictly unarmed and non-combat throughout."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1444",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Debate They Couldn't Silence\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-debate-they-couldnt-silence.md), Industrial Myth "
            "Alias Chronicle XCVI, wave 32, closing the wave. The method's first formal public "
            "debate, staged by three regional administrators at a merchants' assembly hall to "
            "contest the crew's right to operate at all rather than any single figure's accuracy; "
            "Kanja wins through structured persuasion in front of a neutral guild audience rather "
            "than documentation or a tribunal ruling, distinct from the earlier hostile-cross-"
            "examination tribunal entry (MCD-745). No new named characters; the rhetorician and "
            "administrators are unnamed. Strictly unarmed and non-combat throughout. Closes the "
            "Industrial Myth's thirty-second wave (with \"The Man Who Wouldn't Claim His Own Debt,\" "
            "MCD-1442, and \"The Second Pair of Hands,\" MCD-1443)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1445",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Copy That Wasn't His\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-copy-that-wasnt-his.md), Industrial Myth Alias "
            "Chronicle XCVII, wave 33, first entry. The first entry featuring a dishonest copycat of "
            "the method's own process -- testimony, cross-referencing, a posted finding -- who "
            "skims a cut of every settlement rather than claiming to be Kanja, distinct from the "
            "earlier identity impostor (MCD-759). Resolved through public reconciliation of the "
            "corrected figures rather than confrontation. No new named characters; the copycat "
            "tally-taker is unnamed and one-scene. Strictly unarmed and non-combat throughout."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1446",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Bribe Ezio Almost Kept\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-bribe-ezio-almost-kept.md), Industrial Myth Alias "
            "Chronicle XCVIII, wave 33. Extends the crew's internal-transparency discipline "
            "(MCD-1152, Kanja's own refused personal bribe) to Ezio for the first time: a mill "
            "owner's steward offers Ezio a bribe to leave one page un-cross-referenced; Ezio "
            "genuinely hesitates before refusing and discloses the offer, and his own honest "
            "temptation, to Kanja before deciding rather than after. No new named characters; the "
            "steward is unnamed and one-scene. Strictly unarmed and non-combat throughout."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1447",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What No One Owed\" (full narrative text at docs/lords-of-cian/chronicles/"
            "what-no-one-owed.md), Industrial Myth Alias Chronicle XCIX, wave 33, closing the wave. "
            "The method's first genuinely blameless fatality finding: a mine-roof collapse kills six "
            "men with no negligence, no shortfall, and no responsible party found after a full "
            "audit, distinct from every prior fatality entry (MCD-1172, MCD-1398) in that there is "
            "no debt at all to record; the finding preserves the six names with no figure attached, "
            "extending the 'Recorded. Unrecoverable. True.' documentation category (MCD-926) into a "
            "case with zero monetary or liability content. No new named characters; the six deceased "
            "miners and their families are unnamed. Strictly unarmed and non-combat throughout. "
            "Closes the Industrial Myth's thirty-third wave (with \"The Copy That Wasn't His,\" "
            "MCD-1445, and \"The Bribe Ezio Almost Kept,\" MCD-1446)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1448",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Testimony Coerced in Plain Sight\" (full narrative text at docs/lords-of-cian/"
            "chronicles/the-testimony-coerced-in-plain-sight.md), Industrial Myth Alias Chronicle C, "
            "wave 34, first entry. An administrator stages uniform, coerced testimony openly in "
            "Kanja's own presence, betting the alias's unarmed non-confrontational method has no way "
            "to counter it in the moment; resolved through private follow-up re-interviews once the "
            "coercive audience is removed rather than direct confrontation in the yard, distinct "
            "from the earlier coerced-collaborator case (MCD-1157, a clerk coerced into falsifying "
            "records under threat, not live staged testimony). No new named characters; the "
            "administrator and workers are unnamed. Strictly unarmed and non-combat throughout."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1449",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Tier They Called Reduced\" (full narrative text at docs/lords-of-cian/chronicles/"
            "the-tier-they-called-reduced.md), Industrial Myth Alias Chronicle CI, wave 34. The "
            "method's first wage-tier discrimination case: a weaving-house's formal 'reduced tier' "
            "pays disabled workers a fixed lower wage regardless of actual output; six weeks of "
            "output records prove several outproduce able-bodied peers, and the finding eliminates "
            "the tier entirely rather than adjusting it, distinct from the earlier testimony-"
            "credibility entry for a blind quarry worker (MCD-1154). No new named characters; the "
            "owner and weavers are unnamed. Strictly unarmed and non-combat throughout."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1450",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Record He Asked Them to Erase\" (full narrative text at docs/lords-of-cian/"
            "chronicles/the-record-he-asked-them-to-erase.md), Industrial Myth Alias Chronicle CII, "
            "wave 34, closing the wave. The method's first request to erase, rather than soften or "
            "withhold, an honest finding: a dying, long-reformed administrator asks that his decade-"
            "old proven fraud be struck from the record so his grandchildren won't inherit the "
            "shame; Kanja refuses to alter or remove the original finding but establishes a new "
            "standing practice -- a truthful, dated addendum recording genuine subsequent "
            "restitution and reform may be appended beside it -- distinct from the earlier "
            "withdrawn-but-preserved complaint (MCD-1168) and the 'Recorded. Unrecoverable. True.' "
            "category (MCD-926), and extending the archive's permanence theme (MCD-1174). No new "
            "named characters; the administrator is unnamed. Strictly unarmed and non-combat "
            "throughout. Closes the Industrial Myth's thirty-fourth wave (with \"The Testimony "
            "Coerced in Plain Sight,\" MCD-1448, and \"The Tier They Called Reduced,\" MCD-1449) and "
            "this three-wave run (waves 32-34)."
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
            "batch": 278,
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
