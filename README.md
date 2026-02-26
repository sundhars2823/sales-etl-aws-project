🚀 Cloud-Based Sales ETL Pipeline

An end-to-end ETL pipeline built using Python, PostgreSQL, and AWS S3 to transform raw retail sales data into a structured Data Warehouse using Star Schema modeling.

🏗 Architecture

S3 (Raw Data Layer)
↓
Python ETL (Transformation Layer)
↓
PostgreSQL (Star Schema Data Warehouse)

⚙️ Tech Stack

Python (Pandas, Psycopg2, Boto3)

PostgreSQL

AWS S3

SQL

Git

📊 Data Modeling

Dimension Tables

dim_customer

dim_product

Fact Table

fact_sales

Concepts Used

Surrogate Keys

Foreign Key Constraints

Referential Integrity

Indexing for Performance Optimization

🔄 ETL Features

Data ingestion from AWS S3

Data cleaning and transformation

Column normalization

Datetime conversion handling

Encoding issue resolution

Duplicate prevention using UNIQUE constraints

Logging and structured error handling

📈 Sample Analytical Queries
Total Sales by Segment
SELECT dc.segment,
       ROUND(SUM(fs.sales), 2) AS total_sales
FROM fact_sales fs
JOIN dim_customer dc
ON fs.customer_key = dc.customer_key
GROUP BY dc.segment
ORDER BY total_sales DESC;
Top 5 Products by Profit
SELECT dp.product_name,
       ROUND(SUM(fs.profit), 2) AS total_profit
FROM fact_sales fs
JOIN dim_product dp
ON fs.product_key = dp.product_key
GROUP BY dp.product_name
ORDER BY total_profit DESC
LIMIT 5;
🛠 How to Run

Configure AWS credentials

Create PostgreSQL database

Run schema.sql

Run:

python scripts/etl.py
🎯 Learning Outcomes

Built an end-to-end ETL pipeline

Designed Star Schema warehouse

Integrated AWS S3

Optimized SQL queries

👨‍💻 Author

Sundhar
Aspiring Data Engineer
