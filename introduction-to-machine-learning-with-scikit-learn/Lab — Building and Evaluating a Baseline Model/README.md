# Lab: Building and Evaluating a Baseline Model

In this lab, you will apply **machine learning fundamentals** to build and evaluate a **baseline predictive model** using Scikit-Learn.

Building on the time series analysis and forecasting concepts from Module 13, you will now transition from **forecasting future values** to **predicting outcomes based on features**. Using the same validated dataset, you will:

- Prepare data for machine learning
- Split data into training and test sets
- Train baseline models using Scikit-Learn
- Evaluate model performance using appropriate metrics
- Interpret results and communicate limitations

This lab reinforces **supervised learning fundamentals**, **model evaluation**, and **responsible interpretation of predictive outputs**.

---
## Learning Focus and Expectations

This lab is designed to demonstrate the **end-to-end workflow of supervised machine learning** using Scikit-Learn, including data preparation, model training, evaluation, and interpretation.

The models used in this lab are **baseline models**. Achieving high predictive performance is **not the goal**. Instead, the focus is on:

- Understanding the difference between regression and classification
- Applying standard train/test splits
- Using appropriate evaluation metrics
- Interpreting results responsibly and recognizing limitations

Low or moderate model performance is expected and does not indicate incorrect work.

---
## Lab Objectives

By completing this lab, you will be able to:

- Split data into training and test sets using Scikit-Learn's `train_test_split`
- Fit baseline models (Linear Regression and Logistic Regression) using Scikit-Learn
- Evaluate model performance using **accuracy** (classification) and **RMSE** (regression)
- Interpret model results and communicate limitations clearly
- Compare the machine learning approach to the baseline forecasting from Module 13

---

## Project Structure

Your project should follow the structure below:

```text
Lab_Building_and_Evaluating_a_Baseline_Model/
│
├── data/
│   └── validated_dataset_m14.csv
│
├── notebooks/
│   └── baseline_model_lab.ipynb
│
├── outputs/
│   ├── figures/
│   └── model_metrics.csv
│
├── solutions/
│   └── baseline_model_lab_solution.ipynb
│
└── README.md
```

### Folder Descriptions

**data/**  
Contains the validated dataset carried forward from previous modules.  
This file represents analysis-ready input data and must not be modified.

**notebooks/**  
Contains the Jupyter Notebook where you perform data preparation,  
model training, evaluation, and markdown-based interpretation.

**outputs/**  
Contains artifacts generated during the lab, including:
- Saved figures (feature distributions, predictions vs actuals)
- Model evaluation metrics (accuracy, RMSE)

**solutions/**  
Contains the completed solution notebook for instructor reference.

Separating validated inputs from analytical outputs supports reproducibility  
and professional analytical workflows.

---

## How to Work Through the Lab

Follow the steps below in order.  
Run each cell as you go and read the markdown instructions carefully.

### 1. Set Up Your Notebook

Open the starter notebook:

```text
notebooks/baseline_model_lab.ipynb
```

In the setup section, you will:

- Import required libraries (pandas, numpy, matplotlib, scikit-learn)
- Load the dataset from `data/validated_dataset_m14.csv`
- Explore the dataset structure

This step ensures you have the tools and data ready for machine learning.

### 2. Understand the Prediction Tasks

Before building models, you must understand what you're predicting.

In this lab, you will work on two prediction tasks:

| Task | Type | Target Variable | Features |
|------|------|-----------------|----------|
| Regression | Predict a number | `revenue_usd` | price, discount, marketing spend, web sessions, units sold |
| Classification | Predict a category | `high_revenue` (derived) | price, discount, marketing spend, web sessions, units sold |

Understanding the difference between regression and classification is fundamental to choosing the right model and metrics.

### 3. Prepare Features and Target Variables

Machine learning requires separating:
- **Features (X)**: The input variables used to make predictions
- **Target (y)**: The output variable you want to predict

You will:

- Select relevant numeric features
- Create the target variable for each task
- Handle any missing values

### 4. Split Data into Training and Test Sets

To evaluate how well your model generalizes, you must split the data.

You will:

- Use `train_test_split` from Scikit-Learn
- Keep 20% of data for testing
- Set `random_state=42` for reproducibility

**Key principle:** Never evaluate on the same data you trained on.

### 5. Train Baseline Models

You will train two baseline models:

**For Regression (predicting `revenue_usd`):**
- Linear Regression

**For Classification (predicting `high_revenue`):**
- Logistic Regression

These simple models establish a performance baseline before trying more complex approaches.

### 6. Evaluate Model Performance

You will compute appropriate metrics for each task:

**Regression metrics:**
- **RMSE (Root Mean Squared Error)** — penalizes larger errors
- **MAE (Mean Absolute Error)** — average magnitude of errors

**Classification metrics:**
- **Accuracy** — proportion of correct predictions

You will save evaluation results to `outputs/model_metrics.csv`.

### 7. Visualize Predictions

Visual inspection complements numerical metrics.

You will:

- Plot actual vs predicted values (regression)
- Create a confusion matrix (classification)
- Identify patterns in prediction errors

Visuals help contextualize model performance.

### 8. Compare with Module 13 Forecasting

Reflect on the differences between:

- **Time series forecasting (M13):** Predicting future values based on temporal patterns
- **Machine learning prediction (M14):** Predicting outcomes based on feature relationships

Both approaches have their place in data analysis.

### 9. Interpret and Document Results

In markdown cells, clearly explain:

- Which model performed better and why
- What limitations exist in the models
- Whether the predictions would be reliable for decision-making
- What additional features or methods might improve results

Machine learning is about reasoned interpretation, not just numbers.

---

## AI Reflection Prompt

Before finalizing your submission, use an AI assistant of your choice and ask:

> "What are the key differences between time series forecasting and supervised machine learning, and when should each approach be used?"

Reflect on the response by considering:

- How the prediction task determines the approach
- Why baseline models matter in both contexts
- The importance of appropriate evaluation metrics

Use this reflection to critically assess your modeling approach.

---

## Version Control and Submission

From your project directory, initialize version control and commit your work:

```bash
git init
git add .
git commit -m "Build and evaluate baseline ML model"
```

Create a new repository on GitHub, then push your local project:

```bash
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

---

## Tips for Success

- Always split data before training — never peek at test data
- Start with simple models before complex ones
- Interpret metrics in context (what does an RMSE of 500 mean for revenue?)
- Compare training and test performance to detect overfitting
- Clearly state assumptions and limitations

---

## Deliverables

Your final submission should include:

- A completed Jupyter Notebook with code and markdown explanations
- At least one regression model with RMSE evaluation
- At least one classification model with accuracy evaluation
- Visualizations of model predictions
- Model evaluation metrics saved to CSV
- Clear written interpretation of results
- A GitHub repository containing all project files

---

## Additional Resources

- **Scikit-Learn Documentation**  
  https://scikit-learn.org/stable/documentation.html

- **Scikit-Learn: train_test_split**  
  https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

- **Understanding Regression Metrics**  
  https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics

- **Understanding Classification Metrics**  
  https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics

- **Google Machine Learning Crash Course**  
  https://developers.google.com/machine-learning/crash-course
