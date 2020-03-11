# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:27:40 2019

@author: jaideep
"""

class product:
    def product_info(self):
        self.product_ID = input("Enter product ID :")
        self.product_name = input("Enter the product name :")
        self.product_company= input("Enter the product company:")
        self.product_price = input("Enter the product price:")
    def display(self):
        print(self.product_ID)
        print(self.product_name)
        print(self.product_company)
        print(self.product_price)
e1 = product()
e1.product_info()
print ("*"*50)
e1.display()
print ("*"*50)
e2 = product()
e2.product_info()
print ("*"*50)
e2.display()

    