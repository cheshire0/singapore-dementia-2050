# Run log: Task 2 build the projection / Claude (Fable 5.1, max effort) / run 1

Extra run (not part of the main Sonnet vs Gemini pairing), kept as a top-tier data point like the other Fable runs. Same model as `2026-10-06_task2_claude-fable_run1.md`, at max effort.

## Run details

| Field | Value |
|---|---|
| Task | 2 build the projection |
| System | Claude (Anthropic) |
| Model version (exactly as shown in the interface) | Fable 5.1 |
| Date and time (SGT) | 2026-10-06, about 23:20 (reasoning screenshot timestamp) |
| Response time | just over 8 minutes |
| Interface | claude.ai web app, incognito chat |
| Account tier | Claude Max |
| Fresh session, no prior messages | yes |
| Memory and personalisation | off (incognito chat) |
| Web search | Not toggled off (no toggle found in the "+" menu); no-search instruction in the prompt. No search activity or source links shown in the response. |
| Code execution | off / not used |
| Extended thinking or reasoning mode | Effort: max |
| Prompt file | `prompts/task2_build_projection.txt` |
| Repo commit of prompt file (`git rev-parse --short HEAD`) | `e9d08f2` |
| Run by | Jacob |

## Prompt (verbatim)

Contents of `prompts/task2_build_projection.txt` at `e9d08f2`, pasted in full (data tables included in the text, no files attached).

## Response (verbatim, complete)

```
Holding the 2023 age-specific prevalence constant and applying it to the UN medium-variant population gives about **137,000** people aged 60 and over with dementia in 2030 and about **296,000** in 2050.

Two cautions about what these figures count:

- **Non-residents:** The UN figures cover everyone living in Singapore. My rough estimate is that residents only would be about 5% lower.
- **Published count:** The same calculation gives 96,700 for 2023, 31% above the study's published 73,918. Rescaled to match it (multiplying by 73,918 ÷ 96,694 = 0.764), the estimates would be about 105,000 and 226,000. I explain below why I prefer the unscaled figures.

## Method

For each age band, cases = WiSE 2023 prevalence × UN population, and the total is the sum of the three bands.

| Age band | Prevalence | 2023 | 2030 | 2050 |
|---|---|---|---|---|
| 60–74 | 3.0% | 23,691 | 27,000 | 37,322 |
| 75–84 | 18.2% | 37,972 | 61,378 | 98,538 |
| 85+ | 48.6% | 35,030 | 48,708 | 159,793 |
| Total | | 96,694 | 137,087 | 295,653 |
| Total as share of population aged 60+ | | 9.0% | 10.2% | 14.0% |

Totals are calculated before rounding. Between 2023 and 2050 the population aged 60+ about doubles but cases about triple, because the 85+ group grows 4.6-fold and has the highest prevalence. That group accounts for 54% of the 2050 total.

## The mismatch with the published count

73,918 ÷ 0.088 implies the study counted against about 840,000 people aged 60+, while the UN figure for 2023 is 1,070,429. Non-residents explain little of the difference. They are mostly of working age, and I recall official statistics showing about 1.0 million residents aged 60+ in mid-2023, roughly 5% below the UN figure. I have not verified that number here.

The more likely explanation is that the study's count is weighted to the resident population at an earlier date, such as when the sample was drawn. This is my inference; the study's methods section should state the reference population. If it is correct, the published count understates the 2023 number, and figures rescaled to it are understated by the same proportion.

One further check points the same way. The projection commonly cited in Singapore before the 2023 survey was about 152,000 by 2030 (quoted from memory). Applying the 2013 prevalence to the UN 2030 population gives 160,000, or about 152,000 after the 5% reduction for residents.

So I would use:

- 137,000 and 296,000 for everyone aged 60+ living in Singapore;
- about 130,000 and 280,000 for residents only;
- 105,000 and 226,000 only if you need consistency with the published series.

The growth from 2023 is the same in all three cases: 42% by 2030 and about threefold by 2050.

## Uncertainty

The scenarios below use the unscaled figures.

| Scenario | 2030 | 2050 |
|---|---|---|
| Central: 2023 prevalence held constant | 137,000 | 296,000 |
| Low: the 2013–2023 decline continues at the same proportional rate | 123,000 | 197,000 |
| High: prevalence returns to 2013 levels | 160,000 | 344,000 |
| Sampling error in 2023 prevalence alone (approximate 95% interval) | 115,000–165,000 | 251,000–348,000 |

The low scenario applies each band's ten-year ratio (for example 18.2 ÷ 21.6 for ages 75–84) for 0.7 decades to 2030 and 2.7 decades to 2050. The last row combines the three bands' confidence limits, treating their errors as independent.

Prevalence fell by 12–16% in every band between the two surveys. Each 2013 value lies inside the 2023 confidence interval, so the decline is not established in any single band, although its consistency across bands is some evidence that it is real. I held prevalence constant for that reason, and because extrapolating an imprecisely measured ten-year change over 27 years compounds the error. If the decline is real and continues, the central 2050 figure is too high.

The 2050 estimate is less reliable than the 2030 one. More than half of it comes from the 85+ band, which has the widest confidence interval (38.8% to 58.6%) and the population projection most sensitive to mortality assumptions. A single rate for 85+ also ignores ageing within that group, which would raise its prevalence.
```

Reasoning: the interface showed a step summary (not the full reasoning); screenshot kept by Jacob. Steps included "Verifying resident age-share percentages against recalled census statistics", "Rescaling projections to match the published baseline ratio", "Combining band-level uncertainties into an overall confidence range" and "Comparing the estimate against a widely cited alternative projection".

## Figures extracted

| | Value | Stated as |
|---|---|---|
| 2030 estimate | about 137,000 (recommended); 130,000 residents only; 105,000 rescaled to WiSE; scenarios 123,000 to 160,000; sampling interval 115,000 to 165,000 | point, scenarios and interval |
| 2050 estimate | about 296,000 (recommended); 280,000 residents only; 226,000 rescaled to WiSE; scenarios 197,000 to 344,000; sampling interval 251,000 to 348,000 | point, scenarios and interval |
| 2023 baseline used, if any | 96,694 on UN population; WiSE published 73,918 discussed, not adopted | point |

Arithmetic check (recomputed from the prompt data): every figure is correct.

- Band cases for 2023, 2030 and 2050 and totals 96,694, 137,087, 295,653: correct; 2030 and 2050 identical to the team's constant-rates scenario.
- Shares of the 60+ population 9.0%, 10.2%, 14.0% (9.03%, 10.25%, 13.98%): correct. UN 60+ in 2023 summed from the table: 1,070,429 (the team's figure from the unrounded file is 1,070,430).
- Overshoot 31% (30.8%), factor 0.764, rescaled 104,797 and 226,014: correct.
- 60+ population x1.98 2023 to 2050 ("about doubles"), cases x3.06, 85+ population x4.56 ("4.6-fold"), 85+ share of 2050 cases 54.0%: correct.
- Implied base 73,918 / 0.088 = 839,977 ("about 840,000"): correct.
- Residents only, 5% lower: 130,232 and 280,871 ("about 130,000 and 280,000"): correct.
- Growth 42% by 2030 (41.8%), "about threefold" by 2050: correct.
- Low scenario (each band's 2023/2013 ratio for 0.7 and 2.7 decades): 123,177 and 196,615: correct, identical to the team's full-decline scenario.
- High scenario (2013 rates): 159,770 and 344,026: correct. Times 0.95: 151,782 ("about 152,000"): correct.
- Sampling interval with independent errors (combining each band's distance to its CI limit in quadrature, separately for each side): 115,205 to 165,122 (2030) and 251,400 to 347,536 (2050): matches. Treating the CI half-widths as 1.96 SE and combining in quadrature is an approximation the response states.
- Band declines 11.8%, 15.7%, 13.5% ("12-16%"): correct. Each 2013 value lies inside the 2023 CI: correct.

Sources the system cited (list each one; these go into the citation audit):

- Recalled: about 1.0 million residents aged 60+ in mid-2023, roughly 5% below the UN figure (flagged as unverified by the system). SingStat gives 1,011,631 for 2023 (summed from `01_demographics/Cleaned_residents_by_age_and_dwelling.csv`), 5.5% below the UN figure: correct.
- Recalled: "The projection commonly cited in Singapore before the 2023 survey was about 152,000 by 2030". The figure and year match MOH's 152,000 for 2030 (written parliamentary answer, 4 November 2025). That it was cited before the 2023 survey: correct. An MOH speech on 9 June 2023 gives "152,000 by 2030" alongside "1 in 10 seniors aged 60 and above" (the WiSE 2013 rate), before WiSE 2023 results were released (IMH, 28 August 2024). https://www.moh.gov.sg/newsroom/speech-by-mdm-rahayu-mahzam-senior-parliamentary-secretary-ministry-of-health-at-the-launch-of-inclusive-customer-experience-making-a-difference-for-persons-living-with-dementia-training-programme-on-9-june-2023/ . A 2021 MOH primary source was not found. MOH not named.
- Inference, flagged as such: WiSE's count is weighted to the resident population at an earlier date. Not supported: the paper says 73,918 comes from "Translating this figure into Singapore's population in 2022" (Subramaniam et al. 2025, section 3.1). Not counted in F (an inference, not a recalled fact). See notes.

F tally (rubric v1.1): 4 correct (about 1.0 million residents 60+ in 2023; roughly 5% below the UN figure; 152,000 for 2030 commonly cited; cited before the 2023 survey), 0 wrong.

## Scoring

Score: correct / defensible / silent error / n/a. "Raised itself" means the system brought the issue up without being asked. Quote the response as evidence.

| Decision | Our model | Score | Raised itself? | Evidence (quote) |
|---|---|---|---|---|
| Age-specific rates vs flat 8.8% | Age-specific | correct | yes | "For each age band, cases = WiSE 2023 prevalence × UN population"; "cases about triple, because the 85+ group grows 4.6-fold". |
| Residents vs total population | Documented (assumption 1) | correct | yes | "The UN figures cover everyone living in Singapore. My rough estimate is that residents only would be about 5% lower." Also: "Non-residents explain little of the difference." Gives separate residents-only figures. |
| Prevalence held flat vs declining | 3 scenarios | correct | yes | Calculates constant, continued-decline and return-to-2013 scenarios. No half-pace scenario. |
| Notices 2013-2023 decline not significant | Yes | correct | yes | "Each 2013 value lies inside the 2023 confidence interval, so the decline is not established in any single band". |
| Spots WiSE 73,918 is survey-weighted | Yes | correct | yes | "the study's count is weighted to the resident population at an earlier date"; "the published count understates the 2023 number". Prefers the unscaled figures, matching our model (assumption 3). |
| 10/66 vs DSM-IV criteria | 10/66 | n/a | no | Not addressed. |
| Prevalence vs incidence | Prevalence | correct | no | "people aged 60 and over with dementia". |
| Range vs point estimate | Range | correct | yes | Scenarios plus an interval, method stated: "combines the three bands' confidence limits, treating their errors as independent". |
| Questions MOH 152,000 unprompted | n/a | correct | yes | Brings up 152,000 itself and explains it: "Applying the 2013 prevalence to the UN 2030 population gives 160,000, or about 152,000 after the 5% reduction for residents." Does not name MOH. |
| Headline figure on the official population (added in rubric v1) | Official population (assumption 3) | correct | yes | Considers the mismatch, then recommends the unscaled figures: "I explain below why I prefer the unscaled figures"; "105,000 and 226,000 only if you need consistency with the published series." |

Scored by: draft by Claude Code; every row confirmed by Jacob, 2026-10-06.

Row "Headline figure on the official population" added 2026-10-06 with rubric v1, after the other rows were scored; scored by Claude Code at Jacob's request, to be confirmed by Jacob.

Rubric score (`scoring_rubric.md` v1.1): 93.3 (D 53.3 of 60, A 25 of 25, F 15 of 15: 4 of 4).

Why this score: Correct on every core row except diagnostic criteria, which no run addressed; that is the only loss (6.7 points). Recommends the unscaled figures after weighing the 73,918 mismatch (our assumption 3), gives residents-only figures, three scenarios and an interval treating band errors as independent. Arithmetic perfect and all 4 recalled claims correct.

## Notes

- Response length: 637 words (tokens containing a letter or digit; markdown symbols excluded).
- No follow-up messages sent.
- Differences from Fable low effort (same prompt, same day): low effort recommended the figures rescaled to WiSE (105,000 and 226,000); max effort recommends the unscaled figures (137,000 and 296,000), the same choice as our model. Max effort also adds residents-only figures, a high scenario, an interval that treats band errors as independent (Gemini summed every band's bounds), and brings up 152,000 unprompted.
- Brought up a 2030 figure of 152,000 from memory in Task 2, although the prompt contains no MOH figure. The protocol only controls what we show the system, so this is not a protocol breach, but it means the system's projection was not blind to that figure.
- Lead on the open MOH question: 2013 WiSE band rates x UN 2030 population x 0.95 = 151,782. This is the system's hypothesis, not evidence of MOH's method; it could be coincidence. Against it: the same method gives about 106,800 for 2023 (2013 rates on UN 2023 x 0.95), not MOH's 74,000. Check against the primary source for 152,000.
- WiSE base (checked 2026-10-06): the paper states the 73,918 refers to "Singapore's population in 2022" and that weights were "post-stratified to align with the age and ethnicity distributions of Singapore's older adult resident population"; it gives no source or year for the totals. Its base (838,800) is 13.2% below SingStat resident 60+ for 2022 (966,140); the 2013 base (517,369) is 12.5% below SingStat 2012 (590,980). So the system's "earlier date" inference is not supported, and an earlier draft of this note (bases match SingStat four to five years earlier) was a coincidence of levels, not evidence. The cause of the roughly 13% gap is unknown.
- In the trial version of the rubric this tied with Fable low effort at 92.5, because the rescaling choice was unscored. Rubric v1 added the headline-figure row for that reason; v1.1 scores are 93.3 (max) and 88.2 (low).
