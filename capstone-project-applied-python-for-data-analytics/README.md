# Capstone Project — Applied Python for Data Analytics

## Overview

The **Capstone Project** is the culminating experience of the Python for AI & Data course. This project integrates all the skills you have developed throughout the course into a complete, end-to-end data analytics workflow.

You will select a dataset, define analytical questions, clean and explore the data, build a predictive model, and present your findings in a professional, reproducible format. This project demonstrates your readiness to deliver high-quality analytical solutions in real-world settings.

---

## Project Timeline

| Phase | Activity | Time Allocation |
|-------|----------|-----------------|
| 1 | Project Setup & Data Selection | 20 minutes |
| 2 | Data Cleaning & Documentation | 40 minutes |
| 3 | Analysis, Modeling & Presentation | 60 minutes |
| **Total** | | **120 minutes** |

**Note:** You may use artefacts from previous labs to accelerate your work. The focus is on integration and professional presentation, not starting from scratch.

---

## Learning Objectives

By completing this project, you will demonstrate your ability to:

- **Integrate** Python programming, data handling, and analysis techniques to complete an applied analytics project
- **Document** methods, code, and results in a reproducible Jupyter Notebook
- **Present** findings and submit a final GitHub repository demonstrating technical proficiency

---

## Project Requirements

### Choose Your Path

You have **two options** for your capstone project:

#### Option A: Use the Provided Dataset
Use the `capstone_dataset.csv` provided in the `data/` folder. This dataset contains e-commerce sales data with multiple analysis opportunities.

#### Option B: Bring Your Own Dataset
Select a dataset relevant to your interests or career goals. Your dataset must:
- Contain at least 200 rows
- Include both numeric and categorical variables
- Be appropriate for regression or classification tasks

---

## Project Structure

Your final submission must follow this structure:

```text
Capstone_Applied_Python_Analytics/
│
├── data/
│   ├── raw/
│   │   └── capstone_dataset.csv       ← Original data (do not modify)
│   └── processed/
│       └── cleaned_dataset.csv        ← Your cleaned data
│
├── notebooks/
│   └── capstone_analysis.ipynb        ← Main analysis notebook
│
├── models/
│   ├── final_model.joblib             ← Saved model
│   └── MODEL_CARD.md                  ← Model documentation
│
├── outputs/
│   ├── figures/
│   │   ├── eda_visualization.png
│   │   └── model_performance.png
│   └── predictions.csv
│
├── docs/
│   └── PROJECT_SUMMARY.md             ← Executive summary
│
├── requirements.txt                   ← Environment dependencies
├── README.md                          ← This file
└── .gitignore
```

---

## Deliverables Checklist

Your capstone submission must include:

### 1. Data Processing (Required)
- [ ] Raw dataset in `data/raw/`
- [ ] Cleaned dataset in `data/processed/`
- [ ] Documentation of cleaning steps in notebook

### 2. Analysis Notebook (Required)
- [ ] Clear problem statement
- [ ] Exploratory Data Analysis with visualizations
- [ ] Statistical analysis or hypothesis testing
- [ ] Machine learning model (regression or classification)
- [ ] Model evaluation with appropriate metrics
- [ ] Markdown documentation throughout

### 3. Model Artefacts (Required)
- [ ] Saved model file (`.joblib`)
- [ ] Model Card documenting features, metrics, and limitations

### 4. Outputs (Required)
- [ ] At least 2 professional visualizations
- [ ] Predictions on test data (CSV)

### 5. Documentation (Required)
- [ ] Project summary (1-2 pages)
- [ ] `requirements.txt` file
- [ ] Complete README

### 6. GitHub Repository (Required)
- [ ] All files committed and pushed
- [ ] Clear commit history
- [ ] Professional repository structure

---

## Dataset Description (Option A)

The provided `capstone_dataset.csv` contains **500 records** of e-commerce transactions with the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `transaction_id` | string | Unique transaction identifier |
| `date` | date | Transaction date |
| `customer_id` | string | Customer identifier |
| `customer_segment` | category | Customer type (New, Returning, VIP) |
| `product_category` | category | Product category |
| `product_price` | float | Price in USD |
| `quantity` | int | Units purchased |
| `discount_applied` | float | Discount percentage (0-1) |
| `marketing_channel` | category | Acquisition channel |
| `region` | category | Geographic region |
| `total_revenue` | float | Transaction revenue in USD |
| `customer_satisfaction` | int | Satisfaction score (1-5) |
| `returned` | bool | Whether item was returned |

### Suggested Analysis Questions

1. **Regression:** Can you predict `total_revenue` based on transaction features?
2. **Classification:** Can you predict whether a transaction will result in a `returned` item?
3. **Segmentation:** How do purchasing patterns differ across `customer_segment`?
4. **Time Analysis:** Are there temporal patterns in sales data?

---

## Workflow Guide

### Phase 1: Project Setup (20 minutes)

1. **Fork or clone** the capstone repository
2. **Select your dataset** (provided or your own)
3. **Define your problem statement:**
   - What question are you trying to answer?
   - Is this a regression or classification problem?
   - What business value does this analysis provide?

### Phase 2: Data Cleaning & EDA (40 minutes)

1. **Load and inspect** the data
2. **Handle data quality issues:**
   - Missing values
   - Duplicates
   - Outliers
   - Data type corrections
3. **Perform EDA:**
   - Summary statistics
   - Distribution analysis
   - Correlation analysis
   - Create at least 2 visualizations
4. **Document** your findings in markdown cells

### Phase 3: Modeling & Presentation (60 minutes)

1. **Prepare features** for modeling
2. **Split data** into training and test sets
3. **Train a baseline model:**
   - Linear Regression (for regression tasks)
   - Logistic Regression (for classification tasks)
4. **Evaluate model performance:**
   - RMSE/MAE for regression
   - Accuracy for classification
5. **Save your model** using Joblib
6. **Create Model Card** documentation
7. **Write project summary**
8. **Commit and push** to GitHub

---

## Evaluation Criteria

Your project will be evaluated on the following criteria:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| **Data Handling** | 20% | Proper cleaning, transformation, and documentation |
| **Analysis Quality** | 20% | Meaningful EDA with clear insights |
| **Model Implementation** | 20% | Correct model training and evaluation |
| **Documentation** | 20% | Clear, professional markdown documentation |
| **Reproducibility** | 20% | Complete GitHub repo with all artefacts |

### Grading Scale

| Score | Level | Description |
|-------|-------|-------------|
| 4.0 | Advanced | Exceeds expectations; portfolio-ready work |
| 3.0 | Proficient | Meets all requirements at a satisfactory level |
| 2.0 | Developing | Meets some requirements; needs improvement |
| 1.0 | Beginning | Significant gaps; major revisions needed |

**Passing Score:** 12/20 (average of 3.0 across all criteria)

---

## Tips for Success

### Do's ✅
- Start with a clear problem statement
- Document as you go — don't leave it for the end
- Use meaningful variable names and comments
- Test that your notebook runs from top to bottom
- Commit frequently with descriptive messages
- Be honest about limitations in your Model Card

### Don'ts ❌
- Don't skip the train-test split
- Don't forget to save your model
- Don't submit without testing reproducibility
- Don't plagiarize — cite any external resources
- Don't overcomplicate — a simple, well-documented project beats a complex, confusing one

---

## Using AI Assistants

AI assistants (ChatGPT, Claude, GitHub Copilot) **may be used** to:
- Debug code errors
- Explain concepts
- Suggest approaches
- Review documentation

AI assistants **should not** be used to:
- Generate your entire notebook
- Write your analysis interpretation
- Create your project summary

**Important:** If you use AI assistance, briefly acknowledge it in your documentation. The goal is learning, not just completion.

---

## Submission Instructions

### 1. Prepare Your Repository
```bash
# Ensure all files are committed
git add .
git commit -m "Final capstone submission"
git push origin main
```

### 2. Verify Completeness
Run through the Deliverables Checklist above and ensure all items are checked.

### 3. Submit
- Share your GitHub repository URL via the LMS
- Ensure the repository is **public** or instructor has access

### 4. Presentation (if required)
Be prepared to present your project in a 5-10 minute presentation covering:
- Problem statement
- Key findings
- Model performance
- Lessons learned

---

## Resources

### Course Materials
- Module 14: Introduction to Machine Learning with Scikit-Learn
- Module 15: Model Deployment and Automation
- All previous lab notebooks

### External Resources
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)
- [Model Cards for Model Reporting](https://modelcards.withgoogle.com/about)

### Sample Projects
Review the structure and documentation style of professional data science projects on GitHub for inspiration.

---

## Getting Help

If you encounter issues:
1. Review relevant module materials
2. Check documentation for the specific library
3. Use an AI assistant to debug
4. Reach out to your instructor via the course chat

---

## Final Thoughts

This capstone project is your opportunity to demonstrate everything you've learned. Focus on:

- **Clarity** over complexity
- **Documentation** over quantity
- **Reproducibility** over perfection

A well-documented, reproducible project that answers a clear question is more valuable than a complex, messy analysis that's difficult to understand.

**Good luck! 🚀**

---

*Python for AI & Data — General Assembly*
