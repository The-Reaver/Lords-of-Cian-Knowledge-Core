#!/usr/bin/env python3
"""Batch 46: follow-up extraction from the full-scope audit -- six
previously-unaccounted-for Lore Vault documents. Talisman of Mao (mostly
confirms locked material, one new fact), Ever_Haunt_Expansion_v3.2 (new
countermeasure mechanism), SBD Executive Director A.M. Directives (new
institutional protocol), Book2_Structural_Outline_Champions (Book 2
structure + full Five Champions profiles), 09_Anirak_Psychological_Profile
standalone (new character mechanism), and the MRD_CultDossiers file-identity
check (resolved clean, no new material -- confirmed duplicate of the
already-processed 'Weighing Communities' source, no batch entry needed for
that item)."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE_TALISMAN = (
    "'Talisman of Mao' (Google Drive, standalone doc, Lore Vault) -- reads "
    "as the origin source for most of the already-locked Talisman "
    "mechanics (Sovereign Umbrella, Grounded Bastion, Internal Quench and "
    "their named sub-functions across MCD-060/061/142 and the Long Mask "
    "Chronicles batches); consistent throughout, one genuinely new fact "
    "extracted. The document's embedded pseudo-physics equations are "
    "flavor text, not canon. Its repeated '16 Avatars' framing is the "
    "known pre-correction undercount already resolved in the Trust's "
    "favor by MCD-140 (19 Avatars)."
)

SOURCE_EVERHAUNT = (
    "'Ever_Haunt_Expansion_v3.2' (Google Drive, Lore Vault) -- a detailed "
    "companion document to the one-paragraph Ever-Haunt summary already "
    "locked at WC-019, adding named crew countermeasure tactics and the "
    "Green Mark contamination's removal mechanism."
)

SOURCE_SBD = (
    "'SBD Executive Director A.M. Directives' (Google Drive, Lore Vault) "
    "-- internal SBD correspondence concerning the Triad Guardians "
    "(Varkul, Varruk, Sorya). Both named figures in it (Executive "
    "Director A.M., Grave-Analyst Abbott Gage) are already-locked "
    "characters, not new; the new material is institutional protocol."
)

SOURCE_BOOK2 = (
    "'Book2_Structural_Outline_Champions.docx' (Google Drive, Lore Vault) "
    "-- Book 2's three-act structure plus full profiles for all of "
    "T.D.K.'s Five Champions, previously locked only as names and "
    "divisions at WC-018. One real conflict surfaced and resolved by "
    "Abad: this document states Sereth Vaul's density as 900x, "
    "contradicting the already-locked 9,500x (Batch 39). Abad's ruling: "
    "both stand, at different points in time -- 900x at the Great Breach "
    "(freshly reactivated, early Ever-Haunt symbiosis), escalating to the "
    "already-locked 9,500x by the time of his 314-year Karkosa operation "
    "(a later-book timeframe), reflecting deepening symbiotic "
    "integration. Mirrors the Orlok Book 2 baseline / later-book upgrade "
    "precedent at POL-080. General Baryon's 'exact measurement "
    "classified' framing here is the same kind of period-appropriate "
    "mystery, not a conflict with his already-locked 22,000x. This "
    "document's spelling 'Lauris Leatia' is normalized to the "
    "already-locked Letitia, per the established document-internal-"
    "spelling-drift precedent (Karren/Korren Highlands)."
)

SOURCE_ANIRAK = (
    "'09_Anirak_Psychological_Profile.docx' (Google Drive, Lore Vault, "
    "standalone -- confirmed NOT included in the All_Psychological_"
    "Profiles.zip processed in Batch 44, so genuinely unread until this "
    "batch) -- companion document to Character Codex Entry #18."
)

NEW_RULES = [
    {
        "id": "MCD-278",
        "category": "World Mechanics",
        "statement": (
            "The Grounded Bastion (Stage 2 of the Talisman of Mao) serves "
            "a dual purpose beyond managing Kanja's own Aethelgard "
            "energy: it also responds to a planetary structural strain "
            "caused by Titans -- Vargo Vakas, Anu Un Ra, and other dense "
            "beings, 'some yet to be released' -- who have been "
            "straining the world's structural integrity for roughly a "
            "thousand years despite prior reinforcement efforts."
        ),
        "status": "locked",
        "source": SOURCE_TALISMAN,
    },
    {
        "id": "MCD-279",
        "category": "World Mechanics",
        "statement": (
            "Book 2's premise: the Great Breach (Book 1 epilogue) "
            "activates T.D.K.'s legacy dependencies, collapsing the "
            "Ever-Haunt's containment kennels and giving the Five "
            "Champions their first operational directives in millennia. "
            "Three-act structure: Act I, Ozmund builds the Unchained "
            "Kingdom in the Shattered Kingdoms while Kanja stabilizes "
            "post-Pi-Awakening at sea, ending with the Ever-Haunt's "
            "arrival at the Kingdom's perimeter as a signal, not an "
            "attack. Act II, the Moonvault journey and the Ten Gifts' "
            "forging, while Sereth Vaul hunts Lauris and Lady Vestige "
            "destabilizes the Sovereign Trust. Act III, the Five "
            "Champions' first open war: Baryon's march against the "
            "Unchained Kingdom (repelled), Kanja's naval engagement "
            "against Ever-Haunt forces redirected toward the Foldtide, "
            "and Bolo Troth's attempt to retrieve Archon Meridian "
            "colliding with Ezio's investigation. Book 2 ends with "
            "Ezio's discovery that the Crown-Scar is a root-access "
            "tether T.D.K. could reactivate to seize direct control of "
            "Ozmund's mind -- the door, not just the code."
        ),
        "status": "locked",
        "source": SOURCE_BOOK2,
    },
    {
        "id": "MCD-280",
        "category": "World Mechanics",
        "statement": (
            "General Baryon (extends the already-locked 22,000x "
            "density): a living being, not undead, sustained ~18,500 "
            "years through the same Exchange Protocol degradation/"
            "maintenance cycles that sustain Anu Un Ra himself "
            "(corroborating CULT-004/CULT-194) -- he is MAINTAINED, not "
            "immortal, and requires periodic centuries-long dormancy. "
            "Book 2's 'exact measurement classified' framing is "
            "period-appropriate mystery, not a contradiction of his "
            "later-revealed density, following the same pattern as "
            "Orlok's Book 2 baseline (POL-080). In Book 2 he commands "
            "T.D.K.'s conventional military assets against the Unchained "
            "Kingdom and loses -- not from being outmatched, but because "
            "Ozmund's Karesian-hardware command architecture was built "
            "to counter exactly his doctrine."
        ),
        "status": "locked",
        "source": SOURCE_BOOK2,
    },
    {
        "id": "MCD-281",
        "category": "World Mechanics",
        "statement": (
            "Sereth Vaul ('the Silencer'): a mortal tracker whose "
            "biology was rewritten by prolonged Ever-Haunt exposure, "
            "carrying the Green Mark permanently as stable symbiotic "
            "integration rather than progressive contamination -- the "
            "only being who can walk inside an Ever-Haunt Anti-Resonance "
            "field and remain functional. His density was 900x at the "
            "Great Breach (freshly reactivated); it escalates to the "
            "already-locked 9,500x by the time of his 314-year operation "
            "against the Karkosa (a later-book timeframe), reflecting "
            "deepening symbiotic integration rather than a contradiction "
            "-- per Abad's explicit ruling. In Book 2 he hunts Lauris "
            "Letitia (spelling normalized from this document's "
            "'Leatia'), plus the Verehimu bloodline and reclaimed SBD "
            "assets, and separately redirects Ever-Haunt naval forces "
            "toward the Foldtide's Living Drakma resonance to test Kanja "
            "post-Awakening."
        ),
        "status": "locked",
        "source": SOURCE_BOOK2,
    },
    {
        "id": "MCD-282",
        "category": "World Mechanics",
        "statement": (
            "Lady Vestige ('the Mirages'): not a combatant but an "
            "institutional perception-warfare specialist, operating "
            "entirely through physics -- engineered optics, acoustic "
            "warfare, and physical document/communication manipulation "
            "-- never through frequency-craft or illusion-as-mysticism. "
            "Her power is unmeasured because every assessment attempt is "
            "itself compromised by her perception field. In Book 2 she "
            "destabilizes the Sovereign Trust's government to redirect "
            "its military resources away from the Shattered Kingdoms, "
            "clearing the operational space for Baryon's campaign "
            "without ever being identified as the cause."
        ),
        "status": "locked",
        "source": SOURCE_BOOK2,
    },
    {
        "id": "MCD-283",
        "category": "World Mechanics",
        "statement": (
            "Lord Varro Dominael ('the Crownless Marshal,' already "
            "locked as formerly Varro Kharas): executed roughly 20,000 "
            "years ago for opposing T.D.K., then reanimated via "
            "death-tech (neural residue mapping, bioelectric harvesting, "
            "structural reconstruction -- physical process, not "
            "mysticism) into a compliant instrument despite retaining "
            "conscious awareness and hatred of T.D.K.; the compliance is "
            "engineered at the biological level, overriding volition. "
            "Commands the Crownless Host, an army of similarly "
            "reanimated soldiers replenished from any battlefield it "
            "crosses. In Book 2 his Host serves as Baryon's vanguard "
            "against the Unchained Kingdom, a deliberate moral mirror to "
            "the freed-Cestari army it fights."
        ),
        "status": "locked",
        "source": SOURCE_BOOK2,
    },
    {
        "id": "MCD-284",
        "category": "World Mechanics",
        "statement": (
            "Bolo Troth ('the Post-Thren'): T.D.K.'s newest champion, "
            "appointed after Nadea Thren's defection dissolved the "
            "Mirrored Chorus division -- a replacement chosen for "
            "availability and loyalty, not capability. Roughly 450 years "
            "old, 4,200x density, an asset-retrieval specialist rather "
            "than an assassin or general. In Book 2 he's sent to "
            "retrieve Archon Meridian before Archon can discover his own "
            "parentage, and his operation collides with Ezio's "
            "investigation, since Archon sits at the center of the "
            "institutional connections Ezio is tracing."
        ),
        "status": "locked",
        "source": SOURCE_BOOK2,
    },
    {
        "id": "CULT-197",
        "category": "ever-haunt-countermeasures",
        "statement": (
            "A coordinated Ever-Haunt countermeasure floods an entity's "
            "Anti-Resonance field with competing frequencies from three "
            "simultaneous sources, forcing it to flee or collapse to its "
            "lowest tier: Onyx's Cadence Ruin, Sephtis's Chrono-Anchor "
            "bells, and Ironbane's King's Roar. A separate light-"
            "vulnerability toolkit (Ironbane's bio-electric discharge, "
            "Pyro's thermal flash-heating, Anirak's Lantern-Star strobe "
            "mode) causes involuntary dispersal in lower tiers and "
            "degraded function in higher ones. Extends WC-019."
        ),
        "status": "locked",
        "source": SOURCE_EVERHAUNT,
    },
    {
        "id": "CULT-198",
        "category": "ever-haunt-countermeasures",
        "statement": (
            "The Ever-Haunt's Green Mark contamination (the tracking-"
            "beacon effect placed on a marked target) can be suppressed "
            "but not cured by sustained high-intensity resonance "
            "exposure -- Ironbane's discharge, Pyro's thermal output, or "
            "contact with actively self-repairing Living Drakma; full "
            "removal requires severing the specific Ever-Haunt that "
            "placed the mark. The original containment method (still "
            "used, inherited without understanding by the SBD) is "
            "resonance-loop 'kennels': an entity's own frequency "
            "sustains the standing wave that traps it. Extends WC-019."
        ),
        "status": "locked",
        "source": SOURCE_EVERHAUNT,
    },
    {
        "id": "CULT-199",
        "category": "sbd-protocol",
        "statement": (
            "The SBD's internal protocol for documenting the Triad "
            "Guardians (Varkul, Varruk, Sorya) enforces a 'Stone, Iron, "
            "Meat' lexicon banning modern-technology metaphors (radar, "
            "telepathy, electronics) as a category error, since the "
            "Guardians operate on principles incompatible with SBD "
            "technology. A parallel 'Continuity Lock' directive strips "
            "proper names from all classified fileline titles going "
            "forward, producing a 'Double-Blind' archive where even "
            "cleared archivists are meant to eventually forget the "
            "entities' true names."
        ),
        "status": "locked",
        "source": SOURCE_SBD,
    },
    {
        "id": "CULT-200",
        "category": "sbd-protocol",
        "statement": (
            "The SBD tracks its own institutional uncertainty via the "
            "Oracle Conflict Map, six domains (Demaron Ingress "
            "Mechanism, Vessel Termination Necessity Logic, Triad Bond "
            "Mechanics, Harrow Ring Clause Conditions, SBD Obfuscation "
            "Viability, Non-SBD Architecture Depth) checked against "
            "reality by a sealed Oracle network. A 'Conflict Flag = YES' "
            "result -- meaning reality has contradicted an SBD "
            "assumption -- triggers the 'Tighten' posture: all "
            "direct-contact testing frozen, spoken names suspended in "
            "favor of code-designations, and the underlying incident "
            "permanently held open, never closed."
        ),
        "status": "locked",
        "source": SOURCE_SBD,
    },
    {
        "id": "CC-112",
        "category": "character-crew",
        "statement": (
            "Anirak's Siren (bioluminescent violet eyes) is an always-on "
            "biological effect, not a deployable ability -- every person "
            "who looks at her, friend or enemy, is subject to some "
            "degree of attention-capture, leaving her unable to "
            "distinguish genuine attention from biologically-induced "
            "attention. This directly parallels Ozmund's Crown-Scar "
            "loyalty-uncertainty problem. Ren's negative-density field "
            "is the one known exception: it strips the Siren's effect "
            "within its radius, letting him see her clearly."
        ),
        "status": "locked",
        "source": SOURCE_ANIRAK,
    },
    {
        "id": "CC-113",
        "category": "character-crew",
        "statement": (
            "Anirak's momentum-stacking biology generates more torque in "
            "denser media, making her measurably faster and more "
            "powerful underwater than on land (already a Codex "
            "mandate); the mechanism is torque-through-resistance, and "
            "she additionally has acoustic hydro-sensitivity functioning "
            "as a sonar-like sense underwater."
        ),
        "status": "locked",
        "source": SOURCE_ANIRAK,
    },
    {
        "id": "CC-114",
        "category": "character-crew",
        "statement": (
            "Anirak and Ren (Abyss) are established as a deliberate "
            "tactical/relational pairing -- 'Surface Storm' (Anirak's "
            "kinetic, rotational output) and 'Deep Pressure' (Ren's "
            "gravitational field) -- complementary both in combat (her "
            "blades shred structure, his field collapses the weakened "
            "structure under its own augmented weight) and as siblings: "
            "Anirak positioned herself as his protector without formal "
            "assignment, recognizing a body the world wasn't built for."
        ),
        "status": "locked",
        "source": SOURCE_ANIRAK,
    },
]

BATCH_NOTE = (
    'Abad approved the full draft as pasted in-conversation, and resolved '
    'the Sereth Vaul density conflict explicitly: "Both, at different '
    'points in time" (900x at the Great Breach, escalating to the '
    'already-locked 9,500x in a later book) -- confirmed with "locked. '
    'continue"'
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
            "batch": 46,
            "source_doc": "Six-document scope-audit follow-up: Talisman of Mao, Ever_Haunt_Expansion_v3.2, SBD Executive Director A.M. Directives, Book2_Structural_Outline_Champions.docx, 09_Anirak_Psychological_Profile.docx (standalone), and MRD_CultDossiers file-identity verification (resolved clean, no new material)",
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 1,
            "conflicts_resolved": 1,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "4.9"
    ledger["last_updated"] = "2026-09-02"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
