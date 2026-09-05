#!/usr/bin/env python3
"""Batch 59: converts the Phase 2 pre-Book-1 homage-era conversational
development (docs/lords-of-cian/phase2-homage-era-development.md) into
locked canon-ledger.json material under a new prefix, PH2-. Covers all
five NYC territories/leaders, the Areito Policy-era underworld trio,
Xaragua's 21-figure supporting cast (bundled into six cluster rules),
all five LA territories/leaders, LA's supporting cast, and the Sankofa
crack-era twist trio -- plus one rule capturing the naming convention
itself as a standing writer's-guide fact. Every individual piece was
already drafted in full and explicitly approved in-conversation
("locked" / "lock it" / "proceed" / "confirm Guanin and lock it") one
territory or character group at a time; this batch is the final
conversion step Abad explicitly authorized in one instruction."""
import json

LEDGER_PATH = "canon-ledger.json"

SOURCE = (
    "Phase 2 pre-Book-1 homage-era conversational development, chat-drafted "
    "2026-09-05, no external source document -- original invention. Fully "
    "tracked at docs/lords-of-cian/phase2-homage-era-development.md. Every "
    "territory, leader, and character below was drafted in full and "
    "explicitly approved one piece at a time across the same 2026-09-05 "
    "conversation before this batch converted the whole set into the "
    "ledger."
)

NEW_RULES = [
    {
        "id": "PH2-001",
        "category": "phase2-homage-nyc-territory",
        "statement": (
            "Phase 2 homage era (a separate World per MCD-313): Xaragua is "
            "the Bronx-equivalent territory, named for a real Taino "
            "chiefdom (in what is now Haiti) once ruled by Anacaona. "
            "Supplies the five-territory alliance's raw, uncompromising "
            "force."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-002",
        "category": "phase2-homage-nyc-leader",
        "statement": (
            "Ogoun Xarey leads Xaragua, homage to Jean-Jacques Dessalines, "
            "designated 'the Mightiest Hero' of the homage era. Name from "
            "Ogou Feray, the Haitian Vodou warrior-lwa of iron, fire, and "
            "liberation invoked at the 1791 Bois Caiman ceremony; 'Xarey' "
            "echoes Xaragua. Rose under a political mentor who believed "
            "the old empire could be reasoned with (shaped by the real "
            "Toussaint Louverture, referenced in backstory only, not a "
            "separate character); that mentor was taken by a lie dressed "
            "as a peace conference and died in a foreign cell. Ogoun "
            "Xarey's defining response: no partial freedom, no "
            "negotiating with the hand that held the chain -- he tore the "
            "negotiated middle out of the old banner himself. Revered as "
            "a liberator; also a source of unresolved grief in Xaragua "
            "for a total-war doctrine that never learned to stop being at "
            "war. Signature ability, 'No Second Master': cannot be "
            "controlled, only killed -- any attempt to restrain, capture, "
            "poison, or negotiate with him under duress fails and "
            "redirects as a killing strike. Straightforward violence can "
            "still hurt him; the ability specifically punishes control, "
            "making careful institutional enemies exactly what it's built "
            "to destroy."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-003",
        "category": "phase2-homage-nyc-territory",
        "statement": (
            "Areito is the Harlem-equivalent territory, named for the "
            "real Taino ceremonial song/dance/gathering held in the "
            "batey. Its underworld (numbers, corners, the criminal "
            "economy) is the alliance's supply line and intelligence "
            "network; its Renaissance (art, music, the exemplary and "
            "beautiful) is its legitimacy and recruitment engine."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-004",
        "category": "phase2-homage-nyc-leader",
        "statement": (
            "Kwame Ade leads Areito, homage to Malcolm X, explicitly "
            "equally formidable to Ogoun Xarey (not a force-multiplier "
            "archetype, matched combat-tier). 'Kwame' is an Akan "
            "day-name and also Kwame Nkrumah's name, fitting Malcolm X's "
            "post-Mecca Pan-Africanist turn; 'Ade' is Yoruba for crown. "
            "Rises out of the same underworld he'll later be asked to "
            "save people from, running under a different street name "
            "during his Areito years; imprisonment is where the "
            "reinvention happens, and that self-remade certainty is his "
            "actual power, not physical dominance. Undergoes a second "
            "reinvention late in his arc (mirroring the real Mecca "
            "pilgrimage and NOI break), costing him old allies and "
            "marking him for death by people who once called him "
            "brother. Signature ability, conviction as armor: violence "
            "thrown by anyone acting on doubt, hesitation, or a "
            "half-measure simply doesn't land. Only someone matching his "
            "own absolute certainty can hurt him, meaning the one real "
            "threat to him was always going to come from someone who "
            "once stood exactly where he stood."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-005",
        "category": "phase2-homage-nyc-territory",
        "statement": (
            "Yara is the Brooklyn-equivalent territory, its name tied to "
            "the 1868 'Grito de Yara,' the opening cry of Cuba's Ten "
            "Years' War. Its own founding myth holds it as the oldest "
            "free ground in the alliance, settled before Xaragua ever "
            "burned or Areito ever sang."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-006",
        "category": "phase2-homage-nyc-leader",
        "statement": (
            "Yalokona leads Yara, homage to Shirley Chisholm. Name built "
            "from 'Lokono,' the real self-name of the Arawak people of "
            "Guyana (Chisholm's mother's homeland), meaning 'the people' "
            "-- Taino and Lokono are the same language family. Leads by "
            "inherited independence, not conquest or martyrdom: every "
            "institution that tried to own her compliance failed, "
            "including her own movement when it wanted her to wait her "
            "turn for someone more electable; she ran anyway. Signature "
            "ability, 'Unbought and Unbossed': nothing whose purpose is "
            "to make her stop, comply, or disappear can succeed against "
            "her -- money, threat, blackmail, or force, all under one "
            "principle. Vulnerability: the immunity only holds in the "
            "light, with a witness or a record present; something done "
            "to her genuinely in the dark, unwitnessed, off the record, "
            "can still land. Augmentation, 'The Caucus': any alliance she "
            "personally brokers between two parties becomes binding in a "
            "way neither side can secretly break -- plausibly why the "
            "alliance holds together at all. Augmentation, 'The Door "
            "That Stays Open': any barrier she personally breaks stays "
            "broken behind her, permanently, for everyone who comes "
            "after."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-007",
        "category": "phase2-homage-nyc-territory",
        "statement": (
            "Guanin is the Queens-equivalent territory, named for a real "
            "Taino/pan-Caribbean term for the prestige gold-copper alloy "
            "caciques traded as a mark of status -- prestige earned and "
            "exchanged rather than seized by force."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-008",
        "category": "phase2-homage-nyc-leader",
        "statement": (
            "Eri Kotoko leads Guanin, homage to Jackie Robinson. 'Eri' is "
            "Yoruba for witness/proof/evidence; 'Kotoko' is the Akan word "
            "for porcupine, tied to the real Twi proverb 'Kum apem a, "
            "apem beba' (kill a thousand, a thousand more will come). "
            "Chosen by a patron who needs him to succeed on condition "
            "that whatever is done to him, he cannot answer in kind, not "
            "for years; he holds the space anyway, becoming undeniable "
            "through excellence while everyone waits for him to crack. "
            "When the bargain ends he becomes one of the loudest, most "
            "uncompromising voices in Guanin. Carries real, documented "
            "public friction with Kwame Ade (their real-world "
            "counterparts sharply disagreed, in print, over strategy), "
            "kept as genuine unresolved alliance tension. Signature "
            "ability, 'The Unanswered Blow': every insult, attack, or "
            "provocation he doesn't answer in the moment is banked, "
            "returning later at a target and time of his choosing with "
            "total precision. Cost: only works through deliberate, "
            "conscious release -- lashing out in real anger resets the "
            "banked force to nothing."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-009",
        "category": "phase2-homage-nyc-territory",
        "statement": (
            "Boriken is an invented fifth NYC-adjacent territory (not a "
            "real borough, no Staten Island homage), named for the real "
            "pre-colonial Taino name for Puerto Rico, root of 'Boricua.' "
            "Fills the alliance's thematic gap in organized mutual aid "
            "and direct action as community institution-building: the "
            "network itself -- clinics, breakfast programs, occupied "
            "buildings turned into shelters -- meaning the alliance can "
            "survive losing a fight in any one place."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-010",
        "category": "phase2-homage-nyc-leader",
        "statement": (
            "Guani leads Boriken, homage to Felipe Luciano and the NYC "
            "Young Lords (one of the era's two flagship organizations "
            "alongside the Black Panthers). Name is the real Taino word "
            "for hummingbird. Starts as a street poet whose words spread "
            "faster than he can travel; when the city lets his "
            "neighborhood rot he puts the city's own refused garbage "
            "back at its front door and takes over a hospital wing to "
            "run health screenings the city won't fund (echoing the real "
            "1969 Garbage Offensive and the Young Lords' breakfast/clinic "
            "programs), both working because a hundred people who never "
            "spoke to each other move on his word at the same hour. "
            "Signature ability, 'No Single Point': his real self is "
            "never located in only one place -- every clinic, occupied "
            "building, and rooftop meeting carries a genuine fragment of "
            "his authority, so capturing or killing 'him' in one "
            "location doesn't end him. Cost: entirely relational, not "
            "personal -- an enemy who attacks the institutions themselves "
            "rather than hunting the man is the one force that wears him "
            "down."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-011",
        "category": "phase2-homage-nyc-underworld",
        "statement": (
            "Kwasi Owolabi, 'the Policy King of Areito,' is the "
            "underworld power standing above a young, not-yet-reinvented "
            "Kwame Ade during his Areito street years. Homage to "
            "Ellsworth 'Bumpy' Johnson, the Harlem numbers-racket power "
            "broker of the Great Migration era. 'Kwasi' is an Akan "
            "Sunday-born day-name (witty, unbothered, philosophical "
            "temperament); 'Owolabi' is a real Yoruba name meaning "
            "roughly 'wealth is born of honor.' A composite 'twist' "
            "character built on crime-fiction narrative DNA (Vito "
            "Corleone's outsider-builds-respect arc; Michael Corleone's "
            "cost-of-power isolation; Thomas Shelby's WWI-veteran "
            "always-three-moves-ahead mind, haunted by a dead "
            "brother-in-arms; Alfie Solomons' digressive negotiating "
            "style flipping warmth to threat inside one sentence; "
            "Nikolai Luzhin's hidden layer -- Policy profits quietly "
            "funding the network young Kwame Ade first encounters; "
            "Michael Sullivan Sr./Tommy Angelo's conscience thread -- "
            "nothing touches a child, a private accounting of every "
            "person the business has cost him, one boy he shields from "
            "the life entirely; Vito Scaletta/Lincoln Clay's "
            "veteran-operator arc, paying off in a patient dismantling "
            "of the rival organization when they finally burn down what "
            "he built), none reused as names, only as skeleton."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-012",
        "category": "phase2-homage-nyc-underworld",
        "statement": (
            "Nia, Kwasi Owolabi's mentor and the one who built Policy "
            "before him. Homage to Stephanie 'Madame Queen' St. Clair, "
            "Bumpy Johnson's real historical mentor and boss, an "
            "Afro-Martinican immigrant who fiercely and publicly resisted "
            "an Italian mob incursion into Harlem's Policy racket in the "
            "1930s. Name is Swahili for 'purpose' (renamed 2026-09-05 "
            "from 'Nzinga,' the historical Angolan warrior-queen's name, "
            "for pronounceability -- word-initial 'Nz-' is hard for "
            "English readers). Chose Kwasi as her successor specifically "
            "because he was the only man in her organization who never "
            "once tried to take Policy from her by force."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-013",
        "category": "phase2-homage-nyc-underworld",
        "statement": (
            "Nunzio Ferro is the antagonist of Areito's Policy-era saga, "
            "built on Gyp Rosetti's psychology: a fragile ego that reads "
            "even a neutral 'good luck' as a mortal insult, launching "
            "disproportionate, spiraling retaliation out of pure spite. "
            "Represents the era's real Italian-American mob incursion "
            "into Harlem's Policy racket, reframed as an original "
            "character rather than the real historical figures or their "
            "fictionalized-TV analog. He is the reason the conflict "
            "escalates far past anything business logic would justify, "
            "and the reason Kwasi Owolabi's opposite trait (discipline) "
            "ultimately wins. His organization is referred to as 'the "
            "Downtown Combine.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-014",
        "category": "phase2-homage-nyc-supporting-cast",
        "statement": (
            "Xaragua's Dominican-roots supporting cast: Cibao (homage: "
            "Sebastian Lemba), name from the real Taino term for "
            "Hispaniola's central mountain stronghold region -- a "
            "half-legendary ancestral figure from centuries before Ogoun "
            "Xarey, the first man to turn the mountains into a refuge "
            "for the escaped and hunted. Guama (homage: Juan Pablo "
            "Duarte; renamed 2026-09-05 from 'Guarocuya' for "
            "pronounceability), a real Taino cacique name -- the "
            "idealist who lights Xaragua's independence movement "
            "generations before Ogoun Xarey, founds the secret society "
            "that starts it all, refuses the throne he made possible, "
            "dies sidelined by harder men. Kwabena (homage: Gregorio "
            "Urbano Gilbert), Akan Tuesday-born name -- an 18-year-old "
            "who shoots an occupier alone, unordered, then years later "
            "crosses the sea to fight beside Yaque (PH2-018), rising to "
            "captain under him. Baiguate (homage: Francisco Caamano), a "
            "real Taino waterfall name meaning roughly 'hidden water' -- "
            "trains for years in secret with allies abroad, returns, and "
            "dies within two weeks of landing."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-015",
        "category": "phase2-homage-nyc-supporting-cast",
        "statement": (
            "Xaragua's 19th-century Cuban-line supporting cast: Akewi "
            "(homage: Jose Marti), Yoruba for 'poet' -- unites rival "
            "factions through conviction, breaks publicly with his own "
            "generals over principle, reconciles years later, dies "
            "riding at the enemy line in his first battle. Chuma "
            "(homage: Antonio Maceo), a pan-Bantu word for iron -- "
            "refuses a peace that leaves slavery intact even when "
            "refusing costs him everything, serves directly under "
            "Bohio. Bohio (homage: Carlos Manuel de Cespedes), Taino "
            "for house/home -- frees the enslaved people of his own "
            "household and arms them before declaring anything to "
            "anyone else."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-016",
        "category": "phase2-homage-nyc-supporting-cast",
        "statement": (
            "Xaragua's 20th-century Cuban-underground supporting cast: "
            "Kwaku (homage: Julio Antonio Mella), Akan Wednesday-born -- "
            "a student agitator, exiled, shot in the back at 25, "
            "chronologically the outlier of this cluster. Imole (homage: "
            "Frank Pais), Yoruba for 'light' -- runs the underground by "
            "principle, times a city-wide uprising to a landing that "
            "comes late by hours, dies in the street at 22, recruits and "
            "mentors Ina and Iranti directly. Ina (homage: Vilma Espin), "
            "Yoruba for 'fire' -- an engineer who builds weapons for the "
            "cause, recruited by Imole, becomes courier between the "
            "mountains and the exiles abroad. Aabo (homage: Haydee "
            "Santamaria), Yoruba for 'shelter' -- survives torture and "
            "the murder of everyone she loved in one failed attack, "
            "later builds an institution sheltering exactly who her own "
            "revolution might otherwise discard. Iranti (homage: Celia "
            "Sanchez), Yoruba for 'memory' -- builds the reception "
            "network years before it's needed, keeps the record of the "
            "whole war, works side by side with Ina."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-017",
        "category": "phase2-homage-nyc-supporting-cast",
        "statement": (
            "Extends PH2-002 (Ogoun Xarey): his Haiti-era supporting "
            "cast, two of whom fold directly into his own profile as "
            "named mentor/officer. Mino (homage: Victoria 'Gran Toya' "
            "Montou), the real Fon/Dahomey term for the warrior women "
            "Europeans called 'Amazons' ('our mothers') -- the woman who "
            "taught a young Ogoun Xarey to fight with his hands and a "
            "blade before he ever held a banner, enslaved beside him, "
            "later honored as kin; a second, distinct mentor from the "
            "political-mentor figure in his backstory (one taught him "
            "ideas, the other taught him war). Chui (homage: Sanite "
            "Belair; renamed 2026-09-05 from 'Ngo' for pronounceability), "
            "Swahili for 'leopard' -- an officer under Ogoun Xarey's "
            "command, captured in an ambush, demands the harder death "
            "sentence instead of the lesser one so she and her husband "
            "die together, facing forward, no blindfold. Jagun (homage: "
            "Charlemagne Peralte; renamed 2026-09-05 from 'Jagunjagun'), "
            "Yoruba for 'warrior' -- a generation-later guerrilla leader "
            "against a different occupier, betrayed and killed by "
            "infiltrators in his own camp, his corpse displayed as a "
            "warning that instead becomes a martyr-icon. Otito (homage: "
            "Baron de Vastey), Yoruba for 'truth' -- the philosopher who "
            "writes the first real unmasking of the whole colonial "
            "system by name, becoming the intellectual root of what "
            "Xaragua later claims to stand for."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-018",
        "category": "phase2-homage-nyc-supporting-cast",
        "statement": (
            "Yaque (homage: Augusto Cesar Sandino), a real Taino river "
            "name meaning roughly 'the path' -- a foreign ally, not "
            "Xaragua's own son, who refuses to disarm when every other "
            "faction does and is assassinated the same night he dined as "
            "a guest of the government that promised him peace. Kwabena "
            "(PH2-014) fought at his side and rose to captain under him "
            "-- a real historical connection (Gilbert served under "
            "Sandino)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-019",
        "category": "phase2-homage-nyc-supporting-cast",
        "statement": (
            "Xaragua's Mirabal-Sisters supporting cast (three files "
            "opened, one survivor): Ile (homage: Patria Mirabal), Yoruba "
            "for 'home' -- the eldest, devout, quiet, turns her own "
            "house into the weapons cache and safe house nobody "
            "suspects. Akin (homage: Minerva Mirabal), Yoruba for "
            "'brave/heroic' -- the ringleader, earns a law degree the "
            "state then refuses to let her use, recruits her own "
            "sisters, the fiercest of the three. Itan (homage: Maria "
            "Teresa Mirabal), Yoruba for 'story' -- the youngest, "
            "radicalized through love and loyalty before ideology, "
            "keeps a diary from childhood to the eve of her death. "
            "Kesho (homage: Dede Mirabal; renamed 2026-09-05 from "
            "'Nkrabea' for pronounceability), Swahili for 'tomorrow' -- "
            "the sister who survives, raises the orphaned children, and "
            "spends her life making sure the other three are never "
            "forgotten."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-020",
        "category": "phase2-homage-la-territory",
        "statement": (
            "Sankofa is the South Central-equivalent LA territory, "
            "named for the Akan concept 'go back and get it.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-021",
        "category": "phase2-homage-la-leader",
        "statement": (
            "Baale leads Sankofa, homage to Alprentice 'Bunchy' Carter -- "
            "leader of the Slauson Renegades street gang, radicalized in "
            "prison (first toward Malcolm X/the Nation of Islam, then "
            "Eldridge Cleaver's Black Panther politics), founder of the "
            "Southern California Black Panther chapter. Name is a real "
            "Yoruba title for a local community head, a direct "
            "translation of Carter's real nickname 'Mayor of the "
            "Ghetto.' Assassinated alongside his co-founder Kra (homage: "
            "John Huggins) during a Panther/US-Organization conflict a "
            "real, documented FBI COINTELPRO campaign deliberately "
            "inflamed with forged letters and cartoons. Commands total "
            "loyalty from men who used to answer to no one -- not "
            "through force, but because everyone who's raised a hand "
            "against him ends up serving him afterward; dies not in open "
            "combat but ambushed by a conflict manufactured by people "
            "who never once confronted him directly. Signature ability, "
            "'The Turn': anyone who attacks Baale directly, if they "
            "survive the exchange, becomes bound to serve him from that "
            "point on -- charisma at an almost physical intensity. Cost: "
            "only works in person, one at a time, face to face; cannot "
            "reach across distance, through intermediaries, or through a "
            "conspiracy that never shows its face."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-022",
        "category": "phase2-homage-la-territory",
        "statement": (
            "Aztlan is the East LA-equivalent territory, named for the "
            "real mythic ancestral homeland the Chicano movement invoked "
            "for itself (Nahuatl vocabulary used for this territory and "
            "its cast, per the naming convention's extension to "
            "Chicano-anchored material, PH2-034)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-023",
        "category": "phase2-homage-la-leader",
        "statement": (
            "Ollin leads Aztlan, homage to David Sanchez, founder of the "
            "Brown Berets, central organizer of the 1968 East LA school "
            "walkouts and the 1970 Chicano Moratorium. Name is Nahuatl "
            "for 'movement,' also a real Aztec calendar day-sign "
            "(renamed 2026-09-05 from 'Cuauhtli,' Nahuatl for 'eagle,' "
            "for pronounceability -- the Nahuatl 'tl' sound doesn't "
            "exist in English). Builds the first real paramilitary "
            "structure his community has ever had, wins two of the era's "
            "defining victories through organized discipline -- then "
            "loses the whole thing from the inside, because he never "
            "listened to the people who built it beside him: his first "
            "woman minister, Iya (homage: Gloria Arellanes), led every "
            "woman in the organization out in 1970 over unaddressed "
            "sexism, a schism that outlasted the group's external "
            "enemies. Signature ability, 'The Formation': when Ollin "
            "stands at the center of a group he's personally organized "
            "and drilled, that group fights and moves as a single, "
            "dramatically amplified force. Cost: the moment real, "
            "ignored grievance inside his own ranks reaches its breaking "
            "point, the formation fractures explosively, leaving "
            "everyone in it worse off than if they'd never organized at "
            "all."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-024",
        "category": "phase2-homage-la-territory",
        "statement": (
            "Atunbi is the Watts-equivalent territory, named for the "
            "Yoruba concept 'reborn.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-025",
        "category": "phase2-homage-la-leader",
        "statement": (
            "Oluwole leads Atunbi, homage to Ted Watkins, who fled a "
            "lynching threat in Mississippi as a teenager, became a UAW "
            "organizer, and founded the Watts Labor Community Action "
            "Committee in the direct aftermath of the August 1965 Watts "
            "uprising. Name is a real Yoruba name meaning roughly 'the "
            "Lord builds the house.' Answers a burned neighborhood not "
            "with anger but with his hands -- clearing vacant lots, "
            "turning rubble into gardens, then hospitals, then jobs, "
            "refusing charity without ownership attached, under the real "
            "motto 'Don't Move... Improve.' Signature ability, 'Don't "
            "Move, Improve': wherever he stays rooted for a sustained "
            "stretch, the ground becomes more resilient and livable, a "
            "slow reclamation nothing can permanently undo. Cost: "
            "glacially slow, requires him to stay in place, useless "
            "against anything fast enough to strike and leave before it "
            "takes hold."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-026",
        "category": "phase2-homage-la-territory",
        "statement": (
            "Ijoko is the Compton-equivalent territory, named for the "
            "Yoruba word for 'seat/throne,' root of 'ijoba' "
            "(government)."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-027",
        "category": "phase2-homage-la-leader",
        "statement": (
            "Adwoa leads Ijoko, homage to Doris Davis, Compton's first "
            "female City Clerk, elected mayor in 1973, among the first "
            "Black women to govern a U.S. city of real size, governing "
            "through white flight and a hollowing tax base. Name is an "
            "Akan day-name for a girl born on Monday, linked to a calm, "
            "composed temperament. Takes the chair everyone told her a "
            "woman shouldn't sit in, runs the room with an iron hand "
            "under a warm laugh, spends her term holding the line "
            "against a decline composure alone can't reverse. No real "
            "throughline connects her era to Compton's later "
            "gangsta-rap-era reputation -- that stays a separate, later "
            "chapter, not conflated here. Signature ability, 'The Iron "
            "Hand in the Velvet Glove': no insult, mockery, or attempt "
            "to destabilize her through disrespect can rattle her -- "
            "every jab makes her grip on the room visibly steadier. "
            "Cost: only defends against social/political attacks, does "
            "nothing against real, impersonal economic forces working "
            "against her."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-028",
        "category": "phase2-homage-la-territory",
        "statement": (
            "Orin is the Leimert Park-equivalent territory, named for "
            "the Yoruba word for 'song.'"
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-029",
        "category": "phase2-homage-la-leader",
        "statement": (
            "Onilu leads Orin, homage to Horace Tapscott, who walked "
            "away from a touring jazz career with Lionel Hampton to "
            "found the Underground Musicians Association / Pan Afrikan "
            "Peoples Arkestra, central to the real 'Watts Renaissance' "
            "cultural movement. Name is Yoruba for 'drummer.' Quits the "
            "road at the height of a real career because none of it was "
            "going home with him, spends the rest of his life building "
            "something that can't be bought, only shared. Signature "
            "ability, 'The Ark': everyone who genuinely hears him play "
            "together in the same room carries a real, lasting bond to "
            "everyone else who heard it with them. Cost: the instant "
            "anyone tries to sell, commercialize, or perform it for "
            "fame, the binding vanishes completely and permanently for "
            "that performance."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-030",
        "category": "phase2-homage-la-supporting-cast",
        "statement": (
            "Aztlan/Sankofa's LA supporting cast: Mati (homage: Sal "
            "Castro), Nahuatl root meaning 'to know' -- a history "
            "teacher at East Gate High (wholly invented school name) who "
            "builds pride in Chicano students, becomes the "
            "inside-the-schools instigator of Aztlan's defining walkout "
            "while Ollin organizes the outside paramilitary support; "
            "arrested and charged, charges collapse two years later. "
            "Ohun (homage: Ruben Salazar), Yoruba for 'voice/sound' -- a "
            "journalist covering Aztlan's rise from inside the "
            "community, killed mid-sentence in a bar by a projectile "
            "fired into a crowd he was only documenting, on the same day "
            "the Moratorium he covered turned violent. Iya (homage: "
            "Gloria Arellanes), Yoruba for 'mother' -- Aztlan's first "
            "woman minister (see PH2-023 for the walkout she led). Kra "
            "(homage: John Huggins), Akan for 'soul' -- Baale's "
            "co-founder and equal partner in Sankofa (see PH2-021), "
            "killed alongside him; his widow carries the work forward as "
            "a real, ongoing legacy."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-031",
        "category": "phase2-homage-la-underworld",
        "statement": (
            "Kasi leads Sankofa's crack-era saga, a direct generational "
            "sequel to Baale's own story: after COINTELPRO crushes "
            "Sankofa's political movement, the next generation's only "
            "remaining path to real power runs through the underground "
            "economy instead. Homage to 'Freeway' Rick Ross, who built "
            "one of the era's largest crack-cocaine distribution "
            "networks in South Central LA in the 1980s, later implicated "
            "in journalist Gary Webb's real, still-disputed 'Dark "
            "Alliance' reporting alleging ties to CIA-linked Nicaraguan "
            "Contra fundraising. Name is Swahili for 'speed,' echoing "
            "the real 'Freeway' nickname. A composite 'twist' character "
            "(Vito Corleone's rise-from-nothing arc; Thomas Shelby's "
            "paranoid always-three-moves-ahead mind; Tommy Angelo/Vito "
            "Scaletta's personal restraint from violence; a partial "
            "Nikolai Luzhin thread -- his own network secretly used by "
            "forces above him; Michael Corleone's real cost -- the "
            "empire hollows out the community that raised him; a late "
            "Lincoln Clay payoff -- turns and dismantles the apparatus "
            "that built him once he learns the truth), none reused as "
            "names, only as skeleton."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-032",
        "category": "phase2-homage-la-underworld",
        "statement": (
            "Doyle is the handler in Sankofa's crack-era saga, built "
            "fully on Nikolai Luzhin's deep-cover-patience skeleton: "
            "presents as a reliable, unremarkable supplier, plays a much "
            "longer game than anyone around him grasps; his loyalty was "
            "never to Kasi or to Sankofa, only to the operation above "
            "him. A deliberately plain, ordinary name -- the cold, "
            "bureaucratic, institutional hand in the room. Built from "
            "the real, still-disputed allegation at the center of Gary "
            "Webb's reporting that parts of the supply chain feeding the "
            "1980s crack epidemic in South Central had ties to a "
            "Contra-fundraising operation; a fictionalized face for that "
            "thread, not a real person under a different name."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-033",
        "category": "phase2-homage-la-underworld",
        "statement": (
            "Moto is the rival in Sankofa's crack-era saga, built on Gyp "
            "Rosetti's psychology: a fragile ego that reads a neutral "
            "slight as a mortal insult and answers with wildly "
            "disproportionate violence. Name is a widespread Bantu word "
            "for 'fire.' The chaos Kasi's own restraint stands against, "
            "and part of what eventually makes Kasi vulnerable, since "
            "Kasi won't fight Moto's way."
        ),
        "status": "locked",
        "source": SOURCE,
    },
    {
        "id": "PH2-034",
        "category": "phase2-homage-naming-convention",
        "statement": (
            "Phase 2 homage-era naming convention (standing rule for all "
            "future homage-era material): both real-world people and "
            "real-world places/institutions that inspire this era get "
            "wholly invented in-world names -- never the literal real "
            "name, including institutions like schools. Names draw from "
            "real Taino, Yoruba, Akan, Kikongo, Nahuatl, Swahili, or "
            "other real Black/brown-diasporic vocabulary, blending "
            "freely across traditions rather than staying 'pure' to one "
            "tradition per figure. Pronounceability and memorability for "
            "an English-reading audience outrank strict etymological "
            "purity -- avoid word-initial consonant clusters English "
            "doesn't use (e.g. 'Nz-', 'Ng-', 'Nkr-') and sounds absent "
            "from English (e.g. the Nahuatl 'tl'). The real-world figure "
            "or place is always kept as a documented research anchor "
            "(not the in-world name) for continuity and provenance."
        ),
        "status": "locked",
        "source": SOURCE,
    },
]

BATCH_NOTE = (
    'Every territory, leader, and character in this batch was individually '
    'drafted and explicitly approved in-conversation across the same '
    '2026-09-05 session ("locked", "lock it", "proceed", "confirm Guanín '
    'and lock it"). This batch\'s own authorization, converting the whole '
    'set into the ledger, was Abad\'s direct instruction: "convert what\'s '
    'been worked on into locked Canon Ledger .json material"'
)


def main():
    with open(LEDGER_PATH) as f:
        ledger = json.load(f)

    existing_ids = {r["id"] for r in ledger["rules"]}
    new_ids = [r["id"] for r in NEW_RULES]
    collisions = existing_ids.intersection(new_ids)
    assert not collisions, f"ID collision(s): {collisions}"
    assert len(new_ids) == len(set(new_ids)), "duplicate IDs within this batch"

    ledger["rules"].extend(NEW_RULES)

    ledger["batches_completed"].append(
        {
            "batch": 59,
            "source_doc": (
                "Phase 2 pre-Book-1 homage-era conversational development "
                "(docs/lords-of-cian/phase2-homage-era-development.md) -- "
                "converts the full NYC and LA build-out (5 territories/"
                "leaders each, NYC's Policy-era underworld trio, Xaragua's "
                "21-figure supporting cast, LA's 4-figure supporting cast, "
                "LA's crack-era twist trio, and the naming-convention "
                "standing rule) into locked canon under a new PH2- prefix."
            ),
            "source_id": None,
            "rule_count": len(NEW_RULES),
            "status": "complete",
            "conflicts_found": 0,
            "note": BATCH_NOTE,
        }
    )

    ledger["ledger_version"] = "6.2"
    ledger["last_updated"] = "2026-09-05"

    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")

    all_ids = [r["id"] for r in ledger["rules"]]
    assert len(all_ids) == len(set(all_ids)), "duplicate IDs after merge!"
    print(f"OK: {len(all_ids)} total rules, zero duplicate IDs, ledger_version={ledger['ledger_version']}")


if __name__ == "__main__":
    main()
