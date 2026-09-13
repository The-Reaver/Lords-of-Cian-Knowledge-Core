# Brain Trust on-demand protocol, the room for how to request and run a review

A structure note, map-of-content pattern. Written 2026-08-08 at Abad's direct instruction, after he
had to ask twice in the same day for the fleet's review process to run somewhere other than a
separate chat he manually drives. His own words: "this should be a process i can and should be
able to request on demand. it should be part of a menu option for me. when we run the brain trust
i should not have to repeat this step again. i should be asked, want me to run the brain trust?"

## What this closes

Before today, running a Brain Trust review meant Abad personally opening a fresh chat per seat,
pasting a dispatch, collecting the verdict, and repeating that seven times, then again for the
table, the vote, and both of Elijah's interviews. That is real friction, and it fell entirely on
him. It also meant no session ever offered the review unprompted, he had to remember the process
exists and ask for it by name every time.

## The standing rule, going forward

1. **Any Cowork or Claude Code session with subagent access (the Agent tool, or equivalent) can run
   the full review inside itself, seat by seat, without Abad opening separate chats.** Proven
   2026-08-08: the workstation-UI and CIPP/E-connectivity review ran this way end to end, six seats,
   both Elijah interviews, the table, the vote, in one session, using subagents as the seats. This
   is not a lighter substitute for the real process, it is the same process, same seats, same fixed
   verdict schema, same vote mechanics, run by an agent instead of by Abad's own copy-paste.
2. **A session should offer the review, not wait to be asked, whenever it produces or receives a
   proposal, architecture decision, or scoping question with real stakes** (a new build, a security-
   or compliance-relevant change, anything already being written up as a `brain-trust-queue`
   candidate note). The offer is a direct question: "Want me to run the Brain Trust on this?" Not a
   silent decision, not a silent defer, an actual question, put to Abad, before proceeding either
   way.
3. **The canonical template is `GEO_BRAIN_TRUST_DISPATCH_2026-08-08.md`**, in the stag repo root.
   Read it before building any future dispatch packet. Its shape: a shared brief (scope ruling,
   what's settled, what's open), one dispatch per seat with a fixed verdict schema
   (SHIP / SHIP WITH CONDITIONS / HOLD / FAIL, confidence, blocking/non-blocking findings, confirmed
   working, cannot-determine, one ask of the operator, case for the table), Elijah's first interview,
   the table, the vote (simple majority, NO CONFIDENCE lowers the denominator, dissents recorded
   verbatim, Abad's veto per Mandate 1), Elijah's second interview, and the handoff.
4. **Seat count adapts to scope.** GEO used all seven (Celestina, Jasiah, Oluwole, Amaya, Omar,
   Bink, Sentinel) because a trustworthiness-of-score question was in play. CIPP/E and the
   2026-08-08 workstation-UI/CIPP/E-connector review both used six, dropping Bink, since neither
   turned on whether a numeric score means anything. Match the seat list to what the decision
   actually needs, do not run all seven by default.
5. **Nothing here changes Mandate 1.** A carried vote is a recommendation. Abad ratifies. This
   protocol makes the review easier to request and run, it does not make the review self-executing
   past a verdict.

## Open, for a future ratification pass

This note documents the protocol and is already being followed as of 2026-08-08. Whether it should
also become a numbered Mandate, the way Mandate 9 and Mandate 10 were ratified through a Brain
Trust ruling, is a separate question this note does not decide. Abad can request that ratification
pass whenever he wants it formalized; until then this structure note is the standing reference any
session should read before saying "you'd have to run that yourself" to a Brain Trust request.

## 6. How deep to review: the reversibility test

Added 2026-08-29 at Abad's instruction, so review depth stops being re-litigated case by case.
Section 4 sizes the seat list to the question. This sizes the *whole review* to the blast radius.

**The test, one question:** would a wrong answer be caught by the next commit, or only by something
breaking in production or surfacing months later?

- **Caught by the next commit** -> a scoped panel is enough, and the implementation seat hands back
  to one cold reviewer. Failure is loud, local and instantly reversible.
- **Only in production, or months later** -> full depth: a cold panel *and* a separately cold
  Opus 5 review, neither of them the session that wrote the thing. Two sessions, deliberately.

Worked example of the cheap side, 2026-08-29: the `model_tier_gate` slice. Its worst failure mode
is blocking every commit in the repo -- alarming, but loud and revertible in one command. Scoped
review was correct.

Worked examples of the expensive side, all live in this fleet as of 2026-08-29:

1. **Credential rotation plus a git-history purge on Stag-Fleet.** History rewrite on a repo with a
   live remote; every clone diverges and a wrong rotation order can leave the old key valid while
   taking a service down. The 2026-08-25 ledger row already records this class going wrong in the
   measurement stage: an initial "7 real keys" was later corrected to 2, the other 5 being
   kebab-case false positives. A purge scoped off a wrong count destroys history for nothing.
2. **The S-34b lockfile and the Dockerfile install change.** P-8: any redeploy re-resolves every
   dependency, so `git revert` does not restore the last-known-good image. Unrevertable by
   definition, and the lock must resolve for linux/python3.13 from a Windows/python3.14 machine.
3. **Applying a migration and flipping a store flag against live Supabase.** Schema plus behaviour
   against real clients and users, where the migration class has already silently failed four times
   and the detection path is itself broken (`SUPABASE_DB_URL`'s password is wrong, so
   `deploy_verify` silently skips its migration check).

**Different axis, same answer -- architectural blast radius.** The 768-vs-1536 embedding-dimension
conflict between ADR-0005 and `SPEC_KNOWLEDGE_CORE.md` is not a production risk, but being wrong is
paid months later in a full re-embed, and both documents warn against letting other work silently
resolve it. Cost-of-being-wrong deferred into the future counts as expensive, even when nothing is
live. The trap is that a cheap review looks retrospectively unnecessary right up until it doesn't.

**Nothing here changes Mandate 1.** Depth chosen, vote carried, Abad still ratifies.

## Links
- relates, terminal-glossary.md, same map-of-content pattern for a different room.
- relates, 2026-08-08-preliminary-panel-read-workstation-ui-and-cippe-connector.md, the informal read this protocol was written alongside.
