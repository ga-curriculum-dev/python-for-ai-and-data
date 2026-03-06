# **Module 6: Exploratory Data Analysis with Pandas — Instructor Guide**

**Module Time:** 120 minutes

---

**What This Module is About:**  
This module introduces learners to Exploratory Data Analysis (EDA) using Pandas, focusing on summarising data, grouping and aggregation, and interpreting patterns to prepare datasets for downstream analysis.

**Core Objectives:**  
- Develop analytical intuition through exploratory analysis  
- Use Pandas to calculate and interpret descriptive statistics  
- Apply grouping and aggregation to answer analytical questions  
- Identify trends, patterns, and potential anomalies in data  

**Must-Hit Topics:**  
- Purpose and role of EDA in analytics workflows  
- Descriptive statistics with Pandas  
- Grouping and aggregation using `groupby()`  
- Interpreting results and identifying anomalies  
- Preparing analysis-ready outputs  

---

## 1. **Introduction to Exploratory Data Analysis (EDA)**
**(Time: ~10 minutes)**

- **Purpose:**  
  Establish why exploratory analysis is a critical step before visualisation, modelling, or statistical testing.

- **Talking Points:**
  - EDA focuses on understanding data before drawing conclusions  
  - EDA helps validate assumptions and detect unexpected behaviour  
  - EDA is an iterative process, not a single command  

- **Teaching Tips:**
  - Emphasise that EDA is about *asking better questions*, not finding final answers  
  - Encourage learners to verbalise what they expect the data to show before running code  
  - Reference the conceptual EDA workflow diagram to frame the module  

---

## 2. **Descriptive Statistics with Pandas**
**(Time: ~20 minutes)**

- **Purpose:**  
  Help learners summarise datasets numerically and understand what “typical” looks like in their data.

- **Talking Points:**
  - Using `df.describe()` to understand central tendency and spread  
  - Differences between mean, median, and standard deviation  
  - Using `value_counts()` for categorical variables  
  - Recognising when summary statistics may hide important details  

- **Teaching Tips:**
  - Ask learners to interpret outputs in plain language  
  - Highlight how outliers can distort averages  
  - Reinforce that statistics describe data, but do not explain *why*  

---

## 3. **Grouping and Aggregation**
**(Time: ~20 minutes)**

- **Purpose:**  
  Show how grouping transforms row-level data into meaningful summaries.

- **Talking Points:**
  - Using `groupby()` to segment data  
  - Aggregating metrics to compare categories  
  - Examples of real-world analytical questions answered through grouping  

- **Teaching Tips:**
  - Start with simple groupings before introducing multiple aggregations  
  - Encourage learners to think about *which level of aggregation makes sense*  
  - Reinforce the connection between grouping and business or research questions  

---

## 4. **Identifying Patterns and Anomalies**
**(Time: ~20 minutes)**

- **Purpose:**  
  Develop learners’ ability to interpret results and recognise signals worth investigating.

- **Talking Points:**
  - Identifying unexpected values or ranges  
  - Spotting large differences between groups  
  - Recognising trends that require further analysis  
  - Noting when additional cleaning may be required  

- **Teaching Tips:**
  - Emphasise interpretation over code complexity  
  - Ask learners *why* a pattern might exist, not just *what* it is  
  - Reinforce that anomalies are often the most informative observations  

---

## 5. **Preparing Data for Downstream Analysis**
**(Time: ~10 minutes)**

- **Purpose:**  
  Connect EDA outputs to future steps such as visualisation, statistical testing, or modelling.

- **Talking Points:**
  - Filtering and aggregating data for reuse  
  - Saving analysis-ready outputs  
  - Importance of reproducibility and clear file naming  

- **Teaching Tips:**
  - Reinforce good project structure and version control habits  
  - Highlight how EDA decisions influence later analysis quality  
  - Encourage saving intermediate results for transparency  

---

## **Wrap-Up Reflection**
**(Time: ~10 minutes)**

- **Key Takeaways:**
  - Exploratory analysis builds understanding before modelling or visualisation  
  - Descriptive statistics and grouping reveal patterns not visible in raw data  
  - Interpretation and reasoning are as important as correct code  

- **Next Steps:**  
  Learners move on to the **Exploratory Data Analysis Lab**, where they apply these concepts to a real dataset using Pandas.

---

