# Module 13 — Time Series and Forecasting: Instructor Guide

**Module Time:** 120 minutes

---

## What This Module is About

This module introduces learners to analysing and forecasting time-based data using Python.  
Students learn how to structure time series correctly, apply simple forecasting techniques, and evaluate forecast accuracy using standard error metrics.

---

## Core Objectives

- Understand what makes time series data different from other datasets  
- Process and analyse time-based data using Pandas and NumPy  
- Apply rolling statistics to identify trends and smooth noise  
- Build and interpret baseline forecasting models  
- Evaluate forecast accuracy using MAE and RMSE  
- Communicate forecasts, limitations, and uncertainty clearly  

---

## Must-Hit Topics

- Time series structure and ordering  
- Date parsing and indexing in Pandas  
- Rolling averages and trend smoothing  
- Baseline forecasting concepts  
- Forecast error metrics (MAE, RMSE)  
- Interpretation and responsible communication of forecasts  

---

## 1. Introduction to Time Series Data
**(Time: ~20 minutes)**

**Purpose:**  
Help learners understand what time series data is and why time ordering fundamentally changes how analysis and forecasting work.

### Talking Points

- Definition of time series data  
- Examples of real-world time series (sales, traffic, sensor data)  
- Importance of chronological order  
- Difference between cross-sectional data and time series  
- Common components: trend, noise (seasonality introduced later)  

### Teaching Tips

- Use familiar examples (daily steps, monthly expenses, weather)  
- Emphasise that shuffling time series data breaks analysis  
- Encourage students to describe patterns verbally before coding  

---

## 2. Working with Time-Based Data & Rolling Statistics
**(Time: ~40 minutes)**

**Purpose:**  
Teach learners how to correctly prepare time-based data and apply rolling statistics to reveal trends.

### Talking Points

- Converting date columns with `pd.to_datetime()`  
- Setting a datetime index  
- Sorting and slicing time-based data  
- Why noise can obscure patterns  
- Rolling mean as a smoothing technique  
- Choosing appropriate window sizes  

### Teaching Tips

- Stress correctness of date parsing before analysis  
- Show visually how rolling averages smooth volatility  
- Ask learners what happens when the window is too small or too large  
- Reinforce that rolling statistics support interpretation, not prediction  

---

## 3. Baseline Forecasting and Accuracy Evaluation
**(Time: ~40 minutes)**

**Purpose:**  
Introduce simple forecasting approaches and teach learners how to evaluate forecasts quantitatively using error metrics.

### Talking Points

- Why analysts start with baseline forecasts  
- Naïve forecasts vs rolling average forecasts  
- Difference between prediction and explanation  
- Meaning of forecast error  
- MAE: intuition, interpretation, strengths  
- RMSE: penalising large errors, when it matters  
- Comparing models using multiple metrics  

### Teaching Tips

- Reinforce that baseline ≠ bad — it’s essential  
- Ask students which metric they would trust in different scenarios  
- Avoid formula overload — focus on interpretation  
- Emphasise uncertainty and limitations of forecasts  

---

## Wrap-Up Reflection
**(Time: ~2 minutes)**

### Key Takeaways

- Time ordering fundamentally changes how data must be analysed  
- Simple, explainable forecasts are essential before complex models  
- Forecast evaluation is as important as forecast creation  

### Next Steps

Learners move on to the **Lab — Time Series Analysis and Forecasting**, where they apply rolling statistics, build baseline forecasts, and evaluate accuracy using MAE and RMSE on real data.

---
