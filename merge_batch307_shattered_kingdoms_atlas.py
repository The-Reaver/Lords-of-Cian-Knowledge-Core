#!/usr/bin/env python3
"""Batch 307: The Shattered Kingdoms Political Atlas -- deep political/military/cultural
detail for all five Shattered Kingdoms nations plus a full Orlok Character Codex extension.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Shattered_Kingdoms_Political_Atlas (Google Drive, Lore Vault) -- a previously-unlogged "
    "document found via a fresh full Lore Vault audit, already partially load-bearing (the "
    "ledger cites it by name at MCD-229's Zenith-Prime note, and CC-059/ARS-384's Zenith-Rod "
    "material derives from it; WC-012 is its own compressed five-nation summary). This batch "
    "extracts the deep political/military/cultural detail and the full Orlok Character Codex "
    "material the earlier compressed extraction never captured."
)

NEW_RULES = [
    {
        "id": "MCD-1850",
        "category": "World Mechanics",
        "statement": (
            "The Verehimu-Aethel-Gard bloodline connection, the mechanism behind WC-012's "
            "'Verehimu bloodline origin ~8,000 years ago' one-liner: the first Verehimu was a "
            "Root-Born Aethel-Gard general who left the nation during a succession crisis "
            "roughly 8,000 years ago and traveled to the Old Dominion's capital territory, "
            "where T.D.K. recognized his military capability and elevated him -- the Crown-Scar "
            "was installed in the Verehimu bloodline during this period. Aethel-Gard has "
            "watched the Verehimu line from the highlands ever since, waiting to see if the "
            "bloodline 'remembers where it came from' -- the standing blood-connection leverage "
            "that buys Ozmund an audience (not an alliance) with the nation in Book 2, extending "
            "CC-127's Elora-Grace/Thane-Gorm commitment."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "POL-101",
        "category": "political-atlas-nation",
        "statement": (
            "Aethel-Gard's government is a Dual Court: a High-Born Sovereign and a Root-Born "
            "Thane ruling side by side, joint edicts requiring both signatures. Wulfaric "
            "('the All-Seer'), ~3,400 years old, is the High-Born Sovereign, an Odin-homage "
            "figure whose intelligence network has watched T.D.K.'s southeastern 'dead ground' "
            "for centuries without confirming what's there. Vult-Gwyn ('the Shadow-Weaver'), a "
            "Loki-homage spymaster of deliberately unconfirmed age/identity (the ambiguity is "
            "operational), runs external intelligence. Extends CC-127's already-locked "
            "Thane-Gorm (the Root-Born Thane half of the same Dual Court) and WC-012."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "POL-102",
        "category": "political-atlas-nation",
        "statement": (
            "The Obsidian Prefecture's government is an oligarchic Senate of Twelve Patriarchs "
            "(POL-040) whose legal system enforces familial obligation as binding law across "
            "generations, giving the Senate leverage over every citizen's inherited debts. Voss "
            "Labyrinth (Jupiter homage), ~2,800 years old, was First Patriarch and Senate "
            "chairman for a long predecessor tenure before the seat passed to the already-"
            "locked Severin Ebonrath (POL-100) -- his institutional-founder status is real "
            "Prefecture history, not a competing claim on the current seat. Dhampir Black (Mars "
            "homage), Fourth Patriarch and the Prefecture's military commander (~1,600 years "
            "old, 2,200x density), controls the legionary command structure. Iron-Gore (Vulcan "
            "homage), Tenth Patriarch and Chief Engineer, controls the roads/aqueducts/"
            "fortifications/siege-weapon infrastructure that gives the Prefecture's "
            "200,000-strong legionary army its reach."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "POL-103",
        "category": "political-atlas-archipelago-houses",
        "statement": (
            "The Astral Archipelago's floating islands (Living Drakma deposits in the geology "
            "producing buoyancy through tidal resonance) and fixed volcanic islands are "
            "governed by the Council of Crossroads through consensus (at least six of nine "
            "seats must agree before any action). Star-Bloom (Erzulie/Oshun homage), ~1,400 "
            "years old, holds the Third Seat (domain: health and love, treated as one domain) "
            "and is the Council's most diplomatic voice, most likely to advocate answering the "
            "Rexmar debt (POL-104). The Archipelago's naval superiority comes from ships built "
            "of Living Drakma-infused timber, navigated by a resonance sense non-natives cannot "
            "replicate -- the Archipelago has never been successfully invaded by sea. Extends "
            "POL-095/096/WC-012; deliberately does not address how the Council's other seats "
            "(including the still-open Master Void-Cusp/Event Horizon question) relate to the "
            "Marlunar/Marvault/Marossen hereditary seats."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "POL-104",
        "category": "political-atlas-rexmar-origin",
        "statement": (
            "The Astral Archipelago's 'standing Rexmar debt' (WC-012) is a felt-not-understood "
            "obligation the Council of Crossroads has carried since its founding: 'when the "
            "Rexmar come, we answer.' Its most likely true origin (unknown to the Council "
            "itself -- the historical record has gaps too clean to be accidental): during "
            "Haku's war against T.D.K. roughly 5,000 years ago, his campaign liberated Living "
            "Drakma ore from T.D.K.'s vaults, and displaced populations who carried that "
            "liberated ore founded the Archipelago, making the floating islands possible. The "
            "debt is existential, not transactional -- the Archipelago exists because a Rexmar "
            "freed the material that made it possible."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "POL-105",
        "category": "political-atlas-nation",
        "statement": (
            "The Celestial Zenith's government, the Sovereign Pavilion, is purely "
            "meritocratic -- every seat earned through public demonstration of a recognized "
            "discipline, no birthright. The Binary-Architects (Fuxi/Nuwa homage), a bonded pair "
            "functioning as one authority (~4,500 years old each), hold the Second and Third "
            "Seats and designed the Zenith's own infrastructure: the floating monasteries, the "
            "jade-glass forging process, and the cultivation methodology itself -- they are also "
            "the ones who gifted Orlok the Zenith-Rod (CC-143). Mercy-Nebula (Guanyin homage), "
            "Fourth Seat, ~2,100 years old, is the Zenith's chief physician, her cultivation "
            "discipline a biological-diagnosis-through-touch capability comparable in principle "
            "to Damu's blood-reading but cultivated rather than variant biology. Loyalty-Quasar "
            "(Guan Yu homage), Sixth Seat, ~2,800 years old and 3,200x density, is the Zenith's "
            "general, commanding its 8,000 cultivated warriors (average density 1,800-3,000x) "
            "as an integrated system. Extends MCD-229's already-locked Zenith-Prime (First "
            "Seat) and Orlok's formerly-held Fifth Seat."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "POL-106",
        "category": "political-atlas-nation",
        "statement": (
            "The Hollow Shogunate's Parasitic Sovereignty (already locked at POL-070 as the "
            "mechanism Vile-Sire and Hollow-Dam rule through) is now mechanically defined: it "
            "siphons a biological analogue of Living Drakma's Impact Memory property from the "
            "citizenry -- extraction diminishes the source (slower, duller, faster-aging) and "
            "concentrates capability into the rulers and their champions. The Seven Sin-Eaters, "
            "the Shogunate's elite guard (4,000-6,000x density), are manufactured Proven-tier "
            "threats built from thousands of citizens' extracted Impact Memory compressed into "
            "single bodies, not trained warriors -- the moral inverse of the Zenith's "
            "earned-cultivation model. Glare-Tyrant (Amaterasu homage, inverted), ~1,100 years "
            "old, augmented to ~5,500x, commands the Sin-Eaters as the Shogunate's public "
            "enforcement arm. Scourge-Tempest (Susanoo homage), ~800 years old, augmented to "
            "~6,200x, is the Shogunate's solo destruction asset, deployed where the Sin-Eaters' "
            "collective approach can't reach."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "POL-107",
        "category": "political-atlas-lawless-reaches",
        "statement": (
            "The Lawless Reaches' political layer (POL-090, the Rathaan Federation/the Ash "
            "Maw's Trade Council/the Frontier Maw/pirate harbors) is deepened: the Rathaan "
            "Federation is not a warrior culture but a merchant one -- nomadic clans following "
            "seasonal trade opportunity, governed by seasonal elder councils, surviving by "
            "being useful to every Shattered Kingdoms nation and threatening to none. The Ash "
            "Maw's Trade Council manages the border-exchange economy where the five nations' "
            "currencies, the Sovereign Trust's Scrip, and the Reaches' own barter systems "
            "intersect, taking a percentage of every transaction. Kanja's Long Mask fleet "
            "operated from the Reaches' pirate harbors for the full 284 years, some "
            "independent, some Archipelago-affiliated, some built by escaped Cestari."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "POL-108",
        "category": "political-atlas-map",
        "statement": (
            "The Shattered Kingdoms alignment table toward Kanja's and Ozmund's cause, "
            "consolidating and confirming what's already independently locked: Aethel-Gard "
            "neutral with potential to ally, waiting for proof beyond the Verehimu blood "
            "connection (MCD-1850); the Obsidian Prefecture antagonist, its scheduled "
            "territorial expansion into the Lawless Reaches structurally conflicting with "
            "Ozmund's Unchained Kingdom regardless of personal animus; the Astral Archipelago "
            "allied, bound by the standing Rexmar debt (POL-104); the Celestial Zenith allied "
            "through Orlok's earned respect; the Hollow Shogunate antagonist, an ideological "
            "(not merely territorial) mirror-conflict against the Unchained Kingdom's "
            "liberation premise, confirmed Book 3+ per POL-070."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-141",
        "category": "character-orlok",
        "statement": (
            "Orlok's origin: born Root-Born in the Celestial Zenith ~76,003 years ago to a "
            "family of jade-glass miners, with no access to the Pavilion's cultivation "
            "infrastructure. He taught himself density manipulation through pure empirical "
            "practice rather than any recognized methodology, presenting at the Pavilion's "
            "assessment hall at ~age 200 with a capability the masters couldn't replicate or "
            "explain; held the Fifth Seat for 1,400 years, then resigned because his method -- "
            "a relationship between his specific body and density physics -- couldn't be "
            "taught to anyone else. Physically: ~5'7\", lean and wiry, white hair (a cultivation "
            "side-effect, not age), amber eyes that brighten gold during Kinetic Ascension. His "
            "core capability, Density Manipulation, lets him shift his own density in real time "
            "(including asymmetric distribution within his body for rotational momentum); "
            "Kinetic Ascension is his 3-5-second peak state. The Atlas document's own resting/"
            "combat figures (~1,200x/3,500-4,500x) read as an earlier-book baseline preceding "
            "the escalation already locked at MCD-096 (finalized resting 12,000x, combat "
            "16,000-18,000x, ascension 20,000x post-reforge) -- matching the same "
            "across-books-escalation precedent already applied to Sereth Vaul (Batch 46) and "
            "Orlok himself at POL-080."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-142",
        "category": "character-orlok",
        "statement": (
            "Orlok's relationships: with Kanja, mutual recognition between two self-taught "
            "masters of their respective crafts (smithing vs. density manipulation), cemented "
            "by a fourteen-hour first conversation during the Moonvault journey that resolves "
            "nothing and satisfies both; with Ozmund, respect earned through demonstrated "
            "capability rather than granted to a title -- Orlok watches him build the Unchained "
            "Kingdom for three days before offering his staff ('You're building a wall with "
            "your hands. I'm good at walls.'); with Red Beard, combat camaraderie that produces "
            "the first draw of Red Beard's career (Red Beard's attrition-endurance style can't "
            "be calibrated against Orlok's constantly-shifting density) and an immediate "
            "friendship; with the Zenith-Prime, a 2,400-year-running, still-unresolved "
            "disagreement over whether governance requires structure or requires the governed "
            "to be strong enough not to need it -- mutual respect, no concession on either side."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-143",
        "category": "character-orlok",
        "statement": (
            "Orlok joins Kanja and Ozmund during the Moonvault journey (Act II of Book 2, "
            "extending MCD-279), roughly 80 years into independent travel through the Lawless "
            "Reaches after leaving the Pavilion, looking for something that required his full "
            "capability -- the Unchained Kingdom's formation and the Ever-Haunt's deployment "
            "are that something. His tactical role: a mobile strike asset answering threats too "
            "large for a single command to hold, deployed against a Hollow Shogunate Sin-Eater "
            "or a Tier 3 Ever-Haunt breach past the Vigil Standard's perimeter. His staff, the "
            "Zenith-Rod (jade-glass/Dead Drakma composite, already locked at CC-059/ARS-384), "
            "was the Binary-Architects' gift when he earned the Fifth Seat -- the only weapon "
            "in the Zenith's arsenal engineered specifically to survive density-variable combat "
            "stress, and the reason it's endured 2,400 years of his fighting style before "
            "Kanja's later reforge raised its ceiling further."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "lock it."'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == 12, f"expected 12 new rules, got {len(new_ids)}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 307,
            "date": str(date.today()),
            "source": "Shattered_Kingdoms_Political_Atlas (Google Drive, Lore Vault)",
            "rule_count": len(NEW_RULES),
            "note": (
                "A fresh full Lore Vault audit (40 files, cross-checked against all 306 prior "
                "batches) turned up the Shattered_Kingdoms_Political_Atlas document -- "
                "previously unlogged but already partially load-bearing (MCD-229's "
                "Zenith-Prime note and CC-059/ARS-384's Zenith-Rod material both derive from "
                "it; WC-012 is its own compressed five-nation summary). This batch extracts the "
                "deep political/military/cultural detail: Aethel-Gard's Dual Court (Wulfaric, "
                "Vult-Gwyn, extending the already-locked Thane-Gorm) and the Verehimu bloodline "
                "connection's true mechanism (MCD-1850, Crown-Scar installed by T.D.K. ~8,000 "
                "years ago); the Obsidian Prefecture's familial-debt legal system and Twelve "
                "Patriarchs (Dhampir Black, Iron-Gore, and Voss Labyrinth as a predecessor "
                "First Patriarch -- a real naming collision with the already-locked current "
                "First Patriarch Severin Ebonrath, POL-100, resolved per Abad's explicit ruling "
                "'Voss Labyrinth is a predecessor'); the Astral Archipelago's floating-island "
                "geography, consensus government, naval doctrine, Star-Bloom (Third Seat), and "
                "the true mechanism behind its standing Rexmar debt (Haku's war-liberated "
                "Living Drakma, POL-104) -- deliberately leaving the Council of Crossroads' "
                "Master Void-Cusp/Event Horizon seat-structure question open, unresolved "
                "pending a separate ruling; the Celestial Zenith's meritocratic Sovereign "
                "Pavilion (the Binary-Architects, Mercy-Nebula, Loyalty-Quasar, extending the "
                "already-locked Zenith-Prime); the Hollow Shogunate's Parasitic Sovereignty "
                "mechanically defined as Impact Memory extraction, plus Glare-Tyrant and "
                "Scourge-Tempest; the Lawless Reaches' Rathaan Federation and Ash Maw Trade "
                "Council culture/economics; a consolidated five-nation alignment table "
                "(POL-108); and a full Orlok Character Codex extension (CC-141 through "
                "CC-143) -- origin, capability (density figures reconciled against MCD-096 as "
                "an earlier-book baseline, matching the established Sereth Vaul escalation "
                "precedent), relationships with Kanja/Ozmund/Red Beard/the Zenith-Prime, and "
                "his Book 2 role, extending his existing thin CC-059/ARS-384/MCD-096/MCD-229/"
                "POL-080 references. Full cross-check against the live ledger found zero new "
                "proper-noun collisions across all 12 rules. " + BATCH_NOTE
            ),
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate IDs after merge"
    print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
          f"Batches: {len(ledger['batches_completed'])}.")


if __name__ == "__main__":
    main()
