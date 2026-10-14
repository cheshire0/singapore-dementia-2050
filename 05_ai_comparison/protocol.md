# AI comparison protocol

## Purpose
Test whether two different AI systems make sound modelling decisions when projecting Singapore dementia cases, scored against our validated model and the MOH benchmark.

## Systems
- AI 1: Claude Sonnet 5.5 (Anthropic), claude.ai web app, incognito chat, effort low
- AI 2: Gemini 3.8 Flash (Google), Google AI Studio, thinking low, Grounding with Google Search off, all other settings default, no system instructions

Pairing rule: each company's current mid-tier model at low reasoning effort. The match is approximate; no two models from different companies are exactly equivalent. A first Task 1 run used Claude Fable 5.1 (Anthropic's top tier) against Gemini 3.8 Flash; that tier mismatch would confound "system" with "model size", so the pairing was changed. Extra top-tier data points (not part of the main comparison) will be run on Mythos 5.1 at low and max effort. The earlier extra runs on Fable 5.1 (low and max effort, Tasks 1 and 2) were withdrawn on 2026-10-14; their logs remain in git history up to `b736991`.

The same pairing and settings are used for every task and the citation audit. Gemini runs use AI Studio rather than the Gemini app because AI Studio shows the exact model and lets search grounding be switched off. Exact model labels and settings are recorded in each run log.

## Controls
- Fresh session every run, no memory or prior context
- Identical prompt, pasted verbatim
- No web search. The web search toggle could not be found in the claude.ai interface (checked 2026-10-06), so every prompt includes the same sentence after the instruction: "Answer using only your own knowledge and any data in this message; do not search the web." Each run log records whether the system searched anyway.
- Log date, model version, settings, full response; screenshot of each response kept as the primary record
- AI never sees our answer or MOH's 152,000 during tasks 1 and 2

## Data package (tasks 2 and 3 only)
- 01_demographics/model_input_population.csv
- WiSE 2013 and 2023 age-specific prevalence rates
- The research question

## Tasks
1. Cold recall: no data. "How many people in Singapore will have dementia in 2050?" plus the no-search sentence.
2. Build the projection: data package given. Produce 2030 and 2050 estimates and explain the method.
3. Reverse-engineer MOH: given 2023 baseline and population data, told someone estimated 152,000 for 2030. What assumptions produce that?

Task 2 repeated once per system on a different day to test stability.

### Task 2 prompt versions

To compare prompting strategies, Task 2 is run on each main system with three prompt versions. Only the instructions differ; the data block is identical in all three (checked by script).

| Version | File | Strategy |
|---|---|---|
| V1 minimal | `prompts/task2_v1_minimal.txt` | The question and the data only. No request to explain the method. |
| V2 standard | `prompts/task2_build_projection.txt` | Research question, data, "produce estimates and explain your method". Used for run 1 and run 2. |
| V3 guided | `prompts/task2_v3_guided.txt` | Role ("You are an epidemiologist ...") plus a seven-step checklist: assumptions, method, check 2023 against the published count, judge the 2013-2023 change, range of estimates, headline choice, limitations. |

All versions are scored with rubric v1.1. V3 asks directly about several scored issues (rows 3, 4, 5, 8, 10), so in V3 those rows can be correct but are not counted as raised by the AI itself. With one run per version, a difference between versions may be run-to-run noise; compare it with the run 1 vs run 2 difference for V2.

### Task 3 prompt

`prompts/task3_reverse_engineer_moh.txt`. Same research question, no-search sentence and data block as Task 2 (data block identical, checked with `diff`). Added before the instruction: the published estimate, given as "about 74,000 people ... in 2023", taken from the second WiSE study, growing "to 152,000 by 2030", with no method, assumptions or age breakdown. This matches the MOH written parliamentary answer of 4 November 2025, which gives no age range or method.

Design choices:
- The source is called "a published estimate", not named as MOH, so the systems reason from the data rather than from what they may recall about MOH.
- The prompt asks only what assumptions would produce 152,000. It does not ask whether they are plausible, so questioning the figure (row 9, core in Task 3) is unprompted.
- Run once per main system (Sonnet 5.5, Gemini 3.8 Flash) with the same settings as Tasks 1 and 2, fresh session, no follow-ups.

## Scoring sheet
Each row scored: correct / defensible / silent error, plus whether the AI raised the issue itself.

Rule for "Questions MOH 152,000 unprompted": if a run never mentions 152,000 or any MOH figure, score n/a. Repeating 152,000 uncritically, attaching it to the wrong year, or giving a wrong MOH figure scores silent error.

| Decision | Our model | AI 1 | AI 2 |
|---|---|---|---|
| Age-specific rates vs flat 8.8% | Age-specific | | |
| Residents vs total population | Documented (assumption 1) | | |
| Prevalence held flat vs declining | 3 scenarios | | |
| Notices 2013-2023 decline not significant | Yes | | |
| Spots WiSE 73,918 is survey-weighted | Yes | | |
| 10/66 vs DSM-IV criteria | 10/66 | | |
| Prevalence vs incidence | Prevalence | | |
| Range vs point estimate | Range | | |
| Questions MOH 152,000 unprompted | n/a | | |
| Headline figure on the official population | Official population (assumption 3) | | |

Row tests, applicability by task, and the calculation of a score out of 100 are defined in `scoring_rubric.md`.

## Citation audit
Ask each system for: WiSE 2023 prevalence by band, Singapore 60+ population 2023, relative risk of dementia for physical inactivity. Check every figure against source. Report accuracy rate.

Prompt: `prompts/citation_audit.txt`. Fresh session per system, same settings as Tasks 1 to 3, no follow-ups. It asks for each figure with its source and says to admit not knowing rather than guess.

Five figures are asked for: the three WiSE 2023 band prevalences, the 2023 resident 60+ population, and one relative risk. Score = 100 x (figures correct) / 5.

- A figure is correct if it matches its primary source within the precision shown (2% if given as "about"), and the source named for it exists and contains it. A right number with a wrong or invented source is wrong.
- Reference values: WiSE 2023 bands 3.0%, 18.2%, 48.6% (Subramaniam et al. 2025, Alzheimer's & Dementia, Supplementary Table S1); resident 60+ in 2023, 1,011,631 (SingStat, residents by age group, mid-year). The relative risk is checked against whichever source the system names (for example Iso-Markku et al. 2022, pooled RR 0.80 for active vs inactive, i.e. 1.25 for inactive; or the 2020 Lancet Commission).
- "I don't know" counts as not correct but is recorded separately from wrong answers, so the report can show calibration as well as accuracy.
- Extra figures the system volunteers (CIs, overall prevalence, other years) are listed in the log and checked, but are not part of the score.

## Outputs
- Raw responses saved in 05_ai_comparison/runs/
- Completed scoring sheet
- Comparison table: our model vs AI 1 vs AI 2 vs MOH
