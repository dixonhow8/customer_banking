# Customer Banking

This project provides functionality to calculate interest earned and update the balances for savings and certificate of deposit (CD) accounts. It includes two main functions: `create_savings_account` and `create_cd_account`, which are imported and used in the main script.

## Prerequisites

- Python 3.x

## Files

- `account.py`: Contains the `Account` class with methods to set and get the balance and interest.
- `savings_account.py`: Contains the `create_savings_account` function.
- `cd_account.py`: Contains the `create_cd_account` function.
- `main.py`: Main script to interact with the user, calculate interest, and display updated balances.

## Account Class

The `Account` class is defined in `account.py`:

```python
class Account:
    """Creating an Account class with methods."""
    
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        """Sets the balance for the account."""
        self.balance = balance

    def set_interest(self, interest):
        """Sets the interest gained for the account."""
        self.interest = interest

    def get_balance(self):
        """Gets the balance of the account."""
        return self.balance

    def get_interest(self):
        """Gets the interest of the account."""
        return self.interest

## Savings Account

The `create_savings_account` function, defined in `savings_account.py`, creates a savings account, calculates interest earned, and updates the account balance.

### Function Definition

```python
from account import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.
    
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The annual interest rate (APR) for the savings account.
        months (int): The number of months to calculate interest for.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        float: The interest earned.
    """
    # Create a new savings account instance
    savings_account = Account(balance, 0)
    
    # Calculate interest earned
    interest_earned = savings_account.get_balance() * (interest_rate / 100) * (months / 12)
    
    # Update account balance and interest
    future_balance = savings_account.get_balance() + interest_earned
    savings_account.set_balance(future_balance)
    savings_account.set_interest(interest_earned)
    
    return future_balance, interest_earned

##  **CD Account**
The create_cd_account function is defined in cd_account.py:

from account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        float: The interest earned.
    """
    # Function implementation

Main Script
The main.py script (customer_banking) interacts with the user to get the required inputs and display the results:

## **How to Run**

1. Ensure all the Python files (`account.py`, `savings_account.py`, `cd_account.py`, `main.py`) are in the same directory.

2. Run the `customer_banking.py` script:

    ```
    python customer_banking.py
    ```

3. Follow the prompts to enter the necessary information for the savings and CD accounts.

4. The script will display the interest earned and the updated balances for both accounts.

