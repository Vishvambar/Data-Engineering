# Enterprise Data Engineering & Database Architecture Portfolio

This portfolio showcases production-ready data engineering pipelines, distributed processing architectures, relational database management systems, and NoSQL document stores built with **Python**, **Apache PySpark**, **PostgreSQL**, **MongoDB**, **SQLAlchemy**, and **Pandas**.

---

## 🏛️ Project Catalog & Standalone Repositories

| Project # | Project Title | Key Technologies | Local Directory | Standalone GitHub Repository |
| :---: | :--- | :--- | :--- | :--- |
| **Project 1** | **Python-Based Employee Management System using SQL/PostgreSQL** | PostgreSQL 18, `psycopg2`, Tabulate, Seaborn | [`AnalysisOf_Employee_Management_System/`](AnalysisOf_Employee_Management_System/) | [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/Vishvambar/Employee-Management-System-PostgreSQL) |
| **Project 2** | **Production Data Pipeline & ETL Architecture with PostgreSQL** | PostgreSQL 18, SQLAlchemy, Pandas, Logging | [`Build_Data_Pipeline_PostgreSQL/`](Build_Data_Pipeline_PostgreSQL/) | [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/Vishvambar/Data-Pipeline-ETL-PostgreSQL) |
| **Project 3** | **Python MongoDB Client & Collection Operations (CRUD, Replace, Aggregate)** | MongoDB 9.0, `pymongo`, Aggregation Pipeline, Seaborn | [`MongoDB_Client_Document_Operations/`](MongoDB_Client_Document_Operations/) | [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/Vishvambar/MongoDB-Client-Document-Operations) |
| **Project 4** | **Hospital Clinical Management System Application (MongoDB Backend)** | MongoDB 9.0, `pymongo`, Relational `$lookup` Joins, Seaborn | [`Hospital_Management_System_MongoDB/`](Hospital_Management_System_MongoDB/) | [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/Vishvambar/Hospital-Management-System-MongoDB) |
| **Project 5** | **Distributed Data Cleaning & Feature Processing using Apache PySpark** | Apache Spark 3.5.3, PySpark MLlib, OpenJDK 17, Parquet | [`Data_Cleaning_Feature_Processing_PySpark/`](Data_Cleaning_Feature_Processing_PySpark/) | [![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)](https://github.com/Vishvambar/PySpark-Data-Cleaning-Feature-Processing) |

---

## Project 1: Python-Based Employee Management System (SQL/PostgreSQL)
Relational 3NF tables (`departments`, `roles`, `employees`), transaction-safe CRUD operations, multi-table `INNER JOIN` queries, and visual executive payroll dashboards.  
- **Directory**: [`AnalysisOf_Employee_Management_System/`](AnalysisOf_Employee_Management_System/)
- **Documentation**: [`TECHNICAL_SPECIFICATION.md`](AnalysisOf_Employee_Management_System/TECHNICAL_SPECIFICATION.md) | [`BENCHMARKS_AND_VERIFICATION.md`](AnalysisOf_Employee_Management_System/BENCHMARKS_AND_VERIFICATION.md)

---

## Project 2: Production Data Pipeline & ETL Architecture (SQL/PostgreSQL)
Automated ETL pipeline: extracts uncleaned CSV data, cleans/deduplicates and imputes missing values in Pandas, loads into PostgreSQL via SQLAlchemy `Engine`, and validates rows with traceable logging.  
- **Directory**: [`Build_Data_Pipeline_PostgreSQL/`](Build_Data_Pipeline_PostgreSQL/)
- **Documentation**: [`TECHNICAL_SPECIFICATION.md`](Build_Data_Pipeline_PostgreSQL/TECHNICAL_SPECIFICATION.md) | [`BENCHMARKS_AND_VERIFICATION.md`](Build_Data_Pipeline_PostgreSQL/BENCHMARKS_AND_VERIFICATION.md)

---

## Project 3: Python MongoDB Client & Collection Operations (PyMongo)
NoSQL document operations on Collection objects: `insert_one`/`insert_many`, `find`/regex search, atomic `update_one`/`update_many` (`$set`, `$inc`, `$push`, `upsert`), `replace_one`, `delete_one`/`delete_many`, and multi-stage `$unwind` aggregation pipelines.  
- **Directory**: [`MongoDB_Client_Document_Operations/`](MongoDB_Client_Document_Operations/)
- **Documentation**: [`TECHNICAL_SPECIFICATION.md`](MongoDB_Client_Document_Operations/TECHNICAL_SPECIFICATION.md) | [`BENCHMARKS_AND_VERIFICATION.md`](MongoDB_Client_Document_Operations/BENCHMARKS_AND_VERIFICATION.md)

---

## Project 4: Hospital Clinical Management System Application (MongoDB Backend)
Models a complete Hospital Clinical Management System across 5 relational-like collections (`departments`, `doctors`, `patients`, `appointments`, `medical_reports`) utilizing multi-stage `$lookup` joins and visual healthcare dashboards.  
- **Directory**: [`Hospital_Management_System_MongoDB/`](Hospital_Management_System_MongoDB/)
- **Documentation**: [`TECHNICAL_SPECIFICATION.md`](Hospital_Management_System_MongoDB/TECHNICAL_SPECIFICATION.md) | [`BENCHMARKS_AND_VERIFICATION.md`](Hospital_Management_System_MongoDB/BENCHMARKS_AND_VERIFICATION.md)

---

## Project 5: Distributed Data Cleaning & Feature Processing (PySpark)

### Architectural Overview:
Localized high-throughput PySpark environment, distributed SparkSession orchestration, explicit `StructType` schema ingestion, statistical data cleaning, and PySpark ML feature vectorization:
1. **Explicit Schema Enforcement**: Define `StructType` schemas to bypass costly schema inference passes.
2. **Distributed Data Cleaning**: Deduplication (`.dropDuplicates()`), string trimming/casing, outlier invalidation & Winsorization.
3. **Missing Value Imputation**: PySpark MLlib `Imputer` (median strategy for numerical features) and default categorical imputation.
4. **PySpark ML Pipeline**: 7-stage pipeline combining `StringIndexer`, `OneHotEncoder`, `VectorAssembler`, and `StandardScaler` producing 32-dimensional standardized feature vectors.
5. **Window Functions & Analytics**: Partition-based ranking (`Window.partitionBy()`), running averages, and cohort aggregations.
6. **Visual Feature Analytics**: 300 DPI publication-quality charts for missing value resolution, outlier Winsorization, and cohort economics.

### Quick Start:
```bash
cd "Data_Cleaning_Feature_Processing_PySpark"

# Run automated 100% verification test suite with execution benchmarks:
./run.sh test

# Launch interactive CLI menu:
./run.sh

# Run end-to-end pipeline:
./run.sh pipeline

# Generate publication-grade visualizations:
./run.sh vis
```

### Engineering Documentation:
- Technical Specification & Architecture: [`TECHNICAL_SPECIFICATION.md`](Data_Cleaning_Feature_Processing_PySpark/TECHNICAL_SPECIFICATION.md)
- Production Verification & Benchmark Report: [`BENCHMARKS_AND_VERIFICATION.md`](Data_Cleaning_Feature_Processing_PySpark/BENCHMARKS_AND_VERIFICATION.md)
