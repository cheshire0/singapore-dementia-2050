# AI comparison protocol

## Purpose
Test whether two different AI systems make sound modelling decisions when projecting Singapore dementia cases, scored against our validated model and the MOH benchmark.

## Systems
- AI 1: TBD (name + version)
- AI 2: TBD (name + version)

## Controls
- Fresh session every run, no memory or prior context
- Identical prompt, pasted verbatim
- Log date, model version, full response
- AI never sees our answer or MOH's 152,000 during tasks 1 and 2

## Data package (tasks 2 and 3 only)
- 01_demographics/model_input_population.csv
- WiSE 2013 and 2023 age-specific prevalence rates
- The research question

## Tasks
1. Cold recall: no data. "How many people in Singapore will have dementia in 2050?"
2. Build the projection: data package given. Produce 2030 and 2050 estimates and explain the method.
3. Reverse-engineer MOH: given 2023 baseline and population data, told someone estimated 152,000 for 2030. What assumptions produce that?

Task 2 repeated once per system on a different day to test stability.

## Scoring sheet
Each row scored: correct / defensible / silent error, plus whether the AI raised the issue itself.

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

## Citation audit
Ask each system for: WiSE 2023 prevalence by band, Singapore 60+ population 2023, relative risk of dementia for physical inactivity. Check every figure against source. Report accuracy rate.

## Outputs
- Raw responses saved in 05_ai_comparison/runs/
- Completed scoring sheet
- Comparison table: our model vs AI 1 vs AI 2 vs MOH
