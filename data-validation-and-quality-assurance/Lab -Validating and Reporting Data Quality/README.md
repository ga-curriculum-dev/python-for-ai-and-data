# Lab: Validating and Reporting Data Quality  
**Module 9 — Data Validation and Quality Assurance**

**Estimated Time:** 30–40 minutes

---

## Introduction

In this lab, you will apply **systematic data-validation and quality-assurance techniques** to a dataset before any correlation, regression, or statistical analysis is performed.

Rather than assuming data is “good enough,” you will make **data-quality expectations explicit** using assertions, structured checks, and clear documentation.

This lab reinforces professional practices for producing **audit-ready, reproducible datasets** that can be trusted in downstream analytical workflows.

---

## Learning Objectives

By the end of this lab, you will be able to:

- Apply data-quality checks and assertions to validate a dataset  
- Detect missing values, duplicates, anomalies, and inconsistencies  
- Distinguish between automated validation and manual analytical judgement  
- Generate and document a reproducible data-quality report  
- Version validated outputs using Git and GitHub  

---

## Tools & Libraries

You will use:

- Python 3  
- Jupyter Notebook  
- Pandas  
- NumPy  
- Git & GitHub  

---

## Project Structure

Your project should follow the structure below:

```text
data-validation-lab/
│
├── data/
│   └── dataset.csv
│
├── notebooks/
│   └── data_quality_validation_lab.ipynb
│
├── output/
│   └── validated_dataset.csv
│
├── README.md
└── .git/
```
---
## Folder Descriptions

- **data/**  
  Contains the original dataset provided for the lab.  
  This file represents the source data and must not be overwritten.

- **notebooks/**  
  Contains the Jupyter Notebook where you implement data-quality checks,  
  assertions, and markdown documentation.

- **output/**  
  Contains files generated during the lab, including the validated dataset  
  and any outputs created as part of your data-quality workflow.

Keeping source data separate from outputs supports reproducibility,  
auditability, and professional analytics practices.

---

## How to Work Through the Lab

Follow the steps below in order.  
Run each cell as you go and read the markdown instructions carefully.

---

### 1. Set Up Your Notebook

Open the starter notebook:

```text
notebooks/data_quality_validation_lab.ipynb
```
In the setup section, you will:

- Import required libraries  
- Load the dataset from `data/dataset.csv`  
- Perform an initial inspection of structure and content  

---

## 2. Inspect Data Quality

Before applying any validation rules, explore the dataset to identify potential issues.

You will:

- Check dataset shape and data types  
- Inspect missing values  
- Identify potential duplicates  
- Look for unexpected ranges or values  

This step establishes **baseline expectations** for your validation logic.

---

## 3. Apply Data-Quality Checks and Assertions

Implement explicit checks to validate assumptions, such as:

- Required columns are present  
- Numeric values fall within valid ranges  
- Critical fields are not missing  
- Duplicate records are detected  

Use assertions or conditional checks to make these expectations explicit.

Focus on **why each check exists**, not just how it is implemented.

---

## 4. Handle Errors, Anomalies, and Inconsistencies

After detecting issues, decide how to handle them.

You may:

- Remove invalid records  
- Flag anomalies for review  
- Document unresolved issues  

Not all problems should be “fixed” automatically — some require **analytical judgement**.

Clearly document any decisions made.

---

## 5. Generate a Data-Quality Report

In markdown cells, document:

- What issues were detected  
- Which checks were automated  
- Which issues required manual judgement  
- Any assumptions or limitations  

This report should be understandable to a teammate reviewing your work later.

---

## 6. Save and Version Validated Outputs

Once validation is complete:

- Save the validated dataset to the `output/` folder  
- Use a clear filename indicating validation (e.g. `validated_dataset.csv`)  
- Ensure source data remains unchanged  

This validated dataset will be used in later analytical modules.

---

## AI Reflection Prompt

Before moving on to downstream analysis, use an AI assistant of your choice and ask:

> **“What are the most common data-quality risks in real-world datasets, and how can analysts detect them early?”**

Reflect on the response by considering:

- Which risks were addressed by your validation checks  
- Which risks required human judgement  
- How these practices would scale for larger or frequently updated datasets  

---

## Version Control and Submission

From your project directory, initialise a Git repository and commit your work:

```bash
git init
git add .
git commit -m "Validate and document data quality"
```
## Create a GitHub Repository and Push Your Project

Create a new repository on GitHub, then push your local project:

```bash
git branch -M main
git push -u origin main
```
---
## Tips for Success

- Make assumptions explicit using assertions  
- Inspect data before and after validation  
- Avoid silently modifying data without explanation  
- Separate source data from validated outputs  
- Write clear, concise markdown explanations  
- Treat validation as a core analytical task, not an afterthought  

---

## Deliverables

Your final submission should include:

- A completed Jupyter Notebook with code and markdown explanations  
- Explicit data-quality checks and assertions  
- A validated dataset saved in the `output/` folder  
- A documented data-quality report in markdown  
- A GitHub repository containing all project files  

---

## Additional Resources

- **Pandas Documentation**  
  https://pandas.pydata.org/docs/

- **Pandas User Guide — Missing Data**  
  https://pandas.pydata.org/docs/user_guide/missing_data.html

- **Great Expectations — Data Quality Concepts**  
  https://docs.greatexpectations.io/

- **Real Python — Data Validation with Pandas**  
  https://realpython.com/pandas-dataframe-validation/



