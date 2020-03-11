# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:24:51 2019

@author: jaideep
"""
bank_account_numbers=['HDFC5582','HDFC6546','HDFC8745','HDFC7343']
class bank:
    bank_name='HDFC bank'
    bank_address='Ammerpet,hyd'
    bank_website='www.hdfcbank.com'
    bank_IFSC='IND5846'

    def __init__(self):
        self.AC_number=input("Enter account number:")
        self.AC_holder_name=input("Enter account holder name:")
        self.AC_holder_moibile=input("Enter account holder mobile number:")
    def display(self):
        print("BANK NAME:",bank.bank_name)
        print("BANK ADDRESS:",bank.bank_address)
        print("BANK IFSC:",bank.bank_IFSC)
        print("BANK WEBSITE",bank.bank_website)
        print(self.__dict__)
    def account_amount_details(self):
        if self.AC_number in bank_account_numbers:
            self.total_amount=float(input("Enter the total amount:"))
            print("total balance:",self.total_amount)
            self.SGST=self.total_amount*(2/100)
            self.CGST=self.total_amount*(4/100)
            self.available_amount=self.total_amount+self.SGST+self.CGST
            print("Available balance:",self.available_amount)
        else:
            print("Enter valid account number:")

ramu=bank()
ramu.display()
ramu.account_amount_details()

ravi=bank()
ravi.display()
ravi.account_amount_details()
