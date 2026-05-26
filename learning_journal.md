# Data Cleaning Learning Journal

**Author:** Gerum Berhanu  
**Started:** May 2026  
**Goal:** Track the evolution of my data cleaning skills and mindset.

---

## Preface

When I started this journal, I was already into my fourth project "FIFA 21 Messy Data".

---

## May 24, 2026 | 04_fifa_21

I decided to clean this FIFA 21 dataset, and one idea came to my mind which is that for every dataset to be cleaned, we need to know the purpose of cleaning it. 

- Is it for model training purpose, for which case I assume the annihilation of every null/undefined value is required (even if it takes dropping few rows).

- Is it for simple analytics, for which case I assume it's better to fill null/undefined values with some key term like "Unknown" instead of interpolation or dropping.

We choose our cleaning strategy based on the essence of the dataset. And that's the first need we need to ask our clients, in data cleaning, what their actual goal is.

So what is the goal of cleaning this FIFA 21 data? Since it is the data of professional football players, I assume a football game company, one like FIFA, would want to implement it in their upcoming football game. In this case, no such thing as "Unkown" is needed. No dropping rows, 100% interpolation.

Also, I used to do column-specific explorations. But now that I'm working on a dataset with 77 columns, I gotta change my habit to bundled explorations.

## May 25, 2026 | 04_fifa_21

Mindblowing thing I've learned just right now. If you find a column with so much of varying formats where it is near impossible to standardize the column without data loss, you can create other new columns representing the variety here. Let's see how Gemini brilliantly explained it to me:

---

In data science, trying to force the `Contract` column into a single format would be a huge headache because the column contains **three entirely different concepts of time and employment** mixed together:
1. A date range (`2018 ~ 2024`)
2. A specific date plus a status (`Jun 30, 2021 On Loan`)
3. A categorical status (`Free`)

You can't convert that into a simple `datetime` or `integer` column without losing information.

This approach is a mix of **Feature Extraction** and **Data Unpacking**. 

When a raw column is a "garbage drawer" of mixed information, the best practice is *never* to try and "fix" the column in place. Instead, you treat the messy column as a **source of truth** and extract what you need into clean, perfectly formatted *new* columns. 

Here is how this method typically plays out for a column like `Contract`:

**1. Create a Categorical Column (What we just did)**
First, you extract the *status* into a `Contract_Type` column (`Permanent`, `On Loan`, `Free`). This allows you to easily filter the dataset later (e.g., "Show me only players on loan whose loan expires this year").

**2. Extract the Numbers into New Columns**
Next, you write a script to look *only* at the "Permanent" contracts, split that `~` symbol, and create two brand new numeric columns:
*   `Contract_Start_Year` (e.g., 2018)
*   `Contract_End_Year` (e.g., 2024)

**3. Leave the Exceptions Null (NaN)**
For players who are "Free" or "On Loan", their `Contract_Start_Year` and `Contract_End_Year` will just be blank (`NaN`/Null). That is perfectly fine! In fact, it's correct data modeling. If they are on loan, you simply look at the `Loan Date End` column instead.

**4. Drop the Original Column**
Once you have squeezed all the useful information out of the original `Contract` column and put it into your new, clean columns (`Contract_Type`, `Contract_Start_Year`, `Contract_End_Year`), the original `Contract` column is virtually useless. At the very end of your script, you can confidently write `df = df.drop(columns=['Contract'])`.

By breaking one messy column into several distinct, single-purpose columns, your data becomes incredibly easy to analyze and visualize later!

---

I've just learned that values can be left as null if their absence is explained by other columns.