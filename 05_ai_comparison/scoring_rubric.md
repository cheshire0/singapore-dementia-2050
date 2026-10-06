# AI comparison scoring rubric

Status: version 1.1, 2026-10-06. Not yet reviewed by the rest of the group. Frozen from Task 2 run 2 onward: do not change it while scoring. Any later change must be logged under "Change log" with its date, and every run rescored.

## Principles

1. Every point comes from an observable test on the response text or a recomputation, never from an overall impression.
2. Which rows apply to which task is fixed in advance (table below), not decided per response. This removes the per-response "n/a" judgement.
3. Weights are equal within each component, so no row is weighted up or down to favour a system.
4. A confident error scores below saying nothing. Silence earns 0; a silent error earns -0.5. Penalties can cancel partial (defensible) credit and each other, but never a fully correct row.
5. Every score needs a quote (decisions) or a recomputed value or source reference (numbers and facts) in the run log.

## Components and weights

| Component | Task 1 | Task 2 | Task 3 |
|---|---|---|---|
| D. Modelling decisions | 50 | 60 | 60 |
| A. Arithmetic accuracy | n/a | 25 | 25 |
| F. Factual accuracy (recalled claims) | 50 | 15 | 15 |

If a component has nothing to check in a run (for example no recalled claims in Task 2), it is dropped and the score is rescaled:

Run score = 100 x (sum of points earned) / (sum of weights of the components that applied)

The citation audit is scored separately as 100 x (figures correct) / (figures asked for).

## D. Modelling decisions

### Row levels

| Level | Units | Meaning |
|---|---|---|
| Correct | 1 | Meets the "correct" test for the row |
| Defensible | 0.5 | Meets the "defensible" test |
| Omitted | 0 | Row not addressed, and no claim or calculation in the response depends on it |
| Silent error | -0.5 | Meets the "silent error" test |

### Which rows apply

Core rows: always scored for that task. Penalty-only rows: scored only if the response meets the silent error test (then -0.5); otherwise ignored. Penalty-only rows never add points.

| Row | Task 1 | Task 2 | Task 3 |
|---|---|---|---|
| 1. Age-specific vs flat rate | core | core | core |
| 2. Residents vs total population | penalty-only | core | core |
| 3. Prevalence flat vs changing | core | core | core |
| 4. 2013-2023 decline not significant | penalty-only | core | core |
| 5. WiSE 73,918 on a smaller base | penalty-only | core | core |
| 6. Diagnostic criteria (10/66) | penalty-only | core | core |
| 7. Prevalence vs incidence | core | core | core |
| 8. Range vs point estimate | core | core | core |
| 9. Questions MOH 152,000 | penalty-only | penalty-only | core |
| 10. Headline figure on the official population | not scored | core | core |

Row 10 is not scored in Task 1 because there is no published count to rescale to.

Reason for the Task 1 split: with no data, a system cannot be expected to know about the survey base, the CIs or the population coverage, so only rows any careful answer must address are core.

D score = component weight x max(sum of units, number of correct core rows) / (number of core rows)

The floor means silent errors (on core or penalty-only rows) can never take D below the credit from rows the system got fully right. Without it, a response with one correct row and two silent errors scores the same as one that gets nothing right.

### Row tests

1. Age-specific vs flat rate
   - Correct: Task 2/3: calculates cases band by band. Task 1: names applying age-specific rates to the projected age structure as the method, and does not itself calculate with a single overall rate.
   - Defensible: mentions that the older age mix raises cases, but calculates or reasons with a single overall rate (or names no method).
   - Silent error: calculates with a single overall rate and never mentions age structure.

2. Residents vs total population
   - Correct: states that the population figures cover a different group from the prevalence survey (non-residents included) and states the direction of the bias (too high), without attributing to coverage a gap that coverage cannot explain.
   - Defensible: raises the mismatch only as one possibility with no direction, or attributes to coverage a gap larger than coverage can explain.
   - Silent error: treats the population figures as residents with no comment.

3. Prevalence flat vs changing
   - Correct: Task 2/3: calculates at least two scenarios, one with constant and one with changing rates. Task 1: states that prevalence has been falling (or may change) and that this changes the projection.
   - Defensible: one scenario only, but states the direction in which a change in rates would move the result.
   - Silent error: assumes constant rates (or a given figure) and never mentions that rates could change.

4. 2013-2023 decline not significant
   - Correct: compares the 2013 values with the 2023 CIs, or states that the decline is not statistically established.
   - Defensible: raises the possibility that the decline is sampling noise without checking it.
   - Silent error: states the decline as fact ("fell", "declined") with no qualification.

5. WiSE 73,918 on a smaller base
   - Correct: notices that 2023 rates on the given 2023 population do not reproduce 73,918, and attributes it to the survey's base being smaller than the actual resident 60+ population.
   - Defensible: notices the mismatch but gives a wrong or no cause.
   - Silent error: Task 2/3: projects from the given population without reconciling with 73,918. Any task: uses 73,918 (or "about 74,000") as a census count of all residents with dementia.
   - Whether the system then rescales to 73,918 is a modelling choice: record it in the notes, do not score it.

6. Diagnostic criteria
   - Correct: states that the criteria used (10/66) affect the prevalence figure and so its comparability with estimates using other criteria.
   - Defensible: says methods or definitions differ between studies, without naming diagnostic criteria.
   - Silent error: compares its figure with another source's figure as like for like when the other source is known to use different criteria or methods (for example GBD).

7. Prevalence vs incidence
   - Correct: the answer is a count of people living with dementia.
   - Silent error: presents new cases per year as the answer, or mixes the two.
   - (No defensible level.)

8. Range vs point estimate
   - Correct: gives a range or scenarios for each year asked, and either the method is valid or its limitation is stated.
   - Defensible: gives a range, but the method is invalid and unflagged (for example adding all lower CI bounds and calling it a 95% CI), or a range for only some of the years asked.
   - Silent error: a single point estimate with no statement of uncertainty.

9. Questions MOH 152,000
   - Correct: mentions 152,000 (or MOH's projection) and questions whether it is consistent with the data or with other figures.
   - Defensible: reports the figure correctly (2030, MOH) without questioning it.
   - Silent error: repeats it uncritically as fact, attaches it to the wrong year, or gives a wrong MOH figure.

10. Headline figure on the official population
   - Tests the decision in assumption 3: apply WiSE rates to the official population, not rescale results to WiSE's published 73,918. Row 5 tests whether the system spots and explains the mismatch; this row tests which figures it then puts forward as its answer.
   - Correct: after considering the mismatch with 73,918, recommends figures on the official population (with or without a residents-only adjustment for non-residents).
   - Defensible: recommends figures on the official population without ever considering the mismatch, or recommends figures rescaled to 73,918 while stating they are probably too low.
   - Silent error: presents figures rescaled to 73,918 as the answer without stating they are probably too low.

## A. Arithmetic accuracy

List every number the system derived from the prompt data (not numbers copied from the prompt). Count each distinct number once. Statements about its own results ("85+ is about 70% of 2050 cases") count.

A number is correct if, after recomputation from the prompt data with the system's own stated method, it matches to the precision shown: within half a unit of its last shown digit, or within 2% if introduced with "about", "roughly", "around" or "≈". If one sentence states two incompatible figures for the same quantity, each is checked separately.

A score = 25 x (correct numbers) / (numbers checked)

## F. Factual accuracy

List every claim taken from outside the prompt that contains a number, a date, a named source, or a statement attributed to an organisation.

| Verdict | Counts as |
|---|---|
| Correct: matches the primary source (within the precision shown) | 1 |
| Wrong: contradicts the primary source, wrong year, wrong attribution, or not found in the source it names | 0 |
| Uncheckable: no primary source measures that quantity, or the named source cannot be obtained after a real attempt | excluded, but listed |

Hedging ("I think", "from memory") does not change the verdict. Record it in the notes.

F score = component weight x (correct) / (correct + wrong)

The F component applies only if a run makes at least three checkable claims (correct + wrong >= 3). With fewer, a single claim would swing up to 15 or 50 points, so the component is dropped and the claims are reported in the run log only.

Every verdict needs the source reference in the run log. A claim not yet checked blocks the F score; the run score is then "provisional".

## System score

Score each task, average runs within a task (Task 2 run 1 and run 2), then take the plain mean of Task 1, Task 2, Task 3 and the citation audit. Report the Task 2 run 1 vs run 2 difference alongside as the stability measure; it is not part of the score.

## The "Raised itself?" column

Not scored. The protocol allows no follow-up messages, so anything a response addresses is unprompted by definition. Keep recording it, because it still shows whether a point came from the system or from a hint in the prompt.

## Reliability check

Before reporting, a second team member scores at least two runs blind (without seeing the first scorer's sheet), using only this rubric. Report the share of rows on which both scorers agree. Where they disagree, the row test is ambiguous: fix the wording, log the change, rescore all runs.

## Limitations to disclose in the report

- The rubric was written after Task 1 and Task 2 run 1 had been scored, so it was not blind to those results. Mitigation: it was frozen before Task 2 run 2 and Task 3, and all earlier runs were rescored mechanically under it.
- Component weights (50/50, 60/25/15) are a choice. Report the component scores separately as well, so a reader can reweight.
- "Correct" means agreeing with the team's documented modelling decisions, which are themselves judgements (assumptions log).

## Change log

- 2026-10-06, version 1. Changes made after a trial scoring of Task 2 run 1, before Task 2 run 2 or Task 3 were run:
  - Added row 10 (headline figure on the official population). In the trial, row 5 mixed two things, spotting the mismatch with 73,918 and choosing which figures to report, so the rescaling decision in assumption 3 went unscored: Fable 5.1 low and max tied although only max followed assumption 3.
  - F component needs at least three checkable claims.
  - Arithmetic tolerance extended to "≈"; self-contradictory sentences checked figure by figure.
  - Disclose in the report that row 10 was added after seeing trial scores, and why.
- 2026-10-06, version 1.1. Changed after scoring Task 1, before Task 2 run 2 or Task 3 were run:
  - D floor changed from 0 to the number of correct core rows. Under version 1, Gemini 3.8 Flash's Task 1 run scored 0: its one correct row (prevalence vs incidence) was cancelled by two silent errors (range, MOH), which read as "nothing right". Effects: Gemini Task 1 from 0.0 to 25.0; Fable 5.1 low Task 1 from 81.3 to 87.5 (its row 4 silent error no longer offsets its three correct rows). No Task 2 score changes.
  - Disclose this change in the report alongside row 10.

## Scores: Task 1

Core rows 1, 3, 7, 8 (4 rows; D of 50). Penalty-only rows count only when triggered. All row scores confirmed by Jacob. Recalled claims checked 2026-10-06; verdicts and sources in each run log.

| Row | Gemini 3.8 Flash | Sonnet 5.5 | Fable 5.1 low (extra) | Fable 5.1 max (extra) |
|---|---|---|---|---|
| 1 | 0 | 0.5 | 0 | 0.5 |
| 3 | 0 | 0.5 | 1 | 1 |
| 7 | 1 | 1 | 1 | 1 |
| 8 | -0.5 | 1 | 1 | 1 |
| Penalty rows triggered | 9: -0.5 | 9: -0.5 | 4: -0.5 | 4: -0.5 |
| Sum of units | 0.0 | 2.5 | 2.5 | 3.0 |
| Correct core rows (floor) | 1 | 2 | 3 | 3 |
| D (of 50) | 12.5 | 31.3 | 37.5 | 37.5 |
| F (of 50) | dropped (1 checkable claim: 0 of 1) | 20.0 (2 of 5) | 50.0 (5 of 5) | 50.0 (4 of 4) |
| Run score | 12.5 / 50 = 25.0 | 51.3 / 100 = 51.3 | 87.5 | 87.5 |

## Scores: Task 2 run 1

Decision units: correct 1, defensible 0.5, not addressed 0, silent error -0.5. Rows 1 to 5, 7 and 8 were scored and confirmed by Jacob; row 10 was scored by Claude Code at Jacob's request on 2026-10-06 and needs his confirmation. Row 9 is penalty-only in Task 2 and no run triggered it.

| Row | Gemini 3.8 Flash | Sonnet 5.5 | Fable 5.1 low (extra) | Fable 5.1 max (extra) |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 0.5 | 1 | 1 |
| 3 | 0.5 | 0.5 | 1 | 1 |
| 4 | -0.5 | 0.5 | 1 | 1 |
| 5 | -0.5 | 0.5 | 1 | 1 |
| 6 | 0 | 0 | 0 | 0 |
| 7 | 1 | 1 | 1 | 1 |
| 8 | 0.5 | 1 | 1 | 1 |
| 10 | 0.5 | -0.5 | 0.5 | 1 |
| Sum / 9 | 3.5 | 4.5 | 7.5 | 8.0 |
| D (of 60) | 23.3 | 30.0 | 50.0 | 53.3 |
| A (of 25) | 25.0 (all correct) | 22.7 (20 of 22) | 25.0 (all correct) | 25.0 (all correct) |
| F (of 15) | dropped (0 claims) | dropped (0 claims) | dropped (1 claim) | 15.0 (4 of 4) |
| Run score | 48.3 / 85 = 56.9 | 52.7 / 85 = 62.0 | 75.0 / 85 = 88.2 | 93.3 / 100 = 93.3 |

The version 1.1 floor changes no Task 2 score. Fable 5.1 max's last unchecked claim (152,000 "commonly cited ... before the 2023 survey") was verified on 2026-10-06, so its F component now applies (it was 92.2, provisional, before the check).

For comparison, the trial version (8 core rows, F with any number of claims) gave Gemini 55.9, Sonnet 71.4, Fable low 92.5, Fable max 92.5.
