# content of test_add.py
def add(x: int, y: 2):
    return x + y


# content of test_subtract.py
def subtract(x: int, y: int):
    return x - y


# content of test_multiply.py
def multiply(x: int, y: int):
    return x * y


# content of test_divide.py
def divide(x: int, y: int):
    return x / y


class InsufficientFunds(Exception):
    pass

# Person bank account class
class BankAccount():
    # define a (constructor):
    # to reference account balance starting value(0)
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    # deposite money into bank account
    def deposit(self, amount):
        # add(x, += deposit_amount(x))
	    # deposit amount value of (x)
        self.balance += amount

    # withdraw: subtract money from bank account
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds in account")
        # subtract (x, -= withdraw_amount)
        # withdraw amount value of (x) amount
        self.balance -= amount

    # collect interest accrue per year
    def collect_interest(self):
        # take 1% interest rate(1.1%) by default
	    # multiply(balance by interest_rate 1.1%)
        self.balance *= 1.1

# # content of test_floor-division.py
# def divide(x: int, y: int):
#     return x // y


