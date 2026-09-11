#!/usr/bin/env python3
"""Batch 255: Trench Monarch Alias Chronicle waves 22-30 (27 entries)."""
import json
from datetime import date

LEDGER_PATH = "canon-ledger.json"

SOURCE = "Original invention, chat-drafted 2026-09-11, no source document."

BATCH_NOTE = (
    "The Trench Monarch's twenty-second through thirtieth Alias Chronicle waves (9 waves, 27 "
    "entries), drafted under Abad's blanket authorization to continue all eleven aliases' waves "
    "22-30 uninterrupted. All set within the already-established pre-Black-Trench window (Onyx of "
    "Oblivion solo, Mafesto dormant and Obsidian Malice undeployed per MCD-232), none contradicting "
    "the wave-15/wave-21 closures at MCD-650/MCD-1064. Genuinely new registers explored: a failed "
    "Trust charter and the quiet economic sanctions that followed it, closed by a grudging formal "
    "review (MCD-1121, MCD-1138, MCD-1141, MCD-1145); dedicated deep-dives on Whisper of Shadows, "
    "Soulbound Edge, and Cadence Ruin with the gift's first shown personal costs (MCD-1122, "
    "MCD-1127, MCD-1133); Dol Maren's and Corren Halst's first dedicated Trench-Monarch-era solo "
    "entries (MCD-1123, MCD-1137); a labor dispute and a bad harvest the tally method cannot fully "
    "resolve (MCD-1124, MCD-1135); a mass epidemic and a drought, both first-time environmental/"
    "civilian registers (MCD-1129, MCD-1139); the first entry where a failure is unambiguously "
    "Kanja's own command misjudgment (MCD-1136); the first entry where an armed group escalates to "
    "violence citing him as inspiration (MCD-1134); Pell Ostra's first shown skill-limit failure "
    "(MCD-1143); an intimate sealed-well rescue distinct from the prior mine-collapse showcase "
    "(MCD-1144); a payoff to the Kessic flats collateral-cost thread (MCD-1142); and a deliberate "
    "ensemble closer explicitly distinct from the already-locked eve-of-Black-Trench beat "
    "(MCD-1147). No new named characters were introduced anywhere in this run; every entry reused "
    "already-locked crew (Corren Halst, Danne Sok, Maret Vos, Garren Hask, Callum Breck, Efa Gol, "
    "Pell Ostra, Tavin Greer, Dol Maren, Onyx of Oblivion). One new unnamed group label, \"the "
    "Dredge Line's Answer\" (MCD-1134), collision-checked clean against the live ledger. Abad's "
    "approval: \"lets do this 22nd Alias Chronicle wave for any/all of the eleven aliases to the "
    "30th wave and you are to continue uninterrupted until completion this includes rigorous "
    "testing, commit, push to main origin.\""
)

NEW_RULES = [
    {
        "id": "MCD-1121",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Charter Actually Said\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-charter-actually-said.md), Trench Monarch Alias "
            "Chronicle LXIV, wave 22. Rebellion era, pre-Black-Trench. The Trust registrar's charter "
            "offer (MCD-1064) returns after six weeks with an auditor clause that quietly "
            "reinstates Trust oversight of the method's own figures, directly contradicting the "
            "condition Kanja set. Garren Hask catches the clause; Kanja sends the charter back with "
            "it circled rather than sign or reject it outright, leaving the thread deliberately "
            "unresolved and seeding the sanctions arc that follows later this wave-set. No new "
            "named characters -- the registrar (already established, unnamed) and Garren Hask "
            "appear in their established roles."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1122",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Whisper of Shadows Was For\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-whisper-of-shadows-was-for.md), Trench Monarch "
            "Alias Chronicle LXV, wave 22. Rebellion era, pre-Black-Trench -- Onyx of Oblivion solo. "
            "A dedicated, non-combat showcase of Whisper of Shadows used for covert reconnaissance "
            "rather than blind-spot combat nullification: Kanja infiltrates a grain factor's compound "
            "to copy a hidden second ledger proving wage theft, the gift providing not invisibility "
            "but repeated fractional near-misses in a watcher's attention. Establishes the gift's "
            "first explicit cost -- real perceptual/physical strain after sustained use. No new named "
            "characters -- the grain factor is unnamed."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1123",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Dol Maren Built to Fail Safely\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-dol-maren-built-to-fail-safely.md), Trench Monarch "
            "Alias Chronicle LXVI, wave 22, closing the wave. Rebellion era, pre-Black-Trench. Dol "
            "Maren's first dedicated Trench-Monarch-era solo entry: one of his seventeen plank-"
            "bridges (CC-121) fails under an unexpectedly heavy Compliance requisition wagon, but "
            "fails exactly as designed -- sacrificial support beams letting go first, tipping the "
            "wagon safely into the canal rather than collapsing the span under the workers crossing "
            "it. Establishes his engineering philosophy of designing structures to fail predictably "
            "and safely, the direct origin of the load-assessment competence he later carries into "
            "shipwright work. No new named characters -- the wagon's two drivers are unnamed. Closes "
            "the Trench Monarch's twenty-second wave (with \"What the Charter Actually Said,\" "
            "MCD-1121, and \"What Whisper of Shadows Was For,\" MCD-1122)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1124",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Dispute With No Wrong Man In It\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-dispute-with-no-wrong-man-in-it.md), Trench Monarch "
            "Alias Chronicle LXVII, wave 23. Rebellion era, pre-Black-Trench. The first labor "
            "dispute where cross-witnessed verification finds a true, honest wage shortfall with no "
            "owner wrongdoing behind it at all -- a widowed rope-walk owner has paid what she "
            "genuinely has after a Trust tariff collapsed her market, and the true number the method "
            "reveals has no coin behind it to close. Resolves not into restitution but into a "
            "documented, shared, multi-year deficit both sides agree to carry -- the method's honest "
            "arithmetic finding a real gap it is powerless to close. No new named characters -- the "
            "widow and her twelve rope-walkers are unnamed. First entry in the Trench Monarch's "
            "twenty-third wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1125",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Water That Rose Without Warning\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-water-that-rose-without-warning.md), Trench Monarch "
            "Alias Chronicle LXVIII, wave 23. Rebellion era, pre-Black-Trench. An early-snowmelt "
            "flood threatens the low-lying eastern canal rows; a pure evacuation register with no "
            "dispute, no owner, and no Onyx use of any kind -- Kanja, Corren Halst, Danne Sok, and "
            "Maret Vos carry forty families to higher ground before the current turns dangerous. "
            "Distinct from MCD-900's storm-repair labor: this is live rescue against rising water, "
            "not structural shoring. No new named characters -- the elderly dredge hand and the "
            "forty families are unnamed. Second entry in the Trench Monarch's twenty-third wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1126",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Books That Were Built to Pass\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-books-that-were-built-to-pass.md), Trench Monarch "
            "Alias Chronicle LXIX, wave 23, closing the wave. Rebellion era, pre-Black-Trench. The "
            "tally-verification method's first genuine defeat by sophisticated fraud rather than an "
            "honest gap or a bad-faith imitation: a tannery owner presents cross-witnessed books that "
            "pass every check because they were deliberately constructed to survive the audit, real "
            "workers replaced by hires trained to corroborate a fabricated ledger. Caught not by the "
            "figures but by Efa Gol's outside instinct that the story is 'too clean,' prompting a "
            "permanent procedural patch requiring an independent witness with no prior relationship "
            "to the owner. No new named characters -- the tannery owner and both sets of workers are "
            "unnamed. Closes the Trench Monarch's twenty-third wave (with \"The Dispute With No "
            "Wrong Man In It,\" MCD-1124, and \"The Water That Rose Without Warning,\" MCD-1125)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1127",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Blade Remembered Before Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-blade-remembered-before-him.md), Trench Monarch "
            "Alias Chronicle LXX, wave 24. Rebellion era, pre-Black-Trench. A rare private, wordless "
            "exchange between Kanja and Onyx of Oblivion clarifies Soulbound Edge as a renewable, "
            "revocable bond rather than possession -- the blade carries an unspecified centuries-deep "
            "history of prior wielders, including one whose bond it ended on its own terms for asking "
            "it to be a weapon it would not agree to be. No combat, no new named characters. First "
            "entry in the Trench Monarch's twenty-fourth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1128",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Man They Punished for Standing Near Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-man-they-punished-for-standing-near-him.md), Trench "
            "Monarch Alias Chronicle LXXI, wave 24. Rebellion era, pre-Black-Trench. An owner's men "
            "beat an entirely uninvolved dockhand -- guilty of nothing but exchanging a dozen words "
            "with Kanja at a public well -- as a warning against mere proximity to the reputation, "
            "distinct from MCD-901's targeted cooperator. The tally method has no figure to offer "
            "him; Kanja instead makes ordinary proximity itself uninformative by publicly speaking "
            "with a dozen more unconnected bystanders. No new named characters -- the dockhand is "
            "unnamed. Second entry in the Trench Monarch's twenty-fourth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1129",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Summer the Canal Went Dry\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-summer-the-canal-went-dry.md), Trench Monarch Alias "
            "Chronicle LXXII, wave 24, closing the wave. Rebellion era, pre-Black-Trench. A drought "
            "empties the founding canal to a cracked silt bed, the first entry deliberately inverting "
            "the water-and-flood motif that dominates the alias's prior Chronicles -- Dol Maren's "
            "plank-bridges stand over nothing, and an owner exploits the resulting wagon-traffic "
            "bottleneck to divert goods out of sight. Garren Hask adapts the tally method to wagon "
            "manifests and wheel-rut counts, catching the diversion through documentation alone, no "
            "combat or Onyx use. No new named characters -- the diverting owner is unnamed. Closes "
            "the Trench Monarch's twenty-fourth wave (with \"What the Blade Remembered Before Him,\" "
            "MCD-1127, and \"The Man They Punished for Standing Near Him,\" MCD-1128)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1130",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Owners Who Took Him to Court\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-owners-who-took-him-to-court.md), Trench Monarch "
            "Alias Chronicle LXXIII, wave 25. Rebellion era, pre-Black-Trench. Eleven owners petition "
            "Canal House to have the tally-verification method itself declared coercion regardless of "
            "its accuracy -- the first entry where Kanja personally answers for his own methods in an "
            "adversarial legal proceeding, distinct from the Trust's own institutional inquest "
            "(MCD-645) and the registrar's cooperative charter offer. The petition is denied, but "
            "Kanja concedes one genuine prior overreach by a crew member unprompted, keeping the "
            "outcome honest rather than a clean vindication. No new named characters -- the eleven "
            "owners and the magistrate are unnamed. First entry in the Trench Monarch's twenty-fifth "
            "wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1131",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Tavin Greer Filed Late\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-tavin-greer-filed-late.md), Trench Monarch Alias "
            "Chronicle LXXIV, wave 25. Rebellion era, pre-Black-Trench. An active, in-era Tavin "
            "Greer entry, distinct from his two prior reflection/legacy entries (MCD-403, MCD-644): "
            "still in Directorate service, he is ordered to compile accurate strike-timing "
            "intelligence against Kanja's crew and files it precisely, honestly, and four days late "
            "under an entirely defensible pretext, causing the resulting strike to arrive after the "
            "site correction has already concluded. Kanja never learns the cause. No new named "
            "characters beyond the already-locked Tavin Greer. Second entry in the Trench Monarch's "
            "twenty-fifth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1132",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Birth That Stopped the Count\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-birth-that-stopped-the-count.md), Trench Monarch "
            "Alias Chronicle LXXV, wave 25, closing the wave. Rebellion era, pre-Black-Trench. Kanja "
            "halts an active five-owner negotiation mid-session to clear a blocked street for a "
            "midwife during a difficult labor, the reputation's usual unstoppable momentum "
            "deliberately paused for one uninvolved life; the negotiation is shown surviving the "
            "interruption intact and resumes without incident. No new named characters -- the "
            "laboring woman, the midwife, and the five owners are unnamed. Closes the Trench "
            "Monarch's twenty-fifth wave (with \"The Owners Who Took Him to Court,\" MCD-1130, and "
            "\"What Tavin Greer Filed Late,\" MCD-1131)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1133",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Duel Fought to Its Own Rhythm\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-duel-fought-to-its-own-rhythm.md), Trench Monarch "
            "Alias Chronicle LXXVI, wave 26. Rebellion era, pre-Black-Trench -- Onyx of Oblivion "
            "solo. A dedicated Cadence Ruin deep-dive against a duelist trained in a maximally "
            "rhythmic, ceremonial fighting style, deliberately complementing MCD-402's arrhythmic "
            "duelist: the gift inhabits and compresses the duelist's own cadence, winning in under two "
            "minutes, but leaves Kanja's own reflexes briefly mistuned to ordinary, non-rhythmic "
            "threats afterward -- the power's first shown post-use cost. No new named characters -- "
            "the duelist is unnamed. First entry in the Trench Monarch's twenty-sixth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1134",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Men Who Fought in His Name\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-men-who-fought-in-his-name.md), Trench Monarch Alias "
            "Chronicle LXXVII, wave 26. Rebellion era, pre-Black-Trench. A twelve-person group calling "
            "itself the Dredge Line's Answer forms citing Kanja as inspiration and burns a storehouse "
            "in his name before verifying any figures -- the first entry where the reputation is "
            "hijacked toward sanctioned violence, distinct from a rival organizer's competing "
            "non-violent method (MCD-481) and an accidentally-botched imitation of the method "
            "(MCD-947). Kanja disavows the act publicly and corrects the group directly rather than by "
            "force; eight of twelve accept tutelage in the real method. New unnamed group label \"the "
            "Dredge Line's Answer,\" collision-checked clean against the live ledger. No new named "
            "individual characters. Second entry in the Trench Monarch's twenty-sixth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1135",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Bad Harvest Left Behind\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-bad-harvest-left-behind.md), Trench Monarch "
            "Alias Chronicle LXXVIII, wave 26, closing the wave. Rebellion era, pre-Black-Trench. A "
            "blight-driven regional grain shortfall across three upriver districts gives the tally "
            "method nothing to verify and no owner to correct; Kanja instead uses two years of "
            "cross-district trust to organize a voluntary, honest accounting and redistribution of "
            "scarce grain, with Efa Gol running the logistics. Two districts refuse and are not "
            "coerced; nobody starves, but no district is made whole either -- the method's real "
            "institutional legacy paying off in a form it was never built to produce. No new named "
            "characters. Closes the Trench Monarch's twenty-sixth wave (with \"The Duel Fought to Its "
            "Own Rhythm,\" MCD-1133, and \"The Men Who Fought in His Name,\" MCD-1134)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1136",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Cost of the Call He Made\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-cost-of-the-call-he-made.md), Trench Monarch Alias "
            "Chronicle LXXIX, wave 27. Rebellion era, pre-Black-Trench. The first entry in this "
            "alias's run where a failure is unambiguously Kanja's own command misjudgment rather than "
            "an opponent's tactic or the method's structural limit: choosing to move a raid a day "
            "earlier than his own reconnaissance warranted, he puts a three-week volunteer in the path "
            "of an unrostered patrol he'd have caught with one more day of watching, and the volunteer "
            "dies. Kanja institutes a standing two-day-minimum watching rule afterward, applied to "
            "himself first. No new named characters -- the volunteer is unnamed. First entry in the "
            "Trench Monarch's twenty-seventh wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1137",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Corren Halst Never Told the Others\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-corren-halst-never-told-the-others.md), Trench "
            "Monarch Alias Chronicle LXXX, wave 27. Rebellion era, pre-Black-Trench. Corren Halst's "
            "first dedicated origin entry -- the last of the four founding figures (alongside Danne "
            "Sok, Maret Vos, and Garren Hask) without one. Reveals he was freed once before, by a "
            "rebellion cell that collapsed to internal betrayal, and approached Kanja's crew only "
            "after three weeks of careful observation, ultimately trusting Garren Hask's meticulous, "
            "cross-witnessed ledger before he trusted Kanja himself. No new named characters beyond "
            "the already-locked Corren Halst. Second entry in the Trench Monarch's twenty-seventh "
            "wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1138",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Trust Took Back Quietly\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-trust-took-back-quietly.md), Trench Monarch "
            "Alias Chronicle LXXXI, wave 27, closing the wave. Rebellion era, pre-Black-Trench. "
            "Direct fallout of MCD-1121's failed charter: rather than revising the auditor clause, "
            "the Trust launches quiet, individually deniable licensing-review sanctions against "
            "owners who cooperated with Warehouse Twelve, a friction the method's documentation "
            "strength cannot directly counter. Kanja absorbs the cooperating owners' practical costs "
            "through crew resources and Dol Maren's engineering competence rather than confronting the "
            "Trust directly, and no cooperating owner backs away from the tally table. No new named "
            "characters. Closes the Trench Monarch's twenty-seventh wave (with \"The Cost of the Call "
            "He Made,\" MCD-1136, and \"What Corren Halst Never Told the Others,\" MCD-1137)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1139",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fever That Wasn't His\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fever-that-wasnt-his.md), Trench Monarch Alias "
            "Chronicle LXXXII, wave 28. Rebellion era, pre-Black-Trench. A mass canal-borne fever "
            "outbreak strikes dozens of dredge workers at once, distinct from Kanja's own earlier "
            "personal illness (MCD-942) -- the tally method is entirely inapplicable, and Kanja "
            "organizes boiled-water distribution, quarantine, and care rotation instead, with Efa Gol "
            "running logistics and Pell Ostra tracing the outbreak to a collapsed drainage joint. "
            "Seven deaths are recorded as an honest, unprevented cost; the district's sanitation rule "
            "is expanded into a standing quarantine protocol. No new named characters. First entry in "
            "the Trench Monarch's twenty-eighth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1140",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Fighter Who Studied the Sword\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-fighter-who-studied-the-sword.md), Trench Monarch "
            "Alias Chronicle LXXXIII, wave 28. Rebellion era, pre-Black-Trench -- Onyx of Oblivion "
            "solo. A mercenary who spent four months studying secondhand accounts of Onyx's own "
            "fighting patterns nearly defeats Kanja by compressing two independent lines of attack "
            "into one motion, landing the first wound from an opponent specifically targeting the "
            "sword's reputation; Kanja wins by tracking her physical tell rather than relying on "
            "Cadence Ruin or Veil Piercer, grounded in ordinary trained skill underneath the gifts "
            "(extending MCD-643). No new named characters -- the mercenary is unnamed. Second entry "
            "in the Trench Monarch's twenty-eighth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1141",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Owners Who Broke the Blacklist Themselves\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-owners-who-broke-the-blacklist-themselves.md), Trench "
            "Monarch Alias Chronicle LXXXIV, wave 28, closing the wave. Rebellion era, pre-Black-"
            "Trench. The licensing-review sanctions from MCD-1138 collapse not through Trust "
            "concession but because uninvolved owners begin voluntarily seeking tally verification as "
            "a shield against the same reviews, forcing the Trust to quietly let the original "
            "sanctions lapse rather than expose the coordinated punishment. A deliberately mixed, "
            "morally complicated resolution rather than a clean vindication. No new named characters. "
            "Closes the Trench Monarch's twenty-eighth wave (with \"The Fever That Wasn't His,\" "
            "MCD-1139, and \"The Fighter Who Studied the Sword,\" MCD-1140)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1142",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Grew Back on the Kessic Flats\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-grew-back-on-the-kessic-flats.md), Trench Monarch "
            "Alias Chronicle LXXXV, wave 29. Rebellion era, pre-Black-Trench. A direct, deliberately "
            "incomplete payoff to MCD-1062: a year into the crew's reclamation labor, six of the "
            "salt-killed orchard's original forty grafted trees survive, and the unnamed woman "
            "returns to see them. Garren Hask amends the original blank-owner ledger page with an "
            "honest addition -- 'six grafts survived... the rest remains owed' -- without pretending "
            "the loss has been made whole. No new named characters -- the woman is unnamed, matching "
            "her original entry. First entry in the Trench Monarch's twenty-ninth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1143",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Pell Ostra Couldn't Keep Safe\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-pell-ostra-couldnt-keep-safe.md), Trench Monarch "
            "Alias Chronicle LXXXVI, wave 29. Rebellion era, pre-Black-Trench. Pell Ostra's second "
            "dedicated entry, extending her origin vignette (MCD-629) with her first genuine skill-"
            "limit failure: a professional thief, hired by a wealthier owner, studies and defeats her "
            "urgency-built countermeasures through sheer patience, stealing records recoverable only "
            "because Garren Hask kept independent copies. Ostra rebuilds her protection system with "
            "patience-resistant elements afterward. No new named characters -- the professional thief "
            "is unnamed. Second entry in the Trench Monarch's twenty-ninth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1144",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"The Well That Closed Over the Boy\" (full narrative text at "
            "docs/lords-of-cian/chronicles/the-well-that-closed-over-the-boy.md), Trench Monarch "
            "Alias Chronicle LXXXVII, wave 29, closing the wave. Rebellion era, pre-Black-Trench. A "
            "seven-year-old falls eleven feet down a sealed, narrow well shaft; distinct from "
            "MCD-636's mine-collapse rescue, the shaft is too narrow for Veil Piercer or any Onyx "
            "application to matter at all. Dol Maren assesses the crumbling stone's remaining "
            "strength and lowers Kanja down by hand-played rope; the boy is pulled up unhurt through "
            "pure engineering judgment and physical rescue work, no gift, no blade. No new named "
            "characters -- the boy and his mother are unnamed. Closes the Trench Monarch's twenty-"
            "ninth wave (with \"What Grew Back on the Kessic Flats,\" MCD-1142, and \"What Pell Ostra "
            "Couldn't Keep Safe,\" MCD-1143)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1145",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Auditors Never Found\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-auditors-never-found.md), Trench Monarch Alias "
            "Chronicle LXXXVIII, wave 30. Rebellion era, pre-Black-Trench. Closes the charter/"
            "sanctions institutional thread opened at MCD-1121: an eleven-day exhaustive Trust review "
            "of Warehouse Twelve's own books, launched as a last pretext to discredit the method, "
            "finds nothing but honest, cross-witnessed figures and issues a grudging, bureaucratic "
            "statement that the practice meets or exceeds the Trust's own documentation standard -- no "
            "apology, no acknowledgment of the sanctions campaign, the closest thing to formal "
            "vindication the method ever receives. No new named characters -- the review team is "
            "unnamed. First entry in the Trench Monarch's thirtieth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1146",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What Garren Hask Packed That Week\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-garren-hask-packed-that-week.md), Trench Monarch "
            "Alias Chronicle LXXXIX, wave 30. Rebellion era, pre-Black-Trench. A quiet, unexplained "
            "instinct: Garren Hask, with no flagged threat or report behind it, spends an entire week "
            "restocking emergency supplies and filing redundant ledger backups across every site the "
            "crew uses. Neither he nor Kanja names the feeling as anything specific; the extra "
            "preparation sits unused for weeks afterward, a deliberately understated dramatic-irony "
            "register distinct from MCD-648's explicit, shared sense of coming change. No new named "
            "characters beyond the already-locked Garren Hask. Second entry in the Trench Monarch's "
            "thirtieth wave."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "MCD-1147",
        "category": "kanja-alias-chronicle",
        "statement": (
            "\"What the Districts Kept After Him\" (full narrative text at "
            "docs/lords-of-cian/chronicles/what-the-districts-kept-after-him.md), Trench Monarch "
            "Alias Chronicle XC, wave 30, closing the wave. Rebellion era, pre-Black-Trench. An "
            "ensemble closer, explicitly not a restaging of MCD-650's already-locked eve-of-the-"
            "Black-Trench closure: on an unspecified ordinary afternoon, Kanja walks the full dredge "
            "line, finding Corren Halst, Danne Sok, Maret Vos, Garren Hask, Callum Breck, Efa Gol, and "
            "Pell Ostra each doing established, unremarkable work that no longer needs his direct "
            "involvement -- the method's accumulated self-sufficiency, not battle foreboding, is the "
            "entry's center. No new named characters. Closes the Trench Monarch's thirtieth wave (with "
            "\"What the Auditors Never Found,\" MCD-1145, and \"What Garren Hask Packed That Week,\" "
            "MCD-1146) and the full run of waves 22 through 30."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]


def main():
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert len(NEW_RULES) == 27, f"expected 27 new rules, got {len(NEW_RULES)}"

    new_ids = [r["id"] for r in NEW_RULES]
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within NEW_RULES"

    existing_ids = {r["id"] for r in ledger["rules"]}
    collisions = set(new_ids) & existing_ids
    assert not collisions, f"ID collision with existing ledger: {collisions}"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 255,
            "date": str(date.today()),
            "source": "Original invention, chat-drafted 2026-09-11, no source document",
            "rule_count": len(NEW_RULES),
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = str(date.today())

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs found post-write!"

    print(
        f"OK. Total rules: {len(ledger['rules'])}. "
        f"Ledger version: {ledger['ledger_version']}. "
        f"Batches: {len(ledger['batches_completed'])}."
    )


if __name__ == "__main__":
    main()
