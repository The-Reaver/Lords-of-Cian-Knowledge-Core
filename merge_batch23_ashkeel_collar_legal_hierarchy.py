#!/usr/bin/env python3
"""Merge Batch 23 into canon-ledger.json: Ashkeel, collar/legal hierarchy and the Basalt Codex."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'Guild of the Extraordinary' (Google Drive fileId "
    "1cGEqnWXfUZOGSVksys32TSQninqSI_fWZ0LC7fSUGXM), Part 1 ('Social Order: The Dual-Identity "
    "Hierarchy' and 'The Mandate of the Iron Collars') and Part 5 ('COUNCIL OF ASSASSINS // "
    "HIGH JURISPRUDENCE OF THE FLESH', the Basalt Codex). Same source document as Batches 19 "
    "and 22. House Thorne translated to House Kestrion throughout, matching ASH-014's already-"
    "locked rename (confirmed independently by ASH-015's description of Kestrion governing "
    "arbitration/Iron Collar command, matching this material's Bladeless Court role). "
    "Recruitment age drafted at the already-locked ASH-016 baseline of thirty, not the source "
    "document's uncorrected 'ages of 16 and 22' (a child-safety issue, corrected in "
    "conversation 2026-08-25; superseded once the age-30 floor confirmed it did not apply). "
    "'The Sanctuary of Cian' renamed to 'the Sanctuary of Ashkeel' per Abad's naming "
    "correction, 2026-08-25."
)

NEW_RULES = [
    {
        "id": "ASH-031",
        "category": "Ashkeel",
        "statement": (
            "Ashkeel's citizenry is stratified into four registered statuses layered on top of "
            "the Council of Strikers' seven-seat structure (ASH-012): the Council of Strikers "
            "itself, acting as high priests and grand magistrates whose rulings on contract "
            "breach or ritual heresy are instant and final; the Dominus Class (patrons and "
            "house heads, expected to demonstrate mastery and self-control, cruelty without "
            "consent or control is a demotable offense); the Pledged and Devotees (those in "
            "voluntary structured service, granted sanctuary, care, and legal protection in "
            "exchange); and the Iron Collars (ASH-016), the masked enforcer corps ensuring "
            "public decorum and instant dispute arbitration."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-032",
        "category": "Ashkeel",
        "statement": (
            "Ashkeel's habitable structure is organized into four vertical tiers, each with a "
            "distinct civic function: the Obsidian Spires (+12,600 to +5,000 ft), housing the "
            "Council chambers and high temples; the Grand Promenade and Ateliers (+5,000 ft to "
            "sea level), the civic sphere of baths, plazas, and artisan foundries; the Velvet "
            "Labyrinths (sea level to -30,000 ft), private house estates and sensory lounges; "
            "and the Iron Crucible (-30,000 to -75,000 ft), the martial academies, blood-pact "
            "archives, and power cores."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-033",
        "category": "Ashkeel",
        "statement": (
            "Three laws of transgression enforce Ashkeel's founding consent principle (ASH-011, "
            "ASH-021) at street level: the Inviolable Safe-Sign (ignoring a cessation signal is "
            "Blood Treachery, punished by stripped rank and Council trial); the Sanctuary of "
            "the Neutral Ground (unsolicited physical contact in public spaces without prior "
            "registered dynamic or formal greeting means banishment); and the Rite of Grievance "
            "(unresolvable disputes between Dominus-tier citizens go before the Council for "
            "arbitration or ritual combat to submission in the Obsidian Ring, never street "
            "warfare)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-034",
        "category": "Ashkeel",
        "statement": (
            "Registered status is visibly marked. Collars for the Pledged/Devotee class carry "
            "legal weight: the Iron Torc marks an apprentice or probationary pledge (1-6 month "
            "trial); Burnished Silver marks an established, favored house submissive with "
            "limited negotiating authority; Gold with Gemstone Inset marks a consort of high "
            "station or ritual partner to a Striker or High Dominus, and touching one without "
            "leave costs a hand. Leash-ring placement further specifies role: front sternum "
            "(open/public service), nape-mounted (private house attendance only), or flush/no "
            "loop (ceremonial, fully integrated companion)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-035",
        "category": "Ashkeel",
        "statement": (
            "Public conduct runs on three fixed codes: the Law of the Cloak (touching another "
            "citizen's attire, collar, or skin without explicit negotiation or an active "
            "registered contract is treated as assault on the Sanctuary); the Raised Hand (an "
            "open, closed-fist-to-palm gesture halts all action anywhere in public, with "
            "immediate Iron Collar intervention for violators); and the Masking Rite (the "
            "Lacquered Visor half-mask lets a citizen attend public festivities without "
            "revealing civilian house lineage, at the cost of full subjection to whichever "
            "lounge's house rules apply while masked)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-036",
        "category": "Ashkeel",
        "statement": (
            "Iron Collar recruitment (ASH-016) proceeds through three Weeding Trials once a "
            "candidate reaches the baseline age of thirty: the Labyrinth of Desire (72 hours in "
            "sensory-saturated pleasure chambers under psychoactive stimulants, testing total "
            "non-response, any involuntary engagement disqualifies); the Stone Marrow (a solo "
            "48-hour descent into unmapped geothermal fissures at -60,000 ft, testing spatial "
            "logic and resilience to sensory deprivation); and the Sovereign Severance "
            "(publicly burning family heraldry, dissolving all existing romantic/dynamic "
            "contracts, and surrendering one's given name to the Council archive). Passing "
            "candidates receive an alphanumeric strike-cipher (e.g., Sentry Null-Seven) and a "
            "welded, keyless baseline iron neck-band."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-037",
        "category": "Ashkeel",
        "statement": (
            "Iron Collar martial training runs in the Abyssal Redoubts (-45,000 to -55,000 ft) "
            "across four pillars: close-quarters restraint (the Silent Shackle, joint locks, "
            "pressure points, weighted-silk garrotes); the Shear Arts (twin 14-inch blades, the "
            "Council Shears, trained for surgical precision including clean decapitation "
            "without collateral blood); environmental/zero-visibility combat (blindfolded "
            "sparring in steam vaults and echo chambers); and kinetic endurance conditioning "
            "under high hyperbaric pressure."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-038",
        "category": "Ashkeel",
        "statement": (
            "Psychological conditioning (extending ASH-017) has three named components: the "
            "Still Basin (neuro-linguistic conditioning decoupling stress hormones from heart "
            "rate, an active Enforcer holds 45-55 BPM even mid-combat); the Jurisprudence of "
            "the Flesh (memorizing all ~1,200 articles of the Basalt Codex, including safe-sign "
            "breach definitions across seven cultural dialects); and the Unseeing Eye Protocol "
            "(viewing all physical interactions through a clinical, biomechanical lens "
            "regardless of intensity). Final initiation, the Rite of the Seamless Visor, takes "
            "place before the Council in the Obsidian Spires: a mirror-glass-and-titanium mask "
            "with no eye or mouth openings (internal micro-lenses feed vision directly to the "
            "optic nerve) is fitted, a voice modulator replaces the wearer's natural voice with "
            "a genderless metallic cadence, and the recruit immediately arbitrates a live "
            "dispute, required to name the broken code and execute the statutory penalty within "
            "60 seconds. Standard loadout: the Mirror Visor (biometric HUD), the Locked Gorget "
            "(keyless titanium-basalt neck ring), a composite ballistic-weave shell styled as "
            "skin-tight leather, the Dual Shears, and Cord & Seal Tethers (tungsten garrotes, "
            "magnetic boundary seals). Once masked, an Iron Collar never eats, drinks, or "
            "unmasks in public, and moves the Promenade only in silent, synchronized pairs."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-039",
        "category": "Ashkeel",
        "statement": (
            "The Basalt Codex is Ashkeel's governing legal text (referenced at ASH-030, "
            "ASH-038), formally the 'Council of Assassins, High Jurisprudence of the Flesh.' "
            "Its Section IV governs dynamic-bond contracts (the Official Register of Dynamic "
            "Bonding), filed under jurisdiction of the Sanctuary of Ashkeel. A standard "
            "registration records both parties (Dominus of record and Initiate/Pledged of "
            "record, by name, lineage tier, and station), a fixed term (traditionally three "
            "lunar rotations, renewable), and a hard ceiling of inviolable boundaries the "
            "Dominus may never cross regardless of contract terms: no permanent branding, "
            "scarring, or fracture; no third party introduced without a signed written "
            "addendum; no submersion below Tier IV (-30,000 ft) in uncertified abyssal vents."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-040",
        "category": "Ashkeel",
        "statement": (
            "Two universal safe-signals hold absolute legal force under the Basalt Codex, "
            "breach of either constituting Blood Treachery: the oral tiers 'Amber' (immediate "
            "reduction of intensity, postural check) and 'Obsidian' (total cessation and "
            "immediate aftercare), and the physical closed-fist-to-open-palm gesture, which "
            "carries Obsidian's identical legal weight. A disputed breach is heard within 24 "
            "hours before a House Kestrion Arbitrator in the Bladeless Court; no private "
            "reprisal, duel, or blade-draw is permitted on Sanctuary ground pending that "
            "hearing."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-041",
        "category": "Ashkeel",
        "statement": (
            "Contract elevation from Iron Torc to Silver Collar is a formal rite before the "
            "Council in the Chamber of the Bladeless Court, at the Altar of the First Bond (a "
            "white-marble slab, the only pale stone permitted in the monolith). A House "
            "Kestrion Magistrate confirms both parties hold a clean ledger, then orders the "
            "Iron Torc physically unlocked and removed. An Obsidian Forge-Masters apprentice "
            "presents the Silver Torc (sterling silver and titanium, no front leash-loop, "
            "engraved with the presenting house's sigil), which the Dominus locks onto the "
            "Initiate. A blood-and-bread rite follows: a drop of the Dominus's blood sealed "
            "into the collar's locking mechanism, a bite of honey and salt taken without lips "
            "touching the metal, and a formal address elevating the Initiate to Consort of the "
            "house. This sequence was directly illustrated in the Codex using Lord Corren of "
            "House Vane elevating his Initiate Caelen to Consort, registered and archived by an "
            "Iron Collar scribe (Sentry Null-Nine) in the Black Archives."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-042",
        "category": "Ashkeel",
        "statement": (
            "Silver Consort status (elevation from ASH-041) carries specific legal rights under "
            "the Basalt Codex, Section IV, Articles 102-148: treble-damage protection against "
            "unauthorized third-party contact (automatically prosecuted as Assault on Sanctuary "
            "Sovereign Property, triggering an Iron Collar lethal-arrest warrant); unescorted "
            "movement on all public concourses; and the right to petition a House Kestrion "
            "Magistrate directly at the Bladeless Court, rather than requiring the Dominus to "
            "speak on their behalf. Financially, a Silver Consort holds independent guild "
            "credit (up to 5,000 Obsidian Denarii per lunar cycle without patron co-sign) "
            "across all four chartered Promenade guilds, priority commissioning access, and "
            "restricted apothecary dispensation through House Moros without a script. "
            "Diplomatically, a Consort may cast the house's guild-assembly vote, act as "
            "embassy-recognized proxy, witness probationary contracts, and, when the Dominus is "
            "absent, host foreign ambassadors and seal non-lethal alliances under the house "
            "seal."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Abad ruled the recruitment-age conflict (ASH-016\'s locked 30 vs. his own restated 25) in '
    'favor of the already-locked age: "30 stands, change the word Cian in Sanctuary of Cian" '
    '(interrupting an initial "keep Sanctuary of Cian as-is"), then approved the full draft as '
    'pasted in-conversation: "lock it"'
)


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
            "batch": 23,
            "source_doc": "Guild of the Extraordinary (Ashkeel, collar/legal hierarchy + Basalt Codex)",
            "source_id": "1cGEqnWXfUZOGSVksys32TSQninqSI_fWZ0LC7fSUGXM",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 1,
            "conflicts_resolved": 1,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "2.6"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
