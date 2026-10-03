import json, re
P = "canon-ledger.json"
D = "docs/lords-of-cian/chronicles/"
APPROVAL = "go"
SOURCE = "Original invention, chat-drafted 2026-10-02/03, no source document"
d = json.load(open(P, encoding="utf-8"))
E = [
 ("MCD-1883", "kanja-chronicle-v-the-names-in-the-correction-book.md", "No child-safety issues.*",
  "Kanja Chronicle V, 'The Names in the Correction Book' (full text at docs/lords-of-cian/chronicles/kanja-chronicle-v-the-names-in-the-correction-book.md). Fifth entry of the Kanja-version track and the first Long Mask Onyx account (VB-062, ARS-437, VB-063 Phase 4). Age 55. Dramatizes the Chain Harbor Massacre (MCD-251) for the first time: garrison master Edric Grenmoor orders all six harbor-wall pens (912 prisoners) drowned at the top of the flood while Anirak breaks fetters in the eastern passage; the Captain stops the west sluice wheel (Dunmore and eight others killed turning it, the ninth kneels and is spared) while Torian boils the east wheel housing; the 220-strong garrison then charges to retake the wheels, terms are called once, every man who sits is untouched, and the 32 who come at him die; Skarrow dies reopening the east gate and Grenmoor dies on the drowning steps after hauling the drowning-gate bar and drawing first -- 43 deaths, all necessity kills under CC-161 (Batches 355-356), nothing read to anyone. Only afterward does the Captain take the garrison's correction book and hand it to the spared keeper Mabry ('Keep writing. Every name. Mine with them.'); Onyx's own verdict, after the fact, is that every man who died is in the book and no man outside it died. Anirak's recruitment and the forging of her chained hook-swords, gorget (built to carry her own Siren voice), and three-shape mace (ARS-130/411) follow. Kanja's second marquee kill under MCD-1881, his first of the Long Mask. New named characters: Edric Grenmoor, Dunmore, Skarrow (killed), Mabry (spared)."),
 ("MCD-1884", "kanja-chronicle-vi-vellacourts-rule.md", "No child-safety issues.*",
  "Kanja Chronicle VI, 'Vellacourt's Rule' (full text at docs/lords-of-cian/chronicles/kanja-chronicle-vi-vellacourts-rule.md). Sixth entry of the Kanja-version track, a Long Mask Onyx account (VB-062, ARS-437, VB-063 Phase 4). Age 48, the opening act of the Pirate Dawn, weeks before the Night of Black Sails (MCD-250) -- the Captain's first kill since the Sovereign Pier, closing MCD-1882's no-kill window. Admiral Teshar Vellacourt, a bought-rank convoy admiral under a Sovereign Trust forced-labor charter paid per head for 'cargo lost to piracy,' floods his holds when pursued (Vellacourt's Rule, copied onto nine ships; 612 drowned by his own filings). After a season spent working out how to board a ship nobody can board, the Captain swims under the hull, ruins both sea-cock spindles, reaches the 340 chained below, then stands on the lit deck and states terms once ('Sit. You row home.'). The lever fails twice; Vellacourt reads his charter aloud, orders lamp oil into the hold, carries a lantern to the hatch himself, and draws; the cutlass opens the Captain's left wrist through the unbraced V1 gauntlet gap, and one stroke of the Rexmar Machete kills him in the attack -- a necessity kill under CC-161. Sailing master Mordane carries the account home ('Tell it exact.'); the harbors draw the two-ways lesson themselves, the red levers come out within a season, and ships later strike to the black sails on sight. Marquee kill under MCD-1881. New named characters: Teshar Vellacourt (killed), Mordane."),
 ("MCD-1885", "kanja-chronicle-vii-the-man-who-did-not-get-up.md", "No child-safety issues.*",
  "Kanja Chronicle VII, 'The Man Who Did Not Get Up' (full text at docs/lords-of-cian/chronicles/kanja-chronicle-vii-the-man-who-did-not-get-up.md). Seventh entry of the Kanja-version track, a Long Mask Onyx account (VB-062, ARS-437, VB-063 Phase 4). Age 240. Dramatizes the Sleeping Giant (MCD-262) for the first time: twelve Choice-Branded commandos contracted around Standing Order 44-B attack a rock-cut salt cellar holding eleven Ghost-Lattice copyists while Valen and Stormbreaker chase a false signal. The Captain, who no longer fights, checks their arms (no Cestari among them -- a filter for whom he will not kill), states terms once ('Walk back. You live.'), and all twelve refuse; every blow they land is drunk by the Talisman and routed down his bones into the bedrock floor, leaving each man stopped at the end of his own strike for the half-second that ends him. Verrick alone reads him and wounds him with slow pressure under the left ribs. After eleven are dead Garrick asks whether the offer stands and is answered 'Yes. Walk.'; he stays for the unpaid half of the contract and attacks -- every kill a necessity kill under CC-161. The Sleeping Giant's preview of the eventual Pi-Awakening is carried by a single unremarked detail: the stone under the Captain's heels pressed down a finger deep, smooth as a worn stair. Origin of the crew's 'the old man doesn't get up' and Valen's immobility-as-a-weapon doctrine. Marquee kill under MCD-1881. New named characters: Garrick, Rusk, Verrick, Ghast (all killed)."),
]
ids = {r["id"] for r in d["rules"]}
for rid, fn, tail, stmt in E:
    assert rid not in ids, rid
    t = open(D + fn, encoding="utf-8").read()
    pat = r"\*UNLOCKED -- pending Abad's approval\. Draft,? 2026-10-03(?: \(redraft of the 2026-10-02 draft\))?\."
    assert len(re.findall(pat, t)) == 1, fn
    t = re.sub(pat, lambda m: f"*Locked canon, Batch {{NB}}, 2026-10-03 (`{rid}`).", t)
    m = re.search(r"No\s+child-safety\s+issues\.\*", t)
    assert m, fn
    t = t[:m.start()] + m.group(0)[:-1] + f" Abad's approval: \"{APPROVAL}.\"*" + t[m.end():]
    open(D + fn, "w", encoding="utf-8").write(t)
    d["rules"].append({"id": rid, "category": "kanja-character-chronicle", "statement": stmt + " Abad's approval: '" + APPROVAL + "'", "status": "locked", "source": SOURCE})
nb = max(b["batch"] for b in d["batches_completed"]) + 1
for _, fn, _, _ in E:
    p = D + fn; t = open(p, encoding="utf-8").read().replace("{NB}", str(nb)); open(p, "w", encoding="utf-8").write(t)
d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": 3,
  "note": "Kanja Chronicles V-VII locked (MCD-1883-1885): the first Long Mask Onyx accounts -- Chain Harbor (age 55), Vellacourt's Rule (age 48, first kill since the Pier), the Sleeping Giant (age 240) -- redrafted to the VB-063 Phase 4 voice and the CC-161 necessity-kill doctrine before presentation. Abad's approval: \"" + APPROVAL + "\""})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
