# 🛒 End-to-End E-Commerce Supply Chain ETL Pipeline

> A fully automated data pipeline processing 99,441 e-commerce orders using Python, SQL, PySpark, SQLite and Tableau.

## 📊 Key Findings


| KPI | Result |
|-----|--------|
| Total Orders | 99,441 |
| Delivery Success Rate | 97.02% |
| Average Delivery | 11.87 days EARLY |
| Top Category | Health & Beauty — R$1,258,681 |
| Data Period | 25 months (2016–2018) |

## 🏗 Pipeline Architecture

Raw CSVs → Python Ingest → Clean & Transform → SQLite DB → Tableau Dashboard → Automated Daily

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Core pipeline scripting |
| pandas | Data cleaning and transformation |
| PySpark | Large-scale aggregation |
| SQL / SQLite | KPI queries and storage |
| Tableau | Interactive dashboard |
| schedule | Daily automation |
| GitHub | Version control |

## 🔍 Key Insights

- Health & Beauty is #1 revenue category at R$1,258,681
- 97.02% of all orders delivered successfully
- Orders arrive 11.87 days early on average
- Order volume grew 30x from 2016 to 2018
- Only 0.63% of orders cancelled

## ▶ How to Run

1. Clone the repo:
git clone https://github.com/AzmeeraManjula/ecommerce-etl-pipeline.git

2. Install dependencies:
pip install pandas sqlalchemy pyspark schedule

3. Run pipeline:
python scripts/02_transform.py
python scripts/03_pyspark_transform.py
python scripts/04_load.py

4. Run automation:
python scripts/05_automate.py

## 👩‍💼 Author

Azmeera Manjula
MBA – Business Analytics | ISBR Business School, Bengaluru
Email: manjulaazmeera2@gmail.com
GitHub: https://github.com/AzmeeraManjula






