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
- Transaction Date *(datetime)*

As-is, each recorded data is of type string as perceived by pandas. Though, throughout this data cleaning process, I implemented the aformentioned expected data types except for `Quantity` for which I converted it to float.

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

## NaN Values

Originally the dataset contained two other dirty values which are UNKNOWN and ERROR. I have converted them to NaN values and the beneath NaN analysis considers this conversion.

||Transaction ID|Item|Quantity|Price Per Unit|Total Spent|Payment Method|Location|Transaction Date|
|---|---|---|---|---|---|---|---|---|
|NaN|0|969|479|533|502|**3178**|**3961**|460|
|NaN Percentage|0%|9.7%|4.8%|5.3%|5%|**31.8%**|**39.6%**|4.6%|

The column **Location** has the most nan values **3961** among the other columns.

Out of the total 10,000 rows, **6911 rows** -- meaning around 70% of them -- contain at least 1 nan value. This means, blindly droping rows with nan values for the sake of cleanliness is NOT an option here.

## Column specific detailed insight

### Item

The available items are **Cake**, **Coffee**, **Cookie**, **Juice**, **Salad**, **Sandwich**, **Smoothie** and **Tea**.

### Payment Method

The available payment methods are **Credit Card**, **Cash**, and **Digital Wallet**.

### Location

The available location values are **Takeaway** and **In-store**.

### Transaction Date

Mainly the dataset is about sales of items made in a day throughout the 365 days of the entire 2023 year.

## Inter-column Deduction

### Relation between `Item` and `Price Per Unit` (1st round check)

I mapped the missing values for `Price Per Unit` based on their valid `Item` values. In doing so, now, the NaN count for `Price Per Unit` **goes down from 533 to 54**.

However, mapping missing `Item` values based on their unit price is a bit tricky because there are two available items for a single price; A price of 3 for Cake and Juice. So I decided to leave the item value as NaN where the price is either 3 or 4. As a result, the NaN count **goes down from 969 to 501**.

### Relation among `Quantity`, `Price Per Unit`, and `Total Spent`

`Total Spent` is the product of `Quantity` and `Price Per Unit`. So, for records where `Total Spent` is nan while `Quantity` and `Price Per Unit` have valid values, we can deduce the true value for `Total Spent` by taking the product of the rest of the two. We can infer for such similar cases where `Quantity` or `Price Per Unit` are nan and find their value too. In doing so, here is a brief report on how many nan values were recovered:

- `Total Spent`: from 502 to 23 nans
- `Quantity`: from 479 to 23 nans
- `Price Per Unit`: from 54 to 6 nans

### Relation between `Item` and `Price Per Unit` (2nd round check)

With this second round check, I have managed to deduce **21 more values (501 - 480) for missing items**. This is possible because we got more valid price values in the quantity-price-total deduction step.

### Conclusion

After this Inter-column Deduction process, we now know that:

- the 480 missing values for items are guaranteed to be one of these: **Cake**, **Juice**, **Sandwich** or **Smoothie**.
- there exist no combination of quantity, unit price and total spent where only one of them is nan while the other two have valid values. In other words, it's either `[nan, nan, valid]` (in any permutation) or `[nan, nan, nan]` if there has to be nan in the combination of these three columns.