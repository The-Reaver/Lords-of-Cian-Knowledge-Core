#!/usr/bin/env python3
"""Batch 267: Industrial Myth Alias Chronicle wave 31 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."
BATCH_NOTE = (
    "The Industrial Myth's thirty-first Alias Chronicle wave, drafted under Abad's blanket "
    "authorization to continue a 31st wave for all eleven aliases. Three genuinely new registers, "
    "kept strictly unarmed throughout: the method's first case turned inward on a workers' own "
    "mutual-aid fund rather than any employer, extending the never-flinch impartiality discipline "
    "onto the crew's own community (\"The Fund They Kept for Themselves,\" MCD-1397); the method's "
    "first workplace-fatality liability case, extending MCD-1172's injury framework into a death no "
    "settlement can fully redress (\"The Debt a Death Left Open,\" MCD-1398); and the method's first "
    "fully solo case run start-to-finish by a trained district auditor with Kanja and Ezio absent "
    "throughout, the fullest test yet of MCD-483's 'replicable rather than personal' theme, closing "
    "the wave (\"The Case They Never Touched,\" MCD-1399). No new named characters were introduced -- "
    "all three entries use unnamed figures, consistent with the alias's established convention. "
    "Abad's approval: \"let's do a 31st alias wave for all eleven.\""
)

NEW_RULES = [
    {
        "id": "MCD-1397",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fund They Kept for Themselves\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fund-they-kept-for-themselves.md), Industrial Myth "
            "Alias Chronicle XCI, wave 31. The method's first case turned inward on a workers' own "
            "burial-and-sickness fund rather than any employer or administrator: an elected treasurer "
            "padded his family's sickness claims by small, cumulative degrees over three years, and "
            "Kanja refuses to let the finding be softened or kept private just because the fund was "
            "built by the workers themselves, extending MCD-1065's 'the numbers don't flinch either "
            "way' discipline onto the crew's own community. No new named characters; the treasurer "
            "and fund members are unnamed. Strictly unarmed and non-combat throughout."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1398",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Debt a Death Left Open\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-debt-a-death-left-open.md), Industrial Myth Alias "
            "Chronicle XCII, wave 31. The method's first workplace-fatality liability case, directly "
            "extending MCD-1172's forge-door injury precedent into a death no settlement can fully "
            "redress: a foundry worker dies when a twice-flagged, unreplaced safety chain fails; the "
            "finding explicitly separates the paid settlement from the acknowledged, unpayable "
            "remainder of the debt, and the widow's request to have her husband's name posted "
            "publicly is honored as a new standing practice. No new named characters; the widow, the "
            "owner, and the deceased worker are unnamed. Strictly unarmed and non-combat throughout."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1399",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Case They Never Touched\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-case-they-never-touched.md), Industrial Myth Alias "
            "Chronicle XCIII, wave 31, closing the wave. The method's first case run entirely solo by "
            "a trained district auditor with neither Kanja nor Ezio present at any stage -- the "
            "report reaches them four weeks after the case has already closed, cross-referenced and "
            "posted to the same standard as their own work -- directly testing MCD-483's 'replicable "
            "rather than personal' theme at its fullest extent, distinct from MCD-483 in that this "
            "auditor was formally trained by the crew rather than working from an incomplete "
            "secondhand account. No new named characters; the district auditor is unnamed, consistent "
            "with the collectively-unnamed trained-auditor convention established at MCD-1174. "
            "Strictly unarmed and non-combat throughout. Closes the Industrial Myth's thirty-first "
            "wave (with \"The Fund They Kept for Themselves,\" MCD-1397, and \"The Debt a Death Left "
            "Open,\" MCD-1398)."
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
            "batch": 267,
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
