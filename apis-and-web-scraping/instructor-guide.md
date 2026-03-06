# Module 8 — APIs and Web Scraping: Instructor Guide

**Module Time:** 120 minutes

---

## What This Module is About
This module introduces learners to external data acquisition using APIs and web scraping. Learners learn how to retrieve structured data programmatically, extract information from web pages responsibly, and prepare raw data for analysis workflows.

---

## Core Objectives
- Retrieve structured data from APIs using the Requests library
- Understand API authentication and response handling
- Extract data from HTML using BeautifulSoup
- Store raw data for analysis while respecting ethical and legal constraints

---

## Must-Hit Topics
- APIs vs Web Scraping
- HTTP requests and responses
- JSON data structures
- HTML parsing with BeautifulSoup
- Ethical and legal considerations in data collection
- Storing raw data for downstream analysis

---

## 1. APIs and Data Retrieval
**(Time: ~35 minutes)**

**Purpose:**  
Help learners understand how APIs provide structured, reliable access to external data sources.

**Talking Points:**
- What an API is and why APIs are preferred over scraping when available
- HTTP methods (GET) and response status codes
- Working with JSON responses
- Introduction to authentication concepts (API keys, headers)
- Rate limits and responsible API usage

**Teaching Tips:**
- Emphasise reading API documentation before writing code
- Show learners how to inspect a JSON response structure visually
- Reinforce that APIs are designed for data access, not websites

---

## 2. Web Scraping with BeautifulSoup
**(Time: ~35 minutes)**

**Purpose:**  
Introduce web scraping as a fallback technique when APIs are unavailable, with strong emphasis on ethics and legality.

**Talking Points:**
- When scraping is appropriate vs when it is not
- Basic HTML structure (tags, classes, ids)
- Using BeautifulSoup to parse and navigate HTML
- Extracting text and tabular data
- Checking robots.txt and terms of service

**Teaching Tips:**
- Keep scraping examples simple and controlled
- Reinforce that scraping should respect site rules and limits
- Stress that scraping raw HTML is less stable than APIs

---

## 3. Storing Raw Data for Analysis
**(Time: ~30 minutes)**

**Purpose:**  
Connect data acquisition to the broader analytics workflow by showing how raw data is stored and prepared for analysis.

**Talking Points:**
- Why raw data should be stored before cleaning or transformation
- Common formats for raw data (JSON, CSV)
- Folder structures that support reproducibility
- Linking external data acquisition to Pandas-based EDA

**Teaching Tips:**
- Reference earlier modules on reproducible project structure
- Emphasise transparency and traceability of data sources
- Encourage descriptive file naming for raw datasets

---

## Wrap-Up Reflection
**(Time: ~2 minutes)**

**Key Takeaways:**
- APIs are the preferred method for accessing structured external data when available
- Web scraping should be used responsibly and only when appropriate
- Storing raw data correctly is essential for reproducible analytics workflows

**Next Steps:**  
Learners will move into a hands-on lab where they retrieve data using APIs or scraping techniques and prepare it for exploratory analysis.

---

