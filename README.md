python -c "
content = '''# 🛒 End-to-End E-Commerce Supply Chain ETL Pipeline

> A fully automated data pipeline processing 99,441 e-commerce orders using Python, SQL, PySpark, SQLite and Tableau.

---

## 📊 Key Findings

| KPI | Result |
|-----|--------|
| 📦 Total Orders | 99,441 |
| ✅ Delivery Success Rate | 97.02% |
| ⏱ Average Delivery | 11.87 days EARLY |
| 🏆 Top Category | Health and Beauty - R\$1,258,681 |
| 📅 Data Period | 25 months (2016-2018) |

---

## 🏗 Pipeline Architecture

---

## 🛠 Technology Stack

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

## 📁 Dataset

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

## 📂 Folder Structure

---

## ▶ How to Run

### 1. Clone the repository

### 2. Install dependencies

### 3. Download dataset
Download from Kaggle and place all 9 CSV files in dataraw/archive/

### 4. Run pipeline step by step

### 5. Run automated pipeline

Runs pipeline once immediately, then daily at 8:00 AM

---

## 📈 Tableau Dashboard

3 interactive KPI visualizations built in Tableau:

| Chart | Type | Insight |
|-------|------|---------|
| Top 10 Categories by Revenue | Horizontal Bar | Health and Beauty leads at R\$1.25M |
| Order Status Distribution | Pie Chart | 97.02% of orders delivered successfully |
| Monthly Orders Trend | Line Chart | 30x growth from 200 to 6,500 orders/month |

---

## 🔍 Key Insights

- 🥇 Health and Beauty is the #1 revenue category at R\$1,258,681
- ✅ 97.02% of all orders are delivered successfully
- ⏰ Orders arrive 11.87 days early on average
- 📈 Order volume grew 30x from Sep 2016 to Sep 2018
- ❌ Only 0.63% of orders are cancelled

---

## 🗺 Pipeline Specification

Full workflow specification document available in docs/Workflow_Spec_Doc_Manjula.docx

Covers:
- ✅ Project objectives and scope
- ✅ Data source documentation
- ✅ Pipeline architecture (7 stages)
- ✅ KPI definitions and targets
- ✅ Technology stack justification
- ✅ 7-day project timeline

---

## 👩‍💼 Author

**Azmeera Manjula**
MBA - Business Analytics | ISBR Business School, Bengaluru
📧 manjulaazmeera2@gmail.com
🐙 https://github.com/AzmeeraManjula

---

## 📄 License

This project uses the Olist Brazilian E-Commerce Dataset
available under CC BY-NC-SA 4.0 license.
'''

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('README with emojis created successfully!')
"

