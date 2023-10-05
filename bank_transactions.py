"""
Description:
Author: Zander Santos
Date: October 2, 2023
Usage:
"""
# import section
import random
import os
from time import sleep

transaction_options = ["D", "W", "Q"]
user_balance = float(random.randint(-1000,10000))

interface_break = "*" * 40
user_input = ""

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

    user_input = (input("Enter your selection: "))
    
    if not user_input in transaction_options:
        print("INVALID SELECTION".center(40," "))
        print(interface_break)
        
    elif user_input == "D":
        enter_transaction = (float(input("Enter amount of transaction:")))
        user_balance = user_balance + enter_transaction
        
        print(interface_break)
        print(f"Your current balance is: ${user_balance:,.2f}".center(40, " "))
        print(interface_break)

    elif user_input == "W":
        enter_transaction = (float(input("Enter amount of transaction:")))
        if enter_transaction > user_balance:
            print("INSUFFICIENT FUNDS".center(40," "))
        else:
            user_balance = user_balance - enter_transaction
            print(f"Your current balance is: ${user_balance:,.2f}".center(40, " "))

    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

