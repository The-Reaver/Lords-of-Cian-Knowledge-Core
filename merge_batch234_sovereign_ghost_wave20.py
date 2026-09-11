#!/usr/bin/env python3
"""Batch 234: Sovereign Ghost of the Great Sea Alias Chronicle wave 20 (3 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "Locks the Sovereign Ghost of the Great Sea's twentieth three-entry Alias Chronicle wave "
    "(MCD-1038 through MCD-1040). Three genuinely new registers for this alias: a detailed Trinity "
    "combat showcase whose objective is stopping a panicked Trust quarantine-by-scuttling order "
    "rather than defeating raiders or slavers, pairing the combat with a plague/medical-crisis "
    "element never used in any of the prior 57 entries ('The Ship They Meant to Sink'); Dol Maren's "
    "(he/him, CC-120/CC-121) first succession/mentorship entry, training an apprentice shipwright, "
    "mirroring the Storm That Walks alias's own successor-training beat ('What Dol Maren Passed "
    "Down'); and a deepening of the wave-4 foreign-nation thread from a one-time acknowledgment "
    "letter into a sustained bilateral joint-patrol alliance with a shared accountability ledger "
    "('The Pact Signed in Salt Water'). No new named characters introduced; all three entries reuse "
    "already-locked crew (Danne Sok, Efa Gol, Garren Hask, Dol Maren) and leave one-scene antagonists "
    "and envoys unnamed, consistent with this alias's established convention. Collision-checked: "
    "MCD-1038 through MCD-1040 confirmed unused before drafting. Abad's approval: \"doorway for all "
    "the aliases that remain\" (approval of Bane's individually-presented wave 20 plus blanket "
    "authorization to continue the same wave for the remaining ten aliases)."
)

NEW_RULES = [
    {
        "id": "MCD-1038",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Ship They Meant to Sink\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-ship-they-meant-to-sink.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LVIII, wave 20. A detailed naval Trinity combat showcase with a "
            "new objective for this alias -- stopping a panicked Trust cordon from scuttling a "
            "becalmed, fever-stricken merchant hauler under standing quarantine regulation, rather "
            "than defeating raiders, hunters, or slavers. Mafesto's Kinetic Transfer System reads the "
            "cordon's rigging tension ahead of the fire order, Obsidian Malice disables two mounted "
            "cannons without harming their gunners, and Onyx of Oblivion's Whisper of Shadows, "
            "Cadence Ruin, and Veil Piercer break a boarding-repulsion line and read the third "
            "captain's hesitation clean, ending the engagement with no deaths on either side. Efa Gol "
            "organizes a genuine eleven-day quarantine with volunteer fever-resistant crew rather "
            "than a rescue; sixty-one of a hundred and four aboard survive, and Garren Hask logs every "
            "name, living and dead. Extends the coercion-versus-enmity distinction (MCD-542) into "
            "institutional panic rather than conscription. No new named characters. First entry in the "
            "twentieth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1039",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Dol Maren Passed Down\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-dol-maren-passed-down.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LIX, wave 20. Dol Maren (already locked, CC-120/CC-121, "
            "he/him) discovers a stowaway dockyard boy's instinctive aptitude for reading hull stress "
            "and spends a season training him in the flexible-hull principle behind the alias's own "
            "established hurricane-survival technique (MCD-411), teaching by hands-on example rather "
            "than lecture. During a genuine squall, Maren deliberately stands back and lets the boy "
            "call the repair order alone -- every call lands right -- and reflects afterward that a "
            "hull doesn't care who is standing on it when it fails, only that whoever is matters. "
            "Garren Hask logs the fleet's second hull-reader as a plain ledger entry. First entry to "
            "show Dol Maren training a successor, mirroring the Storm That Walks alias's own "
            "successor-training beat and extending Maren's own already-locked reflection on the "
            "ledger outlasting any one person (MCD-959). The apprentice is deliberately left unnamed. "
            "No new named characters. Second entry in the twentieth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1040",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Pact Signed in Salt Water\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-pact-signed-in-salt-water.md), Sovereign Ghost of the "
            "Great Sea Alias Chronicle LX, wave 20, closing the wave. Three years after the foreign "
            "nation's one-time safe-harbor acknowledgment letter (MCD-490, wave 4), the same nation's "
            "envoy returns to negotiate a sustained bilateral arrangement -- ongoing joint patrols "
            "against shared slaving routes, a mutual distress-signal system, and a season's-notice "
            "suspension clause -- rather than a single gesture of goodwill. Kanja insists Garren Hask "
            "keep one shared ledger for both powers' patrols rather than two separately compared "
            "books, extending Hask's already-locked true-record role (MCD-445) into a formal "
            "cross-power accountability mechanism for the first time. The pact is signed aboard The "
            "Ledger in salt-stained ink rather than in a formal chamber; its first season intercepts "
            "four slaving vessels neither power could have reliably caught alone. Distinct from the "
            "wave-4 letter, the tribunal surrender of navigation logs (MCD-410), and the "
            "single-instance witnessed-terms passage (wave 8). The envoy is deliberately left unnamed. "
            "No new named characters. Closes the twentieth wave (with MCD-1038 and MCD-1039)."
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
            "batch": 234,
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
