# Lab: Optimising Calculations with NumPy Arrays

**Estimated Time:** 30 minutes

---

## Lab Overview

In this lab, you will explore how **NumPy arrays enable faster and more efficient numerical computations** compared to traditional Python loops.

You will implement the same calculation using both loop-based logic and vectorised NumPy operations, compare performance, and reflect on why vectorisation is essential for scalable analytics and data science workflows.

This lab strengthens your understanding of **computational efficiency**, **quantitative reasoning**, and **performance-aware coding**.

---

## Learning Goals

By the end of this lab, you will be able to:

- Perform numerical calculations using NumPy arrays  
- Compare loop-based and vectorised implementations  
- Measure and interpret performance differences  
- Optimise calculations for clarity and efficiency  
- Document results and reasoning clearly  

---

## How to Work Through the Lab

Follow the steps below **in order**.  
Run each cell as you go to confirm your code behaves as expected.

---

## 1. Set Up Your Environment

Open the starter notebook:

```
notebooks/numpy_optimisation_lab.ipynb
```

In the first code cell:

- Import NumPy  
- Import any standard libraries needed for timing or inspection  

This confirms your environment is ready for numerical computation.

---

## 2. Generate Sample Numerical Data

Create a large numerical dataset using NumPy.

You will:

- Generate a NumPy array containing numeric values  
- Inspect its shape and data type  

This dataset will be used for all subsequent calculations.

---

## 3. Loop-Based Calculation

Implement a numerical calculation **using a Python loop**.

For example:

- Squaring each value  
- Normalising values  
- Applying a simple transformation  

Store the result and ensure it produces the correct output.

**Checkpoint:**  
You should have a working calculation implemented using a loop.

---

## 4. Vectorised NumPy Calculation

Rewrite the same calculation using **NumPy vectorised operations**.

You should:

- Avoid explicit Python loops  
- Apply the operation directly to the NumPy array  
- Store the result in a new array  

Confirm that the output matches the loop-based version.

---

## 5. Compare Performance

Measure and compare the execution time of:

- The loop-based calculation  
- The vectorised NumPy calculation  

Record your observations directly in the notebook.

**Reflection prompt (markdown cell):**

- Which approach is faster?  
- Why does NumPy perform better in this case?  

---

## 6. Interpret and Document Results

Add markdown cells explaining:

- What calculation was performed  
- How the two implementations differ  
- Why vectorised operations are preferred in analytical workflows  

Clear explanation is as important as correct code.

---

## Version Control and Submission

From your project folder:

```
git init
git add .
git commit -m "Optimise numerical calculations using NumPy arrays"
```

Create a new repository on GitHub and push your work:

```
git branch -M main
git push -u origin main
```

---

## Deliverables

Your final submission should include:

- A completed Jupyter Notebook with:
  - Loop-based and vectorised implementations  
  - Performance comparison  
  - Clear explanations in markdown  
- Correct and readable NumPy-based calculations  
- A GitHub repository containing all project files  

---

## Tips for Success

- Focus on clarity before optimisation  
- Always verify correctness before comparing speed  
- Use NumPy operations instead of Python loops whenever possible  
- Explain *why* performance differs, not just *that* it does  

---

## Additional Resources

- **NumPy Documentation**  
  https://numpy.org/doc/

- **NumPy Performance Tips**  
  https://numpy.org/doc/stable/user/absolute_beginners.html#why-numpy-is-fast

- **Real Python — NumPy Array Operations**  
  https://realpython.com/numpy-array-programming/

- **GitHub Documentation**  
  https://docs.github.com
