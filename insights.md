# Data Cleaning Report

## Overview

There are 10,000 records (recorded data) with 8 fields/columns. The 8 fields, with their **expected** data types are:
- Transaction ID *(str)*
- Item *(str)*
- Quantity *(int)*
- Price Per Unit *(float)*
- Total Spent *(float)*
- Payment Method *(str)*
- Location *(str)*
- Transaction Date *(str)*

As-is, each recorded data is of type string as perceived by pandas.

## Null Values

||Transaction ID|Item|Quantity|Price Per Unit|Total Spent|Payment Method|Location|Transaction Date|
|---|---|---|---|---|---|---|---|---|
|Null|0|333|138|179|173|**2579**|**3265**|159|
|Null Percentage|0%|3.3%|1.4%|1.8%|1.7%|**25.8%**|**32.7%**|1.6%|

The column **Location** has the most null values **3265** among the other columns.

Out of the total 10,000 rows, **5450 rows** -- meaning more than half of them -- contain at least 1 null value. This means, blindfoldly droping rows with null values for the sake of cleanliness is NOT an option here.

## Column specific detailed insight

### Item

Unwanted (dirty) values are: ERROR, UNKNOWN, nan

| Item | Count |
| --- | --- |
| Juice | 1171 |
| Coffee | 1165 |
| Salad | 1148 |
| Cake | 1139 |
| Sandwich | 1131 |
| Smoothie | 1096 |
| Cookie | 1092 |
| Tea | 1089 |
| *UNKNOWN* | *344* |
| *nan* | *333* |
| *ERROR* | *292* |

**Total unwanted values: 969**

There are no significant differences among the orders of the items. Meaning, there is no hidden pattern to discover.

### Quantity

Unwanted (dirty) values are: ERROR, UNKNOWN, nan

| Quantity | Count |
| --- | --- |
| 5 | 2013 |
| 2 | 1974 |
| 4 | 1863 |
| 3 | 1849 |
| 1 | 1822 |
| *UNKNOWN* | *171* |
| *ERROR* | *170* |
| *nan* | *138* |

**Total unwanted values: 479**
**Minimum quantity: 1**
**Maximum quantity: 5**

> I think I should stop saving `value_counts` because more than half of the dataset contains null values. Quantity 5 has 2013 appearances, including those whose item is UNKOWN or whose price is nan. So, I don't think there would lie any meaningful info in keeping the counts.

### Price Per Unit

*(provided information)* Prices for menu items are consistent but may have missing or incorrect values introduced. The dataset includes the following menu items with their respective price ranges: 

|Item|Price($)|
|---|---|
|Coffee|2|
|Tea|1.5|
|Sandwich|4|
|Salad|5|
|Cake|3|
|Cookie|1|
|Smoothie|4|
|Juice|3|

### Total Spent

For records where `Total Spent` is null while `Quantity` and `Price Per Unit` are valid values, we recover (deduce the value of) `Total Spent` by multiplying the two valid columns. In doing so, the initial **502 NaNs** are reduced to **40 NaNs**.

Applying this for `Quantity` and `Price Per Unit`, there respective initial NaN values and reduced ones are:

- `Quantity`: from **479** to **38**
- `Price Per Unit`: from **533** to **38**
- `Total Spent`: from **502** to **40**

Overall, by doing this correlating process, **1398 rows (individual datapoints)** were affected; those with a NaN value in either of the three columns are deduced to a valid form.

### Payment Method

The available payment methods are **Credit Card**, **Cash**, and **Digital Wallet**.

### Location

The available location values are **Takeaway** and **In-store**.

### Transaction Date

Turns out, the dataset is about transactions made each day throughout the 365 days of the entire 2023 year.

- **Minimum** sales happened in a day is **14** on **Feb 17**, **Mar 11**, and **Jul 22**.
- **Maximum** sales happened in a day is **40** on **Feb 6**, and **Jun 16**.
- On average (median), **26 sales** were made in a day.