#!/usr/bin/env python3
"""Batch 128: Lock Bane's third three-entry Alias Chronicle wave (MCD-431 through MCD-433),
starting the continuation of the Alias Chronicles / territory Chronicles track under Abad's
"#1 and #2 now and continue uninterrupted until completion" authorization."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    'Abad: "#1 and #2 now and continue uninterrupted until completion this includes test, commit, '
    'push to main origin" -- #1 (more Alias Chronicle waves) and #2 (more territory Chronicles) from '
    'the offered options menu. Starts a third Alias Chronicle wave, beginning with Bane.'
)

NEW_RULES = [
    {
        "id": "MCD-431",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Wounded He Chose to Carry\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-wounded-he-chose-to-carry.md), Bane Alias Chronicle "
            "VII, first entry in the third wave. After a Suppression Brigade detachment breaks and "
            "flees rather than fight, Bane spends two hours personally carrying six wounded enemy "
            "soldiers back within sight of their own lines rather than leaving them, deliberately "
            "undercutting his own fear-based reputation on the principle that 'the fear only works "
            "if it's true' -- a moral-complexity entry extending VB-060's presence-trait framing "
            "into an act of mercy. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-432",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Full Weight of the Trinity\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-full-weight-of-the-trinity.md), Bane Alias Chronicle "
            "VIII. A detailed single-combat Trinity showcase against the fortified Kessic Overwatch "
            "garrison: Mafesto's Kinetic Transfer System absorbing a six-impact volley into stored "
            "charge, Obsidian Malice's two-year dormant charge breaching the inner gate in one "
            "strike, and Onyx of Oblivion's Cadence Ruin/Veil Piercer breaking a trained formation "
            "into six isolated fighters, ending with the garrison's surrender and the Trinity's "
            "remaining charge deliberately left unspent. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-433",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Efa Gol Saw First\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-efa-gol-saw-first.md), Bane Alias Chronicle IX, "
            "closing the third wave. Efa Gol (already locked, CC-130), who has known Kanja since "
            "before any alias existed, is the one crew member who still checks on the man rather "
            "than the reputation, and he confirms to her that the Bane persona is a deliberate, "
            "costly performance rather than an involuntary transformation -- a quiet closer "
            "grounding VB-060's presence trait in its real personal cost. No new named characters "
            "beyond the already-locked Efa Gol. Closes Bane's third three-Chronicle wave (with "
            "'The Wounded He Chose to Carry,' MCD-431, and 'The Full Weight of the Trinity,' "
            "MCD-432)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 128,
            "date": str(date.today()),
            "source": SOURCE,
            "rule_count": len(NEW_RULES),
            "note": (
                "Locks Bane's third three-entry Alias Chronicle wave (MCD-431 through MCD-433), "
                "the first of a new continuous run covering both more Alias Chronicle waves and "
                "more territory Chronicles. " + BATCH_NOTE
            ),
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate IDs after merge"
    print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
          f"Batches: {len(ledger['batches_completed'])}.")


if __name__ == "__main__":
    main()
