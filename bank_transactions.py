"""
Description:
Author: Zander Santos
Date: October 2, 2023
Usage:
"""
# import section
import random

transaction_options = ["D", "W", "Q"]
user_balance = float(random.randint(-1000,10000))

print(user_balance)

interface_break = "*" * 40

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