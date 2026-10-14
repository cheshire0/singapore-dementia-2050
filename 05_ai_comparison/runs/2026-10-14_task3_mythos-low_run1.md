# Run log: Task 3 reverse-engineer MOH 152,000 / Mythos 5.1 (low effort) / run 1

Extra top-tier run, not part of the main Sonnet vs Gemini pairing.

## Run details

| Field | Value |
|---|---|
| Task | 3 reverse-engineer the published 152,000 for 2030 |
| System | Claude (Anthropic) |
| Model version (exactly as shown in the interface) | Mythos 5.1 |
| Date and time (SGT) | 2026-10-14, time not recorded |
| Response time | Not recorded |
| Interface | claude.ai web app, incognito chat |
| Account tier | Claude Max |
| Fresh session, no prior messages | yes |
| Memory and personalisation | off (incognito chat) |
| Web search | Off or not used; no search activity or source links shown. |
| Code execution | Not used; no code shown. |
| Extended thinking or reasoning mode | Effort: Low |
| Prompt file | `prompts/task3_reverse_engineer_moh.txt` |
| Repo commit of prompt file (`git rev-parse --short HEAD`) | Not committed at time of logging (HEAD `2373361`); committed together with this log. |
| Run by | Jacob |

Run details assumed to be the standard Mythos low settings used for the other Mythos low runs; not separately confirmed for this run.

## Prompt (verbatim)

Contents of `prompts/task3_reverse_engineer_moh.txt` (286 words by `wc -w`; data tables included in the text, no files attached), pasted in full.

## Response (verbatim, complete)

Copied text pasted by Jacob on 2026-10-14.

```
**Short answer:** no single clean method in the data reproduces 152,000 exactly. The closest is applying the **2013** age-specific prevalence rates to the UN medium-variant 2030 population aged 60+, which gives about 160,000. Applying the **2023** rates gives about 137,000. The 152,000 sits between the two, and getting there also requires mixing two different population denominators. Details below.

## Step 1: Check the denominators

The 2023 WiSE figure of 73,918 at 8.8% implies a base population of 73,918 / 0.088 ≈ **840,000** residents aged 60+. The UN 2023 total for 60+ is 789,711 + 208,640 + 72,078 = **1,070,429**. The UN counts total population (including non-residents); WiSE counts citizens and PRs only. The resident base is about 78% of the UN base.

If you apply the 2023 WiSE rates to the UN 2023 population, you get 23,700 + 38,000 + 35,000 ≈ **96,700**, not 73,918. So any projection that starts from 73,918 and ends on a UN-based 2030 number has switched denominators mid-stream, which inflates the apparent growth by roughly 30%.

## Step 2: Project 2030 on the UN population

| Rates used | 60-74 | 75-84 | 85+ | Total 2030 |
|---|---|---|---|---|
| 2023 rates (3.0 / 18.2 / 48.6%) | 27,000 | 61,400 | 48,700 | **137,100** |
| 2013 rates (3.4 / 21.6 / 56.2%) | 30,600 | 72,800 | 56,300 | **159,800** |
| 2023 upper CI (4.7 / 24.5 / 58.6%) | 42,300 | 82,600 | 58,700 | 183,700 |

A crude overall-rate check: 152,000 / 1,337,479 (UN 60+ in 2030) = 11.4%. That is above both surveys' overall rates (10.0%, 8.8%), but ageing within the 60+ group raises the overall rate under fixed age-specific rates: the 2013 rates imply 11.9% in 2030 and the 2023 rates imply 10.3%.

## Step 3: What set of assumptions gets to 152,000

The combination that lands nearest is:

1. 2030 base = UN medium variant, **total** population (not residents only).
2. Age-specific prevalence held at or near the **2013** WiSE levels (160,000), or 2023 rates for 60-74 with 2013 rates for the two older bands (156,000). Either way, the assumption is that the 2013-to-2023 decline in age-specific prevalence does not continue, and in effect is partly reversed.
3. The 2023 starting point quoted (73,918) comes from a residents-only survey, so the 2023-to-2030 growth of 2.06x is overstated. On a consistent basis, growth is about 1.42x under either rate set (73,918 → roughly 105,000 residents in 2030).

My best guess is that the 152,000 figure is older than the 2023 WiSE result: it matches the kind of projection made from the 2013 survey (10% prevalence, 2013 age rates) onto a total-population forecast, and was later paired with the 2023 number. I cannot verify that without searching.

## Consistent estimates for your own use

Holding 2023 age-specific rates fixed:

- **2030:** 137,000 on the UN total-population base; about 107,000 on a residents-only base (×0.785).
- **2050:** 37,300 + 98,500 + 159,800 ≈ **296,000** on the UN base; about 232,000 residents-only.

The 2050 figure is dominated by the 85+ band (328,792 people at 48.6%), so it is sensitive to both the 85+ prevalence estimate (CI 38.8 to 58.6%) and to whether the prevalence decline seen from 2013 to 2023 continues. A range of roughly 240,000 to 350,000 on the UN base covers the CI alone.
```

## Figures extracted

| | Value | Stated as |
|---|---|---|
| Assumptions it says come nearest to 152,000 | UN total population with 2013 rates (about 160,000) or 2023 rates for 60-74 and 2013 rates above 75 (156,000), quoted against a residents-only 2023 base; best guess that 152,000 predates WiSE 2023 | alternatives with a best guess, flagged as unverified |
| 2030, constant 2023 rates | 137,000 (UN base); about 107,000 residents-only (x0.785); also "roughly 105,000" from 73,918 x 1.42 | two bases |
| 2050, constant 2023 rates | about 296,000 (UN base); about 232,000 residents-only; "roughly 240,000 to 350,000" for the CI | point with range |

Arithmetic check (recomputed from the prompt data; script run 2026-10-14):

- 73,918 / 0.088 = 839,977, "≈ 840,000" correct; 1,070,429 correct; 839,977 / 1,070,429 = 78.5%, "about 78%" correct.
- 2023 cells 23,691; 37,972; 35,030; total 96,694: "23,700 + 38,000 + 35,000 ≈ 96,700" correct.
- "inflates the apparent growth by roughly 30%": starting from 73,918 and ending on a UN-based figure inflates growth by 96,694 / 73,918 = 1.308, i.e. 30.8%; 30 is 2.6% below 30.8, outside the 2% tolerance. Incorrect.
- 2030 table: 2023 rates 27,000; 61,378; 48,708; 137,087; 2013 rates 30,600; 72,844; 56,325; 159,770; upper CI 42,301; 82,624; 58,731; 183,656. All twelve cells correct to the hundreds shown.
- 152,000 / 1,337,479 = 11.36%, "11.4%" correct. 2013 rates in 2030: 159,770 / 1,337,479 = 11.95%, "11.9%" correct. 2023 rates in 2030: 137,087 / 1,337,479 = 10.2496%, "10.3%" incorrect (rounds to 10.2%; same case as the "10.3% for 10.2496%" convention).
- Mixed rates: 27,000 + 72,844 + 56,325 = 156,170, "156,000" correct. "about 160,000" correct.
- "growth of 2.06x" (152,000 / 73,918 = 2.056) correct. "about 1.42x under either rate set": 2023 rates 137,087 / 96,694 = 1.418; 2013 rates 159,770 / 112,424 = 1.421. Correct. "73,918 → roughly 105,000" (104,796) correct.
- Residents-only: 0.785 (839,977 / 1,070,429 = 0.7847) correct; 137,087 x 0.785 = 107,613, "about 107,000" correct; 295,653 x 0.785 = 232,088, "about 232,000" correct. (This factor differs from the 0.764 ratio implied by 73,918 / 96,694, which is why its two 2030 resident figures, 105,000 and 107,000, differ; each is correct by its own method.)
- 2050 cells 37,322; 98,538; 159,793: "37,300 + 98,500 + 159,800 ≈ 296,000" correct. "dominated by the 85+ band" (54%) correct.
- "A range of roughly 240,000 to 350,000 on the UN base covers the CI alone": 85+ CI only gives 263,432 to 328,532; all bands at their limits give 222,676 to 383,791. Neither endpoint matches either reading. Both incorrect.

Count under rubric v1.1: 39 numbers or derived statements, 35 correct.

- Incorrect (4): "roughly 30%" (30.8%); 10.3% (10.2496%); 240,000 and 350,000 (CI range).

A = 25 x 35 / 39 = 22.4.

Sources the system cited (list each one; these go into the citation audit):

- None beyond the data in the prompt.

Recalled claims from outside the prompt: none with a number, date or named source. Its guess that 152,000 is "older than the 2023 WiSE result" is an inference, flagged as unverified ("I cannot verify that without searching"), not a recalled claim. F tally: 0 checkable claims, component dropped.

## Scoring

Score: correct / defensible / silent error / n/a. "Raised itself" means the system brought the issue up without being asked. The Task 3 prompt asks only what assumptions reproduce 152,000. Quote the response as evidence. Rubric v1.2: row 10 not scored in Task 3; row 8 read as a range of assumption sets.

| Decision | Our model | Score | Raised itself? | Evidence (quote) |
|---|---|---|---|---|
| Age-specific rates vs flat 8.8% | Age-specific | correct | yes | Band-by-band table for three rate sets; notes that "ageing within the 60+ group raises the overall rate under fixed age-specific rates". |
| Residents vs total population | Documented (assumption 1) | defensible | yes | "The UN counts total population (including non-residents); WiSE counts citizens and PRs only. The resident base is about 78% of the UN base." Attributes the whole gap to coverage (UN is about 5.8% above SingStat residents at 60+ in 2023). |
| Prevalence held flat vs declining | 3 scenarios | correct | yes | 2023 rates, 2013 rates, upper CI and a mixed set, for 2030. |
| Notices 2013-2023 decline not significant | Yes | silent error | yes | "the assumption is that the 2013-to-2023 decline in age-specific prevalence does not continue, and in effect is partly reversed"; "whether the prevalence decline seen from 2013 to 2023 continues". Treated as established; the 2013 values are never compared with the 2023 CIs. |
| Spots WiSE 73,918 is survey-weighted | Yes | defensible | yes | Notices the mismatch ("≈ 96,700, not 73,918") and the 840,000 base, and sees that a projection mixing the two "has switched denominators mid-stream", but calls 840,000 "residents aged 60+" and puts the gap on coverage. |
| 10/66 vs DSM-IV criteria | 10/66 | omitted (0) | no | Not addressed. |
| Prevalence vs incidence | Prevalence | correct | no | Counts of people with dementia throughout. |
| Range vs point estimate | Range | correct | yes | Two assumption sets that come near 152,000 (2013 rates, 160,000; mixed rates, 156,000), plus the denominator switch, with a best guess and its limit stated: "My best guess is that the 152,000 figure is older than the 2023 WiSE result ... I cannot verify that without searching." |
| Questions MOH 152,000 unprompted | n/a | correct | yes | "no single clean method in the data reproduces 152,000 exactly"; "the 2023-to-2030 growth of 2.06x is overstated. On a consistent basis, growth is about 1.42x"; reaching it means the decline "in effect is partly reversed". |
| Headline figure on the official population | Official population (assumption 3) | not scored (v1.2) | | |

Scored by: draft by Claude Code under Jacob's standing instruction to apply its recommendations (2026-10-14); open to Jacob's review.

Rubric score (`scoring_rubric.md` v1.2): 69.5 (D 36.7 of 60, A 22.4 of 25: 35 of 39, F dropped: no recalled claims).

D working: units 1 (row 1) + 0.5 (row 2) + 1 (row 3) - 0.5 (row 4) + 0.5 (row 5) + 0 (row 6) + 1 (row 7) + 1 (row 8) + 1 (row 9) = 5.5; 9 core rows; correct core rows 5 (rows 1, 3, 7, 8, 9); D = 60 x max(5.5, 5) / 9 = 36.7. Run score = 100 x (36.7 + 22.4) / 85 = 69.5.

Why this score: Reaches the team's conclusion: 152,000 needs rates at or near 2013 levels (the decline reversed) on the total population, and the 2.06x growth from 73,918 is inflated by mixing a residents-only base with a total-population projection (1.42x on a consistent basis). Its unverified guess that 152,000 predates WiSE 2023 agrees with the dated sources found in the Gemini Task 3 source check (earliest confirmed appearance September 2021). Same deductions as the other Task 3 runs: decline treated as fact, gap put on coverage, criteria not raised. Four arithmetic slips, all in side figures (the 30% inflation, 10.3%, and the 2050 CI range).

## Notes

- Response length: 555 words by `wc -w` on the copied text.
- No follow-up messages sent.
- Same D score as both main systems (36.7). As noted in the results caveats, the rubric does not separate a correct reading of what 152,000 requires (Sonnet, Mythos low) from a reversed one (Gemini).
- It uses two different resident factors (0.785 from population, implicitly 0.764 from 73,918 / 96,694) without reconciling them, giving 105,000 and 107,000 for 2030 residents.
