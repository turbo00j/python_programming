# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:31:22 2019

@author: jaideep
"""

class product:
    def __init__(self):
        self.product_id=int(input("Enter product ID:"))
        self.product_name=input("Enter product name:")
        self.product_company=input("Enter product company :")
        self.product_price=float(input("Enter product price:"))
    def Display_product_info(self):
        print('*'*30)
        print(self.__dict__)
        print('*'*30)
p1=product()
p1.Display_product_info()
