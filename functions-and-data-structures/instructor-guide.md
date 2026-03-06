# Instructor Guide  
## Module 3 – Functions and Data Structures

**Module Time:** ~120 minutes

---

## What This Module Is About

In this module, learners move from linear Python scripts to modular, reusable analytical code. The focus is on defining custom functions, working with core data structures, introducing Pandas as a function-level tool for data cleaning, and validating outputs to support scalable and reproducible analytics workflows.

This module prepares learners to write clean, maintainable Python code that can be reused across projects.

---

## Core Objectives

By the end of this module, learners should be able to:

- Define and reuse custom Python functions
- Use Python data structures to manage and validate structured data
- Apply Pandas inside functions for basic data cleaning tasks
- Validate outputs using assertions
- Refactor repetitive logic into reusable utilities
- Version reusable scripts using Git and GitHub

---

## Must-Hit Topics

- Why modular code matters in analytics
- Function design best practices
- Lists, dictionaries, and tuples for structured data
- Introductory use of Pandas inside functions
- Assertions and validation
- Versioning reusable logic with Git

---

## 1. Why Functions and Modular Code Matter  
**(Time: ~20 minutes)**

**Purpose:**  
Help learners understand why copy-paste code does not scale and why functions are essential for maintainable analytics.

**Talking Points:**
- The risks of repetitive, linear scripts
- Benefits of modular code: reuse, consistency, debugging
- How functions support scalable workflows
- Connecting this idea to real-world data projects

**Teaching Tips:**
- Use real examples of repeated logic learners have already written
- Emphasise readability and maintainability over clever code
- Reinforce that functions are about clarity, not complexity

---

## 2. Defining and Reusing Functions  
**(Time: ~25 minutes)**

**Purpose:**  
Introduce function syntax and best practices for reusable analytical logic.

**Talking Points:**
- Function definition syntax (`def`)
- Parameters vs return values
- Designing functions that do one clear task
- Why explicit returns matter in analysis

**Teaching Tips:**
- Walk through a simple function live
- Ask learners what inputs and outputs should be
- Reinforce naming conventions and clarity

---

## 3. Python Data Structures for Structured Data  
**(Time: ~25 minutes)**

**Purpose:**  
Show how core data structures support validation and organisation of analytical data.

**Talking Points:**
- Lists for ordered collections
- Dictionaries for labelled records
- Tuples for fixed or immutable data
- Using data structures inside functions

**Teaching Tips:**
- Use realistic record-style examples
- Emphasise structure and validation over complexity
- Connect data structures to real datasets learners will see later

---

## 4. Intro to Pandas for Function-Based Data Cleaning  
**(Time: ~30 minutes)**

**Purpose:**  
Introduce Pandas as a supporting tool used inside functions, not as a full data-wrangling framework yet.

**Talking Points:**
- What Pandas is and why it’s widely used
- DataFrames as structured, tabular data
- Using Pandas inside functions for:
  - Loading small datasets
  - Handling missing values
  - Returning clean outputs
- Positioning Pandas as part of reusable logic

**Teaching Tips:**
- Keep Pandas usage lightweight and focused
- Avoid overwhelming learners with advanced Pandas features
- Emphasise readability and function-based design

---

## 5. Validation, Refactoring, and Lab Overview  
**(Time: ~20 minutes)**

**Purpose:**  
Prepare learners for the lab by reinforcing validation, assertions, and clean code practices.

**Talking Points:**
- Why validation matters before analysis
- Using assertions to catch errors early
- Refactoring repeated logic into utility functions
- Versioning reusable code with Git

**Teaching Tips:**
- Explain assertions as guardrails, not tests
- Encourage learners to fail early and clearly
- Connect refactoring to professional coding standards

---

## Lab: Creating Reusable Functions

**Lab Goal:**  
Learners build a small utility module containing reusable functions for data cleaning and summarising. They validate outputs using assertions, refactor repetitive code, and version their work with Git and GitHub.

**What Learners Will Do:**
- Create reusable functions in a `utils.py` file
- Work with structured records using dictionaries and lists
- Use Pandas inside functions for basic cleaning
- Validate outputs with assertions
- Organise code into starter and solution structures
- Push their work to GitHub

**Instructor Notes:**
- Encourage learners to work incrementally
- Remind them to document logic clearly
- Reinforce separation between starter code and solutions

---

## Wrap-Up Reflection  
**(Time: ~2 minutes)**

**Key Takeaways:**
- Functions are essential for scalable, maintainable analytics
- Data structures support validation and organisation
- Validating outputs improves reliability and trust in analysis

**Next Steps:**  
Learners will build on these foundations in the next module by applying their reusable logic to more complex datasets and workflows.

---

