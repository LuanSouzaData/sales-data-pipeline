# 📊 Sales Data Pipeline

![Tests](https://github.com/LuanSouzaData/sales-data-pipeline/actions/workflows/tests.yml/badge.svg)

A production-oriented data pipeline built with Python for extracting, validating, transforming, and loading sales data into SQLite.

The project is being developed as a practical study in **Data Engineering**, with emphasis on data quality, modular architecture, automated testing, Git workflows, and Continuous Integration (CI).

---

## 🎯 Project Goals

This project demonstrates an end-to-end data pipeline capable of:

* Extracting sales data from CSV files
* Validating and cleaning incoming data
* Removing duplicate sales records
* Validating quantities, prices, and dates
* Standardizing categories
* Normalizing customer names
* Calculating derived sales metrics
* Loading transformed data into SQLite
* Updating existing records through an upsert strategy
* Rolling back database transactions when loading fails
* Running automated tests with Pytest
* Validating changes automatically with GitHub Actions
* Maintaining a clean and modular project structure

---

## 🏗️ Pipeline Architecture

```text
                 ┌─────────────────┐
                 │    CSV Files    │
                 │   data/raw/     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │     Extract     │
                 │     Pandas      │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │    Transform    │
                 │                 │
                 │ • Deduplication │
                 │ • Validation    │
                 │ • Standardizing │
                 │ • Normalization │
                 │ • Calculations  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │      Load       │
                 │     SQLite      │
                 │                 │
                 │ • Upsert        │
                 │ • Transactions  │
                 │ • Rollback      │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   sales.db      │
                 │     SQLite      │
                 └─────────────────┘

                    Automated CI
                         │
                         ▼
                 ┌─────────────────┐
                 │ GitHub Actions  │
                 │     Pytest      │
                 └─────────────────┘
```

---

## 🧰 Technologies

| Technology     | Purpose                                 |
| -------------- | --------------------------------------- |
| Python 3.13    | Main programming language               |
| Pandas         | Data extraction and transformation      |
| SQLite         | Relational database for pipeline output |
| Pytest         | Automated testing                       |
| Git            | Version control                         |
| GitHub         | Repository and collaboration            |
| GitHub Actions | Continuous Integration                  |

---

## 📂 Project Structure

```text
sales-data-pipeline/
│
├── data/
│   ├── processed/
│   └── raw/
│       └── sales_2026_08_01.csv
│
├── database/
│   ├── sales.db
│   └── schema.sql
│
├── docs/
│   └── data_quality.md
│
├── logs/
│   └── pipeline.log
│
├── src/
│   ├── main.py
│   │
│   └── sales_pipeline/
│       ├── __init__.py
│       ├── config.py
│       ├── database.py
│       ├── extract.py
│       ├── load.py
│       ├── logger.py
│       └── transform.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_extract.py
│   ├── test_load.py
│   └── test_transform.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── .gitignore
├── LICENSE
├── pyproject.toml
├── pytest.ini
├── README.md
└── requirements.txt
```

---

## 🔄 Data Pipeline

The pipeline follows an **Extract → Transform → Load (ETL)** architecture.

### Extract

The extraction layer reads all CSV files from:

```text
data/raw/
```

The files are loaded into Pandas DataFrames and combined into a single dataset.

If no CSV files are found, the pipeline raises a `FileNotFoundError`.

---

### Transform

The transformation layer applies a sequence of data-quality and business rules.

#### 1. Remove duplicates

Duplicate sales are identified using the `sale_id` column.

Only one record for each `sale_id` is retained.

#### 2. Validate quantity

Records with quantities less than or equal to zero are removed.

```text
quantity > 0
```

#### 3. Validate prices

Records with unit prices less than or equal to zero are removed.

```text
unit_price > 0
```

#### 4. Validate dates

The `date` column is converted to a datetime representation.

Invalid dates are converted to missing values and removed.

#### 5. Standardize categories

Category values are normalized by removing surrounding whitespace and converting text to lowercase before applying the standard category mapping.

Examples:

```text
books
BOOKS
 Books
electronics
ELECTRONICS
```

are standardized to:

```text
Books
Electronics
```

#### 6. Normalize customer names

Customer names are cleaned by:

* Removing unnecessary whitespace
* Standardizing capitalization
* Replacing missing names with `Unknown`

Examples:

```text
" ana silva "  →  "Ana Silva"
"CARLOS SOUZA" →  "Carlos Souza"
None            →  "Unknown"
```

#### 7. Calculate total price

The pipeline derives the total value of each sale:

```text
total_price = quantity × unit_price
```

The transformation functions operate on copies of the input DataFrame to avoid unintentionally mutating the original dataset.

---

### Load

The loading layer stores the transformed data in SQLite.

The destination database is:

```text
database/sales.db
```

Records are inserted using a parameterized SQL statement.

The pipeline uses an **upsert** strategy based on `sale_id`:

* New `sale_id` values are inserted.
* Existing `sale_id` values are updated.

Database transactions are committed after a successful load.

If an error occurs during the operation, the transaction is rolled back and the exception is propagated.

---

## 🗃️ Database

The pipeline uses SQLite as the relational storage layer.

The database schema is defined in:

```text
database/schema.sql
```

The main table is:

```sql
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    customer_name TEXT NOT NULL,
    category TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    total_price REAL NOT NULL
);
```

The database can be inspected using tools such as DBeaver or the SQLite command-line interface.

---

## 🧪 Automated Tests

The project uses **Pytest** for automated testing.

The current test suite contains **13 tests** covering the main pipeline components.

### Extract tests

`tests/test_extract.py`

* Extract multiple CSV files
* Handle missing CSV files

### Transform tests

`tests/test_transform.py`

* Remove duplicate sales
* Remove invalid quantities
* Remove invalid prices
* Validate dates
* Standardize categories
* Normalize customer names
* Calculate total prices
* Validate the complete transformation pipeline

### Load tests

`tests/test_load.py`

* Load transformed records into SQLite
* Update existing records using upsert
* Roll back transactions when loading fails

### Run the tests

From the project root:

```bash
python -m pytest -v
```

Current result:

```text
13 passed
```

---

## 🚀 Running the Pipeline

### 1. Clone the repository

```bash
git clone https://github.com/LuanSouzaData/sales-data-pipeline.git
cd sales-data-pipeline
```

### 2. Create a virtual environment

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

The project dependencies, including Pytest, are defined in:

```text
requirements.txt
```

### 4. Run the pipeline

```bash
python src/main.py
```

The pipeline reads CSV files from:

```text
data/raw/
```

and loads the transformed records into:

```text
database/sales.db
```

Application logs are written to:

```text
logs/pipeline.log
```

---

## 🔁 Continuous Integration

The project uses **GitHub Actions** to automatically execute the test suite.

The workflow is located at:

```text
.github/workflows/tests.yml
```

Whenever changes are pushed to the configured branches or a Pull Request is opened against `main`, GitHub Actions:

1. Checks out the repository
2. Sets up Python 3.13
3. Installs project dependencies
4. Runs the automated test suite
5. Reports the test result

The badge at the top of this README reflects the current status of the CI workflow.

---

## 🌿 Git Workflow

The project follows a feature-branch workflow.

Example:

```bash
git checkout main
git pull origin main

git checkout -b feature/my-feature
```

After implementing and testing the feature:

```bash
python -m pytest -v

git status
git diff

git add .
git commit -m "feat: describe the change"
git push origin feature/my-feature
```

A Pull Request is then opened against `main`.

After the CI checks pass, the feature can be merged.

### Commit Convention

The project follows **Conventional Commits**.

Examples:

```text
feat: add new pipeline functionality
fix: handle invalid sales records
test: add pipeline tests
refactor: simplify transformation logic
docs: update README
chore: update dependencies
```

Small, focused commits are preferred so that each change has a clear purpose.

---

## 📋 Data Quality

Data-quality rules and validation decisions are documented in:

```text
docs/data_quality.md
```

The pipeline currently handles:

* Duplicate records
* Invalid quantities
* Invalid prices
* Invalid dates
* Category inconsistencies
* Missing customer names
* Derived total prices

The transformation layer is designed to produce a clean and standardized dataset before it reaches the database.

---

## 🗺️ Roadmap

### Completed

* [x] Project structure
* [x] CSV extraction
* [x] Data cleaning and validation
* [x] Duplicate removal
* [x] Quantity validation
* [x] Price validation
* [x] Date validation
* [x] Category standardization
* [x] Customer name normalization
* [x] Total price calculation
* [x] SQLite database
* [x] SQLite upsert behavior
* [x] Transaction rollback
* [x] Modular ETL architecture
* [x] Automated tests with Pytest
* [x] Extract tests
* [x] Transform tests
* [x] Load tests
* [x] Git feature-branch workflow
* [x] Conventional Commits
* [x] GitHub Actions CI

### Planned

* [ ] Expand integration tests for the complete ETL flow
* [ ] Improve error handling and retry strategies
* [ ] Add test coverage reporting
* [ ] Improve data validation and schema enforcement
* [ ] Containerize the application with Docker
* [ ] Add pipeline orchestration with Apache Airflow
* [ ] Introduce cloud storage with AWS S3
* [ ] Add monitoring and observability
* [ ] Expand the pipeline toward a cloud-based data platform

---

## 📚 What This Project Demonstrates

This project is designed to demonstrate practical knowledge of:

* ETL / ELT concepts
* Data extraction
* Data cleaning and validation
* Data quality practices
* Python for Data Engineering
* Pandas
* SQL
* SQLite
* Modular software architecture
* Automated testing
* Test fixtures
* Database transactions
* Upsert strategies
* Git and feature branches
* Conventional Commits
* Pull Requests
* Continuous Integration
* GitHub Actions

---

## 👨‍💻 Author

**Luan Souza**

Data Engineering enthusiast focused on building practical projects involving data pipelines, cloud technologies, Python, SQL, and distributed data processing.

---

## 📄 License

This project is licensed under the terms defined in the `LICENSE` file.
