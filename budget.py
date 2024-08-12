from enum import Enum
from datetime import datetime

class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

    def get_name(self):
        return self.name.capitalize()
    
class CategoryType(Enum):
    EXPENSE = 1
    INCOME = 2

# Create a monthly budget
class Budget:
    def __init__(self, user_date: datetime = datetime.now()):
        self.month = Month(int(user_date.strftime("%m")))
        self.year = int(user_date.strftime("%Y"))
        print(f'{self.month}')
        

# Create budget categories
class Category:
    def __init__(self, name: str, type: CategoryType):
        self.main_name = name
        self.type = type
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
