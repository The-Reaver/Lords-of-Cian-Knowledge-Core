#!/usr/bin/env python3
"""Batch 253: Xaragua Chronicle VI, "What He Came Without Being Asked" -- the Kanja/Arturo long-arc payoff."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-11, no source document. Full narrative text at "
    "docs/lords-of-cian/chronicles/xaragua-chronicle-vi-what-he-came-without-being-asked.md."
)

BATCH_NOTE = (
    "Xaragua Chronicle VI, \"What He Came Without Being Asked\" -- the direct closing payoff to the "
    "Kanja/Arturo Salvatierra Duho long-arc flagged since Batch 66 (PH2-061): Kanja \"becomes one\" of "
    "Arturo's loved ones. Set after Chronicle V (MCD-1024). Kanja arrives unsummoned after hearing "
    "Arturo has been unwell following a use of Blood Debt's reverse face; Arturo, testing him one last "
    "time, concludes the visit has nothing to do with usefulness and everything to do with being "
    "genuinely fond of him -- explicitly distinguished from, not equated with, Yaisa's unique standing "
    "(hers rooted in remembering who he was before the reputation; Kanja's in caring now, with nothing "
    "to gain). The unnamed-guest convention is preserved in full -- Arturo still never learns Kanja's "
    "real name -- but gives him a private chosen nickname, \"Guaikan\" (Taino remora/guide-fish "
    "folklore, collision-checked clean), paralleling without duplicating the already-locked \"Captain\" "
    "naming pattern. No new named characters; Yaisa (PH2-062) reused with an expanded role. Abad's "
    "approval: \"lock it.\""
)

NEW_RULES = [
    {
        "id": "MCD-1093",
        "category": "territory-chronicle",
        "statement": (
            "Xaragua Chronicle VI, \"What He Came Without Being Asked\" (full narrative text at "
            "docs/lords-of-cian/chronicles/xaragua-chronicle-vi-what-he-came-without-being-asked.md), "
            "the sixth Xaragua Chronicle, set after Chronicle V (MCD-1024). Direct closing payoff to "
            "the long-arc flagged since Batch 66 (PH2-061): Kanja \"becomes one\" of Arturo Salvatierra "
            "Duho's loved ones. Word reaches Kanja, unsummoned, that Arturo has been unwell for eleven "
            "days after using Blood Debt's reverse face on a child-trafficker; he goes to him anyway, "
            "with no territory business and nothing to gain. Arturo, testing him one final time, "
            "concludes the visit proves Kanja is 'fond of him' rather than useful to him -- explicitly "
            "distinguishing this from Yaisa's (PH2-062) unique standing rather than granting parity "
            "with it: her standing depends on remembering who Arturo was before the reputation existed; "
            "Kanja's depends on nothing but caring now, with no history to draw on and no stake in the "
            "outcome. The unnamed-guest convention is preserved in full -- Arturo still never learns "
            "Kanja's real name or alias, consistent with Batch 66/67's explicit walk-back of an earlier "
            "draft that broke this -- but gives him a private, self-chosen nickname instead: "
            "\"Guaikan,\" from Taino coastal folklore's remora/guide-fish that travels beside a shark "
            "unfed and unharmed, by choice. This parallels without duplicating the already-locked "
            "\"Captain\" naming pattern (a name given by loved ones, distinct from any Directorate "
            "classification or birth name). Closes on the first genuine, unguarded banter between "
            "Arturo and Kanja, with Yaisa's blessing implicit throughout. No new named characters; "
            "Yaisa (PH2-062) reused with an expanded but still-secondary role. Closes the long-arc "
            "thread opened in Chronicle II (MCD-337) and advanced in Chronicle V (MCD-1024)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 1, f"expected 1 new rule, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 253,
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
