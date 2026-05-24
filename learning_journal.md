# Data Cleaning Learning Journal

**Author:** Gerum Berhanu  
**Started:** May 2026  
**Goal:** Track the evolution of my data cleaning skills and mindset.

---

## Preface

When I started this journal, I was already into my fourth project "FIFA 21 Messy Data".

---

## May 24, 2026 | 04_fifa_21

So I decided to clean this FIFA 21 dataset, and one idea came to my mind which is that for every dataset to be cleaned, we need to know the purpose of cleaning it. 

- Is it for model training purpose, for which case I assume the annihilation of every null/undefined value is required (even if it takes dropping few rows).

- Is it for simple analytics, for which case I assume it's better to fill null/undefined values with some key term like "Unknown" instead of interpolation or dropping.

We choose our cleaning strategy based on the essence of the dataset. And that's the first need we need to ask our clients, in data cleaning, what their actual goal is.

So what is the goal of cleaning this FIFA 21 data? Since it is the data of professional football players, I assume a football game company, one like FIFA, would want to implement it in their upcoming football game. In this case, no such thing as "Unkown" is needed. No dropping rows, 100% interpolation.