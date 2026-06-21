# Employee Metrics — Data Cleaning Report

## At a Glance

This dataset holds **1,020 employee records** from a fictional company — names, departments, salaries, performance scores, and more. The raw file had awkward column names, combined fields that needed splitting, phone numbers stored as negative integers, and **211 missing ages** and **24 missing salaries**. After cleaning, every employee has complete age and salary values (filled using group medians), properly formatted phone numbers, and a logical column layout. All **1,020 rows** were kept.

## Who Would Use This Data?

- **HR manager / people ops:** Track headcount by department and region, monitor performance distribution, and review remote-work adoption.
- **ML engineer / data scientist:** Build attrition or performance prediction models using department, region, salary, and tenure features.
- **Web developer:** Populate an internal employee directory or HR portal API with clean, consistently formatted contact and org data.
- **Compensation analyst:** Compare salary ranges across departments and regions after missing values are sensibly filled.

## About the Dataset

- **Source:** [Kaggle — Messy Employee Dataset](https://www.kaggle.com/datasets/desolution01/messy-employee-dataset). Loaded from `data/raw.csv`.
- **Size:** **1,020 rows × 12 columns** (raw) → **1,020 rows × 12 columns** (final)

| Column | What it means |
|--------|---------------|
| `employee_id` | Unique ID (EMP1000–EMP2019) |
| `full_name` | Employee's first and last name combined |
| `age` | Age in years |
| `email` | Work email address |
| `phone` | Phone number (XXX-XXX-XXXX format) |
| `department` | Team: Admin, Cloud Tech, DevOps, Finance, HR, or Sales |
| `region` | US state/region: California, Florida, Illinois, Nevada, New York, or Texas |
| `join_date` | Date the employee joined the company |
| `salary` | Annual salary in USD |
| `status` | Employment status: Active, Inactive, or Pending |
| `performance_score` | Rating: Poor, Average, Good, or Excellent |
| `remote_work` | Whether the employee works remotely (true/false) |

## What Was Wrong With the Raw Data?

- **Inconsistent column names:** Mixed casing and underscores (`Employee_ID`, `Department_Region`).
- **Combined field:** `Department_Region` merged department and region into one string (e.g. `Finance-Texas`).
- **Separate name columns:** First and last names were in two columns instead of one full name.
- **Missing ages:** 211 rows had no age — too many to simply delete.
- **Missing salaries:** 24 rows had no salary.
- **Phone numbers as negative integers:** Stored as large negative numbers (e.g. `-1651623197`) instead of formatted phone strings.
- **Extra whitespace:** Leading/trailing spaces on text fields.

## Cleaning Process

1. **Header normalization** — Lowercased column names, stripped spaces, replaced spaces with underscores.

2. **Whitespace trimming** — Removed extra spaces from all text columns.

3. **Duplicate check** — Found **0 duplicate rows**; none removed.

4. **Name merging** — Combined `first_name` and `last_name` into a single `full_name` column; dropped the originals.

5. **Email validation** — All **1,020 emails** matched a valid format. The dataset uses 8 first names × 8 last names = 64 unique email patterns across 1,020 employees.

6. **Department/region split** — Split `Department_Region` into separate `department` and `region` columns. Six departments × six regions = **36 unique combinations**.

7. **Join date parsing** — Converted text dates to proper datetime values. **0 missing dates** after conversion. Date range: **2020-01-01 to 2024-12-29**.

8. **Phone formatting** — Took absolute values of negative numbers, zero-padded to 10 digits, and formatted as `XXX-XXX-XXXX`. **0 invalid formats** after cleaning.

9. **Column reordering** — Arranged columns in a logical HR order: ID → name → contact → org → dates → compensation → status.

10. **Age imputation (filling missing values)** — For the **211 missing ages**, filled each gap with the **median age of employees in the same department and region**. Rationale: people in similar roles and locations tend to share demographic patterns. Result: **0 missing ages**.

11. **Salary imputation** — Explored whether performance score could predict salary, but performance is volatile and doesn't reliably scale with pay. Instead, filled **24 missing salaries** with the **median salary by department and region** — a safer, outlier-resistant approach. Result: **0 missing salaries**.

12. **Final duplicate check** — Confirmed **0 duplicates** before export.

## Key Results

| Metric | Value |
|--------|-------|
| Rows before / after | 1,020 / 1,020 |
| Ages imputed | 211 → 0 missing |
| Salaries imputed | 24 → 0 missing |
| Mean salary | ~$85,155 |
| Salary range | $50,047 – $119,972 |
| Status split | Pending 356, Active 352, Inactive 312 |
| Performance split | Good 270, Average 267, Excellent 267, Poor 216 |
| Remote work | True 513, False 507 |
| Join date range | Jan 2020 – Dec 2024 |

## Output Files

| File | Description |
|------|-------------|
| `data/raw.csv` | Original messy input |
| `data/clean.csv` | Final cleaned dataset (1,020 rows, dates as YYYY-MM-DD) |

## Notebook

Full step-by-step code and outputs: [`03_data_cleaning.ipynb`](03_data_cleaning.ipynb)
