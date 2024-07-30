import snowflake.connector
import pandas as pd

# Database connection details
def get_connection():
    conn = snowflake.connector.connect(
        user='ajaykamble4241',
        password='Mira@123',
        account='mmskenx-jt39546',
        warehouse='COMPUTE_WH',
        database='OMS_DATABASE',
        schema='OMS_SCHEMA'
    )
    return conn

# Fetch functions
def fetch_customers():
    conn = get_connection()
    query = "SELECT customer_id, name, email FROM CUSTOMER"
    customers = pd.read_sql(query, conn)
    conn.close()
    
    print(customers.head())  # Debug: Print the first few rows of the DataFrame
    print(customers.columns)  # Debug: Print the column names of the DataFrame
    
    return customers


def fetch_products():
    conn = get_connection()
    query = "SELECT product_id, product_name, price FROM PRODUCT"
    products = pd.read_sql(query, conn)
    conn.close()
    return products

# Add similar functions for fetching orders and order items
def fetch_orders():
    conn = get_connection()
    query = "SELECT order_id, customer_id, order_date, status FROM ORDERS"
    orders = pd.read_sql(query, conn)
    conn.close()
    return orders

def fetch_order_items():
    conn = get_connection()
    query = "SELECT item_id, order_id, product_name, quantity, price FROM ORDERITEM"
    order_items = pd.read_sql(query, conn)
    conn.close()
    return order_items


# CRUD operations
def create_order_db(order_id, customer_id, order_date, status):
    conn = get_connection()
    query = f"INSERT INTO ORDERS (order_id, customer_id, order_date, status) VALUES ('{order_id}', '{customer_id}', '{order_date}', '{status}')"
    conn.cursor().execute(query)
    conn.close()

def update_order_db(order_id, customer_id, order_date, status):
    conn = get_connection()
    query = f"UPDATE ORDERS SET customer_id='{customer_id}', order_date='{order_date}', status='{status}' WHERE order_id='{order_id}'"
    conn.cursor().execute(query)
    conn.close()

def delete_order_db(order_id):
    conn = get_connection()
    query = f"DELETE FROM ORDERS WHERE order_id='{order_id}'"
    conn.cursor().execute(query)
    conn.close()

def add_product_db(product_id, product_name, price):
    conn = get_connection()
    query = f"INSERT INTO PRODUCT (product_id, product_name, price) VALUES ('{product_id}', '{product_name}', {price})"
    conn.cursor().execute(query)
    conn.close()

def update_product_db(product_id, product_name, price):
    conn = get_connection()
    query = f"UPDATE PRODUCT SET product_name='{product_name}', price={price} WHERE product_id='{product_id}'"
    conn.cursor().execute(query)
    conn.close()

def delete_product_db(product_id):
    conn = get_connection()
    query = f"DELETE FROM PRODUCT WHERE product_id='{product_id}'"
    conn.cursor().execute(query)
    conn.close()

# db_utils.py

def fetch_order_report():
    conn = get_connection()
    query = "SELECT * FROM orders_report_fact"
    order_report = pd.read_sql(query, conn)
    conn.close()
    return order_report

def fetch_product_report():
    conn = get_connection()
    query = "SELECT * FROM products_report_fact"
    product_report = pd.read_sql(query, conn)
    conn.close()
    return product_report
