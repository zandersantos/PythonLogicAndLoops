"""
Description:
Author: Zander Santos
Date: October 2, 2023
Usage:
"""

import pprint
import csv


account_balances = {}


with open('account_balances.txt','r') as file:
    for row in file:
        key, value = row.strip().split('|')
        account_balances [key] = float(value)
    
        
pprint.pprint(account_balances)

interest = 0.0
for key, value in account_balances.items():
    if value < 1000 and value >= 0:
        interest = 0.01
        value = value + ((value * interest)/12.0)
        account_balances[key] = value
        
    elif value < 5000 and value >= 1000:
        interest = 0.025
        value = value + ((value * interest)/12.0)
        account_balances[key] = value

                
    elif value >= 5000:
        interest = 0.05
        value = value + ((value * interest)/12)
        account_balances[key] = value

                
    elif value < 0:
        interest = 0.1
        value = value - ((value * interest)/12)
        account_balances[key] = value

     
pprint.pprint(account_balances)

fieldnames = ['Account', 'Balance']

with open("2023-10-02-ZS","w", newline='') as file:
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    
    for account, balance in account_balances.items():
        writer.writerow({'Account': account, 'Balance': balance})
        
with open('2023-10-02-ZS', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Account'], row['Balance'])
    
    
    