#!/usr/bin/env python3
"""Batch 80: Kwan Chronicle I ("The Weight of Being Asked"), the first
entry in Kwan's own Chronicle series -- protagonist Kasa (PH2-038), Kanja
as unnamed guest, matching the established territory-Chronicle convention
(MCD-334/335/336/339/340/341/342). Continues Chicago's own run of
territory Chronicles."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Kwan Chronicle I ('The Weight of Being Asked'), chat-drafted 2026-09-09, "
    "original invention, no external source document. Full narrative text "
    "at docs/lords-of-cian/chronicles/kwan-chronicle-i-the-weight-of-being-asked.md."
)

NEW_RULES = [
    {
        "id": "MCD-343",
        "category": "World Mechanics",
        "statement": (
            "Kwan Chronicle I ('The Weight of Being Asked') is the first "
            "entry in Kwan's own Chronicle series, per the established "
            "structure (MCD-334/335/336/339/340/341/342): each Phase 2 "
            "homage-era territory has its own Chronicles, with its own "
            "leader as protagonist and Kanja appearing only as an unnamed "
            "guest. After eleven weeks of stalled open-housing organizing, "
            "Kasa (PH2-038) personally asks an unnamed, long-entrenched "
            "ward broker not to march but to speak one public sentence "
            "endorsing the cause in his own voice. Kasa's signature "
            "ability ('The Invitation,' PH2-038) is shown directly in "
            "operation for the first time via this fresh recipient, "
            "deliberately distinct from the ability's own already-locked "
            "backstory event (the coalition's invitation of a real-world- "
            "shaped outside leader, who per PH2-038 stays backstory-only "
            "and is never separately named or dramatized on-page, matching "
            "the Toussaint-Louverture/Ogoun-Xarey precedent): the broker's "
            "single sentence converts eleven previously unreachable "
            "homeowners into marchers overnight. The ability's stated cost "
            "is honored explicitly and not softened -- the broker's words "
            "do not stop a single rock when the resulting march is "
            "attacked three blocks in, and the eventual agreement is left "
            "as a victory of uncertain real weight, consistent with "
            "PH2-038's own framing. An unnamed Kanja is present at the "
            "march and shields a struck marcher without taking command, "
            "credit, or narrative authorship. No new named characters "
            "introduced. Slots into no existing mainline battle -- "
            "original homage-era material set in Kwan itself, continuing "
            "Chicago's own run of territory Chronicles (Umoja and Ide "
            "already have one; Jibaro and Uhuru still do not)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "lock it"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 80,
            "source_doc": (
                "Kwan Chronicle I ('The Weight of Being Asked', MCD-343) -- "
                "the ninth territory Chronicle overall and Kwan's first "
                "(Kasa), continuing Chicago's own run of territory "
                "Chronicles and the open-ended Phase 2 territory-Chronicle "
                "expansion (alongside Xaragua I/II, Umoja I, Yara I, "
                "Areito I, Guanin I, Boriken I, Ide I) that was never gated "
                "by the Pre-Book-1 Foundation Complete milestone (Batch "
                "75)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "8.3"
    ledger["last_updated"] = "2026-09-09"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
