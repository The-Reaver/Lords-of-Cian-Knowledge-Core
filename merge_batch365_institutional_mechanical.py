import json
P = "canon-ledger.json"
APPROVAL = "anything that needs correction is mandated to be corrected everything has to make sense"
SOURCE = "Institutional reconciliation of locked rules against each other (MCD-297, WC-011/POL-107, MAW-022/053/089/145, MCD-145/227/219/084/218, CC-161, MCD-1880/1887, VB-062/063/064); chat-drafted 2026-10-03, no new source document"
d = json.load(open(P, encoding="utf-8"))
R = {r["id"]: r for r in d["rules"]}
nb = max(b["batch"] for b in d["batches_completed"]) + 1
touched = set()

def amend(rid, old, new):
    s = R[rid]["statement"]
    assert s.count(old) == 1, (rid, old, s.count(old))
    R[rid]["statement"] = s.replace(old, new)
    touched.add(rid)

# Item 3: Yuto = given name, Haku = designation (MCD-297)
amend("MCD-201", "Yuto Haku, Kanja's revered ancestor already locked",
      "Yuto Haku (Haku the Unifier's own given name; 'Haku' is the biological designation he carries, MCD-297), Kanja's revered ancestor already locked")

# Item 4: parallel-currency reading
amend("ASH-018", "Ashkeel's economy runs on the same Scrip used across the rest of the Shattered Kingdoms, represented locally as",
      "Ashkeel's economy runs on Trust Scrip, the parallel currency that circulates through the Shattered Kingdoms' banking houses, borderland exchanges, and underworld alongside the five nations' own physical-currency hierarchy (WC-011, POL-107). It is represented locally as")
amend("WC-011", "no access to Trust-territory markets without exchanging at Trust-controlled border rates.",
      "no access to Trust-territory markets without exchanging at Trust-controlled border rates. Trust Scrip still circulates inside the Shattered Kingdoms as a parallel currency, through Scrip-banks, the Ash Maw border exchange, cult and underworld channels, and Ashkeel's sanctuary markets (POL-107, ASH-018, CULT-015, CULT-076, WGD-009). No Shattered Kingdoms nation issues it or prices its sovereign coin in it.")

# Item 6: Osseren stays demoted; Council seats attach to doctrinal domains
amend("MAW-020", "The Seven Pillar Houses: Dravos, Korrath, Velthari, Maekar, Osseren, Threnn, Selenar, each with a founding-era doctrine and patron dynasty.",
      "The seven founding Pillar Houses: Dravos, Korrath, Velthari, Maekar, Osseren, Threnn, Selenar, each with a founding-era doctrine and patron dynasty. Osseren was stripped of Pillar status ~400 years ago (MAW-022, MAW-089) and has not been reinstated. Its doctrine remains one of the seven doctrinal domains, each holding an Iron Council seat (MAW-053, MAW-145).")
amend("MCD-081", "Pillars (7 founding Houses)",
      "Pillars (7 founding Houses; six have held Pillar status since Osseren's demotion, MAW-022/MAW-089)")
amend("MAW-035", "Pillars hold permanent hereditary Council seats; Banners hold state-issued renewable charters.",
      "Pillar status is permanent and hereditary, revocable only by the Compact for cause (once in history: Osseren, MAW-022/MAW-089), and each of the seven Pillar doctrinal domains holds a permanent Iron Council seat filled by election (MAW-053). Banners hold state-issued renewable charters.")
amend("MAW-089", "the Compact stripped Osseren's Pillar status,",
      "the Compact stripped Osseren's Pillar status (the scheme Sable Kin exposed from inside the House, MAW-022; the only Pillar demotion in Maw history, never reversed),")

# Item 10a: combat-ceiling schedule = prevailing on-page register
amend("MCD-144", "Combat density ceilings escalate on a fixed schedule across the five books, and the world's response escalates to match",
      "The prevailing on-page combat register, meaning the density levels the world openly sees fought, escalates on a fixed schedule across the five books, and the world's response escalates to match")
amend("MCD-144", "the system visibly at capacity throughout.",
      "the system visibly at capacity throughout. Concealed apex figures run above each book's register in brief, suppressed, or unwitnessed moments. In Book 1: Kanja ~18,000x ceiling (MCD-227); Ozmund 15,000x resting (MCD-219); Red Beard 16,000x actual while the world believes 4,800x (MCD-084). In Book 3: Kanja's 32,000x push (MCD-218). None of these register as world response, because the system's failure ceiling sits far higher (MCD-145).")

# Item 10b: Pier cross-reference
amend("MCD-245", "and Kanja killed nine of them and drove three into the harbor",
      "and Kanja killed nine of them (necessity kills under CC-161, dramatized at MCD-1880) and drove three into the harbor")

# Item 11
amend("MCD-1882", "records no kill spike across the whole span", "records no kill jolt across the whole span")
amend("MCD-1878", "consistent with his profile's note that Chronicle LII (MCD-1870) remains the only entry putting him personally in physical danger",
      "consistent with his profile's note that Chronicle LII (MCD-1870) was then the only entry putting him personally in physical danger (Daba Chronicle LIX, MCD-1887, later puts him at the charge footing in person)")
amend("MCD-1855", ", and is a candidate beat for a future wave of Daba's own Character Chronicle series rather than any already-drafted entry", "")
amend("MCD-1870", "Does not touch or dramatize the separate, still-undramatized Harek Vondel defeat reserved at MCD-1855.",
      "Does not touch or dramatize the separate Harek Vondel defeat (MCD-1855), later dramatized at MCD-1878.")
amend("MCD-1626", "giving narrative texture to VB-024's own standing rule that Fermand's warmth is reserved only for 'My dear Ezio.'",
      "giving narrative texture to Fermand's warmth toward 'My dear Ezio' (VB-024; for Lauris's series VB-064 supersedes the Ezio-only clause, and this entry's warmth toward Ezio stands).")
amend("VB-063", "Phase 3 27-30, Phase 4 the Long Mask.",
      "Phase 3 27-30, Phase 4 the Long Mask. At a shared boundary age (27, 30) the phase follows the event's place in the Twenty-Two Victories order: Phase 2 through Victory XIV, Phase 3 from Victory XV, Phase 4 from the sealing.")
amend("MCD-1885", "The Captain, who no longer fights, checks their arms",
      "The Captain, who no longer fights on his feet (he cannot dodge, turn fast, or run), checks their arms")
amend("MCD-262", "do the work of combat he can no longer physically perform",
      "do the work of the mobile combat he can no longer physically perform (he still walks, climbs, grips, and grounds a blow through the Forge-Coat; he no longer dodges, turns fast, or runs)")

d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": len(touched),
  "note": "Mechanical institutional reconciliations under Abad's connective-tissue mandate (\"" + APPROVAL + "\"), no new facts: MCD-201 names Yuto as Haku's given name per MCD-297; ASH-018/WC-011 reconciled as a parallel-currency reading (POL-107); Osseren stays demoted and Council seats attach to doctrinal domains (MAW-020, MAW-035, MAW-089, MCD-081); MCD-144's schedule read as the prevailing on-page register with concealed apex figures noted; MCD-245 cross-referenced to CC-161/MCD-1880; MCD-1882 'kill spike' -> 'kill jolt'; stale 'only entry / undramatized / future beat' clauses cleared in MCD-1878, MCD-1855, MCD-1870; MCD-1626 notes VB-064; VB-063 phase-boundary ages disambiguated; MCD-1885 and MCD-262 narrowed from 'no longer fights' to Chronicle VII's own 'cannot dodge, turn fast, or run'. Items needing new facts (CULT-201, CC-163, COS-001, Patient Stone renames, narrator split, near-collision renames, Aethelgard Kinetic Radiance) deliberately left for Abad's ruling."})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
