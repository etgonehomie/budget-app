import pytest
# https://testdriven.io/blog/pytest-for-beginners/

from enum import Enum


def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

class CategoryType(Enum):
    EXPENSE = 1
    INCOME = 2

# Create budget categories
class Category:
    def __init__(self, name):
        self.main_name = name
    # main_name: str
    # budget_year: date
    # budget_month: date
    # subcategories: [Sub-category]
    # type: CategoryType

class SubCategory(Category):
    def __init__(self, name):
        self.sub_name = name
    # sub_name: str
    # amount_planned: float
    # amount_remaining: float
    # amount_spent: float
    # transactions: [Transaction]
    # is_favorite: bool
    # notes: str

class Transaction:
    def __init__(self, name):
        self.name = name
    # purchase_date: date
    # amount: float
    # name: str
    # notes: str
    # category: SubCategory
