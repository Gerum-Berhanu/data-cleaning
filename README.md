# Data Cleaning Portfolio

## About

Hi! I'm **Gerum Berhanu**. This repo is my **data cleaning portfolio**. I take messy CSV files and turn them into datasets you can fully trust, with a clear note on every choice I make.

Here's what's inside:

- **Six projects so far** (01–06), each with a different kind of dirty data (more to come)
- A **plain-language report** in every project folder. No need to read code
- **Jupyter notebooks** you can re-run step by step
- **Clean exports** (`clean.csv`, and Excel where it fits)

The projects are numbered in order on purpose. Early ones show where I started; later ones show where I am now. New projects will keep that sequence and extend the same ideas.

---

## Featured Project: IMDb Movies

> **⭐ [06. IMDb Top Netflix Movies and TV Shows](projects/06_imdb_movies/README.md)**
>
> **9,999 titles | 12 columns | ROMI + new fields | CSV + Excel**

This is my favorite work so far. It shows the full way I clean data today:

- **Clear workflow**: overview, before/after samples, export at the end
- **ROMI**: check Relations, Outliers, Mismatches, then decide on Interpolation (fill or skip)
- **Feature Engineering**: split year into Movie/Series, start year, end year; split directors from cast
- **Real decisions**: kept 857 duplicate-looking rows because there is no safe way to merge them without IDs
- **No fake data**: box office gross exists for only 460 titles; the rest stay blank

Full report: **[Project 06 →](projects/06_imdb_movies/README.md)**

---

## How I Use Regex

**Regex** (regular expressions) is pattern matching for text. I use it in almost every project. This is because messy data is usually messy *text*: wrong symbols, mixed formats, typos hiding in plain sight.

| What regex helps with | Example from this repo |
|-----------------------|------------------------|
| **Spot bad formats** | Find spend values with `$` (Marketing), dates that aren't `MM/DD/YYYY` (E-commerce), years that aren't `(2021)` or `(2010-2022)` (IMDb) |
| **Strip junk** | Remove `$` and letters from money fields; pull `★` off star ratings (FIFA) |
| **Check rules** | Valid email shape (Employee), phone `XXX-XXX-XXXX`, SoFIFA player URLs (FIFA) |
| **Pull out parts** | Season name from campaign title `Q4_Summer_CMP-00001` (Marketing); director vs cast from one `stars` column (IMDb) |
| **Split combined fields** | Department and region from `Finance-Texas` (Employee); height in `6'2"` vs `182cm` (FIFA) |

I combine regex with pandas (`.str.match`, `.str.contains`, `.str.replace`) so I can flag bad rows, fix formats in bulk, and only then decide what to drop, fill, or leave alone. Regex finds the mess; the cleaning rules decide what to do about it.

---

## How My Approach Grew (Projects 01 → 06 …)

Each project adds one idea I still use. Together they're one story.

| Step | Project | Main idea |
|------|---------|-----------|
| Start | [01 — Cafe Sales](projects/01_cafe_sales/README.md) | Use logic between columns when you can; only guess when you must |
| Build | [02 — Marketing Campaign](projects/02_marketing_campaign/README.md) | Same steps every time: names → types → typos → logic checks → outliers |
| Context | [03 — Employee Metrics](projects/03_employee_metrics/README.md) | Fill gaps using groups (e.g. median salary by department + region) |
| Purpose | [04 — FIFA 21](projects/04_fifa_21/README.md) | Clean for *why* the client needs the data; split mixed columns instead of forcing one shape |
| Framework | [05 — E-Commerce Sales](projects/05_ecommerce_sales/README.md) | ROMI checklist; save bad rows separately instead of deleting quietly |
| Latest | [06 — IMDb Movies ⭐](projects/06_imdb_movies/README.md) | Full ROMI + new columns + written trade-offs |

I also write in a **[learning journal](learning_journal.md)**,  dated notes on what I learned and how my workflow changed.

---

## Core Principles

1. **Know the goal**: Training a model, a dashboard, and a website need different kinds of "clean."
2. **Fix what you can prove**: e.g. Total = Quantity × Price. Fill gaps only when you have to, and say so.
3. **Split messy columns**: One column with mixed info (contracts, years, cast lists) becomes several clean ones.
4. **Blank is OK sometimes**: Missing gross on 9,500 movies is honest; making up numbers is not.
5. **Write it down**: Every project has a README anyone can read.
6. **Keep a paper trail**: Bad orders go to a reject list.

---

## All Projects (So Far)

New rows will appear here as I publish more work. Same layout every time: `projects/NN_name/`, notebook, README, and `data/`.

| # | Project | Data | Raw → Final | Report |
|---|---------|------|-------------|--------|
| 01 | Cafe Sales | Café sales | 10,000 → 9,064 × 8 | [README](projects/01_cafe_sales/README.md) |
| 02 | Marketing Campaign | Ad campaigns | 2,020 × 12 | [README](projects/02_marketing_campaign/README.md) |
| 03 | Employee Metrics | HR records | 1,020 × 12 | [README](projects/03_employee_metrics/README.md) |
| 04 | FIFA 21 | Player stats | 18,979 × 78 | [README](projects/04_fifa_21/README.md) |
| 05 | E-Commerce Sales | Online orders | 103 → 95 × 11 | [README](projects/05_ecommerce_sales/README.md) |
| 06 | **IMDb Movies ⭐** | Netflix titles | 9,999 × 12 | [README](projects/06_imdb_movies/README.md) |

Each folder has `NN_data_cleaning.ipynb` (notebook) and `README.md` (report).

**Data files:** CSVs live in each project's `data/` folder. That folder is ignored by git, so run the download script below after you clone.

---

## Getting Started

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
python load_dataset.py --check
```

Open a notebook in Jupyter or VS Code, e.g. `projects/06_imdb_movies/06_data_cleaning.ipynb`.

**Downloads:** [`load_dataset.py`](load_dataset.py) gets Kaggle data for projects **01, 03, 04, 05, 06**. For **02** (Marketing), use the [YouTube tutorial](https://youtu.be/NeJKaolLQqU) data and put `raw.csv` in `projects/02_marketing_campaign/data/`.

---

## Tech Stack

| Tool | Use |
|------|-----|
| Python | Main language |
| pandas / numpy | Cleaning and numbers |
| Jupyter | Notebooks |
| kagglehub | Download datasets |
| openpyxl | Excel export (project 06) |

See [`requirements.txt`](requirements.txt) for the full list.

---

## Quick Links

- **Featured report:** [06 IMDb Movies](projects/06_imdb_movies/README.md)
- **Learning journal:** [learning_journal.md](learning_journal.md)
- **Download datasets:** [load_dataset.py](load_dataset.py)
