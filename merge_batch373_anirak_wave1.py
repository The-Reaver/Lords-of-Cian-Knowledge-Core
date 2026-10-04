"""Batch 373: Anirak's Character Chronicle wave 1 locked -- MCD-1898, MCD-1899, MCD-1900."""
import json
import sys
from collections import Counter

LEDGER = sys.argv[1] if len(sys.argv) > 1 else "canon-ledger.json"
CH = "docs/lords-of-cian/chronicles/"
APPROVAL = "Abad's approval: 'approved'."
CAT = "anirak-character-chronicle"

RULES = [
    ("MCD-1898", CH + "anirak-chronicle-i-what-maw-11-kept.md",
     "Anirak Chronicle I, 'What Maw-11 Kept' (full text at docs/lords-of-cian/chronicles/"
     "anirak-chronicle-i-what-maw-11-kept.md). First entry of Anirak's Character Chronicle series, "
     "close-third per VB-065. Kanja age 140, the Long Mask: dramatizes the Maw Cascade's inside job at "
     "Maw-11 (MCD-264) for the first time, and locks her part in it, which MCD-264 did not name. She "
     "mapped Ghostwind's route from her own knowledge of the tunnels and, unable to go in unseen "
     "(CC-112), went in openly by the front gate as the visible draw, holding the yard while Ghostwind "
     "carried tuned bronze reeds to the pens. The held sang the Hymn-Engine's counter-frequency "
     "themselves (ARS-398, MCD-236, MCD-265), overloading the suppression mast's box; the freed bent "
     "and sheared their own grates. Her Blight Immunity comes from the Sovereign Umbrella, whose "
     "recipient is the crew (MCD-060, MCD-140). The yard's fighters are free guards and hired wardens, "
     "all disarmed or dropped, none killed; the Slab crews and staging hands, overwhelmingly Cestari "
     "(MAW-077), walk out with the pens, and 3,800 counts everyone held behind the walls. Her first "
     "marquee kill under MCD-1881: Gethin Tamber, Maw-11's free tunnel master, who held her in her "
     "years there, killed with the Morning Star at the first grate after terms given once ('Leave it. "
     "Walk.'), as he drives a knife through the bars at a singer -- a CC-164 necessity kill fought at "
     "Warm. Only Tamber speaks her name; the freed say none, and the yard calls her Blades Fury "
     "(CC-163). Her three hold the front gate. New named character: Gethin Tamber, collision-checked. "
     "Clean on the fifth independent review."),
    ("MCD-1899", CH + "anirak-chronicle-ii-the-second-harness.md",
     "Anirak Chronicle II, 'The Second Harness' (full text at docs/lords-of-cian/chronicles/"
     "anirak-chronicle-ii-the-second-harness.md). Second entry of Anirak's Character Chronicle series, "
     "close-third per VB-065. Roughly Kanja 175, the Long Mask, at Tideglass (MCD-255), after Maw-11 "
     "and before Ren comes aboard. A thirteen-strong Sealbound Directorate Level 3 Retrieval Detachment "
     "(SBD-050; distinct from the Foundling Detachment, SBD-061) comes for Ardith, an adult escaped "
     "Directorate subject, and brings a rig built against Anirak: a net of leather bands packed with "
     "lead shot over mail, six cords, and a soaked hood sewn into a crown that cinches. The shot "
     "swallows her strikes so nothing banks, the cords hold her still so her Stack drains (ARS-439), "
     "and the hood answers the Siren and is soaked against the gorget on the Directorate's misreading "
     "of the Voice as a sound in the air (MCD-1727). It fails on the Voice, felt in the body and "
     "carried by water (ARS-438); she banks Stack from the cord-men's weight, and Hamund and Odile take "
     "the cords off her (ARS-447). New facts locked: the rig and its failure, and the rig's design "
     "surviving in its maker's record and the detachment's field file (SBD-052), with no future use "
     "reserved or implied; and a Level 3 unit fielding such a rig as an edge-of-tier contingency "
     "carried under its own retrieval sign-off, Military-Standard engagement being Level 2's task "
     "(SBD-050). The detachment uses only subduing force and no one dies; under CC-164 she has no "
     "necessity kill to make. Ardith is taken and not recovered. Her sea-sense stays coarse and "
     "ambient (ARS-367, ARS-371). Notable register. New named character: Ardith, collision-checked. "
     "Clean on the sixth independent review."),
    ("MCD-1900", CH + "anirak-chronicle-iii-the-body-the-world-was-not-built-for.md",
     "Anirak Chronicle III, 'The Body the World Was Not Built For' (full text at docs/lords-of-cian/"
     "chronicles/anirak-chronicle-iii-the-body-the-world-was-not-built-for.md). Third entry of "
     "Anirak's Character Chronicle series, closing its launch wave, close-third per VB-065. Roughly "
     "Kanja 300, late in the Long Mask: Ren (Abyss, CC-066, CC-101, CC-138) comes aboard an adult, "
     "recruited off the page and unnamed on it (CC-101's recruiter; the entry takes no side on "
     "approval-list item 38). His passive field (+30% within about 5 m) clears an empty ring around "
     "him on deck. Because he is always inside his own field, the Siren never catches his face "
     "(CC-112, ARS-446): his is the one face that leaves her and comes back by its own choosing. She "
     "walks into the ring, takes the load, eats on her feet inside it, and takes him as her charge "
     "unasked -- the origin of their pairing (CC-114). The Captain sends for his measure for boots and "
     "a vest, seeding CC-101's compensator gear. Her three stay outside the ring, so the reserved "
     "payoff of her three inside Ren's field is untouched; neither asks the other's origin (CC-163). "
     "No fight, no kill. No new named characters. Clean on the fourth independent review."),
]

d = json.load(open(LEDGER, encoding="utf-8"))
ids = {r["id"] for r in d["rules"]}
for rid, src, stmt in RULES:
    assert rid not in ids, rid
    d["rules"].append({"id": rid, "category": CAT, "statement": stmt + " " + APPROVAL,
                       "status": "locked", "source": src})

nb = max(b["batch"] for b in d["batches_completed"]) + 1
assert nb == 373, nb
d["batches_completed"].append({
    "batch": nb,
    "source": "Anirak Character Chronicle wave 1 (Game Plan pitches 2, 3, 1), drafted 2026-10-04; "
              "full texts at docs/lords-of-cian/chronicles/anirak-chronicle-i/ii/iii-*.md",
    "rules_affected": 3,
    "note": "Anirak's launch wave locked: Chronicle I 'What Maw-11 Kept' (MCD-1898, Kanja 140, her "
            "first marquee kill, Gethin Tamber), Chronicle II 'The Second Harness' (MCD-1899, ~Kanja "
            "175, the SBD anti-Stack rig), Chronicle III 'The Body the World Was Not Built For' "
            "(MCD-1900, ~Kanja 300, Ren comes aboard). Each passed the Connective-Tissue Gate and was "
            "clean on independent review (I fifth round, II sixth, III fourth). " + APPROVAL,
})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-04"
json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(LEDGER, "a", encoding="utf-8").write("\n")

d = json.load(open(LEDGER, encoding="utf-8"))
dups = [k for k, v in Counter(r["id"] for r in d["rules"]).items() if v > 1]
print("duplicates:", dups, "| rules:", len(d["rules"]), "| version:", d["ledger_version"],
      "| batch:", max(b["batch"] for b in d["batches_completed"]))
