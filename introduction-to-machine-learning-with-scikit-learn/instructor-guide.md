# **Module 14 — Introduction to Machine Learning with Scikit-Learn: Instructor Guide**

**Module Time:** 120 minutes

---

**What This Module is About:**  
This module introduces learners to the fundamentals of machine learning, guiding them through building and evaluating a baseline predictive model using Scikit-Learn. Learners will understand how to split data, train models, interpret performance metrics, and communicate model limitations responsibly.

**Core Objectives:**  
- Split data into training and test sets and fit a baseline model using Scikit-Learn
- Evaluate model performance using accuracy or RMSE metrics
- Interpret results and communicate model limitations in context

**Must-Hit Topics:**  
- Supervised learning: classification vs regression
- The importance of train-test splits
- Scikit-Learn's consistent API pattern (fit, predict, evaluate)
- Accuracy for classification, MAE and RMSE for regression
- Overfitting, underfitting, and model limitations
- Responsible communication of model results

---

## 1. **What is Machine Learning?**

**(Time: ~15 minutes)**

-   **Purpose:** Establish foundational understanding of machine learning concepts and set the context for supervised learning techniques covered in this module.

-   **Talking Points:**
    -   Machine learning is a subset of AI where algorithms learn patterns from data to make predictions — no explicit programming required for every scenario
    -   Three main types exist: supervised learning (labeled data), unsupervised learning (no labels), and reinforcement learning (learning from feedback)
    -   This module focuses on supervised learning, which includes classification (predicting categories) and regression (predicting continuous numbers)
    -   Real-world examples: spam detection (classification), house price prediction (regression), customer churn prediction (classification)

-   **Teaching Tips:**
    -   Start with a relatable example — ask learners "How would you predict if an email is spam?" to get them thinking about features and patterns
    -   Use the mermaid diagram to visually show the hierarchy of ML types
    -   Emphasize that we're not trying to build complex models — the goal is understanding the fundamentals
    -   Clarify the classification vs regression distinction early; learners often confuse these initially

---

## 2. **The Machine Learning Workflow**

**(Time: ~15 minutes)**

-   **Purpose:** Provide learners with a mental framework for approaching any machine learning problem systematically.

-   **Talking Points:**
    -   Every ML project follows seven key stages: Define Problem → Collect Data → Prepare Data → Split Data → Train Model → Evaluate Model → Interpret Results
    -   Defining the problem correctly is crucial — you must know if it's classification or regression before choosing a model
    -   Data preparation (cleaning, handling missing values) often takes 80% of a data scientist's time
    -   The workflow is iterative — poor evaluation results send you back to earlier stages

-   **Teaching Tips:**
    -   Walk through each stage with a concrete example (e.g., predicting house prices)
    -   Ask learners: "What could go wrong at each stage?" to promote critical thinking
    -   Stress that this workflow applies to ALL machine learning projects, regardless of complexity
    -   Connect back to previous modules — they've already learned data preparation and EDA

---

## 3. **Splitting Data: Training and Test Sets**

**(Time: ~20 minutes)**

-   **Purpose:** Explain why proper data splitting is essential for building trustworthy models that generalize to new data.

-   **Talking Points:**
    -   The fundamental question: "Will my model work on data it has never seen before?"
    -   Training on the same data you evaluate on gives unrealistically optimistic results — the model has already "seen the answers"
    -   Standard split: 70-80% training, 20-30% testing
    -   Key parameters in `train_test_split`: `test_size`, `random_state` (reproducibility), `stratify` (maintains class balance)
    -   Never, ever use test data during training — this is called "data leakage"

-   **Teaching Tips:**
    -   Use an analogy: "It's like a student memorizing the exact test questions vs. actually learning the material"
    -   Live code the `train_test_split` function — show learners the shapes of resulting arrays
    -   Emphasize `random_state` for reproducibility — different seeds give different splits
    -   Common mistake to highlight: forgetting to set `random_state` and getting different results each run

---

## 4. **Building a Baseline Model with Scikit-Learn**

**(Time: ~20 minutes)**

-   **Purpose:** Introduce Scikit-Learn's consistent API and demonstrate how to train baseline models for both regression and classification tasks.

-   **Talking Points:**
    -   Scikit-Learn is Python's most popular ML library — consistent API across all algorithms
    -   The universal pattern: Import → Create Instance → Fit → Predict → Evaluate
    -   Linear Regression for regression tasks: assumes linear relationship between features and target
    -   Logistic Regression for classification tasks: despite the name, it's a classifier that predicts probabilities
    -   Baseline models are simple, interpretable, and establish minimum acceptable performance

-   **Teaching Tips:**
    -   Live code both Linear Regression and Logistic Regression examples
    -   Emphasize the beauty of Scikit-Learn's consistent API — once you know one model, you know them all
    -   Ask: "Why start simple instead of jumping to complex models?" — baseline models help detect data issues and set benchmarks
    -   Show that switching algorithms is often just changing one line of code (the import and model instantiation)

---

## 5. **Evaluating Model Performance**

**(Time: ~20 minutes)**

-   **Purpose:** Teach learners how to quantitatively assess model performance using appropriate metrics and understand what those metrics actually mean.

-   **Talking Points:**
    -   "All models are wrong, but some are useful" — evaluation tells us HOW useful
    -   Classification metric — Accuracy: proportion of correct predictions; misleading with imbalanced classes
    -   Regression metric — MAE: average magnitude of errors, easy to interpret, same units as target
    -   Regression metric — RMSE: penalizes large errors more heavily, useful when big mistakes are costly
    -   If RMSE >> MAE, your model has some large prediction errors worth investigating

-   **Teaching Tips:**
    -   Calculate metrics by hand for a small example before showing the Scikit-Learn functions
    -   Use concrete numbers: "An MAE of $15,000 means on average we're off by $15,000"
    -   Discuss when accuracy is misleading — the classic "99% accuracy on 99% negative class" problem
    -   Ask learners: "Is 80% accuracy good?" (Answer: it depends on the context and baseline!)

---

## 6. **Interpreting Results and Communicating Limitations**

**(Time: ~8 minutes)**

-   **Purpose:** Ensure learners can critically interpret model results and communicate findings responsibly to stakeholders.

-   **Talking Points:**
    -   Four common limitations: overfitting (high train/low test), underfitting (low both), data quality issues, missing features
    -   Always report: what the model predicts, how well it performs (with context), where it struggles, confidence level
    -   Good communication example: "Our model predicts house prices with an average error of $15,000. It performs well for mid-range homes but underestimates luxury properties."
    -   Bad communication example: "Our model predicts house prices with 95% accuracy" — misleading and lacks context

-   **Teaching Tips:**
    -   Role-play: "You're presenting to a non-technical manager — how do you explain your model's performance?"
    -   Emphasize that acknowledging limitations builds trust and credibility
    -   Connect to ethical considerations — deploying a model with known limitations has real consequences
    -   Remind learners that interpretation is just as important as the technical implementation

---

## 7. **Lab — Building and Evaluating a Baseline Model**

**(Time: ~30 minutes)**

-   **Purpose:** Provide hands-on practice where learners apply all concepts from the module to build, evaluate, and interpret a predictive model using real data.

-   **Lab Overview:**
    -   Learners will work with a provided dataset to train and test a predictive model using Scikit-Learn
    -   They will split data into training and test sets using `train_test_split`
    -   They will fit a baseline model (Linear Regression or Logistic Regression) on the training data
    -   They will generate predictions on the test set and evaluate performance using accuracy (classification) or RMSE (regression)
    -   They will interpret model results and document their findings

-   **Instructor Role During Lab:**
    -   Monitor learners' progress and check that they are correctly splitting their data (common mistake: forgetting `random_state`)
    -   Help learners who get stuck on syntax errors — especially with Scikit-Learn imports
    -   Prompt struggling learners with guiding questions rather than giving direct answers
    -   Encourage learners to share their metrics in the chat and discuss: "Is this good performance? Why or why not?"

-   **Common Issues to Watch For:**
    -   Forgetting to import necessary libraries (numpy, sklearn modules)
    -   Confusing `X` (features) and `y` (target) — ensure correct variable assignment
    -   Using the wrong metric for the task (e.g., accuracy for regression)
    -   Not interpreting results — just printing numbers without context

-   **Debrief Questions (Last 5 minutes):**
    -   "What was your model's performance? How would you explain this to a non-technical stakeholder?"
    -   "Did anything surprise you about your results?"
    -   "What limitations does your model have?"

---

## **Wrap-Up Reflection**

**(Time: ~2 minutes)**

-   **Key Takeaways:**
    -   Always split your data into training and test sets to evaluate how well your model generalizes to unseen data — never train and test on the same data
    -   Scikit-Learn provides a consistent API (fit, predict, evaluate) that works across all algorithms, making it easy to experiment with different models
    -   Model evaluation requires context — a "good" accuracy or RMSE value depends entirely on the problem, and responsible communication includes acknowledging limitations

-   **Next Steps:** Learners will now apply these concepts in the hands-on lab, where they will build and evaluate a baseline predictive model using Scikit-Learn, splitting data into training and test sets and interpreting their model's performance metrics.

---
