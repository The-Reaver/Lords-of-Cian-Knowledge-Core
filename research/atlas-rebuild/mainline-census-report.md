# Mainline Cian Place-Name Census: groundwork for the Atlas rebuild

Fact-finding only. Nothing here is a canon edit or a proposed rule. It counts what the corpus
already says about places, measures that against the current Atlas, and lists the conflicts and
gaps a rebuilt Atlas has to settle. The companion data file is `mainline-gazetteer.json` in this
folder (348 entries).

## 1. Scope and method

**In scope.** Mainline Cian: Kanja's world, the Lords of Cian, Daba and 1804, Ozmund and House
Verehimu, Lauris's Directorate career and present day on Cian, the Maw, the cults, Ashkeel, and the
SBD.

**Excluded.** The Phase 2 homage World (every `PH2-` rule and the 20 territory Chronicle series) and
Kares Prime. Kares Prime is covered by a separate census. Lauris's Strand K files were still scanned,
but only Cian place names count.

**Sources read.**
- All 2,618 non-`PH2` rules plus `open_decisions` in `canon-ledger.json`.
- 1,440 mainline Chronicle files and the 2 interstitials.
- 14 character-profile docs.
- About 8.1 million characters of text in total.

**How places were found.**
- Four extraction passes:
  - suffix patterns (Harbor, Keep, Road, Narrows and so on)
  - capitalized names after location prepositions
  - capitalized names inside sentences that use location vocabulary
  - "the X garrison/depot/settlement" patterns, run per track
- Every candidate was then curated by hand against its context.
- People, institutions, artifacts, ships and events were dropped unless they name a place.
- Spelling variants and renames were merged as aliases: Ash Harbor/Ghost Harbor, Forge-7/Scrip-Forge,
  Maw-7/Keldane Maw/Slab of Judgment, the Teeth/Frontier Maw/Maw-12, Sarrow (formerly "Corrow"),
  Callow (formerly "Varrow"), Orencliff (formerly "Ferrenline").

**How mentions were counted.**
- `mention_count` scans the text with longest-match attribution. "Kessic Overwatch" counts toward
  the Overwatch, not toward Kessic.
- Ambiguous terms were restricted:
  - "Kairo" counts only in capital context; most hits are Stormreaver.
  - "Mother" and "Belly" count only as Maw-1 and Maw-3.
  - "Cian" excludes "Lords of Cian".
  - "Great Sea" is still inflated by the alias name "Sovereign Ghost of the Great Sea".

**How claims were gathered.**
- `locational_claims` holds sentences that contain the place and any direction, distance, terrain,
  coast or adjacency word.
- They are ranked by how strong the claim is: cardinal directions, numeric distances and travel times
  rank highest. Each entry keeps at most 12, and the total count is in `locational_claims_total`.
- These are machine-filtered sentences, so read them before relying on one.

**`atlas_status`.**
- `locked-GEO` means the place is named in GEO-002, 003, 005, 006 or 007. Most of these are also on
  the live sheet.
- `on-live-sheet` means the place is on the live Google Sheet but no GEO rule names it.
- `unplaced` means everything else.

**`first_source`** is the first hit in ledger order, then file order. It is a pointer, not a proven
first appearance.

## 2. Headline numbers

| Measure | Count |
|---|---|
| Census entries | **348** |
| On the current Atlas (locked-GEO 36 + on-live-sheet 84) | **120** |
| Unplaced | **228** |
| Atlas places mentioned anywhere in the mainline corpus | **42 of 120** |
| Atlas places never mentioned (pure map furniture) | **78 of 120** |
| Share of named-place mentions that point at *unplaced* places (excl. Cian, Great Sea, Ossenmere, Old Dominion) | **73%** (2,226 of 3,036) |
| Mainline Chronicle files that name **no** place in this census | **907 of 1,442** |

The current Atlas has 11 regions and 70 Gazetteer rows. The corpus has built about 230 additional
named places on top of that. **Roughly three of every four place-mentions in the corpus are to
places the Atlas cannot show.** That is the concrete form of "the world tripled." The geography is
also lopsided. The Atlas is evenly spread across eleven regions. The corpus concentrates in four or
five dense theaters, and the Atlas barely represents any of them: Jicome's Southern District, the
Trust heartland, the southern sea lanes, the 1804 hinterland, and the Verehimu lands.

### By region (as locked or implied)

| Region | Total | locked-GEO | on-live-sheet | unplaced |
|---|---|---|---|---|
| No region determinable from the text | 161 | 0 | 0 | 161 |
| Jicome (incl. implied Southern District/Portside) | 47 | 4 | 11 | 32 |
| Sovereign Trust Domain | 31 | 4 | 6 | 21 |
| Lawless Reaches | 18 | 9 | 8 | 1 |
| Obsidian Prefecture | 17 | 4 | 12 | 1 |
| Hollow Shogunate | 11 | 2 | 8 | 1 |
| Old Dominion Ruins | 11 | 2 | 6 | 3 |
| Shattered Kingdoms (frontier region) | 10 | 2 | 8 | 0 |
| Aethel-Gard | 9 | 2 | 7 | 0 |
| Celestial Zenith | 9 | 2 | 7 | 0 |
| Astral Archipelago | 8 | 2 | 6 | 0 |
| Offshore (Ashkeel and its interior) | 8 | 0 | 0 | 8 |
| T.D.K. Peninsula | 7 | 2 | 5 | 0 |
| Shattered Kingdoms (macro term) | 1 | 1 | 0 | 0 |

The five Shattered Kingdoms nations, the T.D.K. Peninsula and the Lawless Reaches are almost entirely
Atlas-only content, and the corpus barely visits them. The two regions where the story actually
happens, Jicome and the Trust Domain, are where two-thirds of entries are unplaced. Most of the 161
places with no region come from the Rebellion and Long Mask alias tracks, which mostly never say
where they are.

### By type (grouped)

| Type group | Total | locked-GEO | on-live-sheet | unplaced |
|---|---|---|---|---|
| Settlement / town / village / market | 51 | 1 | 15 | 35 |
| Fort / garrison / hold / depot | 49 | 3 | 21 | 25 |
| Road / route / pass / crossing / bridge / ford | 48 | 1 | 24 | 23 |
| Facility / vault / archive / office | 29 | 1 | 2 | 26 |
| Coast / harbor / port / pier / wharf | 28 | 0 | 7 | 21 |
| Water (sea, strait, river, reef, trench) | 27 | 0 | 13 | 14 |
| District / quarter / city level | 24 | 0 | 1 | 23 |
| Maw / arena / pit / Pillar compound | 23 | 7 | 1 | 15 |
| Capital / city | 21 | 12 | 0 | 9 |
| Nation / region / polity | 18 | 11 | 0 | 7 |
| Terrain / natural feature | 14 | 0 | 0 | 14 |
| Site / landmark / other | 10 | 0 | 0 | 10 |
| House seat / estate / realm | 3 | 0 | 0 | 3 |
| World / moon | 3 | 0 | 0 | 3 |

The current Atlas has no districts, no facilities, no city interiors and no noble estates. The
corpus has 24 districts and city levels, 29 facilities, and a whole House realm.

### By cluster (see §4)

| Cluster | Entries | Unplaced | Mentions |
|---|---|---|---|
| Jicome Southern District / Portside (Rebellion home theater) | 30 | 28 | 951 |
| Regions & macro-geography | 22 | 11 | 791 |
| Long Mask & Southern Seaboard maritime theater | 42 | 42 | 300 |
| Live Atlas Gazetteer (sheet-only places) | 107 | 0 | 279 |
| Lauris: Directorate operations & present-day sites | 16 | 16 | 252 |
| Rebellion field theater (alias one-offs) | 47 | 47 | 154 |
| 1804 network (Daba) | 10 | 10 | 154 |
| Trust Domain interior, Kesmara & SBD/Directorate sites | 17 | 17 | 153 |
| House Verehimu realm (Ozmund) | 10 | 10 | 130 |
| Cult geography, deep history & Book-era sites | 9 | 9 | 120 |
| Maw system, Pits & shadow economy | 11 | 11 | 78 |
| Voskharen coastal province | 5 | 5 | 48 |
| Karkosa interior, Maw compounds, cult & Ashkeel interiors | 22 | 22 | 46 |

Most-mentioned unplaced places, by mention count:
- Black Trench (215)
- L9 / the Silent Infinite (87)
- the Rookery (71)
- Dredge-Line (64)
- Gale Straits (64)
- Warehouse Twelve (61)
- Ash-Wharf (58)
- Scrip-Forge (57)
- Iron Shallows (49)
- Pier Nine (47)
- Living Gate (46)
- Furnace District (45)
- Drowning Vault (35)
- Greyfen (33)
- Korren Highlands (32)
- Maw-9 (32)
- Brokenwall (32)
- Sovereign Pier (31)
- Velaris (31)
- Ashkeel (28)

## 3. Conflicts between locational claims

These are conflicts, or unresolved tensions, between claims that are already locked or written,
quoted with their sources. Items marked *(pending)* overlap the earlier reconciliation pass
(`reconcile/D-atlas.md`) and are still awaiting a ruling.

### Hard conflicts

1. **One continent or four?**
   - GEO-002: "The continent maps eleven named regions..."
   - MCD-142: the Talisman's pulse "aligns dormant Living Drakma ore veins running through the crust
     beneath three of the four continents."
   - The Atlas is a single "Continental Atlas" with 342 of its 600 cells blank. The ledger says the
     world has four continents.
   - "The Flag From a Foreign Sea" (MCD-490) and its sequel add a foreign nation across an unmapped
     sea.

2. **Living Drakma's range.**
   - WC-013: "Living Drakma is Jicome-exclusive sentient ore".
   - MCD-315: the Moonvault holds "the only known Living Drakma deposit outside Jicome's Mao Volcano".
   - POL-103: the Archipelago's floating islands have "Living Drakma deposits in the geology producing
     buoyancy".
   - MCD-142 (above): ore veins beneath three of the four continents.
   - POL-104 half-reconciles the Archipelago case. It says liberated ore was carried there, which is
     not a native deposit, and that still contradicts POL-103's "in the geology".
   - MCD-147 (Batch 364) narrows the crustal claim to "diffuse trace". MCD-142's "ore veins" were not
     narrowed with it.

3. **The Hollow Shogunate and the Astral Archipelago are neighbors in the cult rules but far apart
   on the Atlas.**
   - CULT-011: about forty Weighing Communities "occupy the administrative borderland between the
     Hollow Shogunate and the Astral Archipelago's outer island chain."
   - CULT-086: the Compact navigates "dead-water channel... between the Astral Archipelago's outer
     islands and the Hollow Shogunate's coastal waters."
   - On the Atlas, the Shogunate (SH) is at R05-T08 in the northeast and the Archipelago (AA) is at
     I26-L28 in the south. They are about 18 rows apart, roughly 3,600 miles, with no shared border.

4. **The Lawless Reaches' share.** *(pending)*
   - POL-010: "approximately 12% of the world... of the full 200-mile world overview grid". This only
     works if the RA and UK cells are counted.
   - WC-012: "the Lawless Reaches (30% of SK landmass...".
   - With RA and UK counted, the Reaches come to about 39% of the Shattered Kingdoms' land. Without
     them they are about 9% of the grid.
   - MCD-094's 75/15/10 split works only as a land-area share with the Old Dominion Ruins counted as
     Trust.

5. **Travel time to the Frontier Maw.** *(pending)*
   - MAW-078: "Keldane Reach to Frontier in ~3 days, the full Southern Seaboard in ~2 weeks, Southern
     Seaboard to Shattered Kingdoms in ~6 weeks via the Frontier Maw".
   - GEO-007: the Teeth is "roughly a thousand miles east of the Sovereign Trust Domain".
   - Three days for 1,000+ miles is impossible at this world's tech level.
   - MAW-078 also contradicts itself: 3 days to the Frontier Maw, but 6 weeks to the Shattered
     Kingdoms through that same Frontier Maw.

6. **Distance from the Domain to the Teeth.**
   - GEO-007 says "roughly a thousand miles".
   - On the grid, G16 to N16 is 7 cells × 200 mi, which is about **1,400 miles**.
   - Small, but GEO-007 is the only locked distance on the whole map.

7. **The Southern Seaboard.** *(pending, MCD-112 flagged)*
   - Uses that make it Jicome's coast:
     - MCD-237: "all nine Blight Frequency relay towers on Jicome's stretch of the Southern Seaboard"
     - Chronicle VIII: "the Trust's Southern Seaboard grain route"
   - Uses that make it the Domain's coast:
     - MAW-144: Keldane Hollow is "the largest active Named Pit on the Southern Seaboard"
     - MAW-133: the Sektori Consortium, "the Southern Seaboard's largest Scrip-lending institution...
       in Karkosa's financial district"
   - CC-150 also places the Seaboard: "Gale Straits/Southern Seaboard waters".
   - The Atlas has Jicome (A01-C09) and the Domain (G15-H17) about 1,400 miles apart. Neither region
     has a "southern seaboard" that reaches the other.

8. **Where the Old Dominion was, and when.**
   - GEO-007: the empire's former capital "survives as the ruins housing the Ash Maw/the Scar (J19,
     Lawless Reaches)", while the OD region is "the empire's ruined northern heartland" at M03-O09.
     That puts the capital about 1,000 miles south of its own heartland.
   - WC-010: the Broken Meridian lies "beneath what later became the Old Dominion's foundations"
     without saying which.
   - MCD-098: Book 5's Gate is at "the Broken Meridian entrance".
   - CULT-108: Old Dominion ruin sites span "all five nations".
   - The dates disagree as well:
     - MAW-091: Era I, the Old Dominion, "~5,000-3,000 years ago".
     - CULT-156 and CULT-108: the Null-Walkers' "roughly eleven-thousand-year-old circuit", begun as
       workers "maintaining active Old Dominion infrastructure".
     - MCD-1850: the first Verehimu reached "the Old Dominion's capital territory" about 8,000 years
       ago.
     - MAW-065: the Mother (~4,900 years) is "T.D.K.'s prototype" Maw.

9. **T.D.K.'s seat has five candidate locations.**
   - The Dark Spire is the T.D.K. Peninsula's capital (GEO-003). It sits in "T.D.K.'s southeastern
     'dead ground'" (POL-101).
   - The Ash Maw ruins are "T.D.K.'s original court complex" (GEO-007).
   - The Measurist Guild places "T.D.K.'s central administrative infrastructure" in "a specific
     mountain range in the Hollow Shogunate's interior" (CULT-028). This is an in-world theory.
   - The Broken Meridian, under Old Dominion foundations (WC-010).
   - These need a layered chronology, not a single pin.

10. **What the `##` strip on the Atlas is.**
    - POL-020: "the five nations like points around a central volcanic ridge running north-south."
    - CC-091: Orlok was born at "a volcanic-ridge Dominion extraction site (later the Celestial
      Zenith's territory)".
    - MAW-025: Maekar's Forge Tier is "cut into a dormant volcanic ridge".
    - The earlier reconciliation counted the undefined 13-cell `##` strip in column K (rows 01-18,
      passing through Zenith) as "water".
    - Its position and shape fit POL-020's central north-south ridge better. The two readings
      conflict, and the land-share percentages depend on which one is chosen.

11. **"Shattered Kingdoms" names two things.**
    - GEO-002 lists "Shattered Kingdoms (SK)" as one of eleven regions, a frontier region at M16-Q22
      holding the Teeth and the Moonvault.
    - WC-012 and MCD-094 use "Shattered Kingdoms" for the whole bloc of five nations, the Lawless
      Reaches and T.D.K.'s corner.
    - POL-090 has to say "the Shattered Kingdoms frontier region" to tell them apart.

12. **"The Karkosa": capital or ship.** *(pending)*
    - MCD-203: Kanja forged a weapon "at the Karkosa's forge... during an unrelated supply stop" at
      Mao. Also MCD-156, 169, 196-212: "aboard the Karkosa", "the Karkosa's home harbor".
    - Against those, Karkosa is the canon-locked capital (GEO-001/003).

### Scale and capacity tensions (not contradictions, but the current Atlas cannot hold them)

13. **The Sovereign Trust Domain is three cells.**
    - On the Atlas the Domain is G15-H17, about 600 × 400 miles.
    - The corpus puts all of the following in or around it:
      - Karkosa and its nine vertical levels (WC-009)
      - Karkosa's highlands, coastal flats, and financial and medical districts
      - Keldane with its plateau, coast, Hollow, Maw and Reach, about 400 km from the Throat (MAW-121)
      - Stormshelter Cove, the Iron Hold, the Threnn fort and the Still Point
      - the Rookery "on the Trust Domain's own periphery" (MCD-1566)
      - the Sealed Annex
    - It may also have to hold Kesmara, Voskharen, the Korren Highlands and the whole Verehimu realm,
      where the earlier reconciliation proposed placing them.
    - The Verehimu evidence on its own is large:
      - House Renlow and House Ashmere "held adjoining territories some distance north of the Verehimu
        lands" (Ozmund LXXXIV)
      - a retainer's "river town some days south of Karkosa" (Ozmund LXXXVII)
      - Duskmere, "a river town three weeks south by the low roads" (Ozmund V)
    - MCD-147 also refers to "the Sovereign Trust's interior holdings."
    - The ledger's Trust is far larger than the Atlas's TR region.

14. **The Rebellion is fought in Trust-held Jicome.**
    - The Southern Garrison, Southern District Command, the Scrip-Registry and "all ten Jicome
      Scrip-Banking houses" (MCD-240) are Trust institutions inside Jicome. No Atlas layer shows that
      occupation.
    - Daba's own network spans the Trust Domain's periphery (the Rookery), the Rebellion's Jicome
      theater (the Furnace District ridge, MCD-1613; the young Kanja at the Sarrow ore-cut), and,
      through his antagonist Harek Vondel, "the Shattered Kingdoms' rural interior" (CC-147).
    - That is more than 1,400 grid-miles for "the smallest standing force" in the ledger.

15. **Small Portside tensions.**
    - Chronicle VI says Killane is "thirty kilometers inland from the coast". The same Chronicle has
      "three days of overland travel between Killane and the Portside harbor".
    - The canal arc puts "a canal region three weeks' travel south of the five districts"
      (the-copy-that-broke-what-it-borrowed.md). Portside sits at Jicome's southern edge (C09, GEO-006),
      so that region would be offshore unless the canal districts are not at Portside.

16. **Maw numbering ambiguities that a map has to show.**
    - Resolved, but fragile: Maw-15 is both the Prefecture's Drowning Floor (GEO-003 "Praetura/Maw-15")
      and the Southern-network Cascade site ("Maw-15 sat on the Southern Seaboard", withdrawn Chronicle
      IX). MAW-066 resolves this.
    - Not yet determinable: whether the Unarmed Siege of Maw-3 (MCD-247, age 31) is the Grand Circuit
      Belly (K13, Lawless Reaches, "subterranean", MAW-063) or a Southern-network Maw-3.

### Name-collision hazards for the rebuild (no contradiction yet)

- The **Iron- cluster:** Ironhold (Lawless Reaches capital), the Iron Hold (Dravos, TR H16), Ironmere
  (Aethel-Gard), Ironport, Iron Shallows, the Iron-Spire, the Iron-Halls of Velkar and the Black Iron
  Citadel.
- The **Spire cluster:** The Spire (Zenith), the Dark Spire, Ashkeel's High Spire/Obsidian Spires, the
  Iron-Spire and the Spire Causeway.
- The **Thren-/Thresh- cluster:**
  - Threnfall (1804), Threnmoor, Threndale, Threshbend, Threshway and Threll's Watch
  - House Threnn
  - Kares Prime's Threnarr
- The **-Hollow suffix:** Keldane Hollow, Ostrey Hollow, Reth, Voss, Adren's and Corvane Hollows, the
  Vask of the Hollow, Hollowmere Keep and the Hollow Shogunate.
- The **Ash- cluster:** Ash Harbor, Ash-Wharf, the Ash Maw, Ashgate, Ashcoral, Ashfall Fueling
  Station, Ashkeel, the Ashen Channel, the Ashen Vein, House Ashmere and House Ashworth.
- The **Kess- cluster:** Kessic, Kessin Ridge, the Kessarine Pass, Kesmara, and Kess (a person).
- The **Verr- cluster:** Verrow Hold, Verrow Marsh, Verrow's Landing, Verrin, and the old "Varrow".
- **Places and people with the same name:**
  - the capital Kairo and Stormreaver (Kairo)
  - the Upper/Lower Maro rivers and King Maro
  - Skarnhold (an Aethel-Gard Atlas hold) and House Skarne
  - Corren's Ford and Corren Halst
  - Corvain's Rest and Lord Corvain
- **Velkar:** the Atlas hold Velkar (M20) and Lauris's Velkar riverbed, Velkar Mills and Iron-Halls of
  Velkar. This could be a deliberate link. It is not asserted anywhere.

## 4. Unplaced clusters that obviously belong together

Each of these needs one placement decision, not dozens.

### A. Jicome's Southern District and Portside (Rebellion home theater): 30 entries, 951 mentions

- **Portside:** Lower Portside, Dock-Row Six and Four, Piers Nine and Eleven, Crane Six, the Third
  Wharf, Warehouse Twelve, the Ash-Wharf, the Portside Dockmaster's Office.
- **Canal districts:** the Dredge-Line, Marrow Landing, Ferrymouth, Deepcut, Silt Row, the Third Canal
  Bend, Canal House.
- **Kessic:** the Kessic flats, the Kessic Overwatch and the Kessic Wardline (a sub-Atlas wardline).
- **Elsewhere in the district:** the Black Trench, the Scrip-Forge (Forge-7), Iron Shallows, Killane
  (locked at C09), Ghost/Ash Harbor (locked at A09), the Southern Garrison, Southern District Command.
- **Probably here:** the Furnace District.

Hard constraints:
- The Black Trench is "one kilometer through the bedrock south of the Portside manufacturing zone".
- The fleet anchored "two kilometers south of the Ash-Wharf".
- The Ash-Wharf is built on pilings "where the harbor's commercial district met the manufacturing zone".
- Killane is 30 km inland on a volcanic tableland.
- The Dredge-Line flood reached the Kessic flats.

This theater needs a **city plan at kilometer scale**, not a 200-mile cell.

### B. The Trust heartland, Kesmara and the Directorate: 17 + 22 + 5 entries

- **Karkosa:**
  - city levels: the Security Strata, the Granite Megalopolis, the Gear-Forest, L9 (the Silent
    Infinite)
  - districts and buildings: the Throat and its Grand Archive, the financial and medical districts
    (the Anatomy), the highlands (Selenar Archive), the coastal flats (the Iron Hold)
- **Keldane:** the plateau and the Still Point, the coast and the Threnn fort, the Keldane Maw, the
  Hollow and the Reach.
- **Elsewhere in the Domain:** Stormshelter Cove (the Orphan's Harbor, the Breaker's Yard) and the
  Sealed Annex.
- **Kesmara (unplaced):** the orbital descent station, the harbor district, the Eastern District with
  the External Operations Coordination Center, the Eastern Hills, the Continuity Vault, the Compliance
  Exchange, and the Tallow Road ("an hour's ride").
- **Voskharen (unplaced):**
  - coastal records facility
  - an island about 14 km offshore
  - the Wetlands' 22 m tidal channels
  - the Trench, with the Drowning Vault about 1,200 m down
  - the Span over a 200 m gorge
  - the Naval Authority
  - MCD-207 calls Kesmara and Voskharen "regions" with "major coastal cities".
- **The Korren Highlands (unplaced):**
  - eastern foothills
  - "coastal approaches"
  - "high country above" with the Iron-Spire
  - a "frontier holding two days inland"
  - depots "six days" east of a settlement
  - a "southern approach"

### C. The House Verehimu realm (Ozmund): 10 entries

The House realm:
- the Verehimu seat and the estate's lower lake
- the "Verehimu lands", including the "eastern holdings"
- the Verehimu Wetlands: Greyfen, Sennick ("three days upriver from the nearest road"), Lowmere ("a fen
  hamlet east of Greyfen"), and Aldenmoor with its flooded quarry
- Duskmere (three weeks south)
- the House Renlow and Ashmere territories (north)

The corpus also names Houses Dellark, Varnhelt, Skarne, Ashworth and Corvain, with lands left
implicit. This is a **whole noble realm with a crown** (MCD-025: Ozmund "rejects the crown"), and the
Atlas has no polity for it at all.

### D. The Long Mask and Southern Seaboard maritime theater: 42 entries, all unplaced

- **Straits and narrows:** the Gale Straits, the Kothrane Narrows, the Boiling Strait.
- **Battle and engagement sites:** the Salt Keep (with its reef and survivor settlement), Chain Harbor,
  Callow ("forty miles down the coast"), Dead Reckoning's shoals, Gallows Bay, the Meridian Crossing,
  Fort Gallan, the Glass Reef, the Salt Reach.
- **Ports and sea routes:** the Orencliff docks, Ironport, Pier 19, the Sovereign Coast, Vellacourt's
  harbors, the Ghost Fleet's Anchorage, the Sovereign Pier.
- **The Southern Sweep settlements:** Brinewell, Coppermouth, Tideglass, Ashcoral, Windbreak.
- **The Dock-Clearing targets:** the Portside Dockmaster's Office, the Keldane Fish Market, Ashfall,
  Thornwall.
- **Long Mask landmarks:** Saltmarsh, Vastok, the Raptor's Nest, the Breathing Dark, the Gilded
  Lighthouse (the Pi-Awakening site), the Living Gate cavern system.
- **Long Mask networks:** the Overland Connection (400 km), the Independent Port Network (31
  harbors), the Sanctuary Harbors (3).
- **The pirate harbors in the Reaches** (POL-107).

This is the largest cluster of places with no Atlas presence. The Pi-Awakening site in particular
needs a fixed point.

### E. The 1804 network (Daba): 10 entries, all unplaced

- the Rookery (Trust Domain periphery)
- Threnfall (the safehouse)
- Fenmark (salt-flats, with Coen's shop)
- Sabeth's "river towns" to the east, a hundred miles away
- the Sarrow ore-cut and approach ("two ridges past the nearest garrison town")
- the Corrow cut (shared with Bane's Corrow ravine network)
- the Sootgate and Half-Ford depots
- Pallow's Reach
- the Fenwold blocks
- Ashgate
- Mika's coastal house

Unnamed but recurring: the founding cistern, the marsh camps, and the hill country. The doctrine
(MCD-1569) forbids a center, so the Atlas should show a **diffuse overlay**, not pins. It does need
anchor regions.

### F. Lauris's Directorate operations and present-day sites: 16 entries, all unplaced

- Velaris and Brokenwall (cities with central plazas)
- Settlement K-447
- the Vask of the Hollow (a 14 km subterranean gallery)
- the Iron-Spire
- the Black Choir substation at Velkar Mills
- the Velkar riverbed
- the Iron-Halls of Velkar ("river settlements")
- Voren
- the Salt-Locked Archive
- the Drowning Vault
- the Far Trench
- Site K-Theta (about 8 km², partly subterranean) and its relocated cave system
- the Coastal Containment Office
- the Cairnholt Intake (a hillside quarry-cut block)

Most of these sit along the Korren and Voskharen arcs.

### G. Rebellion field theater (alias one-offs): 47 entries, all unplaced

- **Fortified points:** Threshbend, Threshway, Threnmoor, Threll's Watch, Duren Watch, Coalfell,
  Hallmere, Marrenfeld Keep, Hollowmere Keep, Dessin Hold, Verrow Hold, Reth Hollow, Voss Hollow,
  Kessin Ridge, Fort Tidewall, the Old Foundry.
- **Settlements:** Karrow's Bend, Threndale, Kettren, Adren's Hollow, Corvane Hollow, Corvain's Rest,
  Coalgate, Warrow Bend, Halworth Reach, Marrow's Edge, the Merrow Compact.
- **Crossings and routes:** Drennock Bridge, Sennow Crossing, the Kelder Ford, Corren's Ford, Serrin's
  Cut, Ferrow Cut, the Kessarine Pass, the Orphan and Caravan Roads, the Voss Corridor, Bridge Eleven.
- **Flats, marsh and water edges:** the Amitane flats, the Undertide flats, the Underlow culvert, the
  Verrin crossing, Verrow Marsh, Verrow's Landing, Vell's Landing, Fenrow Landing.
- **Other:** the Free Quarter (40,000 people), Brinemoor (deliberately unplaced).

Almost none of these carry a direction. They need a **theater box**, meaning the Trust-occupied
interior of Jicome and the marches, rather than pins.

### H. Cult, deep-history and Book-era sites: 9 entries, plus Ashkeel's 8 tiers

- the Domus Inviolate's seven villages (the Prefecture's eastern high borderland)
- the Weighing Communities' borderland (needs a ruling on conflict 3)
- the Anchor Stones
- the Measurist site in the Shogunate interior
- the Deposition Vault (Old Dominion Ruins)
- the Broken Meridian
- the Book 5 western shore (the Tide Line)
- the Demaron site
- the Free State (Fermand's origin)
- Ashkeel, offshore near the Lawless Reaches, with its eight vertical tiers

## 5. Recommendations for the rebuilt Atlas

1. **Settle the world frame first.**
   - Decide whether MCD-142's "four continents" stands.
   - If it does, the overview grows from one continent to a world sheet: three further landmasses plus
     the "Foreign Sea" nation, even if they are left as blank coasts.
   - If it does not, amend MCD-142.
   - Also rule on the Living Drakma range (conflict 2). It decides which landmasses get deposits.

2. **Use a tiered scale instead of one grid.**
   - **Tier 0, world sheet.** Continents, oceans, the Great Sea and the Foreign Sea.
   - **Tier 1, continental overview.** Keep the 200-mile cell grid, but trim the 342 empty `~~` cells.
     Expand it eastward or southward if the continents get placed.
   - **Tier 2, theater insets at 10-20 mile cells**, one each for the five dense theaters:
     - Jicome's Southern District
     - the Trust heartland (Karkosa-Keldane-Kesmara-Voskharen-Korren and the Verehimu lands)
     - the Southern Seaboard sea lanes
     - the 1804 hinterland
     - the Lawless Reaches' pirate coast
   - **Tier 3, plans:**
     - Portside at kilometer scale
     - Karkosa, with its L1-L9 vertical section
     - Ashkeel's vertical section from +12,600 to -75,000 ft
     - the Throat
   - The corpus's distances (1 km, 2 km, 14 km, 30 km, 400 km, 800 km, "three weeks") mostly live
     below the 200-mile cell. That is why a single grid has failed.

3. **Grow the Sovereign Trust.**
   - Three cells cannot hold the corpus's Trust.
   - Either enlarge the TR region substantially (12-20 cells, with Kesmara, Voskharen, Korren and the
     Verehimu realm inside), or add a separate **"Trust sphere" political overlay** that covers TR,
     occupied southern Jicome, and the Old Dominion Ruins. The second option also answers the
     MCD-094 percentages.

4. **Add these regions and sub-regions, which the corpus implies but the Atlas lacks:**
   - Jicome's Southern District (Trust-garrisoned) and the Mar archipelago (MCD-110 has no cells for
     it)
   - the Kesmara and Voskharen provinces and the Korren Highlands
   - the Verehimu realm and its neighbor Houses
   - the Southern Seaboard, as a named sea and coast theater with its own Southern Maw network
     (MAW-066)
   - named RA (Rathaan) and UK sub-areas in the Lawless Reaches (OPEN-012)
   - the Domus Inviolate highlands
   - an Old Dominion **historical overlay** showing ruins across all five nations, the Ash Maw capital,
     and the Broken Meridian's subterranean extent
   - T.D.K.'s dead ground
   - the Book 5 western shore

5. **Define the undefined grid codes.**
   - `##` (column K): decide between ridge and water. POL-020 points to the central volcanic ridge.
   - Name RA and UK.
   - Define the orphan codes NP and AS.
   - Rename the "Shattered Kingdoms" frontier region, for example "the Frontier" or "the Moonvault
     Marches", so the name stops doing two jobs.

6. **Reconcile adjacency before drawing.**
   - The Shogunate and the Archipelago are adjacent in CULT-011 and CULT-086 but far apart on the
     Atlas. One side has to change.
   - Fix MAW-078's travel times and GEO-007's "thousand miles".

7. **Reuse the 78 unused Atlas slots before inventing new cells.**
   - GEO-005's 52 free-to-rename holds and settlements are almost never used.
   - Several fit unplaced corpus places directly:
     - Velkar (M20) for Lauris's Velkar sites
     - the Jicome ports Sulvane and Cindreth for the Southern Seaboard harbors
     - Cressel, the Lawless Reaches' Free-town, for a pirate harbor
     - Brenwell (a waystation) for the Painter's waystation
     - the Old Dominion salvage camp Vaelreld for the Null-Walkers' circuit
   - These are suggestions only.

8. **Data model for the rebuild.** Give every place:
   - an ID
   - a parent
   - a scale tier
   - a cell, plus a sub-cell where needed
   - a placement confidence: locked, derived from claims, or placeholder
   - era of existence and renames (Ash Harbor becomes Ghost Harbor; Callow, formerly Varrow; the Free
     Quarter burned and rebuilt; Kesmara, formerly the source's "Jicome")
   - the rule IDs that constrain it
   - `mainline-gazetteer.json` already carries parent, region, claims and sources and can seed this.

9. **Don't name what the tracks keep unnamed.**
   - 907 of 1,442 mainline Chronicles name no place. The alias tracks deliberately use "the
     settlement" and "the garrison".
   - The Atlas should give those tracks reusable anchor districts, with no obligation to name every
     setting.
   - The collision clusters in §3 suggest new coinages should avoid the Iron-, Ash-, Thren-, Kess-,
     Verr- and -Hollow stems.

10. **Rulings this rebuild depends on.** The open items from the earlier reconciliation and this
    census, in suggested order:
    - four continents
    - Living Drakma range
    - the Trust's size and the Verehimu placement
    - Kesmara and Voskharen placement
    - the Southern Seaboard definition
    - the `##` strip
    - Shogunate-Archipelago adjacency
    - the Karkosa ship rename
    - MAW-078
    - the regional-share percentages
    - Old Dominion chronology
