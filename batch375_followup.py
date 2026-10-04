"""Batch 375 follow-up: hand fixes to entry files and CLAUDE.md paths that the rename tool cannot judge.

Run after merge_batch375_series_names_account_types.py and after the hand-edited living docs are in place.
Every edit is an exact match with an expected count.
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, "scripts")
from rename_series import path_subs  # noqa: E402

CH = "docs/lords-of-cian/chronicles/"
EDITS = {
    CH + "ezio-exhibit-i-the-frequency-that-never-failed.md": [
        ("(`docs/lords-of-cian/character-chronicle-\ngameplan.md`) -- the fourth Exhibit protagonist to open and clear the gate",
         "(`docs/lords-of-cian/series-gameplan.md`) -- the fourth protagonist to open and clear the gate", 1),
        ("matching the register established in Lauris Record I. Record\nI candidate 1 from the Game Plan",
         "matching the register established in Lauris Record I. Exhibit\nI candidate 1 from the Game Plan", 1),
    ],
    CH + "kanja-chronicle-ii-the-lesson-he-carried-alone.md": [
        ("Daba's own 50-Chronicle launch", "Daba's own 50-entry launch", 2),
    ],
    CH + "kazi-annals-vi-the-names-he-was-teaching-to-read-the-floor.md": [
        ("at the chronicle's close", "at the entry's close", 1),
    ],
    CH + "lauris-record-lxvii-what-a-civilization-takes-its-time-deciding.md": [
        ("a deliberation the\nchronicle does not compress", "a deliberation the\nentry does not compress", 1),
    ],
    CH + "the-notebook-garren-hask-finally-opened.md": [
        ("the Sankofa territory Annals entry's \"crack\" entry", "the Sankofa Annals' \"crack\" entry", 1),
    ],
}
for path, pairs in EDITS.items():
    t = open(path, encoding="utf-8").read()
    for old, new, n in pairs:
        assert t.count(old) == n, (path, old, t.count(old))
        t = t.replace(old, new)
    open(path, "w", encoding="utf-8").write(t)

# Ozmund headers: "Testament track, Ozmund Verehimu's series" reads as "The Testaments, Ozmund Verehimu's series".
n = 0
for f in os.listdir(CH):
    if f.startswith("ozmund-testament-"):
        p = CH + f
        t = open(p, encoding="utf-8").read()
        t2 = re.sub(r"Testament(\s+)track,(\s+)Ozmund", r"The\1Testaments,\2Ozmund", t)
        if t2 != t:
            n += 1
            open(p, "w", encoding="utf-8").write(t2)
print("ozmund headers tidied:", n)


# Eleventh-review residue: count nouns, compounds, a quoted correction record, corpus scope.
TERR = (r"(?:Xaragua|Areíto|Areito|Yara|Guanín|Guanin|Borikén|Boriken|Ide|Kwan|Umoja|Jibaro|Uhuru|Sankofa|"
        r"Aztlán|Aztlan|Atunbi|Ijoko|Orin|Kazi|Taifa|Hekalu|Nyansa|Kiti)")
SING = re.compile(r"\b((?:[Aa]|any|every|(?:the\s+)?\*?(?:[Ff]irst|[Ss]econd|[Tt]hird|[Ff]ourth|[Ff]ifth|[Ss]ixth)\*?)"
                  r"(?:\s+(?:other|prior|future))?\s+" + TERR + r"\s+Annals)\b(?!\s+entr|\s+[IVXLC]+\b)")
PLUR = re.compile(r"\b(the\s+four\s+" + TERR + r"\s+Annals)\b(?!\s+entr)")
FIXES = [
    (re.compile(r"\b(\d+)-wave\b"), r"\1-entry wave"),
    (re.compile(r"\bfirst-Annals entry level\b"), "first-entry level"),
    (re.compile(r"\bfive-Annals entry (run|arc)\b"), r"five-entry \1"),
    (re.compile(r"\bterritory-Annals entry (coverage|convention|file-naming)\b"), r"territory-Annals \1"),
    (re.compile(r"full(\s+)ledger(\s+)and(\s+)Collection(\s+)corpus"), r"full\1ledger\2and\3entry\4corpus"),
    (re.compile(r"across(\s+)other(\s+)Annals(\s+)of\b"), r"across\1other\2Annals entries\3of"),
    (re.compile(r"a Annals entry-numbering(\s+)writers'-room leak \(\"three Annals before\""),
     r"an entry-numbering\1writers'-room leak (the old \"three Chronicles before\""),
]


def residue(t):
    t = SING.sub(r"\1 entry", t)
    t = PLUR.sub(r"\1 entries", t)
    for rx, rep in FIXES:
        t = rx.sub(rep, t)
    return t


SCOPE = [CH + f for f in os.listdir(CH)
         if re.match(r"(lauris-record|daba-roll|ozmund-testament|ezio-exhibit|anirak-collection|[a-z]+-annals)-", f)]
SCOPE += [CH + f for f in os.listdir(CH) if f.startswith(("the-", "what-")) and "Annals" in open(CH + f, encoding="utf-8").read()]
SCOPE += ["docs/lords-of-cian/phase2-homage-era-development.md"]
nf = 0
for p in sorted(set(SCOPE)):
    t = open(p, encoding="utf-8").read()
    t2 = residue(t)
    if t2 != t:
        nf += 1
        open(p, "w", encoding="utf-8").write(t2)
import json  # noqa: E402
d = json.load(open("canon-ledger.json", encoding="utf-8"))
nr = 0
TRACK_CATS = {"lauris-records", "daba-rolls", "ozmund-testaments", "ezio-exhibits", "anirak-collections",
              "phase2-territory-annals"}
for r in d["rules"]:
    if r.get("category") in TRACK_CATS:
        cut = r["statement"].find("Abad's approval")
        head, tail = (r["statement"], "") if cut < 0 else (r["statement"][:cut], r["statement"][cut:])
        new = residue(head) + tail
        if new != r["statement"]:
            nr += 1
            r["statement"] = new
json.dump(d, open("canon-ledger.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open("canon-ledger.json", "a", encoding="utf-8").write("\n")
print("residue fixed: files", nf, "| rules", nr)

# CLAUDE.md batch history: file paths only (VB-066).
out = subprocess.run(["git", "diff", "--cached", "--name-status", "-M"], capture_output=True, text=True, check=True).stdout
renames = {}
for line in out.splitlines():
    f = line.split("\t")
    if f[0].startswith("R") and f[1].startswith(CH):
        renames[os.path.basename(f[1])] = os.path.basename(f[2])
t = open("CLAUDE.md", encoding="utf-8").read()
t2 = path_subs(t, renames)
open("CLAUDE.md", "w", encoding="utf-8").write(t2)
left = re.findall(r"character-chronicle-gameplan|ezio-chronicle-ii`", t2)
print("renames:", len(renames), "| CLAUDE.md changed:", t != t2, "| stale paths left:", len(left))
