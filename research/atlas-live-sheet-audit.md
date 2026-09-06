# Live Regional Atlas Audit — vs. locked GEO- rules

Pure fact-finding. Nothing below is a proposed canon edit; it is a catalog of what the live
Google Sheet ("The Lords_of_Cian_Regional_Atlas") actually contains as of this session, and where
it agrees or disagrees with the currently-locked `GEO-001` through `GEO-005` rules in
`canon-ledger.json`. No new GEO- rules are drafted here — that comes after Abad reviews this.

**Source of the live text**: the full sheet was fetched this session to
`/root/.claude/projects/-home-user-Lords-of-Cian-Knowledge-Core/195feb94-2811-5ec6-b57d-6031cdaf1569/tool-results/mcp-Google_Drive-read_file_content-1788708556644.txt`
(117,461-character `{fileContent: string}` JSON blob, extracted with `jq`/`python3`/grep). The
export is a flat sequence of markdown tables with no sheet-name headers or tab-index markers —
tab identity below is inferred from content structure and the "0 - Overview" / "3 - Jicome" style
numbering Abad's own prompt used as an example, not read directly from spreadsheet metadata. That
inference is noted wherever it matters; everything else (grid contents, tables, prose) is quoted
or transcribed directly from the fetched text.

---

## 1. Full tab list

Content-block order in the export, with inferred tab numbering (unverified against actual Sheets
tab indices — the export carries no tab-name metadata):

| # (inferred) | Tab | What it holds |
|---|---|---|
| 0 | Overview | Whole-continent 20×30 grid (columns A-T, rows 01-30), 200-mile master cells |
| 1 | Holdfast Classes | 23-row fortification-type legend (Code/Class/Tier/What it is) |
| 2 | How to use | Title block, legend (box colors, line colors), and the "NAMES" canon-lock note |
| 3 | Jicome (JI) | Region detail grid + CANON SITES / HOLDS / SETTLEMENTS / ROADS & RIVERS |
| 4 | Aethel-Gard (AG) | same structure |
| 5 | Zenith (ZN) | same structure |
| 6 | The Prefecture (PR) | same structure |
| 7 | The Shogunate (SH) | same structure |
| 8 | Astral Archipelago (AA) | same structure |
| 9 | Old Dominion Ruins (OD) | same structure |
| 10 | Sovereign Trust Domain (TR) | same structure |
| 11 | Lawless Reaches (LR) | same structure |
| 12 | Shattered Kingdoms (SK) | same structure |
| 13 | T.D.K. Peninsula (DK) | same structure |
| 14 | Gazetteer | Flat master index, 70 rows: Place / Region / Cell / Type / Class / Tier |

That's **15 tabs**, 11 of them region detail tabs — one per `GEO-002` region, in the same order
`GEO-002` lists them, so region-tab *count and coverage* match `GEO-002` cleanly. (Region tab
order in the export is Jicome, Aethel-Gard, Zenith, The Prefecture, The Shogunate, Astral
Archipelago, Old Dominion Ruins, Sovereign Trust Domain, Lawless Reaches, Shattered Kingdoms,
T.D.K. Peninsula — identical order to `GEO-002`'s statement.)

---

## 2. Whole-world overview grid — every code, and how much space it occupies

Grid is 20 columns (A-T) × 30 rows (01-30) = 600 cells. Non-empty/coded cells, by code
(count = number of master cells):

| Code | Count | Notes |
|---|---|---|
| `~~` | 342 | blank/unclaimed filler — not a region code |
| SK | 54 | Shattered Kingdoms |
| LR | 50 | Lawless Reaches |
| OD | 36 | Old Dominion Ruins |
| JI | 23 | Jicome |
| `##` | 13 | all in column K, rows 01-18 (with gaps at site-code cells) — undefined symbol, see §7 |
| **RA** | **10** | rows 19-21, cols H/I/K/L — **not one of the 11 GEO-002 codes** |
| AG | 9 | Aethel-Gard |
| SH | 9 | The Shogunate |
| ZN | 9 | Zenith |
| PR | 8 | The Prefecture |
| AA | 7 | Astral Archipelago |
| **UK** | **5** | rows 10-12, cols D/E — **not one of the 11 GEO-002 codes** |
| TR | 3 | Sovereign Trust Domain |
| DK | 3 | T.D.K. Peninsula |
| IR, RX, NP, KR, SP, IH, BE, PA, DR, KA, TE, SL, AS, MV, SC, RP, MO, SV, DS | 1 each | single-cell overlays marking a named site's exact master cell (see §7 for the two, NP and AS, that don't correspond to any named site anywhere in the document) |

All 11 `GEO-002` region codes (JI, AG, ZN, PR, SH, AA, OD, TR, LR, SK, DK) are present in the
grid — confirmed, none missing.

---

## 3. Codes in the live grid NOT in GEO-002's 11-region list

- **`RA`** — 10 master cells (H19, I19, K19, H20, I20, K20, L20, I21, J21, K21), clustered tightly
  around Rathaan Prime (J20) and Ash Maw Scar (J19), both of which the Gazetteer files under
  **Lawless Reaches**. `RA` is never defined in the Holdfast Classes tab, the How-to-use legend,
  any region tab's own CANON SITES/HOLDS/SETTLEMENTS list, or the Gazetteer. Most likely reading:
  an unlabeled sub-district of Lawless Reaches (a "Rathaan" territory) that never got folded into
  the `GEO-002` 11-region list or given its own tab — but that's an inference, not something the
  document states outright.
- **`UK`** — 5 master cells (D10, E10, D11, D12, E12), bordering Lawless Reaches' northwest edge.
  Lawless Reaches' own ROADS & RIVERS table names a road "**UK Spur**" leading in that direction,
  which suggests `UK` denotes an "Unknown/Uncharted" zone rather than a named region — but again,
  nowhere in the fetched text is `UK` actually spelled out or defined.
- **`##`** — 13 cells, all in column K rows 01-18, forming a broken vertical strip between the
  Jicome/Aethel-Gard block (west) and the Old Dominion Ruins block (east). Never defined in any
  legend. Plausibly represents a strait/sea-lane (possibly the canon-locked "the Throat," see §7),
  but nothing in the document actually says so.

All 11 `GEO-002` codes are confirmed present (see §2), so nothing is missing from the grid on that
front — the mismatch is purely that the grid contains **more** than 11 codes, and three of them
(`RA`, `UK`, `##`) are structurally significant (18 cells combined, more space than TR or DK get)
without any backing definition anywhere in the fetched document.

---

## 4. Region-by-region canon Capital/Maw sites vs. GEO-003

`GEO-003` (locked): *"Rexhaven, Ironmere, The Spire, Praetura/Maw-15, Kairo, Skyvault, Khorvane,
Karkosa/Maw-7 Slab, Frontier Maw/Moonvault, Dark Spire."* — 10 named items, one per region, for
10 of the 11 `GEO-002` regions.

Live-sheet CANON SITES per region (from each region tab's own side panel, cross-checked against
the Gazetteer's `Capital/Maw` rows):

| Region | GEO-003 says | Live sheet actually has | Match? |
|---|---|---|---|
| Jicome (JI) | Rexhaven | RX — Rexhaven, B05, Crownhold (L) | Match |
| Aethel-Gard (AG) | Ironmere | IR — Ironmere, G03, Wallcrown City (L) | Match |
| Zenith (ZN) | The Spire | SP — The Spire, K10, Crownhold (L) | Match |
| The Prefecture (PR) | Praetura/Maw-15 | PA — Praetura, C15, Crownhold (L); DR — Maw-15 Drowning, B16, Maw/venue | Match |
| The Shogunate (SH) | Kairo | KR — Kairo, R07, Corehold (L) | Match |
| Astral Archipelago (AA) | Skyvault | SV — Skyvault, K27, Wallcrown City (L) | Match |
| **Old Dominion Ruins (OD)** | **Khorvane** | **CANON SITES table is empty.** Khorvane appears only under HOLDS (KH, N05, Crownhold/L, tier M — a plain Hold, not flagged Capital/Maw). Gazetteer lists Khorvane's Type as `Hold`, not `Capital/Maw`. | **MISMATCH** |
| Sovereign Trust Domain (TR) | Karkosa/Maw-7 Slab | KA — Karkosa, G16, Wallcrown City (L); SL — Maw-7 Slab, G17, Maw/venue | Match |
| **Lawless Reaches (LR)** | *(no entry in GEO-003 at all)* | **5 Capital/Maw sites**: IH — Ironhold, E11, Spurstar Fort (L); RP — Rathaan Prime, J20, Thornwork (S); plus three Maw-class venues — SC (Ash Maw Scar, J19), MO (Maw-1 Mother, H22), BE (Maw-3 Belly, K13) | **MISSING FROM GEO-003 ENTIRELY** |
| Shattered Kingdoms (SK) | Frontier Maw/Moonvault | TE — Frontier Maw, N16, Corehold (L); MV — Moonvault, O18, Delvework (L) | Match |
| T.D.K. Peninsula (DK) | Dark Spire | DS — Dark Spire, S29, Corehold (L) | Match |

**Two real mismatches**, both significant:

1. **Old Dominion Ruins has no canon capital in the live sheet.** `GEO-003` names Khorvane as
   OD's capital, but the live sheet demotes Khorvane to an ordinary Hold (Crownhold/L) and leaves
   OD's CANON SITES section blank — both in OD's own tab and on the master overview grid (no
   site-code overlay anywhere in OD's 36 master cells).
2. **Lawless Reaches is entirely absent from `GEO-003`.** The rule lists exactly 10 items for 11
   regions, skipping straight from Sovereign Trust Domain to Shattered Kingdoms. The live sheet
   gives LR its own real capital, **Ironhold** (Spurstar Fort, L-tier, E11) — distinct from
   Aethel-Gard's similarly-named **Ironmere** — plus four Maw-class venues, the most of any single
   region in the sheet.

One naming note, not a mismatch: **Ironhold** (Lawless Reaches' capital) and **Ironmere**
(Aethel-Gard's capital) are one letter apart — worth flagging for anyone drafting off memory
rather than the sheet.

---

## 5. "How to use" tab — full text, verbatim

> MY RIVAL'S DISTANCE - THE LORDS OF CIAN
> Continental Atlas - Definitive Edition
>
> Tab 0 is the whole continent. Holdfast Classes lists every fortification type. Gazetteer indexes
> every named place.
> Region tabs zoom each 200-mile master cell into finer sub-cells, with heavy lines marking the
> master boundaries.
>
> LEGEND
> Black box = capital or Maw (canon). Steel box = hold (its class shown in the side panel). Orange
> = settlement.
> Brown line = road. Blue line = river or sea-lane. Dark stone line = a wardline (frontier wall of
> mile-forts).
>
> NAMES
> Canon names (Karkosa, Moonvault, the Maws, the Throat, the Teeth) are locked. Settlement and
> hold names are original coinages with no real-world tie. Each hold is classed by the Codex of
> Holdfasts. Move or rename anything freely.

This matches `GEO-001` word-for-word on the canon-locked name list (Karkosa, Moonvault, the Maws,
the Throat, the Teeth). See §7 for the fact that "the Throat" and "the Teeth" don't actually
appear anywhere else in the fetched document — no map cell, no Gazetteer row, no region-tab
mention.

The Overview tab's own sub-header (from §1/§2) adds one more piece of legend text not in the
"How to use" block above: *"Each cell = 200 x 200 miles. Region tabs carry renamed settlements,
holds, roads, rivers and fortifications. See Holdfast Classes and Gazetteer tabs."*

### Holdfast Classes (full 23-row table)

| Code | Class | Tier | What it is |
|---|---|---|---|
| LH | Loophold | S - Tactical | Slit-tower |
| CW | Crouchwork | S - Tactical | Sunk nest |
| DT | Drumtower | S - Tactical | Coast drum |
| WT | Wardtower | S - Tactical | Watch-house |
| SB | Skywarden Block | S - Tactical | Sky-block |
| DV | Delvework | S - Tactical | Underhold |
| TW | Thornwork | S - Tactical | Field-star |
| BW | Breakwork | S - Tactical | Split-box |
| SW | Sweepway | S - Tactical | Ditch-gallery |
| MH | Moundhold | M - Seat | Mound-and-yard |
| RK | Ringkeep | M - Seat | Ring-crown |
| TH | Twinward Hold | M - Seat | Hold-in-hold |
| QH | Quadrangle Hold | M - Seat | Square-and-towers |
| HF | Hallfast | M - Seat | Fortified hall |
| CT | Charterwall Town | M - Seat | Charter-walled town |
| CF | Courtfast | M - Seat | Court-palace |
| CH | Crownhold | M - Seat | Seat-citadel |
| SF | Spurstar Fort | L - Regional | Bastion-star |
| CO | Corehold | L - Regional | Last-keep |
| AF | Anglehold Fort | L - Regional | Long-wall fort |
| WC | Wallcrown City | L - Regional | Ringed city |
| DC | Double Cordon | L - Regional | Siege-rings |
| WL | Wardline | L - Regional | Frontier line |

(This table matches the "Codex of Holdfasts" naming taxonomy already locked at `HLD-001`/`010`-`021` — not independently re-checked cell-by-cell against those rules here, since that wasn't in scope, but no contradiction was noticed in passing.)

---

## 6. Every named Hold and Settlement, by region

Compiled from each region tab's own side panel (CANON SITES / HOLDS / SETTLEMENTS / ROADS &
RIVERS), cross-checked against the Gazetteer's matching rows — the two sources agree everywhere
except where §4 already flags a mismatch (Khorvane/OD).

### Jicome (JI) — master cells A01-C09
- **Capital/Maw**: Rexhaven (B05, Crownhold L)
- **Holds**: Emberward (C06, Ringkeep M), Vethkar (B01, Drumtower S), Straithe (C03, Wardtower S)
- **Settlements**: Sulvane (A05, Port), Cindreth (A08, Port), Orrum (C04, Mine-town), Vaelkarn (B08, Town)
- **Roads/Rivers**: West Harbor Road, Ore Road, South Ridge Road; Maofall Stream (water)

### Aethel-Gard (AG) — master cells E01-G05 (approx.)
- **Capital/Maw**: Ironmere (G03, Wallcrown City L)
- **Holds**: Skarnhold (F01, Twinward Hold M), Orvane (G02, Wardtower S)
- **Settlements**: Saelmere (E02, Port), Haeldrun (F04, Town)
- **Roads/Rivers**: Coast Road, Highland Road; Fjordmelt (water)

### Zenith (ZN) — master cells I09-L11 (approx.)
- **Capital/Maw**: The Spire (K10, Crownhold L)
- **Holds**: Vorngate (J11, Wardtower S), Cauldraeth (K11, Delvework S)
- **Settlements**: Auvelle (I10, Town), Sennrime (L10, Camp)
- **Roads/Rivers**: West Gondola Line, East Gondola Line; Glacier Run (water)

### The Prefecture (PR) — master cells A13-C16 (approx.)
- **Capital/Maw**: Praetura (C15, Crownhold L); Maw-15 Drowning (B16, Maw/venue)
- **Holds**: Veduun (C14, Quadrangle Hold M), Vanegate (A13, Drumtower S), Aubry Ward (B13, Breakwork S)
- **Settlements**: Vance (A14, Port), Aubrymead (B13, Town), Tessold (B15, Town)
- **Wardline**: The March (border, Wardline L)
- **Roads/Rivers**: West Artery, North Artery, East Artery, South Artery; Upper Maro, Lower Maro (water)

### The Shogunate (SH) — master cells R05-T08 (approx.)
- **Capital/Maw**: Kairo (R07, Corehold L)
- **Holds**: Reefward (R05, Drumtower S), Lornspire (T06, Wardtower S)
- **Settlements**: Veskport (R06, Port), Sorrel (S05, Isle-town), Skelvane (T07, Forge-isle)
- **Roads/Rivers**: Deepport Lane, North Reef Lane, Forge Lane (all water/sea-lane)

### Astral Archipelago (AA) — master cells I26-L28 (approx.)
- **Capital/Maw**: Skyvault (K27, Wallcrown City L)
- **Holds**: The Skywarden (J28, Skywarden Block S)
- **Settlements**: Aurspan (J27, Bridge-town), Aurae (I26, High-isle), Solmere (K28, Landing-port)
- **Roads/Rivers**: Aerie Span, Landing Span (roads)

### Old Dominion Ruins (OD) — master cells M03-O09 (approx.)
- **Capital/Maw**: *none* (see §4 mismatch)
- **Holds**: Khorvane (N05, Crownhold L), Vael Gorr (O03, Quadrangle Hold M), Gorrhal (N09, Wardtower S)
- **Settlements**: Vaelreld (M04, Salvage-camp), Greld (N07, Market)
- **Roads/Rivers**: Ruined Way (N), Ruined Way (S) (roads); The Grey Channel (water)

### Sovereign Trust Domain (TR) — master cells G15-H17 (approx.)
- **Capital/Maw**: Karkosa (G16, Wallcrown City L); Maw-7 Slab (G17, Maw/venue)
- **Holds**: The Iron Hold (H16, Corehold L)
- **Settlements**: Stormshelter Cove (G15, Port), Keldane Hollow (G17, The Pit)
- **Roads/Rivers**: Slab Road, Cove Road; Keldane Water

### Lawless Reaches (LR) — master cells D09-K22 (approx., largest region tab)
- **Capital/Maw**: Ironhold (E11, Spurstar Fort L), Rathaan Prime (J20, Thornwork S), Ash Maw Scar (J19, Maw/venue), Maw-1 Mother (H22, Maw/venue), Maw-3 Belly (K13, Maw/venue)
- **Holds**: Rysgate (D11, Breakwork S), Vaelthorn (H14, Quadrangle Hold M)
- **Settlements**: Cressel (F13, Free-town), Duskvane (I20, Trade-town), Brenwell (G09, Waystation), Tannvane (F16, Crossroads)
- **Roads/Rivers**: Reaches Track, "UK Spur" (see §3/§7), Rathaan Circuit, South Track (roads); Reaches River
- Also lists (in its own CANON SITES panel only — cross-references, see §7) The Spire and Karkosa, both belonging to other regions

### Shattered Kingdoms (SK) — master cells M16-Q22 (approx.)
- **Capital/Maw**: Frontier Maw (N16, Corehold L); Moonvault (O18, Delvework L)
- **Holds**: Khaelward (Q22, Wardtower S), Velkar (M20, Quadrangle Hold M)
- **Settlements**: Sevrin (M17, Frontier-outpost), Caldrath (P18, Nomad-camp), Velmoura (N18, Approach-camp)
- **Roads/Rivers**: The Deep Road, Frontier Track (roads); The Ashen Channel

### T.D.K. Peninsula (DK) — master cells S26-S29 (approx.)
- **Capital/Maw**: Dark Spire (S29, Corehold L)
- **Holds**: Gorthal (S27, Breakwork S), Vornhael (S28, Wardtower S)
- **Settlements**: Sevmoor (S26, Last-camp)
- **Roads/Rivers**: The Spire Causeway (road); Ashen Vein (water)

**Gazetteer totals** (master index, 70 rows): 17 Capital/Maw, 23 Hold, 29 Settlement, 1 Wardline.
Holds + Settlements = **52**, not "roughly 40" as `GEO-005` currently estimates — see §7/Summary.

---

## 7. Internal inconsistencies / leftover artifacts found in the live sheet itself

1. **Lawless Reaches' own CANON SITES panel cross-lists sites that belong to other regions, and
   mislabels their class when it does.** LR's side panel includes `SP — The Spire, K10, Maw /
   venue` and `KA — Karkosa, G16, Maw / venue` (plus `SL — Maw-7 Slab, G17, Maw / venue`, which is
   at least classed correctly). But The Spire's *own* tab (Zenith) classes it `Crownhold (L)`, and
   Karkosa's *own* tab (Sovereign Trust Domain) classes it `Wallcrown City (L)` — real
   architectural capital classes, not "Maw / venue." The Gazetteer agrees with the home-region
   tabs, not with LR's cross-listing. This looks like a copy/paste artifact in LR's panel rather
   than a deliberate "these are visible from Lawless Reaches too" note, since the class label is
   simply wrong for two of the three borrowed entries.

2. **Two orphan overlay codes on the master grid, defined nowhere**: `NP` at K07 and `AS` at K17.
   Every other single-occurrence overlay code on the Overview grid matches a named site in some
   region tab's CANON SITES table (RX=Rexhaven, IR=Ironmere, SP=The Spire, KR=Kairo, PA=Praetura,
   DR=Maw-15 Drowning, KA=Karkosa, SL=Maw-7 Slab, IH=Ironhold, RP=Rathaan Prime, SC=Ash Maw Scar,
   MO=Maw-1 Mother, BE=Maw-3 Belly, TE=Frontier Maw, MV=Moonvault, SV=Skyvault, DS=Dark Spire).
   `NP` and `AS` don't match anything — no region tab, no Gazetteer row, no legend entry.

3. **`RA` (10 cells) and `UK` (5 cells) are large, structurally real areas on the Overview grid
   with no defining tab or legend entry anywhere** (detailed in §3). `RA` in particular occupies
   more grid space than the entire Sovereign Trust Domain or T.D.K. Peninsula regions get, which
   makes it hard to read as a minor leftover — it reads like a genuine sub-area that never got
   written up.

4. **The `##` column-K strip (13 cells) is likewise undefined.** No legend entry (the "How to
   use" LEGEND section only defines Capital/Maw, Hold, Settlement, Road, River/sea-lane, and
   Coast — no symbol for `##` or `~~`). Its shape (a near-continuous vertical line separating the
   Jicome/Aethel-Gard cluster from Old Dominion Ruins) is consistent with a strait/sea-lane, and
   the canon-locked term "the Throat" is a plausible candidate, but the document never actually
   says so.

5. **"The Throat" and "the Teeth"** — both named as canon-locked in the How-to-use NAMES note
   (and in locked `GEO-001`) — **do not appear anywhere else in the fetched document.** No map
   cell, no Gazetteer entry, no region-tab mention under either name. Either they're represented
   by an unlabeled symbol (candidate: the `##` strip above) or they simply aren't placed on this
   version of the map yet.

6. **Old Dominion Ruins has an empty CANON SITES section** with a header row and no data row under
   it (confirmed at the raw-table level, not just absence from the summary) — this is the same
   shape of gap as the `GEO-003` mismatch in §4, just described here as a sheet-level artifact
   rather than a ledger-comparison.

7. No `TODO`/`TBD`/`draft`/placeholder text strings were found anywhere in the fetched content —
   the sheet reads as deliberately filled in everywhere except the OD capital gap and the
   undefined-code cells above.

---

## Summary of what needs correcting

Concrete, confirmed mismatches only — no speculation, no proposed fixes:

1. **`GEO-003` is missing Lawless Reaches entirely.** The rule lists 10 capital sites for 11
   regions; Lawless Reaches has no entry. The live sheet gives it a real capital (**Ironhold**,
   Spurstar Fort L-tier, cell E11) plus four Maw-class venues (Rathaan Prime, Ash Maw Scar,
   Maw-1 Mother, Maw-3 Belly) — more named capital/Maw sites than any other single region.

2. **`GEO-003`'s Khorvane entry for Old Dominion Ruins doesn't match the live sheet.** The live
   sheet has no capital/Maw site for Old Dominion Ruins at all — its CANON SITES table is empty,
   and Khorvane is filed only as a plain Hold (Crownhold, tier M), not as the region's capital.

3. **`GEO-005`'s "roughly 40 additional Holds and Settlements" undercounts the live sheet.** The
   Gazetteer's actual Hold + Settlement total is **52** (23 Holds + 29 Settlements), plus one
   Wardline (The March) that GEO-005's framing doesn't account for as a category at all.

4. **The live sheet itself carries unresolved internal issues** that any Atlas redo will need to
   ask Abad about before they can be turned into canon text: two undefined orphan site-codes
   (`NP` at K07, `AS` at K17), two sizeable undefined area-codes (`RA`, 10 cells; `UK`, 5 cells),
   an undefined `##` symbol (13 cells, column K), and a Lawless Reaches CANON SITES panel that
   cross-lists two other regions' capitals under the wrong class ("Maw / venue" for what are
   actually Crownhold/Wallcrown City sites elsewhere in the same document).

5. **"The Throat" and "the Teeth"** are canon-locked by name (`GEO-001`, matching the live sheet's
   own legend) but have no located, labeled placement anywhere in the fetched document — worth a
   direct question to Abad (or a fresh look at the live Sheet in its native UI, which may carry
   cell coloring/shape information the text export can't capture) before the Atlas redo asserts
   anything about where they are.

Everything else checked — all 11 `GEO-002` region codes and names, 8 of 10 `GEO-003` capital
entries, the `GEO-001` canon-name list, the Holdfast Classes taxonomy, and every region tab's
Hold/Settlement/Road/River roster against the Gazetteer — came back internally consistent, with no
further contradictions found.
