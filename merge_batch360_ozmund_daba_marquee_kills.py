import json, re
P = "canon-ledger.json"
D = "docs/lords-of-cian/chronicles/"
APPROVAL = "as long as it makes sense I approve"
SOURCE = "Original invention, chat-drafted 2026-10-03, no source document"
d = json.load(open(P, encoding="utf-8"))
E = [
 ("MCD-1886", "ozmund-character-chronicle", "ozmund-chronicle-cxxi-the-night-the-dike-held.md",
  "Ozmund Chronicle CXXI, 'The Night the Dike Held' (full text at docs/lords-of-cian/chronicles/ozmund-chronicle-cxxi-the-night-the-dike-held.md). Ozmund Verehimu's single pre-Fulfillment-Ceremony marquee kill under MCD-1881, unwitnessed by Colonel Viktor Draconis (CC-085), narrated by Red Beard to the Voice Bible's Narrator 2 sheet. Grown but pre-Ceremony, Ozmund walks alone at night to Lowmere, a fen hamlet east of Greyfen (eleven houses below the waterline, forty-one people), to hear a petition from a dike warden whose hand was broken by Marek Draye -- a Branded deserter from a provincial circuit, roughly 600x density, extorting a toll on the dike road. Draye is levering the sluice-gate chain toward failure, which would breach the dike and drown the hamlet within a minute. Ozmund gives one command ('Step off.'); Draye pulls; with grappling, striking the bar, and waiting all ruled out on the page, Ozmund kills him with one open hand to the chest -- the Density Spike shown by effect only -- and Draye goes into the fen, never recovered. Ozmund resets the chain and leaves before dawn without revealing himself. The unattributed legend 'the night the dike held itself' spreads through the wetlands and can be referenced in Book 1; Draconis, returning from the northern circuit with Aethelgard, reads it as weather and luck and doubles the wetland guard at his own expense. Red Beard records it as the one kill of Ozmund's two hundred years before the Ceremony; the Book 3 Dark Monarch escalation stays unspent. New named characters: Marek Draye (killed); new place: Lowmere."),
 ("MCD-1887", "daba-character-chronicle", "daba-chronicle-lix-the-count-at-the-bottom-of-the-stair.md",
  "Daba Chronicle LIX, 'The Count at the Bottom of the Stair' (full text at docs/lords-of-cian/chronicles/daba-chronicle-lix-the-count-at-the-bottom-of-the-stair.md). Daba's marquee kill under MCD-1881, and the single personal kill that rule allows him (every other 1804 marquee kill stays network-executed). Set in the network's mature era. Orsk Dresk intercepts a quartermaster's requisition for oil, pitch, and stair charges for a Trust correction column against the Fenwold blocks; 1804 evacuates quietly under a fever rumor rather than fight the column (MCD-1567), with Daba personally chalking every likely charge footing. The column arrives a night early with twenty-two people (a laundry-guild children's night class and four teachers) still on the east block's fourth floor; Mika counts them down the service stair while Daba finds an officer at the chalked footing moving a lit slow-match to the fuse, and kills him with a short blade under the jaw -- a necessity kill made before he knows who the man is -- then crushes the coal out in his bare left hand. Twenty-two at the top, twenty-two at the bottom: the count that came out wrong at the Rookery (MCD-1571) comes out right. The column burns both blocks empty; no one dies. Only afterward does the officer's service book name him -- Captain Edran Brannick -- and record 'Rookery. Correction. Stairs first. Complete.', so the Rookery connection surfaces only after the fact and the scene never reads as vengeance. Daba does not add Brannick's name to his private list, which holds only 1804's own dead (MCD-1610). The kill stays publicly unattributed (MCD-1569): the Trust lists Brannick as lost to a fire of undetermined origin, mirroring its record of the Rookery (MCD-1566); inside 1804 it is called the Fenwold stair. New named characters: Captain Edran Brannick (killed); new place: the Fenwold blocks."),
]
ids = {r["id"] for r in d["rules"]}
nb = max(b["batch"] for b in d["batches_completed"]) + 1
for rid, cat, fn, stmt in E:
    assert rid not in ids, rid
    t = open(D + fn, encoding="utf-8").read()
    pat = r"\*UNLOCKED -- pending Abad's approval\. Draft, 2026-10-03, proposed `" + rid + "`\."
    assert len(re.findall(pat, t)) == 1, fn
    t = re.sub(pat, lambda m: f"*Locked canon, Batch {nb}, 2026-10-03 (`{rid}`). Abad's approval: \"{APPROVAL}.\"", t)
    open(D + fn, "w", encoding="utf-8").write(t)
    d["rules"].append({"id": rid, "category": cat, "statement": stmt + " Abad's approval: '" + APPROVAL + "'", "status": "locked", "source": SOURCE})
d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": 2,
  "note": "Ozmund Chronicle CXXI and Daba Chronicle LIX locked (MCD-1886, MCD-1887): the anchor-hero marquee kills under MCD-1881 for Ozmund (his single pre-Ceremony kill, Marek Draye at the Lowmere dike, unwitnessed by Draconis) and Daba (his single personal kill, Captain Edran Brannick at the Fenwold stair, the Rookery link surfacing only afterward). Both written to the gated Voice Bible standard. Abad's approval: \"" + APPROVAL + "\""})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
