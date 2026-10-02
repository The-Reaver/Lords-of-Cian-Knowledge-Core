#!/usr/bin/env python3
"""Batch 344: Phase 4 fable-review mechanical fixes across the PH2-, WC-,
POL-, VB-, and COS- rule-prefix blocks.

Applies only the mechanical/reconciliation findings from a read-only
Fable-model review of those blocks: anachronism/wording fixes (this world
has no firearms; killed-not-shot phrasing), a stale "function TBD" filled
by an already-locked cross-reference, a density-tier gap reconciled
against already-locked figures, two real-world-event citations clarified
as homage rather than literal history, two cross-references added between
already-locked rules, and category/status field normalization (null
categories filled in per the project's own established naming convention;
uppercase "LOCKED" status strings lowercased to match the rest of the
ledger).

Deliberately NOT applied -- left completely untouched, per the review's
own NEEDS ABAD flags: C1 (POL-010's Lawless Reaches percentage, tied to
the open MCD-094 area-vs-population-weight question), C2 (the VB-020/
VB-023 vs CC-034 Ezio-narrator conflict), C8 (COS-001's "Vakas power" vs
"the Vault" framing), E5 (PH2-031's Kasi premise vs Sankofa's survival
ruling), all N1-N15 enrichment items (new creative/worldbuilding
decisions), and E12 (ledger-wide orthography/diacritic normalization,
out of scope for this batch).
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Phase 4 fable-review of the PH2- (definitional), WC-, POL-, VB-, and "
    "COS- rule-prefix blocks against the full ledger. Mechanical/"
    "reconciliation subset only."
)

AMENDMENTS = {
    "PH2-014": (
        "Xaragua's Dominican-roots supporting cast: Cibao (homage: Sebastian "
        "Lemba), name from the real Taino term for Hispaniola's central "
        "mountain stronghold region -- a half-legendary ancestral figure from "
        "centuries before Ogoun Xarey, the first man to turn the mountains "
        "into a refuge for the escaped and hunted. Guama (homage: Juan Pablo "
        "Duarte; renamed 2026-09-05 from 'Guarocuya' for pronounceability), a "
        "real Taino cacique name -- the idealist who lights Xaragua's "
        "independence movement generations before Ogoun Xarey, founds the "
        "secret society that starts it all, refuses the throne he made "
        "possible, dies sidelined by harder men. Kwabena (homage: Gregorio "
        "Urbano Gilbert), Akan Tuesday-born name -- an 18-year-old who kills "
        "an occupier alone and unordered, then years later crosses the sea "
        "to fight beside Yaque (PH2-018), rising to captain under him. "
        "Baiguate (homage: Francisco Caamano), a real Taino waterfall name "
        "meaning roughly 'hidden water' -- trains for years in secret with "
        "allies abroad, returns, and dies within two weeks of landing."
    ),
    "PH2-016": (
        "Xaragua's 20th-century Cuban-underground supporting cast: Kwaku "
        "(homage: Julio Antonio Mella), Akan Wednesday-born -- a student "
        "agitator, exiled, killed from behind at 25, chronologically the "
        "outlier of this cluster. Imole (homage: Frank Pais), Yoruba for "
        "'light' -- runs the underground by principle, times a city-wide "
        "uprising to a landing that comes late by hours, dies in the street "
        "at 22, recruits and mentors Ina and Iranti directly. Ina (homage: "
        "Vilma Espin), Yoruba for 'fire' -- an engineer who builds weapons "
        "for the cause, recruited by Imole, becomes courier between the "
        "mountains and the exiles abroad. Aabo (homage: Haydee Santamaria), "
        "Yoruba for 'shelter' -- survives torture and the murder of everyone "
        "she loved in one failed attack, later builds an institution "
        "sheltering exactly who her own revolution might otherwise discard. "
        "Iranti (homage: Celia Sanchez), Yoruba for 'memory' -- builds the "
        "reception network years before it's needed, keeps the record of "
        "the whole war, works side by side with Ina."
    ),
    "PH2-048": (
        "Survival, mainline integration, and the 'what if' principle "
        "(standing decision, per Abad's explicit direction): the homage era "
        "is not sealed off from mainline Cian. Every homage-era character, "
        "across every city, is a comrade of Kanja's. This world's baseline "
        "lifespans already run hundreds to tens of thousands of years -- a "
        "character who survives their own origin-era conflict, rather than "
        "dying the way the real person did, has the intervening time to "
        "grow into an extraordinarily skilled, ancient veteran by Kanja's "
        "own era. Chronicles are written as each homage-era territory's own "
        "numbered series, with that territory's leader as protagonist and "
        "Kanja present only as an unnamed guest with no command, credit, or "
        "resolution authorship (Batch 64, MCD-334 through 336, superseding "
        "the earlier 'Kanja Chronicles with guest appearances' framing). "
        "The growing, accumulating number of these now-ancient comrades "
        "bleeds into Book 1 and becomes the reinforcement that turns the "
        "tide roughly midway through the five-book series. Survival is "
        "hand-picked by Abad case by case, not automatic -- reserved "
        "especially for figures whose real deaths left a genuine 'what if' "
        "feeling. Already applied: Kofi (PH2-040), Baale and Kra (PH2-021, "
        "amended), Ohun (PH2-030, amended), Sauti (PH2-046), and Duro "
        "(PH2-047). Everything else built before this ruling stays exactly "
        "as written. Journalists and whistleblowers specifically get their "
        "own design principle: written as 'regular people,' not combat-tier "
        "leaders -- their signature traits keep them alive and effective in "
        "their own domain (documentation, sourcing, credibility, "
        "persistence) rather than granting physical combat power."
    ),
    "PH2-049": (
        "World tech level, reconfirmed for the homage era (standing "
        "decision): this world is firmly pre-industrial (Norse/Gothic and "
        "Roman/Imperial-styled nations per WC-012, ritual-forged Drakma "
        "weapons that explicitly cannot be industrialized per WC-013, no "
        "engines beyond the Drakma-resonance Hymn-Engine and the ancient "
        "Meridian Engine, no firearms, no electronic or broadcast media of "
        "any kind -- CULT-199 bans modern-tech metaphors outright). "
        "Homage-era characters whose real anchors used period tech that "
        "doesn't exist here (broadcast television, radios, etc.) get "
        "translated to period-appropriate in-world equivalents (public "
        "criers, hand-copied broadsheets and pamphlets) rather than keeping "
        "the real mechanism -- see PH2-047 (Duro and Doss). Realized for "
        "mainline Cian only at ARS-426 (Batch 308): SBD-issue Dead Drakma "
        "small arms, culturally coded as cowardly and mechanically "
        "incapable of harming any density-scaled combatant at any tier. "
        "The homage World itself still has none, since the SBD does not "
        "operate there (MCD-313; Batch 338)."
    ),
    "WC-018": (
        "T.D.K.'s Five Champions: Weights/Conquest (General Baryon), "
        "Echoes/Nameless Pursuit (Sereth Vaul 'The Silencer', commands the "
        "Ever-Haunt), Mirages/Illusions (Lady Vestige), Crownless Host/"
        "Dominion (Lord Varro Dominael, undead legions), and a fifth "
        "post-Thren division (Bolo Troth, 'the Post-Thren,' an "
        "asset-retrieval specialist, MCD-284)."
    ),
    "WC-024": (
        "Density Tiers 0 through 6 with named exemplars: Tier 0 Baseline "
        "25x (average Jicome civilian), Tier 1 Elite 100-500x (Cassius "
        "Verehimu 100x), Tier 2 Military 500-1,000x (Colonel Draconis "
        "700x), Tier 3 Branded Peak 2,200-4,900x (Red Beard public "
        "4,800x), Tier 3.5 Reclamation-Proven 5,000-8,000x (fewer than "
        "200 in history), Tier 3.75 High Proven/Lower Sovereign "
        "8,000-16,000x and Sovereign 16,000-22,000x (bands per MCD-144; "
        "Red Beard's actual concealed density is 16,000x, MCD-084), Tier "
        "4 Synthetic Apex 20,000x (Vargo Vakas Prime), Tier 5 Density "
        "Spike (Kanja/Ozmund, variable/limitless), Tier 6 Sovereign Mass "
        "classified (Anu Un Ra/T.D.K., heavier than Vargo Vakas)."
    ),
    "WC-003": (
        "Seven-tier Density Scale: Baseline/Jicome (25x Earth) -> Elite "
        "Warriors (500x) -> Specialized Military (1,000x) -> Branded "
        "fighters (2,200x-4,900x) -> Precision Variants (sub-Branded peak, "
        "extreme fluidity, e.g. Valen) -> Vargo Vakas Prime (20,000x "
        "synthetic apex) -> Kanja/Ozmund Spike (limitless at impact). "
        "(WC-024 is the finer-grained numbered tier table; Precision "
        "Variants, CC-035, are a biology type rather than a density band.)"
    ),
    "PH2-009": (
        "Boriken is an invented fifth Batey territory (not a real borough, "
        "no Staten Island homage), named for the real pre-colonial Taino "
        "name for Puerto Rico, root of 'Boricua.' Fills the alliance's "
        "thematic gap in organized mutual aid and direct action as "
        "community institution-building: the network itself -- clinics, "
        "breakfast programs, occupied buildings turned into shelters -- "
        "meaning the alliance can survive losing a fight in any one place."
    ),
    "PH2-023": (
        "Ollin leads Aztlan, homage to David Sanchez, founder of the Brown "
        "Berets, central organizer of the 1968 East LA school walkouts and "
        "the 1970 Chicano Moratorium. Name is Nahuatl for 'movement,' also "
        "a real Aztec calendar day-sign (renamed 2026-09-05 from "
        "'Cuauhtli,' Nahuatl for 'eagle,' for pronounceability -- the "
        "Nahuatl 'tl' sound doesn't exist in English). Builds the first "
        "real paramilitary structure his community has ever had, wins two "
        "of the era's defining victories through organized discipline -- "
        "then loses the whole thing from the inside, because he never "
        "listened to the people who built it beside him: his first woman "
        "minister, Iya (homage: Gloria Arellanes), led every woman in the "
        "organization out (the real 1970 Arellanes walkout) over "
        "unaddressed sexism, a schism that outlasted the group's external "
        "enemies. Signature ability, 'The Formation': when Ollin stands at "
        "the center of a group he's personally organized and drilled, that "
        "group fights and moves as a single, dramatically amplified force. "
        "Cost: the moment real, ignored grievance inside his own ranks "
        "reaches its breaking point, the formation fractures explosively, "
        "leaving everyone in it worse off than if they'd never organized "
        "at all."
    ),
    "PH2-042": (
        "Omoba leads Jibaro, homage to Jose 'Cha Cha' Jimenez -- founded "
        "the original Young Lords Organization in Chicago's Lincoln Park "
        "in 1968, predating and directly inspiring the later Batey chapter "
        "(Guani, PH2-010); occupied a seminary and a church, running free "
        "breakfast, health, and daycare programs from the latter; "
        "personally co-founded, with Kofi, the cross-territory alliance "
        "homaging the real 1969 Rainbow Coalition; later helped build the "
        "coalition that elected Ofin (the real 1983 Washington coalition). "
        "Name is Yoruba for 'prince.' A gang leader who reads himself into "
        "a different person during solitary confinement, turns his own "
        "street organization into a political one overnight, then takes "
        "over a church and a seminary building by simply walking in and "
        "staying. Signature ability, 'The Occupation': wherever Omoba and "
        "those loyal to him physically hold a space for more than a day, "
        "it permanently becomes a sanctuary no outside authority can "
        "reclaim by force. Cost: only works on space belonging to an "
        "institution he can shame into complicity; doesn't work on open "
        "ground or purely private property."
    ),
    "VB-026": (
        "Book 1, and any future Kanja-POV treatment of the Rebellion (ages "
        "18-30, including a rewrite of Chronicles I-VIII), uses a "
        "progressive narrator handoff. Prose opens in a normal, neutral "
        "narrative voice; Onyx of Oblivion appears only as a short coda at "
        "each chapter's end. Across the Rebellion's twelve years, Onyx's "
        "presence grows steadily more prominent, bleeding further into the "
        "main narration with each successive chapter, until by the "
        "Rebellion's end (age 30, the Trinity's surrender, MCD-246) Onyx "
        "has fully become the narrator -- matching the already-established "
        "steady-state credit at VB-020/021 for all Long Mask-era and later "
        "Kanja material. The transition must read as smooth and subtle, "
        "never an abrupt jump. Does not apply to the Phase 2 homage-era "
        "territory Chronicles (Xaragua, Umoja, Yara, etc.), which are "
        "close-third on their own territory protagonists, not Kanja-POV, "
        "per VB-020's narrator scope. Applies to the Kanja-version "
        "Chronicle track (Batch 313, MCD-1866 onward) and Book 1; the "
        "Alias Chronicle track (MCD-365 onward, 'the regular accounting') "
        "is exempt and stays as written, per Abad's 2026-09-28 ruling."
    ),
    "VB-020": (
        "Five designated narrators, one per narrative thread: Onyx of "
        "Oblivion (Kanja chapters), Red Beard (Ozmund chapters), Ezio "
        "Valcari (investigation chapters), Fermand Aurelias (investigation "
        "chapters, alternate), Anansi (scattered POV chapters, "
        "infrequent). Track assignments since locked: Kanja-version track "
        "= Onyx via VB-026; Ozmund Character Chronicles = Red Beard "
        "(CC-020); Lauris and Ezio Character Chronicles = Fermand "
        "(CC-034); Alias, Territory, and Daba Chronicles = neutral "
        "close-third with no designated narrator."
    ),
    "VB-060": (
        "Kanja's presence, under any alias and in any era, carries a "
        "standing characterization signature: people who share a scene "
        "with him at a moment of real consequence do not experience him as "
        "someone deciding, weighing, or negotiating in real time. They "
        "experience the specific, unsettling sense that he already reached "
        "his conclusion somewhere they were not invited to, and is only "
        "now, in this room, informing them of the result. This is a "
        "character trait, not a supernatural power -- a quality of "
        "already-settled certainty, delivered without volume, threat, or "
        "performance, that reads to anyone still operating in negotiation "
        "mode as something closer to terror than confrontation. First put "
        "on the page in \"The Pivotal Piece\" (MCD-365), via the unnamed "
        "Undersecretary's reaction to Bane: he came prepared with three "
        "rehearsed responses to theatrical refusal and none of them "
        "applied, because nothing he heard was a refusal being negotiated "
        "in front of him -- it was a result being reported. This trait is "
        "intended to recur across the series whenever a POV character "
        "meets Kanja, under whichever alias fits the era (Bane, the "
        "Scourge, and the other nine aliases), at a scene of genuine "
        "stakes -- an early, personal-scale precursor to the "
        "already-locked \"legend is the weapon\" doctrine (established "
        "in-story at the False Dragon's Wake, age 35), which operates at "
        "institutional/reputational scale where this trait operates at "
        "the scale of a single room."
    ),
    "CC-105": (
        "Vargo Vakas is roughly 18,000 years old, one of the world's "
        "'Titans' (present during the Merak purge's aftermath); his "
        "20,000x density was purchased through Hollow Shogunate synthetic "
        "augmentation (Abyssal Bile and extraction methodology) rather "
        "than cultivated, making him the prototype the Shogunate later "
        "mass-produced into its Sin-Eater champions (4,000-6,000x, with "
        "the solo asset Scourge-Tempest augmented to ~6,200x, POL-106)."
    ),
    "POL-102": (
        "The Obsidian Prefecture's government is an oligarchic Senate of "
        "Twelve Patriarchs (POL-040) whose legal system enforces familial "
        "obligation as binding law across generations, giving the Senate "
        "leverage over every citizen's inherited debts. Voss Labyrinth "
        "(Jupiter homage), ~2,800 years old, was First Patriarch and "
        "Senate chairman for a long predecessor tenure before the seat "
        "passed to the already-locked Severin Ebonrath (POL-100) -- his "
        "institutional-founder status is real Prefecture history, not a "
        "competing claim on the current seat. Dhampir Black (Mars "
        "homage), Fourth Patriarch and the Prefecture's military "
        "commander (~1,600 years old, 2,200x density), controls the "
        "legionary command structure. Iron-Gore (Vulcan homage), Tenth "
        "Patriarch and Chief Engineer, controls the roads/aqueducts/"
        "fortifications/siege-weapon infrastructure that gives the "
        "Prefecture's legionary army (200,000 of which are eventually "
        "committed to the alliance's western front, MCD-328) its reach."
    ),
    "WC-001": (
        "The Crown-Scar (neural residue graft of T.D.K.'s command-"
        "frequency architecture) was installed in the first Verehimu "
        "BEFORE his betrayal of T.D.K., as a command-layer upgrade for "
        "succession continuity, designed to include a root-access tether "
        "back to T.D.K. The tether was severed during Haku's campaigns; "
        "the Crown-Scar now runs without the leash. (The tether is "
        "dormant and re-establishable, CC-019/MCD-279; the "
        "lower-intensity bloodline-wide siphon, MCD-290, continues "
        "regardless.)"
    ),
    "PH2-061": (
        "Arturo 'de la Muerte' Salvatierra Duho leads the Five Families "
        "(PH2-060), a Xaragua native and a homage-era comrade in a "
        "structurally distinct role: not a one-off guest in a Kanja "
        "battle, but Kanja's standing point of contact across all five "
        "Batey territories. Two surnames per Abad's direction, and "
        "neither is incidental. Arturo Salvatierra -- both the given name "
        "and the surname -- is not his family's name; it is the name "
        "Spanish colonization imposed on his lineage generations back, "
        "when his ancestors were stripped of who they were and folded "
        "into the colonizer's own naming system. He kept it deliberately, "
        "not from resignation but as a standing reminder of exactly what "
        "is owed and to whom. Later in life he traced what colonization "
        "tried to erase -- falsified records, destroyed archives, "
        "generations who could not say their own clan's name aloud "
        "without danger -- and recovered Duho, his actual clan name, the "
        "one erasure was built to make sure no one would ever find again. "
        "He added it rather than replacing anything, so both truths sit "
        "in his name at once: what was done to his family, and what "
        "survived it anyway. His nickname is a reputation, not a "
        "description -- earned by what happens to people who threaten "
        "what's his, not by how he treats his own. Physics: a "
        "biochemical branch (per VB-005's mass/sound/pressure/chemistry "
        "backbone), not density-scaling -- his signature ability, 'Blood "
        "Debt,' has three faces: protective (wounds seal, toxins break "
        "down, bleeding stops near him or on anyone he's personally "
        "claimed), its dark reverse (catastrophic hemorrhage or organ "
        "failure on someone he's decided is finished, almost never used), "
        "and turned inward (his own aging arrested at a chosen point, "
        "explaining why a much older man still looks mid-40s). Cost: "
        "only works at close range -- a hand on a shoulder, a shared "
        "table -- not a battlefield-wide aura, meaning grievances get "
        "settled at his table because that's the only place his "
        "protection holds; and every true use of the reverse face "
        "visibly ages him, since his youth is a resource he spends, not "
        "a fact about him. Personality: a force of nature, very rarely "
        "outwitted, unflappable and commanding without ever being "
        "boastful; the one exception is playful banter with those who've "
        "earned it, which as of Xaragua Chronicle II is only Yaisa "
        "(PH2-062); Kanja later earns the same standing on his own terms "
        "in Xaragua Chronicle VI (MCD-1093). Toward anyone descended "
        "from the specific colonial lineage responsible for what was "
        "done to his own -- regardless of that individual's rank, "
        "danger, or personal innocence -- he is deliberately, "
        "purposefully adversarial, and enjoys being so; this is a chosen "
        "and ongoing position, not a loss of control, and his S-tier "
        "standing means consequence was never what held him back from "
        "it. He is fully aware that race as a category did not exist "
        "before the colonial system that invented it to organize who "
        "could take from whom -- he is not confused about the science of "
        "it, and he directs his war at the lineage that built and "
        "benefited from that invented structure anyway, because the "
        "categories may be constructed but the harm done using them was "
        "not. He carries none of this as complaint or unresolved rage; "
        "he made his peace with the choice long ago and has never once "
        "second-guessed it. Backstory: a tormented past that is the "
        "actual source of his authority -- as a young man in Xaragua he "
        "was one of a tight cohort of dock boys who were each other's "
        "real family; war took several overseas, and Xaragua's own "
        "street war took most of the rest while he was gone, until only "
        "he and Yaisa remained from that generation. He did not study "
        "the criminal world from above; he survived every rung of it in "
        "sequence on the way up, which is why he understands it better "
        "than anyone. The Five Families, and 'No Blood at My Table' "
        "specifically, are his direct answer to that decade -- a debt he "
        "is still paying, not resolved grief. First appears in Xaragua "
        "Chronicle II ('The Man at the Head of the Table'), granting the "
        "still-unnamed Kanja passage through all five Batey territories "
        "on tested behavior alone -- Kanja declines to give his name even "
        "here, and Arturo does not press, consistent with the "
        "unnamed-guest pattern across Ogoun Xarey's and Yalokona's own "
        "Chronicles. Paid off in Xaragua Chronicle VI (MCD-1093): Kanja "
        "earns a place among Arturo's small circle capable of unguarded "
        "banter, under the private nickname 'Guaikán,' without Arturo "
        "ever learning his name."
    ),
}

# Category-field normalization: null/legacy categories filled in to match
# the project's own established slug convention.
CATEGORY_FIXES = {
    "world-codex": [f"WC-{n:03d}" for n in range(1, 25)],
    "political-atlas-archipelago-houses": ["POL-097", "POL-098", "POL-099"],
    "political-atlas-character": ["POL-100"],
    "voice-bible-narrator-handoff": ["VB-026"],
    "phase2-homage-detroit-territory": [
        "PH2-050", "PH2-052", "PH2-054", "PH2-056", "PH2-058",
    ],
    "phase2-homage-detroit-leader": [
        "PH2-051", "PH2-053", "PH2-055", "PH2-057", "PH2-059",
    ],
    "phase2-homage-nyc-underworld": ["PH2-060", "PH2-061", "PH2-062"],
}

# Status-field normalization: uppercase "LOCKED" -> lowercase "locked",
# only for plain "LOCKED" values (free-text statuses are left untouched).
STATUS_FIX_IDS = (
    [f"VB-{n:03d}" for n in (1, 2, 3, 4, 5, 10, 11, 12, 13, 20, 21, 22, 23, 24, 25, 30, 40, 50)]
    + [f"POL-{n:03d}" for n in (10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 96)]
    + ["COS-001"]
)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    rules_by_id = {r["id"]: r for r in ledger["rules"]}

    amended = []
    for rid, new_statement in AMENDMENTS.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        rules_by_id[rid]["statement"] = new_statement
        amended.append(rid)

    category_changed = []
    for new_cat, ids in CATEGORY_FIXES.items():
        for rid in ids:
            assert rid in rules_by_id, f"missing rule {rid}"
            old_cat = rules_by_id[rid].get("category")
            if old_cat != new_cat:
                rules_by_id[rid]["category"] = new_cat
                category_changed.append(rid)

    status_changed = []
    for rid in STATUS_FIX_IDS:
        assert rid in rules_by_id, f"missing rule {rid}"
        old_status = rules_by_id[rid].get("status")
        if old_status == "LOCKED":
            rules_by_id[rid]["status"] = "locked"
            status_changed.append(rid)

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs found"

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": 0,
        "note": (
            "Phase 4 fable-review mechanical fixes across the PH2- "
            "(definitional), WC-, POL-, VB-, and COS- rule-prefix blocks. "
            "Statement-level fixes: PH2-014/PH2-016 (no-firearms world, "
            "'shoots'/'shot in the back' corrected to 'kills'/'killed from "
            "behind'); PH2-048 (the stale 'Kanja Chronicles with guest "
            "appearances' framing corrected to the real, since-established "
            "territory-leader-as-protagonist Chronicle structure, Batch 64, "
            "MCD-334-336; survival-applied list extended with Sauti and "
            "Duro, PH2-046/047); PH2-049 (the 'possible future firearms "
            "addition' placeholder replaced with its real resolution at "
            "ARS-426, Batch 308); WC-018 (Bolo Troth's 'function TBD' "
            "filled from the already-locked MCD-284); WC-024 (a new Tier "
            "3.75 band reconciles the Tier 3.5 ceiling against Red Beard's "
            "already-locked 16,000x concealed density, MCD-084/144); "
            "WC-003 (cross-referenced against WC-024 and CC-035 to resolve "
            "an apparent scale mismatch); PH2-009 ('Batey-adjacent' "
            "corrected to 'Batey', matching every sibling territory rule); "
            "PH2-023/PH2-042 (two real-world-event references clarified as "
            "homage citations rather than literal in-world history, "
            "matching the project's own standing real-world-proper-noun "
            "convention); VB-026/VB-020 (narrator-track assignments made "
            "explicit, including the Kanja-version track's VB-026 "
            "applicability and the Alias Chronicle track's exemption, "
            "Abad's 2026-09-28 ruling); VB-060 ('others still "
            "undramatized' updated now that all eleven aliases have "
            "dramatized entries); CC-105 (Sin-Eater champion density range "
            "reconciled against POL-106's named Scourge-Tempest outlier); "
            "POL-102 (the Prefecture's legionary-army figure cross-"
            "referenced against its own already-locked western-front "
            "commitment, MCD-328); WC-001 (cross-referenced against "
            "CC-019/MCD-279's dormant-tether and MCD-290's bloodline-wide "
            "siphon layer); PH2-061 (the 'fourth homage-era comrade' count "
            "claim dropped as unverifiable/uncounted). Category field "
            "normalized for 24 WC- rules (null -> 'world-codex'), POL-097/"
            "098/099 ('Politics' -> 'political-atlas-archipelago-houses'), "
            "POL-100 ('political-figure' -> 'political-atlas-character'), "
            "VB-026 ('Voice Bible' -> 'voice-bible-narrator-handoff'), 5 "
            "Detroit territory rules and 5 Detroit leader rules (generic "
            "'Phase 2 Homage Era' -> the city's established territory/"
            "leader convention), and PH2-060/061/062 ('Phase 2 Homage "
            "Era' -> 'phase2-homage-nyc-underworld'). Status field "
            "normalized from uppercase 'LOCKED' to lowercase 'locked' for "
            "18 VB- rules, 11 POL- rules, and COS-001. Deliberately NOT "
            "applied, per the review's own NEEDS ABAD flags: C1 (POL-010's "
            "Lawless Reaches percentage, tied to the open MCD-094 area-vs-"
            "population-weight question), C2 (the VB-020/VB-023 vs CC-034 "
            "Ezio-narrator conflict), C8 (COS-001's 'Vakas power' vs 'the "
            "Vault' framing), E5 (PH2-031's Kasi premise vs Sankofa's "
            "survival ruling), all N1-N15 enrichment items (new creative/"
            "worldbuilding decisions), and E12 (ledger-wide orthography/"
            "diacritic normalization, out of scope for this batch)."
        ),
    })

    old_version = float(ledger["ledger_version"])
    ledger["ledger_version"] = str(round(old_version + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(
        f"OK: {len(ledger['rules'])} total rules, "
        f"{len(ledger['batches_completed'])} batches, ledger_version "
        f"{ledger['ledger_version']}, zero duplicate IDs.\n"
        f"{len(amended)} rule statements amended: {', '.join(amended)}.\n"
        f"{len(category_changed)} categories normalized: "
        f"{', '.join(category_changed)}.\n"
        f"{len(status_changed)} statuses normalized: "
        f"{', '.join(status_changed)}."
    )


if __name__ == "__main__":
    main()
