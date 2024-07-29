import pytest
from models import Customer, Product

def test_customer_creation():
    customer = Customer('1', 'John Doe', 'john@example.com')
    assert customer.name == 'John Doe'

def test_product_creation():
    product = Product('1', 'Product A', 100.0)
    assert product.price == 100.0
