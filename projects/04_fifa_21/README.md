# FIFA 21 Player Data — Data Cleaning Report

## At a Glance

This dataset contains **18,979 FIFA 21 football players** with 77 columns of identity, contract, and skill data — names, clubs, heights, wages, and detailed ratings from pace to goalkeeping. The raw file had inconsistent units (feet/inches vs centimeters, pounds vs kilograms), euro amounts stored as text (`€2.5M`), star symbols on skill ratings, and a tangled contract field. After cleaning, every player remains with **78 standardized columns** and numeric values ready for analysis or a player comparison tool.

## Who Would Use This Data?

- **Sports fan / gamer:** Build a player comparison website (similar to SoFIFA) showing ratings, value, and stats side by side.
- **ML engineer / data scientist:** Train models for player valuation, scouting recommendations, or fantasy-team optimization using 55 skill attributes.
- **Web developer:** Power a football stats API or interactive dashboard with clean numeric fields and formatted player URLs.
- **Game developer:** Use cleaned contract dates, wages, and skill blocks as structured input for a football simulation or roster management feature.

## About the Dataset

- **Source:** [Kaggle — FIFA 21 Messy Raw Dataset](https://www.kaggle.com/datasets/yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring). Player URLs reference [SoFIFA](https://sofifa.com). Loaded from `data/raw.csv`.
- **Size:** **18,979 rows × 77 columns** (raw) → **18,979 rows × 78 columns** (final)

The dataset splits naturally into two blocks:

**Player info (23 columns):** ID, Name, Long Name, Photo Url, Player Url, Nationality, Age, OVA (overall rating), POT (potential), Club, Positions, Height, Weight, Preferred Foot, BOV, Best Position, Joined, Contract Type, Contract End Year, Loan Date End, Value, Wage, Release Clause

**Player stats (55 columns):** Detailed skill ratings — Attacking, Movement, Power, Mentality, Defending, Goalkeeping, aggregate stats (PAC, SHO, PAS, DRI, DEF, PHY), work rates (A/W, D/W), weak foot (W/F), skill moves (SM), international reputation (IR), and Hits (page views)

## What Was Wrong With the Raw Data?

- **Inconsistent column names:** camelCase (`photoUrl`), special characters (`↓OVA`), extra whitespace.
- **Mixed height units:** 40 players used feet/inches (`6'2"`) while the rest used centimeters (`182cm`).
- **Mixed weight units:** 40 players used pounds (`165lbs`) while the rest used kilograms (`75kg`).
- **Money as text:** Value, Wage, and Release Clause stored as strings like `€2.5M`, `€12K`, or bare `€900`.
- **Tangled contract field:** Combined contract type and year range in one column (`2020 ~ 2023`).
- **Redundant contract start year:** Duplicated information already in the `Joined` date.
- **Star symbols on ratings:** W/F, SM, and IR columns included `★` characters.
- **Hits in mixed formats:** Some values used K/M suffixes (`1.6K`); **2,595 rows** had missing hits.
- **Dates as text:** Joined and Loan Date End needed datetime conversion.

## Cleaning Process

1. **Column name cleanup** — Stripped whitespace, removed non-ASCII characters, split camelCase into spaced words, and capitalized the first letter of each column name.

2. **Duplicate check** — **0 full-row duplicates** found.

3. **Split into two dataframes** — Separated player info (through Release Clause) from skill stats (Attacking through Hits) for targeted cleaning, then merged back.

4. **Contract unstacking** — Broke the combined `Contract` field into:
   - `Contract Type` (Permanent, On Loan, Free, or Unknown)
   - `Contract Start Year` and `Contract End Year` extracted from patterns like `2020 ~ 2023`

5. **Dropped redundant Contract Start Year** — Compared against the year from `Joined`; **0 mismatches**. The Joined date is more precise, so Contract Start Year was removed.

6. **Height conversion** — Converted **40** feet/inches values to centimeters; kept existing cm values as floats.

7. **Weight conversion** — Converted **40** pound values to kilograms; kept existing kg values as floats.

8. **Money parsing** — Stripped `€` symbols and parsed K (×1,000) and M (×1,000,000) suffixes into plain euro floats. Handled edge cases like `€0`, `€900`, `€850` with a fallback plain-number path.

9. **Date and year conversion** — `Joined` and `Loan Date End` → datetime; `Contract End Year` → integer.

10. **Duplicate ID checks** — **0 duplicate IDs**, **0 duplicate rows** (even excluding ID).

11. **String cleanup** — Trimmed whitespace on 10 string columns; normalized extra spaces and newlines in Club names.

12. **URL validation** — Checked Photo Url and Player Url against expected SoFIFA patterns. **0 anomalies** found.

13. **Star rating cleanup (W/F, SM, IR)** — Stripped `★` symbols and converted to integers.

14. **Work rate validation (A/W, D/W)** — Confirmed all values are Low, Medium, or High only.

15. **Hits parsing** — Converted **28** K/M-format values (e.g. `1.6K` → 1600) to integers. Missing hits (**2,595 rows**) set to **0**.

16. **Merge and export** — Recombined info and stats into one dataframe: **18,979 rows × 78 columns**.

## Key Results

| Metric | Value |
|--------|-------|
| Rows before / after | 18,979 / 18,979 (none dropped) |
| Columns before / after | 77 / 78 |
| Mean overall rating (OVA) | 65.7 |
| Mean potential (POT) | 71.1 |
| Mean age | 25.2 years |
| Mean height | 181.2 cm |
| Mean weight | 75.0 kg |
| Mean player value | ~€2.87M |
| Mean wage | ~€9,092 |
| Mean release clause | ~€3.96M |
| Max player value | €185.5M |
| Missing contract end years | 1,250 |
| Missing loan end dates | 17,966 (expected — most players aren't on loan) |
| Mean Hits (page views) | ~23 |

## Output Files

| File | Description |
|------|-------------|
| `data/raw.csv` | Original messy input |
| `data/clean.csv` | Final cleaned dataset (18,979 rows × 78 columns, dates as YYYY-MM-DD) |

## Notebook

Full step-by-step code and outputs: [`04_data_cleaning.ipynb`](04_data_cleaning.ipynb)
