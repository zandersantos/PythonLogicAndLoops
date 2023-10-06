"""
Description: Applies an interest dependant on their balance
Author: Zander Santos
Date: October 2, 2023
Usage: Applies interest to multiple customers accounts based on their current balance to help them grow wealth over time
"""

#Imports
import pprint
import csv

#Dict
account_balances = {}

#Opens the account_balances text file and adds the contents into the account_balances dict
#In a given line/row, all content before the | character is added to the key
#While all content in a row after the | character is added to the values
#All unecessary characters, "\n" are removed/"stripped"
with open('account_balances.txt','r') as file:
    for row in file:
        key, value = row.strip().split('|')
        account_balances [key] = float(value)
    
pprint.pprint(account_balances)

#applies interest to all balances based on amount
interest = 0.0
for key, value in account_balances.items():
    
    #all balances less then 1000 and more or equal to 0 gets an interest rate of 1.0%
    if value < 1000 and value >= 0:                 
        interest = 0.01
        value = value + ((value * interest)/12.0)
        account_balances[key] = value
        
    #all balances less then 5000 and more or equal to 1000 gets an interest rate of 2.5%
    elif value < 5000 and value >= 1000:            
        interest = 0.025
        value = value + ((value * interest)/12.0)
        account_balances[key] = value
                
    #all balances more then 5000 gets an interest rate of 5%
    elif value >= 5000:                             
        interest = 0.05
        value = value + ((value * interest)/12)
        account_balances[key] = value

    #all balances less then 0 gets an charged interest rate of 10.0%              
    elif value < 0:                                 
        interest = 0.1
        value = value - ((value * interest)/12)     
        account_balances[key] = value
     
pprint.pprint(account_balances)

#csv headings
fieldnames = ['Account', 'Balance']

#the csv with the name based on the current date has the headings added
#the dictionary contents in account_balances are added
with open("2023-10-02-ZS","w", newline='') as file:
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    
    for account, balance in account_balances.items():
        writer.writerow({'Account': account, 'Balance': balance})
        
#the contents of the csv are displayed in the console
with open('2023-10-02-ZS', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Account'], row['Balance'])
    
    
    