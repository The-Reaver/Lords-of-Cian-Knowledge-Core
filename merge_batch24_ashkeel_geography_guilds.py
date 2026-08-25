#!/usr/bin/env python3
"""Merge Batch 24 into canon-ledger.json: Ashkeel, internal geography and the merchant guilds."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'Guild of the Extraordinary' (Google Drive fileId "
    "1cGEqnWXfUZOGSVksys32TSQninqSI_fWZ0LC7fSUGXM), Part 1 ('The Tiered Terraces of the Grand "
    "Promenade', 'The Four Merchant Guilds of the Spine', 'Social Clubs') and Part 2 ('The "
    "Abyssal Foundation', 'The High Spire'). Same source document as Batches 19, 22, and 23. "
    "'The Apothecaries of Cian' standardized to 'the Apothecaries of the Deep' (the document's "
    "own alternate name for the same guild, also resolving an internal inconsistency). 'The "
    "Redoubts of Cian' renamed to 'the Iron Redoubts'. Per Abad's standing rule, 2026-08-25: "
    "any 'Cian' usage unrelated to Kanja's crew gets renamed."
)

NEW_RULES = [
    {
        "id": "ASH-043",
        "category": "Ashkeel",
        "statement": (
            "The Grand Promenade (informally 'the Obsidian Spine') spans nearly a vertical mile "
            "between +5,000 ft and sea level, carved as concentric amphitheater-steps around "
            "the Downdraft and Updraft air cores. It has three tiers: the Ember Galleries (high "
            "ateliers and salons), the Basalt Strand (the great concourse and grand markets), "
            "and the Baths of Lethe (sub-sea-level hydrothermal complexes). The Spiral Ramp "
            "(the Great Incline) is a 60-foot-wide connecting concourse with brass-inlaid "
            "traffic lanes; the Heliostat Arches funnel genuine daylight down through optical "
            "shafts; the Hanging Gardens of Myrrh are suspended, atmosphere-purifying terraces "
            "along the cavern walls."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-044",
        "category": "Ashkeel",
        "statement": (
            "Four merchant guilds hold Council charters over the Promenade's commerce: the "
            "Guild of the Flushed Tether (ASH-024's master guild for Ars Funis, hide-work, "
            "harnesses, suspension rigging, signature mark a blindfolded serpent); the "
            "Obsidian Forge-Masters (metallurgy, locking torcs, the Silver Torc's makers per "
            "ASH-041, signature mark crossed keys over an anvil); the Weavers of the Veil "
            "(structural corsetry, concealed ballistic apparel, lacquered half-visors, "
            "signature mark a needle piercing silk); and the Apothecaries of the Deep "
            "(alchemy, tonics, aftercare formulations feeding ASH-030's pharmacopoeia, "
            "signature mark a glass vial cradling a crescent moon)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-045",
        "category": "Ashkeel",
        "statement": (
            "Four chartered social clubs anchor Promenade nightlife, each with its own house "
            "rule: the Black Mirror (+4,200 ft, high-society restraint, silent service, no "
            "raised voices); the Gilded Knot (+2,800 ft, suspension-art theater, spectators "
            "barred from touching performers); the House of the Velvet Vise (+1,500 ft, "
            "sensory deprivation and tactile indulgence, mandatory masking at the door); and "
            "the Thermal Baths of Lethe (sea level, geothermal communal recovery, no weapons "
            "or commerce permitted)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-046",
        "category": "Ashkeel",
        "statement": (
            "The Abyssal Foundation (-30,000 to -75,000 ft) is built as isolated concentric "
            "rings of pressure-forged eclogite (ASH-006), nitrogen-buffered from the living "
            "rock, organized into three zones: the Stygian Plazas (-35,000 to -45,000 ft, "
            "staging grounds and dormitories for active Iron Collars and retired Strikers) sit "
            "above the Iron Redoubts (-30,000 ft tier, Iron Collar barracks and trial arenas); "
            "the Silent Cloisters (-45,000 to -55,000 ft, meditation vaults and hyperbaric "
            "recovery cells) match the Abyssal Redoubts training ground already locked at "
            "ASH-037; and the Low Perimeter & Trench Gates (-65,000 to -75,000 ft) anchor the "
            "counter-seismic dampening struts into the continental plate."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-047",
        "category": "Ashkeel",
        "statement": (
            "The Black Archives sit at -52,000 ft, a hermetically sealed obsidian sphere "
            "flooded with argon gas and kept by the Blind Record-Keepers, a cloistered sect of "
            "elder initiates under permanent vows of silence who communicate only by tactile "
            "finger-signing. Three record sets are held there: the Blood Registers (every "
            "active, fulfilled, and breached dynamic contract since the Sanctuary's founding), "
            "the Purge Chronicles (the uncensored history behind the Council's Neutrality "
            "Code), and the Oblivion Seals (the real names and lineages every sworn Iron "
            "Collar surrendered at recruitment, per ASH-036). All three are physically "
            "recorded on the Black Ledger, titanium sheets stamped in cinnabar wax with "
            "lineage signets."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-048",
        "category": "Ashkeel",
        "statement": (
            "The Geothermal Crucible (-70,000 to -75,000 ft) powers the entire monolith via a "
            "closed-loop supercritical-CO2 turbine cycle drawing on 450C mantle-boundary heat, "
            "supplemented by the Archimedes Hydrostatic Siphons (deep crustal water tables, "
            "scrubbed and routed to the Promenade's bathhouses and the Spire's gardens). Waste "
            "heat vents through the central Updraft Core, driving Ashkeel's permanent internal "
            "air-circulation chimney effect. The Obsidian Floodgate (ASH-009) is triggered by "
            "a single physical key held by the Arch-Magistrate in the High Spire: turning it "
            "breaks the thermal expansion collars at -75,000 ft, flooding the lowest levels "
            "with high-pressure brine and steam to scour the interior and seal the monolith "
            "shut against an unrecoverable breach."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ASH-049",
        "category": "Ashkeel",
        "statement": (
            "The High Spire (+5,000 to +12,600 ft) holds four tiers: the Pinnacle of "
            "Retribution (the Council's apex, the Seven High Thrones carved from "
            "garnet-eclogite, and the mechanical Purge Key vault); the Chamber of the "
            "Bladeless Court (+11,000 ft, the physical seat of the arbitration already locked "
            "at ASH-040/ASH-041, all weapons banned on pain of defenestration, its Altar of "
            "the First Bond the same white-marble slab named at ASH-041); the Enclaves of the "
            "Seven Veils (+7,500 to +10,000 ft, extraterritorial embassy compounds under the "
            "same sovereignty rule as ASH-019, bound by what this material calls the Three "
            "Universal Safe-Signs, matching the two oral tiers and one physical gesture "
            "already locked at ASH-040); and the Sky Terraces & Astral Atriums (+6,000 to "
            "+7,500 ft, formal galas and masquerades, including the Golden Hour Atrium's glass "
            "conservatory)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Abad ruled the Black Ledger naming overlap with MCD-023 stays as-is ("keep both, they\'re '
    'different things"), then set a standing rule superseding the earlier per-instance Cian '
    'policy: "anything with Cian that has nothing to do with Kanja\'s crew should be changed." '
    'Approved the full draft as pasted in-conversation: "lock it"'
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
            "batch": 24,
            "source_doc": "Guild of the Extraordinary (Ashkeel, internal geography + merchant guilds)",
            "source_id": "1cGEqnWXfUZOGSVksys32TSQninqSI_fWZ0LC7fSUGXM",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "2.7"
    ledger["last_updated"] = "2026-08-25"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
