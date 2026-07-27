import os
import sqlite3

os.chdir(r'C:\Users\Aaryan\Desktop\Project')

print("=" * 55)
print("FINAL PROJECT CHECKLIST")
print("=" * 55)

# 1. Check all scripts exist
print("\n1. SCRIPTS")
scripts = [
    'scripts/02_transform.py',
    'scripts/03_pyspark_transform.py',
    'scripts/04_load.py',
    'scripts/05_automate.py'
]
for s in scripts:
    if os.path.exists(s):
        print(f"   PASS - {s}")
    else:
        print(f"   FAIL - {s} NOT FOUND")

# 2. Check ingestion log
print("\n2. INGESTION LOG")
if os.path.exists('ingestion_log.txt'):
    with open('ingestion_log.txt') as f:
        lines = f.readlines()
    print(f"   PASS - ingestion_log.txt exists ({len(lines)} lines)")
else:
    print("   FAIL - ingestion_log.txt NOT FOUND")

# 3. Check processed files
print("\n3. PROCESSED CSV FILES")
processed = [
    'data/processed/orders_clean.csv',
    'data/processed/kpi_category_revenue.csv',
    'data/processed/kpi_order_status.csv',
    'data/processed/kpi_monthly_orders.csv'
]
for f in processed:
    if os.path.exists(f):
        size = os.path.getsize(f)
        print(f"   PASS - {f} ({size/1024:.1f} KB)")
    else:
        print(f"   FAIL - {f} NOT FOUND")

# 4. Check SQLite database
print("\n4. SQLITE DATABASE")
if os.path.exists('data/ecommerce.db'):
    conn = sqlite3.connect('data/ecommerce.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    conn.close()
    print(f"   PASS - ecommerce.db exists with {len(tables)} tables:")
    for t in tables:
        print(f"          - {t[0]}")
else:
    print("   FAIL - ecommerce.db NOT FOUND")

# 5. Check PySpark output
print("\n5. PYSPARK OUTPUT")
spark_path = 'data/processed/spark_status_summary'
if os.path.exists(spark_path):
    files = os.listdir(spark_path)
    print(f"   PASS - spark_status_summary exists ({len(files)} files)")
else:
    print("   FAIL - spark_status_summary NOT FOUND")

# 6. Check docs folder
print("\n6. DOCUMENTATION")
if os.path.exists('docs/Workflow_Spec_Doc_Manjula.docx'):
    print("   PASS - Workflow_Spec_Doc_Manjula.docx exists")
else:
    print("   FAIL - Workflow spec doc NOT FOUND")

# 7. Check GitHub
print("\n7. GITHUB")
print("   CHECK MANUALLY - github.com/AzmeeraManjula/ecommerce-etl-pipeline")

# 8. Check Tableau
print("\n8. TABLEAU DASHBOARD")
if os.path.exists('ecommerce_dashboard.twb') or os.path.exists('ecommerce_dashboard.twbx'):
    print("   PASS - Tableau dashboard file exists")
else:
    print("   FAIL - Tableau dashboard file NOT FOUND")

print("\n" + "=" * 55)
print("CHECKLIST COMPLETE")
print("=" * 55)