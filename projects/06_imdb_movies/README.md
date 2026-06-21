# IMDb Top Netflix Movies and TV Shows — Data Cleaning Report

## At a Glance

This dataset lists **9,999 movies and TV shows** from Netflix's IMDb catalog — titles, years, genres, ratings, cast, runtime, and box-office gross. The raw file had inconsistent formatting (Unicode dashes in years, dollar amounts as text, comma-separated vote counts), **857 duplicate-looking rows**, and a combined "stars" field mixing directors and actors. After cleaning, all **9,999 titles** remain with **12 structured columns** including new fields for content type, start/end years, and separated directors and cast.

## Who Would Use This Data?

- **Movie buff / content curator:** Browse a clean catalog of Netflix titles with ratings, genres, and runtime for recommendations.
- **ML engineer / data scientist:** Train models to predict IMDb ratings or popularity (votes) from genre, runtime, and year features — 460 titles have box-office gross for revenue-related models.
- **Web developer:** Build a Netflix-style discovery app or REST API serving movie/series metadata with parsed years and split cast/director fields.
- **Streaming platform analyst:** Compare movie vs series distributions, rating trends by decade, and genre popularity.

## About the Dataset

- **Source:** [Kaggle — Movies Dataset for Feature Extraction/Prediction](https://www.kaggle.com/datasets/bharatnatrayn/movies-dataset-for-feature-extracion-prediction?select=movies.csv). Loaded from `data/raw.csv`.
- **Size:** **9,999 rows × 9 columns** (raw) → **9,999 rows × 12 columns** (final)

| Column | What it means |
|--------|---------------|
| `movies` | Title of the movie or TV show |
| `type` | `Movie` or `Series` (derived from year format) |
| `start_year` | First year of release or series start |
| `end_year` | Series end year (empty for movies and ongoing series) |
| `genre` | Comma-separated genres (Action, Drama, Comedy, etc.) |
| `rating` | IMDb rating (1.0 – 9.9) |
| `one_line` | Short plot summary |
| `directors` | Director name(s), extracted from the original stars field |
| `stars` | Cast/actor names only (directors removed) |
| `votes` | Number of IMDb user votes |
| `runtime` | Length in minutes |
| `gross` | US box-office gross in dollars (only 460 titles have this) |

## What Was Wrong With the Raw Data?

- **Extra whitespace:** Tabs, newlines, and multiple spaces in text fields.
- **Inconsistent column names:** Mixed casing (`MOVIES`, `RunTime`, `ONE-LINE`).
- **857 duplicate rows:** Identical title + plot summary pairs — but no unique ID or series/episode metadata to judge whether they are true duplicates.
- **Messy year formats:** Unicode dashes (–, —), letters, and invalid patterns like `(III)` or `(2021 TV Special)` mixed with valid `(2021)` or `(2010-2022)`.
- **Gross as text:** Values like `$75.47M` instead of numeric dollars.
- **Votes with commas:** Numbers like `1,713,028` stored as text.
- **Combined stars field:** Directors and actors listed together in one column.
- **Heavy missing data:** Gross missing for 95% of titles; runtime missing for ~30%; rating and votes missing for ~18%.

## Cleaning Process

1. **Whitespace cleaning** — Normalized all text columns: replaced tabs/newlines with spaces, collapsed multiple spaces, trimmed edges.

2. **Column rename** — Lowercased, stripped spaces, replaced hyphens with underscores (`ONE-LINE` → `one_line`, `RunTime` → `runtime`).

3. **Duplicate decision** — Found **857 rows** duplicate on `(movies, one_line)`. **Kept all rows** — without a unique ID or series/episode type, removing them could accidentally delete legitimately different entries.

4. **Year formatting** — Replaced Unicode en/em dashes with ASCII hyphens, stripped letters and spaces, kept only valid patterns: `(YYYY)` for movies or `(YYYY-YYYY)` / `(YYYY-)` for series. Invalid values became missing. Year missing count went from **644 to 748** (+104 improper values removed).

5. **Gross conversion** — All **460** valid gross values matched `$X.XXM` format. Parsed to float dollars (e.g. `$75.47M` → 75,470,000).

6. **Votes conversion** — Removed commas and converted to integer (e.g. `1,713,028` → 1713028).

7. **ROMI checks:**
   - **Relation:** No calculable relationships between columns.
   - **Outlier:** No numeric outliers flagged.
   - **Mismatch:** **38 movie titles** appear with more than one year value (77 unique title–year pairs). Judged to be **different productions sharing a name** or maybe **remakes**, not data errors.
   - **Interpolation:** Not needed — missing ratings, runtime, and gross were left as-is.

8. **Feature engineering:**
   - **`type`** — Hyphen in year string → `Series`; single year → `Movie`.
   - **`start_year` / `end_year`** — Extracted from the year string (e.g. `(2010-2022)` → start 2010, end 2022).
   - **`directors` / `stars` split** — Parsed the combined stars text: first name(s) before a comma pattern become directors; remaining names become cast-only stars.
   - **Dropped raw `year`** — Replaced by `type`, `start_year`, and `end_year`.

9. **Column reordering** — Final order: movies, type, start_year, end_year, genre, rating, one_line, directors, stars, votes, runtime, gross.

## Key Results

| Metric | Value |
|--------|-------|
| Rows before / after | 9,999 / 9,999 (none dropped) |
| Columns before / after | 9 / 12 |
| Duplicates kept (by decision) | 857 |
| Mean IMDb rating | 6.92 (range 1.1 – 9.9) |
| Mean runtime | 68.7 minutes (max 853 — likely a long-running series) |
| Mean votes | ~15,124 (max ~1.7M) |
| Titles with gross data | 460 (mean ~\$43.7M, max ~\$504M) |
| Type populated | 9,251 (748 missing due to invalid years) |
| Series with end year | 1,388 |
| Directors extracted | 6,353 |
| Cast (stars) extracted | 8,615 |
| Start year range | 1932 – 2023 (median 2018) |

**Missing values in final dataset:**

| Column | Missing |
|--------|---------|
| type / start_year | 748 |
| end_year | 8,611 |
| genre | 80 |
| rating / votes | 1,820 each |
| directors | 3,646 |
| stars | 1,384 |
| runtime | 2,958 |
| gross | 9,539 |

## Output Files

| File | Description |
|------|-------------|
| `data/raw.csv` | Original messy input |
| `data/clean.csv` | Final cleaned dataset (9,999 rows × 12 columns) |
| `data/clean.xlsx` | Same data in Excel format (sheet: `movies`) |

## Notebook

Full step-by-step code and outputs: [`06_data_cleaning.ipynb`](06_data_cleaning.ipynb)
