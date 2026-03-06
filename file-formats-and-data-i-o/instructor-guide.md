**Module 4 — Instructor Guide**
===============================

**File Formats and Data I/O**

**Module Time:** 120 minutes (incl. lab)

**What This Module is About**
-----------------------------

This module introduces learners to how data moves **into and out of Python**, focusing on common file formats and reproducible data I/O workflows. It also establishes **NumPy** as a foundation for efficient numerical computing and performance-aware analysis.

**Core Objectives**

*   Understand common data file formats used in analytics projects
    
*   Read and write CSV, JSON, and NumPy array files in Python
    
*   Explain when and why to use NumPy arrays instead of Python lists
    
*   Apply vectorised operations for performance and clarity
    
*   Follow reproducible project structures for data I/O
    

**Must-Hit Topics**

*   CSV vs JSON vs NumPy binary formats
    
*   Reading and writing data safely
    
*   NumPy arrays and vectorisation
    
*   Performance implications of loops vs arrays
    
*   Reproducible folder structures
    

1\. **Understanding Data I/O and File Formats**
-----------------------------------------------

**(Time: ~20 minutes)**

*   **Purpose:**Establish why file formats and I/O decisions matter in real-world analytics workflows.
    
*   **Talking Points:**
    
    *   Data analysis starts with reading data and ends with writing results
        
    *   CSV, JSON, and NumPy formats serve different use cases
        
    *   Trade-offs between simplicity, structure, and performance
        
    *   Importance of reproducibility and transparency
        
*   **Teaching Tips:**
    
    *   Ask learners where data usually comes from in their work
        
    *   Emphasise that “file choice is a design decision”
        
    *   Reinforce that no single format is always “best”
        

2\. **Working with CSV and JSON Data**
--------------------------------------

**(Time: ~20 minutes)**

*   **Purpose:**Build comfort with loading and inspecting structured data from common formats.
    
*   **Talking Points:**
    
    *   CSV as flat, tabular data
        
    *   JSON as nested and structured data
        
    *   Reading data before analysing it
        
    *   Validating structure before computation
        
*   **Teaching Tips:**
    
    *   Encourage learners to print and inspect raw data
        
    *   Highlight how JSON structure affects downstream processing
        
    *   Reinforce separating data loading from analysis logic
        

3\. **Introduction to NumPy Arrays**
------------------------------------

**(Time: ~20 minutes)**

*   **Purpose:**Introduce NumPy as the backbone of numerical computing in Python.
    
*   **Talking Points:**
    
    *   Differences between Python lists and NumPy arrays
        
    *   Memory efficiency and data typing
        
    *   Why NumPy is foundational for pandas, SciPy, and ML libraries
        
    *   Concept of vectorised operations
        
*   **Teaching Tips:**
    
    *   Use simple numeric examples to contrast lists vs arrays
        
    *   Emphasise “arrays think in batches, not loops”
        
    *   Reinforce that NumPy is not just faster — it’s clearer
        

4\. **Vectorised Operations and Performance**
---------------------------------------------

**(Time: ~20 minutes)**

*   **Purpose:**Show how vectorisation improves performance and readability.
    
*   **Talking Points:**
    
    *   Loop-based vs vectorised computation
        
    *   Readability and error reduction
        
    *   Why performance matters at scale
        
    *   When optimisation becomes important
        
*   **Teaching Tips:**
    
    *   Avoid premature optimisation — focus on clarity first
        
    *   Frame vectorisation as a professional best practice
        
    *   Encourage learners to reason about performance, not memorise syntax
        

5\. **Lab: Loading and Processing Data with NumPy**
---------------------------------------------------

**(Time: ~30 minutes)**

*   **Purpose:**Apply file I/O and NumPy concepts in a hands-on, realistic workflow.
    
*   **Talking Points:**
    
    *   Loading data from CSV and JSON
        
    *   Converting data into NumPy arrays
        
    *   Applying vectorised calculations
        
    *   Saving processed outputs
        
    *   Maintaining a clean project structure
        
*   **Teaching Tips:**
    
    *   Remind learners to work cell by cell
        
    *   Encourage experimentation with array operations
        
    *   Reinforce reproducibility over “getting the right answer”
        

**Wrap-Up Reflection**
----------------------

**(Time: ~10 minutes)**

*   **Key Takeaways:**
    
    *   File formats shape how data is analysed and reused
        
    *   NumPy enables efficient, readable numerical computation
        
    *   Vectorised operations outperform loop-based approaches
        
    *   Reproducible I/O workflows are a professional standard
        
*   **Next Steps:**Learners will build on these skills in subsequent modules by applying NumPy-based workflows to statistical analysis and data visualisation.
