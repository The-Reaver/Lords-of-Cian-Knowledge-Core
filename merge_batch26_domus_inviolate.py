#!/usr/bin/env python3
"""Merge Batch 26 into canon-ledger.json: the Domus Inviolate cult dossier."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'Domus_Inviolate_Dossier' (Google Drive fileId "
    "19FOKjvEaBqCU39_wkOX6GCFMokHDKPgYsw_f4U4w90U, Lore Vault folder; two other byte-identical "
    "copies exist at Drive root, 1TeMFE2qZBRNWgxRhz6llYR_wQ5uH9um8-LtMX8sZITc and .docx "
    "1a0_sTug3IibEYSmTGaSz6vFAUTHTNYuR, not separately extracted). Resolves the forward "
    "cross-references planted at CULT-022, CULT-030, CULT-035, CULT-036, and CULT-134 in "
    "earlier cult-network batches, all of which explicitly anticipated this batch."
)

NEW_RULES = [
    {
        "id": "CULT-182",
        "category": "Cult Network",
        "statement": (
            "The Domus Inviolate ('the Unbroken House') is a Category One rural-family cult, "
            "one of the 'rural-family cults' already cross-referenced at CULT-134 alongside "
            "the Weighing Communities and the Zero-Point Households. It self-identifies as a "
            "household, not a religion: members claim genuine multigenerational descent from "
            "the administrative household staff (record-keepers, provisioners, infrastructure "
            "maintainers, not soldiers or spiritual intermediaries) of T.D.K.'s Old Dominion "
            "court. This descent claim is accurate. The theology layered over it, that the "
            "Accounting is devotional maintenance owed against 'the debt of the Resumption' "
            "pending the King's return, is not, but the five-thousand-year practice it produced "
            "is CULT-134's exact case study: effective because it was always disciplined "
            "resource management, not because anyone was watching."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-183",
        "category": "Cult Network",
        "statement": (
            "The Domus Inviolate occupies seven villages in the high interior of the Obsidian "
            "Prefecture's eastern borderland, above the altitude line the Prefecture's "
            "administration doesn't reach. The seven villages function as one household ('one "
            "house with seven rooms'), sharing labor, resources, and authority. Leadership "
            "descends through a single unbroken bloodline: the Accountant is always the eldest "
            "female of the primary descent line, no election or contest. Below her, three "
            "tiers: the Keepers (one per village, responsible for the physical Carrier "
            "Weights), the Readers (maintain the oral and written Ledger), and the Measured "
            "(full adult members who passed the density verification, a membership gate rather "
            "than a real diagnostic)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-184",
        "category": "Cult Network",
        "statement": (
            "Twice daily, every adult member performs the Weight Recitation (~40 minutes): "
            "reciting memorized density values tied to specific Old Dominion administrative "
            "roles, facing the direction their records mark as T.D.K.'s last governance "
            "chamber. They believe this is Frequency Submission, maintaining a signal "
            "architecture the King will detect from dormancy, using genuine but fragmentary "
            "pieces of the Ten Tongues frequency architecture (WC-021). The belief is wrong; "
            "the practice is not inert. Structured group vocalization from real Old Dominion "
            "calibration documentation produces measurable bioelectric synchronization among "
            "practitioners, which the community attributes to royal attention rather than to "
            "what it actually is."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-185",
        "category": "Cult Network",
        "statement": (
            "Three thousand years ago the Domus Inviolate closed its bloodline to outside "
            "marriage, to preserve what they call the 'correct weight profile.' The result, in "
            "the source material's own clinical framing, is 'a genuinely compressed genetic "
            "profile, significant heritable conditions, and an absolute cultural inability to "
            "recognize this as a problem.' The community's most severe cases, individuals who "
            "cannot maintain standard gravitational interaction with their environment, are "
            "revered as 'the Weight returning,' a direct biological sign of the King's favor, "
            "rather than recognized as the specific shape their harm takes. The Ledger has no "
            "framework for hereditary disease, only for density compliance, so every symptom "
            "is read back through that lens as confirmation."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-186",
        "category": "Cult Network",
        "statement": (
            "For three generations, some Domus Inviolate members have also been ingesting "
            "fragments of Warbody Residue (T.D.K.'s shed biological/engineered material across "
            "30-40,000 years of active governance, the same relic category the Concordat "
            "separately holds seven fragments of per CULT-035), believing consumption "
            "transfers the King's measure directly. The source material's assessment: this is "
            "'engineered biological material with an unknown effect profile on standard human "
            "biology.' The community's heritable conditions therefore have two "
            "indistinguishable possible causes from inside their own framework, genetic "
            "compression and three generations of ingested engineered material, both read "
            "identically as the Weight returning, neither ever examined from outside."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-187",
        "category": "Cult Network",
        "statement": (
            "The Keeper cabinets across the seven villages hold genuine Old Dominion "
            "administrative instruments, treated as sacred but not understood. The primary "
            "object is a density-compliance calibration rod once used to verify T.D.K.'s "
            "architects worked to specification, one piece of an incomplete three-piece "
            "Calibration Array (per CULT-035, the other pieces are elsewhere in the "
            "Concordat's holdings). Two of the seven cabinets also hold Crown-Scar "
            "documentation, records (not the procedure itself) of how T.D.K.'s governance "
            "architecture was embedded in the Verehimu bloodline's biological predecessor, "
            "written in an administrative hand and sealed in dead Drakma. Per the source "
            "material, this is among the most dangerous unlocated documentation in the "
            "Shattered Kingdoms."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-188",
        "category": "Cult Network",
        "statement": (
            "The Accountant authorized her nineteen-year-old son, a Reader, to leave the "
            "villages for the first time in his life and sell the calibration rod to a "
            "Concordat of the Long Account representative (CULT-031), the community's first "
            "outside transaction in five thousand years. The sale also produced a Crown-Scar "
            "documentation rubbing, later brokered separately by a Ledger Family head and "
            "confiscated by the Concordat (CULT-022, CULT-036). The Concordat killed the "
            "Reader rather than let him return with knowledge of their operation and to "
            "prevent his public sale from setting a precedent that would expose "
            "Keeper-cabinet objects to the wider cult ecosystem (CULT-036); the ordering "
            "Creditor secured the rod but left a Concordat commercial seal in the Reader's "
            "pocket. He died in a Karkosa district three days before the Fulfillment "
            "Ceremony."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-189",
        "category": "Cult Network",
        "statement": (
            "On learning of her son's death, the Accountant declared all seven villages into "
            "administrative suspension: the Accounting stopped, the Recitations stopped, the "
            "Keeper cabinets sealed shut. To the community this reads as 'the equivalent of "
            "cutting life support,' a procedural response to a double breach of custodial "
            "obligation (the Reader's death and the calibration rod's loss) rather than grief "
            "in any outside sense. Some members, having never left the villages, began walking "
            "toward Karkosa to retrieve what was taken, unequipped and unfamiliar with how the "
            "city or the Concordat's operation works, making them conspicuous in a city "
            "mid-crisis over the double regicide."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-190",
        "category": "Cult Network",
        "statement": (
            "An investigator traces the Reader's death (via a Ledger entry, a commercial seal, "
            "and the missing calibration rod) back to the seven villages, arriving during the "
            "administrative suspension. He finds no functioning community to question, only "
            "the suspension in progress: cabinets sealed, Ledger unopened, the Accountant in "
            "formal procedural withdrawal rather than refusal, and members already gone toward "
            "the city. No Crown-Scar intelligence is available at the source; the path to the "
            "documentation runs through the Concordat's side of the transaction instead."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-191",
        "category": "Cult Network",
        "statement": (
            "After the Fulfillment Ceremony and Great Breach, the Accountant, watching only "
            "from a distance through disruption reports, concludes the Resumption is complete: "
            "the King returned to open governance. She has no access to the fact that he was "
            "returned and then re-contained by his own architecture. The administrative "
            "suspension ends; the villages reopen, cabinets unlock, Recitations resume, and "
            "the Accountant declares the household's compliance obligation fulfilled, five "
            "thousand years vindicated."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-192",
        "category": "Cult Network",
        "statement": (
            "For the first time in recorded history, the Domus Inviolate lifts its exclusion "
            "and begins accepting Uncounted members, people who could have been born into the "
            "household but weren't. This ends three thousand years of closed-bloodline policy "
            "at the exact moment its most dangerous asset, the Crown-Scar documentation, "
            "becomes newly exposed: unlike the insular community itself, an outside-born new "
            "member with prior exposure to Old Dominion notation or the Ledger Families'/urban "
            "cult networks' interpretive resources could actually extract operational "
            "intelligence about the Crown-Scar procedure from those sealed records, something "
            "no born-Domus member has ever been positioned to do."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-193",
        "category": "Cult Network",
        "statement": (
            "The community has no clean post-Breach ideological schism, only a silent, "
            "structurally unresolvable one. Members who walked to Karkosa during the "
            "suspension returned holding outside information the Ledger has no language for, "
            "specifically the concept of containment, which contradicts the Accountant's "
            "'Resumption complete' declaration. The household's structure provides no "
            "mechanism to challenge the Accountant's authority, so the contradiction goes "
            "unspoken rather than unresolved: held silently by returning members in a "
            "community that has never before had to hold a contradiction the Ledger couldn't "
            "settle."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation: "lock it"'


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
            "batch": 26,
            "source_doc": "Domus_Inviolate_Dossier",
            "source_id": "19FOKjvEaBqCU39_wkOX6GCFMokHDKPgYsw_f4U4w90U",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "2.9"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
