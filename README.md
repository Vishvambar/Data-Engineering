# Data Engineering & Visualisation Laboratory Coursework

This repository contains practical implementations of database-driven applications, ETL pipelines, and visual analytics using **Python**, **PostgreSQL**, **Pandas**, **SQLAlchemy**, and **Seaborn**.

---

## Catalog of Completed Practical Tasks

| Task # | Practical Title | Key Technologies | Directory Link |
| :---: | :--- | :--- | :--- |
| **Task 1** | **Development of Python-Based Employee Management System using SQL/PostgreSQL** | PostgreSQL 18, `psycopg2`, Tabulate, Seaborn | [`AnalysisOf_Employee_Management_System/`](AnalysisOf_Employee_Management_System/) |
| **Task 2** | **Build Data Pipeline to Work with Databases SQL/PostgreSQL (ETL)** | PostgreSQL 18, SQLAlchemy, Pandas, Logging | [`Build_Data_Pipeline_PostgreSQL/`](Build_Data_Pipeline_PostgreSQL/) |

---

## Task 2: Build Data Pipeline to Work with Databases SQL/PostgreSQL

### Aim & Objectives
To design and implement an automated Python ETL data pipeline that extracts uncleaned data from a CSV source, performs data cleaning and transformation in Pandas, loads it into a PostgreSQL relational database using an SQLAlchemy engine, and verifies loaded records with traceable logging.

### Pipeline Architecture:
$$\text{CSV File} \xrightarrow{\quad\text{EXTRACT}\quad} \text{Raw DataFrame (23 rows)} \xrightarrow{\quad\text{TRANSFORM}\quad} \text{Cleaned DataFrame (20 rows)} \xrightarrow{\quad\text{LOAD}\quad} \text{PostgreSQL (students\_cleaned)} \xrightarrow{\quad\text{VERIFY}\quad} \text{SQL Validation Query}$$

### Quick Start:
```bash
cd "/home/vishvambar/Desktop/Data Visualisation/Data-Engineering/Build_Data_Pipeline_PostgreSQL"

# Run the full automated ETL pipeline:
python3 etl_pipeline.py

# Launch interactive CLI control panel:
python3 main.py

# Generate pipeline data quality & visual analytics charts:
python3 visualize_pipeline.py
```

### Lab Reports:
- Full Academic Lab Manual: [`EXPERIMENT_2_REPORT.md`](Build_Data_Pipeline_PostgreSQL/EXPERIMENT_2_REPORT.md)
- Printable 1–2 Page Output & Evaluator Viva Report: [`OUTPUT_REPORT_SUBMISSION.md`](Build_Data_Pipeline_PostgreSQL/OUTPUT_REPORT_SUBMISSION.md)
