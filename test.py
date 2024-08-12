import pytest
from datetime import datetime
from category import Category, CategoryType, SubCategory, Budget, Month

@pytest.fixture
def budget():
    return Budget()

@pytest.fixture
def now():
    return datetime.now()

@pytest.fixture
def income():
    """Fixture to provide a Dog instance for testing."""
    return Category(name='Eric PGE', type=CategoryType.INCOME)

# def test_initialization(income):
#     assert income.main_name == "Eric PGE"
#     assert income.type == CategoryType.INCOME

def test_initialization(budget, now):
    current_month = int(now.strftime("%m"))
    current_year = int(now.strftime("%Y"))
    assert budget.year == current_year
    assert budget.month == Month(current_month)
