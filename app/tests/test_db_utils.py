import pytest
from db_utils import fetch_customers, fetch_products

def test_fetch_customers():
    df = fetch_customers()
    assert not df.empty

def test_fetch_products():
    df = fetch_products()
    assert not df.empty
