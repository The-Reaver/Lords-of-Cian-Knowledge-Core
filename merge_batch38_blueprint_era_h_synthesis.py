#!/usr/bin/env python3
"""Batch 38: World Adaptation Blueprint, Section VI Era H (Synthesis) -- closes the Lauris Letitia Chronicle."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'World_Adaptation_Blueprint' (Google Drive fileId "
    "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA, Lore Vault), Section VI "
    "('The Lauris Letitia Chronicle'), Era H ('Synthesis') -- the "
    "chronicle's closing frame. No new operational events; this era "
    "consolidates the accumulated Section VI material into her present-day "
    "identity, clarifies what she is not, sketches a flexible five-book "
    "structural framework (explicitly not fixed plot specification), and "
    "frames the chronicle's thematic function. One minor number "
    "normalized: the source's 'karth-ven achieved at age 1,841' is locked "
    "to match the already-locked age 1,840 (MCD-172), a one-year rounding "
    "discrepancy rather than a substantive conflict. This batch closes "
    "Section VI (Eras A through H) of the World Adaptation Blueprint in "
    "its entirety."
)

NEW_RULES = [
    {
        "id": "MCD-212",
        "category": "World Mechanics",
        "statement": (
            "At the start of My Rival's Distance Book 1, Lauris's "
            "consolidated present-day identity is: roughly 4,000 years "
            "old, the final pure-blood Karesian of Kares Prime, the "
            "synthesis evolution of her species' final 1,200-year "
            "preservation program, her species' most lethal individual, "
            "Ezio Valcari's operational asset and Attia, wielder of the "
            "Forged Triad and the Integrated Variable Phalanx, "
            "joint-archive holder with Sephtis on Anu Un Ra's engineering "
            "tradition, operational coordinator with Aerelin's autonomous "
            "Kareth War-Order network, protector of roughly 700+ "
            "engineered Karesian subjects across her accumulated cave "
            "systems and contained facilities (the Drowning Vault's 120, "
            "Site K-Theta's 200, Operation 37's ~280, and further "
            "accumulated rescues), the biological analog of the planet's "
            "Talisman-driven hardening, and the only homeworld-native "
            "Karesian the Karkosa's senior crew knows exists (Val Mirel's "
            "parallel alignment held via deliberate non-contact). The "
            "Lords of Cian's operational structure rests on four anchors: "
            "Sephtis (archival), Kanja (command), Ezio (strategic), "
            "Lauris (operational) -- the rest of the senior crew operates "
            "in support of these four."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-213",
        "category": "World Mechanics",
        "statement": (
            "Lauris is not Karesian-derived; she is the homeworld source "
            "population itself, of which the Kareth War-Order (Ozmund's "
            "and Kanja's maternal lineage) is a 122,000-year-old diaspora "
            "descendant at a different developmental epoch (MCD-151). Nor "
            "is she the cooperative-era Karesian baseline: the 47-donor "
            "synthesis recombination that produced her (MCD-157) "
            "integrated structural advantages across the species' full "
            "preserved developmental potential, making her the genome "
            "direction her species was evolving toward when the K-strand "
            "decline interrupted it, not a return to what it had been."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-214",
        "category": "World Mechanics",
        "statement": (
            "Lauris's chronological age relative to the Kareth War-Order "
            "inverts against Karesian adult-developmental seniority: she "
            "is roughly twelve times Kanja's age in calendar years, but "
            "her synthesis-genome youth places her, in Karesian "
            "generational terms, at biological 'young first adult' status "
            "-- younger in adult-developmental terms than several senior "
            "Kareth War-Order operatives (including Val Saeryn at 93,179, "
            "MCD-155) despite being chronologically older than all of "
            "them. The Karesian framework for relative seniority does not "
            "produce a clean ordering across the Kares Prime / "
            "Kareth-diaspora developmental divergence."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-215",
        "category": "World Mechanics",
        "statement": (
            "Lauris has had no romantic partner across her roughly 4,000 "
            "years; her present-day relationships (professional trust "
            "with Ezio, operational deference and equipment-maintenance "
            "authority with Kanja, archival alliance with Sephtis, "
            "sparring companionship with Valen, adequate-but-"
            "undemonstrative ties to the rest of the crew) are all "
            "non-romantic, consistent with the non-romantic character of "
            "both the Karesian Pair-Hold and Sister-Hold traditions she "
            "was raised in. Nor is she lonely: her karth-ven integration "
            "of her species' loss (MCD-172, age 1,840) has held ever "
            "since, and her psychology -- rooted in the Karesian practice "
            "of witness -- does not require continuous social "
            "affirmation; her closest present-day companionships "
            "(Sephtis, Valen) are conducted at low conversational volume "
            "across long durations."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-216",
        "category": "World Mechanics",
        "statement": (
            "The chronicle's closing frame sketches a flexible, "
            "non-binding structural framework (explicitly not fixed plot "
            "specification) for Lauris's role across My Rival's "
            "Distance's five books: Book 1, operational anchor and "
            "visible deterrent during the Karkosa Heist, her deference "
            "toward Kanja still distant; Book 2, continued anchor, a "
            "possible early quay-stones conversation with Ezio, "
            "unexplained Aerelin-sourced support, deepening Sephtis "
            "archive work; Book 3, the first on-page articulation of the "
            "World Adaptation observation (to Ezio), with Orlok "
            "independently identifying the Talisman of Mao as the "
            "anomaly's source and Sephtis confirming it -- still "
            "undisclosed to Kanja; Book 4, the Sephtis-Kanja conversation "
            "that reveals the Talisman's autonomous operation, the "
            "Blueprint Eye reading that closes the Kanja 'Gap' (MCD-200), "
            "and the first Val Mirel contact via Sephtis's broker "
            "protocol (MCD-198), opening the deferred Verith question "
            "(MCD-180); Book 5, her highest sustained combat of her life, "
            "and the discharge of her standing operational debts -- the "
            "Drowning Vault's 120 released and the cave-system "
            "populations revived -- forming the foundation of Cian's "
            "post-T.D.K. Karesian population."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-217",
        "category": "World Mechanics",
        "statement": (
            "The chronicle frames Lauris as 'a chapter of the world, "
            "walking': the personal-scale echo of the Talisman of Mao's "
            "planetary hardening (MCD-208) -- when her body hardens "
            "against a sustained engagement, it previews in miniature "
            "what the Foundry Anvil mechanism is doing to Cian's crust. "
            "As of Book 1's present-day, she is roughly 4,000 years old "
            "with roughly 96,000 years of expected lifespan remaining, "
            "consistent with the already-locked ~100,000-year Karesian "
            "lifespan (MCD-148). The chronicle is treated as an open, "
            "continuing documentation project rather than a closed "
            "biography."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full draft as pasted in-conversation, closing Section VI of the World Adaptation Blueprint (Eras A through H) in its entirety: "lock it. roadmap update"'


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
            "batch": 38,
            "source_doc": "World_Adaptation_Blueprint (Section VI, Era H: Synthesis -- closes the Lauris Letitia Chronicle, Eras A-H complete)",
            "source_id": "1L89Y-CxdnRPmQoDLEUHD2viTcSLoB11rFC72KT7UZJA",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "4.1"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
