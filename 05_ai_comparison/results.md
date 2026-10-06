# AI comparison: results so far

Last updated 2026-10-06. Scores use `scoring_rubric.md` version 1.1. Full evidence (quotes, recomputed numbers, source checks) is in each run log in `runs/`.

Main comparison: Claude Sonnet 5.5 vs Gemini 3.8 Flash (each company's mid-tier model, low reasoning effort). Claude Fable 5.1 at low and max effort are extra runs showing what a top-tier model catches; they are not part of the main comparison.

## Status

| Item | Status |
|---|---|
| Task 1 cold recall | Done, all four runs scored |
| Task 2 build projection, run 1 | Done, all four runs scored. Row 10 (headline figure) scored by Claude Code, awaiting Jacob's confirmation |
| Task 2 run 2 (stability) | Not run |
| Task 3 reverse-engineer MOH | Prompt not written |
| Citation audit | Not run |
| Second-scorer reliability check | Not done |

## Scores

| Run | Task 1 | Task 2 run 1 |
|---|---|---|
| Gemini 3.8 Flash | 25.0 | 56.9 |
| Claude Sonnet 5.5 | 51.3 | 62.0 |
| Claude Fable 5.1 low (extra) | 87.5 | 88.2 |
| Claude Fable 5.1 max (extra) | 87.5 | 93.3 |

Component breakdown (D decisions, A arithmetic, F recalled facts; "dropped" means fewer than three checkable claims):

| Run | Task 1 D / 50 | Task 1 F / 50 | Task 2 D / 60 | Task 2 A / 25 | Task 2 F / 15 |
|---|---|---|---|---|---|
| Gemini 3.8 Flash | 12.5 | dropped (0 of 1) | 23.3 | 25.0 | dropped (0 claims) |
| Claude Sonnet 5.5 | 31.3 | 20.0 (2 of 5) | 30.0 | 22.7 (20 of 22) | dropped (0 claims) |
| Claude Fable 5.1 low | 37.5 | 50.0 (5 of 5) | 50.0 | 25.0 | dropped (1 of 1) |
| Claude Fable 5.1 max | 37.5 | 50.0 (4 of 4) | 53.3 | 25.0 | 15.0 (4 of 4) |

## Headline figures

| Run | Task 1, 2050 | Task 2, 2030 | Task 2, 2050 |
|---|---|---|---|
| Gemini 3.8 Flash | 152,000 (MOH's 2030 figure, wrong year) | 137,087 | 295,653 |
| Claude Sonnet 5.5 | 150,000 to 200,000 | about 105,000 (rescaled to WiSE) | about 226,000 (rescaled) |
| Claude Fable 5.1 low | 190,000 to 240,000 | about 105,000 (rescaled, "may be too low") | about 226,000 (rescaled) |
| Claude Fable 5.1 max | 190,000 to 240,000 | about 137,000 | about 296,000 |
| Team model (three scenarios) | | 123,177 to 137,087 | 196,615 to 295,653 |
| MOH | | 152,000 | none published |

## Findings

1. Sonnet scored above Gemini on both tasks, by 26.3 points on Task 1 and 5.1 on Task 2. The Task 2 gap is small, and Gemini's headline is closer to the team's model.
2. Arithmetic does not separate the systems. All four reproduced the team's constant-rates figures (137,087 and 295,653) exactly; the only arithmetic errors were two in Sonnet's commentary. What separates them is judgement: whether they check the method against the published 2023 count, whether they treat the 2013-2023 decline as established, and which figures they recommend.
3. Gemini Task 2 was accurate but uncritical: perfect arithmetic and the right headline, but it never checked its 2023 figure against WiSE's published 73,918 and treated the decline as real although the confidence intervals it was given include the 2013 values.
4. Sonnet Task 2 was more critical but reached a worse answer: it noticed the mismatch with 73,918, put it down to the wrong cause (non-residents), and rescaled its headline down by 24% to match, without saying the result is probably too low.
5. In cold recall (Task 1) both mid-tier models stated wrong figures with little hedging: Gemini attached MOH's 2030 figure to 2050; Sonnet attributed 80,000 by 2030 to MOH and appears not to know about WiSE 2023. Recall accuracy: Gemini 0 of 1 checkable claims, Sonnet 2 of 5, Fable low 5 of 5, Fable max 4 of 4.
6. No run addressed diagnostic criteria (10/66 vs others), even though the Task 2 prompt names them.
7. Top tier vs mid tier: both Fable runs checked the decline against the confidence intervals and explained the 73,918 mismatch as a smaller survey base; neither mid-tier model did both. Max effort differed from low effort mainly in which figures it recommended (unscaled, matching our assumption 3) and in bringing up MOH's 152,000 unprompted.
8. A lead from Fable 5.1 max (unverified as MOH's method): 2013 WiSE rates applied to the UN 2030 population, less 5% for non-residents, gives 151,782, close to MOH's 152,000.

## Caveats for the report

- The rubric was revised twice after seeing results (row 10 added; decisions floor added). Both changes are logged in `scoring_rubric.md` and must be disclosed.
- One scorer so far (Jacob, with Claude Code drafting). The reliability check has not been done.
- One run per system per task so far; Task 2 run 2 will show how stable the scores are.
- "Correct" means agreeing with the team's documented modelling decisions, which are themselves judgements.
- The ADI 2006 figure (187,000) could not be checked against the primary report and is excluded from the recall scores.
