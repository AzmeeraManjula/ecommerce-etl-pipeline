python -c "
readme = open('README.md', 'w', encoding='utf-8')
readme.write('''# \U0001f6d2 End-to-End E-Commerce Supply Chain ETL Pipeline

> A fully automated data pipeline processing 99,441 e-commerce orders using Python, SQL, PySpark, SQLite and Tableau.

![Dashboard](dashboard.png)

---

## \U0001f4ca Key Findings

| KPI | Result |
|-----|--------|
| \U0001f4e6 Total Orders | 99,441 |
| \u2705 Delivery Success Rate | 97.02% |
| \u23f1 Average Delivery | 11.87 days EARLY |
| \U0001f3c6 Top Category | Health and Beauty - R\$1,258,681 |
| \U0001f4c5 Data Period | 25 months (2016-2018) |

---

## \U0001f3d7 Pipeline Architecture

\`\`\`
Raw CSVs --> Python Ingest --> Clean and Transform --> SQLite DB --> Tableau Dashboard --> Automated Daily
\`\`\`

---

## \U0001f6e0 Technology Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.11 | Core pipeline scripting |
| pandas | 3.0.3 | Data cleaning and transformation |
| PySpark | 3.5.1 | Large-scale data aggregation |
| SQL / SQLite | - | Database queries and KPI computation |
| sqlalchemy | - | Python-to-database connection |
| Tableau | 2026.1 | Interactive dashboard visualization |
| schedule | 1.2.2 | Automated daily pipeline execution |
| Git / GitHub | - | Version control and portfolio hosting |

---

## \U0001f4c1 Dataset

| Property | Detail |
|----------|--------|
| Name | Brazilian E-Commerce Public Dataset by Olist |
| Source | https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce |
| Volume | 100,000 orders across 9 CSV files (45 MB) |
| Period | September 2016 - October 2018 |
| Domain | E-Commerce / Supply Chain / Logistics |

### 9 Source Files

| File | Contents |
|------|----------|
| olist_orders_dataset.csv | Master orders - status, timestamps, delivery dates |
| olist_customers_dataset.csv | Customer city, state, unique ID |
| olist_order_items_dataset.csv | Product IDs, prices, freight values |
| olist_products_dataset.csv | Product details and category names |
| olist_sellers_dataset.csv | Seller location and ID |
| olist_order_payments_dataset.csv | Payment type and value |
| olist_order_reviews_dataset.csv | Customer satisfaction scores |
| olist_geolocation_dataset.csv | Zip codes mapped to coordinates |
| product_category_name_translation.csv | Portuguese to English categories |

---

## \U0001f4c2 Folder Structure

\`\`\`
ecommerce-etl-pipeline/
|-- scripts/
|   |-- 02_transform.py
|   |-- 03_pyspark_transform.py
|   |-- 04_load.py
|   |-- 05_automate.py
|-- sql/
|   |-- 01_data_validation.sql
|-- data/processed/
|   |-- orders_clean.csv
|   |-- kpi_category_revenue.csv
|   |-- kpi_order_status.csv
|   |-- kpi_monthly_orders.csv
|-- docs/
|   |-- Workflow_Spec_Doc_Manjula.docx
|-- .gitignore
|-- README.md
\`\`\`

---

## \u25b6 How to Run

### 1. Clone the repository
\`\`\`bash
git clone https://github.com/AzmeeraManjula/ecommerce-etl-pipeline.git
cd ecommerce-etl-pipeline
\`\`\`

### 2. Install dependencies
\`\`\`bash
pip install pandas sqlalchemy pyspark schedule openpyxl
\`\`\`

### 3. Download dataset
Download from Kaggle and place all 9 CSV files in dataraw/archive/

### 4. Run pipeline step by step
\`\`\`bash
python scripts/02_transform.py
python scripts/03_pyspark_transform.py
python scripts/04_load.py
\`\`\`

### 5. Run automated pipeline
\`\`\`bash
python scripts/05_automate.py
\`\`\`
Runs pipeline once immediately, then daily at 8:00 AM

---

## \U0001f4c8 Tableau Dashboard

| Chart | Type | Insight |
|-------|------|---------|
| Top 10 Categories by Revenue | Bar Chart | Health and Beauty leads at R\$1.25M |
| Order Status Distribution | Pie Chart | 97.02% delivered successfully |
| Monthly Orders Trend | Line Chart | 30x growth over 25 months |

---

## \U0001f50d Key Insights

- \U0001f947 Health and Beauty is #1 revenue category at R\$1,258,681
- \u2705 97.02% of all orders delivered successfully
- \u23f0 Orders arrive 11.87 days early on average
- \U0001f4c8 Order volume grew 30x from Sep 2016 to Sep 2018
- \u274c Only 0.63% of orders cancelled

---

## \U0001f5fa Pipeline Specification

Full workflow specification in docs/Workflow_Spec_Doc_Manjula.docx

Covers:
- \u2705 Project objectives and scope
- \u2705 Data source documentation
- \u2705 Pipeline architecture (7 stages)
- \u2705 KPI definitions and targets
- \u2705 Technology stack justification
- \u2705 7-day project timeline

---

## \U0001f469\u200d\U0001f4bc Author

**Azmeera Manjula**
MBA - Business Analytics | ISBR Business School, Bengaluru
\U0001f4e7 manjulaazmeera2@gmail.com
\U0001f419 https://github.com/AzmeeraManjula

---

## \U0001f4c4 License

This project uses the Olist Brazilian E-Commerce Dataset
available under CC BY-NC-SA 4.0 license.
''')
readme.close()
print('README created!')
"