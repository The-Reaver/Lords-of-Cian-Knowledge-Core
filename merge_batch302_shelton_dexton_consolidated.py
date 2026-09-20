#!/usr/bin/env python3
"""Batch 302: consolidated draft-and-lock pass for all queued Shelton Dexton SBD-informant material
(Tier 1 x4, Tier 2 x5, Tier 3 x6 -- see CLAUDE.md's Batch 301 section for the full triage/ruling
history this batch formalizes into rule text)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Shelton Dexton SBD-informant source material: THIS_IS_SUPERIOR_MANDATED_BY_IMPERATOR_SHELTON_"
    "DEXTON_1.docx, IMPERATOR_SHELTON_DEXTON_1.docx, SEALBOUND_DIRECTORATE_-_ASSET_MANAGEMENT_"
    "DOSSIER.docx, MESSAGES_BETWEEN_A.M._AND_ABBOTT_GAGE_1.docx and _2.docx, SBD_Executive_Director_"
    "A.M._Directives_2.pdf, SBD_Classifications-Kanja_Legacy-Pantheaon-Moon-Sun-_1.docx (all uploaded "
    "directly by Abad, ~700K characters total). Five parallel background agents triaged the corpus "
    "against the live ledger; findings were worked through with Abad one item at a time across "
    "several turns ('Work through Tier 1 one at a time'), each ruling made explicitly before this "
    "consolidated draft-and-lock pass. Abad's closing authorization: 'move straight into the full "
    "consolidated draft-and-lock pass now for everything queued.'"
)

NEW_RULES = [
    # --- Tier 1 ---
    {
        "id": "SBD-041",
        "category": "sbd-institutional-error",
        "statement": (
            "The SBD's own file on the Pyro Birth Incident and the Triad's origin -- authored by "
            "informant Shelton Dexton, transmitted to A.M. under full-transparency posture -- is "
            "false, not the truth it replaces. Dexton's account (Pyro's birth as natural, the Triad "
            "raised from birth by Pyro's mother in her own Shattered Kingdoms homeland, and Kanja's "
            "wife killed by an anomaly-class monster rather than the Living Gate containment event) "
            "directly contradicts the already-locked, correct account at MCD-131/132/133 (Pyro's "
            "mother is not dead; she inverted T.D.K.'s Living Gate into a forge and is fused into its "
            "own architecture, no longer dead but transformed). Dexton reported this in complete good "
            "faith, per CC-140 -- he was himself misled by his own informant network, not knowingly "
            "lying to A.M. The file stands as a documented SBD institutional error, its source and "
            "the reason for the deception both unidentified, reserved as a future thread for either "
            "Archon Meridian's eventual SBD cleanup or Dexton's own reckoning with whoever fed him "
            "the false account."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-136",
        "category": "Character",
        "statement": (
            "Sorya (CC-096/097) has a genuine combat/ambush capability layer beneath her locked "
            "memory/oath-bound profile (Witness-Scouting, Vow-Taste, Shard-Recall): a five-technique "
            "predation kit exploiting her melanistic coat and emerald-eye morphology -- Black-Rosette "
            "Vanish (her faint rosette pattern intermittently appearing and vanishing under shifting "
            "light causes range misjudgment and target 'loss', letting her close from a new angle), "
            "Throatline Shear (a near-instant neck/airway termination attempt against a target caught "
            "in a confined space with limited lateral escape), Green-Eye Fixation Trap (her visible "
            "eye-marker draws and holds a target's forward attention while she flanks from an offset "
            "angle), Bone-Engine Pin (using mass and leverage to pin and crush against structural "
            "obstacles rather than repeated mauling), and Silent-Break Commit (attacking during the "
            "exact interval a human team's attention shifts to quiet internal coordination). This "
            "layer is real; the SBD's own dossier on it, however, overclaims certainty -- its "
            "'CONFIRMED' confidence ratings rest on the same informant-stream reporting network "
            "Shelton Dexton (CC-140) has already partially purged for corruption, not on direct "
            "field verification the file itself admits it lacks. CC-096/097 remain locked and "
            "unchanged; this extends rather than replaces them."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-137",
        "category": "Character",
        "statement": (
            "Aeron Dusane is a young diplomat and aerial combatant from a small island community "
            "known for its practiced environmental equilibrium -- distinct from Matar (CC-067/102), "
            "not an alias or cover identity of his. An SBD dossier conflated the two under a single "
            "file (see SBD-042), wrongly attaching Aeron's profile to Matar's name. Aeron functions "
            "as a diplomatic node and aerial combatant within his own community's affairs, known for "
            "a rapid, adaptive learning capacity and a personal balance of firmness and gentleness "
            "that makes him an effective mediator under pressure; his combat capability, still "
            "developing relative to Matar's own centuries of discipline, escalates sharply once "
            "genuinely provoked or once his own people are threatened. No connection to Kanja's crew "
            "or the Lords of Cian is established by this rule; his relationship to the wider setting "
            "remains open for future drafting."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "SBD-042",
        "category": "sbd-institutional-error",
        "statement": (
            "The SBD's dossier on 'Subject SBD-014' conflates two distinct individuals -- Matar "
            "(CC-067/102, a 620-year-old assassin operating through guerrilla mastery and tactical "
            "discipline rather than density) and Aeron Dusane (CC-137, an unrelated young diplomat "
            "and aerial combatant) -- under a single case file and a single classification, "
            "'Aerial Combat Specialist / Social Dynamics Harmonizer.' This is a misattribution error, "
            "not a real dual identity: CC-067/102 remains Matar's whole and correct profile, "
            "untouched. The error is another standing SBD institutional-reliability thread alongside "
            "SBD-041 (the false Pyro Birth file) and CC-136's overclaimed Sorya confidence ratings."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "SBD-043",
        "category": "sbd-asset-registry",
        "statement": (
            "SBD-011, registered as 'Sinisterblade,' resolves to Bloodreaver (Torian, Cruor-Kin "
            "biology, ARS's own already-locked Furnace Kit) rather than Valen -- the file's "
            "'Sinisterblade' label is a clerical duplicate error, colliding with Valen's own correct "
            "registry number SBD-008. The dossier's classification, 'Kinetic Combat Specialist / "
            "Blood-Resonance Enforcer,' its description of an obsessive dedication to arms mastery, "
            "and its note that the subject is protective of lower-tier HVAH assets and close to "
            "'SBD-001' (Kanja) all match Bloodreaver's already-locked profile directly -- Cruor-Kin "
            "biology running blood near-boiling, the only crew member besides Kanja physically able "
            "to restrain Kanja without being crushed, and an arms-heavy kit (Temper Maul, Ventspikes, "
            "Slagline Chain). The sequential numbering of this document's asset registry (SBD-012 = "
            "Ghostwind, already locked) confirms the SBD-0XX series in this source catalogues the "
            "Avatar/Titan roster generally, resolving this entry cleanly rather than requiring a new "
            "identity."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Tier 2 ---
    {
        "id": "SBD-044",
        "category": "sbd-classification",
        "statement": (
            "The SBD rates Miremaw Varkul OMEGA-PRIME threat classification, and separately, the "
            "world itself regards him as the strongest non-human presence in the setting, alongside "
            "Varruk and Sorya as a single combined posture package. Varkul's power stays density-"
            "unrated and pure biology per CC-094 -- not 'as dense as Vargo Vakas' as one SBD "
            "directive claims -- and his true ceiling is deliberately never shown maxed on the page, "
            "hinted at across future material rather than resolved. Genuinely worthy opponents for "
            "Varkul and the Triad remain to be drawn from the SBD's own captive/experimental stock "
            "and Hollow Shogunate holdings in future drafting. Varkul's own arc is set up but not "
            "drafted here: he begins unaware of the SBD's surveillance and classification apparatus "
            "built around him and the Triad, gradually discovers it, and that discovery -- not any "
            "external threat -- is what turns him aggressive; this arc is intended to eventually "
            "intersect with Archon Meridian's own unknowing dismantling of his father's SBD "
            "architecture (MCD-122/130)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "SBD-045",
        "category": "sbd-institutional-error",
        "statement": (
            "The SBD's file on Varruk claims a five-tactic 'Offensive Capability Suite' rated "
            "CONFIRMED -- Wake-Scissor (re-patterning wake turbulence to desynchronize pursuing "
            "vessels), Pressure-Seam Drop (using storm-front pressure edges to close on deck crews "
            "with minimal warning), Lantern-Denial Pass (a low pass that extinguishes exposed lamp "
            "signals to break convoy coordination), Oarline Misfire Window (disrupting synchronized "
            "rowing cadence to collapse a vessel's propulsion), and Refusal-Trap Coercion (his "
            "already-locked Guidance by Refusal, SBD-021, reframed as funneling crews into "
            "predictable, ambush-exposed corridors). This 'CONFIRMED' certainty rests on the same "
            "informant-stream network already flagged as partially corrupted (Shelton Dexton "
            "terminated an entire compromised lattice, CC-140); the reliability of this suite as "
            "described is contested, joining SBD-041/SBD-042/CC-136's confidence-rating issue as a "
            "standing thread. CC-098/099 remain Varruk's real, locked profile, untouched."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-138",
        "category": "Character",
        "statement": (
            "Abyss (Ren Oshaal, CC-066/101) origin and texture extension: found as an orphan on a "
            "remote island associated with old serpent-lore, with faint serpent-pattern dermal "
            "markings; his defining personal throughline is an unresolved quest for identity and "
            "belonging, and he regards Kanja as a paternal figure. His Negative-Density Variant "
            "gravitational-pressure biology extends to passive long-range detection -- a felt "
            "vibration/pressure sense that once gave the crew roughly fifteen kilometers of warning "
            "before a Directorate sub-surface retrieval team made sonar contact -- read by outside "
            "observers as a distinct 'seismic sense' but mechanically the same pressure-field biology "
            "already locked at CC-101, not a separate ability. Fully compatible extension; CC-066/101 "
            "unchanged."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-139",
        "category": "Character",
        "statement": (
            "Cooper (Ronan Kellsward, CC-068/103) extension: before his already-locked years as a "
            "Jicome dock laborer, he spent a formative period apprenticing in a mountainous region "
            "known for its exacting craftsmanship tradition, where he first trained the structural "
            "and material instincts that later made him the crew's Quartermaster/logistics architect. "
            "His Mass-Compression Variant biology (absorbing external mass through contact to raise "
            "his own density, CC-068/103) genuinely extends outward as well as inward: applied "
            "through sustained contact to a ship's hull or frame rather than his own body, the same "
            "biology lets him read, redistribute, and reinforce a vessel's structural integrity -- "
            "the mechanical reality behind an SBD file's cruder description of him as a 'structural "
            "integrity specialist' performing 'sub-atomic structural manipulation.' CC-068/103's "
            "origin (Jicome dock laborer) and core density figures remain unchanged and controlling; "
            "this adds an earlier life chapter and a real second application of his existing biology, "
            "not a competing origin or a separate power."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1727",
        "category": "World Mechanics",
        "statement": (
            "The SBD maintains a private, sealed intelligence apparatus, the SBD-Oracle Conflict Map "
            "(designation OR-19-AL), that tracks drift between the SBD's own working assumptions and "
            "reality across six named Conflict Domains: Demaron Ingress Mechanism, Vessel Termination "
            "Necessity Logic, Triad Bond Mechanics, Harrow Ring Clause Conditions, SBD Obfuscation "
            "Viability, and Non-SBD Architecture Depth. Director A.M. accesses it through a private "
            "network of 'sealed Oracles' via split-custody key KEY-B (SBD-030); Grave-Analyst Abbott "
            "Gage is the one who analyzes them and can return a 'Conflict Flag = YES' finding -- a "
            "formal admission that the SBD's own assumptions in a given domain are false. A.M.'s "
            "standing doctrine on a Conflict Flag: 'if the lattice contradicts our assumptions, the "
            "assumption breaks, not the record.' A confirmed Conflict Flag triggers the 'Tighten' "
            "posture -- freezing direct-contact testing and validation activity requiring proximity, "
            "moving to code-designations only, and shifting to 'Deception-by-Saturation' (multiplying "
            "decoys rather than relying on concealment) -- and the Continuity Lock, a standing "
            "directive stripping proper names from SEALBLACK case-file titles going forward so that "
            "even cleared archivists eventually lose the true names of what they guard. This "
            "apparatus is the SBD's own institutional acknowledgment that its intelligence, including "
            "everything documented at SBD-041/042/043/044/045 and CC-136, is fallible by design, not "
            "merely by accident -- and stands as a concrete future target for anyone (Archon Meridian, "
            "Shelton Dexton, or Kanja's own crew) seeking to expose or exploit the SBD's institutional "
            "blind spots."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Tier 3 ---
    {
        "id": "ARS-389",
        "category": "avatar-arsenal",
        "statement": (
            "Lunar Resonance is a self-repair subsystem of Mafesto's Living Drakma plating (ARS-010), "
            "triggered by direct moonlight: over the course of a full moon's exposure it accelerates "
            "the armor's ordinary repair cycle and temporarily strengthens its resilience to further "
            "damage, drawing on the same resonance-growth principle behind Ozmund's Bastion "
            "(ARS-380). A real, minor addition to Mafesto's already-locked gear profile, distinct "
            "from and layered beneath the Kinetic Transfer System (ARS-010) and the Sovereign "
            "Umbrella's Blight Immunity (MCD-060)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-390",
        "category": "avatar-arsenal",
        "statement": (
            "The Last Ward is a maximum-charge defensive discharge mode of Obsidian Malice (ARS-030, "
            "ARS-342), alongside its existing offensive discharge: rather than releasing Mafesto's "
            "stored kinetic energy outward as a strike, it releases the charge as a brief containment "
            "field around Kanja and whoever is in his immediate reach, a last-resort measure rather "
            "than a standing defense. Same weapon, same 3-5 second recharge and separate long-term "
            "passive-accumulation cycle already locked; a second application of Obsidian Malice's "
            "existing charge mechanics, not new gear."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-391",
        "category": "avatar-arsenal",
        "statement": (
            "Kanja's density is measurably, if minorly, responsive to real astronomical events, "
            "grounded in the Talisman of Mao's and Living Drakma's already-locked light-responsiveness "
            "(MCD-142): during an actual eclipse, the brief light disruption can cause a momentary "
            "lapse in the Talisman's ordinary suppression of his Aethelgard Kinetic Radiance, "
            "producing a rare, involuntary density spike ('Eclipse Warrior' in older, informal "
            "terminology). At the year's solstices and equinoxes -- its true solar extremes -- ambient "
            "Living Drakma resonance in his gear peaks measurably, producing minor, real stamina and "
            "combat-balance improvements ('Solstice Endurance'/'Equinox Balance') rather than a "
            "mystical timing bonus. The fourth item in this older informal grouping, 'Dusk's "
            "Embrace' (appearing as multiple figures to enemies in low light), is not a separate "
            "power -- it folds into his already-locked stealth/decoy toolkit (the Smoke System, "
            "Hymn-Engine-adjacent misdirection tactics)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1728",
        "category": "World Mechanics",
        "statement": (
            "The Master Frequency Crystal is a real artifact held in the Sealbound Directorate's "
            "deepest vault: the acoustic key required to fully harmonize the Scrip economy's global "
            "soul-debt architecture (extends WC-007's Metabolic Tether mechanics) and trigger its "
            "complete activation. T.D.K. (Anu Un Ra) does not yet possess it and does not currently "
            "seek it -- his already-locked 5,000-year dormancy runs until the Great Breach (Book 1's "
            "epilogue, MCD-070), and his legacy dependencies, including any active move on the "
            "Crystal, only reactivate from Book 2 onward (MCD-279). Once active, his 'Surgeon's Raid' "
            "to reclaim it exploits the same inherited Ionic Rite backdoor architecture the SBD "
            "unknowingly sits on (CULT-008) rather than any direct assault -- he does not seek to "
            "rule the SBD again, only to retrieve what he stored there. Recovering or destroying the "
            "Crystal before he can complete the harmonization reinforces, rather than replaces, the "
            "already-locked Book 5 endgame objective of severing the Crown-Scar siphon via the "
            "Meridian Engine fragment (MCD-099/327) -- both are part of the same larger mechanism "
            "the heroes must stop before T.D.K. can fully manifest as what an SBD informant file "
            "calls 'the Administrator of Reality.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "CC-140",
        "category": "Character",
        "statement": (
            "Shelton Dexton, self-titled Imperator, is an independent informant and power broker "
            "operating out of the Shattered Kingdoms, deliberately location-redacted even from A.M., "
            "and commands a private force known as the Havik Legions. He reports to A.M. as a source "
            "but answers to no one, SBD or otherwise, and treats full transparency as his core "
            "method: he believes suppressing or softening a hard truth only builds pressure that "
            "eventually fractures into worse exposure, so he reports exactly what his own network "
            "gives him, however unwelcome. He has, on his own authority and without A.M.'s permission, "
            "eliminated an entire informant lattice he judged too compromised to safely isolate -- "
            "acting alone, explaining himself only afterward, a pattern that defines him. He is a "
            "tweener, not a villain or a hero outright: his methods run genuinely gray-to-ruthless "
            "(unilateral action, dissolving networks, answering to no authority), but his core "
            "commitment -- expose the truth, never suppress it, protect people from institutions that "
            "lie to control them -- is fundamentally heroic in intent, making him likable despite the "
            "harshness of what he actually does. His confident report on the Pyro Birth Incident and "
            "the Triad's origin (SBD-041) is false, and he does not know it -- his own network fed him "
            "a convincing fabricated account, and he transmitted it to A.M. in complete good faith, "
            "consistent with his own transparency doctrine. Who planted that disinformation, and why, "
            "is a live, unresolved mystery reserved for future material -- a natural future collision "
            "point with Archon Meridian's own eventual dismantling of the SBD's architecture, since "
            "Dexton's independence and ruthlessness make him a wildcard who could help that effort, "
            "complicate it, or both, without ever being formally part of it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1729",
        "category": "World Mechanics",
        "statement": (
            "Cinderhilt is a real anomaly-class creature, independent of the false account (SBD-041) "
            "that originally attached it to Kanja's wife's death: a roughly seven-foot humanoid of "
            "dense, engine-like build, its skin reading like cooled slag -- matte, dark, fissured, "
            "with the fissures emitting a slow, breathing heat -- and dull ember-core eyes the color "
            "of metal just before it stops being workable. It moves with economy rather than rage, "
            "targeting structural supports (doorframes, stair spines, load-bearing corners) rather "
            "than opponents directly, and its primary hazard is not fire but what informant reporting "
            "calls 'thermal permission': it does not so much burn matter as convince it to stop "
            "holding its current form, so fabrics soften and fail, metal loses temper, and stone "
            "sweats and cracks along old stress lines, without a conventional flame ever being "
            "present. A secondary pressure effect around it induces false certainty in witnesses, who "
            "swear afterward they saw a demon or a divine sign rather than a repeatable, physical "
            "threat -- how myths about it get planted. It is not invulnerable: rapid cooling disrupts "
            "its thermal-permission field, and it can be forced into predictable movement by "
            "controlling and denying it structural collapse routes. What Cinderhilt has actually "
            "fought, and against whom, remains open for future drafting."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Abad: "move straight into the full consolidated draft-and-lock pass now for everything queued '
    '(the four Tier 1 items, the five-plus Tier 2 items, the Tier 3 armor/gear additions, the Master '
    'Frequency Crystal, the Conflict Flag apparatus, and Shelton Dexton/Cinderhilt)."'
)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 302,
            "date": str(date.today()),
            "source": "Shelton Dexton SBD-informant source material (7 uploaded documents)",
            "rule_count": len(NEW_RULES),
            "note": (
                "Consolidated draft-and-lock pass closing out the full Shelton Dexton SBD-informant "
                "triage: Tier 1 (SBD-041 false Pyro Birth file, CC-136 Sorya's real second ability "
                "layer, CC-137/SBD-042 Aeron Dusane as a distinct character from Matar, SBD-043 "
                "SBD-011 resolved as Bloodreaver), Tier 2 (SBD-044 Varkul's OMEGA-PRIME status and "
                "arc hook, SBD-045 Varruk's contested Offensive Capability Suite, CC-138 Abyss's "
                "extended origin, CC-139 Cooper's mountainous apprenticeship and structural-"
                "manipulation extension, MCD-1727 the SBD-Oracle Conflict Map apparatus), and Tier 3 "
                "(ARS-389 Lunar Resonance, ARS-390 the Last Ward, ARS-391 the Celestial Power Curve, "
                "MCD-1728 the Master Frequency Crystal correctly placed post-Great-Breach, CC-140 "
                "Shelton Dexton as a tweener-leaning-hero character, MCD-1729 Cinderhilt as a real "
                "anomaly-class creature). Every item was individually discussed and ruled on across "
                "several prior turns before this batch formalized the rule text. " + BATCH_NOTE
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
