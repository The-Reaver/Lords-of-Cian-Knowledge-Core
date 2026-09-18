#!/usr/bin/env python3
"""Batch 298: Lauris Letitia's second four-strand Chronicle wave
(MCD-1623 through MCD-1626, Chronicles VI-IX)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-18, no source document. Second "
    "four-strand wave of Lauris Letitia's own Chronicle series "
    "(docs/lords-of-cian/character-chronicle-gameplan.md)."
)

BATCH_NOTE = (
    "Second four-strand wave (Strand K/D/L/W) in Lauris Letitia's own Chronicle series, "
    "following the pacing convention established in Batch 293. MCD-1623 (Strand K, "
    "'What Continuing Unchanged Meant') dramatizes the already-locked MCD-172 confrontation "
    "with Selene at age 1,840 for the first time -- the fourteen-hour conversation, 'Then I "
    "am a record' / 'You are also a person,' and Lauris achieving karth-ven within "
    "twenty-four hours not through visible processing but by continuing unchanged. MCD-1624 "
    "(Strand D, 'What the Twins Could Not Explain') is a full-scene treatment of Operation 6, "
    "the Twin Anomaly (previously only summarized at MCD-1535) -- the quiet, unremarked first "
    "data point in the institutional-doubt trajectory Chronicle III's 'inherited' realization "
    "later completes. MCD-1625 (Strand L, 'The Count She Keeps Current') advances the K-Theta "
    "cave-system thread (MCD-190/193) without touching the reveal-to-Kanja detail MCD-193 "
    "reserves for a future book or resolving the discharge Book 5 reserves at MCD-216 -- a "
    "present-day maintenance visit confirming the concealment still holds. MCD-1626 (Strand W, "
    "'My Dear Ezio') extends her Attia-bond cover-maintenance function for Ezio (CC-111) into "
    "a genuinely quiet, non-combat register for the first time, and gives narrative texture to "
    "VB-024's own standing rule that Fermand's narration reserves warmth only for 'My dear "
    "Ezio.' No new named characters across any of the four entries. Abad's approval: \"lock "
    "them up.\""
)

NEW_RULES = [
    {
        "id": "MCD-1623",
        "category": "lauris-character-chronicle",
        "statement": (
            "Lauris Chronicle VI, \"What Continuing Unchanged Meant\" (full narrative text at "
            "docs/lords-of-cian/chronicles/lauris-chronicle-vi-what-continuing-unchanged-meant.md), "
            "the sixth entry in her own Chronicle series, the second entry of Strand K (Kares "
            "Prime / deep past). Dramatizes directly, for the first time, the fourteen-hour "
            "conversation with Selene at age 1,840 already locked at MCD-172 -- the full truth "
            "of the K-strand decline and the synthesis conception, the exchange 'Then I am a "
            "record' / 'You are also a person,' and Lauris achieving karth-ven within "
            "twenty-four hours not through visible processing but by simply continuing "
            "unchanged. No new named characters; Selene already locked."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1624",
        "category": "lauris-character-chronicle",
        "statement": (
            "Lauris Chronicle VII, \"What the Twins Could Not Explain\" (full narrative text at "
            "docs/lords-of-cian/chronicles/lauris-chronicle-vii-what-the-twins-could-not-explain.md), "
            "the seventh entry in her own Chronicle series, the second entry of Strand D "
            "(Sealbound Directorate years). Full-scene treatment of Operation 6, the Twin "
            "Anomaly (previously only summarized at MCD-1535): assassin twins Velek and Velka, "
            "whose paired kinetic-load-sharing capability Lauris judges biologically "
            "inconsistent with their claimed origin, an early data point in the "
            "institutional-doubt trajectory Chronicle III's 'inherited' realization later "
            "completes. No new named characters; Velek and Velka already locked."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1625",
        "category": "lauris-character-chronicle",
        "statement": (
            "Lauris Chronicle VIII, \"The Count She Keeps Current\" (full narrative text at "
            "docs/lords-of-cian/chronicles/lauris-chronicle-viii-the-count-she-keeps-current.md), "
            "the eighth entry in her own Chronicle series, the second entry of Strand L (the "
            "Ledger / present-day operational debts). Advances the K-Theta cave-system thread "
            "(MCD-190/193) without touching the reveal-to-Kanja detail MCD-193 reserves for a "
            "future book, and without resolving the discharge Book 5 reserves at MCD-216 ('the "
            "cave-system populations revived'): a present-day maintenance visit confirming the "
            "concealment still holds, decades into the standing debt. No new named characters; "
            "the 200 relocated subjects stay uncounted individually, matching MCD-190's own "
            "phrasing."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1626",
        "category": "lauris-character-chronicle",
        "statement": (
            "Lauris Chronicle IX, \"My Dear Ezio\" (full narrative text at "
            "docs/lords-of-cian/chronicles/lauris-chronicle-ix-my-dear-ezio.md), the ninth "
            "entry in her own Chronicle series, the second entry of Strand W (Witness / "
            "present-day, quiet register). A stakes-free evening with Ezio himself, extending "
            "the already-locked cover-maintenance function of her Attia bond (CC-111) into a "
            "genuinely quiet, non-combat register for the first time, and giving narrative "
            "texture to VB-024's own standing rule that Fermand's warmth is reserved only for "
            "'My dear Ezio.' No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 4, f"expected 4 new rules, got {len(NEW_RULES)}"
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 298,
            "date": str(date.today()),
            "source": SOURCE,
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
