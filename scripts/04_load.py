import os
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

os.chdir(r'C:\Users\Aaryan\Desktop\Project')

engine = create_engine('sqlite:///data/ecommerce.db')

def load_table(csv_path, table_name):
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Loaded {table_name}: {len(df)} rows")
    return len(df)

print("=" * 50)
print("Starting Final Load")
print("=" * 50)

# Load clean orders
load_table('data/processed/orders_clean.csv', 'orders_clean')

# Load raw files for KPI calculation
print("\nCalculating KPIs...")

order_items = pd.read_csv('data/raw/olist_order_items_dataset.csv')
products    = pd.read_csv('data/raw/olist_products_dataset.csv')
categories  = pd.read_csv('data/raw/product_category_name_translation.csv')

# KPI 1: Category Revenue
merged = order_items.merge(products, on='product_id') \
                    .merge(categories, on='product_category_name')

category_rev = merged.groupby('product_category_name_english')['price'] \
                     .sum().reset_index()
category_rev.columns = ['category', 'total_revenue']
category_rev = category_rev.sort_values('total_revenue', ascending=False)

# Save to database and CSV
category_rev.to_sql('kpi_category_revenue', engine,
                    if_exists='replace', index=False)
category_rev.to_csv('data/processed/kpi_category_revenue.csv', index=False)
print(f"KPI 1 saved: Top category = {category_rev.iloc[0]['category']}")
print(f"             Revenue = R$ {category_rev.iloc[0]['total_revenue']:,.2f}")

# KPI 2: Order Status Distribution
orders = pd.read_csv('data/processed/orders_clean.csv')
status_dist = orders.groupby('order_status').agg(
    count=('order_id', 'count')
).reset_index()
status_dist['percentage'] = (
    status_dist['count'] / status_dist['count'].sum() * 100
).round(2)
status_dist = status_dist.sort_values('count', ascending=False)

status_dist.to_sql('kpi_order_status', engine,
                   if_exists='replace', index=False)
status_dist.to_csv('data/processed/kpi_order_status.csv', index=False)
print(f"\nKPI 2 saved: Order status breakdown")
print(status_dist.to_string(index=False))

# KPI 3: Monthly Orders Trend
orders['order_purchase_timestamp'] = pd.to_datetime(
    orders['order_purchase_timestamp']
)
orders['month'] = orders['order_purchase_timestamp'].dt.to_period('M').dt.to_timestamp()
monthly = orders.groupby('month').agg(
    order_count=('order_id', 'count')
).reset_index()
monthly = monthly.sort_values('month')

monthly.to_sql('kpi_monthly_orders', engine,
               if_exists='replace', index=False)
monthly.to_csv('data/processed/kpi_monthly_orders.csv', index=False)
print(f"\nKPI 3 saved: Monthly orders trend ({len(monthly)} months)")

print("\n" + "=" * 50)
print("Load complete! Database ready for Tableau.")
print("=" * 50)
print("\nFiles saved in data/processed/:")
print("  - orders_clean.csv")
print("  - kpi_category_revenue.csv")
print("  - kpi_order_status.csv")
print("  - kpi_monthly_orders.csv")