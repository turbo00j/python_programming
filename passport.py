# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:49:57 2019

@author: jaideep
"""

passport_number = input("Enter the pass port numbers:")
customer_passport = input("Enter your pass port number:")
if customer_passport in passport_number:
    print("Passport number is valid")
    visa_number = input("Enter the VISA numbers:")
    passenger_visa = input("Enter your VISA number:")  
    if passenger_visa in visa_number:
        print ("VISA is valid")
        print("$"*30)
        print("H@ppy j0urney")
        print("$"*30)
    else:
        print("Dear passenger, Enter valid VISA number")
else:
    print("Dear passenger, Enter valid passport number")