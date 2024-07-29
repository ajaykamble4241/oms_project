import pytest
from utils import calculate_order_total

def test_calculate_order_total():
    total = calculate_order_total('1')
    assert total == 150.0  # Example value, replace with actual expected value
