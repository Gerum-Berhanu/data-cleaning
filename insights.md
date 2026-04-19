# Data Cleaning Report

## General

There are 10,000 records (recorded data) with 8 fields/features/columns. 

Each recorded data is of type string.

## Null Values

||Transaction ID|Item|Quantity|Price Per Unit|Total Spent|Payment Method|Location|Transaction Date|
|---|---|---|---|---|---|---|---|---|
|Null|0|333|138|179|173|**2579**|**3265**|159|
|Null Percentage|0%|3.3%|1.4%|1.8%|1.7%|**25.8%**|**32.7%**|1.6%|

The column **Location** has the most null values **3265** among the other columns.

Out of the total 10,000 rows, **5450 rows** -- meaning more than half of them -- contain at least 1 null value. This means, blindfoldly droping rows with null values for the sake of cleanliness is NOT an option here.