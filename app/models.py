from db_utils import get_connection, create_order_db, update_order_db, delete_order_db, add_product_db, update_product_db, delete_product_db

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def create(self):
        query = f"INSERT INTO CUSTOMER (customer_id, name, email) VALUES ('{self.customer_id}', '{self.name}', '{self.email}')"
        conn = get_connection()
        conn.cursor().execute(query)
        conn.close()

    def update(self):
        query = f"UPDATE CUSTOMER SET name='{self.name}', email='{self.email}' WHERE customer_id='{self.customer_id}'"
        conn = get_connection()
        conn.cursor().execute(query)
        conn.close()

    def delete(self):
        query = f"DELETE FROM CUSTOMER WHERE customer_id='{self.customer_id}'"
        conn = get_connection()
        conn.cursor().execute(query)
        conn.close()


class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def create(self):
        add_product_db(self.product_id, self.product_name, self.price)

    def update(self):
        update_product_db(self.product_id, self.product_name, self.price)

    def delete(self):
        delete_product_db(self.product_id)

class Order:
    def __init__(self, order_id, customer_id, order_date, status):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.status = status

    def create(self):
        query = f"INSERT INTO ORDERS (order_id, customer_id, order_date, status) VALUES ('{self.order_id}', '{self.customer_id}', '{self.order_date}', '{self.status}')"
        conn = get_connection()
        conn.cursor().execute(query)
        conn.close()

class OrderItem:
    def __init__(self, item_id, order_id, product_name, quantity, price):
        self.item_id = item_id
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

    def create(self):
        query = f"INSERT INTO ORDERITEM (item_id, order_id, product_name, quantity, price) VALUES ('{self.item_id}', '{self.order_id}', '{self.product_name}', '{self.quantity}', '{self.price}')"
        conn = get_connection()
        conn.cursor().execute(query)
        conn.close()


# Wrapper functions to be used in main.py
def create_order(order_id, customer_id, order_date, status):
    create_order_db(order_id, customer_id, order_date, status)

def update_order(order_id, customer_id, order_date, status):
    update_order_db(order_id, customer_id, order_date, status)

def delete_order(order_id):
    delete_order_db(order_id)

def add_product(product_id, product_name, price):
    add_product_db(product_id, product_name, price)

def update_product(product_id, product_name, price):
    update_product_db(product_id, product_name, price)

def delete_product(product_id):
    delete_product_db(product_id)
