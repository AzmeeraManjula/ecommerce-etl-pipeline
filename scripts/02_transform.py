import os
import pandas as pd
from sqlalchemy import create_engine

# Set working directory
os.chdir(r'C:\Users\Aaryan\Desktop\Project')

# Create processed folder if not exists
os.makedirs('data/processed', exist_ok=True)

# YOUR actual CSV path
CSV_PATH = 'data/raw/'

# Load orders
orders = pd.read_csv(f'{CSV_PATH}olist_orders_dataset.csv')

# --- CLEANING STEPS ---
print("Before cleaning:", orders.shape)

# 1. Convert date columns to datetime
date_cols = [
    'order_purchase_timestamp',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors='coerce')

# 2. Drop rows where purchase date is missing
orders = orders.dropna(subset=['order_purchase_timestamp'])

# 3. Remove duplicates
orders = orders.drop_duplicates(subset='order_id')

# 4. Create derived column: delivery delay in days
orders['delivery_delay_days'] = (
    orders['order_delivered_customer_date'] -
    orders['order_estimated_delivery_date']
).dt.days

# 5. Data quality report
print("After cleaning:", orders.shape)
print("\nNulls remaining:\n", orders.isnull().sum())
print("\nDelay stats:\n", orders['delivery_delay_days'].describe())

# Save clean file
orders.to_csv('data/processed/orders_clean.csv', index=False)
print("\nSaved: data/processed/orders_clean.csv")

# Also load all 9 files into SQLite
print("\nNow loading all files into SQLite database...")
engine = create_engine('sqlite:///data/ecommerce.db')

tables = {
    'orders'     : 'olist_orders_dataset.csv',
    'customers'  : 'olist_customers_dataset.csv',
    'order_items': 'olist_order_items_dataset.csv',
    'products'   : 'olist_products_dataset.csv',
    'sellers'    : 'olist_sellers_dataset.csv',
    'payments'   : 'olist_order_payments_dataset.csv',
    'reviews'    : 'olist_order_reviews_dataset.csv',
    'categories' : 'product_category_name_translation.csv'
}

for table_name, filename in tables.items():
    df = pd.read_csv(f'{CSV_PATH}{filename}')
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Loaded {table_name}: {len(df)} rows")

print("\nAll done! Database created at data/ecommerce.db")
