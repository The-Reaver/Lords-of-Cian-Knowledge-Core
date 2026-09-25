#!/usr/bin/env python3
"""Batch 308: The Arsenal of Cian Definitive Edition v2, mined and locked in full.

Six parallel background agents drafted mechanical elaborations of ~30 already-locked
name-only ARS- stub rules (ARS-010 through ARS-340, a pre-batch-log-discipline extraction
pass). Seven real contradictions/naming collisions surfaced; rather than resolve them
unilaterally, a five-judge independent "fleet" panel was convened (no cross-talk between
judges) to render verdicts, which were then consolidated and presented to Abad in full.
Abad's approval: "lock it."
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"
SOURCE = (
    "Arsenal_of_Cian_Definitive_Edition_v2 (Google Drive, ~200K characters, 31 sections). "
    "Six parallel background agents each mined a cluster of sections, cross-checking every "
    "named item against the live ledger and discovering that nearly all of it extends "
    "already-locked name-only 'stub' rules (ARS-010 through ARS-340, an older pre-batch-log "
    "extraction of this same document's item names only, status uppercase LOCKED). Seven "
    "real contradictions/naming collisions were flagged rather than resolved unilaterally: "
    "Dead Drakma Small Arms vs. the locked no-firearms world-tech constraint (PH2-049); a "
    "triple naming collision on 'Cadence Ruin' (Onyx's blade power, Varruk's ability, and a "
    "new semantically-opposite use for Sereth Vaul's Green Mark aura); a materially "
    "incompatible 'Old Dragon' collision between MCD-302's undetailed Rexmar item and a newly "
    "drafted Valen Sinisterblade sword; a direct authorship contradiction on Fermand "
    "Aurelias's Palimpsest (MCD-268 says Kanja forged it, this source says Fermand "
    "commissioned it elsewhere); Ezio Valcari's Archive-Key losing its housing when Attia's "
    "Rite was reassigned to Lauris (ARS-359); Red Beard's 'granted manumission' claim "
    "appearing to conflict with his established Book 1 Unchained Legion defection; and two "
    "minor open items (Valen's four unnamed Talons, an unlocked 'the Clarity' epithet). Per "
    "Abad's direction ('let the fleet render a verdict'), five independent background-agent "
    "judges (no visibility into each other's reasoning) each rendered a full verdict on all "
    "seven items against the project's own established precedents (rename-on-collision, "
    "compatible-reading-preferred, the no-firearms floor, the Sereth Vaul density-escalation "
    "precedent). Two judges independently pulled MAW-079 and found it already locks Red Beard "
    "as one of the fewer-than-200 Cestari in 5,000 years to cross the genuine financial "
    "manumission threshold -- sharpening the manumission item into a precise two-fact "
    "untangling rather than a simple accept/reject call. The five verdicts were consolidated "
    "into one resolution per item (by vote plurality, weighted toward judges who verified "
    "against primary-locked-source text) and presented to Abad in full before drafting."
)

with open(LEDGER_PATH, "r", encoding="utf-8") as f:
    ledger = json.load(f)

existing_ids = {r["id"] for r in ledger["rules"]}

NEW_RULES = [
    # --- Anu Un Ra / T.D.K. (extends ARS-270) ---
    {
        "id": "ARS-392",
        "category": "antagonist-arsenal",
        "statement": (
            "Extends CULT-004/CULT-194: the Exchange Protocol's cyclical rebuilding requires "
            "biological material from compatible donors, and Karesian -- Rex-Mar bloodline -- "
            "biology specifically is the highest-fidelity donor material available. This is "
            "the true mechanical reason T.D.K. maintains a fixed interest in the Rexmar line: "
            "not political retaliation, but because Kanja's own existence, and specifically "
            "his Aethelgard Kinetic Radiance at the frequency level, actively disrupts the "
            "Exchange Protocol's maintenance cycle -- a biological threat to T.D.K.'s continued "
            "operation, not merely a military one. Degradation is slow (centuries, not years) "
            "but irreversible without fresh compatible material: T.D.K. is maintained rather "
            "than immortal, and the maintenance can, in principle, be cut off at its source."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-393",
        "category": "antagonist-arsenal",
        "statement": (
            "The Legacy Lattice (named at ARS-270, undetailed until now) is Anu Un Ra's second "
            "arsenal component alongside the Warbody, not a physical weapon: his surviving "
            "network of embedded root-permissions in every institution built on technology he "
            "originated roughly 25,000 years ago, giving proper name and mechanism to CULT-008's "
            "already-locked 'root protocol hierarchies embedded in the earliest architecture.' "
            "The Sealbound Directorate's Blight Frequency network, Scrip-Tether system, and "
            "Ionic Rite containment protocols all run on his original architecture; its current "
            "operators believe they own the technology, not knowing T.D.K. still holds "
            "root-level commands over it. The Crown-Scar (MCD-052) is a Legacy Lattice node "
            "embedded in Verehimu biology rather than institutional infrastructure -- the same "
            "mechanism in a different substrate, which is what Ozmund actually discovers in "
            "Book 1 (extends MCD-052/053). Five thousand years of the Directorate's own "
            "incompetent stewardship has degraded the Lattice's fidelity -- root commands still "
            "function but imperfectly. The Great Breach (CULT-009) is now explained as T.D.K. "
            "testing how much of the Lattice still answers to his voice after five millennia "
            "of dormancy."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Vargo Vakas (extends ARS-280) ---
    {
        "id": "ARS-394",
        "category": "antagonist-arsenal",
        "statement": (
            "Extends ARS-280/CC-105: Vargo Vakas's static 20,000x density is also his one "
            "exploitable weakness. He is immensely heavy and immensely slow -- any surface he "
            "stands on must be specifically engineered to support his mass, standard "
            "architecture collapses under him, and he cannot pursue a target that maintains "
            "distance. His combat doctrine is Azar Dreadlord's Immovable Horror (ARS-140) "
            "scaled to geological proportions: he occupies ground and anything entering it is "
            "destroyed, but cannot chase what declines to enter it. Against mobile Avatars "
            "built for range and evasion -- Sylas 'Ghostwind,' Jax 'Voidbreaker,' Kairo "
            "'Stormreaver' -- his density becomes a liability; the crew's actual doctrine "
            "against him is to flow around him rather than engage his space directly."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- T.D.K.'s Champions (extends ARS-290/MCD-283) ---
    {
        "id": "ARS-395",
        "category": "antagonist-arsenal",
        "statement": (
            "Sereth Vaul's Green Mark grants him a personal ~30-meter passive "
            "sensory-disruption field -- the Void Wake (renamed from the source document's "
            "'Cadence Ruin' to resolve a real triple naming collision with Onyx of Oblivion's "
            "blade power and Varruk's disruption ability, per the five-judge fleet's unanimous "
            "verdict; consistent with the Ever-Haunt's own established 'Void-' naming "
            "convention: Void-Spore, Void-Swarm, Void Hound, Void Steed, Void Weaver) -- inside "
            "which electronics, coordination signals, and technological targeting degrade; he "
            "tracks by scent, sound, vibration, and sight alone. This extends, rather than "
            "restates, the already-locked fact that he can walk inside an Ever-Haunt "
            "Anti-Resonance field and remain functional: his own body now generates a "
            "smaller-scale version of that phenomenon as a byproduct of stable Green Mark "
            "integration. The Talisman of Mao's Shadow-Pulse and the Void Wake are competing "
            "frequencies -- near Sereth specifically, the Sovereign Umbrella's protections "
            "measurably degrade for anyone nearby. His vulnerability: the Void Wake jams his "
            "own senses too, so against a target with comparable non-technological biological "
            "awareness -- Varruk's Pattern-Scouting/Angle-Whisper (CC-098) specifically -- the "
            "pursuit degrades into a pure endurance contest."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-396",
        "category": "antagonist-arsenal",
        "statement": (
            "Extends MCD-283: Lord Varro Dominael personally retains full combat capability "
            "from the warlord he was before execution -- his compliance is engineered at the "
            "biological level, not a loss of capacity. His division (Division 4, Crownless "
            "Host/Dominion) fields, alongside the already-locked cataclysm-tier organisms "
            "(CULT-009), a distinct arsenal of Cataclysm-tier siege engines: dormant Old "
            "Dominion war machines with self-replenishing ammunition that advance at the pace "
            "of the slowest engine and never stop. He flies no banner -- the absence itself is "
            "read as his standard. His true vulnerability: his command authority over the Host "
            "is delegated FROM the Legacy Lattice (ARS-393), not sourced independently -- if "
            "the delegation is severed, the Host doesn't turn hostile, it simply stops."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- SBD Standard Issue (extends ARS-300) ---
    {
        "id": "ARS-397",
        "category": "directorate-equipment",
        "statement": (
            "Extends ARS-300: SBD Dead Drakma Plate Armor is modular, effective against "
            "baseline-through-Elite Standard threats (25x-500x) and ineffective above Military "
            "Standard, non-self-repairing -- the direct material-property inverse of Kanja's "
            "self-repairing Living Drakma (ARS-010). Its structural weakness: Dead Drakma "
            "alloy resonates at a fixed frequency, and Kanja's Aegis-Talisman (ARS-050) "
            "broadcasts that exact frequency, causing sympathetic vibration across any Dead "
            "Drakma plate in range."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-398",
        "category": "directorate-equipment",
        "statement": (
            "Extends ARS-300: SBD Blight Frequency Projectors come in portable (~500m) and "
            "fixed tower-mounted (~50km) configurations. Mechanically, the signal is a "
            "degraded copy of T.D.K.'s original Ionic Rite frequency, operating close enough "
            "to Kanja's own Aethelgard resonance that the Talisman of Mao's Blight Immunity "
            "(MCD-060) generates a near-perfect anti-phase cancellation, and the Hymn-Engine "
            "(ARS-310) produces a cruder functional approximation using synchronized human "
            "voices -- explaining, for the first time, why both already-locked systems work "
            "against it."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-399",
        "category": "directorate-equipment",
        "statement": (
            "Extends ARS-300/WC-007/MAW-081: SBD Scrip-Tethers are the physical enforcement "
            "layer of the Metabolic Tether (WC-007) -- an economic-biological feedback loop: "
            "the device monitors labor output, calculates debt position, and applies "
            "metabolic suppression proportional to indebtedness, so deeper debt produces a "
            "heavier-feeling body and slower metabolism, deepening the debt further. Its "
            "already-locked weaknesses (the Sovereign Umbrella nullifies it in radius; Ezio's "
            "forensic accounting exposes its fraudulent basis) are joined by one "
            "characterization: the single most effective weapon ever used against the "
            "Scrip-Tether system was arithmetic -- publicly proving the debt's math was wrong."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Ozmund Verehimu (extends ARS-060) ---
    {
        "id": "ARS-400",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-060: Dragondal, Ozmund's primary warhammer, is a single dense Living "
            "Drakma block forged by Kanja Rexmar as a personal commission -- one of the few "
            "weapons Kanja has forged for someone other than himself -- lattice-optimized to "
            "channel Ozmund's Density Spike (MCD-024) without structural failure. At full "
            "Spike, a Dragondal strike produces a 'Gravity Quake': localized gravitational "
            "compression at the impact point (liquefying stone, folding metal, shattering "
            "Dead Drakma) accompanied by a chest-felt pressure wave audible to roughly 100 "
            "meters; its weight makes it a finishing weapon rather than a fencing tool, so "
            "Ozmund relies on Shadow's Whisper or unarmed combat for extended engagements. "
            "Shadow's Whisper, his secondary short sword, is Living Drakma tuned to absorb "
            "its own acoustic output -- silent drawn, striking, and sheathed -- reserved for "
            "precision work where Dragondal's collateral would be unacceptable, and serves as "
            "his primary blade during the Accession Games, whose Maw-bred format favors speed "
            "and technique over demolition."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-401",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-060: the Crown-Gauntlets are Living Drakma forearm shields, crafted "
            "by Kanja and integrated into Ozmund's wrist-and-forearm armor, serving as his "
            "primary fighting instrument since he fights principally with his hands. They "
            "function as defensive plating for blocks and parries and as Density Spike "
            "focusing lenses -- concentrating a punch's infinite mass into a knuckle-sized "
            "contact surface -- and additionally project resonance-echo images of past "
            "Verehimu warriors encoded in the Drakma's lattice memory, consistent with "
            "Drakma's established responsive-lattice physics (MCD-301) and the precedent of "
            "Lauris's Memory-Plate Technology in the Phalanx (ARS-360). Activation produces a "
            "momentary amber flash along the knuckle ridges the crew nicknames 'the Crown'; "
            "the gauntlets are calibrated specifically to Ozmund's Karesian biology and would "
            "function as ordinary Living Drakma forearm guards, without Spike-channeling, for "
            "any other wearer. Red Beard's own account frames the three-piece kit as one "
            "operating philosophy: Dragondal for structures, Shadow's Whisper for throats, "
            "the gauntlets for everything in between."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Sephtis (extends ARS-080/CC-110/CULT-197) ---
    {
        "id": "ARS-402",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-080/CC-110/CULT-197: the thirteen Chrono-Anchor Bells perform three "
            "functions beyond the verification mechanic already locked at CC-110 -- (1) "
            "anchoring Sephtis to the present moment, immune to temporal distortion; (2) "
            "functioning as a three-dimensional compass, responsive to barometric pressure, "
            "magnetic fields, and Legacy Lattice tension, reading safe passage; and (3) "
            "transmitting a synchronization pulse across distance no signal jammer can block. "
            "This third function is offered as the likely coordination mechanism behind the "
            "already-locked Three-Day Blackout (MCD-237) -- compatible with, not replacing, "
            "that event's credited nine Hymn-Engine teams; the bells plausibly supplied the "
            "unjammable simultaneous-timing signal, not the overload itself. Each bell's note "
            "forms a code the crew reads by ear (a single low chime = caution, a cascade of "
            "high chimes = immediate danger, deliberate silence = Sephtis muffling them, the "
            "most alarming signal of all); separated from Sephtis, the bells revert to inert "
            "Living Drakma chimes."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-403",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-080: the Drakma Barn Owl Skull mask is a Living Drakma sensory "
            "apparatus, its eye sockets fitted with multi-spectral lenses reading visual, "
            "thermal, and Lattice-resonance frequencies simultaneously, compensating for the "
            "biological degradation of Sephtis's 1,997-year-old eyes while adding "
            "capabilities no organic eye possesses, including 'Cold Mapping' -- reading the "
            "residue historical events leave imprinted on the Lattice. The True Log is "
            "Sephtis's personal 1,997-year archive, bound in Living Drakma covers with "
            "Drakma-filament pages inscribed at the molecular level, making entries "
            "impossible to erase, alter, or forge; it functions as the rebellion's "
            "institutional memory -- the second-most comprehensive archive in existence after "
            "Onyx's Black Ledger (MCD-023), narrower in scope despite its own near-two-"
            "millennium span. Sephtis's own name for Sorya, the Triad Guardian, is 'The True "
            "Log' -- his highest compliment, recognizing her already-locked Witness-Scouting "
            "capability (CC-096) as functionally identical to his own instrument."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Ezio Valcari (extends ARS-210; ARS-359's cane-sword supersession stands) ---
    {
        "id": "ARS-404",
        "category": "intelligence-tier-arsenal",
        "statement": (
            "Extends ARS-210 (that entry's Attia's Rite/cane-sword listing for Ezio remains "
            "superseded in favor of Lauris per ARS-359 and is not restated here): the "
            "Archive-Key is a set of twelve hair-thin Living Drakma filaments, bio-tuned to "
            "Ezio's own resonance, housed in the hollow shaft of the Cipher Cane -- a plain, "
            "unremarkable cane that reads publicly as a theorist's affectation, privately as "
            "his only concealed-carry prop, distinct from and never confused with Attia's "
            "Rite. The filaments defeat locks and mechanisms by touch-reading their internal "
            "structure through micro-vibration feedback -- he identifies the correct "
            "configuration by feel, the way a doctor reads an X-ray, then shapes a filament "
            "to match it. A secondary function lets the filaments interface directly with "
            "Directorate Drakma data-plates, reading sealed classified SBD records back to "
            "him as touch-interpreted micro-vibration. Structural Interrogation -- mapping a "
            "room's density and structure in two taps -- is performed with the same Cipher "
            "Cane."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-405",
        "category": "intelligence-tier-arsenal",
        "statement": (
            "Extends ARS-210: the Socratic Trap is Ezio's signature interrogation method, not "
            "a physical weapon -- oblique, apparently academic questions that lead a target "
            "down a logical path where only a truthful final answer avoids self-"
            "contradiction, closed with a deliberate silence that pressures the target to "
            "fill the void. Consistent with Ezio's classified combat profile (CC-027/WC-016/"
            "CC-111), the Trap is characterized in-canon as having extracted more intelligence "
            "than any blade in the crew's arsenal."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Ironbane (extends ARS-100/CC-041) ---
    {
        "id": "ARS-406",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-100: Thunder-Cleaver is a Living Drakma broadsword with a "
            "superconductive core running its full length, with a charged mode where the "
            "core banks his bio-electric output until impact, delivering a combined kinetic-"
            "plus-electrical strike that overloads organic nervous systems and shorts "
            "mechanical systems -- against Dead Drakma armor, the discharge finds structural "
            "imperfections and blows out seams rather than penetrating directly. King's Roar "
            "is a Drakma-plated vocal amplifier converting his bio-electric vocal output into "
            "a directional ~50-meter sonic weapon calibrated to Dead Drakma's resonance "
            "frequency; used defensively, it also carries a standing +25% passive morale "
            "boost to nearby allies as a side-effect of his baseline bio-electric field."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-407",
        "category": "avatar-arsenal",
        "statement": (
            "Extending CC-041's already-locked life-support/Critical-Overload fact, the "
            "Ionic Ground Bracer's actual mechanism is passive environmental grounding of "
            "Ironbane's constant, uncontrolled bio-electric output -- a simpler, single-"
            "wearer analogue of the Talisman of Mao's Stage 2 grounding function; visible "
            "confirmation is Lichtenberg-figure scarring glowing white-blue in proportion to "
            "discharge volume. The Lichtenberg Gauntlets are a separate melee-augmentation "
            "piece drawing off the same charge-management system: directed electrical "
            "discharge through unarmed strikes, causing nervous-system disruption against "
            "organic targets and system shorts against mechanical ones, trading Thunder-"
            "Cleaver's reach for grappling-range lethality."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Anansi (extends ARS-110/MCD-302) ---
    {
        "id": "ARS-408",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-110: Anansi's Null-Thread Spinnerets are a biological weapon system "
            "-- a silk-analogue fiber from modified sweat glands, tensile strength exceeding "
            "military cable, invisible below 0.3mm. The fiber serves seven field functions "
            "including vibration-transmission communication (the physical layer of his "
            "Ghost-Lattice network, extends MCD-240/242) and bio-compatible wound suturing. "
            "The Loom-Blade is a narrow Living Drakma stiletto retractable into his sleeve, "
            "forged by Kanja to Anansi's specification for single-wound assassination "
            "doctrine. The Rim is his signature fedora, Living-Drakma-reinforced and razor-"
            "edged, co-designed with Kanja, functioning as a returning thrown weapon, a "
            "ballistic-deflecting shield, and his real-time room-geometry survey method via "
            "its habitual brim-tip. The Kinetic Tail-Weights are dense Drakma-alloy weights "
            "sewn into his longcoat's hemline, converting the coat's swing into a momentum "
            "weapon -- together the four pieces mean Anansi is functionally always armed "
            "since he is always dressed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Ghostwind (extends ARS-160/CC-061) ---
    {
        "id": "ARS-409",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-160/CC-061: the Slipstream Harness is an ultra-light Living Drakma "
            "mesh engineered around Sylas's Hollowed Density biology, providing aerodynamic "
            "drag reduction (~60%) sustaining his triple-speed movement, and at full "
            "activation a 'Zero-Drag Field' eliminating his sonic signature. The Wind-Razors "
            "are paired recurve daggers built for draw-cuts delivered mid-transit at triple-"
            "speed, functionally useless in static, positional combat. The Vane-Compass is a "
            "sternum-worn disc reading atmospheric pressure, wind patterns, and Lattice "
            "density in real time, establishing him as the crew's pathfinder -- 'what the "
            "Compass does for navigation, Onyx does for judgment.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Stormreaver (extends ARS-170/MCD-259) ---
    {
        "id": "ARS-410",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-170/MCD-259: the Zephyr-Frame is a Living Drakma articulated wing-"
            "frame generating lift through localized atmospheric pressure manipulation, "
            "giving Kairo true three-dimensional flight to ~3,000 meters silently; it "
            "degrades in vacuum or severe atmospheric disruption (e.g., inside an Ever-Haunt "
            "field, extends CULT-197). The Insight Lenses amplify his baseline dual-spectrum "
            "sensory biology: the gold lens reads structural/tactical information, the silver "
            "lens reads emotional/physiological information and is also the focusing point "
            "for a biological trust/de-escalation effect he can direct at individuals during "
            "negotiation without removing their agency over the resulting decision. The "
            "Raptor-Gauntlets are talon-hook gauntlets used offensively and for casualty "
            "extraction. (The source's real-world-deity 'archetype' label for this biology is "
            "deliberately dropped per the established Batch 301/302 precedent -- only the "
            "underlying mechanics are drafted.)"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Anirak (extends ARS-130/ARS-367-374) ---
    {
        "id": "ARS-411",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-130 and the already-locked Twin Fangs/Siren's Voice mechanics "
            "(ARS-367 through ARS-374): the Triform Morning Star is the third weapon in "
            "Anirak's Chain Storm kit, a Drakma-alloy mace whose head shifts between three "
            "states via wrist-torque and impact-force triggers: Grapple-Star (spike-and-"
            "talon capture/disarm), Lantern-Star (a strobing light core, corroborating the "
            "already-locked Ever-Haunt-countermeasure reference to 'Anirak's Lantern-Star "
            "strobe mode'), and Split-Crown (~40% wider striking radius for crowd control). "
            "Doctrine: the Twin Fangs set the perimeter, the Siren's Voice degrades "
            "perception of it, the Morning Star punishes anyone who crosses it. Minor "
            "scaling texture for the already-locked weapons: the Twin Fangs' kill radius "
            "runs ~3m at low Stack to ~6m at high Stack; the Siren's Voice's forward cone "
            "runs to ~10m with a 15-20% distance-misjudgment effect."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- The Triad Guardians (extends CC-094-099) ---
    {
        "id": "ARS-412",
        "category": "dhar-kael-system",
        "statement": (
            "Extends CC-094/CC-095/MCD-020: Varkul's flanks carry bioluminescent markings "
            "that pulse with threat proximity; his hooves are reinforced with biological "
            "Drakma-carbonate. The Density Compression Charge is a distinct ability separate "
            "from the already-locked Hydro-Inertia: Varkul temporarily increases his own mass "
            "during a charge (effective weight fluctuating ~2-8 tons) -- colloquial "
            "terminology, not a claim about his formal density rating, which stays unrated/"
            "pure biology as already locked. His bio-armor is three layers (keratinous "
            "plate, shock-absorbing cartilage, Drakma-mineralized bone); only Drakma-forged "
            "weapons or Titan-class impacts penetrate all three. The Guardian Clause is a "
            "real in-universe restriction confining the Harrow Ring strictly to Pyro-vowed "
            "defense -- it cannot be invoked for any other purpose -- giving concrete content "
            "to the Harrow Ring Clause Conditions the SBD's Oracle Conflict Map (CULT-200/"
            "MCD-1727) already tracks as an area of institutional uncertainty."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-413",
        "category": "dhar-kael-system",
        "statement": (
            "Extends CC-098/CC-099: Varruk's plumage runs pale cream to buff-white, "
            "deliberately stained rust-orange through iron-rich dust bathing as intentional "
            "scent-masking rather than passive coloring. His Cadence-disruption vocalization "
            "(extends the already-locked Cadence Ruin, CC-098) operates at ~200m radius, "
            "interfering with communication and targeting simultaneously. A distinct named "
            "behavior, the Stare: fixing a threat with unblinking intensity, producing a "
            "sensation of being observed at a level deeper than visual contact -- separate "
            "from Angle-Whisper's geometric-certainty projection. Beneath the resonance-bond "
            "with the Triad, Varruk maintains an everyday vocal register the crew reads: "
            "growls signal danger, purrs signal safety, a specific whine signals detected "
            "deception."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-414",
        "category": "dhar-kael-system",
        "statement": (
            "Extends CC-096/CC-097: the Witness Shriek is a distinct, higher-escalation "
            "capability beyond Sorya's Shard-Recall/Mimic Speech kit, reserved for genuine "
            "emergencies -- a multi-frequency vocalization producing ~3 seconds of total "
            "sensory confusion, which Varkul and Varruk exploit to extract Pyro from danger. "
            "Sephtis's nickname for her, 'the True Log,' is confirmed as a deliberate "
            "homage-echo of his own True Log codex (ARS-403) and his highest compliment. "
            "Extends CC-048's Pyro bond with a forward-looking function: when Pyro eventually "
            "learns his father's identity, Sorya is established as the one who can show him "
            "his own history from outside his own perspective."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Fermand Aurelias (extends ARS-230) ---
    {
        "id": "ARS-415",
        "category": "intelligence-tier-arsenal",
        "statement": (
            "Extends ARS-230: the Palimpsest is a Living Drakma rapier, forged by Kanja per "
            "MCD-268, etched with Drakma-filament micro-channels that record the resonance "
            "signature of everything the blade contacts as it cuts. Fermand reads this data "
            "by running his thumb along the channels -- the same tactile technique Ezio uses "
            "with the Archive-Key (ARS-404), a deliberate cross-character consistency in how "
            "Drakma-recording instruments are read. Its existence is nonetheless a genuine "
            "act of personal investment from a man who keeps little that is his own: Fermand "
            "asked Kanja for it directly, rather than accepting whatever standard-issue "
            "Trinity-adjacent gear was on offer, and personally specified its exact design, "
            "etching pattern, and proportions -- resolving a five-judge fleet review's "
            "flagged conflict against this source's own claim that an outside Karesian "
            "bladesmith forged it, which is rejected in favor of MCD-268's authorship "
            "standing intact. The Archive-Cask is a hermetically sealed, blast-resistant Dead "
            "Drakma survival case carrying Fermand's operational package: document copies, "
            "chemical reagents, a miniaturized charcoal-rubbing kit (extends MCD-286), lock-"
            "defeat tools, and field-surgery medical supplies. Its sealed inner chamber holds "
            "a single item Fermand has never shown anyone -- classified even from Kanja, a "
            "deliberate open hook. The Baroque Tongue grounds Fermand's narration register "
            "(VB-024/CC-034) as an actual operational technique: his ornate, digressive "
            "syntax occupies a listener's analytical bandwidth, and the gap between hearing "
            "and comprehending his sentence is the window in which he reads their unguarded "
            "micro-expressions."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Lady Nadea Thren (extends ARS-240/CC-072-074) ---
    {
        "id": "ARS-416",
        "category": "intelligence-tier-arsenal",
        "statement": (
            "Extends ARS-240/CC-072/CC-073/CC-074: the Viper's Fang is a Drakma-tipped spear "
            "coated in Widow's Gavel, a coagulant Nadea developed during her Red-Salt "
            "Odyssey (an operational period in the Shattered Kingdoms, extending her SBD "
            "Division of Perceptual Analytics background) causing instant stroke on contact "
            "with broken skin. The Recurve Siege-Bow is fired from a full gallop using "
            "floating-anchor mounted archery -- this combined mounted-lethality capability is "
            "named 'the Centaur State,' the source framing her as rivaled only by Ozmund and "
            "Kanja among named characters. The Oxidation-Seal is her chemical/pheromonal "
            "arsenal: Pheromonal Dictation (perfumes inducing panic or compliance before she "
            "speaks), the Invisible Guillotine (dormant contact poisons the Directorate's own "
            "forensics has never identified as assassination), and Red-Salt Immunity (self-"
            "administered micro-dosing leaving her immune to any known poison). The "
            "Oxidation-Guard is her personal armored-cavalry escort riding sealed filtering "
            "masks."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Stormbreaker/Kaelen (extends ARS-120/CC-044/045/062) ---
    {
        "id": "ARS-417",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-120 with full mechanics for three of Stormbreaker's (Kaelen, "
            "Seismic Variant, CC-044/045/062) six Siege Platform pieces. The Equinox is a "
            "Living Drakma meteor hammer whose spherical head acts as a gravity-focus lens: "
            "on impact it amplifies his localized gravity anomaly at the contact point, so "
            "struck targets are pulled into the hit rather than knocked away -- armor "
            "compresses and structures crumple inward rather than shattering outward, a "
            "visible gravitational corona ('the Drag') bending dust and light toward the "
            "swinging sphere. The Verdict is a gauntlet on his primary hand that fires a "
            "forward-facing cone (~15m) multiplying local gravity 10-50x, pinning everyone in "
            "the cone to the ground simultaneously under their own unbearable weight ('the "
            "Kneel'); this is explicitly directional, and Stormbreaker is flank-vulnerable "
            "while it's active. The Graviton Maul is his conventional-force backup hammer, "
            "striking outward rather than crushing inward, reserved for straightforward "
            "demolition too slow for the Equinox's compression effect. T.D.K.'s Warbody "
            "rates him 'Fortress-Killer,' the same opponent-classification convention already "
            "established for Valen ('WORST CASE,' ARS-070)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "ARS-418",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-120 with the remaining three Siege Platform pieces. Seismic Boots "
            "translate Stormbreaker's footfalls into localized tremors, usable as sustained "
            "area-denial or a directed shockwave erupting beneath a distant target; they "
            "double as passive geological sensing, letting him 'feel' tunnels, voids, and "
            "structural weaknesses through vibration feedback. The Tectonic Girdle is load-"
            "bearing armor, not a weapon: it suppresses his ambient gravitational leakage so "
            "he can exist in normal spaces without cracking floors, meaning he activates the "
            "Equinox/Verdict/Thunder-Shot by RELEASING the Girdle's suppression rather than "
            "generating additional force -- Girdle damage causes leakage that turns him into "
            "a hazard to allies as well as enemies. Thunder-Shot is a wrist-mounted launcher "
            "firing Living Drakma micro-spheres that detonate into temporary (~5-second) "
            "localized gravity wells (~3m diameter), used for anti-fortification, anti-"
            "personnel bombardment, and area denial at range."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Voidbreaker/Jax (extends ARS-150) ---
    {
        "id": "ARS-419",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-150 with full mechanics for Jax's ('Voidbreaker,' Spatial-"
            "Displacement Variant) Spotter's Kit. The Phase-Rippers are paired Living Drakma "
            "karambit blades tuned to survive being spatially folded alongside him; his "
            "doctrine is a ~0.3-second displacement-strike, effective only at close range and "
            "requiring him to already know the target's exact position and guard -- reduced "
            "against opponents who can sense spatial displacement (e.g. Onyx's Lattice-"
            "awareness). Void-Marker Darts are wrist-launched anchor points (12 carried per "
            "engagement, limited and must be retrieved/redeployed): once a dart embeds in any "
            "surface, Jax can fold directly to that point from any range within his "
            "operational limit. The Null-Cloak is a Living Drakma-filament garment extending "
            "his displacement field to his whole body while passively micro-displacing his "
            "visual profile by fractions of a centimeter, leaving him permanently slightly "
            "out of focus to observers."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Soulreaver Zora (extends ARS-180; confirmed not a new character) ---
    {
        "id": "ARS-420",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-180 with full mechanics for Zora's ('Soulreaver') Tempest's "
            "Arsenal, consistent with her locked Atmospheric/barometric-asphyxiation "
            "biology. The Scream is a 3m Living Drakma chain-whip with resonance chambers in "
            "each link that amplify air displacement into a sonic boom arriving "
            "simultaneously with physical impact -- a 5m-radius shockwave cone that ruptures "
            "eardrums, disorients balance, and cracks brittle materials. Lung-Collapse "
            "Grenades are hen's-egg-sized Drakma-shell vacuum charges (8 carried per "
            "engagement, thrown accurately to ~30m) that on detonation create a ~4m near-"
            "zero-pressure bubble lasting 8-12 seconds. The Gale-Shield gauntlets run two "
            "modes: a forward pressure-wall (Repulsion) that deflects small-arms fire and "
            "staggers armored infantry, and an inverted vacuum field at point-blank "
            "grappling range (Asphyxiation Focus) that evacuates air from the space between "
            "her arms and a held target's chest -- this second mode is the mechanical "
            "delivery system for her signature Asphyxiation Field ability, described in-"
            "source as 'stealing the breath.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Pyro/Ignis Rexmar (extends ARS-190) ---
    {
        "id": "ARS-421",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-190 with full mechanics for Pyro's (Ignis Rexmar) three 'Heart's "
            "Tools,' none of them Living Drakma and none of them weapons in the conventional "
            "sense -- consistent with his locked status as Kanja's unknowing son who carries "
            "no forged inheritance. The Cian-Feast Kit is ordinary Dead Drakma kitchen "
            "implements that function as combat tools purely through his Thermal Variant "
            "biology heating any metal he grips to searing, cauterizing temperatures -- his "
            "kitchen-honed spatial/situational awareness doubles directly as combat instinct, "
            "and his food's already-locked biologically real performance/healing effect "
            "(MCD-7106, Metabolic Overdrive) is the same mechanism the crew experiences as "
            "'eating well before a fight.' Thermal Vents are a passive-to-active biological "
            "capability: a warming radiance at rest that the crew unconsciously gravitates "
            "toward, escalating under stress to involuntary heat spikes and, under fear or "
            "anger, a directed thermal blast that flash-ignites combustibles in a 5m cone -- "
            "tied directly to his emotional state, the mechanical reason the Triad Guardians' "
            "role includes keeping him emotionally stable. The Rexmar Apron has zero "
            "mechanical function, carried purely as dramatic-irony/identity texture against "
            "Mafesto, his unclaimed inheritance he doesn't know exists."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Valen (extends ARS-070) ---
    {
        "id": "ARS-422",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-070's naming-only Five-Weapon System list with full mechanical "
            "detail. The Duality: twin Living Drakma blades forged as a matched pair by "
            "House Valcari's own master armorer -- Old Dragon runs hot (dense, dark, heat-"
            "conducting, searing on contact; retaining this name per the five-judge fleet's "
            "plurality verdict, since MCD-302's own thinly-detailed, zero-Chronicle-usage "
            "Rexmar-lineage item of the same name is renamed instead, see MCD-302 amendment "
            "this batch), and the other, White Void, runs cold (pale, heat-absorbing, flash-"
            "freezing tissue at the wound site); paired strikes exploit thermodynamic shock. "
            "White Void's name corroborates the already-locked 'White Void Duel' (MCD-248, "
            "age 23) as the blade's own namesake origin scene. The Vertebrae: segmented "
            "Living Drakma linked by high-tensile cable, collapsing into nunchuck form or "
            "extending via magnetic alignment into a full quarterstaff, exploiting Valen's "
            "Precision Variant biology (CC-035) for leverage and reach against heavier "
            "opponents. The Law-Giver: a Living Drakma spear with a leaf-shaped Karesian head "
            "matching Onyx of Oblivion's own blade geometry scaled to polearm length, keeping "
            "opponents who outmass Valen at the range he dictates. The Talons: four Living "
            "Drakma daggers, each bio-tuned to Valen's own frequency for resonance-recall, "
            "designed for close-range Lethal Parity engagements against 20,000x-density "
            "targets (WC-024) -- the source names the set as a unit but does not give each of "
            "the four daggers an individual name, a genuine gap left open for future material "
            "per the fleet's verdict rather than an omission on this pass. The Spirit-Ward: a "
            "ceremonial Living Drakma blade inscribed with ancient Valcari frequency-maps, "
            "Valen's tool against Ever-Haunt and residual void-energy contamination -- it "
            "performs no Tongue-based exorcism, instead severing the frequency tether between "
            "contamination and host directly. Together, the five weapons are why T.D.K.'s "
            "Warbody rates Valen 'WORST CASE' (ARS-070) -- total range coverage rather than "
            "concentrated power."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Bloodreaver/Torian (extends ARS-090/CC-040) ---
    {
        "id": "ARS-423",
        "category": "avatar-arsenal",
        "statement": (
            "Extends ARS-090's naming-only Furnace Kit list with full mechanical detail, "
            "consistent throughout with Torian's already-locked Cruor-Kin near-boiling-blood "
            "biology and his physical/thermodynamic-only constraint (CC-040). Cinder-Gate "
            "Aegis: a Living Drakma shield with a Heat-Shear Rim held at Torian's own blood "
            "temperature (~96 degrees C) via forearm contact, cutting and cauterizing on "
            "contact. Temper Maul: a Living Drakma warhammer whose head tracks his blood "
            "heat, striking via a heat-crack-shatter Stress-Fracture Cascade -- the first hit "
            "heats the target material, the rapid post-withdrawal cooling induces thermal "
            "stress fractures, and a second hit lands on already-compromised material. "
            "Ventspikes: spring-loaded Drakma spikes in bracers, heated to blood temperature, "
            "giving his Cruor-Kin biology a controlled emergency thermal-discharge path. "
            "Slagline Chain: a heavy Drakma chain with weighted, heat-radiating ends, "
            "establishing a visible, glowing thermal perimeter marking his kill zone. Furnace "
            "Harness: torso/shoulder/upper-arm Living Drakma armor with integrated heat-sink "
            "channels and vent ports, actively managing his thermal output -- extends the "
            "already-locked Boiling Strait engagement (MCD-250, age 52), where he reverse-"
            "vents this same harness to raise a steam plume disabling an enemy Blight "
            "projector. The harness's visible smoke is framed, echoing the established Onyx-"
            "voice convention, against Mafesto's engineered theatrical smoke as biological "
            "necessity rather than performance."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Red Beard/Tarn Cestari (extends CC-021/022, MAW-079, MAW-121, ARS-250) ---
    {
        "id": "ARS-424",
        "category": "branded-arsenal",
        "statement": (
            "Extends CC-021/022/MAW-121 (Red Beard/Tarn Cestari: publicly 4,800x Branded "
            "Peak, actual concealed 16,000x, 247 documented Maw victories) with his personal "
            "three-piece gear set; consistent with ARS-250's already-resolved conflict-check, "
            "the gear runs entirely on inert Dead Drakma matching his public 4,800x persona "
            "rather than any frequency-craft or Living Drakma enhancement. The Cestari "
            "Cleaver: an ~80-kilogram single-bit Dead Drakma battle-axe with a salt-cured-"
            "hide-wrapped haft in Maw tradition, that crushes armor inward via raw kinetic "
            "delivery rather than cutting through it. The Pit-Shield: a 1.5-meter Dead "
            "Drakma tower shield, used in Maw tradition as an advancing wall, a battering "
            "ram, and a striking platform. The Cestari Brand-Knife: a plain ~15-centimeter "
            "Dead Drakma utility knife -- the only personal possession permitted a Cestari "
            "slave in the Maws -- used for the ritual self-scarification marking each "
            "survived bout; his 247 scars (matching MAW-121's locked victory count exactly) "
            "were each cut with this blade, which he still sharpens nightly as his last "
            "ritual before sleep. The Cleaver has been his since a Maw-3 championship bout, "
            "awarded as his right-of-victory prize under ordinary Maw custom -- unconnected "
            "to manumission status. He separately crossed the Directorate's own 3:1 "
            "financial manumission threshold at roughly the same point in his career "
            "(extends MAW-079's already-locked 'fewer than 200 Cestari in five thousand "
            "years'), resolving a real apparent conflict the source document's loose "
            "'granted manumission' phrasing raised, per the five-judge fleet's verdict -- but "
            "never formally activated or claimed it, choosing to remain inside the system, "
            "consistent with everything else locked about him (the Quiet Table, the Brand-"
            "Line correspondence) until his real, exercised freedom came via the Book 1 "
            "Unchained Legion defection (CC-023). All three gear pieces are carried forward "
            "from the Maw system itself rather than reforged or upgraded afterward, "
            "paralleling the already-locked precedent (ARS-260/MCD-246) of Kanja's own "
            "Rexmar Machete surviving unchanged alongside the Trinity's engineered gear -- "
            "both men keep the plainest, truest weapon they own rather than the most "
            "powerful one."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- The Rexmar Machete (extends ARS-260/ARS-346/349/356) ---
    {
        "id": "ARS-425",
        "category": "ancestral-blade",
        "statement": (
            "Extends ARS-260 (the Rexmar Machete: Kanja's ancestral, non-magical Dead Drakma "
            "field blade, passed father-to-son, predating the Trinity, never sealed in L9) "
            "with companion detail, consistent with the already-locked Long Mask timeline "
            "(MCD-246) and Sovereign Pier Accords (CC-009/MCD-085). The blade stayed on "
            "Kanja's belt continuously across his life and the full 284-year Long Mask -- "
            "worn at the Furnace District Strike (MCD-244, age 21) and at the Sovereign Pier "
            "-- and was the last weapon King Maro Rexmar saw his son carry before the "
            "surrender Maro himself had personally negotiated (CC-009). Physically: a worn, "
            "brass-riveted Dead Drakma laborer's tool whose handle is worn smooth by "
            "generational use and whose blade profile has narrowed roughly a centimeter "
            "through repeated sharpening across ownership predating Kanja, his father, and "
            "his grandfather. Framed, in the established Onyx voice, as categorically "
            "distinct from the Trinity: where Mafesto is 'the weapon of war' and Obsidian "
            "Malice 'the weapon of finality,' the Machete is 'the weapon of identity.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- SBD Small Arms (extends ARS-300/PH2-049; new, reframed per fleet verdict) ---
    {
        "id": "ARS-426",
        "category": "directorate-equipment",
        "statement": (
            "Extends ARS-300/PH2-049: SBD Dead Drakma small arms are real standard-issue "
            "sidearms and long-arms, kinetic-slug ammunition propelled by Drakma-powder "
            "charges -- and, per the already-locked world-tech constraint, mechanically "
            "incapable of harming any density-scaled combatant at any tier, baseline "
            "included, regardless of the weapon's own sophistication; their only real effect "
            "is against wholly unrated civilians and property. This reframes rather than "
            "adopts the source document's own claim that they mechanically wound baseline-"
            "through-Elite-Standard combatants, which is rejected outright per the five-judge "
            "fleet's unanimous verdict as a direct violation of the locked constraint. In-"
            "world they are a mark of institutional distrust and personal inadequacy -- an "
            "officer who carries one is read as lacking real density-craft or courage -- "
            "fitting the same bureaucratic-failure register already established for the SBD "
            "elsewhere (the Oracle Conflict Map apparatus, MCD-1727; its own informant-"
            "network errors, SBD-041 through 045)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

# --- Sanity checks ---
new_ids = [r["id"] for r in NEW_RULES]
assert len(new_ids) == 35, f"Expected 35 new rules, got {len(new_ids)}"
assert len(set(new_ids)) == len(new_ids), "Duplicate IDs within this batch"
collisions = existing_ids & set(new_ids)
assert not collisions, f"ID collision with existing ledger: {collisions}"

# --- Append new rules ---
ledger["rules"].extend(NEW_RULES)

# --- Amend MCD-302 in place: rename "the Old Dragon" -> "the Elder Wyrm" ---
amended = False
for r in ledger["rules"]:
    if r["id"] == "MCD-302":
        old_text = r["statement"]
        assert "'the Old Dragon'" in old_text, "MCD-302 no longer contains the expected phrase"
        r["statement"] = old_text.replace("'the Old Dragon'", "'the Elder Wyrm'")
        r["source"] = (
            r["source"]
            + " AMENDED Batch 308, 2026-09-25: renamed from 'the Old Dragon' to 'the Elder "
            "Wyrm' to resolve a real material-composition collision with a newly drafted "
            "Living Drakma sword of the same name belonging to Valen Sinisterblade (ARS-422), "
            "per the five-judge fleet's plurality verdict (this item had zero Chronicle usage "
            "to date, making it the lower-cost side of the rename)."
        )
        amended = True
        break
assert amended, "Failed to find and amend MCD-302"

# --- Batch log entry ---
batch_note = (
    "Abad's direction to resolve the six-agent Arsenal-of-Cian mining pass's seven flagged "
    "contradictions: \"let the fleet render a verdict.\" Five independent background-agent "
    "judges, no cross-talk, each rendered a full verdict on all seven items; verdicts were "
    "consolidated by plurality (weighted toward judges who verified against primary locked-"
    "source text, e.g. two judges independently confirmed via MAW-079 that Red Beard already "
    "carries a locked genuine manumission-threshold crossing) and presented to Abad in full. "
    "Abad's approval: \"lock it.\""
)
ledger["batches_completed"].append(
    {
        "batch": 308,
        "date": str(date.today()),
        "source": "Arsenal_of_Cian_Definitive_Edition_v2 (Google Drive)",
        "rule_count": len(NEW_RULES),
        "note": batch_note,
    }
)

ledger["ledger_version"] = f"{round(float(ledger['ledger_version']) + 0.1, 1):.1f}"
ledger["last_updated"] = str(date.today())

with open(LEDGER_PATH, "w", encoding="utf-8") as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
      f"Batches: {len(ledger['batches_completed'])}.")
