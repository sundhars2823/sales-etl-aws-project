import boto3
import os
import pandas as pd

# ---------- S3 CONFIG ----------
bucket_name = "sales-etl-2026-sundhar"
file_key = "sales.csv"

# ---------- DOWNLOAD FROM S3 ----------
s3 = boto3.client("s3")

download_path = "temp_sales.csv"
s3.download_file(bucket_name, file_key, download_path)

print("File downloaded from S3 ✅")

# ---------- LOAD DATA ----------
df = pd.read_csv(download_path, encoding="latin1")

# Clean columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce").dt.date

print("Data loaded from S3 successfully ✅")

import os

db_password = os.getenv("DB_PASSWORD")