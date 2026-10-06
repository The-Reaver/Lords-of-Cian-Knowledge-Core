"""Batch 378: the Long Mask, the Sovereign Pier Accords and Book 1 on one clock (Abad's ruling,
2026-10-05; resolves approval-list item 1). Locks MCD-1901 (the timeline), MCD-1902 (the Accords broken
and the Trinity reclaimed, a Book 1 beat), MCD-1903 (the aging misconception), MCD-1904 (the Pi-Awakening's
trigger, the Last Breakfast and "one day too late"), MCD-1905 (the honor of the cook), MCD-1906 (the order
chain behind the regicide and the strike) and MCD-1907 (the second attempt); amends every rule that
states the old 284-year Long Mask or the 296-year Pier-to-Ceremony offset; carries the change to every
entry, profile, tracker row and doc that states it, and appends the Batch 378 history paragraph to
CLAUDE.md.
Usage: python3 merge_batch378_pact_long_mask_timeline.py <draft.md> "<approval quote>"
"""
import json
import re
import sys
from collections import Counter

LEDGER = "canon-ledger.json"
SOURCE = "Abad's ruling in conversation, 2026-10-05; drafted to resolve approval-list item 1"
NEW_IDS = ["MCD-1901", "MCD-1902", "MCD-1903", "MCD-1904", "MCD-1905", "MCD-1906", "MCD-1907"]
CH = "docs/lords-of-cian/chronicles/"
PR = "docs/lords-of-cian/character-profiles/"
LM = "the Long Mask of just over 283 years"

# ---------------------------------------------------------------------------------------------
# (b) Ledger rule amendments: (rule id, exact old substring, new substring). Each old substring
# must occur exactly once in the rule's statement.
# ---------------------------------------------------------------------------------------------
BOILER = ("despite this Chronicle's placement well within the 284-year Long Mask era",
          "despite this Chronicle's placement well within the Long Mask era of just over 283 years")
AMEND = [
    ("MCD-091", "The Fulfillment Ceremony is separate from the Sovereign Pier Accords, roughly 296 years apart.",
     "The Fulfillment Ceremony is separate from the Sovereign Pier Accords: the Accords were concluded at "
     "the Sovereign Pier just over 283 years before the Ceremony, and the murders there broke them (MCD-1901)."),
    ("ARS-010", "for roughly 296 years -- the full 284-year Long Mask and beyond (MCD-091) --",
     "for just over 283 years -- the whole Long Mask and on to the Karkosa Heist (MCD-1901) --"),
    ("ARS-310", "Kanja maintained the Scourge persona for 284 years using",
     "Through the Long Mask of just over 283 years (MCD-1901) Kanja maintained the Scourge persona, born at "
     "Ash-Wharf at age 22 (MCD-235) and set down on the coat night (MCD-1022), using"),
    ("CC-005", "Kanja's Long Mask persona lasted 284 years, ending when the Gravity-Fetter pendant was severed at "
               "the Gilded Lighthouse, triggering the Pi-Awakening.",
     "Kanja's Long Mask lasted just over 283 years, ending when the Gravity-Fetter pendant was severed at the "
     "Gilded Lighthouse on the sixth day after his 314th birthday, triggering the Pi-Awakening (MCD-1901). The Scourge persona "
     "itself is set down by his own choice on the coat night (MCD-1022), in the last month before the "
     "Fulfillment Ceremony."),
    ("CC-012", "for the entire 284-year Long Mask period.",
     "for the entire Long Mask period of just over 283 years (MCD-1901)."),
    ("MCD-236", "part of his later 284-year Long Mask theatrical disguise system.",
     "part of his later theatrical disguise system for " + LM + "."),
    ("MCD-245", "beginning the already-locked 284-year Long Mask.",
     "beginning the already-locked Long Mask of just over 283 years (MCD-1901)."),
    ("MCD-246", "The 284-year Long Mask persona that followed comprised",
     "The Long Mask that followed, lasting just over 283 years (MCD-1901), comprised"),
    ("ARS-346", "developed over the Long Mask's 284 years",
     "developed over " + LM),
    ("ARS-353", "deployed eleven times across 284 years,",
     "deployed eleven times across " + LM + ","),
    ("POL-107", "for the full 284 years,",
     "for the full Long Mask, just over 283 years,"),
    ("ARS-425", "the full 284-year Long Mask --",
     "the full Long Mask of just over 283 years --"),
    ("ARS-437", "it holds for the entire 284-year Long Mask.",
     "it holds for the entire Long Mask of just over 283 years (MCD-1901)."),
    ("ARS-437", "Onyx reads 284 years out of his body",
     "Onyx reads just over 283 years out of his body"),
    ("MCD-272", "The Eve of Awakening (age 314) --",
     "The Eve of Awakening (age 314, the day before the Pi-Awakening, MCD-1901) --"),
    ("MCD-1022", "Age 314, V4 gear, the final year of the 284-year Long Mask.",
     "Age 313, in the last month before the Fulfillment Ceremony (MCD-1901), V4 gear, in the last year of "
     + LM + "."),
    ("MCD-1022", "ending the span by conscious choice, deliberately left open for future material.",
     "ending the Scourge persona by conscious choice, deliberately left open for future material; the Long "
     "Mask itself ends later, at the pendant's severing on the sixth day after his 314th birthday (CC-005, "
     "MCD-1901)."),
    ("MCD-1252", "building toward the Long Mask's established close (MCD-1022, age 314)",
     "building toward the Scourge persona's established close (MCD-1022, age 313)"),
    ("MCD-1255", "Age 313, V4 gear, one year before the Long Mask's already-locked close (MCD-1022, age 314).",
     "Age 312, in the last three weeks of that age (MCD-1901), V4 gear, one year before the Scourge "
     "persona's already-locked close (MCD-1022, age 313)."),
    ("MCD-1408", "Age 314, the eve of the persona's already-locked final mission",
     "Age 313, in the last month before the Fulfillment Ceremony (MCD-1901), the eve of the persona's "
     "already-locked final mission"),
    ("MCD-1477", "(`MCD-1022`, age 314)", "(`MCD-1022`, age 313)"),
    ("MCD-1235", "deployed eleven times across 284 years,",
     "deployed eleven times across " + LM + ","),
    ("MCD-1484", "decades into the 284-year Long Mask,", "decades into " + LM + ","),
    ("ARS-348", "V4 (ages 180-284)", "V4 (ages 180-313, until the coat comes off, MCD-1022)"),
    ("MCD-1076", "locks V4 at ages 180-284, which age 235 falls within",
     "locks V4 at ages 180-313, which age 235 falls within"),
    ("MCD-1322", "(ages 33-284)", "(ages 33-314)"),
    ("CC-101", "Pyro, roughly 24-36 at Book 1, is younger",
     "Pyro, 23 at the Fulfillment Ceremony (MCD-270, MCD-1901), is younger"),
    ("CC-110", "for 24 years", "for 23 years"),
    ("WC-022", "Book 1 The Deposed King (murder investigation -> 10-Day Interregnum -> Pi-Awakening -> Great Breach "
               "epilogue)",
     "Book 1 The Deposed King (murder investigation -> 10-Day Interregnum, which opens on the day after the "
     "murder, his 314th birthday, and within which fall his deathbed days and the Pi-Awakening on the sixth day after "
     "that birthday, the seventh day of the Interregnum (MCD-1901) -> Great Breach epilogue)"),
]
for rid in ["MCD-589", "MCD-984", "MCD-1053", "MCD-1058", "MCD-1091", "MCD-1338", "MCD-1367", "MCD-1374",
            "MCD-1381", "MCD-1386", "MCD-1419", "MCD-1506", "MCD-1510", "MCD-1511", "MCD-1515", "MCD-1518",
            "MCD-1521"]:
    AMEND.append((rid,) + BOILER)
# Correction notes appended to rules whose entries' counts or placements change in this batch.
APPEND = {
    # Change to Book 1's structure; awaiting Abad's confirmation (see the draft head).
    "MCD-070": " The Investigation opens at the murder and runs on through the Interregnum, which opens the next "
               "day (MCD-1901); the acts are narrative movements and overlap in time.",
    "MCD-1883": " Corrected Batch 378, 2026-10-05: the Dark Ledger count recomputed from the Pier's date "
                "(MCD-1901), 791,942,400 to 762,998,400 seconds (24 years and 71 days); the age and the moment "
                "within it are unchanged.",
    "MCD-1884": " Corrected Batch 378, 2026-10-05: the Dark Ledger count recomputed from the Pier's date "
                "(MCD-1901), 584,928,000 to 555,984,000 seconds (17 years and 230 days), and 'eighteen years of "
                "count' to 'seventeen'; the age and the moment within it are unchanged.",
    "MCD-1885": " Corrected Batch 378, 2026-10-05: the Dark Ledger count recomputed from the Pier's date "
                "(MCD-1901), 6,632,323,200 to 6,603,379,200 seconds (209 years and 143 days), and 'two hundred "
                "and ten years' to 'two hundred and nine'; the age and the moment within it are unchanged. Also cut from the "
                "narration (Abad, 2026-10-05, 'yes'): the sentences that named the Talisman as the cause of the "
                "decline; the cut keeps the decline's cause out of pre-Book-1 material (MCD-1903).",
    "MCD-277": " Batch 378 note: the Last Breakfast is the meal during which the Pi-Awakening's trigger strikes "
               "(MCD-1904). It is held at the Gilded Lighthouse, in the upper room where Kanja lies, and is the first "
               "ceremonial breakfast since Maro's murder, with Pyro serving Kanja as the cook (MCD-1905). The "
               "Countdown Annotation (age 310) was written by Sephtis, who stays silent about what it means "
               "(MCD-1903).",
    "MCD-1406": " Corrected Batch 378, 2026-10-05: set in the first three weeks of age 313 (MCD-1901); Garren "
                "Hask's ledger span corrected from 'past two hundred and eighty-three years' to 'past two "
                "hundred and eighty-two'.",
    "MCD-1407": " Placed Batch 378, 2026-10-05: in the last month of age 313, after the Pier's 283rd "
                "anniversary and before 'The Night Before the Last Coat' (MCD-1901).",
    "MCD-1246": " Placed Batch 378, 2026-10-05 (MCD-1901): in the last 30 days of age 290, after the Pier's 260th "
                "anniversary, so the entry's stated span of two hundred and sixty years holds exactly.",
    "MCD-1252": " Placed Batch 378, 2026-10-05 (MCD-1901): in the last 30 days of age 308, after the Pier's 278th "
                "anniversary, so the entry's stated span of two hundred and seventy-eight years holds exactly.",
    "MCD-1253": " Placed Batch 378, 2026-10-05 (MCD-1901): in the last 30 days of age 310, after the Pier's 280th "
                "anniversary, so the entry's stated span of two hundred and eighty years holds exactly.",
}

# ---------------------------------------------------------------------------------------------
# (c) File edits: (path, region, exact old, new, expected count). Region: P narrative prose,
# H header note, N continuity note, D doc.
# ---------------------------------------------------------------------------------------------
V4 = [CH + f for f in [
    "kanja-chronicle-vii-the-man-who-did-not-get-up.md", "senas-own-student.md",
    "the-blade-she-almost-didnt-sheathe.md", "the-charge-she-measured-twice.md",
    "the-coat-he-almost-didnt-put-back-on.md", "the-coat-that-went-back-to-ash-wharf.md",
    "the-duel-he-didnt-need-onyx-for.md", "the-fever-that-outran-the-rescue.md",
    "the-first-night-in-the-new-coat.md", "the-fleet-that-wasnt-his-to-command.md",
    "the-forge-that-bought-its-own-freedom.md", "the-glass-reef.md", "the-grandson-who-came-to-warn-him.md",
    "the-half-second-the-blade-bought.md", "the-last-depot-on-the-old-charts.md",
    "the-names-the-ledger-kept-track-of.md", "the-night-before-the-last-coat.md",
    "the-one-who-chose-to-leave.md", "the-ones-who-sold-him-out.md", "the-pocket-he-almost-opened.md",
    "the-rival-who-called-him-a-setback.md", "the-ruling-that-changed-nothing.md",
    "the-smoke-that-spoke-first.md", "the-successors-first-command-alone.md",
    "the-window-that-wouldnt-come-twice.md", "what-efa-gol-never-asked-twice.md",
    "what-the-successor-chose-to-keep.md"]]
BOILER_FILES = [CH + f for f in [
    "the-apprentices-first-fleet.md", "the-boarding-in-the-blind-dark.md", "the-break-in-the-floe.md",
    "the-calm-bought-for-a-handshake.md", "the-fleet-that-went-blind-together.md",
    "the-night-they-came-for-the-school.md", "the-order-he-didnt-question.md",
    "the-silence-with-no-wind-in-it.md", "the-storm-they-read-backward.md", "the-storm-they-read-too-late.md",
    "the-truce-they-wouldnt-honor.md", "the-window-that-ended-the-smuggling.md", "what-held-the-causeway.md",
    "what-the-ash-choked-off.md"]]

EDITS = []
for p in V4:
    EDITS.append((p, "N", "180-284", "180-313", 1))
for p in BOILER_FILES:
    EDITS.append((p, "H", "well within the 284-year Long Mask era", "well within the Long Mask era of just over 283 years", 1))
K5 = CH + "kanja-chronicle-v-the-names-in-the-correction-book.md"
K6 = CH + "kanja-chronicle-vi-vellacourts-rule.md"
K7 = CH + "kanja-chronicle-vii-the-man-who-did-not-get-up.md"
C1255 = CH + "the-coat-he-almost-didnt-put-back-on.md"
C1406 = CH + "the-window-that-wouldnt-come-twice.md"
C1408 = CH + "the-night-before-the-last-coat.md"
C1022 = CH + "the-last-coat-he-ever-wore.md"
EDITS += [
    # --- narrative prose ---
    (K5, "P", "Dark Ledger. 791,942,400 seconds.\n", "Dark Ledger. 762,998,400 seconds.\n", 1),
    (K5, "P", "Dark Ledger. 791,942,400 seconds. Reconciled.", "Dark Ledger. 762,998,400 seconds. Reconciled.", 1),
    (K6, "P", "Dark Ledger. 584,928,000 seconds.", "Dark Ledger. 555,984,000 seconds.", 1),
    (K6, "P", "Eighteen years of count stand behind it.", "Seventeen years of count stand behind it.", 1),
    (K6, "P", "Five hundred eighty-four million, nine hundred twenty-eight thousand seconds. One kill jolt.",
     "Five hundred fifty-five million, nine hundred eighty-four thousand seconds. One kill jolt.", 1),
    (K7, "P", "Dark Ledger. 6,632,323,200 seconds.", "Dark Ledger. 6,603,379,200 seconds.", 1),
    (K7, "P", "Two hundred and ten years of dark by then.", "Two hundred and nine years of dark by then.", 1),
    (K7, "P", "The weight grows in him a little more each year. The long Rexmar span spends slowly. The Talisman spends "
     "him another way and presses him down into his own bones. Year by year.",
     "The weight grows in him a little more each year. Year by year.", 1),
    (C1255, "P", "that two hundred and eighty-three years under this name might",
     "that two hundred and eighty-two years behind this mask might", 1),
    (C1255, "P", "for two\nhundred and eighty-three years running.", "for two\nhundred and eighty-two years running.", 1),
    (C1255, "P", "whether two hundred and\neighty-three years was enough", "whether two hundred and\neighty-two years was enough", 1),
    (C1406, "P", "now ran past two hundred and eighty-three years", "now ran past two hundred and eighty-two years", 1),
    (C1022, "P", "\"Two hundred and eighty-four years,\" he said. \"That's how long the Long Mask has run, since a morning\n"
     "on a burned wharf set its shape \u2014 not planned, not chosen, just the thing it became.\"",
     "\"Two hundred and eighty-three years,\" he said. \"That's how long the mask has run since the pier. A\n"
     "morning on a burned wharf set its shape.\"", 1),
    # --- header notes ---
    (K7, "H", "Age 240, two hundred and ten years past the Sovereign Pier.",
     "Age 240, two hundred and nine years past the Sovereign Pier.", 1),
    (C1255, "H", "Age 313, V4 gear, one year before the Long Mask's established close.",
     "Age 312, V4 gear, one year before the persona's established close.", 1),
    (C1408, "H", "Age 314, the eve of the persona's already-locked final mission.",
     "Age 313, the eve of the persona's already-locked final mission.", 1),
    (CH + "the-pass-above-the-orphan-road.md", "H", "deep in the 284-year Long Mask", "deep in " + LM, 1),
    (CH + "the-first-watch-under-the-new-chair.md", "H", "during the Trinity's 284-year sealing",
     "during the Trinity's sealing of just over 283 years", 1),
    (CH + "what-they-tried-to-erase-from-the-wall.md", "H", "for the entire 284-year Long Mask era",
     "for the entire Long Mask era of just over 283 years", 1),
    (CH + "what-they-wouldnt-let-him-take.md", "H", "Set during the 284-year Long Mask era",
     "Set during the Long Mask era of just over 283 years", 1),
    (CH + "the-first-coin-they-took-from-the-trust.md", "H", "for the entire 284-year Long Mask era",
     "for the entire Long Mask era of just over 283 years", 1),
    (CH + "the-first-job-that-wasnt-the-war.md", "H", "for the entire 284-year Long Mask",
     "for the entire " + LM[4:], 1),
    (CH + "what-the-golden-terror-left-behind.md", "H", "for the full 284-year Long Mask period",
     "for the full Long Mask period of just over 283 years", 1),
    (CH + "the-grandchildren-of-the-freed.md", "H", "generations into the persona's 284-year span",
     "generations into the Long Mask's span of just over 283 years", 1),
    (CH + "the-boy-who-didnt-know-his-name.md", "H", "generations into the persona's 284-year span",
     "generations into the Long Mask's span of just over 283 years", 1),
    (CH + "the-watch-callum-breck-called.md", "H", "for the era's full 284 years",
     "for the era's full span of just over 283 years", 1),
    (CH + "what-burned-loud-enough-to-hear.md", "H", "decades into the 284-year Long Mask", "decades into " + LM, 1),
    (CH + "what-the-coat-couldnt-shed.md", "H", "(ages 33-284)", "(ages 33-314)", 1),
    (CH + "what-the-smoke-said.md", "H", "Long Mask, ages 33-284 --", "Long Mask, ages 33-314 --", 1),
    # --- continuity notes ---
    (K5, "N", "exact seconds-count 791,942,400 (twenty-five years and forty-one days past the\nSovereign Pier treaty",
     "exact seconds-count 762,998,400 (twenty-four years and seventy-one days past the\nSovereign Pier treaty", 1),
    (K6, "N", "states eighteen years of count with no kill jolt", "states seventeen years of count with no kill jolt", 1),
    (K6, "N", "584,928,000 seconds from the Sovereign Pier treaty", "555,984,000 seconds from the Sovereign Pier treaty", 1),
    (K7, "N", "exact count 6,632,323,200 seconds", "exact count 6,603,379,200 seconds", 1),
    (CH + "kanja-chronicle-iv-ninety-seconds-on-the-sovereign-pier.md", "N",
     "the 284-vs-296-year interval question (open) is not touched.",
     "the Pier-to-Ceremony interval (just over 283 years, `MCD-1901`) is not touched.", 1),
    (CH + "the-boy-who-didnt-know-his-name.md", "N", "across the Long Mask's\n284-year span,",
     "across the Long Mask's\nspan of just over 283 years,", 1),
    (CH + "the-watch-callum-breck-called.md", "N", "sealed away for the entire 284 years per",
     "sealed away for the entire span of just over 283 years per", 1),
    (CH + "what-burned-loud-enough-to-hear.md", "N", "deep in the 284-year Long Mask.", "deep in " + LM + ".", 1),
    (CH + "the-first-quiet-performance.md", "N", "the already-locked\n284-year sustained-persona framework",
     "the already-locked\nsustained-persona framework of just over 283 years", 1),
    (CH + "the-half-second-the-blade-bought.md", "N", "\"deployed eleven times across\n284 years, saving",
     "\"deployed eleven times across\nthe Long Mask of just over 283 years, saving", 1),
    (CH + "the-last-names-before-the-silence.md", "N", "Long Mask's established close (`MCD-1022`, age 314)",
     "Scourge persona's established close (`MCD-1022`, age 313)", 1),
    (CH + "the-last-depot-on-the-old-charts.md", "N", "own end (`MCD-1022`, age 314)", "own end (`MCD-1022`, age 313)", 1),
    (CH + "the-coat-that-went-back-to-ash-wharf.md", "N", "persona (`MCD-1022`, age 314)", "persona (`MCD-1022`, age 313)", 1),
    (CH + "the-ones-who-sold-him-out.md", "N", "age 314, and its immediate approach", "age 313, and its immediate approach", 1),
    (C1255, "N", "final mission (\"The Last Coat He Ever Wore,\" `MCD-1022`, age 314)",
     "final mission (\"The Last Coat He Ever Wore,\" `MCD-1022`, age 313)", 1),
    (C1255, "N", "No new named characters. Age 313,\nV4 gear", "No new named characters. Age 312,\nV4 gear", 1),
    (C1406, "N", "(\"The Coat He\nAlmost Didn't Put Back On,\" `MCD-1255`, age 313)",
     "(\"The Coat He\nAlmost Didn't Put Back On,\" `MCD-1255`, age 312)", 1),
    (C1408, "N", "(`MCD-1022`,\nage 314, the persona's literal final mission and the Long Mask's already-locked close)",
     "(`MCD-1022`,\nage 313, the persona's literal final mission, weeks before the Long Mask's close at the pendant, `CC-005`)", 1),
    (C1408, "N", "(`MCD-1255`, age 313)", "(`MCD-1255`, age 312)", 1),
    (C1408, "N", "Age 314, V4 gear", "Age 313, V4 gear", 1),
    (C1022, "N", "Deliberately states only that the 284-year span (MCD-246, ARS-310) has run its course",
     "Deliberately states only that the Long Mask's span of just over 283 years (MCD-246, ARS-310, MCD-1901) has run its course", 1),
    (C1022, "N", "chooses to end it consciously rather than let it drift",
     "chooses to end the Scourge persona consciously rather than let it drift", 1),
]
NOTE_APPEND = {
    K5: " Corrected Batch 378, 2026-10-05: the Dark Ledger count recomputed from the Pier's date, 30 days "
        "before Kanja's 31st birthday (`MCD-1901`); the age and the moment within it are unchanged.",
    K6: " Corrected Batch 378, 2026-10-05: the Dark Ledger count and the years of count recomputed from the "
        "Pier's date, 30 days before Kanja's 31st birthday (`MCD-1901`); the age and the moment within it are "
        "unchanged.",
    K7: " Corrected Batch 378, 2026-10-05: the Dark Ledger count and the years past the Pier recomputed from "
        "the Pier's date, 30 days before Kanja's 31st birthday (`MCD-1901`); the age and the moment within it "
        "are unchanged. The two sentences that named the Talisman as the cause of the weight are cut from the "
        "narration (Abad, 2026-10-05, 'yes'); the decline's cause stays out of pre-Book-1 material (`MCD-1903`).",
    C1255: " Corrected Batch 378, 2026-10-05: re-dated to age 312, in the last three weeks of that age after "
           "the Pier's 282nd anniversary (`MCD-1901`), so the chosen year ends at the coat night before the "
           "Fulfillment Ceremony; the three in-prose counts move from two hundred and eighty-three to two "
           "hundred and eighty-two years, matching the Pier date exactly.",
    C1406: " Corrected Batch 378, 2026-10-05: set in the first three weeks of age 313, three weeks after "
           "`MCD-1255` (`MCD-1901`); Garren Hask's ledger span moves from past two hundred and eighty-three to "
           "past two hundred and eighty-two years, matching the Pier date exactly.",
    CH + "what-efa-gol-never-asked-twice.md":
        " Placed Batch 378, 2026-10-05 (MCD-1901): in the last 30 days of age 290, after the Pier's 260th "
        "anniversary, so the entry's two-hundred-and-sixty-year span holds exactly.",
    CH + "the-last-names-before-the-silence.md":
        " Placed Batch 378, 2026-10-05 (MCD-1901): in the last 30 days of age 308, after the Pier's 278th "
        "anniversary, so the entry's two hundred and seventy-eight years of keeping the ledger hold exactly.",
    CH + "the-last-depot-on-the-old-charts.md":
        " Placed Batch 378, 2026-10-05 (MCD-1901): in the last 30 days of age 310, after the Pier's 280th "
        "anniversary, so Garren Hask's two hundred and eighty years hold exactly.",
    CH + "the-names-the-ledger-kept-track-of.md":
        " Placed Batch 378, 2026-10-05: in the last month of age 313, after the Pier's 283rd anniversary, "
        "where Hask's two hundred and eighty-three years are exact (`MCD-1901`).",
    C1408: " Corrected Batch 378, 2026-10-05: set at age 313, in the last month before the Fulfillment "
           "Ceremony (`MCD-1901`).",
    C1022: " Corrected Batch 378, 2026-10-05: set at age 313, in the last month before the Fulfillment "
           "Ceremony (`MCD-1901`), so Kanja's spoken count moves from two hundred and eighty-four to two "
           "hundred and eighty-three years. The coat night ends the Scourge persona by his choice; the Long "
           "Mask itself ends later, at the pendant's severing on the sixth day after his 314th birthday "
           "(`CC-005`, `MCD-1901`).",
}

BRACKET = ("[Added Batch 378 (`MCD-070` amended): the Investigation opens at the murder and runs on through the "
           "Interregnum, which opens the next day (`MCD-1901`); the acts are narrative movements and overlap in time.]")
AL = "docs/lords-of-cian/approval-list-2026-10-03.md"
ITEM1_OLD = """**1. Book 1's offset from the Sovereign Pier: 284 or 296 years?**
- **Recommend 284, so Kanja is 314 at Book 1.** 296 is arithmetically impossible: it would put the
  Fulfillment Ceremony after the Pi-Awakening, which `CC-006` sets at age 314 and `WC-022` places
  inside Book 1.
- Ten or more rules already assume 284: `CC-005`, `ARS-437` ("Onyx reads 284 years"), `MCD-269`,
  `CC-110`, `MCD-214`, `MCD-226`, `MCD-305`, `MCD-260`, and Maw Era IV.
- The Batch 56 ruling that `MCD-091` controls rested on a mistaken belief that the 284 years were a
  different interval from the Long Mask. This item reverses that ruling.
- Scope: `MCD-091`, `ARS-010`, and `CC-101` ("24-36" becomes "24"), plus seven docs.
- Alternative: none that holds together.
"""
ITEM1_NEW = """**1. Book 1's offset from the Sovereign Pier. RESOLVED, Batch 378 (`MCD-1901`).**
- Abad, 2026-10-05: "Kanja is 313 years old when his father dies." The murder falls on the last day
  of his age 313. The Pi-Awakening stays at age 314 (`CC-006`) and comes after his 314th birthday: "the
  Long mask has to be after his 314th birthday." The Long Mask runs from the Sovereign Pier to the
  pendant's severing at the Awakening: "The Long Mask lasts just over 283 years." The Accords are
  broken by the murder, a week earlier.
- This supersedes the Batch 56 ruling that `MCD-091`'s 296 controls. Every rule, entry and doc
  that stated 284 or 296 is listed in Batch 378's note.
"""
EDITS += [
    (AL, "D", ITEM1_OLD, ITEM1_NEW, 1),
    (AL, "D", """- **Hask's death moves to late in Kanja's 313th year.** The rules that move are `MCD-1422` (death),""",
     """- **Hask's death moves to the last month of Kanja's age 313: after `MCD-1408`, where he is alive, and
  before the Fulfillment Ceremony on the last day of that age (`MCD-1901`).** The rules that move are `MCD-1422` (death),""", 1),
    (AL, "D", """- Alternative: he dies the morning after the last coat. That needs no Scourge edits, but it lands in
  Book 1's own year.""",
     """- Alternative: he dies the morning after the last coat (`MCD-1022`). That needs no Scourge edits. Under
  Batch 378 the coat night falls in the same last month, before the Ceremony, so this too lands before
  Book 1.""", 1),
    (AL, "D", "- **Recommend about 309, five years younger than Kanja.** This follows from item 1.",
     "- **Recommend about 308, five years younger than Kanja.** This follows from item 1: Kanja is 313 at\n"
     "  the Fulfillment Ceremony (`MCD-1901`).", 1),
    (AL, "D", "24 years of knowing Pyro's father (`CC-110`).", "23 years of knowing Pyro's father (`CC-110`).", 1),
    ("docs/lords-of-cian/chronicle-tracks-status.md", "D",
     "age at Book 1 depends on the 284/296 ruling",
     "23 at the Fulfillment Ceremony (born in Kanja's age 290; Kanja is 313 then, Batch 378, `MCD-1901`)", 1),
    ("docs/lords-of-cian/kanja-chronicles-production-roadmap.md", "D",
     "negotiated in secret roughly 296 years before Book 1 opens",
     "negotiated in secret and concluded at the Sovereign Pier just over 283 years before Book 1 opens", 1),
    ("docs/lords-of-cian/kanja-chronicles-production-roadmap.md", "D",
     "fulfilling the Accords 284 years after Kanja put on the mask",
     "fulfilling the Accords just over 283 years after Kanja put on the mask", 1),
    ("docs/lords-of-cian/kanja-chronicles-production-roadmap.md", "D",
     "it ended one day too late.\"\n",
     "it ended one day too late.\"\n  [Corrected Batch 378: the quoted pitch line is kept as source wording. The Long Mask runs "
     "just over 283 years, from the Sovereign Pier to the pendant's severing on the sixth day after Kanja's 314th "
     "birthday, seven days after his father's murder (`MCD-1901`). What the line means is set at `MCD-1904`.]\n", 1),
    (PR + "kanja-haku-rexmar.md", "D", "The 284-year Long\n  Mask that follows comprises",
     "The Long Mask that\n  follows, lasting just over 283 years (`MCD-1901`), comprises", 1),
    (PR + "kanja-haku-rexmar.md", "D", "The Long Mask persona runs 284 years, ending when the Gravity-Fetter pendant",
     "The Long Mask runs just over 283 years (`MCD-1901`), ending when the Gravity-Fetter pendant", 1),
    (PR + "kanja-haku-rexmar.md", "D", "  birthdays (\"Day 0\" = age 314).\n",
     "  birthdays (\"Day 0\" = age 314, the Pi-Awakening itself; it falls on the sixth day after his 314th\n"
     "  birthday, `MCD-1901`).\n", 1),
    (PR + "kanja-haku-rexmar.md", "D", "for the entire 284-year Long\n  Mask that follows.",
     "for the entire Long Mask\n  of just over 283 years that follows.", 1),
    (PR + "kanja-haku-rexmar.md", "D", "everything in this walkthrough (ages 18–314) sits *before* it.",
     "everything in this walkthrough (ages 18–313) sits *before* it, except the Eve of Awakening, the Last "
     "Breakfast and the Pi-Awakening (age 314), which fall inside Book 1's window (`MCD-1901`).", 1),
    (PR + "kanja-haku-rexmar.md", "D", "it is the seed of a future Book-1-era or post-Fulfillment-Ceremony psychological profile.\n",
     "it is the seed of a future Book-1-era or post-Fulfillment-Ceremony psychological profile. Its Book 1\n"
     "  consequence is locked at `MCD-1902`: the Accords broken, and the Trinity reclaimed at the Karkosa Heist.\n", 1),
    (PR + "kanja-haku-rexmar.md", "D", "unable to stand unaided on bad days by 300 (`MCD-260`/`262`/`271`).\n",
     "unable to stand unaided on bad days by 300 (`MCD-260`/`262`/`271`). The cause is the Governor's\n"
     "  Shackle, which Kanja and the crew read as age (`MCD-1903`); no entry confirms that he is aging out.\n", 1),
    (PR + "kanja-haku-rexmar.md", "D", "plus the Eve of Awakening/Pi-Awakening at 314\n  (`MCD-272`, `MCD-1022`),",
     "plus the coat night (age 313, `MCD-1022`), the Eve of\n  Awakening (age 314, after the murder, `MCD-272`) and the Pi-Awakening (age 314, the sixth day after his\n  birthday, `MCD-1901`),", 1),
    (PR + "alias-captain.md", "D", "Kanja's Long Mask persona begins and runs 284 years, ending",
     "Kanja's Long Mask begins and runs just over 283 years (`MCD-1901`), ending", 1),
    (PR + "alias-captain.md", "D", "Machete for the 284-year Long Mask that followed.",
     "Machete for the Long Mask that followed, just over 283 years.", 1),
    (PR + "alias-captain.md", "D", "sealed at L9 for the entire 284-year Long Mask, ages 30-314)",
     "sealed at L9 for the entire Long Mask of just over 283 years, ages 30-314)", 1),
    (PR + "alias-captain.md", "D", "284-year Long Mask (ages 30-314) that begins",
     "Long Mask of just over 283 years (ages 30-314) that begins", 1),
    (PR + "alias-crow-king.md", "D", "across the entire 284-year Long Mask (ages 30–314).",
     "across the entire Long Mask of just over 283 years (ages 30–314).", 1),
    (PR + "alias-crow-king.md", "D", "stays sealed throughout the entire 284-year Long Mask (per",
     "stays sealed throughout the entire Long Mask of just over 283 years (per", 1),
    (PR + "alias-crow-king.md", "D", "**the Scourge's** 284-year Long Mask persona",
     "**the Scourge's** Long Mask persona of just over 283 years", 1),
    (PR + "alias-blue-collar-titan.md", "D", "the 284-year Long Mask that follows runs",
     "the Long Mask that follows, just over 283 years, runs", 1),
    (PR + "alias-sovereign-ghost.md", "D", "during the subsequent 284-year Long Mask,",
     "during the subsequent Long Mask of just over 283 years,", 1),
    (PR + "daba.md", "D", "(which itself spans 284 years\n  per `MCD-246`)",
     "(which itself spans just over 283\n  years per `MCD-246`, `MCD-1901`)", 1),
    (PR + "ezio-valcari.md", "D",
     "double regicide, hired by Ozmund. Three acts: Investigation → 10-Day Interregnum → Karkosa Heist.\n",
     "double regicide, hired by Ozmund. Three acts: Investigation → 10-Day Interregnum → Karkosa Heist.\n"
     "  " + BRACKET + "\n", 1),
    (PR + "kanja-haku-rexmar.md", "D", "dormancy ending. This is the hard chronological wall",
     "dormancy ending. " + BRACKET + " This is the hard chronological wall", 1),
    ("docs/lords-of-cian/kanja-chronicles-production-roadmap.md", "D", "epilogue (The Great Breach, SBD uncovered).",
     "epilogue (The Great Breach, SBD uncovered). " + BRACKET, 1),
    ("docs/lords-of-cian/master-to-do-list.md", "D", "early in the 10-Day Interregnum.",
     "early in the 10-Day Interregnum. [Batch 378 note: the Pi-Awakening falls on the sixth day after his 314th "
     "birthday (confirmed by Abad); with the Interregnum opening on that birthday (confirmed by Abad, "
     "`MCD-1901`), that is the seventh day of the Interregnum.]", 1),
    ("docs/lords-of-cian/master-to-do-list.md", "D", "rather than rebuilding it from scratch.\n",
     "rather than rebuilding it from scratch. [Batch 378: 'one day too late' is the enemy's belief about the "
     "Pi-Awakening (MCD-1904); it does not describe the timing of the murder.]\n", 1),
    ("docs/lords-of-cian/kanja-chronicles-production-roadmap.md", "D", "including future chronicle drafts.\n",
     "including future chronicle drafts. [Batch 378: 'one day too late' is the enemy's belief about the "
     "Pi-Awakening (MCD-1904); it does not describe the timing of the murder.]\n", 1),
    (PR + "anirak.md", "D",
     "The launch wave ends with the Long Mask at Kanja 314 (`MCD-1022`), so the Scourge\n"
     "    persona governs every entry. Whether any gap lies between the Long Mask's end and the\n"
     "    Fulfillment Ceremony is the open 284-versus-296 question on the approval list. The launch wave stays strictly",
     "The launch wave ends before the Fulfillment Ceremony (the last day of Kanja's age\n"
     "    313, `MCD-1901`), so the Scourge persona governs every entry until the coat comes off (`MCD-1022`,\n"
     "    Kanja 313). The Long Mask itself ends seven days after the Ceremony, at the pendant's severing on the\n"
     "    sixth day after his 314th birthday (`CC-005`, `MCD-1901`). The launch wave stays strictly", 1),
    (PR + "anirak.md", "D", "- Era: late Long Mask, by Kanja 314, within the last ~29 years before Book 1.",
     "- Era: late Long Mask, by Kanja 313, within the last ~29 years before Book 1.", 1),
]


def clean(t):
    t = re.sub(r"-\n\s*", "-", t)
    return re.sub(r"\s+", " ", t.replace("`", "").replace("**", "")).strip()


def parse_new(text):
    out = {}
    for m in re.finditer(r"\*\*(MCD-190[1-7])\*\*\s*\(category: ([^)]+)\)\.\s*(.+?)(?=\n\n)", text, re.S):
        out[m.group(1)] = (m.group(2).strip(), clean(m.group(3)))
    assert sorted(out) == NEW_IDS, sorted(out)
    return out


def wrap_onto(body, clause, width=100):
    """Wrap an appended clause so it continues the note's last line at the file's own width."""
    col = len(body) - body.rfind("\n") - 1
    out, line = "", ""
    for w in clause.split():
        if col + len(line) + 1 + len(w) > width and (line or col):
            out += line + "\n"
            col, line = 0, w
        else:
            line = (line + " " + w) if line else (" " + w if col else w)
    return out + line


def apply_file_edits():
    texts = {}
    for path, _region, old, new, n in EDITS:
        if path not in texts:
            texts[path] = open(path, encoding="utf-8").read()
        c = texts[path].count(old)
        assert c == n, (path, old[:80], c)
        texts[path] = texts[path].replace(old, new)
    for path, clause in NOTE_APPEND.items():
        t = texts.get(path) or open(path, encoding="utf-8").read()
        body = t.rstrip("\n")
        assert body.endswith("*") and "Batch 378" not in body[-len(clause) - 50:], path
        texts[path] = body[:-1] + wrap_onto(body[:-1], clause) + "*\n"
    for path, t in texts.items():
        open(path, "w", encoding="utf-8").write(t)
    return sorted(texts)


def main():
    draft, approval = sys.argv[1], sys.argv[2]
    new = parse_new(open(draft, encoding="utf-8").read())
    d = json.load(open(LEDGER, encoding="utf-8"))
    byid = {r["id"]: r for r in d["rules"]}
    assert not set(NEW_IDS) & set(byid), "ID collision"
    amended = set()
    for rid, old, newtxt in AMEND:
        s = byid[rid]["statement"]
        assert s.count(old) == 1, (rid, old[:80], s.count(old))
        byid[rid]["statement"] = s.replace(old, newtxt)
        amended.add(rid)
    for rid, clause in APPEND.items():
        assert "Batch 378" not in byid[rid]["statement"], rid
        byid[rid]["statement"] += clause
        amended.add(rid)
    for rid in NEW_IDS:
        cat, st = new[rid]
        d["rules"].append({"id": rid, "category": cat, "statement": st, "status": "locked", "source": SOURCE})
    files = apply_file_edits()
    d["batches_completed"].append({
        "batch": 378, "source": SOURCE, "rules_affected": len(NEW_IDS) + len(amended),
        "note": ("The Long Mask, the Sovereign Pier Accords and Book 1 on one clock (resolves approval-list item 1; "
                 "supersedes the Batch 56 ruling that MCD-091's 296 controls). Abad, 2026-10-05: 'Kanja is 313 years "
                 "old when his father dies'; 'The Pact was broken that day... so it really lasted 283 years'; 'Yes the "
                 "long mask ends there'; 'The Long Mask lasts just over 283 years'; 'the Long mask has to be after his "
                 "314th birthday'; 'shortly after his birthday he starts feeling worse and worse it seems he's on his "
                 "death bed and then that's when it happens'; 'yes Macana is Obsidian Malice, six days works'; 'yes the Pier is 30 days "
                 "before his 31st birthday'; 'the interregnum day 1 counting works'; 'The pie Awakening gave him confidence and he knew "
                 "something changed he knew that his feeling that he was getting old was a misconception', and on the Awakening's trigger: "
                 "'the trigger is the danger', 'it was something that was bound to happen' (full quotation in the draft). "
                 "Abad's answers of 2026-10-05: on the murder falling on the last day of age 313, 'yes'; on cutting from Kanja VII the "
                 "sentences that name the Talisman as the cause of his decline, 'yes'; on the attack, 'Yes. this is also a ceremonial "
                 "breakfast that he had with Kanja & Maro at the same time every time they did have breakfast together.'; on where the Last Breakfast is held, 'the last breakfast can take place in the most logical place that makes sense for the story cuz it doesn't have to take place where it always takes place could be a reason any reason could be pyrule doesn't want to have breakfast there because of the memories it could be anything it could be because of the lack of movement that Kanja has'; on who shares it, 'the breakfast is Father and Son and they do not tell pyro why he always joins we can make up some sort of excuse like the cook is very coveted in their culture so it's easy to make them to cook and it's easy for them to be so warm towards the cook and loving towards the cook and have to cook close at heart because they feed a nourish everyone so that's a good way for them to have an excuse to always eat with him it's too honor to cook and that's the excuse that you have to spend time with him.'; on "
                 "Sephtis putting the decline together and staying silent, and having written the Countdown Annotation, 'yes'; on "
                 "Lauris knowing Kanja's mother through Sephtis, 'yes'; on the enemy and the 314 threshold, 'the enemy does not know "
                 "they just want to eliminate him from the picture because they know he is next of kin and would seek revenge' and "
                 "'similar to Haku except he literally had the means to do it and the Weaponry to do it'; his correction, "
                 "'he did bring it to his needs but didn't finish it' ('needs' is dictation for 'knees'); and on Lauris, 'Lauris should "
                 "obviously be able to send his density or sense that he's family somehow she is an extraordinary character so that "
                 "is something that I think should be evident to her but she can't put everything else together. if she knows who his "
                 "mother is through Sephtis, then she would obviously know that he could potentially be dense'. Abad's answers of 2026-10-05/06 on the orders, the breakfast, Sephtis, the cook's culture and Maro, verbatim (the 'I' in 'I savage team' reads 'a'): 'option 1 proxy, the Three Ronin, Book 4 works.\n\nwe need a second attempt\n\nThe Quiet Hand (SBD-059). A standing SEALBLACK cell kept for politically sensitive individual targets.\n\npaired with\n\nI savage team of animals and 1 Brute Beast Master.\n\nKanja, Pyro & The Triad UNLEASHED.\n\nThe Rexmar Lineage honors the cook.\n\nMaro knows'; and on when the second attempt comes, 2026-10-06, 'the second attacks have come at some point after the first not to long after the first as they think they regrouped and figured out how to attack them which turns out disastrous for the attackers.'; and on the placement, 2026-10-06, 'after the Karkosa Heist, with the Trinity.' MCD-1901 locks the clock: the murder on the last day of "
                 "Kanja's age 313, the Pi-Awakening at age 314 (unchanged) on the sixth day after his 314th birthday, "
                 "the Pier 30 days before his 31st birthday (confirmed by Abad), the Accords 283 years and 29 days, the Long Mask 283 "
                 "years and 36 days, and the late-Scourge placements. MCD-1902 locks the Book 1 beat (the Accords "
                 "broken, the Rebellion's operation brought to its knees and not finished; the Trinity reclaimed at the Karkosa Heist). MCD-1903 locks the aging misconception, "
                 "culminating in the deathbed state after his 314th birthday, with Sephtis's silence, Lauris's sense of kin, and Kanja's knowing the Haku legend without knowing it applies to him; Kanja learns it from Sephtis early in Book 4, set off by the first visible Bastion revisit, with Book 3's near-death as the reason Sephtis cannot stay silent. MCD-1904 locks the Awakening's trigger (the danger, a threat of deadly force at the Lighthouse, during the Last Breakfast), the Last Breakfast itself (a father-and-son ceremonial breakfast, Maro and Kanja, with Pyro always joining as the cook and never told why; held on the day at the Gilded Lighthouse, in the upper room where Kanja lies; the surge carries him down several stories and cracks the foundation) and the enemy's 'one day too late' belief (the enemy does not know of the 314 threshold), with the surge mechanism confirmed by Abad ('yes the surge snapping the pendant works'); the attack is made by the Three Ronin, all three survive, and how they reach him and the reveal's placement stay open. MCD-1905 locks the honor of the cook as the Rexmar lineage's, the reason Maro and Kanja give for always having Pyro at the table, and that Maro knows Pyro is his grandson. MCD-1906 locks the order chain: the regicide and the strike are SEALBLACK deployments ordered by SBD leadership, an unnamed leadership member signing as the Director's named proxy under SBD-051 with Grave-Analyst Abbott Gage's technical clearance, Director Ilona Corrance's knowledge left open, the proxy's identity reserved from pre-Book-1 entries. MCD-1907 locks the second attempt: after the Ronin fail, the Quiet Hand (SBD-059) with a savage team of animals under one Beast Master comes after the Karkosa Heist, not long after the first, and meets Kanja (with the Trinity reclaimed) with Pyro and the Triad unleashed, to the attackers' disaster; the Beast Master is unnamed and the attempt's place against the epilogue's Great Breach is not asserted. MCD-070 is amended so the "
                 "Investigation opens at the murder and runs on through the Interregnum. Amended: "
                 + ", ".join(sorted(amended)) + ". Files carried: " + ", ".join(files)
                 + f". Abad's approval, verbatim: \"{approval}\"."),
    })
    d["ledger_version"] = "38.0"
    d["last_updated"] = "2026-10-05"
    json.dump(d, open(LEDGER, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    open(LEDGER, "a", encoding="utf-8").write("\n")

    n_entries = sum(1 for f in files if f.startswith(CH))
    n_docs = len(files) - n_entries
    c = open("CLAUDE.md", encoding="utf-8").read()
    anchor = "Ledger at `ledger_version` 37.9, 2,721 rules, 377 batches.\n"
    assert c.count(anchor) == 1
    c = c.replace(anchor, anchor + f"""
**Batch 378: the Long Mask, the Accords and Book 1 on one clock (`MCD-1901`-`MCD-1907`).** Abad: "{approval}"
- **The ruling.** Abad, 2026-10-05: "Kanja is 313 years old when his father dies." The murder falls on
  the last day of his age 313 (confirmed by Abad: "yes"). The Pi-Awakening stays at age 314, and "the Long mask has to be after
  his 314th birthday": it falls on the sixth day after that birthday (confirmed by Abad: "yes Macana is
  Obsidian Malice, six days works"). The 10-Day Interregnum opens on that birthday, which
  makes the Awakening its seventh day (confirmed by Abad: "the interregnum day 1 counting works").
  The Long Mask runs from the Sovereign Pier to the pendant's severing at the Awakening, "just over
  283 years." The Accords end with the murder. This resolves approval-list item 1 and supersedes the
  Batch 56 ruling that `MCD-091`'s 296 controls.
- **The clock (`MCD-1901`).** The Pier falls 30 days before his 31st birthday (confirmed by Abad: "yes
  the Pier is 30 days before his 31st birthday"). The Accords held 283
  years and 29 days, the Long Mask 283 years and 36 days. The late-Scourge entries are placed on it:
  "one more year" at 312, the coat night at 313 before the Ceremony, the Eve of Awakening at 314 on
  the day before the Awakening. The Scourge persona ends at the coat night; the Long Mask ends at the
  pendant.
- **Book 1 (`MCD-1902`).** Kanja holds the murder as the Trust's breaking of the Accords. At thirty he
  had brought the enemy's whole operation to its knees, as Haku had, and had not finished it (Abad: "he
  did bring it to his needs but didn't finish it", "needs" being dictation for "knees"). After the
  Pi-Awakening he reclaims the Trinity at the Karkosa Heist to crush his enemies. No entry set before
  Book 1 may dramatize or foreshadow the murder, that reading, or the reclaiming. Retrospective tellers'
  after-the-fact mentions already locked stay permitted. `MCD-070` is amended: the Investigation opens at
  the murder and runs on through the Interregnum, which opens the next day.
- **The aging misconception (`MCD-1903`).** Kanja reads the Governor's Shackle as age. After his
  314th birthday the decline culminates in a deathbed state in which he believes he is dying; the
  Pi-Awakening releases the Shackle and shows him the decline was not age. Sephtis puts together that
  it is the Shackle and that its release is near; he does not know the timing or the trigger, he wrote
  the Countdown Annotation (`MCD-277`, age 310), and he stays silent, keeping it from Kanja under
  `MCD-208`'s mandate and from Lauris (Abad: "yes"). Kanja learns it from Sephtis early in Book 4,
  set off by the first visible Bastion revisit, with Book 3's near-death (`MCD-218`) as the reason Sephtis can no longer stay silent; he never
  knew the trigger, so the truth behind "one day too late" reaches the reader by another route (`MCD-216`). Lauris senses the density in Kanja and senses that he is kin; through
  Sephtis she knows his mother is Val Saeryn Kareth, so she knows he carries Kareth density, and she
  cannot put the rest together (Abad: "yes"). Kanja knows the Haku legend and does not know it applies
  to him. The sentences naming the Talisman as the cause are cut from Kanja VII (Abad: "yes").
- **The trigger (`MCD-1904`).** Abad: the Awakening falls on the sixth day after his birthday, and the trigger
  is the danger. By his deathbed days the Shackle is at its limit and would have broken on its own about a
  week later. What triggers it on the sixth day, at the Gilded Lighthouse, is a physical threat of deadly
  force. Confirmed by Abad ("yes the surge snapping the pendant works"): his body's surge in answer to the
  threat snaps the pendant. The attack comes during the Last Breakfast, while Pyro serves Kanja. Abad:
  "Yes. this is also a ceremonial breakfast that he had with Kanja & Maro at the same time every time
  they did have breakfast together." It is the first since Maro's murder, seven days before. The surge
  that snaps the pendant carries him down several stories (see the next bullet). The strike never lands,
  and a landed strike would have caused a world-scale event. The enemy that orders the
  murder and the strike does not know of the 314 threshold or the Pi-Awakening (Abad: "the enemy does
  not know they just want to eliminate him from the picture because they know he is next of kin and
  would seek revenge"; "similar to Haku except he literally had the means to do it and the Weaponry to
  do it"). They strike to remove Maro's next of kin, who brought their operation to its knees and has
  the means to finish it. T.D.K. is distinct: his containment was built to prevent the Awakening and he
  stays dormant until Book 1's epilogue. "One day too late" is the enemy's belief: seeing him awaken,
  they conclude it was coming anyway and that they missed by one day. It recurs through the books; the
  truth is revealed to the reader only later. The Three Ronin make the attack and all three survive it;
  how they reach him and where the reveal falls stay open. No entry set before Book 1 may state or hint at
  the trigger or the belief. Abad on Lauris: "Lauris should obviously be able to send his density or sense that he's
  family somehow she is an extraordinary character so that is something that I think should be evident
  to her but she can't put everything else together. if she knows who his mother is through Sephtis,
  then she would obviously know that he could potentially be dense".
- **The Last Breakfast and the cook's honor (`MCD-1904`, `MCD-1905`).** Abad, on where it is held:
  "the last breakfast can take place in the most logical place that makes sense for the story cuz it doesn't have to take place where it always takes place could be a reason any reason could be pyrule doesn't want to have breakfast there because of the memories it could be anything it could be because of the lack of movement that Kanja has"
  Abad, on who shares it: "the breakfast is Father and Son and they do not tell pyro why he always joins we can make up some sort of excuse like the cook is very coveted in their culture so it's easy to make them to cook and it's easy for them to be so warm towards the cook and loving towards the cook and have to cook close at heart because they feed a nourish everyone so that's a good way for them to have an excuse to always eat with him it's too honor to cook and that's the excuse that you have to spend time with him."
  The ceremonial breakfast is a father-and-son breakfast, Maro and Kanja, held at the same hour every
  time they breakfast together. Pyro always joins as the cook, who is held in honor and kept close at
  heart (`MCD-1905`); that honor is the reason Maro and Kanja give, and they never tell him why he always
  joins (`CC-047` already locks that he does not know his parentage). On the day, Kanja on his deathbed
  cannot be moved and Pyro cannot face the old table, so the breakfast is held at the Gilded Lighthouse,
  in the upper room where Kanja lies, at the usual hour. The strike comes during the meal. The surge
  carries him out of the upper room and down several stories, and he lands hard enough to crack the
  Lighthouse's foundation (the 2026-08-13 staging, `master-to-do-list.md`). The strike never lands, so
  the fall belongs to the surge. The Last Breakfast is the first since Maro's murder. Abad, 2026-10-06:
  "The Rexmar Lineage honors the cook." and "Maro knows". Maro knows Pyro is his grandson and Kanja knows
  Pyro is his son (`CC-079`); both know why Pyro always joins, and neither tells him (`CC-047`,
  `ARS-414`).
- **The order chain and the second attempt (`MCD-1906`, `MCD-1907`).** Abad, 2026-10-06, verbatim (the
  "I" in "I savage team" reads "a"):
  > "option 1 proxy, the Three Ronin, Book 4 works.
  >
  > we need a second attempt
  >
  > The Quiet Hand (SBD-059). A standing SEALBLACK cell kept for politically sensitive individual targets.
  >
  > paired with
  >
  > I savage team of animals and 1 Brute Beast Master.
  >
  > Kanja, Pyro & The Triad UNLEASHED.
  >
  > The Rexmar Lineage honors the cook.
  >
  > Maro knows"

  The regicide and the strike are SEALBLACK deployments ordered by SBD leadership. Under `SBD-051`, an unnamed
  leadership member signs as the Executive Director's named proxy and Grave-Analyst Abbott Gage gives the
  technical clearance; whether Director Ilona Corrance knew stays open, and the proxy's identity is reserved
  from pre-Book-1 entries (`MCD-1906`). After the Ronin fail, the Quiet Hand with a savage team of animals under
  one Beast Master (unnamed) comes as a second attempt. Abad, on when it comes: "the second attacks have come
  at some point after the first not to long after the first as they think they regrouped and figured out how
  to attack them which turns out disastrous for the attackers." Kanja, Pyro and the Triad meet it unleashed
  and defeat it. Abad, on the placement: "after the Karkosa Heist, with the Trinity." The attempt comes
  after the Heist (`MCD-070`), not long after the first, and Kanja fights it with the Trinity reclaimed
  (`MCD-1902`): Mafesto, Onyx of Oblivion and Obsidian Malice. The Quiet Hand normally works untraceable
  removals of individuals who need no anomaly-handling expertise (`SBD-059`); leadership pairs it with the
  Beast Master and his animals to supply what the cell lacks. Whether it falls before or inside the
  epilogue's Great Breach is not asserted (`MCD-1907`).
- **Propagation.** {len(amended)} rule statements amended; {n_entries} entries and {n_docs} docs carried,
  including the three Onyx seconds-counts (Kanja V-VII), recomputed from the Pier's date. The pitch
  line keeps its source wording, with a bracketed note. Syncs owed (Batch 377 practice): the mirrored
  Voice Progression Sheet under `docs/lords-of-cian/voice/` still reads 284 years (about line 145); the
  mirrored Voice Bible reads "314 years of performing a role" (about line 205) and carries "8,517,120,000
  seconds" at Pyro's birth (lines 107 and 109), which matches neither `MCD-270` nor the Pier's date. Neither
  mirror is edited; the Drive source documents are Abad's to update. `research/atlas-rebuild/mainline-gazetteer.json`
  carries 9 stale 284/296 strings, and its regeneration from the ledger is owed. The Pyro and Triad
  profiles carry the Batch 378 figures in their rule quotes, the age-table and A1 notes, and the Varruk
  age line; the rest of their review stays owed.
Ledger at `ledger_version` 38.0, {len(d['rules']):,} rules, 378 batches.
""")
    open("CLAUDE.md", "w", encoding="utf-8").write(c)

    d = json.load(open(LEDGER, encoding="utf-8"))
    dup = [k for k, v in Counter(r["id"] for r in d["rules"]).items() if v > 1]
    print("duplicates:", dup, "| total rules:", len(d["rules"]), "| version:", d["ledger_version"],
          "| rules amended:", len(amended), "| files edited:", len(files))


if __name__ == "__main__":
    main()
