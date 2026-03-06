# Python for AI & Data
# Capstone Project Brief

## Overview and Purpose

The **Capstone Project** serves as the culminating experience of the Python for AI & Data course, designed to integrate and demonstrate mastery of the key concepts, tools, and skills developed throughout the learning process. This project emphasizes real-world application, innovation, and professional readiness. It provides an opportunity to synthesize knowledge into a cohesive, outcome-driven deliverable that reflects industry relevance, technical proficiency, and creative problem-solving.

---

## Learning Objectives

The capstone project measures the following learning objectives:

- **Integrate** Python programming, data handling, and analysis techniques to complete an applied analytics project
- **Clean and transform** raw data into analysis-ready datasets using Pandas and NumPy
- **Perform exploratory data analysis** to identify patterns, trends, and insights
- **Build and evaluate** a baseline machine learning model using Scikit-Learn
- **Document** methods, code, and results in a reproducible Jupyter Notebook and GitHub repository

---

## Project Description

The project centers on completing an **end-to-end data analytics workflow** using Python. Learners will apply the full analytical process — from data ingestion and cleaning to exploratory analysis, machine learning, and professional documentation — to deliver a final analytical solution that demonstrates technical proficiency and clear communication.

Learners may use the provided e-commerce dataset or select their own dataset relevant to their interests or career goals. The project culminates in a reproducible GitHub repository containing a documented Jupyter Notebook, saved model artefacts, and a professional project summary.

---

## Deliverables

The Capstone Project culminates in the following final deliverables that demonstrate applied mastery of course concepts and practical skills:

### Required Components

**1. Primary Artefact: Jupyter Notebook**
- Complete analytical workflow from data loading to model evaluation
- Clear markdown documentation explaining methodology and findings
- Professional code with comments and logical organization

**2. Data Artefacts**
- Raw dataset (original, unmodified)
- Cleaned/processed dataset
- Documentation of data transformations

**3. Model Artefacts**
- Saved model file (`.joblib` format)
- Model Card documenting features, metrics, and limitations

**4. Visualizations**
- Minimum 2 professional visualizations (EDA and model performance)
- Saved as PNG files in outputs folder

**5. Documentation**
- Project Summary (1-2 page executive summary)
- Complete README file
- `requirements.txt` for environment reproducibility

**6. GitHub Repository**
- All project files committed and organized
- Clear commit history demonstrating iterative development
- Professional repository structure

---

## Deliverable Requirements

### Tools and Technologies

Learners must use the following tools:
- **Python 3** — Primary programming language
- **Jupyter Notebook** — Analysis environment
- **Pandas** — Data manipulation
- **NumPy** — Numerical computing
- **Matplotlib/Seaborn** — Data visualization
- **Scikit-Learn** — Machine learning
- **Joblib** — Model serialization
- **Git/GitHub** — Version control and submission

### AI or Automation Usage

AI tools (e.g., ChatGPT, Claude, GitHub Copilot) **may be used** for:
- Debugging code errors
- Explaining concepts or syntax
- Suggesting analytical approaches
- Reviewing documentation quality

AI tools **should not** be used to:
- Generate the complete analysis notebook
- Write interpretation of findings
- Create the project summary without learner input

**Acknowledgment Required:** If AI assistance is used, briefly note this in your documentation.

### File Format & Submission

| Deliverable | Format | Location |
|-------------|--------|----------|
| Analysis Notebook | `.ipynb` | `notebooks/` |
| Datasets | `.csv` | `data/raw/` and `data/processed/` |
| Model | `.joblib` | `models/` |
| Model Card | `.md` | `models/` |
| Visualizations | `.png` | `outputs/figures/` |
| Project Summary | `.md` | `docs/` |
| Requirements | `.txt` | Root directory |
| README | `.md` | Root directory |

**Submission Method:** Submit the GitHub repository URL via the LMS.

### Collaboration Guidelines

- This is an **individual project**
- Peer discussion and feedback is encouraged
- Code sharing or copying is not permitted
- All work must be your own (with AI assistance acknowledged)

### Other Requirements

- Dataset must contain at least 200 rows
- Notebook must execute without errors from top to bottom
- All visualizations must have titles, axis labels, and legends where appropriate
- Model must be evaluated with appropriate metrics (RMSE/MAE for regression, Accuracy for classification)
- Commit history should show incremental progress (minimum 5 commits)

---

## Presentation Requirements

### Format
- **5-10 minute presentation** (live or recorded, as specified by instructor)
- Slide-based presentation recommended

### Length/Duration
- 5-10 slides covering key aspects of the project
- Focus on insights and findings, not code walkthrough

### Tools and Platforms
- Google Slides, PowerPoint, or similar presentation tool
- Screen sharing for live presentations

### Content Expectations

Your presentation must include:

1. **Problem Statement** — What question are you answering?
2. **Data Overview** — What data did you use? Any quality issues?
3. **Key Findings** — What did EDA reveal?
4. **Model Results** — How well does your model perform?
5. **Limitations** — What are the constraints of your analysis?
6. **Conclusions** — What actionable insights can you provide?

### Submission Details
- Upload presentation slides to the LMS (if required)
- Be prepared to present during the final class session
- Live Q&A may follow the presentation

---

## Capstone Project Rubric

You will be evaluated based on this scoring rubric. For each criterion, you will be categorized as **Advanced**, **Proficient**, **Developing**, or **Beginning**.

**Passing Criteria:** To pass, you must achieve a total score of **12/20** (average of 3.0).

| Criterion | Advanced (4 pt.) | Proficient (3 pt.) | Developing (2 pt.) | Beginning (1 pt.) |
|-----------|------------------|--------------------|--------------------|-------------------|
| **Data Handling & Cleaning** | Data is thoroughly cleaned with documented transformations. Handles edge cases and missing values appropriately. Cleaning steps are reproducible. | Data is properly cleaned with basic documentation. Missing values and duplicates handled. Minor issues may exist. | Data has some cleaning but with gaps or undocumented steps. Some quality issues remain unaddressed. | Little to no data cleaning. Major data quality issues unresolved. No documentation of steps. |
| **Exploratory Data Analysis** | Comprehensive EDA with multiple visualizations. Clear insights documented. Statistical summaries provided. Patterns and outliers identified and explained. | Adequate EDA with required visualizations. Basic insights documented. Summary statistics included. | Limited EDA with minimal visualizations. Few insights documented. Missing important patterns. | No meaningful EDA. Missing or poor quality visualizations. No insights provided. |
| **Model Implementation** | Model correctly implemented with appropriate preprocessing. Train-test split used correctly. Multiple metrics calculated. Model saved with complete metadata. | Model implemented correctly. Basic preprocessing done. Train-test split used. Primary metrics calculated. Model saved. | Model implemented with errors or missing steps. Incomplete preprocessing or evaluation. Model may not be saved correctly. | Model not implemented or fundamentally incorrect. Missing train-test split. No evaluation metrics. |
| **Documentation Quality** | Exceptional documentation throughout. Clear problem statement. Methods explained. Results interpreted. Professional markdown formatting. | Good documentation. Problem stated clearly. Methods documented. Results described. Adequate formatting. | Some documentation but incomplete. Problem unclear. Methods partially explained. Poor formatting. | Little to no documentation. No clear problem statement. Code uncommented. No interpretation. |
| **Reproducibility & Repository** | Complete, professional repository. All artefacts present. Runs without errors. Clear commit history. README comprehensive. | Repository complete with all required files. Notebook runs with minor issues. Commit history present. README adequate. | Repository incomplete. Missing some artefacts. Notebook has errors. Few commits. Basic README. | Repository missing major components. Notebook doesn't run. No commit history. Missing README. |

### Final Score: ___/20

---

## Project Timeline Summary

| Phase | Duration | Focus |
|-------|----------|-------|
| Setup & Planning | 20 min | Select dataset, define problem, initialize repo |
| Data Work | 40 min | Clean data, perform EDA, create visualizations |
| Modeling & Documentation | 60 min | Build model, evaluate, document, finalize submission |
| **Total** | **120 min** | |

---

## Support Resources

- **Course Materials:** Review Modules 1-15 for reference
- **Documentation:** Pandas, Scikit-Learn, Matplotlib official docs
- **AI Assistance:** Use responsibly for debugging and explanations
- **Instructor:** Available via course chat for questions

---

*Good luck with your Capstone Project!*

*Python for AI & Data — General Assembly*
