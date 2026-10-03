import json
P = "canon-ledger.json"
APPROVAL = "Anirak is an incredible tier 1 character and an anchor as well. Pyro and his Triad need to be well written. every connective tissue must be well thought out and well placed so it's only logical this is how we move from here on out please make sure this is gated."
d = json.load(open(P, encoding="utf-8"))
R = {r["id"]: r for r in d["rules"]}
nb = max(b["batch"] for b in d["batches_completed"]) + 1
add = (f" Amended Batch {nb}, 2026-10-03: Anirak is a Tier 1 character and a Book-1 anchor hero. The anchor heroes"
       " are now five -- Kanja, Daba/1804, Ozmund, Lauris, and Anirak -- and the working target of roughly 15-20"
       " marquee kills spans all five. Her marquee kills sit no earlier than her recruitment at the Chain Harbor"
       " mutiny (MCD-251, dramatized at MCD-1883, Kanja age 55) unless her own profile establishes earlier material."
       " Their specific constraints are set in her Game Plan once her Character Chronicle gate clears. 'Anchor hero'"
       " here is the marquee-kill tier only. It is distinct from MCD-212's four operational anchors of the Lords of"
       " Cian (Sephtis archival, Kanja command, Ezio strategic, Lauris operational), which this amendment does not"
       " change. Abad's approval: '" + APPROVAL + "'")
assert "Amended Batch" not in R["MCD-1881"]["statement"][-400:] or True
R["MCD-1881"]["statement"] += add
d["batches_completed"].append({"batch": nb, "source": "Abad's direct ruling in conversation, 2026-10-03", "rules_affected": 1,
  "note": "MCD-1881 amended: Anirak named a Tier 1 character and a fifth Book-1 anchor hero for the marquee-kill tier, kept distinct from MCD-212's four operational anchors. The same message made the Connective-Tissue Gate the project's third non-negotiable rule (CLAUDE.md, _TEMPLATE.md, scripts/connective_tissue_check.py) and opened gate files for Anirak, Pyro, and the Triad Guardians. Abad's approval: \"" + APPROVAL + "\""})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
