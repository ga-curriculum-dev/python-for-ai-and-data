# Lab: Cleaning and Transforming Data in Pandas

## Overview

In this lab, you will work with a realistic dataset that requires cleaning before it can be analysed.

Using **Pandas DataFrames**, you will inspect data quality, handle missing values and duplicates, standardise formats, and produce an **analysis-ready dataset** that can be reused in later modules.

This lab builds practical data-wrangling skills used across analytics, data science, and machine learning workflows.

---

## Learning Objectives

By completing this lab, you will:

- Load raw data into a Pandas DataFrame
- Inspect dataset structure and data quality
- Handle missing values and duplicate records
- Standardise column names and text formats
- Save a cleaned dataset for reuse
- Document cleaning decisions clearly and reproducibly

---

## Project Structure

Your project should follow this structure:

```text
Lab_Cleaning_and_Transforming_Data_in_Pandas/
│
├── data/
│   └── raw/sales_sample.csv
│   └── processed/
│
├── notebooks/
│   └── module5_pandas_wrangling.ipynb
│
├── output/
│   └── .gitkeep
│
├── solutions/
│   └── module5_pandas_wrangling_solution.ipynb
│
└── README.md
```
> Note: The dataset is provided in `data/raw/sales_sample.csv`. The `output/` folder is included for any saved outputs you create during the lab.

## How to Work Through the Lab

Follow the steps below **in order**.  
Run each cell as you go to confirm your code works as expected.

---

### 1. Set Up Your Notebook

- Open the starter notebook:  
  `notebooks/module5_pandas_wrangling.ipynb`

- Import **Pandas** and any other required libraries

- Load the dataset from:  
  `data/raw/sales_sample.csv`

---

### 2. Inspect Data Quality

Before cleaning, inspect the dataset to understand its structure.

Use methods such as:

```python
df.head()
df.info()
df.describe()
df.isna().sum()
```
Focus on identifying:

- Missing values  
- Unexpected data types  
- Duplicate rows  
- Inconsistent formatting  

---

### 3. Handle Missing Data and Duplicates

Apply appropriate cleaning strategies, such as:

- Removing rows with critical missing values  
- Filling missing values using context-appropriate statistics  
- Removing duplicate records  

**Example:**

```python
df = df.drop_duplicates()
df = df.fillna(df.mean(numeric_only=True))
```
There is no single *“correct”* cleaning strategy — decisions should be justified based on context.

---

### 4. Transform and Standardise Data

Prepare the dataset for analysis by standardising formats and values.

Examples include:

- Renaming columns for consistency  
- Converting data types  
- Normalising text values  
- Creating derived columns if needed  

```python
df.columns = df.columns.str.lower()
df["category"] = df["category"].str.strip().str.lower()
```
### 5. Save the Cleaned Dataset

Once your data is cleaned:

- Save the processed dataset to:  
  `data/processed/`

- Use a clear filename indicating the data is cleaned

```python
df.to_csv("data/processed/clean_sales_data.csv", index=False)
```
### 6. Document Your Work

In your notebook, add markdown cells explaining:

- How the data was loaded  
- What data quality issues were found  
- Which cleaning steps were applied  
- Why specific decisions were made  

In your notebook, clearly document:

- The purpose of the lab  
- The input dataset  
- The cleaned output produced  

Clear documentation is essential for reproducible analytics workflows.

---
## Version Control and Submission

From your project folder, run:

```bash
git init
git add .
git commit -m "Clean and transform customer data using Pandas"
```
Create a new repository on GitHub and push your work:

```bash
git branch -M main
git push -u origin main
```
---
## Tips for Success

- Inspect data before modifying it  
- Avoid unnecessary complexity  
- Justify cleaning decisions in markdown cells  
- Keep raw and processed data separate  
- Use clear, readable code  

---

## Deliverables

Your final submission should include:

- A completed Jupyter Notebook with code and explanations  
- Cleaned data saved to `data/processed/`  
- Clear documentation of cleaning steps  
- A GitHub repository containing all project files  

---

## Additional Resources

- **Pandas Documentation**  
  https://pandas.pydata.org/docs/
- **Pandas User Guide — Missing Data**  
  https://pandas.pydata.org/docs/user_guide/missing_data.html
- **Real Python — Pandas Tutorials**  
  https://realpython.com/pandas-dataframe/
- **GitHub Documentation**  
  https://docs.github.com


