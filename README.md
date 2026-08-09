# 📊 Sales Data Pipeline

![Tests](https://github.com/LuanSouzaData/sales-data-pipeline/actions/workflows/tests.yml/badge.svg)

A production-oriented data pipeline built with Python for extracting, validating, transforming, and loading sales data into SQLite.

The project is being developed as a practical study in **Data Engineering**, with emphasis on data quality, modular architecture, automated testing, Git workflows, and Continuous Integration (CI).

---

## 🎯 Project Goals

This project demonstrates an end-to-end data pipeline capable of:

- Extracting sales data from CSV files
- Validating and cleaning incoming data
- Standardizing categories and customer names
- Calculating derived sales metrics
- Loading transformed data into SQLite
- Running automated unit tests with Pytest
- Validating changes automatically with GitHub Actions
- Maintaining a clean and modular project structure

---

## 🏗️ Pipeline Architecture

```text
                 ┌─────────────────┐
                 │    CSV Files    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │     Extract     │
                 │     (Pandas)    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │    Transform    │
                 │                 │
                 │ • Deduplication │
                 │ • Validation    │
                 │ • Standardizing │
                 │ • Calculations  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │      Load       │
                 │    (SQLite)     │
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

| Technology | Purpose |
|---|---|
| Python 3.13 | Main programming language |
| Pandas | Data extraction and transformation |
| SQLite | Relational database for the pipeline output |
| Pytest | Automated unit testing |
| Git | Version control |
| GitHub | Repository and collaboration |
| GitHub Actions | Continuous Integration |

---

## 📂 Project Structure

```text
sales-data-pipeline/
│
├── data/
│   └── raw/
│       └── sales_2026_08_01.csv
│
├── database/
│   └── sales.db
│
├── docs/
│   └── data_quality.md
│
├── logs/
│
├── src/
│   ├── main.py
│   │
│   └── sales_pipeline/
│       ├── __init__.py
│       ├── config.py
│       ├── extract.py
│       ├── load.py
│       ├── logger.py
│       └── transform.py
│
├── tests/
│   ├── conftest.py
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

## 🔄 Data Transformation

The transformation layer currently performs the following operations:

### 1. Remove duplicates

Duplicate sales records are identified and removed.

### 2. Validate quantity

Records with invalid quantities, such as zero or negative values, are removed.

### 3. Validate prices

Records with invalid or negative unit prices are removed.

### 4. Validate dates

Invalid dates are converted to missing values and removed from the final dataset.

### 5. Standardize categories

Category values such as:

```text
books
BOOKS
 Books
electronics
ELECTRONICS
```

are standardized into consistent values:

```text
Books
Electronics
```

### 6. Normalize customer names

Customer names are cleaned and standardized.

Missing customer names are replaced with:

```text
Unknown
```

### 7. Calculate total price

The pipeline derives the total value of each sale:

```text
total_price = quantity × unit_price
```

---

## 🗃️ Database

The transformed data is loaded into a SQLite database:

```text
database/sales.db
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

The project uses Pytest for unit testing.

The current test suite covers the transformation layer:

- `remove_duplicates()`
- `remove_invalid_quantity()`
- `remove_invalid_prices()`
- `validate_dates()`
- `standardize_categories()`
- `normalize_customer_names()`
- `calculate_total_price()`

Current result:

```text
7 passed
```

### Run the tests

From the project root:

```bash
python -m pytest -v
```

Expected result:

```text
7 passed
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
python -m pip install pytest
```

### 4. Run the pipeline

```bash
python src/main.py
```

The pipeline processes the CSV input and loads the transformed records into:

```text
database/sales.db
```

---

## 🔁 Continuous Integration

The project uses **GitHub Actions** to automatically run the test suite.

The workflow is located at:

```text
.github/workflows/tests.yml
```

Whenever changes are pushed to the configured branches or a Pull Request is opened against `main`, GitHub Actions:

1. Checks out the repository
2. Sets up Python 3.13
3. Installs the project dependencies
4. Installs Pytest
5. Runs the automated test suite

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

git add .
git commit -m "feat: describe the change"
git push origin feature/my-feature
```

A Pull Request is then opened against `main`.

After the CI checks pass, the feature can be merged.

---

## 📋 Data Quality

Data-quality rules and validation decisions are documented in:

```text
docs/data_quality.md
```

The pipeline currently handles:

- Duplicate records
- Invalid quantities
- Invalid prices
- Invalid dates
- Category inconsistencies
- Missing customer names
- Derived total prices

---

## 🗺️ Roadmap

### Completed

- [x] Project structure
- [x] CSV extraction
- [x] Data cleaning and validation
- [x] Category standardization
- [x] Customer name normalization
- [x] Total price calculation
- [x] SQLite database
- [x] Modular pipeline architecture
- [x] Unit tests with Pytest
- [x] Git feature-branch workflow
- [x] GitHub Actions CI

### Planned

- [ ] Improve test coverage
- [ ] Add integration tests for the database layer
- [ ] Add database CRUD operations
- [ ] Improve error handling and retry strategies
- [ ] Add test coverage reporting
- [ ] Containerize the application with Docker
- [ ] Add pipeline orchestration with Apache Airflow
- [ ] Introduce cloud storage with AWS S3
- [ ] Add monitoring and observability
- [ ] Expand the pipeline toward a cloud-based data platform

---

## 📚 What This Project Demonstrates

This project is designed to demonstrate practical knowledge of:

- ETL / ELT concepts
- Data cleaning and validation
- Python for Data Engineering
- Pandas
- SQL and relational databases
- SQLite
- Modular software architecture
- Unit testing
- Test fixtures
- Git and feature branches
- Conventional Commits
- Pull Requests
- Continuous Integration
- Data quality practices

---

## 👨‍💻 Author

**Luan Souza**

Data Engineering enthusiast focused on building practical projects involving data pipelines, cloud technologies, Python, SQL, and distributed data processing.

---

## 📄 License

This project is licensed under the terms defined in the `LICENSE` file.