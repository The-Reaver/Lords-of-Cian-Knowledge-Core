import json
P = "canon-ledger.json"
d = json.load(open(P, encoding="utf-8"))
APPROVAL = "go with your recommendation on the CC-161 amendment"
SOURCE = "Original invention, chat-drafted 2026-10-03, no source document"
ADD = (" Amended Batch 355, 2026-10-03: before Maro Rexmar's death, every kill by Kanja's own hand is a "
    "necessity kill -- the person is an active, immediate threat to life in that moment (attacking, or "
    "working the wheel, lever, or blade that is killing others). He never names or recites a person's "
    "crimes, asks them to confirm their guilt, or pronounces a verdict and then kills them; he never "
    "executes a man who is surrendering or no longer a threat, deterrence included -- an offered "
    "surrender is honored. Any deterrent effect is a consequence others carry away, never his stated "
    "reason. Judgment of the dead belongs to Onyx's narration after the fact (the Black Ledger's "
    "Iron/Rust verdicts), never to Kanja beforehand. The verdict-then-execution register stays reserved "
    "for after Maro's death, alongside the urge to destroy his enemies. Abad's approval: '" + APPROVAL + "'")
n = 0
for r in d["rules"]:
    if r["id"] == "CC-161":
        assert "Amended Batch 355" not in r["statement"]
        r["statement"] += ADD
        n += 1
assert n == 1
nb = max(b["batch"] for b in d["batches_completed"]) + 1
d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": 1,
    "note": "CC-161 amended: pre-Book-1 kills by Kanja's own hand are necessity kills only -- no verdict-then-execution, no killing a surrendering man, judgment of the dead belongs to Onyx's narration afterward. Abad's approval: \"" + APPROVAL + "\""})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
