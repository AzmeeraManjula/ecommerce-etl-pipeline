import pandas as pd

orders = pd.read_csv(
    r"C:\Users\Aaryan\Desktop\Project\data/raw/\olist_orders_dataset.csv"
)

print("Shape:", orders.shape)
print("\nColumns:")
print(orders.columns.tolist())
print("\nData Types:")
print(orders.dtypes)
print("\nFirst 3 Rows:")
print(orders.head(3))
print("\nMissing Values:")
print(orders.isnull().sum())

import os
import pandas as pd

folder = r"C:\Users\Aaryan\Desktop\Project\data/raw/"

files = [
    "olist_orders_dataset.csv",
    "olist_customers_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "product_category_name_translation.csv"
]

for file in files:
    path = os.path.join(folder, file)

    print(f"\n{'='*60}")
    print(f"File: {file}")
    print('='*60)

    df = pd.read_csv(path)

    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())

import pandas as pd
import os
from datetime import datetime

RAW_PATH = r"C:\Users\Aaryan\Desktop\Project\data/raw/"

LOG_FILE = "ingestion_log.txt"

def log(msg):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

    print(msg)


def ingest_file(filename):
    path = os.path.join(RAW_PATH, filename)

    df = pd.read_csv(path)

    log(f"Loaded {filename} — {df.shape[0]} rows, {df.shape[1]} cols")

    return df


orders = ingest_file("olist_orders_dataset.csv")
customers = ingest_file("olist_customers_dataset.csv")
order_items = ingest_file("olist_order_items_dataset.csv")
products = ingest_file("olist_products_dataset.csv")
sellers = ingest_file("olist_sellers_dataset.csv")
payments = ingest_file("olist_order_payments_dataset.csv")
reviews = ingest_file("olist_order_reviews_dataset.csv")
geolocation = ingest_file("olist_geolocation_dataset.csv")
categories = ingest_file("product_category_name_translation.csv")

log("------ Ingestion Complete ------")
log(f"Total Orders : {len(orders)}")
log(f"Total Customers : {len(customers)}")

import pandas as pd
import os
from sqlalchemy import create_engine

RAW_PATH = r"C:\Users\Aaryan\Desktop\Project\data/raw/"

engine = create_engine("sqlite:///ecommerce.db")

tables = {
    "orders": "olist_orders_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "categories": "product_category_name_translation.csv",
}

for table_name, filename in tables.items():
    path = os.path.join(RAW_PATH, filename)

    df = pd.read_csv(path)

    df.to_sql(table_name, engine, if_exists="replace", index=False)

    print(f"Loaded {table_name}: {len(df)} rows")

    import os
print("DATABASE LOCATION:", os.path.abspath("ecommerce.db"))

