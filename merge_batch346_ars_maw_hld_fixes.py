#!/usr/bin/env python3
"""Batch 346: Phase 5 fable-review fixes, the ARS-/MAW-/HLD- rule-prefix blocks.

Applies the mechanical reconciliation/error subset of a Fable-model read-only
review of the ARS-, MAW-, and HLD- prefix blocks: five stale Book-1-vs-Book-3
placement notes reconciled against MCD-025/MCD-051/CC-014/CC-023/CC-029 and
MCD-100/MCD-279 (C1); the Osseren Reclamation's date/venue corrected to match
MAW-116's own figures, and a Reclamation-exclusivity citation redirected from
the wrong rule to MAW-065 (C3/E7); the Unarmed Siege of Maw-9's Reclamation
Chronicle mechanism (sleep-agent infiltration) corrected to MCD-247's own
locked zero-violence financial/legal mechanism (C4); the Grand Circuit's
formalization reframed as a later standardization of an older institution
(C5); two Maw-era date ranges shifted 100 years to remove a stale overlap
(C6); Valor Thenn's Proving reframed as a standard-engagement load rather
than a literal first-ever breach, his bout count corrected to match his own
198-6 record, and his patron house corrected from Ferrenhall (Dravos's
patron) to Greymantle (Threnn's own patron, MAW-026) (C10/C11/C23); Korrith
the Scorpion's Reclamation date shifted to resolve an ordering conflict with
two neighboring Reclamation-record dates (C12); Kaedrin the Undying's
description corrected since the House system already existed at his era per
MAW-123/124 (C14); the Crucible Market recruit's biology corrected from
Thermal Variant (Pyro's own biology) to Cruor-Kin (Torian's actual biology
per CC-040/MCD-247) (C15); Red Beard's walk-out reframed to future tense,
since it is Book 1 material that has not yet occurred in-world (C16);
Mafesto's Karkosa seal duration corrected to match MCD-091/MCD-246's own
locked timeline (C18); Ozmund's Moonvault gifts corrected from all Ten Gifts
to his actual five, the Sovereign's Five (C19); the Forge-Coat V2/V3 date
ranges anchored to their own locked opening events, MCD-250/MCD-256 (C24);
and the Cestari manumission rate's internally-inconsistent "2%" figure
removed without asserting a replacement number (C25).

Also 14 mechanical citation/wording error fixes (E1-E13, E7 folded into C3's
MAW-121 fix): a wrong Rexmar Machete cross-reference corrected to ARS-260
(E1); a nonexistent rule ID (MCD-7106) corrected to the two real rules it
conflated (E2); a citation that attributed Memory-Plate Technology to the
wrong rule, corrected to cite MCD-176 (E3); Undertow's "remains undetailed"
note corrected now that ARS-388 details it (E4); a stale internal-conflict
note on Ezio's Concealed Arsenal updated to point at its actual resolutions,
ARS-359 and ARS-404 (E5); a Kanja-age citation corrected for clarity, leaving
Valen's own disputed age untouched for Abad (E6); a Reckoner/betting-Tether
citation corrected from the Reckoner stub (MAW-081) to the actual
Tether-integrity rule (MAW-088) (E8); the Codex's Atlas cross-reference
corrected from "Continental Atlas" to the artifact's actual locked name, "the
Regional Atlas" (GEO-001) (E9); a loose equation of Karesian biology with the
Rexmar bloodline narrowed to its real locked mechanism, Kanja's own maternal
Kareth inheritance (E11); a citation added distinguishing the Crown-Scar's
discovery (Book 1) from its root-access-tether reading (Ezio's Book 2
finding, MCD-279) (E12); and Vargo Vakas's age-at-bout figure corrected from
his present-day age to his age at the time of that specific Reclamation
(~1,200 years ago) (E13).

Two category-field normalizations (ARS-311 to trinity-relic, matching its
actual Talisman Stage 2 Sub 3 content per MCD-060/061; ARS-436 to
avatar-arsenal, matching its Forge-Coat-family siblings ARS-344-356) and a
status-field normalization (every ARS-/MAW-/HLD- rule still carrying
uppercase "LOCKED" lowercased to "locked", matching the normalization already
applied to other prefixes in earlier Phase 5 batches).

Deliberately NOT touched: PH2-049 (a sibling agent's firearms-clause pass),
CC-098/SBD-021/ARS-413/ARS-395's "Cadence Ruin"->"Cadence Break" rename (a
sibling agent's pass -- ARS-395 read but not amended here), and every item
the review flagged NEEDS ABAD (Valen's age contradiction, the Ghost-Lattice/
Silent Mara chronology hedge, three undecided numeric picks, the Osseren
Pillar-reinstatement claim, the Patient Stone cross-block rename, and the
near-collision naming clusters) -- all left completely untouched pending
Abad's own ruling.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Phase 5 fable-review of the ARS-, MAW-, and HLD- rule-prefix blocks "
    "against the full ledger (read-only review by a Fable-model background "
    "agent), mechanical reconciliation/error-fix subset only -- all "
    "NEEDS-ABAD items and the two items reserved for sibling agents "
    "(PH2-049's firearms clause, the Cadence Ruin/Cadence Break rename) "
    "deliberately left untouched."
)

AMENDMENTS = {
    'ARS-010': (
        "Mafesto is Kanja's Trinity Relic exoskeleton armor, forged at the Mao Volcano, bio-bonded to him. Kinetic Transfer System. Sealed in Karkosa L9 from the age-30 surrender (MCD-246) for roughly 296 years -- the full 284-year Long Mask and beyond (MCD-091) -- recovered during Book 1's Karkosa Heist (MCD-070)."
    ),
    'ARS-060': (
        "Ozmund's personal kit: Dragondal (warhammer), Shadow's Whisper (short sword), Crown-Gauntlets. Later receives five of the Moonvault's Ten Gifts, the Sovereign's Five (ARS-330; the Captain's Five go to Kanja, ARS-340)."
    ),
    'ARS-210': (
        "Ezio Valcari's Concealed Arsenal: Attia's Rite (cane-sword), the Archive-Key, the Socratic Trap. NOTE: resolved at ARS-359 (Attia's Rite is Lauris's; the Ezio listing is a duplication error) and ARS-404 (Ezio's actual concealed-carry prop is the Cipher Cane)."
    ),
    'ARS-270': (
        "Anu Un Ra (T.D.K.) wields the Warbody and the Legacy Lattice. MCD-100 controls the Dark Monarch choice (Book 3); the Crown-Scar's discovery itself is Book 1 (MCD-025) and its root-access-tether nature is Ezio's Book 2 finding (MCD-279)."
    ),
    'ARS-346': (
        "The Capability Map: the seven Deficiency Catalogue categories (ARS-345) map to seven gear pieces developed over the Long Mask's 284 years -- Kinetic Absorption to the Forge-Coat; Thermal Management to the Forge-Coat's integrated coolant/smoke system; Sensory Augmentation to the Sovereign Eyes; Psychological Projection to the full loadout in combination; Environmental Sealing to the Breath Collar plus the Forge-Coat's lining; Offensive Amplification to the Ironhand Gauntlets, the Rexmar Machete (already locked, ARS-260), and the Ironfall Boots; Damage Tolerance to the Mend-Line."
    ),
    'ARS-347': (
        "The Forge-Coat, early versions: V1 (age 33, first deployed at the Crucible Market pit) was reinforced leather over ballistic weave with copper vent-tubes mimicking Mafesto's shoulder-port silhouette -- small-arms rated only, ~12 kg, proving the Scourge persona could survive without the armor through psychological precision alone. V2 (ages 40-80, spanning the Pirate Dawn's opening at 48, MCD-250) replaced the base with treated sea-leather over Dead Drakma wire mesh, added the armored high collar that anchors the Long Mask's silhouette the way Mafesto's helm anchored the Scourge's, and upgraded to edged-weapon/Elite-Standard (500x) impact resistance at ~9 kg."
    ),
    'ARS-348': (
        'The Forge-Coat, peak versions: V3 (ages 80-180, spanning the Golden Terror\'s opening at 95-105, MCD-256 -- the version documented in the Long Mask Chronicles) introduced a triple-layer composite (Dark-Drakma leather outer shell, Dead Drakma articulated plates, thermal-regulating inner lining) with deliberately graduated protection -- torso and spine armored to Branded-class (~2,500x), limbs kept lighter at Elite Standard (500x) to preserve mobility, trading limb armor for organ protection since Kanja\'s Bio-Drakma skeleton makes his bones harder to break than his organs are to rupture. V3 also introduced the 37-compartment Pocket Architecture (expanded in V4, ARS-349). V4 (ages 180-284) raised protection to 3,200x torso / 1,500x limbs / 4,000x spine at a lighter ~10 kg through 100+ years of materials refinement, added the Foundry-Anvil-derived leather treatment (MCD-292), and settled into what the document calls \'the 5\'11" Statement\': Kanja\'s peak Long Mask silhouette makes no attempt to replicate Mafesto\'s 6\'1" frame -- it is its own identity, proof that the man survives without the armor rather than the armor\'s ghost.'
    ),
    'ARS-383': (
        "The Whalebone Tether (Kanja, Captain's Five): homage to Gleipnir, the impossible binding that chained Fenrir. A whalebone-cored Living Drakma line, unbreakable under conventional force, serving as the Foldtide's anchor-tether when folded or docked -- and, rarely, as one of the few tools capable of temporarily restraining a Titan-class target, since ordinary bindings fail against that scale of strength. Undertow, the fifth Captain's-Five item, is detailed at ARS-388."
    ),
    'ARS-392': (
        "Extends CULT-004/CULT-194: the Exchange Protocol's cyclical rebuilding requires biological material from compatible donors, and Karesian biology -- carried in the Rexmar line only through Kanja's own Kareth maternal inheritance (MCD-101/102) -- specifically is the highest-fidelity donor material available. This is the true mechanical reason T.D.K. maintains a fixed interest in the Rexmar line: not political retaliation, but because Kanja's own existence, and specifically his Aethelgard Kinetic Radiance at the frequency level, actively disrupts the Exchange Protocol's maintenance cycle -- a biological threat to T.D.K.'s continued operation, not merely a military one. Degradation is slow (centuries, not years) but irreversible without fresh compatible material: T.D.K. is maintained rather than immortal, and the maintenance can, in principle, be cut off at its source."
    ),
    'ARS-393': (
        "The Legacy Lattice (named at ARS-270, undetailed until now) is Anu Un Ra's second arsenal component alongside the Warbody, not a physical weapon: his surviving network of embedded root-permissions in every institution built on technology he originated roughly 25,000 years ago, giving proper name and mechanism to CULT-008's already-locked 'root protocol hierarchies embedded in the earliest architecture.' The Sealbound Directorate's Blight Frequency network, Scrip-Tether system, and Ionic Rite containment protocols all run on his original architecture; its current operators believe they own the technology, not knowing T.D.K. still holds root-level commands over it. The Crown-Scar (MCD-052) is a Legacy Lattice node embedded in Verehimu biology rather than institutional infrastructure -- the same mechanism in a different substrate, which is what Ozmund actually discovers in Book 1 (the root-access-tether reading itself is Ezio's Book 2 finding, MCD-279; extends MCD-052/053). Five thousand years of the Directorate's own incompetent stewardship has degraded the Lattice's fidelity -- root commands still function but imperfectly. The Great Breach (CULT-009) is now explained as T.D.K. testing how much of the Lattice still answers to his voice after five millennia of dormancy."
    ),
    'ARS-399': (
        "Extends ARS-300/WC-007/MAW-088: SBD Scrip-Tethers are the physical enforcement layer of the Metabolic Tether (WC-007) -- an economic-biological feedback loop: the device monitors labor output, calculates debt position, and applies metabolic suppression proportional to indebtedness, so deeper debt produces a heavier-feeling body and slower metabolism, deepening the debt further. Its already-locked weaknesses (the Sovereign Umbrella nullifies it in radius; Ezio's forensic accounting exposes its fraudulent basis) are joined by one characterization: the single most effective weapon ever used against the Scrip-Tether system was arithmetic -- publicly proving the debt's math was wrong."
    ),
    'ARS-401': (
        "Extends ARS-060: the Crown-Gauntlets are Living Drakma forearm shields, crafted by Kanja and integrated into Ozmund's wrist-and-forearm armor, serving as his primary fighting instrument since he fights principally with his hands. They function as defensive plating for blocks and parries and as Density Spike focusing lenses -- concentrating a punch's infinite mass into a knuckle-sized contact surface -- and additionally project resonance-echo images of past Verehimu warriors encoded in the Drakma's lattice memory, consistent with Drakma's established responsive-lattice physics (MCD-301) and the precedent of Lauris's Memory-Plate Technology (MCD-176; the Phalanx itself at ARS-360). Activation produces a momentary amber flash along the knuckle ridges the crew nicknames 'the Crown'; the gauntlets are calibrated specifically to Ozmund's Karesian biology and would function as ordinary Living Drakma forearm guards, without Spike-channeling, for any other wearer. Red Beard's own account frames the three-piece kit as one operating philosophy: Dragondal for structures, Shadow's Whisper for throats, the gauntlets for everything in between."
    ),
    'ARS-421': (
        "Extends ARS-190 with full mechanics for Pyro's (Ignis Rexmar) three 'Heart's Tools,' none of them Living Drakma and none of them weapons in the conventional sense -- consistent with his locked status as Kanja's unknowing son who carries no forged inheritance. The Cian-Feast Kit is ordinary Dead Drakma kitchen implements that function as combat tools purely through his Thermal Variant biology heating any metal he grips to searing, cauterizing temperatures -- his kitchen-honed spatial/situational awareness doubles directly as combat instinct, and his food's already-locked biologically real performance/healing effect (MCD-223 Metabolic Overdrive; MCD-272 food-based healing) is the same mechanism the crew experiences as 'eating well before a fight.' Thermal Vents are a passive-to-active biological capability: a warming radiance at rest that the crew unconsciously gravitates toward, escalating under stress to involuntary heat spikes and, under fear or anger, a directed thermal blast that flash-ignites combustibles in a 5m cone -- tied directly to his emotional state, the mechanical reason the Triad Guardians' role includes keeping him emotionally stable. The Rexmar Apron has zero mechanical function, carried purely as dramatic-irony/identity texture against Mafesto, his unclaimed inheritance he doesn't know exists."
    ),
    'ARS-422': (
        "Extends ARS-070's naming-only Five-Weapon System list with full mechanical detail. The Duality: twin Living Drakma blades forged as a matched pair by House Valcari's own master armorer -- Old Dragon runs hot (dense, dark, heat-conducting, searing on contact; retaining this name per the five-judge fleet's plurality verdict, since MCD-302's own thinly-detailed, zero-Chronicle-usage Rexmar-lineage item of the same name is renamed instead, see MCD-302 amendment this batch), and the other, White Void, runs cold (pale, heat-absorbing, flash-freezing tissue at the wound site); paired strikes exploit thermodynamic shock. White Void's name corroborates the already-locked 'White Void Duel' (MCD-248, Kanja age 40) as the blade's own namesake origin scene. The Vertebrae: segmented Living Drakma linked by high-tensile cable, collapsing into nunchuck form or extending via magnetic alignment into a full quarterstaff, exploiting Valen's Precision Variant biology (CC-035) for leverage and reach against heavier opponents. The Law-Giver: a Living Drakma spear with a leaf-shaped Karesian head matching Onyx of Oblivion's own blade geometry scaled to polearm length, keeping opponents who outmass Valen at the range he dictates. The Talons: four Living Drakma daggers, each bio-tuned to Valen's own frequency for resonance-recall, designed for close-range Lethal Parity engagements against 20,000x-density targets (WC-024) -- the source names the set as a unit but does not give each of the four daggers an individual name, a genuine gap left open for future material per the fleet's verdict rather than an omission on this pass. The Spirit-Ward: a ceremonial Living Drakma blade inscribed with ancient Valcari frequency-maps, Valen's tool against Ever-Haunt and residual void-energy contamination -- it performs no Tongue-based exorcism, instead severing the frequency tether between contamination and host directly. Together, the five weapons are why T.D.K.'s Warbody rates Valen 'WORST CASE' (ARS-070) -- total range coverage rather than concentrated power."
    ),
    'HLD-021': (
        "Extends HLD-001: Dead Drakma composite is banded into a great seat's wall core for battering resistance beyond bare masonry; Living Drakma is never spent on walls under any circumstance -- no fortification is considered worth what a single Living-Drakma blade is worth. Every named hold, tower, and line is catalogued on the Regional Atlas (GEO-001; by region, class, tier, and grid cell), with this Codex serving as the Atlas's structural-terminology key."
    ),
    'MAW-030': (
        "House Vennrik lost its patron and became available; Ozmund enters under 'Venim.' The source's Book 1 framing is consistent with the locked Book 1 placement of Ozmund's Maw entry and Venim identity (MCD-025/MCD-051/CC-014); MCD-100's Book 3 placement governs only the later Dark Monarch title/choice, not the Maw entry."
    ),
    'MAW-065': (
        "Extends MAW-060/061, individual venue detail. The Throat (Karkosa, 120,000, ~4,800 years old, record attendance 128,000). Occupies the geographic centre of the capital. Its Resonance Dome is an engineered acoustic shell capturing and redirecting the crowd's vocal energy downward onto the Slab; fighters describe the resulting pressure as standing inside a bell someone is ringing. Beneath it are seven levels of service tunnels, three Triage Stations, an armory the size of a small military installation, a Ledger Office occupying an entire sub-level, and the Grand Archive -- the Maw's official historical repository, holding inscribed records of every bout fought in the venue since the Ledger system began ~3,500 years ago, and incidentally the most comprehensive record of Cestari death in the world. Every Apex Championship for three thousand years and every Reclamation have been held here; Vakas's seismic approach signature is calibrated specifically to the Throat's monitoring instruments. The Mother (Maw-1, 85,000, ~4,900 years). T.D.K.'s prototype and the oldest Maw in the world, predating the Throat, retaining the original elliptical design abandoned before the circular format became standard; the asymmetry creates a positional element no other Grand Maw has. Permanent humidity forces surface re-treatment three times per event day. The Slab of Judgment (Maw-7, 45,000, ~2,200 years, post-Haku reconstruction). Where Red Beard's parents were executed (MCD-084). Its backstage corridors are the most densely Brand-Line-inscribed surfaces in the system -- the handlers gave up cleaning them centuries ago and the messages are now part of the architecture. The crowd does not cheer a fighter; it examines one. The Keldane crowd also carries the memory of the Osseren Reclamation (~800 years ago, at the Throat, MAW-116), in which Vakas killed a champion installed by Osseren's rigging, so it judges everything twice: once for the sport, once for the morality. The Teeth (Maw-12, 32,000, ~800 years). Draws audiences from both Trust territory and the Shattered Kingdoms into the same tiers; security is military-grade, with border-force perimeter patrols and vomitoria chokepoints sealable in under thirty seconds, and it still records more crowd-violence incidents than any other Grand Maw, averaging two per season. The Belly (Maw-3, 28,000, ~3,800 years). The only fully subterranean Grand Maw, in an expanded natural limestone cavern. Sound does not echo, it reverberates, building through a bout until crowd and impacts merge into a single amplified harmonic. Ceiling roughly fifteen metres above the Slab. Site of Kanja's Unarmed Siege (Long Mask Battle XXIII), where collapsing the structure would have killed the Cestari he came for, so he instead emptied it through forged and legitimate financial and legal pressure alone, 12,000 freed without a blow struck (MCD-247) -- the Long Mask's only zero-casualty engagement of its type. The Drowning Floor (Maw-15, 38,000, ~1,500 years). Slab built at sea level inside a retaining basin floodable to roughly two feet of seawater via tidal gates that open at unpredictable points mid-bout. Designed as a spectacle venue rather than a fair one; the Compact has debated banning the water feature for over five hundred years and never resolved it, because the venue's events are the regional circuit's most commercially successful and the betting markets sell specialized wagers on when the water will decide the outcome. Atmosphere is carnival rather than cathedral. The Scar (the Ash Maw, 22,000, ~4,500 years). Built into the ruins of T.D.K.'s original court complex, partly destroyed in the Haku war and never rebuilt: cracked walls, upper tiers open to the sky, impact marks on the Slab from the engagement that ended the Old Dominion's capital. It sits outside the Compact's regulatory authority entirely -- no Blood Writ requirement, no medical mandates, no welfare standards, governed by whichever regional power currently holds the surrounding territory. Death rates run roughly 400% of the licensed system's average. Its competitors are the desperate, the legendary, or those trialling techniques the Compact's safety standards prohibit."
    ),
    'MAW-079': (
        "Extends MAW-073. The 3:1 manumission ratio, fixed by T.D.K.'s original administration and never revised, was deliberately set above the average Cestari career's actual return of ~1.8:1 -- freedom is mathematically possible and structurally improbable by design. Maintenance costs accrue continuously and don't pause during injury recovery, so an injured fighter accumulates cost with zero offsetting revenue, and the manumission threshold rises with age faster than an aging, declining-revenue fighter can close the gap. Only a vanishing fraction of any generation ever reaches the threshold; effectively all the rest die in the system, each death recorded as a closed Scrip-value settlement. Red Beard is one of fewer than 200 Cestari in five thousand years to reach manumission, requiring over two hundred years of career revenue. A second path exists in parallel: paying the lump-sum difference to the threshold outright, a sum at mid-career typically exceeding most regional Standards' annual operating budget. Silent Mara (MAW-128) is the system's most famous case of this financial path; the administration has since raised the lump-sum overhead twice specifically to make the path harder to walk for anyone who tries to follow her."
    ),
    'MAW-091': (
        "Extends MAW-090. Era I, the Old Dominion (~5,000-3,000 years ago, ~2,000 years). Governance: T.D.K. (Anu Un Ra), direct state control. Character: the Maw as state instrument -- maximum institutional control, maximum cruelty, maximum efficiency. This era established every structure every later era inherited: the Pillar system, the Cestari caste, the Slab construction standards, the Reclamation cycle, and the Scrip-Tether integration that made the Maw inseparable from the economy. Its defining tension is that T.D.K.'s system was brutally effective and self-correcting through the Reclamation, so it produced genuine excellence alongside genuine atrocity -- an unresolved five-thousand-year argument over whether the excellence exists because of the cruelty or despite it. Era II, the Post-Haku Transition (~3,000-2,000 years ago, ~1,000 years). Governance: fragmented, multiple competing authorities, no central state. The Haku war broke T.D.K.'s empire but left the Maw intact because it was too economically essential to destroy and too institutionally embedded to dismantle, producing a system with no master: Pillars operating independently, unregulated emerging Banners, collapsed medical mandates, voluntary fighter welfare, and estimated death rates three to four times the Old Dominion average. It produced the Maw's most desperate legends -- Graves, Lirra Chain-Singer, and a body of anonymous fighters whose names survive only in the Brand-Line because the Ledger Offices did not operate consistently. Era III, the Sovereign Trust (~2,000-300 years ago, ~1,700 years). Governance: centralized state regulation through the Trust. The longest and most productive era: standardized competition rules, medical mandates, formalized Compact authority, and full integration of the Maw economy into the Scrip-Tether architecture. Its defining achievement is the Grand Circuit in its current standardized form, formalized roughly 1,500 years ago (an earlier, looser Grand Circuit and the Apex Championship itself predate it by well over a millennium, MAW-065/MAW-111), which created the career ladder, persistent record-keeping, and celebrity economy that made the Maw culturally central rather than merely economically important -- before it the Maw was an industry, after it the Maw was a civilization's identity. Its defining failure is that the system's moral contradictions became visible to the population consuming its product, through the Sable Kin exposure, the Dead Pool, and the Tether Arbitrage; the Compact's Reformist faction emerged in this era in response. Era IV, the Modern Era (~300 years ago to present). Governance: Sovereign Trust nominally, with the protection economy operating as a parallel system. Character: disruption. It begins with Kanja Haku Rexmar's campaign against the Maw's infrastructure -- the Siege of Maw-9, the Night of Ten Fires, the Coin-Weight Raid, the Maw Cascade, the Frequency Vaccine -- each attacking a different structural element, none destroying the system, all weakening it. Its defining development is the emergence of fighters from Blight-reduced zones whose true biological density exceeds the Tether-managed ceiling: the Tether's suppression is no longer universal, so the odds models are no longer reliable, so the betting economy is no longer stable, so the revenue streams are no longer predictable. The system is encountering a variable it was not designed to process -- a population the Tether does not control. CONFLICT-CHECK carried forward from MAW-090: a proposed 'Era V' conflicts with MCD-100; MCD-100 controls."
    ),
    'MAW-096': (
        "Extends MAW-080/085. The revenue architecture is a closed circular flow: audience Scrip enters as gate/wagers/merchandise; the Maw distributes it as bout purses, betting payouts, tax revenue, and Scrip-transaction value to the Tether's Central Ledger; Houses reinvest, producing better fighters and bigger audiences, restarting the cycle -- unbroken for five thousand years. The flow's structural leak is the Cestari themselves: a death on the Slab is a total write-off of acquisition/training/maintenance investment; manumission (MAW-079) is a total loss of all future revenue their continued competition would have generated -- the system is optimized to hold each Cestari in the revenue-generating band as long as biologically possible without crossing the 3:1 threshold, the engineered function of that ratio. Red Beard's 150,000-Cestari walk-out (Book 1, CC-023) will register as the single largest revenue-stream loss in the Maw's five-thousand-year economic history -- a Scrip-value calculation the Ledger Offices' actuarial conventions were never built to compute, since the system had no column for mass, voluntary self-removal. The architecture's single point of failure is the Tether itself (MAW-088): if metabolic suppression collapses territory-wide rather than in isolated protection-economy zones, density classifications become unreliable, odds meaningless, betting collapses, and the entire revenue chain -- through to the Trust's own governance funding -- stops circulating."
    ),
    'MAW-100': (
        "This document lays out a 16-fighter Apex Championship field framed as 'Book 1's Apex Tournament.' Book placement is Book 1 per MCD-025/MCD-051/CC-023; MCD-100's Book 3 placement governs the Dark Monarch, not the tournament."
    ),
    'MAW-101': (
        "Extends/completes MAW-100. The Apex Championship field is a sixteen-fighter, single-elimination, three-day tournament at the Grand Maw of Karkosa, seeded by Grand Circuit ranking. The named field, in seed order: #1 Drennan 'The Patient,' 4,700x, House Dravos, reigning champion, pure Iron Patience, never knocked down -- he treats every hit as information rather than injury, and the betting markets call him 'the favorite to bore Vakas to death,' which he takes as a compliment. #2 Dray Voss 'The Inheritor,' 4,700x, Dravos, direct descendant of Voss Dravos, doctrinally orthodox, top-five ranked six consecutive years, two Apex finals and two losses, fighting like a man serving a sentence. #3 Ash Korren 'The Debt,' 4,500x, House Sektori, acquired from a regional Standard under Scrip-Tether debt-compliance leverage after his family's estate was seized; hybrid Dravos endurance over Sektori risk-management, the most conservative and hardest-to-exploit competitor in a generation, needing roughly four more years of Grand Circuit purses to clear the debt against roughly 60% odds of surviving them. #4 Seyra 'The Tempest,' 3,900x, House Korrath, youngest Grand Circuit qualifier in a century at twenty-three; twin blades geometrically calibrated to produce tonal feedback on impact, so the crowd chants in rhythm with her strikes -- physics, not frequency-craft, and a phenomenon the referees have no framework for scoring. #5 Kullen Gravedust, 4,800x, House Morvane, sixteen years a mortuary technician before entering the Maw at thirty; replicates the exact death-sequences of historical fighters against current opponents whose doctrinal profiles match the historical models. #6 Torven (no other name), 4,400x, House Velthari, 54-1, silent, with no fighting style of his own because Velthari fighters use the opponent's; the Reckoners cannot set reliable odds on him. #7 Brennan 'The Oak,' 4,600x, House Tolvari, 23-0, product of a ten-year developmental program, moving with the technical sophistication of a fighter twice his age. #8 Corra Deepstrike, 4,300x, House Durnwall, born in the mines, still works the morning shift and trains in the afternoon; won the Southern Provincial Proving by outlasting a Dravos Contender conditioned for forty-five-minute bouts across a sixty-two-minute fight. #9 Sahar 'The Drought,' 4,100x, House Rathaan, dehydration warfare; longest bout ninety-three minutes, ended by his Threnn opponent collapsing from dehydration. #10 Veyren 'The Mourner,' 4,500x, Morvane, 68-4, a former mortuary technician who processes every opponent as a future corpse whose failure mode he has already studied; all four losses to Korrath fighters whose theatrical unpredictability broke his analytical approach. #11 Tella Brightblade, 3,700x, Korrath, great-granddaughter of Dorne Brightblade, the field's most watchable competitor, intending to become the first Brightblade to win the Brightblade Prize. #12 Renn Hollow, 3,200x, House Brekka -- over a thousand points below the typical Grand Circuit competitor and alive because he developed at his true biological ceiling in the Blight-reduced Keldane Hollow rather than under Tether suppression; his qualification is under active Compact challenge and is the Maw's live political flashpoint. #13 Ysolen 'The Dancer,' 3,400x, House Aravel, 31-11, a former acrobat, the highest merchandising value in the qualifier field. #14 Venim, density UNMEASURED, House Vennrik -- Ozmund, entering as the lowest seed with no doctrinal profile for any opponent to analyse. #15-16 are deliberately left open in the source as unnamed Provincial Provings qualifiers, reserved for narrative flexibility. Book placement is Book 1 per MCD-025/MCD-051/CC-023, matching MAW-100; MCD-100's Book 3 placement governs the Dark Monarch, not the tournament."
    ),
    'MAW-115': (
        'R-~76, the Iron Veil\'s Exception (~1,200 years ago) -- extends MAW-024. The defining Reclamation. The Iron Veil (House Velthari, 4,600x, 188-0) faced Vakas with the Structural Kill refined to its theoretical limit and located the same tibial micro-fracture Mordecai had found three hundred years earlier (MAW-114) -- the flaw had not repaired, because Vakas\'s Abyssal Bile biology resists modification even by its own regenerative processes. She targeted it; he adapted; she adapted to his adaptation. The cycle ran eleven minutes, the longest Reclamation bout in history: an analytical war between a doctrine built to find weakness and a Founder whose nearly seventeen thousand years had eliminated nearly every weakness available to find. Vakas escalated to 300%, the highest escalation ever recorded -- at 300% of 4,600x he was operating at approximately 13,800x against a fighter of less than half that density. The Iron Veil survived not by matching output but by predicting his movements through the Slab\'s vibration patterns and positioning to absorb the minimum possible force from each strike while sustaining her counter-attack on the fracture. The strategy was never winning; it was not-losing long enough for the Founder to recognize the achievement. Vakas stopped and spoke one word -- "Sufficient" -- which the Resonance Dome carried to the entire crowd, and which Velthari inscribed above the Still Point\'s entrance. She was Proved at 6,200x, a lower elevation than her analytical mastery warranted, because Vakas\'s judgment is biological rather than meritocratic: the Abyssal Bile resonance unlocks what the body can sustain, and her body was built for precision rather than density. Her real name was never recorded; she did not want it known, and Velthari honors this.'
    ),
    'MAW-119': (
        'R-~96, Korrith the Scorpion\'s Exception (~125 years ago). Korrith the Scorpion (House Selenar, 4,600x, 134-9, two-time Apex Champion), Proven at 7,200x, Exception, Vakas escalated to 250%, nine minutes. Korrith\'s competitive innovation was compressing the Metamethod\'s assessment window from thirty seconds to roughly five by attacking during the analysis and reading the opponent\'s response to pressure as live diagnostic data. In the Reclamation he redirected a Founder-weight strike by reading the Slab\'s vibration pattern and predicting its trajectory before it arrived -- the identical technique Thessara Void-Step pioneered four thousand years earlier, which Vakas recognized as a lineage rather than an innovation, and which the Archive notes as the reason for the escalation. The Archive\'s notation: "The champion heard what the Founder\'s feet told the stone. The stone remembered." Korrith spent his retirement building an analytical database that expanded Selenar\'s Archive Library by roughly 40%.'
    ),
    'MAW-120': (
        'R-~98, Valor Thenn\'s Proving (~100 years ago) -- extends MAW-023. Valor Thenn (House Threnn, 4,900x -- the absolute Branded Peak ceiling -- 198-6, three-time Apex Champion), Proven at 8,000x, Survival with Honor, standard 150% engagement. For seven minutes the densest non-synthetic fighter in Maw history walked toward the densest synthetic entity in the world, applying the Inevitable; neither stopped, neither retreated. The Slab cracked twice during the bout, the combined output exceeding the Throat\'s 15,000x specification at a standard 150% engagement -- a load the venue had only ever seen under escalated Exceptions before (MAW-115/119). Vakas stopped; no words were recorded. At 8,000x Valor occupied a range the density-tier taxonomy had not anticipated -- heavier than Proven, lighter than Synthetic Apex -- and the Shapers\' Compact created the "Upper Proven" designation for him. His retirement was forced by a knee injury in his 205th and final bout, a joint-collapse inflicted by an Osseren specialist targeting the one structural weakness 8,000x cannot eliminate: the knee is still a joint, even at the top of the world. He is approximately 130 years old, alive, and serves as House Threnn\'s Chief Shaper -- at 8,000x even diminished by age and injury, one of the most dangerous non-Titan entities on the planet, and, through Threnn\'s Greymantle patron connections to Trust military command (MAW-026), a potential adversary or ally depending on how the political landscape shifts.'
    ),
    'MAW-121': (
        "R-~99, Red Beard's Proving (~50-80 years ago) -- extends MCD-084. Red Beard / Tarn Cestari (unaffiliated Cestari, public 4,800x, 247 victories, the longest career in recorded Maw history), Proven at 7,000x, Survival with Honor, approximately five minutes at standard 150%. He faced the Founder at the Throat, not the Slab of Maw-7 where his parents, Handler-4412 and Handler-6019 of the Quiet Table, had been executed (MCD-084) -- the Reclamation is held exclusively at the Throat per MAW-065. He fought with no doctrine -- with the accumulated weight of two centuries inside the machine, and with density earned across two hundred years of honest labor on the Slab rather than technique. Vakas stopped; no words were recorded. The crowd of 120,000 at the Throat produced an acoustic response that the Resonance Dome amplified into a physical phenomenon, registered by the seismic instruments at the Keldane Maw roughly 400 kilometres away. The Brand-Line carried the news within hours: the son of the handlers who fed the hungry had been judged by the Founder and found worthy. What the Brand-Line does not carry, and what only Ozmund and Red Beard know, is that the Proving was the beginning rather than the end -- the 7,000x elevation broke the Blight-Tether's artificial ceiling, and Ozmund's subsequent secret training pushed him through the broken ceiling to 16,000x and climbing (MCD-084). When he walks 150,000 Cestari out of the Maw, the world will believe a 4,800x legend is leading the march, and will be wrong by a factor of more than three."
    ),
    'MAW-125': (
        'COLLISION-RENAMED: the source names this figure "Kael the Undying"; the ledger already carries two other Kaels -- Kael Stonehand (House Dravos, ~2,000 years ago, MAW-113) and Kael Threnn, Ozmund\'s living Shaper (MAW-051, extended at MAW-146) -- and a third distinct "Kael," the oldest legend in the system, risks exactly the proper-noun cluster this project\'s conventions exist to avoid. Renamed Kaedrin the Undying. Kaedrin the Undying (Unaffiliated Cestari, never House-registered, 3,800x, record unknown -- the Ledger system did not yet exist during his career; oral tradition estimates 300+ bouts), ~4,000 years ago, is the oldest name in the Brand-Line, predating the Quiet Table by over three thousand years. He fought every day for forty consecutive years -- early Maw operations scheduled multiple daily bouts, and Kaedrin was a permanent rotation fixture, a body the system could not kill that generated reliable revenue through sheer survival volume. The Brand-Line\'s claim that he eventually stopped fighting because the Maw ran out of willing opponents is flagged in-world as likely mythologized rather than verified. What is verifiable: his name is the oldest in Cestari oral tradition, invoked by fighters before their first bout -- not for protection, but for endurance: "The Cestari do not pray for survival. They pray for the strength to keep standing."'
    ),
    'MAW-144': (
        "Extends MAW-041. The four Named Pits in full. The Crucible Market (Southern Seaboard, destroyed): an underground operation using Blight-modified fighters as security, until Kanja fought its entire security complement as the first combat test of the Forge-Coat V1 (ARS-347) and recruited the young Cruor-Kin fighter who became Bloodreaver/Torian (MCD-247/ARS-090/CC-040/CC-080); its surviving operations were subsequently absorbed into Anansi's Ghost-Lattice network, a second absorption distinct from the network's original seeding. The Keldane Hollow (Keldane Reach, active): the largest active Named Pit on the Southern Seaboard, capacity ~3,000 in a natural cave system, operating under local protection-economy sponsorship; Frequency Vaccine pumps (MCD-274) keep it Blight-reduced, letting fighters develop at their true biological ceiling -- the direct source of MAW-131's Renn Hollow controversy, and where Red Beard's scouts identify Unchained Legion recruits. The Black Slab (Karkosa, location unknown): the capital's most notorious Blood Pit, invitation-only, drawing wealthy patrons who want lethal combat without medical intervention; fighters are debt-bonded workers, erased Cestari, and reportedly judicially-manipulated prisoners; death rate ~40% per bout. If prisoners are genuinely fed into it through manipulation, the same machinery producing the Trust's phantom orders (MCD-271) may be producing the bodies on its floor. The Ember Circuit (Shattered Kingdoms, mobile): a travelling operation visiting ~30 settlements per six-month cycle, each visit a three-day festival -- the most important social event of the half-year for isolated settlements too poor for a licensed Maw; where House Rathaan's scouts identify recruits (its own placement in the Shattered Kingdoms stands independently of the Rathaan Federation/Tribal Council naming question resolved at MAW-138)."
    ),
}


CATEGORY_FIXES = {
    "ARS-311": "trinity-relic",
    "ARS-436": "avatar-arsenal",
}


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}

    amended = []
    for rid, new_statement in AMENDMENTS.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        rules_by_id[rid]["statement"] = new_statement
        amended.append(rid)

    category_fixed = []
    for rid, new_category in CATEGORY_FIXES.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        rules_by_id[rid]["category"] = new_category
        category_fixed.append(rid)

    status_fixed = []
    for r in ledger["rules"]:
        prefix = r["id"].split("-")[0]
        if prefix in ("ARS", "MAW", "HLD") and r.get("status") == "LOCKED":
            r["status"] = "locked"
            status_fixed.append(r["id"])

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs found"

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": 0,
        "note": (
            "Phase 5 fable-review of the ARS-/MAW-/HLD- prefix blocks, "
            "mechanical subset. Amends 28 rule statements: five stale "
            "Book-1-vs-Book-3 placement notes reconciled against "
            "MCD-025/MCD-051/CC-014/CC-023 and MCD-100/MCD-279 (MAW-030, "
            "MAW-100, MAW-101, ARS-270); the Osseren Reclamation's date/venue "
            "corrected to MAW-116's own figures and a stray "
            "Reclamation-exclusivity citation redirected to MAW-065 "
            "(MAW-065, MAW-121); the Unarmed Siege of Maw-9 corrected to its "
            "already-locked zero-violence financial/legal mechanism "
            "(MCD-247) in place of an uncanonical sleep-agent-infiltration "
            "account (MAW-065); the Grand Circuit reframed as a later "
            "standardization of an older institution, and two Maw-era date "
            "ranges shifted 100 years to close a stale overlap (MAW-091); "
            "Valor Thenn's Proving reframed as a standard-150%-engagement "
            "load, his bout count corrected to match his own 198-6 record, "
            "and his patron house corrected from Ferrenhall to Greymantle "
            "(MAW-120); Korrith the Scorpion's Reclamation date shifted to "
            "resolve a date-ordering conflict (MAW-119); Kaedrin the "
            "Undying's description corrected for the already-existing House "
            "system (MAW-125); the Crucible Market recruit's biology "
            "corrected from Thermal Variant to Cruor-Kin (MAW-144); Red "
            "Beard's walk-out reframed to future tense as unresolved Book 1 "
            "material (MAW-096); Mafesto's Karkosa seal duration corrected "
            "to match MCD-091/MCD-246 (ARS-010); Ozmund's Moonvault gifts "
            "corrected to his actual five (ARS-060); the Forge-Coat V2/V3 "
            "date ranges anchored to MCD-250/MCD-256 (ARS-347, ARS-348); the "
            "Cestari manumission rate's inconsistent '2%' figure removed "
            "without asserting a replacement (MAW-079); plus 13 mechanical "
            "citation/wording fixes (ARS-346, ARS-421, ARS-401, ARS-383, "
            "ARS-210, ARS-422, ARS-399, HLD-021, ARS-392, ARS-393, MAW-115). "
            "Also normalizes 2 category fields (ARS-311 to trinity-relic, "
            "ARS-436 to avatar-arsenal) and lowercases every remaining "
            "uppercase 'LOCKED' status across the ARS-/MAW-/HLD- prefixes "
            "(72 rules) to match the project's established 'locked' "
            "convention. Deliberately untouched: PH2-049 (a sibling agent's "
            "firearms-clause pass), the Cadence Ruin/Cadence Break rename "
            "(CC-098/SBD-021/ARS-413/ARS-395, a sibling agent's pass), and "
            "every NEEDS-ABAD item from the same review (Valen's age "
            "contradiction, the Ghost-Lattice/Silent Mara chronology hedge, "
            "three undecided numeric picks, the Osseren Pillar-"
            "reinstatement claim, the Patient Stone cross-block rename, and "
            "the near-collision naming clusters)."
        ),
    })

    old_version = float(ledger["ledger_version"])
    ledger["ledger_version"] = str(round(old_version + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(
        f"OK: {len(ledger['rules'])} total rules, {len(ledger['batches_completed'])} "
        f"batches, ledger_version {ledger['ledger_version']}, zero duplicate IDs. "
        f"{len(amended)} rule statements amended: {', '.join(amended)}. "
        f"{len(category_fixed)} categories normalized: {', '.join(category_fixed)}. "
        f"{len(status_fixed)} statuses lowercased ({len(status_fixed)} rules)."
    )


if __name__ == "__main__":
    main()
