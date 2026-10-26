# Data Engineering & Visualisation Laboratory Coursework

This repository contains practical implementations of database-driven applications, ETL pipelines, document-oriented NoSQL operations, and visual analytics using **Python**, **PostgreSQL**, **MongoDB**, **Pandas**, **SQLAlchemy**, and **Seaborn**.

---

## Catalog of Completed Practical Tasks

| Task # | Practical Title | Key Technologies | Directory Link |
| :---: | :--- | :--- | :--- |
| **Task 1** | **Development of Python-Based Employee Management System using SQL/PostgreSQL** | PostgreSQL 18, `psycopg2`, Tabulate, Seaborn | [`AnalysisOf_Employee_Management_System/`](AnalysisOf_Employee_Management_System/) |
| **Task 2** | **Build Data Pipeline to Work with Databases SQL/PostgreSQL (ETL)** | PostgreSQL 18, SQLAlchemy, Pandas, Logging | [`Build_Data_Pipeline_PostgreSQL/`](Build_Data_Pipeline_PostgreSQL/) |
| **Task 3** | **Python MongoDB Client & Collection Operations (CRUD, Replace, Aggregate)** | MongoDB 9.0, `pymongo`, Aggregation Pipeline, Seaborn | [`MongoDB_Client_Document_Operations/`](MongoDB_Client_Document_Operations/) |

---

## Task 1: Python-Based Employee Management System (SQL/PostgreSQL)
Relational 3NF tables (`departments`, `roles`, `employees`), transaction-safe CRUD operations, multi-table `INNER JOIN` queries, and visual executive payroll dashboards.  
- Directory: [`AnalysisOf_Employee_Management_System/`](AnalysisOf_Employee_Management_System/)

---

## Task 2: Build Data Pipeline to Work with Databases SQL/PostgreSQL (ETL)
Automated ETL pipeline: extracts uncleaned CSV data, cleans/deduplicates and imputes missing values in Pandas, loads into PostgreSQL via SQLAlchemy `Engine`, and validates rows with traceable logging.  
- Directory: [`Build_Data_Pipeline_PostgreSQL/`](Build_Data_Pipeline_PostgreSQL/)

---

## Task 3: Python MongoDB Client & Collection Operations (PyMongo)

### Aim & Objectives:
To create a Python-based MongoDB client using the `pymongo` module and, using a Collection object, practice the core document operations:
1. **Insert:** `insert_one()`, `insert_many()`
2. **Search:** `find_one()`, `find()` with comparison (`$gte`), logical (`$or`), regex (`$regex`), sorting, and projection
3. **Update:** `update_one()`, `update_many()` with `$set`, `$inc`, `$push`, and `upsert=True`
4. **Replace:** `replace_one()`
5. **Remove:** `delete_one()`, `delete_many()`
6. **Aggregate:** Multi-stage aggregation pipelines (`$match`, `$group`, `$sort`, `$project`, `$unwind`)
7. **Data Visualisation:** High-resolution charts of category inventory valuation, price spread box plots, and executive analytics dashboard.

### Quick Start:
```bash
cd "/home/vishvambar/Desktop/Data Visualisation/Data-Engineering/MongoDB_Client_Document_Operations"

# Run the 100% automated verification test suite:
python3 test_all_operations.py

# Launch the interactive menu CLI:
python3 main.py

# Generate/refresh high-resolution visual charts:
python3 visualize_mongodb.py
```

### Lab Reports:
- Full Academic Lab Manual: [`EXPERIMENT_3_REPORT.md`](MongoDB_Client_Document_Operations/EXPERIMENT_3_REPORT.md)
- Printable 1–2 Page Output & Evaluator Viva Report: [`OUTPUT_REPORT_SUBMISSION.md`](MongoDB_Client_Document_Operations/OUTPUT_REPORT_SUBMISSION.md)
