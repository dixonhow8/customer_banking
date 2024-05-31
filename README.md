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
The create_savings_account function is defined in savings_account.py:

from account import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.
    
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        float: The interest earned.
    """
    savings_account = Account(balance, 0)
    interest_earned = savings_account.get_balance() * (interest_rate / 100) * (months / 12)
    future_balance = savings_account.get_balance() + interest_earned
    savings_account.set_balance(future_balance)
    savings_account.set_interest(interest_earned)
    return future_balance, interest_earned

## CD Account
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
    cd_account = Account(balance, 0)
    cd_interest_earned = cd_account.get_balance() * (interest_rate / 100) * (months / 12)
    future_cd_balance = cd_account.get_balance() + cd_interest_earned
    cd_account.set_balance(future_cd_balance)
    cd_account.set_interest(cd_interest_earned)
    return future_cd_balance, cd_interest_earned

## Main Script
The main.py script interacts with the user to get the required inputs and display the results:

from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    """This function prompts the user to enter the savings and CD account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    savings_balance = float(input("Enter your savings account balance: "))
    savings_interest = float(input("Enter your savings account interest rate(in decimal): "))
    savings_maturity = int(input("Enter the number of months for the savings account: "))

    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    print(f"The interest earned for savings account: ${interest_earned: .2f}")
    print(f"The updated savings account balance is: ${updated_savings_balance: .2f}")

    cd_balance = float(input("Enter your CD account balance: "))
    cd_interest = float(input("Enter your CD account interest rate(in decimal): "))
    cd_maturity = int(input("Enter the number of months for the CD account: "))

    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    print(f"The interest earned for your CD account is: ${cd_interest_earned: .2f}")
    print(f"The updated CD account balance is: ${updated_cd_balance: .2f}")

if __name__ == "__main__":
    main()

## How to Run
1. Ensure all the Python files (account.py, savings_account.py, cd_account.py, main.py) are in the same directory.
2. Run the main.py script:

python main.py

3. Follow the prompts to enter the necessary information for the savings and CD accounts.
4. The script will display the interest earned and the updated balances for both accounts.

## Example Usage

Enter your savings account balance: 1000
Enter your savings account interest rate(in decimal): 5
Enter the number of months for the savings account: 12
The interest earned for savings account: $ 50.00
The updated savings account balance is: $ 1050.00
Enter your CD account balance: 2000
Enter your CD account interest rate(in decimal): 3
Enter the number of months for the CD account: 6
The interest earned for your CD account is: $ 30.00
The updated CD account balance is: $ 2030.00

