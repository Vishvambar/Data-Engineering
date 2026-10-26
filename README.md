# Data Engineering & Visualisation Laboratory Coursework

This repository contains practical implementations of database-driven applications, ETL pipelines, document-oriented NoSQL operations, relational-like NoSQL architectures, and visual analytics using **Python**, **PostgreSQL**, **MongoDB**, **Pandas**, **SQLAlchemy**, and **Seaborn**.

---

## Catalog of Completed Practical Tasks & Standalone Repositories

| Task # | Practical Title | Key Technologies | Local Directory | Standalone GitHub Repository |
| :---: | :--- | :--- | :--- | :--- |
| **Task 1** | **Development of Python-Based Employee Management System using SQL/PostgreSQL** | PostgreSQL 18, `psycopg2`, Tabulate, Seaborn | [`AnalysisOf_Employee_Management_System/`](AnalysisOf_Employee_Management_System/) | [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/Vishvambar/Employee-Management-System-PostgreSQL) |
| **Task 2** | **Build Data Pipeline to Work with Databases SQL/PostgreSQL (ETL)** | PostgreSQL 18, SQLAlchemy, Pandas, Logging | [`Build_Data_Pipeline_PostgreSQL/`](Build_Data_Pipeline_PostgreSQL/) | [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/Vishvambar/Data-Pipeline-ETL-PostgreSQL) |
| **Task 3** | **Python MongoDB Client & Collection Operations (CRUD, Replace, Aggregate)** | MongoDB 9.0, `pymongo`, Aggregation Pipeline, Seaborn | [`MongoDB_Client_Document_Operations/`](MongoDB_Client_Document_Operations/) | [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/Vishvambar/MongoDB-Client-Document-Operations) |
| **Task 4** | **Hospital Management System Application Using Python and MongoDB Backend** | MongoDB 9.0, `pymongo`, Relational `$lookup` Joins, Seaborn | [`Hospital_Management_System_MongoDB/`](Hospital_Management_System_MongoDB/) | [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/Vishvambar/Hospital-Management-System-MongoDB) |
| **Task 5** | **Data Frame Manipulation, Data Cleaning, and Feature Processing using PySpark** | Apache Spark 3.5.3, PySpark MLlib, OpenJDK 17, Parquet | [`Data_Cleaning_Feature_Processing_PySpark/`](Data_Cleaning_Feature_Processing_PySpark/) | [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/Vishvambar/PySpark-Data-Cleaning-Feature-Processing) |


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
Models a complete Hospital Management System across 5 relational-like collections (`departments`, `doctors`, `patients`, `appointments`, `medical_reports`) utilizing multi-stage `$lookup` joins and visual healthcare dashboards.  
- Directory: [`Hospital_Management_System_MongoDB/`](Hospital_Management_System_MongoDB/)
- Lab Reports: [`EXPERIMENT_4_REPORT.md`](Hospital_Management_System_MongoDB/EXPERIMENT_4_REPORT.md) | [`OUTPUT_REPORT_SUBMISSION.md`](Hospital_Management_System_MongoDB/OUTPUT_REPORT_SUBMISSION.md)

---

## Task 5: Data Frame Manipulation, Data Cleaning, and Feature Processing (PySpark)

### Aim & Objectives:
To setup a localized PySpark environment, instantiate a distributed Spark Session, construct structured DataFrames, and perform foundational operations for engineering clean, model-ready data features:
1. **Explicit Schema Enforcement**: Define `StructType` schemas to bypass costly schema inference passes.
2. **Distributed Data Cleaning**: Deduplication (`.dropDuplicates()`), string trimming/casing, outlier invalidation & Winsorization.
3. **Missing Value Imputation**: PySpark MLlib `Imputer` (median strategy for numerical features) and default categorical imputation.
4. **PySpark ML Pipeline**: 7-stage pipeline combining `StringIndexer`, `OneHotEncoder`, `VectorAssembler`, and `StandardScaler` producing 32-dimensional standardized feature vectors.
5. **Window Functions & Analytics**: Partition-based ranking (`Window.partitionBy()`), running averages, and cohort aggregations.
6. **Visual Feature Analytics**: 300 DPI publication-quality charts for missing value resolution, outlier Winsorization, and cohort economics.

### Quick Start:
```bash
cd "/home/vishvambar/Desktop/Data Visualisation/Data-Engineering/Data_Cleaning_Feature_Processing_PySpark"

# Run automated 100% verification test suite with execution benchmarks (47s):
./run.sh test

# Launch interactive CLI menu:
./run.sh

# Run end-to-end pipeline:
./run.sh pipeline

# Generate publication-grade visualizations:
./run.sh vis
```

### Lab Reports:
- Full Academic Lab Manual: [`EXPERIMENT_5_REPORT.md`](Data_Cleaning_Feature_Processing_PySpark/EXPERIMENT_5_REPORT.md)
- Printable 1–2 Page Output & Evaluator Viva Report: [`OUTPUT_REPORT_SUBMISSION.md`](Data_Cleaning_Feature_Processing_PySpark/OUTPUT_REPORT_SUBMISSION.md)

