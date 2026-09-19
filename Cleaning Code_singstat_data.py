"""
Clean three SingStat population datasets into tidy, analysis-ready CSVs.

Input files (as uploaded):
  1. HM_SingaporeResidentsByAgeGroupAndTypeOfDwellingAnnual.csv
     -> indented cross-tab: AgeGroup > DwellingType > HDB Room Type, wide by year
  2. HM_Singapore_Residents_By_Planning_Region__Age_Group_And_Sex__End_June_csv.xlsx
     -> indented cross-tab: Region (+ Male/Female) > AgeGroup, wide by year
  3. HM_ResidentPopulationbySingleYearofAgeEthnicGroupandSexCensusofPopulation2020_csv.xlsx
     -> already-tabulated single-year-of-age x Ethnicity_Sex columns (2020 Census)

Each is reshaped into a "long"/tidy table (one row per observation) and
written to /mnt/user-data/outputs/ as a CSV. Run this script directly:

    python3 clean_singstat_data.py

Requires: pandas, openpyxl
"""

import re
import pandas as pd

IN_DIR = "/mnt/user-data/uploads"
OUT_DIR = "/mnt/user-data/outputs"


# ---------------------------------------------------------------------------
# 1. Residents by Age Group and Type of Dwelling (annual, wide CSV)
# ---------------------------------------------------------------------------
def clean_dwelling_by_age(path):
    """
    Keeps only the most granular rows: real age brackets (drops the
    "Residents" grand-total-across-ages row) x the finest dwelling-type
    leaf available (drops the "Total HDB Dwellings" subtotal, keeping its
    4 room-type children instead, alongside Condominiums/Landed/Other).
    """
    df = pd.read_csv(path)
    year_cols = [c for c in df.columns if c != "DataSeries"]

    records = []
    age_group = None
    in_hdb_block = False

    for _, row in df.iterrows():
        raw_label = row["DataSeries"]
        indent = len(raw_label) - len(raw_label.lstrip(" "))
        label = raw_label.strip()

        if indent == 0:
            # Top-level age bracket. Skip the "Residents" row entirely -
            # it's the grand total across every age bracket, not an age
            # bracket itself.
            if label == "Residents":
                age_group = None
                continue
            age_group = label
            in_hdb_block = False

        elif indent == 4 and age_group is not None:
            if label == "Total HDB Dwellings":
                # Subtotal of the 4 HDB room types below it - skip the
                # subtotal itself, keep tracking that we're in this block
                # so the indent==8 rows still know their age_group.
                in_hdb_block = True
                continue
            in_hdb_block = False
            for year in year_cols:
                records.append({
                    "age_group": age_group,
                    "dwelling_type": label,
                    "year": int(year),
                    "residents": row[year],
                })

        elif indent == 8 and age_group is not None and in_hdb_block:
            # HDB room-type breakdown - the finest level available, kept as-is
            for year in year_cols:
                records.append({
                    "age_group": age_group,
                    "dwelling_type": label,
                    "year": int(year),
                    "residents": row[year],
                })

    out = pd.DataFrame(records)
    out["residents"] = pd.to_numeric(out["residents"], errors="coerce")
    return out


# ---------------------------------------------------------------------------
# 2. Residents by Planning Region, Age Group and Sex (end June, wide xlsx)
# ---------------------------------------------------------------------------
def clean_region_age_sex(path):
    """
    Keeps only Male/Female rows for each region x age group, dropping the
    unsuffixed "<Region>" block, which is the combined-sex total.
    """
    raw = pd.read_excel(path, header=None)

    # Find the header row ("Data Series", 2025, 2024, ...) and where the
    # data ends (the "Definitions and Footnotes:" block).
    header_idx = raw[raw[0] == "Data Series"].index[0]
    years = raw.loc[header_idx, 1:].tolist()
    years = [int(y) for y in years]

    footer_matches = raw[raw[0].astype(str).str.contains(
        "Definitions and Footnotes", na=False)]
    end_idx = footer_matches.index[0] if len(footer_matches) else len(raw)

    data = raw.loc[header_idx + 1:end_idx - 1].dropna(how="all")

    records = []
    region, sex = None, None
    sex_pattern = re.compile(r"^(.*)\s\((Male|Female)\)$")

    for _, row in data.iterrows():
        label = str(row[0]).strip()

        m = sex_pattern.match(label)
        if m:
            # A new region/sex block, e.g. "Central Region (Male)"
            region, sex = m.group(1), m.group(2)
            continue
        if "Years" not in label:
            # A new region block, e.g. plain "Central Region" - this is the
            # combined-sex total block, so mark sex=None to skip its rows.
            region, sex = label, None
            continue

        # Otherwise this is an age-group row within the current region/sex block
        if sex is None:
            continue  # inside the combined-sex ("Total") block - skip
        age_group = label
        for year, value in zip(years, row[1:len(years) + 1]):
            records.append({
                "region": region,
                "sex": sex,
                "age_group": age_group,
                "year": year,
                "residents": value,
            })

    out = pd.DataFrame(records)
    out["residents"] = pd.to_numeric(out["residents"], errors="coerce")
    return out


# ---------------------------------------------------------------------------
# 3. Resident Population by Single Year of Age, Ethnic Group and Sex
#    (Census of Population 2020)
# ---------------------------------------------------------------------------
def clean_ethnic_age_sex(path):
    """
    Keeps only real ages (drops the "Total" grand-total-across-ages row)
    x real ethnic groups (drops the "Total_*" columns, which sum the 4
    ethnic groups) x real sexes (drops "*_Total", which sums Male+Female).
    """
    # The workbook ships a raw pivot sheet and two cleaned-up sheets;
    # the full breakdown (with Total/Male/Female for every ethnic group)
    # lives in the third sheet.
    df = pd.read_excel(path, sheet_name="HM_ResidentPopulationbySingleYe")
    df = df.rename(columns={df.columns[0]: "age"})

    # Drop the grand-total-across-ages row
    df = df[df["age"] != "Total"]

    # "-" denotes nil/negligible per SingStat notation -> treat as 0
    df = df.replace("-", 0)

    # Only keep <Ethnicity>_<Sex> columns for real ethnicities and real
    # sexes - drop every "Total_*" and "*_Total" column
    value_cols = [c for c in df.columns
                  if c != "age" and not c.startswith("Total_")
                  and not c.endswith("_Total")]

    long = df.melt(id_vars="age", value_vars=value_cols,
                    var_name="ethnicity_sex", value_name="residents")

    split = long["ethnicity_sex"].str.rsplit("_", n=1, expand=True)
    long["ethnicity"] = split[0]
    long["sex"] = split[1]
    long = long.drop(columns="ethnicity_sex")
    long = long.rename(columns={"age": "age_group"})

    long["residents"] = pd.to_numeric(long["residents"], errors="coerce")
    long = long[["age_group", "ethnicity", "sex", "residents"]]

    # melt() groups all rows by source column (i.e. all ages for
    # Chinese_Males, then all ages for Chinese_Females, ...), which
    # separates related rows. Re-sort so each age group shows every
    # ethnicity x sex together, in a natural age order.
    def age_sort_key(age):
        if age == "Below 1":
            return -1
        if age == "100 & Over":
            return 100
        return int(age)

    long["_age_sort"] = long["age_group"].map(age_sort_key)
    ethnicity_order = ["Chinese", "Malays", "Indians", "Others"]
    sex_order = ["Males", "Females"]
    long["ethnicity"] = pd.Categorical(long["ethnicity"], categories=ethnicity_order, ordered=True)
    long["sex"] = pd.Categorical(long["sex"], categories=sex_order, ordered=True)
    long = long.sort_values(["_age_sort", "ethnicity", "sex"]).drop(columns="_age_sort")
    return long.reset_index(drop=True)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import os
    os.makedirs(OUT_DIR, exist_ok=True)

    dwelling = clean_dwelling_by_age(
        f"{IN_DIR}/HM_SingaporeResidentsByAgeGroupAndTypeOfDwellingAnnual.csv")
    dwelling.to_csv(f"{OUT_DIR}/clean_residents_by_age_and_dwelling.csv", index=False)
    print(f"Dwelling-by-age table: {dwelling.shape[0]} rows -> "
          f"clean_residents_by_age_and_dwelling.csv")

    region = clean_region_age_sex(
        f"{IN_DIR}/HM_Singapore_Residents_By_Planning_Region__Age_Group_And_Sex__End_June_csv.xlsx")
    region.to_csv(f"{OUT_DIR}/clean_residents_by_region_age_sex.csv", index=False)
    print(f"Region-age-sex table: {region.shape[0]} rows -> "
          f"clean_residents_by_region_age_sex.csv")

    ethnic = clean_ethnic_age_sex(
        f"{IN_DIR}/HM_ResidentPopulationbySingleYearofAgeEthnicGroupandSexCensusofPopulation2020_csv.xlsx")
    ethnic.to_csv(f"{OUT_DIR}/clean_residents_by_age_ethnicity_sex.csv", index=False)
    print(f"Age-ethnicity-sex table: {ethnic.shape[0]} rows -> "
          f"clean_residents_by_age_ethnicity_sex.csv")
