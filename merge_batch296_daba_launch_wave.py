#!/usr/bin/env python3
"""Batch 296: Daba's own 50-Chronicle launch wave (MCD-1571 through MCD-1620),
the first entries in his own protagonist Chronicle series.

Already run against canon-ledger.json (ledger_version 29.9, 2286 rules,
296 batches). RULES_PATH pointed at a consolidated JSON file assembled from
ten parallel drafting agents' output (in the now-removed .batch296_scratch/
working directory); kept here as the batch's permanent record per the
project's merge-script convention, not intended to be re-run.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
RULES_PATH = ".batch296_scratch/consolidated_rules.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-18, no source document. Launch wave "
    "of Daba's own protagonist Chronicle series, produced by ten parallel "
    "background drafting agents (five entries each) and consolidated centrally."
)

BATCH_NOTE = (
    "Daba's own 50-entry Chronicle launch wave -- the first entries in his own "
    "protagonist series, following the territory-leader model (himself as POV, "
    "Kanja an unnamed/background or directly-named presence only where the "
    "already-locked mentorship, MCD-1568, actually calls for it). Abad picked "
    "this track from an options menu, then authorized the batched, multi-agent "
    "production directly: \"rate 50 Chronicles in batches using as many agents as "
    "needed to make it efficient.\" Ten parallel agents each drafted a five-entry "
    "block covering a distinct chronological/thematic stretch of Daba's life, "
    "assigned non-overlapping MCD-1571-1620 ID ranges and Chronicle numerals "
    "I-L up front to avoid coordination collisions: Block A (I-V, MCD-1571-1575) "
    "the immediate aftermath of the Rookery tragedy, pre-founding, no Kanja; "
    "Block B (VI-X, MCD-1576-1580) founding 1804 in earnest, choosing the name, "
    "the first operation, no Kanja; Block C (XI-XV, MCD-1581-1585) first contact "
    "and the early mentorship, Kanja named on-page for the first time per "
    "MCD-1568's own two-way framing; Block D (XVI-XX, MCD-1586-1590) the "
    "guerrilla-doctrine side of the mentorship deepened into the direct "
    "ancestor of Kanja's own Dredge-Line Ambush; Block E (XXI-XXV, MCD-1591-1595) "
    "the forging side deepened, closing on the explicit joint realization that "
    "'density is not power if the terrain neutralizes it' is one lesson taught "
    "from two directions; Block F (XXVI-XXX, MCD-1596-1600) building the mature "
    "dispersed network in Daba's own post-mentorship years, Kanja absent; Block G "
    "(XXXI-XXXV, MCD-1601-1605) MCD-1570's armament mechanic dramatized end to "
    "end, selection through generational distance from Daba himself; Block H "
    "(XXXVI-XL, MCD-1606-1610) genuine, unresolved costs and failures of staying "
    "deliberately small; Block I (XLI-XLV, MCD-1611-1615) the semi-dormant years "
    "running parallel to Kanja's Rebellion and Long Mask, Kanja never physically "
    "present, never inserted into any of his own already-locked battle rosters, "
    "per MCD-1569's 'never folded into... never publicly credited alongside it'; "
    "and Block J (XLVI-L, MCD-1616-1620) the closing quiet/personal register, "
    "deliberately leaving MCD-1569's Book 1 trigger open rather than resolving "
    "Daba's larger story. Every agent collision-checked its own new proper nouns "
    "against the live ledger before use and was barred from touching "
    "canon-ledger.json or git; two internal duplicate names surfaced only once "
    "all ten blocks were compared against each other and were fixed before this "
    "merge: Block I's minor character 'Perrin Kettel' was renamed 'Deryn Kettel' "
    "to avoid colliding with Block J's unrelated senior-coordinator character "
    "also named Perrin, and Block J's minor recruit 'Wrenna' was renamed "
    "'Tessin' to avoid colliding with Block F's 'Isolde Wrenna.' Zero collisions "
    "against the live ledger itself across all 50 entries' new proper nouns. "
    "Kanja's exact age is left unspecified throughout the mentorship-era blocks "
    "per the project's own established practice; all mentorship-era content is "
    "strictly platonic training material. No child-safety issues -- the Rookery "
    "tragedy's child deaths are referenced only with the same non-exploitative "
    "gravity already established elsewhere in the ledger (Nelle Adessi/Tomas "
    "Grieve, the Ash-Wharf Massacre), never depicted directly. Abad's approval: "
    "\"rate 50 Chronicles in batches using as many agents as needed to make it "
    "efficient.\""
)


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    with open(RULES_PATH, "r", encoding="utf-8") as f:
        new_rules = json.load(f)

    assert len(new_rules) == 50, f"expected 50 new rules, got {len(new_rules)}"
    new_ids = [r["id"] for r in new_rules]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within new_rules"
    expected_ids = [f"MCD-{n}" for n in range(1571, 1621)]
    assert new_ids == expected_ids, "IDs are not the expected sequential MCD-1571..1620 range"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(new_rules)

    ledger["batches_completed"].append(
        {
            "batch": 296,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(new_rules),
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
