# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:04:57 2019

@author: jaideep
"""

Bank_account =int(input("Enter the bank account number :"))
Account_balance = float(input("Enter the account balance of your account :"))
Amount_withdrawal = float(input("Enter the withdrawal amount of your account:"))
if Amount_withdrawal > Account_balance:
    print ("Insufficient funds PLEASE maintain sufficient balance")
else:
    Account_balance = Account_balance-Amount_withdrawal
    print ("your account balance is :", Account_balance)
    
print("**************************************")    
print("THANKS FOR USING OUR BANKING SERVICES")
print("***************************************")

