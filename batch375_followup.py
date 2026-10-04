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
