"""Batch 374: mechanical conflict fixes -- banned words, a name collision, and tech-level breaks.

Abad's direction: 'keep going, fix those conflicts too'. Each change only realigns a locked rule or
entry with already-locked canon (VB-013, VB-050, VB-010, ARS-020/CC-013, WC-013, CULT-199).
"""
import json
from collections import Counter

LEDGER = "canon-ledger.json"
APPROVAL = "Abad's direction: 'keep going, fix those conflicts too'."
NOTE = " Corrected Batch 374, 2026-10-04: {}."

EDITS = {
    "CC-021": [("Old Dominion's Maw gladiatorial economy", "Old Dominion's Maw fighting economy")],
    "CC-085": [("Ozmund's entry into the Accession Games as a gladiator", "Ozmund's entry into the Accession Games as a fighter")],
    "CC-090": [("fighting in the Accession Games arena", "fighting in the Accession Games")],
    "CC-155": [("in shifting arenas", "in shifting pits")],
    "WGD-001": [("arena and betting circles", "Pit and betting circles")],
    "WGD-006": [("(arena stock,", "(Pit stock,"), ("the arena-betting circles", "the Pit-betting circles")],
    "WGD-008": [("the Weregildd's arena circuit", "the Weregildd's fighting circuit"), ("in shifting arenas", "in shifting pits")],
    "ASH-046": [("trial arenas", "trial grounds")],
    "MCD-234": [("undermining the arena's own load-bearing", "undermining the Maw's own load-bearing")],
    "MAW-031": [("House Galthorn ('the Black Ledger')", "House Galthorn ('the Black Dot')")],
    "MAW-136": [('House Galthorn ("the Black Ledger")', 'House Galthorn ("the Black Dot")')],
    "MAW-146": [("synchronized to the specific venue crowd's acoustic recordings",
                 "paced to the known roar of the specific venue's crowd")],
    "ASH-007": [("Closed-loop supercritical carbon dioxide turbines draw electrical power directly from the roughly four-hundred-degree thermal gradient between the summit and the base, and the same loop vents its waste heat into the central Updraft Core chimney that already carries stale air to the surface, so power generation and cooling solve each other's byproduct in one pass.",
                 "Sealed heat-galleries carry warmth up from the roughly four-hundred-degree thermal gradient between the summit and the base, and vent it into the central Updraft Core chimney, whose draw pulls fresh air down through every level and carries stale air to the surface, so heating and ventilation solve each other's byproduct in one pass, by convection and stone, with no engine and no electricity.")],
    "ASH-048": [("powers the entire monolith via a closed-loop supercritical-CO2 turbine cycle drawing on 450C mantle-boundary heat,",
                 "heats and ventilates the entire monolith by convection from 450C mantle-boundary heat carried up through sealed heat-galleries (ASH-007),")],
}
WHY = {
    "CC-021": "a banned Maw-terminology word replaced (VB-013/VB-050)",
    "CC-085": "a banned Maw-terminology word replaced (VB-013/VB-050)",
    "CC-090": "a banned venue word replaced (VB-050)",
    "CC-155": "a banned venue word replaced (VB-050)",
    "WGD-001": "a banned venue word replaced (VB-050)",
    "WGD-006": "a banned venue word replaced (VB-050)",
    "WGD-008": "a banned venue word replaced (VB-050)",
    "ASH-046": "a banned venue word replaced (VB-050)",
    "MCD-234": "a banned venue word replaced (VB-050)",
    "MAW-031": "House Galthorn's epithet renamed from 'the Black Ledger', which collided with Onyx's Black Ledger (ARS-020, CC-013), to 'the Black Dot', after its own mark (MAW-136)",
    "MAW-136": "House Galthorn's epithet renamed from 'the Black Ledger', which collided with Onyx's Black Ledger (ARS-020, CC-013), to 'the Black Dot', after the house's own mark",
    "MAW-146": "'acoustic recordings' removed; no recording technology exists (WC-013, CULT-199)",
    "ASH-007": "electrical turbines removed; heating and ventilation now by convection, consistent with the setting's tech level (CULT-199)",
    "ASH-048": "electrical turbine cycle removed; aligned with the corrected ASH-007",
}

FILES = {
    "docs/lords-of-cian/chronicles/the-meal-he-ate-as-no-one.md": [
        ("he gave any operational report — none of it true, exactly, and none of it entirely a lie either,\neach version some fragment of an actual night reshaped",
         "he gave any operational report: each version a fragment of an actual night, reshaped")],
    "docs/lords-of-cian/chronicles/chronicle-vi-the-sewer-war-of-killane.md": [
        ("matching the arena/Maw terminology", "matching the Maw terminology")],
    "docs/lords-of-cian/chronicles/the-weight-maret-vos-chose-to-carry.md": [
        ("was swapped for an arena-appropriate one", "was swapped for a Maw-appropriate one")],
}

d = json.load(open(LEDGER, encoding="utf-8"))
rules = {r["id"]: r for r in d["rules"]}
for rid, pairs in EDITS.items():
    s = rules[rid]["statement"]
    for old, new in pairs:
        assert s.count(old) == 1, (rid, old)
        s = s.replace(old, new)
    rules[rid]["statement"] = s + NOTE.format(WHY[rid]) + " " + APPROVAL
for path, pairs in FILES.items():
    t = open(path, encoding="utf-8").read()
    for old, new in pairs:
        assert t.count(old) == 1, (path, old)
        t = t.replace(old, new)
    open(path, "w", encoding="utf-8").write(t)

nb = max(b["batch"] for b in d["batches_completed"]) + 1
assert nb == 374, nb
d["batches_completed"].append({
    "batch": nb,
    "source": "Conflicts surfaced by the account craft standard's canon survey, 2026-10-04",
    "rules_affected": len(EDITS),
    "note": "Mechanical conflict fixes, no new plot facts: banned Maw-terminology and venue words replaced in CC-021, "
            "CC-085, CC-090, CC-155, WGD-001, WGD-006, WGD-008, ASH-046, MCD-234 (and two Chronicle header "
            "notes); House Galthorn's epithet renamed 'the Black Dot' (MAW-031, MAW-136) to clear its "
            "collision with Onyx's Black Ledger; MAW-146's 'acoustic recordings' and ASH-007/ASH-048's "
            "electrical turbines removed as tech-level breaks; MCD-825's prose antithesis removed (VB-010). "
            + APPROVAL,
})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-04"
json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(LEDGER, "a", encoding="utf-8").write("\n")
d = json.load(open(LEDGER, encoding="utf-8"))
dups = [k for k, v in Counter(r["id"] for r in d["rules"]).items() if v > 1]
print("duplicates:", dups, "| rules:", len(d["rules"]), "| version:", d["ledger_version"],
      "| batch:", max(b["batch"] for b in d["batches_completed"]))
