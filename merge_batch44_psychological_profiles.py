#!/usr/bin/env python3
"""Batch 44: All_Psychological_Profiles.zip -- deep psychology/mechanism
material for Anu Un Ra, Vargo Vakas, Orlok, Valen, Sephtis, and Lauris.
Also promotes four long-stalled draft rules (CULT-003/004/005, WC-016) that
this document independently corroborates, and resolves a real conflict
(Lauris's knowledge of Ezio's classified combat capability) per Abad's
explicit ruling."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'All_Psychological_Profiles.zip' (Google Drive fileId "
    "1diE9NWChARTBz8UTrdo6ECOj99ZKhDhO, Lore Vault) -- eight character "
    "psychological-profile companion documents (01_Anansi through "
    "08_Valen), each keyed to its Character Codex entry. Fetched and read "
    "in full; four (Anansi, Valeria, most of Lauris) were found to be "
    "almost entirely prose/writing-craft elaboration of already-locked "
    "facts and are not separately drafted here. The other four -- Anu Un "
    "Ra, Vargo Vakas, Orlok, Valen, Sephtis, and one section of Lauris's -- "
    "contained genuinely new mechanism, origin, and plot facts. Two "
    "pre-existing draft-status rules this document independently "
    "corroborates are promoted to locked in this same batch: CULT-003/"
    "004/005 (the original 'DOSSIER: ANU UN RA' extraction's psychology, "
    "Meridian Engine/Exchange Protocol origin, and Ionic Rite methodology "
    "rules) and WC-016 (the Ezio/Valen cousin and classified-capability "
    "rule, amended below). A real conflict surfaced during drafting: "
    "Lauris's profile states she personally knows Ezio's classified "
    "combat capability and that her Attia role functions partly as "
    "deliberate cover-maintenance for him, directly contradicting the "
    "already-locked closed list of four (Valen, Sephtis, Kanja, Anansi) "
    "at CC-027 and WC-016. Presented to Abad rather than resolved "
    "unilaterally; his ruling -- \"she does know\" -- is applied by "
    "amending CC-027 and WC-016 in place to add Lauris to the list, "
    "consistent with the Batch 41 precedent of a merge script editing an "
    "existing rule rather than only appending."
)

# --- In-place amendments (existing rules) ---

def amend_cc027(rule):
    rule["statement"] = (
        "Ezio Valcari is publicly known as a theorist/spymaster, but is "
        "classified as an elite close-quarters combatant capable of "
        "killing a room in three seconds; this is known only to Valen, "
        "Sephtis, Kanja, Anansi, and Lauris."
    )
    rule["note"] = (
        "Amended in Batch 44 to add Lauris per Abad's explicit ruling "
        "('she does know') resolving a conflict raised by the "
        "Psychological Profiles document, which states she has seen the "
        "Valcari War-Side in action and that her Attia role includes "
        "deliberate cover-maintenance for Ezio (see CC-111)."
    )


def amend_wc016(rule):
    rule["statement"] = (
        "Ezio Valcari and Valen (Sinisterblade) are first cousins from a "
        "shared martial family tradition ('the Sinister Bloodline'). "
        "Ezio's true combat capability (can kill a room in three seconds) "
        "is classified; only Valen, Sephtis, Kanja, Anansi, and Lauris "
        "know it. Valen protects Ezio's cover."
    )
    rule["status"] = "locked"
    rule["note"] = (
        "Promoted from draft to locked in Batch 44, independently "
        "corroborated by the Psychological Profiles document, and "
        "amended to add Lauris per Abad's explicit ruling ('she does "
        "know') -- see CC-027's matching amendment and CC-111."
    )


AMENDMENTS = {
    "CC-027": amend_cc027,
    "WC-016": amend_wc016,
}

PROMOTIONS = {
    "CULT-003": "Promoted from draft to locked in Batch 44, independently corroborated by the Anu Un Ra Psychological Profile document.",
    "CULT-004": "Promoted from draft to locked in Batch 44, independently corroborated by the Anu Un Ra Psychological Profile document, which also supplies the Warbody-as-life-support framing at CULT-194.",
    "CULT-005": "Promoted from draft to locked in Batch 44, independently corroborated by the Anu Un Ra Psychological Profile document.",
}

NEW_RULES = [
    {
        "id": "CULT-194",
        "category": "anu-un-ra-psychology",
        "statement": (
            "The Warbody is fundamentally a life-support and maintenance "
            "apparatus for the Exchange Protocol's physiological "
            "degradation, not primarily a weapon -- every deployment is "
            "simultaneously a medical procedure and a military operation. "
            "Extends CULT-004/ARS-270."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-195",
        "category": "anu-un-ra-psychology",
        "statement": (
            "Anu Un Ra's psychology is not sociopathy: he processes the "
            "suffering his actions cause as real, classifies it as a "
            "cost, and enters it into a permanent mental ledger rather "
            "than failing to register it. His patience is conservation "
            "-- every engagement is weighed against a fixed, narrowing "
            "maintenance budget the degradation imposes -- not fear or "
            "strategy for its own sake."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CULT-196",
        "category": "anu-un-ra-psychology",
        "statement": (
            "Anu's relationship to his hidden son Archon is institutional, "
            "not paternal: Archon is 'maintained,' filed as a "
            "contingency asset, placed under a false name specifically so "
            "he cannot be leveraged through attachment. Whether Anu is "
            "capable of something warmer than architecture is "
            "deliberately left unresolved. Extends MCD-130/CC-054."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-105",
        "category": "character-antagonist",
        "statement": (
            "Vargo Vakas is roughly 18,000 years old, one of the world's "
            "'Titans' (present during the Merak purge's aftermath); his "
            "20,000x density was purchased through Hollow Shogunate "
            "synthetic augmentation (Abyssal Bile and extraction "
            "methodology) rather than cultivated, making him the "
            "prototype the Shogunate later mass-produced into its "
            "Sin-Eater champions (4,000-6,200x)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-106",
        "category": "character-antagonist",
        "statement": (
            "The Book 4 Orlok/Vakas draw is a genuine mutual stalemate -- "
            "Vakas's permanence and Orlok's variability neutralize each "
            "other for the full 30-45 second Ascension window, with "
            "neither able to end the other -- and this stalemate directly "
            "triggers Orlok's path to Enlightenment. Vakas fights among "
            "the opposing forces at the Book 5 Gate Battle, where an "
            "Enlightened Orlok resolves the rivalry, ending the "
            "mirror-conflict."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-107",
        "category": "character-orlok",
        "statement": (
            "Extends CC-093/MCD-096: Orlok's Enlightenment (density-fluid, "
            "no ceiling, no transitions, no recovery cost) carries a "
            "biological cost -- it accelerates erosion of the cellular "
            "architecture his cultivation built, making the Enlightened "
            "state finite and self-consuming rather than a stable new "
            "baseline."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-108",
        "category": "character-crew",
        "statement": (
            "Extends CC-035: Valen personally and familially trained Ezio "
            "in the Sinister Bloodline's War-Side tradition, rather than "
            "the two merely sharing a tradition. Valen's combat baseline "
            "is measured at 99.97% efficiency; the remaining 0.03% waste "
            "is the standard against which he judges every engagement."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-109",
        "category": "character-crew",
        "statement": (
            "Extends CC-035: Serai Noth's ('the Blade') signature "
            "technique is a 0.8-second target-elimination window. Her "
            "already-locked Book 5 reckoning by Valen is resolved without "
            "a mark on his white robes -- a first -- and its emotional "
            "register is correction of a corrupted shared tradition, not "
            "vengeance."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-110",
        "category": "character-crew",
        "statement": (
            "Extends CC-037: Sephtis's Chrono-Anchor bells verify spoken "
            "claims against his own memory of the True Timeline, "
            "registering a mismatch as a perceptible signal; the "
            "verification is non-transferable -- he can testify to what "
            "he remembers but cannot prove it to anyone else. He has "
            "known Kanja is Pyro's father for 24 years and has never "
            "disclosed it. His core worldview is Flow vs. Stagnation "
            "rather than Good vs. Evil: institutional stasis maintained "
            "for extraction is worse than open collapse."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-111",
        "category": "character-crew",
        "statement": (
            "Extends CC-027/WC-016 (amended in this same batch, per "
            "Abad's ruling 'she does know'): Lauris knows Ezio's "
            "classified combat capability, and her Attia bond to him "
            "functions partly as deliberate cover-maintenance -- her "
            "conspicuous, undisguised lethality occupies the crew's and "
            "the enemy's threat assessment so no engagement ever forces "
            "Ezio to reveal what his own capability actually is."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Abad approved the full draft as pasted in-conversation, and resolved '
    'the flagged Lauris/Ezio-secret conflict explicitly: "she does know"'
)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    by_id = {r["id"]: r for r in ledger["rules"]}

    for rid, fn in AMENDMENTS.items():
        assert rid in by_id, f"amendment target {rid} not found"
        fn(by_id[rid])

    for rid, note in PROMOTIONS.items():
        assert rid in by_id, f"promotion target {rid} not found"
        assert by_id[rid]["status"] == "draft", f"{rid} was not draft"
        by_id[rid]["status"] = "locked"
        by_id[rid]["note"] = note

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 44,
            "source_doc": "All_Psychological_Profiles.zip (8 companion psychology documents: Anansi, Orlok, Valeria, Lauris, Sephtis, Anu Un Ra, Vargo Vakas, Valen)",
            "source_id": "1diE9NWChARTBz8UTrdo6ECOj99ZKhDhO",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 1,
            "conflicts_resolved": 1,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "4.7"
    ledger["last_updated"] = "2026-09-02"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
