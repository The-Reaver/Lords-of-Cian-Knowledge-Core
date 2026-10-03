import json
P = "canon-ledger.json"
APPROVAL = "anything that needs correction is mandated to be corrected everything has to make sense"
SOURCE = "Atlas reconciliation of research/atlas-live-sheet-audit.md against locked MAW-060/061/063/065, POL-010/090, GEO-003/006 and the Batch 40 rename (MCD-275); chat-drafted 2026-10-03, no new source document"
d = json.load(open(P, encoding="utf-8"))
R = {r["id"]: r for r in d["rules"]}
nb = max(b["batch"] for b in d["batches_completed"]) + 1
touched = set()

def amend(rid, old, new):
    s = R[rid]["statement"]
    assert s.count(old) == 1, (rid, old, s.count(old))
    R[rid]["statement"] = s.replace(old, new)
    touched.add(rid)

# MCD-147: finish the Batch 40 geographic rename; diffuse trace Living Drakma reading
amend("MCD-147", "the Verehimu Wetlands, the Broken Meridian",
      "the Voskharen Wetlands (the Batch 40 rename of the source's reused geographic 'Verehimu,' MCD-275), the Broken Meridian")
amend("MCD-147", "a small Verehimu Archipelago island partially submerges",
      "a small island off the Voskharen coast partially submerges")
amend("MCD-147", "Living Drakma deposit density is distributed unevenly across the crust",
      "Living Drakma deposit density -- diffuse trace Living Drakma dispersed through the crust (the anomalous concentrations Lauris has detected since her arrival, MCD-207), increasingly reinforced around Kanja's operational presence by the Talisman's Stage 2 incorporation (MCD-208), not workable ore; the Moonvault remains the only known workable deposit outside Mao (MCD-287/MCD-315) -- is distributed unevenly across the crust")

# The Teeth placement
amend("MAW-063", "The Teeth (Maw-12, Frontier) --", "The Teeth (Maw-12, the Frontier Maw, Atlas cell N16, GEO-007) --")
amend("POL-090", "the Frontier Maw,",
      "the Frontier Maw (sited just past the Reaches' eastern edge in the Shattered Kingdoms frontier region, GEO-003/GEO-007, but economically bound into the Reaches' border-exchange system),")

# Jicome Eastern Seaboard -> Southern Seaboard
amend("MCD-237", "on the Jicome Eastern Seaboard simultaneously", "on Jicome's stretch of the Southern Seaboard simultaneously")

# Prefecture coastline
amend("POL-040", "The Obsidian Prefecture is a western inland plateau power,",
      "The Obsidian Prefecture is a western plateau power, its heartland inland but holding a short western coastline (the port of Vance, the coast-drum Vanegate, and the coastal Drowning Floor at Praetura, GEO-003/MAW-063),")

# Ash Harbor near-landlocked basin
amend("MCD-235", "a six-warship blockade of a landlocked basin",
      "a six-warship blockade of a near-landlocked basin (a Port-class harbor, GEO-006, reached only through a reef gap, CC-131)")
amend("GEO-006", "Ash Harbor (Settlement, Port-class, cell A09,",
      "Ash Harbor (Settlement, Port-class near-landlocked basin reached through a reef gap, MCD-235/CC-131, cell A09,")

# GEO-007 (new)
assert "GEO-007" not in R
GEO011 = ("The Atlas's two canon-locked Maw names are both placed: the Throat lies within Karkosa (KA, G16; MAW-060), and the Teeth is the Frontier Maw (overlay code TE, N16; MAW-061 Maw-12), on the western edge of the Shattered Kingdoms frontier region -- the Trust's farthest-forward capital-registry venue on Shattered Kingdoms ground, roughly a thousand miles east of the Sovereign Trust Domain across the Lawless Reaches, economically bound into the Reaches' border-exchange system (POL-090/POL-107); the Moonvault (O18) lies roughly 800 km beyond it (MCD-315). The Old Dominion's former capital -- T.D.K.'s original court complex -- survives as the ruins housing the Ash Maw/the Scar (J19, Lawless Reaches; MAW-065); the Old Dominion Ruins region (OD) is the empire's ruined northern heartland, which is why it has no capital (GEO-003). The grid codes RA (10 cells around Rathaan Prime and the Ash Maw Scar) and UK (5 cells around Ironhold, on the 'UK Spur') are sub-areas of the Lawless Reaches -- its own region tab places Rysgate at D11 and Duskvane at I20 -- and count toward its share (POL-010); what the two codes stand for remains open (OPEN-012).")
d["rules"].append({"id": "GEO-007", "category": "atlas-canon-sites", "statement": GEO011, "status": "locked", "source": SOURCE})
touched.add("GEO-007")

# OPEN-012
o = [x for x in d["open_decisions"] if x.get("id") == "OPEN-012"]
assert len(o) == 1
o = o[0]
oldn = "on the border between the Sovereign Trust's territory and the Shattered Kingdoms."
assert o["note"].count(oldn) == 1
o["note"] = o["note"].replace(oldn, "on the political frontier of Trust reach -- sited on the western edge of the Shattered Kingdoms region at Atlas cell N16 (overlay code TE), roughly a thousand miles east of the Sovereign Trust Domain across the Lawless Reaches (GEO-007).")
assert o["statement"].count("represent?") == 1
o["statement"] = o["statement"].replace("represent?", "represent? (Region membership is resolved by GEO-007: both are Lawless Reaches sub-areas; only what the two codes stand for remains open.)")

d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": len(touched) + 1,
  "note": "Mechanical Atlas reconciliations under Abad's connective-tissue mandate (\"" + APPROVAL + "\"), no new creative facts: MCD-147's geographic 'Verehimu' completed to Voskharen per the Batch 40 rename (MCD-275) and its deposits read as diffuse trace Living Drakma consistent with WC-013/MCD-287/MCD-315; the Teeth placed at Atlas cell N16 (MAW-063, POL-090, OPEN-012 note, new GEO-007, which also records the Throat, the Old Dominion capital at the Scar ruins, and RA/UK as Lawless Reaches sub-areas); MCD-237 'Jicome Eastern Seaboard' -> Southern Seaboard (the 2026-08-08 correction never applied to the ledger); POL-040 given its short western coastline; Ash Harbor read as a near-landlocked reef-gap basin (MCD-235, GEO-006). OPEN-012 now asks only what RA/UK stand for. Wetlands two-place question, the Karkosa ship rename, MAW-078, WC-012, MCD-112, MCD-094, GEO-007 through GEO-010 and the Ironhold disambiguation deliberately left for Abad's ruling."})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
