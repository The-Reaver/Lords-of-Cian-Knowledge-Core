#!/usr/bin/env python3
"""Connective-tissue check for a draft, run before any draft is presented to Abad.

Usage: python3 scripts/connective_tissue_check.py <draft.md> [--max-rules N]

The draft can be a Chronicle, a rule draft, a correction note, or a profile section. It reports:
  1. Every cited rule ID, with its status. A missing, superseded, or withdrawn ID fails the run.
  2. Every proper noun in the draft, with the ledger rules and Chronicle files that already use it.
     This is the list the draft must agree with.
  3. New proper nouns (no ledger or Chronicle hit), each with near-collisions in existing canon
     (same first letter, edit distance of 2 or less).
  4. Every number in the narrative with its context: ages, years, counts, densities, distances.
     Each one has to be checked by hand against the rules listed in step 2.

This script is the mechanical half of the gate. The other half is an independent fresh-context
reviewer who reads the draft beside every rule listed here and tries to break it. See the
"third non-negotiable rule" in CLAUDE.md.
"""
import json, re, sys, glob, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "canon-ledger.json")
CHRON = os.path.join(ROOT, "docs", "lords-of-cian", "chronicles")

STOP = set("""A An And As At Be But By For From He Her Hers His I If In Into Is It Its No Not Of On One Or
She So That The Their Them Then There These They This Those To Two Three Was We What When Where Which
Who Why With You Your Yes After Before Behind Below Above Every Each Once Only Some Most Many Much
Nothing None Nobody Everyone Someone Anything All Any Both Few More Other Another Such Than Too Very
Here Now Later Still Just Even Also Again Back Down Up Out Over Under Within Without Through During
Until Since While Because Although Though Whether How Whose Whom Let Did Do Does Done Had Has Have
My Me Mine Our Ours Us Him Himself Herself Itself Themselves Yourself Myself Ourselves Four Five Six
Seven Eight Nine Ten Eleven Twelve Twenty Thirty Forty Fifty Hundred Thousand First Second Third Last
Next Left Right North South East West Locked Draft Continuity Abad Batch Chronicle Chronicles Strand
Wave Section Rule Rules Archive Book Books Lord Lady Captain Colonel General Warden Sergeant Master
Mr Mrs Sir Old New Great Little High Low Grand Black White Red Grey Gray Green Blue Dark Iron Stone
Pleased Good Stop Sit Walk Count Keep Tell Step Run Ten Eleven""".split())


def load():
    d = json.load(open(LEDGER, encoding="utf-8"))
    return {r["id"]: r for r in d["rules"]}


def narrative(text):
    """Strip the italic header note and the closing continuity-notes block."""
    parts = re.split(r"\n-{3,}\n", text)
    if len(parts) >= 3:
        return "\n".join(parts[1:-1])
    return text


def proper_nouns(text):
    out = defaultdict(int)
    for sent in re.split(r"(?<=[.!?\"'])\s+|\n+", text):
        toks = re.findall(r"[A-Z][a-zA-Z'À-ſ-]+(?:\s+(?:of|the|de|la|del|van|von)?\s*[A-Z][a-zA-Z'À-ſ-]+)*", sent)
        for i, t in enumerate(toks):
            t = re.sub(r"'s$", "", t).strip()
            t = re.sub(r"^The\s+", "", t)
            if re.match(r"(?i)^(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred)\b", t):
                continue
            words = t.split()
            if len(words) == 1 and (t in STOP or len(t) < 3):
                continue
            if sent.strip().startswith(t) and len(words) == 1 and t.lower() in text:
                continue
            out[t] += 1
    return out


def lev(a, b):
    if abs(len(a) - len(b)) > 2:
        return 9
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    path = sys.argv[1]
    maxr = int(sys.argv[sys.argv.index("--max-rules") + 1]) if "--max-rules" in sys.argv else 12
    text = open(path, encoding="utf-8").read()
    rules = load()
    fail = False

    print(f"CONNECTIVE-TISSUE CHECK: {os.path.relpath(path, ROOT)}\n")

    print("1. CITED RULE IDS")
    prefixes = sorted({rid.split("-")[0] for rid in rules}, key=len, reverse=True)
    cited = sorted(set(re.findall(r"\b((?:" + "|".join(prefixes) + r")-\d{2,4})\b", text)))
    for rid in cited:
        r = rules.get(rid)
        if not r:
            print(f"   FAIL  {rid}: not in ledger")
            fail = True
            continue
        st = r.get("status", "")
        flag = "" if st == "locked" else f"  <-- status '{st}'"
        if re.search(r"\b(WITHDRAWN|SUPERSEDED)\b", r["statement"][:200]):
            flag += "  <-- statement marks itself withdrawn/superseded"
        if flag:
            fail = True
        print(f"   {rid}: {r['statement'][:110]}{flag}")
    if not cited:
        print("   (none)")

    corpus = {}
    for f in glob.glob(os.path.join(CHRON, "*.md")):
        if os.path.abspath(f) != os.path.abspath(path):
            corpus[os.path.basename(f)] = open(f, encoding="utf-8").read()
    vocab = set()
    for r in rules.values():
        vocab.update(re.findall(r"\b[A-Z][a-z'À-ſ-]{2,}\b", r["statement"]))

    body = narrative(text)
    nouns = proper_nouns(body)
    print("\n2. PROPER NOUNS -- the draft must agree with every rule listed")
    new = []
    for n in sorted(nouns, key=lambda x: (-nouns[x], x)):
        pat = re.compile(r"\b" + re.escape(n) + r"\b")
        hits = [rid for rid, r in rules.items() if pat.search(r["statement"])]
        files = [fn for fn, t in corpus.items() if pat.search(t)]
        if not hits and not files:
            new.append(n)
            continue
        shown = ", ".join(hits[:maxr]) + (f" (+{len(hits) - maxr} more)" if len(hits) > maxr else "")
        print(f"   {n}  x{nouns[n]}: {len(hits)} rules [{shown}]; {len(files)} Chronicle files")

    print("\n3. NEW PROPER NOUNS -- collision-check each; near-collisions listed")
    for n in new:
        last = n.split()[-1]
        near = sorted({v for v in vocab if v[0] == last[0] and v != last and lev(v.lower(), last.lower()) <= 2})
        print(f"   NEW  {n}" + (f"   near: {', '.join(near[:10])}" if near else "   near: none"))
    if not new:
        print("   (none)")

    print("\n4. NUMBERS IN THE NARRATIVE -- check each against the rules in section 2")
    numwords = r"(?:\d[\d,]*(?:\.\d+)?x?|(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand)(?:[- ](?:one|two|three|four|five|six|seven|eight|nine|hundred|thousand))*)"
    for m in re.finditer(r"[^.\n]*\b" + numwords + r"\b[^.\n]*", body, re.I):
        s = " ".join(m.group(0).split())
        if s:
            print(f"   - {s[:160]}")

    print("\nRESULT:", "FAIL (fix cited IDs before review)" if fail else
          "mechanical pass -- now run the independent reviewer against every rule listed above")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
