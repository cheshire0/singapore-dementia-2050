# /// script
# requires-python = ">=3.10"
# dependencies = ["openpyxl"]
# ///
"""Build the Task 4 (extended projection) prompt from the repo data.

Run from anywhere:
    uv run 05_ai_comparison/build_task4_prompt.py

Writes:
    05_ai_comparison/prompts/task4_extended_projection.txt

Items 1 and 2 of the data block are the Task 2 data package, unchanged.
Items 3 to 7 add WiSE 2023 prevalence by sex and ethnicity, NPHS 2024
physical activity, and SingStat residents aged 60+ by dwelling, region and
ethnicity, collapsed to the WiSE age bands.
The prompt must not contain our projections, our relative risk or MOH's
152,000 (see protocol.md).
"""
import csv
import re
from collections import defaultdict
from pathlib import Path

import openpyxl

from build_data_package import BANDS, NO_SEARCH, RESEARCH_QUESTION, WISE_XLSX, build_package, clean

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "05_ai_comparison" / "prompts" / "task4_extended_projection.txt"
DEMO = ROOT / "01_demographics"
NPHS_CSV = ROOT / "04_physical_activity" / "PA_Prevalence_NPHS_2024.csv"

TASK4_INSTRUCTION = f"""I am working on this research question: {RESEARCH_QUESTION[:-1]}, and how many of those cases could be avoided by reducing physical inactivity?

Using the data below:
1. Produce estimates for 2030 and 2050.
2. Estimate how many of those cases could be avoided if the share of older adults who are insufficiently active fell by 15% in relative terms.
3. Break your estimates down by sex, ethnicity, type of dwelling and region.

Explain your method and what drives your results. If you use any figure that is not in the data, say what it is and where it comes from. {NO_SEARCH}"""


def band(age_label):
    """Map a SingStat age label ('60-64 Years', '60 - 64 Years', '72', '100 & Over') to a WiSE band."""
    m = re.match(r"\s*(\d+)", age_label)
    if not m or age_label.startswith("Below"):
        return None
    age = int(m.group(1))
    if 60 <= age < 75:
        return "60-74"
    if 75 <= age < 85:
        return "75-84"
    if age >= 85:
        return "85+"
    return None


def table(header, rows):
    lines = ["| " + " | ".join(header) + " |", "|---" * len(header) + "|"]
    lines += ["| " + " | ".join(r) + " |" for r in rows]
    return lines


def band_counts(path, keys, year=None):
    counts = defaultdict(float)
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            if year and row["year"] != str(year):
                continue
            b = band(row["age_group"])
            if b:
                counts[tuple(row[k] for k in keys) + (b,)] += float(row["residents"])
    return counts


def wise_subgroups():
    rows = {"Gender": [], "Ethnicity": []}
    sheet = openpyxl.load_workbook(WISE_XLSX, data_only=True)["Supplementary S1"]
    for variable, category, _n, prev, lo, hi in sheet.iter_rows(min_row=2, values_only=True):
        if variable in rows:
            rows[variable].append((clean(category), f"{prev:.1f}% ({lo:.1f} to {hi:.1f})"))
    return rows


def nphs():
    with open(NPHS_CSV, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f, delimiter=";"):
            if row["Age"] == "60-74":
                return row["Sufficient PA (%)"], row["Males (%)"], row["Females (%)"]
    raise SystemExit("60-74 row not found in PA_Prevalence_NPHS_2024.csv")


def extra_items():
    lines = []
    wise = wise_subgroups()
    lines += [
        "",
        "3. Dementia prevalence in 2023 by sex and by ethnicity, from the same WiSE study",
        "Residents aged 60 and over, all ages combined (not broken down by age band).",
        "",
    ]
    lines += table(["Group", "2023 prevalence (95% CI)"], wise["Gender"] + wise["Ethnicity"])

    total, men, women = nphs()
    lines += [
        "",
        "4. Physical activity",
        "Source: Ministry of Health, National Population Health Survey 2024. Share of residents "
        "meeting the recommended level of physical activity. The survey covers residents aged 18 to 74.",
        "",
    ]
    lines += table(["Age band", "All", "Men", "Women"], [("60-74", f"{total}%", f"{men}%", f"{women}%")])

    dwelling = band_counts(DEMO / "Cleaned_residents_by_age_and_dwelling.csv", ["dwelling_type"], 2023)
    lines += [
        "",
        "5. Residents aged 60 and over by type of dwelling, 2023",
        "Source: Department of Statistics Singapore, Singapore residents by age group and type of dwelling.",
        "",
    ]
    types = sorted({k[0] for k in dwelling})
    lines += table(["Type of dwelling"] + BANDS,
                   [(t, *(f"{dwelling[(t, b)]:,.0f}" for b in BANDS)) for t in types])

    region = band_counts(DEMO / "Cleaned_residents_by_region_age_sex.csv", ["region", "sex"], 2023)
    lines += [
        "",
        "6. Residents aged 60 and over by planning region and sex, 2023",
        "Source: Department of Statistics Singapore, Singapore residents by planning region, age group and sex.",
        "",
    ]
    regions = sorted({k[0] for k in region})
    lines += table(["Region", "Sex"] + BANDS,
                   [(r, s, *(f"{region[(r, s, b)]:,.0f}" for b in BANDS))
                    for r in regions for s in ("Male", "Female")])

    ethnicity = band_counts(DEMO / "Cleaned_residents_by_age_ethnicity_sex.csv", ["ethnicity", "sex"])
    lines += [
        "",
        "7. Residents aged 60 and over by ethnic group and sex, 2020",
        "Source: Department of Statistics Singapore, Census of Population 2020, resident population "
        "by single year of age, ethnic group and sex.",
        "",
    ]
    lines += table(["Ethnic group", "Sex"] + BANDS,
                   [(e, s, *(f"{ethnicity[(e, s, b)]:,.0f}" for b in BANDS))
                    for e in ("Chinese", "Malays", "Indians", "Others") for s in ("Males", "Females")])
    return "\n".join(lines) + "\n"


def main():
    prompt = TASK4_INSTRUCTION + "\n\n" + build_package() + extra_items()
    OUT.write_text(prompt)
    print(prompt)


if __name__ == "__main__":
    main()
