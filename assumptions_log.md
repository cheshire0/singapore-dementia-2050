# Assumptions log

| # | Assumption | Source | Reason | Effect on projection | Sensitivity tested? |
|---|---|---|---|---|---|
| 1 | Population projections from UN World Population Prospects 2024, not SingStat | UN WPP 2024, 5-year age groups | SingStat publishes no projections by age band | UN counts total population incl. non-residents, ~5.8% above SingStat residents at 60+ in 2023, so estimates run slightly high | Not yet |
| 2 | Medium variant used | UN WPP 2024 | High/low are fertility variants; everyone 60+ in 2050 was born by 1990 | None. 60+ bands identical across all three variants until ~2085 | Yes, checked: identical |
| 3 | WiSE age-specific rates applied to official population, not WiSE's weighted total | WiSE 2023, Table 2 | WiSE's 838,800 is the sum of survey weights. WiSE says its count refers to "Singapore's population in 2022" (Subramaniam et al. 2025, section 3.1), but 838,800 is 13.2% below SingStat resident 60+ for 2022 (966,140) and ~17% below 2023 (1,011,631); cause unknown | 2023 baseline is 89,387 vs WiSE's 73,918, so our figures run above WiSE/MOH-based numbers | Yes: 2013 gives 61,480 vs 51,934, same direction |
| 4 | Report absolute case counts as the headline; express any rates as % of the 60+ population, not % of total population | Our analysis; supports lecturer comment 3a ("do not forget about absolute values") | % of total population depends on fertility variant (5.25% low vs 4.53% high in 2050) because total includes births after 2024 | None on case counts or 60+ rates | Yes, checked |
