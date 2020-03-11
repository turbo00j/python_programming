# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:52:57 2019

@author: jaideep
"""
111010

class product:
    def __init__(self,pno,pname,pcompany,pprice):
        self.product_id=pno
        self.product_name=pname
        self.product_company=pcompany
        self.product_price=pprice
    def Display_product_info(self):
        print('*'*30)
        print(self.__dict__)
        print('*'*30)
p1=product(input("Enter product ID:"),input("Enter product name:"),input("Enter product company:"),float(input("Enter product price:")))
p1.Display_product_info()
