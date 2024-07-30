import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
from db_utils import fetch_customers, fetch_products, fetch_orders, fetch_order_items, fetch_product_report, fetch_order_report
from models import create_order, update_order, delete_order, add_product, update_product, delete_product, Customer, Order, OrderItem


# Streamlit app code
st.title('Order Management System')
st.markdown(
    """
    <style>
    #GithubIcon {
        visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# CRUD operations
menu = st.sidebar.selectbox("Menu", ["Customer Management", "Product Management", "Order Management", "Order Report", "Product Report"])

if menu == "Customer Management":
    # Code for Customer CRUD operations
    st.subheader("Manage Customers")
    action = st.selectbox("Action", ["Add Customer", "Update Customer", "Delete Customer"])

    if action == "Add Customer":
        with st.form("add_customer"):
            customer_id = st.text_input("Customer ID")
            name = st.text_input("Name")
            email = st.text_input("Email")
            submit_button = st.form_submit_button(label="Add Customer")

        if submit_button:
            new_customer = Customer(customer_id, name, email)
            new_customer.create()
            st.success(f"Customer {name} added successfully!")

    elif action == "Update Customer":
        with st.form("update_customer"):
            customer_id = st.text_input("Customer ID")
            name = st.text_input("New Name")
            email = st.text_input("New Email")
            submit_button = st.form_submit_button(label="Update Customer")

        if submit_button:
            updated_customer = Customer(customer_id, name, email)
            updated_customer.update()
            st.success(f"Customer {customer_id} updated successfully!")

    elif action == "Delete Customer":
        with st.form("delete_customer"):
            customer_id = st.text_input("Customer ID")
            submit_button = st.form_submit_button(label="Delete Customer")

        if submit_button:
            Customer(customer_id, None, None).delete()
            st.success(f"Customer {customer_id} deleted successfully!")

elif menu == "Product Management":
    # Code for Product CRUD operations
    st.subheader("Manage Products")
    action = st.selectbox("Action", ["Add Product", "Update Product", "Delete Product"])

    if action == "Add Product":
        with st.form("add_product"):
            product_id = st.text_input("Product ID")
            product_name = st.text_input("Product Name")
            price = st.number_input("Price", min_value=0.0, format="%.2f")
            submit_button = st.form_submit_button(label="Add Product")

        if submit_button:
            add_product(product_id, product_name, price)
            st.success(f"Product {product_name} added successfully!")

    elif action == "Update Product":
        with st.form("update_product"):
            product_id = st.text_input("Product ID")
            product_name = st.text_input("New Product Name")
            price = st.number_input("New Price", min_value=0.0, format="%.2f")
            submit_button = st.form_submit_button(label="Update Product")

        if submit_button:
            update_product(product_id, product_name, price)
            st.success(f"Product {product_id} updated successfully!")

    elif action == "Delete Product":
        with st.form("delete_product"):
            product_id = st.text_input("Product ID")
            submit_button = st.form_submit_button(label="Delete Product")

        if submit_button:
            delete_product(product_id)
            st.success(f"Product {product_id} deleted successfully!")


# Order and Product Reports
if menu == "Order Report":
    st.subheader("Order Report")
    order_report = fetch_order_report()
    st.write(order_report)

    st.subheader("Order Graphical Report")
    fig, ax = plt.subplots()
    ax.bar(order_report.iloc[:, 3], order_report.iloc[:, 5])
    st.pyplot(fig)
    
    

elif menu == "Product Report":
    st.subheader("Product Report")
    product_report = fetch_product_report()
    st.write(product_report)

    st.subheader("Product Graphical Report")
    fig, ax = plt.subplots()
    ax.bar(product_report.iloc[:, 1], product_report.iloc[:, 3])
    st.pyplot(fig)
    
    
    
