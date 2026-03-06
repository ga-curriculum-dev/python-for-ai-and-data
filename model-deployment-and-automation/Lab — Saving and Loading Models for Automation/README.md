# Lab: Saving and Loading Models for Automation

In this lab, you will apply **model deployment fundamentals** to save, load, and automate predictions using trained machine learning models.

Building on the machine learning concepts from Module 14, you will now transition from **training and evaluating models** to **deploying them for real-world use**. Using the model you trained previously, you will:

- Save trained models using Joblib
- Load models and generate predictions on new data
- Build a reusable prediction pipeline
- Document your model for reproducibility

This lab reinforces **model serialization**, **automation workflows**, and **professional documentation practices** — essential skills for your Capstone Project.

---

## Lab Objectives

By completing this lab, you will be able to:

- Save trained Scikit-Learn models to disk using Joblib
- Load saved models and generate predictions on new data
- Create a standalone prediction script for automation
- Document model metadata for reproducibility
- Prepare a complete model package ready for deployment

---

## Project Structure

Your project should follow the structure below:

```text
Lab_Saving_and_Loading_Models/
│
├── data/
│   └── validated_dataset_m15.csv
│
├── models/
│   ├── revenue_model.joblib
│   └── model_metadata.json
│
├── notebooks/
│   └── model_deployment_lab.ipynb
│
├── outputs/
│   ├── figures/
│   └── predictions.csv
│
├── scripts/
│   └── predict.py
│
├── solutions/
│   └── model_deployment_lab_solution.ipynb
│
└── README.md
```

### Folder Descriptions

**data/**  
Contains the validated dataset carried forward from Module 14.  
This file represents analysis-ready input data.

**models/**  
Contains saved model files and metadata.  
This folder stores your trained models for later use.

**notebooks/**  
Contains the Jupyter Notebook where you train, save, load, and test your model.

**outputs/**  
Contains artifacts generated during the lab, including:
- Prediction results on new data
- Visualizations comparing predictions

**scripts/**  
Contains standalone Python scripts for automated predictions.

**solutions/**  
Contains the completed solution notebook for instructor reference.

---

## How to Work Through the Lab

Follow the steps below in order.  
Run each cell as you go and read the markdown instructions carefully.

### 1. Set Up Your Notebook

Open the starter notebook:

```text
notebooks/model_deployment_lab.ipynb
```

In the setup section, you will:

- Import required libraries (pandas, numpy, scikit-learn, joblib)
- Create the necessary folder structure
- Load the dataset from `data/validated_dataset_m15.csv`

This step ensures you have the tools and data ready for model deployment.

### 2. Train a Model (Quick Review)

Before saving a model, you need one to save!

You will:

- Prepare features and target variable
- Split data into training and test sets
- Train a Linear Regression model (quick review from M14)
- Evaluate performance to confirm the model works

This is a condensed version of Module 14 — the focus here is on deployment, not training.

### 3. Save the Model with Joblib

This is the core new skill in this lab.

You will:

- Use `joblib.dump()` to save your trained model
- Choose appropriate file names and locations
- Verify the file was created successfully

**Key concept:** Serialization converts your model to a file that can be stored and reloaded later.

### 4. Load the Model and Predict

Demonstrate that your saved model works.

You will:

- Use `joblib.load()` to reload the model
- Generate predictions on the test set
- Verify predictions match the original model

**Key concept:** The loaded model is identical to the original — no retraining needed.

### 5. Save Model Metadata

A model without documentation is incomplete.

You will create a metadata file containing:

- Feature names used for training
- Training date and metrics
- Model type and version information
- Any limitations or notes

This metadata ensures your model can be used correctly in the future.

### 6. Create a Prediction Script

Move from notebook to automation.

You will:

- Create a standalone `predict.py` script
- Load the saved model
- Accept new data as input
- Generate and save predictions

**Key concept:** Scripts enable automation — your model can run without Jupyter.

### 7. Test on New Data

Simulate real-world deployment.

You will:

- Create sample "new" data (rows the model hasn't seen)
- Run predictions using your saved model
- Save results to `outputs/predictions.csv`

This demonstrates the complete deployment workflow.

### 8. Document Your Work

Professional documentation is essential.

You will:

- Create a Model Card summarizing your model
- Document the prediction workflow
- Ensure reproducibility for your Capstone Project

---

## AI Reflection Prompt

Before finalizing your submission, use an AI assistant of your choice and ask:

> "What are the key considerations when deploying a machine learning model from a Jupyter Notebook to a production environment?"

Reflect on the response by considering:

- The difference between development and production environments
- Why documentation is crucial for deployed models
- How version control helps manage model updates

Use this reflection to improve your deployment workflow.

---

## Version Control and Submission

From your project directory, initialize version control and commit your work:

```bash
git init
git add .
git commit -m "Save and deploy ML model for automation"
```

Create a new repository on GitHub, then push your local project:

```bash
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

---

## Tips for Success

- Always test that loaded models produce the same predictions as originals
- Use descriptive file names with version numbers (e.g., `revenue_model_v1.joblib`)
- Save metadata alongside your model — you'll thank yourself later
- Keep your `models/` folder organized
- Document limitations honestly

---

## Deliverables

Your final submission should include:

- A completed Jupyter Notebook with code and markdown explanations
- A saved model file (`.joblib`) in the `models/` folder
- Model metadata (JSON or markdown) documenting features and metrics
- A standalone prediction script (`predict.py`)
- Predictions on new data saved to CSV
- Clear written interpretation of the deployment workflow
- A GitHub repository containing all project files

---

## Connection to Capstone Project

This lab prepares you directly for Module 16 (Capstone Project):

| This Lab (M15) | Capstone (M16) |
|----------------|----------------|
| Save one model | Save your final model |
| Basic metadata | Complete Model Card |
| Simple prediction script | Documented workflow |
| Test on sample data | Apply to your chosen dataset |

The skills you practice here will be essential for delivering a professional, complete Capstone Project.

---

## Additional Resources

- **Scikit-Learn: Model Persistence**  
  https://scikit-learn.org/stable/model_persistence.html

- **Joblib Documentation**  
  https://joblib.readthedocs.io/

- **Model Cards for Model Reporting**  
  https://modelcards.withgoogle.com/about

- **Python Scripts vs Notebooks**  
  https://realpython.com/run-python-scripts/

- **JSON in Python**  
  https://docs.python.org/3/library/json.html
