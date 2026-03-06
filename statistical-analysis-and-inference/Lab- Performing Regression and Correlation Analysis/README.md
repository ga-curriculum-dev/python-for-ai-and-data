# Lab: Performing Regression and Correlation Analysis

In this lab, you will apply correlation and regression techniques to explore and interpret relationships between variables in a validated dataset.

Building on the exploratory analysis from Module 10, you will now move from describing patterns to quantifying relationships, using statistical methods to support data-driven conclusions.

This lab strengthens applied statistical reasoning, interpretation of results, and clear analytical communication, preparing you to explain findings confidently to non-technical audiences.

---

## Lab Objectives

By completing this lab, you will be able to:

- Perform correlation analysis to assess the strength and direction of relationships
- Apply simple linear regression to model relationships between variables
- Interpret coefficients, R² values, and statistical significance in plain language
- Distinguish between correlation, association, and explanatory modelling
- Communicate statistical insights clearly using markdown, visuals, and written interpretation

---

## Project Structure

Your project should follow the structure below:
```text
Lab_Statistical_Analysis_and_Inference/
│
├── data/
│   └── validated_dataset_m11.csv
│
├── notebooks/
│   └── correlation_regression_lab.ipynb
│
├── output/
│   ├── figures/
│   └── regression_summary.txt
│
└── README.md
```

### Folder Descriptions

**data/**  
Contains the validated dataset carried forward from Module 10.  
This file represents analysis-ready input data and must not be modified.

**notebooks/**  
Contains the Jupyter Notebook where you perform correlation and regression analysis, generate plots, and document interpretation in markdown.

**output/**  
Contains artefacts generated during statistical analysis, such as:
- Saved figures supporting interpretation
- Exported regression summaries or key outputs

Separating validated inputs from analytical outputs supports reproducibility and professional analytical workflows.

---

## How to Work Through the Lab

Follow the steps below in order.  
Run each cell as you go and read the markdown instructions carefully.

### 1. Set Up Your Notebook

Open the starter notebook:
```text
notebooks/correlation_regression_lab.ipynb
```

In the setup section, you will:
- Import required libraries (pandas, numpy, matplotlib, scipy, statsmodels)
- Load the validated dataset from `data/validated_dataset_m11.csv`
- Briefly inspect the dataset to recall key variables and structure

### 2. Define Analytical Questions

Before running any statistics, clarify what you want to understand.

You will:
- Identify at least one pair of variables to analyse
- Formulate a clear analytical question (e.g. "Is there a relationship between X and Y?")
- State expectations or hypotheses in markdown

This reinforces that statistical analysis starts with questions, not functions.

### 3. Correlation Analysis

Use correlation analysis to assess the strength and direction of relationships.

You will:
- Compute correlation coefficients (e.g. Pearson correlation)
- Interpret the magnitude and sign of relationships
- Visualise relationships using scatter plots

Focus on what the correlation tells you — not just the numeric value.

### 4. Simple Linear Regression

Apply simple linear regression to model relationships between variables.

You will:
- Define independent and dependent variables
- Fit a regression model using Python statistical libraries
- Extract key outputs (coefficients, R², p-values)

Regression is used here as an explanatory tool, not a predictive model.

### 5. Interpret Coefficients and Significance

Carefully interpret your regression results.

You will:
- Explain what the regression coefficient means in real-world terms
- Discuss statistical significance conceptually
- Distinguish between statistical significance and practical relevance
- Identify assumptions and limitations of the model

This step is essential for responsible statistical analysis.

### 6. Visualise and Support Interpretation

Support statistical findings with visuals.

You will:
- Create plots showing relationships and fitted regression lines
- Save key figures to the `output/figures/` folder
- Ensure visuals are clearly labelled and easy to interpret

Visuals should support interpretation, not replace it.

### 7. Summarise and Communicate Insights

In markdown cells, clearly explain:
- What relationships were found
- How strong and meaningful they are
- What conclusions can reasonably be drawn
- What limitations or uncertainties remain

Your explanations should be understandable to a non-technical audience.

---

## AI Reflection Prompt

Before finalising your conclusions, use an AI assistant of your choice and ask:

> "When is correlation analysis insufficient, and why might regression provide deeper insight?"

Reflect on the response by considering:
- What correlation can and cannot explain
- How regression adds explanatory power
- The risks of over-interpreting statistical relationships
- How context shapes interpretation

Use this reflection to critically review your own analysis.

---

## Version Control and Submission

From your project directory, initialise version control and commit your work:
```bash
git init
git add .
git commit -m "Perform correlation and regression analysis"
```

Create a new repository on GitHub, then push your local project:
```bash
git branch -M main
git push -u origin main
```

---

## Tips for Success

- Start with analytical questions, not statistical functions
- Interpret coefficients in plain, real-world language
- Never assume causation from correlation
- Always discuss assumptions and limitations
- Use visuals to clarify, not decorate
- Prioritise clarity over complexity

---

## Deliverables

Your final submission should include:
- A completed Jupyter Notebook with code and markdown explanations
- Correlation analysis with interpretation
- A simple regression model with clearly explained coefficients
- At least one saved visual supporting interpretation
- Clear, non-technical written conclusions
- A GitHub repository containing all project files

---

## Additional Resources

- **Pandas Documentation**  
  https://pandas.pydata.org/docs/

- **SciPy Documentation**  
  https://docs.scipy.org/doc/scipy/

- **StatsModels Documentation**  
  https://www.statsmodels.org/stable/index.html

- **Correlation and Regression (Conceptual Overview)**  
  https://www.statisticshowto.com/probability-and-statistics/correlation-analysis/

- **Real Python — Correlation & Regression with Pandas**  
  https://realpython.com/pandas-correlation-regression/
