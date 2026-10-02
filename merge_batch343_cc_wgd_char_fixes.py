#!/usr/bin/env python3
"""Batch (computed at runtime): Fable-review fixes for the CC-/WGD-/CHAR- rule
blocks (character dossiers, Weregildd slaver economics, and the small early
CHAR- prefix).

Applies the subset of a Fable-model read-only review's findings that are pure
mechanical/reconciliation fixes against already-locked canon -- age-clause
wording, a half-applied Batch-321 "freed independently" reconciliation, a
stale pre-MCD-1851 age ranking, a stale false-claim in an SBD institutional-
error file, a pronoun slip, a character misattribution, a writers'-room
"pending further discussion" leak, stale source/note fields, two wording
fixes, an event-name cross-reference, a field-value category/status
normalization pass, three optional soft-tension wording softeners, and a
collision rename (Varruk's own "Cadence Ruin"/"Cadence Saturation" vs.
Onyx of Oblivion's load-bearing "Cadence Ruin" blade power, ARS-020 --
Onyx's own usage is NOT touched).

Items flagged NEEDS ABAD by the review (Ezio's age CC-028, Matar's
recruitment date CC-067/102, Orlok's timeline CC-091/141/142/143, and all
ENRICHMENT items) are deliberately NOT applied here and remain queued for
Abad's own ruling.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Fable-model read-only review of the CC-/WGD-/CHAR- rule-prefix blocks "
    "(character dossiers, Weregildd slaver economics, the small early CHAR- "
    "prefix) against the full ledger, implemented by this session."
)

# ---------------------------------------------------------------------------
# Rule-statement amendments
# ---------------------------------------------------------------------------
AMENDMENTS = {
    # C3: age-clause wording -- Abyss is the crew's youngest *adult recruit*,
    # not its youngest member outright (Pyro is younger).
    "CC-101": (
        "Abyss (Ren Oshaal), deeper physiology: his Negative-Density Variant "
        "biology generates a localized gravitational-pressure field -- "
        "passive (~5m radius, +30% gravitational load), active (~15m radius, "
        "+200% load), and the Depth-Charge (field compressed to ~1m, "
        "approximating deep-ocean crush pressure, costing ~6 hours' "
        "recovery). Age ~45 (the crew's youngest adult recruit; Pyro, "
        "roughly 24-36 at Book 1, is younger), personal density ~150x, "
        "carries no weapons -- his field is his arsenal, moderated by "
        "Kanja-built Dead Drakma gravitational-compensator boots and a "
        "field-moderating mesh vest for close proximity to allies. Origin: "
        "a deep-ocean pressure-adapted community on the Jicome continental "
        "shelf; sent to the surface at 16 after his field's output exceeded "
        "his settlement's structural tolerance at 14; recruited by Sephtis."
    ),
    "MCD-1715": (
        "Lauris Chronicle XCVIII, 'The Weight Nobody Else Would Stand "
        "Under' (full narrative text at "
        "docs/lords-of-cian/chronicles/lauris-chronicle-xcviii-the-weight-"
        "nobody-else-would-stand-under.md), ninety-eighth entry in her own "
        "Chronicle series, Strand W. A stakes-free entry pairing Lauris "
        "with Abyss (Ren Oshaal, CC-101), the crew's youngest recruit -- "
        "she becomes his preferred practice partner for controlling his "
        "Negative-Density Variant field's active-range output, since her "
        "own biology tolerates standing inside it without discomfort. Puts "
        "CC-134's combat-joy trait on the page as pleasure taken in a "
        "genuine physical limit tested safely. No new named characters."
    ),

    # C5: reconcile the half-applied Batch-321 fix -- the three earliest
    # crew members found each other and found Kanja together; none of them
    # was "freed" by him.
    "CC-159": (
        "Danne Sok: he/him (reconciled Batch 320, 2026-10-01, same "
        "resolution as `CC-158`). One of the three earliest crew members -- "
        "alongside Corren Halst and Maret Vos, all three Maw survivors who "
        "found each other on the docks before finding Kanja (Batch 321, "
        "2026-10-02) -- fighting alongside him by the Black Trench (age 19, "
        "`MCD-234`). Runs an intelligence/verification network referenced "
        "extensively across the Bane Alias Chronicle corpus (e.g. "
        "independently confirming a Directorate defector's account over six "
        "weeks, `MCD-1027`). Privately kept, for the whole of the war, a "
        "memory of the young Kanja's hands shaking for an hour on the first "
        "night the three of them stood with him, before any alias existed "
        "(`MCD-530`). Has a daughter (deliberately kept unnamed) who grows "
        "up visiting the crew's ships and eventually enlists, leading her "
        "own first independent operation a generation after Corren Halst's "
        "own comparable growth (`MCD-1002`/`1517`)."
    ),
    "MCD-530": (
        "\"What Danne Sok Never Told Anyone\" (full narrative text at "
        "docs/lords-of-cian/chronicles/what-danne-sok-never-told-anyone.md), "
        "Bane Alias Chronicle XV, closing the fifth wave. Danne Sok "
        "(already locked, one of the three earliest crew members freed "
        "before the Black Trench) finally shares a memory kept private the "
        "whole war: the young Kanja's hands shaking for an hour after the "
        "first fight the three of them stood beside him, before any alias "
        "existed -- a private counterweight to the legend, extending the "
        "'tired, not scary' theme (MCD-478) back to its literal origin. No "
        "new named characters beyond the already-locked Danne Sok. Closes "
        "Bane's fifth three-Chronicle wave (with 'The Boy Who Wanted to Be "
        "Him,' MCD-528, and 'The Siege That Took Nine Days,' MCD-529)."
    ),
    "MCD-234": (
        "The Siege of Maw-9 and the Sewer War of Killane. Maw-9: freed "
        "roughly 12,000 Cestari by undermining the arena's own "
        "load-bearing foundation arches from tunnels below, collapsing the "
        "guard tiers under the garrison's own weight rather than attacking "
        "it directly. Three freed Cestari already fighting alongside Kanja "
        "by this point -- Corren Halst, Danne Sok, and Maret Vos -- had "
        "each freed themselves independently before Maw-9 (by the Black "
        "Trench, age 19), forming the nucleus of his earliest crew before "
        "the mass liberation; Maw-9 added further recruits to that "
        "existing core rather than being the original meeting point. The "
        "Sewer War of Killane (Blue-Collar Titan alias reinforced): an "
        "80-fighter, six-week infiltration through Killane's forgotten "
        "pre-modern sewer layer that diverted 600 of the city's "
        "1,200-soldier garrison chasing sabotaged infrastructure while "
        "copying the Southern District's Scrip-Registry ledger undetected "
        "for four months -- the battle marking fifteen-year-old Ezio "
        "Valcari's first on-page appearance, already eight months into "
        "work as a junior intelligence courier."
    ),

    # C6: close the gap MCD-1851 (Batch 309) left -- Orlok is also younger
    # than Soledad Keme.
    "CC-058": (
        "Orlok is approximately 76,003 years old, a self-taught S-Tier "
        "fighter who reaches 20,000x density (equal to Vargo Vakas's "
        "static ceiling) temporarily through cultivation rather than "
        "augmentation; he is younger only than T.D.K. (Anu Un Ra) and "
        "Soledad Keme (MCD-1851)."
    ),

    # C8: remove "Pyro's birth as natural" from Dexton's false-claims list
    # -- MCD-022 locks natural birth as TRUE, not false.
    "SBD-041": (
        "The SBD's own file on the Pyro Birth Incident and the Triad's "
        "origin -- authored by informant Shelton Dexton, transmitted to "
        "A.M. under full-transparency posture -- is false, not the truth "
        "it replaces. Dexton's account (the Triad raised from birth by "
        "Pyro's mother in her own Shattered Kingdoms homeland, and Kanja's "
        "wife killed by an anomaly-class monster rather than the Living "
        "Gate containment event) directly contradicts the already-locked, "
        "correct account at MCD-131/132/133 (Pyro's mother is not dead; "
        "she inverted T.D.K.'s Living Gate into a forge and is fused into "
        "its own architecture, no longer dead but transformed). Dexton "
        "reported this in complete good faith, per CC-140 -- he was "
        "himself misled by his own informant network, not knowingly lying "
        "to A.M. The file stands as a documented SBD institutional error, "
        "its source and the reason for the deception both unidentified, "
        "reserved as a future thread for either Archon Meridian's eventual "
        "SBD cleanup or Dexton's own reckoning with whoever fed him the "
        "false account."
    ),

    # E1: pronoun fix -- Pyro is he/him (CC-047).
    "MCD-022": (
        "Pyro's hidden birth name is Ignis. \"Pyro\" is a ship-name. His "
        "birth is NATURAL. The Dhar-Kael bond was completed by his mother "
        "(the last keeper) BEFORE T.D.K.'s Living Gate curse. The Demaron "
        "event is separate from and after the birth; Stormbreaker's trauma "
        "is preserved, resequenced rather than replaced."
    ),

    # E2: misattribution fix -- CC-088 is Lucius Blackthorne's dossier, not
    # Cooper's (Cooper is CC-068/103).
    "SBD-048": (
        "Extends WC-007/CC-088/MCD-258: reaching 'the Hollowed' (100% "
        "Scrip-debt ratio) is not merely an economic dead end. Once a "
        "person's debt ratio is confirmed at 100%, the SBD classifies them "
        "as Fully Hollowed and eligible for Biological Repurposing -- "
        "consciousness suppressed via sustained amnestic dosing, the body "
        "retained as passive processing infrastructure (containment-field "
        "maintenance, archive indexing, the kind of continuous "
        "low-cognition labor the Directorate doesn't want a will attached "
        "to). This is the fate CC-088's Lucius Blackthorne fears "
        "specifically from Onyx of Oblivion, and the reason Level 3 Mythic "
        "Contamination (SBD-047) is designed to walk an offending agent to "
        "100% debt on an accelerated timeline rather than punish them any "
        "other way -- reassignment to Expendable Asset status is the "
        "waiting room, Hollowing is the actual sentence."
    ),

    # E5: writers'-room leak removed.
    "WGD-009": (
        "The Writedown Compact, the Weregildd's economic circuit, extends "
        "predatory Scrip credit lines to struggling minor holds and "
        "mercenary houses, creating debt-bondage dependencies that "
        "discourage outside intervention. This sits parallel to House "
        "Draeven and House Brekka's debt entanglement with the Legion; no "
        "direct link is asserted."
    ),

    # C7: clarify the Sovereignty Summit / Fulfillment Ceremony are the same
    # occasion.
    "MCD-091": (
        "The Double Regicide: both Maro Rexmar and Aethelgard Verehimu are "
        "murdered at the Fulfillment Ceremony, killed by the Three Ronin "
        "with SBD wet-work support team cover-up. The Fulfillment Ceremony "
        "is the ceremonial event held at the Sovereignty Summit; the two "
        "names refer to the same occasion. The Fulfillment Ceremony is "
        "separate from the Sovereign Pier Accords, roughly 296 years "
        "apart."
    ),
    "CC-009": (
        "King Maro Rexmar negotiated the secret Sovereign Pier Accords with "
        "Aethelgard Verehimu, promising Directorate recognition of Maro as "
        "sovereign King of Jicome in exchange for Kanja surrendering the "
        "Trinity; the pact died when Aethelgard was murdered at the "
        "Fulfillment Ceremony (the Sovereignty Summit, MCD-091; Book 1 "
        "opening)."
    ),

    # E7: minor wording fixes.
    "CC-148": (
        "Orven Castellan is a Sovereign Trust Regional Magistrate-General "
        "overseeing Suppression Brigade deployments across a Directorate "
        "province during Kanja's Rebellion era -- a command-tier officer, "
        "not a personal combatant, with a static density within WC-024's "
        "Tier 2 Military band (500-1,000x; Colonel Draconis exemplar 700x) "
        "whose real threat is institutional: he can authorize "
        "brigade-scale force, falsify after-action reports, and end "
        "careers, but he has never personally fought at any "
        "density-relevant tier. He is a distinct figure from Suppression "
        "Brigade Kethane's own (already-destroyed, MCD-232) command "
        "structure -- a different province, a later point in the "
        "Rebellion. Personality: image-obsessed and politically ambitious, "
        "genuinely believing that a single decisive, well-publicized "
        "victory over Kanja's Rebellion would secure him a Sovereign Trust "
        "Council seat; he has spent two years quietly inflating his "
        "brigade's actual engagement record to build that reputation "
        "before ever facing Kanja directly."
    ),
    "CC-022": (
        "Red Beard's publicly known density is 4,800x (upper Branded "
        "Peak); his actual concealed density is 16,000x and climbing, a "
        "secret known only to Ozmund, who trained him."
    ),
    "CC-154": (
        "Ossa Drem is the Weregildd's 'Handler-Prime' commanding a "
        "Leash-Bound enforcer cadre (WGD-004) -- a failed candidate from "
        "one of the licensed Cestari breeding Farms (MAW-070) decades ago, "
        "rejected from competitive selection, who rose through the "
        "Weregildd's own ranks by brutality until he commanded the "
        "apparatus that had once discarded him. His own Leash-Bound collar "
        "mechanically caps his suppressed density at roughly 1,000-1,200x "
        "regardless of provocation (per WGD-004/MAW-121's own black-market "
        "Blight-Tether-derivative mechanism), making him physically "
        "formidable against ordinary soldiers but structurally incapable "
        "of approaching a Branded Peak fighter, let alone anything higher. "
        "Personality: a broken man who has converted his own rejection "
        "into a belief system -- he genuinely tells himself he is 'kinder' "
        "to the Offcuts and captives under his command than whatever would "
        "happen to them otherwise, and enforces that self-image with real "
        "cruelty whenever it's challenged."
    ),

    # N1: rename Varruk's own "Cadence Ruin"/"Cadence Saturation" to resolve
    # the collision with Onyx of Oblivion's load-bearing "Cadence Ruin"
    # blade power (ARS-020, untouched). New name: "the Riptide Break" /
    # "Riptide Saturation" -- zero collisions anywhere in the ledger or the
    # Chronicle corpus (checked before drafting), consistent with Varruk's
    # own established naval-flavored register (Wake-Scissor, Pressure-Seam
    # Drop, Oarline Misfire Window, SBD-045) and matching the precedent
    # already set for Sereth Vaul's own renamed "Void Wake" (ARS-395).
    "CC-098": (
        "Varruk's morphology and capabilities: 15% larger than Argentavis "
        "magnificens (~195 lbs, 27.6 ft wingspan, hollow-bone build, the "
        "lightest of the Triad by design rather than weakness). Five "
        "capabilities: Pattern-Scouting (reconstructs a complete strategic "
        "picture from fragmentary observation), Angle-Whisper (projects "
        "compressed geometric certainty -- not words or images -- directly "
        "into a bonded mind), the Riptide Break (disrupts enemy "
        "coordination via low-altitude passes and targeted-frequency "
        "screams; renamed from 'Cadence Ruin' to resolve a naming "
        "collision with Onyx of Oblivion's own load-bearing blade power, "
        "ARS-020, matching the precedent already set for Sereth Vaul's own "
        "renamed 'Void Wake,' ARS-395), Storm-Lane Travel (navigates "
        "hurricane-force weather as express routes), and Guidance by "
        "Refusal (communicates danger by refusing to land on or fly a "
        "given path, never by warning)."
    ),
    "CC-099": (
        "Varruk's bond and vulnerabilities: the Pyro Bond manifests in "
        "Varruk as navigational certainty -- he always knows the safest "
        "(not fastest) path to Pyro, and is the most visibly bonded of the "
        "Triad in daily life (constant overwatch rather than hovering). "
        "Hierarchy: Pyro first, pattern second, ship third -- he will "
        "abandon a reconnaissance mid-flight if Pyro is threatened. "
        "Vulnerable to Blight Frequencies (degrades "
        "Pattern-Scouting/Angle-Whisper), is functionally grounded in "
        "enclosed spaces (his capabilities need open sky/water), and "
        "Riptide Saturation (renamed from 'Cadence Saturation' alongside "
        "the Riptide Break rename, CC-098; self-limiting: overuse of his "
        "own frequency projection causes disorientation via reverberation "
        "in his own hollow bones)."
    ),
    "SBD-021": (
        "SBD's Varruk is rated OMEGA-PRIME threat. Named capabilities: "
        "Pattern-Scouting, Angle-Whisper, Guidance by Refusal, the "
        "Riptide Break (CC-098)."
    ),
    "ARS-413": (
        "Extends CC-098/CC-099: Varruk's plumage runs pale cream to "
        "buff-white, deliberately stained rust-orange through iron-rich "
        "dust bathing as intentional scent-masking rather than passive "
        "coloring. His Riptide-disruption vocalization (extends the "
        "already-locked Riptide Break, CC-098) operates at ~200m radius, "
        "interfering with communication and targeting simultaneously. A "
        "distinct named behavior, the Stare: fixing a threat with "
        "unblinking intensity, producing a sensation of being observed at "
        "a level deeper than visual contact -- separate from "
        "Angle-Whisper's geometric-certainty projection. Beneath the "
        "resonance-bond with the Triad, Varruk maintains an everyday vocal "
        "register the crew reads: growls signal danger, purrs signal "
        "safety, a specific whine signals detected deception."
    ),

    # Optional soft-tension wording softeners (applied -- no new facts).
    "CC-138": (
        "Abyss (Ren Oshaal, CC-066/101) origin and texture extension: "
        "found as an orphan, orphaned within that community (CC-101's "
        "deep-ocean pressure-adapted Jicome continental-shelf settlement), "
        "on a remote island associated with old serpent-lore, with faint "
        "serpent-pattern dermal markings; his defining personal "
        "throughline is an unresolved quest for identity and belonging, "
        "and he regards Kanja as a paternal figure. His Negative-Density "
        "Variant gravitational-pressure biology extends to passive "
        "long-range detection -- a felt vibration/pressure sense that once "
        "gave the crew roughly fifteen kilometers of warning before a "
        "Directorate sub-surface retrieval team made sonar contact -- read "
        "by outside observers as a distinct 'seismic sense' but "
        "mechanically the same pressure-field biology already locked at "
        "CC-101, not a separate ability. Fully compatible extension; "
        "CC-066/101 unchanged."
    ),
    "CC-114": (
        "Anirak and Ren (Abyss) are established as a deliberate "
        "tactical/relational pairing -- 'Surface Storm' (Anirak's "
        "kinetic, rotational output) and 'Deep Pressure' (Ren's "
        "gravitational field) -- complementary both in combat (her blades "
        "shred structure, his field collapses the weakened structure "
        "under its own augmented weight) and as a sibling-like bond: "
        "Anirak positioned herself as his protector without formal "
        "assignment, recognizing a body the world wasn't built for."
    ),
    "CC-046": (
        "The Living Gate event: T.D.K. (Anu Un Ra) installed a "
        "voice-keyed 'Living Gate' curse into Kanja's first and only wife "
        "(a veil-reader) as a containment response to her discovering his "
        "hidden architecture; her pregnancy amplified the Gate, a Demaron "
        "entity inhabited her, and Pyro and the three Dhar-Kael guardians "
        "(Varkul, Varruk, Sorya) were produced as her final act (the "
        "Dhar-Kael bond itself having been completed beforehand, "
        "MCD-136). The Codex's own framing that her 'body's vessel was "
        "ultimately ended' is deliberate in-universe misdirection (per "
        "MCD-133); MCD-131/MCD-132 are the sole authorial truth -- she "
        "survived, inverting the Gate into a forge and fusing into its "
        "architecture rather than being ended."
    ),
}

# ---------------------------------------------------------------------------
# E4: category-field normalization (not a statement change -- set directly)
# ---------------------------------------------------------------------------
# CC-001 through CC-080: currently null/None -> "character-codex"
CATEGORY_NULL_TO_CODEX = [f"CC-{i:03d}" for i in range(1, 81)]

# CC-135 through CC-157: currently "Character" (capitalized) -> specific
# normalized values. (CC-141/142/143 already carry "character-orlok" and
# are left untouched.)
CATEGORY_CHARACTER_CREW = ["CC-135", "CC-138", "CC-139"]
CATEGORY_CHARACTER_CODEX_135 = ["CC-136", "CC-137", "CC-140"]
CATEGORY_CHARACTER_ANTAGONIST = [f"CC-{i:03d}" for i in range(144, 158)]

# CHAR-001/CHAR-002: status "LOCKED" -> "locked"
STATUS_LOWERCASE = ["CHAR-001", "CHAR-002"]

# E6: stale source/note field updates (not statement changes)
SOURCE_UPDATES = {
    "CHAR-001": (
        "originated in chat 2026-08-15; the Character Codex document was "
        "processed in Batch 27 (2026-08-25), and the Painter was further "
        "elaborated in the standalone interstitial Chronicle 'What the "
        "Canvas Kept' (MCD-1622, Batch 297, 2026-09-18), given the "
        "unconfirmed legend-name 'Vantine.'"
    ),
}
NOTE_APPENDS = {
    "CC-075": " Resolved: MCD-140 locks the Avatar count at nineteen.",
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

    recategorized = []

    for rid in CATEGORY_NULL_TO_CODEX:
        assert rid in rules_by_id, f"missing rule {rid}"
        if rules_by_id[rid].get("category") is None:
            rules_by_id[rid]["category"] = "character-codex"
            recategorized.append((rid, None, "character-codex"))

    for rid in CATEGORY_CHARACTER_CREW:
        assert rid in rules_by_id, f"missing rule {rid}"
        old = rules_by_id[rid].get("category")
        if old == "Character":
            rules_by_id[rid]["category"] = "character-crew"
            recategorized.append((rid, old, "character-crew"))

    for rid in CATEGORY_CHARACTER_CODEX_135:
        assert rid in rules_by_id, f"missing rule {rid}"
        old = rules_by_id[rid].get("category")
        if old == "Character":
            rules_by_id[rid]["category"] = "character-codex"
            recategorized.append((rid, old, "character-codex"))

    for rid in CATEGORY_CHARACTER_ANTAGONIST:
        assert rid in rules_by_id, f"missing rule {rid}"
        old = rules_by_id[rid].get("category")
        if old == "Character":
            rules_by_id[rid]["category"] = "character-antagonist"
            recategorized.append((rid, old, "character-antagonist"))

    restatused = []
    for rid in STATUS_LOWERCASE:
        assert rid in rules_by_id, f"missing rule {rid}"
        old = rules_by_id[rid].get("status")
        if old == "LOCKED":
            rules_by_id[rid]["status"] = "locked"
            restatused.append((rid, old, "locked"))

    source_updated = []
    for rid, new_source in SOURCE_UPDATES.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        rules_by_id[rid]["source"] = new_source
        source_updated.append(rid)

    note_updated = []
    for rid, append_text in NOTE_APPENDS.items():
        assert rid in rules_by_id, f"missing rule {rid}"
        r = rules_by_id[rid]
        if "note" in r:
            r["note"] = r["note"] + append_text
        else:
            r["note"] = append_text.strip()
        note_updated.append(rid)

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate rule IDs found"

    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({
        "batch": next_batch,
        "date": str(date.today()),
        "source": SOURCE,
        "rule_count": 0,
        "note": (
            "Fable-review fixes for the CC-/WGD-/CHAR- rule blocks -- "
            "mechanical/reconciliation subset only. Amends: CC-101/MCD-1715 "
            "(Abyss's 'youngest member' age clause clarified against Pyro's "
            "own younger age); CC-159/MCD-530/MCD-234 (reconciles a "
            "half-applied Batch-321 fix -- Corren Halst/Danne Sok/Maret Vos "
            "found each other and found Kanja together, none was 'freed' by "
            "him -- a matching Chronicle-prose check on "
            "what-danne-sok-never-told-anyone.md, or a similarly titled "
            "file, is still owed in a future pass, not done here since no "
            "narrative .md files are in scope for this batch); CC-058 "
            "(Orlok is younger than T.D.K. AND Soledad Keme, closing the "
            "gap MCD-1851/Batch 309 left open); SBD-041 (drops 'Pyro's "
            "birth as natural' from Dexton's false-claims list, since "
            "MCD-022 locks natural birth as true); MCD-022 (pronoun fix, "
            "Pyro is he/him per CC-047); SBD-048 (CC-088 is Lucius "
            "Blackthorne's dossier, not Cooper's -- Cooper is CC-068/103); "
            "WGD-009 (drops a writers'-room 'vector b of the "
            "corruption-vector plan; pending further discussion' leak); "
            "MCD-091/CC-009 (clarifies the Fulfillment Ceremony and the "
            "Sovereignty Summit are the same occasion); CC-148 (density "
            "citation corrected to WC-024's actual Tier 2 Military band, "
            "500-1,000x, Draconis exemplar 700x); CC-022 (garbled 'known "
            "only to have been trained with Ozmund in secret' reworded to "
            "'a secret known only to Ozmund, who trained him'); CC-154 "
            "(density-cap citation corrected to WGD-004/MAW-121, since "
            "WGD-004 alone only locks compliance/relapse, not the ceiling "
            "mechanism); CHAR-001 (stale source field updated -- the "
            "Character Codex was processed in Batch 27, and the Painter "
            "was elaborated at MCD-1622 under the legend-name 'Vantine'); "
            "CC-075 (note appended recording MCD-140's resolution of the "
            "16-vs-17 Avatar count). N1: renames Varruk's own 'Cadence "
            "Ruin'/'Cadence Saturation' (CC-098, CC-099, SBD-021, and the "
            "cross-referencing ARS-413) to 'the Riptide Break'/'Riptide "
            "Saturation' to resolve a real naming collision with Onyx of "
            "Oblivion's own load-bearing 'Cadence Ruin' blade power "
            "(ARS-020, used across 40+ Alias Chronicles -- NOT touched), "
            "collision-checked at zero hits anywhere in the ledger or "
            "Chronicle corpus before picking the name, consistent with "
            "Varruk's own established naval-flavored register (Wake-"
            "Scissor, Pressure-Seam Drop, Oarline Misfire Window, SBD-045) "
            "and matching the precedent already set for Sereth Vaul's own "
            "renamed 'Void Wake' (ARS-395, Batch 308). Also applies three "
            "optional reconciliation-level wording softeners with no new "
            "facts: CC-138 (orphaned within CC-101's own community, "
            "resolving an apparent origin mismatch), CC-114 ('as siblings' "
            "-> 'as a sibling-like bond'), and CC-046 (a parenthetical "
            "clarifying the Dhar-Kael bond was completed beforehand per "
            "MCD-136). E4: normalizes category-field drift -- CC-001 "
            "through CC-080 (80 rules, all null) to 'character-codex'; "
            "among CC-135 through CC-157's stale 'Character' values, "
            "CC-135/138/139 to 'character-crew', CC-136/137/140 to "
            "'character-codex', and CC-144 through CC-157 (the Ronin "
            "figures and the eleven Batch-312 pre-Book-1 villains) to "
            "'character-antagonist' (CC-141/142/143 already carried "
            "'character-orlok' and were left untouched); and CHAR-001/"
            "CHAR-002's uppercase 'LOCKED' status to the ledger's standard "
            "lowercase 'locked'. Deliberately NOT applied, left completely "
            "untouched per the review's own NEEDS ABAD flags: C1 (CC-028's "
            "Ezio age, already flagged in Batch 332), C2 (CC-067/102's "
            "Matar recruitment date), C4 (CC-091/141/142/143's Orlok "
            "timeline), and all ENRICHMENT items (CHAR-002's uncle "
            "material, thin dossiers, etc.)."
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
        f"{len(recategorized)} rules recategorized: {recategorized}.\n"
        f"{len(restatused)} rules re-statused: {restatused}.\n"
        f"{len(source_updated)} rule source fields updated: "
        f"{source_updated}.\n"
        f"{len(note_updated)} rule note fields appended: {note_updated}."
    )


if __name__ == "__main__":
    main()
