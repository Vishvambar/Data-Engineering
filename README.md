# Data Engineering & Visualisation Laboratory Coursework

This repository contains practical implementations of database-driven applications, ETL pipelines, document-oriented NoSQL operations, relational-like NoSQL architectures, and visual analytics using **Python**, **PostgreSQL**, **MongoDB**, **Pandas**, **SQLAlchemy**, and **Seaborn**.

---

## Catalog of Completed Practical Tasks

| Task # | Practical Title | Key Technologies | Directory Link |
| :---: | :--- | :--- | :--- |
| **Task 1** | **Development of Python-Based Employee Management System using SQL/PostgreSQL** | PostgreSQL 18, `psycopg2`, Tabulate, Seaborn | [`AnalysisOf_Employee_Management_System/`](AnalysisOf_Employee_Management_System/) |
| **Task 2** | **Build Data Pipeline to Work with Databases SQL/PostgreSQL (ETL)** | PostgreSQL 18, SQLAlchemy, Pandas, Logging | [`Build_Data_Pipeline_PostgreSQL/`](Build_Data_Pipeline_PostgreSQL/) |
| **Task 3** | **Python MongoDB Client & Collection Operations (CRUD, Replace, Aggregate)** | MongoDB 9.0, `pymongo`, Aggregation Pipeline, Seaborn | [`MongoDB_Client_Document_Operations/`](MongoDB_Client_Document_Operations/) |
| **Task 4** | **Hospital Management System Application Using Python and MongoDB Backend** | MongoDB 9.0, `pymongo`, Relational `$lookup` Joins, Seaborn | [`Hospital_Management_System_MongoDB/`](Hospital_Management_System_MongoDB/) |

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
NoSQL document operations on Collection objects: `insert_one`/`insert_many`, `find`/regex search, atomic `update_one`/`update_many` (`$set`, `$inc`, `$push`, `upsert`), `replace_one`, `delete_one`/`delete_many`, and multi-stage `$unwind` aggregation pipelines.  
- Directory: [`MongoDB_Client_Document_Operations/`](MongoDB_Client_Document_Operations/)

---

## Task 4: Hospital Management System Application (MongoDB Backend)

### Aim & Objectives:
To design, implement, and demonstrate a Python-based application that models a Hospital Management System utilizing MongoDB as a NoSQL backend database to support full CRUD across relational-like documents:
1. **Departments**: Hospital wards, locations, and bed counts.
2. **Doctors**: Specialists, consultation fees, and weekly availability.
3. **Patients**: Clinical demographics, blood groups, and admission statuses.
4. **Appointments**: Scheduling, doctor-patient linkage, and status management.
5. **Medical Reports**: Clinical diagnoses, nested prescription arrays, and lab test results.
6. **Relational `$lookup` Joins**: Reconstructing unified views and calculating departmental revenues.
7. **Visual Healthcare Dashboards**: High-resolution charts of department appointment revenues, patient demographic profiles, and hospital executive overview.

### Quick Start:
```bash
cd "/home/vishvambar/Desktop/Data Visualisation/Data-Engineering/Hospital_Management_System_MongoDB"

# Run automated 100% verification test suite:
python3 test_all_operations.py

# Launch interactive CLI control panel:
python3 main.py

# Generate visual healthcare analytics charts:
python3 visualize_hospital.py
```

### Lab Reports:
- Full Academic Lab Manual: [`EXPERIMENT_4_REPORT.md`](Hospital_Management_System_MongoDB/EXPERIMENT_4_REPORT.md)
- Printable 1–2 Page Output & Evaluator Viva Report: [`OUTPUT_REPORT_SUBMISSION.md`](Hospital_Management_System_MongoDB/OUTPUT_REPORT_SUBMISSION.md)
