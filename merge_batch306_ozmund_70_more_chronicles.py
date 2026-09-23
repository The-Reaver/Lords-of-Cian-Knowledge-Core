#!/usr/bin/env python3
"""Batch 306: Ozmund Verehimu Character Chronicles, wave 3 -- 70 new entries
(Chronicles LI-CXX, MCD-1780 through MCD-1849) bringing each of his six
Chronicle strands (Draconis, Aethelgard, Val Mirel, House politics, Wider
Household/Guard, coming-of-age) to 20 entries each -- 120 Chronicles total.
"""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-23, no source document. Ozmund Verehimu's own "
    "Character Chronicle series, wave 3 -- 70 new entries (Chronicles LI-CXX) produced via eight "
    "parallel background agents, one per strand block, each reading its strand's full prior "
    "entries and docs/lords-of-cian/character-profiles/ozmund-verehimu.md before drafting and "
    "collision-checking every new proper noun against the live ledger and every other strand's "
    "own new names. Brings all six strands (Draconis, Aethelgard, Val Mirel, House politics, "
    "Wider Household/Guard, coming-of-age) to 20 entries each -- 120 Chronicles total. Full "
    "narrative texts at docs/lords-of-cian/chronicles/ozmund-chronicle-<numeral>-<slug>.md."
)

NEW_RULES = [
    # --- Draconis strand wave 3 (MCD-1780-1788, Chronicles LI-LIX) ---
    {
        "id": "MCD-1780",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LI, \"What He Almost Said\" -- Draconis strand wave 3 opener, set "
            "some years after Chronicle XXV (MCD-1754), strictly pre-Fulfillment-Ceremony, "
            "Aethelgard alive. The strand's first entry to dramatize genuine doubt in Ozmund "
            "himself rather than in Draconis -- a private nighttime reflection mirroring Chronicle "
            "III's (MCD-1732) near-discovery entry, in which he questions for the first time "
            "whether his silence about MCD-024/CC-015/017 is protection of Draconis or protection "
            "of his own need to be loved as \"just a man.\" Extends the profile's psych-layer note "
            "on the silence's dual function without resolving it or advancing toward disclosure. "
            "Narrated by Red Beard per VB-020/022/CC-020. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1781",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LII, \"The Man Who Called It Waste\" -- Draconis strand wave 3, same "
            "general span as Chronicle LI, Aethelgard alive. Tests the purity of the CC-085 "
            "dynamic against outside provocation for the first time in the strand: an unnamed "
            "visiting garrison commander accuses Draconis of wasting his career and implies Ozmund "
            "manipulates his loyalty; Draconis answers from unshaken conviction, reinforcing "
            "Chronicle XXIV's (MCD-1753) \"identity, not debt\" reading, while Ozmund, overhearing, "
            "is forced to confront how closely an outsider's bad-faith guess brushes the truth. "
            "Does not push Draconis toward suspicion or Ozmund toward disclosure. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1782",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LIII, \"The Sister Who Came North\" -- Draconis strand wave 3, same "
            "general span, Aethelgard alive. Brings Halyn (established off-page in Chronicle V, "
            "MCD-1734) and her two unnamed children on-page for the first time, visiting the "
            "Verehimu seat en route to a family wedding; a deliberately warm, stakes-free domestic "
            "entry giving Draconis interiority outside his role, with Ozmund introduced to her "
            "only as an unranked household officer, preserving his \"just a man\" cover. No threat, "
            "no test, no advance on the purity-test dynamic. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1783",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LIV, \"What the Silence Cost\" -- Draconis strand wave 3, same "
            "general span, Aethelgard alive. The strand's first entry to dramatize a real, "
            "visible, permanent cost of Ozmund's established restraint: during a raider ambush on "
            "an eastern grain-assessment column, Ozmund again fights at human pace rather than end "
            "the fight in one motion, and Brenner (Chronicle XXI, MCD-1750) takes a wound that "
            "leaves him permanently lamed. Extends CC-090/ARS-381's dignity-through-agency value "
            "into its costly underside; Ozmund privately arranges anonymous long-term care, "
            "echoing but darkening the Chronicle V (MCD-1734) almsfund mechanism. Draconis never "
            "learns the true cause. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1784",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LV, \"The Ones He's Teaching Now\" -- Draconis strand wave 3, same "
            "general span, Aethelgard alive. Continues Brenner's arc directly from Chronicle LIV "
            "(MCD-1783): now permanently lamed, he is given the autumn musters by Draconis and "
            "independently reproduces the instinct-over-polish recruiting standard Draconis first "
            "applied to him in Chronicle XXI (MCD-1750), passing it to a new unnamed recruit "
            "without knowing its origin -- a second-generation extension of Chronicle XXII's "
            "(MCD-1751) \"taught without meaning to\" theme, showing a genuine good growing out of "
            "Chronicle LIV's cost without erasing it. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1785",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LVI, \"The Worst Cast He Ever Tied\" -- Draconis strand wave 3, same "
            "general span, Aethelgard alive. The strand's designated warm, stakes-free "
            "near-banter entry: a return, years later, to the same lake and fishing-line motif "
            "from Chronicle XXV (MCD-1754), with Draconis and Ozmund trading genuine, unforced "
            "teasing for the first time in the series. No threat, no test, no advance on the "
            "purity-test dynamic. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1786",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LVII, \"The Night He Didn't Have a Plan\" -- Draconis strand wave 3, "
            "same general span, Aethelgard alive. The wave's centerpiece high-stakes entry: a "
            "border-road ambush escalates Chronicle I's (MCD-1730) original attack and Chronicle "
            "LIV's (MCD-1783) established cost pattern to its sharpest point yet -- a bolt meant "
            "for Ozmund strikes Draconis instead, who nearly dies; Ozmund, acting without a plan "
            "for the first time in the series, fights conventionally to preserve his cover even at "
            "maximal personal stakes, then saves Draconis through explainable-but-extreme physical "
            "effort. Draconis survives, permanently scarred, crediting luck; the purity-test "
            "dynamic (CC-085) survives intact but the doubt raised in Chronicle LI (MCD-1780) is "
            "deepened rather than resolved. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1787",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LVIII, \"What Twenty Years Sounds Like\" -- Draconis strand wave 3, "
            "same general span, Aethelgard alive. A quiet reflective entry on ordinary aging: "
            "Ozmund notices, for the first time, the accumulated physical signs of Draconis's age "
            "(grey hair, a stiffening sword hand, careful knees), confronting a vulnerability in "
            "their relationship he has no power to answer -- deliberately not connected to or "
            "foreshadowing MCD-025's Fulfillment Ceremony. Reuses Halyn's son (Chronicle LIII, "
            "MCD-1782) rather than a new name. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1788",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LIX, \"The Road, Revisited,\" closing the Draconis strand's third "
            "wave (Chronicles LI-LIX). Draconis strand wave 3, same general span, Aethelgard "
            "alive. A deliberate structural bookend: routine business carries Ozmund and Draconis "
            "back past the exact site of Chronicle I's (MCD-1730) road ambush years later; "
            "Draconis notices an unaccountable chill in the ground without ever naming why, and "
            "neither man speaks its true subject aloud. Closes the wave on quiet, unresolved "
            "resonance, mirroring the closing register of Chronicles VI (MCD-1735) and XXV "
            "(MCD-1754); the purity-test dynamic remains exactly as open as it began. No new named "
            "characters. Closes the Draconis strand at 20 entries total (Chronicles I-VI, "
            "XXI-XXV, LI-LIX)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Aethelgard strand wave 3 (MCD-1789-1798, Chronicles LX-LXIX) ---
    {
        "id": "MCD-1789",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LX, \"What He Could Not Set Right\" -- Aethelgard strand wave 3, "
            "strictly pre-Fulfillment-Ceremony, Aethelgard alive. A wasting fever reaches the "
            "remote Verehimu Wetlands settlement of Sennick two months late because the House's "
            "twice-yearly reporting mechanism failed it, and by the time Aethelgard arrives "
            "seventeen are already dead; unlike Chronicle IX's (MCD-1738) corrected levee, there "
            "is nothing left to fix, only a standing relay to build and a public admission that "
            "the system failure cost lives no order can restore. Extends ARS-381/CC-090's "
            "public-accountability framing through genuine, unresolved cost rather than a repaired "
            "mistake. New place name: Sennick, in the Verehimu Wetlands."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1790",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXI, \"What the Law Was For\" -- Aethelgard strand wave 3, Aethelgard "
            "alive. A young House hand steals grain to feed a sick sister; Ozmund argues for quiet "
            "leniency on grounds of desperation over greed, Aethelgard holds that mercy granted by "
            "sympathy alone becomes indistinguishable from favoritism and erodes trust in the rule "
            "itself, and the two settle on a partial consequence that satisfies neither, with both "
            "positions left genuinely, permanently unresolved -- a second father-son disagreement "
            "distinct in subject from Chronicle XXVIII (MCD-1757). No new named characters (the "
            "hand is deliberately unnamed)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1791",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXII, \"The Doubt He Carried Alone\" -- Aethelgard strand wave 3, "
            "Aethelgard alive. Young Ozmund overhears, unseen, Aethelgard privately confessing to "
            "Val Mirel that he sometimes doubts whether he is the House's best possible lord or "
            "simply a stubborn man who has never stopped showing up; Val Mirel doesn't contradict "
            "him, only affirms that the House needs the lord it actually has. Distinct in register "
            "from Chronicle X's (MCD-1739) external, generalized fear -- this is private doubt "
            "about personal adequacy, never spoken to Ozmund directly. Val Mirel appears briefly, "
            "her own strand's reserved material untouched. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1792",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXIII, \"Two Different Kinds of Command\" -- Aethelgard strand wave "
            "3, Aethelgard and Val Mirel both alive. River bandits raiding grain barges surface a "
            "genuine, warm disagreement between Val Mirel (swift decisive interception, Kareth "
            "War-Order doctrine) and Aethelgard (find the root cause first); both approaches run "
            "in parallel and both matter -- Val Mirel's party takes the raiders cleanly, "
            "Aethelgard's own investigation finds and relieves the blight-driven desperation that "
            "caused the raids in the first place. The strand's first dedicated marriage-dynamic "
            "entry, extending MCD-101's Seventh Wing tactician framing and CC-090's discipline "
            "framing as complementary rather than competing. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1793",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXIV, \"The Coin That Would Not Settle\" -- Aethelgard strand wave 3, "
            "Aethelgard alive. Aethelgard uses the \"coin on its edge\" ritual (MCD-1736/1737/1740) "
            "for the first time on people other than Ozmund -- the Rell and Tamsy households, "
            "whose three-generation half-acre dispute (background-established at MCD-1738) turns "
            "out to be rooted in a genuine flood-displaced boundary marker rather than temper -- "
            "and discovers the coin's real limit: it buys patience, not truth, and the dispute is "
            "finally settled by a surveyor rather than the ritual. New named figures: the Rell and "
            "Tamsy families, feuding Verehimu fen-households."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1794",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXV, \"The Afternoon He Let Himself Be Foolish\" -- Aethelgard strand "
            "wave 3, Aethelgard alive. Aethelgard takes young Ozmund fishing, demonstrates "
            "backwards technique with total confidence, and falls dramatically out of the boat in "
            "front of the household and a passing barge crew, insisting afterward that his son "
            "never let him live it down -- the strand's first entry of pure levity with no "
            "governance principle, disagreement, or fear attached, deliberately showing Aethelgard "
            "letting himself be seen as ridiculous rather than only capable. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1795",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXVI, \"What Became of Hallum's Girl\" -- Aethelgard strand wave 3, "
            "Aethelgard alive. Years after Chronicle XXVI (MCD-1755), Petrin Hallum dies of age; "
            "rather than let the quiet debt lapse, Aethelgard redirects the same anonymous "
            "payments to Hallum's adult daughter, Fenna Hallum, and for the first time brings the "
            "now-older Ozmund along to witness the arrangement continue without ever revealing "
            "itself to her. Extends the \"currency no one else sees spent\" theme (ARS-381/CC-090) "
            "past its original recipient's death. New named character: Fenna Hallum."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1796",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXVII, \"The Vote He Lost\" -- Aethelgard strand wave 3, Aethelgard "
            "alive. Aethelgard brings a Wetlands toll-relief measure (grown directly out of what "
            "Sennick, MCD-1789, taught him) to House Council and loses cleanly to Lord Ashvane's "
            "honest, defensible opposition on behalf of dry-land holdings that would bear the "
            "cost; rather than retaliate, Aethelgard thanks the Council, seeks Ashvane out "
            "personally, and returns a year later with a revised proposal that wins Ashvane's own "
            "support. A genuine political defeat with no hidden villainy, deliberately distinct "
            "from the reserved antagonist thread. New named character: Lord Ashvane."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1797",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXVIII, \"What His Hands Remembered\" -- Aethelgard strand wave 3, "
            "Aethelgard alive. Aethelgard and young Ozmund spend an afternoon patching a leaking "
            "skiff's hull themselves rather than summoning a shipwright, failing twice before "
            "succeeding; Aethelgard explains he wants his son to have at least one skill that "
            "belongs to nobody's expectations of him and owes nothing to title, blood, or the "
            "Density Spike. A quiet ordinary-competence register distinct from the strand's "
            "swordwork entry (MCD-1737). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1798",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXIX, \"The Father Beneath the Lord,\" closing wave 3 of the "
            "Aethelgard strand. Aethelgard alive. Red Beard synthesizes Chronicles LX-LXVIII "
            "across several more nights of telling, concluding that what defines Aethelgard isn't "
            "any single lesson but the sheer accumulation of ordinary, unglamorous choices to "
            "remain a person rather than become a legend before his time; the coin surfaces once "
            "more, now mostly carried rather than ritually used. Deliberately open-ended, matching "
            "Chronicle XXX's (MCD-1759) precedent -- not a capstone for the whole strand. No new "
            "named characters. Closes the Aethelgard strand at 20 entries total (Chronicles "
            "VII-XI, XXVI-XXX, LX-LXIX)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Val Mirel strand wave 3 (MCD-1799-1808, Chronicles LXX-LXXIX) ---
    {
        "id": "MCD-1799",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXX, \"The Door That Could Only Open Once\" -- Val Mirel strand wave "
            "3, strictly pre-Fulfillment-Ceremony, Aethelgard alive. Ozmund, roughly eleven "
            "(between Chronicles XII and XIII), witnesses Val Mirel command a real-life triage "
            "during a flood at a House-adjacent millers' quarter, choosing to send the one "
            "available rescue boat to the mill-house that could not survive a delay rather than "
            "splitting the crossing evenly. Introduces the Narrow Door, a third original Kareth "
            "War-Order discipline (MCD-101/CC-004) distinct from the Stone Count (patience, "
            "MCD-1741) and the Hollow Stand (grief, MCD-1745) -- the discipline of choosing "
            "cleanly under irreversible scarcity and carrying the unchosen loss without pretending "
            "the choice was kinder than it was. Seeds, without naming any future event, the same "
            "clean command-under-scarcity instinct Ozmund later shows at scale in his Book 2 "
            "command architecture (MCD-279/280)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1800",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXI, \"What Distance Would Not Hold\" -- Val Mirel strand wave 3, "
            "Aethelgard alive. Ozmund, roughly thirteen, survives an ambush aimed specifically at "
            "him; Val Mirel, a day's ride away on Seventh Wing business, arrives faster than any "
            "message could travel and ends the fight herself in full view of witnesses -- the one "
            "time in the strand her carefully maintained public invisibility breaks. Directly "
            "tests and confirms Chronicle XIV's (MCD-1743) \"chosen distance\" philosophy as "
            "conditional on his safety rather than absolute: she tells him the distance was always "
            "a door kept closed on purpose, not a wall, and he has just seen the one condition "
            "under which it opens. The ambush's instigator is deliberately left unidentified and "
            "unconnected to any locked antagonist."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1801",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXII, \"Two Kinds of Safekeeping\" -- Val Mirel strand wave 3, "
            "Aethelgard and Val Mirel both alive. Roughly three weeks after Chronicle LXXI (Ozmund "
            "~14), he overhears a genuine, unresolved disagreement between Val Mirel and "
            "Aethelgard over how to raise him post-ambush: Aethelgard wants formalized, visible "
            "institutional protection (escort, curtailed travel, eventual alliance marriages); Val "
            "Mirel argues that over-protection produces a son untested by the world, and pushes "
            "for accelerated Kareth discipline instead. Neither parent is framed as wrong; they "
            "synthesize into quiet increased oversight plus deepened training in the already-"
            "locked Stone Count and Narrow Door, extending Chronicle XII's \"genuine partnership "
            "across two registers\" framing into an actual worked disagreement for the first time."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1802",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXIII, \"The Wound She Let Him See\" -- Val Mirel strand wave 3, "
            "Aethelgard alive. Ozmund, roughly sixteen, tends to Val Mirel after she returns "
            "genuinely injured from an unnamed campaign -- the first time in the strand the "
            "caregiving dynamic reverses (contrast Chronicle XVI, MCD-1745, where she cares for "
            "his grief). She tells him she has let no one care for her this way since before he "
            "was born, extending the profile's \"genuine intimacy is rare and hard-won\" "
            "relationship-pattern layer to her own side of the relationship for the first time. "
            "The wound's cause is deliberately undisclosed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1803",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXIV, \"The Woman Before the Mother\" -- Val Mirel strand wave 3, "
            "Aethelgard alive. Ozmund, roughly eighteen, overhears a retired soldier of Val "
            "Mirel's Wing recount a story of her as a young, doubted, unproven tactician centuries "
            "before his birth -- the strand's first dramatized moment of Ozmund beginning to see "
            "Val Mirel Kareth (MCD-101/CC-004) as a full person with her own interior history "
            "rather than only a parent. The unnamed soldier and unnamed campaign are one-scene, "
            "non-specific background detail."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1804",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXV, \"The First Time She Asked\" -- Val Mirel strand wave 3, "
            "Aethelgard alive. Ozmund, roughly twenty-one, is consulted by Val Mirel on a genuine, "
            "classified Seventh Wing tactical problem as a peer rather than taught as a student -- "
            "the mirror-image turning point to Chronicle LXXIV (MCD-1803), extending Chronicle "
            "XIII's (MCD-1742) observation-based tactical method into Ozmund's own independent "
            "application of it for the first time, recognized and validated by her."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1805",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXVI, \"What Made Her Laugh\" -- Val Mirel strand wave 3, "
            "Aethelgard and Val Mirel both alive. A deliberately lighter-toned entry: Ozmund, "
            "roughly twenty-four, witnesses a rare, ordinary family dinner where Val Mirel makes a "
            "single dry joke at Aethelgard's expense (about his consistently mistimed jokes) -- "
            "the first time in the project she and Aethelgard are shown sharing genuine domestic "
            "ease and mutual enjoyment rather than parallel-register partnership or careful "
            "non-intervention. Her humor is framed as an extension of, not a break from, her "
            "established flat discipline."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1806",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXVII, \"The Years She Would Not Have\" -- Val Mirel strand wave 3, "
            "Aethelgard alive. Ozmund, roughly twenty-six, finds Val Mirel in a private, "
            "unguarded moment of existential reckoning with the disparity between her ~89,003-year "
            "Kareth lifespan (MCD-101) and his own much shorter one. She names it not as fear but "
            "as a debt entered knowingly, and states she would rather love him briefly than never "
            "at all -- deepening, without contradicting, Chronicle XIV's (MCD-1743) rationale for "
            "her chosen distance. States nothing about her own eventual fate."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1807",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXVIII, \"The Door He Opened Himself\" -- Val Mirel strand wave 3, "
            "Aethelgard alive. Ozmund, roughly twenty-eight, independently applies the Narrow Door "
            "discipline (MCD-1799) as an adult during a landslide rescue, without his mother "
            "present, choosing to commit all resources to the camp on unstable ground rather than "
            "split them -- a direct structural bookend to Chronicle LXX. Writes to her afterward; "
            "her reply confirms the discipline \"stopped being hers... the moment he stopped "
            "needing her standing beside him to use it,\" completing the strand's \"teaching by "
            "eventually letting go\" pattern."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1808",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXIX, \"The Words She Finally Chose,\" closing wave 3 of the Val "
            "Mirel strand. Aethelgard alive. Shortly after Chronicle LXXVIII, Val Mirel gives "
            "Ozmund his first fully spoken statement of maternal pride -- not for his capability, "
            "but for who he has chosen to become when no one was watching -- deliberately "
            "contrasted with, and paired alongside, Chronicle XXXV's (MCD-1764) wordless "
            "palm-against-the-chest promise. Closes the strand's three waves on an escalating "
            "structure of expressed love: taught discipline (wave 1, the Hollow Stand) -> "
            "wordless gesture (wave 2) -> spoken words (wave 3), reprising rather than replacing "
            "the Chronicle XXXV gesture at its close. Closes the Val Mirel strand at 20 entries "
            "total (Chronicles XII-XVI, XXXI-XXXV, LXX-LXXIX)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- House politics strand wave 3 (MCD-1809-1819, Chronicles LXXX-XC) ---
    {
        "id": "MCD-1809",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXX, \"The Boundary That Settled Itself\" -- House politics strand "
            "wave 3, strictly pre-Fulfillment-Ceremony, age 23. A minor land dispute between two "
            "smallholding families under House Verehimu (Bram Corwyth and Iona Adderwell, feuding "
            "over a hedgerow encroachment) is resolved by Ozmund through private mediation and "
            "structured listening rather than adjudication -- he walks the boundary with both "
            "parties separately, gives each what they actually wanted (acknowledgment, not land), "
            "and lets the two families rebuild an ordinary working relationship on their own. "
            "Extends CC-090/ARS-381's dignity-through-agency throughline into interpersonal "
            "reconciliation. New named characters: Bram Corwyth and Iona Adderwell, one-off "
            "smallholding family heads."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1810",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXXI, \"What the Envoy Came to Measure\" -- House politics strand "
            "wave 3, age 24. Lord Ansel Varnhelt of House Varnhelt, assessing House Verehimu as a "
            "marriage-alliance partner, tests Ozmund by inviting him to disparage an absent rival "
            "House over wine; Ozmund declines the bait without overcorrecting into rigidity, "
            "redirecting the conversation instead, and earns a favorable private report. Extends "
            "the \"listening\" lesson from Chronicle XXXVIII (MCD-1767) into a self-presentation "
            "register. New named figures: Lord Ansel Varnhelt and House Varnhelt, a one-off envoy "
            "and House."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1811",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXXII, \"The Weight of an Old Quota\" -- House politics strand wave "
            "3, age 25. Ozmund discovers his House's sixty-year-old flat-percentage grain tithe "
            "formula has drifted into regressive unfairness (largest, most productive holdings "
            "effectively pay less than smallholders); working collaboratively with the House "
            "Quartermaster rather than around him, he designs a banded-scale replacement and "
            "presents it as jointly authored. Systemic reform distinct from Chronicle XXXVII's "
            "individual-petition scale (MCD-1766). New named character: Quartermaster Aldous "
            "Prynn."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1812",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXXIII, \"What They Said When He Wasn't Listening\" -- House "
            "politics strand wave 3. Told secondhand through Bevin (MCD-1747) about an earlier "
            "household kitchen-staff gathering where several women, comparing notes for the first "
            "time, realize each had separately received an unexplained small kindness from Ozmund "
            "(a mended apron, supplemental firewood, help with ruined dough) -- none had known how "
            "many others were quietly carrying the same experience. Extends the "
            "dignity-through-agency/uncredited-decency pattern and directly anticipates Chronicle "
            "XL's synthesis (MCD-1769). No new named characters (kitchen staff left unnamed)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1813",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXXIV, \"The Precedence No One Wanted to Concede\" -- House "
            "politics strand wave 3, age 24. A three-generation ceremonial seating-precedence "
            "dispute between allied Houses Renlow and Ashmere is resolved by Ozmund not through a "
            "ruling but through a structural compromise -- a formally recorded rotating seniority "
            "-- winning acceptance by privately showing both delegations that continued escalation "
            "cost more than either side's pride was worth. New named Houses: House Renlow and "
            "House Ashmere, one-off allied Houses."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1814",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXXV, \"The Envoy Who Came to Provoke\" -- House politics strand "
            "wave 3, age 26. Ser Dravot Skarne of House Skarne, carrying an old three-generation "
            "grievance against House Verehimu, visits under pretext of a grazing dispute and "
            "spends the visit constructing deniable provocations designed to extract either an "
            "apology or a loss of composure; Ozmund refuses both traps through level, honest "
            "non-engagement, denying Skarne the reaction he came for. Extends "
            "discipline-as-armor (CC-090/ARS-381) into sustained patience under indirect pressure. "
            "New named figures: Ser Dravot Skarne and House Skarne."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1815",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXXVI, \"What the Old Practice Cost\" -- House politics strand wave "
            "3, age 26. Presiding over his first solo \"Reckoning Walk\" (a sixty-year-old "
            "public-shaming debt custom), Ozmund is troubled by the humiliation it inflicts beyond "
            "what fairness requires, and persuades Aethelgard to permanently retire its public "
            "form in favor of an equally rigorous private accounting. Extends Chronicle XIX's "
            "private-justice instinct (MCD-1748) into a permanent institutional reform. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1816",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXXVII, \"The Door They Left Unlocked\" -- House politics strand "
            "wave 3, spanning roughly ages 12-27. Retired night-watchman Wendell Rowe recounts a "
            "fifteen-year unspoken arrangement in which he quietly left one House side-door "
            "unlocked during the hours young Ozmund was known to walk at night, never discussed by "
            "either man, and eventually recognized and matched by other household staff -- the "
            "household's own reciprocal, unrequested trust in him. New named character: Wendell "
            "Rowe, a one-off House Verehimu night-watchman."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1817",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXXVIII, \"The Quarrel Between Two Old Men\" -- House politics "
            "strand wave 3, age 27. A three-year feud between House Verehimu's Master of Hounds "
            "and Master of Stables over yard precedence during the autumn hunt is resolved by "
            "Ozmund not through ruling but by making each man describe, aloud and in front of the "
            "other, what he admires about the other's work -- reconciling them into working "
            "colleagues again. A light/comedic-register rivalry entry. No new named characters "
            "(titled roles only)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1818",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle LXXXIX, \"The Toll They Couldn't Agree On\" -- House politics strand "
            "wave 3, age 27. A stalled annual river-shipping toll negotiation with Factor Yewen "
            "Ashworth of House Ashworth is resolved when Ozmund, noticing standard counter-"
            "pressure isn't working, asks Ashworth directly what has actually changed -- "
            "uncovering an undisclosed barge-repair financial strain -- and structures a "
            "multi-year shipping commitment that solves the real problem rather than the stated "
            "one. Extends the \"listening\" lesson into active inquiry. New named figures: Factor "
            "Yewen Ashworth and House Ashworth."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1819",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XC, \"What the Room Had Learned to Expect of Him,\" closing wave 3 "
            "of the House politics strand. The wave's closing, retrospective entry: Red Beard and "
            "Ozmund reflect together on how, across ages 23-27, the region came to expect honest "
            "hearing and fair dealing from Ozmund in these small rooms, and how that earned, "
            "dispute-by-dispute political authority became the one form of power he fully trusts, "
            "since it was built rather than inherited or exercised through his Crown-Scar. "
            "Synthesizes Chronicles LXXX-LXXXIX by name without advancing any reserved thread -- "
            "the Crown-Scar's true siphon nature (MCD-290) is referenced only as a form of power "
            "he chooses not to lean on, no mechanism detail. No new named characters. Closes the "
            "House politics strand at 20 entries total (Chronicles XVII-XX, XXXVI-XL, LXXX-XC)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Wider Household/Guard strand wave 2 part A (MCD-1820-1827, Chronicles XCI-XCVIII) ---
    {
        "id": "MCD-1820",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XCI, \"The Night the Feed Barn Burned\" -- Wider Household/Guard "
            "strand wave 2, age ~13, strictly pre-Fulfillment-Ceremony. A fire breaks out in the "
            "lower feed barn at night, threatening the adjoining stable block. Armsmaster Berrin "
            "Hollis organizes bucket lines that Sergeant Oswin Kade folds his guardsmen into "
            "rather than compete with; Ozmund pulls horses out by hand alongside stable boy Cobb "
            "rather than use his Density Spike, consciously choosing the slower, deniable method "
            "over a display that would raise questions. No horse is lost; the barn is a total "
            "loss. Dramatizes deliberate non-use of his power as a live, costly choice. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1821",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XCII, \"What the Winter Nearly Cost\" -- Wider Household/Guard "
            "strand wave 2, age ~11. A hard winter and a bad grain count threaten falconer Annis "
            "Fairweather's mews birds specifically, since hunting birds can't simply be rationed "
            "the way horses can. Ozmund brings Fairweather and Master Alric Fenmoor together to "
            "solve it -- Fenmoor building a rationing table around what Fairweather actually needs "
            "rather than generic household arithmetic. Two birds go off condition but none are "
            "lost; the episode is the first real conversation Fairweather and Fenmoor ever have. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1822",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XCIII, \"The Distance Station Made\" -- Wider Household/Guard strand "
            "wave 2, age ~15. At a formal dinner, Cobb must attend Ozmund in the hall for the "
            "first time, addressing him with correct formal distance rather than the ease of the "
            "stable yard. Ozmund is unsettled watching what the formality costs Cobb to perform; "
            "afterward, at a side door, the two agree the hall can have its correct forms while "
            "the stable yard keeps what it always was. First direct test of the friendship against "
            "real station. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1823",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XCIV, \"Two Old Men and One Yard\" -- Wider Household/Guard strand "
            "wave 2, age ~16. A long-running institutional friction between Hollis (wants recruits "
            "fully trained before real duty) and Kade (wants real duty as the truer teacher) comes "
            "to a head when Ozmund, now sitting in on minor household governance, asks each man a "
            "mirrored question about actual outcomes rather than instinct. The two settle on a "
            "staged rotation neither had proposed alone, deepening a decades-long friendship built "
            "on disagreement rather than agreement. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1824",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XCV, \"The Fever in the Mews\" -- Wider Household/Guard strand wave "
            "2, age ~14. Fairweather falls seriously ill for three weeks. Fenmoor visits daily to "
            "read her written feeding charts aloud and verify compliance; Cobb, knowing nothing "
            "about hawks, executes the charts to the letter; Ozmund carries messages and covers "
            "one morning himself. No bird is lost -- proof that disciplined execution of someone "
            "else's expertise, not improvisation, is what saved the mews. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1825",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XCVI, \"What the Drought Asked of the House\" -- Wider "
            "Household/Guard strand wave 2, age ~17. A drought-driven water shortage brings "
            "Hollis, Fairweather, and Kade into open disagreement over allocation priorities at a "
            "household meeting; Fenmoor works the real figures rather than arguing from position "
            "and finds genuine slack (the ornamental gardens, which no one considered a real "
            "stake) that lets everyone keep what mattered. The strand's first full ensemble scene "
            "with all four established figures together, explicitly framed by Red Beard as a "
            "reconstruction from four partial memories rather than one complete account. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1826",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XCVII, \"The Boy Who Learned to Bow\" -- Wider Household/Guard "
            "strand wave 2, age ~18. Ozmund watches Kade recommend Cobb for a mounted-courier post "
            "carrying real standing and long postings away from the household. Cobb asks Ozmund "
            "directly whether taking it would be a betrayal; Ozmund tells him a friendship that "
            "only survives through proximity isn't worth defending, and Cobb accepts. Their "
            "parting is warm but the narration notes neither man ever explained, even decades "
            "later, why they let the resulting distance become permanent -- Cobb's ultimate fate "
            "stays open. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1827",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XCVIII, \"An Ordinary Evening at Verehimu,\" closing part A of the "
            "Wider Household/Guard strand's wave 2. A deliberately stakes-free closing entry: Red "
            "Beard's own composite meditation, built from five separate unremarkable evening "
            "routines (Hollis walking the yard, Fairweather closing the mews, Fenmoor working by "
            "candlelight, Kade at the gate, Cobb bedding down horses) that together, without any "
            "single dramatic act, is what actually held the household together -- a chorus none of "
            "the five ever heard as one until asked. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Wider Household/Guard strand wave 2 part B (MCD-1828-1834, Chronicles XCIX-CV) ---
    {
        "id": "MCD-1828",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XCIX, \"What Kade Passed Down\" -- Wider Household/Guard strand wave "
            "2. Sergeant Oswin Kade, in his last five years of active service, deliberately "
            "trained an unnamed successor guardsman -- chosen not for swordwork but for having "
            "once self-reported an error unprompted -- passing forward the reciprocal House/Guard "
            "\"arrangement\" ethos established at Chronicle XLV (MCD-1774) as a taught inheritance "
            "rather than a fact that simply persists. Establishes that Kade framed the culture as "
            "belonging to the post itself, not to him personally. Extends Chronicle XLV's "
            "institutional register into a generational-transmission register. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1829",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle C, \"The Book Fenmoor Never Finished\" -- Wider Household/Guard "
            "strand wave 2. Master Alric Fenmoor's own unfinished scholarly ambition -- a full "
            "accounting of the Sovereign Trust's earliest Scrip correspondence, dismissed by an "
            "unnamed senior scholar for being inconvenient rather than wrong -- is the personal "
            "root of the intellectual rigor he demanded of young Ozmund at Chronicle XLIII "
            "(MCD-1772). Fenmoor recognized his own younger frustration in Ozmund's early reaction "
            "to correction, and deliberately never disclosed the personal wound behind the lesson "
            "to his student. Extends Chronicle XLIII with a generational/legacy layer. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1830",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CI, \"What Annis Kept Beyond the Mews\" -- Wider Household/Guard "
            "strand wave 2. Falconer Annis Fairweather's patient attentiveness toward frightened "
            "animals, and toward young Ozmund in Chronicle XLII (MCD-1771), traces to a private "
            "grief: her own son, who wanted to join a House Guard, died of fever before reaching "
            "service age. She recognized in Ozmund's stillness around the goshawk the same "
            "instinct that drew her back to falconry after her loss, and deliberately never told "
            "him any of it during his boyhood. Extends Chronicle XLII with a generational/legacy "
            "layer. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1831",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CII, \"The Mistake Cobb Couldn't Take Back\" -- Wider "
            "Household/Guard strand wave 2. Years after Chronicle XLIV, an adolescent Ozmund "
            "personally intervenes when stable hand Cobb blames himself for a stall-latch failure "
            "(likely a hardware fault, not his error) that let a gelding loose overnight with no "
            "injuries. Ozmund refuses to let Cobb treat an honest mistake as shame, quietly has "
            "the stable's hardware replaced House-wide so no blame is assigned, and applies to "
            "Cobb the same \"wrong method vs. honest failure\" lesson Fenmoor taught him "
            "(MCD-1772). Extends Chronicle XLIV and demonstrates the profile's \"dignity through "
            "agency\" value applied outward to a peer for the first time. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1832",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CIII, \"The Yard Hollis Would Leave Behind\" -- Wider "
            "Household/Guard strand wave 2. Armsmaster Berrin Hollis, training an unnamed "
            "assistant instructor late in his career, catches himself repeating his own original "
            "mistake from Chronicle XLI (MCD-1770) -- misreading a trainee's caution as weakness -- "
            "until he learns the caution stems from having once seen a student injured through "
            "careless instruction. Hollis reworks his training approach in response, paying "
            "forward, unknowingly to Ozmund, the lesson Ozmund once taught him. Deliberately "
            "mirrors Chronicle XCIX's generational structure. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1833",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CIV, \"The Night the Gate Went Unwatched\" -- Wider Household/Guard "
            "strand wave 2. Sergeant Oswin Kade confesses to an adolescent Ozmund, decades late, a "
            "genuine lapse from his own early guardsman years -- standing a watch with his full "
            "attention elsewhere due to his father's fatal illness, though nothing ever came of "
            "it. Ozmund's graceful response (no fault-finding, since nothing was actually "
            "endangered) and his suggestion that the story become instruction rather than "
            "confession is established as the direct origin of the honest-reporting culture Kade "
            "later builds his successor's training around in Chronicle XCIX. Extends and grounds "
            "Chronicle XLV's account of quiet policy reform. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1834",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CV, \"One Table, Five Debts,\" closing wave 2 of the Wider "
            "Household/Guard strand. Red Beard reconstructs, from five independently gathered "
            "accounts, a single unremarkable evening in Ozmund's later adolescence when he "
            "privately gathered Berrin Hollis, Annis Fairweather, Alric Fenmoor, Cobb, and Oswin "
            "Kade together at one table to thank them collectively, in the open, for raising him "
            "-- a one-time, deliberately non-ceremonial act, consistent with his established "
            "pattern of formalizing what others would leave unspoken. No new named characters. "
            "Closes the Wider Household/Guard strand at 20 entries total (Chronicles XLI-XLV, "
            "XCI-CV)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Coming-of-age strand wave 2 part A (MCD-1835-1842, Chronicles CVI-CXIII) ---
    {
        "id": "MCD-1835",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CVI, \"The Gate That Would Not Open\" -- coming-of-age strand wave "
            "2. Locks a formative test of Ozmund's \"no threshold to cross\" discipline "
            "(CC-015/017/MCD-024) at its most mundane register -- a stuck winter granary gate with "
            "no stakes and no witness, where using even a harmless sliver of the Density Spike "
            "would have gone unnoticed by everyone present. He refuses regardless, freeing it "
            "entirely by hand over roughly four hours with an axe and hot water, refusing Osric's "
            "offer of a stronger back. Establishes, in his own later reflection, that a discipline "
            "only held when it costs something or is being watched isn't a real discipline at "
            "all. Distinct from Chronicle XLIX's solitary floor-testing (MCD-1778). No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1836",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CVII, \"The Mark on His Father's Hand\" -- coming-of-age strand wave "
            "2. Locks a private realization, never voiced to anyone until this telling, that a "
            "small permanent scar on Aethelgard Verehimu's smallest finger is the mark of his "
            "infant son's own unconscious grip, evidence the Density Spike was active and beyond "
            "any conscious control from Ozmund's earliest infancy (extending MCD-024's \"active "
            "from birth\"). Ozmund works this out alone, unconfirmed by his father, and never "
            "raises it with him. Establishes that Aethelgard knowingly carried a permanent mark of "
            "exactly the danger everyone feared in his son and chose to let it read as an ordinary "
            "mishap rather than a grievance. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1837",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CVIII, \"The Question He Kept for Himself\" -- coming-of-age strand "
            "wave 2, age ~16. Locks a recurring, private adolescent daydream -- never a plan, "
            "never acted on -- in which Ozmund imagines an alternate life defined by an ordinary "
            "craft rather than inheritance (recalling Joren's wheelwright trade, MCD-1776), "
            "explicitly with the succession entirely uncontested and no crisis prompting it. "
            "Resolves internally not into rejection or resentment of his future role but into a "
            "quiet decision that the inheritance is worth more for having once been freely, if "
            "idly, weighed against another option. Explicitly distinguished from any Book-1-era "
            "crown rejection. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1838",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CIX, \"The Match He Chose to Lose\" -- coming-of-age strand wave 2. "
            "Locks a specific personal cost of Ozmund's restraint instinct, isolated for the first "
            "time from the Density Spike itself -- his ordinary physical strength alone, "
            "deliberately throttled at a Greyfen harvest-day wrestling contest out of fear of "
            "misjudging the safe margin under real contest conditions rather than any "
            "supernatural risk. The unremarkable showing this produces costs him the casual "
            "belonging of a local peer group that gathers around the contest's actual winner "
            "instead. A direct companion piece to Chronicle XLVII (MCD-1776). No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1839",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CX, \"The Names He Said Before Sleep\" -- coming-of-age strand wave "
            "2. Locks a private nightly habit, never disclosed to anyone in his youth, of "
            "silently reviewing and specifically naming everyone he dealt with that day before "
            "sleep, striving to recall one true concrete detail about each rather than letting "
            "them collapse into their functional role. Establishes this quiet, self-imposed "
            "discipline as an early, undramatic root of the value later shown fully and publicly "
            "at MAW-084/CC-022 -- seeing Red Beard and, eventually, the Cestari as whole people "
            "rather than roles or cargo. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1840",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CXI, \"The Closest He Ever Came to Losing the Floor\" -- coming-of-"
            "age strand wave 2. Locks a private, told-only-once incident in which an unplanned, "
            "purely instinctive grip -- reflexively catching a wagon harness during a "
            "spooked-horse near-accident on a mountain road -- cracks a solid oak yoke with force "
            "Ozmund never consciously chose or measured. Establishes a genuine, privately-held "
            "fear distinct from every deliberately-tested limit shown elsewhere in the series: "
            "that his instinctive reflexes, formed outside any of his practiced discipline, might "
            "not hold to the same careful threshold his conscious control always has. No one is "
            "harmed in the incident itself. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1841",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CXII, \"The One Afternoon He Let Himself Win\" -- coming-of-age "
            "strand wave 2. Locks a deliberately lighter, warmer entry -- a household "
            "harvest-festival log-toss contest against Osric in which Ozmund, for the first time "
            "in the series, consciously lets his full ordinary physical strength through in a "
            "fully safe, fully witnessed context and wins decisively. Establishes that his "
            "restraint elsewhere is a chosen discipline rather than an involuntary cage, giving "
            "him rare access to uncomplicated pride and belonging on this one occasion. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1842",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CXIII, \"The Words He Kept for No One,\" closing part A of the "
            "coming-of-age strand's wave 2. Locks a private, unceremonial writing habit distinct "
            "from the formal House lineage copying shown in Chronicle XLVIII (MCD-1777) -- "
            "periodically drafting an unaddressed letter beginning \"to whoever asks, someday, "
            "what kind of man I actually was,\" read by no one and eventually burned each time. "
            "Establishes this as Ozmund's most literal act of self-authorship, used to articulate "
            "values (earned trust, being valued apart from his blood, fear of being remembered "
            "only for an unchosen power) with zero audience, ceremony, or performative pressure. "
            "No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    # --- Coming-of-age strand wave 2 part B (MCD-1843-1849, Chronicles CXIV-CXX) ---
    {
        "id": "MCD-1843",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CXIV, \"What He Helped Another Carry\" -- coming-of-age strand wave "
            "2. Young Ozmund extends Val Mirel Kareth's Hollow Stand discipline (MCD-1745) "
            "outward for the first time, finding Osric alone with a private, previously unstated "
            "thirty-year-old grief (his wife's death) and sitting with him in silence rather than "
            "trying to fix it. He learns that the discipline his mother gave him for holding his "
            "own unanswerable weight was \"built to be lent,\" not only for his own use. "
            "Deliberately echoes without restaging the earlier Joren entry (MCD-1776). No new "
            "named characters (Osric reused from MCD-1730)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1844",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CXV, \"The Race He Let Himself Lose\" -- coming-of-age strand wave "
            "2. A rare, unguarded entry of pure joy -- Ozmund and stable boy Cobb (MCD-1772) race "
            "repeatedly in the lower paddock, and Ozmund realizes he has been unconsciously "
            "holding back even in a harmless footrace out of long-ingrained habit. One afternoon "
            "he runs freely for once, wins decisively, and Cobb's cheerful, uncomplicated reaction "
            "to losing teaches him that the careful version of himself is a chosen door, not the "
            "only one available, even though he goes back to holding back the very next day. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1845",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CXVI, \"The Name He Wanted to Be Worth\" -- coming-of-age strand "
            "wave 2. Overhearing two household guardsmen speak admiringly of him as an already-"
            "forming legend, Ozmund experiences a quiet vertigo at realizing he has no control "
            "over the reputation the world is assembling for him. He resolves privately to stop "
            "measuring himself against that external legend and instead measure himself only "
            "against whether he was actually trustworthy to the specific people in front of him "
            "each day -- a distinction he decides is the only one that will ever matter to him. "
            "Purely internal; no new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1846",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CXVII, \"The Test He Set for Himself\" -- coming-of-age strand wave "
            "2. A week-long visit from an unnamed lesser-House retainer who needles him repeatedly "
            "forces Ozmund to confront whether his habitual silence under provocation is still a "
            "genuine choice or has hardened into an unexamined reflex. He deliberately tests the "
            "question by choosing, for one morning, to answer plainly and factually rather than "
            "stay silent -- resolved through plain speech alone, with zero use of the Density "
            "Spike -- and confirms to himself that the restraint remains a tool he wields rather "
            "than a trap he's fallen into. No new named characters; the retainer is deliberately "
            "unnamed and non-recurring."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1847",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CXVIII, \"What He Gave Instead of Kept\" -- coming-of-age strand "
            "wave 2. Years after losing Joren to his own practiced distance (MCD-1776), an unnamed "
            "Greyfen miller's boy shows Ozmund the same open curiosity Joren once did. This time, "
            "catching himself mid-reflex, Ozmund deliberately allows a little more presence and "
            "warmth than the old habit would have permitted -- small gestures, not a confession -- "
            "demonstrating hard-won, incremental growth in how he applies the \"no threshold to "
            "cross\" discipline to ordinary peer contact. No new named characters; the boy is "
            "deliberately left unnamed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1848",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CXIX, \"The Math He Didn't Say Aloud\" -- coming-of-age strand wave "
            "2. Watching Osric's hands begin to show age, Ozmund does the arithmetic of his own "
            "Karesian-inherited long lifespan (extending MCD-101's 89,003-year-old Val Mirel "
            "Kareth) against the ordinary human spans of Osric and Cobb, and confronts the "
            "knowledge that he will very likely outlive both of them by an enormous margin. Rather "
            "than withdrawing to limit future grief, he deliberately chooses to love them at full "
            "measure anyway, privately, without ever burdening either of them with the calculation "
            "-- resolved without despair or any foreshadowed death. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1849",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle CXX, \"The Distance Between Two Evenings,\" closing the entire "
            "70-entry wave-3 batch across all six strands. Ozmund revisits the flooded quarry "
            "below Aldenmoor (MCD-1778) years after his solitary practice there, this time simply "
            "to sit and take stock, synthesizing the full distance traveled across the series "
            "(Draconis, Aethelgard, Val Mirel, Osric, Cobb, Joren, the wider household) without "
            "advancing or foreshadowing any reserved thread. He concludes that a life is made "
            "mostly of its small chosen moments rather than its largest ones, and that he no "
            "longer needs the quarry itself to know who he is -- a quiet, settled close with no "
            "dread and no forward-pointing hook. No new named characters. Closes the coming-of-age "
            "strand at 20 entries total (Chronicles XLVI-L, CVI-CXX) and completes Ozmund's series "
            "at 120 Chronicles total, 20 entries per strand across all six strands."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Abad: "let\'s make sure each of these entries have 20 total entries. logically woven into '
    'our rules and batches" -- executed as a 70-entry wave-3 run across all six Ozmund Chronicle '
    'strands via eight parallel background agents, matching the blanket-authorization precedent '
    'already established for Batches 304-305.'
)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == 70, f"expected 70 new rules, got {len(new_ids)}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 306,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-23, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "Ozmund Verehimu Character Chronicle series, wave 3 -- 70 new entries "
                "(Chronicles LI-CXX, MCD-1780 through MCD-1849) bringing all six thematic "
                "strands (Draconis, Aethelgard, Val Mirel, House politics, Wider Household/"
                "Guard, coming-of-age) to 20 entries each, 120 Chronicles total. Produced via "
                "eight parallel background agents (Draconis +9, Aethelgard +10, Val Mirel +10, "
                "House politics +11, Household/Guard split into two 8/7 sub-waves, coming-of-age "
                "split into two 8/7 sub-waves), each reading its strand's full prior entries and "
                "the profile doc before drafting, collision-checking every new proper noun. All "
                "entries strictly pre-Fulfillment-Ceremony (MCD-025), Aethelgard alive throughout, "
                "no Book-1-era material. Every reserved thread held: Draconis never learns "
                "Ozmund's true nature (the purity-test dynamic, CC-085, is deepened via doubt, "
                "outside provocation, and a near-fatal cost in Chronicle LVII but never broken); "
                "Cassius Verehimu appears in zero entries this wave (excluded entirely, matching "
                "wave 2's precedent); Lucius Blackthorne and Grulak do not appear; the Crown-"
                "Scar's true siphon nature (MCD-290) is never revealed; CC-071 and MCD-319 are "
                "untouched; MCD-318's strangers-until-adulthood constraint is respected throughout "
                "the Val Mirel strand. New proper nouns (Sennick, the Rell and Tamsy families, "
                "Fenna Hallum, Lord Ashvane, the Narrow Door discipline, Bram Corwyth, Iona "
                "Adderwell, Lord Ansel Varnhelt/House Varnhelt, Quartermaster Aldous Prynn, House "
                "Renlow, House Ashmere, Ser Dravot Skarne/House Skarne, Wendell Rowe, Factor Yewen "
                "Ashworth/House Ashworth) were collision-checked by their drafting agents and "
                "re-verified by the orchestrating session against the full live ledger and each "
                "other -- zero collisions found (the ledger's 15 pre-existing substring hits for "
                "'rell' all resolved to unrelated words -- Arellanes, Mirella, Umbrella -- not the "
                "standalone name). " + BATCH_NOTE
            ),
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    ids = [r["id"] for r in ledger["rules"]]
    assert len(ids) == len(set(ids)), "duplicate IDs after merge"
    print(f"OK. Total rules: {len(ledger['rules'])}. Ledger version: {ledger['ledger_version']}. "
          f"Batches: {len(ledger['batches_completed'])}.")


if __name__ == "__main__":
    main()
