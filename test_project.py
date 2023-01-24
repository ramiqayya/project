import pytest
from project import stock_name, multiply, sum_num


def test_stock_name():
    assert stock_name('tsla') == 'Tesla Inc'


def test_multiply():
    assert multiply(2, 5) == 10


def test_sum_num():
    assert sum_num(2, 5) == 7
