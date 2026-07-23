from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg
import os
import pandas as pd

os.chdir(r'C:\Users\Aaryan\Desktop\Project')

print("=" * 50)
print("Starting PySpark")
print("=" * 50)

spark = SparkSession.builder \
    .appName("PySpark Transformation") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

try:
    input_file = "data/processed/orders_clean.csv"
    print("Reading:", input_file)

    df = spark.read.csv(
        input_file,
        header=True,
        inferSchema=True
    )

    print(f"Total rows: {df.count()}")
    df.printSchema()

    # Transformation: group by order status
    status_summary = df.groupBy("order_status") \
        .agg(
            count("order_id").alias("order_count"),
            avg("delivery_delay_days").alias("avg_delay")
        ) \
        .orderBy("order_count", ascending=False)

    print("\nOrder Status Summary:")
    status_summary.show()

    # Save using pandas to avoid Hadoop error
    output_path = "data/processed/spark_status_summary"
    os.makedirs(output_path, exist_ok=True)

    status_summary.toPandas().to_csv(
        f"{output_path}/summary.csv",
        index=False
    )

    print("Saved to:", output_path)
    print("PySpark transformation complete!")

except Exception as e:
    print(f"Error: {e}")

finally:
    spark.stop()
    print("Spark stopped.")