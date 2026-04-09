# Titanic Data Analysis with Pandas

## Project Overview

This project analyzes the Titanic dataset using pandas in Google Colab.
The objective is to explore the data, clean it, and extract insights about survival patterns.

---

## Environment Setup (Google Colab + Google Drive)

Mount Google Drive in Colab:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Set the file path:

```python
import pandas as pd

path = "/content/drive/MyDrive/Titanic-Dataset.csv"
df = pd.read_csv(path)
```

---

## Part 1: Custom Dataset

A dataset was created using a dictionary with:

* 5 columns: Name, Age, Gender, Score, Passed
* 15 rows
* Custom index labels (S1–S15)

This demonstrates how to build a DataFrame from scratch.

---

## Part 2: Titanic Dataset

### Step 1: Exploration

Basic exploration was done using:

* df.head()
* df.info()
* df.describe()

---

### Step 2: Data Cleaning

The dataset was cleaned as follows:

* Missing values in Age were filled using the median
* Missing values in Embarked were filled using the mode
* Cabin column was dropped due to excessive missing values
* Duplicate rows were removed

---

### Step 3: Data Analysis

Using groupby():

* Survival rate by gender
* Survival rate by passenger class
* Average age per class
* Survival rate by age group

---

### Step 4: Filtering

The following subsets were extracted:

* Female passengers who survived
* Children who survived
* First-class passengers who survived

---

## Key Insights

### Gender

Women had a much higher survival rate than men.
Roughly 7 out of 10 women survived, compared to about 2 out of 10 men.

---

### Class

Passenger class had a strong impact:

* First class had the highest survival rate
* Third class had the lowest

Passengers in higher classes had better access to lifeboats.

---

### Children

Children were more likely to survive than adults.
This suggests that evacuation efforts prioritized younger passengers.

---

### Highest Survival Group

The group with the highest survival rate was:

* Female
* First class
* Younger age

---

## Conclusion

Survival on the Titanic depended on multiple factors:

* Gender
* Social class
* Age

Women, children, and first-class passengers had the highest chances of survival, while third-class male passengers had the lowest.

---

## Requirements

Install pandas if needed:

```bash
pip install pandas
```

---

## How to Run in Colab

1. Upload the dataset to Google Drive
2. Open the notebook in Google Colab
3. Mount Google Drive
4. Run all cells step by step

