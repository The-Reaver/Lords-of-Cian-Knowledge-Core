import json, re, sys
P = "canon-ledger.json"
D = "docs/lords-of-cian/chronicles/"
APPROVAL = "I want to go with all of the recommendations for world travel"
LOCK = sys.argv[1] if len(sys.argv) > 1 else ""
SOURCE = "Original invention, chat-drafted 2026-10-03, no source document"
d = json.load(open(P, encoding="utf-8"))
R = {r["id"]: r for r in d["rules"]}
nb = max(b["batch"] for b in d["batches_completed"]) + 1
TAIL = f" Abad's approval: '{APPROVAL}' / '{LOCK}'"
NEW = [
 ("MCD-1893", "world-cosmology", "One World, Many Shores: there is no space travel in this universe. Every 'world' in the series is a continent-world of one great planet, separated from the others by the World-Sea, so vast and lethal that each is a separate world to the others in language, law, sky, and history. The planet carries four continents (MCD-142): Cian, Kanja's world -- all eleven regions of GEO-002 -- whose people call their own continent-world 'Cian'; Kares Prime, Lauris's homeworld, on the planet's far side; the homage World of the Phase 2 era (MCD-313), across the World-Sea; and the fourth continent, uncharted, its peoples unknown on Cian. (The Foreign Sea nation of MCD-490/MCD-1040 is a maritime power within the waters reachable from Cian by ordinary sailing, not the fourth continent.) The planet as a whole has no common name among any of its peoples. Every crossing between worlds is made by sea."),
 ("MCD-1894", "world-cosmology", "The Long Currents: the World-Sea can be crossed only along a few vast ocean currents, driven by pressure, salinity, and temperature, and each runs one way -- a vessel rides it across in weeks but cannot sail against it. Returning requires finding a return loop, a second current that bends back, which shifts with the seasons and is hard to read. Few pilots in any age can read them. This is why crossings are rare, why the second Karesian diaspora's women left 'rarely returning' (MCD-158), why the Kareth War-Order's founding expedition never went home (MCD-151), and why migration between worlds is, for most people, one-way. Kares Prime lies where several Long Currents converge, so its crossing-harbors receive far more arrivals -- traders, raiders, castaways -- than any other shore, and those who leave again go by the return loops that Karesian pilots, and a few foreign ones, learned to read. A Long Current also runs from the homage World's shore to Cian, which is the route its comrades take into Book 1 (PH2-048). Kanja, carrying the Mar sense at a strength few even of his own bloodline match, is among the few who can cross both ways: his Mar bloodline's navigation tradition, barometric pressure read through the inner ear and salt content tasted on the water (MCD-295), is exactly the sense the return loops require. That is how he becomes a recurring guest in the homage World across his eras, and why the Sovereign Trust and the SBD cannot reliably follow: they can ride out, but they cannot get home."),
 ("MCD-1895", "world-cosmology", "Kares Prime, the dense shore: its continent rides over the planet's densest mass concentration, which is why its surface gravity is ~4.7x Cian's (MCD-148) -- density physics, not distance. Suspended hexagonal mineral crystal in its dense, mineral-heavy atmosphere splits the one sun into a permanent second image (a parhelion), the doubled sun Karesians have always lived under, and filters its light amber-and-bronze (MCD-1549). The continent stands as a high, dense plateau whose escarpment rises even above the World-Sea's mounded swell around it: from the Olmedrin crossing-harbor on that escarpment the sea and every other world lie below, which is the literal ground of Lauris's departure line, 'The world is below me' (MCD-1558). Living Drakma comes from a single celestial impact at Mao (WC-013, MCD-142); the impact's shock, focused through the planet to its antipode, seeded ore veins in the crust beneath three of the four continents -- Cian, Kares Prime, and the fourth continent. The homage World is the one continent with none, which is why its people's gifts are their own biology and chemistry, never Drakma-forged (as already locked for Arturo Salvatierra Duho's non-density biochemistry, PH2-061)."),
 ("MCD-1896", "world-cosmology", "The Deep Road: beneath the World-Sea runs an abyssal route along the trench floors (the Voskharen Trench among them), crossable only by bodies or hulls that can bear crushing pressure. It is the home ground of the Vael Kem, the pressure-born deep-ocean civilization, scattered, not destroyed (MCD-041). It is rare, secret, and dangerous: the route by which T.D.K.'s sea forces, the Ever-Haunt, and engineered Tide-Wraiths move where the Long Currents do not run, and one reason the Book 5 Tide Line must be held undersea (MCD-1889). Pressure-born beings, Ren (Abyss) and Anirak among them, can travel it where ordinary sailors cannot."),
 ("MCD-1897", "world-cosmology", "The Low Water: every few decades, the moon Ossenmere's long tidal cycle (COS-001) drags the World-Sea down far enough to surface shoals and land bridges along certain crossings for a single season, before the water returns. It is a generational event, the one time a crossing can be walked, held in reserve for the homage era's migration material. Where and between which shores it first appears on the page is reserved for drafting."),
]
for rid, cat, stmt in NEW:
    assert rid not in R, rid
    d["rules"].append({"id": rid, "category": cat, "statement": stmt + TAIL, "status": "locked", "source": SOURCE})
AM = [
 ("MCD-143", "what the planet of Cian is undergoing", "what the world of Cian is undergoing"),
 ("MCD-143", "functionally, a Karesian planet.", "functionally, a Karesian world."),
 ("MCD-148", "Kares Prime is a high-gravity world (~4.7x Cian's surface gravity) orbiting in the inner ring of a binary star system,", "Kares Prime is a high-gravity continent-world on the far side of the World-Sea (~4.7x Cian's surface gravity, its continent riding over the planet's densest mass concentration, MCD-1895), under a doubled sun (MCD-1549),"),
 ("MCD-151", "left Kares Prime in a colonial expedition and settled on Cian", "left Kares Prime in a colonial expedition, crossed the World-Sea on the Long Currents (MCD-1894), and settled on Cian"),
 ("MCD-153", "through orbital trade contacts", "through crossing-harbor trade contacts"),
 ("MCD-155", "defending an orbital trade-point", "defending a crossing-harbor"),
 ("MCD-158", "building the orbital-travel infrastructure that produced", "building the crossing-harbors and training the current pilots (MCD-1894) that produced"),
 ("MCD-160", "orbital-trade specialists managing contact with departing travelers", "crossing-harbor specialists managing contact with arriving traders and departing travelers"),
 ("MCD-171", "An orbital trade representative", "A crossing-harbor trade representative"),
 ("MCD-174", "through the Olmedrin orbital trade-point, with roughly 1,200 Karesian women present to see her off.", "through the Olmedrin crossing-harbor, with roughly 1,200 Karesian women present to see her off, riding the Long Current to Cian (MCD-1894)."),
 ("MCD-175", "making planetfall at the orbital descent station of Kesmara,", "making landfall at the crossing-harbor of Kesmara,"),
 ("MCD-313", "a distinct, physically reachable planet with its own conditions,", "a distinct continent-world across the World-Sea (MCD-1893), physically reachable by sea, with its own conditions,"),
 ("MCD-313", "Travel between worlds is available as an in-fiction mechanism,", "Travel between worlds is available as an in-fiction mechanism (the Long Currents, MCD-1894; there is no space travel),"),
 ("MCD-1549", "Kares Prime's binary-star light, filtered through its dense atmosphere,", "Kares Prime's doubled sun -- the one sun split by its dense atmosphere into a permanent second image (MCD-1895) --"),
 ("MCD-1550", "through orbital trade-points in low planetary orbit,", "through crossing-harbors on Kares Prime's escarpment, reached by the Long Currents (MCD-1894),"),
 ("MCD-1555", "at orbital trade-points", "at crossing-harbors"),
 ("MCD-1688", "the Vask Olmedrin orbital trade-point", "the Vask Olmedrin crossing-harbor"),
 ("WC-013", "Living Drakma is Jicome-exclusive sentient ore", "Living Drakma is sentient ore whose only workable native veins on Cian lie in Jicome and the Moonvault caldera (MCD-287), with diffuse trace through the crust (MCD-147) and the Archipelago's deposits descending from ore liberated in Haku's war (POL-104); its veins also run beneath Kares Prime and the fourth continent (MCD-1895). It is"),
 ("PH2-049", "ritual-forged Drakma weapons that explicitly cannot be industrialized per WC-013,", "ritual-forged Drakma weapons that explicitly cannot be industrialized per WC-013 -- none of it present in the homage World, whose continent holds no Living Drakma (MCD-1895) --"),
 ("MCD-173", "orbital-trade rumor", "crossing-harbor rumor"),
 ("MCD-196", "orbital-trade rumor", "crossing-harbor rumor"),
 ("MCD-201", "orbital-trade rumor", "crossing-harbor rumor"),
 ("MCD-1633", "at orbital trade-points", "at crossing-harbors"),
 ("MCD-147", "outside Mao", "outside Mao on Cian"),
 ("MCD-315", "outside Jicome's Mao Volcano", "outside Jicome's Mao Volcano on Cian"),
]
for rid, a, b in AM:
    s = R[rid]["statement"]; assert s.count(a) == 1, (rid, a); R[rid]["statement"] = s.replace(a, b)
norm = 0
for r in d["rules"]:
    if r["status"] == "LOCKED":
        r["status"] = "locked"; norm += 1
FILES = [
 ("lauris-chronicle-lxxi-the-world-is-below-me.md", "the Vask Olmedrin orbital trade-point", "the Vask Olmedrin crossing-harbor"),
 ("lauris-chronicle-lxxi-the-world-is-below-me.md", "since making planetfall on Cian", "since making landfall on Cian"),
 ("lauris-chronicle-xvi-the-weight-they-meant-to-take.md", "at orbital trade-points", "at crossing-harbors"),
]
for fn, a, b in FILES:
    t = open(D + fn, encoding="utf-8").read()
    pat = r"\s+".join(re.escape(w) for w in a.split())
    assert len(re.findall(pat, t)) == 1, (fn, a)
    t = re.sub(pat, b, t); open(D + fn, "w", encoding="utf-8").write(t)
d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": len(NEW) + len({x[0] for x in AM}),
  "note": "World cosmology locked, no space travel (MCD-1893-1897): One World, Many Shores (four continent-worlds of one planet, per MCD-142: Cian, Kares Prime, the homage World, the Foreign Sea continent); the one-way Long Currents and their return loops, read by Kanja's Mar senses; Kares Prime's density-driven gravity and doubled sun; Living Drakma beneath three continents, none under the homage World; the Deep Road; the Low Water in reserve. All orbital and planetfall wording replaced (MCD-143, 148, 151, 153, 155, 158, 160, 171, 174, 175, 313, 1549, 1550, 1555, 1688; WC-013; PH2-049) and in three Lauris Chronicles; status casing normalized on " + str(norm) + " rules. Abad's approval: \"" + APPROVAL + "\" / \"" + LOCK + "\""})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1)); d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False); open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]; print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
