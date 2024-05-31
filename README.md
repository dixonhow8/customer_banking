# Customer Banking System

## Overview
This Customer Banking System is a simple application that allows users to calculate and track interest earned on savings and CD (Certificate of Deposit) accounts. By running this application, users can input their account information, view the interest earned, and see the updated balances after a specified number of months.

## File Structure
- **Account.py:** Contains the base class `Account` which serves as the parent class for `SavingsAccount` and `CDAccount`.
- **customer_banking.py:** The main script of the application where users can interact with the system.
- **savings_account.py:** Contains the `SavingsAccount` class for handling savings account operations.
- **cd_account.py:** Contains the `CDAccount` class for handling CD account operations.

## Features
- **Savings Account:** Users can input their savings account details including initial balance, interest rate, and duration.
- **CD Account:** Users can input their CD account details including initial balance, interest rate, duration, and maturity date.
- **Interest Calculation:** The application calculates and displays the interest earned on both savings and CD accounts.
- **Updated Balances:** Users can view the updated balances after a specified number of months.
- **User-friendly Interface:** The application provides a simple and intuitive interface for users to interact with.

## Usage
1. **Clone Repository:** Clone this repository to your local machine.
2. **Navigate to Directory:** Open a terminal and navigate to the directory where you cloned the repository.
3. **Run the Application:** Run the main script of the application (`customer_banking.py`).
4. **Input Account Details:** Follow the prompts to input your savings and CD account details.
5. **View Results:** Once the details are entered, the application will calculate the interest earned and display the updated balances.

## Dependencies
- Python 3.x

## Customer_Banking.py (Main Script)

```python
from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    savings_balance = float(input("Enter your savings account balance: "))
    savings_interest = float(input("Enter your savings account interest rate (in decimal): "))
    savings_maturity = int(input("Enter the number of months for the savings account: "))

    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    print(f"The interest earned for savings account: ${interest_earned:.2f}")
    print(f"The updated savings account balance is: ${updated_savings_balance:.2f}")

    cd_balance = float(input("Enter your CD account balance: "))
    cd_interest = float(input("Enter your CD account interest rate (in decimal): "))
    cd_maturity = int(input("Enter the number of months for the CD account: "))

    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    print(f"The interest earned for your CD account is: ${cd_interest_earned:.2f}")
    print(f"The updated CD account balance is: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()

## Sample Output
Enter your savings account balance: 1000
Enter your savings account interest rate (in decimal): 0.05
Enter the number of months for the savings account: 12
The interest earned for savings account: $0.50
The updated savings account balance is: $1000.50
Enter your CD account balance: 20000
Enter your CD account interest rate (in decimal): 0.50
Enter the number of months for the CD account: 15
The interest earned for your CD account is: $125.00
The updated CD account balance is: $20125.00
