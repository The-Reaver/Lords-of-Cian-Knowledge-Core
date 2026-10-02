#!/usr/bin/env python3
"""Batch 321: reconciliation corrections surfaced by a read-only review pass on the Industrial
Myth Alias Chronicle corpus (102 entries). Mechanical fixes (rule-ID leaks in narrative prose,
wrong footer citations, a title-string leaked into dialogue, an internal count error, stale
tracker/profile figures) plus one ruling applied directly (the Furnace District Strike's age
locked at 21, not 19 -- Ezio Valcari's age math only works at 21) and its downstream
reconciliations: the strike's own four-day tally vs. its eleven-day gate stand, the alias name's
informal pre-Strike circulation vs. its formal Directorate classification at the Strike, a
geography fix (Efa Gol's pre-Strike crowd-control experience), a Pell Ostra pronoun fix matching
her already-locked she/her (CC-132/CC-133), and an already-locked rule outside this track
(ARS-425) that wrongly placed the strictly-unarmed Rexmar Machete at the Strike. All prose-level
fixes to the Chronicle .md files themselves were applied directly to those files in this same
batch; this script carries only the canon-ledger.json-side amendments. No new creative facts --
pure reconciliation against already-locked canon, matching the Batch 226/68/320 precedent."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Read-only review pass (Industrial Myth Alias Chronicle corpus), reconciliation pass, 2026-10-02"

with open(LEDGER_PATH) as f:
    ledger = json.load(f)

rules_by_id = {r["id"]: r for r in ledger["rules"]}

# --- Amend rule statements ---
AMENDMENTS = {
    # C1 + C3: Furnace District Strike age corrected 19 -> 21 (Ezio Valcari's age math only works
    # at 21); plus the informal-circulation-before-formal-classification clause that reconciles
    # the six pre-Strike entries (MCD-753/754/759/761/762/768) using "the Industrial Myth" as an
    # already-known name without needing to touch their own prose.
    "MCD-230": (
        "Kanja's Twenty-Two Victories (ages 18-30, 12 years) break down precisely as 10 "
        "Conventional Victories, 6 Unwinnable Victories (each earning a Directorate-classified "
        "alias), and 6 Operational/labor-logistics Campaigns -- correcting the earlier draft's "
        "(WC-023) imprecise 'sixteen conventional' paraphrase (a secondary source's coarser "
        "bucketing of 10 Conventional plus 6 Campaigns together). Aliases in acquisition order: "
        "the Trench Monarch (18), Bane (19, Black Trench, Unwinnable), the Industrial Myth (21, "
        "first iteration, Furnace District Strike), the Blue-Collar Titan (20, Sewer War of "
        "Killane), Sovereign Ghost of the Great Sea (21, Ghost Harbor, Unwinnable), the Scourge "
        "(22, Ash-Wharf), the Crow King (23, Unwinnable), the Iron Bastard (25, Unwinnable), the "
        "Lord of Embers (27, Unwinnable), the Storm That Walks (29, Gale Straits, Unwinnable) -- "
        "and Captain, the one name that was never a Directorate classification. Corrected Batch "
        "321, 2026-10-02: the Furnace District Strike's age corrected from 19 to 21 (Ezio "
        "Valcari's own age math across the Industrial Myth Alias Chronicle corpus only resolves "
        "at 21). The name 'the Industrial Myth' itself circulated informally among workers before "
        "the Strike; the Directorate's own formal classification of it dates to the Strike itself, "
        "reconciling the several pre-Strike Chronicle entries that already use the name "
        "informally."
    ),
    "VB-061": (
        "A standing catalog of quotes attributed to Kanja's labor-adjacent aliases, in a "
        "blue-collar register distinct from VB-060's presence-doctrine framing -- extends but "
        "does not repeat it. The Trench Monarch (age 18, his first alias): 'Every king I ever "
        "heard of inherited his crown. Mine's mud and iron, and I dug it up myself.' The "
        "Industrial Myth (age 21, Furnace District Strike, MCD-244): 'A myth doesn't clock in. I "
        "do. That's the difference between a story and a man you can find on the floor when the "
        "whistle blows.' The Blue-Collar Titan (age 20, Sewer War of Killane, MCD-234): 'They "
        "keep calling it a title, like it's something I put on. It isn't. It's just what happens "
        "when you never stop being the man who worked for a living, and the work got bigger than "
        "anyone planned for.' The Lord of Embers (age 27, the Rolling Foundry Campaign, MCD-241): "
        "'You want to burn a workingman's home down, go ahead. Just know somebody's going to be "
        "standing in the ashes with a hammer before your smoke clears -- and that somebody's "
        "going to be me.' Captain (never a Directorate classification, his own crew's name for "
        "him): 'The Directorate names what scares them. We named the man who feeds the crew "
        "before he feeds himself. That name's ours. They don't get to touch it' -- attributed to "
        "the crew collectively rather than to Kanja himself, matching the already-locked "
        "distinction that 'Captain' is affectionate and self-given, not an institutional "
        "threat-classification. Corrected Batch 321, 2026-10-02: the Industrial Myth quote's age "
        "corrected from 19 to 21, matching MCD-230's own correction."
    ),
    # C6: ARS-425 wrongly placed the strictly-unarmed Rexmar Machete at the Furnace District
    # Strike (MCD-244/MCD-482/MCD-372 all confirm the Strike is unarmed throughout). Drop the
    # Strike clause, keep the Sovereign Pier clause.
    "ARS-425": (
        "Extends ARS-260 (the Rexmar Machete: Kanja's ancestral, non-magical Dead Drakma field "
        "blade, passed father-to-son, predating the Trinity, never sealed in L9) with companion "
        "detail, consistent with the already-locked Long Mask timeline (MCD-246) and Sovereign "
        "Pier Accords (CC-009/MCD-085). The blade stayed on Kanja's belt continuously across his "
        "life and the full 284-year Long Mask -- worn at the Sovereign Pier -- and was the last "
        "weapon King Maro Rexmar saw his son carry before the surrender Maro himself had "
        "personally negotiated (CC-009). Physically: a worn, brass-riveted Dead Drakma laborer's "
        "tool whose handle is worn smooth by generational use and whose blade profile has "
        "narrowed roughly a centimeter through repeated sharpening across ownership predating "
        "Kanja, his father, and his grandfather. Framed, in the established Onyx voice, as "
        "categorically distinct from the Trinity: where Mafesto is 'the weapon of war' and "
        "Obsidian Malice 'the weapon of finality,' the Machete is 'the weapon of identity.' "
        "Corrected Batch 321, 2026-10-02: dropped a claim that the blade was 'worn at the "
        "Furnace District Strike' -- the Strike (MCD-244, MCD-482, MCD-372) is strictly unarmed "
        "throughout, and the Machete's companion status there would contradict that."
    ),
    # C5: Pell Ostra pronoun fix, matching her already-locked she/her (CC-132/CC-133).
    "MCD-770": (
        '"Pell Ostra\'s Last Watch of the Campaign" (full narrative text at '
        "docs/lords-of-cian/chronicles/pell-ostras-last-watch-of-the-campaign.md), The Industrial "
        "Myth Alias Chronicle XLV, wave 15 of ten (waves 6-15). The night before the Furnace "
        "District Strike, Pell Ostra reflects on the full arc of what her unarmed guard duty "
        "actually accomplished, closing the ten-wave run. Corrected Batch 321, 2026-10-02: "
        "pronoun corrected from his to her, matching her already-locked she/her (CC-132/CC-133)."
    ),
    # E4: MCD-1442's own statement said "No new named characters" while its Chronicle text
    # introduces Renner Kall by name; fix the statement to name him as a new,
    # collision-checked-clean minor character.
    "MCD-1442": (
        '"The Man Who Wouldn\'t Claim His Own Debt" (full narrative text at '
        "docs/lords-of-cian/chronicles/the-man-who-wouldnt-claim-his-own-debt.md), Industrial "
        "Myth Alias Chronicle XCIV, wave 32, first entry. The worst-off-first discipline "
        "(MCD-371) and the 'numbers don't flinch either way' impartiality theme (MCD-1065) "
        "applied for the first time against a claimant's own pride-driven self-understatement: a "
        "veteran loom-fitter deliberately understates his own unpaid overtime by more than half "
        "so as not to seem needier than younger workers; Ezio's cross-referencing corrects the "
        "figure upward against the man's own stated wishes once the attendance records show more "
        "is truly owed. Renner Kall (the veteran loom-fitter) is a new, collision-checked-clean, "
        "one-scene, unarmed, non-combat minor character with no further role implied. Strictly "
        "unarmed and non-combat throughout. Corrected Batch 321, 2026-10-02: the statement's own "
        "'No new named characters' language corrected to name Renner Kall directly, matching the "
        "Chronicle file's own continuity notes, which already named him."
    ),
}

for rid, new_statement in AMENDMENTS.items():
    assert rid in rules_by_id, f"Missing rule: {rid}"
    rules_by_id[rid]["statement"] = new_statement

ledger["batches_completed"].append({
    "batch": 321,
    "date": str(date.today()),
    "source": SOURCE,
    "rule_count": 0,
    "note": (
        "Reconciliation pass following a read-only review of the Industrial Myth Alias Chronicle "
        "corpus (102 entries). No new rules -- pure amendments to already-locked rule statements, "
        "plus matching prose-level fixes applied directly to the affected Chronicle .md files in "
        "this same batch (not tracked by this script). Ruling applied: the Furnace District "
        "Strike's age locked at 21, not 19, per the review's own airtight arithmetic (Ezio "
        "Valcari's age math only resolves at 21) -- MCD-230's and VB-061's parenthetical ages "
        "corrected, and the nine Industrial Myth file headers that said 'age 19, the Furnace "
        "District Strike' (MCD-437, 438, 439, 482, 483, 484, 534, 535, 536) plus MCD-1174's "
        "'at nineteen' corrected to twenty-one, directly in their files -- MCD-244's and "
        "MCD-373'/'753's own already-correct age-21 framing left untouched. Three entries "
        "(MCD-438, MCD-439, MCD-483) wrongly had the whole fifteen-day strike resolving on the "
        "fourth day; corrected directly in their files to distinguish the four-day tally's own "
        "conclusion from the strike's full eleven-day stand at the gate per MCD-244. The alias "
        "name's informal pre-Strike circulation (used already by six entries, MCD-753/754/759/"
        "761/762/768) reconciled against the Strike's own formal-classification origin by one "
        "added clause on MCD-230, with no changes needed to those six files' own prose. MCD-755's "
        "geography fixed (Iron Shallows, age 19, CC-130, in place of the chronologically-later "
        "Ash-Wharf evacuation) directly in its file. Pell Ostra's pronoun corrected to she/her "
        "throughout MCD-765, MCD-770, and MCD-928 (matching her already-locked she/her, "
        "CC-132/CC-133), including MCD-770's own rule statement here. ARS-425 (outside this "
        "track) corrected to drop its claim that the strictly-unarmed Rexmar Machete was worn at "
        "the Furnace District Strike, keeping only its Sovereign Pier clause. Mechanical fixes "
        "applied directly to the Chronicle files: five rule-ID citations leaked into narrative "
        "prose removed and reworded to plain prose (MCD-1150, 1159, 1169, 1173 x2, 1174); a "
        "Chronicle title leaked into in-world dialogue as if it were a place name reworded "
        "(MCD-931); six wrong footer citations corrected (MCD-439: CC-105 -> CC-027/029/030/"
        "WC-016; MCD-755: CC-116 -> CC-130/131; MCD-758: 'MCD-534 era wave' -> MCD-743; MCD-1158: "
        "MCD-928 -> MCD-405; MCD-746: 'MCD-437-439' -> MCD-438; MCD-1066: 'every prior "
        "thirty-nine-district campaign' -> 'every prior district campaign'); MCD-1442's own "
        "statement corrected to name Renner Kall directly rather than contradict its own "
        "'No new named characters' line (its Chronicle file already named him correctly); "
        "MCD-745's internal clerk-count inconsistency ('two clerks' then 'Three clerks') made "
        "consistent at two; stale Chronicle-count and supporting-cast figures corrected in "
        "`docs/lords-of-cian/chronicle-tracks-status.md` (Industrial Myth 93 -> 102; Ezio "
        "Valcari's Industrial Myth appearance count 31 -> 84) and in "
        "`docs/lords-of-cian/character-profiles/ezio-valcari.md` (same 31 -> 84 figure, two "
        "locations). Pure reconciliation throughout -- no new creative facts beyond naming an "
        "already-drafted minor character, matching the Batch 226/68/320 precedent."
    ),
})

ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
ledger["last_updated"] = str(date.today())

ids = [r["id"] for r in ledger["rules"]]
assert len(ids) == len(set(ids)), "Duplicate rule IDs detected!"

with open(LEDGER_PATH, "w") as f:
    json.dump(ledger, f, indent=2)
    f.write("\n")

print(f"OK: {len(ledger['rules'])} total rules, {len(ledger['batches_completed'])} batches, "
      f"ledger_version {ledger['ledger_version']}, zero duplicate IDs.")
