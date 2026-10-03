import json, re
P = "canon-ledger.json"
DRAFT = "docs/lords-of-cian/drafts/2026-10-03-tide-line-and-world-crossing.md"
APPROVAL = "and all of my recommendations in this she will shine and we will display her incredible array of devastating combinations"
PRIOR = "go with C and all your recommendations"
SOURCE = "Original invention, chat-drafted 2026-10-03, no source document"
d = json.load(open(P, encoding="utf-8"))
R = {r["id"]: r for r in d["rules"]}
nb = max(b["batch"] for b in d["batches_completed"]) + 1
TAIL = f" Abad's approval: '{PRIOR}' / '{APPROVAL}'"
NEW = [
 ("MCD-1889", "The Tide Line is Book 5's fourth front, held by Anirak alone in command with her own unit drawn from the Long Mask pirate crew. It opens in the Talisman's 48-hour reallocation deficit (MCD-145-147), when the planet's coastal hardening runs at reduced capacity, and covers the sea approaches and the western shore the other three fronts leave open. It runs in two phases inside those 48 hours: undersea, where the pirate crew and fleet hold the sea approach against Sereth Vaul's Ever-Haunt naval forces and engineered Tide-Wraiths from a third production site (the distributed redundancy already implied at MCD-191; not the third Operation 38 facility); then ashore, on the western shore, the 'alliance's western front' of MCD-328. It is the longest sustained engagement in the series, which is why Anirak reaches Flood State there and nowhere else (ARS-369). Its success keeps the sea and the western coast closed while the Engine front recovers the Meridian Engine fragment (MCD-327). It touches the Line exactly once, where the shore phase meets the Line's flank, and her active sonar relays naval positions to Ironbane's fleet on the Line throughout (ARS-371)."),
 ("MCD-1890", "The Tide Line's roster: Anirak, Blades Fury, in sole command. Her core is her original Chain Harbor unit (MCD-251, MCD-1883): Edda, Hamund, and Odile, the three prisoners she freed by hand in the eastern passage, Maw-raised and loyal to her before any loyalty to Kanja -- the first sub-crew in the Lords of Cian loyal to a lieutenant. The pirate crew: Torian (Bloodreaver), Stormbreaker (Kaelen), Azar Dreadlord, Voidbreaker (Jax), Ghostwind (Sylas), Stormreaver (Kairo), and Soulreaver Zora, none of whom has another locked Book 5 placement, most recruited during the Long Mask and the Pirate Dawn. Ren (Abyss) holds his locked role at her side as aftermath-radius manager (ARS-369, ARS-372, CC-114). The fleet is the Long Mask fleet the pirate crew sailed under the Scourge. Ironbane stays on the Line with his fleet (MCD-221); Zora, his partner (CC-063), fights on the Tide Line, so the two fronts' standing links run through the two of them and through Anirak's sonar relays. Valen's reckoning with the Blade (CC-146, ARS-385) keeps no fixed front. The founding dock crew, about 330-350 years old at Book 1, do not fight on the Tide Line."),
 ("MCD-1891", "The Obsidian Prefecture's 200,000 legionaries (MCD-328) arrive on the western shore as the alliance's committed reinforcement and are turned mid-battle by Lady Vestige's perception-warfare (MCD-282, POL-100): forged orders, engineered optics, and manipulated signals make the legions read the alliance as the enemy, while Severin Ebonrath's Senate believes the commitment was its own patient calculus. The turned legions are living soldiers, so Anirak's Siren's Voice and gaze work on them (ARS-373), and her always-on attention-capture (CC-112) is the one force on the shore that competes directly with Vestige's perception field. Anirak and the pirate crew hold 200,000 turned legionaries on the shore until the deception breaks. How the turn breaks, and what it costs, is reserved for Book 5's own drafting."),
 ("MCD-1892", "Sereth Vaul, 'the Silencer,' is Anirak's named Book 5 opponent in the Tide Line's undersea phase: the Silencer against the Siren's Voice. He is the only being who stays functional inside an Ever-Haunt Anti-Resonance field (MCD-281); her Lantern-Star is a locked Ever-Haunt countermeasure (ARS-411, CULT-197); both of them hunt by sound. The outcome of their engagement is reserved for Book 5's own drafting, and no pre-Book-5 material may assert or imply it."),
]
for rid, stmt in NEW:
    assert rid not in R, rid
    d["rules"].append({"id": rid, "category": "book5-structure", "statement": stmt + TAIL, "status": "locked", "source": SOURCE})
AM = [
 ("MCD-097", "Book 5, The Miner's Son: three fronts,", "Book 5, The Miner's Son: four fronts (the Engine, the Gate, the Line, and the Tide Line, MCD-1889),"),
 ("WC-022", "Book 5 The Miner's Son (three fronts,", "Book 5 The Miner's Son (four fronts -- the Engine, the Gate, the Line, and the Tide Line, MCD-1889 --"),
 ("MCD-221", "Book 5's three fronts (already locked in general at MCD-097) break down as: Engine front -- Kanja, Ozmund, Pyro. Gate front -- Orlok, Anansi, Ezio, Fermand, Legbara (matching the already-locked Gate team of MCD-098). Line front -- commanded independently by Red Beard (not literally alone), comprising Anirak, Ironbane's fleet,",
             "Book 5's four fronts (already locked in general at MCD-097) break down as: Engine front -- Kanja, Ozmund, Pyro, and Lauris (ARS-386). Gate front -- Orlok, Anansi, Ezio, Fermand, Legbara (matching the already-locked Gate team of MCD-098), with Valeria present for the on-page sibling reveal (MCD-220/MCD-224). Line front -- commanded independently by Red Beard (not literally alone), comprising Ironbane's fleet,"),
 ("MCD-221", "and the Astral Archipelago fleet.", "and the Astral Archipelago fleet. Tide Line -- Anirak in sole command with her pirate-crew unit (MCD-1889, MCD-1890); amended Batch " + str(nb) + ", when Anirak moved from the Line to the new fourth front."),
 ("ARS-368", "(Book 5 Line front only -- see ARS-369 --", "(Book 5 Tide Line only, MCD-1889 -- see ARS-369 --"),
 ("ARS-369", "(Book 5 Line front exclusively -- the series' longest sustained engagement, extending MCD-221's Line-front roster)", "(Book 5 Tide Line exclusively, MCD-1889 -- the series' longest sustained engagement)"),
 ("ARS-369", "Red Beard (commanding the Line front per MCD-221) responds to her reaching Flood State by silently increasing his own operational distance by 30 meters.", "Red Beard (commanding the Line front per MCD-221) responds to her reaching Flood State by silently increasing his own operational distance by 30 meters, at the single moment the Tide Line's shore phase meets the Line's flank -- the one time he stands within sight of her at Flood State."),
 ("ARS-371", "making her the Line front's earliest naval-perimeter warning system -- she reports positions to Ironbane (extends MCD-221's Ironbane's-fleet Line-front component)", "making her the alliance's earliest naval-perimeter warning system -- from the Tide Line (MCD-1889) she reports positions to Ironbane's fleet on the Line (MCD-221)"),
 ("ARS-373", "Flood State occurs only in the Book 5 Line front;", "Flood State occurs only on the Book 5 Tide Line (MCD-1889);"),
 ("ARS-374", "(extends MCD-221's Line-front roster)", "(any shared engagement before Book 5; in Book 5 Lauris is on the Engine front, ARS-386, and Anirak on the Tide Line, MCD-1889)"),
 ("ARS-374", "In a shared Book 5 engagement,", "In a shared engagement,"),
 ("MCD-328", "commits 200,000 legionaries to the alliance's western front", "commits 200,000 legionaries to the alliance's western front -- the Tide Line's shore phase (MCD-1889), where Lady Vestige turns them mid-battle (MCD-1891) --"),
]
for rid, a, b in AM:
    s = R[rid]["statement"]; assert s.count(a) == 1, (rid, a); R[rid]["statement"] = s.replace(a, b)
d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": 4 + len({x[0] for x in AM}),
  "note": "The Tide Line locked as Book 5's fourth front (MCD-1889-1892): Anirak in sole command of a pirate-crew unit (her Chain Harbor core Edda, Hamund, Odile; Torian, Stormbreaker, Azar, Voidbreaker, Ghostwind, Stormreaver, Zora; Ren), undersea against Sereth Vaul's Ever-Haunt sea forces and a third Tide-Wraith site, then ashore holding the Prefecture's 200,000 legionaries turned by Lady Vestige. Flood State, the Ironbane sonar relay, and Red Beard's 30 meters relocated intact; MCD-221's roster aligned with ARS-386 (Lauris, Engine) and MCD-220/224 (Valeria, Gate); ARS-374 rescoped before Book 5. Abad's approval: \"" + PRIOR + "\" and \"" + APPROVAL + "\""})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1)); d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False); open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]; print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
t = open(DRAFT, encoding="utf-8").read()
a = "*UNLOCKED -- pending Abad's approval. Drafted 2026-10-03"
assert t.count(a) == 1
t = t.replace(a, f"*Part 1 LOCKED, Batch {nb}, 2026-10-03 (`MCD-1889`-`1892` and the listed amendments). Abad's approval: \"{PRIOR}\" and \"{APPROVAL}.\" Part 2 is still a pending choice. Drafted 2026-10-03")
open(DRAFT, "w", encoding="utf-8").write(t)
