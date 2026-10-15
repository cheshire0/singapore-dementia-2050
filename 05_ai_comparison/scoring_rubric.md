# AI comparison scoring rubric

Status: version 1.3, 2026-10-15 (Task 4 rows 11 to 16, written before any Task 4 run; see change log). Version 1.2, 2026-10-14. Version 1.1, 2026-10-06. Not yet reviewed by the rest of the group. Frozen from Task 2 run 2 onward: do not change it while scoring. Any later change must be logged under "Change log" with its date, and every run rescored.

## Principles

1. Every point comes from an observable test on the response text or a recomputation, never from an overall impression.
2. Which rows apply to which task is fixed in advance (table below), not decided per response. This removes the per-response "n/a" judgement.
3. Weights are equal within each component, so no row is weighted up or down to favour a system.
4. A confident error scores below saying nothing. Silence earns 0; a silent error earns -0.5. Penalties can cancel partial (defensible) credit and each other, but never a fully correct row.
5. Every score needs a quote (decisions) or a recomputed value or source reference (numbers and facts) in the run log.

## Components and weights

| Component | Task 1 | Task 2 | Task 3 | Task 4 |
|---|---|---|---|---|
| D. Modelling decisions | 50 | 60 | 60 | 60 |
| A. Arithmetic accuracy | n/a | 25 | 25 | 25 |
| F. Factual accuracy (recalled claims) | 50 | 15 | 15 | 15 |

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

| Row | Task 1 | Task 2 | Task 3 | Task 4 |
|---|---|---|---|---|
| 1. Age-specific vs flat rate | core | core | core | core |
| 2. Residents vs total population | penalty-only | core | core | core |
| 3. Prevalence flat vs changing | core | core | core | core |
| 4. 2013-2023 decline not significant | penalty-only | core | core | core |
| 5. WiSE 73,918 on a smaller base | penalty-only | core | core | core |
| 6. Diagnostic criteria (10/66) | penalty-only | core | core | core |
| 7. Prevalence vs incidence | core | core | core | core |
| 8. Range vs point estimate | core | core | core | core |
| 9. Questions MOH 152,000 | penalty-only | penalty-only | core | penalty-only |
| 10. Headline figure on the official population | not scored | core | not scored (v1.2) | core |
| 11. Relative risk and its source | not scored | not scored | not scored | core |
| 12. Avoidable-case method | not scored | not scored | not scored | core |
| 13. Inactivity data stops at 74 | not scored | not scored | not scored | core |
| 14. Association vs causation | not scored | not scored | not scored | core |
| 15. Dwelling and region: no prevalence data | not scored | not scored | not scored | core |
| 16. Sex and ethnicity: all-ages rates, no projections | not scored | not scored | not scored | core |

Task 4 has 15 core rows. Rows 1 to 10 are read as in Task 2, applied to the overall projection. Report the D units for rows 11 to 16 separately as well ("Task 4 new rows"), so the new material can be compared without the Task 2 rows diluting it.

Row 10 is not scored in Task 1 because there is no published count to rescale to, and not in Task 3 (from version 1.2) because Task 3 asks for no projection of its own.

Row 8 in Task 3 (from version 1.2): correct means more than one assumption set that reproduces 152,000 (or a range for a key assumption), with a statement of which is more likely or why it cannot be told; defensible means one assumption set with its uncertainty stated; silent error means one assumption set presented as the answer with no uncertainty.

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

11. Relative risk and its source (Task 4)
   - Correct: states the relative risk (or equivalent effect size) of dementia for physical inactivity that it uses, and names a source that exists and contains that figure for that comparison. The source is checked under F; a source that fails the F check means this row is not correct.
   - Defensible: states the figure it uses but gives no source or only a vague one ("studies suggest"), or names a correct source but uses its figure for a different comparison without saying so (for example a midlife figure applied to people aged 60+).
   - Silent error: estimates avoidable cases without stating any effect size, or names a source that does not contain the figure used.
   - Any figure in the published range is acceptable (for example Iso-Markku et al. 2022, RR 1.25 for inactive vs active; 2020 Lancet Commission, RR 1.4 for late-life inactivity; 2024 Lancet Commission, RR 1.2). The row tests sourcing, not agreement with the team's 1.25.

12. Avoidable-case method (Task 4)
   - Correct: derives the exposed share as insufficiently active (100% - 80.3% = 19.7% at 60-74), combines it with the relative risk in an attributable-fraction formula (PAF = P(RR-1) / (1 + P(RR-1)), or an equivalent), and for the 15% scenario uses the reduced exposure (potential impact fraction; for a 15% relative cut this equals 0.15 x PAF), applied to its own projected case counts.
   - Defensible: correct structure with a stated simplification (for example P x (RR-1) without the denominator, called an approximation), or gives only the full PAF (all inactivity removed) without the 15% scenario.
   - Silent error: takes 80.3% as the exposed share; treats a 15% cut in inactivity as a 15% (or RR-sized) cut in cases; applies the relative risk to all cases; or gives avoidable cases with no traceable method.
   - Reference (team, RR 1.25): PAF 4.69%; 15% scenario 0.704%, which is 965 cases in 2030 and 2,082 in 2050 at constant 2023 rates. With RR 1.4: PAF 7.30%, 15% scenario 1.096%. For A, recompute with the system's own figures and method.

13. Inactivity data stops at 74 (Task 4)
   - Correct: notes that the physical activity data covers only ages 60-74 among older adults, states the assumption it makes for 75 and over (same rate, a higher rate, or 60-74 only), and states which way that assumption moves the result.
   - Defensible: states the assumption for 75+ but not its direction, or restricts the calculation to 60-74 without saying what is left out.
   - Silent error: applies the 60-74 rate to everyone aged 60+ (or to all cases) with no comment.

14. Association vs causation (Task 4)
   - Correct: says the avoidable-case figure assumes the relative risk is causal, and names a reason it may not be (reverse causation, since early dementia reduces activity; confounding), or a reason the effect would not appear by 2030 or 2050 (time lag between activity change and dementia prevalence).
   - Defensible: a general caveat ("observational data", "estimates are uncertain") not linked to the avoidable-case figure.
   - Silent error: presents avoidable cases as a definite result of reducing inactivity with no caveat.

15. Dwelling and region: no prevalence data (Task 4)
   - Correct: states that the data gives no dementia prevalence by type of dwelling or by region, and either declines those breakdowns or gives them only as the distribution of the population at risk, or as cases under a stated assumption (for example the same age-specific rates everywhere), labelled as such.
   - Defensible: gives a dwelling or region breakdown under an assumption it states, without saying the data has no prevalence by dwelling or region; or covers one of the two (dwelling or region) correctly and omits the other.
   - Silent error: presents dementia counts or rates by dwelling or region as if measured, or uses rates for them that are not in the data without stating an assumption.

16. Sex and ethnicity: all-ages rates, no projections (Task 4)
   - Correct: makes both points: (a) the sex and ethnicity prevalences are for all ages 60+ combined, so differences between groups partly reflect age (for example women are older on average), and the response either adjusts for age or says this; (b) the data has no projection of the population by sex or ethnicity to 2030 or 2050 (and the ethnicity counts are from 2020), so any future split rests on a stated assumption (for example shares held at 2020 or 2023).
   - Defensible: makes one of the two points.
   - Silent error: applies the all-ages sex or ethnicity rates to group populations and projects them to 2030 or 2050 with neither point made.
   - Rows 15 and 16 test the team's documented position: the data supports a 2023 description of who is at risk, not a projection by subgroup.

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

Score each task, average runs within a task (Task 2 run 1 and run 2), then take the plain mean of Task 1, Task 2, Task 3 and the citation audit. Task 4 (added in version 1.3) is reported as a separate score, averaged over its runs, and is not added to the system score, so the system scores already reported do not change. Report the Task 2 run 1 vs run 2 difference alongside as the stability measure; it is not part of the score.

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
  - Added row 10 (headline figure on the official population). In the trial, row 5 mixed two things, spotting the mismatch with 73,918 and choosing which figures to report, so the rescaling decision in assumption 3 went unscored: Fable 5.1 low and max tied although only max followed assumption 3 (Fable runs withdrawn 2026-10-14; logs in git history up to `b736991`).
  - F component needs at least three checkable claims.
  - Arithmetic tolerance extended to "≈"; self-contradictory sentences checked figure by figure.
  - Disclose in the report that row 10 was added after seeing trial scores, and why.
- 2026-10-06, version 1.1. Changed after scoring Task 1, before Task 2 run 2 or Task 3 were run:
  - D floor changed from 0 to the number of correct core rows. Under version 1, Gemini 3.8 Flash's Task 1 run scored 0: its one correct row (prevalence vs incidence) was cancelled by two silent errors (range, MOH), which read as "nothing right". Effects: Gemini Task 1 from 0.0 to 25.0; Fable 5.1 low Task 1 from 81.3 to 87.5 (its row 4 silent error no longer offsets its three correct rows; Fable runs withdrawn 2026-10-14; logs in git history up to `b736991`). No Task 2 score changes.
  - Disclose this change in the report alongside row 10.

- 2026-10-14, version 1.2. Changed before any Task 3 response was scored (the first, Gemini 3.8 Flash, had been run but not scored):
  - Row 10 not scored in Task 3. Task 3 asks which assumptions reproduce 152,000, not for a projection, so the row would score 0 for most responses whatever their quality. Task 3 now has 9 core rows.
  - Row 8 given a Task 3 reading (range of assumption sets, see "Which rows apply").
  - Applied on Claude Code's recommendation under Jacob's standing instruction to use its recommendations (2026-10-14). No Task 1 or Task 2 score changes. Disclose alongside the earlier changes.

- 2026-10-15, version 1.3. Written before any Task 4 run (Task 4 prompt committed in `a9a15f1`):
  - Task 4 column added. Rows 1 to 10 apply as in Task 2, except row 9 (penalty-only). New core rows 11 to 16 for physical activity and subgroups. Weights as Task 2 (60/25/15).
  - Task 4 reported separately, not added to the system score.
  - No change to rows 1 to 10 or to any Task 1 to 3 score. Drafted by Claude Code; disclose alongside the earlier changes.

## Scoring conventions (clarifications, 2026-10-14)

Agreed by Jacob on 2026-10-14 while confirming the Mythos 5.1 runs. They interpret existing tests and do not change them. Checked against the Sonnet 5.5 and Gemini 3.8 Flash Task 2 run 1 logs: no score changes there.

- A total that equals the sum of the response's own displayed (rounded) cells counts as correct, even if it differs from the exact sum by rounding.
- A total that equals the sum of band cells rounded to whole people counts as correct even if the cells are not displayed, when whole-person cells are the response's evident method elsewhere (added with Sonnet 5.5 Task 2 run 2; no other run affected).
- The 2% tolerance for "about" numbers is relative (2% of the value), including for percentages.
- A result computed with an unrounded factor counts as correct when the response displays the factor rounded (for example "×0.76" with results matching 0.7645).
- A figure that misses the half-unit test by rounding (for example 10.3% for 10.2496%) is incorrect.
- A rate given as "about x% a year" is checked against the effective (pooled) rate across bands, as well as against each band.
- "About" applied to a headline also covers ranges given in the same statement.
- Worded comparisons derived from the data ("closest to significance", "would hold") count in A as statements about the response's own results.
- Row 8: a range with all bands at their CI limits together, not flagged, is still correct if the response also gives valid scenarios for every year asked.
- Row 8: point estimates with uncertainty stated only in words (no numeric range or scenarios) score 0: the defensible test needs a numeric range, and the silent-error test needs no statement of uncertainty. Added with the Sonnet 5.5 V1 run; no other run is affected.
- Row 5: locating the gap in a smaller survey base is correct even if the cause offered for the smaller base is unsupported (as in the confirmed Fable 5.1 max ruling); record the wrong cause in the notes.
- F: a single attribution naming two sources, one of them wrong, is one wrong claim. Inferences about why a published base is small are not counted in F. A two-part claim with one half verified and the other half unfindable is scored on the verified half.

## Scores: Task 1

Core rows 1, 3, 7, 8 (4 rows; D of 50). Penalty-only rows count only when triggered. All row scores confirmed by Jacob. Recalled claims checked 2026-10-06; verdicts and sources in each run log.

| Row | Gemini 3.8 Flash | Sonnet 5.5 |
|---|---|---|
| 1 | 0 | 0.5 |
| 3 | 0 | 0.5 |
| 7 | 1 | 1 |
| 8 | -0.5 | 1 |
| Penalty rows triggered | 9: -0.5 | 9: -0.5 |
| Sum of units | 0.0 | 2.5 |
| Correct core rows (floor) | 1 | 2 |
| D (of 50) | 12.5 | 31.3 |
| F (of 50) | dropped (1 checkable claim: 0 of 1) | 20.0 (2 of 5) |
| Run score | 12.5 / 50 = 25.0 | 51.3 / 100 = 51.3 |

## Scores: Task 2 run 1

Decision units: correct 1, defensible 0.5, not addressed 0, silent error -0.5. Rows 1 to 5, 7 and 8 were scored and confirmed by Jacob; row 10 was scored by Claude Code at Jacob's request on 2026-10-06 and confirmed by Jacob, 2026-10-14. Row 9 is penalty-only in Task 2 and no run triggered it.

| Row | Gemini 3.8 Flash | Sonnet 5.5 |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 1 | 0.5 |
| 3 | 0.5 | 0.5 |
| 4 | -0.5 | 0.5 |
| 5 | -0.5 | 0.5 |
| 6 | 0 | 0 |
| 7 | 1 | 1 |
| 8 | 0.5 | 1 |
| 10 | 0.5 | -0.5 |
| Sum / 9 | 3.5 | 4.5 |
| D (of 60) | 23.3 | 30.0 |
| A (of 25) | 25.0 (all correct) | 22.7 (20 of 22) |
| F (of 15) | dropped (0 claims) | dropped (0 claims) |
| Run score | 48.3 / 85 = 56.9 | 52.7 / 85 = 62.0 |

The version 1.1 floor changes no Task 2 score.

For comparison, the trial version (8 core rows, F with any number of claims) gave Gemini 55.9, Sonnet 71.4.
