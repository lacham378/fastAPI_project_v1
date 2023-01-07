import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds

# assigned a fixture variable:
# run fixture function first before any other
# to call this function(zero_bank_account)
@pytest.fixture
def zero_bank_account():
  print("creating zero_bank_account")
  return BankAccount()


@pytest.fixture
def bank_account():
  return BankAccount(50)

# parametrize the bank account 
# (def test_add(x, y, result))
@pytest.mark.parametrize("x, y, result", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)

])
def test_add(x, y, result):
  print('testing functionality')
  # sum == x+y==result
  assert add(x, y) == result

# define a fuction test_subtract
def test_subtract():
  print('testing functionality')
  assert subtract(9, 4) == 5
  

# define a fuction test_multiply
def test_multiply():
  print('testing functionality')
  assert multiply(4, 3) == 12
  
  
# define a fuction test_divide
def test_divide():
  print('testing functionality')
  assert divide(20, 5) == 4


# define a new bank account(x)
def test_bank_set_initial_amount(bank_account):
    #bank_account = BankAccount(50)
    print("testing my bank account")
    assert bank_account.balance == 50
    
    
def test_bank_default_amount(zero_bank_account):
    # bank_account = BankAccount()
    print("testing my bank balance")
    assert zero_bank_account.balance == 0


def test_withdraw(bank_account):
    # bank_account = BankAccount(50)
    bank_account.withdraw(20)
    print("testing my bank withdraw")
    assert bank_account.balance == 30


def test_deposit(bank_account):
    # bank_account = BankAccount(50)
    bank_account.deposit(30)
    print("testing my bank deposit")
    assert bank_account.balance == 80


def test_collect_interest(bank_account):
    # bank_account = BankAccount(50)
    bank_account.collect_interest()
    print("testing my bank interest")
    assert round(bank_account.balance, 6) == 55
    
    
@pytest.mark.parametrize("deposited, withdraw, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
])
def test_bank_transaction(zero_bank_account, deposited, withdraw, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected
    

def test_insufficient_funds(bank_account):
  with pytest.raises(InsufficientFunds):
    bank_account.withdraw(200)
  
  