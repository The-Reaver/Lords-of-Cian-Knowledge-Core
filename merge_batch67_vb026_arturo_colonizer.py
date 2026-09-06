#!/usr/bin/env python3
"""Batch 67: two things.

1. Locks VB-026: the progressive Onyx-of-Oblivion narrator handoff for
   Book 1 / any future Kanja-POV rewrite of Chronicles I-VIII covering
   the Rebellion (ages 18-30). Pure prose-craft standing decision, no
   narrative content of its own.

2. Amends PH2-061 (Arturo) in place: his given name and Spanish
   surname are colonial impositions he keeps deliberately as a
   reminder, Duho is the clan name he recovered through his own
   investigation of his erased lineage, and he is purposefully (not
   uncontrolled, not complaining) adversarial toward anyone descended
   from that colonial lineage -- fully aware race is a constructed
   category, still choosing to direct his war at the lineage that
   built and benefited from it."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "VB-026 and the Arturo colonizer-backstory amendment, chat-drafted "
    "2026-09-06, original invention, no external source document."
)

NEW_RULES = [
    {
        "id": "VB-026",
        "category": "Voice Bible",
        "statement": (
            "Book 1, and any future Kanja-POV treatment of the "
            "Rebellion (ages 18-30, including a rewrite of Chronicles "
            "I-VIII), uses a progressive narrator handoff. Prose opens "
            "in a normal, neutral narrative voice; Onyx of Oblivion "
            "appears only as a short coda at each chapter's end. Across "
            "the Rebellion's twelve years, Onyx's presence grows "
            "steadily more prominent, bleeding further into the main "
            "narration with each successive chapter, until by the "
            "Rebellion's end (age 30, the Trinity's surrender, "
            "MCD-246) Onyx has fully become the narrator -- matching "
            "the already-established steady-state credit at VB-020/021 "
            "for all Long Mask-era and later Kanja material. The "
            "transition must read as smooth and subtle, never an "
            "abrupt jump. Does not apply to the Phase 2 homage-era "
            "territory Chronicles (Xaragua, Umoja, Yara, etc.), which "
            "are close-third on their own territory protagonists, not "
            "Kanja-POV, per VB-020's narrator scope."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

AMENDMENTS = [
    (
        "PH2-061",
        (
            "Two surnames per Abad's direction: Salvatierra (Spanish) kept "
            "alongside Duho added to it (the real Taino word for a "
            "cacique's ceremonial seat of judgment), reflecting the double "
            "Spanish/Taino heritage common to Dominican identity."
        ),
        (
            "Two surnames per Abad's direction, and neither is incidental. "
            "Arturo Salvatierra -- both the given name and the surname -- "
            "is not his family's name; it is the name Spanish colonization "
            "imposed on his lineage generations back, when his ancestors "
            "were stripped of who they were and folded into the "
            "colonizer's own naming system. He kept it deliberately, not "
            "from resignation but as a standing reminder of exactly what "
            "is owed and to whom. Later in life he traced what "
            "colonization tried to erase -- falsified records, destroyed "
            "archives, generations who could not say their own clan's "
            "name aloud without danger -- and recovered Duho, his actual "
            "clan name, the one erasure was built to make sure no one "
            "would ever find again. He added it rather than replacing "
            "anything, so both truths sit in his name at once: what was "
            "done to his family, and what survived it anyway."
        ),
    ),
    (
        "PH2-061",
        (
            "Personality: a force of nature, very rarely outwitted, "
            "unflappable and commanding without ever being boastful; the "
            "one exception is playful banter with those who've earned it, "
            "which as of Xaragua Chronicle II is only Yaisa (PH2-062)."
        ),
        (
            "Personality: a force of nature, very rarely outwitted, "
            "unflappable and commanding without ever being boastful; the "
            "one exception is playful banter with those who've earned it, "
            "which as of Xaragua Chronicle II is only Yaisa (PH2-062). "
            "Toward anyone descended from the specific colonial lineage "
            "responsible for what was done to his own -- regardless of "
            "that individual's rank, danger, or personal innocence -- he "
            "is deliberately, purposefully adversarial, and enjoys being "
            "so; this is a chosen and ongoing position, not a loss of "
            "control, and his S-tier standing means consequence was never "
            "what held him back from it. He is fully aware that race as a "
            "category did not exist before the colonial system that "
            "invented it to organize who could take from whom -- he is "
            "not confused about the science of it, and he directs his war "
            "at the lineage that built and benefited from that invented "
            "structure anyway, because the categories may be constructed "
            "but the harm done using them was not. He carries none of "
            "this as complaint or unresolved rage; he made his peace with "
            "the choice long ago and has never once second-guessed it."
        ),
    ),
]

BATCH_NOTE = 'Abad: "Onyx of Oblivion is confirmed. and I approve the colonizer backstory Amendment"'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    amended = []
    for rule_id, old_tail, new_tail in AMENDMENTS:
        found = False
        for rule in ledger["rules"]:
            if rule["id"] == rule_id:
                assert old_tail in rule["statement"], f"old_tail not found in {rule_id}"
                rule["statement"] = rule["statement"].replace(old_tail, new_tail)
                found = True
        assert found, f"{rule_id} not found"
        amended.append(rule_id)

    ledger["batches_completed"].append(
        {
            "batch": 67,
            "source_doc": (
                "VB-026 (the progressive Onyx-narrator handoff for Book 1 "
                "/ Chronicles I-VIII) and the Arturo colonizer-backstory "
                "amendment to PH2-061 (colonial-imposed given name and "
                "surname kept as a reminder, Duho recovered through "
                "self-directed lineage investigation, purposeful "
                "adversarial stance toward the colonizer lineage, race "
                "framed in-world as a constructed category)."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "7.0"
    ledger["last_updated"] = "2026-09-06"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")
    print(f"Amended: {amended}")


if __name__ == "__main__":
    main()
