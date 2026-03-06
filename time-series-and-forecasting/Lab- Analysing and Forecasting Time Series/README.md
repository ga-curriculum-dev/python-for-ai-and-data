# Lab: Analyzing and Forecasting Time Series

In this lab, you will work with **time-based data** to explore trends over time and build **simple baseline forecasts**.

Building on the validated datasets and analytical insights from previous modules, you will now focus on **time series analysis**, using Pandas and NumPy to:

- Process temporal data
- Apply rolling averages
- Create baseline forecasting models
- Evaluate forecast performance using error metrics

This lab reinforces **forecasting fundamentals**, **analytical judgment**, and **responsible interpretation of predictive outputs**.

---

## Lab Objectives

By completing this lab, you will be able to:

- Process and analyze time-based data using Pandas and NumPy
- Apply rolling averages to smooth time series data
- Create simple baseline forecasts
- Evaluate forecast accuracy using **MAE** and **RMSE**
- Interpret forecast performance and limitations clearly

---

## Project Structure

Your project should follow the structure below:
```text
Lab_Time_Series_and_Forecasting/
│
├── data/
│   └── validated_dataset_m11.csv
│
├── notebooks/
│   └── time_series_forecasting_lab.ipynb
│
├── output/
│   ├── figures/
│   └── forecast_metrics.csv
│
└── README.md
```

### Folder Descriptions

**data/**  
Contains the validated dataset produced in previous modules.  
This file represents analysis-ready input data and must not be modified.

**notebooks/**  
Contains the Jupyter Notebook where you perform time series processing,  
forecasting, evaluation, and markdown-based interpretation.

**output/**  
Contains artifacts generated during the lab, including:
- Saved figures (time series plots, forecasts)
- Forecast evaluation metrics (MAE, RMSE)

Separating validated inputs from analytical outputs supports reproducibility  
and professional analytical workflows.

---

## How to Work Through the Lab

Follow the steps below in order.  
Run each cell as you go and read the markdown instructions carefully.

### 1. Set Up Your Notebook

Open the starter notebook:
```text
notebooks/time_series_forecasting_lab.ipynb
```

In the setup section, you will:

- Import required libraries (pandas, numpy, matplotlib)
- Load the dataset from `data/validated_dataset_m11.csv`
- Convert the relevant date column into a datetime format
- Set the date column as the DataFrame index

**Important:**  
Time series aggregation in Pandas (for example using `.resample()`) only works when the DataFrame index is a **DatetimeIndex**. This means you must explicitly convert the date column to datetime format and set it as the index before performing any time-based aggregation.  

If this step is skipped, Pandas will raise errors even if the dates appear to be correctly formatted.
This step ensures the data is properly structured for time series analysis.

### 2. Explore the Time Series

Before forecasting, you must understand how the data behaves over time.

You will:

- Plot the time series
- Identify trends, seasonality, or irregular patterns
- Observe potential gaps or anomalies

This exploration informs which forecasting approaches are appropriate.

### 3. Apply Rolling Averages

Rolling averages help smooth short-term fluctuations.

You will:

- Compute rolling averages (e.g., 3-period or 7-period windows)
- Compare smoothed series with the original data
- Visualize how rolling windows affect trend visibility

Rolling averages are a foundational technique in time series analysis.

### 4. Create Baseline Forecasts

Rather than complex models, you will start with simple baselines.

You may implement approaches such as:

- Naive forecast (last observed value)
- Mean-based forecast
- Rolling-average-based forecast

Baseline models provide a reference point for evaluating future improvements.

### 5. Evaluate Forecast Accuracy

Forecasts must be evaluated quantitatively.

You will compute:

- **MAE (Mean Absolute Error)** — average magnitude of forecast errors
- **RMSE (Root Mean Squared Error)** — penalizes larger errors

These metrics help you:

- Compare forecasting approaches
- Identify unstable or poor forecasts
- Communicate uncertainty responsibly

You will save evaluation results to `output/forecast_metrics.csv`.

### 6. Visualize Forecasts and Errors

Visual inspection complements numerical metrics.

You will:

- Plot actual vs forecasted values
- Visualize forecast errors over time
- Identify periods of under- or over-prediction

Visuals help contextualize model performance.

### 7. Interpret and Document Results

In markdown cells, clearly explain:

- Which baseline forecast performed best and why
- What limitations exist in the forecasting approach
- Whether the forecast would be reliable for decision-making
- What additional data or methods might improve results

Forecasting is about reasoned interpretation, not just numbers.

---

## AI Reflection Prompt

Before finalizing your submission, use an AI assistant of your choice and ask:

> "Why are simple baseline forecasts important before applying advanced time series models?"

Reflect on the response by considering:

- What baselines reveal about data behavior
- How evaluation metrics guide model selection
- The risks of jumping to complex models too early

Use this reflection to critically assess your forecasting approach.

---

## Version Control and Submission

From your project directory, initialize version control and commit your work:
```bash
git init
git add .
git commit -m "Analyze and forecast time series data"
```

Create a new repository on GitHub, then push your local project:
```bash
git branch -M main
git push -u origin main
```

---

## Tips for Success

- Always visualize time series before forecasting
- Start with simple baselines before complex models
- Interpret MAE and RMSE in context
- Avoid overconfidence in short datasets
- Clearly state assumptions and limitations

---

## Deliverables

Your final submission should include:

- A completed Jupyter Notebook with code and markdown explanations
- Time series visualizations and rolling averages
- At least one baseline forecast
- Forecast evaluation metrics (MAE and RMSE)
- Clear written interpretation of results
- A GitHub repository containing all project files

---

## Additional Resources

- **Pandas Time Series Documentation**  
  https://pandas.pydata.org/docs/user_guide/timeseries.html

- **Forecast Evaluation Metrics Explained**  
  https://www.statisticshowto.com/mean-absolute-error/

- **Time Series Forecasting Concepts**  
  https://otexts.com/fpp2/

- **Real Python — Time Series Analysis with Pandas**  
  https://realpython.com/time-series-analysis-python/
