"""Batch 377: VB-004 amended (comic registers in told accounts) and LEX-001 to LEX-025 locked (in-world
common vocabulary and venue names, the approved picks of the account-craft naming table). Propagation
to the locked account craft standard and CLAUDE.md is carried in the same batch.
Usage: python3 merge_batch377_vb004_amendment_lex_names.py <draft.md> "<approval quote>"
"""
import json
import re
import sys
from collections import Counter

LEDGER = "canon-ledger.json"
DRAFT, APPROVAL = sys.argv[1], sys.argv[2]
SOURCE = "Original invention, chat-drafted 2026-10-04, no source document"
STD = "docs/lords-of-cian/voice/account-craft-standard.md"
TABLE = "docs/lords-of-cian/drafts/2026-10-04-account-craft-names-and-rule.md"

def clean(t):
    return re.sub(r"\s+", " ", t.replace("`", "").replace("**", "")).strip()

text = open(DRAFT, encoding="utf-8").read()
amend = clean(re.search(r'\n"(Amended Batch 377\..+?)"\n', text, re.S).group(1))
lex = {m.group(1): clean(m.group(2)) for m in
       re.finditer(r"\*\*(LEX-\d{3})\*\*\. (.+?)(?=\n\n)", text, re.S)}
assert sorted(lex) == [f"LEX-{i:03d}" for i in range(1, 26)], sorted(lex)
CAT = {**{f"LEX-{i:03d}": "lexicon-mainline" for i in range(1, 15)},
       **{f"LEX-{i:03d}": "lexicon-homage-world" for i in range(15, 25)},
       "LEX-025": "lexicon-ashkeel"}

d = json.load(open(LEDGER, encoding="utf-8"))
byid = {r["id"]: r for r in d["rules"]}
assert not set(lex) & set(byid)
assert "Amended Batch 377" not in byid["VB-004"]["statement"]
byid["VB-004"]["statement"] += " " + amend
for k in sorted(lex):
    d["rules"].append({"id": k, "category": CAT[k], "statement": lex[k], "status": "locked",
                       "source": SOURCE})
d["batches_completed"].append({
    "batch": 377, "source": SOURCE, "rules_affected": 26,
    "note": ("VB-004 amended: in a told account (a Comrade Account, Adversary Account, or Hearsay entry, or "
             "a storytelling scene), characters' talk may use the comic registers Abad ruled on at VB-068's "
             "lock; narration, Dossier text, designated narrators, and track voice rulings stay as before; "
             "child-safety line added. LEX-001 to LEX-025 lock the approved vocabulary picks (a new LEX "
             "prefix for in-world common vocabulary and venue names); N10b and the RULE NEEDED keys held. "
             "The account craft standard and CLAUDE.md updated in the same batch. "
             f"Abad's approval, verbatim: \"{APPROVAL}\"."),
})
d["ledger_version"] = "37.9"
d["last_updated"] = "2026-10-04"
json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(LEDGER, "a", encoding="utf-8").write("\n")

# --- propagation: the standard ---
s = open(STD, encoding="utf-8").read()
NAMES = {
    "N1": "tapstead (`LEX-001`)", "N2a": "the Slack Hawser (`LEX-002`)",
    "N2b": "the Tallow Lamp (`LEX-003`)", "N2c": "the Last Bell (`LEX-004`)",
    "N3": "the Call Yard (`LEX-005`)", "N4": "the Trough (`LEX-006`)", "N5": "the Sweat (`LEX-007`)",
    "N8": "a hewer (`LEX-008`)", "N9": "a bell (`LEX-009`)", "N10a": "dice-house (`LEX-010`)",
    "N11": "the lykewake (`LEX-011`)", "N14": "the pump, its regulars the pump-lads (`LEX-013`)",
    "N15": "a whistler (`LEX-014`)", "H1": "the Shekere (`LEX-015`)", "H2": "kibanda (`LEX-016`)",
    "H3": "kinyozi (`LEX-017`)", "H4": "egbe (`LEX-018`)", "H8": "oju (`LEX-019`)",
    "H9": "pembe (`LEX-020`)", "H10": "kete (`LEX-021`)", "H11": "ulli (`LEX-022`)",
    "H12": "baraza (`LEX-023`)", "H13": "ayie (`LEX-024`)", "A1": "brazier-house (`LEX-025`)",
}
REPL = [
    ("The form of that notice is **[NAME NEEDED: N12]**.",
     "Common speech calls a posted Trust notice the posted bill (`LEX-012`); no rule sets its form."),
    ("- The Trust's public-notice form: **[NAME NEEDED: N12]**.",
     "- Common speech for a posted Trust notice: the posted bill (`LEX-012`); no rule sets its form."),
    ("- **`VB-068`** (proposed) binds", "- **`VB-068`** binds"),
    ("humor limited to irony and understatement (`VB-004`), no",
     "humor in narration limited to irony and understatement, with characters' talk in a told account\n"
     "  as broad as `VB-004` as amended (Batch 377) allows, no"),
    ("""  Each is written through deadpan irony and understatement only (`VB-004`): the insult arrives flat
  and short, and the toast leaves its biggest claim unsaid.""",
     """  In characters' talk in a told account, each may run as broad as `VB-004` as amended (Batch 377)
  allows; narration stays at irony and understatement."""),
    ("""  larger claim told in a flatter voice, through irony and understatement only (`VB-004`).""",
     """  larger claim, as broad as `VB-004` as amended (Batch 377) allows."""),
    ("""  disclaimer before a polished telling, and a dry, understated line left a beat to land
  (`VB-004`).""",
     """  disclaimer before a polished telling, and a line left a beat to land (`VB-004` as amended,
  Batch 377)."""),
    ("""- Comic stories grow, each telling a larger claim in a drier voice: irony and understatement only
  (`VB-004`).""",
     """- Comic stories grow, each telling a larger claim (`VB-004` as amended, Batch 377)."""),
    ("- *Open:* an insult that means welcome, said flat and understated (`VB-004`).",
     "- *Open:* an insult that means welcome (`VB-004` as amended, Batch 377)."),
    ("""- Seniority and skill. The senior hand anchors the ritual joke, a dry line of irony or
  understatement (`VB-004`).""",
     """- Seniority and skill. The senior hand anchors the ritual joke (`VB-004` as amended, Batch
  377)."""),
    ("- *Open:* ritual teasing, deadpan (`VB-004`).",
     "- *Open:* ritual teasing (`VB-004` as amended, Batch 377)."),
    ("""It is a recognized genre of tall telling, told deadpan: the
  teller states the impossible in the flattest voice on the watch (`VB-004`).""",
     """It is a recognized genre of tall telling, often told deadpan:
  the teller states the impossible in the flattest voice on the watch (`VB-004` as amended, Batch
  377)."""),
]
for a, b in REPL:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
# section 7 item 14 humor bullet
i = s.index("    - Humor is irony and understatement only (`VB-004`). Every comic register")
j = s.index("    - No balanced antithesis", i)
s = s[:i] + ("    - Narration's humor is irony and understatement only (`VB-004`). Characters' talk in a told\n"
             "      account may use the comic registers `VB-004` as amended (Batch 377) lists, R0.4, R15,\n"
             "      R18, M1, M2's funny boast, M3's parting jab, M4, M7, M9, and the comic stories of M6\n"
             "      and M11, and none broader. Designated narrators and Dossier text stay at irony and\n"
             "      understatement.\n") + s[j:]
# R0.4 ruling note
a = """  - Abad ruled at `VB-068`'s lock that these registers may run broader in told accounts. The
    broader registers apply once the `VB-004` amendment that sets them out locks. Until then,
    `VB-004` holds.
"""
assert s.count(a) == 1
s = s.replace(a, "")
for k, v in NAMES.items():
    pat = f"**[NAME NEEDED: {k}]**"
    assert pat in s, k
    s = s.replace(pat, v)
assert "NAME NEEDED: N12" not in s and "until the `VB-004` amendment" not in s
open(STD, "w", encoding="utf-8").write(s)

# --- propagation: the naming table header ---
t = open(TABLE, encoding="utf-8").read()
a = "Part (b)'s approved picks lock as their own rules; nothing in part (b) is usable before then."
assert t.count(a) == 1
t = t.replace(a, "Part (b)'s approved picks locked as `LEX-001` to `LEX-025`, Batch 377; N10b and the "
                 "[RULE NEEDED] keys (N6, N7, N13, N16, H5, H6, H7) are held.")
open(TABLE, "w", encoding="utf-8").write(t)

# --- propagation: CLAUDE.md prefix list ---
c = open("CLAUDE.md", encoding="utf-8").read()
a = "`WGD`, `ASH`, `PH2`. A new institution"
assert c.count(a) == 1
c = c.replace(a, "`WGD`, `ASH`, `PH2`, `LEX`. A new institution")
a = "rather than folding into `MCD`/`CC`/etc.)."
assert c.count(a) == 1
c = c.replace(a, a[:-2] + "; `LEX-` was claimed 2026-10-04, Batch 377, for in-world common vocabulary and "
              "venue names, each locked as its own rule per `VB-068`).")
open("CLAUDE.md", "w", encoding="utf-8").write(c)

d = json.load(open(LEDGER, encoding="utf-8"))
dup = [k for k, v in Counter(r["id"] for r in d["rules"]).items() if v > 1]
print("duplicates:", dup, "| total rules:", len(d["rules"]), "| version:", d["ledger_version"])
