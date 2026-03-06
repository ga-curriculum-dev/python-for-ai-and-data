# Lab: Loading and Processing Data with NumPy

## Exercise Overview

In this lab, you will practise loading data from common file formats and processing it efficiently using NumPy. You will work with CSV and JSON files, convert raw data into NumPy arrays, apply vectorised calculations, and save processed outputs back to disk.

The goal is to strengthen your understanding of **data input/output workflows** and **numerical performance** while maintaining a clean, reproducible project structure. 

> **Note:** This lab focuses on file input/output workflows and NumPy fundamentals, rather than complex data cleaning or analysis.


---

## Learning Goals

By completing this lab, you will:

- Load data from CSV and JSON files
- Convert raw data into NumPy arrays
- Apply vectorised operations for numerical analysis
- Save processed data to appropriate output files
- Organise your project using a reproducible folder structure
- Prepare clean, analysis-ready data for later modules
- Read from and write to external data files using reproducible, relative file paths.

---

## How to Work Through the Lab

Follow the steps below in order.  
Run each code cell as you go to confirm your results.

---

## 1. Set Up Your Project

1. Create a new project folder for this lab.
2. Inside the project, create the following structure:

```text
lab_Loading_and_Processing_Data_with_NumPy/
│
├── data/
│   ├── raw/
│   │   ├── sample_data.csv
│   │   ├── sample_data.json
│   │  
│   └── processed/
│       
│
├── notebooks/
│   └── file_formats_numpy.ipynb
│
├── solutions/
│   └── module4_file_io_solution.ipynb
│
└── README.md
```
Place the provided starter notebook into the `notebooks/` folder.

---

## 2. Loading Data from Files

You may use either the Python standard library (`csv`, `json`) or NumPy where appropriate.

Inside your notebook:

- Load a CSV file from the `data/raw/` folder
- Load a JSON file from the `data/raw/` folder
- Inspect the raw data structure and confirm it matches your expectations

### Guidance

- Focus on understanding the shape and content of the data
- Do not modify the raw files
---
## 3. Converting Data to NumPy Arrays

- Convert relevant numeric data into NumPy arrays
- Confirm the array shape and data type
- Compare this representation with using Python lists

```python
import numpy as np
```
### Checkpoint

You should now have at least one NumPy array representing numeric data loaded from a file.

---
## 4. Applying Vectorised Calculations

Using your NumPy arrays:

- Apply at least one vectorised calculation (for example, normalisation or scaling)
- Avoid explicit Python loops
- Store the result in a new NumPy array

### Reflection Prompt (Markdown Cell)

- Why is this operation easier or clearer using NumPy arrays?

---

## 5. Saving Processed Outputs

- Save your processed NumPy data to the `data/processed/` folder
- Use an appropriate file format (for example, `.npy` or `.csv`)
- Ensure filenames clearly indicate that the data is processed

For example, processed outputs may be saved as files such as `processed_data.npy` or `processed_data.csv`.

---

## 6. Documenting Your Work

Add markdown cells explaining:

- How the data was loaded
- Why NumPy arrays were used
- What calculations were applied

Create a `README.md` at the root of the project describing:

- The purpose of this lab
- The input data formats used
- The outputs produced

Clear documentation is essential for reproducible analytics workflows.

---
## Version Control and Submission

1. Open a terminal in your project folder.
2. Initialise a Git repository:

```bash
git init
git add .
git commit -m "Complete data I/O and NumPy processing lab"
```
3. Create a new repository on GitHub.
4. Push your project to GitHub:

```bash
git branch -M main
git push -u origin main
```
---

## Tips for Success

- Run cells frequently to catch issues early
- Keep raw and processed data separate
- Prefer vectorised NumPy operations over loops
- Use clear file and variable names
- Document decisions in markdown cells

---

## Deliverables

Your final submission should include:

- A completed Jupyter Notebook with code and explanations
- Loaded data from CSV and JSON formats
- NumPy-based vectorised calculations
- Saved processed outputs
- A clean and reproducible project structure
- A GitHub repository containing all files

This lab prepares you for the next module, where you will work with larger datasets and higher-level data manipulation tools.
A completed lab includes a runnable notebook that reads from CSV and JSON files and writes validated outputs to disk.

---

## Additional Resources

- NumPy Documentation: https://numpy.org/doc/
- Python File I/O: https://docs.python.org/3/tutorial/inputoutput.html
- CSV Module: https://docs.python.org/3/library/csv.html
- JSON Module: https://docs.python.org/3/library/json.html

