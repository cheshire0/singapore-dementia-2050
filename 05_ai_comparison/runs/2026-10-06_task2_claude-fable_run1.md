# Run log: Task 2 build the projection / Claude (Fable 5.1) / run 1

Extra run (not part of the main Sonnet vs Gemini pairing), kept as a top-tier data point like the Task 1 Fable runs.

## Run details

| Field | Value |
|---|---|
| Task | 2 build the projection |
| System | Claude (Anthropic) |
| Model version (exactly as shown in the interface) | Fable 5.1 |
| Date and time (SGT) | 2026-10-06 (time of day not recorded) |
| Response time | under 1 minute |
| Interface | claude.ai web app, incognito chat |
| Account tier | Claude Max |
| Fresh session, no prior messages | yes |
| Memory and personalisation | off (incognito chat) |
| Web search | Not toggled off (no toggle found in the "+" menu); no-search instruction in the prompt. No search activity or source links shown in the response. |
| Code execution | off / not used |
| Extended thinking or reasoning mode | Effort: low |
| Prompt file | `prompts/task2_build_projection.txt` |
| Repo commit of prompt file (`git rev-parse --short HEAD`) | `e9d08f2` |
| Run by | Jacob |

## Prompt (verbatim)

Contents of `prompts/task2_build_projection.txt` at `e9d08f2`, pasted in full (234 words; data tables included in the text, no files attached).

## Response (verbatim, complete)

Transcribed from the response text pasted by Jacob. Formatting such as bold is approximate.

```
**Estimate:** about 105,000 Singapore residents aged 60+ with dementia in 2030 and about 226,000 in 2050, on a basis consistent with the published WiSE counts. If the UN population figures are used without adjustment, the numbers are about 137,000 and 296,000.

## Method

1. **Apply 2023 age-specific prevalence to the UN population in each band.** This assumes prevalence within each band stays at its 2023 level.

| Age band | 2023 prevalence | 2030 cases | 2050 cases |
|---|---|---|---|
| 60-74 | 3.0% | 27,000 | 37,322 |
| 75-84 | 18.2% | 61,378 | 98,538 |
| 85+ | 48.6% | 48,708 | 159,793 |
| Total | | 137,087 | 295,653 |

2. **Check the method against 2023.** The same calculation on the 2023 UN population gives 96,694 cases, against the published 73,918. The method overshoots by 31%.

3. **Identify the cause.** Age structure is not the cause: the UN age mix implies a crude prevalence of 9.0%, close to the published 8.8%. The gap is in the population base. The published count implies about 840,000 people aged 60+ (73,918 / 0.088), while the UN figure is 1,070,429.

4. **Calibrate.** Multiplying by 73,918 / 96,694 = 0.764 gives 104,797 for 2030 and 226,014 for 2050.

## Which figure to use

| Scenario | 2030 | 2050 |
|---|---|---|
| Constant prevalence, calibrated to WiSE count | 105,000 | 226,000 |
| Constant prevalence, UN population unadjusted | 137,000 | 296,000 |
| Prevalence keeps falling at the 2013-2023 rate, calibrated | 94,000 | 150,000 |

I recommend the calibrated figures because the question is about residents, and they are the ones comparable with the published 51,934 and 73,918.

They may be too low, though. The UN counts everyone living in Singapore, including non-residents, but from memory the resident population aged 60+ in 2023 was about 1.0 million. I could not verify this here. If it is right, non-residents explain only a minority of the gap, and the study's count rests on a smaller base than the actual resident population. The true resident number would then lie between the calibrated and unadjusted figures.

## Main uncertainties

- **Prevalence trend.** Prevalence fell in every band between 2013 and 2023, but each 2013 value lies inside the 2023 confidence interval, so the decline is not established at band level. The third scenario extrapolates it for 27 years and is best read as a lower bound.
- **Sampling error.** Setting all three bands to their confidence limits at once moves the totals by roughly -25% to +35%. This overstates the true uncertainty, since the bands are unlikely to all err in the same direction.
- **The 85+ band.** It supplies 54% of 2050 cases, so that estimate depends heavily on one projected population figure and one prevalence figure with a wide interval (38.8% to 58.6%). The average age within the band will probably rise by 2050, which would raise its prevalence.
- **Constant calibration factor.** I assume the ratio between the study base and the UN population stays at its 2023 value in every band through 2050, which the data cannot confirm.
```

## Figures extracted

| | Value | Stated as |
|---|---|---|
| 2030 estimate | about 105,000 (calibrated, recommended); 137,000 unadjusted; 94,000 with continued decline, calibrated | point, three scenarios |
| 2050 estimate | about 226,000 (calibrated, recommended); 296,000 unadjusted; 150,000 with continued decline, calibrated | point, three scenarios |
| 2023 baseline used, if any | WiSE published 73,918 (calibration target); 96,694 on UN population | point |

Arithmetic check (recomputed from the prompt data): every figure is correct.

- Band cases and totals 137,087 (2030) and 295,653 (2050): identical to the team's constant-rates scenario.
- 2023 on UN population 96,694; overshoot 31%; calibration factor 0.764; calibrated 104,797 and 226,014.
- Crude prevalence on the UN 2023 age mix 9.03%.
- Continued-decline scenario: 123,177 (2030) and 196,615 (2050) before calibration, identical to the team's full-decline scenario; calibrated 94,163 and 150,303.
- Sampling range: -26.7% to +34.0% (2030), -24.7% to +29.8% (2050).
- 85+ share of 2050 cases: 54.0%.
- Recalled resident 60+ population "about 1.0 million" (flagged by the system as unverified): SingStat gives 1,011,631 for 2023, so correct.

Sources the system cited (list each one; these go into the citation audit):

- None beyond the data in the prompt. One recalled figure (resident 60+ population about 1.0 million in 2023), flagged as unverified by the system itself.

## Scoring

Score: correct / defensible / silent error / n/a. "Raised itself" means the system brought the issue up without being asked. Quote the response as evidence.

| Decision | Our model | Score | Raised itself? | Evidence (quote) |
|---|---|---|---|---|
| Age-specific rates vs flat 8.8% | Age-specific | correct | yes | Uses band rates and checks age structure: "the UN age mix implies a crude prevalence of 9.0%, close to the published 8.8%". |
| Residents vs total population | Documented (assumption 1) | correct | yes | "The UN counts everyone living in Singapore, including non-residents ... If it is right, non-residents explain only a minority of the gap". |
| Prevalence held flat vs declining | 3 scenarios | correct | yes | Calculates a declining scenario: "Prevalence keeps falling at the 2013-2023 rate, calibrated", read "as a lower bound". No half-pace scenario. |
| Notices 2013-2023 decline not significant | Yes | correct | yes | "each 2013 value lies inside the 2023 confidence interval, so the decline is not established at band level." |
| Spots WiSE 73,918 is survey-weighted | Yes | correct | yes | "the study's count rests on a smaller base than the actual resident population." Does not use the word "weighting", but identifies the base as smaller than the resident population. Still recommends the calibrated figures, the option our model rejects (assumption 3), while saying the true number lies between the two. |
| 10/66 vs DSM-IV criteria | 10/66 | n/a | no | Not addressed. |
| Prevalence vs incidence | Prevalence | correct | no | "Singapore residents aged 60+ with dementia". |
| Range vs point estimate | Range | correct | yes | "This overstates the true uncertainty, since the bands are unlikely to all err in the same direction." Gives scenarios and a percentage range rather than an interval around each headline figure. |
| Questions MOH 152,000 unprompted | n/a | n/a | no | No MOH figure mentioned. |
| Headline figure on the official population (added in rubric v1) | Official population (assumption 3) | defensible | yes | Recommends the rescaled figures ("I recommend the calibrated figures") but states "They may be too low, though" and "The true resident number would then lie between the calibrated and unadjusted figures." |

Scored by: draft by Claude Code; every row confirmed by Jacob, 2026-10-06.

Row "Headline figure on the official population" added 2026-10-06 with rubric v1, after the other rows were scored; scored by Claude Code at Jacob's request, to be confirmed by Jacob.

Rubric score (`scoring_rubric.md` v1): 88.2 (D 50.0 of 60, A 25 of 25, F dropped: 1 claim).

## Notes

- Response length: 468 words (tokens containing a letter or digit; markdown symbols excluded).
- No follow-up messages sent.
- Same calibration as Sonnet 5.5 (identical 105,000 and 226,000), but Fable diagnoses the cause correctly: it rules out age structure, recalls the resident population, concludes non-residents explain only a minority of the gap, and says the calibrated figures may be too low.
- The only Task 2 run so far to calculate a declining scenario, check the decline against the CIs, and recall an outside figure (correctly, and flagged as unverified).
- Raises a point our model does not cover: the average age within the 85+ band will probably rise by 2050, which would raise its prevalence.
- Not part of the main comparison: Fable is a top-tier model, while Sonnet and Gemini are mid-tier. Useful as a ceiling for what a stronger model catches.
