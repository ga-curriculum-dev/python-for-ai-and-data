# Cleaning and Transforming Data with Pandas — Instructor Guide

**Module Time:** 120 minutes

---

## What This Module is About

This module introduces learners to practical data wrangling with Pandas, focusing on inspecting, cleaning, and transforming real-world datasets into analysis-ready tables.

---

## Core Objectives

- Understand why data wrangling is a critical step in analysis
- Inspect DataFrames to assess data quality and structure
- Handle missing values and duplicates appropriately
- Transform and standardize fields for consistent analysis
- Prepare a clean dataset and explain cleaning choices clearly

---

## Must-Hit Topics

- DataFrame inspection (head, info, describe)
- Data quality checks and common issues
- Missing data strategies
- Duplicate detection and handling
- Transformations and standardization (types, categories, strings)
- Preparing a final "analysis-ready" dataset

---

## 1. Introduction to Data Wrangling with Pandas

**(Time: ~15 minutes)**

**Purpose:**  
Frame data wrangling as a necessary step for turning raw data into trustworthy analysis.

**Talking Points:**

- What "data wrangling" means in practice
- Why real datasets are messy (missing values, inconsistent labels, duplicates)
- Cleaning decisions affect conclusions (business logic matters)
- Pandas as the standard tool for tabular data workflows

**Teaching Tips:**

- Ask: "What's the messiest dataset you've ever seen?"
- Emphasize that wrangling is about quality and trust, not perfection
- Reinforce: "Explain your decisions like an analyst"

---

## 2. Inspecting DataFrames and Data Quality

**(Time: ~20 minutes)**

**Purpose:**  
Build a habit of inspecting data before modifying it.

**Talking Points:**

- Load the dataset and inspect shape, columns, and dtypes
- Quick scans: `head()`, `tail()`, `sample()`
- Structure checks: `info()`, missingness, unexpected types
- Basic profiling: `describe()` and value counts
- Identifying "red flags" early

**Teaching Tips:**

- Encourage learners to narrate what they observe ("What stands out?")
- Highlight that assumptions about data schema often break
- Tie inspection to avoiding downstream debugging

---

## 3. Handling Missing Data and Duplicates

**(Time: ~20 minutes)**

**Purpose:**  
Teach learners to handle missingness and duplicates using context-appropriate strategies.

**Talking Points:**

- Types of missingness (true missing vs unknown vs invalid)
- Options: drop, fill, impute, flag (and when each is appropriate)
- Finding duplicates and deciding what "duplicate" means
- Using checks to confirm cleaning impact (before/after row counts)

**Teaching Tips:**

- Ask learners: "What would a stakeholder prefer here?"
- Reinforce that "dropping data" is a decision that must be justified
- Encourage saving a copy before destructive operations

---

## 4. Transforming and Standardizing Data

**(Time: ~25 minutes)**

**Purpose:**  
Show how transformations create consistency and make analysis possible.

**Talking Points:**

- Standardizing text fields (trim, case normalization)
- Converting data types safely (strings → numbers, dates)
- Creating derived columns (e.g., revenue metrics)
- Consistent category values (typos, casing, synonyms)
- Business logic decisions (e.g., excluding returns when summarizing revenue)

**Teaching Tips:**

- Emphasize: transform for analysis needs, not aesthetics
- Encourage learners to verify results after each transformation
- Tie each transform to "What question are we trying to answer?"

---

## 5. Preparing Data for Analysis + Lab Preview

**(Time: ~10 minutes)**

**Purpose:**  
Connect the wrangling steps into a single pipeline and set expectations for the lab.

**Talking Points:**

- What "analysis-ready" means: consistent schema, validated values, documented choices
- Quick recap: inspect → clean missing/dupes → transform → validate
- Preview lab deliverables and workflow
- Remind learners to work cell-by-cell in order

**Teaching Tips:**

- Show a "before vs after" snapshot conceptually (rows/columns/types)
- Clarify what the lab is not (not perfection; not auto-fixing everything)
- Encourage Markdown explanations alongside code

---

## 6. Lab — Cleaning and Transforming Data in Pandas

**(Time: ~30 minutes)**

**Purpose:**  
Apply Pandas wrangling skills end-to-end on a realistic dataset.

**Talking Points:**

- Use inspection to identify issues
- Apply missing-data and duplicate handling decisions
- Standardize and transform fields for analysis
- Validate the output and document reasoning

**Teaching Tips:**

- Encourage learners to run cells in order
- If learners get stuck: return to inspection (`info`, `value_counts`)
- Reinforce documenting decisions (especially filters and exclusions)

---

## Wrap-Up Reflection

**(Time: ~2 minutes)**

**Key Takeaways:**

- Inspection first: understand the dataset before changing it
- Cleaning decisions must be justified and validated
- Transformations standardize data for trustworthy analysis

**Next Steps:**  
Learners will build on these wrangling skills by comparing loop-based approaches to vectorized NumPy operations and measuring performance tradeoffs.

---
