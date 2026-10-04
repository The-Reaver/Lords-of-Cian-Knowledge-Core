#!/usr/bin/env python3
"""VB-066 series rename: "Chronicle" stays Kanja's; every other series takes its own name.

Usage: python3 scripts/rename_series.py [--apply] [--tracks ezio,anirak,...]

Dry run (default) prints what would change and every bare-"Chronicle" replacement with context,
so a reviewer can check that no Kanja reference was renamed. --apply writes the changes and
renames the files (git mv). Historical batch notes keep their wording; only file paths in them
are updated so links keep resolving. Verbatim approval quotes are never touched.
"""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = "docs/lords-of-cian/chronicles/"
LEDGER = "canon-ledger.json"

TERR = {  # territory -> name variants
    "xaragua": ["Xaragua"], "areito": ["Areíto", "Areito"], "yara": ["Yara"],
    "guanin": ["Guanín", "Guanin"], "boriken": ["Borikén", "Boriken"], "ide": ["Ide"],
    "kwan": ["Kwan"], "umoja": ["Umoja"], "jibaro": ["Jibaro", "Jíbaro"], "uhuru": ["Uhuru"],
    "sankofa": ["Sankofa"], "aztlan": ["Aztlán", "Aztlan"], "atunbi": ["Atunbi"],
    "ijoko": ["Ijoko"], "orin": ["Orin"], "kazi": ["Kazi"], "taifa": ["Taifa"],
    "hekalu": ["Hekalu"], "nyansa": ["Nyansa"], "kiti": ["Kiti"],
}
TRACKS = {
    "ezio": dict(names=["Ezio Valcari", "Ezio"], sing="Exhibit", plur="Exhibits",
                 cat=("ezio-character-chronicle", "ezio-exhibits"), fp=("ezio-chronicle-", "ezio-exhibit-")),
    "anirak": dict(names=["Anirak"], sing="Collection", plur="Collections",
                   cat=("anirak-character-chronicle", "anirak-collections"), fp=("anirak-chronicle-", "anirak-collection-")),
    "daba": dict(names=["Daba"], sing="Roll", plur="Rolls",
                 cat=("daba-character-chronicle", "daba-rolls"), fp=("daba-chronicle-", "daba-roll-")),
    "lauris": dict(names=["Lauris Letitia", "Lauris"], sing="Record", plur="Records",
                   cat=("lauris-character-chronicle", "lauris-records"), fp=("lauris-chronicle-", "lauris-record-")),
    "ozmund": dict(names=["Ozmund Verehimu", "Ozmund"], sing="Testament", plur="Testaments",
                   cat=("ozmund-character-chronicle", "ozmund-testaments"), fp=("ozmund-chronicle-", "ozmund-testament-")),
}
for t, v in TERR.items():
    TRACKS[t] = dict(names=v, sing="Annals", plur="Annals",
                     cat=("phase2-territory-chronicle", "phase2-territory-annals"),
                     fp=(t + "-chronicle-", t + "-annals-"), territory=True)

ROMAN = r"[IVXLC]+\b"
KANJA_Q = r"(?:Alias|Kanja|manuscript|Kanja-version|Onyx|Onyx-narrated|Onyx-track|Mask|Victories)"


def file_track_map(rules):
    """Chronicle file basename -> track key."""
    m = {}
    for f in os.listdir(CH):
        for k, tr in TRACKS.items():
            if f.startswith(tr["fp"][0]):
                m[f] = k
    cat2 = {}
    for k, tr in TRACKS.items():
        cat2.setdefault(tr["cat"][0], []).append(k)
    for r in rules:
        ks = cat2.get(r.get("category"))
        if not ks:
            continue
        fs = [f for f in set(re.findall(r"([a-z0-9][a-z0-9-]+\.md)", r["statement"] + " " + r.get("source", "")))
              if os.path.exists(CH + f)]
        for f in fs:
            if f in m:
                continue
            if len(ks) == 1:
                m[f] = ks[0]
            else:
                m[f] = rule_territory(r, f)
    return m


def rule_territory(r, f=None):
    if f:
        for k in TERR:
            if f.startswith(k + "-"):
                return k
    txt = r["statement"]
    best = None
    for k, v in TERR.items():
        for n in v:
            mm = re.search(r"\b" + re.escape(n) + r"\b", txt)
            if mm and (best is None or mm.start() < best[0]):
                best = (mm.start(), k)
    return best[1] if best else None


def named_subs(text, keys=None):
    """Replace explicitly named references ("Lauris Chronicle IX", "Xaragua Chronicles"). Safe anywhere."""
    for k, tr in TRACKS.items():
        if keys and k not in keys:
            continue
        for n in sorted(tr["names"], key=len, reverse=True):
            text = re.sub(r"\b(" + re.escape(n) + r"(?:'s)?(?: own)?(?: launch)?) (?:Character )?Chronicle wave\b",
                          lambda mm: mm.group(1) + " wave", text)
            # "Lauris Letitia's own Character Chronicle series" / "Anirak's Character Chronicle series"
            text = re.sub(r"\b(" + re.escape(n) + r"(?:'s)?(?: own)?) (?:Character |territory )?Chronicle series\b",
                          lambda mm: mm.group(1) + " " + tr["plur"], text)
            text = re.sub(r"\b(" + re.escape(n) + r") (?:Character |territory )?Chronicles\b",
                          lambda mm: mm.group(1) + " " + tr["plur"], text)
            text = re.sub(r"\b(" + re.escape(n) + r") (?:Character |territory )?Chronicle\b",
                          lambda mm: mm.group(1) + " " + tr["sing"], text)
            text = re.sub(r"\b(" + re.escape(n) + r"'s(?: own)?) (?:Character |territory )?Chronicles\b",
                          lambda mm: mm.group(1) + " " + tr["plur"], text)
            text = re.sub(r"\b(" + re.escape(n) + r"'s(?: own)?) (?:Character |territory )?Chronicle\b",
                          lambda mm: mm.group(1) + " " + tr["sing"], text)
    return text


def generic_subs(text):
    text = text.replace("Character Chronicle Launch Protocol", "Series Launch Protocol")
    text = text.replace("Character Chronicle Gameplan", "Series Gameplan")
    text = text.replace("character-chronicle-gameplan.md", "series-gameplan.md")
    text = re.sub(r"\bNot a territory Chronicle\b", "Not a territory Annals entry", text)
    text = re.sub(r"\b(homage-era |Phase 2 homage-era )?[Tt]erritory Chronicles\b",
                  lambda m: (m.group(1) or "") + "territory Annals", text)
    text = re.sub(r"\b(homage-era )?[Tt]erritory Chronicle\b",
                  lambda m: (m.group(1) or "") + "territory Annals entry", text)
    return text


NAME_RE = [(k, re.compile(r"\b(?:" + "|".join(re.escape(n) for n in tr["names"]) + r")\b"))
           for k, tr in TRACKS.items()]


def nearest_track(pre, own):
    """The renamed track named closest before a bare reference; own track if none."""
    best = None
    for k, rx in NAME_RE:
        for mm in rx.finditer(pre):
            if best is None or mm.start() > best[0]:
                best = (mm.start(), k)
    return best[1] if best else own


APPROVAL_Q = re.compile(r"""(?:approval|direction|approved|asked)[^"'“]{0,60}?(?:"[^"]{0,600}"|“[^”]{0,600}”|'[^']{0,600}?'(?=[.,;)\s]|$))""", re.I)


def bare_subs(text, key, log, where):
    masks = []

    def mask(mm):
        masks.append(mm.group(0))
        return "\x00%d\x00" % (len(masks) - 1)
    text = APPROVAL_Q.sub(mask, text)
    text = _bare_subs(text, key, log, where)
    return re.sub(r"\x00(\d+)\x00", lambda mm: masks[int(mm.group(1))], text)


def _bare_subs(text, key, log, where):
    """Inside one track's own scope: bare "Chronicle N"/"Chronicle series"/"Chronicle wave"."""
    tr = TRACKS[key]
    s, p = tr["sing"], tr["plur"]

    def rep(mm):
        pre = text[max(0, mm.start() - 40):mm.start()]
        post = text[mm.end():mm.end() + 12]
        if re.search(KANJA_Q + r"\s*$", pre) or re.match(r"\s*(?:I-VIII|I through VIII)\b", mm.group(0)[-1:] + post) \
                or re.search(r"Chronicles?\s+I-VIII|Chronicles?\s+I through VIII", mm.group(0) + post):
            return mm.group(0)
        kk = nearest_track(text[max(0, mm.start() - 160):mm.start()], key)
        s2, p2 = TRACKS[kk]["sing"], TRACKS[kk]["plur"]
        out = (p2 if mm.group(1) else s2) + mm.group(2)
        log.append((where, pre[-40:].replace("\n", " "), mm.group(0), out))
        return out

    text = re.sub(r"\b(?:Character )?Chronicle series\b", p, text)
    text = re.sub(r"\b(?:Character )?Chronicle wave\b", "wave", text)
    text = re.sub(r"\bChronicle(s)?(\s+" + ROMAN + r")", rep, text)
    text = re.sub(r"\b(?:Character )?Chronicle(s)?(\b(?! [IVXLC]))", rep, text)
    return text


def path_subs(text, renames):
    for old, new in renames.items():
        text = text.replace(old, new)
    return text


def main():
    apply = "--apply" in sys.argv
    only = None
    if "--tracks" in sys.argv:
        only = set(sys.argv[sys.argv.index("--tracks") + 1].split(","))
        if "territories" in only:
            only |= set(TERR)
    os.chdir(ROOT)
    d = json.load(open(LEDGER, encoding="utf-8"))
    fmap = file_track_map(d["rules"])
    keys = set(TRACKS) if only is None else only
    renames = {}
    for f, k in fmap.items():
        if k in keys and f.startswith(TRACKS[k]["fp"][0]):
            renames[f] = TRACKS[k]["fp"][1] + f[len(TRACKS[k]["fp"][0]):]
    log, changed = [], []

    # 1. chronicle files
    for f in sorted(os.listdir(CH)):
        if not f.endswith(".md"):
            continue
        src = open(CH + f, encoding="utf-8").read()
        t = generic_subs(src)
        t = named_subs(t, keys)
        if fmap.get(f) in keys:
            t = bare_subs(t, fmap[f], log, f)
        t = path_subs(t, renames)
        if t != src:
            changed.append(CH + f)
            if apply:
                open(CH + f, "w", encoding="utf-8").write(t)

    # 2. ledger: statements, sources, categories (batch notes: paths only)
    cat_map = {tr["cat"][0]: tr["cat"][1] for k, tr in TRACKS.items() if k in keys}
    nrule = 0
    for r in d["rules"]:
        before = (r["statement"], r.get("source", ""), r.get("category"))
        for fld in ("statement", "source"):
            if fld not in r or not isinstance(r[fld], str):
                continue
            v = generic_subs(r[fld])
            v = named_subs(v, keys)
            cat = r.get("category")
            k = None
            for kk, tr in TRACKS.items():
                if kk in keys and tr["cat"][0] == cat:
                    k = kk if not tr.get("territory") else rule_territory(r)
                    break
            if k and k in keys:
                v = bare_subs(v, k, log, r["id"])
            r[fld] = path_subs(v, renames)
        if r.get("category") in cat_map:
            r["category"] = cat_map[r["category"]]
        if before != (r["statement"], r.get("source", ""), r.get("category")):
            nrule += 1
    for b in d["batches_completed"]:
        for fld in ("source", "note"):
            if isinstance(b.get(fld), str):
                b[fld] = path_subs(b[fld], renames)
    if apply:
        json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        open(LEDGER, "a", encoding="utf-8").write("\n")
        for old, new in renames.items():
            subprocess.run(["git", "mv", CH + old, CH + new], check=True)

    # 3. docs (profiles, tracker, gameplan, roadmap) and CLAUDE.md: named, generic, paths
    docs = [os.path.join("docs/lords-of-cian/character-profiles", f)
            for f in os.listdir("docs/lords-of-cian/character-profiles")]
    docs += [os.path.join("docs/lords-of-cian", f) for f in os.listdir("docs/lords-of-cian") if f.endswith(".md")]
    docs += ["CLAUDE.md"]
    for p in docs:
        src = open(p, encoding="utf-8").read()
        t = path_subs(named_subs(generic_subs(src), keys), renames)
        if t != src:
            changed.append(p)
            if apply:
                open(p, "w", encoding="utf-8").write(t)

    print(f"files changed: {len(changed)} | rules changed: {nrule} | renames: {len(renames)} | bare subs: {len(log)}")
    out = os.environ.get("RENAME_LOG")
    if out:
        with open(out, "w", encoding="utf-8") as fh:
            for row in log:
                fh.write(" | ".join(row) + "\n")


if __name__ == "__main__":
    main()
