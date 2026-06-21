# Marketing Campaign Data — Data Cleaning Report

## At a Glance

This dataset contains **2,020 digital advertising campaigns** — each record tracks where an ad ran, how much was spent, and how many people saw and clicked it. The raw file had messy column names, currency symbols baked into numbers, typos in channel names, mixed yes/no formats, swapped dates, and a few extreme spend values. After cleaning, all **2,020 campaigns** remain with **12 tidy columns**, ready for analysis or dashboard use. The cleaned data lives in the notebook only (no export file was created).

## Who Would Use This Data?

- **Marketing manager / business analyst:** Compare ad spend and conversions across channels (TikTok, Facebook, Email, etc.) and plan future budgets.
- **ML engineer / data scientist:** Train models to predict conversions from impressions, clicks, and spend — useful for campaign optimization.
- **Web developer:** Power a marketing dashboard or campaign calendar in a full-stack app — show active campaigns, date ranges, and channel performance.
- **Finance team:** Audit ad spend totals and flag anomalies after currency normalization and outlier capping.

## About the Dataset

- **Source:** Implementation of the YouTube tutorial [Watch me Cleaning Data in minutes with Python](https://youtu.be/NeJKaolLQqU) by **Lore So What**. Loaded from `data/raw.csv`.
- **Size:** **2,020 rows × 12 columns** (raw) → **2,020 rows × 12 columns** (final, after adding a `season` column and removing a duplicate column)

| Column | What it means |
|--------|---------------|
| `campaign_id` | Unique campaign identifier (e.g. CMP-00001) |
| `campaign_name` | Descriptive name, often encoding quarter and season |
| `start_date` / `end_date` | When the campaign ran |
| `channel` | Ad platform (TikTok, Facebook, Email, Instagram, Google Ads) |
| `impressions` | How many times the ad was shown |
| `clicks` | How many times users clicked the ad |
| `spend` | Money spent on the campaign (USD) |
| `conversions` | Desired actions completed (e.g. sign-ups, purchases) |
| `active` | Whether the campaign is currently active (true/false) |
| `campaign_tag` | Short channel code (e.g. TI, FA, EM) |
| `season` | Extracted from campaign name (Summer, Winter, Launch, BlackFriday, etc.) |

## What Was Wrong With the Raw Data?

- **Messy column names:** Extra spaces (` Campaign_ID `, `Clicks `) and inconsistent casing.
- **Duplicate column:** Two columns both named `Clicks` — the second was mostly empty (40 values).
- **Currency in numbers:** 298 spend values included `$` symbols and were stored as text, not numbers.
- **Channel typos:** Variants like `Gogle`, `Facebok`, `Tik_Tok`, `Insta_gram`, `E-mail` instead of clean names.
- **Mixed boolean formats:** `Active` used Y, Yes, True, 1, No, False, 0 interchangeably.
- **Dates as text:** Start and end dates were strings in mixed formats.
- **Swapped dates:** 110 campaigns had an end date *before* the start date.
- **Spend outliers:** 6 campaigns showed $500,000 spend — far above the normal range.
- **Negative spend:** 19 campaigns had negative spend values.
- **Missing values:** 101 missing channels; 200 missing conversion counts (left unchanged).

## Cleaning Process

1. **Header cleaning** — Stripped whitespace, lowercased names, and replaced spaces with underscores so every column follows a consistent `snake_case` pattern.

2. **Currency cleaning on spend** — Removed `$` and other non-numeric characters from 298 rows, then converted spend to a proper number.

3. **Channel typo fixes** — Mapped known misspellings to their correct names (e.g. `Gogle` → Google Ads, `Facebok` → Facebook). Channel list went from 11 messy variants down to 5 clean platforms plus missing values.

4. **Boolean normalization on active** — Converted all yes/no variants (`Y`, `Yes`, `True`, `1`, etc.) into a simple true/false flag.

5. **Date parsing** — Converted start and end dates from text to proper dates, handling mixed formats (some MM/DD/YYYY, some YYYY-MM-DD).

6. **Duplicate column removal** — Dropped the extra empty `clicks` column, keeping the one with full data.

7. **Logical check: clicks vs impressions** — Verified that clicks never exceed impressions (an ad cannot get more clicks than views). **0 violations** found.

8. **Swapped date fix** — For 110 campaigns where the end date came before the start date, swapped the two values — likely a data-entry mistake.

9. **Outlier handling on spend (winsorizing)** — Used a statistical method (3× IQR above the 75th percentile) to identify 6 campaigns with implausibly high spend ($500,000 each plus one at $8,921.51). Capped all six to **$8,921.51** (the lowest among the outliers). Also converted **19 negative spend** values to their absolute values.

10. **Feature extraction: season** — Parsed campaign names like `Q4_Summer_CMP-00001` to pull out the season keyword (Summer, Winter, Launch, BlackFriday) into a new `season` column for easier grouping.

## Key Results

| Metric | Value |
|--------|-------|
| Rows before / after | 2,020 / 2,020 (none dropped) |
| Columns before / after | 12 / 12 |
| Campaign date range | Dec 2022 – Jan 2024 |
| Mean impressions | ~49,840 |
| Mean clicks | ~1,501 |
| Mean spend (after capping) | ~$3,095 |
| Mean conversions | ~186 (1,820 rows with data) |
| Spend range (after cleaning) | ~$20 – $8,921.51 |
| Date swaps corrected | 110 |
| Spend outliers capped | 6 |
| Negative spends fixed | 19 |

## Output Files

| File | Status |
|------|--------|
| `data/raw.csv` | Original messy input |
| `data/clean.csv` | **Not created** — cleaned data remains in the notebook only |

## Notebook

Full step-by-step code and outputs: [`02_data_cleaning.ipynb`](02_data_cleaning.ipynb)
