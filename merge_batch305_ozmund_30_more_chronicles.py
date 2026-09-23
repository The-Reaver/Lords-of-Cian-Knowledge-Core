#!/usr/bin/env python3
"""Batch 305: 30 more Ozmund Verehimu Character Chronicles (XXI-L), strictly pre-Book-1."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Original invention, chat-drafted 2026-09-23, no source document. Ozmund Verehimu's own "
    "Character Chronicle series, per Abad's direction '30 more' following Batch 304's 19-entry "
    "wave. Drafted by six parallel background agents, one per strand -- Draconis wave 2 (XXI-XXV), "
    "Aethelgard wave 2 (XXVI-XXX), Val Mirel Kareth wave 2 (XXXI-XXXV), House politics wave 2 "
    "(XXXVI-XL), a new Household/Guard strand (XLI-XLV), and a new closing coming-of-age strand "
    "(XLVI-L) -- each grepping canon-ledger.json before inventing any proper noun. All 30 entries "
    "are strictly pre-Fulfillment-Ceremony (MCD-025), matching the standing constraint recorded in "
    "docs/lords-of-cian/character-profiles/ozmund-verehimu.md. A full cross-strand collision sweep "
    "against all 17 new proper nouns introduced this wave (Brenner, Fenwick, Petrin Hallum, Renwick "
    "Farrow, Hesper Vale, the Seventh Cord, Sella, Lord Corvain, House Dellark, Garrow, Berrin "
    "Hollis, Annis Fairweather, Alric Fenmoor, Cobb, Oswin Kade, Osric, Joren) confirmed zero "
    "collisions against the live ledger and against each other. Brings Ozmund's series to 50 "
    "Chronicles total (I-L)."
)

NEW_RULES = [
    {
        "id": "MCD-1750",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXI, \"The Recruit He Almost Turned Away\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxi-the-recruit-he-almost-turned-away.md"
            "), opening a second Draconis-strand wave (Chronicles II-VI), set later in the same "
            "pre-ceremony span, still strictly before the Fulfillment Ceremony (MCD-025), Aethelgard "
            "Verehimu alive. Dramatizes Draconis's (CC-085) standard for judging a House Guard "
            "recruit -- character surviving a bad first impression over polish -- through a "
            "rough-edged candidate, Brenner, who breaks formation to save a groundskeeper's child "
            "rather than hold the line as drilled; Draconis keeps him over his own second's "
            "objection. Ozmund privately absorbs a deliberately general lesson about judging "
            "instinct over performance, kept unspecific per the standing non-foreshadowing "
            "constraint. New minor named figure: Brenner (one-scene)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1751",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXII, \"What He Taught Without Meaning To\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxii-what-he-taught-without-meaning-to."
            "md), set in the same general pre-ceremony span as Chronicle XXI, Aethelgard alive. Red "
            "Beard (Tarn Cestari, VB-020/022/CC-020) recognizes in his own later command habits a "
            "specific practice -- standing still in an unfamiliar room to learn its 'nothing' before "
            "anything can announce itself as a threat, and distributing real trust to subordinates "
            "in small increments well ahead of any actual test -- that traces back to Draconis "
            "(CC-085), absorbed by a young Ozmund watching without either man ever naming it as "
            "instruction. The forward echo into Ozmund's own later command style is carried strictly "
            "in Red Beard's own retrospective narrating voice, never stated within the reconstructed "
            "scene itself. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1752",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXIII, \"The Order He Refused\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxiii-the-order-he-refused.md), set in "
            "the same pre-ceremony span, Aethelgard alive. Dramatizes Draconis (CC-085) refusing a "
            "dishonorable order -- forcibly dispersing peacefully petitioning tenant families over a "
            "Scrip-rate dispute -- issued in Aethelgard's name without Aethelgard's actual word by "
            "Guard-Marshal Fenwick, commanding the House Guard's outer/levy command that Draconis's "
            "own inner escort sits formally beneath; Draconis is relieved of his posting and "
            "threatened with formal review. Ozmund quietly surfaces the true facts to his father "
            "through an ordinary, deniable channel, prompting Aethelgard's own inquiry, which clears "
            "Draconis and turns the review onto Fenwick instead -- extending the 'help at human "
            "scale, credit never taken' pattern established at MCD-1734, with Ozmund's hand never "
            "revealed to Draconis. New minor named figure: Guard-Marshal Fenwick (one-scene "
            "antagonist)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1753",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXIV, \"What He Never Asked For\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxiv-what-he-never-asked-for.md), set "
            "some time after Chronicle XXIII, still pre-ceremony, Aethelgard alive. Dramatizes "
            "Draconis (CC-085) declining a genuine, unindebted honor -- a Sovereign Trust warden's "
            "commission over a southern garrison district, offered on the strength of his own "
            "two-decade record rather than sought -- deliberately distinguished from the earlier "
            "coastal-command refusal (MCD-1733/Chronicle IV): where that refusal paid down an "
            "unexplained debt at real cost, this one reveals his loyalty to House Verehimu functions "
            "as identity rather than ambition, duty, or debt. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1754",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXV, \"The Quiet Between Assignments\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxv-the-quiet-between-assignments.md), "
            "closing the second Draconis-strand wave (Chronicles XXI-XXV), set some time after "
            "Chronicle XXIV, still strictly pre-ceremony, Aethelgard alive. A deliberately "
            "stakes-free entry: an unplanned free day, Draconis and Ozmund fishing at the estate's "
            "lower lake, Draconis sharing ordinary childhood memories of Duskmere (extending rather "
            "than repeating MCD-1734's material) with no threat, test, or near-discovery -- closing "
            "the wave on unguarded companionship, mirroring Chronicle VI's (MCD-1735) closing "
            "register for wave one while remaining content-distinct from it. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1755",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXVI, \"The Debt He Paid in Silence\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxvi-the-debt-he-paid-in-silence.md), "
            "opening the Aethelgard strand's second wave, strictly pre-ceremony. Years before "
            "Ozmund's birth, House Guardsman Petrin Hallum lost the use of his sword arm shielding "
            "Aethelgard from an assassination attempt; the House's public commendation and standard "
            "pension proved inadequate, and Aethelgard has since sent Hallum quarterly support from "
            "his own purse via a neutral factor, with no name attached, for over two decades. Ozmund "
            "discovers the arrangement by accident as a boy and is told directly why it stays "
            "silent: a public restoration would feed the House's comfort with itself, while quiet "
            "money lets a proud man keep both his dignity and his family fed. Extends ARS-381's "
            "'legible instrument of trust' and CC-090's 'dignity through agency' a generation early, "
            "and previews (without naming) the instinct behind the Unchained Legion's later "
            "quiet-aid institutions. New minor character: Petrin Hallum (retired House Guardsman)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1756",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXVII, \"What the Ledger Doesn't Show\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxvii-what-the-ledger-doesnt-show.md), "
            "second entry of the Aethelgard strand's second wave, strictly pre-ceremony. House "
            "Treasurer Renwick Farrow correctly applies the standard river-toll formula, which "
            "nonetheless would bankrupt a settlement hit by an unrelated blight; Aethelgard "
            "validates Farrow's concern about precedent, personally covers the shortfall, then has "
            "Farrow rebuild a standing hardship clause into the formula itself rather than leave "
            "future cases to depend on a lord's personal attention. Dramatizes the divergence "
            "between bureaucratic correctness and actual rightness and Aethelgard's instinct to fix "
            "the underlying system rather than grant a one-off exception, a direct thematic "
            "precursor to Ozmund's later economic/institutional instincts (ARS-375, MCD-279/280). "
            "New minor character: Renwick Farrow (House Treasurer)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1757",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXVIII, \"The Argument They Never Finished\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxviii-the-argument-they-never-finished."
            "md), third entry of the Aethelgard strand's second wave, strictly pre-ceremony. An "
            "adolescent Ozmund argues that being shielded from real stakes isn't discipline but "
            "delay, guaranteeing his first real mistake happens publicly at the worst possible "
            "moment; Aethelgard agrees with the logic but holds that an ordinary heir's mistakes and "
            "Ozmund's carry different categories of risk he hasn't yet learned to calibrate. Neither "
            "position yields, and the disagreement ends unresolved rather than reconciled -- "
            "extending ARS-381's 'dignity through agency' value and later informing, without "
            "resolving it here, Ozmund's refusal ever to make those he commands wait the way he was "
            "made to wait. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1758",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXIX, \"What He Wished for His Son\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxix-what-he-wished-for-his-son.md), "
            "fourth entry of the Aethelgard strand's second wave, strictly pre-ceremony. Told to Red "
            "Beard directly by Hesper Vale (the House physician who has tended Ozmund since infancy) "
            "rather than by Ozmund himself -- a deliberate variation in this strand's narrative "
            "source -- Aethelgard, on an ordinary night in his son's infancy, voices specific hopes "
            "for him: that he learn to trust people faster than caution advises, that he recognize "
            "the rare person who wants nothing from what he can do, that he keep some appetite in "
            "life belonging only to himself, and that he hold future power as something borrowed "
            "rather than owed. Kept deliberately general and atmospheric, with no premonition of "
            "danger or the Fulfillment Ceremony (MCD-025). New minor character: Hesper Vale (House "
            "physician)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1759",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXX, \"The Lesson He Was Still Teaching\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxx-the-lesson-he-was-still-teaching.md)"
            ", closing the Aethelgard strand's second wave, strictly pre-ceremony. Aethelgard shows "
            "an adolescent Ozmund a private, deliberately unfinished journal of governing decisions "
            "he has revised whenever he later judged himself wrong, framing a finished account as "
            "proof a leader has stopped being surprised by himself -- closing wave two on legacy as "
            "a debt continually paid into rather than a sum inherited once. Gives the 'coin on its "
            "edge' motif (MCD-1736/1737/1740) one final light callback without restaging its ritual, "
            "and deliberately does not resolve the strand, consistent with Aethelgard's story "
            "remaining open from the reader's vantage inside this pre-Book-1 timeframe. No new named "
            "characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1760",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXXI, \"What the Stone Count Couldn't Hold\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxxi-what-the-stone-count-couldnt-hold."
            "md), opens the Val Mirel strand's second wave, strictly pre-ceremony, Ozmund age "
            "seventeen. A dispatch during a shared dawn Stone Count (MCD-1741) breaks Val Mirel "
            "Kareth's (MCD-101/CC-004) own discipline for the first time on the page -- a genuine "
            "failure she lives through rather than a lesson she teaches -- and Ozmund holds the "
            "count's rhythm aloud for her until she finds her way back into it herself. Extends the "
            "profile's 'discipline means knowing how to come back' throughline with its origin "
            "moment. The dispatch's content and the name on it are deliberately never revealed. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1761",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXXII, \"The Gift She Almost Didn't Give\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxxii-the-gift-she-almost-didnt-give.md)"
            ", strictly pre-ceremony, Ozmund age twenty. Introduces the Seventh Cord, a private "
            "Kareth War-Order heirloom of Val Mirel Kareth's (MCD-101/CC-004) own Seventh Wing "
            "tactician role -- a cord plaited from every soldier she personally carried off a field "
            "she couldn't otherwise save, worn hidden beneath her vambrace as an unseen tally of "
            "cost rather than a mark of victory. She visibly hesitates over whether a son who has "
            "never commanded or lost anyone has the right to hold it, then gives it to him unworn, "
            "with the condition he not wear it until he understands it from the inside. New proper "
            "noun: the Seventh Cord (artifact), distinct from Lauris Letitia's own Kareth-sister "
            "artifacts (the Convergence, the Gradient, the Patient Stone). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1762",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXXIII, \"What Two Languages Taught Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxxiii-what-two-languages-taught-him.md"
            "), strictly pre-ceremony, Ozmund age twenty-three. Resolving a millrace dispute between "
            "two House Verehimu stewards, Ozmund fuses Val Mirel Kareth's (MCD-101/CC-004) patient, "
            "watch-first Seventh Wing method with House Verehimu's political persuasion register "
            "into a single unconscious act for the first time, rather than alternating between them "
            "-- extending Chronicle XIII's (MCD-1742) 'two currencies against the same debt' "
            "observation into genuine synthesis. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1763",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXXIV, \"The Year She Didn't Come\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxxiv-the-year-she-didnt-come.md), "
            "strictly pre-ceremony, spanning Ozmund's twenty-sixth to twenty-seventh year. Extends "
            "Val Mirel Kareth's (MCD-101/CC-004) 'chosen distance' theme (Chronicle XIV, MCD-1743) "
            "through her longest single absence in the strand -- sparse, impersonal dispatches in "
            "place of visits, and a live, deliberately unresolved doubt on Ozmund's part about "
            "whether her stated choice to stay away has become something closer to circumstance "
            "beyond her control. Closes on a final dispatch carrying four undisclosed words in her "
            "own hand. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1764",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXXV, \"What She Promised Without Words\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxxv-what-she-promised-without-words.md)"
            ", closing entry of the Val Mirel strand's second wave, strictly pre-ceremony, "
            "immediately after Chronicle XXXIV. Val Mirel Kareth (MCD-101/CC-004) returns and, "
            "without a word, places her open palm flat against Ozmund's chest and holds it until his "
            "pulse answers hers -- a deliberate callback to her very first appearance in Chronicle "
            "XII (a hand on a sleeping nine-year-old's shoulder) -- establishing this wordless "
            "gesture as her standing, recurring promise that she will always come when it truly "
            "matters. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1765",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXXVI, \"What the Court Expected\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxxvi-what-the-court-expected.md), opens "
            "the House-politics strand's second wave, strictly pre-ceremony, Ozmund age twenty-two. "
            "Ozmund gives his first public Assize of Harvests address and breaks the ritual's "
            "unspoken convention of charming self-deprecation, instead delivering a plainly honest "
            "account of a difficult season including an unprompted apology to a neighboring holding, "
            "which the court receives with relief rather than offense. Extends CC-090/ARS-381's "
            "dignity-through-agency and discipline-as-armor threads into a full public-court "
            "register, distinct from Chronicle XIX's (MCD-1748) private household-scale defiance. "
            "Aethelgard neither praises nor corrects him, marking it as genuinely Ozmund's own. No "
            "new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1766",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXXVII, \"The Petition No One Else Read\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxxvii-the-petition-no-one-else-read.md)"
            ", second entry of the House-politics strand's second wave, strictly pre-ceremony. "
            "During routine correspondence review, Ozmund personally finds and corrects a tenant "
            "widow's (Sella, new minor character) tax-reassessment petition, buried for months by "
            "the clerks' office's own triage, riding out alone to verify the error himself and "
            "filing the correction through ordinary administrative channels so its true origin is "
            "never traced back to him. Extends the household-scale dignity-through-agency pattern "
            "established with Bevin (MCD-1747) into bureaucratic/institutional scale, per "
            "CC-090/ARS-381. Sella never learns who corrected her assessment. New minor character: "
            "Sella (tenant widow)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1767",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXXVIII, \"What He Learned From Being Underestimated\" (full narrative "
            "text at docs/lords-of-cian/chronicles/ozmund-chronicle-xxxviii-what-he-learned-from-"
            "being-underestimated.md), third entry of the House-politics strand's second wave, "
            "strictly pre-ceremony. During a water-rights negotiation with visiting House Dellark, "
            "its leader Lord Corvain (both new, minor, non-recurring) treats Ozmund as the pleasant, "
            "unremarkable heir and inadvertently reveals, in an aside addressed only to Aethelgard, "
            "that Dellark's usual leverage is a bluff for that season; Ozmund catches it, and the "
            "House secures markedly better terms on a follow-up letter. Deliberately scoped to this "
            "single negotiation as a lesson about listening rather than the origin of any later "
            "strategy of concealment, leaving the deferred Book-1-era 'just a man' Accession Games "
            "pitch untouched. New minor characters: Lord Corvain, House Dellark."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1768",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XXXIX, \"The Feast He Didn't Attend\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xxxix-the-feast-he-didnt-attend.md), "
            "fourth entry of the House-politics strand's second wave, strictly pre-ceremony, Ozmund "
            "age twenty-five. Ozmund skips House Verehimu's obligatory attendance at the regional "
            "Assembly of Harvest's Close to sit through the final days of the House's dying "
            "kennel-master, Garrow (new minor character), who asked not to die alone; Aethelgard "
            "attends alone and spends much of the gathering absorbing other Houses' reading of the "
            "absence as a slight, without ever fully explaining the true reason. A real, specific "
            "external political cost for a real, specific personal choice, distinct from Chronicle "
            "XIX's (MCD-1748) privately contained household defiance. New minor character: Garrow "
            "(kennel-master)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1769",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XL, \"What the House Remembered of Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xl-what-the-house-remembered-of-him.md)"
            ", closing the House-politics strand's second wave. Red Beard synthesizes his own "
            "accumulated retellings -- Bevin (MCD-1747), Marta (MCD-1748), Ysbel (MCD-1749), Garrow "
            "(MCD-1768) -- plus two further unnamed household vignettes, into a single reflection on "
            "how years of small, uncredited decencies quietly became the household's collective "
            "memory of Ozmund, all recalled events themselves occurring pre-Fulfillment-Ceremony. "
            "Closes the wave's theme without resolving or advancing anything about Ozmund's future, "
            "the Crown-Scar, or any reserved thread. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1770",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XLI, \"The Armsmaster's Doubt\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xli-the-armsmasters-doubt.md), opens the "
            "new Wider Verehimu Household/Guard strand, distinct from the dedicated Draconis strand "
            "(Chronicles II-VI). Set in early adolescence, strictly pre-ceremony: Berrin Hollis (new "
            "named character), House Verehimu's armsmaster, spends nearly a year doubting a young "
            "Ozmund's commitment to formal weapons training, reading his deliberately incomplete "
            "guard as a noble's son coasting on his name, before discovering the boy has been "
            "arriving hours early, unsupervised, to work the same forms alone -- extending the "
            "profile's 'discipline as armor' defense mechanism a generation early. New named "
            "character: Berrin Hollis (armsmaster)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1771",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XLII, \"What the Falconer Saw\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xlii-what-the-falconer-saw.md), second "
            "entry in the Wider Verehimu Household/Guard strand. Set in boyhood, strictly "
            "pre-ceremony: Annis Fairweather (new named character), House Verehimu's falconer, gives "
            "Red Beard a small, unwitnessed vignette of an unguarded seven- or eight-year-old Ozmund "
            "laughing openly after being knocked down by a young goshawk -- deliberately stakes-free "
            "and politics-free, matching Chronicle XVIII's household-account register. New named "
            "character: Annis Fairweather (falconer)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1772",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XLIII, \"The Tutor Who Wouldn't Flatter\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xliii-the-tutor-who-wouldnt-flatter.md)"
            ", third entry in the Wider Verehimu Household/Guard strand. Set in adolescence, "
            "strictly pre-ceremony: Master Alric Fenmoor (new named character), House Verehimu's "
            "scholarly tutor, refuses deference to Ozmund's rank, failing a plausible-but-flawed "
            "Scrip-mechanics working outright and demanding real intellectual rigor until, over "
            "roughly two years, the boy shifts from seeking confirmation to genuinely seeking "
            "correction -- establishing a discipline of the mind distinct from Hollis's weapons "
            "training (MCD-1770) and Val Mirel's Kareth War-Order disciplines. New named character: "
            "Master Alric Fenmoor (tutor)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1773",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XLIV, \"What the Stable Boy Taught Him About Fear\" (full narrative "
            "text at docs/lords-of-cian/chronicles/ozmund-chronicle-xliv-what-the-stable-boy-"
            "taught-him-about-fear.md), fourth entry in the Wider Verehimu Household/Guard strand. "
            "Set in boyhood, strictly pre-ceremony, sourced directly from Ozmund rather than "
            "secondhand: Cobb (new named character), a House Verehimu stable boy roughly Ozmund's "
            "own age with no rank or power, handles a newly-broken, dangerous gelding with visibly "
            "shaking hands every morning for two months rather than let fear excuse him from the "
            "work, teaching a young Ozmund that courage and fear coexist rather than one replacing "
            "the other -- the series' first genuine childhood-peer relationship, extending the "
            "profile's 'dignity through agency' value (CC-090/ARS-381). New named character: Cobb "
            "(stable boy)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1774",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XLV, \"What the Guard Owed the House\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xlv-what-the-guard-owed-the-house.md), "
            "closing entry of the Wider Verehimu Household/Guard strand. Set in later adolescence, "
            "strictly pre-ceremony: Sergeant Oswin Kade (new named character), a senior House "
            "Verehimu Guard sergeant whose service predates Colonel Viktor Draconis's own tenure, "
            "gives Red Beard an institutional account of reciprocal obligation between the House "
            "Guard and the family it serves -- injured-guardsman pensions kept whole, fallen "
            "soldiers' families housed as standing policy, retirement treated as earned rather than "
            "granted -- reforms Kade traces to the years the young heir began involving himself in "
            "governance, deliberately distinct in register from Chronicle IV's individual 'The House "
            "Guard's Own Doubt.' New named character: Sergeant Oswin Kade."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1775",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XLVI, \"The First Time He Led\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xlvi-the-first-time-he-led.md), opens "
            "the closing coming-of-age strand of this wave, strictly pre-ceremony, Aethelgard alive "
            "and away from the estate. A flood emergency at the already-locked settlement of Greyfen "
            "(MCD-1738) has young Ozmund, present without formal rank, take real operational "
            "responsibility for the first time -- prioritizing grain stores and evacuation under "
            "time pressure and working the line himself rather than merely directing it -- a "
            "leadership instinct distinct from both Aethelgard's diplomatic register and Val Mirel "
            "Kareth's War-Order command discipline, exercised without any use of the Density Spike. "
            "New named character: Osric, the Verehimu household's senior steward."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1776",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XLVII, \"What Discipline Cost Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xlvii-what-discipline-cost-him.md), "
            "second entry of the closing coming-of-age strand, strictly pre-ceremony. Dramatizes a "
            "real personal cost of the 'no threshold to cross' discipline (CC-015/017/MCD-024) for "
            "the first time -- a near-friendship with a wheelwright's apprentice, Joren, kept "
            "deliberately at arm's length across several of Aethelgard's twice-yearly grain-market "
            "circuits (extending Chronicle I's established custom, MCD-1730), lost to ordinary "
            "relocation (to the already-locked Hold of Khorvane) before Ozmund ever lets it become "
            "what it could have been. Extends the profile's 'discipline as armor' facet from its "
            "cost side rather than its heroic side. New named character: Joren (wheelwright's "
            "apprentice)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1777",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XLVIII, \"The Year He Stopped Asking Why\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xlviii-the-year-he-stopped-asking-why."
            "md), third entry of the closing coming-of-age strand, strictly pre-ceremony. A purely "
            "internal turning point, grounded in the already-locked Drakmund-to-Aethelgard-to-Ozmund "
            "lineage's hand-copied House record (MCD-138) and Val Mirel's Stone Count discipline "
            "(MCD-1741): over the course of a year, Ozmund shifts from resenting/questioning his "
            "unchosen inheritance to consciously choosing what to do with it, the series' clearest "
            "single statement yet of the 'no threshold to cross' and 'discipline as armor' "
            "psychological facets. No combat, no external event. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1778",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle XLIX, \"What He Practiced in the Dark\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-xlix-what-he-practiced-in-the-dark.md)"
            ", fourth entry of the closing coming-of-age strand, strictly pre-ceremony. The series' "
            "most interior, least-witnessed entry to date: alone at night at the already-locked "
            "flooded quarry near Aldenmoor (MCD-1747), young Ozmund deliberately tests the floor "
            "rather than the ceiling of his Density Spike -- the one part of his inheritance "
            "genuinely his to define rather than born into -- extending CC-015/017/MCD-024's 'no "
            "threshold to cross' psychology into its most self-authored register. Narrator Red Beard "
            "explicitly flags this as reconstructed from a single sparse mention, the thinnest "
            "evidentiary base in the series. No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1779",
        "category": "ozmund-character-chronicle",
        "statement": (
            "Ozmund Chronicle L, \"The Man He Was Becoming\" (full narrative text at "
            "docs/lords-of-cian/chronicles/ozmund-chronicle-l-the-man-he-was-becoming.md), closes "
            "the coming-of-age strand and this 30-Chronicle wave, bringing Ozmund's series to 50 "
            "Chronicles total. Set strictly pre-Fulfillment-Ceremony, Aethelgard alive and "
            "unremarkable throughout, no foreshadowing of the Ceremony or anything after it. A quiet "
            "synthesizing entry -- an essentially grown Ozmund, walking the estate wall alone, takes "
            "stock of Draconis's loyalty (MCD-1730-1735), his parents' two inheritances (the "
            "Aethelgard and Val Mirel strands, MCD-1736-1745), the wider household, and his own "
            "private discipline (MCD-1775-1778) -- without resolving any reserved thread (CC-071, "
            "MCD-319, Cassius Verehimu, Lucius Blackthorne, Grulak, the 'Venim' meaning, and the "
            "Draconis/Blackthorne payoffs all remain untouched). No new named characters."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = 'Abad: "30 more."'


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"
    assert len(new_ids) == 30, f"expected 30 rules, got {len(new_ids)}"
    collisions = existing_ids & set(new_ids)
    assert not collisions, f"ID collisions with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 305,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-23, no source document",
            "rule_count": len(NEW_RULES),
            "note": (
                "30 more Ozmund Verehimu Character Chronicles (XXI-L), bringing his series to 50 "
                "entries total. Drafted by six parallel background agents across six strands -- "
                "Draconis wave 2 (XXI-XXV), Aethelgard wave 2 (XXVI-XXX), Val Mirel Kareth wave 2 "
                "(XXXI-XXXV), House politics wave 2 (XXXVI-XL), a new Wider Household/Guard strand "
                "(XLI-XLV, introducing Armsmaster Berrin Hollis, falconer Annis Fairweather, tutor "
                "Alric Fenmoor, stable boy Cobb, and Sergeant Oswin Kade), and a new closing "
                "coming-of-age strand (XLVI-L, Ozmund's own interiority, closing on Chronicle L, "
                "'The Man He Was Becoming'). All 30 entries strictly pre-Fulfillment-Ceremony per "
                "the standing constraint in docs/lords-of-cian/character-profiles/ozmund-verehimu.md"
                ". A full cross-strand collision sweep confirmed zero collisions across all 17 new "
                "proper nouns, against the live ledger and against each other. " + BATCH_NOTE
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
