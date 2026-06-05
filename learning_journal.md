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

## May 26, 2026 | 04_fifa_21

Do you know why it takes me so long on a single cleaning step? in other words, why can't I have a smooth, fast, and continuous workflow? Why do I need to stop at a step and think longer than it should take? Well obviously lack of experience it is. But I can't waste any more time till I get experienced. What's the shortcut to get there? The answer lies in identifying what the so-called "experience" would teach me; probably having clear guidelines. **Knowing where to start and what follows is the key to a blitzing workflow.**

Below is the reflection of Gemini 3.1 Pro on the above statement.

---

**The 5-Step Data Cleaning Assembly Line**

**1. The High-Level Sweep (Structure & Standardization)**

**Goal:** Make the dataset easy to handle before doing deep work.
**Action:** Standardize all column names (lowercase, no spaces).
**Action:** Drop entirely empty rows and columns.
**Action:** Check for and remove duplicate rows.

**2. Type Conversion & Consistency (The Parsing Phase)**

**Goal:** Ensure Python sees the data the way you see it.
**Action:** Convert dates to datetime.
**Action:** Strip currencies/symbols (like € or lbs) and cast to float/int.
**Action:** Standardize categorical text (e.g., lowercase everything, strip trailing whitespaces).

**3. Feature Extraction (The "Unpacking" Phase)**

**Goal:** Break down garbage-drawer columns.
**Action:** This is exactly what you did with the Contract column! Split mixed data into multiple, single-purpose columns.

**4. The Missing Data Strategy (Imputation)**

**Goal:** Handle the nulls. (Doing this AFTER extraction and type conversion is crucial, because those previous steps often reveal or create new nulls!).
**Action:** Revisit your rule from May 24 (What is the goal? Model training vs Analytics?).
**Action:** Drop, impute (mean/median/mode), or fill with "Unknown".

**5. Sanity Checks & Outliers (The Logic Phase)**

**Goal:** Catch things that are formatted correctly but logically impossible.
**Action:** describe() to check min/max. Are there players weighing 5kg? Are there negative salaries?
**Action:** Use Regex to find weird name formats (like the "jjjjjj" thought you had!).

If you paste a checklist like this at the top of every new Jupyter Notebook, you will never get stuck wondering "what's next?" again. You just move to the next item on the assembly line.

---

I've finished cleaning the FIFA 21 dataset (though I may check back somethings). I didn't write an overall report because cmon I don't expect myself to learn everything at once. Clean report writing comes when I master the raw cleaning process.

## May 29, 2026 | 05_ecommerce_sales

The `duplicated` method of dataframes spares the first occurrences.

---

I found a case where expected column relations are broken. For example, usually $\text{Quantity} \times \text{Price} = \text{Total}$. In this `05_ecommerce_sales` project, I found 10 occurrences where their is a noticable inequality to the total amount. However, `Total` may include tax, discounts, or refunds. Assuming this, I chose to keep these inequalities as-is. Now I'm reminded to ask the client for such crucial information about the dataset and column relations.

## June 5, 2026 | 06_imdb_movies

Two rows which are exactly identical, except for a single entry where one row contains NA while the other has a valid value, are considered duplicates (in pandas). This raises a whole new issue in handling duplicates.

Case A\) If two rows are exactly identical in every aspect, we drop one of them.

Case B\) For two identical rows where one of them contain more NA values but not any value that isn't in the other row, we simply drop it.

Case C\) When two identical rows contain NA in different entries, they are still considered duplicates in pandas. In such cases, the right thing to do is to merge the two rows. Otherwise, dropping one of them at first glance means losing a potential valid data.

The challenging (new) part of this path is in the merging of rows (Case C). How to achieve that?