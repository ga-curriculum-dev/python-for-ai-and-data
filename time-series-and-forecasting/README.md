# Module 13 — Time Series and Forecasting

**Session Time:** 120 minutes

---

## Prerequisites

- Python fundamentals (functions, conditionals)
- Working with Pandas DataFrames
- Exploratory Data Analysis (EDA)
- Basic statistical reasoning
- Completion of **Module 12 — Data Visualisation with Matplotlib and Seaborn**

---

## Session Breakdown

| Segment | Topic                                              | Duration (minutes) |
|-------:|----------------------------------------------------|--------------------|
| 1      | Introduction to Time Series Data                   | 15                 |
| 2      | Working with Time-Based Data in Pandas             | 20                 |
| 3      | Rolling Statistics and Trend Smoothing             | 20                 |
| 4      | Baseline Forecasting Models                        | 20                 |
| 5      | Evaluating Forecast Accuracy                       | 15                 |
|        | **Lab — Time Series Analysis & Forecasting**       | **30**             |

---
# Time Series and Forecasting

**Session Time:** 120 minutes

---

## Prerequisites

- Completed Module 11: Statistical Analysis and Inference
- Familiarity with Pandas DataFrames and basic statistical concepts

---

## Learning Objectives

By the end of this module, you'll be able to:

- Process and analyze time-based data using Pandas and NumPy
- Apply rolling statistics to smooth and interpret trends
- Build baseline forecasting models
- Evaluate forecast accuracy using MAE and RMSE
- Interpret forecasts critically and communicate uncertainty clearly

---

## What You Will Learn

In this module, you move from describing the past to reasoning about the future.

Time series analysis focuses on data collected over time, such as:

- Daily sales
- Monthly revenue
- Website traffic
- Sensor readings
- Economic indicators

You will learn how to:

- Structure time-based data correctly
- Identify patterns such as trends and variability
- Build simple, explainable forecasts
- Evaluate how reliable those forecasts actually are

The goal is not complex modeling, but sound analytical reasoning.

---

## Introduction to Time Series Data

A time series is a sequence of observations indexed by time.

Key characteristics of time series data:

- Observations are ordered
- Values may depend on previous points
- Visual patterns often matter as much as numbers

Common components include:

- **Trend** — long-term direction
- **Noise** — short-term randomness
- **Seasonality** (introduced later)

Understanding these components is essential before forecasting.

---

## Working with Time-Based Data in Pandas

Pandas provides powerful tools for handling time series.

In this module, you will learn how to:

- Parse date columns using `pd.to_datetime()`
- Set a date column as an index
- Sort and slice data chronologically
- Resample data to different time frequencies

Correct time indexing ensures that calculations and forecasts are meaningful.

---

## Rolling Statistics and Trend Smoothing

Raw time series data can be noisy.

Rolling statistics help smooth short-term fluctuations to reveal trends.

Common rolling measures include:

- Rolling mean
- Rolling median

For example, a rolling mean answers:

> "What is the average value over the last N time periods?"

Rolling statistics help:

- Reduce noise
- Highlight underlying trends
- Support visual and numerical interpretation

In the lab, you will apply rolling averages to real time series data.

---

## Baseline Forecasting Models

Before building complex models, analysts start with baseline forecasts.

Baseline models are:

- Simple
- Transparent
- Easy to interpret

Examples include:

- **Naïve forecast** — assumes the next value equals the last observed value
- **Rolling average forecast** — predicts future values using recent averages

Baseline forecasts provide a reference point:

> "Does a more complex model actually perform better than this?"

---

## Evaluating Forecast Accuracy

Forecasts must be evaluated quantitatively, not just visually.

A forecast is only useful if we can measure how far it deviates from the true values.

### Mean Absolute Error (MAE)

MAE measures the average magnitude of forecast errors.
```
MAE = (1/n) × Σ |y_true − y_predicted|
```

Key points:

- All errors are treated equally
- Easy to interpret (same units as the data)
- Stable and intuitive

MAE answers:

> "On average, how wrong is my forecast?"

### Root Mean Squared Error (RMSE)

RMSE penalizes larger errors more strongly.
```
RMSE = √[(1/n) × Σ (y_true − y_predicted)²]
```

Key points:

- Sensitive to large deviations
- Highlights instability or occasional big errors
- Useful when large mistakes matter

RMSE answers:

> "How severe are my biggest forecasting errors?"

### Why Use Both Metrics?

Using both MAE and RMSE helps you:

- Compare forecasting approaches
- Detect overfitting or instability
- Communicate uncertainty responsibly

In the lab, you will compute and interpret both metrics for baseline forecasts.

---

## Conceptual Forecasting Workflow
```mermaid
flowchart LR
  A[Time-Based Dataset] --> B[Initial Exploration]
  B --> C[Rolling Statistics]
  C --> D[Baseline Forecast]
  D --> E[MAE & RMSE Evaluation]
  E --> F[Interpretation & Conclusions]
```

---

## AI Reflection Prompt

Before starting the lab, use an AI assistant of your choice and ask:

> "Why should analysts start with simple baseline forecasts before using complex forecasting models?"

As you review the response, reflect on:

- The value of transparency in forecasting
- How baselines help detect overfitting
- Why interpretability matters in decision-making

Keep these ideas in mind as you build and evaluate forecasts in the lab.

---

## Wrap-Up Reflection

- Why is time ordering critical in forecasting analysis?
- What are the limitations of baseline forecasting models?
- How do MAE and RMSE complement each other?
- Why is forecast evaluation as important as forecast creation?

---

## Resources

- **Pandas Time Series Documentation**  
  https://pandas.pydata.org/docs/user_guide/timeseries.html

- **NumPy Documentation**  
  https://numpy.org/doc/stable/

- **Forecast Accuracy Metrics Explained**  
  https://otexts.com/fpp3/accuracy.html

- **Real Python — Time Series Analysis with Pandas**  
  https://realpython.com/time-series-analysis-python/
