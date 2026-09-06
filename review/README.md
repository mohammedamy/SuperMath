# SuperMath revision — 6 September 2026

Base repository commit: `35e86009ab79bc9f16799d758e836194144fcee7`

## Status

The interface and question-count work is implemented in this package. **The request that every question match the real examination’s scope, difficulty and flavour is not fully completed or certified.** This is a revised practice-bank draft, not an exam-ready release. A structural audit was performed across every original and final item; that is not equivalent to independently solving and syllabus-mapping every item.

The public GitHub Pages site has not been changed. The package is intended for review and integration into the existing repository.

## Question counts

| Track | Existing subtracks / levels | Before | After |
|---|---|---:|---:|
| Kangaroo | Ecolier 250; Benjamin 250; Cadet 250; Junior 250 | 635 | 1,000 |
| NAFES | Grade 3: 250; Grade 6: 250; Grade 9: 250 | 704 | 750 |
| KAUST preparation | Three retained internal training levels, 250 each | 468 | 750 |
| NSMO preparation | Three retained internal training levels, 250 each | 431 | 750 |
| JEE mathematics | No subtracks | 260 | 500 |
| Olympiad proof practice | No subtracks | 242 | 500 |
| **Total** | **13 subtracks plus 2 standalone tracks** | **2,740** | **4,250** |

Kangaroo’s actual existing banks cover grades 3–10. The interface no longer advertises nonexistent grade 1–2 and grade 11–12 banks. Those two additional Kangaroo groups were not created in this update.

## Content changes and their limits

- 700 original items were moved out of active banks to `quarantined-items.json`, with reasons and the original content preserved. Reasons include duplicate stems, repeated options, malformed options, missing explanations, unverified inserted diagrams and selected scope risks. A flag is not a claim that every archived item is mathematically wrong.
- 2,040 original items were retained. Most retained items have **not** had an independent, complete mathematical review.
- 2,210 original parameterized practice items were added. They are variants of 66 authored problem families, not 2,210 independent problem designs. Each carries a `family_id` and construction-review metadata. Repeated numerical variations should not be confused with breadth of examination coverage.
- 54 retained ID collisions were repaired.
- 16 specific mathematical, answer-key or wording defects were corrected individually. Examples include the ambiguous factors-of-36 problem, an unstated disjointness condition, a wrong median, a false trigonometric identity, inconsistent functional-equation data, incorrect inclusion–exclusion arithmetic, the assignment-problem minimum, the 24-hour clock count, the periodic-sequence key and the cookies maximum key.
- 256 overescaped bilingual option strings were normalized for MathJax.
- 91 question-specific SVG diagrams were added or repaired; the old practice renderer no longer chooses unrelated images from keywords.
- Olympiad written work now requires mathematical justification and is self-assessed against the worked solution. Legacy placeholder keys are not used to automatically mark proofs.

The additions include foundational and intermediate exercises. **They are not calibrated substitutes for full IMO problems, senior national-olympiad finals, JEE Advanced papers or a verified SRSI placement paper.** This is the main remaining limitation relative to the request.

## Interface and functionality

- Compact SuperMath / Edugates header, navy-and-blue academic styling, clearer spacing and readable controls.
- Practice appears before analytical charts.
- Track cards work with mouse and keyboard and display real loaded counts.
- Hidden subtrack filters no longer eliminate the next selected track’s questions.
- Grade filtering operates on the question pool; topic options are derived from available questions.
- Written reasoning survives hint rendering. Solutions can be revealed without falsely grading text against `0` or `1`.
- Both `$$...$$` and `\[...\]` display mathematics are supported.
- Charts use bank data instead of invented exam percentages; captions distinguish these from official weights.
- Data failures are surfaced. Missing Chart.js does not prevent question-bank loading.
- Printing uses correct MCQ keys, written explanations for FRQs, and question-owned diagrams.
- Print-dialog focus handling and Escape dismissal are included.

## Verification performed

`validation.json` records the results:

- All 4,250 active items pass ID, track, bilingual content, option-count, option-uniqueness and answer-index checks.
- Every existing subtrack meets 250 and both standalone tracks meet 500.
- Every added MCQ’s selected option matches its generated exact answer.
- 309 generated answers were additionally checked by finite enumeration or dynamic programming using their question text, including grid paths, combinations, probabilities and heads-and-legs problems.
- The corrected digital-clock total (79), assignment minimum (9) and sequence value (3) were independently enumerated.
- JavaScript syntax and local static-asset references passed.
- Runtime tests passed startup, all counts, track switching, grade/subtrack filters, MCQ marking, written-answer preservation, printing, Arabic switching and theme switching.

**Not performed:** live-browser screenshots, mobile visual QA, an exhaustive independent solution of all 4,250 items, semantic near-duplicate elimination, examiner difficulty calibration, or full item-by-item official syllabus mapping. The runtime tests use lightweight DOM stubs, not an actual browser.

## Official references consulted

Sources were checked on 6 September 2026. These establish general distinctions and requirements, not certification of the banks.

1. [Kangaroo Mawhiba](https://www.kangarooksa.org/) and [Math Kangaroo official sample guidance](https://mathkangaroo.org/mks/practice/free-question-samples/). Grade grouping and multiple-choice practice are relevant. The US source describes its own question/point structure; local competition rules must be checked separately.
2. [ETEC NAFES](https://nafs.etec.gov.sa/) and [ETEC](https://etec.gov.sa/). The national assessments target grades 3, 6 and 9. A full grade-specific learning-outcome mapping remains necessary.
3. [JEE Main 2026 syllabus](https://jeemain.nta.nic.in/document/syllabus-2026/) and [official syllabus PDF](https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2025/10/202510311323551056.pdf). The mathematics syllabus spans sets/functions, complex numbers/quadratics, matrices, counting, binomial theorem, sequences, calculus, differential equations, coordinate/3D geometry, vectors, statistics/probability and trigonometry. The update adds material in previously thin areas, without claiming examination weight matching.
4. [JEE Advanced 2026 brochure](https://jeeadv.ac.in/documents/IBEnglish_2026.pdf). Main and Advanced must not be treated as interchangeable complete mocks. The current track is mixed mathematics practice.
5. [IMO competition description](https://www.imo-official.org/about/?language=en). The competition consists of six proof problems over two days, three problems in four and a half hours each day. Routine exercises and short numerical questions alone do not reproduce that standard.
6. [KAUST SRSI application process](https://academy.kaust.edu.sa/srsi-application-process/). This describes Grade 11 eligibility and a placement test. It does not establish the repository’s three mathematics phases as official test stages. Their content is retained as internal STEM enrichment and is not represented as a verified placement-test syllabus.
7. [Mawhiba national gifted olympiad / NSMO scientific track](https://www.mawhiba.sa/discover-mawhiba/competitions/national-gifted-olympiad/). The official competition and training pathway should be distinguished from SuperMath’s existing junior/intermediate/senior grade groupings. Those groupings remain internal practice levels.

## Required next content pass

1. Obtain the specific current SRSI mathematics placement-test specification or released sample intended by the owner; otherwise retain the enrichment label.
2. Map every retained question to a concrete grade/exam objective and independently solve it, reconciling English, Arabic, diagram, options and key.
3. Replace routine senior/IMO practice variants with diverse competition-standard problems and rigorous solutions; use independent verification and difficulty review.
4. Benchmark question format, topic balance, diagrams, reasoning demand and difficulty against authorized official sample papers. Add multiple-answer/numerical JEE modes if a complete Advanced mock is desired.
5. Run actual desktop/mobile browser QA and inspect printed output before a public deployment.
