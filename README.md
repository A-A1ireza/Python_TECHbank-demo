# Python_TECHbank-demo
# TECH_Bank

A simple bank management system built using Python. It allows users to create bank accounts, deposit, withdraw, check balances, transfer money, and edit account information. The data is stored in a CSV file (`data.csv`), making it persistent between runs.

## Features

- **Create Account**: Users can create new accounts and receive a unique account number.
- **View Balance**: Users can view their current account balance.
- **Deposit Funds**: Users can deposit money into their account.
- **Withdraw Funds**: Users can withdraw money from their account (with balance checks).
- **Edit Account Information**: Users can update their name, phone number, and email address.
- **Transfer Money**: Users can transfer money to other accounts (balance check before transfer).
- **Save and Exit**: Saves all account data to a CSV file before quitting.

## Requirements

- Python 3.6+
- No external libraries required (standard Python libraries used).


## File Structure

main.py: Main script where the bank operations are handled.

validation.py: Contains all the validation functions for user input (e.g., name validation, phone number validation).

data.csv: Stores account data (user details and balances). This file is automatically created and updated as users interact with the program.



## Usage
Main Menu Options

When you run the program, you'll be presented with a menu of options:

1. Create an Account (1 or C)

Allows the user to create a new bank account.

2. View Bank Account Balance (2 or V)

Displays the current balance of the user's account.

3. Deposit to Your Bank Account (3 or D)

Deposits money into the user's bank account.

4. Withdrawal from Your Bank Account (4 or W)

Withdraws money from the user's bank account (only if the balance is sufficient).

5. Edit Your Account Information (5 or E)

Allows the user to update their name, phone number, or email address.

6. Transfer to Another Account (6 or T)

Transfers money from the user's account to another account.

7. Save and Quit (7 or Q or S)

Saves all changes to the data.csv file and exits the program.



## Sample Usage
Options: 

1. Create an account => [1 or C]
2. View bank account balance => [2 or V]
3. Deposit to your bank account => [3 or D]
4. Withdrawal from your bank account => [4 or W]
5. Edit your account information => [5 or E]
6. Transfer to another account => [6 or T]
7. Save and Quit => [7 or Q or S]

Please select an option: 1



## Data Storage

The user data (including name, email, phone number, and balance) is saved in a CSV file (data.csv). Each row represents an individual account.

The CSV format is as follows:

account_number,first_name,last_name,email,phone_number,balance
123456,John,Doe,johndoe@email.com,555-5555,1000


