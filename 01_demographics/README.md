# singapore-dementia-2050
A data-driven projection of dementia prevalence in Singapore to 2050 using demographic and WiSE data, with validation against MOH estimates and scenario modelling of how increased physical activity could reduce future dementia burden.
"# singapore-dementia-2050" 

# I uploaded the original and the cleaned version

## Files

Cleaned_residents_by_*.csv - SingStat resident counts (citizens + PRs), 2000-2025. Historical actuals, no projections. Cleaned by Cleaning Code_singstat_data.py.

singapore_population_by_age_1950_2100.csv - Singapore rows from UN World Population Prospects 2024 (5-year age groups, both sexes). Values converted from thousands to persons. source column: Estimates = 1950-2023, Medium variant = 2024-2100 projections. UN counts total population incl. non-residents, so it runs ~5.8% above SingStat at 60+. High/low variants are identical to medium for 60+ until ~2085.

model_input_population.csv - the above collapsed to WiSE's bands (60-74 / 75-84 / 85+) for 2023, 2030 and 2050. This is what the projection model uses.
