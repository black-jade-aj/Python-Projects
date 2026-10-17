import sqlite3
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

query = """
SELECT orders.order_id,
customers.first_name,
customers.last_name,
orders.product_name,
orders.category,
orders.quantity,
orders.unit_price
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id"""

df = pd.read_sql_query(query, conn)

df["total_price"] = df["quantity"] * df["unit_price"]

print("---ALL ORDERS WITH CUSTOMER DETAILS---")
print(df)

print("\n---TOTAL REVENUE BY CATEGORY---")
category_summary = df.groupby("category")["total_price"].sum().reset_index()
print(category_summary)

conn.close()
