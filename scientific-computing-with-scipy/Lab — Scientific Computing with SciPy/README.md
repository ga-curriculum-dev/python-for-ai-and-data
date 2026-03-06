# Lab: Statistical Testing with SciPy  
**Module 7 — Scientific Computing with SciPy**

**Estimated Time:** 30 minutes

---

## Introduction

In this lab, you will apply **scientific and statistical computing techniques** using **SciPy** to move from descriptive analysis to **statistical inference**.

You will compute summary statistics, perform a **hypothesis test**, visualise data distributions, and interpret results in context. The goal is not just to run statistical functions, but to **reason about what the results mean** and whether they support a data-driven conclusion.

This lab builds applied skills in **statistical testing, interpretation, and reproducible analytical reporting**.

---

## Learning Objectives

By the end of this lab, you will be able to:

- Compute descriptive statistics using SciPy and Pandas  
- Perform a hypothesis test using SciPy  
- Interpret p-values and statistical outputs responsibly  
- Visualise data distributions to support interpretation  
- Document conclusions clearly using markdown  

---

## Tools & Libraries

You will use:

- Python 3  
- Jupyter Notebook  
- SciPy  
- Pandas  
- Matplotlib
  
## Included Dataset

This lab includes the following dataset:

- `experiment_results.csv` (provided in the `data/` folder)

---

## Lab Overview

You will work through a structured statistical workflow:

```mermaid
flowchart LR
  A[Dataset] --> B[Descriptive Statistics]
  B --> C[Hypothesis Definition]
  C --> D[Statistical Test]
  D --> E[Visualise Distribution]
  E --> F[Interpret Results]
  F --> G[Document Conclusions]
```
---
## How to Work Through the Lab

Follow the steps below **in order**.  
Some cells depend on variables defined earlier, so avoid skipping sections.  
Run each cell as you go and read the markdown instructions carefully.

---

> **Important:** This is an **unrun starter notebook**.  
> Work through the notebook **cell by cell, in order**, reading the markdown instructions before running each section.

---

### 1. Set Up Your Notebook

Open the starter notebook:
- `notebooks/scipy_statistical_testing_lab.ipynb`

In the setup section, you will:

- Import required libraries (`scipy`, `pandas`, `numpy`, `matplotlib`)
- Load the provided dataset into a DataFrame

--- 

## 2. Compute Descriptive Statistics

Before running any statistical test, explore the data numerically.

You will:

- Calculate summary statistics (mean, standard deviation)
- Inspect the distribution of key variables
- Confirm assumptions about scale and variability

This step ensures you understand the data before testing hypotheses.

---

## 3. Define a Hypothesis

You will explicitly define:

- A null hypothesis (H₀)
- An alternative hypothesis (H₁)

Clear hypothesis definition is essential for valid inference.

---

## 4. Perform a Statistical Test

Using SciPy, you will:

- Run an appropriate hypothesis test (e.g. t-test)
- Capture the test statistic and p-value
- Assess whether results are statistically significant

Focus on **interpretation**, not just execution.

---

## 5. Visualise the Data

To support interpretation, you will:

- Plot the data distribution using Matplotlib
- Compare groups visually where appropriate
- Use plots to contextualise numerical results

Visualisation helps detect patterns and anomalies that statistics alone may miss.

---

## 6. Interpret and Document Results

In markdown cells, you will explain:

- What the test results indicate
- Whether the null hypothesis is rejected
- Any assumptions or limitations
- What conclusions can (and cannot) be drawn

Clear documentation is a core part of scientific analysis.
## Version Control and Submission

From your project directory, initialise a Git repository and commit your work:

```bash
git init
git add .
git commit -m "Perform statistical testing with SciPy"
```
Create a GitHub repository and push your work:

```bash
git branch -M main
git push -u origin main
```
---

## Tips for Success

- Always inspect data before testing  
- Do not rely on p-values alone — always consider context  
- Check assumptions behind statistical tests  
- Use visualisation to support conclusions  
- Explain results clearly in markdown  

---

## Deliverables

Your final submission should include:

- A completed Jupyter Notebook with code and explanations  
- At least one statistical test performed using SciPy  
- Visualisations supporting interpretation  
- Clear markdown summaries of findings  
- A GitHub repository containing all project files  

---

## Additional Resources

- **SciPy Documentation**  
  https://docs.scipy.org/doc/scipy/

- **SciPy Tutorial**  
  https://docs.scipy.org/doc/scipy/tutorial/

- **Real Python — SciPy Guide**  
  https://realpython.com/python-scipy/

- **Statistics and Hypothesis Testing Overview**  
  https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/


