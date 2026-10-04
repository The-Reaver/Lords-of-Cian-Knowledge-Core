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
amend = clean(re.search(r'\n"(Amended Batch 377, 2026-10-04:.+?)"\n', text, re.S).group(1))
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
byid["VB-004"]["statement"] += (" " + amend + f" Abad's ruling at VB-068's lock: 'lock it, approve the picks, "
                                 f"confirm all three'; approval of this text: '{APPROVAL}'.")
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
             "LEX-025 fixes one hall feature (a stone basin over a sealed heat-gallery, no open flame). "
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
    "N4": "the Trough (`LEX-006`)", "N5": "the Sweat (`LEX-007`)",
    "N8": "a hewer (`LEX-008`)", "N9": "a bell (`LEX-009`)", "N10a": "dice-house (`LEX-010`)",
    "N11": "the lykewake (`LEX-011`)", "N14": "the pump and the pump-lads (`LEX-013`)",
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
    ("""phatic talk, the 50% dialogue cut, humor limited to irony and understatement (`VB-004`), no
  balanced antithesis, none of the banned words or borrowed terms, and the Density Spike never
  named.""",
     """phatic talk; the 50% dialogue cut; dialogue humor limited to irony and understatement outside a
  told account (`VB-004`), and in one as broad as `VB-004` as amended (Batch 377) allows; no
  balanced antithesis; none of the banned words or borrowed terms; and the Density Spike never
  named."""),
    ("""  Each is written through deadpan irony and understatement only (`VB-004`): the insult arrives flat
  and short, and the toast leaves its biggest claim unsaid.""",
     """  The toast is a long rhymed boasting narrative. In characters' talk in a told account, each may
  run as broad as `VB-004` as amended (Batch 377) allows; otherwise each is written through irony
  and understatement only (`VB-004`)."""),
    ("- A dock hiring place, if one is drafted: **[NAME NEEDED: N3]**.",
     "- The dock hiring yard: the Call Yard (`LEX-005`)."),
    ("""Its exaggeration or edge
drift on any matter of fact locks as fact unless traced (`VB-067`, §4.1), so a Comrade teller there
brags in judgment, feeling, and dry understatement.""",
     """Its exaggeration or edge
drift on any matter of fact locks as fact unless traced (`VB-067`, §4.1), so a Comrade teller there
inflates a matter of fact only within `VB-067`'s Comrade bound (on a matter where a locked rule or
reliable narration records the teller as mistaken or misled, or in secondhand relay, and traced),
whatever the register (`VB-004` as amended, Batch 377)."""),
    ("The everyday hall is\n  **[NAME NEEDED: A1]**.", "The everyday hall is a\n  brazier-house (`LEX-025`)."),
    ("""  larger claim told in a flatter voice, through irony and understatement only (`VB-004`).""",
     """  larger claim (in a told account, as broad as `VB-004` as amended, Batch 377, allows; otherwise
  irony and understatement, `VB-004`)."""),
    ("""  disclaimer before a polished telling, and a dry, understated line left a beat to land
  (`VB-004`).""",
     """  disclaimer before a polished telling, and a line left a beat to land (in a told account, as
  broad as `VB-004` as amended, Batch 377, allows; otherwise irony and understatement, `VB-004`)."""),
    ("""- Comic stories grow, each telling a larger claim in a drier voice: irony and understatement only
  (`VB-004`).""",
     """- Comic stories grow, each telling a larger claim (in a told account, as broad as `VB-004` as
  amended, Batch 377, allows; otherwise irony and understatement, `VB-004`)."""),
    ("- *Open:* an insult that means welcome, said flat and understated (`VB-004`).",
     "- *Open:* an insult that means welcome (in a told account, as broad as `VB-004` as amended,\n"
     "  Batch 377, allows; otherwise irony and understatement, `VB-004`)."),
    ("""- Seniority and skill. The senior hand anchors the ritual joke, a dry line of irony or
  understatement (`VB-004`).""",
     """- Seniority and skill. The senior hand anchors the ritual joke (in a told account, as broad as
  `VB-004` as amended, Batch 377, allows; otherwise irony and understatement, `VB-004`)."""),
    ("""- Gaps:
  - corner and crew **[NAME NEEDED: H9]**
  - lookout **[NAME NEEDED: H8]**
  - street game **[NAME NEEDED: H10]**""",
     """- Street words:
  - corner and crew: pembe (`LEX-020`)
  - lookout: oju (`LEX-019`)
  - street game: kete (`LEX-021`)"""),
    ("""    and non-explicit, and no character under thirty appears in or near any Ashkeel setting (M13).""",
     """    and non-explicit, and no character under thirty appears in or near any Ashkeel setting (M13).
    In a told account, every comic register stays non-explicit; sexual talk is between adults only,
    with no minor present, addressed, or referenced, and no minor is the subject of a sexual insult,
    boast, or story (`VB-004` as amended, Batch 377)."""),
    ("- *Open:* ritual teasing, deadpan (`VB-004`).",
     "- *Open:* ritual teasing (in a told account, as broad as `VB-004` as amended, Batch 377, allows;\n"
     "  otherwise irony and understatement, `VB-004`)."),
    ("""It is a recognized genre of tall telling, told deadpan: the
  teller states the impossible in the flattest voice on the watch (`VB-004`).""",
     """It is a recognized genre of tall telling, often told deadpan:
  the teller states the impossible in the flattest voice on the watch (in a told account, as broad
  as `VB-004` as amended, Batch 377, allows; otherwise irony and understatement, `VB-004`)."""),
]
for a, b in REPL:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
# section 7 item 14 humor bullet
i = s.index("    - Humor is irony and understatement only (`VB-004`). Every comic register")
j = s.index("    - No balanced antithesis", i)
s = s[:i] + "    - Outside a told account, dialogue humor is irony and understatement only (`VB-004`), whatever\n      room a scene is set in. In a told account, characters' talk may use only the comic registers\n      `VB-004` as amended (Batch 377) lists: in the homage World, ritual insult, signifying, call\n      and response, and the toast (a long rhymed boasting narrative), and on Cian, dock, forge, and\n      Maw idiom (R0.4); R15; R18; every comic register of M1, M4, and M7; M2's funny boast; M3's\n      parting jab; M9's tall telling; and the comic stories of M6 and M11. Any other register, M8's\n      comic arc and its closing drink toast and M10's tall tales among them, stays at irony and\n      understatement, whatever its idiom or World. For this purpose the teller's voice in a Comrade\n      Account, an Adversary Account, or a Hearsay entry counts as characters' talk, its reliability\n      as `VB-067` sets it. In a Comrade Account, a register that inflates a matter of fact is used\n      only within `VB-067`'s Comrade bound, traced (§4.1, item 7). The 50% rule, the phatic bar,\n      fact over emotion, and every hard constraint still apply. The amendment changes no narration\n      and no Dossier text, speech quoted in a Dossier included. Each designated narrator, as\n      narrator, as teller, and as a speaking character, keeps their own sheet (`VB-021` to\n      `VB-025`). Every track voice ruling and every character's own voice (`VB-030`) still governs\n      that character's diction, and these registers run inside it. Onyx stays under `VB-063` alone.\n      Every such register stays non-explicit (item 17).\n" + s[j:]
# R0.4 ruling note
a = """  - Abad ruled at `VB-068`'s lock that these registers may run broader in told accounts. The
    broader registers apply once the `VB-004` amendment that sets them out locks. Until then,
    `VB-004` holds.
"""
assert s.count(a) == 1
s = s.replace(a, "")
for k, v in NAMES.items():
    pat = f"**[NAME NEEDED: {k}]**"
    s = s.replace(pat, v)
for k in list(NAMES) + ["N12"]:
    assert f"[NAME NEEDED: {k}]" not in s, k
assert "NAME NEEDED: N12" not in s and "until the `VB-004` amendment" not in s
open(STD, "w", encoding="utf-8").write(s)

# --- propagation: Lauris's profile ---
LP = "docs/lords-of-cian/character-profiles/lauris-letitia.md"
lp = open(LP, encoding="utf-8").read()
a = "    (the 50% rule, no phatic lines, understatement for humor)."
assert lp.count(a) == 1, "lauris pillar 3 line"
lp = lp.replace(a, "    (the 50% rule, no phatic lines; humor through irony and understatement outside a told account,\n"
                   "    and in one as broad as `VB-004` as amended, Batch 377, allows; Fermand keeps his own sheet).")
open(LP, "w", encoding="utf-8").write(lp)

# --- propagation: the naming table header ---
t = open(TABLE, encoding="utf-8").read()
a = "Part (b)'s approved picks lock as their own rules; nothing in part (b) is usable before then."
assert t.count(a) == 1
t = t.replace(a, "Part (b)'s approved picks locked as `LEX-001` to `LEX-025`, Batch 377; N10b and the "
                 "[RULE NEEDED] keys (N6, N7, N13, N16, H5, H6, H7) are held. Part (c), item 8 is resolved by "
                 "`VB-004` as amended, Batch 377.")
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
a = "Ledger at `ledger_version` 37.8, 2,696 rules, 376 batches.\n"
assert c.count(a) == 1
c = c.replace(a, a + f"""
**Batch 377: comic registers in told accounts (`VB-004` amended) and the account-craft vocabulary
(`LEX-001` to `LEX-025`).** Abad: "{APPROVAL}"
- **The amendment.** In a told account (a Comrade Account, Adversary Account, or Hearsay entry, or a
  storytelling scene), characters' talk may use the comic registers Abad ruled on at `VB-068`'s lock.
  Narration and Dossier text are unchanged. Each designated narrator keeps their own sheet, and every
  track voice ruling still governs its characters' diction. Onyx stays under `VB-063` alone. A Comrade
  teller inflates fact only within `VB-067`'s bound. Child-safety and Ashkeel lines are written in.
- **The names.** `LEX-` is a new prefix for in-world common vocabulary and venue names, one rule per
  name as `VB-068` requires: 14 mainline, 10 homage-World, 1 Ashkeel. LEX-025 fixes one hall feature,
  a stone basin over a sealed heat-gallery with no open flame. N10b and the [RULE NEEDED] keys are
  held.
- **Propagation.** The standard's name markers and deadpan-only lines were updated in the same batch.
  Sync owed: the mirrored Voice Bible's Pillar 3 humor line (`docs/lords-of-cian/voice/voice-bible-definitive.md`)
  is a read-only copy and now differs from `VB-004` as amended; the ledger rule controls, and the
  Drive source document is Abad's to update.
Ledger at `ledger_version` 37.9, 2,721 rules, 377 batches.
""")
open("CLAUDE.md", "w", encoding="utf-8").write(c)

d = json.load(open(LEDGER, encoding="utf-8"))
dup = [k for k, v in Counter(r["id"] for r in d["rules"]).items() if v > 1]
print("duplicates:", dup, "| total rules:", len(d["rules"]), "| version:", d["ledger_version"])
