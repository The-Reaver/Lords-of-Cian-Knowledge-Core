import json, re
P = "canon-ledger.json"
D = "docs/lords-of-cian/chronicles/"
APPROVAL = "anything that needs correction is mandated to be corrected everything has to make sense. above all things everything has to connect to everything else logically the connective tissue must be Flawless that is the number one priority above all things"
PRIOR = "as long as it makes sense I approve"
SOURCE = "Original invention, chat-drafted 2026-10-03, no source document"
d = json.load(open(P, encoding="utf-8"))
ids = {r["id"] for r in d["rules"]}
nb = max(b["batch"] for b in d["batches_completed"]) + 1
fn = "lauris-chronicle-cx-the-instruments-read-an-empty-room.md"
t = open(D + fn, encoding="utf-8").read()
pat = r"\*UNLOCKED -- pending Abad's approval\. Draft, 2026-10-03, proposed `MCD-1888`\."
assert len(re.findall(pat, t)) == 1
t = re.sub(pat, lambda m: f"*Locked canon, Batch {nb}, 2026-10-03 (`MCD-1888`). Abad's approval: \"{PRIOR}\" and \"{APPROVAL}.\"", t)
t = t.replace("(proposed\n`VB-064`)", "(`VB-064`)").replace("(proposed `VB-064`)", "(`VB-064`)").replace("(proposed `CC-162`)", "(`CC-162`)")
assert "proposed `" not in t and "(proposed\n" not in t, "stray proposed marker"
open(D + fn, "w", encoding="utf-8").write(t)
NEW = [
 ("MCD-1888", "lauris-character-chronicle",
  "Lauris Chronicle CX, 'The Instruments Read an Empty Room' (full text at docs/lords-of-cian/chronicles/lauris-chronicle-cx-the-instruments-read-an-empty-room.md). First entry after her gate was cleared (backfill, 2026-10-03); Strand L, present day before Book 1; Lauris's marquee kill under MCD-1881. Pays off the CP-609 thread at its live edge (MCD-1663/MCD-1704) as the one sanctioned partial discharge of a Strand L thread. The Cairnholt Intake, a small holding operation split off from a Directorate regional containment office, carries corridor density instruments tuned to the Karesian signature and an inherited protocol to seal and flood its lowest level for 'non-viable' transfer subjects; thirty-eight are listed, CP-609 twelfth. Lauris disables the eleven-man yard guard with Attia's Rite (MCD-170), no deaths, entering Density Saturation through seven minutes of sustained engagement; the corridor instruments then read first 'calibration fault' and then total absence (ARS-358's two stages) while the guards watch her walk the full length. Warden Ilmar Hesketh is turning the sealing wheel that floods the cells; told once to stop, he turns it again, and she kills him with one Aristocrat strike -- a necessity kill under CC-162 -- then reverses the wheel. Thirty-seven walk out; CP-609 declines protection and runs, from Lauris too, the first time CP-414's 'Run' (MCD-187) means a chance rather than a clean death. Hesketh's nineteen-year ledger records six prior transfers closed 'lost to water' and four receiving facilities, three unregistered, widening 'you will not be the last.' Cairnholt is not the third Operation 38 facility (MCD-191). The guards' phrase 'the instruments read an empty room' reaches her Reclassified -- Hostile file (MCD-192), a legend Book 1 can quote. Narrated by Fermand under VB-064. New named characters and places: Warden Ilmar Hesketh (killed), the Cairnholt Intake."),
 ("VB-064", "voice-bible-narrator-fermand",
  "Fermand Aurelias's narration of Lauris Letitia's Character Chronicles keeps the established first-person transcriber frame -- each entry opening on a short archive fragment in Lauris's own spare voice (MCD-211, MCD-1558), then Fermand as transcriber and witness -- and CC-034's Baroque/Zafon-Noir register. For this series it supersedes the parts of VB-024's Narrator 4 sheet that conflict with that frame: the third-person-limited instruction and the rule that only Ezio receives Fermand's warmth (his regard for Lauris may show, never as panic or broken composure). The Voice Bible's hard constraints bind every entry, old and new, without exception: no balanced antithesis, no contractions in narration, no banned words, the Density Spike never named, violence rendered as physics in Narrator 4's autopsy register, powers shown through sensation. Existing entries that break a hard constraint or contradict locked canon are corrected; the frame and register themselves are not changed."),
 ("CC-162", "character-lauris",
  "Lauris Letitia's kill register after the Defection (Operation 40, MCD-192). Her forty Directorate contracts, including the terminations of cornered or non-resisting targets (CP-414, MCD-187; Hellem Veth-Kovan by agreement, MCD-192) and the killing of Selene's killer, stand exactly as already locked. From the Defection onward, every kill by her own hand is a necessity kill: the person is an active, immediate threat to life in that moment, and where there is time she gives one warning. She disables rather than kills whenever disabling suffices (Attia's Rite exists for exactly this), never executes a surrendering or fleeing person, and never kills for deterrence. Parallels Kanja's doctrine at CC-161 without merging the two. Her combat-joy (CC-134) lives in the body's full capacity and never in the kill."),
]
for rid, cat, stmt in NEW:
    assert rid not in ids, rid
    d["rules"].append({"id": rid, "category": cat, "statement": stmt + " Abad's approval: '" + PRIOR + "' / '" + APPROVAL + "'", "status": "locked", "source": SOURCE})
d["batches_completed"].append({"batch": nb, "source": SOURCE, "rules_affected": 3,
  "note": "Lauris Chronicle CX locked (MCD-1888), her marquee kill under MCD-1881 and the first entry after her gate cleared, with VB-064 (Fermand's Lauris voice: first-person transcriber frame and CC-034 register stand; hard constraints bind every entry) and CC-162 (her post-Defection kill register: necessity only). Abad's approval: \"" + PRIOR + "\" and \"" + APPROVAL + "\""})
d["ledger_version"] = str(round(float(d["ledger_version"]) + 0.1, 1))
d["last_updated"] = "2026-10-03"
json.dump(d, open(P, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(P, "a").write("\n")
ids = [r["id"] for r in d["rules"]]
print("batch", nb, "version", d["ledger_version"], "rules", len(ids), "dupes", len(ids) - len(set(ids)))
