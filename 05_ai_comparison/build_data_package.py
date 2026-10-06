# /// script
# requires-python = ">=3.10"
# dependencies = ["openpyxl"]
# ///
"""Build the AI comparison data package and prompt files from the repo data.

Run from anywhere:
    uv run 05_ai_comparison/build_data_package.py
or  pip install openpyxl && python 05_ai_comparison/build_data_package.py

Writes:
    05_ai_comparison/data_package.md
    05_ai_comparison/prompts/task1_cold_recall.txt
    05_ai_comparison/prompts/task2_build_projection.txt

The prompt files contain only the text to paste into the chat, nothing else.
The package must not contain our projections or MOH's 152,000 (see protocol.md).
"""
import csv
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "05_ai_comparison"
POPULATION_CSV = ROOT / "01_demographics" / "model_input_population.csv"
WISE_XLSX = ROOT / "02_dementia_prevalence" / "james dataset.xlsx"

BANDS = ["60-74", "75-84", "85+"]
YEARS = [2023, 2030, 2050]

RESEARCH_QUESTION = (
    "How many Singapore residents aged 60 and over will have dementia "
    "in 2030 and in 2050?"
)

# Same sentence in every prompt so the search condition is identical across systems.
NO_SEARCH = "Answer using only your own knowledge and any data in this message; do not search the web."

TASK1_PROMPT = f"How many people in Singapore will have dementia in 2050? {NO_SEARCH}"

TASK2_PROMPT = f"""I am working on this research question: {RESEARCH_QUESTION}

Using the data below, produce estimates for 2030 and 2050 and explain your method. {NO_SEARCH}"""


def clean(label):
    """The workbook uses en dashes in band labels (60–74); the CSV uses hyphens."""
    return str(label).replace("–", "-").strip()


def read_population():
    pop, source = {}, {}
    with open(POPULATION_CSV, newline="") as f:
        for row in csv.DictReader(f):
            year = int(row["year"])
            pop[(year, row["age_band"])] = int(row["population"])
            source[year] = row["source"]
    missing = [(y, b) for y in YEARS for b in BANDS if (y, b) not in pop]
    if missing:
        raise SystemExit(f"model_input_population.csv is missing {missing}")
    return pop, source


def read_wise():
    wb = openpyxl.load_workbook(WISE_XLSX, data_only=True)

    # 2023 band prevalence with 95% CI: Supplementary Table S1 of the 2025 paper
    p2023 = {}
    for variable, category, _n, prev, lo, hi in wb["Supplementary S1"].iter_rows(
        min_row=2, values_only=True
    ):
        if variable == "Age group":
            p2023[clean(category)] = (prev, lo, hi)

    # 2013 band prevalence, overall prevalence and case counts: IMH release table
    p2013, overall, cases = {}, None, None
    for label, v2013, v2023, _notes in wb["IMH WiSE Comparison"].iter_rows(
        min_row=2, values_only=True
    ):
        label = clean(label)
        if label.startswith("Dementia prevalence: "):
            band = label.removeprefix("Dementia prevalence: ")
            p2013[band] = v2013 * 100
            # the two sheets must agree on the 2023 rate
            if abs(v2023 * 100 - p2023[band][0]) > 1e-9:
                raise SystemExit(f"2023 prevalence for {band} differs between sheets")
        elif label == "Overall dementia prevalence":
            overall = (v2013 * 100, v2023 * 100)
        elif label == "Number of older adults with dementia":
            cases = (v2013, v2023)

    if sorted(p2013) != sorted(BANDS) or not overall or not cases:
        raise SystemExit("could not find all WiSE figures in james dataset.xlsx")
    return p2013, p2023, overall, cases


def build_package():
    pop, source = read_population()
    p2013, p2023, overall, cases = read_wise()

    lines = [
        "DATA",
        "",
        "1. Population of Singapore by age band",
        "Source: United Nations World Population Prospects 2024, Singapore, "
        "both sexes combined.",
        "",
        "| Year | " + " | ".join(BANDS) + " | Type |",
        "|---|" + "---|" * (len(BANDS) + 1),
    ]
    for y in YEARS:
        counts = " | ".join(f"{pop[(y, b)]:,}" for b in BANDS)
        lines.append(f"| {y} | {counts} | {source[y]} |")

    lines += [
        "",
        "2. Dementia prevalence from the Well-being of the Singapore Elderly "
        "(WiSE) study",
        "Source: Institute of Mental Health, Singapore. Two nationally "
        "representative cross-sectional surveys of Singapore residents "
        "(citizens and permanent residents) aged 60 and over, in 2013 and "
        "2023. Dementia diagnosed using the 10/66 criteria.",
        "",
        "| Age band | 2013 prevalence | 2023 prevalence (95% CI) |",
        "|---|---|---|",
    ]
    for b in BANDS:
        prev, lo, hi = p2023[b]
        lines.append(f"| {b} | {p2013[b]:.1f}% | {prev:.1f}% ({lo:.1f} to {hi:.1f}) |")
    lines += [
        f"| All aged 60+ | {overall[0]:.1f}% | {overall[1]:.1f}% |",
        "",
        "Number of people aged 60+ with dementia as published by the study: "
        f"{cases[0]} in 2013, {cases[1]} in 2023.",
    ]
    return "\n".join(lines) + "\n"


def main():
    package = build_package()
    (OUT / "data_package.md").write_text(package)
    (OUT / "prompts").mkdir(exist_ok=True)
    (OUT / "prompts" / "task1_cold_recall.txt").write_text(TASK1_PROMPT + "\n")
    (OUT / "prompts" / "task2_build_projection.txt").write_text(
        TASK2_PROMPT + "\n\n" + package
    )
    print(package)


if __name__ == "__main__":
    main()
