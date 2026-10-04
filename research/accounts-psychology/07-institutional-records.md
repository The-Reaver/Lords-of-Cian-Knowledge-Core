# 07 -- Institutional Records: How Bureaus Write, and How They Misread

Evidence synthesis for writing in-world dossiers, field reports, informant notes, and redacted
archive copies. The target is a pre-industrial intelligence bureau: clerks, field officers,
informant streams, a sealed analytic office, a redaction desk, and a director, with no computers.

---

## 1. Scope and search method

**Question.** What does the research and official-standards literature say about (a) how
intelligence, police, military, and bureaucratic institutions structure their written reports,
and (b) the systematic ways those institutions misread the world? What are the textual markers of
each, usable on the page?

**Method.** I verified sources by web search on 2026-10-04: official standards documents (ODNI ICD
203 and ICD 206, the NATO/Admiralty grading system), the primary texts (Kent, Heuer, Wohlstetter,
Jervis, Vaughan, Scott, Trouillot), and the empirical work that tests them (Mandel & Barnes; Dhami
& Mandel; Dhami, Belton & Mandel; Friedman et al.; Wintle et al.; Neuschatz et al.; Walker et al.;
Moreno-Medina et al.). I prioritized official standards, reviews, and large-sample or experimental
studies. Book-length case studies count as influential qualitative evidence, not as experiments.
Any citation I could not confirm is marked **[unverified]**. Where a finding rests mainly on case
studies, the grade says so.

**Grades.**
- **STRONG:** codified in official standards, or replicated empirically across independent studies.
- **MODERATE:** one strong study plus convergent qualitative or case evidence, or multiple
  influential case studies with a shared mechanism.
- **CONTESTED/WEAK:** influential but poorly supported empirically, or disputed.

**Limits.** Most of the empirical work is modern and Anglo-American. Transferring it to a
pre-industrial bureau means applying the mechanisms (category, incentive, workflow, compression),
not the technology. The police-language and euphemism findings come from news and lab settings. As
evidence about internal files they are suggestive, not direct.

---

## 2. Findings

### F1. Institutions encode uncertainty in words, and readers decode those words inconsistently

**Grade: STRONG.**

Kent (1964) found that a phrase like "serious possibility" in a National Intelligence Estimate was
read by its own authors as anything from about 20% to 80%. He proposed a fixed word-to-odds table
and split analysts into "poets," who prefer words, and "mathematicians," who prefer numbers. The
CIA did not adopt it in his lifetime. ICD 203 (ODNI 2015) now mandates a seven-step lexicon:
- Almost no chance (01-05%)
- Very unlikely (05-20%)
- Unlikely (20-45%)
- Roughly even chance (45-55%)
- Likely (55-80%)
- Very likely (80-95%)
- Almost certain (95-99%)

It also tells analysts not to mix rows and to state confidence separately from likelihood.

Experiments show the lexicon is still misread. Wintle et al. (2019, n=924) found readers' numeric
interpretations of ICD 203 terms often fell outside the mandated ranges unless the numbers were
printed next to the words. Dhami & Mandel (2021) review the field and argue that words-only
lexicons stay ambiguous and regress toward the middle. Friedman et al. (2018) coarsened 888,328
tournament forecasts into verbal bins and found a consistent loss of accuracy.

**On the page.**
- A bureau should have a house scale of estimative words, enforced by the sealed office and drifted
  away from by the field.
- Field reports use loose words ("it is thought," "there is talk").
- The analytic summary converts them to the house scale ("probable"), and the director's brief
  compresses that to a bare verdict ("He is in the city").
- Each step loses the uncertainty. A marginal note by a careful clerk ("probable *how*?") marks the
  gap.
- A mature bureau keeps two separate fields: **Likelihood** (how probable is the claim) and
  **Confidence** (how good is our basis). Confusing the two is a realistic in-world error.

### F2. Expert institutional forecasts can be well calibrated, but the errors are systematic

**Grade: MODERATE.**

Mandel & Barnes (2014, PNAS) scored over 1,500 strategic forecasts from a real assessment unit
covering about six years. Discrimination and calibration were good. Where analysts were
miscalibrated, they were *underconfident*: they hedged more than their accuracy warranted,
especially on hard questions and on questions flagged as important to policy. Friedman &
Zeckhauser (2012), working from nearly 400 declassified NIEs, argue that tradecraft tries to
*eliminate* uncertainty when it should *assess* it, which pushes products toward vagueness.

Only one large calibration dataset exists, hence MODERATE.

**On the page.** A competent sealed office is not usually *wrong*. It is usually *hedged*, and it
hedges most on the items the director cares most about. Its products thicken with qualifiers
exactly where the stakes rise ("cannot be excluded," "remains a possibility worth monitoring").
The institution's characteristic failure is a confident category error (F4-F6), not a bad
probability on a well-posed question.

### F3. Source reliability and information credibility are graded separately, and in practice they bleed together

**Grade: STRONG** for the system; **MODERATE** for the bleed-through.

The Admiralty/NATO system (AJP-2.1, STANAG 2511, with reporting formats under STANAG 2022) gives
every item two grades:
- **A letter for the source:** A completely reliable, B usually reliable, C fairly reliable, D not
  usually reliable, E unreliable, F reliability cannot be judged.
- **A digit for the information:** 1 confirmed by other sources, 2 probably true, 3 possibly true,
  4 doubtful, 5 improbable, 6 truth cannot be judged.

Doctrine says the two must be judged independently. ICD 206 (ODNI) adds that sourcing must be
transparent enough for a reader to judge the quality and scope of the sources and retrieve them.

Empirically, users do not keep the axes apart. Samet (1975, US Army Research Institute; 37 Army
captains) found that credibility drove judgments of accuracy more strongly than reliability did.
Baker, McKendry & Mace (1968, ARI Technical Research Note 200) is the earlier operational study of
these ratings. Its specific correlation result is as reported in the secondary literature
**[unverified content]**. Later work by Irwin & Mandel (2019, *Intelligence and National Security*)
critiques the system's ambiguity and its lack of independence **[unverified: title and pages not
confirmed by search]**.

**On the page.**
- Give every informant line a two-character grade: **B2**, **D3**, **F6**.
- A trusted source's report gets graded up ("A-source, so 2") without corroboration. A
  marginal "credibility raised on source standing -- not independently confirmed" is the honest
  version of this error.
- **F6** ("cannot be judged") is the most common grade on new walk-ins. Bureaucratic pressure
  moves it to **C3** within a few reports, through familiarity rather than verification.
- A grade survives copying while the reasoning behind it does not. By the archive copy, "B2" has
  become a fact about the world.

### F4. Analysts see what their categories and expectations let them see

**Grade: STRONG** for the mechanism (cognitive psychology); **MODERATE** for the corrective tools.

Heuer (1999) synthesizes the cognitive-psychology evidence:
- Perception is shaped by expectation.
- New information gets assimilated to existing images.
- Analysts overweight vivid and consistent evidence and underweight absent evidence.
- Initial hypotheses anchor.

His remedy is Analysis of Competing Hypotheses (ACH): list every hypothesis, then score evidence
by how well it *discriminates* among them, not by how well it fits the favored one. Testing does
not support the remedy cleanly. Dhami, Belton & Mandel (2019; 50 analysts, randomized) found that
analysts trained in ACH did not follow all its steps, that the evidence it reduces confirmation
bias was mixed, and that it may *increase* inconsistency. Rossmo (2009) documents the same failure
in police work as "tunnel vision": settling early on a suspect and then filtering evidence toward
that suspect.

**On the page.**
- The file already has a working theory in its title line ("Re: the Harbor Conspiracy"). Every
  later entry is filed under it, so evidence that doesn't fit has nowhere to go.
- A bureau may have a formal "competing accounts" sheet, and its clerks fill it in pro forma: the
  favored hypothesis gets a full paragraph, the rest a line each.
- Absent evidence is not recorded ("no sign of X") unless someone was told to look for X.

### F5. Warning failures are signal-to-noise and attention failures, not missing data

**Grade: MODERATE** (foundational case studies, convergent).

Wohlstetter (1962) showed that before Pearl Harbor the signals of attack were present but buried
in noise. They were dispersed across agencies and drowned out by competing alarms, and they were
read through the prevailing expectation that the target would be elsewhere. Jervis (2010) examined
two failures: CIA's belief that the Shah was secure in 1978, and the 2002 Iraq WMD estimate. He
rejects political pressure and groupthink as sufficient explanations. In his account the failures
came from weak attention to how information should be interpreted, lack of self-awareness about
the basis of judgments, and a culture that didn't probe its own weak points. The Iraq estimate had
an internally coherent story that rested on stacked inferences.

**On the page.**
- The decisive warning *is in the archive*, in a minor field report, filed under the wrong
  heading, initialed and passed on.
- After the event, a post-mortem memo finds it and quotes it in full. The memo's tone of
  institutional surprise ("the information was in our possession") is the marker.
- Before the event, the bureau's attention budget is visible: some report types get a full reading
  log, others a stamp.

### F6. Organizations normalize anomalies until they stop being anomalies

**Grade: MODERATE** (deep ethnography; widely replicated as a concept in safety science, not
experimentally).

Vaughan (1996) traced how NASA engineers met repeated O-ring erosion. Each time a flight survived
an anomaly, the anomaly was redefined as an acceptable, understood risk. No rule was broken. The
culture's own procedures produced the decision. The deviance was normalized *through* paperwork:
each acceptance became precedent for the next.

**On the page.** Look for a recurring line in successive reports that softens over time:
- Report 1: "Irregularity in the courier count -- flagged for review."
- Report 7: "Courier count variance within expected range."
- Report 15: the field is gone from the form.

The archive preserves the drift, and no single document shows a decision.

### F7. States see through the categories they build for administration

**Grade: MODERATE** (influential historical synthesis; supported by archival scholarship).

Scott (1998) argues that states make populations "legible" by imposing standardized categories:
fixed surnames, cadastral maps, census categories, standard measures. Those categories become both
what the state can see and what it acts on, and whatever doesn't fit is invisible or treated as
disorder. Stoler (2009), reading the nineteenth-century Netherlands Indies archive, shows that
colonial files record their categories *failing*. Officials hedge, revise, and argue in the
margins about who counts as what. The archive is a record of administrative anxiety as much as of
fact.

**On the page.**
- Every subject is forced into the bureau's taxonomy ("Class 3 agitator," "debtor-of-record,"
  "unaffiliated").
- A real person who straddles two categories gets two files that never meet.
- The tell of a category failure is a form field filled with "other," "misc.," or a scrawled
  subcategory the printed form never anticipated.
- Margins are where the institution argues with itself: "Not a Class 3 -- no affiliation found.
  Retain Class 3 for continuity."

### F8. Report language shifts agency away from the institution

**Grade: MODERATE.** Strong for news language, experimentally supported for reader effects;
indirect for internal files.

Moreno-Medina, Ouss, Bayer & Ba (2025, *QJE*) analyzed over 190,000 US TV news stories. Coverage
of police killings used responsibility-obscuring structures (passive voice, nominalizations,
intransitive verbs) far more than coverage of civilian killings, especially in the first sentence.
Their evidence points to police-department narratives as the likely origin. In an online
experiment, the obfuscatory phrasing reduced readers' attribution of moral responsibility. Orwell
(1946) is the classic framing: "pacification," "transfer of population," and the phrase that
"names things without calling up mental pictures of them." He is cited as argument, not evidence.

**On the page.** Institutional agency vanishes grammatically:
- "The subject was injured during the detention."
- "An exchange of force occurred."
- "The premises were rendered unusable."

Compare the field officer's first draft ("I struck him twice"), the supervisor's revision ("force
was applied"), and the filed copy ("the subject was subdued"). Others' agency, meanwhile, is
active and specific: "The subject *attacked*."

### F9. Euphemism changes judgments without being read as lying

**Grade: MODERATE** (two independent experimental lines).

Walker et al. (2021; n=1,906) found that replacing a disagreeable term with an agreeable relative
("enhanced interrogation" for "torture") made actions seem more acceptable. Readers judged
euphemistic speakers more trustworthy than liars and the descriptions as largely truthful. Detail
reduced the effect but did not eliminate it. Farrow, Grolleau & Mzoughi (2021) found that
euphemisms made unethical corporate practices seem less unethical.

**On the page.** Euphemism lets an institution soften a record without falsifying it, which makes
it the safest tool for a careful file-keeper. Give the bureau a standing euphemism vocabulary:
- "Retired" (killed)
- "Reassigned" (purged)
- "Placed in quiet keeping" (imprisoned without process)
- "Processed" (anything)

A new clerk who writes the plain word gets corrected in the margin. The reader who knows the
vocabulary can decode it.

### F10. Informant-driven error is a leading, documented failure mode

**Grade: STRONG** (convergent: official inquiry, case compilation, experiment, legal scholarship).

The WMD Commission (2005) found that the mobile-bioweapons-lab judgment rested heavily on a single
fabricating source, "Curveball," who was never adequately vetted. An analyst who raised doubts was
sidelined, and the institution resisted retraction out of concern for how it would look upward.
The SSCI (2004) found that the Iraq assessments overstated what the underlying reporting
supported. In criminal justice, Warden (2004, Northwestern Center on Wrongful Convictions) found
false informant testimony in about 45.9% of 111 capital exonerations from 1973 to 2004, the
largest single factor. Neuschatz et al. (2008) found that telling mock jurors about an informant's
incentive did *not* reduce the testimony's persuasive effect. Natapoff (2009) documents how
informant deals make the process secret and dependent on what the informant says.

**On the page.**
- Informant streams are graded, paid, and protected by a handler whose standing depends on the
  stream staying valuable. That is a structural incentive *not* to downgrade.
- A cryptonym replaces the name in every copy above the handler.
- Single-source dependence is visible in the citations: three "independent" reports trace back to
  one cryptonym through a sub-source.
- Payment logs and grades sit in different files, so no one ever sees that the source's grade
  went up as the payments rose.
- The retraction, if it comes at all, is a small notice that never travels to the copies already
  sent up.

### F11. Archives are made by silencing at four separate moments

**Grade: MODERATE** (influential theoretical framework, consistent with Stoler).

Trouillot (1995) identifies four moments where silence enters history:
1. When facts are created (what is recorded at all).
2. When they are assembled into archives (what is kept and how it is indexed).
3. When they are retrieved (what gets pulled for a narrative).
4. When retrospective significance is assigned (what history says it meant).

His central case is the Haitian Revolution, which contemporaries found "unthinkable" and the
record therefore failed to register properly.

**On the page.** Redaction is only the last and crudest silence. In a bureau the earlier ones
matter more:
- The field officer never wrote it down.
- The clerk filed it under a closed case.
- The index has no heading for it.
- The director's brief summarized it out.

A redacted archive copy should show all four: blacked lines, missing enclosures ("Encl. 3 -- not
retained"), an index card with no matching file, and a later reviewer's note, "Significance
unclear; not pursued."

### F12. "Groupthink" is a popular explanation with weak empirical support

**Grade: CONTESTED/WEAK.**

Janis (1972) proposed groupthink from historical case studies. Cohesive groups under stress and
directive leadership converge prematurely and show symptoms such as an illusion of unanimity and
self-censorship. Esser's (1998) 25-year review found limited and mixed support for the full causal
model, much of it from case studies. Baron (2005) argued that the symptoms Janis described appear
broadly in ordinary group polarization, not only under his antecedent conditions, which undermines
the model as a specific theory. Jervis (2010) rejects groupthink as an adequate explanation of the
Iran and Iraq failures.

**On the page.** Characters inside the bureau will *say* "the Council fell into one mind." That is
in-world folk theory, and it can be wrong. A better-grounded portrayal of collective error uses:
- Shared categories (F7)
- A shared working theory (F4)
- Incentives (F10)
- Drift (F6)

---

## 3. Implications by teller state

**Informed (the bureau knows and writes accurately).**
- Two-axis grades are honest, F6 is used without shame, and likelihood and confidence are kept
  separate.
- Absent evidence is recorded explicitly ("checked, nothing found").
- Every judgment cites its sources down to the cryptonym and sub-source.
- Hedging is proportional, not defensive.
- Marginalia disagree openly and get answered.

**Uninformed (an institution confidently wrong).** This is the most realistic state and the one
the literature best supports.
- The prose is fluent, clean, and consistent, because the categories (F7) and the working theory
  (F4) do the work.
- The markers are a stable vocabulary, no "other" entries, citations that converge on one source,
  and confident compression from field report to brief (F1).
- Euphemism and passive voice are habit, not concealment (F8-F9).
- Nobody is lying. The error appears only when a later document collides with this one. When a
  reader-facing reveal is needed, stage it as two files that were never cross-indexed.

**Mistaken (an honest error, recoverable).**
- A single officer misreads, misgrades, or misfiles.
- The marker is local inconsistency: a grade at odds with the narrative, a date that doesn't match
  the courier log, a name spelled two ways.
- Mistakes leave *seams*, and a careful reader or an in-world auditor finds them by cross-checking.
- Corrections appear as dated amendments, a "correction slip," or a struck line with initials.

**Deliberately lying (a file falsified to protect the institution or an officer).**
- The evidence (Curveball's handling; Vaughan's post-hoc rationales) suggests institutional lying
  more often takes the form of *omission, delay, and selective transmission* than invented facts.
- Markers:
  - Missing enclosures.
  - A retraction never forwarded.
  - A grade upgraded without a recorded reason.
  - A field report "superseded" by a summary that cites it but contradicts it.
  - Unusual uniformity: several "independent" accounts with identical phrasing.
  - Euphemism stiffening into code.
  - A sudden switch to passive voice at exactly the moment of an officer's own act.
- Outright forgery shows in the physical record: a different hand or ink, a page out of the
  clerk's numbering sequence, a reading log with no entry for the inserted page.
- Per Walker et al., a skilled liar inside an institution prefers euphemism to falsehood because it
  carries no reputational cost.

---

## 4. Implications by account type: the Dossier

The Dossier is the main consumer. Each template below is a skeleton for a pre-industrial bureau.
Square-bracketed items are fill-ins.

### (a) Field Report (field officer to section clerk)

```
FIELD REPORT                         Ser. No. [section]-[year]-[running no.]
From: [officer's working name / number]      To: [Section] Clerk
Date written: [ ]   Date of events: [ ]   Place: [ ]
Courier: [hand / relay mark]         Copies: 1 (original only)

SUBJECT: [person/place as officer knows it -- often a nickname]

1. What I saw myself: [first person, concrete, active voice]
2. What I was told: [by whom -- cryptonym; how they would know]
3. What I think it means: [loose estimative words: "I believe," "looks like"]
4. What I could not find out: [often blank -- its absence is a marker]
5. Expenses / payments made: [sums, to whom]

Signed: [mark]
[Clerk's receipt stamp]  [Clerk's marginal query, if any]
```

Markers: first person, concrete detail, grammar errors, local names, the honest "I don't know."
This is the most truthful and least legible document in the chain.

### (b) Analytic Assessment (sealed analytic office to director)

```
SEALED OFFICE -- ASSESSMENT          Ref: SO/[year]/[no.]   Handling: [tier]
Prepared by: [analyst initials]  Reviewed: [senior initials]  Date: [ ]
File heading: [the bureau's category, e.g. "Harbor Conspiracy (Class 3)"]

KEY JUDGMENT
  [Subject] is [house-scale term, e.g. PROBABLY] [claim].
  Confidence in this judgment: [LOW / MODERATE / HIGH], because [basis].

BASIS
  Reporting cited: [Ser. Nos.] -- graded [B2], [C3], [F6] ...
  Corroboration: [independent? or traced to single cryptonym]
  Contrary or absent reporting: [often thin]

ALTERNATIVES CONSIDERED
  [Favored hypothesis: full paragraph]
  [Others: one line each]

GAPS / WHAT WOULD CHANGE THIS JUDGMENT
  [ ]

Distribution: Director; [Section heads]   Copy [n] of [n]
```

Markers: the house estimative scale, the category in the heading, passive voice ("it is
assessed"), two-axis grades cited without the reasoning, compression of the field reports'
uncertainty, a formulaic and lopsided alternatives section.

### (c) Informant Contact Note (handler to informant registry)

```
CONTACT NOTE                         Registry No.: INF-[cryptonym]
Handler: [number]   Contact date: [ ]   Place: [safehouse code]
Initiated by: [handler / source]     Duration: [ ]
Source condition: [sober / anxious / evasive / demanding]

Information given (verbatim where possible): [ ]
Source's access to this: [direct / sub-source "[sub-cryptonym]" / hearsay]
Handler's grade: Source [A-F]  Information [1-6]
Grade change since last contact: [ ] Reason recorded: [ ]
Payment: [sum]  Running total this year: [ ]   (held in Payments Ledger, not here)
Tasking given: [ ]
Security concerns: [ ]
Handler's comment: [ ]
```

Markers: the cryptonym only, the grade sitting next to the handler's own interest, payments kept
in a separate ledger (the F10 incentive gap), a blank "reason recorded" for a grade change, a
sub-source chain that makes later "corroboration" circular.

### (d) Redacted Archive Copy (registry, for retention or release)

```
ARCHIVE COPY -- NOT ORIGINAL         Reg. Box [ ] / File [ ] / Item [ ]
Copied by: [clerk no.]  Date copied: [ ]  Copy of: [Ser./Ref. No.]
Review authority: [office]   Review date: [ ]

[Body text with ████ blocks over names, places, sums, and dates]
Encl. 1 -- retained   Encl. 2 -- withdrawn [ref]   Encl. 3 -- not retained
Original: destroyed under [order no.] / held at [restricted location]

Reviewer's note: [e.g. "Significance unclear; not pursued."]
Index cards: [subject card] [cross-reference card -- may point to a file not in the box]
```

Markers: all four of Trouillot's silences (F11), redactions concentrated around an officer's own
acts, withdrawn enclosures with no withdrawal record, a reviewer's note that assigns
insignificance, and index cards that point nowhere. When an original was destroyed, the copy is
the only record, so the clerk's choices become the history.

**How the three registers differ.** The same event moves through three documents:
- **Field report:** "I struck him twice; he went down near the well."
- **Assessment:** "Force was applied; the subject was detained. Reporting [B2] indicates probable
  Class 3 affiliation."
- **Director's brief:** "Harbor cell disrupted."

Each step is shorter, more passive, more categorical, and more confident. The first document is
always the most informative, so in fiction, recovering it is the reveal.

---

## 5. Reference list

1. Baker, J. D., McKendry, J. M., & Mace, D. J. (1968). *Certitude judgments in an operational
   environment* (Technical Research Note 200). US Army Behavioral Science Research Laboratory.
   Catalog: https://mocat.library.unt.edu/catalog/892-6448 (bibliographic record verified; specific
   correlation finding as reported secondarily **[unverified content]**).
2. Baron, R. S. (2005). So right it's wrong: Groupthink and the ubiquitous nature of polarized
   group decision making. *Advances in Experimental Social Psychology*, 37, 219-253. (Existence and
   2005 date confirmed; volume and pages **[unverified]**.)
3. Commission on the Intelligence Capabilities of the United States Regarding Weapons of Mass
   Destruction (Robb-Silberman). (2005). *Report to the President of the United States*, March 31,
   2005. https://irp.fas.org/offdocs/wmdcomm.html
4. Dhami, M. K., Belton, I. K., & Mandel, D. R. (2019). The "analysis of competing hypotheses" in
   intelligence analysis. *Applied Cognitive Psychology*, 33(6), 1080-1090.
   https://doi.org/10.1002/acp.3550
5. Dhami, M. K., & Mandel, D. R. (2021). Words or numbers? Communicating probability in
   intelligence analysis. *American Psychologist*, 76(3), 549-560.
   https://repository.mdx.ac.uk/item/88xz2
6. Esser, J. K. (1998). Alive and well after 25 years: A review of groupthink research.
   *Organizational Behavior and Human Decision Processes*, 73(2-3), 116-141.
7. Farrow, K., Grolleau, G., & Mzoughi, N. (2021). Let's call a spade a spade, not a gardening
   tool: How euphemisms shape moral judgement in corporate social responsibility domains. *Journal
   of Business Research*. https://hal.inrae.fr/hal-03351278/document (full title and venue
   **[unverified]**; the finding is confirmed via the repository record).
8. Friedman, J. A., & Zeckhauser, R. (2012). Assessing uncertainty in intelligence. *Intelligence
   and National Security*, 27(6), 824-847.
   https://www.hks.harvard.edu/publications/assessing-uncertainty-intelligence-0
9. Friedman, J. A., Baker, J. D., Mellers, B. A., Tetlock, P. E., & Zeckhauser, R. (2018). The
   value of precision in probability assessment: Evidence from a large-scale geopolitical
   forecasting tournament. *International Studies Quarterly*, 62(2), 410-422.
   https://doi.org/10.1093/isq/sqx078
10. Heuer, R. J., Jr. (1999). *Psychology of Intelligence Analysis*. Center for the Study of
    Intelligence, CIA.
    https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
11. Irwin, D., & Mandel, D. R. (2019). Improving information evaluation for intelligence
    production. *Intelligence and National Security* **[unverified -- not located by search;
    cited from memory, do not rely on details]**.
12. Janis, I. L. (1972). *Victims of Groupthink*. Houghton Mifflin.
13. Jervis, R. (2010). *Why Intelligence Fails: Lessons from the Iranian Revolution and the Iraq
    War*. Cornell University Press. https://doi.org/10.7591/9780801458859
14. Kent, S. (1964). Words of estimative probability. *Studies in Intelligence*, 8(4).
    https://www.cia.gov/resources/csi/studies-in-intelligence/archives/vol-8-no-4/words-of-estimative-probability
15. Mandel, D. R., & Barnes, A. (2014). Accuracy of forecasts in strategic intelligence.
    *Proceedings of the National Academy of Sciences*, 111(30), 10984-10989.
    https://pmc.ncbi.nlm.nih.gov/articles/4121776/ (volume and pages from memory
    **[unverified]**; article confirmed.)
16. Moreno-Medina, J., Ouss, A., Bayer, P., & Ba, B. A. (2025). Officer-involved: The media
    language of police killings. *Quarterly Journal of Economics*, 140(2), 1525-1580. (NBER Working
    Paper 30209.) https://nber.org/papers/w30209
17. NATO. *AJP-2.1, Allied Joint Doctrine for Intelligence Procedures* (STANAG 2511); reporting
    formats under STANAG 2022. Overview of the A-F / 1-6 grading:
    https://en.wikipedia.org/wiki/Admiralty_code (primary doctrine text not retrieved; the grading
    scheme itself is confirmed across multiple secondary sources).
18. Natapoff, A. (2009). *Snitching: Criminal Informants and the Erosion of American Justice*. New
    York University Press.
    https://hls.harvard.edu/bibliography/snitching-criminal-informants-and-the-erosion-of-american-justice
19. Neuschatz, J. S., Lawson, D. S., Swanner, J. K., Meissner, C. A., & Neuschatz, J. S. (2008).
    The effects of accomplice witnesses and jailhouse informants on jury decision making. *Law and
    Human Behavior*, 32, 137-149. https://link.springer.com/article/10.1007/s10979-007-9100-1
    (author list partly from memory **[unverified]**; article and findings confirmed.)
20. Office of the Director of National Intelligence. (2015). *Intelligence Community Directive
    203: Analytic Standards*. https://www.dni.gov/files/documents/ICD/ICD-203.pdf
21. Office of the Director of National Intelligence. *Intelligence Community Directive 206:
    Sourcing Requirements for Disseminated Analytic Products*.
    https://irp.fas.org/dni/icd/icd-206.pdf
22. Orwell, G. (1946). Politics and the English language. *Horizon*, 13(76). (Used as framing, not
    evidence.)
23. Rossmo, D. K. (Ed.). (2009). *Criminal Investigative Failures*. CRC Press.
    https://www.routledge.com/products/9780429248306
24. Samet, M. G. (1975). *Subjective interpretation of reliability and accuracy scales for
    evaluating military intelligence*. US Army Research Institute for the Behavioral and Social
    Sciences. https://apps.dtic.mil/sti/pdfs/ADA003260.pdf (title per catalog search; a related
    *Human Factors* publication **[unverified]**.)
25. Scott, J. C. (1998). *Seeing Like a State: How Certain Schemes to Improve the Human Condition
    Have Failed*. Yale University Press.
26. Senate Select Committee on Intelligence. (2004). *Report on the U.S. Intelligence Community's
    Prewar Intelligence Assessments on Iraq*. July 7, 2004.
    https://catalog.hathitrust.org/Record/005236453
27. Stoler, A. L. (2009). *Along the Archival Grain: Epistemic Anxieties and Colonial Common
    Sense*. Princeton University Press.
28. Trouillot, M.-R. (1995). *Silencing the Past: Power and the Production of History*. Beacon
    Press.
29. Vaughan, D. (1996). *The Challenger Launch Decision: Risky Technology, Culture, and Deviance at
    NASA*. University of Chicago Press.
30. Walker, A. C., Turpin, M. H., Meyers, E. A., Stolz, J. A., Fugelsang, J. A., & Koehler, D. J.
    (2021). Controlling the narrative: Euphemistic language affects judgments of actions while
    avoiding perceptions of dishonesty. *Cognition*, 211, 104633. (Finding and n=1,906 confirmed;
    author list, volume, and article number from memory **[unverified]**.)
31. Warden, R. (2004). *The Snitch System: How Snitch Testimony Sent Randy Steidl and Other
    Innocent Americans to Death Row*. Center on Wrongful Convictions, Northwestern University School
    of Law.
    https://deathpenaltyinfo.org/new-resource-center-on-wrongful-convictions-examines-the-snitch-system
32. Wintle, B. C., Fraser, H., Wills, B. C., Nicholson, A. E., & Fidler, F. (2019). Verbal
    probabilities: Very likely to be somewhat more confusing than numbers. *PLoS ONE*, 14(4),
    e0213522. https://pmc.ncbi.nlm.nih.gov/articles/PMC6469752/
33. Wohlstetter, R. (1962). *Pearl Harbor: Warning and Decision*. Stanford University Press.
    https://doi.org/10.1515/9781503620698
