# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:12:53 2019

@author: jaideep
"""

class mobile:
    mobile_company = "samsung"
    mobile_address = "Korea"
    def accept_mobile_details(self):
        self.mobile_model=input("Enter the mobile model:")
        self.mobile_price=input("Enter the mobile price:")
    def display(self):
        print("MOBILE COMPANY NAME: ",mobile.mobile_company)
        print("MOBILE COMPANY ADDRESS: ",mobile.mobile_address)
        print("*"*50)
        print("MOBILE INFORMATION")
        print("*"*50) 
        print(self.__dict__) #only instance variables are called because dict is given
m1=mobile()
m1.accept_mobile_details()
m1.display()
"""
In m1 object cotains only instance variables 
they are :
    1.mobile model
    2.mobile price
