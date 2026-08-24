# Lords of Cian Interactive Archive — Game Plan, Backlog & Engagement Roadmap

By Abad Morel. Fleet-reviewed strategy deliverable, adversarial + Opus 5 synthesis, reconciled from three source documents (Visual Direction Document v1.0, System Explanation, Strategy Document), drafted in parallel, adversarially reviewed, and synthesized into one execution-ready plan.

Date: 20 August 2026. Status: Reconciled final. Source repository: The-Reaver/My-Rivals-Distance-Archive.

---

## §0 Executive Summary

Ground truth: the three source documents describe a nearly-finished system; the connected GitHub repository (The-Reaver/My-Rivals-Distance-Archive) is empty, zero commits, zero branches on origin, no src/, no package.json, no migrations. Everything described in the System Explanation exists only inside the Lovable workspace, so no claim in its "Complete" list can be independently verified, and no engineer other than Lovable's own agent can review, test, or safely modify the codebase.

Two live risks sit behind that wall: the source document contradicts itself on whether Row Level Security is actually enabled (§3 and §9's Complete list say yes; §9's Remaining Step 8 says re-enable it), and email confirmation is disabled by design (§7), meaning the demand signal the entire strategy is built to trust (request counts, referral chains, registered-user totals) can currently be manufactured by one person with a script. Everything below is sequenced behind these three facts. The work itself is not large; the ordering is what matters.

Standing caveat: table names, the 11 document types, and clearance rules below are quoted from the source documents. Individual column names and file paths are unverified until the repo sync (P0-1) lands; treat any field-level reference as "assumed, confirm on sync."

---

## §1 Game Plan

Six phases. Each names the backlog items it executes, full detail in the Stock Recommendation below.

### Phase 0 — Establish ground truth
Executes P0-1, P0-2.

Push the Lovable project into GitHub, then run a single read-only audit pass over the real code against the eight documented contradictions and one orphan table listed under P0-2. Nothing gets built in this phase, the output is a decision record, written into CLAUDE.md alongside the Visual Direction tokens, so every later phase is verifying rather than guessing.

Also here, because it's nearly free: confirm the Supabase service-role key and ANTHROPIC_API_KEY don't appear in any file about to enter version control, and rotate the Anthropic key as hygiene now that the codebase is entering a second platform.

Done when: git log on origin shows real history; the src/ tree matches System Explanation §8 or the differences are documented; CLAUDE.md carries the Visual Direction tokens and the resolved decisions; no secrets in the diff.

### Phase 1 — Lock the database and the signal
Executes P0-3, P0-4. Designs P1-1.

Security is sequenced first, not after feature completion. The archive is already deployed to a lovable.app URL anyone holding the link can reach, and the anon key ships in the browser bundle where its only protection is RLS. If RLS is off or permissive, which §9 Step 8 implies, reader emails, engagement rows, and the referral graph are exposed today, not at launch.

Baseline default-deny RLS across all 11 tables now, with per-table clearance-aware read policies, extending the policy set as each new route lands in Phase 2. Alongside it, close the identity hole (P0-4): a demand signal that can be faked is worse than no signal, and the platform's stated identity is "honest by design" (Strategy §9).

One coupling to resolve before writing policies: per-row lockdown on requests and engagement collides with the public UI displaying aggregates of that same data (follower count and Reader Demand Score on the character hero, Visual Direction §4; Character Index sorted by demand score, §6). Design the public aggregate (P1-1) here, so policies are written around it, not against it.

Done when: a Supabase security-advisor pass returns no RLS warnings on any of the 11 tables; a Level 1 test account cannot read Level 2/3 content, another user's profile row, or the referral graph; book-placement spoiler enforcement survives a direct SQL/API attempt bypassing the admin UI; a scripted signup cannot inflate a request count, a referral chain, or the registered-user total.

### Phase 2 — Complete the reader loop
Executes P1-1 through P1-6.

The gaps the source document names itself (Steps 5, 6, 7), plus two the documents imply but never scope: a public demand aggregate (P1-1) and an extraction tool (P1-3), the more important find. The entire content architecture rests on "reader-facing content is a curated slice... extracted from the source material" (Strategy §3): a physical description pulled from a Character Codex, a weapon promoted to a world briefing (System Explanation §4). But no admin section performs extraction, and no remaining build step creates one. Intake routes everything except Chronicle Entries into archive_documents and stops, without extraction, writer-reference content has no path to readers except retyping, and Phase 5's unlock cascade has no legal mechanism at all.

Done when: a Level 1+ reader can browse /archive and read /archive/:id gated by the clearance set at intake; an admin can extract a section from a writer-reference document into a new reader-facing row without altering the source row's storage mode; an admin can paste full chronicle prose into a side-by-side editor and publish it; a public visitor sees a demand score on a character profile while per-row reader data stays unreadable.

### Phase 3 — Launch
Executes P1-7.

Content-readiness gate first: enough Level 0/1 material live to make "pre-book content is a full world, not a teaser" (Strategy §4) true, briefings across the confirmed category set, arsenal entries, and enough chronicle entries beyond the 10 seed rows that a Level 1 reader can plausibly read three to 90%, since that action is load-bearing for Level 2. Then deploy, connect the domain, and run a full four-level QA pass on a disposable account against the Level 2 rule confirmed in Phase 0, not against both readings, and not against whichever one a draft assumed.

Done when: production URL live on the custom domain; all four clearance transitions verified end-to-end; a test request appears correctly in the Demand panel within the session; the landing page matches whichever landing-page resolution Phase 0 recorded.

### Phase 4 — Operate the demand engine
Executes P2-1, P2-2, P2-3. Open-ended.

The steady state, not a task. Neither source document specifies a review cadence, only that the Demand panel carries 7-day and 30-day trend windows; weekly is a recommendation because it matches the shorter window, not a source mandate.

Each cycle: read the Demand panel by trend direction, not raw total (a 150-rising character outranks a 200-flat one, per Strategy §6); check clearance distribution as the diagnostic §6 says it is; check referral chain depth for network structure; and, new from Phase 1, check the anomaly flag before trusting any spike. Feed the resulting priority stack back into the extraction and chronicle-editor tooling from Phase 2.

Done when (recurring): every newly-developed pending character traces back to a documented demand decision, count, trend, engagement, and a clean anomaly check.

### Phase 5 — The Book 1 unlock cascade
Consumes P1-3 and P0-3. No new backlog items.

When Book 1 ships, mark it published in admin_settings. Per Strategy §7 the cascade makes Book-1-tagged vault items eligible to go live, subject to author review.

Correction carried from review: an earlier draft proposed publishing Book-1-tagged Threat Blueprint and Tactical Architecture content directly. Both are Writer-Reference, "system-stored, admin-searchable, never publishable" (Strategy §3). Nothing flips a Writer-Reference row to Live. The correct action is extraction: pull the relevant Book-1 material into new Chronicle Entries or archive documents via the P1-3 tool, leaving the source rows untouched. This is exactly why P1-3 is not optional.

Re-run the Phase 3 QA against this transition specifically, the first time the platform operates in companion mode rather than predecessor mode, and the first live test of book-placement enforcement under real pressure.

Done when: published_books reflects Book 1; Book-1-derived content is live; Book 2-5 content remains vault-locked and unreachable by direct URL or API; Level 3 structural-reveal content has been re-read to confirm it still lands now that Book 1 exists.

The post-series fan-contribution framework (Strategy §7) sits past this horizon, scope it when Book 5 is in sight, not now.

---

## §2 Stock Recommendation

Tiers are dependency-and-risk order, not a strict effort-vs-impact sort, P1-2 can't happen before P0-1 no matter how cheap it is.

### P0 — Blocking

**P0-1 — Push the Lovable project into GitHub.** Origin has no branches. None of the paths in System Explanation §8 exist here. Until this lands, no diff can be reviewed, no test run, no security audit independently verified, the "Complete" list in §9 is an assertion, not a fact. Effort: S if GitHub sync only needs enabling or re-triggering. Potentially larger if the integration was never configured, points at the wrong repo, or lost its GitHub App authorization, "connected but zero commits" is consistent with all three. First step is to open Lovable's GitHub integration settings and find out which, before assuming a one-click fix. Blocks: everything.

**P0-2 — Resolve the source-document contradictions.** Read-only audit against real code, one pass, output written into CLAUDE.md:
- RLS status: §3 and §9-Complete claim RLS ships; §9 Step 8 says re-enable it. Determines whether P0-3 is a fix or a verification.
- Typography: §7 ships Cormorant Garamond / Source Sans Pro; Visual Direction §3 mandates Playfair Display / Inter / JetBrains Mono. Recommendation: Visual Direction v1.0 wins, it self-declares as CLAUDE.md-authoritative with a reject-and-rerun loop (§11). Change the config, not the doc.
- Text color: §7 says #e8e6e0; Visual Direction §2 says #E8E6E3. Trivial, but pick one before it propagates.
- Level 2 rule: System Explanation §2, "complete 2 of 3." Strategy §5, "read 3 entries fully, OR share, OR request 2 chronicles." Materially different gates. Recommendation: the OR reading, pre-launch, Strategy §6 names Level-1 stalling as a content failure to diagnose, and a 2-of-3 gate makes stalling structurally more likely. Tighten later if Level 2 stops meaning anything.
- Landing page: §2/§9 describe the shipped home page as a character grid plus featured excerpt. Visual Direction §6 specifies hero, tagline, and a single "Enter the Archive" CTA, "a door, not a brochure," with the grid on a separate Character Index. Recommendation: build the door, move the grid to the Character Index; both stay indexable.
- Dossier cover visibility: System Explanation §2 lists dossier covers as a Level 1 unlock; Strategy §2 and System Explanation §6 both describe them as visible in the public grid. Decides what a logged-out visitor and a search crawler actually see, Level 0's entire stated job.
- World-briefing categories: §3 says "9 categories" and names eight; §9 reports "nine category tabs" shipped. Enumerate the real values; a genuinely missing ninth would otherwise pass Phase 3 sign-off unnoticed.
- Framework: Visual Direction §11 instructs the orchestrator to generate Next.js components; System Explanation §7 says React with TanStack Router. Any UI task run against the Visual Direction as written targets the wrong framework.
- Plus one orphan: quiz_questions holds 11 seeded rows but appears in no reader route, no admin section, and no remaining build step. Decide in this pass: in scope (to P3-1) or explicitly deprioritized, do not leave it undecided.
Blocks: P1-5, Phase 3 QA.

**P0-3 — Re-enable and verify RLS across all 11 tables.** Per-table, clearance-aware, default-deny: profiles own-row only; chronicle_requests, engagement_events, user_progress insert-only from the authenticated user with no cross-user read; referrals visible only to the two parties in the pair, full graph admin-only, omitted from an earlier risk list despite being who-knows-who data with the same exposure profile; content reads on chronicle_entries, world_briefings, and archive_documents enforcing the row's clearance requirement server-side, not client-trusted. Verify book-placement enforcement (§5) is a database constraint, not an admin-UI check. Confirm "reader and admin sides never cross" (§1) holds at the database layer, not just the router. Effort: M, depends on P1-1 being designed first, or the lockdown breaks the public demand display. Blocks: Launch.

**P0-4 — Close the identity hole in the demand signal.** System Explanation §7: "Email confirmation disabled for frictionless signup." Consequence: unlimited unverified accounts. Level 3 requires only "refer one friend," so one person with two throwaway accounts self-refers into the Inner Circle repeatedly; the same gap inflates registered-user counts, request totals, and referral-chain depth, the exact numbers Strategy §8 names as the 6-month success metric and §6 names as the writing-schedule input. Minimum viable fix, in order:
1. Uniqueness on requests, one active request per user per pending character, enforced at the schema level, surfaced as a toggle rather than an add.
2. Verified identity for signal-bearing actions only. Keep signup frictionless, the whole Level 0-to-1 conversion premise, but require a confirmed email before a referral credits toward Level 3 or the referral graph, and before a request counts toward the public score. Confirmation gates earning, not entering.
3. Rate limiting on signup and request endpoints, plus disposable-domain blocking and a same-device/IP flag on referrer-referred pairs for review, flag, don't auto-reject.
4. Anomaly surfacing wired into P2-1 so a spike is visibly a spike.
Deliberately not recommended: CAPTCHA. It contradicts "frictionless signup," fights the minimal-surface aesthetic, and rate limiting plus verified-earning closes most of the same gap. Revisit only if bot traffic is observed post-launch. Effort: S-M. Blocks: Launch, all P2.

### P1 — Core loop completion

- **P1-1 — Define and expose "Reader Demand Score."** Neither source document defines the formula, yet Visual Direction §4 renders it publicly on every character hero and §6 sorts the Character Index by it. Decide the formula, then expose it through a read-only aggregate, a view or SECURITY DEFINER function returning counts and scores only, never row-level reader identity. Effort: S-M. Blocks: P0-3 policy design.
- **P1-2 — Wire archive_documents into the reader surface (Step 5).** Character profiles, /world, plus new /archive index and /archive/:id reader. Ten of the eleven document types land in this table; until it renders, most of the ~1M-word corpus has no reader-facing surface at all. Needs type-aware rendering across ten document shapes and clearance gating consistent with the existing chronicle reader. Effort: M-L. Blocks: Level 1/2 depth.
- **P1-3 — Extraction tool: writer-reference to reader-facing.** Select a section of a Character Codex, Arsenal Dossier, Tactical Architecture, or Threat Blueprint and promote it into a new reader-facing row, chronicle entry, world briefing, or archive document, with its own clearance and book placement, leaving the source row untouched. Nothing in the nine admin sections or the remaining build steps performs this. Without it, Phase 5's cascade has no legal mechanism and the writer-reference boundary gets broken by whoever implements it first. Effort: M. Blocks: Phase 5.
- **P1-4 — Side-by-side chronicle body editor (Step 7).** Markdown editor with live preview for moving full prose into chronicle_entries. Ten entries exist against 18 characters (nine with none) and 22 battles for Kanja alone. This is the production bottleneck: when the Demand panel names a winner, this determines how fast you can answer. Effort: M. Blocks: Content throughput.
- **P1-5 — Reconcile design tokens and the landing page.** Implement whatever P0-2 decided on typography, text color, the landing page, and the framework mismatch. Configure color, type, and spacing (4px base: xs 4 / sm 8 / md 16 / lg 24 / xl 32 / 2xl 48) as Tailwind theme extensions per Visual Direction §11 rather than inline hex. Every UI task generated after this point is otherwise built against two specs at once. Effort: S-M. Blocks: All future UI work.
- **P1-6 — Bulk Character Codex ingestion (Step 6).** Extend the existing single-document AI parse into multi-section extraction across the codex corpus with arsenal cross-references. Worth reviewing the dated claude-sonnet-4-20250514 model pin in intake.functions.ts against the current model line while in that file. Bulk ingestion of a ~1M-word corpus is exactly the Message Batches use case (asynchronous, 50% cost), with prompt caching on the repeated schema/system prefix. Effort: L. Blocks: Content breadth.
- **P1-7 — Deploy to production, connect the custom domain (Step 9).** Every day on a preview link is a day of zero demand collection against a 6-month milestone. Sequenced strictly after P0-3 and P0-4, deploying first widens exposure from "a link people happen to have" to "indexed and public." Effort: S. Blocks: 6-month milestone.

### P2 — Demand-engine strengthening (post-launch)

- **P2-1 — Demand-panel anomaly detection and trend-quality review.** The 7/30-day trend lines exist, but their value depends on distinguishing a rising 150 from a flat 200 (Strategy §6), untestable against seed data. Once real traffic lands, validate the trend math and add spike detection so P0-4's fraud controls have a visible readout. Effort: S-M.
- **P2-2 — Clearance-distribution stall flag.** Strategy §6 treats clearance distribution as a diagnostic, but it only diagnoses if someone looks. Scope this as an in-dashboard visual flag when Level 1-to-2 conversion stalls week-over-week. True push/email alerting is a separate, larger item, the stack has no notification channel, so that version means choosing and wiring one. Don't conflate the two in a ticket. Effort: M (flag only).
- **P2-3 — Referral chain-depth view.** Strategy §6 wants "who brought who, how deep chains go"; no referral view exists among the nine admin sections. Chain depth is a recursive query over the referrer-referred relation, not an index, plan for a recursive CTE and confirm the actual relation on sync (§3 describes both a referrals table and a referred-by field on profiles). Gate the resulting numbers behind P0-4. Effort: M.

### P3 — Later

- **P3-1 — Quiz as comprehension diagnostic.** If P0-2 keeps quiz_questions in scope, ship it as a diagnostic surface, not a clearance gate. Effort: S-M.
- **P3-2 — Share-card / OG-image optimization.** The share button exists; better preview cards make shared links convert harder, supporting both the Level 0 discovery layer and the share-to-Level-2 path. Polish on a working mechanism. Effort: S.
- **P3-3 — Post-series fan contribution framework.** Explicitly a post-Book-5 feature on Strategy §8's own 10-year timeline. Correctly last. Effort: L.

Cut from an earlier draft: "custom-domain branding polish," whose sole example, branded email-confirmation templates, described an email the system does not send (confirmation is disabled). If P0-4 introduces a confirmation email, that template work belongs inside P0-4, not as a standalone growth item.

---

## §3 Interactive & Engagement Improvements

Ranked by expected impact on the demand signal. Every item extends a mechanic that already exists, clearance, requests, the single-character follow, the referral chain, rather than bolting on points, streaks, or badges. None introduces a carousel, an icon in primary navigation, a box shadow, a gradient on an interactive surface, or a tooltip; JetBrains Mono stays confined to metric values.

Two preconditions apply to the whole section: all schema references are unverified until P0-1, and items 1 and 5 make gameable metrics more public and more decision-critical, neither ships before P0-4.

1. **The Standing Requests Ledger.** Blocked on P0-4. Make the request count reader-visible on a pending character's profile as an in-world ledger, "47 readers have requested this Chronicle," with an optional one-line reason the requester typed, rendered as a plain vertical feed. Signal: converts a private admin metric into a public commitment device, compounding the exact number Strategy §6 uses to pick what gets written next. Build note: needs a pending-character stat bar variant (Requests + reason feed only); the four-metric bar in Visual Direction §4 assumes engagement history a pending character has none of.

2. **Request Fulfillment Loop.** When a requested character's first chronicle entry goes live, every reader holding a request for that character gets one quiet Activity Feed item, timestamped, styled like any other release notice, plus an email. No confetti, no unlock animation. Correction: trigger is the chronicle entry's own live flag flipping true, not the book-publication toggle. Everything in the archive is pre-book by design (Strategy §4); the published_books toggle governs the Book 2-5 vault cascade and would never fire for this feature's primary case. Signal: closes the self-feeding cycle Strategy §6 describes but nothing currently enforces.

3. **Field Notes.** Inside the Chronicle Reader, a reader marks a paragraph as significant, framed as adding it to their own dossier, not as a like. Plain text affordance on hover at the standard 150ms, no icon. Marked passages collect in the reader's private profile. Signal: progress tracking currently records scroll percentage and a completion flag (entry-level). Passage marking gives paragraph-level resolution on which beats land. Build note: markdown bodies have no stable paragraph identity; anchoring needs a deterministic scheme (content hash or index plus fallback) or every body edit orphans every note against it.

4. **Also Drawn To.** Signup forces one followed character, a strong signal per Strategy §5, but one that discards everyone's second interest across an 18-character roster. Add an optional, non-required list a reader can build from the Character Index at any time. Plain text-link additions, vertical feed. Signal: reveals cross-character affinity clusters, readers who follow A but circle back to C are a distinct segment from A-exclusive readers, telling you which pending character's audience overlaps an already-engaged base.

5. **The Referral Lineage.** Blocked on P0-4. At Level 3, render the reader's actual chain as a short in-world genealogy: "Brought in by ___. You brought in: ___." Text only, Inter, no tree diagram, no badge. Signal: Strategy §6 calls referral "the only compounding marketing channel" and wants chain depth; nothing currently surfaces it. Showing it rewards the behavior and, through the same query used in P2-3, tells you which Level 3 readers actually compound versus refer once and stop. Build note: chain depth is a recursive query, not an index.

6. **Correspondence Checkpoints.** Wire the 11 seeded quiz questions into a short in-world "correspondence" a reader completes after finishing a character's arc. Results feed the diagnostic dashboard; they do not gate clearance. Corrections upheld: Level 2 unlocks connective tissue, Level 3 unlocks structural reveals; both stay deliberately distinct, so a quiz gating "Level 2/3" conflates two tiers. Gating access behind a graded test is a genuinely new mechanic, the only item here that fails this section's own selection criterion, and it puts the reader in the position of being evaluated, against Strategy §8's non-gamified posture. Uncapped retries make a pass-rate meaningless. Resolution: keep the feature, drop the gate. Count first attempts only toward the pass-rate diagnostic; allow unlimited retries for the reader's own satisfaction, flagged separately. Signal: per-question first-try pass rate tells you which world element is confusing readers, the fine-grained tool the clearance diagnostic currently lacks.

7. **Follow Reconsideration.** Allow one follow change after a fixed window, say 30 days, presented plainly as "Follow a different character instead." Not an achievement, not a reset. Explicit rule: switching resets Level 3 progress toward the new character; completion history against the previous character is preserved for analytics only and does not count toward clearance. Without this, Level 3 has undefined, and exploitable, behavior mid-arc. Signal: a switch from A to B is itself the data point, sharper than either character's raw follow count; the current schema throws it away by overwriting the field silently.

8. **Connective Tissue Trails.** Passively log which cross-links (character-to-faction, faction-to-institution, character-to-character) readers actually click through in the Level 2 world briefings. Invisible to the reader. Correction: this is a schema change. Engagement events are documented as "type label + entity ID" with no metadata column anywhere in the source material; scope it as adding a metadata JSON column, confirmed against the real schema on sync. Signal: maps which relationships readers are curious about, not just which characters, per §6's "deepest following" criterion.

9. **Two Dossiers, Side by Side.** Let a reader select exactly two characters on the Index and view their dossier-cover data statically side by side. Comparison is a purchase-consideration signal, "I'm choosing between these two," distinct from a request. Corrections: the symmetric two-character layout is new, not inherited (Visual Direction §4's Lore Panel is an asymmetric 60/40 split for a single character, say "visually consistent with the card system," not "reuses the Lore Panel"). Shares item 8's metadata-column dependency: a pair of character IDs doesn't fit a single entity-ID field.

---

## §4 Adversarial Findings — What Changed and Why

### Fixed, critical
- Demand-signal fraud had no coverage anywhere across all three sections. Added P0-4 as a blocking item covering request uniqueness, verified identity for signal-bearing actions, signup rate limiting, referral-pair flagging, and anomaly surfacing. Engagement ideas 1 and 5 are now explicitly gated behind it, the single most serious gap, since the plan treats the demand signal as ground truth for a multi-year writing decision while the source document states email confirmation is disabled.
- Self-referral into Level 3. Folded into P0-4 rather than kept separate, one person with two accounts reaching Inner Circle is the same root cause as inflated request counts.
- Engineering detail asserted against an unverifiable schema. Added the standing caveat at the top of this document, replaced invented column names with prose descriptions throughout, corrected the "no schema change" claims on ideas 8 and 9.

### Fixed, major
- Level 2 rule conflict (2-of-3 vs. any-one) added to the P0-2 audit with a recommendation, Phase 3 QA can't be written against both readings.
- Phase 5 proposed publishing Writer-Reference content. Rewritten as extraction; P1-3 added because no extraction tooling exists anywhere in the described system.
- Landing-page contradiction added to the audit with a resolution that preserves the Level 0 SEO job.
- Public demand score vs. RLS lockdown resolved by adding P1-1 and sequencing its design inside Phase 1, before policies are written.
- Notification trigger (Idea 2) corrected from the book-publication toggle to the entry's live flag, as drafted it would never have fired for its own primary use case.
- Level 2/3 conflation and the quiz-as-gate problem (Idea 6) resolved by dropping the clearance gate entirely and keeping the diagnostic.
- Security sequencing reversed. A Game Plan draft put RLS after feature completion; the backlog put it at P0. The backlog was right, the preview deployment is already reachable by anyone with the link, so this is present exposure, not prospective.

### Fixed, minor
World-briefing 9-vs-8 miscount and quiz_questions orphan status added to the P0-2 audit; weekly cadence relabeled as a recommendation, not a mandate; P0-1's effort hedged on integration state; "unlimited requests" flagged as ambiguous rather than asserted; referrals added to the RLS risk set; P2-2 split into flag-versus-alerting; Lore Panel and stat-bar reuse claims corrected; a redundant closing section deleted; the phantom branded-confirmation-email item cut.

### Found independently, not in either review
Four additional contradictions now in P0-2: the #e8e6e0/#E8E6E3 text-color mismatch; dossier-cover visibility (Level 1 unlock per System Explanation §2 vs. publicly visible per Strategy §2 and §6); the Next.js-versus-TanStack framework mismatch in Visual Direction §11, which would misdirect every generated UI task; and the missing extraction path from writer-reference material to reader-facing content, now P1-3.

### Not changed, deliberately
- CAPTCHA was recommended in review; it is not in the plan. It contradicts "frictionless signup," the load-bearing assumption behind Level 0-to-1 conversion, and rate limiting plus verified-earning closes most of the same gap. Revisit only if bot traffic is actually observed.
- A dedicated "Phase 2.5" for signal integrity was suggested; folded into Phase 1 instead. Fraud controls and RLS are the same question, "is this data real," separating them invites one to ship without the other.
- Items within each backlog tier are not sorted strictly by effort-vs-impact. Dependency dominates: no ordering of P1 matters if P0-1 hasn't landed.
- P1-2 (reader surface) stays ahead of P1-6 (bulk ingestion) despite ingestion being the larger content unlock, because content with nowhere to render is not content.

### For the author's judgment, unresolvable from the documents
The Level 2 rule, the landing-page composition, and dossier-cover visibility are product decisions, not bugs. Each has a recommendation above, but each changes what readers experience, only the author can ratify them. Make all three in one sitting during Phase 0 and write them into CLAUDE.md; leaving any open means Phase 3 QA is certifying behavior nobody chose.
