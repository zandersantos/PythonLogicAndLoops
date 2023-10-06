"""
Description:
Author: Zander Santos
Date: October 2, 2023
Usage:
"""

import pprint

account_balances = {}


with open("account_balances.txt","r") as file:
    for row in file:
        key, value = row.strip().split('|')
        account_balances [key] = float(value)
        
pprint.pprint(account_balances)
