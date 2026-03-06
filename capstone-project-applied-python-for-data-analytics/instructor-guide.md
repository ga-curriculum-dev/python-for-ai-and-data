# **Module 16: Capstone Project — Applied Python for Data Analytics: Instructor Guide**

**Module Time:** 120 minutes

---

**What This Module is About:**  
This capstone module is the culminating experience where learners integrate all skills developed throughout the course into a complete, end-to-end data analytics project. Learners will demonstrate their ability to clean data, perform EDA, build a machine learning model, and document their work professionally in a reproducible GitHub repository.

**Core Objectives:**  
- Integrate Python programming, data handling, and analysis techniques to complete an applied analytics project
- Document methods, code, and results in a reproducible Jupyter Notebook
- Present findings and submit a final GitHub repository demonstrating technical proficiency

**Must-Hit Topics:**  
- End-to-end analytical workflow integration
- Professional project documentation standards
- Model deployment readiness and reproducibility
- Effective presentation of data-driven insights
- GitHub repository best practices

---

## 1. **Project Setup and Planning**
**(Time: ~20 minutes)**

-   **Purpose:** Ensure learners have a clear problem statement and properly configured project structure before diving into analysis.

-   **Talking Points:**
    -   Review the Capstone Project Brief requirements and rubric with the class
    -   Emphasize the importance of defining a clear, answerable analytical question before writing any code
    -   Walk through the required folder structure and explain why organization matters for reproducibility
    -   Discuss dataset options: provided e-commerce dataset vs. bringing their own data

-   **Teaching Tips:**
    -   Have learners verbalize their problem statement to a partner before starting — this catches vague or overly ambitious scopes early
    -   Remind them this is about integration, not perfection — a simple, well-documented project beats a complex, messy one
    -   Point out that they can reuse code from previous labs (M14 and M15 especially) as starting points
    -   Circulate early to catch anyone stuck on environment setup or dataset selection

---

## 2. **Data Cleaning and Exploratory Data Analysis**
**(Time: ~40 minutes)**

-   **Purpose:** Learners apply data wrangling and EDA skills to prepare their dataset and uncover initial insights that will inform their modeling approach.

-   **Talking Points:**
    -   Reinforce the data cleaning workflow: check shape, dtypes, missing values, duplicates, outliers
    -   Stress the importance of documenting every cleaning decision in markdown cells — "Why did you fill missing values this way?"
    -   Remind learners that EDA should answer questions: What patterns exist? What relationships might predict the target?
    -   Minimum requirement: 2 professional visualizations with proper titles, labels, and legends

-   **Teaching Tips:**
    -   Encourage learners to save their cleaned dataset to `data/processed/` before moving to modeling — this creates a checkpoint
    -   If learners are rushing through EDA, ask them: "What did you learn from this visualization? Write it down."
    -   Watch for common mistakes: forgetting to convert date columns, not handling categorical variables, creating visualizations without interpretation
    -   This is a good time for a quick check-in: "Raise your hand if you've saved your cleaned data and created at least one visualization"

---

## 3. **Model Building and Evaluation**
**(Time: ~30 minutes)**

-   **Purpose:** Learners apply their M14 machine learning skills to build, evaluate, and interpret a baseline model appropriate to their analytical question.

-   **Talking Points:**
    -   Review the train-test split process — emphasize setting `random_state=42` for reproducibility
    -   Clarify which metrics to use: RMSE/MAE for regression, Accuracy for classification
    -   Remind learners to interpret their metrics in context: "What does an RMSE of 150 mean for predicting revenue?"
    -   Connect back to M15: the model they build here should be saved using the same Joblib workflow

-   **Teaching Tips:**
    -   If learners are struggling with model choice, default them to LinearRegression (regression) or LogisticRegression (classification)
    -   Watch for the common mistake of fitting the model on the test set — reinforce: fit on train, predict on test
    -   Encourage learners who finish early to try a second model type and compare performance
    -   Remind them that a "bad" model is still a valid result — document why it might not be working well

---

## 4. **Model Saving and Documentation**
**(Time: ~15 minutes)**

-   **Purpose:** Learners apply M15 deployment skills to save their model with metadata and create professional documentation including a Model Card.

-   **Talking Points:**
    -   Walk through the model package structure: model object + feature names + metrics + training date
    -   Review the Model Card template sections: Model Details, Intended Use, Training Data, Performance, Limitations
    -   Emphasize honesty in the Limitations section — this demonstrates professional maturity
    -   Remind learners that the Project Summary should be readable by a non-technical stakeholder

-   **Teaching Tips:**
    -   The Model Card is often rushed — allocate specific time for it and check that learners are actually filling it out
    -   Encourage learners to write limitations based on their actual experience: "What went wrong? What would you do differently?"
    -   If time is tight, have them complete the Model Card as a take-home item before final submission
    -   Point out that good documentation is what separates a student project from a portfolio-ready project

---

## 5. **GitHub Repository and Final Submission**
**(Time: ~10 minutes)**

-   **Purpose:** Learners finalize their repository structure, verify reproducibility, and prepare for submission.

-   **Talking Points:**
    -   Review the deliverables checklist: all required files present in correct locations
    -   Emphasize the reproducibility test: "Can someone else clone your repo and run your notebook without errors?"
    -   Discuss commit history expectations: minimum 5 commits showing incremental progress, not one giant commit
    -   Walk through the submission process: GitHub URL via LMS

-   **Teaching Tips:**
    -   Have learners run their notebook from top to bottom (Kernel → Restart & Run All) as a final check
    -   Pair learners up to review each other's repository structure before submission
    -   Common issues: missing requirements.txt, figures not saved, model file not committed (check .gitignore)
    -   Remind them to make the repository public or add instructor as collaborator

---

## 6. **Presentations (if applicable)**
**(Time: ~Variable, typically 5-10 min per learner)**

-   **Purpose:** Learners practice communicating their analytical findings to an audience, demonstrating both technical understanding and presentation skills.

-   **Talking Points:**
    -   Presentation structure: Problem → Data → Findings → Model → Limitations → Conclusions
    -   Focus on insights, not code — the audience wants to know what you learned, not how you wrote a for loop
    -   Be prepared for questions about methodology and limitations
    -   Time management: 5-10 minutes goes fast, practice beforehand

-   **Teaching Tips:**
    -   If doing live presentations, keep strict time limits to ensure everyone presents
    -   Encourage audience questions — this helps quieter learners engage and gives presenters practice defending their work
    -   Provide brief, constructive feedback after each presentation focusing on one strength and one area for improvement
    -   Consider having learners submit recorded presentations if class time is limited

---

## **Wrap-Up Reflection**
**(Time: ~5 minutes)**

-   **Key Takeaways:**
    -   A complete, well-documented project demonstrates more professional readiness than a complex but messy analysis
    -   Reproducibility is non-negotiable in data science — if someone can't run your code, your work has limited value
    -   The skills practiced in this capstone — data cleaning, EDA, modeling, documentation, version control — are the core competencies employers expect from entry-level data analysts

-   **Next Steps:** Congratulate learners on completing the course! Encourage them to add their capstone project to their portfolio and LinkedIn. Remind them that this project can be expanded and improved over time as they continue learning. Provide information about certificates of completion and any follow-up resources or career support available.

---

## **Common Issues and Solutions**

| Issue | Solution |
|-------|----------|
| Learner's notebook won't run | Check for hardcoded file paths, missing imports, or cells run out of order |
| Model performance is poor | This is okay — document why and suggest improvements in limitations |
| Learner is overwhelmed | Focus on minimum requirements first, polish later if time permits |
| Dataset too small/simple | Acceptable for capstone; note as limitation and suggest richer data for future work |
| GitHub submission issues | Have backup: accept ZIP file upload or screen share of repository |

---

## **Rubric Quick Reference**

| Criterion | What to Look For |
|-----------|------------------|
| Data Handling | Cleaning documented, missing values addressed, data saved to processed folder |
| EDA | Minimum 2 visualizations, insights documented in markdown, summary statistics present |
| Model | Train-test split correct, appropriate metrics calculated, results interpreted |
| Documentation | Clear problem statement, Model Card complete, README present, code commented |
| Repository | All files present, notebook runs without errors, commit history shows progress |

**Passing Score:** 12/20 (average of 3.0 across criteria)
