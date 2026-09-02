#!/usr/bin/env python3
"""Batch 43: Character Codex physiology gaps -- Orlok's Kingdoms of Merak
backstory, and deeper physiology for the Triad Guardians (Varkul/Sorya/
Varruk) and five thinly-locked crew members (Damu, Abyss, Matar, Cooper,
Valeria Korth)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "'LORDS_OF_CIAN_Character_Codex_definitive.docx' (Google Drive fileId "
    "1gpcyrEhLybY9uZluuXB-A1g4t5e7zygn, Lore Vault) -- the full local copy "
    "fetched during Batch 27's approval pass (scratchpad codex.txt) was "
    "re-searched for the specific gaps flagged then and left untouched: "
    "Orlok's Character Codex Entry #30 (Sections III/III-B, his origin and "
    "'What Orlok Knows: The Kingdoms of Merak'), and Character Codex "
    "Entries #25-29 plus the Triad Guardians' individual entries (Drown-"
    "Warden Varkul, Sorya, Varruk, Damu/Julian Dael-Koss, Abyss/Ren Oshaal, "
    "Matar, Cooper/Ronan Kellsward, Valeria Korth), whose existing CC- "
    "rules (CC-049/050/051/064-069) capture only a one-line identity/"
    "capability summary each. This batch adds the deeper physiology, "
    "origin, arsenal, and bond-mechanics detail beneath those summaries. "
    "Deliberately excluded as out of scope for a physiology pass: alias "
    "lists, narrator-voice prose ('how narrators describe X'), and "
    "personality/key-phrase material -- that content belongs with the "
    "Voice Bible rules, not the fact ledger. The Anansi/Valeria sibling "
    "secret recurs in Valeria's entry but was already locked (CC-090 area) "
    "before this batch and is not relocked here. Collision-checked before "
    "drafting: Thread-Kin, Cruor-Kin cross-reference to Bloodreaver, Mercy "
    "Draught, Red Index, the Needle, the Apothecary, the Weaver's Kit, "
    "Cooper's Hook, and Fifth Seat are all new terms with no existing "
    "ledger collisions. The Kingdoms of Merak deep-lore (the Purge "
    "methodology, the Shattering, the Ever-Haunt's pre-Merak origin) "
    "extends the already-locked CC-057 without contradicting any locked "
    "fact about the Warbody, the Ionic Rite, or Lady Vestige's division."
)

NEW_RULES = [
    {
        "id": "CC-091",
        "category": "character-orlok",
        "statement": (
            "Orlok was born a miner's son at a volcanic-ridge Dominion "
            "extraction site (later the Celestial Zenith's territory), "
            "self-taught his density manipulation from childhood by "
            "striking rock and noticing the marginal effect, and spent "
            "all 76,003 years since deepening it with no institutional "
            "training. He presented himself at the Sovereign Pavilion's "
            "assessment hall roughly 3,000 years ago, was granted the "
            "Fifth Seat, held it 1,400 years, and resigned because his "
            "methodology -- built from a single body's relationship with "
            "density over millennia -- could not be taught to anyone "
            "else. Extends CC-058."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-092",
        "category": "character-orlok",
        "statement": (
            "The Purge of the Kingdoms of Merak (extends CC-057): T.D.K.'s "
            "elimination of the Merak rulers over an estimated 30,000-"
            "40,000 years used a consistent methodology -- direct "
            "confrontation (developing and refining the Warbody against "
            "Merak-tier opponents), containment (the Ionic Rite's "
            "methodology, built specifically to hold beings of Merak-tier "
            "capability), and perception warfare (the lineage behind Lady "
            "Vestige's division turning rulers against each other) -- and "
            "discriminated purely by threat level, eliminating "
            "benevolent, malevolent, and indifferent rulers alike because "
            "any uncontrolled variable was a target."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-093",
        "category": "character-orlok",
        "statement": (
            "The Shattering, Orlok's survival, and the Ever-Haunt: after "
            "the Merak rulers fell, T.D.K. targeted the next generation "
            "of anomalies -- individuals whose capability approached "
            "Merak-tier. Orlok survived only because he had no kingdom, "
            "no allies, and no institutional footprint, making him too "
            "unimportant to target until ignoring him cost less than "
            "eliminating him -- the one strategic miscalculation Orlok "
            "has identified in T.D.K.'s otherwise systematic purge. The "
            "remaining shattered populations became the five nations; "
            "'Shattered Kingdoms' names this ancient event, not the Old "
            "Dominion's collapse (consistent with CC-057). Orlok's own "
            "theory, revealed gradually across Books 2-5: the Ever-Haunt "
            "predates the Kingdoms of Merak itself, and T.D.K.'s command "
            "over them is tolerance rather than domestication -- a "
            "compliance that could revert if his direction ever "
            "conflicted with their nature."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-094",
        "category": "character-triad",
        "statement": (
            "Drown-Warden Varkul's dual morphology: Land Form (~4,025 "
            "lbs, 12.6 ft) fights via blunt-force mass displacement "
            "rather than mauling, tracks by scent-first acquisition, and "
            "generates the Harrow Presence -- an instinctive discipline-"
            "collapse effect on nearby groups that the SBD misclassifies "
            "as frequency-craft but is pure biology. Hydro-Titan Form "
            "(88% size increase on submersion, ~7,567+ lbs minimum, 23.7 "
            "ft) adds Hydro-Inertia (near-unstoppable momentum), the "
            "Breach (full-body aerial strikes from water), Snap-Turn, "
            "Wake Distortion, and the Living Depth Charge (mass-"
            "displacement swamping). Both forms are natural adaptive "
            "responses to habitat, not a shapeshifting power (extends "
            "MCD-020)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-095",
        "category": "character-triad",
        "statement": (
            "Varkul's bond and vulnerabilities: the Pyro Bond manifests "
            "in Varkul as Indomitable Will -- refusal to acknowledge pain "
            "or fatigue, sustaining engagement beyond any standard "
            "organism's biological limits. Hierarchy: Pyro first, ship "
            "second, crew third. Vulnerable to Blight Frequencies "
            "(disrupt the Hydro-Titan expansion and Harrow Ring "
            "formation), Abyssal Bile-Salts (suppress the bond's "
            "override of pain/fatigue), and extended separation from "
            "Pyro (non-lethal but increasing biological strain)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-096",
        "category": "character-triad",
        "statement": (
            "Sorya's morphology and capabilities: 15% larger than "
            "Panthera atrox (~1,150-1,300+ lbs, 13.2 ft, melanistic coat "
            "with rosettes visible only in direct light, emerald eyes). "
            "Six capabilities: Witness-Scouting (eidetic sensory recall "
            "across all input channels), Vow-Taste (physically senses a "
            "broken vow as a sensory signature, before the betrayer "
            "acts), Shard-Recall (projects sensory memory-fragments "
            "directly into a target's mind as evidence delivery, not "
            "telepathy), Mimic Speech (reproduces isolated overheard "
            "phrases in the original speaker's exact voice), Long-Haul "
            "Endurance, and Stealth-Dominance (silent despite exceeding "
            "1,000 lbs)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-097",
        "category": "character-triad",
        "statement": (
            "Sorya's Binding and vulnerabilities: her deepest loyalty is "
            "to the Oath itself, not to Pyro or the ship -- hierarchy is "
            "Pyro first, the Oath second, ship third, except that if Pyro "
            "and the Oath ever conflict, the Oath wins; this is the only "
            "scenario where her Pyro-loyalty bends, and if anyone "
            "(including Kanja or Pyro) breaks a sworn vow, she becomes "
            "the instrument of correction. Vulnerable to Blight "
            "Frequencies (degrades Witness-Scouting/Vow-Taste) and "
            "Abyssal Bile-Salts (stalls Shard-Recall's delivery, not the "
            "memory itself); the Oath Paradox -- two valid, conflicting "
            "oaths -- is the only thing that breaks her operational calm."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-098",
        "category": "character-triad",
        "statement": (
            "Varruk's morphology and capabilities: 15% larger than "
            "Argentavis magnificens (~195 lbs, 27.6 ft wingspan, hollow-"
            "bone build, the lightest of the Triad by design rather than "
            "weakness). Five capabilities: Pattern-Scouting (reconstructs "
            "a complete strategic picture from fragmentary observation), "
            "Angle-Whisper (projects compressed geometric certainty -- "
            "not words or images -- directly into a bonded mind), "
            "Cadence Ruin (disrupts enemy coordination via low-altitude "
            "passes and targeted-frequency screams), Storm-Lane Travel "
            "(navigates hurricane-force weather as express routes), and "
            "Guidance by Refusal (communicates danger by refusing to "
            "land on or fly a given path, never by warning)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-099",
        "category": "character-triad",
        "statement": (
            "Varruk's bond and vulnerabilities: the Pyro Bond manifests "
            "in Varruk as navigational certainty -- he always knows the "
            "safest (not fastest) path to Pyro, and is the most visibly "
            "bonded of the Triad in daily life (constant overwatch rather "
            "than hovering). Hierarchy: Pyro first, pattern second, ship "
            "third -- he will abandon a reconnaissance mid-flight if Pyro "
            "is threatened. Vulnerable to Blight Frequencies (degrades "
            "Pattern-Scouting/Angle-Whisper), is functionally grounded in "
            "enclosed spaces (his capabilities need open sky/water), and "
            "Cadence Saturation (self-limiting: overuse of his own "
            "frequency projection causes disorientation via reverberation "
            "in his own hollow bones)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-100",
        "category": "character-crew",
        "statement": (
            "Damu (Julian Dael-Koss), deeper physiology: his Cruor-"
            "Variant blood-spectrum sensitivity reads a person's complete "
            "physiological state through blood contact as felt sensation "
            "(not visual or verbal), distinguishing 200+ specific "
            "conditions with accuracy exceeding Trust medical "
            "instruments; age ~190, baseline-adjacent density ~80x, not a "
            "combatant by mass. Recruited from an unlicensed Cruor-Kin-"
            "community medical practice during the Long Mask's second "
            "century after Bloodreaver (whose own Cruor-Kin biology let "
            "him recognize what Julian's ability was) brought him to "
            "Kanja, who confirmed him by having Julian read his own "
            "biology and detect the Talisman's Internal Quench on "
            "contact. Arsenal: the Surgeon's Belt (Kanja-forged cellular-"
            "precision instruments), the Mercy Draught (a Dhar-Kael-"
            "cartilage-derived compound accelerating natural healing by "
            "~300%), and the Red Index (his 150-year personal diagnostic "
            "archive, the most comprehensive biological database outside "
            "the SBD's classified holdings)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-101",
        "category": "character-crew",
        "statement": (
            "Abyss (Ren Oshaal), deeper physiology: his Negative-Density "
            "Variant biology generates a localized gravitational-pressure "
            "field -- passive (~5m radius, +30% gravitational load), "
            "active (~15m radius, +200% load), and the Depth-Charge "
            "(field compressed to ~1m, approximating deep-ocean crush "
            "pressure, costing ~6 hours' recovery). Age ~45 (the crew's "
            "youngest member), personal density ~150x, carries no "
            "weapons -- his field is his arsenal, moderated by Kanja-"
            "built Dead Drakma gravitational-compensator boots and a "
            "field-moderating mesh vest for close proximity to allies. "
            "Origin: a deep-ocean pressure-adapted community on the "
            "Jicome continental shelf; sent to the surface at 16 after "
            "his field's output exceeded his settlement's structural "
            "tolerance at 14; recruited by Sephtis."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-102",
        "category": "character-crew",
        "statement": (
            "Matar, deeper physiology: standard (non-variant) human "
            "biology operating at 800x purely through discipline and 600 "
            "years of conditioning -- no augmentation, no exotic "
            "biology. Age ~620. His termination methodology is extended "
            "target study followed by a single sub-ten-second engagement, "
            "switching to environmental/chemical methods (poison, "
            "structural sabotage) against targets above his density "
            "range rather than direct confrontation. Arsenal: the Needle "
            "(a 20cm, mono-molecular-edge Dead Drakma stiletto) and the "
            "Apothecary (a case of density-calibrated toxins/sedatives "
            "refined over six centuries). Brought to the crew by Sephtis "
            "roughly 400 years ago with no further explanation of his "
            "origin, extending CC-067."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-103",
        "category": "character-crew",
        "statement": (
            "Cooper (Ronan Kellsward), deeper physiology: his Mass-"
            "Compression Variant biology absorbs external mass through "
            "sustained physical contact, temporarily raising his density "
            "-- resting ~200x, up to a documented ~4,500x maximum after "
            "prolonged contact with Living Drakma ore, bleeding off at "
            "roughly 10% per hour without renewed contact. Age ~180. "
            "Origin: a Jicome dock laborer paid as a single unit of labor "
            "despite tenfold output; recruited by Anansi specifically for "
            "logistics expertise rather than combat capability. Arsenal: "
            "the Manifest (the crew's master supply ledger -- caches, "
            "routes, safehouses) and the Cooper's Hook (a Dead Drakma "
            "cargo hook that becomes a mass-augmented weapon when he's "
            "loaded to Branded-class density)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-104",
        "category": "character-crew",
        "statement": (
            "Valeria Korth, deeper physiology: her Thread-Perception "
            "Variant biology (Thread-Kin community stock, the same clade "
            "underlying Anansi's web-manipulation trait, already locked "
            "as siblings) perceives structural and causal connections as "
            "visible threads rather than modifying them, letting her "
            "identify the single point that unravels a locked room, a "
            "siege formation, or a chain of events. Age ~210, density "
            "350x. Has survived three separate SBD containment attempts, "
            "each time escaping by reading the cell's structural failure "
            "mode the designers hadn't anticipated. Arsenal: the Weaver's "
            "Kit (structural-manipulation escape tools) and the Compass "
            "Needle (a small dagger reserved for cutting the single "
            "obstructing 'thread' -- rope, wire, tendon -- blocking an "
            "escape route; used 73 times in 210 years)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad approved the full 14-rule draft as pasted in-conversation: "looks good"'


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
            "batch": 43,
            "source_doc": "LORDS_OF_CIAN_Character_Codex_definitive.docx (Orlok's Kingdoms of Merak backstory, and deeper physiology for the Triad Guardians and five thinly-locked crew members)",
            "source_id": "1gpcyrEhLybY9uZluuXB-A1g4t5e7zygn",
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "4.6"
    ledger["last_updated"] = "2026-09-02"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
