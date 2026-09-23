#!/usr/bin/env python3
"""Batch 304: 19 more Ozmund Verehimu Character Chronicles (II-XX), strictly pre-Book-1."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-23, no source document. Ozmund Verehimu's own "
    "Character Chronicle series, per Abad's direction 'add 19 more' following Chronicle I "
    "(MCD-1730, Batch 303). Drafted by four parallel background agents, one per strand -- Draconis "
    "(II-VI), Aethelgard (VII-XI), Val Mirel Kareth (XII-XVI), and House politics/broader life "
    "(XVII-XX) -- each grepping canon-ledger.json before inventing any proper noun. All 19 entries "
    "are strictly pre-Fulfillment-Ceremony (MCD-025), matching the standing constraint recorded in "
    "docs/lords-of-cian/character-profiles/ozmund-verehimu.md. A cross-strand collision was caught "
    "and fixed before locking: the Aethelgard strand's Chronicle IX introduced dike-warden 'Corwen "
    "Dask' and the House-politics strand's Chronicle XVIII independently introduced a different "
    "kitchen scullion also named 'Corwen' -- the scullion was renamed to 'Bevin' (grepped clean) "
    "throughout Chronicle XVIII before this merge."
)

NEW_RULES = [
    {
        "id": "MCD-1731",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle II, \"The Second Test\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-ii-the-second-test.md), the second entry "
            "in Ozmund Verehimu's Character Chronicle series, set several years after Chronicle I "
            "(MCD-1730), still strictly pre-Fulfillment-Ceremony (MCD-025). At a formal House "
            "reception years into Draconis's service, an unnamed impostor attendant carries a "
            "resealed, poisoned private-reserve bottle toward the high table; Draconis catches it "
            "through protocol and vigilance alone (a stranger's unpracticed hands on a tray, not a "
            "blade), while the General privately recognizes the same threat and deliberately withholds "
            "a Density Spike intervention that would have ended it in an instant, extending "
            "MCD-024/CC-015/017's \"no threshold to cross\" suppression pattern into a political/"
            "intelligence register distinct from Chronicle I's combat one. Deepens the CC-085 purity-"
            "test dynamic without advancing Draconis's ignorance in either direction. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1732",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle III, \"What He Never Reported\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-iii-what-he-never-reported.md), the third "
            "entry in Ozmund Verehimu's Character Chronicle series, set some years after Chronicle II, "
            "still pre-ceremony. A sparring-gallery beam collapse and a startled-horse incident give "
            "Draconis (CC-085) a genuine near-suspicion of the truth behind MCD-024/CC-015/017 -- not "
            "raw strength, but the total absence of an ordinary fear response -- which he privately "
            "investigates for a season, then deliberately talks himself out of pursuing and never "
            "reports up the household chain, confessed to the General only once, decades later. The "
            "series' designated near-discovery entry: it stays a near-miss, confirming loyalty as the "
            "active mechanism of Draconis's own continued ignorance rather than advancing toward "
            "actual discovery, and sets up (without dramatizing) that the eventual reveal will land as "
            "vindication rather than betrayal. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1733",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle IV, \"The House Guard's Own Doubt\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-iv-the-house-guards-own-doubt.md), the "
            "fourth entry in Ozmund Verehimu's Character Chronicle series, set in the same general "
            "pre-ceremony span as Chronicle III. Draconis (CC-085) turns down a prestigious coastal "
            "command to keep the inner escort, drawing open guardhouse criticism from a senior peer "
            "that he cannot answer except with an unconvincing \"a promise on a road once,\" a real "
            "institutional cost, witnessed firsthand by the General from a doorway, that he can never "
            "explain or repay without revealing the truth beneath it. Extends CC-085's \"loyalty "
            "Ozmund can't fully use\" framing into a concrete career price rather than an abstract "
            "misunderstanding, and deepens the profile's \"purity test\" relationship-pattern note. "
            "Deliberately does not advance Draconis any closer to the truth than Chronicle III already "
            "did. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1734",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle V, \"A Small Mercy\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-v-a-small-mercy.md), the fifth entry in "
            "Ozmund Verehimu's Character Chronicle series, set in the same general pre-ceremony span "
            "as Chronicles III-IV. Draconis (CC-085) confides real personal history to the General for "
            "the first time -- his hometown, the river town of Duskmere, and his younger sister Halyn, "
            "whose flood-damaged home he cannot afford to repair and would never ask the House to fund "
            "-- and the General, deliberately declining to rebuild it outright with his own hands, "
            "instead routes an anonymous, unremarkable sum through the House's ordinary almsfund so "
            "Draconis never learns whose hand actually answered it. Extends the profile's \"dignity "
            "through agency\" value (CC-090/ARS-381) into a new register: help at deliberately human "
            "scale rather than any display of true capability, consistent with his established "
            "preference for the harder, more controlled path (MCD-318). Introduces Halyn and Duskmere, "
            "both collision-checked clean against the full ledger; both one-scene, off-page figures."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1735",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle VI, \"The Watch He Chose to Keep\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-vi-the-watch-he-chose-to-keep.md), the "
            "sixth entry in Ozmund Verehimu's Character Chronicle series, closing the five-entry "
            "Draconis strand opened in Chronicle I. During a storm that leaves Aethelgard feverish and "
            "the household on edge, Draconis (CC-085) voluntarily extends his post outside the "
            "General's chamber through an entire night well past his roster's end, for no reason duty "
            "requires, an act of devotion at its most unforced -- no threat, no test, no near-discovery, "
            "just a choice freely made. Closes the strand without resolving or advancing any reserved "
            "thread: Draconis remains as unaware of MCD-024/CC-015/017 at the close as at Chronicle I's "
            "start, and the eventual reveal stays reserved for a future, Book-1-era-or-later entry per "
            "the profile's Game Plan. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1736",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle VII, \"What Never Had to Be Learned\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-vii-what-never-had-to-be-learned.md) -- "
            "the Aethelgard strand's opening entry in Ozmund Verehimu's Character Chronicle series, "
            "set strictly pre-Book-1 with Aethelgard alive and raising a very young Ozmund. Dramatizes "
            "MCD-024/CC-015/017 directly: the Density Spike as fully active and consciously governed "
            "since before memory, with no Awakening or threshold ever crossed, forcing Aethelgard -- "
            "who per this entry carries no power of his own and cannot take the Spike from his son or "
            "understand it from the inside -- to build a purely procedural discipline around it (a "
            "coin spun on its edge to force patience before temper, a nightly spoken accounting of "
            "whether the Spike \"answered to anything\" that day) rather than an experiential one. "
            "Extends CC-090's \"earned through disciplined living\" framing of Ozmund's adult power a "
            "generation early. Introduces the \"coin on its edge\" motif as a recurring device for this "
            "strand, reused in Chronicles VIII and XI. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1737",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle VIII, \"The Lesson in Losing\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-viii-the-lesson-in-losing.md) -- the "
            "Aethelgard strand's second entry, set strictly pre-Book-1. Aethelgard enforces a standing "
            "house rule barring the Density Spike from the sparring floor, and for eleven straight "
            "years beats a young Ozmund at swordwork on the strength of ordinary, hard-won skill "
            "rather than any power of his own, refusing to let his son's coming inheritance substitute "
            "for what he hasn't yet earned. Closes on Aethelgard's explicit reasoning -- \"there has to "
            "be at least one room... where you're just a student, losing\" -- extending ARS-381's "
            "dignity-through-agency value and CC-090's earned-power framing to Aethelgard's own "
            "deliberate parenting choice. Reuses the \"coin on its edge\" motif from Chronicle VII "
            "(MCD-1736) in a second context. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1738",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle IX, \"What a Lord Owes His People\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-ix-what-a-lord-owes-his-people.md) -- the "
            "Aethelgard strand's third entry, set strictly pre-Book-1. On a routine governance circuit "
            "through the already-locked Verehimu Wetlands, Aethelgard finds a levee at the settlement "
            "of Greyfen falsely reported repaired, personally verifies dike-warden Corwen Dask's "
            "grievance by walking the structure himself, and publicly apologizes to Dask by name "
            "before issuing the repair order, on the principle that a lord who cannot be embarrassed "
            "in front of those he's failed will fail them again. Ties directly, unknown to either "
            "character at the time, to the ethos Ozmund's Unchained Legion is later built on (extends "
            "MCD-279/280, ARS-381, CC-090). New minor named character (Corwen Dask) and new place name "
            "(Greyfen, within the already-locked Verehimu Wetlands), both grepped clean against the "
            "live ledger before drafting."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1739",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle X, \"The Night He Was Afraid For Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-x-the-night-he-was-afraid-for-him.md) -- "
            "the Aethelgard strand's fourth entry, set strictly pre-Book-1, told to Red Beard only "
            "once. A private late-night scene in which Aethelgard admits to an older Ozmund a "
            "generalized, non-specific fear that a power like the Density Spike carries a cost or "
            "target no father's teaching can fully protect against -- deliberately atmospheric rather "
            "than any premonition of the Fulfillment Ceremony (MCD-025), naming no threat and no "
            "suspect. Gives the profile's \"grief converts directly into infrastructure\" psychological "
            "layer a concrete, three-dimensional father to eventually have lost, closing on "
            "Aethelgard's distinction between fearing for someone and doubting them. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1740",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XI, \"What He Carried From His Own Father\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xi-what-he-carried-from-his-own-father.md) "
            "-- the Aethelgard strand's closing entry, set strictly pre-Book-1. Aethelgard tells "
            "Ozmund, for the only time, the full story of Drakmund Verehimu (MCD-138, the original "
            "Crown-Scar recipient, ~5,000 years old) -- the \"Evil King\" Aethelgard himself exiled -- "
            "and reveals that the \"coin on its edge\" ritual (Chronicles VII/VIII, MCD-1736/1737) was "
            "Drakmund's own teaching device first, repurposed from a lesson in leverage into one of "
            "restraint. Frames Drakmund's tyranny as a corruption of will under the Crown-Scar's "
            "command architecture rather than a Density Spike he never possessed (consistent with "
            "WC-004), and closes the strand's inheritance-versus-choice theme without naming or "
            "foreshadowing \"Venim,\" per the profile's explicit reserved-thread instruction. No new "
            "named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1741",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XII, \"Her Son, Not Her Line\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xii-her-son-not-her-line.md), opens the "
            "Val Mirel strand of Ozmund's Character Chronicle series. Set roughly nine years before the "
            "Fulfillment Ceremony (MCD-025), Aethelgard alive and present but deliberately non-"
            "intervening: Val Mirel Kareth (MCD-101/CC-004/CC-016) teaches a nine-year-old Ozmund an "
            "original Kareth War-Order discipline, the Stone Count -- stillness that outlasts urgency "
            "rather than performs it -- directly against House Verehimu's court instinct to always be "
            "seen doing something, giving Ozmund his first on-page moment of holding both inheritances "
            "at once. Plants formative groundwork for his already-locked Solid-Dense Terra 'immovable "
            "foundation' physics (WC-006) and his Book 2 command-discipline at the repulsion of "
            "General Baryon (MCD-279/280). Narrated by Red Beard (Tarn Cestari) per VB-020/022/CC-020, "
            "reconstructed from a story Ozmund told him years later. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1742",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XIII, \"The Reckoning of a Seventh Wing Tactician\" (full narrative text "
            "at docs/lords-of-cian/chronicles/ozmund-chronicle-xiii-the-reckoning-of-a-seventh-wing-"
            "tactician.md), second entry in the Val Mirel strand. Set roughly fifteen years before the "
            "Fulfillment Ceremony (MCD-025), Aethelgard alive but absent (referenced only): facing a "
            "patient raiding band on the grain road, Val Mirel Kareth's Seventh Wing tactical "
            "discipline (MCD-101/CC-004) -- watching a threat long enough to learn what it hides "
            "rather than acting on what it shows -- is set directly against a House Verehimu "
            "seneschal's political toll-negotiation method for the identical problem, with fifteen-"
            "year-old Ozmund taken along only to observe. Resolves with Ozmund understanding both "
            "approaches as the same discipline paid in different currencies, coin against patience, "
            "rather than opposed philosophies. Narrated by Red Beard (Tarn Cestari) per VB-020/022/"
            "CC-020, reconstructed from a story Ozmund told him twice, years apart, with no factual "
            "variance between tellings. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1743",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XIV, \"What She Chose Not to Fight\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xiv-what-she-chose-not-to-fight.md), third "
            "entry in the Val Mirel strand. Set roughly nineteen years before the Fulfillment Ceremony "
            "(MCD-025), Aethelgard alive but present only in reference: after a court reception where "
            "Val Mirel Kareth is treated with hollow, distant deference rather than genuine belonging, "
            "nineteen-year-old Ozmund confronts her directly about her chosen absence from his "
            "upbringing. She explains it as a deliberate protection of his own earned identity -- "
            "refusing to let him grow up inside a shadow he'd never get to prove he didn't need -- "
            "extending the profile's 'consent and earned loyalty' values layer and 'author of your own "
            "will' throughline, while making clear the choice costs her as much as it costs him. "
            "Deliberately left unresolved rather than healed. Narrated by Red Beard (Tarn Cestari) per "
            "VB-020/022/CC-020, reconstructed from a story Ozmund told him only once, very late. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1744",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XV, \"The War-Sister's Warning\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xv-the-war-sisters-warning.md), fourth "
            "entry in the Val Mirel strand. Set roughly twenty-two years before the Fulfillment "
            "Ceremony (MCD-025): on the last night of her longest visit, Val Mirel Kareth tells "
            "twenty-two-year-old Ozmund of an old, unnamed debt carried from the war to a woman she "
            "never names, torn apart from her by the war itself -- an oblique, deliberately "
            "unconfirmed forward reference toward MCD-101/MCD-137 (Val Saeryn and Val Mirel Kareth as "
            "war-sisters, both alive, Val Saeryn in deep cover) that neither names Val Saeryn nor "
            "Kanja nor explains the cousin relationship, fully consistent with MCD-318's locked fact "
            "that the cousins were essentially strangers until adulthood. She instructs him to "
            "recognize and honor the debt without demanding explanation if it is ever called through a "
            "line he cannot predict. Narrated by Red Beard (Tarn Cestari) per VB-020/022/CC-020, "
            "reconstructed from a story Ozmund only fully understood the possible weight of much "
            "later. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1745",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XVI, \"A Different Kind of Armor\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xvi-a-different-kind-of-armor.md), closing "
            "entry in the Val Mirel strand. Set roughly twenty-five years before the Fulfillment "
            "Ceremony (MCD-025), Aethelgard alive but present only in reference: after the death of an "
            "unnamed old House Guard soldier who helped raise him, twenty-five-year-old Ozmund's "
            "Verehimu-taught public composure leaves him with nowhere to put his grief; Val Mirel "
            "Kareth teaches him a second original Kareth War-Order discipline, the Hollow Stand -- "
            "built from the same root as the Stone Count (MCD-1741) but aimed at holding grief fully "
            "through rather than folding it away -- and stays with him through it, giving the strand "
            "its emotional high point and the project's first sustained, three-dimensional scene of "
            "warmth between mother and son. Plants the emotional root of the profile's 'grief "
            "converted directly into infrastructure' defense-mechanism layer, later expressed at "
            "Legion scale. Narrated by Red Beard (Tarn Cestari) per VB-020/022/CC-020, reconstructed "
            "from a story Ozmund told him only once, near the end. No new named characters; closes the "
            "five-entry Val Mirel strand."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1746",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XVII, \"The Cousin Who Smiled Too Easily\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xvii-the-cousin-who-smiled-too-easily.md), "
            "first entry in a new House-politics/broader-life strand of his series, set strictly "
            "pre-Fulfillment-Ceremony (MCD-025). At the confirmation feast for a minor family land-"
            "holding at Aldenmoor, Cassius Verehimu (CC-082-084) delivers a private, charm-wrapped "
            "needle about Ozmund's unearned privilege -- true in its surface claim, blind to "
            "everything it doesn't see -- establishing ordinary House-branch envy rather than any plot "
            "beat; Cassius reads here as merely 'the easiest man in the family to have in a room,' with "
            "nothing that foreshadows his later role in Aethelgard's assassination. Extends CC-090's "
            "discipline-vs-privilege framing from the outside perspective of a relative who only sees "
            "what Ozmund was given. New place name Aldenmoor, collision-checked clean; no new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1747",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XVIII, \"What the Servants Knew\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xviii-what-the-servants-knew.md), second "
            "entry in the House-politics/broader-life strand, set strictly pre-ceremony. Retold to Red "
            "Beard decades later not by Ozmund but by Bevin, a former House Verehimu kitchen scullion "
            "who as an eleven-year-old let the ovens go cold before dawn baking; young Ozmund quietly "
            "relights and tends the ovens himself rather than waking the household or the head cook, "
            "asks Bevin his name, and never mentions the incident again, letting the boy keep his own "
            "credit rather than turning the moment into a display of his own mercy. Dramatizes the "
            "profile's 'dignity through agency' value (extends CC-090/ARS-381) at household scale, a "
            "generation before it recurs with Red Beard (MAW-084) and Lilith (MCD-134), and varies the "
            "series' narrative channel by routing the retelling through the person who lived it rather "
            "than through Ozmund. Introduces one new minor named character, Bevin, a House Verehimu "
            "kitchen scullion -- renamed from an initial draft of 'Corwen' before locking, to avoid a "
            "same-batch collision with Chronicle IX's unrelated dike-warden Corwen Dask (MCD-1738)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1748",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XIX, \"The First Time He Said No\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xix-the-first-time-he-said-no.md), third "
            "entry in the House-politics/broader-life strand, set strictly pre-ceremony, Ozmund age "
            "fifteen. Asked to publicly humiliate linen-stores supervisor Marta before the full staff "
            "over a miscounted shipment as an object lesson, per the House's inherited minor-justice "
            "tradition, he refuses the public setting outright, hears her explanation privately "
            "instead, and levies a proportionate rather than punitive fine -- a small, tightly bounded "
            "act of defiance within ordinary household administration, deliberately scaled far below "
            "and never gesturing toward the later crown rejection (MCD-025). Extends the profile's "
            "'dignity through agency' and 'consent and earned loyalty' values a decade before either is "
            "tested at real scale. Introduces one new minor named character, Marta, a House Verehimu "
            "laundress; the Seneschal is left unnamed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1749",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XX, \"What the Crown-Scar Was Called Before\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xx-what-the-crown-scar-was-called-before."
            "md), fourth and closing entry in this House-politics/broader-life wave, spanning his "
            "infancy through boyhood, strictly pre-ceremony. His nursemaid Ysbel privately called the "
            "mark 'the Waking Weight' rather than the hall's formal 'Crown-Scar,' and passed down a "
            "nursery-worn House legend that Drakmund Verehimu (MCD-138) himself, late in his "
            "five-thousand-year life, described it as something that 'listened harder than it was "
            "listened to, and gave less than it took' -- atmospheric, pre-understanding language that "
            "resonates forward toward the Crown-Scar's true siphon/root-access-tether nature (MCD-290) "
            "without naming, explaining, or spelling out the mechanism itself. Consistent with "
            "MCD-024/CC-015/017's 'no Awakening, present before memory' biology and the profile's 'no "
            "threshold to cross' psychological layer. Introduces one new minor named character, Ysbel, "
            "Ozmund's infant nursemaid. Closes this 19-entry wave (Chronicles II-XX)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "add 19 more."'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 304,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-23, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "19 more Ozmund Verehimu Character Chronicles (II-XX), bringing his series to 20 "
                "entries total. Drafted by four parallel background agents across four strands -- "
                "Draconis (II-VI, deepening the purity-test relationship across several registers, "
                "closing on his most unforced act of devotion), Aethelgard (VII-XI, a real, three-"
                "dimensional father-son relationship built around discipline, governance, loss, and "
                "the Drakmund lineage, using an invented 'coin on its edge' motif as recurring "
                "through-line), Val Mirel Kareth (XII-XVI, giving Ozmund's previously-unwritten mother "
                "real depth for the first time via two new Kareth War-Order disciplines, the Stone "
                "Count and the Hollow Stand, plus an oblique, non-naming forward-hint toward her "
                "war-sister bond with Val Saeryn Kareth per MCD-318's strangers-until-adulthood "
                "constraint), and House politics/broader life (XVII-XX, a strictly unremarkable "
                "Cassius Verehimu cameo per CC-082-084, a servant's-eye-view humility scene, a small-"
                "scale act of household defiance kept well below the eventual crown rejection, and a "
                "closing atmospheric entry on what the Crown-Scar was called before anyone understood "
                "it, gesturing toward MCD-290 without explaining it). All 19 entries strictly "
                "pre-Fulfillment-Ceremony per the standing constraint in "
                "docs/lords-of-cian/character-profiles/ozmund-verehimu.md. One real cross-strand "
                "naming collision was caught and fixed before locking (see MCD-1747's note). Files "
                "were committed to the repo as they completed, satisfying the Stop hook's clean-"
                "working-tree requirement, with the ledger merge itself running only after all four "
                "agents' output and the cross-strand collision sweep were complete. " + BATCH_NOTE
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
