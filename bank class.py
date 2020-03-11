# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:57:48 2019

@author: jaideep
"""

class bank:
    Bank_name = input("Enter the name of your bank :")
    Bank_address = input("Enter the address of your bank :")
    Bank_IFSC = input("Enter the IFSC code of your bank :")
    Bank_website= input("Enter the website of the bank :")
def display():
    print("BANK NAME :",bank.Bank_name,"\nBANK ADDRESS :",bank.Bank_address,"\nBANK IFSC CODE :",bank.Bank_IFSC,"\nBANK WEBSITE :",bank.Bank_website)
    fixed_deposit = float(input("Enter the fixed deposit amount of your account"))
    intrest = fixed_deposit*(12/100)
    print ("Intrest for the fixed deposit is :",intrest)
    fixed_deposit = fixed_deposit+intrest
    print("Total account balance in your fixed deposit is :",fixed_deposit)
display()

    