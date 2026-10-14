# AI comparison: results so far

Last updated 2026-10-14. Scores use `scoring_rubric.md` version 1.1. Full evidence (quotes, recomputed numbers, source checks) is in each run log in `runs/`.

Main comparison: Claude Sonnet 5.5 vs Gemini 3.8 Flash (each company's mid-tier model, low reasoning effort). Extra top-tier runs (Mythos 5.1, low and max effort) will show what a stronger model catches; they are not part of the main comparison. Earlier extra runs on Claude Fable 5.1 were withdrawn on 2026-10-14 and are not reported here.

## Status

| Item | Status |
|---|---|
| Task 1 cold recall | Done, both runs scored |
| Task 2 build projection, run 1 | Done, both runs scored (row 10 confirmed by Jacob, 2026-10-14) |
| Task 2 run 2 (stability) | Done: Sonnet 5.5 (confirmed by Jacob) and Gemini 3.8 Flash (scored on Claude Code's recommendations, Jacob's standing instruction), 2026-10-14 |
| Task 2 prompt versions V1 and V3, main systems | Sonnet 5.5 V1 and V3 done and confirmed by Jacob, 2026-10-14; Gemini V1 and V3 done (scored on Claude Code's recommendations, Jacob's standing instruction) |
| Mythos 5.1 extra runs (low, max), Tasks 1 and 2 | Done: Task 1, and Task 2 with prompts V1, V2 and V3, one run each; all scores confirmed by Jacob, 2026-10-14 |
| Task 3 reverse-engineer MOH | Done for both main systems, 2026-10-14 (rubric v1.2; scored on Claude Code's recommendations under Jacob's standing instruction) |
| Citation audit | Not run |
| Second-scorer reliability check | Not done |

## Scores

| Run | Task 1 | Task 2 run 1 | Task 2 run 2 |
|---|---|---|---|
| Gemini 3.8 Flash | 25.0 | 56.9 | 56.9 |
| Claude Sonnet 5.5 | 51.3 | 62.0 | 81.5 |
| Mythos 5.1 low (extra) | 81.3 | 61.7 |
| Mythos 5.1 max (extra) | 85.0 | 99.4 |
| Gemini 3.8 Flash, Task 2 V1 minimal prompt | | 43.5 (V1 prompt) | |
| Claude Sonnet 5.5, Task 2 V1 minimal prompt | | 46.9 (V1 prompt) |
| Mythos 5.1 low (extra), Task 2 V1 minimal prompt | | 46.3 (V1 prompt) |
| Mythos 5.1 max (extra), Task 2 V1 minimal prompt | | 92.2 (V1 prompt) |
| Gemini 3.8 Flash, Task 2 V3 guided prompt | | 76.5 (V3 prompt) | |
| Claude Sonnet 5.5, Task 2 V3 guided prompt | | 79.8 (V3 prompt) | |
| Mythos 5.1 low (extra), Task 2 V3 guided prompt | | 99.3 (V3 prompt) |
| Mythos 5.1 max (extra), Task 2 V3 guided prompt | | 94.3 (V3 prompt) |

The four "Task 2 V1" rows used prompt version V1 (question and data only, no request to explain the method) and the four "Task 2 V3" rows used prompt version V3 (guided checklist, which asks directly about rows 3, 4, 5, 8 and 10); every other Task 2 cell uses V2. Not directly comparable with V2 runs.

Component breakdown (D decisions, A arithmetic, F recalled facts; "dropped" means fewer than three checkable claims):

| Run | Task 1 D / 50 | Task 1 F / 50 | Task 2 D / 60 | Task 2 A / 25 | Task 2 F / 15 |
|---|---|---|---|---|---|
| Gemini 3.8 Flash | 12.5 | dropped (0 of 1) | 23.3 | 25.0 | dropped (0 claims) |
| Gemini 3.8 Flash, Task 2 run 2 | | | 23.3 | 25.0 (36 of 36) | dropped (0 claims) |
| Claude Sonnet 5.5 | 31.3 | 20.0 (2 of 5) | 30.0 | 22.7 (20 of 22) | dropped (0 claims) |
| Claude Sonnet 5.5, Task 2 run 2 | | | 46.7 | 22.6 (28 of 31) | dropped (at most 1 claim) |
| Mythos 5.1 low (extra) | 37.5 | 43.8 (7 of 8) | 30.0 | 22.4 (26 of 29) | dropped (1 of 1) |
| Mythos 5.1 max (extra) | 50.0 | 35.0 (7 of 10) | 60.0 | 24.4 (44 of 45) | 15.0 (5 of 5) |
| Gemini 3.8 Flash, Task 2 V1 minimal prompt | | | 13.3 | 23.6 (17 of 18) | dropped (0 claims) |
| Claude Sonnet 5.5, Task 2 V1 minimal prompt | | | 16.7 | 23.2 (13 of 14) | dropped (0 claims) |
| Mythos 5.1 low (extra), Task 2 V1 minimal prompt | | | 20.0 | 19.3 (17 of 22) | dropped (0 claims) |
| Mythos 5.1 max (extra), Task 2 V1 minimal prompt | | | 53.3 | 25.0 (31 of 31) | dropped (1 of 1) |
| Gemini 3.8 Flash, Task 2 V3 guided prompt | | | 40.0 | 25.0 (47 of 47) | dropped (0 claims) |
| Claude Sonnet 5.5, Task 2 V3 guided prompt | | | 43.3 | 24.5 (50 of 51) | dropped (0 claims) |
| Mythos 5.1 low (extra), Task 2 V3 guided prompt | | | 60.0 | 24.3 (65 of 67) | 15.0 (5 of 5) |
| Mythos 5.1 max (extra), Task 2 V3 guided prompt | | | 60.0 | 24.8 (101 of 102) | 9.5 (7 of 11) |

Task 3 (reverse-engineer the published 152,000 for 2030; rubric v1.2, 9 core rows):

| Run | Score | D / 60 | A / 25 | F / 15 |
|---|---|---|---|---|
| Gemini 3.8 Flash | 59.8 | 36.7 | 23.1 (37 of 40) | 0.0 (0 of 4) |
| Claude Sonnet 5.5 | 71.3 | 36.7 | 23.9 (44 of 46) | dropped (0 claims) |
| Mythos 5.1 low (extra) | 69.5 | 36.7 | 22.4 (35 of 39) | dropped (0 claims) |
| Mythos 5.1 max (extra) | 92.1 | 53.3 | 23.8 (57 of 60) | 15.0 (4 of 4) |

## Headline figures

| Run | Task 1, 2050 | Task 2, 2030 | Task 2, 2050 |
|---|---|---|---|
| Gemini 3.8 Flash | 152,000 (MOH's 2030 figure, wrong year) | 137,087 | 295,653 |
| Mythos 5.1 low (extra) | 150,000 to 220,000 (central 180,000) | about 105,000 (rescaled to WiSE; 137,087 unscaled; range roughly 95,000 to 115,000; roughly 94,000 if the decline continues) | about 225,000 (rescaled; 295,653 unscaled; range roughly 150,000 to 260,000; roughly 150,000 if the decline continues) |
| Mythos 5.1 max (extra) | 150,000 to 200,000 (own calculation about 170,000) | about 137,000 (137,087; approx. 95% interval 112,000 to 162,000; about 124,000 if the decline continues; 105,000 rescaled, not recommended) | about 296,000 (295,653; interval 248,000 to 344,000; about 199,000 if the decline continues; 226,000 rescaled, not recommended) |
| Mythos 5.1 low (extra), Task 2 V1 minimal prompt | | roughly 105,000 (rescaled to WiSE; 137,100 unscaled) | roughly 225,000 (rescaled; 295,700 unscaled; range roughly 180,000 to 270,000) |
| Mythos 5.1 max (extra), Task 2 V1 minimal prompt | | about 137,000 (137,086; range roughly 100,000 to 184,000; about 123,000 if the decline continues) | about 296,000 (295,653; range roughly 223,000 to 384,000; about 197,000 if the decline continues) |
| Mythos 5.1 low (extra), Task 2 V3 guided prompt | | about 135,000 (137,087; likely 120,000 to 140,000; plausible 100,000 to 185,000; about 123,000 if the decline continues; 94,000 to 105,000 rescaled, not recommended) | about 290,000 (295,653; likely 265,000 to 300,000; plausible 200,000 to 385,000; about 197,000 if the decline continues to 2050, 266,000 if it stops in 2030; 200,000 to 226,000 rescaled, not recommended) |
| Mythos 5.1 max (extra), Task 2 V3 guided prompt | | about 137,000 (137,087; plausible 110,000 to 165,000; approx. 95% interval 112,000 to 162,000; 123,000 if the decline continues; 160,000 at 2013 rates; about 105,000 anchored to WiSE, not recommended) | about 296,000 (295,653; plausible 200,000 to 350,000; interval 248,000 to 344,000; 197,000 if the decline continues; 344,000 at 2013 rates; about 226,000 anchored, not recommended) |
| Gemini 3.8 Flash, Task 2 run 2 | | 137,086 (100,503 to 183,656) | 295,653 (222,676 to 383,791) |
| Gemini 3.8 Flash, Task 2 V1 minimal prompt | | 137,087 (no range) | 295,653 (no range) |
| Claude Sonnet 5.5 | 150,000 to 200,000 | about 105,000 (rescaled to WiSE) | about 226,000 (rescaled) |
| Claude Sonnet 5.5, Task 2 run 2 | | about 105,000 (rescaled to WiSE; 137,087 unscaled; about 94,000 if the decline continues; range 77,000 to 140,000) | about 226,000 (rescaled; 295,655 unscaled; about 151,000 if the decline continues; range 151,000 to 293,000) |
| Gemini 3.8 Flash, Task 2 V3 guided prompt | | 137,000 (137,087; 101,000 to 184,000; 104,800 rescaled, note only) | 296,000 (295,653; 223,000 to 384,000; 226,000 rescaled, note only) |
| Claude Sonnet 5.5, Task 2 V3 guided prompt | | about 105,000 (calibrated; 137,087 uncalibrated; scenarios 94,200 to 122,100; CI outer bound 76,800 to 140,400) | about 226,000 (calibrated; 295,653 uncalibrated; scenarios 150,400 to 263,000; CI outer bound 170,200 to 293,400) |
| Claude Sonnet 5.5, Task 2 V1 minimal prompt | | about 105,000 (rescaled to WiSE; 137,087 unscaled) | about 226,000 (rescaled; 295,653 unscaled; no numeric range) |
| Team model (three scenarios) | | 123,177 to 137,087 | 196,615 to 295,653 |
| MOH | | 152,000 | none published |

## Findings

1. Sonnet scored above Gemini on both tasks, by 26.3 points on Task 1 and 5.1 on Task 2. The Task 2 gap is small, and Gemini's headline is closer to the team's model.
2. Arithmetic does not separate the systems. Both reproduced the team's constant-rates figures (137,087 and 295,653) exactly; the only arithmetic errors were two in Sonnet's commentary. What separates them is judgement: whether they check the method against the published 2023 count, whether they treat the 2013-2023 decline as established, and which figures they recommend.
3. Gemini Task 2 was accurate but uncritical: perfect arithmetic and the right headline, but it never checked its 2023 figure against WiSE's published 73,918 and treated the decline as real although the confidence intervals it was given include the 2013 values.
4. Sonnet Task 2 was more critical but reached a worse answer: it noticed the mismatch with 73,918, put it down to the wrong cause (non-residents), and rescaled its headline down by 24% to match, without saying the result is probably too low.
5. In cold recall (Task 1) both mid-tier models stated wrong figures with little hedging: Gemini attached MOH's 2030 figure to 2050; Sonnet attributed 80,000 by 2030 to MOH and appears not to know about WiSE 2023. Recall accuracy: Gemini 0 of 1 checkable claims, Sonnet 2 of 5; Mythos 5.1 low (extra) 7 of 8, and it questioned MOH's 152,000 unprompted; Mythos 5.1 max (extra) 7 of 10, attributing 187,000 for 2050 to ADI's 2014 report (which gives 241,000) and reporting 152,000 without questioning it.
6. Diagnostic criteria (10/66 vs others) were addressed by only three runs so far, all unprompted: Mythos 5.1 max on Task 2 V2, Mythos 5.1 low on Task 2 V3 and Mythos 5.1 max on Task 2 V3, even though the Task 2 prompt names them.
7. Sonnet 5.5 gave the same headline under V1 (minimal prompt) as under V2: about 105,000 and 226,000, rescaled to 73,918 and blamed on the resident share. Under V1 it dropped the numeric ranges and the "sampling artefact" qualification, so its score fell from 62.0 to 46.9. Prompt and day both differ, so this cannot yet be separated from run-to-run noise.
8. Stability: Sonnet 5.5's Task 2 run 2 (same V2 prompt, 2026-10-14) gave the identical headline and method as run 1, but scored 81.5 against 62.0. The gain came from what it chose to mention: a calculated declining-rate scenario, diagnostic criteria, and a caveat that the rescaled figure may understate cases. A 19.5-point swing on one system with one prompt is larger than the Sonnet vs Gemini gap on run 1 (5.1), so single-run differences between systems should not be reported as real. This also bears on finding 7: the V1 vs V2 difference (46.9 vs 62.0 and 81.5) sits inside the run-to-run range.
9. Prompt versions on Sonnet 5.5: V1 46.9, V2 62.0 and 81.5, V3 79.8. Every Sonnet run, under every prompt, gave the same headline (about 105,000 and 226,000, rescaled to 73,918 and blamed on non-residents). The guided prompt raised the rows it asked about directly (scenarios, the significance check, ranges) but not the judgement that separates Sonnet from the team's model: even when asked to explain the 2023 difference and justify its headline, it kept the rescaled figures. On Mythos 5.1 low, V3 did change the headline. Prompting fixed coverage, not judgement, for Sonnet.
10. Gemini 3.8 Flash under V1 (minimal prompt) did the calculation and nothing else: exact constant-rates figures (137,087 and 295,653), no coverage comment, no check against 73,918, no ranges, no mention of change in prevalence. Score 43.5 against 56.9 under V2. Every other system explained its method and caveats under V1 without being asked. On V1 the two main systems score close together (Gemini 43.5, Sonnet 46.9) for opposite reasons: Gemini says too little, Sonnet says more but rescales its headline.
11. Stability differs by system. Gemini 3.8 Flash's Task 2 run 2 was a near copy of run 1 (same numbers, same ranges, every row scored the same: 56.9 both times). Sonnet 5.5 kept its headline but varied what it discussed (62.0 vs 81.5). Averaging runs as the rubric specifies: Gemini 56.9, Sonnet 71.8 on Task 2 (V2).
12. Prompt versions on Gemini 3.8 Flash: V1 43.5, V2 56.9 (both runs), V3 76.5. The guided prompt brought out the significance check and kept the official-population headline after the 73,918 check, but its "scenarios" are confidence-interval bounds relabelled as risk scenarios (one wrongly called "2013 reversion"), and it newly over-attributed the 73,918 gap to non-residents. Under V3 the main systems score close (Sonnet 79.8, Gemini 76.5) and split on the headline: Gemini keeps the official population, Sonnet rescales.
13. Task 3 (reverse-engineer 152,000): Sonnet 71.3, Gemini 59.8. Sonnet reached the team's conclusion unprompted: 152,000 cannot be reproduced from the data with constant or falling rates and implies x2.06 growth against x1.42 from ageing; it said the authors would need to supply their method. Gemini questioned the figure too, but its explanations misread its own numbers (a rise from 2023 rates called a continued decline; ageing alone said to give 11.37% crude prevalence instead of 10.25%), and its main challenge, that 152,000 is a 2050 figure misquoted as 2030, rests on recalled projections that are all misattributed (0 of 4 correct). Both stated the 2013-2023 decline as fact and put the 73,918 gap on non-residents. Mythos 5.1 low (extra, 69.5) reached the same reading as Sonnet (152,000 needs rates near 2013 levels, and 2.06x growth from 73,918 mixes a residents-only base with a total-population projection) and guessed, flagged as unverified, that 152,000 predates WiSE 2023, which the dated sources support. Mythos 5.1 max (extra, 92.1) was the only Task 3 run to place the 73,918 gap in a survey base smaller than the actual resident population, to check the decline against the CIs, and to decompose the x2.06 growth into ageing (x1.42) and three method differences (base, 2013 rates, a smaller 2030 base); its recalled context checked out (4 of 4).

## Caveats for the report

- The rubric was revised twice after seeing results (row 10 added; decisions floor added). Both changes are logged in `scoring_rubric.md` and must be disclosed.
- One scorer so far (Jacob, with Claude Code drafting). The reliability check has not been done.
- One run per system per task so far; Task 2 run 2 will show how stable the scores are.
- "Correct" means agreeing with the team's documented modelling decisions, which are themselves judgements.
- The rubric can reward the right conclusion reached for the wrong reason. Row 5 counts as correct if a response locates the 73,918 gap in a smaller survey base, even when the cause it gives for the smaller base is unsupported; row 10 scores the headline a response chooses, not its reasoning. Wrong causes are recorded in the run logs but do not lower these rows.
- Same-family bias: the scores were drafted by Claude Code (an Anthropic model) and include Anthropic systems (Sonnet 5.5, Mythos 5.1). Some later rulings (Gemini V1, run 2 and V3) were applied on Claude Code's recommendation under a standing instruction from Jacob rather than confirmed one by one. The blind second-scorer check is the main safeguard and should include at least one Claude and one Gemini run.
- The rubric under-rewards Task 3's central inference. Sonnet concluded that 152,000 needs age-specific prevalence 11% to 45% above 2023 (x2.06 growth against x1.42 from ageing); Gemini's equivalent arithmetic was read as a continued decline. Both score 36.7 on D because neither the direction of the required change nor the growth multiple is a row. The rubric was not changed after seeing this; the difference is reported in words.
- The ADI 2006 figure (187,000) could not be checked against the primary report and is excluded from the recall scores.
