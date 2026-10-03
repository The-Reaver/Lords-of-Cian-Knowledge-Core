"""Gated Onyx voice check (VB-063). Phase 4 (Long Mask) thresholds; run on any Onyx-narrated draft before
it is presented. Usage: python3 scripts/onyx_voice_check.py <chronicle.md> ... Every line must read PASS.
Short Phase 1-3 codas are judged by cadence lines only (Captain/verdict counts scale with length)."""
import re,sys
def body(t):
    p=t.split('\n---\n')
    return p[1] if len(p)>=3 else t
for f in sys.argv[1:]:
    raw=body(open(f,encoding='utf-8').read())
    t=re.sub(r'[*_#`]','',raw)
    narr=re.sub(r'"[^"]*"','',t)  # narration without dialogue
    sents=[s for s in re.split(r'(?<=[.!?])\s+|\n\n+',t) if s.split()]
    w=t.split(); n=len(w)
    avg=n/len(sents)
    frag=100*sum(1 for s in sents if len(s.split())<=4)/len(sents)
    res=[]
    def chk(name,ok,val): res.append((('PASS' if ok else 'FAIL'),name,val))
    chk('avg sentence words 5-12',5<=avg<=12,round(avg,1))
    chk('fragments(<=4w) >=30%',frag>=30,round(frag))
    chk('semicolons = 0',narr.count(';')==0,narr.count(';'))
    fp=re.findall(r"\b(I|me|my|myself|I've|I'd|I'm)\b",narr)
    chk('no first person in narration',len(fp)==0,len(fp))
    chk('"the man" = 0',len(re.findall(r'\b[Tt]he man\b',narr))==0,len(re.findall(r'\b[Tt]he man\b',narr)))
    chk('"Kanja" in narration = 0','Kanja' not in narr,narr.count('Kanja'))
    chk('"the Captain" present',narr.count('Captain')>=5,narr.count('Captain'))
    chk('Iron/Rust verdicts >=3',len(re.findall(r'\b(Iron|Rust)\.',t))>=3,len(re.findall(r'\b(Iron|Rust)\.',t)))
    sp=re.findall(r'\bspik',t,re.I); chk('no "spike"',not sp,len(sp))
    ban=re.findall(r'\b(magic|sorcery|supernatural|mystical|deity|gods?|goddess|divine|enchanted|spell|mana|arcane|conjure|demon|arena|gladiator)\b',t,re.I)
    chk('banned words = 0',not ban,ban)
    hed=re.findall(r'\b(perhaps|maybe|possibly|roughly|near enough|something over|somewhere|to my surprise|not certain|as far as it went|I think|I want)\b',narr,re.I)
    chk('equivocation = 0',not hed,hed)
    anti=re.findall(r"(It was not [^.]*\. It was|It is not [^.]*\. It is|\bNot because\b|not only\b[^.]*\bbut\b|was not [^.]*, but\b|is not [^.]*, but\b)",narr)
    chk('antithesis = 0',not anti,anti[:3])
    longq=[q for q in re.findall(r'"([^"]*)"',t) if len(q.split())>20]
    chk('dialogue lines <=20 words',not longq,[q[:50] for q in longq])
    present=len(re.findall(r'\b(is|are|has|does|comes|goes|stands|turns|holds|falls|drives|reads|takes|moves)\b',narr))
    past=len(re.findall(r'\b(was|were|had|did|came|went|stood|turned|held|fell|drove|read|took|moved)\b',narr))
    chk('present >= past in narration',present>=past,f'{present}/{past}')
    print(f, f'words={n}')
    for r in res: print(' ',*r)
