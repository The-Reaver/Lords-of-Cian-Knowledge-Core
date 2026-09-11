#!/usr/bin/env python3
"""Batch 228: the final four Branded Legends, closing out the Maw Codex source document."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Maw_Codex_Definitive_Edition.docx (Google Drive fileId 1uKHTHJcZob-4oDPjrd7U0o2Nlu-bGSiv), "
    "the same 290,147-character extraction used for Batches 103 and 227. A direct re-check of the "
    "document's own 'BATCH 3: THE BRANDED LEGENDS' section (18 named fighters) against the live "
    "ledger found 14 of the 18 already locked (10 via the Reclamation Records and the Apex "
    "Championship field roster at MAW-101/MAW-111/etc., 4 via Batch 227's new legend rules), leaving "
    "exactly 4 genuinely undrafted: Graves, Ash Korren, Dray Voss, and Tella Brightblade -- all "
    "already named in passing elsewhere in the ledger but with the Branded Legends section's own "
    "fuller texture never pulled in."
)

BATCH_NOTE = (
    "Asked to continue the Maw Codex work to completion, cross-referenced all 18 named fighters in "
    "the source document's Branded Legends section against the live ledger. 14 were already fully "
    "covered (Lirra Chain-Singer, Mordecai the Harvest, Dural the Scarmaker, Korrith the Scorpion, "
    "and Valor Thenn via the Reclamation Records; Draven the First Blood, Thessara Void-Step, "
    "Kaedrin the Undying, Essek Nightfall, Brennan Ironsong, Silent Mara, the Three Sisters of "
    "Dravos, Kullen Gravedust, and Renn Hollow via Batch 227). The remaining 4 were drafted here as "
    "extensions to their existing thin mentions rather than fresh entries, since all four were "
    "already named (Ash Korren, Dray Voss, and Tella Brightblade in MAW-101's Apex field roster and "
    "Graves in MAW-091/MAW-111's Reclamation Records) -- this batch adds the Branded Legends "
    "section's own additional texture (fighting-style detail, family/patron reaction, Book 1 "
    "narrative framing, and for Graves specifically the origin of his own name and the Brand-Line's "
    "closing interpretation of Vakas's pause over his body) without restating what was already "
    "locked. Zero new proper-noun collisions found (Graves, Ash Korren, Dray Voss, Tella "
    "Brightblade, Dorne Brightblade, Voss Dravos, Meritha, Seyra, Torven, Drennan, and Brightblade "
    "Prize all checked clean against the full live ledger). This closes the Maw Codex source "
    "document out in full -- every one of its 8 internal batches (Pillars, Banners+Pits, Branded "
    "Legends, Shapers, Grand Maws, Cestari, Economics, Reclamation Records) is now completely "
    "reflected in canon. Abad's approval, quoted verbatim: \"continue uninterrupted until completion "
    "this includes test, commit, push to main origin complete Maw Codex.\""
)

NEW_RULES = [
    {
        "id": "MAW-147",
        "category": "legend-ash-korren",
        "statement": (
            "Extends MAW-101/MAW-133. Ash Korren \"The Debt\" fights with the cold, transactional "
            "fury of a man discharging a debt rather than competing in a sport -- no performance, no "
            "showmanship, violence applied with the exact efficiency of a financial payment, because "
            "every bout literally is one: each victory reduces the principal against his family's "
            "estate, seized by Sektori's banking patron under Scrip-Tether debt-compliance law. His "
            "style is hybrid -- Dravos endurance from his original Standard's Iron Patience training, "
            "overlaid with Sektori's risk-management doctrine (MAW-133) -- producing the most "
            "conservative Grand Circuit competitor in a generation, a style with every inefficiency "
            "eliminated and nothing left for an opponent to exploit. Currently Grand Circuit #3, "
            "77-3, Apex Contender; the mathematics say roughly four more years of purses clear the "
            "debt, against roughly 60% odds of surviving them. Book 1 Connection: Ash Korren is the "
            "fighter Ozmund must defeat to reach the Apex, framed by the Codex as \"a Forsaken Prince "
            "with unmeasured density against a debt-slave with nothing to lose\" -- the man who "
            "rejected a throne against the man who lost everything a throne is supposed to protect."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-148",
        "category": "legend-dray-voss",
        "statement": (
            "Extends MAW-101. Dray Voss \"The Inheritor\" is the direct descendant of Voss Dravos, a "
            "Cestari-born fighter who earned House Dravos's own name 900 years ago; the Voss line has "
            "held Dravos affiliation across every generation since, a dynasty of Branded fighters "
            "whose family history doubles as the Pillar's own modern history. Doctrinally orthodox "
            "(pure Iron Patience) and technically excellent, he carries the dynasty's weight visibly "
            "-- top-five ranked six consecutive years, two Apex finals, two losses, fighting (the "
            "Codex's own phrase) \"like a man serving a sentence\" rather than pursuing a dream. Book "
            "1 Connection: Dray Voss represents the Pillar establishment that Ozmund's unorthodox "
            "Vennrik entry disrupts; Ozmund defeating the Inheritor of the system's oldest active "
            "dynasty would reverberate through every House in the Maw."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-149",
        "category": "legend-tella-brightblade",
        "statement": (
            "Extends MAW-101. Tella Brightblade is the great-granddaughter of Dorne Brightblade, the "
            "Maw's most commercially successful fighter in history and namesake of the still-unclaimed "
            "Brightblade Prize; she inherited her family's merchandising empire and the Prize's "
            "administrative legacy but rejected the business path to compete herself, fighting under "
            "House Korrath's banner with the Meritha Consortium's (MAW-026) enthusiastic patronage -- "
            "a competing Brightblade is the sport's single most valuable marketing asset -- against "
            "her own family's horror, since the Brightblade fortune was built on spectacle rather "
            "than risk and Tella is risking the body it was built to protect. She fights with twin "
            "crescent blades in a style that quotes her great-grandfather's legendary combination "
            "sequences while innovating past them; not as fast as Seyra \"the Tempest\" (MAW-101) nor "
            "as technically precise as Torven (MAW-101/MAW-146), she is the current Grand Circuit's "
            "most watchable competitor because she fights the way Korrath has always fought -- to "
            "make the crowd love her. Currently Grand Circuit #11, 42-8, rising. No Brightblade has "
            "ever won the Brightblade Prize; Tella intends to be the first."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MAW-150",
        "category": "legend-graves",
        "statement": (
            "Extends MAW-091/MAW-111. Fills in the origin of Graves's own name and one closing detail "
            "the Reclamation Records omit. He earned it during the Maw's most dangerous decade "
            "(MAW-091's Post-Haku Transition, medical mandates and fighter-welfare protections "
            "collapsed with T.D.K.'s state): a Threnn fighter who held the Inevitable doctrine -- "
            "advance, absorb, do not deviate -- when the doctrine's institutional support no longer "
            "existed, and buried more opponents in that decade than any fighter before or since. The "
            "crowd gave him the name, not the Brand-Line or the Ledger Offices: \"Graves,\" because "
            "every bout ended with him standing over what he'd left behind. The Brand-Line's own "
            "retrospective interpretation of Vakas's thirty-second pause over his body after the "
            "second Reclamation kill (MAW-111): even Vakas mourned the honest ones."
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
            "batch": 228,
            "date": str(date.today()),
            "source": "Maw_Codex_Definitive_Edition.docx (final 4 Branded Legends)",
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
