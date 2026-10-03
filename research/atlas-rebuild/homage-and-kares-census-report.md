# Homage World and Kares Prime: Place-Name Census

*Research input for the World Atlas rebuild, 2026-10-03. Read-only census. Nothing here is canon,
and nothing in `canon-ledger.json` or any Chronicle was edited.*

Companion data files, in the same folder:
- `homage-world-gazetteer.json` (89 entries)
- `kares-prime-gazetteer.json` (33 entries)

Each entry carries `name`, `aliases`, `type`, `city_or_region`, `parent`, `homage_of`,
`locational_claims` (each with a source), `first_source`, `mention_count`, `mention_count_basis`
and `notes`.

## 1. Sources read

**Homage World**
- All 66 `PH2-` rules
- The territory-Chronicle rules (`MCD-334` onward, category `phase2-territory-chronicle`) plus
  `MCD-313`, `MCD-331`, `MCD-472` and `OPEN-009`
- The narrative prose of all 74 territory-Chronicle files. That is 63 prefixed files plus 11
  second entries filed without a territory prefix:
  - `the-building-that-wouldnt-choose-a-side.md` (Jibaro)
  - `the-cost-of-being-corrected.md` (Nyansa)
  - `the-fire-that-spread-too-thin.md` (Umoja)
  - `the-ledger-she-built-from-nothing.md` (Ijoko)
  - `the-man-who-had-nothing-left-to-give.md` (Kwan)
  - `the-meal-that-bound-nothing.md` (Hekalu)
  - `the-oath-he-didnt-mean.md` (Taifa)
  - `the-record-they-tried-to-rewrite.md` (Ide)
  - `the-weeks-the-chair-sat-empty.md` (Kiti)
  - `what-patience-actually-grows.md` (Atunbi)
  - `what-the-ark-actually-carries.md` (Orin)
- `docs/lords-of-cian/phase2-homage-era-development.md`
- `research/phase2-homage-source-material/fourth-city-candidates-research.md`
- The Batch 363-367 notes and `approval-list-2026-10-03.md`

**Kares Prime**
- `MCD-140` through `MCD-217` and `MCD-1533` through `MCD-1560`
- Every rule that cites a Strand K entry
- The narrative of all 26 Strand K Lauris Chronicles (II, VI, X-XXI, LX-LXXI), plus a corpus-wide
  grep of all 110 Lauris files

## 2. Counts

**Homage World: 89 gazetteer entries.**

| Group | Entries | What it covers |
|---|---|---|
| World level | 10 | The World itself, the inter-world crossing, the old empire, lands across the sea, the mountains of refuge, Duro's small town, the town two days south, Taifa's claimed land and outer post, Taifa's three or four cities |
| Cities | 4 | Batey, Ìlú-Márùn, Muungano, Mji |
| Territories | 20 | Five per city |
| Sites | 55 | Sites inside territories, plus the Downtown Combine and the Five Families' turfs |

- Only six in-fiction proper place names exist below city level: the 20 territory names, East
  Gate High, and "the Downtown Combine," which implies a district called Downtown.
- Every other site is generic, for example "the barbershop," "the seminary," "the clinic" or "the
  plant."
- No street, avenue, river, shore, neighborhood or building in the homage World has a name.

**Kares Prime: 33 gazetteer entries.**

| Group | Entries | What it covers |
|---|---|---|
| Cosmic and terrain | 4 | The planet, the binary star system, the primary continent, the spine ridge |
| Trade stations | 4 | The general trade-point network, the Olmedrin point, the Chronicle XVI point, Vael's point |
| Vasks | 13 | The forty-Vask set, plus the twelve surviving Vasks |
| Settlement | 1 | Ilvane, the daughter-hold |
| Sites and institutions | 11 | Galleries, the ore-vein, the saddle, the training floor, the terrace, the passages, the Iron-Halls, the Conclave, the Sister-Hold |

- Most-mentioned places (counts include people's surnames such as "Veska Karth-Ven"):
  - Karth-Ven: 141
  - Threnarr: 120
  - Olmedrin: 44
  - Aldreth: 34
- Six of the twelve Vasks appear exactly once in the whole corpus, in the `MCD-160` list: Sethrenn,
  Vor-Meth, Ostrenn, Drenmar, Aerth and Karen-Drael.

## 3. Conflicts between locational claims

### Kares Prime

**K1. Which Vask is the smallest.**
- Karth-Ven is the smallest:
  - `MCD-160`: Karth-Ven is "smallest but operationally critical."
  - `MCD-1554`: "Vask Karth-Ven, the smallest of the twelve surviving Vasks (~480 residents)."
  - Lauris Chronicle XII agrees.
- Olmedrin is the smallest:
  - `MCD-160`, in the same sentence: Olmedrin is "the smallest by population."
  - Lauris Chronicle LXXI: Olmedrin is "the smallest of the twelve surviving Vasks."
- `MCD-160` contradicts itself, so a ruling is needed.

**K2. Is a trade-point in orbit or on the ground?**
- In orbit:
  - `MCD-1550`: "orbital trade-points in low planetary orbit."
  - `MCD-155`: Vael died "defending an orbital trade-point."
- On the ground:
  - Lauris Chronicle LXXI describes "the trade-point's outer gate" and "Olmedrin's modest
    trade-point grounds," where 1,200 women gather. Lauris then "boarded the departing vessel."
  - Lauris Chronicle XVI has a "receiving hall," with crated Drakma loaded onto "a transport sled
    bound for their vessel."
  - `MCD-173` and `MCD-1555`: raiders attack trade-points and Vasks overland.
- One possible reading is a surface port that serves orbital traffic. The map needs a ruling.

**K3. Is Ilvane a Vask?**
- Batch 366 ruled Ilvane a Threnarr daughter-hold. `MCD-1635` now says "never one of the forty
  Vasks," and Chronicle XVIII's own header agrees.
- Chronicle XVIII's closing archive line still says: "*Ilvane no longer exists as a Vask.*"
- This is a leftover the Batch 366 fix missed. The same entry also calls Threnarr and Aldreth "two
  larger Holds," which blurs the words "Hold" and "Vask."

**K4. Who runs the trade-points.**
- `MCD-160`: Olmedrin holds "the orbital-trade specialists."
- Lauris Chronicle LXIX: "Threnarr's thinned trade-points."
- This is a soft conflict over whether each Vask has its own points or Olmedrin runs them all.

**K5. Which Vask is the archive.**
- `MCD-160` gives "historical archives" to one of seven unassigned Vasks, and calls Vask-of-Vasks
  "cultural rather than operational."
- Lauris Chronicle LXVI says Vask-of-Vasks has "its halls given over almost entirely to archive."
- Neither source says where the Iron-Halls of Vask stand (`MCD-158`, `MCD-1548`).

**K6. An ambiguous distance (not a contradiction).**
- Chronicle XVIII says Aldreth sits "nearer Ilvane's location by some six days' travel."
- It is unclear whether six days is the trip to Aldreth or the difference between the two routes.

**K7. A phrasing slip.**
- Lauris Chronicle XIII says Ezio reads her report "centuries and a whole ocean of distance
  later."
- Kares Prime to Cian is an interplanetary distance, not an ocean.

**Cross-world name collisions to keep apart on the maps:**
- "Vask of the Hollow" (`MCD-1537`) is a site on Cian that uses the Kares word "Vask."
- "Iron-Halls of Velkar" (`MCD-181`) on Cian versus the "Iron-Halls of Vask" on Kares Prime. This
  one is already acknowledged as a coincidence.

### Homage World

**H1. Jibaro: church or seminary.**
- `PH2-042`: Omoba "occupied a seminary and a church, running free breakfast, health, and daycare
  programs from the latter."
- Jibaro Chronicle I: "He built the clinic inside the seminary instead."
- No church appears anywhere in Jibaro's three Chronicles.

**H2. Taifa's size against "territory of Mji."**
- `PH2-052`: Taifa is "Mji's second territory."
- Taifa Chronicle I: Taifa's cells are "scattered across three cities and one stretch of claimed
  land none of them could reach inside a week's hard travel." Word also comes "from a fourth city."
- Taifa cannot be drawn as a district of one city.

**H3. Xaragua's scale.**
- `PH2-001` makes Xaragua a borough-equivalent of Batey.
- But canon gives it a nation-scale history:
  - `PH2-002`: "the old empire" and "a foreign cell."
  - `PH2-014` and `PH2-016`: mountains of refuge, crossings by sea, "exiles abroad."
  - Xaragua Chronicle I: "Xaragua's southern approach had been theirs for six generations," a
    seaborne siege on "this spit of land," and "ships on the horizon."
- A ruling is needed on whether the island histories happened inside Batey, or in an old country
  that Xaragua's people carried with them.

**H4. Kazi: plant or district.**
- `PH2-050`: Kazi is anchored "on the auto-plant floor rather than any single building or
  neighborhood."
- Kazi Chronicle III: "freight through Kazi's own district," with piers and a "central loading
  yard."

**H5. Areíto and Guanín share a square.**
- Guanín Chronicle II leaves both pamphlets "in the same square for anyone in either territory to
  weigh."
- This implies the two territories border each other or share a square. Real Harlem and Queens do
  not touch.

**H6. Where Ase's account went.**
- Ide Chronicle I and `MCD-342`: the account is carried "out of Ide," with one copy going to "a
  town two days south."
- `the-record-they-tried-to-rewrite.md`: "carried across the city."
- This is a mild conflict.

**H7. Spelling drift in the city name.**
- `PH2-` rules: "Ílú-Márùn."
- The project instructions file and the brief: "Ìlú-Márùn."
- The ASCII forms "Areito," "Guanin," "Boriken" and "Aztlan" run alongside the accented forms.

**Incidental, not geography:** in `the-man-who-had-nothing-left-to-give.md`, Kasa is "she"
("She sat with him instead"). Kasa is "he" everywhere else.

## 4. Leaked real-world place names in narrative prose

**None found in the homage World.**
- About 70 real place and institution names were scanned against the narrative bodies of all 74
  territory Chronicles: New York, Harlem, Bronx, Chicago, Detroit, Watts, Compton, Haiti, Cuba,
  NAACP, COINTELPRO, Taíno and others.
- There were zero hits. Every real name ("Chicago," "COINTELPRO," "Harold Washington," "Toussaint
  Louverture," "Grace Lee Boggs") sits in headers or continuity notes, which the convention allows.

**Borderline items, flagged rather than ruled:**
- "Doña Alma" (Borikén II) is a Spanish honorific plus given name. Compare the convention's
  treatment of colonial Spanish names in Batch 83 and Batch 101.
- "cantina," "rum" and "plantain" (Xaragua II) are generic words, not proper nouns.
- The `PH2-` rule statements carry real names only as homage citations, which is allowed.

**Kares Prime:** no real-world names.

## 5. Gaps

### Homage World

1. **The World has no name.** It also has no sky, moon, calendar, climate, continent or ocean
   facts.
2. **There is no inter-city geography.**
   - Nothing says whether the four cities share a continent, a nation, a river system or a road
     network, or how far apart they are.
   - The only distances in canon are "a town two days south" of Muungano and Taifa's "a week's hard
     travel."
   - Travel modes are riders, roads, couriers and ships.
3. **There is no crossing to or from Cian.**
   - `MCD-313` says travel between worlds exists. No gate, port, vessel, arrival site or transit
     time is defined on either side.
   - Kanja is never shown arriving.
   - The only scene of an homage figure on Cian (`MCD-331`) was withdrawn.
   - `PH2-048` says these comrades reinforce Book 1, so a route is required.
4. **There are more than four cities.** Taifa I names three unnamed cities and a fourth. There are
   also overseas lands: "the old empire" and Yaque's country.
5. **Ìlú-Márùn has no physical geography at all.** It has no coast, hills, river or freeway
   analogue.
6. **Some territories have no neighborhood.**
   - Uhuru and Kiti are civic overlays.
   - Kazi, Taifa, Hekalu and Nyansa homage institutions, not neighborhoods.
   - Possible real anchor sites (Dodge Main and Hamtramck for Kazi, Linwood Avenue for Hekalu) are
     suggestions in the JSON notes, not canon.
7. **Places inside territories are almost entirely unnamed.**
   - The Five Families are not individually named.
   - "Downtown" is implied but never placed.
   - Nyansa's "plant" is not identified.
8. **The two worlds' timelines are not related.** Umoja I has the stranger "spent centuries
   learning," which places Kanja in his Long Mask era. Nothing maps the homage calendar to Cian's.

### Kares Prime

1. **The sky and continents are thin.** The two stars, any moons, the continents other than the
   "primary" one, and all seas and rivers are unnamed.
2. **Most Vasks have no location or job.**
   - 28 depopulated Vasks are unnamed.
   - Seven of the eight minor surviving Vasks have functions listed in `MCD-160` but not matched to
     individual Vasks.
3. **Only three relative positions are known.**
   - Threnarr and Aldreth are neighbors across a mountain saddle.
   - Ilvane sits nearer Aldreth.
   - Karth-Ven is about three weeks on foot from Olmedrin, with "each of the twelve Vasks... where
     the route allowed" along the way. This implies all twelve are clustered.
4. **Some sites have no seat.** The Iron-Halls of Vask, the Conclave and the cryogenic sample store
   are unplaced. The unnamed neighboring settlement by Karth-Ven's terrace (Lauris LXIII) is the
   only hint of other daughter-holds.
5. **The journey to Cian is undefined.** Transit time, route and distance are missing. The
   arithmetic in `MCD-1533` implies near-zero transit time.
6. **The binary-star sky is never dramatized.** No Chronicle shows it.

## 6. Recommendations for the Atlas

1. **Build one atlas per world, linked by a universe-level page.** That page shows Cian, Kares
   Prime and the homage World, with the known routes:
   - Olmedrin orbital trade-point to the Kesmara orbital descent station (`MCD-174`, `MCD-175`)
   - The undefined homage-to-Cian crossing, marked "pending a ruling"
2. **Homage World, three tiers.**
   - **World map.** It holds the four cities, Taifa's claimed land with its outposts, Duro's town,
     the town two days south, Taifa's other cities, and the overseas old empire and Yaque's
     country. This tier needs four rulings first: the World's name, the inter-city layout, the
     crossing point, and Xaragua's scale (H3).
   - **City maps,** one each for Batey, Ìlú-Márùn, Muungano and Mji.
     - Draw five districts per city, keyed to the real neighborhoods in `homage_of`, but with
       invented in-world street and landmark names that follow `PH2-034`.
     - Draw Uhuru and Kiti as citywide civic layers, centered on their seat-of-power buildings.
     - Draw Taifa as a city headquarters plus a link to its distant claimed land.
   - **Site pins.** Use the 55 site entries, and name the generic ones only when a ruling adopts
     them.
3. **Kares Prime, three tiers.** Stamp every map to Lauris's era, because mountains "rise and fall
   across generations."
   - **System diagram:** the binary stars and the inner-ring orbit.
   - **Continent map:**
     - The spine ridge
     - Markers for the twelve surviving Vasks
     - Ghost markers for the 28 dead Vasks
     - Ilvane
     - The Threnarr–Aldreth saddle and ore-vein
     - The three-week Karth-Ven–Olmedrin passage
     - A trade-point layer, drawn once K2 is ruled
   - **Site plans** for Karth-Ven (the floor, the galleries, the terrace) and Threnarr (the
     medical-archival complex, the mining galleries, the outer line).
4. **Rulings to settle before drawing:** K1 to K3, H1 to H4, the homage World's name, and the
   crossing mechanism.
