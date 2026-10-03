import json, re
P = "canon-ledger.json"
DRAFT = "docs/lords-of-cian/drafts/2026-10-03-anirak-combination-codex.md"
APPROVAL = "keep going, lock the Codex when the review is clean and connecting logically. if not, it NEVER passes."
PRIOR = "draft Anirak's Combination Codex next"
SOURCE = "Original invention, chat-drafted 2026-10-03, no source document; passed four independent adversarial reviews (clean on the fourth)"
d = json.load(open(P, encoding="utf-8"))
ids = {r["id"] for r in d["rules"]}
t = open(DRAFT, encoding="utf-8").read()
body = t.split("**Connective-tissue note.**")[0]
parts = re.split(r"\*\*(ARS-4\d\d) \(new\)\.\*\*", body)
rules = []
for i in range(1, len(parts), 2):
    rid, txt = parts[i], parts[i + 1]
    txt = re.split(r"\n---\n|\n## ", txt)[0]
    txt = txt.replace("`", "").replace("**", "")
    txt = re.sub(r"\n\s*-\s+", " | ", txt)
    txt = " ".join(txt.split())
    rules.append((rid, txt))
assert [r for r, _ in rules] == [f"ARS-{n}" for n in range(438, 448)], [r for r, _ in rules]
nb = max(b["batch"] for b in d["batches_completed"]) + 1
for rid, txt in rules:
    assert rid not in ids, rid
    d["rules"].append({"id": rid, "category": "avatar-arsenal", "statement": "Anirak's Combination Codex. " + txt + f" Abad's approval: '{PRIOR}' / '{APPROVAL}'", "status": "locked", "source": SOURCE})
d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": len(rules),
  "note": "Anirak's Combination Codex locked (ARS-438-447). It closes three gaps: the Siren's Voice as her own sub-audible felt hum, carried and shaped by the Siren Gorget forged at Chain Harbor; the Chain-Strike doctrine defined, with Stack (fuel) and Fury (heart rate, engine) linked and Stack draining under stillness; and Debt Collection defined as her hook-and-pull family. It also states her carry, the Fangs chained at the forearm and the Morning Star across her back. Named combinations: Warm (First Payment, Compound Interest, The Lien, Siren's Draw, Foreclosure); Hot (The Double Take, Echo Cast in Book 5); White (Called Debt, The Long Note); Flood State unnamed; undersea (The Drowning Spiral, Black-Water Lantern); partners (Storm and Depth with Ren, Joint Account with Lauris before Book 5); Tide Line crew (Double Draw, Mark and Collect, Two Storms, The Eastern Passage). The era gate follows from ARS-370: before Book 3 she fights at Warm only; Hot and White are Book 3 onward, fought inland in Books 3-4; active sonar first fires undersea in Book 5. Four independent reviews, NOT CLEAN three times and fixed each time, CLEAN on the fourth. Abad's approval: \"" + PRIOR + "\" / \"" + APPROVAL + "\""})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1)); d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False); open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]; print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
a = "*UNLOCKED -- pending Abad's approval. Drafted 2026-10-03"
assert t.count(a) == 1
open(DRAFT, "w", encoding="utf-8").write(t.replace(a, f"*LOCKED, Batch {nb}, 2026-10-03 (`ARS-438`-`447`), after four independent reviews (clean on the fourth). Abad's approval: \"{PRIOR}\" and \"{APPROVAL}\" Drafted 2026-10-03"))
