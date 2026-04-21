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

From the recorded data, the maximum number of order quantity for an item is 5.