#!/usr/bin/env python3
"""Batch 352: lock Kanja Chronicle IV (the Sovereign Pier), Kanja's killing doctrine (CC-161),
the anchor-kill tiering (MCD-1881), and the two-account Onyx rule (VB-062)."""
import json

LEDGER_PATH = "canon-ledger.json"
APPROVAL = "go with retrospective, keep the two years, lock it."
SOURCE = ("Original invention, chat-drafted 2026-10-02, no source document. Follows Abad's direction "
          "that pre-Book-1 marquee kills be concentrated on the four Book-1 anchor heroes, and his "
          "standing rule that every event in Kanja's life always has an Onyx account.")

NEW_RULES = [
    {"id": "MCD-1880", "category": "kanja-character-chronicle", "statement": (
        "Kanja Chronicle IV, \"Ninety Seconds on the Sovereign Pier\" (full narrative text at "
        "docs/lords-of-cian/chronicles/kanja-chronicle-iv-ninety-seconds-on-the-sovereign-pier.md), "
        "the fourth entry of the Kanja-version track and the first time the Battle of the Sovereign "
        "Pier (MCD-245) and the Trinity's surrender (MCD-246) are dramatized anywhere in the corpus. "
        "Age 30, the Rebellion's final day. King Maro Rexmar walks down the pier while Kanja is "
        "caulking The Audit's hull with active Living Drakma sealant and asks him to accept the "
        "Accords he spent the better part of two years negotiating in secret with Aethelgard "
        "Verehimu (recognition as sovereign King of Jicome in exchange for the Trinity, CC-009/"
        "MCD-085). A twelve-operative Trust team led by Ivo Strell attacks with Blight-projector "
        "sidearms tuned to the relics' Living Drakma; the still-wet sealant absorbs the signal first. "
        "In ninety seconds Kanja kills nine (Strell, Hesk, Vauden, Tasker, Caddel, Orrel, Teague, "
        "Danver, Lisk) -- every operative standing between his father and the landward end of the "
        "pier -- and deliberately drives the three posted at the seaward end into the harbor alive; "
        "Dol Maren hauls them out. Strell's warrant authorizes the attack irrespective of the "
        "negotiation's outcome. Kanja answers 'Yes' and surrenders Mafesto, Obsidian Malice, and "
        "Onyx that night; the Rexmar Machete stays on his belt (ARS-425). Narrated by Onyx "
        "throughout, completing VB-026's handoff: its self-reference shifts from 'the blade' to "
        "'I' at the moment the case closes, beginning the seconds-count MCD-246 locks. The first "
        "Kanja marquee kill under MCD-1881 and the governing precedent for CC-161. Nothing "
        "foreshadows the Fulfillment Ceremony or Maro's death. Abad's approval: '" + APPROVAL + "'"),
     "status": "locked", "source": SOURCE},
    {"id": "CC-161", "category": "character-codex", "statement": (
        "Kanja's killing doctrine. His no-killing stance is a deliberately costed default, never an "
        "absolute. The Scrip-Forge Raid, the Dredge-Line Ambush, and the Maw-9 demolition stay "
        "bloodless because bloodlessness was the better weapon there -- a humiliation the Trust's "
        "bureaucracy has no clean answer to, rather than a war its military can. When the ratio "
        "demands death, he chooses it explicitly and records the cost. Governing precedents: the "
        "Black Trench (MCD-232, 1,400+ Brigade losses), the Falling Bridge (MCD-243, 400 mounted "
        "pursuers dropped into a gorge), and the Sovereign Pier (MCD-245/MCD-1880, nine killed, three "
        "deliberately spared). His kills across the Rebellion and the Long Mask are cold, ledgered, "
        "and terrifying because they are calm and chosen, never rage. The urge to destroy his "
        "enemies stays reserved for the turn caused by Maro Rexmar's death at the Fulfillment "
        "Ceremony; nothing before Book 1 may read as that turn arriving early. Abad's approval: '"
        + APPROVAL + "'"),
     "status": "locked", "source": SOURCE},
    {"id": "MCD-1881", "category": "World Mechanics", "statement": (
        "The anchor-kill tiering, a standing writer's-guide rule for pre-Book-1 material. Three "
        "tiers: Marquee -- a named, fully dramatized kill or defeat that becomes legend and can be "
        "referenced in Book 1, reserved to the four Book-1 anchor heroes (Kanja across the Rebellion "
        "and the Long Mask, Daba/1804, Ozmund, Lauris); Notable -- a real, dramatized victory that "
        "does not define how the world speaks of the hero, for every other hero; Ledger -- "
        "background tallies. Working target roughly 15-20 marquee kills across the four anchors, "
        "each with a named victim and a full scene, never a body count. Constraints: for Daba/1804, "
        "'marquee' means fully dramatized with a named victim in his own series while the kill stays "
        "publicly unattributed per MCD-1569, legend only inside 1804's own record, and network-"
        "executed except for at most one personal kill; Ozmund's stay strictly pre-Fulfillment-"
        "Ceremony, at most one, unwitnessed by Draconis, so his Book 3 escalation is not spent "
        "early; Kanja's Long Mask marquee kills use post-Mafesto gear only, Onyx sealed. Harek "
        "Vondel (MCD-1878, Daba/1804) and the Sovereign Pier (MCD-1880, Kanja) are the first two "
        "marquee kills under this rule. Abad's approval: '" + APPROVAL + "'"),
     "status": "locked", "source": SOURCE},
    {"id": "VB-062", "category": "voice-bible-narrators", "statement": (
        "The two-account rule for Kanja's life. Any event may be told from whatever angle is most "
        "interesting -- neutral third-person, a crew member, an enemy, a witness, his father, anyone "
        "-- and such accounts may coexist, overlap, and differ in emphasis without contradicting "
        "locked fact. In addition, every significant event in Kanja's life always has an Onyx of "
        "Oblivion account. The Kanja-version track is the home of the Onyx accounts; the Alias "
        "Chronicles and any other-angle tellings are the non-Onyx accounts; a marquee event should "
        "normally get both. Onyx narrates in first person from the moment of its sealing at the "
        "Sovereign Pier (MCD-1880) onward. Because Onyx is sealed at L9 for the whole Long Mask "
        "(MCD-246), its Long Mask accounts are retrospective: told after the Karkosa Heist reunites "
        "it with Kanja in Book 1, openly acknowledging it was not present and reconstructing the "
        "years from what it learns once his hand closes on the grip again. Extends VB-020/VB-026. "
        "Abad's approval: '" + APPROVAL + "'"),
     "status": "locked", "source": SOURCE},
]

AMENDMENTS = {
    "MCD-1129": [("Kanja's established no-killing doctrine", "Kanja's established no-killing-by-default doctrine (CC-161)")],
}

BATCH_NOTE = (
    "Locks Kanja Chronicle IV (the Sovereign Pier, MCD-1880, after the light Fable review's fixes "
    "in Batch 351), Kanja's killing doctrine (CC-161), the anchor-kill tiering (MCD-1881), and the "
    "two-account Onyx rule (VB-062, with Long Mask Onyx accounts ruled retrospective). MCD-1129's "
    "'no-killing doctrine' phrasing amended to 'no-killing-by-default' to match CC-161; the Kanja "
    "profile's values facet updated the same way. Abad's approval, quoted verbatim: '" + APPROVAL + "'"
)


def main():
    with open(LEDGER_PATH, encoding="utf-8") as f:
        ledger = json.load(f)
    existing = {r["id"] for r in ledger["rules"]}
    for rule in NEW_RULES:
        assert rule["id"] not in existing, rule["id"]
        ledger["rules"].append(rule)
    rules = {r["id"]: r for r in ledger["rules"]}
    for rid, pairs in AMENDMENTS.items():
        s = rules[rid]["statement"]
        for old, new in pairs:
            assert s.count(old) == 1, (rid, old)
            s = s.replace(old, new)
        rules[rid]["statement"] = s
    next_batch = max(b["batch"] for b in ledger["batches_completed"]) + 1
    ledger["batches_completed"].append({"batch": next_batch, "source": SOURCE,
                                        "rules_affected": len(NEW_RULES) + len(AMENDMENTS),
                                        "note": BATCH_NOTE})
    ledger["ledger_version"] = str(round(float(ledger["ledger_version"]) + 0.1, 1))
    ledger["last_updated"] = "2026-10-02"
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
        f.write("\n")
    ids = [r["id"] for r in ledger["rules"]]
    print(f"OK: {len(ids)} rules, batch {next_batch}, ledger_version {ledger['ledger_version']}, "
          f"zero duplicate IDs: {len(ids) == len(set(ids))}")


if __name__ == "__main__":
    main()
