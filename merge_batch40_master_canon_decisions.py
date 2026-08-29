#!/usr/bin/env python3
"""Batch 40: Master Canon Decisions cross-check (Rexmar decline institutions, Zenith-Prime)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'MASTER CANON DECISIONS.docx' (Google Drive fileId "
    "1NLOAu4Qh_ICV30Yd9tKVoBpX2GNBRiBb, Lore Vault) -- the ledger's own "
    "designated tie-breaker authority per its authority_order field. "
    "Despite its 797KB file size, the document's actual text is only "
    "~28KB (the rest is embedded font data); nearly all of it was "
    "already reflected in the live ledger on cross-check, with zero "
    "unresolved contradictions on any load-bearing fact (Lauris's "
    "biology, T.D.K.'s identity, Ozmund/Kanja lineage, the Kareth "
    "sisters, the Meridian Compact/Sovereign Trust split, the Zenith-Rod). "
    "The document's own 'SESSION LOCKS -- GEOGRAPHY (August 12, 2026)' "
    "section is stale (superseded by the already-locked MCD-110/MCD-111, "
    "dated one day after this document's last edit); since the tool "
    "available in this session cannot edit an existing Drive file's "
    "content in place, Abad had a standalone correction note created "
    "alongside the original in the Lore Vault "
    "('Master_Canon_Decisions_CORRECTIONS', Drive fileId "
    "1FDWJXBgsdf4oeuHBFDRIIbm1vsj7YEn8AB2GaXJbNVM) rather than editing "
    "the ledger itself, since the ledger already carries the correct "
    "ruling. MCD-229's Zenith-Prime definition is original invention, "
    "chat-drafted 2026-08-25, no source document defines the term beyond "
    "naming it as the source of Orlok's Book 4 enlightenment insight; "
    "built to fit the already-locked Celestial Zenith 'Cultivated "
    "Sovereignty' framing from the Shattered Kingdoms Political Atlas."
)

NEW_RULES = [
    {
        "id": "MCD-228",
        "category": "World Mechanics",
        "statement": (
            "After Haku united Jicome's Rex mainland and Mar archipelago "
            "into one kingdom, the Rexmar line held it as functional "
            "Kings of the Sea before five successive generations traded "
            "functional power for ceremonial royalty, each losing the "
            "kingdom through one named concession (extends the bare name "
            "list at MCD-121): Turey Rexmar ('the Traditionalist') "
            "locked the family into the restrictive Sacred Pact; Amaru "
            "Rexmar ('the Visionary') let the Elite gain a foothold in "
            "Jicome in exchange for prospering from the Zephyr Root "
            "trade; Yabura Rexmar ('the Connector') traded the family's "
            "pilotage rights for short-term wealth under the Treaty of "
            "Fathoms; Yaro Rexmar ('the Binder') agreed to the Salt Act "
            "trying to undo past mistakes, losing the common sailors' "
            "support; and Maro Rexmar (Kanja's father) collateralized "
            "the family's drydocks and flagship under the Harbor Bank "
            "Indenture and was assassinated at the Sovereignty Summit "
            "for it. No single concession was unreasonable; together "
            "they let the Meridian Compact (already locked as distinct "
            "from the Sovereign Trust) take the kingdom by treaty, "
            "title, and debt rather than by force."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-229",
        "category": "World Mechanics",
        "statement": (
            "Orlok's Book 4 enlightenment (extends MCD-096) is triggered "
            "by the Vakas draw; the catalyzing insight comes from "
            "Zenith-Prime, the paramount spiritual-political authority "
            "of Celestial Zenith (Orlok's home nation, already locked as "
            "a 'Cultivated Sovereignty' of floating monasteries) -- "
            "doctrinal counsel on releasing fixed ceilings and form, "
            "delivered in the draw's aftermath, not a combat technique. "
            "The enlightenment itself occurs at the end of Book 4 or the "
            "opening of Book 5."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation, including the Zenith-Prime definition and the standalone correction-note approach for the stale geography section: "lock it"'


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
            "batch": 40,
            "source_doc": "MASTER CANON DECISIONS.docx (cross-checked against the live ledger; nearly all content already locked, only two genuinely new items found)",
            "source_id": "1NLOAu4Qh_ICV30Yd9tKVoBpX2GNBRiBb",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "4.3"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
