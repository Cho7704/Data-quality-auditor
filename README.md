# Data-quality-auditor

*A lightweight, modular Python tool for auditing data integrity using Pandas*

---

##  Overview

The **Data Quality Auditor** is a Python-based tool designed to analyze and report issues in datasets, with a primary focus on **data integrity**, such as:

* Missing values
* Outliers
* Duplicate rows
* Type inconsistencies
* Column-level summaries

The project is built with clarity and maintainability in mind, following a clean, modular structure.
It is ideal for ETL validations, exploratory data analysis, or automated quality reporting.

---
##  Features (Tiles)

###  Missing Value Detection

Automatically identifies missing values per column and generates a summary report.

###  Outlier Detection

Uses z-score logic to locate abnormal numerical values.

###  Duplicate Detection

Flags duplicate rows and optionally outputs them for review.

### Column Profiling

Provides column-by-column statistics such as:

* Min / Max
* Mean / Median
* Unique counts
* Standard deviation
* Data types

###  Clean Project Architecture

Structured into reusable modules:

```
src/
 ├── main.py
 ├── auditor.py
 ├── loader.py
 ├── report.py
data/
output/
requirements.txt
README.md
```

###  Exportable Reports

Generates structured reports (JSON + CSV) including:

* Missing value summaries
* Outlier lists
* Duplicate listings
* Column profiling

---
###  Clean Project Architecture

Structured into reusable modules:

```
src/
 ├── main.py
 ├── auditor.py
 ├── loader.py
 ├── report.py
data/
output/
requirements.txt
README.md
```

###  Exportable Reports

Generates structured reports (JSON + CSV) including:

* Missing value summaries
* Outlier lists
* Duplicate listings
* Column profiling

---

##  Project Structure

```
data_quality_auditor/
│
├── data/
│    └── sample.csv        # Input dataset
│
├── output/                # All generated reports
│
├── src/
│    ├── auditor.py        # Core auditing logic
│    ├── loader.py         # Data loading utilities
│    ├── report.py         # Report export functions
│    └── main.py           # Main orchestration script
│
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### 1. Clone the project

```
git clone <your-repo-url>
cd data_quality_auditor
```

### 2. Create a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

##  Running the Auditor

Place a CSV file inside the **/data** directory.
By default, the project uses `data/sample.csv`.

Then run:

```
python src/main.py
```

Results will appear in the **/output** folder:

* `missing_values.csv`
* `outliers.csv`
* `duplicates.csv`
* `profiling.json`
* `full_report.json`
