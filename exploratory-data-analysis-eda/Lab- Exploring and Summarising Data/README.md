# Lab: Exploring and Summarising Data

In this lab, you will conduct **Exploratory Data Analysis (EDA)** using Pandas to better understand a validated dataset.

Building on the data-quality checks from **Module 9**, you will now explore trends, relationships, and potential outliers, and communicate insights using descriptive statistics, grouping, and visualisations.

This lab focuses on developing **analytical curiosity** and **clear descriptive reporting** before moving into correlation, regression, or modelling.

---

## Lab Objectives

By completing this lab, you will be able to:

- Explore datasets to identify trends, relationships, and outliers  
- Summarise findings using descriptive statistics  
- Group, filter, and aggregate data to answer analytical questions  
- Visualise key patterns using simple plots  
- Communicate insights clearly using markdown and saved figures  

---

## Project Structure

Your project should follow the structure below:

```text
Lab_Exploratory_Data_Analysis/
│
├── data/
│   └── validated_dataset.csv 
│
├── notebooks/
│   ├── exploratory_data_analysis_lab.ipynb
│
│
├── output/
│   └── figures/
│
└── README.md

```
## Folder Descriptions

- **data/**  
  Contains the validated dataset produced in Module 9.  
  This file represents analysis-ready input data and should not be modified.

- **notebooks/**  
  Contains the Jupyter Notebook where you perform exploratory analysis,  
  generate statistics, create plots, and document insights.

- **output/**  
  Contains artefacts generated during analysis, such as:  
  - Saved visualisations (e.g. PNG files)  
  - Summary tables exported from Pandas  

Separating validated inputs from analytical outputs supports reproducibility  
and professional reporting workflows.

---

## How to Work Through the Lab

Follow the steps below in order.  
Run each cell as you go and read the markdown instructions carefully.

### 1. Set Up Your Notebook

Open the starter notebook:

```text
notebooks/exploratory_data_analysis_lab.ipynb
```
In the setup section, you will:

- Import required libraries (`pandas`, `numpy`, `matplotlib`)  
- Load the validated dataset from `data/validated_dataset.csv`  
- Perform an initial inspection of structure and content  

---

## 2. Perform Initial Exploration

Begin by understanding the overall shape and composition of the data.

You will:

- Inspect dataset dimensions and data types  
- Review column summaries  
- Identify obvious trends or irregularities  

This step establishes context before deeper analysis.

---

## 3. Descriptive Statistics

Use Pandas to summarise the data numerically.

You will:

- Compute summary statistics (mean, median, standard deviation)  
- Compare distributions across key variables  
- Identify potential outliers or unusual ranges  

Focus on interpretation, not just calculation.

---

## 4. Grouping, Filtering, and Aggregation

Explore how values differ across categories or segments.

You will:

- Group data by one or more categorical variables  
- Compute aggregated metrics (e.g. averages, counts, totals)  
- Filter subsets of interest for closer inspection  

This step helps reveal patterns that are not visible in raw data.

---

## 5. Visual Exploration

Support your numerical findings with visual evidence.

You will:

- Create simple plots (e.g. bar charts, line plots, histograms)  
- Compare groups visually where appropriate  
- Save key figures to the `output/figures/` folder  

Visualisation often highlights patterns and outliers more clearly than tables alone.

---

## 6. Summarise and Document Insights

In markdown cells, clearly explain:

- Key trends and patterns observed  
- Any notable outliers or anomalies  
- What questions the data raises for further analysis  

Your explanations should be understandable to a teammate or stakeholder reviewing your notebook.

---

## AI Reflection Prompt

Before moving on to statistical modelling, use an AI assistant of your choice and ask:

> **“When is exploratory data analysis insufficient on its own, and what additional techniques are needed to draw stronger conclusions?”**

Reflect on the response by considering:

- What insights EDA can and cannot provide  
- When correlation or regression becomes necessary  
- How visual exploration complements numerical analysis  

Keep this perspective in mind as you prepare for the next module.

---
## Version Control and Submission

From your project directory, initialise version control and commit your work:

```bash
git init
git add .
git commit -m "Explore and summarise validated data"
```
Create a new repository on GitHub, then push your local project:

```bash
git branch -M main
git push -u origin main
```
## Tips for Success

- Explore data before jumping to conclusions  
- Always interpret statistics in context  
- Use visuals to support (not replace) reasoning  
- Save figures and tables you reference in markdown  
- Focus on *why* patterns exist, not just *what* they are  

---

## Deliverables

Your final submission should include:

- A completed Jupyter Notebook with code and markdown explanations  
- Descriptive statistics and grouped summaries  
- At least one saved visualisation in `output/figures/`  
- Clear written insights explaining observed patterns  
- A GitHub repository containing all project files  

---

## Additional Resources

- **Pandas Documentation**  
  https://pandas.pydata.org/docs/

- **Pandas User Guide — Visualization**  
  https://pandas.pydata.org/docs/user_guide/visualization.html

- **Real Python — Exploratory Data Analysis with Pandas**  
  https://realpython.com/pandas-python-explore-dataset/

- **EDA Concepts and Best Practices**  
  https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15
