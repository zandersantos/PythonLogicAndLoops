"""
Description: Simulate an ATM for deposits and withdraw transactions
Author: Zander Santos
Date: October 2, 2023
Usage: Allows users to deposit and withdraw amounts to their total balance
"""
# import section
import random
import os
from time import sleep

# Initiating the core parts: options and user balance
transaction_options = ["D", "W", "Q"]
user_balance = float(random.randint(-1000,10000))

# Set interface
interface_break = "*" * 40
user_input = ""

# loop the interface until the user inputs a Q
while not user_input == "Q":
    # print the beginning interface
    print(interface_break)
    print("PIXEL RIVER FINANCIAL".center(40," "))
    print("ATM Simulator".center(40," "))
    print(f"Your current balance is: ${user_balance:,.2f}".center(40," "))
    print(" ")
    print("Deposit: D".center(40," "))
    print("Withdraw: W".center(40," "))
    print("To Quit: Q".center(40," "))
    print(interface_break)

    # asks the user for their selection
    user_input = (input("Enter your selection: "))
    
    # if the users input is not a part of the options
    if not user_input in transaction_options:
        print("INVALID SELECTION".center(40," "))
        print(interface_break)
        
    # if the users input is D
    elif user_input == "D":
        enter_transaction = (float(input("Enter amount of transaction:")))
        user_balance = user_balance + enter_transaction                             # add transaction to balance
        
        print(interface_break)
        print(f"Your current balance is: ${user_balance:,.2f}".center(40, " "))
        print(interface_break)

    # if the user input is W
    elif user_input == "W":
        enter_transaction = (float(input("Enter amount of transaction:")))
        
        # compare transaction with balance to see if it is greater or not
        if enter_transaction > user_balance:            
            print("INSUFFICIENT FUNDS".center(40," "))
        else:
            user_balance = user_balance - enter_transaction
            print(f"Your current balance is: ${user_balance:,.2f}".center(40, " "))

    # after all prompts are finished, wait for 3 seconds and then clear terminal
    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

