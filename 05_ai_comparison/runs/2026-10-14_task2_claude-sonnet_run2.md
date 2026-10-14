# Run log: Task 2 build the projection / Claude (Sonnet 5.5) / run 2

Stability repeat of Task 2 run 1 (2026-10-06) with the same prompt (V2 standard) and settings, on a different day, as the protocol requires.

## Run details

| Field | Value |
|---|---|
| Task | 2 build the projection, run 2 (prompt version V2 standard) |
| System | Claude (Anthropic) |
| Model version (exactly as shown in the interface) | Sonnet 5.5 |
| Date and time (SGT) | 2026-10-14, time not recorded |
| Response time | Not recorded |
| Interface | claude.ai web app, incognito chat |
| Account tier | Claude Max |
| Fresh session, no prior messages | yes |
| Memory and personalisation | off (incognito chat) |
| Web search | Off or not used; no search activity or source links shown. |
| Code execution | Not used; no code shown. |
| Extended thinking or reasoning mode | Effort: low |
| Prompt file | `prompts/task2_build_projection.txt` |
| Repo commit of prompt file (`git rev-parse --short HEAD`) | `f1f7dad` (file unchanged since run 1 at `e9d08f2`) |
| Run by | Jacob |

Run details confirmed by Jacob, 2026-10-14.

## Prompt (verbatim)

Contents of `prompts/task2_build_projection.txt` (234 words by `wc -w`; data tables included in the text, no files attached), pasted in full. Same prompt as run 1.

## Response (verbatim, complete)

Copied text pasted by Jacob on 2026-10-14.

```
## Estimates

| | 2030 | 2050 |
|---|---|---|
| **Main estimate** (2023 prevalence held constant, adjusted to residents) | **about 105,000** | **about 226,000** |
| Lower scenario (2013-2023 decline continues) | about 94,000 | about 151,000 |
| Range from the 2023 confidence intervals | about 77,000 to 140,000 | about 170,000 to 293,000 |

My main estimate is roughly 105,000 residents aged 60+ with dementia in 2030 and 226,000 in 2050, about 1.4 times the 2023 count in 2030 and 3.1 times in 2050.

## Method

1. **Apply age-specific prevalence to the projected population.** Dementia prevalence rises steeply with age, so I used the three age bands separately instead of the overall 8.8%. This matters because the 85+ group grows 3.3 times between 2023 and 2050, while the 60-74 group grows only 1.6 times.

2. **Calibrate to residents.** The UN population includes non-residents, while WiSE covers only citizens and permanent residents. Applying the 2023 WiSE prevalences to the UN 2023 populations gives 96,693 cases, but the study reports 73,918. I scaled by the ratio, 73,918 / 96,693 = 0.765, and applied it to all projections. This implies about 840,000 residents aged 60+ in 2023, against 1.07 million in the UN figures.

3. **Main estimate.** Prevalence is held at the 2023 values (3.0%, 18.2%, 48.6%).
   - 2030 unadjusted: 27,000 + 61,378 + 48,708 = 137,087. Adjusted: about 104,800.
   - 2050 unadjusted: 37,322 + 98,539 + 159,793 = 295,655. Adjusted: about 226,000.

4. **Lower scenario.** Between 2013 and 2023, prevalence fell in every band (60-74: 3.4% to 3.0%; 75-84: 21.6% to 18.2%; 85+: 56.2% to 48.6%). I continued each band's relative decline at the same annual rate, which gives about 2.75%, 16.2% and 43.9% in 2030, and 2.1%, 11.5% and 32.9% in 2050. After the same resident adjustment, this gives about 94,000 and 151,000 cases.

5. **Uncertainty range.** I applied the lower and upper bounds of the 2023 confidence intervals to all bands at once, which gives a wide but defensible range.

## Caveats

- **Resident adjustment.** A single scaling factor assumes the resident share of each age band stays constant. Residents are probably a higher share of the oldest group, so the factor may understate the 85+ population, and therefore cases, particularly in 2050. Official resident projections would be better if available.
- **Prevalence trend.** A fall in prevalence over only two surveys is uncertain. The confidence intervals for 2013 and 2023 likely overlap in places, so the lower scenario is illustrative, not a forecast. Higher rates of diabetes, hypertension and obesity could reverse the decline, while rising education and better vascular care could extend it.
- **UN projections.** The medium variant depends on assumptions about fertility, mortality and migration, particularly for 2050.
- **Case definition.** The 10/66 criteria differ from other diagnostic standards, so counts are not directly comparable with studies that use different definitions.
- **Excluded groups.** WiSE covers community-dwelling residents, so people in institutions may be under-represented.

I would report about 105,000 (range 77,000 to 140,000) for 2030 and about 226,000 (range 151,000 to 293,000) for 2050. The lower end of the 2050 range comes from the declining-prevalence scenario and the upper end from the confidence interval.
```

## Figures extracted

| | Value | Stated as |
|---|---|---|
| 2030 estimate | about 105,000 (scaled by 0.765); 137,087 unscaled; about 94,000 if the decline continues; range 77,000 to 140,000 | point with scenario and range |
| 2050 estimate | about 226,000 (scaled); 295,655 unscaled; about 151,000 if the decline continues; CI range 170,000 to 293,000; reported range 151,000 to 293,000 | point with scenario and range |
| 2023 baseline used, if any | WiSE published 73,918 (calibration target); 96,693 on the UN population | point |

Arithmetic check (recomputed from the prompt data with the response's own stated method; script run 2026-10-14). Scale factor 73,918 / 96,693.72 = 0.76446.

- 2023 on the UN population: exact 96,693.72; band cells rounded to whole people (23,691 + 37,972 + 35,030) sum to 96,693. Response: 96,693. Counted correct: the cells are not displayed, but whole-person cells are the response's evident method (its 2030 and 2050 lines add whole-person cells). Ruling confirmed by Jacob, 2026-10-14.
- "73,918 / 96,693 = 0.765": exact 0.76446, which rounds to 0.764 at three decimals; no "about". Counted correct by Jacob's ruling, 2026-10-14 (strictly it misses the half-unit test by 0.00004; compare the "10.3% for 10.2496%" convention, under which it would be incorrect).
- "This implies about 840,000 residents aged 60+ in 2023": 73,918 / 8.8% = 839,977 (the derivation run 1 showed). Scaling the UN 1,070,429 by 0.76446 would give 818,295. Counted correct by Jacob's ruling, 2026-10-14. "1.07 million in the UN figures": 1,070,429, correct.
- 2030 cells: 27,000.42; 61,378.04; 48,708.38; total 137,086.84. Response: 27,000; 61,378; 48,708; 137,087. All correct. "Adjusted: about 104,800": 104,797. Correct. Headline "about 105,000": correct.
- 2050 cells: 37,322.43; 98,537.89; 159,792.91; total 295,653.24. Response: 37,322 (correct); 98,539 (incorrect: 1.1 above); 159,793 (correct); 295,655 (incorrect: exact 295,653.24, and its displayed cells sum to 295,654, so the sum-of-cells convention does not rescue it). "Adjusted: about 226,000": 226,014. Correct.
- Growth: 137,086.84 / 96,693.72 = 1.418, "about 1.4 times", correct; 295,653.24 / 96,693.72 = 3.058, "3.1 times", correct.
- "the 85+ group grows 3.3 times between 2023 and 2050": 328,792 / 72,078 = 4.56. Incorrect. (3.3 is the 2030-2050 ratio, 328,792 / 100,223 = 3.28.) "the 60-74 group grows only 1.6 times": 1,244,081 / 789,711 = 1.575. Correct.
- Declining-rate scenario (each band's 2013-2023 annual rate continued): 2030 rates 2.748%, 16.144%, 43.900%; 2050 rates 2.140%, 11.461%, 32.830%. Response, under "about": 2.75%, 16.2%, 43.9%, 2.1%, 11.5%, 32.9%. All within 2% (16.2 is 0.3% above 16.144; 32.9 is 0.2% above 32.83). All correct. Scaled cases: 94,163 (2030) and 150,303 (2050). "about 94,000" and "about 151,000": correct.
- CI range (all bands at their bounds, scaled): 2030 76,830 to 140,396; 2050 170,226 to 293,391. "about 77,000 to 140,000" and "about 170,000 to 293,000": correct. Identical to run 1.

Count under rubric v1.1: 31 numbers, 28 correct.

- Correct (28): about 105,000; about 226,000; about 94,000; about 151,000; 77,000; 140,000; 170,000; 293,000; 1.4 times; 3.1 times; 1.6 times (60-74); 96,693; 0.765; 840,000; 1.07 million; 27,000; 61,378; 48,708; 137,087; about 104,800; 37,322; 159,793; 2.75%; 16.2%; 43.9%; 2.1%; 11.5%; 32.9%.
- Incorrect (3): 3.3 times (85+ growth 2023-2050 is 4.56); 98,539 (98,538); 295,655 (295,653).

A = 25 x 28 / 31 = 22.6.

Sources the system cited (list each one; these go into the citation audit):

- None beyond the data in the prompt.

Recalled claims from outside the prompt: "WiSE covers community-dwelling residents" (named study; not checked). "Residents are probably a higher share of the oldest group" (no number or source). Risk-factor statements carry no number or source. F tally: at most 1 checkable claim, component dropped.

## Scoring

Score: correct / defensible / silent error / n/a. "Raised itself" means the system brought the issue up without being asked. Quote the response as evidence.

| Decision | Our model | Score | Raised itself? | Evidence (quote) |
|---|---|---|---|---|
| Age-specific rates vs flat 8.8% | Age-specific | correct | yes | "I used the three age bands separately instead of the overall 8.8%." |
| Residents vs total population | Documented (assumption 1) | defensible | yes | "The UN population includes non-residents, while WiSE covers only citizens and permanent residents." Attributes the whole 0.765 ratio to this, far more than coverage explains (UN is about 5.8% above SingStat residents at 60+ in 2023). Same as run 1. |
| Prevalence held flat vs declining | 3 scenarios | correct | yes | Two calculated scenarios: constant ("Main estimate") and "Lower scenario (2013-2023 decline continues)", for both years. Run 1 had one. |
| Notices 2013-2023 decline not significant | Yes | defensible | yes | "A fall in prevalence over only two surveys is uncertain. The confidence intervals for 2013 and 2023 likely overlap in places, so the lower scenario is illustrative, not a forecast." Raises it without checking the 2013 values against the 2023 CIs, and the method states "prevalence fell in every band". Confirmed by Jacob, 2026-10-14. Same as run 1. |
| Spots WiSE 73,918 is survey-weighted | Yes | defensible | yes | "gives 96,693 cases, but the study reports 73,918"; derives "about 840,000 residents aged 60+". Cause given is non-residents, not that the survey's base is smaller than the actual resident 60+ population. Rescales to 73,918 (modelling choice, noted, not scored here). Same as run 1. |
| 10/66 vs DSM-IV criteria | 10/66 | correct | yes | "The 10/66 criteria differ from other diagnostic standards, so counts are not directly comparable with studies that use different definitions." Run 1 did not address it. |
| Prevalence vs incidence | Prevalence | correct | no | "105,000 residents aged 60+ with dementia in 2030". |
| Range vs point estimate | Range | correct | yes | Ranges and scenarios for both years. The CI range puts all bands at their limits together ("applied the lower and upper bounds ... to all bands at once"), not flagged as wider than a joint interval, but a valid declining scenario is also given for every year, so correct under the 2026-10-14 row 8 convention. |
| Questions MOH 152,000 unprompted | n/a | n/a (penalty-only, not triggered) | no | No MOH figure mentioned. |
| Headline figure on the official population | Official population (assumption 3) | defensible | no | Headline rescaled to 73,918 ("about 105,000", "about 226,000"), but flags it as possibly too low: "Residents are probably a higher share of the oldest group, so the factor may understate the 85+ population, and therefore cases, particularly in 2050." Wrong cause (the real reason is WiSE's smaller survey base), right direction. Defensible, confirmed by Jacob, 2026-10-14. Run 1 was a silent error. |

Scored by: draft by Claude Code; every row and ruling confirmed by Jacob, 2026-10-14.

Rubric score (`scoring_rubric.md` v1.1): 81.5 (D 46.7 of 60, A 22.6 of 25: 28 of 31, F dropped: at most 1 checkable claim).

D working: units 1 (row 1) + 0.5 (row 2) + 1 (row 3) + 0.5 (row 4) + 0.5 (row 5) + 1 (row 6) + 1 (row 7) + 1 (row 8) + 0.5 (row 10) = 7.0; correct core rows 5 (rows 1, 3, 6, 7, 8); D = 60 x max(7.0, 5) / 9 = 46.7. Run score = 100 x (46.7 + 22.6) / 85 = 81.5.

Why this score: Same headline as run 1 (about 105,000 and 226,000, rescaled to 73,918 and blamed on non-residents), but a more complete answer around it: a calculated declining-rate scenario for both years (row 3 up to correct), diagnostic criteria raised unprompted (row 6 up to correct), and a caveat that the rescaled figure may understate cases (row 10 up from silent error to defensible). Rows 2, 4 and 5 unchanged at half credit. Three arithmetic slips: the 85+ growth factor (3.3 times instead of 4.56), one 2050 band cell and the 2050 total.

## Stability (run 1 vs run 2)

| | Run 1 (2026-10-06) | Run 2 (2026-10-14) |
|---|---|---|
| Score | 62.0 | 81.5 |
| D / A | 30.0 / 22.7 | 46.7 / 22.6 |
| Headline 2030 / 2050 | about 105,000 / 226,000 | about 105,000 / 226,000 |
| Ranges | 77,000 to 140,000; 170,000 to 293,000 | same CI ranges; 2050 reported as 151,000 to 293,000 |
| Rows that changed | | 3 (0.5 to 1), 6 (0 to 1), 10 (-0.5 to 0.5) |

Headline numbers and the core method were identical; the score moved by 19.5 points on caveats and an extra scenario. Run-to-run variation in what a model chooses to mention is large relative to the gaps between systems.

## Notes

- Response length: 532 words by `wc -w` on the copied text (run 1: 369 by the older letter-or-digit convention).
- No follow-up messages sent.
- "WiSE covers community-dwelling residents" is unchecked; if WiSE 2023 sampled institutions too, it is wrong. F is dropped either way.
- The 0.765 and 840,000 rulings are more lenient than the strict half-unit test; noted so the second scorer can see them.
