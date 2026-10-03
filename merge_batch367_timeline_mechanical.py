import json
P = "canon-ledger.json"
APPROVAL = "anything that needs correction is mandated to be corrected everything has to make sense"
SOURCE = "Timeline/age/chronology reconciliation of locked rules against each other (MCD-175-198, ARS-344, MCD-1850, MCD-151, MCD-242, CC-037, CC-101); chat-drafted 2026-10-03, no new source document"
d = json.load(open(P, encoding="utf-8"))
R = {r["id"]: r for r in d["rules"]}
nb = max(b["batch"] for b in d["batches_completed"]) + 1
touched = set()

def amend(rid, old, new):
    s = R[rid]["statement"]
    assert s.count(old) == 1, (rid, old, s.count(old))
    R[rid]["statement"] = s.replace(old, new)
    touched.add(rid)

# Item 3 (Lauris only): MCD-267 aligned to MCD-175-198
amend("MCD-267", "Lauris Letitia's exfiltration (age 260): Lauris, then a 12-year Sovereign Trust field contractor, was identified by Ezio's intelligence network",
      "Lauris Letitia's recruitment (age ~114): Lauris, then a ~1,800-year Sealbound Directorate external asset (MCD-175 through MCD-192), was identified by Ezio's intelligence network")

# Item 5: Valen
amend("MCD-248", "is the origin scene for the already-locked Sinisterblade (Valen Valcari, Sinister Bloodline, age 23 at the time), who publicly tested whether 'the man or the equipment' made the Scourge dangerous and, having lost, chose to join.",
      "is the origin of the Sinisterblade's public legend: Valen Valcari (Sinister Bloodline), Kanja's Master-at-Arms since the Rebellion (ARS-344), publicly tested in a staged duel whether 'the man or the equipment' made the post-Trinity Scourge dangerous -- the question his own Valen Protocol had raised -- and, having lost, recommitted to the crew for the Long Mask.")

# Item 7a: Drakmund = first Verehimu, 8,000+ years (MCD-1850)
amend("MCD-138", "roughly 5,000 years old, contemporary with T.D.K.'s Deposition.",
      "at least ~8,000 years old -- the Root-Born Aethel-Gard general of MCD-1850, elevated and Crown-Scarred by T.D.K. ~8,000 years ago, who betrayed him at the Deposition ~5,000 years ago (WC-001, WC-020).")
amend("MCD-1740", "the original Crown-Scar recipient, ~5,000 years old)", "the original Crown-Scar recipient, ~8,000+ years old)")
amend("MCD-1749", "late in his five-thousand-year life", "deep into his very long life")

# Item 7b: MCD-149 adulthood-phase labels for the Kareth sisters
amend("MCD-149", "Val Saeryn Kareth (93,179 years) sits in late second adulthood; Val Mirel Kareth (89,003) in mature second adulthood -- both currently alive and in deep cover per MCD-137, not late in life by Karesian standards at all.",
      "These phases are the homeworld's; the Kareth diaspora's extended ~150,000-year span (MCD-151) runs them proportionally longer (second adulthood ~36,000-90,000, third ~90,000-135,000), so Val Saeryn Kareth (93,179 years) has just entered third adulthood and Val Mirel Kareth (89,003) sits at the close of second adulthood -- both currently alive and in deep cover per MCD-137, not late in life by Kareth standards at all.")

# Item 10d: Silent Mara hedge
s = R["MAW-128"]["statement"]
a = "The source speculates, explicitly hedged as unconfirmed"
b = "given the Rex/Mar bloodline's extreme longevity."
assert s.count(a) == 1 and s.count(b) == 1 and s.index(a) < s.index(b)
i, j = s.index(a), s.index(b) + len(b)
R["MAW-128"]["statement"] = s[:i] + ("The source speculates that those operatives were Anansi's Ghost-Lattice network; that cannot be so -- Mara vanished ~700 years ago, "
    "nearly four centuries before Kanja's birth and the network's seeding during his Rebellion (MCD-242, roughly three centuries before Book 1). "
    "The Brand-Line's later habit of crediting the Ghost-Lattice is myth-making after the fact; who her 'friends in the dark' were remains open.") + s[j:]
touched.add("MAW-128")

# Item 11b: Sephtis as archival knowledge
amend("MCD-196", "his disclosure that he had known of her existence since the orbital-trade rumor reports following the Vask Olmedrin defense -- roughly 1,200 years before her arrival on Cian -- making him the only being on the planet continuously aware of her since before she arrived.",
      "his disclosure that his archive held the orbital-trade rumor reports following the Vask Olmedrin defense -- dating from roughly 1,200 years before her arrival on Cian -- and that he had followed her from early in his own life onward.")
# Item 11c: Black Ledger reservation span
amend("MCD-201", "for roughly 1,200 years", "for roughly 3,000 years")
# Item 11d: Merak-era
amend("MCD-1851", "Old Dominion-era events", "Merak-era events")

d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": len(touched),
  "note": "Mechanical timeline/age reconciliations under Abad's connective-tissue mandate (\"" + APPROVAL + "\"), no new facts: MCD-267 aligned to Lauris's ~age-114 recruitment and ~1,800-year Directorate career (MCD-175-198); MCD-248 drops Valen's contradicting age 23 and recasts the White Void Duel as the origin of his public legend, since he is Master-at-Arms since the Rebellion (ARS-344); MCD-138/MCD-1740/MCD-1749 align Drakmund with MCD-1850 as the same first Verehimu, 8,000+ years old; MCD-149's adulthood-phase labels for the Kareth sisters scaled to the diaspora's ~150,000-year span (MCD-151); MAW-128's Silent Mara hedge resolved against the locked Rebellion chronology; MCD-196 recast so Sephtis held archival reports rather than personal awareness, and MCD-201's Black Ledger reservation span corrected to roughly 3,000 years; MCD-1851 'Old Dominion-era' -> 'Merak-era'. Items needing new facts (A1 284/296, Kares Prime collapse scale, Fermand's joining date, Haryn Dael's age, Ezio's age and sixth-knower, Matar, Orlok, Red Beard narration, Brekka, Aravel, Essek, Maw eras) deliberately left for Abad's ruling."})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
