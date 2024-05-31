# Customer Banking System

## Overview
This Customer Banking System is a simple application that allows users to calculate and track interest earned on savings and CD (Certificate of Deposit) accounts. By running this application, users can input their account information, view the interest earned, and see the updated balances after a specified number of months.

## File Structure
- **account.py:** Contains the base class `Account` which serves as the parent class for `SavingsAccount` and `CDAccount`.
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

## Example
