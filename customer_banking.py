# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter your savings account balance: "))
    savings_interest = float(input("Enter your savings account interest rate(in decimal): "))
    savings_maturity = int(input("Enter the number of months for the savings account: "))

 
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"The interest earned for savings account: ${interest_earned: .2f}")
    print(f"The updated savings accoung balance is: ${updated_savings_balance: .2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    cd_balance = float(input("Enter your CD account balance: "))
    cd_interest = float(input("Enter your CD account interest rate(in decimal): "))
    cd_maturity = int(input("Enter the number of months for the CD account: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"The interest earned for your CD account is : ${cd_interest_earned: .2f}")
    print(f"The updated CD account balance is: ${updated_cd_balance: .2f}")
if __name__ == "__main__":
    # Call the main function.
    main()