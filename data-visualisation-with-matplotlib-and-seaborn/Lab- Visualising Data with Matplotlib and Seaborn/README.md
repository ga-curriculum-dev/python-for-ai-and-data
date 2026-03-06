# Lab: Data Visualization with Matplotlib and Seaborn

In this lab, you will focus on communicating analytical insights visually using Matplotlib and Seaborn.

Building on the correlation and regression analysis performed in Module 11, you will transform statistical findings into clear, professional data visualizations that support interpretation and decision-making.

Rather than discovering new relationships, the goal of this lab is to communicate existing insights effectively, applying visual design principles, exporting figures, and critically evaluating how visual choices influence interpretation.

This lab strengthens data storytelling, visual communication, and analytical judgment.

---

## Lab Objectives

By completing this lab, you will be able to:

- Create professional data visualizations using Matplotlib and Seaborn
- Choose appropriate chart types to communicate statistical relationships
- Apply visual design principles to improve clarity and readability
- Export and version visual assets for reporting and reuse
- Critically evaluate visualizations for effectiveness and potential misinterpretation

---

## Project Structure

Your project should follow the structure below:
```text
Lab_Data_Visualization/
│
├── data/
│   └── validated_dataset_m11.csv
│
├── notebooks/
│   └── data_visualization_lab.ipynb
│
├── output/
│   └── figures/
│       ├── chart_1.png
│       ├── chart_2.png
│
└── README.md
```
## Contents
- Starter notebook
- Dataset used in the lab
- `output/figures/` folder for saved charts

## Notes
Plots are saved to `output/figures` and the folder will be created automatically by the notebook.

---
### Folder Descriptions

**data/**  
Contains the validated dataset produced and analyzed in Module 11.  
This file represents analysis-ready input data and must not be modified.

**notebooks/**  
Contains the Jupyter Notebook where you create visualizations,  
apply styling, and document interpretation in markdown.

**output/**  
Contains exported visual assets generated during the lab, including:
- PNG figures created with Matplotlib or Seaborn

Separating validated inputs from visual outputs supports reproducibility  
and professional reporting workflows.

---

## How to Work Through the Lab

Follow the steps below in order.  
Run each cell as you go and read the markdown instructions carefully.

### 1. Set Up Your Notebook

Open the starter notebook:
```text
notebooks/data_visualization_lab.ipynb
```

In the setup section, you will:
- Import required libraries (pandas, matplotlib, seaborn)
- Load the validated dataset from `data/validated_dataset_m11.csv`
- Perform a quick inspection to recall dataset structure and key variables

This step reconnects you with the data and the relationships identified in Module 11.

### 2. Choose Appropriate Visualizations

Before plotting, think critically about what you want to communicate.

You will:
- Identify key relationships previously analyzed using correlation or regression
- Decide which chart types are appropriate (scatter plots, regression plots, distributions)
- Consider the intended audience and analytical purpose

This step reinforces that visualization choices are analytical decisions, not just technical ones.

### 3. Create Visualizations with Matplotlib

Using Matplotlib, you will:
- Create foundational charts (scatter plots, line plots, histograms)
- Label axes clearly and add informative titles
- Adjust figure size, scale, and layout for readability

Focus on clarity before complexity.

### 4. Enhance Visuals with Seaborn

Using Seaborn, you will:
- Create higher-level statistical visualizations (e.g., regression plots, boxplots)
- Compare groups visually using color and layout
- Leverage Seaborn's default aesthetics for cleaner presentation

Compare how Seaborn differs from raw Matplotlib in expressiveness and ease of use.

### 5. Apply Visual Design Principles

For each visualization, consider:
- Is the chart easy to read at a glance?
- Are colors used meaningfully and consistently?
- Is unnecessary visual clutter removed?
- Does the chart support the analytical message from Module 11?

You will refine at least one plot to improve clarity and interpretability.

### 6. Export and Save Figures

Once satisfied with your visualizations:
- Export key figures as PNG files
- Save them in the `output/figures/` folder
- Use clear, descriptive filenames

These figures should be suitable for inclusion in reports or presentations.

### 7. Critique and Document Visualizations

In markdown cells, clearly explain:
- What each visualization shows
- Why the chosen chart type is appropriate
- Any limitations or potential misinterpretations
- How the visual supports (or challenges) the statistical findings from Module 11

Strong visuals are always paired with strong explanations.

---

## AI Reflection Prompt

Before finalizing your submission, use an AI assistant of your choice and ask:

> "What makes a data visualization misleading, even when the data itself is correct?"

Reflect on the response by considering:
- How design choices influence interpretation
- Which risks you consciously avoided in your charts
- How visual clarity supports ethical data communication

Use this reflection to critically review your own visualizations.

---

## Version Control and Submission

From your project directory, initialize version control and commit your work:
```bash
git init
git add .
git commit -m "Create professional data visualizations"
```

Create a new repository on GitHub, then push your local project:
```bash
git branch -M main
git push -u origin main
```

---

## Tips for Success

- Design visuals to support interpretation, not decoration
- Avoid misleading scales, colors, or annotations
- Use consistency across charts when comparing results
- Always pair visuals with written explanation
- Think about how a non-technical audience might interpret each chart

---

## Deliverables

Your final submission should include:
- A completed Jupyter Notebook with code and markdown explanations
- Professional visualizations created with Matplotlib and Seaborn
- At least two exported figures saved in `output/figures/`
- Clear written interpretation linking visuals to statistical findings
- A GitHub repository containing all project files

---

## Additional Resources

- **Matplotlib Documentation**  
  https://matplotlib.org/stable/

- **Seaborn Documentation**  
  https://seaborn.pydata.org/

- **Pandas User Guide — Visualization**  
  https://pandas.pydata.org/docs/user_guide/visualization.html

- **Data Visualization Best Practices**  
  https://www.data-to-viz.com/

- **Storytelling with Data**  
  https://www.storytellingwithdata.com/
