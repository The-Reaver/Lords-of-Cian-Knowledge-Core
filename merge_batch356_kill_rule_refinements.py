import json, re
P = "canon-ledger.json"
CH4 = "docs/lords-of-cian/chronicles/kanja-chronicle-iv-ninety-seconds-on-the-sovereign-pier.md"
APPROVAL = "approved"
SOURCE = "Original invention, chat-drafted 2026-10-03, no source document"
d = json.load(open(P, encoding="utf-8"))
R = {r["id"]: r for r in d["rules"]}

# 1. MCD-1882: pin the window's closing boundary.
s = R["MCD-1882"]["statement"]
old = "until the opening of the Pirate Dawn (age ~48, MCD-250)"
assert s.count(old) == 1
s = s.replace(old, "until the opening of the Pirate Dawn at age 48 (MCD-250)")
s += (" Amended Batch 356, 2026-10-03: ages 31 through 47 are kill-free by his own hand; his first kill "
      "after the Pier is the Pirate Dawn's opening act at age 48, in the weeks before the Night of Black "
      "Sails. Abad's approval: '" + APPROVAL + "'")
R["MCD-1882"]["statement"] = s

# 2. CC-161: close the gaps the drafts exposed.
s = R["CC-161"]["statement"]
assert "Amended Batch 356" not in s
s += (" Amended Batch 356, 2026-10-03: a person who is fleeing or disengaging is no longer a threat. "
      "Checking a brand or a Maw-slave mark to decide whom he will not kill is a filter and is permitted; "
      "demanding names or a count of the dead is not. He may state terms of surrender once; he never "
      "announces a death in advance. Abad's approval: '" + APPROVAL + "'")
R["CC-161"]["statement"] = s

# 3. Chronicle IV: Caddel is an active threat, not leaving.
t = open(CH4, encoding="utf-8").read()
pat = r"Caddel\s+tried\s+to\s+go\s+over\s+the\s+rail"
assert len(re.findall(pat, t)) == 1
t = re.sub(pat, "Caddel went over the rail to come at the king from the water side", t)
hdr_old = 'Abad\'s approval: "go with retrospective, keep\nthe two years, lock it."*'
assert t.count(hdr_old) == 1
t = t.replace(hdr_old, hdr_old[:-1] + " Corrected Batch 356, 2026-10-03: Caddel goes over the rail to\ncome at the king from the water side, so her death is a necessity kill under `CC-161`; Abad's\napproval: \"approved.\"*")
open(CH4, "w", encoding="utf-8").write(t)
s = R["MCD-1880"]["statement"]
s += (" Corrected Batch 356, 2026-10-03: Caddel goes over the rail to come at the king from the water side "
      "rather than to escape, keeping all nine kills necessity kills under CC-161. Abad's approval: '" + APPROVAL + "'")
R["MCD-1880"]["statement"] = s

nb = max(b["batch"] for b in d["batches_completed"]) + 1
d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": 3,
    "note": "Kill-audit refinements: MCD-1882 boundary pinned (ages 31-47 kill-free, first kill after the Pier at 48); CC-161 adds fleeing/disengaging = no threat, brand-check filter permitted, terms stated once, no announced deaths; Chronicle IV/MCD-1880 Caddel made an active threat. Abad's approval: \"" + APPROVAL + "\""})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
